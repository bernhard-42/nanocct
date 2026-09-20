"""Defined symbols of an OCCT toolkit library, to skip methods that a header declares but no library
defines (they would be link errors). macOS: nm -gU; Linux: nm -D --defined-only; Windows: not available
(the check is skipped and the linker reports leftovers)."""
from __future__ import annotations

import platform
import re
import shutil
import subprocess
from pathlib import Path

# operator() first: otherwise 'operator' + '(' would match as a plain name and the call operator would be missed
_QUALIFIED_RE = re.compile(r"^((?:[A-Za-z_]\w*::)+)(operator\(\)|~?[A-Za-z_]\w*|operator\S*?)\(")


def defined_methods(install: Path, toolkit: str) -> tuple[set[str], set[str]] | None:
    """('Class::Method' names with at least one definition in lib<toolkit>, full demangled signatures without
    whitespace, e.g. 'GCPnts_DistFunction::GCPnts_DistFunction(GCPnts_DistFunctionconst&)'); None if unavailable."""
    nm = shutil.which("nm")
    if nm is None or platform.system() == "Windows":
        return None
    libs = sorted((install / "lib").glob(f"lib{toolkit}.*")) + sorted((install / "lib").glob(f"lib{toolkit}.so*"))
    libs = [l for l in libs if l.suffix in (".dylib", ".so") or ".so." in l.name]
    if len(libs) == 0:
        return None
    if platform.system() == "Darwin":
        cmd = [nm, "-gU", "--demangle", str(libs[0])]
    else:
        cmd = [nm, "-D", "--defined-only", "-C", str(libs[0])]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    names: set[str] = set()
    signatures: set[str] = set()
    for line in out.splitlines():
        parts = line.split(" ", 2)
        if len(parts) < 3 or parts[1] not in ("T", "W", "t"):
            continue
        m = _QUALIFIED_RE.match(parts[2])
        if m is not None:
            names.add(m.group(1) + m.group(2))
            signatures.add(re.sub(r"\s+", "", parts[2]))
    return names, signatures
