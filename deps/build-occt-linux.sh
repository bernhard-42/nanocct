#!/bin/bash
# Build OCCT 8.0.1 on Linux with gcc into deps/occt-8.0.1. The Linux counterpart of deps/build-occt.sh, same OCCT
# flags, so the three installs are comparable (Design.md 8.2). Two deliberate differences from the macOS script:
#
#  - FreeType is the distribution's (libfreetype-dev, found through pkg-config), not the static build from
#    deps/build-freetype.sh. OCCT only needs a FreeType to link against here; the static one exists on macOS and
#    Windows because those platforms have no system FreeType to use.
#  - the sources are cloned by this script if they are missing (`git clone --depth 1 --branch V8_0_1`), which is how
#    the Windows and CI paths get them too.
#
# USE_XLIB=ON is OCCT's own default on Linux (its CMakeLists.txt:389 turns it off only for Apple and the no-Xlib
# platforms) and is what a Linux user expects: with OFF, OCCT goes through EGL, Xw_Window is a stub and the viewer
# never initialises -- "EGL display is unavailable" even with a GPU present. macOS and Windows keep OFF because
# neither has X11; this is the one flag on which the three OCCT builds deliberately differ (2026-09-23).
#
# Prerequisites: git, cmake, ninja, gcc, libfreetype-dev, libegl1-mesa-dev, and deps/rapidjson (deps/fetch-rapidjson.sh).
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$HERE/occt-src"
BUILD="$HERE/occt-build"
PREFIX="$HERE/occt-8.0.1"

[ -d "$HERE/rapidjson/include/rapidjson" ] || { echo "missing $HERE/rapidjson (run deps/fetch-rapidjson.sh)" >&2; exit 1; }
pkg-config --exists freetype2 || { echo "no freetype2 (apt install libfreetype-dev)" >&2; exit 1; }

# A partial occt-src (only the cmake files were staged on banach for the generator) is not a checkout: move it aside
# rather than delete it, and clone next to it.
if [ ! -f "$SRC/CMakeLists.txt" ]; then
  if [ -e "$SRC" ]; then
    mv "$SRC" "$SRC.partial-$(date +%Y%m%d-%H%M%S)"
    echo "moved the partial $SRC aside"
  fi
  git clone --depth 1 --branch V8_0_1 https://github.com/Open-Cascade-SAS/OCCT.git "$SRC"
fi
# likewise for an install prefix that holds only staged headers: OCCT installs into it and stale files would survive
if [ -e "$PREFIX" ] && [ ! -d "$PREFIX/lib" ]; then
  mv "$PREFIX" "$PREFIX.staged-$(date +%Y%m%d-%H%M%S)"
  echo "moved the header-only $PREFIX aside"
fi

FT_INC="$(pkg-config --variable=includedir freetype2)/freetype2"
FT_LIB="$(pkg-config --variable=libdir freetype2)/libfreetype.so"
[ -f "$FT_LIB" ] || { echo "no $FT_LIB" >&2; exit 1; }
echo "freetype: $FT_LIB ($(pkg-config --modversion freetype2)), headers $FT_INC"

cmake -S "$SRC" -B "$BUILD" -G Ninja \
  -D CMAKE_C_COMPILER=/usr/bin/gcc \
  -D CMAKE_CXX_COMPILER=/usr/bin/g++ \
  -D CMAKE_BUILD_TYPE=Release \
  -D INSTALL_DIR="$PREFIX" \
  -D CMAKE_PREFIX_PATH="$HERE/rapidjson" \
  -D 3RDPARTY_FREETYPE_DIR="$(pkg-config --variable=prefix freetype2)" \
  -D 3RDPARTY_FREETYPE_LIBRARY="$FT_LIB" \
  -D 3RDPARTY_FREETYPE_INCLUDE_DIR_ft2build="$FT_INC" \
  -D 3RDPARTY_FREETYPE_INCLUDE_DIR_freetype2="$FT_INC" \
  -D 3RDPARTY_RAPIDJSON_DIR="$HERE/rapidjson" \
  \
  -D USE_VTK=OFF \
  -D USE_TBB=OFF \
  -D USE_TK=OFF \
  -D USE_FREETYPE=ON \
  -D USE_OPENGL=ON \
  -D USE_GLES2=OFF \
  -D USE_XLIB=ON \
  -D USE_RAPIDJSON=ON \
  -D USE_FFMPEG=OFF \
  \
  -D BUILD_CPP_STANDARD=C++17 \
  -D BUILD_RELEASE_DISABLE_EXCEPTIONS=OFF \
  -D BUILD_MODULE_Draw=OFF \
  -D BUILD_GTEST=OFF \
  -D BUILD_OPT_PROFILE=Production

ninja -C "$BUILD" install
echo "OCCT installed to $PREFIX"
