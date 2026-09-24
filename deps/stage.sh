#!/bin/bash
# Stage a build for use through PYTHONPATH: the Python shims from src/nanoocp plus the extension modules built
# into <build-dir>. The same shape on all three platforms (Design.md 7) -- a staged tree is what `make stubs` and
# `make test` import, so the development loop never depends on the package being installed.
#
#   deps/stage.sh <build-dir> <stage-dir>
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="${1:?stage: build directory required}"
STAGE="${2:?stage: stage directory required}"
cd "$ROOT"
# `rm -rf "$STAGE"` below: refuse anything that is not a directory inside the tree, so an empty or stray argument
# cannot aim it somewhere else.
case "$(cd "$(dirname "$STAGE")" 2>/dev/null && pwd)/$(basename "$STAGE")" in
    "$ROOT"/?*) : ;;
    *) echo "stage: refusing to write to '$STAGE' -- not inside $ROOT" >&2; exit 1 ;;
esac
[ -d "$BUILD" ] || { echo "stage: no $BUILD -- run the compile step first" >&2; exit 1; }
rm -rf "$STAGE"
mkdir -p "$STAGE"
cp -r src/nanoocp "$STAGE/nanoocp"
find "$STAGE" -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true
# One -name per extension suffix, not overlapping globs: *.so would match *.abi3.so again and copy each twice.
find "$BUILD" -maxdepth 1 -type f \( -name '*.abi3.so' -o -name '*.pyd' \) -exec cp {} "$STAGE/nanoocp/" \;
n=$(find "$STAGE/nanoocp" -maxdepth 1 -type f \( -name '*.abi3.so' -o -name '*.pyd' \) | wc -l | tr -d ' ')
[ "$n" -gt 0 ] || { echo "stage: no extension modules in $BUILD" >&2; exit 1; }
echo "stage: $n extension modules from $BUILD into $STAGE"

# Put the staged tree on the venv's sys.path with a .pth, the same mechanism an editable install uses, so that
# `import nanoocp` works anywhere in the venv without PYTHONPATH. It must stay the ONLY copy: nanobind registers
# its types per NB_DOMAIN, and a wheel-installed nanoocp beside this one aborts the import with "Critical nanobind
# error" and no traceback -- which is why the compile step uninstalls that copy first.
SITE=$(echo "$ROOT"/.venv/lib/python3.*/site-packages)
if [ -d "$SITE" ]; then
    printf '%s\n' "$ROOT/$(basename "$STAGE")" > "$SITE/_nanoocp_dev.pth"
    echo "stage: $SITE/_nanoocp_dev.pth -> $STAGE"
fi
