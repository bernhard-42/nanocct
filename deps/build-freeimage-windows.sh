#!/bin/bash
# Build FreeImage (sources in deps/freeimage-src) as a shared library into deps/freeimage, with MSVC.
# The Windows counterpart of deps/build-freeimage-macos.sh, same codec switches; see deps/build-occt-windows.sh
# for why preparation runs in Git Bash and the compile in cmd.exe.
#
# Shared, for the same reason as the other two platforms: a static FreeImage compiles out the DllMain that
# calls FreeImage_Initialise, and OCCT never calls it, so the plugin list would stay empty and every format
# would be "unsupported" (measured on macOS 2026-09-25, and DllMain is guarded by the same `#ifndef
# FREEIMAGE_LIB`). deps/build-freeimage-macos.sh has the detail.
#
# No visibility flags: MSVC exports from a DLL only what is marked __declspec(dllexport), which under a shared
# build is FreeImage's own DLL_API and nothing else -- the vendored libpng, zlib, libjpeg, libtiff and OpenJPEG
# mark nothing, so they stay internal to FreeImage.dll without any flag. The assertion at the end checks that
# rather than assuming it.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

[ -d "$HERE/freeimage-src" ] || { echo "missing $HERE/freeimage-src -- run deps/fetch-freeimage-src.sh" >&2; exit 1; }

W_SRC="$(cygpath -w "$HERE/freeimage-src")"
W_BUILD="$(cygpath -w "$HERE/freeimage-build")"
W_PREFIX="$(cygpath -w "$HERE/freeimage")"
BAT="$HERE/_build_freeimage.bat"

# The backticks are escaped because the heredoc is unquoted (it has to expand $W_*): unescaped, bash runs
# vswhere itself while generating the .bat and writes an empty `for /f ... in ()`, so VS_PATH is never set --
# the same trap deps/build-freetype-windows.sh documents.
cat > "$BAT" <<BAT
@echo off
for /f "usebackq delims=" %%i in (\`"%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe" -latest -products * -property installationPath\`) do set "VS_PATH=%%i"
if not defined VS_PATH echo no Visual Studio found & exit /b 1
call "%VS_PATH%\VC\Auxiliary\Build\vcvars64.bat" >nul || exit /b 1
cmake -S "$W_SRC" -B "$W_BUILD" -G Ninja ^
  -D CMAKE_C_COMPILER=cl -D CMAKE_CXX_COMPILER=cl ^
  -D CMAKE_BUILD_TYPE=Release ^
  -D CMAKE_INSTALL_PREFIX="$W_PREFIX" ^
  -D CMAKE_POSITION_INDEPENDENT_CODE=ON ^
  -D FREEIMAGE_STATIC=OFF -D BUILD_SHARED_LIBS=ON -D BUILD_TESTS=OFF ^
  -D BUILD_WEBP=OFF -D BUILD_OPENEXR=OFF -D BUILD_LIBRAWLITE=OFF -D BUILD_JXR=OFF || exit /b 1
ninja -C "$W_BUILD" install || exit /b 1
echo BUILD_OK
BAT

echo "--- generated $BAT ---"
cat "$BAT"
echo "----------------------"
cmd //c "$(cygpath -w "$BAT")"

LIB="$HERE/freeimage/lib/FreeImage.lib"
test -f "$LIB"
DLL="$(ls "$HERE"/freeimage/bin/*.dll "$HERE"/freeimage/lib/*.dll 2>/dev/null | head -1 || true)"
if [ -n "$DLL" ]; then
    DUMPBIN="$(ls "$(cygpath -u "$(cmd //c 'for /f "usebackq delims=" %i in (`"%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe" -latest -products * -property installationPath`) do @echo %i' | tr -d '\r')")"/VC/Tools/MSVC/*/bin/Hostx64/x64/dumpbin.exe 2>/dev/null | head -1 || true)"
    if [ -n "$DUMPBIN" ] && [ -x "$DUMPBIN" ]; then
        leaked=$("$DUMPBIN" //EXPORTS "$(cygpath -w "$DLL")" 2>/dev/null | awk '$1 ~ /^[0-9]+$/ {print $NF}' | grep -vE "^FreeImage_" || true)
        if [ -n "$leaked" ]; then
            echo "FreeImage.dll exports non-FreeImage symbols:" >&2
            echo "$leaked" | sed 's/^/  /' | head -20 >&2
            exit 1
        fi
        echo "FreeImage.dll: only FreeImage_* exported"
    else
        echo "WARNING: dumpbin not found, export check skipped" >&2
    fi
fi
echo "FreeImage installed to $HERE/freeimage"
