#!/bin/bash
# Build FreeImage (sources in deps/freeimage-src) as a shared library into deps/freeimage, with every symbol
# hidden except its own API, and the codecs we do not ship switched off.
#
# Why shared and not static, unlike FreeType (State.md 8.9). FreeImage registers its format plugins in
# FreeImage_Initialise(), which a shared build calls by itself -- DllMain on Windows, __attribute__((constructor))
# elsewhere (Source/FreeImage/FreeImage.cpp) -- and OCCT never calls it, because it assumes the shared library.
# Both auto-initialisers sit inside `#ifndef FREEIMAGE_LIB`, and FREEIMAGE_LIB is exactly what a static build
# defines, so a static FreeImage silently has no plugins at all: measured 2026-09-25, Save() fails for every
# extension and Load() reports "unsupported file format" while AdjustGamma() still works. Making it work would
# mean patching FreeImage, which we do not do; the dylib is bundled by delocate/auditwheel instead.
#
# Shared does not mean leaky. -fvisibility=hidden still applies to everything that does not carry FreeImage.h's
# DLL_API, so the exported surface is FreeImage_* alone -- measured: 254 symbols, and zero png_*, jpeg_*, TIFF*,
# opj_*, crc32, deflate or inflate. Those are the ones that would collide with another libpng or zlib in the
# process (Pillow's, say); FreeImage_* is its own namespace and is what OCCT has to link against.
#
# The codec switches are the four FreeImage honours out of the box; the other BUILD_* options exist but their
# plugins are not guarded, so turning them off is a compile error, not an exclusion (State.md 8.9):
#   BUILD_WEBP=OFF      libwebp's WEBP_EXTERN forces visibility("default"), the one macro -fvisibility=hidden
#                       cannot beat. Switching the codec off removes the symbols instead of patching the source.
#   BUILD_OPENEXR=OFF   7.3 MB of codec we do not need (its Imath/Half part is compiled unconditionally anyway).
#   BUILD_LIBRAWLITE=OFF  the only CDDL-licensed component. Already OFF by default; stated for the record.
#   BUILD_JXR=OFF       already OFF by default off Windows, and does not compile on macOS (MSVC SAL annotations).
# JBIG needs no switch: JBIG-KIT is not vendored and LibTIFF4's tiffconf.h leaves JBIG_SUPPORT undefined.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$HERE/freeimage-src"
BUILD="$HERE/freeimage-build"
PREFIX="$HERE/freeimage"

test -f "$SRC/CMakeLists.txt" || { echo "run deps/fetch-freeimage-src.sh first" >&2; exit 1; }

cmake -S "$SRC" -B "$BUILD" -G Ninja \
  -D CMAKE_C_COMPILER=/usr/bin/clang \
  -D CMAKE_CXX_COMPILER=/usr/bin/clang++ \
  -D CMAKE_OSX_DEPLOYMENT_TARGET=11.1 \
  -D CMAKE_BUILD_TYPE=Release \
  -D CMAKE_INSTALL_PREFIX="$PREFIX" \
  -D CMAKE_POSITION_INDEPENDENT_CODE=ON \
  -D BUILD_SHARED_LIBS=ON \
  -D FREEIMAGE_STATIC=OFF \
  -D BUILD_TESTS=OFF \
  -D BUILD_WEBP=OFF \
  -D BUILD_OPENEXR=OFF \
  -D BUILD_LIBRAWLITE=OFF \
  -D BUILD_JXR=OFF \
  -D CMAKE_C_VISIBILITY_PRESET=hidden \
  -D CMAKE_CXX_VISIBILITY_PRESET=hidden \
  -D CMAKE_VISIBILITY_INLINES_HIDDEN=ON \
  -D CMAKE_INSTALL_NAME_DIR="$PREFIX/lib"
ninja -C "$BUILD" install

LIB="$PREFIX/lib/libFreeImage.dylib"
test -f "$LIB"
# Nothing but FreeImage's own API may be exported. A bundled codec that exported png_* or crc32 would be bound
# by the flat two-level namespace against whatever else the process loaded (Pillow's libpng, for one), which is
# the conflict deps/hide-freetype-symbols.sh exists to prevent for FreeType.
leaked=$(nm -gU "$LIB" | awk '{print $NF}' | grep -vE '^_FreeImage_' || true)
if [ -n "$leaked" ]; then
    echo "FreeImage exports non-FreeImage symbols:" >&2
    echo "$leaked" | sed 's/^/  /' | head -20 >&2
    exit 1
fi
echo "FreeImage installed to $PREFIX ($(du -h "$LIB" | cut -f1); $(nm -gU "$LIB" | wc -l | tr -d ' ') exported, all FreeImage_*)"
