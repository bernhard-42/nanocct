"""Defined symbols of an OCCT toolkit library, to skip members that a header declares but no library defines
(they would be link errors). Compared by mangled name (libclang's Cursor.mangled_name uses the platform mangling,
so the leading underscore of Darwin symbols matches nm's output), which makes the check overload-aware.
macOS: nm -gU; Linux: nm -D --defined-only (unverified); Windows: not available (the check is skipped and the linker
reports leftovers). Design.md 6 R-UNDEFINED."""
from __future__ import annotations

import platform
import shutil
import subprocess
from pathlib import Path


def defined_symbols(install: Path, toolkit: str) -> set[str] | None:
    """Mangled names with a definition in lib<toolkit>; None if unavailable."""
    nm = shutil.which("nm")
    if nm is None or platform.system() == "Windows":
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
        if len(parts) == 3 and parts[1] in ("T", "W", "t"):
            symbols.add(parts[2])
    return symbols
