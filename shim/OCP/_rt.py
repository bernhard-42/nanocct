"""Runtime helpers of the OCP shim (cadquery-ocp 8.0.1 API on OCP3x); the generated OCP/_patches.py calls them.

Most members are adapted by generated code specialised at build time (shim/generate.py). What stays dynamic lives
here: the signature parsing the generator shares, fill() for out-arguments OCP expects to be filled, and dynamic()
for the members whose OCP overload can only be chosen from the argument types at call time.
"""
import importlib
import re

_SIG = re.compile(r"^(?:def )?(\w+)\((.*)\) -> (.+)$")


# ---- signatures -------------------------------------------------------------------------------------------------

def split_top(text: str) -> list[str]:
    parts, depth, cur = [], 0, ""
    for ch in text:
        if ch in "[(<":
            depth += 1
        elif ch in "])>":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip() != "":
        parts.append(cur)
    return parts


def params(text: str) -> list[tuple[str, str, bool]]:
    """(name, last component of the annotated type, has_default) per parameter, without `self`."""
    out = []
    for p in split_top(text):
        head, _, default = p.partition("=")
        name, _, ann = head.partition(":")
        name = name.strip().lstrip("*")
        if name in ("self", "/", ""):
            continue
        typ = ann.strip().split("|")[0].strip().split("[")[0].split(".")[-1]
        out.append((name, typ, default.strip() != ""))
    return out


def param_names(text: str) -> list[str]:
    return [n for n, _, _ in params(text)]


class Overload:
    __slots__ = ("names", "types", "required", "ret")

    def __init__(self, params: list[tuple[str, str, bool]], ret: str):
        self.names = [n for n, _, _ in params]
        self.types = [t for _, t, _ in params]
        self.required = sum(1 for _, _, d in params if not d)
        self.ret = ret

    def fits(self, n: int) -> bool:
        return self.required <= n <= len(self.names)

    def score(self, args) -> int:
        """How many arguments match the annotated type by name (int/float/bool by Python type)."""
        hits = 0
        for a, t in zip(args, self.types):
            k = type(a).__name__
            if k == t or (t == "float" and isinstance(a, (int, float))) or (t == "int" and isinstance(a, int)) \
                    or any(b.__name__ == t for b in type(a).__mro__):
                hits += 1
        return hits


def ocp_overloads(sigs: list[str]) -> list[Overload]:
    out = []
    for s in sigs:
        m = _SIG.match(s)
        if m is not None:
            out.append(Overload(params(m.group(2)), m.group(3).strip()))
    return out


def nano_overloads(fn) -> list[tuple[list[str], str]]:
    out = []
    for entry in getattr(fn, "__nb_signature__", ()):
        m = _SIG.match(entry[0])
        if m is not None:
            out.append((param_names(m.group(2)), m.group(3).strip()))
    return out


# ---- the call adapter -------------------------------------------------------------------------------------------

def fill(dropped: list, values: tuple) -> None:
    """OCP fills caller-provided out-arguments; OCP3x returns them. Copy each returned value into the argument the
    caller holds: streams by write(), containers by Assign, OCAF attributes by Restore. Primitive placeholders are left alone."""
    for arg, value in zip(dropped, values):
        if value is None or arg is None or isinstance(arg, (int, float, bool, str)):
            continue
        if isinstance(value, (bytes, str)) and hasattr(arg, "write"):
            try:                                         # an ostream& argument: OCP writes into the caller's stream
                arg.write(value)
            except TypeError:                            # text formats (STEP, BREP) into a binary stream (BytesIO)
                arg.write(value.encode("utf-8") if isinstance(value, str) else value.decode("utf-8"))
        elif hasattr(arg, "Assign"):
            arg.Assign(value)
        elif hasattr(arg, "Restore") and hasattr(arg, "ID"):
            arg.Restore(value)


def shape(result, ocp_ret: str | None):
    """Return `result` the way OCP's overload returns it."""
    if ocp_ret is None:
        return result
    if ocp_ret == "None":
        return None
    if ocp_ret.startswith("tuple["):
        n = len(split_top(ocp_ret[len("tuple["):-1]))
        if not isinstance(result, tuple):
            return (result,)
        if n < len(result):
            return result[len(result) - n:]           # OCP returns only the out-values, OCP3x (result, *outs)
        return result
    if isinstance(result, tuple) and len(result) > 0:
        return result[0]
    return result


def dynamic(fn, ocp: list[Overload], nano: list[tuple[list[str], str]], bound: bool):
    """bound: an instance method (args[0] is self, which is not part of the parameter lists)."""
    def call(*args, **kwargs):
        head, rest = (args[:1], args[1:]) if bound else ((), args)
        cands = sorted((o for o in ocp if o.fits(len(rest))), key=lambda o: -o.score(rest))
        best_ret = cands[0].ret if len(cands) > 0 else None
        try:
            result = fn(*args, **kwargs)
        except TypeError:
            for o in cands:
                names = o.names[:len(rest)]
                for nano_names, _ in nano:
                    keep = [i for i, p in enumerate(names) if p in nano_names]
                    if len(keep) == len(names):
                        continue
                    try:
                        result = fn(*head, *[rest[i] for i in keep], **kwargs)
                    except TypeError:
                        continue
                    dropped = [rest[i] for i in range(len(names)) if i not in keep]
                    outs = result if isinstance(result, tuple) else (result,)
                    fill(dropped, outs[len(outs) - len(dropped):])
                    return shape(result, o.ret)
            # names that differ between OCP and OCP3x (TDF_Label.FindAttribute: GUID/Attribute vs anID): out-parameters
            # are trailing in practice, so drop from the end
            for k in range(1, len(rest) + 1):
                try:
                    result = fn(*head, *rest[:-k], **kwargs)
                except TypeError:
                    continue
                outs = result if isinstance(result, tuple) else (result,)
                fill(list(rest[-k:]), outs[len(outs) - k:])
                return shape(result, best_ret)
            raise
        return shape(result, best_ret)

    call.__name__ = getattr(fn, "__name__", "call")
    call.__doc__ = getattr(fn, "__doc__", None)
    return call


def differs(ocp: list[Overload], nano: list[tuple[list[str], str]]) -> bool:
    if len(nano) == 0 or len(ocp) == 0:
        return False
    nano_sets = [set(n) for n, _ in nano]
    for o in ocp:
        if not any(set(o.names[:o.required]) <= s for s in nano_sets):
            return True                                  # an OCP-only (out-)parameter
        if o.ret.startswith("tuple["):
            return True                                  # OCP's tuple shape
    if any(r.startswith("tuple[") for _, r in nano) and not all(o.ret.startswith("tuple[") for o in ocp):
        return True                                      # OCP3x returns (result, *outs) where OCP returns the result
    return False


def dynamic_from(fn, sigs: list[str], bound: bool):
    """The dynamic adapter for one member, from its OCP signature lines (embedded in the generated code)."""
    return dynamic(fn, ocp_overloads(sigs), nano_overloads(fn), bound)


# ---- helpers the generated OCP/_patches.py uses so that one py3-none-any wheel works on every platform ----------

def module(pkg: str):
    """OCP3x.<pkg>, or None where this platform does not build it (Cocoa off macOS)."""
    try:
        return importlib.import_module(f"OCP3x.{pkg}")
    except ImportError:
        return None


def get(mod, cls: str | None, name: str):
    """The original callable, or None where this platform does not bind it (R-UNDEFINED differs on Windows)."""
    if mod is None:
        return None
    owner = mod if cls is None else getattr(mod, cls, None)
    return None if owner is None else getattr(owner, name, None)
