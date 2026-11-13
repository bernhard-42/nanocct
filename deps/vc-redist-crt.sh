#!/bin/bash
# Print the folder of the Visual C++ runtime DLLs (msvcp140.dll & co.) of the Visual Studio that builds the wheel, as a
# Windows path for `delvewheel repair --add-path` (Makefile, target delocate).
#
# Why this folder: it is the one Visual Studio's licence lets a licensed user redistribute, unmodified, as
# "Distributable Code" ([VisualStudioFolder]\VC\redist, https://aka.ms/vs/18/redistribution). The copy in System32
# comes with the installed runtime, whose own licence forbids distributing it, and on the GitHub runner it is also older
# than the toolset that compiled the modules (14.40 against 14.51). licenses/Microsoft-VC-Runtime.txt says the rest.
#
# The same Visual Studio as the compile: vswhere -latest -products *, as deps/build-nanocct-windows.sh finds it, and the
# runtime version that Visual Studio names as its default (VC\Auxiliary\Build\Microsoft.VCRedistVersion.default.txt).
set -euo pipefail

# vswhere called directly: `cmd //c 'for /f ...'` gets its quotes escaped by Git Bash ("usebackq delims=" was unexpected
# at this time). ProgramFiles(x86) through printenv, as bash cannot expand a variable name with parentheses.
vswhere="$(cygpath -u "$(printenv 'ProgramFiles(x86)')")/Microsoft Visual Studio/Installer/vswhere.exe"
vs="$("$vswhere" -latest -products '*' -property installationPath | tr -d '\r')"
if [ "$vs" = "" ]; then
    echo "vc-redist-crt: vswhere found no Visual Studio" >&2
    exit 1
fi
vs="$(cygpath -u "$vs")"
version_file="$vs/VC/Auxiliary/Build/Microsoft.VCRedistVersion.default.txt"
if [ ! -f "$version_file" ]; then
    echo "vc-redist-crt: no $version_file -- is the C++ workload installed?" >&2
    exit 1
fi
version="$(tr -d '\r\n ' < "$version_file")"

shopt -s nullglob
crt=("$vs/VC/Redist/MSVC/$version/x64/"Microsoft.VC*.CRT)
if [ "${#crt[@]}" -ne 1 ] || [ ! -f "${crt[0]}/msvcp140.dll" ]; then
    echo "vc-redist-crt: expected one $vs/VC/Redist/MSVC/$version/x64/Microsoft.VC*.CRT with msvcp140.dll, found ${#crt[@]}" >&2
    exit 1
fi
cygpath -w "${crt[0]}"
