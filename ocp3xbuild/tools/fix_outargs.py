"""Rewrite OCP's ignored First/Last out-arguments of the BRep_Tool curve accessors, in place.

    python ocp3xbuild/tools/fix_outargs.py <directory>...

OCP binds `BRep_Tool::Curve(E, First&, Last&)` (and CurveOnSurface(E, F, First&, Last&), CurveOnPlane(E, S, L,
First&, Last&)) returning only the curve: whatever is passed for First/Last is discarded. OCP3x returns them
(R-OUT): `curve, first, last = BRep_Tool.Curve_s(E)`. So `BRep_Tool.Curve_s(e, a, b)` becomes
`BRep_Tool.Curve_s(e)[0]` -- the same value, whatever a and b were. The names are the same in OCP and OCP3x
(R-STATIC-S), so it can run before or after port.py.
"""
import ast
import sys
from pathlib import Path

# positional arity of the OCP call whose last two arguments are the ignored out-parameters
ARITY = {"Curve_s": 3, "CurveOnSurface_s": 4, "CurveOnPlane_s": 5}


def fix_file(p: Path) -> int:
    src = p.read_text()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return 0
    lines = src.splitlines(keepends=True)
    offs = [0]
    for ln in lines:
        offs.append(offs[-1] + len(ln))
    edits = []
    for n in ast.walk(tree):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and isinstance(n.func.value, ast.Name)
                and n.func.value.id == "BRep_Tool" and n.func.attr in ARITY
                and len(n.args) == ARITY[n.func.attr] and len(n.keywords) == 0):
            start = offs[n.lineno - 1] + n.col_offset
            end = offs[n.end_lineno - 1] + n.end_col_offset
            args = ", ".join(ast.get_source_segment(src, a) for a in n.args[:-2])
            edits.append((start, end, f"BRep_Tool.{n.func.attr}({args})[0]"))
    if len(edits) == 0:
        return 0
    for s, e, t in sorted(edits, reverse=True):
        src = src[:s] + t + src[e:]
    p.write_text(src)
    return len(edits)


def main() -> None:
    for root in sys.argv[1:]:
        for p in sorted(Path(root).rglob("*.py")):
            n = fix_file(p)
            if n > 0:
                print(p, n)


if __name__ == "__main__":
    main()
