# OCP3x — one entry point for building it yourself, on macOS, Linux and Windows.
#
#   make deps        fetch and build RapidJSON, FreeType, FreeImage and OCCT from scratch (long: OCCT is ~4 min on an M5)
#   make wheels      generate -> compile -> stubs -> test -> wheel -> shim  (OCP3x's wheel and the shim's, into dist/)
#   make generate compile stubs test        the development loop, step by step
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
# Every step orchestrates its own parallelism (ninja -j, OCP3X_JOBS = one worker per core), so the targets
# themselves are serial.
.NOTPARALLEL:
.DEFAULT_GOAL := wheels

ROOT    := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

# Every clean target builds its paths from ROOT, so an empty or wrong ROOT would aim `rm -rf` at the filesystem
# root. Refuse to run instead of trusting the expansion -- including when ROOT is overridden on the command line.
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
  $(error ROOT=$(ROOT) is not the OCP3x tree -- refusing to run)
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

# The 45 toolkits in scope, hand-sorted in dependency order (Design.md 2). The order is not cosmetic: instantiation
# ownership follows it, and a toolkit that aliases another's instantiation must be imported after it. Update the
# list when OCCT adds a toolkit -- an audit of TOOLKITS.cmake against the manifest is what once found TKDECascade
# missing (State.md 8.15).
TOOLKITS := TKernel TKMath TKG2d TKG3d TKGeomBase TKBRep TKGeomAlgo TKTopAlgo TKPrim TKShHealing TKBO TKBool \
            TKHLR TKHelix TKMesh TKFillet TKOffset TKFeat TKXMesh TKService TKV3d TKOpenGl TKMeshVS TKCDF \
            TKLCAF TKCAF TKVCAF TKBinL TKBin TKXmlL TKXml TKDE TKXSBase TKXCAF TKDEIGES TKDESTEP TKDESTL \
            TKRWMesh TKDEGLTF TKDEOBJ TKDEPLY TKDEVRML TKBinXCAF TKXmlXCAF TKDECascade
TK_FLAGS := --toolkit $(TOOLKITS)

# The development interpreter, pinned so the three machines are the same one. It is NOT the wheel's floor: that
# is `requires-python = ">=3.12"` and `wheel.py-api = "cp312"`, which say what a *user* can install. Until
# 2026-09-24 nothing pinned this and the three had drifted apart -- macOS 3.14.7, Linux 3.12.13, Windows 3.12.12 --
# so the suite ran on a different Python depending on which box you were on. Exercising the 3.12 floor is a job
# for the CI matrix (State.md 8.17), not for whichever interpreter a machine happens to pick.
PY_VERSION := 3.14
CPTAG      := cp$(subst .,,$(PY_VERSION))

# Per-platform plumbing. CONTAINER runs a command inside the manylinux image with the repository at /work.
CONTAINER  := $(DEPS)/run-manylinux.sh
ML_PY      := /work/.venv-ml/bin/python
ML_SYSPY   := /opt/python/$(CPTAG)-$(CPTAG)/bin/python
WIN_PY     := $(ROOT)/.venv/Scripts/python.exe
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

.PHONY: wheels env deps sources occt freetype freeimage rapidjson generate compile stubs test raw_wheel delocate wheel shim shim-parity ocp3xbuild \
        clean_occt clean_freetype clean_rapidjson clean_deps clean_gen clean_dist help

help:
	@echo "targets: env | deps (sources rapidjson freetype freeimage occt) | generate compile stubs test | wheel | shim | wheels | shim-parity | ocp3xbuild"
	@echo "         clean_deps clean_occt clean_freetype clean_freeimage clean_rapidjson clean_gen clean_dist"
	@echo "platform: $(PLATFORM)"

# ---- environment ----------------------------------------------------------------------------------------------
# The venv every other target uses, on PY_VERSION. Building on 3.14 still produces a cp312-abi3 wheel, because
# Py_LIMITED_API=0x030C0000 makes the extension loadable on 3.12 and everything after whatever built it
# (measured 2026-09-24) -- so pinning the development interpreter forward costs no compatibility.
env:
ifeq ($(PLATFORM),linux)
	@# uv here too, against the same pyproject dev group as the other platforms. The hand-written pip list this
	@# replaces had drifted: it was missing libclang, so `make generate` died with "No module named 'clang'"
	@# the first time a Linux tree was built by `make env` (2026-09-24). UV_PROJECT_ENVIRONMENT points uv at
	@# .venv-ml instead of .venv, and `uv venv` replaces an existing environment -- `python -m venv` does not,
	@# which is why pinning the interpreter looked like a no-op until this was measured.
	$(CONTAINER) "cd /work && UV_PROJECT_ENVIRONMENT=/work/.venv-ml uv venv -p $(ML_SYSPY) /work/.venv-ml \
	    && UV_PROJECT_ENVIRONMENT=/work/.venv-ml uv sync --no-install-project"
else
	cd $(ROOT) && uv venv -p $(PY_VERSION)
	@# --no-install-project: `uv sync` would build OCP3x itself, which needs generated sources that do not exist
	@# yet on a fresh clone. The venv here carries the tooling (libclang, nanobind, pytest, mypy, ty); the extension
	@# modules come from `make compile`, and are imported from the staged tree rather than installed.
	cd $(ROOT) && uv sync --no-install-project
endif

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

# deps/occt-src, deps/freetype-src and deps/freeimage-src are the *sources* and are deliberately not cleaned:
# fetching OCCT again is a long download, and re-cloning the other two is pointless --
# neither tree is patched (since 2026-09-25): symbols are kept in at link time and by -fvisibility=hidden.

rapidjson: clean_rapidjson
	$(DEPS)/fetch-rapidjson.sh

# The upstream sources, cloned at a pinned tag if they are not there yet (both scripts are idempotent, so the
# clean_* targets above may delete the builds without touching the checkouts -- a clone of OCCT is 144 MB).
sources:
	$(DEPS)/fetch-occt-src.sh
	$(DEPS)/fetch-freetype-src.sh
	$(DEPS)/fetch-freeimage-src.sh

freetype: clean_freetype
	$(DEPS)/fetch-freetype-src.sh
ifeq ($(PLATFORM),macos)
	$(DEPS)/build-freetype-macos.sh
else ifeq ($(PLATFORM),windows)
	$(DEPS)/build-freetype-windows.sh
else
	$(DEPS)/build-freetype-manylinux.sh
endif

freeimage: clean_freeimage
	$(DEPS)/fetch-freeimage-src.sh
ifeq ($(PLATFORM),macos)
	$(DEPS)/build-freeimage-macos.sh
else ifeq ($(PLATFORM),windows)
	$(DEPS)/build-freeimage-windows.sh
else
	$(DEPS)/build-freeimage-manylinux.sh
endif

occt: clean_occt
	@test -d $(DEPS)/rapidjson || { echo "run 'make rapidjson' first"; exit 1; }
	$(DEPS)/fetch-occt-src.sh
ifeq ($(PLATFORM),macos)
	@test -d $(DEPS)/freetype || { echo "run 'make freetype' first"; exit 1; }
	@test -d $(DEPS)/freeimage || { echo "run 'make freeimage' first"; exit 1; }
	$(DEPS)/build-occt-macos.sh
else ifeq ($(PLATFORM),windows)
	@test -d $(DEPS)/freetype || { echo "run 'make freetype' first"; exit 1; }
	@test -d $(DEPS)/freeimage || { echo "run 'make freeimage' first"; exit 1; }
	$(DEPS)/build-occt-windows.sh
else
	@# On the host, not through $(CONTAINER): the script starts its own container (as build-freetype-manylinux.sh
	@# does). Run through run-manylinux.sh it would be docker inside docker -- "docker: command not found",
	@# which is what `make occt` did on Linux until 2026-09-24, when a build from a bare tree first reached it.
	$(DEPS)/build-occt-manylinux.sh
endif

deps: clean_deps rapidjson freetype freeimage occt

# ---- the development loop -------------------------------------------------------------------------------------

# Only the generated files. src/cpp/common/ocp3x_common.h and ocp3x_ncollection.h are hand-written and tracked,
# as are src/OCP3x/_templates.py and py.typed -- never `rm -rf src/cpp`, which once cost a whole Windows build.
clean_gen:
	rm -rf $(ROOT)/src/cpp/TK*
	rm -f  $(ROOT)/src/cpp/manifest.json $(ROOT)/src/cpp/toolkits.cmake $(ROOT)/src/cpp/common/ncollection_docs.h
	find $(ROOT)/src/OCP3x -mindepth 1 \( -name '_templates.py' -o -name 'py.typed' \) -prune -o -print0 \
	    | xargs -0 rm -rf
	@# The staged tree holds a copy of what was just removed, and the .pth keeps it importable -- without this,
	@# `import OCP3x` would go on working after a clean and quietly serve the previous build.
	rm -rf $(STAGE_DIR)
	rm -f $(wildcard $(ROOT)/.venv/lib/python3.*/site-packages/_ocp3x_dev.pth)

# $(PY), never `uv run`: uv syncs the project before running, which builds OCP3x -- and that needs the generated
# sources this step is about to produce. On a fresh clone it fails on the missing src/cpp/toolkits.cmake.
generate: clean_gen
ifeq ($(PLATFORM),macos)
	cd $(ROOT) && $(PY) -m generator $(TK_FLAGS)
else ifeq ($(PLATFORM),windows)
	cd $(ROOT) && "$(WIN_PY)" -m generator $(TK_FLAGS)
else
	$(CONTAINER) "$(ML_PY) -m generator --occt /work/deps/occt-8.0.1-manylinux --occt-src /work/deps/occt-src $(TK_FLAGS)"
endif

# cmake + ninja directly rather than `uv sync`, so the build reports progress ([12/45] Building CXX object ...)
# instead of sitting behind a spinner for a minute and a half, and so the three platforms have the same shape:
# build into a directory, stage it, and let stubs/test import the staged tree through PYTHONPATH. Installing into
# the venv belongs to the wheel path, not to the development loop.
compile:
ifeq ($(PLATFORM),macos)
	cd $(ROOT) && cmake -S . -B $(BUILD_DIR) -G Ninja -DCMAKE_BUILD_TYPE=Release \
	    -DPython_EXECUTABLE=$(ROOT)/.venv/bin/python -DOCP3X_RAPIDJSON_DIR=$(DEPS)/rapidjson/include
	cd $(ROOT) && cmake --build $(BUILD_DIR)
	$(DEPS)/stage.sh $(BUILD_DIR) $(STAGE_DIR)
	@# Exactly one copy of the extension modules may be in a process: nanobind registers its types per domain, and
	@# a wheel-installed OCP3x next to the staged one aborts the import with "Critical nanobind error".
	cd $(ROOT) && uv pip uninstall -q ocp3x 2>/dev/null || true
else ifeq ($(PLATFORM),windows)
	cd $(ROOT) && ./deps/build-OCP3x-windows.sh
	$(DEPS)/stage.sh $(BUILD_DIR) $(STAGE_DIR)
else
	$(CONTAINER) "cmake -S /work -B /work/build-ml -G Ninja -DCMAKE_BUILD_TYPE=Release \
	    -DPython_EXECUTABLE=$(ML_PY) -DOCP3X_OCCT_DIR=/work/deps/occt-8.0.1-manylinux \
	    -DOCP3X_RAPIDJSON_DIR=/work/deps/rapidjson/include"
	$(CONTAINER) "ninja -k 0 -C /work/build-ml"
	$(CONTAINER) "/work/deps/stage.sh build-ml stage-ml"
endif

stubs:
ifeq ($(PLATFORM),macos)
	cd $(ROOT) && $(PY) -m generator.stubs
	$(DEPS)/stage.sh $(BUILD_DIR) $(STAGE_DIR)          # the stubs are part of the staged tree
else ifeq ($(PLATFORM),windows)
	cd $(ROOT) && PYTHONPATH="$(STAGE_DIR)" "$(WIN_PY)" -m generator.stubs
	$(DEPS)/stage.sh $(BUILD_DIR) $(STAGE_DIR)
else
	$(CONTAINER) "cd /work && PYTHONPATH=/work/stage-ml $(ML_PY) -m generator.stubs"
	$(CONTAINER) "/work/deps/stage.sh build-ml stage-ml"
endif

test:
ifeq ($(PLATFORM),macos)
	cd $(ROOT) && $(PY) -m pytest tests -q -p no:cacheprovider
else ifeq ($(PLATFORM),windows)
	cd $(ROOT) && PYTHONPATH="$(STAGE_DIR)" "$(WIN_PY)" -m pytest tests -q -p no:cacheprovider
else
	$(CONTAINER) "cd /work && PYTHONPATH=/work/stage-ml xvfb-run -a $(ML_PY) -m pytest tests -q -p no:cacheprovider"
endif

# ---- packaging ------------------------------------------------------------------------------------------------
# A built wheel is not portable: the extension modules find the OCCT libraries through an rpath into deps/, so the
# wheel works only on the machine that built it. The repair step copies those libraries in and rewrites the
# references to point inside the wheel (State.md 8.4). Each platform has its own tool, and each leaves the
# system's own libraries alone -- OpenGL and X11 belong to the host, never to the wheel (Design.md 7).
#
# The CI matrix that would run this on every push is a separate, later step (State.md 8.17).

DIST_DIR := $(ROOT)/dist
RAW_DIR  := $(DIST_DIR)/unrepaired

# The tag has to match what OCCT was built against (deps/build-occt-macos.sh sets 11.1). Without this the wheel is
# tagged macosx_11_0 and delocate warns that it will not in fact run on 11.0.
MACOS_TARGET := 11.1
OCCT_BIN_WIN := $(DEPS)/occt-8.0.1/win64/vc14/bin
FREEIMAGE_BIN_WIN := $(DEPS)/freeimage/bin

wheel: delocate

# The unrepaired wheel: correct Python surface, but linked against deps/.
raw_wheel: clean_dist
ifeq ($(PLATFORM),macos)
	cd $(ROOT) && MACOSX_DEPLOYMENT_TARGET=$(MACOS_TARGET) \
	    uv build --wheel --no-build-isolation --python $(PY) -o $(RAW_DIR)
else ifeq ($(PLATFORM),windows)
	@# uv rather than `python -m build`: the venv carries the backend (scikit-build-core), not a build frontend.
	@# --python is not optional. Without it uv picks its own interpreter for the build environment and the build
	@# fails with "No module named 'scikit_build_core'" although the venv has it (measured on gauss 2026-09-24,
	@# where VIRTUAL_ENV is unset; macOS happened to resolve it, which is exactly why both are explicit now).
	cd $(ROOT) && uv build --wheel --no-build-isolation --python "$(WIN_PY)" -o $(RAW_DIR)
else
	$(CONTAINER) "cd /work && uv build --wheel --no-build-isolation --python $(ML_PY) -o /work/dist/unrepaired \
	    -C cmake.define.OCP3X_OCCT_DIR=/work/deps/occt-8.0.1-manylinux \
	    -C cmake.define.OCP3X_RAPIDJSON_DIR=/work/deps/rapidjson/include"
endif
	@ls -lh $(RAW_DIR)

# The repair. Named `delocate` after the macOS tool because that is what the step is, on every platform.
delocate: raw_wheel
ifeq ($(PLATFORM),macos)
	MACOSX_DEPLOYMENT_TARGET=$(MACOS_TARGET) $(ROOT)/.venv/bin/delocate-wheel -w $(DIST_DIR) $(RAW_DIR)/*.whl
else ifeq ($(PLATFORM),windows)
	@# delvewheel cannot read a DLL search path from the binary the way rpath gives it on Unix, so it is told --
	@# both directories, ';'-separated (delvewheel repair --help): FreeImage.dll lives in its own install, not in OCCT's.
	cd $(ROOT) && "$(WIN_PY)" -m delvewheel repair --add-path "$(OCCT_BIN_WIN);$(FREEIMAGE_BIN_WIN)" -w $(DIST_DIR) $(RAW_DIR)/*.whl
else
	@# LD_LIBRARY_PATH for the same reason: the OCCT .so files name each other by SONAME and carry no RUNPATH.
	$(CONTAINER) "LD_LIBRARY_PATH=/work/deps/occt-8.0.1-manylinux/lib auditwheel repair \
	    --plat manylinux_2_28_x86_64 -w /work/dist /work/dist/unrepaired/*.whl"
endif
	@echo "repaired wheel:" && ls -lh $(DIST_DIR)/*.whl

clean_dist:
	rm -rf $(DIST_DIR)

# ---- OCP compatibility shim ---------------------------------------------------------------------------------------
# cadquery-ocp-novtk 8.0.1.0.0+shim: `import OCP.*` on top of OCP3x (shim/). A pure-Python py3-none-any wheel built by
# shim/build_wheel.py with the standard library only, so one build serves every platform. Into dist/, next to OCP3x's.
# Generation reads OCP3x's own signatures, so the staged tree must be importable -- found the way `make test` finds it.
shim:
ifeq ($(PLATFORM),macos)
	$(PY) $(ROOT)/shim/build_wheel.py $(DIST_DIR)
else ifeq ($(PLATFORM),windows)
	cd $(ROOT) && PYTHONPATH="$(STAGE_DIR)" "$(WIN_PY)" shim/build_wheel.py $(DIST_DIR)
else
	$(CONTAINER) "cd /work && PYTHONPATH=/work/stage-ml $(ML_PY) shim/build_wheel.py /work/dist"
endif

# build123d's and ocp-tessellate's own suites through the shim against the real OCP, test by test (shim/parity.py;
# State.md 8.18). Opt-in and not part of `wheels`: two venvs and the suites side by side, ~6 min on the M5. Needs the
# wheels of `make wheels` in DIST_DIR, a build123d checkout (BUILD123D), which it only reads (`git archive HEAD`), and
# the ocp_tessellate sdist ocp3xbuild/ocp3xbuild.sh fetches into build/ocp3xbuild/sdist; everything else goes to
# build/shim-parity. Host-only for now: on Linux the wheels live in the container's world (State.md 8.17).
BUILD123D ?= $(HOME)/Development/CAD/build123d
shim-parity:
ifeq ($(PLATFORM),macos)
	$(PY) $(ROOT)/shim/parity.py --build123d $(BUILD123D) --dist $(DIST_DIR) --work $(ROOT)/build/shim-parity --python $(PY_VERSION)
else
	@echo "shim-parity runs on macOS only so far (see shim/parity.py)"; exit 1
endif

# ---- OCP3x-enabled packages -------------------------------------------------------------------------------------
# build123d 0.13.0, ocpsvg 0.7.0, ocp_gordon 0.3.1 and ocp_tessellate 3.5.3 as sdists from PyPI (sha256-verified),
# patched to import OCP3x instead of OCP (ocp3xbuild/patches, tracked). Output: build/ocp3xbuild/src/<pkg>-<version>,
# ready for `uv pip install dist/ocp3x-*.whl build/ocp3xbuild/src/*` into a fresh venv. Pure source work, so it runs
# on the host on every platform.
# Then a complete test environment in _scratch/.venv (Python 3.14, untracked): recreated on every run, with the OCP3x
# wheel from DIST_DIR (`make wheel` first -- the wheel is what gets tested, not the staged tree) and the four patched
# packages. Activation lasts one shell, so it shares the line with the install.
SCRATCH := $(ROOT)/_scratch
ifeq ($(PLATFORM),windows)
  SCRATCH_ACTIVATE := $(SCRATCH)/.venv/Scripts/activate
else
  SCRATCH_ACTIVATE := $(SCRATCH)/.venv/bin/activate
endif
ocp3xbuild:
	$(ROOT)/ocp3xbuild/ocp3xbuild.sh
	@wheels=$$(ls $(DIST_DIR)/ocp3x-*.whl 2>/dev/null); \
	if [ -z "$$wheels" ]; then echo "ocp3xbuild: no OCP3x wheel in $(DIST_DIR) -- run 'make wheel' first" >&2; exit 1; fi; \
	if [ $$(echo $$wheels | wc -w) -ne 1 ]; then echo "ocp3xbuild: more than one OCP3x wheel in $(DIST_DIR): $$wheels" >&2; exit 1; fi
	mkdir -p $(SCRATCH)
	rm -rf $(SCRATCH)/.venv
	uv venv -p 3.14 $(SCRATCH)/.venv
	@# shell globs, not make's wildcard function: make expands the whole recipe before its first line has created build/ocp3xbuild/src
	. $(SCRATCH_ACTIVATE) && uv pip install $(DIST_DIR)/ocp3x-*.whl $(ROOT)/build/ocp3xbuild/src/*
	@echo "ocp3xbuild: test environment ready -- source $(SCRATCH_ACTIVATE)"

wheels: generate compile stubs test wheel shim
