#!/bin/bash
# Build OCCT on Windows with MSVC into deps/occt, mirroring deps/build-occt-macos.sh flag for flag.
#
# The split follows the rule for this project (2026-09-23): **preparation in Git Bash, compilation with MSVC in
# cmd.exe**. Bash locates the toolchain and writes a .bat; cmd.exe runs `vcvars64.bat` and then cmake/ninja. Importing
# vcvars' environment back into bash is possible but unreadable, and a generated .bat is something a reviewer can read
# (it is printed before it runs). Git Bash is what GitHub Actions' windows-latest offers, so this is also the CI path.
#
# Prerequisites, all of which windows-latest already has: Visual Studio (or Build Tools) with the C++ workload, CMake,
# Ninja, Git. Sources: deps/occt-src (deps/fetch-occt-src.sh), deps/freetype-src, and deps/rapidjson from
# deps/fetch-rapidjson.sh. Build FreeType first with deps/build-freetype-windows.sh.
#
# Two builds come out of this script:
# - the one that ships (default): BUILD_OPT_PROFILE=Production into deps/occt, plus the exports of
#   deps/occt-windows-exports.txt, which deps/occt-windows-exports.cmake adds to the toolkits it names
#   (Standard_EXPORT is __declspec(dllexport) on Windows and empty elsewhere, so members OCCT defines without it would
#   otherwise be missing from the DLLs on Windows only). The
#   list is made for one OCCT version, named in its first line; another TAG stops the build here.
# - NANOCCT_OCCT_EXPORT_ALL=1, for `make occt-exports` only: every function exported (CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS)
#   into deps/occt-exportall, the build the bindings are linked against to find what they call. Default profile, because
#   CMake's export-all reads the object files and cannot read Production's /GL ones ("unrecognized file format").
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TAG="$(sed -n 's/^TAG=//p' "$HERE/fetch-occt-src.sh")"
[ "$TAG" != "" ] || { echo "no TAG= line in $HERE/fetch-occt-src.sh" >&2; exit 1; }

for d in occt-src freetype freeimage rapidjson; do
  [ -d "$HERE/$d" ] || { echo "missing $HERE/$d (see the header of this script)" >&2; exit 1; }
done

EXPORTS="$HERE/occt-windows-exports.txt"
case "${NANOCCT_OCCT_EXPORT_ALL:-0}" in
  0)
    NAME=occt PROFILE=Production
    [ -f "$EXPORTS" ] || { echo "missing $EXPORTS" >&2; exit 1; }
    made_for="$(head -n 1 "$EXPORTS")"
    case "$made_for" in
      "# OCCT $TAG "*) ;;
      *) echo "$EXPORTS was made for another OCCT ('$made_for'), this is $TAG -- run 'make occt-exports'" >&2; exit 1 ;;
    esac
    # absolute: OCCT sets cmake_minimum_required(3.10) and no policies, so target_sources resolves a relative path
    # against each toolkit's own directory (CMP0076 OLD)
    HOOK="$(cygpath -m "$HERE/occt-windows-exports.cmake")"
    EXTRA="-D CMAKE_PROJECT_INCLUDE=\"$HOOK\" -D NANOCCT_OCCT_WINDOWS_EXPORTS=\"$(cygpath -m "$EXPORTS")\""
    ;;
  1)
    NAME=occt-exportall PROFILE=Default
    EXTRA="-D CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=ON"
    ;;
  *) echo "NANOCCT_OCCT_EXPORT_ALL is '$NANOCCT_OCCT_EXPORT_ALL': 1 or unset" >&2; exit 1 ;;
esac

W_SRC="$(cygpath -w "$HERE/occt-src")"
W_BUILD="$(cygpath -w "$HERE/$NAME-build")"
W_PREFIX="$(cygpath -w "$HERE/$NAME")"
W_FT="$(cygpath -w "$HERE/freetype")"
W_FI="$(cygpath -w "$HERE/freeimage")"
W_RJ="$(cygpath -w "$HERE/rapidjson")"
BAT="$HERE/_build_occt.bat"

# USE_XLIB is off here because Windows has no X11 (it uses WGL, which USE_OPENGL=ON
# brings in by itself. Everything else matches build-occt-macos.sh exactly, so the two installs are comparable.
# The backticks are escaped because the heredoc below is unquoted (it has to expand $W_* ): unescaped, bash
# runs vswhere itself while generating the .bat and writes an empty `for /f ... in ()`, so VS_PATH is never
# set and the build stops with "no Visual Studio found" (2026-09-24, found by a build from a bare tree).
cat > "$BAT" <<BAT
@echo off
for /f "usebackq delims=" %%i in (\`"%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe" -latest -products * -property installationPath\`) do set "VS_PATH=%%i"
if not defined VS_PATH echo no Visual Studio found & exit /b 1
call "%VS_PATH%\VC\Auxiliary\Build\vcvars64.bat" >nul || exit /b 1
cmake -S "$W_SRC" -B "$W_BUILD" -G Ninja ^
  -D CMAKE_C_COMPILER=cl -D CMAKE_CXX_COMPILER=cl ^
  -D CMAKE_BUILD_TYPE=Release ^
  -D INSTALL_DIR="$W_PREFIX" ^
  -D CMAKE_PREFIX_PATH="$W_FT;$W_RJ" ^
  -D 3RDPARTY_FREETYPE_DIR="$W_FT" ^
  -D 3RDPARTY_FREETYPE_LIBRARY="$W_FT\lib\freetype.lib" ^
  -D 3RDPARTY_FREETYPE_INCLUDE_DIR_ft2build="$W_FT\include\freetype2" ^
  -D 3RDPARTY_FREETYPE_INCLUDE_DIR_freetype2="$W_FT\include\freetype2" ^
  -D 3RDPARTY_FREEIMAGE_DIR="$W_FI" ^
  -D 3RDPARTY_FREEIMAGE_LIBRARY="$W_FI\lib\FreeImage.lib" ^
  -D 3RDPARTY_FREEIMAGE_INCLUDE_DIR="$W_FI\include" ^
  -D 3RDPARTY_RAPIDJSON_DIR="$W_RJ" ^
  -D USE_VTK=OFF -D USE_TBB=OFF -D USE_TK=OFF ^
  -D USE_FREETYPE=ON -D USE_FREEIMAGE=ON -D USE_OPENGL=ON -D USE_GLES2=OFF -D USE_XLIB=OFF ^
  -D USE_RAPIDJSON=ON -D USE_FFMPEG=OFF ^
  -D BUILD_CPP_STANDARD=C++17 ^
  -D BUILD_RELEASE_DISABLE_EXCEPTIONS=OFF ^
  -D BUILD_MODULE_Draw=OFF ^
  -D BUILD_GTEST=OFF ^
  $EXTRA ^
  -D BUILD_OPT_PROFILE=$PROFILE || exit /b 1
ninja -C "$W_BUILD" install || exit /b 1
echo BUILD_OK
BAT

echo "--- generated $BAT ---"
cat "$BAT"
echo "----------------------"
cmd //c "$(cygpath -w "$BAT")"
echo "OCCT installed to $HERE/$NAME"
