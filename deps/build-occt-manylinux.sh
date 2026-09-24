#!/bin/bash
# Build FreeType and OCCT 8.0.1 for Linux inside the manylinux_2_28 container (deps/manylinux.Dockerfile), so the
# result runs against glibc 2.28 while being compiled by gcc 14. This is the Linux counterpart of
# deps/build-occt-windows.sh; deps/build-occt-linux.sh builds against the host toolchain instead and is only useful
# for a development box.
#
# AlmaLinux's default CMAKE_INSTALL_LIBDIR is lib64; it is forced to lib so the paths match the other platforms.
#
# Usage: deps/build-occt-manylinux.sh [install-prefix]     (default: deps/occt-8.0.1-manylinux)
#
# The container runs as the invoking user so nothing on the mounted tree comes out root-owned; everything root has to
# do is baked into the image instead.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
PREFIX_REL="${1:-deps/occt-8.0.1-manylinux}"
IMAGE=nanoocp-manylinux

docker build -q -t "$IMAGE" -f "$HERE/manylinux.Dockerfile" "$HERE"

[ -d "$HERE/occt-src/.git" ] || git clone --depth 1 --branch V8_0_1 https://github.com/Open-Cascade-SAS/OCCT.git "$HERE/occt-src"
[ -d "$HERE/freetype-src/.git" ] || git clone --depth 1 --branch VER-2-14-3 https://gitlab.freedesktop.org/freetype/freetype.git "$HERE/freetype-src"
"$HERE/hide-freetype-symbols.sh"        # FT_* must not leak out of libTKService
[ -d "$HERE/rapidjson/include/rapidjson" ] || { echo "missing $HERE/rapidjson (run deps/fetch-rapidjson.sh)" >&2; exit 1; }

# HOME: the mapped uid has no passwd entry in the container, so $HOME is empty and cmake tries to write //.cmake
docker run --rm -u "$(id -u):$(id -g)" -e HOME=/tmp -v "$ROOT:/work" -w /work "$IMAGE" bash -euo pipefail -c '
PREFIX="/work/'"$PREFIX_REL"'"
cmake -S deps/freetype-src -B deps/freetype-build-ml -G Ninja \
  -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/work/deps/freetype-ml \
  -D CMAKE_INSTALL_LIBDIR=lib \
  -D CMAKE_POSITION_INDEPENDENT_CODE=ON -D BUILD_SHARED_LIBS=OFF \
  -D FT_DISABLE_ZLIB=TRUE -D FT_DISABLE_BZIP2=TRUE -D FT_DISABLE_PNG=TRUE \
  -D FT_DISABLE_HARFBUZZ=TRUE -D FT_DISABLE_BROTLI=TRUE
ninja -C deps/freetype-build-ml install

# the same OCCT flags as deps/build-occt.sh and deps/build-occt-windows.sh, so the three installs stay comparable
cmake -S deps/occt-src -B deps/occt-build-ml -G Ninja \
  -D CMAKE_BUILD_TYPE=Release \
  -D INSTALL_DIR="$PREFIX" \
  -D CMAKE_PREFIX_PATH="/work/deps/freetype-ml;/work/deps/rapidjson" \
  -D 3RDPARTY_FREETYPE_DIR=/work/deps/freetype-ml \
  -D 3RDPARTY_FREETYPE_LIBRARY=/work/deps/freetype-ml/lib/libfreetype.a \
  -D 3RDPARTY_FREETYPE_LIBRARY_DIR=/work/deps/freetype-ml/lib \
  -D 3RDPARTY_FREETYPE_INCLUDE_DIR_ft2build=/work/deps/freetype-ml/include/freetype2 \
  -D 3RDPARTY_FREETYPE_INCLUDE_DIR_freetype2=/work/deps/freetype-ml/include/freetype2 \
  -D 3RDPARTY_RAPIDJSON_DIR=/work/deps/rapidjson \
  -D USE_VTK=OFF -D USE_TBB=OFF -D USE_TK=OFF \
  -D USE_FREETYPE=ON -D USE_OPENGL=ON -D USE_GLES2=OFF -D USE_XLIB=ON \
  -D USE_RAPIDJSON=ON -D USE_FFMPEG=OFF \
  -D BUILD_CPP_STANDARD=C++17 \
  -D BUILD_RELEASE_DISABLE_EXCEPTIONS=OFF \
  -D BUILD_MODULE_Draw=OFF \
  -D BUILD_GTEST=OFF \
  -D BUILD_OPT_PROFILE=Production
ninja -C deps/occt-build-ml install
echo "OCCT installed to $PREFIX"
'
