#!/bin/bash
# Clone the FreeImage sources into deps/freeimage-src at the pinned tag, if they are not there yet.
#
# Why this fork and not upstream (State.md 8.9): stock FreeImage 3.18.0 has no CMake at all and no per-codec
# switches, so excluding a codec or hiding a symbol would both mean patching. danoli3's 3.19.x has BUILD_<CODEC>
# options and, more importantly, exports nothing but its own FreeImage_* API under -fvisibility=hidden, with no
# patch: every bundled codec (libpng, zlib, libjpeg, libtiff, OpenJPEG) falls to the flag, and only FreeImage.h's
# own DLL_API forces default visibility (Source/FreeImage.h:67). deps/build-freeimage-macos.sh asserts it.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TAG=3.19.15
SRC="$HERE/freeimage-src"

[ -f "$HERE/build-freeimage-macos.sh" ] || { echo "not the nanocct deps directory: $HERE" >&2; exit 1; }

if [ -d "$SRC/.git" ]; then
    echo "FreeImage sources already in $SRC ($(git -C "$SRC" describe --tags --always 2>/dev/null || echo unknown))"
else
    git clone --depth 1 --branch "$TAG" https://github.com/danoli3/FreeImage.git "$SRC"
    echo "FreeImage $TAG cloned into $SRC"
fi
test -f "$SRC/Source/FreeImage.h"
test -f "$SRC/CMakeLists.txt"
