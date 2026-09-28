"""Generate the OCP shim's Python modules from the OCP spec and nanocct's own signatures. Needs nanocct importable.

    python shim/generate.py            (normally called by build_wheel.py)

Input: ocp-8.0.1.0.0.json (names per OCP module) and ocp-8.0.1.0.0-members.json (every member's OCP signatures), both
from shim/extract_spec.py. Output, as {path: text}:

- OCP/__init__.py        loads every nanocct toolkit, then OCP/_patches.py (importing a toolkit AFTER its base classes
                         were patched aborts nanobind -- measured 2026-09-25, cause unknown)
- OCP/_patches.py        every adaptation, decided here and not at call time. Phase 1 takes the ORIGINAL callables,
                         phase 2 assigns: a subclass never wraps its base's wrapper. Per member and argument count:
                         an alias where only OCP's `_s` name is missing; a specialised function with fixed argument
                         indices, fill and result shape where one OCP overload and one nanocct overload decide it; the
                         dynamic adapter of OCP/_rt.py where only the argument types at call time can.
- OCP/<pkg>/__init__.py  `from nanocct.<pkg> import ...` of the names OCP exposes there (OCP.collections: aliases).

This is monkey-patching of nanocct, the one deliberate exception to the project rule, confined to this throwaway shim
(the user's decision, 2026-09-25): a subclass would break isinstance() for objects C++ returns, and nanobind's
metaclass cannot be subclassed to repair that. nanocct is untouched unless `OCP` is imported.
"""
import importlib
import importlib.util
import json
import sys
import types
from collections import Counter
from pathlib import Path

import nanocct.all  # noqa: F401  every toolkit, as at runtime

HERE = Path(__file__).parent
_spec = importlib.util.spec_from_file_location("ocp_shim_rt", HERE / "OCP" / "_rt.py")
rt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rt)

OCP_VERSION = "8.0.1.0"
PRIMITIVES = {"float", "int", "bool", "str"}


def tuple_len(ret: str) -> int | None:
    return len(rt.split_top(ret[len("tuple["):-1])) if ret.startswith("tuple[") else None


def nano_sigs(fn) -> list[tuple[list[tuple[str, str, bool]], str]]:
    out = []
    for entry in getattr(fn, "__nb_signature__", ()):
        m = rt._SIG.match(entry[0])
        if m is not None:
            out.append((rt.params(m.group(2)), m.group(3).strip()))
    return out


def shape_expr(nt: int | None, ocp_ret: str) -> str | None:
    """Python expression turning nanocct's result `r` into OCP's; None when the shapes cannot be matched statically."""
    if ocp_ret == "None":
        return "None"
    ot = tuple_len(ocp_ret)
    if ot is not None:
        if nt is None:
            return "(r,)"
        if nt == ot:
            return "r"
        return f"r[{nt - ot}:]" if nt > ot else None
    return "r[0]" if nt is not None else "r"


def plan(ocp: list, nano: list, n: int):
    """How a call with n arguments (self excluded) maps onto nanocct, decided statically -- or None if it cannot be."""
    fits = [o for o in ocp if o.fits(n)]
    if len(fits) != 1:
        return None
    o = fits[0]
    names = o.names[:n]
    known = {p for ps, _ in nano for p, _, _ in ps}
    keep = [i for i, p in enumerate(names) if p in known]
    drop = [i for i in range(n) if i not in keep]
    kept = [names[i] for i in keep]
    cands = [(ps, ret) for ps, ret in nano
             if {p for p, _, d in ps if not d} <= set(kept) and set(kept) <= {p for p, _, _ in ps}]
    if len(cands) != 1:
        return None
    ps, nret = cands[0]
    if kept != [p for p, _, _ in ps][:len(kept)]:
        return None                                  # nanocct takes them in another order: positional passing is wrong
    nt = tuple_len(nret)
    if len(drop) > 0 and (nt is None and len(drop) > 1 or nt is not None and len(drop) > nt):
        return None
    shape = shape_expr(nt, o.ret)
    if shape is None:
        return None
    fill = None
    if len(drop) > 0 and not all(o.types[i] in PRIMITIVES for i in drop):
        # OCP callers pass float()/int placeholders for primitive out-parameters; only containers, attributes and
        # streams have anything to receive, so a primitive-only drop needs no fill at all (decided here, not per call)
        fill = f"r[{nt - len(drop)}:]" if nt is not None else "(r,)"
    return keep, drop, fill, shape


def direct_shapes(ocp: list, nano: list, arities: list[int]) -> dict[int, str] | None:
    """For a member whose overload only the argument types decide: when every argument count has ONE OCP return shape
    and nanocct returns one shape, the call can go straight through with a fixed result shape; only a TypeError
    (an OCP-style call nanocct does not take) needs the dynamic adapter. None when the shape depends on the overload."""
    nshapes = {tuple_len(r) for _, r in nano}
    if len(nshapes) != 1 or len(arities) == 0:
        return None
    nt = next(iter(nshapes))
    out = {}
    for n in arities:
        rets = {o.ret if not o.ret.startswith("tuple[") else f"tuple{tuple_len(o.ret)}" for o in ocp if o.fits(n)}
        if len(rets) != 1:
            return None
        ret = next(o.ret for o in ocp if o.fits(n))
        shape = shape_expr(nt, ret)
        if shape is None:
            return None
        out[n] = shape
    return out


def emit_direct(fid: str, orig: str, dynamic: str, shapes: dict[int, str], bound: bool) -> list[str]:
    lines = [f"def {fid}(*a, _o={orig}, _d={dynamic}, **k):",
             "    try:",
             "        r = _o(*a, **k)",
             "    except TypeError:",
             "        return _d(*a, **k)",
             f"    n = len(a){' - 1' if bound else ''}"]
    for n, shape in sorted(shapes.items()):
        if shape != "r":
            lines.append(f"    if n == {n}:")
            lines.append(f"        return {shape}")
    lines.append("    return r")
    return lines


def emit_function(fid: str, orig: str, plans: dict, bound: bool) -> list[str]:
    off = 1 if bound else 0
    # the original is bound as a default, not looked up as a module global: _patches.py deletes its globals at the end,
    # so that no module state keeps nanobind objects alive past nanobind's exit leak check
    lines = [f"def {fid}(*a, _o={orig}, **k):",
             f"    if k:",
             f"        return _o(*a, **k)",
             f"    n = len(a){' - 1' if bound else ''}"]
    for n, (keep, drop, fill, shape) in sorted(plans.items()):
        args = (["a[0]"] if bound else []) + [f"a[{i + off}]" for i in keep]
        lines.append(f"    if n == {n}:")
        lines.append(f"        r = _o({', '.join(args)})")
        if fill is not None:
            dropped = ", ".join(f"a[{i + off}]" for i in drop) + ("," if len(drop) == 1 else "")
            lines.append(f"        _rt.fill(({dropped}), {fill})")
        lines.append(f"        return {shape}")
    lines.append("    return _o(*a)")
    return lines


def collision_siblings(obj, source: str, ocp: list) -> dict[int, str]:
    """{argument count: nanocct member} where an OCP call means nanocct's R-COLLISION sibling rather than the plain name.

    nanocct binds the out-parameter form of a colliding overload as `<name>__<type>__…` and keeps the plain name for the
    overload without out-parameters (Design.md 6 R-COLLISION): since 2026-09-27 `gp_Pnt.Coord()` returns the gp_XYZ
    and `Coord__float__float__float()` the numbers. OCP binds both under one name, and where every OCP overload that
    fits an argument count takes the same argument types, pybind always calls the first -- so where that first one
    returns a tuple, the call means the sibling with the same parameters and the same tuple length."""
    sibs = {a: getattr(obj, a) for a in dir(obj) if a.startswith(source + "__") and callable(getattr(obj, a))}
    out: dict[int, str] = {}
    if len(sibs) == 0:
        return out
    for n in sorted({n for o in ocp for n in range(o.required, len(o.names) + 1)}):
        fit = [o for o in ocp if o.fits(n)]
        if len({tuple(o.types[:n]) for o in fit}) != 1 or not fit[0].ret.startswith("tuple["):
            continue
        want = (fit[0].names[:n], tuple_len(fit[0].ret))
        match = sorted(a for a, f in sibs.items() for ps, r in nano_sigs(f)
                       if [p for p, _, d in ps if not d] == want[0] and tuple_len(r) == want[1])
        if len(match) == 1:
            out[n] = match[0]
    return out


def main() -> dict[str, str]:
    names_spec = json.loads((HERE / "ocp-8.0.1.0.0.json").read_text())["modules"]
    members = json.loads((HERE / "ocp-8.0.1.0.0-members.json").read_text())
    stats: Counter = Counter()
    head = ['"""Generated by shim/generate.py from OCP 8.0.1 and nanocct\'s signatures. Do not edit."""',
            "from OCP import _rt", ""]
    phase1: list[str] = []
    phase2: list[str] = []
    mods: dict[str, str] = {}
    counter = 0
    phase3: list[str] = []                            # R-COLLISION siblings, wrapping what phase 2 installed

    def mod_var(pkg: str) -> str:
        # A package another platform does not build (Cocoa is macOS-only, overrides.toml [platform]) must not break
        # `import OCP` there: the wheel is py3-none-any, generated on one platform and installed on all three.
        if pkg not in mods:
            mods[pkg] = f"m_{pkg}"
            head.append(f"m_{pkg} = _rt.module({pkg!r})")
        return mods[pkg]

    def guarded(cond: str, lines: list[str]) -> list[str]:
        """Every patch runs only if its originals exist HERE: members differ by platform (R-UNDEFINED on Windows)."""
        return [f"if {cond}:"] + [("    " + line) if line != "" else "" for line in lines] + [""]

    for pkg in sorted(members):
        try:
            nmod = importlib.import_module(f"nanocct.{pkg}")
        except ImportError:
            continue
        for cname, cm in sorted(members[pkg].items()):
            obj = getattr(nmod, cname, None)
            if obj is None and cname == pkg:
                obj = nmod
            if obj is None or not (isinstance(obj, type) or isinstance(obj, types.ModuleType)):
                continue
            is_module = isinstance(obj, types.ModuleType)
            mv = mod_var(pkg)
            owner = mv if is_module else f"{mv}.{cname}"
            cls_arg = "None" if is_module else repr(cname)
            for name, info in sorted(cm.items()):
                if info["kind"] == "property":
                    getter, setter = getattr(obj, name, None), getattr(obj, "Set" + name, None)
                    if not is_module and callable(getter) and callable(setter) and not isinstance(getter, property):
                        g, s = f"_o{counter}", f"_o{counter + 1}"
                        counter += 2
                        phase1 += [f"{g} = _rt.get({mv}, {cls_arg}, {name!r})", f"{s} = _rt.get({mv}, {cls_arg}, {'Set' + name!r})"]
                        phase2 += guarded(f"{g} is not None and {s} is not None",
                                          [f"{owner}.{name} = property(lambda self, g={g}: g(self), lambda self, v, s={s}: s(self, v))"])
                        stats["property"] += 1
                    continue
                is_static = name.endswith("_s")
                plain = name[:-2] if is_static else name
                # nanocct suffixes every class static like OCP (R-STATIC-S, 2026-09-26), so a class member keeps its OCP
                # name; only a namespace function (a module owner here: OCP's class, nanocct's package) is plain
                source = plain if is_module else name
                if is_module and hasattr(obj, name):
                    continue                          # the module has the OCP spelling itself
                siblings = {} if is_module else collision_siblings(obj, source, rt.ocp_overloads(info["sigs"]))
                if len(siblings) > 0:
                    s_ids = {}
                    for sib in sorted(set(siblings.values())):
                        s_ids[sib] = f"_o{counter}"
                        counter += 1
                        phase1.append(f"{s_ids[sib]} = _rt.get({mv}, {cls_arg}, {sib!r})")
                    fid = f"_p{counter}"
                    counter += 1
                    off = " - 1" if not is_static else ""
                    defaults = "".join(f"_s{n}={s_ids[s]}, " for n, s in sorted(siblings.items()))
                    # phase 3 runs after phase 2, so _f is whatever phase 2 installed (or the original, or nothing:
                    # Quantity_Period has only Values__int__…, no plain Values)
                    body = [f"def {fid}(*a, {defaults}_f=getattr({owner}, {name!r}, None), **k):",
                            f"    n = len(a){off}"]
                    for n, _ in sorted(siblings.items()):
                        body += [f"    if n == {n} and not k:", f"        return _s{n}(*a)"]
                    body += ["    if _f is None:",
                             f"        raise TypeError({(cname + '.' + name + ': no nanocct overload for these arguments')!r})",
                             "    return _f(*a, **k)",
                             f"{owner}.{name} = {'staticmethod(' + fid + ')' if is_static else fid}"]
                    phase3 += guarded(" and ".join(f"{s_ids[s]} is not None" for s in sorted(s_ids)), body)
                    stats["collision sibling"] += 1
                target = getattr(obj, source, None)
                if target is None or not callable(target) or isinstance(target, type):
                    continue
                ocp = rt.ocp_overloads(info["sigs"])
                nano = nano_sigs(target)
                if source == name and not rt.differs(ocp, [([p for p, _, _ in ps], r) for ps, r in nano]):
                    continue                          # same name, same signatures: nothing to adapt
                arities = sorted({n for o in ocp for n in range(o.required, len(o.names) + 1)})
                plans = {n: plan(ocp, nano, n) for n in arities}
                o_id = f"_o{counter}"
                counter += 1
                phase1.append(f"{o_id} = _rt.get({mv}, {cls_arg}, {source!r})")
                wrap = (lambda f: f) if is_module else ((lambda f: f"staticmethod({f})") if is_static else (lambda f: f))
                bound = not is_static and not is_module
                cond = f"{o_id} is not None"
                if len(arities) > 0 and all(p is not None for p in plans.values()):
                    identity = all(len(p[1]) == 0 and p[3] == "r" and p[0] == list(range(n)) for n, p in plans.items())
                    if identity and source == name:
                        continue                      # the signatures differ only in ways the call does not see
                    if identity and is_static:
                        phase2 += guarded(cond, [f"{owner}.{name} = {wrap(o_id)}"])
                        stats["alias"] += 1
                        continue
                    fid = f"_p{counter}"
                    counter += 1
                    phase2 += guarded(cond, emit_function(fid, o_id, plans, bound) + [f"{owner}.{name} = {wrap(fid)}"])
                    stats["specialised"] += 1
                else:
                    call = f"_rt.dynamic_from({o_id}, {info['sigs']!r}, {bound})"
                    shapes = direct_shapes(ocp, nano, arities)
                    if shapes is None:
                        phase2 += guarded(cond, [f"{owner}.{name} = {wrap(call)}"])
                        stats["dynamic"] += 1
                        continue
                    fid = f"_p{counter}"
                    counter += 1
                    phase2 += guarded(cond, emit_direct(fid, o_id, call, shapes, bound) + [f"{owner}.{name} = {wrap(fid)}"])
                    stats["direct + dynamic fallback"] += 1

    files: dict[str, str] = {}
    tail = ["", "# The originals and module references are needed only while patching. Kept as globals they hold nanobind",
            "# functions (and, through their default arguments, types and instances) alive past nanobind's exit leak",
            "# check, which then reports thousands of leaks (measured 2026-09-26). The wrappers hold what they need.",
            "for _name in [n for n in globals() if n.startswith((\"_o\", \"_p\", \"m_\"))]:",
            "    del globals()[_name]",
            "del _name"]
    files["OCP/_patches.py"] = "\n".join(head + ["", "# phase 1: the original callables"] + phase1
                                         + ["", "# phase 2: OCP's conventions"] + phase2
                                         + ["", "# phase 3: calls OCP resolves to an R-COLLISION sibling in nanocct"] + phase3
                                         + tail) + "\n"
    files["OCP/__init__.py"] = (
        '"""OCP 8.0.1 API on nanocct (cadquery-ocp-novtk compatibility wheel). Generated by shim/generate.py."""\n'
        f'__version__ = "{OCP_VERSION}"\n\n'
        "import nanocct.all  # noqa: F401  every toolkit BEFORE patching: importing one after its bases were patched aborts nanobind\n"
        "from OCP import _patches  # noqa: F401,E402\n")
    # the modules
    nc = importlib.import_module("nanocct.NCollection")
    table: dict[str, str] = {}
    for n in dir(nc):
        if n.startswith("NCollection_") and "__" in n:
            kind, _, args = n[len("NCollection_"):].partition("__")
            for key in (args, args.replace("Handle_", ""), args.replace("Handle_", "").replace("NCollection_", "")):
                table.setdefault(kind + "_" + key.replace("__", "_"), n)
    for pkg, v in sorted(names_spec.items()):
        doc = f'"""OCP.{pkg} on nanocct. Generated by shim/generate.py."""\n'
        if pkg == "collections":
            pairs = [(table[o], o) for o in v["names"] if o in table]
            body = "".join(f"from nanocct.NCollection import {a} as {b}\n" for a, b in pairs)
            stats["collections"] += len(pairs)
        else:
            try:
                nmod = importlib.import_module(f"nanocct.{pkg}")
            except ImportError:
                files[f"OCP/{pkg}/__init__.py"] = doc
                stats["module without nanocct counterpart"] += 1
                continue
            present = [n for n in v["names"] if hasattr(nmod, n)]
            body = ""
            if pkg in v["names"] and not hasattr(nmod, pkg):     # OCP.TopoDS.TopoDS; but BRepGProp.BRepGProp is a class
                body += f"import nanocct.{pkg} as {pkg}  # OCP.{pkg}.{pkg}: the namespace is the package module\n"
            if present:
                body += f"from nanocct.{pkg} import (\n" + "".join(f"    {n},\n" for n in present) + ")\n"
            stats["names"] += len(present)
        files[f"OCP/{pkg}/__init__.py"] = doc + body
    print("generated:", dict(sorted(stats.items())), file=sys.stderr)
    return files


if __name__ == "__main__":
    for path, text in main().items():
        print(f"{path}: {len(text)} bytes")
