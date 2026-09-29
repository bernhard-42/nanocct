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
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from .binders import BINDERS
from .parallel import jobs_from_env
from .parse import py_path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "nanocct"
GENERIC = ROOT / "generator" / "stubs"

_SCALARS = {"double": "float", "int": "int", "bool": "bool", "std::string": "str"}
_MANIFEST: dict = json.loads((ROOT / "src" / "cpp" / "manifest.json").read_text())   # read once (was re-read per call)
_PATHS: dict[str, str] = _MANIFEST.get("paths", {})
_CLASSES: dict[str, str] = _MANIFEST["classes"]


def _type_arg(arg: str, classes: dict[str, str], templates: dict[str, dict]) -> str | None:
    """Stub spelling of a template argument: float for double, nanocct.<pkg>.X for a class or handle<X>,
    the bound class for a nested instantiation."""
    if arg in _SCALARS:
        return _SCALARS[arg]
    m = re.match(r"(?:opencascade::)?handle<(.+)>$", arg)
    if m is not None:
        arg = m.group(1)
    inst = templates.get(arg)                    # template instantiations first: their Python name is the alias
    if inst is not None and not inst.get("skipped", False):
        return f"nanocct.{inst['package']}.{inst['name']}"
    if arg in classes and "<" not in arg:
        return f"nanocct.{classes[arg]}.{py_path(arg, classes[arg], _PATHS)}"
    return None


def _generic_spelling(concrete: str, templates: dict[str, dict]) -> str:
    """nanocct.NCollection.NCollection_Map__int -> NCollection_Map[int] (what NCollection_Map[int] denotes statically)."""
    name = concrete.rsplit(".", 1)[-1]
    for key, inst in templates.items():
        if inst.get("name") == name:
            kind, args = re.match(r"([\w:]+)<(.*)>$", key).groups()
            if kind not in BINDERS:            # a 6c instantiation (NCollection_EBTree<int, Bnd_Box2d>): no generic class, the concrete one is the type
                return concrete
            return f"{kind}[{', '.join(_stub_arg(a, templates) for a in _split_args(args))}]"
    return concrete


def _generic_or_none(name: str, templates: dict[str, dict]) -> str | None:
    """NCollection_Map[int] for a concrete instantiation name whose every argument has a stub spelling; None when an
    argument is not bound (NCollection_Array1<BRepGraph_NodeId::Typed<...>>: the concrete class stays)."""
    for key, inst in templates.items():
        if inst.get("name") == name:
            kind, args = re.match(r"([\w:]+)<(.*)>$", key).groups()
            spelled = [_type_arg(a, _CLASSES, templates) for a in _split_args(args)]
            if any(sp is None for sp in spelled):
                return None
            return f"{kind}[{', '.join(spelled)}]"    # type: ignore[arg-type]
    return None


def _stub_arg(arg: str, templates: dict[str, dict]) -> str:
    return _type_arg(arg, _CLASSES, templates) or arg


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


def _unhashable_ignore(text: str) -> str:
    """R-UNHASHABLE: stubgen writes `__hash__: None = None` for the nb::none() attribute. mypy rejects that as an
    incompatible override of object.__hash__ -- and rejects `ClassVar[None]` and a `-> None` method just the same --
    so the line needs the suppression typeshed itself puts on every unhashable class in builtins.pyi. ty accepts all
    the spellings; keeping stubgen's own avoids having to add a typing import to every stub that has one."""
    return re.sub(r"^(\s*__hash__: None = None)$", r"\1  # type: ignore[assignment]", text, flags=re.M)


def _with_imports(text: str) -> str:
    """Add `import nanocct.<pkg>` for every nanocct.<pkg>.X reference the generic spellings introduced."""
    used = set(re.findall(r"\bnanocct\.(\w+)\.", text))
    imported = set(re.findall(r"^import nanocct\.(\w+)$", text, re.M)) | set(re.findall(r"^from nanocct\.(\w+) import", text, re.M))
    missing = sorted(used - imported)
    if len(missing) == 0:
        return text
    lines = text.splitlines(keepends=True)
    anchors = [i for i, line in enumerate(lines) if line.startswith("import nanocct.")]
    if len(anchors) > 0:
        at = anchors[-1] + 1
    else:                                     # after the module docstring (first line) and a blank
        at = 1
        while at < len(lines) and lines[at].strip() != "":
            at += 1
        at += 1
    lines[at:at] = [f"import nanocct.{m}\n" for m in missing]
    return "".join(lines)


def _with_numpy_imports(text: str) -> str:
    """Add the numpy imports a hand-written `nb::sig` needs.

    nanobind's stubgen adds `import numpy` / `from numpy.typing import NDArray` for the signatures it infers
    itself, but not for the ones given as a literal `nb::sig` string -- and the zero-copy accessors that can
    return None have to give theirs by hand, because their C++ return type is `nb::object` (R-VIEW). Without
    this, Image.pyi says `-> NDArray | None` with nothing importing NDArray.
    """
    add = []
    if re.search(r"\bNDArray\b", text) and "from numpy.typing import NDArray" not in text:
        add.append("from numpy.typing import NDArray\n")
    if re.search(r"\bnumpy\.", text) and re.search(r"^import numpy$", text, re.M) is None:
        add.insert(0, "import numpy\n")

    typing_import = re.search(r"^from typing import (.+)$", text, re.M)
    if "Annotated[" in text and typing_import is not None and "Annotated" not in typing_import.group(1).split(", "):
        names = sorted({*typing_import.group(1).split(", "), "Annotated"}, key=str.lower)
        text = text[:typing_import.start()] + "from typing import " + ", ".join(names) + text[typing_import.end():]
    if len(add) == 0:
        return text

    lines = text.splitlines(keepends=True)
    at = next((i for i, line in enumerate(lines) if line.startswith("import nanocct.")), None)
    if at is None:                            # no nanocct imports: after the docstring and its blank line
        at = 1
        while at < len(lines) and lines[at].strip() != "":
            at += 1
        at += 1
    else:                                     # nanobind's own place, with a blank line before the block
        add.append("\n")
    lines[at:at] = add
    return "".join(lines)


def _view_accessor(text: str, name: str) -> str | None:
    """The `__array__` member stubgen generated for a concrete container class, if it has one, docstring included.

    The zero-copy view (R-VIEW) exists only for element types that are a packed run of numpy scalars, and its
    dtype is that scalar -- so it cannot live on the generic `NCollection_Array1(Generic[_T])` stub, which would
    promise it for an array of TopoDS_Shape too. Everything else about a concrete class collapses into the
    generic base; this one member is lifted out first, which keeps the exact dtype without a second copy of the
    element table that `src/cpp/common/nanocct_elem_view.h` already holds.
    """
    m = re.search(rf"^class {re.escape(name)}\b.*?(?=^\S|\Z)", text, re.S | re.M)
    if m is None:
        return None
    member = re.search(r"^    def __array__\(.*?(?=^    \S|^\S|\Z)", m.group(0), re.S | re.M)
    return None if member is None else member.group(0).rstrip()


def _replace_class_block(text: str, name: str, replacement: str) -> str:
    """Replace the top-level `class name...` block (up to the next top-level statement) in a stub."""
    m = re.search(rf"^class {re.escape(name)}\b.*?(?=^\S|\Z)", text, re.S | re.M)
    if m is None:
        return text
    return text[:m.start()] + replacement + "\n" + text[m.end():]


def _shims() -> list[Path]:
    """nanocct/<pkg>.py, or nanocct/<pkg>/__init__.py for a package with C++ namespaces (Python sub-packages)."""
    return sorted([p for p in SRC.glob("*.py") if not p.name.startswith("_")] + list(SRC.glob("*/__init__.py")))


def _stub_of(shim: Path) -> Path:
    return shim.with_suffix(".pyi")


_STUBGEN = r"""
import re, sys, importlib
from pathlib import Path
from nanobind.stubgen import StubGen
# A stub must name every type a signature mentions, including types other toolkits register -- and since
# nanocct/__init__.py stopped importing eagerly (Design.md 6a) nothing else pulls them in, so a cross-toolkit
# parameter would render as a bare name instead of nanocct.<pkg>.<Class>. Load every toolkit first: stub
# generation is the one place that deliberately wants all of them.
import nanocct
for _tk in sys.argv[3].split(","):
    importlib.import_module("nanocct._" + _tk)
mod = importlib.import_module(sys.argv[1])
out = Path(sys.argv[2])
sg = StubGen(module=mod, recursive=True, quiet=True, output_file=out)   # recursive: C++ namespaces are submodules
sg.put(mod)
text = sg.get()
# stubgen binds an imported class as "from nanocct.GC import GC_MakeSegment2d as GCE2d_MakeSegment", which a stub
# does not re-export (typing spec: only the `X as X` form does; ty enforces it), and by __name__, which is wrong for
# a nested class (using CurveD1 = Geom_Curve::ResD1): re-bind such aliases as assignments by module + __qualname__
fixes = []
for name, value in vars(mod).items():
    if isinstance(value, type) and value.__module__ != mod.__name__ and name != value.__qualname__:
        # stubgen writes the import on one line when it fits in 70 characters, else as a parenthesised block
        # (nanobind stubgen.py: `items_v0 if len(items_v0) <= 70 else items_v1`), so both layouts occur
        text, n = re.subn(rf"^    {re.escape(value.__name__)} as {re.escape(name)},?\n", "", text, flags=re.M)
        if n == 0:
            item = f"{value.__name__} as {name}"
            one_line = re.search(rf"^from {re.escape(value.__module__)} import (?!\()(.+)\n", text, flags=re.M)
            if one_line is not None and item in one_line.group(1).split(", "):
                rest = [i for i in one_line.group(1).split(", ") if i != item]
                # nothing left: leave the empty block the wrapped case leaves, so the step below handles both alike
                kept = f"from {value.__module__} import {', '.join(rest)}\n" if len(rest) > 0 else f"from {value.__module__} import (\n)\n"
                text = text[:one_line.start()] + kept + text[one_line.end():]
                n = 1
        if n > 0:
            fixes.append(f"{name} = {value.__module__}.{value.__qualname__}\n")
            have = re.search(rf"^import {re.escape(value.__module__)}$", text, flags=re.M) is not None
            text = re.sub(rf"^from {re.escape(value.__module__)} import \(\n\)\n", "" if have else f"import {value.__module__}\n", text, flags=re.M)
if len(fixes) > 0:
    text = text.rstrip("\n") + "\n\n# C++ typedef aliases\n" + "".join(fixes)
out.write_text(text)
"""


_ALL_TOOLKITS = ",".join(sorted({tk for tk, _ in _MANIFEST.get("packages", {}).items()} and
                                 set(_MANIFEST.get("packages", {}).values())))


def _stubgen(module: str, out: Path) -> None:
    """nanobind's stubgen through its API: the CLI needs a module __file__ for recursive mode, extension submodules
    have none. The stub of a namespace submodule lands next to out (<pkg>/__init__.pyi + <pkg>/<Namespace>.pyi)."""
    subprocess.run([sys.executable, "-c", _STUBGEN, module, str(out), _ALL_TOOLKITS], check=True, cwd="/")
    assert out.exists(), out


def main() -> int:
    classes, templates = _CLASSES, _MANIFEST["templates"]
    toolkit_of = {}
    for pkg_file in _shims():
        m = re.search(r"from nanocct\._(\w+)\.(\w+) import \*", pkg_file.read_text())
        if m is not None:
            toolkit_of[m.group(2)] = (m.group(1), _stub_of(pkg_file))
    # One stub per package module, and they are 97 % of the run (measured 2026-09-24: 97.8 s of 100.8 s, 276 ms per
    # module and flat). Each already runs in a subprocess of its own and writes one file nothing else touches, so they
    # just have to be started at the same time; a thread per subprocess is enough, the work is all in the children.
    # Everything below this loop reads the files it wrote and stays sequential.
    modules = sorted(toolkit_of.items())
    jobs, how = jobs_from_env(len(modules))
    print(f"stubs: {len(modules)} modules, {jobs} job{'' if jobs == 1 else 's'} ({how})", file=sys.stderr)
    with ThreadPoolExecutor(jobs) as pool:
        done = {pool.submit(_stubgen, f"nanocct._{tk}.{pkg}", out): out for pkg, (tk, out) in modules}
        for future in done:
            future.result()                       # the first failure is raised here, with its traceback
            print(f"stub {done[future].relative_to(ROOT)}", file=sys.stderr)
    # nanocct/__init__.pyi: the package is lazy at runtime (PEP 562 __getattr__), so a checker only knows
    # `nanocct.gp` exists if the stub says so. `import X as X` is the re-export form the typing spec requires.
    pkgs = sorted({pkg for pkg, _ in toolkit_of.items()})
    (SRC / "__init__.pyi").write_text(
        '"""nanocct: nanobind (stable ABI) Python bindings for Open CASCADE Technology, 1:1 with the OCCT API."""\n'
        + "".join(f"import nanocct.{p} as {p}\n" for p in pkgs)
        + "\n__all__ = [\n" + "".join(f'    "{p}",\n' for p in pkgs) + "]\n")
    print(f"stub src/nanocct/__init__.pyi ({len(pkgs)} packages)", file=sys.stderr)
    # NCollection: generic container classes + instantiations as their subclasses
    nc = toolkit_of["NCollection"][1]
    text = nc.read_text()
    generic_parts = []
    kinds = sorted({re.match(r"([\w:]+)<", key).group(1) for key, inst in templates.items()
                    if not inst.get("skipped", False) and re.match(r"([\w:]+)<", key).group(1) in BINDERS})
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
        kind, args = re.match(r"([\w:]+)<(.*)>$", key).groups()
        if kind not in BINDERS:
            continue                                   # alias-instantiated class: stubgen's concrete class stays
        spelled = [_type_arg(a, classes, templates) for a in _split_args(args)]
        if any(sp is None for sp in spelled) or not (GENERIC / f"{kind}.pyi").exists():
            continue
        bases = f"{kind}[{', '.join(spelled)}]"
        if kind == "NCollection_Shared":                 # NCollection_Shared<T> derives from T (+ Transient members)
            bases = f"{spelled[0]}, _NCollection_Shared_members"
        body = []
        if "class Iterator(Generic[" in (GENERIC / f"{kind}.pyi").read_text():
            # the generic nested Iterator does not bind the outer arguments (Python nested classes share no type parameters):
            # the concrete class gets a concrete Iterator, so NCollection_List__int.Iterator(...).Value() is int (6b)
            n_it = 2 if kind in ("NCollection_DataMap", "NCollection_IndexedDataMap", "NCollection_DoubleMap") else 1
            body.append(f"    class Iterator({kind}.Iterator[{', '.join(spelled[:n_it])}]): ...")
        view = _view_accessor(text, inst["name"])
        if view is None and kind.startswith("NCollection_HArray"):
            # stubgen does not repeat an inherited member, and NCollection_HArray1<T> inherits __array__
            # from NCollection_Array1<T>. In the stub the H class derives from the *generic* Array1, which
            # cannot carry it (see _view_accessor), so the sibling's member is copied across.
            view = _view_accessor(text, inst["name"].replace("_HArray", "_Array", 1))
        if view is not None:
            body.append(view)
        block = (f"class {inst['name']}({bases}): ..." if len(body) == 0
                 else f"class {inst['name']}({bases}):\n" + "\n".join(body))
        text = _replace_class_block(text, inst["name"], block)
    header = ("from typing import Generic, Self, TypeVar, overload\nfrom collections.abc import Iterator\n"
              "import nanocct.Standard\n\n_T = TypeVar('_T')\n_K = TypeVar('_K')\n_V = TypeVar('_V')\n"
              "_IT = TypeVar('_IT')\n_IK = TypeVar('_IK')\n_IV = TypeVar('_IV')\n\n")   # the nested Iterator classes: a nested class cannot reuse the outer class's type variables
    header += (GENERIC / "NCollection_Shared.pyi").read_text().replace("class NCollection_Shared(Generic[_T]):", "class _NCollection_Shared_members:").replace(
        "    def __init__(self, theOther: _T) -> None: ...", "    def __init__(self, theOther: object) -> None: ...") + "\n"
    nc.write_text(_unhashable_ignore(_with_numpy_imports(header + "".join(generic_parts) + "\n" + text)))
    # OCCT signatures: the generic spelling instead of the concrete class (nanocct.NCollection.NCollection_Array1__double
    # -> nanocct.NCollection.NCollection_Array1[float]), so that a value typed NCollection_Array1[float] (what
    # NCollection_Array1[float](...) produces statically) is accepted as an argument. The concrete class derives from
    # the generic one, so the rewrite is sound for parameters and results alike; the NCollection stub itself keeps the
    # concrete names (they are its class definitions).
    generic_of: dict[str, str] = {}
    for key, inst in templates.items():
        if inst.get("skipped", False) or re.match(r"([\w:]+)<", key).group(1) not in BINDERS:
            continue
        generic = _generic_or_none(inst["name"], templates)
        if generic is not None:
            generic_of[inst["name"]] = "nanocct.NCollection." + generic
    # One alternation for all ~800 names instead of one scan each: this loop used to do
    # 370 files x 4 rounds x ~812 names = 1.2 million whole-file substitutions over 14.8 MB, and was 57% of stub
    # generation (129.9 s of 226.8 s, macOS 2026-09-24). The trailing \b already prevents a shorter name from matching
    # a prefix of a longer one (the names are separated by '_', a word character), and longest-first makes it explicit.
    # A nested-class access (X.Iterator as a base class, Graphic3d_SequenceOfHClipPlane::Iterator) keeps the concrete
    # name: ty rejects the nested class of a specialised generic (6b) -- hence the (?!\.).
    generic_re = re.compile(r"\bnanocct\.NCollection\.(" + "|".join(
        re.escape(n) for n in sorted(generic_of, key=len, reverse=True)) + r")\b(?!\.)") if len(generic_of) > 0 else None
    for stub in sorted(SRC.rglob("*.pyi")):
        if stub == nc:
            continue
        text = stub.read_text()
        # Each round resolves one level of nesting: the generic spelling of an instantiation names its arguments, and
        # an argument is often another instantiation (NCollection_Sequence__NCollection_List__int ->
        # NCollection_Sequence[NCollection_List__int], whose argument still has to be rewritten). The bound used to be
        # a bare range(4), which would silently leave a concrete name behind if the nesting were ever deeper.
        for _ in range(8):
            if generic_re is None:
                break
            new = generic_re.sub(lambda m: generic_of[m.group(1)], text)
            if new == text:
                break
            text = new
        else:
            raise RuntimeError(f"{stub}: the generic rewrite did not converge -- nesting deeper than expected")
        stub.write_text(_unhashable_ignore(_with_numpy_imports(_with_imports(text))))
    (SRC / "py.typed").write_text("")
    print("NCollection.pyi: generic classes for", ", ".join(kinds), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
