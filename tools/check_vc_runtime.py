"""Check that a repaired Windows wheel carries the Visual C++ runtime DLLs of the given folder, with nothing changed but the
names delvewheel gives their dependencies.

    python tools/check_vc_runtime.py <crt-folder> <wheel>...

Run by `make delocate` on Windows after delvewheel, with the folder deps/vc-redist-crt.sh printed. Every DLL in the
wheel's nanocct.libs whose name, without delvewheel's hash suffix, is a file of that folder must be that file
(licenses/Microsoft-VC-Runtime.txt): the check fails if delvewheel took a DLL from elsewhere on PATH -- System32 held
an older one on the GitHub runner -- or changed more than its dependencies' names.

Byte-identical is the normal case (msvcp140.dll imports nothing that is bundled). A runtime DLL that imports another
bundled one -- msvcp140_2.dll imports msvcp140.dll; OCCT 8.0.2's TKG3d needs msvcp140_2.dll for the three-argument
std::hypot -- is rewritten by delvewheel, which renames that dependency to msvcp140-<hash>.dll so that no other copy of
msvcp140.dll in the process is used instead (delvewheel 1.13.1 _dll_utils.replace_needed: the new name in section
padding or a new section, the import descriptor pointing at it, the PE header sizes and checksum, the Authenticode
signature removed). Such a DLL passes when its code is the original's: every executable section byte-identical, the
same exports, and the same imported functions from the same DLLs, where a changed DLL name may only be the mangled name
of a DLL bundled in the same wheel.
msvcp140.dll has to be among them: the modules need it, so a wheel without it is a wrong wheel, not a passing one.
"""
import hashlib
import re
import sys
import zipfile
from pathlib import Path

import pefile

_BUNDLED = re.compile(r"nanocct\.libs/([^/]+?)(-[0-9a-f]{32})?\.dll", flags=re.IGNORECASE)


def _code(pe: pefile.PE) -> dict[bytes, bytes]:
    """The executable sections of a PE file, by name."""
    return {s.Name.rstrip(b"\x00"): s.get_data() for s in pe.sections
            if s.Characteristics & pefile.SECTION_CHARACTERISTICS["IMAGE_SCN_MEM_EXECUTE"] != 0}


def _imports(pe: pefile.PE) -> dict[str, list[bytes]]:
    """Imported functions (name or ordinal) per DLL name, lowercase."""
    return {e.dll.decode().lower(): [i.name if i.name is not None else str(i.ordinal).encode() for i in e.imports]
            for e in getattr(pe, "DIRECTORY_ENTRY_IMPORT", [])}


def _exports(pe: pefile.PE) -> list[tuple]:
    if not hasattr(pe, "DIRECTORY_ENTRY_EXPORT"):
        return []
    return [(s.ordinal, s.name, s.address) for s in pe.DIRECTORY_ENTRY_EXPORT.symbols]


def _same_but_dependency_names(original: bytes, bundled: bytes, mangled: dict[str, str]) -> str:
    """'' when `bundled` is `original` with only dependency names changed by delvewheel, else what differs. `mangled`:
    the bundled file names (lowercase) -> the original DLL name they stand for."""
    a, b = pefile.PE(data=original), pefile.PE(data=bundled)
    if _code(a) != _code(b):
        return "its code differs"
    if _exports(a) != _exports(b):
        return "its exports differ"
    renamed = {mangled.get(dll, dll): funcs for dll, funcs in _imports(b).items()}
    if renamed != _imports(a):
        return "its imports differ beyond delvewheel's renamed dependencies"
    return ""


def main() -> int:
    crt = Path(sys.argv[1])
    originals = {p.name.lower(): p.read_bytes() for p in crt.glob("*.dll")}
    if "msvcp140.dll" not in originals:
        print(f"check_vc_runtime: no msvcp140.dll in {crt}", file=sys.stderr)
        return 1
    failed = False
    for wheel in sys.argv[2:]:
        with zipfile.ZipFile(wheel) as z:
            # every bundled DLL with a hash suffix: its file name -> the name it stands for
            mangled = {f"{m.group(1).lower()}{m.group(2).lower()}.dll": f"{m.group(1).lower()}.dll"
                       for n in z.namelist() if (m := _BUNDLED.fullmatch(n)) is not None and m.group(2) is not None}
            found, identical, renamed = [], [], []
            for name in z.namelist():
                m = _BUNDLED.fullmatch(name)
                if m is None or f"{m.group(1).lower()}.dll" not in originals:
                    continue
                dll = f"{m.group(1).lower()}.dll"
                found.append(dll)
                data = z.read(name)
                if hashlib.sha256(data).digest() == hashlib.sha256(originals[dll]).digest():
                    identical.append(dll)
                    continue
                why = _same_but_dependency_names(originals[dll], data, mangled)
                if why == "":
                    renamed.append(dll)
                else:
                    print(f"check_vc_runtime: {wheel}: {name} differs from {crt / dll}: {why}", file=sys.stderr)
                    failed = True
        if "msvcp140.dll" not in found:
            print(f"check_vc_runtime: {wheel}: no msvcp140.dll in nanocct.libs", file=sys.stderr)
            failed = True
        if len(identical) > 0:
            print(f"check_vc_runtime: {Path(wheel).name}: {', '.join(sorted(identical))} identical to {crt}")
        if len(renamed) > 0:
            print(f"check_vc_runtime: {Path(wheel).name}: {', '.join(sorted(renamed))} as in {crt}, but for the "
                  f"names of bundled dependencies (delvewheel)")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
