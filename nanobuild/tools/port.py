"""Mechanical OCP -> nanoocp rewrite of Python sources, in place: the first pass of a nanobuild patch.

    python nanobuild/tools/port.py <OCP dir of the built shim> <file or directory>...

The OCP dir is the `OCP` package of the shim wheel (`make shim`, then unzip dist/cadquery_ocp_novtk-*.whl): its
generated OCP/<pkg>/__init__.py files are the name map from OCP to nanoocp, the same map build123d's parity run
checked. nanoocp must be importable (the staged tree or an installed wheel).

1. `from OCP.<pkg> import a, b as c` -> `from nanoocp.<pkg> import a, b as c`, the statement left as written when only
   the module path changes. A container (OCP.collections `Array1_gp_Pnt`, OCP 8's `IndexedMap_TopoDS_Shape_...`) becomes
   the generic spelling throughout the file -- `NCollection_Array1[gp_Pnt]`, Design.md 2a -- with its element types
   imported; `import ... as Alias` of one becomes `Alias = NCollection_...[...]`. A namespace module (OCP.TopoDS.TopoDS)
   becomes `import nanoocp.TopoDS as TopoDS`; `import OCP.X as y` becomes `import nanoocp.X as y`.
2. `Cls.Name_s` stays: nanoocp suffixes every static like OCP (R-STATIC-S). Only where nanoocp has no `Name_s` but a
   `Name` -- a function of a C++ namespace -- is the suffix dropped.

Everything it cannot decide is printed as `TODO file:line` (line numbers of the file BEFORE the rewrite) for the hand
pass; out-parameters, streams and results that nanoocp returns are always hand work, found by running the package's
tests natively and by nanobuild/tools/trace_shim.py.
"""
import ast
import importlib
import io
import sys
import tokenize
from pathlib import Path

import nanoocp.all  # noqa: F401  every toolkit, so every name in the map resolves
import nanoocp.NCollection as NCOLLECTION
from nanoocp._templates import Generic

LINE_LIMIT = 88

# concrete instantiation name -> (template name, the element types' (module, qualname)), the reverse of the tables
# behind NCollection_Array1[gp_Pnt] (nanoocp/_templates.py): a key is the element type, or a tuple of them
GENERIC: dict[str, tuple[str, tuple[tuple[str, str], ...]]] = {}
for _tmpl in Generic.__subclasses__():
    for _key, _concrete in _tmpl._instances.items():
        _types = _key if isinstance(_key, tuple) else (_key,)
        GENERIC.setdefault(_concrete.__name__, (_tmpl.__name__, tuple((t.__module__, t.__qualname__) for t in _types)))


def generic_spelling(concrete: str, need: list[tuple[str, str]]) -> str:
    """NCollection_IndexedDataMap__TopoDS_Shape__NCollection_List__TopoDS_Shape__TopTools_ShapeMapHasher ->
    NCollection_IndexedDataMap[TopoDS_Shape, NCollection_List[TopoDS_Shape], TopTools_ShapeMapHasher]; the (module, name)
    pairs the expression needs imported are appended to `need`."""
    tname, specs = GENERIC[concrete]
    need.append(("nanoocp.NCollection", tname))
    parts = []
    for mod, qual in specs:
        if mod == "builtins":
            parts.append(qual)
        elif mod == "nanoocp.NCollection" and qual in GENERIC:
            parts.append(generic_spelling(qual, need))
        else:
            need.append((mod, qual.split(".")[0]))
            parts.append(qual)
    return f"{tname}[{', '.join(parts)}]"


def import_statement(module: str, names: list[str], indent: str, parenthesized: bool) -> str:
    one = f"from {module} import {', '.join(names)}"
    if parenthesized is False and len(indent) + len(one) <= LINE_LIMIT:
        return one
    body = "".join(f"{indent}    {n},\n" for n in names)
    return f"from {module} import (\n{body}{indent})"


def load_maps(ocp_dir: Path) -> dict[str, dict[str, tuple[str, str, bool]]]:
    """OCP package -> {OCP name: (nanoocp module, nanoocp name, is_module)}."""
    maps: dict[str, dict[str, tuple[str, str, bool]]] = {}
    for init in sorted(ocp_dir.glob("*/__init__.py")):
        m: dict[str, tuple[str, str, bool]] = {}
        for node in ast.parse(init.read_text()).body:
            if isinstance(node, ast.ImportFrom) and node.module is not None and node.module.startswith("nanoocp"):
                for a in node.names:
                    m[a.asname if a.asname is not None else a.name] = (node.module, a.name, False)
            elif isinstance(node, ast.Import):
                for a in node.names:
                    if a.name.startswith("nanoocp.") and a.asname is not None:
                        m[a.asname] = (a.name, a.name, True)
        maps[init.parent.name] = m
    return maps


def port_file(path: Path, maps, todo: list[str]) -> bool:
    src = path.read_text()
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        todo.append(f"{path}:{e.lineno}: syntax error, not ported")
        return False
    lines = src.splitlines(keepends=True)
    offs = [0]
    for ln in lines:
        offs.append(offs[-1] + len(ln))

    def pos(line: int, col: int) -> int:
        return offs[line - 1] + col

    edits: list[tuple[int, int, str]] = []
    renames: dict[str, str] = {}          # identifier in this file -> nanoocp identifier or generic expression
    objects: dict[str, object] = {}       # local name -> nanoocp class or module, for the `_s` pass
    # names bound by an import statement, per scope, with the line binding them first: a generic expression needs its
    # element types imported before it is evaluated, but a second import of a name bound earlier is only noise. A
    # scope is the enclosing function or class (0 = the module); an import inside one function binds nothing in
    # another, so only the module's bindings and the statement's own scope count.
    scope_of: dict[int, int] = {}

    def assign_scopes(node, scope: int) -> None:
        for child in ast.iter_child_nodes(node):
            scope_of[id(child)] = scope
            inner = id(child) if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)) else scope
            assign_scopes(child, inner)

    assign_scopes(tree, 0)
    bound_at: dict[tuple[int, str], int] = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            for a in node.names:
                key = (scope_of[id(node)], a.asname if a.asname is not None else a.name.split(".")[0])
                bound_at[key] = min(bound_at.get(key, node.lineno), node.lineno)

    def bound_before(scope: int, name: str, line: int) -> bool:
        return any(bound_at.get((sc, name), line) < line for sc in {0, scope})

    def bound_anywhere(scope: int, name: str) -> bool:
        return any((sc, name) in bound_at for sc in {0, scope})
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module is not None and (
                node.module == "OCP" or node.module.startswith("OCP.")):
            parts = node.module.split(".")
            if len(parts) != 2 or parts[1] not in maps:
                todo.append(f"{path}:{node.lineno}: unhandled `from {node.module} import`")
                continue
            m = maps[parts[1]]
            primary = "nanoocp." + parts[1]
            same: list[str] = []                  # names that keep their module and spelling
            moved: dict[str, list[str]] = {}      # other nanoocp module -> names
            mods: list[str] = []                  # a namespace: `import nanoocp.TopoDS as TopoDS`
            need: list[tuple[str, str]] = []      # what the generic expressions need imported
            need_now: set[str] = set()            # ... of which an assignment evaluates right here
            assigns: list[str] = []               # `Alias = NCollection_Array1[gp_Pnt]` for `import ... as Alias`
            for a in node.names:
                local = a.asname if a.asname is not None else a.name
                spelled = a.name if a.asname is None else f"{a.name} as {a.asname}"
                if a.name not in m:
                    todo.append(f"{path}:{node.lineno}: OCP.{parts[1]}.{a.name} has no nanoocp counterpart in the shim map")
                    same.append(spelled)
                    continue
                nmod, nname, is_mod = m[a.name]
                if is_mod:
                    mods.append(f"import {nmod} as {local}")
                    objects[local] = importlib.import_module(nmod)
                    continue
                if nmod == "nanoocp.NCollection" and nname in GENERIC:
                    if a.asname is None:
                        renames[a.name] = generic_spelling(nname, need)   # Design.md 2a: the generic accessor is primary
                    else:
                        now: list[tuple[str, str]] = []
                        assigns.append(f"{a.asname} = {generic_spelling(nname, now)}")
                        need += now
                        need_now |= {name for _, name in now}
                    continue
                try:
                    objects[local if a.asname is not None else nname] = getattr(importlib.import_module(nmod), nname)
                except AttributeError:
                    todo.append(f"{path}:{node.lineno}: {nmod}.{nname} not importable")
                if nmod == primary and nname == a.name:
                    same.append(spelled)
                else:
                    if a.asname is None and nname != a.name:
                        renames[a.name] = nname
                    moved.setdefault(nmod, []).append(nname if a.asname is None else f"{nname} as {a.asname}")
            start, end = pos(node.lineno, node.col_offset), pos(node.end_lineno, node.end_col_offset)
            if len(same) == len(node.names):
                # only the module path changes: keep the statement as written (formatting, comments, order)
                at = src.index(node.module, start)
                edits.append((at, at + len(node.module), primary))
                continue
            indent = lines[node.lineno - 1][: node.col_offset]
            parenthesized = "(" in src[start:end]
            stmts = []
            if len(same) > 0:
                stmts.append(import_statement(primary, same, indent, parenthesized))
            stmts += mods
            for nmod, names in moved.items():
                stmts.append(import_statement(nmod, names, indent, parenthesized))
            here = {n.split(" as ")[-1] for n in same + [x for names in moved.values() for x in names]}
            by_module: dict[str, list[str]] = {}
            scope = scope_of[id(node)]
            for nmod, name in need:
                # an assignment evaluates the expression right here; a spelling used later in code only needs the name
                # bound somewhere in its scope by the time it runs
                bound = bound_before(scope, name, node.lineno) if name in need_now else bound_anywhere(scope, name)
                if name in here or bound or name in by_module.get(nmod, []):
                    continue
                by_module.setdefault(nmod, []).append(name)
                bound_at[(scope, name)] = min(bound_at.get((scope, name), node.lineno), node.lineno)
            for nmod, names in by_module.items():
                stmts.append(import_statement(nmod, sorted(names), indent, False))
            stmts += assigns
            if len(stmts) == 0:
                # everything it imported is bound already: drop the statement's whole line, not just its text
                line_start = offs[node.lineno - 1]
                line_end = offs[node.end_lineno] if node.end_lineno < len(offs) else len(src)
                if src[line_start:start].strip() == "" and src[end:line_end].strip() == "":
                    edits.append((line_start, line_end, ""))
                    continue
            edits.append((start, end, ("\n" + indent).join(stmts)))
        elif isinstance(node, ast.Import):
            for a in node.names:
                if a.name.startswith("OCP.") and a.asname is not None and len(node.names) == 1:
                    nmod = "nanoocp." + a.name[len("OCP."):]
                    objects[a.asname] = importlib.import_module(nmod)
                    edits.append((pos(node.lineno, node.col_offset), pos(node.end_lineno, node.end_col_offset),
                                  f"import {nmod} as {a.asname}"))
                elif a.name == "OCP" or a.name.startswith("OCP."):
                    todo.append(f"{path}:{node.lineno}: `import {a.name}` needs a hand port")

    # token pass: identifier renames and Cls.Name_s
    toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    for i, t in enumerate(toks):
        if t.type != tokenize.NAME:
            continue
        start = pos(*t.start)
        end = pos(*t.end)
        if any(s <= start < e for s, e, _ in edits):
            continue
        prev = toks[i - 1] if i > 0 else None
        if t.string in renames and (prev is None or prev.string != "."):
            edits.append((start, end, renames[t.string]))
        elif t.string.endswith("_s") and prev is not None and prev.string == "." and i >= 2:
            owner = toks[i - 2].string
            obj = objects.get(owner)
            if obj is None:
                todo.append(f"{path}:{t.start[0]}: `{owner}.{t.string}` owner unknown")
            elif hasattr(obj, t.string):
                pass                                   # nanoocp keeps `_s` here (a static/instance collision)
            elif hasattr(obj, t.string[:-2]):
                edits.append((start, end, t.string[:-2]))
            else:
                todo.append(f"{path}:{t.start[0]}: `{owner}.{t.string}` has neither {t.string} nor {t.string[:-2]} in nanoocp")
        elif t.string == "OCP" and (prev is None or prev.string not in ("import", "from", ".")):
            todo.append(f"{path}:{t.start[0]}: bare `OCP` reference")
    if len(edits) == 0:
        return False
    edits.sort()
    out = []
    last = 0
    for s, e, txt in edits:
        if s < last:
            raise RuntimeError(f"{path}: overlapping edits at offset {s}")
        out.append(src[last:s])
        out.append(txt)
        last = e
    out.append(src[last:])
    path.write_text("".join(out))
    return True


def main() -> None:
    maps = load_maps(Path(sys.argv[1]))
    todo: list[str] = []
    changed = 0
    for arg in sys.argv[2:]:
        p = Path(arg)
        files = sorted(p.rglob("*.py")) if p.is_dir() else [p]
        for f in files:
            if port_file(f, maps, todo):
                changed += 1
    print(f"changed {changed} files")
    for t in todo:
        print("TODO", t)


if __name__ == "__main__":
    main()
