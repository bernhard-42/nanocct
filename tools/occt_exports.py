"""Write deps/occt-windows-exports.txt: the names OCCT's Windows DLLs must export beyond what Standard_EXPORT marks.

    python tools/occt_exports.py exports <export-all OCCT build dir> <binding build dir> <deps/occt-windows-exports.txt>
    python tools/occt_exports.py undefined <src/cpp> <deps/occt-windows-exports.txt>

Run by `make occt-exports` (`exports`) and `make occt-exports-undefined` (`undefined`), on Windows, once per OCCT
release and when the bindings need a name the list does not have. Standard_EXPORT is __declspec(dllexport) on Windows
and empty elsewhere, so a member OCCT defines in a .cxx without it is exported on macOS and Linux but not from the
Windows DLL. deps/occt-windows-exports.cmake turns the [exports] section into a module-definition file per toolkit.

`exports` reads two things from binaries, nothing from the generator:
- what the bindings call: the import tables of the _TK*.pyd built against an OCCT with every function exported
  (deps/build-occt-windows.sh with NANOCCT_OCCT_EXPORT_ALL=1). Members, destructors, vtable slots and the private
  callees of inline members are all imports, so all of them are found, per DLL they resolved to;
- what OCCT exports anyway: the /EXPORT directives dllexport leaves in that build's object files, per toolkit. Measured
  equal, toolkit by toolkit, to the exports of the Production import libraries (OCCT 8.0.2, all 51 toolkits): the
  subtraction needs no Production build, which a new TAG could not have yet.
A data name cannot be exported this way (a client refers to the plain name, a DATA export provides only __imp_): one the
bindings would need stops the tool. The [undefined] section is left empty: `undefined` fills it.

`undefined` writes the R-UNDEFINED lines of the current generation into [undefined]: what Windows still drops with the
list in place (the members OCCT defines nowhere, as on Linux, and a few it does not export that nothing binds).
tests/test_occt_exports.py compares the two on Windows, so a binding that starts to need a name the list lacks fails
the tests there instead of being dropped silently.
"""
from __future__ import annotations

import platform
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from generator import symbols  # noqa: E402  (the generator's dumpbin locator)
from generator.report import read_report  # noqa: E402

_DLL_LINE = re.compile(r"^    (\S+)\.dll$", flags=re.IGNORECASE)
_IMPORT_LINE = re.compile(r"^\s+[0-9A-Fa-f]+\s+(\S+)$")
_BATCH = 150    # object files per dumpbin call: Windows limits a command line to 32 767 characters


def occt_tag() -> str:
    """The OCCT tag deps/fetch-occt-src.sh pins: the one place that sets the version."""
    for line in (ROOT / "deps" / "fetch-occt-src.sh").read_text(encoding="utf-8").splitlines():
        if line.startswith("TAG="):
            return line[len("TAG="):].strip()
    raise SystemExit("no TAG= line in deps/fetch-occt-src.sh")


def read_list(path: Path) -> tuple[str, list[str], list[str]]:
    """(header, [exports] lines, [undefined] lines) of deps/occt-windows-exports.txt."""
    header, sections, current = "", {"exports": [], "undefined": []}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        if header == "":
            header = line
            continue
        if line in ("[exports]", "[undefined]"):
            current = line[1:-1]
            continue
        if line == "" or line.startswith("#"):
            continue
        if current is None:
            raise SystemExit(f"{path}: '{line}' before the first section")
        sections[current].append(line)
    return header, sections["exports"], sections["undefined"]


def write_list(path: Path, exports: list[str], undefined: list[str]) -> None:
    text = [f"# OCCT {occt_tag()} -- written by tools/occt_exports.py (make occt-exports), do not edit",
            "# [exports]: <toolkit> <decorated name>; deps/occt-windows-exports.cmake exports them from that DLL.",
            "# [undefined]: what R-UNDEFINED still drops on Windows with these exports; tests/test_occt_exports.py.",
            "[exports]", *sorted(exports), "[undefined]", *sorted(undefined)]
    path.write_text("\n".join(text) + "\n", encoding="utf-8", newline="\n")


def _dumpbin(*args: str) -> str:
    exe = symbols.dumpbin_path()
    if exe is None:
        raise SystemExit("dumpbin not found (no Visual Studio installation reported by vswhere)")
    return subprocess.run([exe, *args], capture_output=True, text=True, check=True).stdout


def binding_imports(build: Path) -> dict[str, set[str]]:
    """{toolkit: names} the binding modules import from OCCT's DLLs."""
    pyds = sorted(build.rglob("_TK*.pyd"))
    if len(pyds) == 0:
        raise SystemExit(f"no _TK*.pyd under {build}")
    imports: dict[str, set[str]] = defaultdict(set)
    for pyd in pyds:
        dll = None
        for line in _dumpbin("/IMPORTS", str(pyd)).splitlines():
            m = _DLL_LINE.match(line)
            if m is not None:
                dll = m.group(1)
                continue
            if line.strip() == "Summary":
                dll = None
                continue
            if dll is None or not dll.startswith("TK"):
                continue
            entry = _IMPORT_LINE.match(line)
            if entry is not None:
                imports[dll].add(entry.group(1))
    return imports


def occt_exports(occt_build: Path) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    """({toolkit: names its objects mark dllexport}, {toolkit: data names}) of the export-all OCCT build."""
    directed: dict[str, set[str]] = defaultdict(set)
    data: dict[str, set[str]] = defaultdict(set)
    dirs = sorted(occt_build.rglob("TK*.dir"))
    if len(dirs) == 0:
        raise SystemExit(f"no TK*.dir under {occt_build}")
    for d in dirs:
        toolkit = d.name[:-len(".dir")]
        objs = [str(o) for o in sorted(d.rglob("*.obj"))]
        for i in range(0, len(objs), _BATCH):
            for token in _dumpbin("/DIRECTIVES", *objs[i:i + _BATCH]).split():
                if token.startswith("/EXPORT:"):
                    name = token[len("/EXPORT:"):].strip('"')
                    directed[toolkit].add(name.removesuffix(",DATA"))
        # CMake's export-all list marks data with DATA (CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS)
        listing = d / "exports.def"
        if not listing.is_file():
            raise SystemExit(f"{listing} missing: is {occt_build} an export-all build (NANOCCT_OCCT_EXPORT_ALL=1)?")
        for line in listing.read_text(encoding="utf-8", errors="replace").splitlines():
            parts = line.split()
            if len(parts) == 2 and parts[1] == "DATA":
                data[toolkit].add(parts[0])
    return directed, data


def cmd_exports(occt_build: Path, binding_build: Path, out: Path) -> int:
    imports = binding_imports(binding_build)
    directed, data = occt_exports(occt_build)
    lines: list[str] = []
    needed_data: list[str] = []
    for toolkit in sorted(imports):
        if toolkit not in directed:
            raise SystemExit(f"the bindings import from {toolkit}.dll, which {occt_build} did not build")
        for name in sorted(imports[toolkit] - directed[toolkit]):
            if name in data[toolkit]:
                needed_data.append(f"{toolkit} {name}")
            else:
                lines.append(f"{toolkit} {name}")
    if len(needed_data) > 0:
        print("data the bindings import that OCCT does not export -- a .def cannot provide it:", *needed_data,
              sep="\n  ", file=sys.stderr)
        return 1
    write_list(out, lines, [])
    print(f"{out}: {len(lines)} exports in {len({l.split()[0] for l in lines})} toolkits, from "
          f"{sum(len(v) for v in imports.values())} imports; [undefined] empty until `make occt-exports-undefined`")
    return 0


def cmd_undefined(cpp: Path, path: Path) -> int:
    if platform.system() != "Windows":
        raise SystemExit("the [undefined] section is what a Windows generation drops: run this on Windows")
    header, exports, _ = read_list(path)
    if not header.startswith(f"# OCCT {occt_tag()} "):
        raise SystemExit(f"{path} was made for another OCCT ('{header}'): run `make occt-exports` first")
    undefined = sorted(msg for report in sorted(cpp.glob("*/report.txt"))
                       for cat, _, msg in read_report(report) if cat == "undefined")
    if len(undefined) == 0:
        raise SystemExit(f"no R-UNDEFINED lines under {cpp}: run `make generate` first")
    write_list(path, exports, undefined)
    print(f"{path}: {len(undefined)} lines in [undefined]")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) == 4 and argv[0] == "exports":
        return cmd_exports(Path(argv[1]), Path(argv[2]), Path(argv[3]))
    if len(argv) == 3 and argv[0] == "undefined":
        return cmd_undefined(Path(argv[1]), Path(argv[2]))
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
