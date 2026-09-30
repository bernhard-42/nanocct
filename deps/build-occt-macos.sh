#!/bin/bash
# Build OCCT 8.0.1 (V8_0_1 tag, sources in deps/occt-src) with Apple clang into deps/occt-8.0.1.
# Mirrors ~/Development/CAD/ocp-build-system/local-build/02-build-occt-sdk.sh, minus conda:
# FreeType is the static build from deps/build-freetype-macos.sh, FreeImage the one from
# deps/build-freeimage-macos.sh and RapidJSON the vendored copy from deps/fetch-rapidjson.sh (run all three
# first), libc++ is the system one. FreeImage on since 2026-09-25 (State.md 8.9): without it Image_AlienPixMap
# reads nothing at all and writes PPM under whatever extension it is given, so an imported textured model
# cannot be displayed. Its archive exports no symbol of its own, which build-freeimage-macos.sh asserts. OpenGL on since 2026-09-22
# (macOS OpenGL.framework, State.md 8.6a). X11 is off because macOS has none; Linux builds with USE_XLIB=ON,
# OCCT's own default there (deps/build-occt-manylinux.sh).
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
  -D CMAKE_SHARED_LINKER_FLAGS="-Wl,-unexported_symbols_list,$HERE/occt-unexported-symbols.txt" \
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
  -D BUILD_OPT_PROFILE=Production

ninja -C "$BUILD" -j "$CPUS"
ninja -C "$BUILD" install

# Give every installed dylib an @loader_path rpath so it can find its siblings (State.md 8.4).
#
# OCCT names each dependency @rpath/libTKX.8.0.dylib but installs no LC_RPATH on the libraries themselves. At
# runtime that is invisible: the extension module carries the rpath and dyld resolves the whole load chain
# through it. It breaks any tool that walks the graph statically -- delocate stops with "Could not find all
# dependencies" as soon as it reaches libTKBO, because on its own that library has nowhere to look, and it
# offers no flag for extra search paths (only --executable-path and --ignore-missing-dependencies, which would
# silently drop them). One rpath pointing at its own directory makes each library self-contained.
#
# Done here rather than with -D CMAKE_INSTALL_RPATH=@loader_path because this is verified and a rebuild is not
# needed to apply it to an existing install. Adding an rpath twice is an error, so each library is checked first.
added=0
for f in "$PREFIX"/lib/libTK*.dylib; do
    [ -L "$f" ] && continue                      # version aliases point at the real file, which is fixed below
    if ! otool -l "$f" | grep -A2 LC_RPATH | grep -q '@loader_path'; then
        install_name_tool -add_rpath @loader_path "$f"
        added=$((added + 1))
    fi
done
echo "rpath: @loader_path added to $added libraries"

echo "OCCT installed to $PREFIX"
