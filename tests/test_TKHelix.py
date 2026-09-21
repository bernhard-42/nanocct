"""Generated bindings for TKHelix (OCCT 8's helix builders): a BRep helix checked against the analytic length, the parametric
HelixGeom_HelixCurve. Nothing unbound in this toolkit."""
import importlib
import math
from pathlib import Path

import pytest

from nanoocp import BRepGProp, GProp, HelixBRep, HelixGeom, NCollection, TopAbs, TopExp, gp

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKHelix" / "report.txt"


@pytest.mark.parametrize("pkg", ["HelixBRep", "HelixGeom"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def test_helix_length_and_curve():
    builder = HelixBRep.HelixBRep_BuilderHelix()
    pitches = NCollection.NCollection_Array1[float](1, 1)
    pitches.SetValue(1, 1.0)
    turns = NCollection.NCollection_Array1[float](1, 1)
    turns.SetValue(1, 3.0)
    builder.SetParameters(gp.gp_Ax3(gp.gp_Pnt(0, 0, 0), gp.gp_Dir(0, 0, 1)), 2.0, pitches, turns)   # diameter 2, pitch 1, 3 turns
    builder.Perform()
    assert builder.ErrorStatus() == 0
    props = GProp.GProp_GProps()
    BRepGProp.BRepGProp.LinearProperties(builder.Shape(), props)
    assert props.Mass() == pytest.approx(3 * math.sqrt((2 * math.pi) ** 2 + 1), rel=1e-4)      # approximated helix
    assert sum(1 for _ in TopExp.TopExp_Explorer(builder.Shape(), TopAbs.TopAbs_EDGE)) == 3
    curve = HelixGeom.HelixGeom_HelixCurve()
    curve.Load(0.0, 2 * math.pi, 1.0, 1.0, 0.0, True)
    p = curve.Value(math.pi)
    assert (p.X(), p.Y(), p.Z()) == pytest.approx((-1.0, 0.0, 0.5))
    assert [l for l in REPORT.read_text().splitlines() if not l.startswith("#")] == []
