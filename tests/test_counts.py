"""The counts of the generated code, pinned per platform (PINNED): how often each binding rule fires, taken from the
generated sources, the generator's reports, the manifest and the stubs. They are the evidence for the rules in
docs/Binding-Rules.md, which describe the rules without repeating the numbers.

A generator change or an OCCT update moves them; the test then fails with the key, the pinned and the found value and
prints the complete table to adopt, and the pin is updated on purpose -- a count cannot move unseen."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from collections.abc import Callable
from pathlib import Path

import pytest

from test_lifetime_counts import COPY_TAIL

ROOT = Path(__file__).parents[1]
CPP = ROOT / "src" / "cpp"

# The counts this platform's generation must produce, one complete table per platform: the truth the generated code is
# checked against. Why the platforms differ (tests/test_lifetime_counts.py pins its numbers per platform for the same
# reasons):
# - OCCT's headers differ: WNT_Window and WNT_WClass exist only under #if defined(_WIN32), Cocoa only on macOS;
# - the export tables differ: macOS and Linux export everything a header declares, MSVC only what OCCT marks
#   Standard_EXPORT, so R-UNDEFINED drops more members on Windows (undefined-lines), and with them what they used;
# - types differ: size_t is unsigned long long on Windows (LLP64), and Aspect_Drawable is void* there and unsigned
#   long elsewhere -- a void* member makes the layout rule keep constructor arguments (the kept-* counts).
PINNED: dict[str, dict[str, int]] = {
    "darwin": {                                    # the numbers docs/*.md quoted until 2026-10-23, not yet measured here
        "alias-result": 46,
        "array-lines": 7,
        "bitset": 19,
        "copy-heap": 20,
        "copy-keep-original": 528,
        "copy-no-ctor": 308,
        "cstr-null": 15,
        "ctor-keep": 568,
        "default-braced": 8,
        "enum-arg": 2639,
        "iter-keeps": 20,
        "kept-base": 7,
        "kept-classes": 54,
        "kept-ctor-args-cpp": 31,
        "kept-own": 47,
        "kept-slots-cpp": 106,
        "lifetime-lines": 91,
        "lifetime-topopebrepbuild": 56,
        "method-keep-files": 50,
        "method-keep-slots": 811,
        "ncollection-eager": 33,
        "null-bool": 7,
        "optional-ptr": 59,
        "overload-order": 53,
        "owner-args": 114,
        "owner-files": 19,
        "owner-results": 448,
        "owner-tuple": 17,
        "refwrap": 5,
        "result-keep-args": 308,
        "result-keep-results": 207,
        "result-refcount0": 71,
        "result-value-transient": 12,
        "str-ops": 40,
        "stub-enum-defaults": 217,
        "unbound-type": 38,
        "undefined-lines": 133,
        "unhashable": 57,
        "unreachable": 72,
        "view-guard-iterators": 23,
        "view-guard-lambda": 106,
        "view-guard-lines": 149,
        "view-guard-params": 1867,
        "view-guard-toolkits": 35,
        "view-guard-wrapped": 1102,
    },
    "linux": {                                     # measured 2026-10-23 (WSL 2, the manylinux container)
        "alias-result": 46,
        "array-lines": 7,
        "bitset": 19,
        "copy-heap": 20,
        "copy-keep-original": 528,
        "copy-no-ctor": 306,
        "cstr-null": 15,
        "ctor-keep": 567,
        "default-braced": 8,
        "enum-arg": 2639,
        "iter-keeps": 20,
        "kept-base": 7,
        "kept-classes": 54,
        "kept-ctor-args-cpp": 31,
        "kept-own": 47,
        "kept-slots-cpp": 106,
        "lifetime-lines": 91,
        "lifetime-topopebrepbuild": 56,
        "method-keep-files": 50,
        "method-keep-slots": 811,
        "ncollection-eager": 33,
        "null-bool": 7,
        "optional-ptr": 59,
        "overload-order": 53,
        "owner-args": 114,
        "owner-files": 19,
        "owner-results": 448,
        "owner-tuple": 17,
        "refwrap": 5,
        "result-keep-args": 308,
        "result-keep-results": 207,
        "result-refcount0": 71,
        "result-value-transient": 12,
        "str-ops": 40,
        "stub-enum-defaults": 217,
        "unbound-type": 39,
        "undefined-lines": 99,
        "unhashable": 57,
        "unreachable": 72,
        "view-guard-iterators": 23,
        "view-guard-lambda": 106,
        "view-guard-lines": 149,
        "view-guard-params": 1867,
        "view-guard-toolkits": 35,
        "view-guard-wrapped": 1102,
    },
    "win32": {                                     # measured 2026-10-23
        "alias-result": 46,
        "array-lines": 7,
        "bitset": 19,
        "copy-heap": 20,
        "copy-keep-original": 528,
        "copy-no-ctor": 313,
        "cstr-null": 15,
        "ctor-keep": 565,
        "default-braced": 8,
        "enum-arg": 2580,
        "iter-keeps": 20,
        "kept-base": 7,
        "kept-classes": 58,
        "kept-ctor-args-cpp": 34,
        "kept-own": 51,
        "kept-slots-cpp": 109,
        "lifetime-lines": 91,
        "lifetime-topopebrepbuild": 56,
        "method-keep-files": 53,
        "method-keep-slots": 812,
        "ncollection-eager": 33,
        "null-bool": 7,
        "optional-ptr": 61,
        "overload-order": 53,
        "owner-args": 114,
        "owner-files": 19,
        "owner-results": 448,
        "owner-tuple": 17,
        "refwrap": 5,
        "result-keep-args": 305,
        "result-keep-results": 207,
        "result-refcount0": 71,
        "result-value-transient": 12,
        "str-ops": 40,
        "stub-enum-defaults": 219,
        "unbound-type": 35,
        "undefined-lines": 277,
        "unhashable": 57,
        "unreachable": 72,
        "view-guard-iterators": 23,
        "view-guard-lambda": 106,
        "view-guard-lines": 149,
        "view-guard-params": 1863,
        "view-guard-toolkits": 35,
        "view-guard-wrapped": 1100,
    },
}


def _sources() -> dict[Path, str]:
    return {p: p.read_text(encoding="utf-8") for p in sorted(CPP.glob("TK*/*.cpp"))}


def _report() -> list[tuple[str, str, str]]:
    rows = []
    for p in sorted(CPP.glob("TK*/report.txt")):
        for line in p.read_text(encoding="utf-8").splitlines():
            if not line.startswith("#") and line != "":
                category, package, message = line.split("\t", 2)
                rows.append((category, package, message))
    return rows


def _keep_views(text: str) -> Counter[str]:
    """keep_view<R, Owned, Nurse, Elem, Patients...> (nanocct_call_policies.h): R-OWNER when Owned; a result when Nurse is 0, an
    argument written into otherwise; a tuple element when Elem >= 0."""
    out: Counter[str] = Counter()
    for m in re.finditer(r"nanocct::keep_view<.*?, (true|false), (\d+), (-?\d+)((?:, \d+)*)>", text):
        rule = "owner" if m.group(1) == "true" else "result-keep"
        kind = "tuple" if int(m.group(3)) >= 0 else ("results" if m.group(2) == "0" else "args")
        out[f"{rule}-{kind}"] += 1
    return out


def _guarded_parameters(text: str) -> int:
    """The container parameters R-VIEW-GUARD checks: the indices of every guarded<F, k...> plus every lambda check."""
    n = 0
    for m in re.finditer(r"nanocct::guarded<", text):
        depth, i = 1, m.end()
        while depth > 0:
            depth += (text[i] == "<") - (text[i] == ">")
            i += 1
        tail = re.search(r"\)((?:, \d+)+)$", text[m.end():i - 1])
        n += 0 if tail is None else tail.group(1).count(",")
    return n + len(re.findall(r"nanocct::refuse_viewed_argument\(", text))


def _null_passing_bindings(files: dict[Path, str]) -> int:
    """R-OPTIONAL-PTR: bindings whose lambda passes a literal nullptr for a dropped parameter."""
    n = 0
    for text in files.values():
        for line in text.split("\n"):
            if ".def" not in line:
                continue
            body = re.sub(r'R"nbdoc\(.*?\)nbdoc"', "", line)
            body = re.sub(r"static_cast<[^;]*?>\(nullptr\)", "", body)
            n += re.search(r"(?<!>)[(,]\s*nullptr\s*[,)]", body) is not None
    return n


def counts() -> dict[str, int]:
    files = _sources()
    text = "\n".join(files.values())
    report = _report()
    category = Counter(c for c, _, _ in report)
    manifest = json.loads((CPP / "manifest.json").read_text(encoding="utf-8"))
    kept, keepers = set(manifest.get("kept", [])), set(manifest.get("keepers", []))
    views = _keep_views(text)
    stubs = "\n".join(p.read_text(encoding="utf-8") for p in sorted((ROOT / "src" / "nanocct").rglob("*.pyi")))
    nc_init = (ROOT / "src" / "nanocct" / "NCollection" / "__init__.py").read_text(encoding="utf-8")

    def cpp(rx: str) -> int:
        return len(re.findall(rx, text))

    def rep(rx: str) -> int:
        return sum(1 for _, _, m in report if re.search(rx, m) is not None)

    ctor_lines = [l for t in files.values() for l in t.split("\n") if "nb::init<" in l or '"__init__"' in l]
    table: dict[str, Callable[[], int]] = {
        "enum-arg": lambda: cpp(r"\.noconvert\(\)"),
        "optional-ptr": lambda: _null_passing_bindings(files),
        "cstr-null": lambda: cpp(r"nanocct::OptionalCString"),
        "refwrap": lambda: cpp(r'\.def(?:_static)?\("\w+", [^;\n]*std::reference_wrapper'),
        "result-refcount0": lambda: cpp(r"IncrementRefCounter\(\)"),
        "result-value-transient": lambda: cpp(r"opencascade::handle<[\w:<>, ]*> nanocct_result\(new "),
        "alias-result": lambda: cpp(r"nanocct::AliasResult<"),            # R-CAST: reference results that may be an argument
        "default-braced": lambda: cpp(r"= std::decay_t<[^;]*?>\{"),
        "bitset": lambda: cpp(r'\.def(?:_static)?\("\w+", [^;\n]*std::bitset'),
        "unreachable": lambda: rep(r"unreachable|reaches every call|takes over"),
        "unbound-type": lambda: rep(r"(is not bound|not bound as a value).* -> (not bound|constructor not bound)$"),
        "overload-order": lambda: rep(r"takes a derived class of"),
        "null-bool": lambda: category["null-bool"],
        "copy-no-ctor": lambda: rep(r"no copy constructor -- an implicit copy"),
        "copy-heap": lambda: cpp(r"rv_policy::take_ownership"),
        "copy-keep-original": lambda: sum(m.group(1) == "true" for m in COPY_TAIL.finditer(text)),   # R-COPY: implicit copies that keep the original
        "unhashable": lambda: rep(r"__hash__ = None added"),
        "str-ops": lambda: cpp(r'\.def\("__str__"'),                       # R-STR: the print operators bound as __str__
        "ctor-keep": lambda: (sum(len(re.findall(r"nb::keep_alive<\d+, \d+>", l)) for l in ctor_lines)
                              + cpp(r"nanocct::keep_view_arg<") + cpp(r"nanocct::keep_arg<")),
        "method-keep-slots": lambda: cpp(r"nanocct::keep_slot<"),
        "method-keep-files": lambda: sum(1 for t in files.values() if "nanocct::keep_slot<" in t),
        "kept-slots-cpp": lambda: cpp(r"nanocct::keep_slot<[^>]*, true>"),
        "kept-ctor-args-cpp": lambda: cpp(r"nanocct::keep_arg<[^>]*, true>"),
        "kept-classes": lambda: len(kept),
        "kept-own": lambda: len(kept & keepers),
        "kept-base": lambda: len(kept - keepers),
        "lifetime-lines": lambda: category["lifetime"],
        "lifetime-topopebrepbuild": lambda: sum(1 for c, p, _ in report if c == "lifetime" and p == "TopOpeBRepBuild"),
        "result-keep-results": lambda: views["result-keep-results"],
        "result-keep-args": lambda: views["result-keep-args"],
        "iter-keeps": lambda: cpp(r"nanocct_def_iter<[^>(]*, true>"),
        "owner-results": lambda: views["owner-results"],
        "owner-tuple": lambda: views["owner-tuple"],
        "owner-args": lambda: views["owner-args"],
        "owner-files": lambda: sum(1 for t in files.values() if re.search(r"nanocct::keep_view<.*?, true, \d+, -?\d+", t)),
        "view-guard-params": lambda: _guarded_parameters(text),
        "view-guard-toolkits": lambda: len({p.parent.name for p, t in files.items()
                                            if "nanocct::guarded<" in t or "nanocct::refuse_viewed_argument(" in t}),
        "view-guard-wrapped": lambda: cpp(r"nanocct::guarded<"),
        "view-guard-lambda": lambda: cpp(r"nanocct::refuse_viewed_argument\("),
        "view-guard-iterators": lambda: cpp(r"nanocct::view_of<nanocct::view_kind::iterator"),
        "view-guard-lines": lambda: category["view-guard"],
        "undefined-lines": lambda: category["undefined"],
        "array-lines": lambda: sum(1 for c, _, m in report if c == "array" and "static data member" not in m),
        "ncollection-eager": lambda: len(re.findall(r"^import nanocct\._TK", nc_init, re.M)),
        "stub-enum-defaults": lambda: sum(1 for m in re.finditer(r"\w+: (nanocct\.[\w.]+) = (nanocct\.[\w.]+)", stubs)
                                          if m.group(2).startswith(m.group(1) + ".")),
    }
    return {key: f() for key, f in table.items()}


def test_every_platform_pins_the_same_counts():
    keys = {platform: sorted(table) for platform, table in PINNED.items()}
    assert sorted(PINNED) == ["darwin", "linux", "win32"]
    assert keys["linux"] == keys["darwin"] and keys["win32"] == keys["darwin"]


def test_the_generated_code_has_the_pinned_counts():
    """This platform's generation produces exactly PINNED[sys.platform]. On a difference the message lists the keys and
    the complete table to adopt -- on purpose, after reading why the number moved."""
    found = counts()
    pinned = PINNED[sys.platform]
    if found == pinned:
        return
    wrong = [f"  {key:28} pinned {pinned.get(key, '-'):>6}  found {found.get(key, '-'):>6}"
             for key in sorted(set(found) | set(pinned)) if found.get(key) != pinned.get(key)]
    table = "\n".join(f'        "{key}": {n},' for key, n in sorted(found.items()))
    pytest.fail(f"the counts of this generation moved -- update PINNED[{sys.platform!r}] on purpose:\n" + "\n".join(wrong)
                + f"\n\n    {sys.platform!r}: {{\n{table}\n    }},")
