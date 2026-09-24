#!/bin/bash
# Keep FreeType's API out of the library OCCT links it into (Design.md 3.2).
#
# FreeType is linked statically into libTKService, and libTKService re-exported 151 of its FT_* symbols (155 in the
# manylinux build, measured 2026-09-24). ELF has one flat namespace, so a process that also loads another FreeType --
# matplotlib, Pillow and Qt all bundle one -- can bind OCCT's calls to that one instead, which is the problem
# CadQuery/ocp-build-system#54 is about.
#
# FreeType already builds with C_VISIBILITY_PRESET hidden (its CMakeLists.txt), but each of its 226 FT_EXPORT
# declarations carries an explicit visibility("default") that overrides the preset. The macro cannot be redefined
# from the command line: the gcc/clang branch of public-macros.h defines FT_PUBLIC_FUNCTION_ATTRIBUTE
# unconditionally, so a -D loses to the header (clang says "macro redefined" and keeps the header's). The `#ifndef`
# further down is only the fallback for compilers the branch does not know. So the attribute itself is patched.
#
# MSVC needs nothing: its branch only says dllexport under DLL_EXPORT, which a static build does not define.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MACROS="${1:-$HERE/freetype-src}/include/freetype/config/public-macros.h"
[ -f "$MACROS" ] || { echo "hide-freetype-symbols: no $MACROS" >&2; exit 1; }
if grep -q 'visibility( "default" )' "$MACROS"; then
    sed -i.bak 's/visibility( "default" )/visibility( "hidden" )/' "$MACROS"   # -i.bak: BSD and GNU sed alike
    rm -f "$MACROS.bak"
    echo "hide-freetype-symbols: patched $MACROS"
else
    echo "hide-freetype-symbols: already patched"
fi
grep -q 'visibility( "hidden" )' "$MACROS" || { echo "hide-freetype-symbols: patch did not apply" >&2; exit 1; }
