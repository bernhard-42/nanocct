#!/bin/bash
# Build FreeType as a static library inside the manylinux_2_28 container, into deps/freetype-ml.
#
# The Linux counterpart of deps/build-freetype-macos.sh and deps/build-freetype-windows.sh, with the same flags:
# static, position-independent, no optional dependencies (zlib/bzip2/png/harfbuzz/brotli), and the FT_* symbols
# hidden first so they cannot leak out of libTKService (3.2).
#
# Until 2026-09-24 this was part of deps/build-occt-manylinux.sh, which made `make freetype` a no-op on Linux and
# put a FreeType build inside a script named after OCCT. Now every platform has the same two steps.
#
# AlmaLinux's default CMAKE_INSTALL_LIBDIR is lib64; it is forced to lib so the paths match the other platforms.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

"$HERE/fetch-freetype-src.sh"
"$HERE/hide-freetype-symbols.sh"        # FT_* must not leak out of libTKService

"$HERE/run-manylinux.sh" '
cmake -S /work/deps/freetype-src -B /work/deps/freetype-build-ml -G Ninja \
  -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/work/deps/freetype-ml \
  -D CMAKE_INSTALL_LIBDIR=lib \
  -D CMAKE_POSITION_INDEPENDENT_CODE=ON -D BUILD_SHARED_LIBS=OFF \
  -D FT_DISABLE_ZLIB=TRUE -D FT_DISABLE_BZIP2=TRUE -D FT_DISABLE_PNG=TRUE \
  -D FT_DISABLE_HARFBUZZ=TRUE -D FT_DISABLE_BROTLI=TRUE
ninja -C /work/deps/freetype-build-ml install
'
echo "FreeType installed to $HERE/freetype-ml"
