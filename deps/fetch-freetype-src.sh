#!/bin/bash
# Clone the FreeType sources into deps/freetype-src at the pinned tag, if they are not there yet.
#
# macOS and Windows build FreeType statically because they have no system FreeType to link against (3.2), and
# deps/hide-freetype-symbols.sh patches this tree before the build so FT_* stays inside libTKService. Both need
# the sources present; until 2026-09-24 only the manylinux container cloned them.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TAG=VER-2-14-3
SRC="$HERE/freetype-src"

[ -f "$HERE/build-freetype-macos.sh" ] || { echo "not the nanoOCP deps directory: $HERE" >&2; exit 1; }

if [ -d "$SRC/.git" ]; then
    echo "FreeType sources already in $SRC ($(git -C "$SRC" describe --tags --always 2>/dev/null || echo unknown))"
else
    git clone --depth 1 --branch "$TAG" https://gitlab.freedesktop.org/freetype/freetype.git "$SRC"
    echo "FreeType $TAG cloned into $SRC"
fi
test -f "$SRC/include/freetype/config/public-macros.h"
