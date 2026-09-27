"""Generated bindings for TKFeat: feature operations (BRepFeat_MakePrism as cut and fuse, SplitShape) and LocOpe."""
import importlib
import math
from pathlib import Path

import pytest

from generator.report import read_report
from OCP3x import BRepBuilderAPI, BRepFeat, BRepGProp, BRepPrimAPI, GProp, LocOpe, TopAbs, TopExp, TopoDS, gp

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKFeat" / "report.txt"


@pytest.mark.parametrize("pkg", ["LocOpe", "BRepFeat"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"OCP3x.{pkg}").__name__ == f"OCP3x.{pkg}"


def _volume(shape: TopoDS.TopoDS_Shape) -> float:
    props = GProp.GProp_GProps()
    BRepGProp.BRepGProp.VolumeProperties_s(shape, props)
    return props.Mass()


def test_feature_prism_cut_and_fuse():
    box = BRepPrimAPI.BRepPrimAPI_MakeBox(10, 10, 10).Shape()
    top = None
    for f in TopExp.TopExp_Explorer(box, TopAbs.TopAbs_FACE):
        props = GProp.GProp_GProps()
        BRepGProp.BRepGProp.SurfaceProperties_s(f, props)
        if math.isclose(props.CentreOfMass().Z(), 10.0):
            top = TopoDS.Face(f)
    wire = BRepBuilderAPI.BRepBuilderAPI_MakePolygon(gp.gp_Pnt(4, 4, 10), gp.gp_Pnt(6, 4, 10), gp.gp_Pnt(6, 6, 10), gp.gp_Pnt(4, 6, 10), True).Wire()
    sketch = BRepBuilderAPI.BRepBuilderAPI_MakeFace(wire, True).Face()
    cut = BRepFeat.BRepFeat_MakePrism(box, sketch, top, gp.gp_Dir(0, 0, -1), 0, True)       # Fuse = 0: a pocket
    cut.Perform(3.0)
    assert cut.IsDone() and _volume(cut.Shape()) == pytest.approx(1000 - 2 * 2 * 3)
    fuse = BRepFeat.BRepFeat_MakePrism(box, sketch, top, gp.gp_Dir(0, 0, 1), 1, True)        # Fuse = 1: a boss
    fuse.Perform(3.0)
    assert fuse.IsDone() and _volume(fuse.Shape()) == pytest.approx(1012.0)
    assert BRepFeat.BRepFeat_OK is BRepFeat.BRepFeat_StatusError.BRepFeat_OK and hasattr(LocOpe, "LocOpe_Prism")
    assert type(BRepFeat.BRepFeat_SplitShape(box)).__name__ == "BRepFeat_SplitShape"
    rows = read_report(REPORT)
    assert all(cat == "undefined" for cat, _, _ in rows) and len(rows) == 5          # only declared-but-undefined members (R-UNDEFINED)
