"""Make an instrumented copy of the shim's OCP package that records every call site the shim adapts.

    python ocp3xbuild/tools/trace_shim.py <OCP dir of the built shim> <output dir>
    OCP_TRACE=calls.jsonl PYTHONPATH=<output dir>:<package sources> python -m pytest tests

Every phase-2 assignment of the generated OCP/_patches.py is wrapped, so a run of a package's suite through the shim
writes one JSON line per (member, category, file, line) at exit, with a call count. The categories come from the
shim generator: `alias` (only the `_s` name was missing -- port.py does these), `special` (a specialised wrapper:
argument drop, fill or result shape), `dynamic` (decided by argument types at call time) and `property`. The
non-alias ones are the candidates for hand porting; a native run of the tests decides which of them actually break.
Only executed code is recorded -- a path no test reaches is invisible here too.
"""
import re
import shutil
import sys
from pathlib import Path

TRACE_MODULE = '''"""Call-site recorder of the instrumented shim (ocp3xbuild/tools/trace_shim.py). Writes $OCP_TRACE at exit."""
import atexit
import json
import os
import sys

_hits = {}
_OUT = os.environ.get("OCP_TRACE")


def _site(depth):
    f = sys._getframe(depth)
    while f is not None and "/OCP/" in f.f_code.co_filename:
        f = f.f_back
    if f is None:
        return ("?", 0)
    return (f.f_code.co_filename, f.f_lineno)


def _rec(name, cat, depth):
    key = (name, cat) + _site(depth)
    _hits[key] = _hits.get(key, 0) + 1


def fn(name, cat, f):
    def w(*a, **k):
        _rec(name, cat, 2)
        return f(*a, **k)
    w.__name__ = getattr(f, "__name__", name.split(".")[-1])
    return w


def prop(name, p):
    def g(self):
        _rec(name, "property", 2)
        return p.fget(self)

    def s(self, v):
        _rec(name, "property", 2)
        return p.fset(self, v)
    return property(g, s if p.fset is not None else None)


@atexit.register
def _dump():
    if _OUT is None:
        return
    with open(_OUT, "a") as fh:
        for (name, cat, file, line), n in _hits.items():
            fh.write(json.dumps({"name": name, "cat": cat, "file": file, "line": line, "n": n}) + "\\n")
'''

ASSIGN = re.compile(r"^(\s+)(m_\w+\.(\w+)\.(\w+)) = (.+)$")


def category(expr: str) -> str:
    if re.fullmatch(r"_o\d+", expr) is not None:
        return "alias"
    if expr.startswith("_rt.dynamic_from"):
        return "dynamic"
    return "special"


def instrument(src: str) -> tuple[str, int]:
    out = []
    n = 0
    for line in src.splitlines():
        m = ASSIGN.match(line)
        if m is None:
            out.append(line)
            continue
        ind, target, cls, mem, expr = m.groups()
        name = f"{cls}.{mem}"
        if expr.startswith("property("):
            out.append(f"{ind}{target} = _T.prop({name!r}, {expr})")
        elif expr.startswith("staticmethod("):
            inner = expr[len("staticmethod("):-1]
            out.append(f"{ind}{target} = staticmethod(_T.fn({name!r}, {category(inner)!r}, {inner}))")
        else:
            out.append(f"{ind}{target} = _T.fn({name!r}, {category(expr)!r}, {expr})")
        n += 1
    text = "\n".join(out) + "\n"
    head = "from OCP import _rt\n"
    if text.count(head) != 1:
        raise RuntimeError("OCP/_patches.py does not import _rt the way this tool expects")
    return text.replace(head, head + "from OCP import _trace as _T\n", 1), n


def main() -> None:
    src_dir, out_dir = Path(sys.argv[1]), Path(sys.argv[2])
    target = out_dir / "OCP"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(src_dir, target)
    text, n = instrument((target / "_patches.py").read_text())
    (target / "_patches.py").write_text(text)
    (target / "_trace.py").write_text(TRACE_MODULE)
    print(f"wrapped {n} assignments -> {target}")


if __name__ == "__main__":
    main()
