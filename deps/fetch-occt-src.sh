#!/bin/bash
# Clone the OCCT sources into deps/occt-src at the pinned tag, if they are not there yet.
#
# Every platform needs them: the macOS and Windows builds compile from this tree, the manylinux container mounts
# the same checkout, and generator/parse.py reads the headers from the *install*, not from here. Until 2026-09-24
# only deps/build-occt-manylinux.sh cloned them, so `make deps` worked on a machine that happened to have the
# sources already and failed on a fresh clone -- which is the case that matters (State.md 8.4).
#
# A tag rather than a tarball with a checksum, as deps/fetch-rapidjson.sh uses: OCCT publishes no release tarball
# for V8_0_1, and --depth 1 on a tag is what the container has done since it was written. A moved tag would go
# unnoticed here, which is the trade-off.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TAG=V8_0_1
SRC="$HERE/occt-src"

[ -f "$HERE/build-occt-macos.sh" ] || { echo "not the OCP3x deps directory: $HERE" >&2; exit 1; }

if [ -d "$SRC/.git" ]; then
    echo "OCCT sources already in $SRC ($(git -C "$SRC" describe --tags --always 2>/dev/null || echo unknown))"
else
    git clone --depth 1 --branch "$TAG" https://github.com/Open-Cascade-SAS/OCCT.git "$SRC"
    echo "OCCT $TAG cloned into $SRC"
fi
test -f "$SRC/CMakeLists.txt"
