#!/bin/bash
# Build FreeImage as a shared library inside the manylinux_2_28 container, into deps/freeimage-ml.
#
# The Linux counterpart of deps/build-freeimage-macos.sh and deps/build-freeimage-windows.sh, with the same
# flags: shared, position-independent, hidden visibility, and the four codecs FreeImage can drop out of the box
# switched off. See build-freeimage-macos.sh for why it has to be shared (a static FreeImage never registers its
# plugins, because the auto-initialiser is compiled out and OCCT never calls FreeImage_Initialise) and why no
# source patch is needed to keep the bundled codecs' symbols in. Unlike macOS, Linux also needs a link-time export
# list (deps/freeimage-version-script.map): the visibility flags leave libstdc++ symbols exported here.
#
# AlmaLinux's default CMAKE_INSTALL_LIBDIR is lib64; it is forced to lib so the paths match the other platforms.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

"$HERE/fetch-freeimage-src.sh"

"$HERE/run-manylinux.sh" '
set -euo pipefail
cmake -S /work/deps/freeimage-src -B /work/deps/freeimage-build-ml -G Ninja \
  -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/work/deps/freeimage-ml \
  -D CMAKE_INSTALL_LIBDIR=lib \
  -D CMAKE_POSITION_INDEPENDENT_CODE=ON \
  -D FREEIMAGE_STATIC=OFF -D BUILD_SHARED_LIBS=ON -D BUILD_TESTS=OFF \
  -D BUILD_WEBP=OFF -D BUILD_OPENEXR=OFF -D BUILD_LIBRAWLITE=OFF -D BUILD_JXR=OFF \
  -D CMAKE_C_VISIBILITY_PRESET=hidden -D CMAKE_CXX_VISIBILITY_PRESET=hidden \
  -D CMAKE_VISIBILITY_INLINES_HIDDEN=ON \
  -D CMAKE_SHARED_LINKER_FLAGS="-Wl,--version-script=/work/deps/freeimage-version-script.map"
ninja -C /work/deps/freeimage-build-ml install

# The same assertion as on macOS: nothing but FreeImage own API may be exported, so a bundled libpng or zlib
# cannot be bound against another copy in the process. For a shared object the dynamic symbol table *is* the
# export list -- a hidden symbol never reaches .dynsym -- so nm -D --defined-only answers it directly, with no
# need for readelf visibility columns.
LIB=/work/deps/freeimage-ml/lib/libfreeimage.so
if [ ! -f "$LIB" ]; then LIB=/work/deps/freeimage-ml/lib/libFreeImage.so; fi
test -f "$LIB"
leaked=$(nm -D --defined-only "$LIB" | sed "s/.* //" | grep -vE "^FreeImage_|^_init$|^_fini$|^__bss_start$|^_edata$|^_end$" || true)
if [ -n "$leaked" ]; then
    echo "FreeImage exports non-FreeImage symbols:" >&2
    echo "$leaked" | sed "s/^/  /" | head -20 >&2
    exit 1
fi
echo "FreeImage: $(nm -D --defined-only "$LIB" | grep -c FreeImage_) FreeImage_* exported, nothing else"
'
echo "FreeImage installed to $HERE/freeimage-ml"
