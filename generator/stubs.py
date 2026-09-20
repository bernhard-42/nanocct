"""Type stubs: nanobind's stubgen for every generated package module (run after the build, it imports the
extension), plus the generic NCollection container classes so that NCollection_Array1[gp_Pnt] type-checks.

    python -m generator.stubs
"""
from __future__ import annotations

import ast
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "nanoocp"
GENERIC = ROOT / "generator" / "stubs"

_SCALARS = {"double": "float", "int": "int", "bool": "bool", "std::string": "str"}


def _type_arg(arg: str, classes: dict[str, str], templates: dict[str, dict]) -> str | None:
    """Stub spelling of a template argument: float for double, nanoocp.<pkg>.X for a class or handle<X>,
    the bound class for a nested instantiation."""
    if arg in _SCALARS:
        return _SCALARS[arg]
    m = re.match(r"(?:opencascade::)?handle<(.+)>$", arg)
    if m is not None:
        arg = m.group(1)
    if arg in classes:
        return f"nanoocp.{classes[arg]}.{arg}"
    inst = templates.get(arg)
    if inst is not None:
        return f"nanoocp.{inst['package']}.{inst['name']}"
    return None


def _generic_spelling(concrete: str, templates: dict[str, dict]) -> str:
    """nanoocp.NCollection.NCollection_Map__int -> NCollection_Map[int] (what NCollection_Map[int] denotes statically)."""
    name = concrete.rsplit(".", 1)[-1]
    for key, inst in templates.items():
        if inst.get("name") == name:
            kind, args = re.match(r"(\w+)<(.+)>$", key).groups()
            return f"{kind}[{', '.join(_stub_arg(a, templates) for a in _split_args(args))}]"
    return concrete


def _stub_arg(arg: str, templates: dict[str, dict]) -> str:
    manifest = json.loads((ROOT / "src" / "cpp" / "manifest.json").read_text())
    return _type_arg(arg, manifest["classes"], templates) or arg


def _split_args(text: str) -> list[str]:
    out, depth, cur = [], 0, ""
    for ch in text:
        depth += ch == "<"
        depth -= ch == ">"
        if ch == "," and depth == 0:
            out.append(cur.strip()); cur = ""
        else:
            cur += ch
    out.append(cur.strip())
    return out


def _replace_class_block(text: str, name: str, replacement: str) -> str:
    """Replace the top-level `class name...` block (up to the next top-level statement) in a stub."""
    m = re.search(rf"^class {re.escape(name)}\b.*?(?=^\S|\Z)", text, re.S | re.M)
    if m is None:
        return text
    return text[:m.start()] + replacement + "\n" + text[m.end():]


def _aliases_of(shim: Path) -> dict[str, tuple[str, str]]:
    """The _ALIASES table of a generated shim module (parsed, not imported)."""
    for node in ast.parse(shim.read_text()).body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "_ALIASES" for t in node.targets):
            return ast.literal_eval(node.value)
    return {}


def main() -> int:
    manifest = json.loads((ROOT / "src" / "cpp" / "manifest.json").read_text())
    classes, templates = manifest["classes"], manifest["templates"]
    toolkit_of = {}
    for pkg_file in SRC.glob("*.py"):
        m = re.search(r"from nanoocp\._(\w+) import (\w+) as _ext", pkg_file.read_text())
        if m is not None:
            toolkit_of[m.group(2)] = m.group(1)
    for pkg, tk in sorted(toolkit_of.items()):
        out = SRC / f"{pkg}.pyi"
        subprocess.run([sys.executable, "-m", "nanobind.stubgen", "-m", f"nanoocp._{tk}.{pkg}", "-o", str(out), "-q"],
                       check=True, cwd="/")
        print(f"stub {out.relative_to(ROOT)}", file=sys.stderr)
    # deprecated typedef aliases (shim _ALIASES tables) -> explicit assignments in the stubs; alias-only
    # modules (e.g. TColgp) get a stub of their own
    for shim in sorted(SRC.glob("*.py")):
        if shim.name.startswith("_"):
            continue
        aliases = _aliases_of(shim)
        if len(aliases) == 0:
            continue
        out = SRC / f"{shim.stem}.pyi"
        modules = sorted({mod for mod, _ in aliases.values()})
        block = "\n# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)\n" + "".join(
            f"import {mod}\n" for mod in modules) + "".join(
            f"{alias} = {mod}.{name}\n" for alias, (mod, name) in sorted(aliases.items()))
        text = out.read_text() if out.exists() else f'"""{shim.stem}: OCCT pre-8.0 typedef names."""\n'
        out.write_text(text.rstrip("\n") + "\n" + block)

    # NCollection: generic container classes + instantiations as their subclasses
    nc = SRC / "NCollection.pyi"
    text = nc.read_text()
    generic_parts = []
    kinds = sorted({re.match(r"(\w+)<", key).group(1) for key, inst in templates.items() if not inst.get("skipped", False)})
    for kind in kinds:
        g = GENERIC / f"{kind}.pyi"
        if kind == "NCollection_Shared":
            # NCollection_Shared<T> derives from T, which Generic[_T] cannot express: type the accessor with
            # one overload per bound instantiation, returning the concrete class (which derives from T's class)
            lines = ["class _NCollection_Shared_template:",
                     '    """NCollection_Shared[T] -> the bound NCollection_Shared<T> class (derives from T)."""']
            for key, inst in sorted(templates.items()):
                if inst.get("skipped", False) or not key.startswith("NCollection_Shared<"):
                    continue
                wrapped = _type_arg(_split_args(key[len("NCollection_Shared<"):-1])[0], classes, templates)
                if wrapped is None:
                    continue
                generic_wrapped = _generic_spelling(wrapped, templates)
                lines += ["    @overload", f"    def __getitem__(self, item: type[{generic_wrapped}]) -> type[{inst['name']}]: ..."]
            lines += ["    @overload", "    def __getitem__(self, item: type) -> type: ...", "",
                      "NCollection_Shared: _NCollection_Shared_template", ""]
            generic_parts.append("\n".join(lines) + "\n")
        elif g.exists():
            generic_parts.append(g.read_text().rstrip() + "\n")
        else:
            print(f"warning: no generic stub for {kind} (generator/stubs/{kind}.pyi)", file=sys.stderr)
    for key, inst in sorted(templates.items()):
        if inst.get("skipped", False):
            continue
        kind, args = re.match(r"(\w+)<(.+)>$", key).groups()
        spelled = [_type_arg(a, classes, templates) for a in _split_args(args)]
        if any(sp is None for sp in spelled) or not (GENERIC / f"{kind}.pyi").exists():
            continue
        bases = f"{kind}[{', '.join(spelled)}]"
        if kind == "NCollection_Shared":                 # NCollection_Shared<T> derives from T (+ Transient members)
            bases = f"{spelled[0]}, _NCollection_Shared_members"
        text = _replace_class_block(text, inst["name"], f"class {inst['name']}({bases}): ...")
    header = ("from typing import Generic, Self, TypeVar, overload\nfrom collections.abc import Iterator\n"
              "import nanoocp.Standard\n\n_T = TypeVar('_T')\n_K = TypeVar('_K')\n_V = TypeVar('_V')\n\n")
    header += (GENERIC / "NCollection_Shared.pyi").read_text().replace("class NCollection_Shared(Generic[_T]):", "class _NCollection_Shared_members:").replace(
        "    def __init__(self, theOther: _T) -> None: ...", "    def __init__(self, theOther: object) -> None: ...") + "\n"
    nc.write_text(header + "".join(generic_parts) + "\n" + text)
    (SRC / "py.typed").write_text("")
    print("NCollection.pyi: generic classes for", ", ".join(kinds), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
