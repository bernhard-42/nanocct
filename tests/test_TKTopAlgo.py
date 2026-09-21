"""Generated bindings for TKTopAlgo: the BRepBuilderAPI makers, BRepGProp, BRepCheck, BRepExtrema, BRepBndLib, the classifiers,
and what this toolkit introduced -- three more classes through the non-copyable wrapper (R-NONCOPYABLE) and the rule that a nested
enum of a skipped class is skipped with it (no alias, accessor entry or instantiation may name it)."""
import importlib
import json
import math
from pathlib import Path

import pytest

from generator.report import read_report
from nanoocp import (BRepBuilderAPI, BRepCheck, BRepClass, BRepClass3d, BRepExtrema, BRepGProp, BRepLib, BRepMAT2d, BRepTopAdaptor,
                     GProp, MAT, MAT2d, NCollection, Bnd, BRepBndLib, Standard, StdFail, TopAbs, TopExp, TopoDS, gp)

PACKAGES = ["IntCurvesFace", "MAT", "MAT2d", "Bisector", "BRepMAT2d", "BRepCheck", "BRepBndLib", "BRepExtrema", "BRepClass",
            "BRepClass3d", "BRepLib", "BRepGProp", "BRepIntCurveSurface", "BRepTopAdaptor", "BRepBuilderAPI", "BRepApprox"]
REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKTopAlgo" / "report.txt"


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def _rectangle() -> tuple[TopoDS.TopoDS_Wire, TopoDS.TopoDS_Face]:
    """A 10 x 5 planar face in z = 0, built edge by edge."""
    p = [gp.gp_Pnt(0, 0, 0), gp.gp_Pnt(10, 0, 0), gp.gp_Pnt(10, 5, 0), gp.gp_Pnt(0, 5, 0)]
    mw = BRepBuilderAPI.BRepBuilderAPI_MakeWire()
    for i in range(4):
        mw.Add(BRepBuilderAPI.BRepBuilderAPI_MakeEdge(p[i], p[(i + 1) % 4]).Edge())
    assert mw.IsDone()
    wire = mw.Wire()
    return wire, BRepBuilderAPI.BRepBuilderAPI_MakeFace(wire, True).Face()


def test_makers_conversion_operator_and_explorer():
    wire, face = _rectangle()
    assert type(wire) is TopoDS.TopoDS_Wire and type(face) is TopoDS.TopoDS_Face
    # R-CONV: BRepBuilderAPI_MakeShape::operator TopoDS_Shape() -> TopoDS_Shape(aMaker), the same shape as Shape()
    mf = BRepBuilderAPI.BRepBuilderAPI_MakeFace(wire, True)
    assert TopoDS.TopoDS_Shape(mf).IsSame(mf.Shape())
    assert sum(1 for _ in TopExp.TopExp_Explorer(face, TopAbs.TopAbs_EDGE)) == 4          # R-ITER
    assert sum(1 for _ in TopExp.TopExp_Explorer(face, TopAbs.TopAbs_VERTEX)) == 8
    poly = BRepBuilderAPI.BRepBuilderAPI_MakePolygon(gp.gp_Pnt(0, 0, 0), gp.gp_Pnt(1, 0, 0), gp.gp_Pnt(0, 1, 0), True)
    assert poly.IsDone() and type(poly.Wire()) is TopoDS.TopoDS_Wire
    # a maker that is not done raises StdFail_NotDone (a Standard_Failure) as in C++
    bad = BRepBuilderAPI.BRepBuilderAPI_MakeEdge(gp.gp_Pnt(0, 0, 0), gp.gp_Pnt(0, 0, 0))
    assert not bad.IsDone()
    with pytest.raises(StdFail.StdFail_NotDone) as exc:
        bad.Edge()
    assert isinstance(exc.value, Standard.Standard_Failure) and "not done" in str(exc.value)


def test_global_properties_check_and_transform():
    wire, face = _rectangle()
    props = GProp.GProp_GProps()
    BRepGProp.BRepGProp.SurfaceProperties(face, props)                  # static, no _s: no instance method of that name
    assert props.Mass() == pytest.approx(50.0)
    c = props.CentreOfMass()
    assert (c.X(), c.Y(), c.Z()) == pytest.approx((5.0, 2.5, 0.0))
    lin = GProp.GProp_GProps()
    BRepGProp.BRepGProp.LinearProperties(wire, lin)
    assert lin.Mass() == pytest.approx(30.0)
    circ = BRepBuilderAPI.BRepBuilderAPI_MakeEdge(gp.gp_Circ(gp.gp_Ax2(gp.gp_Pnt(0, 0, 0), gp.gp_Dir(0, 0, 1)), 2.0)).Edge()
    lin2 = GProp.GProp_GProps()
    BRepGProp.BRepGProp.LinearProperties(circ, lin2)
    assert lin2.Mass() == pytest.approx(4 * math.pi)
    assert BRepCheck.BRepCheck_Analyzer(face).IsValid()
    t = gp.gp_Trsf()
    t.SetTranslation(gp.gp_Vec(100, 0, 0))
    moved = BRepBuilderAPI.BRepBuilderAPI_Transform(face, t, True).Shape()
    props2 = GProp.GProp_GProps()
    BRepGProp.BRepGProp.SurfaceProperties(moved, props2)
    assert props2.CentreOfMass().X() == pytest.approx(105.0)
    # BRepGProp_Domain iterates the face's edges (R-ITER, More/Next/Value)
    assert len(list(BRepGProp.BRepGProp_Domain(face))) == 4


def test_extrema_bounding_box_and_classifiers():
    _, face = _rectangle()
    v = BRepBuilderAPI.BRepBuilderAPI_MakeVertex(gp.gp_Pnt(20, 2.5, 0)).Vertex()
    dss = BRepExtrema.BRepExtrema_DistShapeShape(face, v)
    assert dss.IsDone() and dss.NbSolution() == 1 and dss.Value() == pytest.approx(10.0)
    p = dss.PointOnShape1(1)
    assert (p.X(), p.Y(), p.Z()) == pytest.approx((10.0, 2.5, 0.0))
    box = Bnd.Bnd_Box()
    BRepBndLib.BRepBndLib.Add(face, box)
    xmin, ymin, zmin, xmax, ymax, zmax = box.Get__float__float__float__float__float__float()     # R-COLLISION suffix
    assert xmin <= 0 < 10 <= xmax and ymin <= 0 < 5 <= ymax and zmin <= 0 <= zmax
    # R-FIXED-ARRAY: Bnd_OBB::GetVertex(gp_Pnt theP[8]) returns the 8 corners as a list
    obb = Bnd.Bnd_OBB()
    BRepBndLib.BRepBndLib.AddOBB(face, obb)
    ok, corners = obb.GetVertex()
    assert ok and len(corners) == 8 and all(type(p) is gp.gp_Pnt for p in corners)
    assert sorted({round(p.X(), 6) for p in corners}) == [0.0, 10.0] and sorted({round(p.Y(), 6) for p in corners}) == [0.0, 5.0]
    assert BRepClass.BRepClass_FaceClassifier(face, gp.gp_Pnt(5, 2.5, 0), 1e-7).State() == TopAbs.TopAbs_IN
    assert BRepClass.BRepClass_FaceClassifier(face, gp.gp_Pnt(50, 2.5, 0), 1e-7).State() == TopAbs.TopAbs_OUT


def test_noncopyable_wrappers():
    # BRepTopAdaptor_FClass2d (a NCollection_Sequence<CSLib_Class2d> member, CSLib_Class2d's copy constructor is deleted),
    # BRepExtrema_ProximityValueTool (NCollection_CellFilter member) and BRepExtrema_ShapeProximity (holds the former by value)
    # are bound through the wrapper struct of overrides.toml [skip] noncopyable, under their own names (R-NONCOPYABLE)
    _, face = _rectangle()
    fc = BRepTopAdaptor.BRepTopAdaptor_FClass2d(face, 1e-7)
    assert type(fc).__name__ == "BRepTopAdaptor_FClass2d" and type(fc).__module__ == "nanoocp.BRepTopAdaptor"
    assert fc.PerformInfinitePoint() == TopAbs.TopAbs_OUT
    assert fc.Perform(gp.gp_Pnt2d(50, 2.5)) == TopAbs.TopAbs_OUT
    assert fc.Perform(gp.gp_Pnt2d(5, 2.5)) == TopAbs.TopAbs_ON             # what OCCT computes here (OCP 7.9.3 agrees), not IN
    sp = BRepExtrema.BRepExtrema_ShapeProximity(face, face, 1.0)
    assert type(sp).__name__ == "BRepExtrema_ShapeProximity" and sp.Tolerance() == 1.0
    assert type(BRepExtrema.BRepExtrema_ProximityValueTool()).__name__ == "BRepExtrema_ProximityValueTool"


def test_nested_enum_of_a_skipped_class_is_skipped_with_it():
    # BRepExtrema_ProximityDistTool is skipped (its BVH_Distance base is unbound); its nested enum ProxPnt_Status, the
    # package-level typedef of it and the NCollection_DynamicArray<ProxPnt_Status> instantiation go with it. Before this
    # rule the alias aborted the import of the toolkit and the accessor entry broke NCollection_DynamicArray[T] for every T.
    assert not hasattr(BRepExtrema, "BRepExtrema_ProximityDistTool") and not hasattr(BRepExtrema, "ProxPnt_Status")
    assert len(list(NCollection.NCollection_DynamicArray)) > 0                 # the accessor table resolves
    assert not any("ProxPnt_Status" in n for n in NCollection.NCollection_DynamicArray.bound())
    manifest = json.loads((REPORT.parents[1] / "manifest.json").read_text())
    assert "BRepExtrema_ProximityDistTool::ProxPnt_Status" not in manifest["classes"]
    assert manifest["templates"]["NCollection_DynamicArray<BRepExtrema_ProximityDistTool::ProxPnt_Status>"]["skipped"] is True
    rows = read_report(REPORT)
    msgs = [msg for _, pkg, msg in rows if pkg == "BRepExtrema"]
    assert "ProxPnt_Status = BRepExtrema_ProximityDistTool::ProxPnt_Status: type alias of a type that is not bound (skipped)" in msgs
    assert ("NCollection_DynamicArray<BRepExtrema_ProximityDistTool::ProxPnt_Status>: element type "
            "BRepExtrema_ProximityDistTool::ProxPnt_Status is not bound (its class is skipped) -> instantiation skipped") in msgs
    assert all(cat != "misc" for cat, _, _ in rows)
    # members whose signature still names the enum are bound but not callable until the type exists (8a, usability)
    sp = BRepExtrema.BRepExtrema_ShapeProximity()
    with pytest.raises(TypeError, match="Unable to convert function return value"):
        sp.ProxPntStatus1()


def test_collision_suffixes_and_undefined_members():
    # R-COLLISION: three FindAPointInTheFace overloads that differ only in their double& out-parameters
    names = [n for n in dir(BRepClass3d.BRepClass3d_SolidExplorer) if n.startswith("FindAPointInTheFace")]
    assert names == ["FindAPointInTheFace", "FindAPointInTheFace__float", "FindAPointInTheFace__float__float",
                     "FindAPointInTheFace__float__float__float"]
    # R-OUT-HANDLE + R-COLLISION: GetUKnots(UMin, UMax, handle<HArray1<double>>&) next to GetUKnots(UMin, UMax, Array1&)
    doc = BRepGProp.BRepGProp_Face.GetUKnots__NCollection_HArray1__double.__doc__
    assert doc.startswith("GetUKnots__NCollection_HArray1__double(self, theUMin: float, theUMax: float) -> "
                          "nanoocp.NCollection.NCollection_HArray1__double")
    assert hasattr(BRepLib.BRepLib, "BuildPCurveForEdgeOnPlane__Geom2d_Curve__bool")
    # R-CONST-TWIN: BRepClass_Edge::Edge() const / Edge() -> only the non-const one
    assert BRepClass.BRepClass_Edge.Edge.__doc__.count("Edge(self") == 1
    # R-UNDEFINED per overload: MAT2d_CutCurve::Perform(handle<Geom2d_Curve>, MAT_Side) has no symbol in libTKTopAlgo
    lines = REPORT.read_text().splitlines()
    assert any(l.startswith("undefined\tMAT2d\tMAT2d_CutCurve::Perform(const occ::handle<Geom2d_Curve> &, const MAT_Side): declared") for l in lines)
    assert "MAT_Side" not in MAT2d.MAT2d_CutCurve.Perform.__doc__


def test_medial_axis_of_a_rectangle():
    # BRepMAT2d: the bisecting locus of a rectangle; MAT_ListOfBisector/MAT_ListOfEdge got __iter__ (More/Next/Current)
    _, face = _rectangle()
    explorer = BRepMAT2d.BRepMAT2d_Explorer(face)
    assert explorer.NumberOfContours() == 1
    locus = BRepMAT2d.BRepMAT2d_BisectingLocus()
    locus.Compute(explorer, 1, MAT.MAT_Side.MAT_Left, True, False)
    assert locus.IsDone() and locus.NumberOfContours() == 1 and locus.NumberOfElts(1) == 4
    graph = locus.Graph()
    assert graph.NumberOfArcs() == 5 and graph.NumberOfBasicElts() == 4
    assert hasattr(MAT.MAT_ListOfBisector, "__iter__") and hasattr(MAT.MAT_ListOfEdge, "__iter__")
