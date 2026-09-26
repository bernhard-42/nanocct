"""Generated bindings for TKPrim: the BRepPrimAPI primitives and sweeps (the first user-facing milestone, BRepPrimAPI_MakeBox),
BRepPrim underneath, BRepSweep/Sweep iterators. Volumes are checked against the analytic values."""
import importlib
import math
from pathlib import Path

import pytest

from generator.report import read_report
from nanoocp import BRepBuilderAPI, BRepCheck, BRepGProp, BRepPrim, BRepPrimAPI, BRepSweep, GProp, NCollection, Sweep, TopAbs, TopExp, TopoDS, gp

PACKAGES = ["BRepPrim", "BRepSweep", "Sweep", "BRepPreviewAPI", "BRepPrimAPI"]
REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKPrim" / "report.txt"


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def _volume(shape: TopoDS.TopoDS_Shape) -> float:
    props = GProp.GProp_GProps()
    BRepGProp.BRepGProp.VolumeProperties_s(shape, props)
    return props.Mass()


def _rectangle() -> TopoDS.TopoDS_Face:
    p = [gp.gp_Pnt(0, 0, 0), gp.gp_Pnt(10, 0, 0), gp.gp_Pnt(10, 5, 0), gp.gp_Pnt(0, 5, 0)]
    mw = BRepBuilderAPI.BRepBuilderAPI_MakeWire()
    for i in range(4):
        mw.Add(BRepBuilderAPI.BRepBuilderAPI_MakeEdge(p[i], p[(i + 1) % 4]).Edge())
    return BRepBuilderAPI.BRepBuilderAPI_MakeFace(mw.Wire(), True).Face()


def test_make_box():
    box = BRepPrimAPI.BRepPrimAPI_MakeBox(10, 20, 30)
    s = box.Shape()
    assert type(s) is TopoDS.TopoDS_Shape and s.ShapeType() == TopAbs.TopAbs_SOLID       # declared return type, as in C++
    assert _volume(s) == pytest.approx(6000.0) and BRepCheck.BRepCheck_Analyzer(s).IsValid()
    assert sum(1 for _ in TopExp.TopExp_Explorer(s, TopAbs.TopAbs_FACE)) == 6
    assert TopoDS.TopoDS_Shape(box).IsSame(s)                                            # R-CONV via BRepBuilderAPI_MakeShape
    # OCCT semantics reproduced: Solid() builds a fresh solid on every call (BRep_Builder::MakeSolid), Shell() replaces myShape
    solid = box.Solid()
    assert type(solid) is TopoDS.TopoDS_Solid and _volume(solid) == pytest.approx(6000.0) and not solid.IsSame(s)
    shell = box.Shell()
    assert type(shell) is TopoDS.TopoDS_Shell and box.Shape().ShapeType() == TopAbs.TopAbs_SHELL
    assert _volume(BRepPrimAPI.BRepPrimAPI_MakeBox(gp.gp_Pnt(1, 1, 1), gp.gp_Pnt(3, 4, 5)).Shape()) == pytest.approx(24.0)
    axes = gp.gp_Ax2(gp.gp_Pnt(0, 0, 0), gp.gp_Dir(0, 0, 1))
    assert _volume(BRepPrimAPI.BRepPrimAPI_MakeBox(axes, 1, 2, 3).Shape()) == pytest.approx(6.0)
    sigs = [l for l in BRepPrimAPI.BRepPrimAPI_MakeBox.__init__.__doc__.splitlines() if l.startswith("__init__")]
    assert len(sigs) == 6          # = default, the four declared, the implicit copy constructor (R-IMPLICIT-COPY)


def test_primitives_against_analytic_volumes():
    assert _volume(BRepPrimAPI.BRepPrimAPI_MakeCylinder(2.0, 5.0).Shape()) == pytest.approx(math.pi * 4 * 5)
    assert _volume(BRepPrimAPI.BRepPrimAPI_MakeSphere(3.0).Shape()) == pytest.approx(4 / 3 * math.pi * 27, rel=1e-6)
    assert _volume(BRepPrimAPI.BRepPrimAPI_MakeCone(2.0, 0.0, 6.0).Shape()) == pytest.approx(math.pi * 4 * 6 / 3, rel=1e-6)
    assert _volume(BRepPrimAPI.BRepPrimAPI_MakeTorus(5.0, 1.0).Shape()) == pytest.approx(2 * math.pi ** 2 * 5, rel=1e-6)
    assert _volume(BRepPrimAPI.BRepPrimAPI_MakeWedge(10, 10, 10, 5).Shape()) == pytest.approx(750.0)
    axes = gp.gp_Ax2(gp.gp_Pnt(0, 0, 0), gp.gp_Dir(0, 0, 1))
    half = BRepPrimAPI.BRepPrimAPI_MakeCylinder(axes, 2.0, 5.0, math.pi).Shape()       # the (Axes, R, H, Angle) overload
    assert _volume(half) == pytest.approx(math.pi * 4 * 5 / 2)
    # BRepPrimAPI_MakeOneAxis::OneAxis() returns Standard_Address (void*): not bound, reported
    assert not hasattr(BRepPrimAPI.BRepPrimAPI_MakeCylinder, "OneAxis")
    rows = read_report(REPORT)
    assert ("raw-pointer", "BRepPrimAPI", "BRepPrimAPI_MakeCylinder::OneAxis(): return: void pointer") in rows
    assert all(cat != "misc" for cat, _, _ in rows)


def test_prism_and_revolution():
    face = _rectangle()
    prism = BRepPrimAPI.BRepPrimAPI_MakePrism(face, gp.gp_Vec(0, 0, 3))
    assert _volume(prism.Shape()) == pytest.approx(150.0)
    first, last = prism.FirstShape(), prism.LastShape()
    assert first.ShapeType() == TopAbs.TopAbs_FACE and last.ShapeType() == TopAbs.TopAbs_FACE and not first.IsSame(last)
    edge = next(iter(TopExp.TopExp_Explorer(face, TopAbs.TopAbs_EDGE)))
    generated = prism.Generated(edge)                       # const NCollection_List<TopoDS_Shape>& -> the bound instantiation
    assert isinstance(generated, NCollection.NCollection_List[TopoDS.TopoDS_Shape]) and len(generated) == 1
    assert next(iter(generated)).ShapeType() == TopAbs.TopAbs_FACE
    revol = BRepPrimAPI.BRepPrimAPI_MakeRevol(face, gp.gp_Ax1(gp.gp_Pnt(-1, 0, 0), gp.gp_Dir(0, 1, 0))).Shape()
    assert _volume(revol) == pytest.approx(math.pi * (11 ** 2 - 1 ** 2) * 5, rel=1e-6)


def test_brepprim_builders_and_sweep_iterators():
    cyl = BRepPrim.BRepPrim_Cylinder(2.0, 5.0)
    assert sum(1 for _ in TopExp.TopExp_Explorer(cyl.Shell(), TopAbs.TopAbs_FACE)) == 3
    wedge = BRepPrim.BRepPrim_Wedge(gp.gp_Ax2(gp.gp_Pnt(0, 0, 0), gp.gp_Dir(0, 0, 1)), 1, 2, 3)
    assert wedge.HasFace(BRepPrim.BRepPrim_Direction.BRepPrim_XMin)
    assert wedge.Face(BRepPrim.BRepPrim_Direction.BRepPrim_XMin).ShapeType() == TopAbs.TopAbs_FACE
    assert BRepPrim.BRepPrim_XMin is BRepPrim.BRepPrim_Direction.BRepPrim_XMin          # R-ENUM export
    # R-ITER on the sweep iterators
    assert hasattr(BRepSweep.BRepSweep_Iterator, "__iter__") and hasattr(Sweep.Sweep_NumShapeIterator, "__iter__")
    assert any(l.startswith("iterator\tBRepSweep\tBRepSweep_Iterator: __iter__ added") for l in REPORT.read_text().splitlines())
