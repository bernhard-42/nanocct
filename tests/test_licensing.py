"""The wheel must carry a licence for everything it bundles (Design.md 7).

nanocct's own code is Apache-2.0, but the binary distribution also ships OCCT, and inside it FreeType,
RapidJSON and nanobind. Each of those licences requires its text and its attribution to travel with the
binary; the OCCT exception in particular is conditional on a "prominent notice in supporting documentation
to this code that it makes use of or is based on facilities provided by the Open CASCADE Technology
software". Until 2026-09-25 the project declared no licence at all and the wheel carried no licence text,
so these tests exist to keep a new bundled dependency from arriving without one.
"""
import tomllib
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
LICENSES = ROOT / "licenses"
PYPROJECT = tomllib.loads((ROOT / "pyproject.toml").read_text())


def test_the_project_declares_its_own_licence():
    assert PYPROJECT["project"]["license"] == "Apache-2.0"          # PEP 639 SPDX expression
    assert (ROOT / "LICENSE").read_text().lstrip().startswith("Apache License")


@pytest.mark.parametrize("name", ["OCCT-LGPL-2.1", "OCCT-LGPL-exception", "FreeType-FTL",
                                  "RapidJSON", "nanobind-BSD-3-Clause", "robin_map-MIT",
                                  "FreeImage-FIPL", "zlib", "libpng", "libjpeg-IJG", "libtiff",
                                  "OpenJPEG-BSD-2-Clause", "Imath-Half-BSD-3-Clause"])
def test_every_bundled_component_has_its_licence_text(name):
    text = (LICENSES / f"{name}.txt").read_text()
    assert len(text.strip()) > 200                                  # a real licence, not a placeholder


def test_the_licence_files_are_declared_for_the_wheel():
    """license-files globs licenses/*.txt, so a new text ships automatically -- but LICENSE, NOTICE and the
    README are named individually and would be dropped silently if the list were edited."""
    declared = PYPROJECT["project"]["license-files"]
    assert "LICENSE" in declared and "NOTICE" in declared
    assert "licenses/*.txt" in declared
    on_disk = {p.name for p in LICENSES.glob("*.txt")}
    assert on_disk == {f"{n}.txt" for n in ("OCCT-LGPL-2.1", "OCCT-LGPL-exception", "FreeType-FTL",
                                            "RapidJSON", "nanobind-BSD-3-Clause", "robin_map-MIT",
                                            "FreeImage-FIPL", "zlib", "libpng", "libjpeg-IJG", "libtiff",
                                            "OpenJPEG-BSD-2-Clause", "Imath-Half-BSD-3-Clause")}


def test_notice_carries_the_attributions_the_licences_require():
    # a NOTICE is wrapped prose, so a required phrase may straddle a line break: match on collapsed whitespace
    notice = " ".join((ROOT / "NOTICE").read_text().split())
    # the OCCT exception's own wording -- it is what the exception is conditional on
    assert "facilities provided by the Open CASCADE Technology" in notice
    # FTL section 1: "you must acknowledge somewhere in your documentation that you have used the FreeType code"
    assert "The FreeType Project" in notice and "freetype.org" in notice
    # LGPL 2.1 section 6: the recipient must be able to get the library's source
    assert "github.com/Open-Cascade-SAS/OCCT" in notice
    for holder in ("Tencent", "Wenzel Jakob", "Thibaut Goetghebuer-Planchon"):
        assert holder in notice
    # FIPL 3.6: the executable may go out under our licence only if a notice says where the source is
    assert "FreeImage Public License" in notice and "github.com/danoli3/FreeImage" in notice
    # no dependency is modified, and the notice must not claim otherwise for the two that used to be in doubt
    assert "FreeType 2.14.3 is **used unmodified**" in notice
    assert "nanocct does not modify FreeImage" in notice


def test_licences_cover_what_is_actually_bundled_and_nothing_build_only():
    readme = (LICENSES / "README.md").read_text()
    for shipped in ("Open CASCADE", "FreeType", "FreeImage", "RapidJSON", "nanobind", "robin_map",
                    "zlib", "libpng", "libjpeg", "libtiff", "OpenJPEG"):
        assert shipped in readme
    # build-time-only tools ship nothing and must not be listed as if they did
    assert "scikit-build-core" in readme and "do not" in readme
