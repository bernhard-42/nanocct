#!/bin/bash
# OCCT 8.0.1 with AddressSanitizer, for `make asan` (macOS). Same options as deps/build-occt-macos.sh except:
#   - build tree build/asan/occt-build, install build/asan/occt
#   - Release config (keeps the install layout lib/ and OCCT's Release-only defines in the exported config),
#     but BUILD_OPT_PROFILE=Default (no -O3 -fomit-frame-pointer -flto) and -O1 -g, so a report has file:line
#   - -fsanitize=address everywhere
# Needs the sources and third-party builds of `make deps` (deps/occt-src, freetype, freeimage, rapidjson). ~4 min on an
# M5, ~4 GB.
set -euo pipefail
R="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
HERE="$R/deps"
[ -d "$HERE/occt-src" ] || { echo "no $HERE/occt-src -- run make deps" >&2; exit 1; }
SRC="$HERE/occt-src"
BUILD="$R/build/asan/occt-build"
PREFIX="$R/build/asan/occt"
CPUS="$(sysctl -n hw.ncpu)"
SAN="-fsanitize=address -fsanitize-recover=address -fno-omit-frame-pointer -fno-optimize-sibling-calls"

cmake -S "$SRC" -B "$BUILD" -G Ninja \
  -D CMAKE_C_COMPILER=/usr/bin/clang \
  -D CMAKE_CXX_COMPILER=/usr/bin/clang++ \
  -D CMAKE_OSX_DEPLOYMENT_TARGET=11.1 \
  -D CMAKE_BUILD_TYPE=Release \
  -D CMAKE_C_FLAGS="$SAN" \
  -D CMAKE_CXX_FLAGS="$SAN" \
  -D CMAKE_C_FLAGS_RELEASE="-O1 -g -DNDEBUG" \
  -D CMAKE_CXX_FLAGS_RELEASE="-O1 -g -DNDEBUG" \
  -D CMAKE_SHARED_LINKER_FLAGS="-fsanitize=address -Wl,-unexported_symbols_list,$HERE/occt-unexported-symbols.txt" \
  -D CMAKE_MODULE_LINKER_FLAGS="-fsanitize=address" \
  -D CMAKE_EXE_LINKER_FLAGS="-fsanitize=address" \
  -D INSTALL_DIR="$PREFIX" \
  -D CMAKE_PREFIX_PATH="$HERE/freetype;$HERE/freeimage;$HERE/rapidjson" \
  -D 3RDPARTY_FREETYPE_DIR="$HERE/freetype" \
  -D 3RDPARTY_FREETYPE_LIBRARY="$HERE/freetype/lib/libfreetype.a" \
  -D 3RDPARTY_FREETYPE_INCLUDE_DIR_ft2build="$HERE/freetype/include/freetype2" \
  -D 3RDPARTY_FREETYPE_INCLUDE_DIR_freetype2="$HERE/freetype/include/freetype2" \
  -D 3RDPARTY_FREEIMAGE_DIR="$HERE/freeimage" \
  -D 3RDPARTY_FREEIMAGE_LIBRARY="$HERE/freeimage/lib/libFreeImage.dylib" \
  -D 3RDPARTY_FREEIMAGE_INCLUDE_DIR="$HERE/freeimage/include" \
  -D 3RDPARTY_RAPIDJSON_DIR="$HERE/rapidjson" \
  \
  -D USE_VTK=OFF \
  -D USE_TBB=OFF \
  -D USE_TK=OFF \
  -D USE_FREETYPE=ON \
  -D USE_FREEIMAGE=ON \
  -D USE_OPENGL=ON \
  -D USE_GLES2=OFF \
  -D USE_XLIB=OFF \
  -D USE_RAPIDJSON=ON \
  -D USE_FFMPEG=OFF \
  \
  -D BUILD_CPP_STANDARD=C++17 \
  -D BUILD_RELEASE_DISABLE_EXCEPTIONS=OFF \
  -D BUILD_MODULE_Draw=OFF \
  -D BUILD_GTEST=OFF \
  -D BUILD_OPT_PROFILE=Default

ninja -C "$BUILD" -j "$CPUS"
ninja -C "$BUILD" install

added=0
for f in "$PREFIX"/lib/libTK*.dylib; do
    [ -L "$f" ] && continue
    if ! otool -l "$f" | grep -A2 LC_RPATH | grep -q '@loader_path'; then
        install_name_tool -add_rpath @loader_path "$f"
        added=$((added + 1))
    fi
done
echo "rpath: @loader_path added to $added libraries"
echo "OCCT (ASan) installed to $PREFIX"
