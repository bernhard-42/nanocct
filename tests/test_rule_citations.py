"""The rule identifiers of docs/Binding-Rules.md and the code that cites them stay in step.

Every `### R-...` entry is cited by at least one comment in the generator or the hand-written C++ -- the code that
implements the rule -- and every rule identifier the sources, tests and documents mention names an entry, so a rule
that is renamed, removed or cited by a short form fails here instead of leaving a dangling reference."""
import re
from pathlib import Path

ROOT = Path(__file__).parents[1]
DOC = ROOT / "docs" / "Binding-Rules.md"
ENTRY = re.compile(r"^### (R-[A-Z0-9]+(?:-[A-Z0-9]+)*)\s*$", re.M)
TOKEN = re.compile(r"(?<![\w-])R-[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*")

# where a rule is implemented: the generator and the hand-written C++
IMPLEMENTATION = [*sorted((ROOT / "generator").glob("*.py")), ROOT / "generator" / "overrides.toml",
                  *sorted((ROOT / "src" / "cpp" / "common").glob("*.h")), *sorted((ROOT / "src" / "cpp" / "AddOns").glob("*.cpp"))]
# everything hand-written that may mention a rule (the generated sources only repeat the generator's strings)
MENTIONS = [*IMPLEMENTATION, *sorted((ROOT / "generator" / "stubs").glob("*.pyi")), *sorted((ROOT / "docs").glob("*.md")),
            ROOT / "Readme.md", ROOT / "Pythonic-OCCT.md", ROOT / "CMakeLists.txt", ROOT / "Makefile",
            ROOT / "src" / "nanocct" / "_templates.py", *sorted((ROOT / "tests").rglob("*.py")),
            *sorted((ROOT / "tools").rglob("*.py"))]

RULES = set(ENTRY.findall(DOC.read_text(encoding="utf-8")))


def _tokens(paths: list[Path]) -> dict[str, list[str]]:
    """identifier -> the files that mention it"""
    found: dict[str, list[str]] = {}
    for path in paths:
        if not path.is_file():
            continue
        for token in set(TOKEN.findall(path.read_text(encoding="utf-8"))):
            found.setdefault(token, []).append(str(path.relative_to(ROOT)))
    return found


def test_the_rule_book_has_entries():
    assert len(RULES) > 80


def test_every_rule_is_cited_where_it_is_implemented():
    cited = set(_tokens(IMPLEMENTATION))
    assert sorted(RULES - cited) == []


def test_every_mentioned_rule_identifier_has_an_entry():
    unknown = {token: files for token, files in _tokens(MENTIONS).items() if token not in RULES}
    assert unknown == {}
