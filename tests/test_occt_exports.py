"""deps/occt-windows-exports.txt: the names the Windows DLLs export beyond what Standard_EXPORT marks
(tools/occt_exports.py, deps/occt-windows-exports.cmake). The list holds what the bindings import, so it can fall behind
the bindings at an unchanged OCCT tag: a generator rule or an overrides.toml edit that binds a member OCCT defines in a
.cxx without Standard_EXPORT. On Windows R-UNDEFINED then drops that member, and only there -- which this test turns
into a failure."""
import re
import sys

import pytest

from generator.report import read_report
from tools.occt_exports import ROOT, occt_tag, read_list

LIST = ROOT / "deps" / "occt-windows-exports.txt"
CPP = ROOT / "src" / "cpp"


def test_the_list_is_for_this_occt_and_well_formed():
    header, exports, undefined = read_list(LIST)
    assert header.startswith(f"# OCCT {occt_tag()} "), f"{LIST} was made for another OCCT: run `make occt-exports`"
    assert exports == sorted(set(exports))
    bad = [line for line in exports if re.fullmatch(r"TK[A-Za-z0-9_]+ \S+", line) is None]
    assert bad == []
    assert len(undefined) > 0, f"{LIST} has no [undefined] lines: run `make occt-exports-undefined` on Windows"
    assert undefined == sorted(undefined)


@pytest.mark.skipif(sys.platform != "win32", reason="the [undefined] section is what a Windows generation drops")
def test_windows_drops_only_what_the_list_expects():
    _, _, expected = read_list(LIST)
    found = sorted(msg for report in sorted(CPP.glob("*/report.txt")) for cat, _, msg in read_report(report)
                   if cat == "undefined")
    new = sorted(set(found) - set(expected))
    assert new == [], ("members defined in OCCT but not exported on Windows, which deps/occt-windows-exports.txt "
                       "does not export yet -- run `make occt-exports` (Makefile):\n  " + "\n  ".join(new))
    gone = sorted(set(expected) - set(found))
    assert gone == [], ("[undefined] lines this generation no longer drops -- run `make occt-exports-undefined`:\n  "
                        + "\n  ".join(gone))
