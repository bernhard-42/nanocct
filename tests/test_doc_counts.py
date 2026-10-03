"""The counts in the design documents stay true: every number marked `N<!-- count: key -->` in docs/*.md is recounted
here from the generated sources, the generator's reports, the manifest and the stubs, and must match.

A generator change or an OCCT update moves these numbers; the test then fails with the key, the documented and the
found value, and the document is updated on purpose -- a number in the rule book cannot go stale unseen. The documents
state the macOS numbers (the generated API is not the same on every platform, see tests/test_lifetime_counts.py), so
the comparison runs on macOS."""
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
MARK = re.compile(r"(\d[\d ]*\d|\d)<!-- count: ([a-z0-9-]+) -->")

pytestmark = pytest.mark.skipif(sys.platform != "darwin", reason="the documents state the macOS counts")


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


def _marked() -> list[tuple[str, str, int]]:
    """(document, key, documented value) for every marked number."""
    out = []
    for doc in sorted((ROOT / "docs").glob("*.md")):
        for m in MARK.finditer(doc.read_text(encoding="utf-8")):
            out.append((doc.name, m.group(2), int(m.group(1).replace(" ", ""))))
    return out


def test_the_documents_mark_their_counts():
    assert len(_marked()) > 30


def test_every_marked_count_is_what_the_generated_code_says():
    found = counts()
    marked = _marked()
    unknown = sorted({key for _, key, _ in marked if key not in found})
    assert unknown == [], f"marked keys this test does not count: {unknown}"
    wrong = [f"  {doc}: {key:28} documented {n:>6}  found {found[key]:>6}" for doc, key, n in marked if found[key] != n]
    assert wrong == [], "counts in the documents no longer hold -- update them on purpose:\n" + "\n".join(wrong)
