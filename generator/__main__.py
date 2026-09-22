"""CLI: python -m generator --toolkit TKMath --package gp [--package ...]

Writes src/cpp/<toolkit>/<package>.cpp, src/cpp/<toolkit>/_<toolkit>.cpp, src/cpp/toolkits.cmake and
src/nanoocp/<package>.py. Prints a report of everything that was not bound and why."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from .binders import BINDERS, instance_args
from .emit import Emitter, emit_toolkit_module, write_package_shims
from .occt import load_tree
from .ncollection import deprecated_aliases, template_docs
from .parse import INCLUDE_PACKAGES, clang_args, configure_libclang, include_prelude, parse_package, py_path
from .report import write_report
from .symbols import defined_symbols

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


_paths: dict[str, str] = {}       # manifest "paths", set by main() for _element_spec
_SCALARS = {"double": ("builtins", "float"), "int": ("builtins", "int"), "bool": ("builtins", "bool"),
            "std::string": ("builtins", "str")}    # other C++ scalars: mangled name only (float, size_t, char, ...)


def _element_spec(arg: str, known: dict[str, str], templates: dict[str, dict]) -> tuple[str, str] | None:
    """Python type that stands for a C++ template argument in NCollection_Xxx[T]: float for double, the OCCT class
    for a class or handle<class>, the bound instantiation for a nested container; None -> no accessor entry."""
    if arg in _SCALARS:
        return _SCALARS[arg]
    m = re.match(r"(?:opencascade::)?handle<(.+)>$", arg)
    if m is not None:
        arg = m.group(1)
    inst = templates.get(arg)                    # template instantiations first: their Python name is the alias
    if inst is not None and not inst.get("skipped", False):
        return (f"nanoocp.{inst['package']}", inst["name"])
    if arg in known and "<" not in arg:
        return (f"nanoocp.{known[arg]}", py_path(arg, known[arg], _paths))     # dotted for nested classes / namespaces
    return None


def _accessors(known: dict[str, str], templates: dict[str, dict]) -> dict[str, dict[tuple[tuple[str, str], ...], str]]:
    out: dict[str, dict[tuple[tuple[str, str], ...], str]] = {}
    for key, inst in templates.items():
        m = re.match(r"([\w:]+)<(.*)>$", key)
        if m is None or inst.get("skipped", False) or m.group(1) not in BINDERS:
            continue                                   # alias-instantiated templates (math_Vector) are plain classes
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


def _rehoming_risks(tree, parsed: list[tuple[str, list]], templates_before: set[str], toolkits_before: list[str],
                    requested: list[str], known: dict[str, str], generated_toolkits: list[str]) -> list[str]:
    """Instantiations this run binds for the first time although a toolkit that is not being regenerated precedes the
    binding toolkit in dependency order and could have needed them: a clean run might home them there instead, so the
    incremental result would not be canonical. Only toolkits at or after the latest toolkit of the instantiation's
    argument types count (NCollection_List<TopoDS_Shape> cannot be owned by TKernel)."""
    order = _topo(tree, generated_toolkits)
    toolkit_of = {name: pk.toolkit for name, pk in tree.packages.items()}
    not_regenerated = [t for t in toolkits_before if t not in requested]
    risks: list[str] = []
    seen: set[str] = set()
    for tk_name, irs in parsed:
        for ir in irs:
            keys = [f"{inst.template}<{', '.join(instance_args(inst.template, inst.args))}>" for inst in ir.instances.values()]
            keys += [c.template_key for c in ir.classes if c.template_key != ""]
            for key in keys:
                if key in templates_before or key in seen:
                    continue
                seen.add(key)
                arg_toolkits = [toolkit_of[known[ident]] for ident in re.findall(r"[A-Za-z_]\w*", key)
                                if ident in known and known[ident] in toolkit_of]
                floor = max((order.index(t) for t in arg_toolkits if t in order), default=0)
                candidates = [t for t in not_regenerated if t in order and floor <= order.index(t) < order.index(tk_name)]
                if len(candidates) > 0:
                    risks.append(f"{key} is newly bound by {tk_name}/{ir.name}; {', '.join(candidates)} not regenerated")
    return risks


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="generator")
    ap.add_argument("--occt-src", type=Path, default=ROOT / "deps" / "occt-src")
    ap.add_argument("--occt", type=Path, default=ROOT / "deps" / "occt-8.0.1")
    ap.add_argument("--toolkit", required=True, action="append", help="toolkit to generate (repeatable)")
    ap.add_argument("--package", action="append", default=None, help="restrict to these packages (default: all of the toolkit)")
    ap.add_argument("--out", type=Path, default=ROOT / "src")
    ap.add_argument("--allow-rehoming", action="store_true",
                    help="let an incremental run bind an instantiation that an earlier, not regenerated toolkit might own in a clean run")
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
    global _paths
    templates: dict[str, dict] = manifest["templates"]
    templates_before = set(templates)                       # instantiations bound by earlier runs (re-homing check below)
    toolkits_before = sorted(set(manifest.get("packages", {}).values()))
    generated_pkgs: dict[str, str] = manifest.setdefault("packages", {})     # package -> toolkit, every generated package
    paths: dict[str, str] = manifest.setdefault("paths", {})    # C++ class -> Python path where py_path() cannot derive it
    _paths = paths
    cpp_root.mkdir(parents=True, exist_ok=True)
    py_root.mkdir(parents=True, exist_ok=True)
    parsed: list[tuple[str, list]] = []
    for tk_name in args.toolkit:
        tk = tree.toolkits[tk_name]
        pkgs = [p for p in tk.packages if args.package is None or p.name in args.package]
        allowed = INCLUDE_PACKAGES.get(tk_name)          # a partial toolkit (the font slice: TKService -> Font, Graphic3d)
        if allowed is not None:
            missing = [n for n in allowed if n not in {p.name for p in tk.packages}]
            if len(missing) > 0:
                print(f"{tk_name}: overrides.toml [include] packages names unknown packages {missing}", file=sys.stderr)
                return 1
            pkgs = [p for p in pkgs if p.name in allowed]
        if len(pkgs) == 0:
            print(f"{tk_name}: no packages selected", file=sys.stderr)
            return 1
        irs = []
        for pkg in pkgs:
            bound_elsewhere = {n for n, pk in known.items() if pk != pkg.name} | {c.name for ir in irs for c in ir.classes}
            irs.append(parse_package(tree, pkg, known_elsewhere=bound_elsewhere))
        symbols = defined_symbols(args.occt, tk_name)
        if symbols is None:
            print(f"{tk_name}: library symbols not checked (nm unavailable)", file=sys.stderr)
        else:
            # R-UNDEFINED: per overload, by mangled name (GeomInt_WLApprox::Perform() next to three defined Perform overloads)
            for ir in irs:
                for c in ir.classes:
                    for m in c.methods:
                        if m.skip_reason is None and not m.defined_in_header and m.mangled not in symbols:
                            m.skip_reason = "declared but not defined in the library"
                            ir.report.append(f"{c.name}::{m.name}({', '.join(p.type for p in m.params)}): declared in the header, no definition in lib{tk_name}")
                    for k in c.ctors:
                        if k.skip_reason is None and not k.is_copy and not k.defined_in_header and k.mangled not in symbols:
                            k.skip_reason = "declared but not defined in the library"
                            ir.report.append(f"{c.name}::{c.name}({', '.join(p.type for p in k.params)}): declared in the header, no definition in lib{tk_name}")
                for fn in ir.functions:            # free functions too (TopOpeBRepDS: FUN_scanloi, FDSSDM_s1s2makesordor)
                    if fn.skip_reason is None and not fn.defined_in_header and fn.mangled not in symbols:
                        fn.skip_reason = "declared but not defined in the library"
                        ir.report.append(f"{fn.qualified}({', '.join(p.type for p in fn.params)}): declared in the header, no definition in lib{tk_name}")
                # a copy constructor declared but never defined (GCPnts_DistFunction: the old idiom to forbid copies) is
                # still "copy constructible" for nanobind, which then instantiates a copy wrapper -> link error:
                # the class cannot be bound at all
                unlinkable = [c for c in ir.classes if "<" not in c.name and any(
                    k.is_copy and not k.defined_in_header and k.mangled not in symbols for k in c.ctors)]
                for c in unlinkable:
                    ir.report.append(f"{c.name}: copy constructor declared in the header, no definition in lib{tk_name} -> class skipped")
                    ir.classes.remove(c)
        for ir in irs:
            generated_pkgs[ir.name] = tk_name
            manifest.setdefault("namespaces", {})[ir.name] = [list(ns) for ns in ir.namespaces]
            # a regenerated package re-binds its own classes and template instances: forget the old entries
            for name in [n for n, pk in known.items() if pk == ir.name]:
                del known[name]
            for key in [k for k, v in templates.items() if v.get("by") == ir.name]:
                del templates[key]
            for name in [n for n in paths if n not in known]:      # this package's classes were just forgotten above
                del paths[name]
            for c in ir.classes:
                known[c.name] = ir.name
                full = ".".join(c.scope + (c.py_name,))
                if full != py_path(c.name, ir.name):
                    paths[c.name] = full
                for e in c.enums:                  # nested enums (gp_Dir::D): types too, e.g. as defaults
                    known[e.name] = ir.name
            for e in ir.enums:                     # enums are element types too (NCollection_IndexedMap<Message_MetricType>)
                known[e.name] = ir.name
        parsed.append((tk_name, irs))
    # toolkits generated by earlier runs (recorded in the manifest, so a partial run into --out sees them) plus this run's
    generated_toolkits = sorted(set(generated_pkgs.values()) | set(args.toolkit))
    rehomed = _rehoming_risks(tree, parsed, templates_before, toolkits_before, args.toolkit, known, generated_toolkits)
    if len(rehomed) > 0:
        for line in rehomed:
            print(f"rehoming: {line}", file=sys.stderr)
        if not args.allow_rehoming:
            print("Instantiations are owned by the first package that needs them in a clean run (Design.md 9); an incremental "
                  "run cannot know whether a toolkit that was not regenerated would own these. Run a clean regeneration "
                  "(rm src/cpp/manifest.json, all toolkits) or pass --allow-rehoming.", file=sys.stderr)
            return 1
    for tk_name, irs in parsed:
        tk = tree.toolkits[tk_name]
        tk_dir = cpp_root / tk_name
        tk_dir.mkdir(parents=True, exist_ok=True)
        # emit in runtime (declaration) order: template instances are bound in that order and an
        # HSequence<T> must find its Sequence<T> already registered. A partial run (--package) keeps the
        # stored order of the toolkit and appends packages not seen before.
        stored = manifest.setdefault("order", {}).get(tk_name, [])
        if args.package is None or len(stored) == 0:
            order = _package_order(irs, known)
        else:
            order = stored + [ir.name for ir in irs if ir.name not in stored]
        manifest["order"][tk_name] = order
        irs = sorted(irs, key=lambda ir: order.index(ir.name))
        pkgs = [tree.packages[ir.name] for ir in irs]
        report_entries: list[tuple[str, str]] = []            # (package, message) of everything not bound
        included: set[str] = set()                            # every OCCT header the emitted sources include (R-LINK)
        cargs = clang_args(tree)
        for ir, pkg in zip(irs, pkgs):
            em = Emitter(ir, tree.include_dir, known, {name: pk.toolkit for name, pk in tree.packages.items()}, templates,
                         _topo(tree, generated_toolkits), paths,
                         prelude_check=lambda headers: include_prelude(headers, tree.include_dir, cargs))
            (tk_dir / f"{pkg.name}.cpp").write_text(em.emit())
            included.update(em.includes)
            for name in em.skipped:            # a class skipped at emit time (base not bound) must not reach the manifest: a later
                known.pop(name, None)          # toolkit deriving from it would abort at import (nb_type_new: base type not known)
                paths.pop(name, None)
            n_methods = sum(1 for c in ir.classes for m in c.methods if m.skip_reason is None)
            print(f"{tk_name}/{pkg.name}: {len(ir.classes)} classes, {len(ir.enums)} enums, {n_methods} methods, "
                  f"{len(ir.functions)} free functions; not bound: {len(ir.report) + len(em.report)}", file=sys.stderr)
            for line in ir.report + em.report:
                print(f"    - {line}", file=sys.stderr)
                report_entries.append((pkg.name, line))
        if args.package is None:            # a partial run would write a report of the given packages only
            counts = write_report(tk_dir / "report.txt", tk_name, report_entries)
            summary = ", ".join(f"{c} {n}" for c, n in counts.most_common()) if len(counts) > 0 else "nothing unbound"
            print(f"{tk_name}: report.txt written ({summary})", file=sys.stderr)
            # R-LINK: OCCT's EXTERNLIB is the link line OCCT itself needs; a header may forward-declare a class of
            # another toolkit (DE_Provider names XSControl_WorkSession and TDocStd_Document), and the handle caster
            # of that class needs its typeinfo -> link the owning toolkits too. A partial run sees only some packages.
            extra_libs = sorted({tree.toolkit_of_header[h] for h in included if h in tree.toolkit_of_header}
                                - tree.link_closure(tk_name))
            manifest.setdefault("links", {})[tk_name] = extra_libs
            if len(extra_libs) > 0:
                print(f"{tk_name}: links additionally {' '.join(extra_libs)} (types named in signatures)", file=sys.stderr)
        # R-LINK: a toolkit whose types this one only *names* is a link dependency; it becomes an import as well when it
        # precedes this toolkit in the canonical order (_TKXSBase imports _TKDE for XSAlgo_ShapeProcessor's
        # DE_ShapeFixParameters default, which nanobind converts at .def time). A toolkit that comes *later* is never
        # needed at registration time -- when this one was generated its classes were not in the manifest yet, so a base
        # or default of such a type would have been skipped -- and importing it back would be a cycle.
        position = {t: i for i, t in enumerate(_topo(tree, generated_toolkits))}
        depends = [d for d in tk.depends if d in generated_toolkits]
        depends += [d for d in manifest.get("links", {}).get(tk_name, [])
                    if d in generated_toolkits and d not in depends and position[d] < position[tk_name]]
        namespaces = {p: [tuple(ns) for ns in manifest["namespaces"].get(p, [])] for p in order}
        (tk_dir / f"_{tk_name}.cpp").write_text(emit_toolkit_module(tk_name, order, depends, namespaces))   # every package of the toolkit
    ordered = _topo(tree, generated_toolkits)
    # Python shims: one per generated package (+ deprecated typedef aliases), one per alias-only prefix
    aliases, unbound = deprecated_aliases(args.occt_src / "src" / "Deprecated" / "NCollectionAliases", clang_args(tree), templates)
    generated_packages = set(generated_pkgs)          # every generated package, with or without classes
    accessors = _accessors(known, templates)
    for pk in sorted(generated_packages):
        namespaces = [tuple(ns) for ns in manifest["namespaces"].get(pk, [])]
        write_package_shims(py_root, pk, generated_pkgs[pk], aliases.get(pk, {}), namespaces,
                            accessors if pk == "NCollection" else None)
    for prefix, amap in sorted(aliases.items()):
        if prefix not in generated_packages:
            write_package_shims(py_root, prefix, None, amap, [])
    print(f"deprecated typedef aliases: {sum(len(a) for a in aliases.values())} resolved, {unbound} not bound yet", file=sys.stderr)
    (py_root / "__init__.py").write_text(
        '"""nanoOCP: nanobind (stable ABI) Python bindings for Open CASCADE Technology, 1:1 with the OCCT API."""\n'
        "# Generated by the nanoOCP generator. All toolkit modules are imported eagerly, in dependency order, so\n"
        "# that NCollection instantiations bound by a later toolkit into an earlier package are always present.\n"
        + "".join(f"import nanoocp._{tk}  # noqa: F401\n" for tk in ordered))
    manifest_path.write_text(json.dumps({"classes": dict(sorted(known.items())), "templates": dict(sorted(templates.items())),
                                         "packages": dict(sorted(generated_pkgs.items())), "order": manifest["order"],
                                         "links": dict(sorted(manifest.get("links", {}).items())),
                                         "namespaces": dict(sorted(manifest["namespaces"].items())), "paths": dict(sorted(paths.items()))}, indent=0) + "\n")
    docs, warnings = template_docs(tree.include_dir, clang_args(tree))
    (cpp_root / "common").mkdir(parents=True, exist_ok=True)
    (cpp_root / "common" / "ncollection_docs.h").write_text(docs)
    for w in warnings:
        print(f"    - {w}", file=sys.stderr)
    links = {tk: libs for tk, libs in sorted(manifest.get("links", {}).items()) if len(libs) > 0}
    (cpp_root / "toolkits.cmake").write_text(
        "# Generated by the nanoOCP generator. Do not edit.\n"
        "# Order = link order: every toolkit after its dependencies.\nset(NANOOCP_TOOLKITS "
        + " ".join(_topo(tree, generated_toolkits)) + ")\n"
        + "# Toolkits whose types a module names although OCCT's own EXTERNLIB does not link them (R-LINK):\n"
        + "".join(f"set(NANOOCP_{tk}_EXTRA_LIBS {' '.join(libs)})\n" for tk, libs in links.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
