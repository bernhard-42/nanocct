# nanocct — one entry point for building it yourself, on macOS, Linux and Windows.
#
#   make deps        fetch and build RapidJSON, FreeType, FreeImage and OCCT from scratch (long: OCCT is ~4 min on an M5)
#   make wheels      generate -> compile -> stubs -> wheel -> delocate -> test -> shim  (nanocct's wheel and the shim's, into dist/)
#   make generate compile stubs wheel delocate test     the same, step by step -- every step runs once: the wheel is packed
#                    from what compile and stubs built, and the tests run against the repaired wheel in a fresh venv
#
# Design.md 3.1/3.2 describe what the dependencies are and why; State.md 9 holds the working state.
#
# PLATFORMS
#   macOS    builds natively with Apple clang, driven through `uv`.
#   Linux    goes through the manylinux_2_28 container only (deps/run-manylinux.sh), so there is one Linux
#            environment and it is the one CI uses. Nothing here builds against the host's toolchain.
#   Windows  runs under Git Bash and reaches MSVC by importing vcvars64 in a generated .bat — never PowerShell.
#            Start it from a real session: launched over ssh, cl.exe fails sporadically with 0xC0000142.
#
# Every step orchestrates its own parallelism (ninja -j, NANOCCT_JOBS = one worker per core), so the targets
# themselves are serial.
.NOTPARALLEL:
.DEFAULT_GOAL := wheels

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Set the root working folder and test dependencies
#
# Every clean target builds its paths from ROOT, so an empty or wrong ROOT would aim `rm -rf` at the filesystem
# root. Refuse to run instead of trusting the expansion -- including when ROOT is overridden on the command line.
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

ROOT    := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

ifeq ($(strip $(ROOT)),)
  $(error ROOT is empty -- refusing to run: the clean targets would expand to /)
endif
ifeq ($(strip $(ROOT)),/)
  $(error ROOT is the filesystem root -- refusing to run)
endif
ifeq ($(wildcard $(ROOT)/Makefile),)
  $(error ROOT=$(ROOT) does not contain this Makefile -- refusing to run)
endif
ifeq ($(wildcard $(ROOT)/generator/__main__.py),)
  $(error ROOT=$(ROOT) is not the nanocct tree -- refusing to run)
endif

DEPS    := $(ROOT)/deps
UNAME_S := $(shell uname -s)

ifeq ($(UNAME_S),Darwin)
  PLATFORM := macos
else ifeq ($(UNAME_S),Linux)
  PLATFORM := linux
else ifneq (,$(filter MINGW% MSYS% CYGWIN%,$(UNAME_S)))
  PLATFORM := windows
else ifeq ($(UNAME_S),)
  # `uname` produced nothing: almost certainly cmd.exe or PowerShell. Everything here is POSIX -- uname, cygpath,
  # shell recipes -- and the Windows build reaches MSVC by importing vcvars64 from a generated .bat, which is a
  # Git Bash idiom. Run it from Git Bash (State.md 9, and the user does not read PowerShell).
  $(error run this from Git Bash -- `uname` is not available, so this looks like cmd.exe or PowerShell)
else
  $(error unsupported platform '$(UNAME_S)')
endif


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Toolkits
#
# The 45 toolkits in scope, hand-sorted in dependency order (Design.md 2). The order is not cosmetic: instantiation
# ownership follows it, and a toolkit that aliases another's instantiation must be imported after it. Update the
# list when OCCT adds a toolkit -- an audit of TOOLKITS.cmake against the manifest is what once found TKDECascade
# missing (State.md 8.15).
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

TOOLKITS := TKernel TKMath TKG2d TKG3d TKGeomBase TKBRep TKGeomAlgo TKTopAlgo TKPrim TKShHealing TKBO TKBool \
            TKHLR TKHelix TKMesh TKFillet TKOffset TKFeat TKXMesh TKService TKV3d TKOpenGl TKMeshVS TKCDF \
            TKLCAF TKCAF TKVCAF TKBinL TKBin TKXmlL TKXml TKDE TKXSBase TKXCAF TKDEIGES TKDESTEP TKDESTL \
            TKRWMesh TKDEGLTF TKDEOBJ TKDEPLY TKDEVRML TKBinXCAF TKXmlXCAF TKDECascade
TK_FLAGS := --toolkit $(TOOLKITS)


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Build variables
#
# The development interpreter, pinned so the three machines are the same one. It is NOT the wheel's floor: that
# is `requires-python = ">=3.12"` and `wheel.py-api = "cp312"`, which say what a *user* can install. Until
# 2026-09-24 nothing pinned this and the three had drifted apart -- macOS 3.14.7, Linux 3.12.13, Windows 3.12.12 --
# so the suite ran on a different Python depending on which box you were on. Exercising the 3.12 floor is a job
# for the CI matrix (State.md 8.17), not for whichever interpreter a machine happens to pick.
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

PY_VERSION := 3.14
CPTAG      := cp$(subst .,,$(PY_VERSION))

# Per-platform plumbing. CONTAINER runs a command inside the manylinux image with the repository at /work.
CONTAINER  := $(DEPS)/run-manylinux.sh
ML_PY      := /work/.venv-ml/bin/python
ML_SYSPY   := /opt/python/$(CPTAG)-$(CPTAG)/bin/python
# the wheel's platform tag follows the host, as the container image does (deps/run-manylinux.sh): x86_64 or aarch64
ML_PLAT    := manylinux_2_28_$(shell uname -m)
WIN_PY     := $(ROOT)/.venv/Scripts/python.exe
# `make test` installs the repaired wheel here, a venv of its own (Linux: /work/.venv-test-ml in the container)
TEST_VENV  := $(ROOT)/.venv-test
# RUN_SH starts a bash script. Empty on macOS and Linux, where the #! line does it. On Windows it is Git Bash by its full
# path: native GNU make (Chocolatey's, "Built for Windows32") turns `#!/bin/bash` into `bash <script>` and calls
# CreateProcess without a path (make 4.4.1, src/w32/subproc/sub_proc.c), and CreateProcess searches System32 before
# PATH (Microsoft's CreateProcess documentation) -- so wherever WSL is installed, C:\Windows\System32\bash.exe wins.
# The first GitHub Actions run (windows-2025, 2026-09-28) stopped in fetch-rapidjson.sh with "Windows Subsystem for
# Linux has no installed distributions"; gauss never saw it because it has no System32\bash.exe.
ifeq ($(PLATFORM),windows)
  GIT_BASH := $(shell cygpath -m /usr/bin/bash.exe)
  ifeq ($(strip $(GIT_BASH)),)
    $(error cannot locate Git Bash (cygpath -m /usr/bin/bash.exe returned nothing) -- run this from Git Bash)
  endif
  RUN_SH := "$(GIT_BASH)"
else
  RUN_SH :=
endif
PY         := $(ROOT)/.venv/bin/python
ifeq ($(PLATFORM),macos)
  BUILD_DIR := $(ROOT)/build/dev
  STAGE_DIR := $(ROOT)/stage-mac
else ifeq ($(PLATFORM),windows)
  BUILD_DIR := $(ROOT)/build-win
  STAGE_DIR := $(ROOT)/stage-win
else
  BUILD_DIR := $(ROOT)/build-ml
  STAGE_DIR := $(ROOT)/stage-ml
endif

.PHONY: wheels env deps sources occt freetype freeimage rapidjson generate compile stubs wheel delocate test shim shim-parity nanocctbuild \
        clean_occt clean_freetype clean_rapidjson clean_deps clean_gen clean_dist help


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Help
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

help:
	@echo "targets: env | deps (sources rapidjson freetype freeimage occt) | generate compile stubs wheel delocate test | shim | wheels | shim-parity | nanocctbuild"
	@echo "         clean_deps clean_occt clean_freetype clean_freeimage clean_rapidjson clean_gen clean_dist"
	@echo "platform: $(PLATFORM)"


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Create the build environment
#
# The venv every other target uses, on PY_VERSION. Building on 3.14 still produces a cp312-abi3 wheel, because
# Py_LIMITED_API=0x030C0000 makes the extension loadable on 3.12 and everything after whatever built it
# (measured 2026-09-24) -- so pinning the development interpreter forward costs no compatibility.
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

env:
ifeq ($(PLATFORM),linux)
	@# uv here too, against the same pyproject dev group as the other platforms. The hand-written pip list this
	@# replaces had drifted: it was missing libclang, so `make generate` died with "No module named 'clang'"
	@# the first time a Linux tree was built by `make env` (2026-09-24). UV_PROJECT_ENVIRONMENT points uv at
	@# .venv-ml instead of .venv, and `uv venv --clear` replaces an existing environment -- `python -m venv` does not,
	@# which is why pinning the interpreter looked like a no-op until this was measured. --clear because uv 0.12
	@# no longer replaces one by itself ("A virtual environment already exists", 2026-09-28, uv 0.12.16 here and
	@# 0.12.18 in the manylinux image; both have -c/--clear).
	$(CONTAINER) "cd /work && UV_PROJECT_ENVIRONMENT=/work/.venv-ml uv venv --clear -p $(ML_SYSPY) /work/.venv-ml \
	    && UV_PROJECT_ENVIRONMENT=/work/.venv-ml uv sync --no-install-project"
else
	cd $(ROOT) && uv venv --clear -p $(PY_VERSION)
	@# --no-install-project: `uv sync` would build nanocct itself, which needs generated sources that do not exist
	@# yet on a fresh clone. The venv here carries the tooling (libclang, nanobind, pytest, mypy, ty); the extension
	@# modules come from `make compile`, and are imported from the staged tree rather than installed.
	cd $(ROOT) && uv sync --no-install-project
endif


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Clean dependencies
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# ---- dependencies ---------------------------------------------------------------------------------------------
# `make deps` builds them in the order OCCT needs: FreeType and RapidJSON first, then OCCT against both.

clean_occt:
	rm -rf $(DEPS)/occt-build $(DEPS)/occt-8.0.1 $(DEPS)/occt-build.log
ifeq ($(PLATFORM),linux)
	rm -rf $(DEPS)/occt-build-ml $(DEPS)/occt-8.0.1-manylinux
endif

clean_freetype:
	rm -rf $(DEPS)/freetype-build $(DEPS)/freetype
ifeq ($(PLATFORM),linux)
	rm -rf $(DEPS)/freetype-build-ml $(DEPS)/freetype-ml
endif

clean_freeimage:
	rm -rf $(DEPS)/freeimage-build $(DEPS)/freeimage
	rm -rf $(DEPS)/freeimage-build-ml $(DEPS)/freeimage-ml

clean_rapidjson:
	rm -rf $(DEPS)/rapidjson $(DEPS)/rapidjson-src $(DEPS)/rapidjson-1.1.0.tar.gz

clean_deps: clean_occt clean_freetype clean_freeimage clean_rapidjson


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Build dependencies
#
# deps/occt-src, deps/freetype-src and deps/freeimage-src are the *sources* and are deliberately not cleaned:
# fetching OCCT again is a long download, and re-cloning the other two is pointless --
# neither tree is patched (since 2026-09-25): symbols are kept in at link time and by -fvisibility=hidden.
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


rapidjson: clean_rapidjson
	$(RUN_SH) $(DEPS)/fetch-rapidjson.sh

# The upstream sources, cloned at a pinned tag if they are not there yet (both scripts are idempotent, so the
# clean_* targets above may delete the builds without touching the checkouts -- a clone of OCCT is 144 MB).
sources:
	$(RUN_SH) $(DEPS)/fetch-occt-src.sh
	$(RUN_SH) $(DEPS)/fetch-freetype-src.sh
	$(RUN_SH) $(DEPS)/fetch-freeimage-src.sh

freetype: clean_freetype
	$(RUN_SH) $(DEPS)/fetch-freetype-src.sh
ifeq ($(PLATFORM),macos)
	$(RUN_SH) $(DEPS)/build-freetype-macos.sh
else ifeq ($(PLATFORM),windows)
	$(RUN_SH) $(DEPS)/build-freetype-windows.sh
else
	$(RUN_SH) $(DEPS)/build-freetype-manylinux.sh
endif

freeimage: clean_freeimage
	$(RUN_SH) $(DEPS)/fetch-freeimage-src.sh
ifeq ($(PLATFORM),macos)
	$(RUN_SH) $(DEPS)/build-freeimage-macos.sh
else ifeq ($(PLATFORM),windows)
	$(RUN_SH) $(DEPS)/build-freeimage-windows.sh
else
	$(RUN_SH) $(DEPS)/build-freeimage-manylinux.sh
endif

occt: clean_occt
	@test -d $(DEPS)/rapidjson || { echo "run 'make rapidjson' first"; exit 1; }
	$(RUN_SH) $(DEPS)/fetch-occt-src.sh
ifeq ($(PLATFORM),macos)
	@test -d $(DEPS)/freetype || { echo "run 'make freetype' first"; exit 1; }
	@test -d $(DEPS)/freeimage || { echo "run 'make freeimage' first"; exit 1; }
	$(RUN_SH) $(DEPS)/build-occt-macos.sh
else ifeq ($(PLATFORM),windows)
	@test -d $(DEPS)/freetype || { echo "run 'make freetype' first"; exit 1; }
	@test -d $(DEPS)/freeimage || { echo "run 'make freeimage' first"; exit 1; }
	$(RUN_SH) $(DEPS)/build-occt-windows.sh
else
	@# On the host, not through $(CONTAINER): the script starts its own container (as build-freetype-manylinux.sh
	@# does). Run through run-manylinux.sh it would be docker inside docker -- "docker: command not found",
	@# which is what `make occt` did on Linux until 2026-09-24, when a build from a bare tree first reached it.
	$(RUN_SH) $(DEPS)/build-occt-manylinux.sh
endif

deps: clean_deps rapidjson freetype freeimage occt


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Generate the OCCT bindings
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# Only the generated files. src/cpp/common/nanocct_common.h and nanocct_ncollection.h are hand-written and tracked,
# as are src/nanocct/_templates.py and py.typed -- never `rm -rf src/cpp`, which once cost a whole Windows build.
clean_gen:
	rm -rf $(ROOT)/src/cpp/TK*
	rm -f  $(ROOT)/src/cpp/manifest.json $(ROOT)/src/cpp/toolkits.cmake $(ROOT)/src/cpp/common/ncollection_docs.h
	find $(ROOT)/src/nanocct -mindepth 1 \( -name '_templates.py' -o -name 'py.typed' \) -prune -o -print0 \
	    | xargs -0 rm -rf
	@# The staged tree holds a copy of what was just removed, and the .pth keeps it importable -- without this,
	@# `import nanocct` would go on working after a clean and quietly serve the previous build.
	rm -rf $(STAGE_DIR)
	rm -f $(wildcard $(ROOT)/.venv/lib/python3.*/site-packages/_nanocct_dev.pth)


# $(PY), never `uv run`: uv syncs the project before running, which builds nanocct -- and that needs the generated
# sources this step is about to produce. On a fresh clone it fails on the missing src/cpp/toolkits.cmake.
generate: clean_gen
ifeq ($(PLATFORM),macos)
	cd $(ROOT) && $(PY) -m generator $(TK_FLAGS)
else ifeq ($(PLATFORM),windows)
	cd $(ROOT) && "$(WIN_PY)" -m generator $(TK_FLAGS)
else
	$(CONTAINER) "$(ML_PY) -m generator --occt /work/deps/occt-8.0.1-manylinux --occt-src /work/deps/occt-src $(TK_FLAGS)"
endif


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Compile the OCCT bindings
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# cmake + ninja directly rather than `uv sync`, so the build reports progress ([12/45] Building CXX object ...)
# instead of sitting behind a spinner for a minute and a half, and so the three platforms have the same shape:
# build into a directory, stage it, and let stubs/test import the staged tree through PYTHONPATH. Installing into
# the venv belongs to the wheel path, not to the development loop.
compile:
ifeq ($(PLATFORM),macos)
	@# The deployment target the wheel is tagged with (MACOS_TARGET): the wheel is packed from these very modules. Without
	@# it they target the SDK's own version (26.0 here), which only the scikit-build-core build had overridden
	@# (pyproject.toml), and delocate refuses the wheel: "has a minimum target of 26.0" (2026-09-28).
	cd $(ROOT) && cmake -S . -B $(BUILD_DIR) -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_OSX_DEPLOYMENT_TARGET=$(MACOS_TARGET) \
	    -DPython_EXECUTABLE=$(ROOT)/.venv/bin/python -DNANOCCT_RAPIDJSON_DIR=$(DEPS)/rapidjson/include
	cd $(ROOT) && cmake --build $(BUILD_DIR)
	$(RUN_SH) $(DEPS)/stage.sh $(BUILD_DIR) $(STAGE_DIR)
	@# Exactly one copy of the extension modules may be in a process: nanobind registers its types per domain, and
	@# a wheel-installed nanocct next to the staged one aborts the import with "Critical nanobind error".
	cd $(ROOT) && uv pip uninstall -q nanocct 2>/dev/null || true
else ifeq ($(PLATFORM),windows)
	cd $(ROOT) && $(RUN_SH) ./deps/build-nanocct-windows.sh
	$(RUN_SH) $(DEPS)/stage.sh $(BUILD_DIR) $(STAGE_DIR)
else
	$(CONTAINER) "cmake -S /work -B /work/build-ml -G Ninja -DCMAKE_BUILD_TYPE=Release \
	    -DPython_EXECUTABLE=$(ML_PY) -DNANOCCT_OCCT_DIR=/work/deps/occt-8.0.1-manylinux \
	    -DNANOCCT_RAPIDJSON_DIR=/work/deps/rapidjson/include"
	$(CONTAINER) "ninja -k 0 -C /work/build-ml"
	$(CONTAINER) "/work/deps/stage.sh build-ml stage-ml"
endif


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Build stubs
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

stubs:
ifeq ($(PLATFORM),macos)
	cd $(ROOT) && $(PY) -m generator.stubs
	$(RUN_SH) $(DEPS)/stage.sh $(BUILD_DIR) $(STAGE_DIR)          # the stubs are part of the staged tree
else ifeq ($(PLATFORM),windows)
	cd $(ROOT) && PYTHONPATH="$(STAGE_DIR)" "$(WIN_PY)" -m generator.stubs
	$(RUN_SH) $(DEPS)/stage.sh $(BUILD_DIR) $(STAGE_DIR)
else
	$(CONTAINER) "cd /work && PYTHONPATH=/work/stage-ml $(ML_PY) -m generator.stubs"
	$(CONTAINER) "/work/deps/stage.sh build-ml stage-ml"
endif


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Execute test
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

test:
	@# The suite runs against what ships: the repaired wheel from `make delocate`, installed into a venv of its own with
	@# the dev tools (pytest, mypy, ty, libclang for the generator tests) -- not against the staged tree, and not in .venv,
	@# where the staged tree's .pth would put a second copy of the modules into the process (the one-copy rule).
	@wheels=$$(ls $(DIST_DIR)/nanocct-*.whl 2>/dev/null); \
	if [ $$(echo $$wheels | wc -w) -ne 1 ]; then echo "test: need exactly one repaired wheel in $(DIST_DIR) -- run make wheel delocate" >&2; exit 1; fi
ifeq ($(PLATFORM),macos)
	cd $(ROOT) && uv venv -q --clear -p $(PY_VERSION) $(TEST_VENV) \
	    && uv pip install -q --python $(TEST_VENV)/bin/python --group dev $(DIST_DIR)/nanocct-*.whl
	cd $(ROOT) && $(TEST_VENV)/bin/python -m pytest tests -q -p no:cacheprovider
else ifeq ($(PLATFORM),windows)
	cd $(ROOT) && uv venv -q --clear -p $(PY_VERSION) $(TEST_VENV) \
	    && uv pip install -q --python "$(TEST_VENV)/Scripts/python.exe" --group dev $(DIST_DIR)/nanocct-*.whl
	cd $(ROOT) && "$(TEST_VENV)/Scripts/python.exe" -m pytest tests -q -p no:cacheprovider
else
	$(CONTAINER) "cd /work && uv venv -q --clear -p $(ML_SYSPY) /work/.venv-test-ml \
	    && uv pip install -q --python /work/.venv-test-ml/bin/python --group dev /work/dist/nanocct-*.whl \
	    && xvfb-run -a /work/.venv-test-ml/bin/python -m pytest tests -q -p no:cacheprovider"
endif


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Clean distribution files
#
# cadquery-ocp-novtk 8.0.1.0.0+shim: `import OCP.*` on top of nanocct (shim/). A pure-Python py3-none-any wheel built by
# shim/build_wheel.py with the standard library only, so one build serves every platform. Into dist/, next to nanocct's.
# Generation reads nanocct's own signatures, so the staged tree must be importable -- found the way `make stubs` finds it.
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

shim:
ifeq ($(PLATFORM),macos)
	$(PY) $(ROOT)/shim/build_wheel.py $(DIST_DIR)
else ifeq ($(PLATFORM),windows)
	cd $(ROOT) && PYTHONPATH="$(STAGE_DIR)" "$(WIN_PY)" shim/build_wheel.py $(DIST_DIR)
else
	$(CONTAINER) "cd /work && PYTHONPATH=/work/stage-ml $(ML_PY) shim/build_wheel.py /work/dist"
endif


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Packaging - create wheels
#
# `make wheel` packs the staged tree -- the modules `make compile` built and the stubs `make stubs` wrote -- with
# generator/wheel.py (stdlib only). Until 2026-09-28 it ran `uv build`, i.e. scikit-build-core, which cannot pack without
# compiling, so every binding was compiled twice; on the slower CI runners that second compile was the longest step
# (Windows: more than 30 min). scikit-build-core stays the build backend for building from source (pip install .).
#
# A packed wheel is not portable: the extension modules find the OCCT libraries through an rpath into deps/, so the
# wheel works only on the machine that built it. The repair step copies those libraries in and rewrites the
# references to point inside the wheel (State.md 8.4). Each platform has its own tool, and each leaves the
# system's own libraries alone -- OpenGL and X11 belong to the host, never to the wheel (Design.md 7).
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# CI runs exactly these targets: .github/workflows/build-wheels.yml (State.md 8.17).

DIST_DIR := $(ROOT)/dist
RAW_DIR  := $(DIST_DIR)/unrepaired

# The tag has to match what OCCT was built against (deps/build-occt-macos.sh sets 11.1). Without this the wheel is
# tagged macosx_11_0 and delocate warns that it will not in fact run on 11.0.
MACOS_TARGET := 11.1
OCCT_BIN_WIN := $(DEPS)/occt-8.0.1/win64/vc14/bin
FREEIMAGE_BIN_WIN := $(DEPS)/freeimage/bin

# The unrepaired wheel, packed from the staged tree: correct Python surface, but linked against deps/. The platform tag
# is the one each repair tool expects: macosx_11_0_<arch> (MACOS_TARGET 11.1 normalises to 11_0), linux_<arch> (auditwheel
# makes it manylinux_2_28_<arch>), win_amd64.
wheel: clean_dist
ifeq ($(PLATFORM),macos)
	cd $(ROOT) && $(PY) -m generator.wheel $(STAGE_DIR) $(RAW_DIR) macosx_11_0_$(shell uname -m)
else ifeq ($(PLATFORM),windows)
	cd $(ROOT) && "$(WIN_PY)" -m generator.wheel "$(STAGE_DIR)" "$(RAW_DIR)" win_amd64
else
	$(CONTAINER) "cd /work && $(ML_PY) -m generator.wheel /work/stage-ml /work/dist/unrepaired linux_$(shell uname -m)"
endif


# The repair. Named `delocate` after the macOS tool because that is what the step is, on every platform. It takes the
# raw wheel `make wheel` left in dist/unrepaired and depends on no other target, so each step runs once.
delocate:
	@ls $(RAW_DIR)/nanocct-*.whl > /dev/null 2>&1 || { echo "delocate: no raw wheel in $(RAW_DIR) -- run make wheel first" >&2; exit 1; }
ifeq ($(PLATFORM),macos)
	MACOSX_DEPLOYMENT_TARGET=$(MACOS_TARGET) $(ROOT)/.venv/bin/delocate-wheel -w $(DIST_DIR) $(RAW_DIR)/*.whl
else ifeq ($(PLATFORM),windows)
	@# delvewheel cannot read a DLL search path from the binary the way rpath gives it on Unix, so it is told --
	@# both directories, ';'-separated (delvewheel repair --help): FreeImage.dll lives in its own install, not in OCCT's.
	cd $(ROOT) && "$(WIN_PY)" -m delvewheel repair --add-path "$(OCCT_BIN_WIN);$(FREEIMAGE_BIN_WIN)" -w $(DIST_DIR) $(RAW_DIR)/*.whl
else
	@# LD_LIBRARY_PATH for the same reason: the OCCT .so files name each other by SONAME and carry no RUNPATH.
	$(CONTAINER) "LD_LIBRARY_PATH=/work/deps/occt-8.0.1-manylinux/lib auditwheel repair \
	    --plat $(ML_PLAT) -w /work/dist /work/dist/unrepaired/*.whl"
endif
	@echo "repaired wheel:" && ls -lh $(DIST_DIR)/*.whl


wheels: generate compile stubs wheel delocate test shim


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Clean distribution files
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

clean_dist:
	rm -rf $(DIST_DIR)


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Parity tests
#
# build123d's and ocp-tessellate's own suites through the shim against the real OCP, test by test (shim/parity.py;
# State.md 8.18). Opt-in and not part of `wheels`: two venvs and the suites side by side, ~6 min on the M5. Needs the
# wheels of `make wheels` in DIST_DIR, a build123d checkout (BUILD123D), which it only reads (`git archive HEAD`), and
# the ocp_tessellate sdist nanocctbuild/nanocctbuild.sh fetches into build/nanocctbuild/sdist; everything else goes to
# build/shim-parity. Host-only for now: on Linux the wheels live in the container's world (State.md 8.17).
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


BUILD123D ?= $(HOME)/Development/CAD/build123d
shim-parity:
ifeq ($(PLATFORM),macos)
	$(PY) $(ROOT)/shim/parity.py --build123d $(BUILD123D) --dist $(DIST_DIR) --work $(ROOT)/build/shim-parity --python $(PY_VERSION)
else
	@echo "shim-parity runs on macOS only so far (see shim/parity.py)"; exit 1
endif


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Create nanocct-enabled packages
#
# build123d 0.13.0, ocpsvg 0.7.0, ocp_gordon 0.3.1 and ocp_tessellate 3.5.3 as sdists from PyPI (sha256-verified),
# patched to import nanocct instead of OCP (nanocctbuild/patches, tracked). Output: build/nanocctbuild/src/<pkg>-<version>,
# ready for `uv pip install dist/nanocct-*.whl build/nanocctbuild/src/*` into a fresh venv. Pure source work, so it runs
# on the host on every platform.
# Then a complete test environment in _scratch/.venv (Python 3.14, untracked): recreated on every run, with the nanocct
# wheel from DIST_DIR (`make wheel delocate` first -- the wheel is what gets tested, not the staged tree) and the four patched
# packages. Activation lasts one shell, so it shares the line with the install.
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

SCRATCH := $(ROOT)/_scratch
ifeq ($(PLATFORM),windows)
  SCRATCH_ACTIVATE := $(SCRATCH)/.venv/Scripts/activate
else
  SCRATCH_ACTIVATE := $(SCRATCH)/.venv/bin/activate
endif
nanocctbuild:
	$(RUN_SH) $(ROOT)/nanocctbuild/nanocctbuild.sh
	@wheels=$$(ls $(DIST_DIR)/nanocct-*.whl 2>/dev/null); \
	if [ -z "$$wheels" ]; then echo "nanocctbuild: no nanocct wheel in $(DIST_DIR) -- run 'make wheel delocate' first" >&2; exit 1; fi; \
	if [ $$(echo $$wheels | wc -w) -ne 1 ]; then echo "nanocctbuild: more than one nanocct wheel in $(DIST_DIR): $$wheels" >&2; exit 1; fi
	mkdir -p $(SCRATCH)
	rm -rf $(SCRATCH)/.venv
	uv venv -p 3.14 $(SCRATCH)/.venv
	@# shell globs, not make's wildcard function: make expands the whole recipe before its first line has created build/nanocctbuild/src
	. $(SCRATCH_ACTIVATE) && uv pip install $(DIST_DIR)/nanocct-*.whl $(ROOT)/build/nanocctbuild/src/*
	@echo "nanocctbuild: test environment ready -- source $(SCRATCH_ACTIVATE)"
