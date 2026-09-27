#!/bin/bash
# Vendor RapidJSON into deps/rapidjson at a pinned tag, so OCCT's glTF reader/writer (TKDEGLTF) compiles against the
# same headers on every platform instead of whatever /opt/homebrew/opt/rapidjson happens to hold (State.md 8.13).
# RapidJSON is header-only: there is nothing to build and nothing extra in the wheel, the headers *are* the library.
#
# v1.1.0 (2016) is the last release. The two-commit patch is the one Homebrew applies and therefore what OCP3x has
# been built and tested against: it removes a GenericStringRef::operator= that falls off the end without returning and
# declares it deleted instead (upstream issue #718). Both downloads are verified against their sha256.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VERSION=1.1.0
TARBALL_URL="https://github.com/Tencent/rapidjson/archive/refs/tags/v${VERSION}.tar.gz"
TARBALL_SHA256=bf7ced29704a1e696fbccf2a2b4ea068e7774fa37f6d7dd4039d0787f8bed98e
PATCH_URL="https://github.com/Tencent/rapidjson/commit/9bd618f545ab647e2c3bcbf2f1d87423d6edf800.patch?full_index=1"
PATCH_SHA256=ce341a69d6c17852fddd5469b6aabe995fd5e3830379c12746a18c3ae858e0e1

TARBALL="$HERE/rapidjson-${VERSION}.tar.gz"
PATCH="$HERE/rapidjson-${VERSION}-718.patch"
SRC="$HERE/rapidjson-src"
PREFIX="$HERE/rapidjson"

# the two rm -rf below are built from $HERE: refuse to run if that is not the deps directory of a checkout
[ -f "$HERE/build-occt-macos.sh" ] || { echo "not the OCP3x deps directory: $HERE" >&2; exit 1; }

[ -f "$TARBALL" ] || curl -fsSL -o "$TARBALL" "$TARBALL_URL"
[ -f "$PATCH" ] || curl -fsSL -o "$PATCH" "$PATCH_URL"
echo "$TARBALL_SHA256  $TARBALL" | shasum -a 256 -c -
echo "$PATCH_SHA256  $PATCH" | shasum -a 256 -c -

rm -rf "$SRC" "$PREFIX"
mkdir -p "$SRC"
tar -xzf "$TARBALL" -C "$SRC" --strip-components=1
patch -p1 -d "$SRC" < "$PATCH"

mkdir -p "$PREFIX"
cp -R "$SRC/include" "$PREFIX/include"
test -f "$PREFIX/include/rapidjson/document.h"
grep -q "Copy assignment operator not permitted" "$PREFIX/include/rapidjson/document.h"
echo "RapidJSON $VERSION (+ upstream #718) installed to $PREFIX"
