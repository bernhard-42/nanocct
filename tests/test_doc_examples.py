"""docs/Binding-Rules.md: every rule entry has the documented form, and every Python example in it runs.

An entry is a `### R-...` heading (with `#### Case N: ...` sub-blocks when one identifier covers several idioms), each
holding the five bullets C++ Idiom, OCCT examples, Rule, Python, Python examples. The examples are the rule's
evidence: each ```python block runs here in a fresh namespace, so an example that no longer matches the bindings fails
in the suite rather than in a reader's hands."""
import re
import textwrap
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
DOC = ROOT / "docs" / "Binding-Rules.md"

LABELS = ["C++ Idiom", "OCCT examples", "Rule", "Python", "Python examples"]
RULE = re.compile(r"^### (R-[A-Z0-9]+(?:-[A-Z0-9]+)*)\s*$")
CASE = re.compile(r"^#### Case (\d+): ")
LABEL = re.compile(r"^- \*\*(.+?)\*\*\s*$")
FENCE = re.compile(r"^(\s*)```python\s*$")


def _entries() -> list[tuple[str, list[str]]]:
    """(label, lines) per rule entry, or per case of a rule with cases, in document order."""
    out: list[tuple[str, list[str]]] = []
    rule = None
    for line in DOC.read_text().split("\n"):
        m = RULE.match(line)
        if m is not None:
            rule = m.group(1)
            out.append((rule, []))
            continue
        if line.startswith("## ") or line.startswith("# "):
            rule = None
            continue
        if rule is None:
            continue
        c = CASE.match(line)
        if c is not None:
            if out[-1][0] == rule:
                assert "".join(out[-1][1]).strip() == "", f"{rule}: text between the heading and Case 1"
                out.pop()                       # the rule's own (empty) block gives way to its cases
            out.append((f"{rule} case {c.group(1)}", []))
            continue
        out[-1][1].append(line)
    return out


def _examples() -> list[tuple[str, str]]:
    """(id, dedented code) for every ```python block, numbered per rule entry or case."""
    out = []
    for label, lines in _entries():
        n, i = 0, 0
        while i < len(lines):
            f = FENCE.match(lines[i])
            if f is None:
                i += 1
                continue
            body, i = [], i + 1
            while re.match(rf"^{f.group(1)}```\s*$", lines[i]) is None:
                body.append(lines[i])
                i += 1
            n += 1
            out.append((f"{label} [{n}]", textwrap.dedent("\n".join(body))))
            i += 1
    return out


ENTRIES = _entries()
EXAMPLES = _examples()


def test_the_document_has_rule_entries():
    assert len(ENTRIES) > 0 and len(EXAMPLES) > 0


@pytest.mark.parametrize("lines", [lines for _, lines in ENTRIES], ids=[label for label, _ in ENTRIES])
def test_every_rule_entry_has_the_five_bullets_in_order(lines):
    assert [m.group(1) for m in map(LABEL.match, lines) if m is not None] == LABELS


@pytest.mark.parametrize("code", [code for _, code in EXAMPLES], ids=[label for label, _ in EXAMPLES])
def test_python_example_runs(code):
    exec(compile(code, "<docs/Binding-Rules.md example>", "exec"), {"__name__": "__doc_example__"})
