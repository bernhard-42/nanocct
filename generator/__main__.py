"""CLI: python -m generator --toolkit TKMath --package gp [--package ...]

Writes src/cpp/<toolkit>/<package>.cpp, src/cpp/<toolkit>/_<toolkit>.cpp, src/cpp/toolkits.cmake and
src/nanoocp/<package>.py. Prints a report of everything that was not bound and why."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .emit import Emitter, emit_package_shim, emit_toolkit_module
from .occt import load_tree
from .ncollection import deprecated_aliases, template_docs
from .parse import clang_args, configure_libclang, parse_package

ROOT = Path(__file__).resolve().parent.parent


def _topo(tree, toolkits: list[str]) -> list[str]:
    """Dependencies first (OCCT's EXTERNLIB order), restricted to the given toolkits."""
    out: list[str] = []
    def visit(t: str) -> None:
        if t in out:
            return
        for d in tree.toolkits[t].depends:
            if d in toolkits:
                visit(d)
        out.append(t)
    for t in toolkits:
        visit(t)
    return out


def _package_order(irs: list, known: dict[str, str]) -> list[str]:
    """Packages of one toolkit ordered so that base classes are declared before derived ones.
    Cycles between packages are reported and left in PACKAGES.cmake order."""
    names = [ir.name for ir in irs]
    deps: dict[str, set[str]] = {ir.name: set() for ir in irs}
    for ir in irs:
        for c in ir.classes:
            for b in c.bases:
                pkg = known.get(b)
                if pkg is not None and pkg in deps and pkg != ir.name:
                    deps[ir.name].add(pkg)
    out: list[str] = []
    state: dict[str, int] = {}
    def visit(n: str) -> None:
        if state.get(n) == 2:
            return
        if state.get(n) == 1:
            print(f"warning: package dependency cycle at {n}", file=sys.stderr)
            return
        state[n] = 1
        for d in sorted(deps[n]):
            visit(d)
        state[n] = 2
        out.append(n)
    for n in names:
        visit(n)
    return out


_SCALARS = {"double": ("builtins", "float"), "int": ("builtins", "int"), "bool": ("builtins", "bool"),
            "std::string": ("builtins", "str")}    # other C++ scalars: mangled name only (float, size_t, char, ...)


def _element_spec(arg: str, known: dict[str, str], templates: dict[str, dict]) -> tuple[str, str] | None:
    """Python type that stands for a C++ template argument in NCollection_Xxx[T]: float for double, the OCCT class
    for a class or handle<class>, the bound instantiation for a nested container; None -> no accessor entry."""
    import re
    if arg in _SCALARS:
        return _SCALARS[arg]
    m = re.match(r"(?:opencascade::)?handle<(.+)>$", arg)
    if m is not None:
        arg = m.group(1)
    if arg in known:
        return (f"nanoocp.{known[arg]}", arg)
    inst = templates.get(arg)
    if inst is not None:
        return (f"nanoocp.{inst['package']}", inst["name"])
    return None


def _accessors(known: dict[str, str], templates: dict[str, dict]) -> dict[str, dict[tuple[tuple[str, str], ...], str]]:
    import re
    out: dict[str, dict[tuple[tuple[str, str], ...], str]] = {}
    for key, inst in templates.items():
        m = re.match(r"(\w+)<(.+)>$", key)
        if m is None:
            continue
        tmpl, args = m.group(1), _split_args(m.group(2))
        specs = [_element_spec(a, known, templates) for a in args]
        if any(sp is None for sp in specs):
            continue
        out.setdefault(tmpl, {})[tuple(specs)] = inst["name"]    # type: ignore[arg-type]
    return out


def _split_args(text: str) -> list[str]:
    """Split 'A, NCollection_List<B, C>' at top-level commas."""
    out, depth, cur = [], 0, ""
    for ch in text:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur.strip()); cur = ""
        else:
            cur += ch
    out.append(cur.strip())
    return out


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="generator")
    ap.add_argument("--occt-src", type=Path, default=ROOT / "deps" / "occt-src")
    ap.add_argument("--occt", type=Path, default=ROOT / "deps" / "occt-8.0.1")
    ap.add_argument("--toolkit", required=True, action="append", help="toolkit to generate (repeatable)")
    ap.add_argument("--package", action="append", default=None, help="restrict to these packages (default: all of the toolkit)")
    ap.add_argument("--out", type=Path, default=ROOT / "src")
    args = ap.parse_args(argv)

    print(configure_libclang(), file=sys.stderr)
    tree = load_tree(args.occt_src, args.occt)
    cpp_root = args.out / "cpp"
    py_root = args.out / "nanoocp"
    # manifest: C++ class -> package, for every class bound by earlier runs (base-class checks across toolkits)
    manifest_path = cpp_root / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    if "classes" not in manifest:
        manifest = {"classes": manifest, "templates": {}}
    known: dict[str, str] = manifest["classes"]
    templates: dict[str, dict] = manifest["templates"]
    cpp_root.mkdir(parents=True, exist_ok=True)
    py_root.mkdir(parents=True, exist_ok=True)
    parsed: list[tuple[str, list]] = []
    for tk_name in args.toolkit:
        tk = tree.toolkits[tk_name]
        pkgs = [p for p in tk.packages if args.package is None or p.name in args.package]
        if len(pkgs) == 0:
            print(f"{tk_name}: no packages selected", file=sys.stderr)
            return 1
        irs = [parse_package(tree, pkg) for pkg in pkgs]
        for ir in irs:
            # a regenerated package re-binds its own classes and template instances: forget the old entries
            for name in [n for n, pk in known.items() if pk == ir.name]:
                del known[name]
            for key in [k for k, v in templates.items() if v.get("by") == ir.name]:
                del templates[key]
            for c in ir.classes:
                known[c.name] = ir.name
        parsed.append((tk_name, irs))
    # toolkits generated by earlier runs (their module files exist) plus this run's
    generated_toolkits = sorted({d.name for d in cpp_root.iterdir() if d.is_dir() and (d / f"_{d.name}.cpp").exists()} | set(args.toolkit))
    for tk_name, irs in parsed:
        tk = tree.toolkits[tk_name]
        tk_dir = cpp_root / tk_name
        tk_dir.mkdir(parents=True, exist_ok=True)
        pkgs = [tree.packages[ir.name] for ir in irs]
        for ir, pkg in zip(irs, pkgs):
            em = Emitter(ir, tree.include_dir, known, {name: pk.toolkit for name, pk in tree.packages.items()}, templates)
            (tk_dir / f"{pkg.name}.cpp").write_text(em.emit())
            n_methods = sum(1 for c in ir.classes for m in c.methods if m.skip_reason is None)
            print(f"{tk_name}/{pkg.name}: {len(ir.classes)} classes, {len(ir.enums)} enums, {n_methods} methods, "
                  f"{len(ir.functions)} free functions; not bound: {len(ir.report) + len(em.report)}", file=sys.stderr)
            for line in ir.report + em.report:
                print(f"    - {line}", file=sys.stderr)
        depends = [d for d in tk.depends if d in generated_toolkits]
        (tk_dir / f"_{tk_name}.cpp").write_text(emit_toolkit_module(tk_name, _package_order(irs, known), depends))
    ordered = _topo(tree, generated_toolkits)
    # Python shims: one per generated package (+ deprecated typedef aliases), one per alias-only prefix
    aliases, unbound = deprecated_aliases(args.occt_src / "src" / "Deprecated" / "NCollectionAliases", clang_args(tree), templates)
    generated_packages = {pk for pk in set(known.values())}
    accessors = _accessors(known, templates)
    for pk in sorted(generated_packages):
        (py_root / f"{pk}.py").write_text(emit_package_shim(pk, tree.packages[pk].toolkit, aliases.get(pk, {}),
                                                            accessors if pk == "NCollection" else None))
    for prefix, amap in sorted(aliases.items()):
        if prefix not in generated_packages:
            (py_root / f"{prefix}.py").write_text(emit_package_shim(prefix, None, amap))
    print(f"deprecated typedef aliases: {sum(len(a) for a in aliases.values())} resolved, {unbound} not bound yet", file=sys.stderr)
    (py_root / "__init__.py").write_text(
        '"""nanoOCP: nanobind (stable ABI) Python bindings for Open CASCADE Technology, 1:1 with the OCCT API."""\n'
        "# Generated by the nanoOCP generator. All toolkit modules are imported eagerly, in dependency order, so\n"
        "# that NCollection instantiations bound by a later toolkit into an earlier package are always present.\n"
        + "".join(f"import nanoocp._{tk}  # noqa: F401\n" for tk in ordered))
    manifest_path.write_text(json.dumps({"classes": dict(sorted(known.items())), "templates": dict(sorted(templates.items()))}, indent=0) + "\n")
    docs, warnings = template_docs(tree.include_dir, clang_args(tree))
    (cpp_root / "common" / "ncollection_docs.h").write_text(docs)
    for w in warnings:
        print(f"    - {w}", file=sys.stderr)
    (cpp_root / "toolkits.cmake").write_text(
        "# Generated by the nanoOCP generator. Do not edit.\n"
        "# Order = link order: every toolkit after its dependencies.\nset(NANOOCP_TOOLKITS "
        + " ".join(_topo(tree, generated_toolkits)) + ")\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
