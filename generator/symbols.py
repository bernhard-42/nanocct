"""Defined symbols of an OCCT toolkit library, to skip members that a header declares but no library defines
(they would be link errors). Compared by mangled name (libclang's Cursor.mangled_name uses the platform mangling,
so the leading underscore of Darwin symbols matches nm's output), which makes the check overload-aware.
macOS: nm -gU; Linux: nm -D --defined-only; Windows: dumpbin /EXPORTS on the import library (Standard_EXPORT is
__declspec(dllexport), so the .lib export list answers the same question). Design.md 6 R-UNDEFINED."""
from __future__ import annotations

import os
import platform
import shutil
import subprocess
from pathlib import Path


def _dumpbin() -> str | None:
    """MSVC's dumpbin, located through vswhere so the generator does not need a vcvars environment (it runs from Git
    Bash). dumpbin itself starts fine without vcvars -- only its arguments must not be mangled, which subprocess
    avoids by not going through a shell."""
    found = shutil.which("dumpbin")
    if found is not None:
        return found
    vswhere = Path(os.environ.get("ProgramFiles(x86)", "C:/Program Files (x86)")) / "Microsoft Visual Studio/Installer/vswhere.exe"
    if not vswhere.is_file():
        return None
    # -products * : without it vswhere does not report a Build Tools installation
    out = subprocess.run([str(vswhere), "-latest", "-products", "*", "-property", "installationPath"],
                         capture_output=True, text=True).stdout.strip()
    if out == "":
        return None
    hits = sorted((Path(out) / "VC" / "Tools" / "MSVC").glob("*/bin/Hostx64/x64/dumpbin.exe"))
    return str(hits[-1]) if len(hits) > 0 else None


def _windows_library(install: Path, toolkit: str) -> Path | None:
    """<install>/win64/<vcNN>/lib/<TK>.lib -- OCCT's Windows install layout."""
    hits = sorted(install.glob(f"win64/*/lib/{toolkit}.lib"))
    return hits[0] if len(hits) > 0 else None


def unavailable_reason(install: Path, toolkit: str) -> str:
    """Why defined_symbols() returned None -- the causes are different and the message used to claim the first
    for all (a Linux box with only the OCCT *headers* staged said "nm unavailable", 2026-09-23)."""
    if platform.system() == "Windows":
        if _dumpbin() is None:
            return "dumpbin not found (no Visual Studio installation reported by vswhere)"
        return f"{toolkit}.lib not found in {install / 'win64'}"
    if shutil.which("nm") is None:
        return "nm not on PATH"
    return f"lib{toolkit} not found in {install / 'lib'}"


def destructor_defined(mangled: str, symbols: set[str]) -> bool:
    """Is the destructor whose libclang mangling is `mangled` defined in the library?

    Everywhere but Windows this is the plain membership test the other members use. On Windows it cannot be: libclang
    hands out the **vbase destructor** mangling (`??_D`), which is a void-returning member function, while the linker
    wants `??1` -- and the two differ in more than the prefix, because `??1` carries the virtual/access code and no
    return type (`??_DBOPAlgo_Options@@QEAAXXZ` vs the exported `??1BOPAlgo_Options@@UEAA@XZ`). Only the qualified
    *name* is common to both, and MSVC terminates it with `@@`, so that prefix is what is compared. Taking the whole
    symbol instead skipped ~280 classes that link perfectly well, BOPAlgo_Builder among them (2026-09-23)."""
    if platform.system() != "Windows":
        return mangled in symbols
    if not mangled.startswith("??_D"):
        return mangled in symbols
    name, sep, _ = mangled[len("??_D"):].partition("@@")
    if sep == "":
        return mangled in symbols
    prefix = f"??1{name}@@"
    return any(sym.startswith(prefix) for sym in symbols)


def defined_symbols(install: Path, toolkit: str) -> set[str] | None:
    """Mangled names with a definition in lib<toolkit>; None if unavailable."""
    if platform.system() == "Windows":
        dumpbin, lib = _dumpbin(), _windows_library(install, toolkit)
        if dumpbin is None or lib is None:
            return None
        out = subprocess.run([dumpbin, "/EXPORTS", str(lib)], capture_output=True, text=True, check=True).stdout
        symbols: set[str] = set()
        in_exports = False
        for line in out.splitlines():
            stripped = line.strip()
            if stripped == "Exports":
                in_exports = True
                continue
            # the trailing "Summary" block is indented too ("          14 .idata$2"), so it has to end the block
            # explicitly or its section sizes are read as symbol names (they were: "14", 2026-09-23)
            if stripped == "Summary":
                in_exports = False
                continue
            if not in_exports or stripped == "" or stripped.startswith("ordinal"):
                continue
            symbols.add(stripped.split()[0])    # "?Name@@sig (demangled form)": the mangled name is the first token
        return symbols
    nm = shutil.which("nm")
    if nm is None:
        return None
    libs = sorted((install / "lib").glob(f"lib{toolkit}.*")) + sorted((install / "lib").glob(f"lib{toolkit}.so*"))
    libs = [l for l in libs if l.suffix in (".dylib", ".so") or ".so." in l.name]
    if len(libs) == 0:
        return None
    if platform.system() == "Darwin":
        cmd = [nm, "-gU", str(libs[0])]
    else:
        cmd = [nm, "-D", "--defined-only", str(libs[0])]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    symbols: set[str] = set()
    for line in out.splitlines():
        parts = line.split()
        # functions (T, W, t) and, for R-STATIC-DATA, data: S (a Mach-O section), D/d, R/r (read-only), B/b, V (weak object),
        # u (unique global) -- IntPatch_WLineTool::myMaxConcatAngle is `S` on macOS and was missed with functions only
        if len(parts) == 3 and parts[1] in ("T", "W", "t", "S", "s", "D", "d", "R", "r", "B", "b", "V", "u"):
            symbols.add(parts[2])
    return symbols
