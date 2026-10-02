"""CLI: python -m generator --toolkit TKMath --package gp [--package ...]

Writes src/cpp/<toolkit>/<package>.cpp, src/cpp/<toolkit>/_<toolkit>.cpp, src/cpp/toolkits.cmake and
src/nanocct/<package>.py. Prints a report of everything that was not bound and why."""
from __future__ import annotations

import argparse
import json
import multiprocessing as mp
import os
import platform
import re
import sys
import time
from pathlib import Path

from .binders import BINDERS, instance_args
from .emit import Emitter, emit_toolkit_module, write_package_shims
from .occt import load_tree
from .ncollection import template_docs
from .parse import EXTRA_LINKS, INCLUDE_PACKAGES, PLATFORM_PACKAGES, clang_args, configure_libclang, include_prelude, parse_package, py_path
from . import parallel as _parallel
from .report import write_report
from .symbols import defined_symbols, destructor_defined, unavailable_reason

ROOT = Path(__file__).resolve().parent.parent


# The one package nanocct writes by hand rather than generating (R-ADDON): src/cpp/AddOns, built by CMakeLists outside
# the toolkit loop and imported as nanocct.AddOns (extension _AddOns). It is a package, never a toolkit.
HANDWRITTEN_PACKAGE = "AddOns"
# Its submodules (nb::module_::def_submodule in src/cpp/AddOns/_AddOns.cpp; tests/test_AddOns.py checks the two agree).
# Declared like a generated package's C++ namespaces, so the shim is the package nanocct/AddOns/ and nanobind's stubgen
# writes AddOns/ShapeClean.pyi next to AddOns/__init__.pyi -- as a single AddOns.py the submodule stubs landed at
# nanocct/ShapeClean.pyi, the stub of a module that does not exist, and nanocct.AddOns.ShapeClean was untyped.
HANDWRITTEN_NAMESPACES = [("ShapeClean",), ("Tessellator",)]


def _topo(tree, toolkits: list[str], extra: dict[str, list[str]] | None = None) -> list[str]:
    """Dependencies first (OCCT's EXTERNLIB order), restricted to the given toolkits.

    `extra` adds edges EXTERNLIB does not have, for the *import* order only (see _base_import_edges)."""
    out: list[str] = []
    extra = extra if extra is not None else {}
    def visit(t: str, stack: tuple[str, ...] = ()) -> None:
        if t in out:
            return
        if t in stack:
            raise SystemExit(f"cycle in the toolkit order: {' -> '.join(stack + (t,))}")
        for d in list(tree.toolkits[t].depends) + extra.get(t, []):
            if d in toolkits:
                visit(d, stack + (t,))
        out.append(t)
    for t in toolkits:
        visit(t)
    return out


# Binding-Rules.md R-IMPORT-BASE
def _base_import_edges(tree, parsed: list, templates: dict, classes: dict[str, str], packages: dict[str, str],
                       toolkit_of: dict[str, str]) -> dict[str, list[str]]:
    """Import edges nanobind needs and EXTERNLIB does not have: {toolkit: [toolkits imported before it]}.

    A class can only be registered after its base is, so the toolkit binding the derived class must import the one
    binding the base -- `nb_type_new` otherwise aborts the whole import with *"base type ... not known to nanobind"*,
    a hard failure with no traceback. OCCT's link graph does not imply those edges in two shapes, and both are here:

    * `NCollection_Shared<T>` derives from T (6a, BINDERS "wraps"): TKMesh binds `Shared<DataMap<TopoDS_Shape, int,
      TopTools_ShapeMapHasher>>` while TKBool binds the DataMap, and neither toolkit links the other. It worked until
      2026-09-23 only because the EXTERNLIB order happened to put TKBool first; adding TKBinXCAF reshuffled it and
      every `import nanocct` failed.
    * a class deriving from an instantiation another toolkit binds (`Class.after_templates`, 6a): `XmlObjMgt_RRelocationTable`
      derives from `NCollection_DataMap<int, handle<Standard_Transient>>`, which TKBinL binds. Until 2026-09-24 this
      shape had no edge at all, and `import nanocct._TKXmlL` on its own aborted -- invisible while nanocct/__init__.py
      imported every toolkit in an order that happened to work.

    And one that does not abort but leaves members uncallable: a signature naming an instantiation another toolkit binds
    (6a ownership: the first package in emit order that needs it binds it, every later one only uses it). Without the
    edge the type is unregistered until something else happens to load its owner -- with only TKLCAF imported,
    `TDataStd_RealList.List()` raised "Unable to convert function return value" because TKGeomBase binds
    `NCollection_List<double>` (63 members in 10 toolkits, found by the final review 2026-09-30). The owner precedes the
    user in emit order by construction, so this edge points backwards and cannot close a cycle."""
    wrapping = {kind for kind, info in BINDERS.items() if info.get("wraps") is True}
    owner = {key: entry["toolkit"] for key, entry in templates.items()
             if isinstance(entry, dict) and entry.get("toolkit")}
    edges: dict[str, list[str]] = {}

    def add(consumer: str, base: str) -> None:
        # An instantiation: the registry is the only trustworthy owner. `classes` maps a 6c instantiation to the LAST
        # package that had it in its IR (`known[c.name] = ir.name` per package), not to the one that binds it --
        # `BVH_PairTraverse<double, 3, void, double>` reads as BRepExtrema there while IntPatch actually binds it, and
        # trusting that produced a false TKGeomAlgo -> TKTopAlgo edge and a spurious cycle.
        if "<" in base:
            base_toolkit = owner.get(base)
        else:
            base_toolkit = packages.get(classes.get(base, ""), None)
        if base_toolkit is None or not consumer or base_toolkit == consumer:
            return
        if base_toolkit in tree.link_closure(consumer):
            return                       # already imported transitively through EXTERNLIB; no edge needed
        edges.setdefault(consumer, []).append(base_toolkit)

    for key, entry in templates.items():                      # Shared<T> wraps T
        kind = key.split("<")[0]
        if kind in wrapping and isinstance(entry, dict) and entry.get("toolkit"):
            add(entry["toolkit"], key[len(kind) + 1:-1].strip())
    for tk_name, irs in parsed:                               # a class deriving from another toolkit's instantiation
        for ir in irs:
            for c in ir.classes:
                for b in c.bases:
                    if "<" not in b:
                        continue
                    base = b[:-len("::Iterator")] if b.endswith("::Iterator") else b
                    # Skip only when this package actually *binds* it: having the key in ir.instances means the
                    # package uses it, and 6a ownership may still put the binding in another package (Emitter._owns).
                    if templates.get(base, {}).get("by") == ir.name:
                        continue         # bound here, in the templates phase before the declare
                    add(tk_name, base)
    for tk_name, irs in parsed:                               # a signature using another toolkit's instantiation
        for ir in irs:
            for key in ir.instances:
                entry = templates.get(key, {})
                if entry.get("skipped", False) or entry.get("by") == ir.name:
                    continue
                add(tk_name, key)
    return {t: sorted(set(d)) for t, d in edges.items()}


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
            "std::string": ("builtins", "str"),
            # the C++ scalars without a Python type of their own: marker keys (nanocct/_templates.py)
            "float": ("nanocct._templates", "float32"), "unsigned char": ("nanocct._templates", "uchar"),
            "unsigned int": ("nanocct._templates", "uint"), "unsigned long": ("nanocct._templates", "ulong"),
            "unsigned long long": ("nanocct._templates", "ulonglong")}    # other C++ scalars (char, size_t, ...): no key


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
        return (f"nanocct.{inst['package']}", inst["name"])
    if arg in known and "<" not in arg:
        return (f"nanocct.{known[arg]}", py_path(arg, known[arg], _paths))     # dotted for nested classes / namespaces
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


def _selected_packages(tree, tk_name: str, only: list[str] | None, this_platform: str) -> list | None:
    """The packages of one toolkit this run generates, or None after printing why there are none.

    Hoisted out of the parse loop because the parallel parse needs the whole job list, in this very order, before the
    first package is parsed: that order is what decides who owns an instantiation (_known_elsewhere_sets)."""
    pkgs = [p for p in tree.toolkits[tk_name].packages if only is None or p.name in only]
    allowed = INCLUDE_PACKAGES.get(tk_name)          # a partial toolkit (the font slice: TKService -> Font, Graphic3d)
    if allowed is not None:
        missing = [n for n in allowed if n not in {p.name for p in tree.toolkits[tk_name].packages}]
        if len(missing) > 0:
            print(f"{tk_name}: overrides.toml [include] packages names unknown packages {missing}", file=sys.stderr)
            return None
        pkgs = [p for p in pkgs if p.name in allowed]
    # overrides.toml [platform]: a package OCCT only compiles on its own platform (Cocoa). Skipped before the parse,
    # so it costs nothing on the other platforms and cannot reach the link there.
    for pkg in [p for p in pkgs if this_platform not in PLATFORM_PACKAGES.get(p.name, [this_platform])]:
        print(f"{tk_name}/{pkg.name}: not built on {this_platform} "
              f"(overrides.toml [platform]: {', '.join(PLATFORM_PACKAGES[pkg.name])})", file=sys.stderr)
        pkgs.remove(pkg)
    if len(pkgs) == 0:
        print(f"{tk_name}: no packages selected", file=sys.stderr)
        return None
    return pkgs


def _known_elsewhere_sets(selected: list[tuple[str, list]], classes_of: dict[tuple[str, str], list[str]],
                          manifest_classes: dict[str, str]) -> dict[tuple[str, str], set[str]]:
    """`known_elsewhere` for every package of the run, derived from a previous round's IRs instead of from the
    sequential accumulation -- the one input a package's parse takes from the packages before it.

    It replays what the sequential loop does to `known`: a package sees the classes of every earlier toolkit (folded in
    at the end of each toolkit, the old entries of a regenerated package deleted first) plus the classes of the earlier
    packages of its own toolkit. Only instantiation spellings are kept: `parse_package` looks the set up for nothing
    else (measured 2026-09-24 -- 339 queries in a 45-toolkit run, every one a name containing `<`), and they are the
    only names the rest of the pipeline cannot change under us, since R-UNDEFINED drops classes only by plain name.

    With `classes_of` empty -- the first round, where nothing has been parsed yet -- every package gets what the
    manifest alone gives it, so each one instantiates everything it uses. That round is what the ownership is then
    derived from: the owner of an instantiation is the first package, in this order, that has it."""
    known = {n: pk for n, pk in manifest_classes.items() if "<" in n}
    out: dict[tuple[str, str], set[str]] = {}
    for tk_name, pkgs in selected:
        earlier: set[str] = set()                   # classes of the earlier packages of this toolkit
        for pkg in pkgs:
            out[(tk_name, pkg.name)] = {n for n, pk in known.items() if pk != pkg.name} | earlier
            earlier |= {n for n in classes_of.get((tk_name, pkg.name), ()) if "<" in n}
        for pkg in pkgs:                            # end of the toolkit: the sequential loop folds its packages into `known`
            for n in [n for n, pk in known.items() if pk == pkg.name]:
                del known[n]
            for n in classes_of.get((tk_name, pkg.name), ()):
                if "<" in n:
                    known[n] = pkg.name
    return out


# Binding-Rules.md R-KEPT
def _own_keeper(c) -> bool:
    """A bound constructor or method of the Transient class keeps an argument its C++ object can keep (kept_cpp)."""
    if not c.is_transient:
        return False
    members = ([k.params for k in c.ctors if k.skip_reason is None]
               + [m.params for m in c.methods if m.skip_reason is None and not m.is_static])
    return any(p.kept and p.kept_cpp for params in members for p in params)


def _decide_kept_classes(parsed: list[tuple[str, list]], bases: dict[str, list[str]], keepers: set[str], kept: set[str],
                         symbols_of) -> None:
    """R-KEPT: a constructible Transient whose bound constructors or methods -- or a bound base's -- keep an argument with
    kept_cpp is constructed as nanocct::Kept<T>, unless the subclass cannot be formed (Class.kept_blocker) or its vtable
    would name a virtual function no OCCT library exports (Class.virtual_symbols; symbols_of(): every toolkit's defined
    symbols, None when they cannot be read -- then not checked, as R-UNDEFINED). Both reported: such a class keeps its
    arguments by its Python object, as before. keepers / kept: the manifest's sets over every run, updated here."""
    classes = [(ir, c) for _, irs in parsed for ir in irs for c in ir.classes]
    for _, c in classes:
        keepers.discard(c.name)
        kept.discard(c.name)
        if _own_keeper(c):
            keepers.add(c.name)
    for ir, c in classes:
        if not c.is_transient or c.is_abstract or not c.constructible:
            continue
        todo, seen, keeps = [c.name], {c.name}, False
        while len(todo) > 0 and not keeps:
            name = todo.pop()
            keeps = name in keepers
            for b in bases.get(name, []):
                if b not in seen:
                    seen.add(b)
                    todo.append(b)
        if not keeps:
            continue
        if c.kept_blocker != "":
            ir.report.append(f"{c.name}: {c.kept_blocker} -> constructed as itself, not as nanocct::Kept<T>: what it keeps lives "
                             f"as long as its Python object (R-KEPT)")
            continue
        symbols = symbols_of() if len(c.virtual_symbols) > 0 else set()
        missing = [] if symbols is None else [s for s in c.virtual_symbols if s not in symbols]
        if len(missing) > 0:
            ir.report.append(f"{c.name}: nanocct::Kept<T>'s vtable would name {', '.join(missing)}, no definition in the "
                             f"OCCT libraries -> constructed as itself: what it keeps lives as long as its Python object (R-KEPT)")
            continue
        c.kept = True
        kept.add(c.name)


def main(argv: list[str]) -> int:
    started = time.perf_counter()
    ap = argparse.ArgumentParser(prog="generator")
    ap.add_argument("--occt-src", type=Path, default=ROOT / "deps" / "occt-src")
    ap.add_argument("--occt", type=Path, default=ROOT / "deps" / "occt-8.0.1")
    # Takes a list -- `--toolkit TKernel TKMath TKG2d ...` -- and is still repeatable. The order is the caller's and
    # it matters: instantiation ownership follows it, and so does the import order a toolkit's aliases depend on.
    ap.add_argument("--toolkit", required=True, action="extend", nargs="+",
                    help="toolkits to generate, in dependency order (repeatable, takes a list)")
    ap.add_argument("--package", action="append", default=None, help="restrict to these packages (default: all of the toolkit)")
    ap.add_argument("--out", type=Path, default=ROOT / "src")
    ap.add_argument("--allow-rehoming", action="store_true",
                    help="let an incremental run bind an instantiation that an earlier, not regenerated toolkit might own in a clean run")
    args = ap.parse_args(argv)

    print(configure_libclang(), file=sys.stderr)
    tree = load_tree(args.occt_src, args.occt)
    cpp_root = args.out / "cpp"
    py_root = args.out / "nanocct"
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
    # R-OVERLOAD-ORDER: C++ class -> its direct bases, for every bound class of every run, so an emitter can tell that
    # TopoDS_Face derives from TopoDS_Shape also where its package only forward-declares the class
    bases: dict[str, list[str]] = manifest.setdefault("bases", {})
    # R-KEPT: the Transient classes whose bound members keep an argument (inherited by derived classes), and those the
    # bindings construct as nanocct::Kept<T> -- for every run, so a partial run sees the other toolkits' classes
    keepers: set[str] = set(manifest.get("keepers", []))
    kept_classes: set[str] = set(manifest.get("kept", []))
    _paths = paths
    cpp_root.mkdir(parents=True, exist_ok=True)
    py_root.mkdir(parents=True, exist_ok=True)
    parsed: list[tuple[str, list]] = []
    symbols_skipped: set[str] = set()   # the R-UNDEFINED skip reason, reported once per run
    this_platform = platform.system()    # overrides.toml [platform]
    timing = {"parse": 0.0, "emit": 0.0}   # wall time in the two phases, reported at the end
    per_toolkit: dict[str, dict[str, float]] = {}    # toolkit -> {"parse": s, "emit": s}, printed at the end
    selected: list[tuple[str, list]] = []            # (toolkit, packages) in parse order, the order ownership follows
    for tk_name in args.toolkit:
        sel = _selected_packages(tree, tk_name, args.package, this_platform)
        if sel is None:
            return 1
        selected.append((tk_name, sel))
    # PARALLEL PARSE (NANOCCT_JOBS>1): every package of every toolkit is parsed in one global pool before the
    # sequential loop runs, which then takes the IRs from `prefetched` instead of parsing -- so everything after the
    # parse is byte for byte the code path of a normal run. Two inputs a package normally inherits from the packages
    # before it have to be derived instead, and both are derived by iterating:
    #   * `known_elsewhere` (who already bound which instantiation), from the previous round's IRs;
    #   * the parser's cross-package state (parse.collect_state), merged at the barrier.
    # Round 1 runs with the manifest alone, so every package instantiates everything it uses and the first package in
    # `selected` order that has an instantiation is its owner -- which is exactly the sequential rule. Round 2 parses
    # again with that derived answer; the loop stops when neither the ownership nor the parser state moves any more.
    prefetched: dict[tuple[str, str], object] = {}
    derived_elsewhere: dict[tuple[str, str], set[str]] | None = None
    # One worker per core by default: the work is CPU-bound libclang parses, and more of them keep paying off even on
    # the efficiency cores (measured on an 18-core M5, 6P + 12E, 45 toolkits: 1 job 161.8 s, 10 jobs 40.9 s, 14 jobs
    # 34.9 s, 18 jobs 29.9 s). `NANOCCT_JOBS` overrides it and **`NANOCCT_JOBS=1` is the sequential path**, which is
    # what a byte-for-byte comparison is run against. Never more workers than packages: a `--package` run would
    # otherwise pay for a pool of idle processes, each loading the OCCT tree.
    n_packages = sum(len(pkgs) for _, pkgs in selected)
    jobs, how = _parallel.jobs_from_env(n_packages)
    if jobs > 1:
        print(f"parallel: {jobs} jobs over {n_packages} packages ({how})", file=sys.stderr)
        t0 = time.perf_counter()
        state = {"noncopyable": set(), "derives": {}, "ancestors": {}}
        elsewhere = _known_elsewhere_sets(selected, {}, known)      # round 1: the manifest alone
        rounds = 0
        with mp.Pool(jobs, initializer=_parallel.init, initargs=(tree.src, tree.install)) as pool:
            while True:
                rounds += 1
                merged = {"noncopyable": set(state["noncopyable"]), "derives": dict(state["derives"]), "ancestors": dict(state["ancestors"])}
                classes_of: dict[tuple[str, str], list[str]] = {}
                prefetched.clear()
                jobs_in = [(tk, pkg.name, sorted(elsewhere[(tk, pkg.name)]), state) for tk, pkgs in selected for pkg in pkgs]
                for tk_name, pkg_name, ir, dt, st in pool.imap_unordered(_parallel.parse_one, jobs_in, chunksize=1):
                    prefetched[(tk_name, pkg_name)] = ir
                    classes_of[(tk_name, pkg_name)] = [c.name for c in ir.classes]
                    per_toolkit.setdefault(tk_name, {"parse": 0.0, "emit": 0.0})["parse"] += dt
                    merged["noncopyable"] |= st["noncopyable"]
                    for k, v in st["derives"].items():
                        if v or k not in merged["derives"]:
                            merged["derives"][k] = v
                    merged["ancestors"].update(st["ancestors"])     # read from definitions only: every process agrees
                derived = _known_elsewhere_sets(selected, classes_of, known)
                # The fixpoint test is on the *inputs*: this round was given what its own result says it should have
                # been given, so another round would repeat it exactly and these IRs are the answer.
                stable = derived == elsewhere and merged == state
                state, elsewhere = merged, derived
                print(f"  round {rounds}: noncopyable {len(state['noncopyable'])}, derives {len(state['derives'])}, "
                      f"ancestors {len(state['ancestors'])}, "
                      f"instantiations {sum(1 for names in classes_of.values() for n in names if '<' in n)}"
                      f"{' (stable)' if stable else ''}", file=sys.stderr)
                if stable:
                    break
                if rounds >= 4:
                    # Without the fixpoint the IRs were parsed with inputs the run has since revised, and there is no
                    # reason left to believe they are what a sequential run produces. Two rounds have always sufficed.
                    print("parallel parse: no fixpoint after 4 rounds; run without NANOCCT_JOBS", file=sys.stderr)
                    return 1
        derived_elsewhere = elsewhere
        wall = time.perf_counter() - t0
        cpu = sum(t["parse"] for t in per_toolkit.values())
        print(f"parallel parse: {len(prefetched)} packages, {jobs} jobs, {rounds} round(s), wall {wall:.1f} s, "
              f"cpu {cpu:.1f} s (speedup {cpu / wall:.2f}x)", file=sys.stderr)
        timing["parse"] += wall

    for tk_index, (tk_name, pkgs) in enumerate(selected, start=1):
        print(f"[parse {tk_index}/{len(selected)}] {tk_name}", file=sys.stderr)
        irs = []
        # Only the instantiation spellings: parse_package consults the set for nothing else, and _known_elsewhere_sets
        # derives the same set for a parallel parse (the reasoning and the measurement are there).
        for pkg in pkgs:
            bound_elsewhere = ({n for n, pk in known.items() if "<" in n and pk != pkg.name}
                               | {c.name for ir in irs for c in ir.classes if "<" in c.name})
            if (tk_name, pkg.name) in prefetched:
                # What the pool was given, against what this loop would have handed the package: the derivation
                # simulates this accumulation from the IRs, and this is the accumulation itself. They must agree, or
                # the parallel parse decided ownership on an input the sequential run never had.
                if derived_elsewhere[(tk_name, pkg.name)] != bound_elsewhere:
                    only_derived = derived_elsewhere[(tk_name, pkg.name)] - bound_elsewhere
                    only_here = bound_elsewhere - derived_elsewhere[(tk_name, pkg.name)]
                    print(f"{tk_name}/{pkg.name}: the parallel parse was given a known_elsewhere this run does not "
                          f"agree with (+{sorted(only_derived)[:3]} -{sorted(only_here)[:3]})", file=sys.stderr)
                    return 1
                irs.append(prefetched.pop((tk_name, pkg.name)))     # parsed by the pool above
                continue
            _t0 = time.perf_counter()
            irs.append(parse_package(tree, pkg, known_elsewhere=bound_elsewhere))
            _dt = time.perf_counter() - _t0
            timing["parse"] += _dt
            per_toolkit.setdefault(tk_name, {"parse": 0.0, "emit": 0.0})["parse"] += _dt
        symbols = defined_symbols(args.occt, tk_name)
        if symbols is None:
            # once per run, not once per toolkit: 45 identical lines said nothing the first one did not
            reason = unavailable_reason(tree.install, tk_name)
            if reason not in symbols_skipped:
                symbols_skipped.add(reason)
                print(f"library symbols not checked ({reason})", file=sys.stderr)
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
                    # R-STATIC-DATA: a static data member whose value is not in the header is read through its symbol, which
                    # the library must export -- IntPatch_WLineTool::myMaxConcatAngle (a `static const double` defined in the
                    # .cxx, no Standard_EXPORT) linked on macOS/Linux but was LNK2019 on Windows (2026-09-30)
                    if "<" not in c.name:
                        for k in [k for k in c.statics if not k.value_in_header and k.mangled not in symbols]:
                            c.statics.remove(k)
                            ir.report.append(f"{k.cpp}: static data member declared in the header, no definition in lib{tk_name}")
                for fn in ir.functions:            # free functions too (TopOpeBRepDS: FUN_scanloi, FDSSDM_s1s2makesordor)
                    if fn.skip_reason is None and not fn.defined_in_header and fn.mangled not in symbols:
                        fn.skip_reason = "declared but not defined in the library"
                        ir.report.append(f"{fn.qualified}({', '.join(p.type for p in fn.params)}): declared in the header, no definition in lib{tk_name}")
                # R-UNDEFINED-COPY: a copy constructor declared but never defined (GCPnts_DistFunction: the old idiom to
                # forbid copies) is still "copy constructible" for nanobind, which then instantiates a copy wrapper -> link
                # error: the class cannot be bound at all, it is skipped and reported
                unlinkable = [c for c in ir.classes if "<" not in c.name and any(
                    k.is_copy and not k.defined_in_header and k.mangled not in symbols for k in c.ctors)]
                for c in unlinkable:
                    ir.report.append(f"{c.name}: copy constructor declared in the header, no definition in lib{tk_name} -> class skipped")
                    ir.classes.remove(c)
                # the same for the destructor: nanobind's wrap_destruct<T> needs ~T(), so a declared-but-not-exported one
                # is a link error for the whole class (Storage_Bucket on Windows, which has no Standard_EXPORT)
                no_dtor = [c for c in ir.classes if "<" not in c.name and c.dtor_mangled != ""
                           and not destructor_defined(c.dtor_mangled, symbols)]
                for c in no_dtor:
                    ir.report.append(f"{c.name}: destructor declared in the header, no definition in lib{tk_name} -> class skipped")
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
            for name in [n for n in bases if n not in known]:
                del bases[name]
            for c in ir.classes:
                known[c.name] = ir.name
                bases[c.name] = list(c.bases)
                full = ".".join(c.scope + (c.py_name,))
                if full != py_path(c.name, ir.name):
                    paths[c.name] = full
                for e in c.enums:                  # nested enums (gp_Dir::D): types too, e.g. as defaults
                    known[e.name] = ir.name
            for e in ir.enums:                     # enums are element types too (NCollection_IndexedMap<Message_MetricType>)
                known[e.name] = ir.name
        parsed.append((tk_name, irs))
    all_symbols: list[set[str] | None] = []

    def symbols_of() -> set[str] | None:
        """Every OCCT toolkit's defined symbols, read once (None when they cannot be read)."""
        if len(all_symbols) == 0:
            union: set[str] | None = set()
            for tk in sorted(tree.toolkits):
                one = defined_symbols(args.occt, tk)
                if one is None:
                    union = None
                    break
                union |= one
            all_symbols.append(union)
        return all_symbols[0]
    _decide_kept_classes(parsed, bases, keepers, kept_classes, symbols_of)
    # toolkits generated by earlier runs (recorded in the manifest, so a partial run into --out sees them) plus this run's
    generated_toolkits = sorted(set(generated_pkgs.values()) | set(args.toolkit))
    rehomed = _rehoming_risks(tree, parsed, templates_before, toolkits_before, args.toolkit, known, generated_toolkits)
    if len(rehomed) > 0:
        for line in rehomed:
            print(f"rehoming: {line}", file=sys.stderr)
        if not args.allow_rehoming:
            print("Instantiations are owned by the first package that needs them in a clean run; an incremental "
                  "run cannot know whether a toolkit that was not regenerated would own these. Run a clean regeneration "
                  "(rm src/cpp/manifest.json, all toolkits) or pass --allow-rehoming.", file=sys.stderr)
            return 1
    # The emit order, hoisted out of the loop below: a parallel emit has to decide the instantiation ownership over
    # every package before the first one is emitted, and this order is what decides it.
    emit_order: list[tuple[str, list, list[str]]] = []      # (toolkit, its IRs in emit order, every package of the toolkit)
    for tk_name, irs in parsed:
        # emit in runtime (declaration) order: template instances are bound in that order and an
        # HSequence<T> must find its Sequence<T> already registered. A partial run (--package) keeps the
        # stored order of the toolkit and appends packages not seen before.
        stored = manifest.setdefault("order", {}).get(tk_name, [])
        if args.package is None or len(stored) == 0:
            order = _package_order(irs, known)
        else:
            order = stored + [ir.name for ir in irs if ir.name not in stored]
        manifest["order"][tk_name] = order
        emit_order.append((tk_name, sorted(irs, key=lambda ir: order.index(ir.name)), order))
    # PARALLEL EMIT: who owns which instantiation is normally decided *by* emitting, first package to need it. So the
    # decision is run first, over every package in emit order and against one shared registry (Emitter.assign_templates,
    # which is the same code the sequential loop runs); every package then knows whether it owns a key or aliases it,
    # and they can be emitted independently (Emitter.preassigned).
    emitted: dict[tuple[str, str], tuple] = {}
    if jobs > 1:
        t0 = time.perf_counter()
        for tk_name, irs, _ in emit_order:
            for ir in irs:
                Emitter(ir, tree.include_dir, known, {name: pk.toolkit for name, pk in tree.packages.items()}, templates,
                        _topo(tree, generated_toolkits), paths, bases_of=bases, kept=kept_classes).assign_templates()
        print(f"instantiation ownership derived for {len(templates)} keys in "
              f"{time.perf_counter() - t0:.1f} s", file=sys.stderr)
        todo_e = [(tk, ir.name, ir) for tk, irs, _ in emit_order for ir in irs]
        t0 = time.perf_counter()
        with mp.Pool(jobs, initializer=_parallel.init_emit,
                     initargs=(tree.src, tree.install, known, templates, paths,
                               _topo(tree, generated_toolkits), bases, kept_classes)) as pool:
            for tk_name, pkg_name, text, rep, inc, skip, dt in pool.imap_unordered(_parallel.emit_one, todo_e, chunksize=1):
                emitted[(tk_name, pkg_name)] = (text, rep, inc, skip)
                per_toolkit.setdefault(tk_name, {"parse": 0.0, "emit": 0.0})["emit"] += dt
        wall = time.perf_counter() - t0
        cpu = sum(t["emit"] for t in per_toolkit.values())
        print(f"parallel emit: {len(todo_e)} packages, {jobs} jobs, wall {wall:.1f} s, cpu {cpu:.1f} s "
              f"(speedup {cpu / wall:.2f}x)", file=sys.stderr)
        timing["emit"] += wall
    for tk_index, (tk_name, irs, order) in enumerate(emit_order, start=1):
        print(f"[emit {tk_index}/{len(emit_order)}] {tk_name}", file=sys.stderr)
        tk = tree.toolkits[tk_name]
        tk_dir = cpp_root / tk_name
        tk_dir.mkdir(parents=True, exist_ok=True)
        pkgs = [tree.packages[ir.name] for ir in irs]
        report_entries: list[tuple[str, str]] = []            # (package, message) of everything not bound
        included: set[str] = set()                            # every OCCT header the emitted sources include (R-LINK)
        cargs = clang_args(tree)
        for ir, pkg in zip(irs, pkgs):
            em = Emitter(ir, tree.include_dir, known, {name: pk.toolkit for name, pk in tree.packages.items()}, templates,
                         _topo(tree, generated_toolkits), paths,
                         prelude_check=lambda headers: include_prelude(headers, tree.include_dir, cargs), bases_of=bases,
                         kept=kept_classes)
            if (tk_name, ir.name) in emitted:
                _emitted, _rep, _inc, _skip = emitted.pop((tk_name, ir.name))
                em.report[:] = _rep
                em.includes[:] = _inc
                em.skipped |= _skip
            else:
                _t0 = time.perf_counter()
                _emitted = em.emit()
                _dt = time.perf_counter() - _t0
                timing["emit"] += _dt
                per_toolkit.setdefault(tk_name, {"parse": 0.0, "emit": 0.0})["emit"] += _dt
            (tk_dir / f"{pkg.name}.cpp").write_text(_emitted)
            included.update(em.includes)
            for name in em.skipped:            # a class skipped at emit time (base not bound) must not reach the manifest: a later
                known.pop(name, None)          # toolkit deriving from it would abort at import (nb_type_new: base type not known)
                paths.pop(name, None)
            n_methods = sum(1 for c in ir.classes for m in c.methods if m.skip_reason is None)
            # "report lines", not "not bound": the count is lines, and 258 of them across the 45 toolkits describe a
            # member that *is* bound (R-WIDTH demotions, R-COLLISION renames, "__iter__ added"). A member with two
            # unsupported parameters also contributes two lines (write_report does not de-duplicate).
            print(f"{tk_name}/{pkg.name}: {len(ir.classes)} classes, {len(ir.enums)} enums, {n_methods} methods, "
                  f"{len(ir.functions)} free functions; report lines: {len(ir.report) + len(em.report)}", file=sys.stderr)
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
            extra_libs = sorted(({tree.toolkit_of_header[h] for h in included if h in tree.toolkit_of_header}
                                 | set(EXTRA_LINKS.get(tk_name, [])))            # overrides.toml [link] extra
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
        # R-IMPORT-BASE: the toolkit binding a base (or an instantiation a signature uses) is imported first. 6a:
        # NCollection_Shared<T> derives from T, so the toolkit binding T must be *imported* before this module registers
        # the wrapper. Ordering nanocct/all.py is not enough -- another toolkit's import chain can reach this one first
        # (_TKV3d imports _TKMesh, and _TKMesh registers a wrapper over a TKBool DataMap).
        # ... and unlike R-LINK's, this edge is not filtered by the EXTERNLIB order: TKBool comes *after* TKMesh
        # there, which is exactly the case the edge exists to repair. A cycle would make the eager order's _topo
        # fail loudly, since it is given the same edges.
        base_edges = _base_import_edges(tree, parsed, templates, known, generated_pkgs,
                                        {n: pk.toolkit for n, pk in tree.packages.items()})
        if len(base_edges.get(tk_name, [])) > 0:
            print(f"{tk_name}: imports {' '.join(base_edges[tk_name])} for base classes and instantiations they bind", file=sys.stderr)
        depends += [d for d in base_edges.get(tk_name, [])
                    if d in generated_toolkits and d not in depends and d != tk_name]
        namespaces = {p: [tuple(ns) for ns in manifest["namespaces"].get(p, [])] for p in order}
        (tk_dir / f"_{tk_name}.cpp").write_text(emit_toolkit_module(tk_name, order, depends, namespaces))   # every package of the toolkit
    # the eager import order alone guarantees registration order, so it carries the base edges EXTERNLIB lacks
    ordered = _topo(tree, generated_toolkits,
                    _base_import_edges(tree, parsed, templates, known, generated_pkgs,
                                       {n: pk.toolkit for n, pk in tree.packages.items()}))
    # Python shims: one per generated package. The pre-8.0 typedef names (TColgp_Array1OfPnt & co, OCCT's
    # src/Deprecated/NCollectionAliases) are NOT exposed -- nanocct is an OCCT 8 binding and code using it is
    # expected to spell the 8.0 names (decision 2026-09-24, Binding-Rules.md 6a).
    generated_packages = set(generated_pkgs)          # every generated package, with or without classes
    # nanocct.AddOns is hand-written (src/cpp/AddOns, built by CMakeLists outside the toolkit loop). Its shim and
    # its entry in _PACKAGES are generated like any other package's, so `make clean_gen` stays correct and
    # `import nanocct; nanocct.AddOns` resolves through the same lazy __getattr__. It must NOT
    # reach generated_pkgs: that goes into the manifest, an incremental run reads it back into
    # generated_toolkits, and _topo then looks for a toolkit OCCT has never heard of (KeyError: 'AddOns').
    generated_packages.add(HANDWRITTEN_PACKAGE)
    accessors = _accessors(known, templates)
    # 6a: which toolkit binds each instantiation that lives in a package other than its own. Only `NCollection`
    # receives them (every 6c instantiation is bound by the package that declares it), so only that shim imports
    # those toolkits eagerly -- but it is derived, not assumed, so a second such package would do the same.
    homed_elsewhere: dict[str, dict[str, str]] = {}
    for entry in templates.values():
        if entry.get("skipped", False) or not entry.get("package") or not entry.get("toolkit"):
            continue
        if generated_pkgs.get(entry["package"]) != entry["toolkit"]:
            homed_elsewhere.setdefault(entry["package"], {})[entry["name"]] = entry["toolkit"]
    # R-LINK forward case: a toolkit that links one coming later cannot import it at registration time (8b).
    position = {tk: i for i, tk in enumerate(_topo(tree, generated_toolkits))}
    late_links = {tk: sorted(e for e in extras if position.get(e, -1) > position.get(tk, 0))
                  for tk, extras in manifest.get("links", {}).items()}
    for pk in sorted(generated_packages):
        namespaces = HANDWRITTEN_NAMESPACES if pk == HANDWRITTEN_PACKAGE else [tuple(ns) for ns in manifest["namespaces"].get(pk, [])]
        tk = HANDWRITTEN_PACKAGE if pk == HANDWRITTEN_PACKAGE else generated_pkgs[pk]
        write_package_shims(py_root, pk, tk, namespaces,
                            accessors if pk == "NCollection" else None,
                            homed_elsewhere.get(pk), late_links.get(tk))
    print(f"6a: {sum(len(v) for v in homed_elsewhere.values())} instantiations bound from other toolkits into "
          f"{len(homed_elsewhere)} package(s), imported eagerly; late R-LINK imports: "
          f"{ {k: v for k, v in late_links.items() if v} }", file=sys.stderr)
    total = time.perf_counter() - started
    print(f"timing: parse {timing['parse']:.1f} s, emit {timing['emit']:.1f} s, other {total - timing['parse'] - timing['emit']:.1f} s"
          f" (total {total:.1f} s)", file=sys.stderr)
    (py_root / "__init__.py").write_text(
        '"""nanocct: nanobind (stable ABI) Python bindings for Open CASCADE Technology, 1:1 with the OCCT API."""\n'
        "# Generated by the nanocct generator. Nothing is imported here: `import nanocct.gp` pulls in _TKMath alone\n"
        "# (and what its registration needs), which is 14 ms rather than the 172 ms and 179 MB that importing all 45\n"
        "# toolkit modules cost. Each extension module already imports its own dependencies -- EXTERNLIB, the R-LINK\n"
        "# extras that precede it and the R-IMPORT-BASE edges (base classes, and the instantiations its signatures\n"
        "# use) -- so registration order holds without a list here.\n"
        "# The one module other toolkits bind into is nanocct.NCollection, and importing it loads every toolkit\n"
        "# that binds an instantiation into it (Binding-Rules.md 6a).\n"
        "\n"
        "# `import nanocct` then `nanocct.gp.gp_Pnt` works: PEP 562 module __getattr__ imports the package on first\n"
        "# access. This is the one place that mechanism earns its keep -- a submodule that genuinely exists, resolved\n"
        "# lazily in a single file, rather than the per-shim fallback that used to paper over a stale star import.\n"
        "import importlib as _importlib\n"
        "\n"
        "_PACKAGES = frozenset((\n"
        + "".join(f'    "{pk}",\n' for pk in sorted(generated_packages)) +
        "))\n"
        "\n"
        "\n"
        "def __getattr__(name):\n"
        "    if name not in _PACKAGES:\n"
        "        raise AttributeError(f\"module {__name__!r} has no attribute {name!r}\")\n"
        "    return _importlib.import_module(f\"{__name__}.{name}\")\n"
        "\n"
        "\n"
        "def __dir__():\n"
        "    return sorted(set(globals()) | _PACKAGES)\n"
        "\n"
        "\n"
        "__all__ = sorted(_PACKAGES)\n")
    # `import nanocct.all` loads every toolkit, in dependency order: on macOS Gatekeeper verifies each dylib the
    # first time it is loaded, so warming all of them once after installing a wheel is cheaper than paying for it
    # scattered through a session. It is *not* needed for DE_Wrapper:
    # nanocct does not bind DE_PluginHolder<T> (a class template no typedef instantiates, R-TEMPLATE-SKIP: "template (not bound)" in the
    # report), so a provider is registered by an explicit `wrapper.Bind(DEBREP_ConfigurationNode())` whatever has been
    # imported -- measured 2026-09-24.
    (py_root / "all.py").write_text(
        '''"""Load every nanocct toolkit: `import nanocct.all`.

Importing nanocct itself loads nothing, and `import nanocct.gp` loads only what gp needs. Use this module when you
want all of it at once:

* after installing a wheel on macOS, so Gatekeeper verifies the OCCT libraries once rather than during your work;
* whenever you would rather have everything to hand than think about which package you need.

It is *not* required for `DE_Wrapper`: nanocct does not bind `DE_PluginHolder<T>`, so a format provider is
registered by an explicit `wrapper.Bind(DEBREP_ConfigurationNode())` regardless of what has been imported.

Generated by the nanocct generator; the order is the dependency order (Design.md 5.1, Binding-Rules.md 6a).
"""
'''
        + "".join(f"import nanocct._{tk}  # noqa: F401\n" for tk in ordered)
        + "\nTOOLKITS = (\n" + "".join(f'    "{tk}",\n' for tk in ordered) + ")\n")
    manifest_path.write_text(json.dumps({"classes": dict(sorted(known.items())), "templates": dict(sorted(templates.items())),
                                         "packages": dict(sorted(generated_pkgs.items())), "order": manifest["order"],
                                         "links": dict(sorted(manifest.get("links", {}).items())),
                                         "namespaces": dict(sorted(manifest["namespaces"].items())), "paths": dict(sorted(paths.items())),
                                         "bases": dict(sorted(bases.items())),
                                         "keepers": sorted(n for n in keepers if n in known),
                                         "kept": sorted(n for n in kept_classes if n in known)}, indent=0) + "\n")
    # per-toolkit cost: where the time goes, and what a dependency layering could at best overlap
    if len(per_toolkit) > 1:
        rows = sorted(per_toolkit.items(), key=lambda kv: -(kv[1]["parse"] + kv[1]["emit"]))
        print("per-toolkit seconds (parse + emit):", file=sys.stderr)
        for name, t in rows:
            print(f"    {name:<14} {t['parse']:7.1f} {t['emit']:7.1f} {t['parse'] + t['emit']:7.1f}", file=sys.stderr)
    docs, warnings = template_docs(tree.include_dir, clang_args(tree))
    (cpp_root / "common").mkdir(parents=True, exist_ok=True)
    (cpp_root / "common" / "ncollection_docs.h").write_text(docs)
    for w in warnings:
        print(f"    - {w}", file=sys.stderr)
    links = {tk: libs for tk, libs in sorted(manifest.get("links", {}).items()) if len(libs) > 0}
    (cpp_root / "toolkits.cmake").write_text(
        "# Generated by the nanocct generator. Do not edit.\n"
        "# Order = link order: every toolkit after its dependencies.\nset(NANOCCT_TOOLKITS "
        + " ".join(_topo(tree, generated_toolkits)) + ")\n"
        + "# Toolkits whose types a module names although OCCT's own EXTERNLIB does not link them (R-LINK):\n"
        + "".join(f"set(NANOCCT_{tk}_EXTRA_LIBS {' '.join(libs)})\n" for tk, libs in links.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
