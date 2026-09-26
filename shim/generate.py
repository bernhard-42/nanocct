"""Generate the OCP shim's Python modules from the OCP spec and nanoocp's own signatures. Needs nanoocp importable.

    python shim/generate.py            (normally called by build_wheel.py)

Input: ocp-8.0.1.0.0.json (names per OCP module) and ocp-8.0.1.0.0-members.json (every member's OCP signatures), both
from shim/extract_spec.py. Output, as {path: text}:

- OCP/__init__.py        loads every nanoocp toolkit, then OCP/_patches.py (importing a toolkit AFTER its base classes
                         were patched aborts nanobind -- measured 2026-09-25, cause unknown)
- OCP/_patches.py        every adaptation, decided here and not at call time. Phase 1 takes the ORIGINAL callables,
                         phase 2 assigns: a subclass never wraps its base's wrapper. Per member and argument count:
                         an alias where only OCP's `_s` name is missing; a specialised function with fixed argument
                         indices, fill and result shape where one OCP overload and one nanoocp overload decide it; the
                         dynamic adapter of OCP/_rt.py where only the argument types at call time can.
- OCP/<pkg>/__init__.py  `from nanoocp.<pkg> import ...` of the names OCP exposes there (OCP.collections: aliases).

This is monkey-patching of nanoocp, the one deliberate exception to the project rule, confined to this throwaway shim
(the user's decision, 2026-09-25): a subclass would break isinstance() for objects C++ returns, and nanobind's
metaclass cannot be subclassed to repair that. nanoocp is untouched unless `OCP` is imported.
"""
import importlib
import importlib.util
import json
import sys
import types
from collections import Counter
from pathlib import Path

import nanoocp.all  # noqa: F401  every toolkit, as at runtime

HERE = Path(__file__).parent
_spec = importlib.util.spec_from_file_location("ocp_shim_rt", HERE / "OCP" / "_rt.py")
rt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rt)

OCP_VERSION = "8.0.1.0"
RTTI = ("get_type_name", "get_type_descriptor")
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
    """Python expression turning nanoocp's result `r` into OCP's; None when the shapes cannot be matched statically."""
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
    """How a call with n arguments (self excluded) maps onto nanoocp, decided statically -- or None if it cannot be."""
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
        return None                                  # nanoocp takes them in another order: positional passing is wrong
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
    and nanoocp returns one shape, the call can go straight through with a fixed result shape; only a TypeError
    (an OCP-style call nanoocp does not take) needs the dynamic adapter. None when the shape depends on the overload."""
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


def main() -> dict[str, str]:
    names_spec = json.loads((HERE / "ocp-8.0.1.0.0.json").read_text())["modules"]
    members = json.loads((HERE / "ocp-8.0.1.0.0-members.json").read_text())
    stats: Counter = Counter()
    head = ['"""Generated by shim/generate.py from OCP 8.0.1 and nanoocp\'s signatures. Do not edit."""',
            "from OCP import _rt", ""]
    phase1: list[str] = []
    phase2: list[str] = []
    mods: dict[str, str] = {}
    counter = 0

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
            nmod = importlib.import_module(f"nanoocp.{pkg}")
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
            own = {} if is_module else vars(obj)
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
                if is_static and (name in own or (is_module and hasattr(obj, name))):
                    continue                          # nanoocp kept the suffix (R-STATIC-S)
                target = getattr(obj, plain, None)
                if target is None or not callable(target) or isinstance(target, type):
                    continue
                ocp = rt.ocp_overloads(info["sigs"])
                nano = nano_sigs(target)
                if not is_static and not rt.differs(ocp, [([p for p, _, _ in ps], r) for ps, r in nano]):
                    continue
                arities = sorted({n for o in ocp for n in range(o.required, len(o.names) + 1)})
                plans = {n: plan(ocp, nano, n) for n in arities}
                o_id = f"_o{counter}"
                counter += 1
                phase1.append(f"{o_id} = _rt.get({mv}, {cls_arg}, {plain!r})")
                wrap = (lambda f: f) if is_module else ((lambda f: f"staticmethod({f})") if is_static else (lambda f: f))
                bound = not is_static and not is_module
                cond = f"{o_id} is not None"
                if len(arities) > 0 and all(p is not None for p in plans.values()):
                    identity = all(len(p[1]) == 0 and p[3] == "r" and p[0] == list(range(n)) for n, p in plans.items())
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
            if not is_module and any(plain in own for plain in RTTI):
                phase2.append(f"_rt.rtti({mv}, {cname!r})")    # the default: OCP's RTTI `_s` names, from the class's OWN statics
                stats["rtti classes"] += 1

    files: dict[str, str] = {}
    tail = ["", "# The originals and module references are needed only while patching. Kept as globals they hold nanobind",
            "# functions (and, through their default arguments, types and instances) alive past nanobind's exit leak",
            "# check, which then reports thousands of leaks (measured 2026-09-26). The wrappers hold what they need.",
            "for _name in [n for n in globals() if n.startswith((\"_o\", \"_p\", \"m_\"))]:",
            "    del globals()[_name]",
            "del _name"]
    files["OCP/_patches.py"] = "\n".join(head + ["", "# phase 1: the original callables"] + phase1
                                         + ["", "# phase 2: OCP's conventions"] + phase2 + tail) + "\n"
    files["OCP/__init__.py"] = (
        '"""OCP 8.0.1 API on nanoocp (cadquery-ocp-novtk compatibility wheel). Generated by shim/generate.py."""\n'
        f'__version__ = "{OCP_VERSION}"\n\n'
        "import nanoocp.all  # noqa: F401  every toolkit BEFORE patching: importing one after its bases were patched aborts nanobind\n"
        "from OCP import _patches  # noqa: F401,E402\n")
    # the modules
    nc = importlib.import_module("nanoocp.NCollection")
    table: dict[str, str] = {}
    for n in dir(nc):
        if n.startswith("NCollection_") and "__" in n:
            kind, _, args = n[len("NCollection_"):].partition("__")
            for key in (args, args.replace("Handle_", ""), args.replace("Handle_", "").replace("NCollection_", "")):
                table.setdefault(kind + "_" + key.replace("__", "_"), n)
    for pkg, v in sorted(names_spec.items()):
        doc = f'"""OCP.{pkg} on nanoocp. Generated by shim/generate.py."""\n'
        if pkg == "collections":
            pairs = [(table[o], o) for o in v["names"] if o in table]
            body = "".join(f"from nanoocp.NCollection import {a} as {b}\n" for a, b in pairs)
            stats["collections"] += len(pairs)
        else:
            try:
                nmod = importlib.import_module(f"nanoocp.{pkg}")
            except ImportError:
                files[f"OCP/{pkg}/__init__.py"] = doc
                stats["module without nanoocp counterpart"] += 1
                continue
            present = [n for n in v["names"] if hasattr(nmod, n)]
            body = ""
            if pkg in v["names"] and not hasattr(nmod, pkg):     # OCP.TopoDS.TopoDS; but BRepGProp.BRepGProp is a class
                body += f"import nanoocp.{pkg} as {pkg}  # OCP.{pkg}.{pkg}: the namespace is the package module\n"
            if present:
                body += f"from nanoocp.{pkg} import (\n" + "".join(f"    {n},\n" for n in present) + ")\n"
            stats["names"] += len(present)
        files[f"OCP/{pkg}/__init__.py"] = doc + body
    print("generated:", dict(sorted(stats.items())), file=sys.stderr)
    return files


if __name__ == "__main__":
    for path, text in main().items():
        print(f"{path}: {len(text)} bytes")
