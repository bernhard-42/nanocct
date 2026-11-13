"""Check that a repaired Windows wheel carries the Visual C++ runtime DLLs of the given folder, byte for byte.

    python tools/check_vc_runtime.py <crt-folder> <wheel>...

Run by `make delocate` on Windows after delvewheel, with the folder deps/vc-redist-crt.sh printed. Every DLL in the
wheel's nanocct.libs whose name, without delvewheel's hash suffix, is a file of that folder must have that file's
SHA-256: the redistribution right is for the unmodified file (licenses/Microsoft-VC-Runtime.txt), and the check fails
if delvewheel took a DLL from elsewhere on PATH -- System32 held an older one on the GitHub runner -- or changed it.
msvcp140.dll has to be among them: the modules need it, so a wheel without it is a wrong wheel, not a passing one.
"""
import hashlib
import re
import sys
import zipfile
from pathlib import Path


def main() -> int:
    crt = Path(sys.argv[1])
    originals = {p.name.lower(): hashlib.sha256(p.read_bytes()).hexdigest() for p in crt.glob("*.dll")}
    if "msvcp140.dll" not in originals:
        print(f"check_vc_runtime: no msvcp140.dll in {crt}", file=sys.stderr)
        return 1
    failed = False
    for wheel in sys.argv[2:]:
        with zipfile.ZipFile(wheel) as z:
            found, identical = [], []
            for name in z.namelist():
                m = re.fullmatch(r"nanocct\.libs/([^/]+?)(-[0-9a-f]{32})?\.dll", name, flags=re.IGNORECASE)
                if m is None or f"{m.group(1).lower()}.dll" not in originals:
                    continue
                dll = f"{m.group(1).lower()}.dll"
                found.append(dll)
                if hashlib.sha256(z.read(name)).hexdigest() == originals[dll]:
                    identical.append(dll)
                else:
                    print(f"check_vc_runtime: {wheel}: {name} differs from {crt / dll}", file=sys.stderr)
                    failed = True
        if "msvcp140.dll" not in found:
            print(f"check_vc_runtime: {wheel}: no msvcp140.dll in nanocct.libs", file=sys.stderr)
            failed = True
        if len(identical) > 0:
            print(f"check_vc_runtime: {Path(wheel).name}: {', '.join(sorted(identical))} identical to {crt}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
