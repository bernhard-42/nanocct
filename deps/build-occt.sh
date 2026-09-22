#!/bin/bash
# Build OCCT 8.0.1 (V8_0_1 tag, sources in deps/occt-src) with Apple clang into deps/occt-8.0.1.
# Mirrors ~/Development/CAD/ocp-build-system/local-build/02-build-occt-sdk.sh, minus conda:
# FreeType is the static build from deps/build-freetype.sh and RapidJSON the vendored copy from
# deps/fetch-rapidjson.sh (run both first), libc++ is the system one. OpenGL on since 2026-09-22
# (macOS OpenGL.framework, Design.md 8.6a); X11 stays off -- it is the Linux half of that decision.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$HERE/occt-src"
BUILD="$HERE/occt-build"
PREFIX="$HERE/occt-8.0.1"
CPUS="$(sysctl -n hw.ncpu)"

cmake -S "$SRC" -B "$BUILD" -G Ninja \
  -D CMAKE_C_COMPILER=/usr/bin/clang \
  -D CMAKE_CXX_COMPILER=/usr/bin/clang++ \
  -D CMAKE_OSX_DEPLOYMENT_TARGET=11.1 \
  -D CMAKE_BUILD_TYPE=Release \
  -D INSTALL_DIR="$PREFIX" \
  -D CMAKE_PREFIX_PATH="$HERE/freetype;$HERE/rapidjson" \
  -D 3RDPARTY_FREETYPE_DIR="$HERE/freetype" \
  -D 3RDPARTY_FREETYPE_LIBRARY="$HERE/freetype/lib/libfreetype.a" \
  -D 3RDPARTY_FREETYPE_INCLUDE_DIR_ft2build="$HERE/freetype/include/freetype2" \
  -D 3RDPARTY_FREETYPE_INCLUDE_DIR_freetype2="$HERE/freetype/include/freetype2" \
  -D 3RDPARTY_RAPIDJSON_DIR="$HERE/rapidjson" \
  \
  -D USE_VTK=OFF \
  -D USE_TBB=OFF \
  -D USE_TK=OFF \
  -D USE_FREETYPE=ON \
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
  -D BUILD_OPT_PROFILE=Production

ninja -C "$BUILD" -j "$CPUS"
ninja -C "$BUILD" install
echo "OCCT installed to $PREFIX"
