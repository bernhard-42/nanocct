"""The report of everything the generator did not bind, persisted next to the generated code.

Every skipped class, member, function, namespace or instantiation produces one free-form line ("what: why") in
PackageIR.report / Emitter.report. This module sorts those lines into the categories of Design.md 8a and writes
src/cpp/<TK>/report.txt, so a regeneration shows coverage changes in `git diff` and tests can assert that an
omission is reported. The categories are derived from the message text (first matching pattern wins); a message
no pattern knows lands in "misc", which is the list to look at when a new OCCT idiom shows up.
"""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

# (category, pattern on the message). Order matters: the first match wins.
CATEGORIES: list[tuple[str, str]] = [
    ("deprecated", r"\bdeprecated\b"),
    ("override", r"overrides\.toml"),
    ("undefined", r"no definition in lib"),
    ("iterator", r"STL-style iterator|__iter__ added"),
    ("hash", r"__hash__ = None added"),
    ("null-bool", r"__bool__ = not IsNull\(\) added"),
    ("view", r"zero-copy numpy views added"),
    ("lifetime", r"R-CTOR-KEEP could not follow|\(R-RESULT-KEEP\)"),
    ("template", r"\btemplate\b|dependent type|cannot (read|match) template arguments|non-type argument|nested class of a class template|instantiated as .* \(spelling mismatch\)|probe typedef did not compile"),
    ("stream", r"iostream type|not bound as __str__"),
    ("raw-pointer", r"raw pointer to primitive|is a raw pointer|void pointer|reference to pointer|member pointer|function pointer|pointer to incomplete type|dependent pointer/mutable reference result"),
    ("operator", r"operator has no Python equivalent|free operator not mapped"),
    ("conversion", r"conversion (operator|skipped)"),
    ("overload-collision", r"same Python signature as|ambiguous with another constructor|const twin of a less const overload|takes a derived class of"),
    ("namespace", r"anonymous namespace|namespace skipped"),
    ("unbound-type", r"unbound type|is not bound|not known"),
    ("incomplete", r"incomplete type"),
    ("not-constructible", r"operator new is not public|copy constructor declared in the header"),
    ("noncopyable", r"non-copyable wrapper|no non-copyable wrapper possible"),
    ("inheritance", r"additional base|non-public base|of a base, not a method"),
    ("array", r"\barray\b"),
    ("rvalue", r"rvalue reference"),
    ("variadic", r"\bvariadic\b"),
    ("std", r"std::"),
    ("field", r"\bfield\b"),
    ("header", r"headers not self-contained"),
]


def categorize(message: str) -> str:
    for category, pattern in CATEGORIES:
        if re.search(pattern, message) is not None:
            return category
    return "misc"


def write_report(path: Path, toolkit: str, entries: list[tuple[str, str]]) -> Counter[str]:
    """entries: (package, message). Written sorted by category, package, message; returns the per-category counts."""
    rows = sorted((categorize(msg), pkg, msg) for pkg, msg in entries)
    counts: Counter[str] = Counter(cat for cat, _, _ in rows)
    lines = [f"# nanocct generator report for {toolkit}: {len(rows)} report lines. Generated, do not edit.",
             "# Format: category<TAB>package<TAB>what: why. Categories follow Design.md 8a (generator/report.py)."]
    lines += [f"# {cat}: {n}" for cat, n in sorted(counts.items())]
    lines += [f"{cat}\t{pkg}\t{msg}" for cat, pkg, msg in rows]
    path.write_text("\n".join(lines) + "\n")
    return counts


def read_report(path: Path) -> list[tuple[str, str, str]]:
    """(category, package, message) rows of a written report."""
    rows: list[tuple[str, str, str]] = []
    for line in path.read_text().splitlines():
        if line.startswith("#") or line == "":
            continue
        cat, pkg, msg = line.split("\t", 2)
        rows.append((cat, pkg, msg))
    return rows
