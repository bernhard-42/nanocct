# nanoOCP — one entry point for building it yourself, on macOS, Linux and Windows.
#
#   make deps        fetch and build OCCT, FreeType and RapidJSON from scratch (long: OCCT is ~4 min on an M5)
#   make all         generate -> compile -> stubs -> test -> wheel
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
# Every step orchestrates its own parallelism (ninja -j, NANOOCP_JOBS = one worker per core), so the targets
# themselves are serial.
.NOTPARALLEL:
.DEFAULT_GOAL := all

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
  $(error ROOT=$(ROOT) is not the nanoOCP tree -- refusing to run)
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

# Per-platform plumbing. CONTAINER runs a command inside the manylinux image with the repository at /work.
CONTAINER  := $(DEPS)/run-manylinux.sh
ML_PY      := /work/.venv-ml/bin/python
ML_SYSPY   := /opt/python/cp312-cp312/bin/python
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

.PHONY: all env deps occt freetype rapidjson generate compile stubs test delocate wheel \
        clean_occt clean_freetype clean_rapidjson clean_deps clean_gen help

help:
	@echo "targets: env | deps (occt freetype rapidjson) | generate compile stubs test | wheel | all"
	@echo "         clean_deps clean_occt clean_freetype clean_rapidjson clean_gen"
	@echo "platform: $(PLATFORM)"

# ---- environment ----------------------------------------------------------------------------------------------
# The venv every other target uses. No Python is pinned: `requires-python = ">=3.12"` is the floor (emit.py uses
# PEP 701 f-strings, so 3.10 fails at import), and 3.12 is what the *wheel* targets -- Py_LIMITED_API=0x030C0000
# makes the extension loadable on 3.12 and everything after, whatever built it. Building on 3.14 produces a
# cp312-abi3 wheel just the same (measured 2026-09-24), so the development interpreter can be the current one.
env:
ifeq ($(PLATFORM),linux)
	$(CONTAINER) "$(ML_SYSPY) -m venv /work/.venv-ml && /work/.venv-ml/bin/pip install -q -U pip pytest mypy ty"
else
	cd $(ROOT) && uv venv
	@# --no-install-project: `uv sync` would build nanoocp itself, which needs generated sources that do not exist
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

clean_rapidjson:
	rm -rf $(DEPS)/rapidjson $(DEPS)/rapidjson-src $(DEPS)/rapidjson-1.1.0.tar.gz

clean_deps: clean_occt clean_freetype clean_rapidjson

# deps/occt-src and deps/freetype-src are the *sources* and are deliberately not cleaned: fetching OCCT again is a
# long download, and the FreeType tree carries the visibility patch (deps/hide-freetype-symbols.sh).

rapidjson: clean_rapidjson
	$(DEPS)/fetch-rapidjson.sh

freetype: clean_freetype
ifeq ($(PLATFORM),macos)
	$(DEPS)/build-freetype.sh
else ifeq ($(PLATFORM),windows)
	$(DEPS)/build-freetype-windows.sh
else
	@echo "linux: FreeType is built inside the container as part of 'make occt' (deps/build-occt-manylinux.sh)"
endif

occt: clean_occt
	@test -d $(DEPS)/rapidjson || { echo "run 'make rapidjson' first"; exit 1; }
ifeq ($(PLATFORM),macos)
	@test -d $(DEPS)/freetype || { echo "run 'make freetype' first"; exit 1; }
	$(DEPS)/build-occt.sh
else ifeq ($(PLATFORM),windows)
	@test -d $(DEPS)/freetype || { echo "run 'make freetype' first"; exit 1; }
	$(DEPS)/build-occt-windows.sh
else
	$(CONTAINER) /work/deps/build-occt-manylinux.sh
endif

deps: clean_deps rapidjson freetype occt

# ---- the development loop -------------------------------------------------------------------------------------

# Only the generated files. src/cpp/common/nanoocp_common.h and nanoocp_ncollection.h are hand-written and tracked,
# as are src/nanoocp/_templates.py and py.typed -- never `rm -rf src/cpp`, which once cost a whole Windows build.
clean_gen:
	rm -rf $(ROOT)/src/cpp/TK*
	rm -f  $(ROOT)/src/cpp/manifest.json $(ROOT)/src/cpp/toolkits.cmake $(ROOT)/src/cpp/common/ncollection_docs.h
	find $(ROOT)/src/nanoocp -mindepth 1 \( -name '_templates.py' -o -name 'py.typed' \) -prune -o -print0 \
	    | xargs -0 rm -rf
	@# The staged tree holds a copy of what was just removed, and the .pth keeps it importable -- without this,
	@# `import nanoocp` would go on working after a clean and quietly serve the previous build.
	rm -rf $(STAGE_DIR)
	rm -f $(wildcard $(ROOT)/.venv/lib/python3.*/site-packages/_nanoocp_dev.pth)

# $(PY), never `uv run`: uv syncs the project before running, which builds nanoocp -- and that needs the generated
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
	    -DPython_EXECUTABLE=$(ROOT)/.venv/bin/python -DNANOOCP_RAPIDJSON_DIR=$(DEPS)/rapidjson/include
	cd $(ROOT) && cmake --build $(BUILD_DIR)
	$(DEPS)/stage.sh $(BUILD_DIR) $(STAGE_DIR)
	@# Exactly one copy of the extension modules may be in a process: nanobind registers its types per domain, and
	@# a wheel-installed nanoocp next to the staged one aborts the import with "Critical nanobind error".
	cd $(ROOT) && uv pip uninstall -q nanoocp 2>/dev/null || true
else ifeq ($(PLATFORM),windows)
	cd $(ROOT) && ./deps/build-nanoocp-windows.sh
	$(DEPS)/stage.sh $(BUILD_DIR) $(STAGE_DIR)
else
	$(CONTAINER) "cmake -S /work -B /work/build-ml -G Ninja -DCMAKE_BUILD_TYPE=Release \
	    -DPython_EXECUTABLE=$(ML_PY) -DNANOOCP_OCCT_DIR=/work/deps/occt-8.0.1-manylinux \
	    -DNANOOCP_RAPIDJSON_DIR=/work/deps/rapidjson/include"
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
# Not implemented yet (State.md 8.4): bundling the OCCT libraries per platform with delocate / auditwheel
# (excluding libGL, libEGL and libX11, which belong to the host) / delvewheel, and the CI matrix around it.

delocate:

wheel: delocate

all: generate compile stubs test wheel
