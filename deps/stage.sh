#!/bin/bash
# Stage a build for use through PYTHONPATH: the Python shims from src/OCP3x plus the extension modules built
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
cp -r src/OCP3x "$STAGE/OCP3x"
find "$STAGE" -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true
# One -name per extension suffix, not overlapping globs: *.so would match *.abi3.so again and copy each twice.
find "$BUILD" -maxdepth 1 -type f \( -name '*.abi3.so' -o -name '*.pyd' \) -exec cp {} "$STAGE/OCP3x/" \;
n=$(find "$STAGE/OCP3x" -maxdepth 1 -type f \( -name '*.abi3.so' -o -name '*.pyd' \) | wc -l | tr -d ' ')
[ "$n" -gt 0 ] || { echo "stage: no extension modules in $BUILD" >&2; exit 1; }
echo "stage: $n extension modules from $BUILD into $STAGE"

# Windows: the extension modules find the OCCT DLLs through os.add_dll_directory and nothing else -- Python has
# ignored PATH for extension modules since 3.8. The wheel gets this from delvewheel, which prepends the same call
# to OCP3x/__init__.py; the staged tree needs its own, or `make stubs` and `make test` fail with "DLL load
# failed while importing _TKBO" (2026-09-24 -- they always would have, but every run until then had set the
# directory by hand). sitecustomize is imported by `site` at startup, so it is in place before any OCP3x import.
# FreeImage.dll is not in OCCT's bin directory but in its own install (deps/freeimage/bin), and TKService links it,
# so without that second directory every toolkit above TKernel fails to load (measured on gauss 2026-09-25, the first
# Windows build since FreeImage: "DLL load failed while importing _TKBinXCAF").
if ls "$STAGE/OCP3x"/*.pyd >/dev/null 2>&1; then
    OCCT_BIN="$ROOT/deps/occt-8.0.1/win64/vc14/bin"
    FREEIMAGE_BIN="$ROOT/deps/freeimage/bin"
    [ -d "$OCCT_BIN" ] || { echo "stage: no $OCCT_BIN -- run 'make occt' first" >&2; exit 1; }
    [ -f "$FREEIMAGE_BIN/FreeImage.dll" ] || { echo "stage: no $FREEIMAGE_BIN/FreeImage.dll -- run 'make freeimage' first" >&2; exit 1; }
    {   echo "import os"
        for d in "$OCCT_BIN" "$FREEIMAGE_BIN"; do
            w="$(cygpath -w "$d" 2>/dev/null || echo "$d")"
            echo "if os.path.isdir(r\"$w\"):"
            echo "    os.add_dll_directory(r\"$w\")"
            echo "stage: sitecustomize.py -> os.add_dll_directory($w)" >&2
        done
    } > "$STAGE/sitecustomize.py"
fi
# Put the staged tree on the venv's sys.path with a .pth, the same mechanism an editable install uses, so that
# `import OCP3x` works anywhere in the venv without PYTHONPATH. It must stay the ONLY copy: nanobind registers
# its types per NB_DOMAIN, and a wheel-installed OCP3x beside this one aborts the import with "Critical nanobind
# error" and no traceback -- which is why the compile step uninstalls that copy first.
SITE=$(echo "$ROOT"/.venv/lib/python3.*/site-packages)
if [ -d "$SITE" ]; then
    printf '%s\n' "$ROOT/$(basename "$STAGE")" > "$SITE/_ocp3x_dev.pth"
    echo "stage: $SITE/_ocp3x_dev.pth -> $STAGE"
fi
