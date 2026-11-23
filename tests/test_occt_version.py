"""The OCCT version is set in one place, TAG in deps/fetch-occt-src.sh; these tests hold the two things that have to
follow it by hand: nanocct's own version, which starts with the OCCT version (release.yml: v8.0.1.0 is OCCT 8.0.1,
nanocct's counter 0), and the texts a wheel ships, which name the OCCT it bundles. The install prefix carries no
version, so nothing else spells it (the generator and CMake check the trees against each other at build time)."""
from __future__ import annotations

import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).parents[1]
PYPROJECT = tomllib.loads((ROOT / "pyproject.toml").read_text())

# A mention of an OCCT version in prose ("OCCT 8.0.2", "Open CASCADE Technology 8.0.2"), as a tag (V8_0_2) or as an
# install prefix (deps/occt-8.0.2). A nanocct version (8.0.2.0) is not one: the lookahead refuses a fourth component.
_MENTIONS = (re.compile(r"(?:OCCT|Open CASCADE Technology)\s+(\d+\.\d+\.\d+)(?![.\d])"),
             re.compile(r"\bV(\d+_\d+_\d+)\b"),
             re.compile(r"\bocct-(\d+\.\d+\.\d+)(?![.\d])"))


def pinned_occt() -> str:
    """The version TAG in deps/fetch-occt-src.sh names: V8_0_2 -> "8.0.2"."""
    text = (ROOT / "deps" / "fetch-occt-src.sh").read_text()
    found = re.findall(r"^TAG=V(\d+)_(\d+)_(\d+)$", text, flags=re.M)
    assert len(found) == 1, f"deps/fetch-occt-src.sh: expected one TAG=V<major>_<minor>_<maintenance> line, got {found}"
    return ".".join(found[0])


def shipped_texts() -> list[Path]:
    """What a wheel carries as text about itself: the long description (pyproject `readme`), the licence files
    (`license-files`), and licenses/components.toml, whose names become the licensing tables."""
    files = {ROOT / PYPROJECT["project"]["readme"], ROOT / "licenses" / "components.toml"}
    for pattern in PYPROJECT["project"]["license-files"]:
        files.update(ROOT.glob(pattern))
    return sorted(files)


def test_nanocct_version_starts_with_the_pinned_occt():
    version = PYPROJECT["project"]["version"]
    parts = version.split(".")
    assert len(parts) == 4, f"nanocct's version is the OCCT version and a counter, got {version}"
    assert ".".join(parts[:3]) == pinned_occt(), (
        f"pyproject.toml version {version} does not start with the OCCT pinned in deps/fetch-occt-src.sh"
        f" ({pinned_occt()})")


def test_shipped_texts_name_only_the_pinned_occt():
    pinned = pinned_occt()
    wrong: list[str] = []
    mentions = 0
    for path in shipped_texts():
        for lineno, line in enumerate(path.read_text(errors="replace").splitlines(), start=1):
            for pattern in _MENTIONS:
                for m in pattern.finditer(line):
                    mentions += 1
                    if m.group(1).replace("_", ".") != pinned:
                        wrong.append(f"{path.relative_to(ROOT)}:{lineno}: {m.group(0)}")
    assert wrong == [], f"OCCT version other than the pinned {pinned}:\n" + "\n".join(wrong)
    assert mentions > 0, "no OCCT version found in the shipped texts -- the patterns no longer match them"
