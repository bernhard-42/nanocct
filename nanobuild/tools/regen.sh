#!/bin/bash
# Regenerate nanobuild/patches/<pkg>.patch from the verified sdists, the tools and the hand layer:
#
#   sdist -> tools/port.py -> tools/fix_outargs.py -> tools/manual/<pkg>.patch -> tools/static_names.py -> tools/mkpatch.py
#
#   nanobuild/tools/regen.sh            (after `make nanobuild`, which fetches and verifies the sdists)
#
# The mechanical part comes from the tools; nanobuild/tools/manual/<pkg>.patch holds only what a human decided (results that
# nanoocp returns where OCP filled an argument, streams, version branches, the dependency on nanoocp, tests that need
# a newer upstream). Needs nanoocp importable (the staged tree) and the shim wheel in dist/ (`make shim`): port.py
# reads the OCP -> nanoocp name map from the shim's generated modules. Rerun the four suites against the real OCP
# afterwards (tools/junit_cmp.py) -- a regenerated patch is only as good as that comparison.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NB="$(dirname "$HERE")"
ROOT="$(dirname "$NB")"
PY="${PY:-$ROOT/.venv/bin/python}"
SDIST="$ROOT/build/nanobuild/sdist"
WORK="$ROOT/build/nanobuild/regen"

# the rm -rf below is built from $ROOT: refuse to run if that is not a nanoOCP checkout
[ -f "$ROOT/generator/__main__.py" ] && [ -f "$NB/nanobuild.sh" ] || { echo "not a nanoOCP checkout: $ROOT" >&2; exit 1; }
SHIM_WHEEL="$(ls "$ROOT"/dist/cadquery_ocp_novtk-*.whl 2>/dev/null | head -1)"
[ -n "$SHIM_WHEEL" ] || { echo "no shim wheel in dist/ -- run make shim first" >&2; exit 1; }

# the directories of each sdist that hold Python code importing OCP (a case, not an associative array: macOS's
# /bin/bash is 3.2)
dirs_of() {
    case "$1" in
        build123d-0.13.0)     echo "src tests examples docs tools" ;;
        ocpsvg-0.7.0)         echo "ocpsvg tests examples" ;;
        ocp_gordon-0.3.1)     echo "src_py tests examples" ;;
        ocp_tessellate-3.5.3) echo "ocp_tessellate tests examples" ;;
        *) echo "unknown package $1" >&2; exit 1 ;;
    esac
}

rm -rf "${WORK:?}"
mkdir -p "$WORK"
( cd "$WORK" && unzip -q "$SHIM_WHEEL" 'OCP/*' )
for pkg in ocpsvg-0.7.0 ocp_gordon-0.3.1 ocp_tessellate-3.5.3 build123d-0.13.0; do
    tarball="$SDIST/$pkg.tar.gz"
    [ -f "$tarball" ] || { echo "missing $tarball -- run make nanobuild first" >&2; exit 1; }
    tar -xzf "$tarball" -C "$WORK"
    ( cd "$WORK/$pkg"
      dirs=()
      for d in $(dirs_of "$pkg"); do if [ -d "$d" ]; then dirs+=("$d"); fi; done
      "$PY" "$HERE/port.py" "$WORK/OCP" "${dirs[@]}" > "$WORK/$pkg.port.txt"
      "$PY" "$HERE/fix_outargs.py" . > /dev/null
      patch -p1 --forward --quiet --no-backup-if-mismatch < "$HERE/manual/$pkg.patch"
      "$PY" "$HERE/static_names.py" . > /dev/null )
    "$PY" "$HERE/mkpatch.py" "$tarball" "$WORK/$pkg" "$NB/patches/$pkg.patch"
done
echo "patches regenerated; the rewriter's TODO lists are in $WORK/*.port.txt"
