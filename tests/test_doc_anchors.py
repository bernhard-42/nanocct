"""Every link to a heading in the hand-written Markdown documents leads to a heading that exists.

A link `[text](#anchor)` or `[text](other.md#anchor)` -- or an absolute link to a document of this repository, as the
Readme uses because it is also the PyPI description -- names a heading by its GitHub anchor. Renaming, moving or
splitting a heading changes that anchor without any warning: GitHub then opens the page at its top. This test fails
instead, naming the link. Code blocks are skipped (a `#` there is no heading, a link there is no link)."""
import collections
import re
from pathlib import Path

ROOT = Path(__file__).parents[1]
# the tracked, hand-written documents
DOCUMENTS = [ROOT / "Readme.md", ROOT / "Pythonic-OCCT.md", ROOT / "CHANGELOG.md", *sorted((ROOT / "docs").glob("*.md")),
             ROOT / "licenses" / "README.md"]
REPOSITORY = "https://github.com/bernhard-42/nanocct/blob/main/"

FENCE = re.compile(r"^(```|~~~).*?^\1", re.S | re.M)
HEADING = re.compile(r"^#{1,6}[ \t]+(.+?)[ \t#]*$", re.M)
LINK = re.compile(r"\]\(([^)\s]*?)#([^)\s]+)\)")


def _slug(heading: str) -> str:
    """GitHub's anchor of a heading: the text of a link in it, lower case, punctuation dropped (letters, digits, `_`
    and `-` stay), spaces as `-`"""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading).strip().lower()
    return re.sub(r"[^\w\- ]", "", text).replace(" ", "-")


def _anchors(path: Path) -> set[str]:
    """the anchors of a document's headings; a repeated heading gets `-1`, `-2`, ... as on GitHub"""
    seen: collections.Counter[str] = collections.Counter()
    anchors = set()
    for heading in HEADING.findall(FENCE.sub("", path.read_text(encoding="utf-8"))):
        slug = _slug(heading)
        anchors.add(slug if seen[slug] == 0 else f"{slug}-{seen[slug]}")
        seen[slug] += 1
    return anchors


def broken_links(root: Path, documents: list[Path]) -> list[str]:
    """`document: target#anchor` for every link to a heading that does not exist; links to other sites, and to files
    of this repository that are not Markdown documents, are not checked"""
    broken = []
    for document in documents:
        for target, anchor in LINK.findall(FENCE.sub("", document.read_text(encoding="utf-8"))):
            if target.startswith(REPOSITORY):
                destination = root / target[len(REPOSITORY):]
            elif "://" in target or (target != "" and not target.endswith(".md")):
                continue
            elif target == "":
                destination = document
            else:
                destination = (document.parent / target).resolve()
            name = f"{document.relative_to(root)}: {target}#{anchor}"
            if not destination.is_file():
                broken.append(f"{name} (no such document)")
            elif anchor not in _anchors(destination):
                broken.append(name)
    return broken


def test_the_documents_link_to_headings():
    assert all(document.is_file() for document in DOCUMENTS)
    links = sum(len(LINK.findall(FENCE.sub("", document.read_text(encoding="utf-8")))) for document in DOCUMENTS)
    assert links > 0


def test_every_link_to_a_heading_resolves():
    broken = broken_links(ROOT, DOCUMENTS)
    assert broken == [], "links to headings that do not exist:\n" + "\n".join(broken)
