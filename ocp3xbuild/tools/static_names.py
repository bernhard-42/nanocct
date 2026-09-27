"""Bring `Cls.Static(...)` calls in Python sources to OCP3x's names, in place: `Cls.Name` -> `Cls.Name_s` (and
`Cls.Name__suffix` -> `Cls.Name_s__suffix`) wherever the class has the suffixed static and no plain member of that name.

    python ocp3xbuild/tools/static_names.py <file or directory>...

For code written against OCP3x before 2026-09-26, when only colliding statics carried `_s` (R-STATIC-S), and for the
hand-written lines of a ocp3xbuild patch. Decided by the live build, OCP3x must be importable. String literals are
searched too, so `mock.patch("pkg.module.BRep_Tool.Surface")` is renamed with the call it patches. A static called
through an instance (`shape_tool.GetShape(label)`) is not recognised: the owner is not a class name.
"""
import inspect
import io
import re
import sys
import tokenize
from pathlib import Path

import OCP3x.all  # noqa: F401  every toolkit, so every class is known

CLASSES: dict[str, list[type]] = {}     # short name -> every bound class of that name (nested classes can share one)


def _collect(owner, depth: int) -> None:
    for name, obj in vars(owner).items():
        if inspect.isclass(obj) and getattr(obj, "__module__", "").startswith("OCP3x"):
            seen = CLASSES.setdefault(name, [])
            if obj not in seen:
                seen.append(obj)
                if depth < 3:
                    _collect(obj, depth + 1)


for _name, _mod in list(sys.modules.items()):
    if _name.startswith("OCP3x.") and _mod is not None:
        _collect(_mod, 0)

# every `A.B` pair, overlapping, so `OCP3x.BRep.BRep_Tool.Surface` yields (BRep, BRep_Tool) and (BRep_Tool, Surface)
PAIR = re.compile(r"(?<!\w)(?=([A-Za-z_]\w*)\.([A-Za-z_]\w*)\b)")


def renamed(owner: str, attr: str) -> str | None:
    if attr.endswith("_s") or "_s__" in attr:
        return None
    base, sep, rest = attr.partition("__")
    new = base + "_s" + sep + rest
    for cls in CLASSES.get(owner, []):
        if hasattr(cls, new) and hasattr(cls, attr) is False:
            return new
    return None


def fix_file(p: Path) -> int:
    src = p.read_text()
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    except (tokenize.TokenError, SyntaxError):
        return 0
    offs = [0]
    for line in src.splitlines(keepends=True):
        offs.append(offs[-1] + len(line))

    def pos(rc: tuple[int, int]) -> int:
        return offs[rc[0] - 1] + rc[1]

    edits: set[tuple[int, int, str]] = set()
    for i, t in enumerate(toks):
        if i >= 2 and t.type == tokenize.NAME and toks[i - 1].string == "." and toks[i - 2].type == tokenize.NAME:
            new = renamed(toks[i - 2].string, t.string)
            if new is not None:
                edits.add((pos(t.start), pos(t.end), new))
        elif t.type == tokenize.STRING:
            for m in PAIR.finditer(t.string):
                new = renamed(m.group(1), m.group(2))
                if new is not None:
                    at = pos(t.start) + m.start(2)
                    edits.add((at, at + len(m.group(2)), new))
    if len(edits) == 0:
        return 0
    for s, e, txt in sorted(edits, reverse=True):
        src = src[:s] + txt + src[e:]
    p.write_text(src)
    return len(edits)


def main() -> None:
    total = 0
    for arg in sys.argv[1:]:
        p = Path(arg)
        for f in (sorted(p.rglob("*.py")) if p.is_dir() else [p]):
            n = fix_file(f)
            if n > 0:
                print(f, n)
                total += n
    print("renamed", total)


if __name__ == "__main__":
    main()
