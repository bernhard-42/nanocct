#!/bin/bash
# Build FreeType (sources in deps/freetype-src) as a static library with no optional dependencies into deps/freetype,
# with MSVC. The Windows counterpart of deps/build-freetype-macos.sh, same flags; see deps/build-occt-windows.sh for why
# preparation runs in Git Bash and the compile in cmd.exe.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

[ -d "$HERE/freetype-src" ] || { echo "missing $HERE/freetype-src" >&2; exit 1; }
"$HERE/hide-freetype-symbols.sh"        # a no-op for MSVC, but keeps the three builds on one patched source tree

W_SRC="$(cygpath -w "$HERE/freetype-src")"
W_BUILD="$(cygpath -w "$HERE/freetype-build")"
W_PREFIX="$(cygpath -w "$HERE/freetype")"
BAT="$HERE/_build_freetype.bat"

# The backticks are escaped because the heredoc below is unquoted (it has to expand $W_* ): unescaped, bash
# runs vswhere itself while generating the .bat and writes an empty `for /f ... in ()`, so VS_PATH is never
# set and the build stops with "no Visual Studio found" (2026-09-24, found by a build from a bare tree).
cat > "$BAT" <<BAT
@echo off
for /f "usebackq delims=" %%i in (\`"%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe" -latest -products * -property installationPath\`) do set "VS_PATH=%%i"
if not defined VS_PATH echo no Visual Studio found & exit /b 1
call "%VS_PATH%\VC\Auxiliary\Build\vcvars64.bat" >nul || exit /b 1
cmake -S "$W_SRC" -B "$W_BUILD" -G Ninja ^
  -D CMAKE_C_COMPILER=cl ^
  -D CMAKE_BUILD_TYPE=Release ^
  -D CMAKE_INSTALL_PREFIX="$W_PREFIX" ^
  -D CMAKE_POSITION_INDEPENDENT_CODE=ON ^
  -D BUILD_SHARED_LIBS=OFF ^
  -D FT_DISABLE_ZLIB=TRUE -D FT_DISABLE_BZIP2=TRUE -D FT_DISABLE_PNG=TRUE ^
  -D FT_DISABLE_HARFBUZZ=TRUE -D FT_DISABLE_BROTLI=TRUE || exit /b 1
ninja -C "$W_BUILD" install || exit /b 1
echo BUILD_OK
BAT

echo "--- generated $BAT ---"
cat "$BAT"
echo "----------------------"
cmd //c "$(cygpath -w "$BAT")"
test -f "$HERE/freetype/lib/freetype.lib"
echo "FreeType installed to $HERE/freetype (freetype.lib)"
