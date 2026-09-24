#!/bin/bash
# Build FreeType (sources in deps/freetype-src) as a static library with no optional
# dependencies (no zlib/bzip2/png/harfbuzz/brotli) into deps/freetype.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
"$HERE/hide-freetype-symbols.sh"        # FT_* must not leak out of libTKService
cmake -S "$HERE/freetype-src" -B "$HERE/freetype-build" -G Ninja \
  -D CMAKE_C_COMPILER=/usr/bin/clang \
  -D CMAKE_OSX_DEPLOYMENT_TARGET=11.1 \
  -D CMAKE_BUILD_TYPE=Release \
  -D CMAKE_INSTALL_PREFIX="$HERE/freetype" \
  -D CMAKE_POSITION_INDEPENDENT_CODE=ON \
  -D BUILD_SHARED_LIBS=OFF \
  -D FT_DISABLE_ZLIB=TRUE -D FT_DISABLE_BZIP2=TRUE -D FT_DISABLE_PNG=TRUE \
  -D FT_DISABLE_HARFBUZZ=TRUE -D FT_DISABLE_BROTLI=TRUE
ninja -C "$HERE/freetype-build" install
echo "FreeType installed to $HERE/freetype"
