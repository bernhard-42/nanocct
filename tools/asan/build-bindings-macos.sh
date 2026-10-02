#!/bin/bash
# nanocct's extension modules with AddressSanitizer, against the ASan OCCT in build/asan/occt (`make asan`, macOS), from the
# generated sources in src/cpp. RelWithDebInfo: a Release build is stripped by nanobind (-Wl,-x -S, NB_OPT =
# Release|MinSizeRel), so its reports would have no file:line. OCCT's exported config adds its five defines only for
# Release (OpenCASCADECompileDefinitionsAndFlags-release.cmake), so they are given by hand here.
# Staged into build/asan/stage by hand: deps/stage.sh would also point .venv's _nanocct_dev.pth at it. The Python files and
# stubs come from stage-mac (`make compile stubs` of the same sources).
set -euo pipefail
R="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
B="$R/build/asan/bindings"
STAGE="$R/build/asan/stage"
SAN="-fsanitize=address -fsanitize-recover=address -fno-omit-frame-pointer -fno-optimize-sibling-calls"
DEFS="-DHAVE_FREETYPE -DHAVE_FREEIMAGE -DHAVE_OPENGL_EXT -DHAVE_RAPIDJSON -DOCC_CONVERT_SIGNALS"

cd "$R"
cmake -S . -B "$B" -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_OSX_DEPLOYMENT_TARGET=11.1 \
    -DCMAKE_CXX_FLAGS="$SAN $DEFS" -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="-O1 -g -DNDEBUG" \
    -DCMAKE_SHARED_LINKER_FLAGS="-fsanitize=address" -DCMAKE_MODULE_LINKER_FLAGS="-fsanitize=address" \
    -DPython_EXECUTABLE="$R/.venv/bin/python" \
    -DNANOCCT_OCCT_DIR="$R/build/asan/occt" -DNANOCCT_RAPIDJSON_DIR="$R/deps/rapidjson/include"
cmake --build "$B"

# the staged tree: stage-mac's Python files and stubs (same HEAD), the ASan modules instead of its own
[ -d "$R/stage-mac/nanocct" ] || { echo "no stage-mac -- run make compile stubs" >&2; exit 1; }
case "$STAGE" in "$R"/build/asan/stage) : ;; *) echo "bad STAGE $STAGE" >&2; exit 1 ;; esac
rm -rf "$STAGE"
mkdir -p "$STAGE"
cp -R "$R/stage-mac/nanocct" "$STAGE/nanocct"
find "$STAGE/nanocct" -maxdepth 1 -name '*.abi3.so' -delete
find "$STAGE" -name '__pycache__' -type d -prune -exec rm -rf {} +
find "$B" -maxdepth 1 -type f -name '*.abi3.so' -exec cp {} "$STAGE/nanocct/" \;
n=$(find "$STAGE/nanocct" -maxdepth 1 -name '*.abi3.so' | wc -l | tr -d ' ')
m=$(find "$R/stage-mac/nanocct" -maxdepth 1 -name '*.abi3.so' | wc -l | tr -d ' ')
[ "$n" = "$m" ] || { echo "stage: $n ASan modules, stage-mac has $m" >&2; exit 1; }
echo "stage: $n ASan modules into $STAGE"
