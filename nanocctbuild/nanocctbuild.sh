#!/bin/bash
# Fetch build123d and the three packages it builds on as sdists from PyPI, verify each against its sha256, and apply
# the nanocct patch from nanocctbuild/patches: the result is four source trees that import nanocct instead of OCP.
#
#   make nanocctbuild                       (or: nanocctbuild/nanocctbuild.sh)
#   uv venv -p 3.14 /path/to/venv
#   VIRTUAL_ENV=/path/to/venv uv pip install dist/nanocct-*.whl build/nanocctbuild/src/*
#
# The patches carry the port (imports, OCP's `_s` statics, out-parameters that nanocct returns, streams, the
# dependency on nanocct instead of cadquery-ocp-novtk / cadquery-ocp-proxy), including each package's own tests,
# so every tree can run its suite against nanocct. The trees are rebuilt from the verified sdist on every run.
#
# nanocctbuild/patches/<pkg>.patch is the one complete patch per package, and the only thing applied here. It is generated
# by nanocctbuild/tools/regen.sh -- edit nanocctbuild/tools/manual/<pkg>.patch (the hand-made part, an input), never patches/.
# nanocctbuild/tools/files/<pkg>/ holds files the sdist lacks and a text patch cannot carry (ocp_tessellate's test image,
# from its git repository); they are copied over the patched tree as they are.
#
# How a patch is made (nanocctbuild/tools, each with its usage in the docstring): tools/port.py does the mechanical part
# from the shim's name map and lists the rest as TODOs, tools/fix_outargs.py the ignored BRep_Tool out-arguments;
# tools/trace_shim.py records the call sites the shim adapts while the package's suite runs through it; the rest is
# hand work driven by native test runs. tools/mkpatch.py writes the patch, tools/junit_cmp.py checks parity against
# the real OCP test by test (run serially).
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(dirname "$HERE")"

# name-version  sha256  url   (PyPI's own digests, https://pypi.org/pypi/<name>/<version>/json)
PACKAGES=(
    "ocpsvg-0.7.0 e8a03495e873943398df61e1cd02bd0d6f0f206665a2c9f86430b75bd2ecc152 https://files.pythonhosted.org/packages/77/93/6731a317aca67604914e69f4d92d544c5637c89d8fd54e5dde9ddbc93561/ocpsvg-0.7.0.tar.gz"
    "ocp_gordon-0.3.1 e55e695fd421e4dc10fe91636e7f2fa376ad81572faaf74e7bbed4b78c7918b7 https://files.pythonhosted.org/packages/35/b2/66ed6601660648ad5bf84a571460cd57e9db4b28c6833c55e229211a418d/ocp_gordon-0.3.1.tar.gz"
    "ocp_tessellate-3.5.3 3f627da7099cd078081432b26db179b7f225241d1ca9474ce959e714f6cac564 https://files.pythonhosted.org/packages/ef/59/f5affe69a54587413b03b22020b0353fba1b4aeb3a281912eb6eaeef9347/ocp_tessellate-3.5.3.tar.gz"
    "build123d-0.13.0 97c5577a777ff7219714b10f70f253c7109e84bb3ec621eea5d4597b4c7656b4 https://files.pythonhosted.org/packages/4b/6c/47b531b579d5238e4627b5113375d8f7a7145a24b3447413be318422ee71/build123d-0.13.0.tar.gz"
)

OUT="$ROOT/build/nanocctbuild"
SDIST="$OUT/sdist"
SRC="$OUT/src"

# the rm -rf below is built from $ROOT: refuse to run if that is not an nanocct checkout
[ -f "$ROOT/generator/__main__.py" ] && [ -f "$HERE/nanocctbuild.sh" ] || { echo "not an nanocct checkout: $ROOT" >&2; exit 1; }

mkdir -p "$SDIST" "$SRC"
for entry in "${PACKAGES[@]}"; do
    read -r pkg sha url <<< "$entry"
    tarball="$SDIST/$pkg.tar.gz"
    patch_file="$HERE/patches/$pkg.patch"
    [ -f "$patch_file" ] || { echo "missing patch: $patch_file" >&2; exit 1; }
    [ -f "$tarball" ] || curl -fsSL -o "$tarball" "$url"
    echo "$sha  $tarball" | shasum -a 256 -c -

    rm -rf "${SRC:?}/$pkg"
    tar -xzf "$tarball" -C "$SRC"
    [ -d "$SRC/$pkg" ] || { echo "$tarball did not unpack to $pkg" >&2; exit 1; }
    patch -p1 --forward --quiet -d "$SRC/$pkg" < "$patch_file"
    if grep -rqE '^\s*(from OCP[. ]|import OCP([. ,]|$))' --include='*.py' "$SRC/$pkg"; then
        echo "$pkg still imports OCP after patching:" >&2
        grep -rnE '^\s*(from OCP[. ]|import OCP([. ,]|$))' --include='*.py' "$SRC/$pkg" >&2
        exit 1
    fi
    # files the sdist lacks and a text patch cannot carry (ocp_tessellate's test image), copied over the tree as they are
    if [ -d "$HERE/tools/files/$pkg" ]; then
        cp -R "$HERE/tools/files/$pkg/." "$SRC/$pkg/"
        echo "$pkg: added $(find "$HERE/tools/files/$pkg" -type f | wc -l | tr -d ' ') file(s) from tools/files/$pkg"
    fi
    echo "$pkg: patched ($(grep -c '^+++ ' "$patch_file") files) -> $SRC/$pkg"
done
