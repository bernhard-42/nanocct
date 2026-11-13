"""The wheel must carry a licence for everything it bundles (Build.md).

nanocct's own code is Apache-2.0, but the binary distribution also ships OCCT, and inside it FreeType,
RapidJSON and nanobind. Each of those licences requires its text and its attribution to travel with the
binary; the OCCT exception in particular is conditional on a "prominent notice in supporting documentation
to this code that it makes use of or is based on facilities provided by the Open CASCADE Technology
software". Until 2026-09-25 the project declared no licence at all and the wheel carried no licence text,
so these tests exist to keep a new bundled dependency from arriving without one.
"""
import importlib.metadata
import re
import sys
import tomllib
from pathlib import Path

import pytest
from packaging.licenses import canonicalize_license_expression

import nanocct
from generator.wheel import COMPONENTS, license_expression

ROOT = Path(__file__).parents[1]
LICENSES = ROOT / "licenses"
PYPROJECT = tomllib.loads((ROOT / "pyproject.toml").read_text())
PACKAGE = Path(nanocct.__file__).parent                              # the installed wheel under `make test`
TABLE = tomllib.loads(COMPONENTS.read_text())["component"]
PLATFORMS = ("macos", "linux", "windows")
PLATFORM = {"darwin": "macos", "linux": "linux", "win32": "windows"}[sys.platform]
LICENCE_TEXTS = ("OCCT-LGPL-2.1", "OCCT-LGPL-exception", "FreeType-FTL", "RapidJSON", "nanobind-BSD-3-Clause",
                 "robin_map-MIT", "FreeImage-FIPL", "zlib", "libpng", "libjpeg-IJG", "libtiff", "OpenJPEG-BSD-2-Clause",
                 "Imath-Half-BSD-3-Clause", "fontconfig", "libpng-1.6.34", "bzip2", "libuuid",
                 "Microsoft-VC-Runtime")


def test_the_licence_is_declared_per_wheel():
    """The Core Metadata License-Expression "only applies to the Distribution Archive containing the metadata with
    this field", and the wheels differ (the Linux system libraries, the Windows Visual C++ runtime): pyproject.toml
    declares the licence dynamic, and generator/wheel.py writes each wheel's expression from licenses/components.toml."""
    assert "license" not in PYPROJECT["project"] and "license" in PYPROJECT["project"]["dynamic"]
    assert (ROOT / "LICENSE").read_text().lstrip().startswith("Apache License")


def test_the_component_table_is_consistent():
    notice = " ".join((ROOT / "NOTICE").read_text().split())
    readme = (LICENSES / "README.md").read_text()
    for c in TABLE:
        assert set(c["platforms"]) <= set(PLATFORMS) and len(c["platforms"]) > 0, c["name"]
        for term in c["spdx"]:
            assert canonicalize_license_expression(term) == term, term          # a valid term in its canonical spelling
            if term.startswith("LicenseRef-"):
                assert term in readme, f"{term}: not defined in licenses/README.md"
        for f in c["files"]:
            assert (ROOT / f).is_file(), f"{c['name']}: no {f}"
        if "library" in c:
            assert c["notice"] in notice, f"{c['name']}: NOTICE does not name {c['notice']!r}"
    # licenses/README.md shows the union of all wheels' terms as the project's inventory
    union: list[str] = []
    for c in TABLE:
        union += [term for term in c["spdx"] if term not in union]
    assert " AND ".join(union) in " ".join(readme.split())


def test_each_wheel_names_exactly_its_own_components():
    """The macOS wheel bundles no system library and no Microsoft runtime; Linux adds the five system libraries the
    manylinux image provides, Windows the Visual C++ runtime -- and nothing of the other platforms."""
    common = ("Apache-2.0 AND LGPL-2.1-only WITH OCCT-exception-1.0 AND FTL AND FreeImage AND Zlib AND libpng-2.0"
              " AND libpng-1.6.35 AND LicenseRef-IJG-libjpeg-10 AND libtiff AND BSD-2-Clause AND BSD-3-Clause AND MIT")
    assert license_expression("macos") == common
    assert license_expression("linux") == (common + " AND HPND-sell-variant AND LicenseRef-libpng-1.6.34"
                                           " AND bzip2-1.0.6 AND LicenseRef-libuuid")
    assert license_expression("windows") == common + " AND LicenseRef-Microsoft-VC-Runtime"
    for platform in PLATFORMS:
        expression = license_expression(platform)
        assert canonicalize_license_expression(expression) == expression


def test_the_installed_wheel_declares_its_own_expression():
    try:
        metadata = importlib.metadata.metadata("nanocct")
    except importlib.metadata.PackageNotFoundError:
        pytest.skip("not an installed wheel: the staged tree has no metadata")
    assert metadata["License-Expression"] == license_expression(PLATFORM)


@pytest.mark.parametrize("name", LICENCE_TEXTS)
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
    assert on_disk == {f"{n}.txt" for n in LICENCE_TEXTS}


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
                    "zlib", "libpng", "libjpeg", "libtiff", "OpenJPEG", "Imath",
                    "fontconfig", "bzip2", "libuuid", "msvcp140"):
        assert shipped in readme
    # build-time-only tools ship nothing and are not listed
    assert not any(tool in readme for tool in ("scikit-build-core", "cmake", "ninja", "libclang"))
    # OpenEXR's half.cpp is compiled into libFreeImage although the EXR codec is off (FreeImage's CMakeLists adds
    # Source/OpenEXR/Half unconditionally): its BSD-3 text must be the licence itself, not a pointer to it
    imath = (LICENSES / "Imath-Half-BSD-3-Clause.txt").read_text()
    assert "Contributors to the OpenEXR Project" in imath and "Redistributions in binary form must reproduce" in imath


def test_every_stub_carries_the_occt_notice():
    """The stubs' docstrings reproduce OCCT header documentation, and a stub is source text, which the Open CASCADE
    exception does not cover: each .pyi as a whole is LGPL-2.1-only WITH OCCT-exception-1.0 and has to say so, also when
    it is copied on its own -- with the OCCT and nanocct versions it was made from (LGPL-2.1 section 2b)."""
    stubs = sorted(PACKAGE.rglob("*.pyi"))
    assert len(stubs) > 300
    without = [s.relative_to(PACKAGE).as_posix() for s in stubs
               if not s.read_text(encoding="utf-8").startswith("# Generated by nanocct ")]
    assert without == []
    head = " ".join(stubs[0].read_text(encoding="utf-8").split("\n\n", 1)[0].replace("#", " ").split())
    version = PYPROJECT["project"]["version"]
    assert re.match(rf"Generated by nanocct {re.escape(version)} from Open CASCADE Technology \(OCCT\) \d+\.\d+\.\d+\.", head)
    assert f"adapted to Python docstrings by nanocct {version}." in head
    assert "SPDX-License-Identifier: LGPL-2.1-only WITH OCCT-exception-1.0" in head
    assert "Copyright (c) OPEN CASCADE SAS" in head and "nanocct contributions: Copyright (c) 2026 Bernhard Walter." in head
    assert "licenses/OCCT-LGPL-2.1.txt" in head and "licenses/OCCT-LGPL-exception.txt" in head


# The libraries a repaired wheel bundles (delocate: nanocct/.dylibs, auditwheel and delvewheel: nanocct.libs), by the
# name the repair tool keeps (`libfreetype-2f3b32b6.so.6.16.1` -> freetype), must be exactly the `library` entries of
# licenses/components.toml for this platform. OCCT's own TK* libraries are the OCCT component. A library without an
# entry fails, so a new bundled dependency cannot arrive without its licence (ocp-build-system#71 asks exactly this of
# the OCP wheels); an entry without a library fails too, so the wheel's License-Expression names nothing it lacks.


def _bundled_libraries() -> list[str]:
    dirs = [d for d in (PACKAGE / ".dylibs", PACKAGE.parent / "nanocct.libs") if d.is_dir()]
    if len(dirs) == 0:
        pytest.skip("not a repaired wheel: the staged tree links its libraries from deps/")
    return sorted(p.name for d in dirs for p in d.iterdir() if re.search(r"\.(so(\.[0-9.]+)?|dylib|dll)$", p.name))


def _library_component(name: str) -> str:
    m = re.match(r"(?:lib)?([A-Za-z0-9_+]+?)(?:-[0-9a-f]{8,})?\.", name)
    assert m is not None, name
    return m.group(1)


def test_every_bundled_library_is_a_component_of_this_wheel():
    bundled = {_library_component(n) for n in _bundled_libraries()}
    bundled = {b for b in bundled if not b.startswith("TK")}          # OCCT: its own component and licence texts
    expected = {c["library"] for c in TABLE if "library" in c and PLATFORM in c["platforms"]}
    assert sorted(bundled - expected) == [], "bundled libraries without a component entry"
    assert sorted(expected - bundled) == [], "component entries without a bundled library"
