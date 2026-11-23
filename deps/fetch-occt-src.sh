#!/bin/bash
# Clone the OCCT sources into deps/occt-src at the pinned tag, if they are not there yet.
#
# Every platform needs them: the macOS and Windows builds compile from this tree, the manylinux container mounts
# the same checkout, and generator/parse.py reads the headers from the *install*, not from here. Until 2026-09-24
# only deps/build-occt-manylinux.sh cloned them, so `make deps` worked on a machine that happened to have the
# sources already and failed on a fresh clone -- which is the case that matters.
#
# A tag rather than a tarball with a checksum, as deps/fetch-rapidjson.sh uses: the assets of OCCT's releases are
# build packages and documentation, no source tarball, and --depth 1 on a tag is what the container has done since it
# was written. A moved tag would go unnoticed here, which is the trade-off.
#
# TAG is the one place that sets the OCCT version. The install prefix carries no version (deps/occt, like
# deps/freetype); what keeps an old tree from passing for the new one is a check at each step: this script checks the
# checkout against TAG, the generator checks the install against these sources (generator/occt.py), CMake checks it
# against the generated sources (CMakeLists.txt), and tests/test_occt_version.py checks nanocct's version and the
# shipped texts against TAG.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TAG=V8_0_2
SRC="$HERE/occt-src"

[ -f "$HERE/build-occt-macos.sh" ] || { echo "not the nanocct deps directory: $HERE" >&2; exit 1; }

if [ -d "$SRC/.git" ]; then
    # A checkout of another tag must not pass: the build would compile it into the prefix named after $TAG. It is not
    # replaced here either -- the old tree may be the only copy of the sources an existing install was built from.
    have="$(git -C "$SRC" describe --tags --exact-match 2>/dev/null || echo unknown)"
    if [ "$have" != "$TAG" ]; then
        echo "$SRC is at '$have', not $TAG -- move it aside (e.g. to $SRC-$have) and run this again" >&2
        exit 1
    fi
    echo "OCCT sources already in $SRC ($have)"
else
    git clone --depth 1 --branch "$TAG" https://github.com/Open-Cascade-SAS/OCCT.git "$SRC"
    echo "OCCT $TAG cloned into $SRC"
fi
test -f "$SRC/CMakeLists.txt"
