#!/bin/bash
# Compile the extension modules with MSVC and stage them into stage-win. Bash prepares, cmd.exe builds: MSVC is
# reached by importing vcvars64 in a generated .bat, never through PowerShell (Design.md 7). vswhere needs
# `-products *` because this box has Build Tools rather than a full Visual Studio.
#
# Run this from a real session. Launched from an ssh command, cl.exe fails sporadically with 0xC0000142
# (STATUS_DLL_INIT_FAILED) -- a process-start failure with no error C#### in the log.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
W_ROOT="$(cygpath -w "$ROOT")"
BAT="$ROOT/_build_nanoocp.bat"
cat > "$BAT" <<BAT
@echo off
for /f "usebackq delims=" %%i in (\`"%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe" -latest -products * -property installationPath\`) do set "VS_PATH=%%i"
if not defined VS_PATH echo no Visual Studio found & exit /b 1
call "%VS_PATH%\VC\Auxiliary\Build\vcvars64.bat" >nul || exit /b 1
cmake -S "$W_ROOT" -B "$W_ROOT\build-win" -G Ninja ^
  -D CMAKE_BUILD_TYPE=Release ^
  -D Python_EXECUTABLE="$W_ROOT\.venv\Scripts\python.exe" ^
  -D NANOOCP_OCCT_DIR="$W_ROOT\deps\occt-8.0.1" ^
  -D NANOOCP_RAPIDJSON_DIR="$W_ROOT\deps\rapidjson\include" || exit /b 1
ninja -k 0 -C "$W_ROOT\build-win" || exit /b 1
echo BUILD_OK
BAT
cmd //c "$(cygpath -w "$BAT")"
