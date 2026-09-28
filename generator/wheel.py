"""The raw nanocct wheel, packed from the staged tree that `make compile` and `make stubs` produced. Stdlib only.

    python -m generator.wheel <stage-dir> <out-dir> <platform-tag>      e.g. stage-mac dist/unrepaired macosx_11_0_arm64

The build steps each run once: generate -> compile -> stubs -> wheel -> delocate -> test. Until 2026-09-28 the wheel
came from `uv build`, i.e. scikit-build-core, which cannot pack without compiling -- so every binding was compiled a
second time in its own build directory, the most expensive step on the slower CI runners. This packs what is already
built instead: the staged `nanocct/` (the .py and .pyi files, py.typed and the extension modules; `__pycache__` left
out), the metadata from pyproject.toml, the licence files it names (PEP 639), and a RECORD. The result has the files and metadata
of the wheel scikit-build-core made (compared 2026-09-28; only `Requires-Dist` keeps pyproject.toml's spelling,
`numpy>=2,<3` for scikit-build-core's `numpy<3,>=2`); the repair step (delocate, auditwheel, delvewheel) then
bundles the OCCT libraries as before. scikit-build-core stays the build backend for building from source.

The platform tag comes from the Makefile, which knows the platform: macosx_11_0_<arch> (the OCCT build's deployment
target, 11.1, normalises to 11_0), linux_<arch> (auditwheel turns it into manylinux_2_28_<arch>), win_amd64.
"""
from __future__ import annotations

import base64
import hashlib
import sys
import tomllib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _digest(data: bytes) -> str:
    return "sha256=" + base64.urlsafe_b64encode(hashlib.sha256(data).digest()).rstrip(b"=").decode()


def _license_files(patterns: list[str]) -> list[str]:
    """The files the license-files globs of pyproject.toml match, sorted as one list (scikit-build-core's order)."""
    return sorted({path.relative_to(ROOT).as_posix() for pattern in patterns for path in ROOT.glob(pattern) if path.is_file()})


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__, file=sys.stderr)
        return 2
    stage, out_dir, platform_tag = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), sys.argv[3]
    package = stage / "nanocct"
    if not (package / "__init__.py").is_file():
        print(f"wheel: no staged package in {package} -- run make compile and make stubs first", file=sys.stderr)
        return 1

    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text())
    project = pyproject["project"]
    name, version = project["name"], project["version"]
    py_api = pyproject["tool"]["scikit-build"]["wheel"]["py-api"]               # "cp312": the stable ABI floor
    tag = f"{py_api}-abi3-{platform_tag}"
    licenses = _license_files(project["license-files"])

    metadata = ["Metadata-Version: 2.4", f"Name: {name}", f"Version: {version}", f"Summary: {project['description']}",
                f"License-Expression: {project['license']}"]
    metadata += [f"License-File: {rel}" for rel in licenses]
    metadata += [f"Requires-Python: {project['requires-python']}"]
    metadata += [f"Requires-Dist: {dep}" for dep in project["dependencies"]]
    wheel = ["Wheel-Version: 1.0", "Generator: nanocct generator/wheel.py", "Root-Is-Purelib: false", f"Tag: {tag}"]

    info = f"{name}-{version}.dist-info"
    files: list[tuple[str, Path | None, bytes]] = []                       # (path in the wheel, source file, content)
    for path in sorted(package.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
            files.append((path.relative_to(stage).as_posix(), path, path.read_bytes()))
    files += [(f"{info}/licenses/{rel}", ROOT / rel, (ROOT / rel).read_bytes()) for rel in licenses]
    files += [(f"{info}/METADATA", None, ("\n".join(metadata) + "\n").encode()),
              (f"{info}/WHEEL", None, ("\n".join(wheel) + "\n").encode())]
    record = "".join(f"{arc},{_digest(data)},{len(data)}\n" for arc, _, data in files) + f"{info}/RECORD,,\n"

    out_dir.mkdir(parents=True, exist_ok=True)
    whl = out_dir / f"{name}-{version}-{tag}.whl"
    with zipfile.ZipFile(whl, "w", zipfile.ZIP_DEFLATED) as z:
        for arc, source, data in files:
            if source is None:
                z.writestr(arc, data)
            else:
                entry = zipfile.ZipInfo.from_file(source, arc)                 # keeps the file mode (and mtime)
                entry.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(entry, data)
        z.writestr(f"{info}/RECORD", record)
    print(f"{whl} ({whl.stat().st_size // (1024 * 1024)} MB, {len(files) + 1} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
