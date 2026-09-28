#!/bin/bash
# Build OCCT 8.0.1 for Linux inside the manylinux_2_28 container (deps/manylinux.Dockerfile), so the result runs
# against glibc 2.28 while being compiled by gcc 14. This is the Linux counterpart of deps/build-occt-macos.sh and
# deps/build-occt-windows.sh, and it is the only Linux build: the container is the Linux platform (Design.md 7),
# so there is one Linux environment and it is the one CI will use. FreeType comes from
# deps/build-freetype-manylinux.sh first, exactly as the other two platforms expect `make freetype` before
# `make occt`.
#
# FreeImage is named twice, because OCCT asks for it twice. Its configure step (adm/cmake/3rdparty_macro.cmake)
# searches for CSF_FreeImagePlus, which is lowercase "freeimage", unless 3RDPARTY_FREEIMAGE_LIBRARY_freeimage already
# names an existing file -- and the library is libFreeImage.so, which a case-sensitive filesystem does not match
# (macOS's does, so the macOS script gets away with the generic name). The link step then takes the file name from
# 3RDPARTY_FREEIMAGE_LIBRARY (adm/cmake/occt_macros.cmake, PROCESS_CSF_LIBRARIES).
#
# The OCCT libraries get a RUNPATH to FreeImage ($ORIGIN-relative, so it holds in the container and on the host). An
# extension module finds the OCCT libraries through its own RUNPATH only because it NEEDs each of them directly; a
# RUNPATH does not reach the dependencies of a dependency, so libTKService's NEEDED libFreeImage.so had no search path
# at all (measured on banach 2026-09-25: "libFreeImage.so: cannot open shared object file"). macOS never saw this:
# there libTKService records FreeImage by its absolute install name. auditwheel follows the RUNPATH when it bundles.
#
# AlmaLinux's default CMAKE_INSTALL_LIBDIR is lib64; it is forced to lib so the paths match the other platforms.
#
# Usage: deps/build-occt-manylinux.sh [install-prefix]     (default: deps/occt-8.0.1-manylinux)
#
# The container runs as the invoking user so nothing on the mounted tree comes out root-owned; everything root has to
# do is baked into the image instead.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PREFIX_REL="${1:-deps/occt-8.0.1-manylinux}"

# One place pins the tags, so the container and the host cannot drift apart (both scripts are idempotent).
"$HERE/fetch-occt-src.sh"
[ -d "$HERE/rapidjson/include/rapidjson" ] || { echo "missing $HERE/rapidjson (run deps/fetch-rapidjson.sh)" >&2; exit 1; }
[ -f "$HERE/freetype-ml/lib/libfreetype.a" ] || { echo "missing $HERE/freetype-ml (run 'make freetype')" >&2; exit 1; }
[ -f "$HERE/freeimage-ml/lib/libFreeImage.so" ] || { echo "missing $HERE/freeimage-ml (run 'make freeimage')" >&2; exit 1; }

# Through run-manylinux.sh like the FreeType and FreeImage builds, so the image and its architecture are named in one
# place (until 2026-09-28 this script ran its own `docker build`/`docker run`, and the rename to OCP3x broke both).
"$HERE/run-manylinux.sh" '
set -euo pipefail
PREFIX="/work/'"$PREFIX_REL"'"
# the same OCCT flags as deps/build-occt-macos.sh and deps/build-occt-windows.sh, so the three installs stay comparable
cmake -S deps/occt-src -B deps/occt-build-ml -G Ninja \
  -D CMAKE_BUILD_TYPE=Release \
  -D INSTALL_DIR="$PREFIX" \
  -D CMAKE_PREFIX_PATH="/work/deps/freetype-ml;/work/deps/freeimage-ml;/work/deps/rapidjson" \
  -D 3RDPARTY_FREETYPE_DIR=/work/deps/freetype-ml \
  -D 3RDPARTY_FREETYPE_LIBRARY=/work/deps/freetype-ml/lib/libfreetype.a \
  -D 3RDPARTY_FREETYPE_LIBRARY_DIR=/work/deps/freetype-ml/lib \
  -D 3RDPARTY_FREETYPE_INCLUDE_DIR_ft2build=/work/deps/freetype-ml/include/freetype2 \
  -D 3RDPARTY_FREETYPE_INCLUDE_DIR_freetype2=/work/deps/freetype-ml/include/freetype2 \
  -D 3RDPARTY_FREEIMAGE_DIR=/work/deps/freeimage-ml \
  -D 3RDPARTY_FREEIMAGE_LIBRARY=/work/deps/freeimage-ml/lib/libFreeImage.so \
  -D 3RDPARTY_FREEIMAGE_LIBRARY_DIR=/work/deps/freeimage-ml/lib \
  -D 3RDPARTY_FREEIMAGE_LIBRARY_freeimage=/work/deps/freeimage-ml/lib/libFreeImage.so \
  -D 3RDPARTY_FREEIMAGE_LIBRARY_DIR_freeimage=/work/deps/freeimage-ml/lib \
  -D 3RDPARTY_FREEIMAGE_INCLUDE_DIR=/work/deps/freeimage-ml/include \
  -D 3RDPARTY_RAPIDJSON_DIR=/work/deps/rapidjson \
  -D USE_VTK=OFF -D USE_TBB=OFF -D USE_TK=OFF \
  -D CMAKE_SHARED_LINKER_FLAGS="-Wl,--version-script=/work/deps/occt-version-script.map" \
  -D "CMAKE_INSTALL_RPATH=\$ORIGIN/../../freeimage-ml/lib" \
  -D USE_FREETYPE=ON -D USE_FREEIMAGE=ON -D USE_OPENGL=ON -D USE_GLES2=OFF -D USE_XLIB=ON \
  -D USE_RAPIDJSON=ON -D USE_FFMPEG=OFF \
  -D BUILD_CPP_STANDARD=C++17 \
  -D BUILD_RELEASE_DISABLE_EXCEPTIONS=OFF \
  -D BUILD_MODULE_Draw=OFF \
  -D BUILD_GTEST=OFF \
  -D BUILD_OPT_PROFILE=Production
ninja -C deps/occt-build-ml install
echo "OCCT installed to $PREFIX"
'
