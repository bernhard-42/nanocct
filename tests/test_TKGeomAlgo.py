"""Generated bindings for TKGeomAlgo (the first ModelingAlgorithms toolkit): GeomAPI/Geom2dAPI algorithms, 2D constraint
solvers (GccAna), intersections, and the rules this toolkit introduced -- ambiguous constructors (R-CTOR-AMBIGUOUS),
non-self-contained headers without a forward declaration (R-PRELUDE), per-overload undefined members (R-UNDEFINED)."""
import importlib
import json
from pathlib import Path

import pytest

from nanoocp import GCE2d, GccAna, GccEnt, Geom, Geom2dAPI, GeomAPI, GeomInt, IntPatch, IntPolyh, IntWalk, NCollection, Standard, gp

PACKAGES = ["Hatch", "GeomInt", "IntStart", "IntWalk", "IntImp", "IntCurveSurface", "IntSurf", "IntPatch", "Geom2dInt",
            "IntImpParGen", "IntRes2d", "IntCurve", "TopTrans", "Intf", "ApproxInt", "GccAna", "GccEnt", "GccInt", "HatchGen",
            "Geom2dHatch", "Law", "AppBlend", "Plate", "GeomPlate", "LocalAnalysis", "GeomAPI", "GeomFill", "Geom2dAPI",
            "Geom2dGcc", "FairCurve", "NLPlate", "IntPolyh", "TopClass"]
REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKGeomAlgo" / "report.txt"


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def _points() -> NCollection.NCollection_Array1:
    pts = NCollection.NCollection_Array1[gp.gp_Pnt](1, 4)
    for i, p in enumerate([gp.gp_Pnt(0, 0, 0), gp.gp_Pnt(1, 1, 0), gp.gp_Pnt(2, 0, 0), gp.gp_Pnt(3, 1, 0)], 1):
        pts.SetValue(i, p)
    return pts


def test_points_to_bspline_and_projection():
    bs = GeomAPI.GeomAPI_PointsToBSpline(_points())
    assert bs.IsDone()
    c = bs.Curve()
    assert type(c) is Geom.Geom_BSplineCurve and c.Degree() == 3 and c.NbPoles() == 4
    proj = GeomAPI.GeomAPI_ProjectPointOnCurve(gp.gp_Pnt(1.5, 5.0, 0.0), c)
    assert proj.NbPoints() >= 1
    u = proj.LowerDistanceParameter()
    assert proj.Parameter(1) == u                         # R-COLLISION: Parameter(int) -> double wins over Parameter(int, double&)
    assert c.Value(u).Distance(proj.NearestPoint()) < 1e-9
    assert "Parameter(self, Index: int) -> float" in proj.Parameter.__doc__


def test_interpolate_with_tangents_flags():
    # NCollection_HArray1<bool> (one of the four instantiations build123d constructs directly) arrives with this toolkit
    pts = NCollection.NCollection_HArray1[gp.gp_Pnt](1, 3)
    pts.SetValue(1, gp.gp_Pnt(0, 0, 0)); pts.SetValue(2, gp.gp_Pnt(1, 1, 0)); pts.SetValue(3, gp.gp_Pnt(2, 0, 0))
    itp = GeomAPI.GeomAPI_Interpolate(pts, False, 1e-7)
    tangents = NCollection.NCollection_Array1[gp.gp_Vec](1, 3)
    flags = NCollection.NCollection_HArray1[bool](1, 3)
    for i in range(1, 4):
        tangents.SetValue(i, gp.gp_Vec(1, 0, 0))
        flags.SetValue(i, i != 2)
    itp.Load(tangents, flags, True)
    itp.Perform()
    assert itp.IsDone()
    curve = itp.Curve()
    assert curve.Value(curve.FirstParameter()).Distance(gp.gp_Pnt(0, 0, 0)) < 1e-9


def test_2d_intersection_and_gcc_constraints():
    line = GCE2d.GCE2d_MakeLine(gp.gp_Pnt2d(0, 0), gp.gp_Dir2d(1, 0)).Value()
    circle = GCE2d.GCE2d_MakeCircle(gp.gp_Ax2d(gp.gp_Pnt2d(0, 0), gp.gp_Dir2d(1, 0)), 1.0).Value()
    inter = Geom2dAPI.Geom2dAPI_InterCurveCurve(line, circle)
    xs = sorted(inter.Point(i).X() for i in range(1, inter.NbPoints() + 1))
    assert inter.NbPoints() == 2 and xs[0] == pytest.approx(-1.0) and xs[1] == pytest.approx(1.0)
    # GccAna: circles of radius 1 tangent to two lines through the origin (x and y axis) -> 4 solutions, centres at (+-1, +-1)
    l1 = gp.gp_Lin2d(gp.gp_Pnt2d(0, 0), gp.gp_Dir2d(1, 0))
    l2 = gp.gp_Lin2d(gp.gp_Pnt2d(0, 0), gp.gp_Dir2d(0, 1))
    solver = GccAna.GccAna_Circ2d2TanRad(GccEnt.GccEnt.Unqualified(l1), GccEnt.GccEnt.Unqualified(l2), 1.0, 1e-9)
    assert solver.IsDone() and solver.NbSolutions() == 4
    centres = sorted((round(c.Location().X()), round(c.Location().Y())) for c in (solver.ThisSolution(i) for i in range(1, 5)))
    assert centres == [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # R-OUT: Tangency1(Index, ParSol&, ParArg&, PntSol&) -> (ParSol, ParArg), PntSol filled in place (R-REF-CLASS)
    pnt = gp.gp_Pnt2d()
    par_sol, par_arg = solver.Tangency1(1, pnt)
    assert isinstance(par_sol, float) and isinstance(par_arg, float) and abs(pnt.Y()) < 1e-9


def test_ambiguous_constructors_bound_with_unambiguous_arity():
    # IntPolyh_Array<T>(const int aIncrement = 256) and (const int aN, const int aIncrement = 256): a one-argument call is
    # ambiguous in C++, so the first is bound without its argument (R-CTOR-AMBIGUOUS) and the second in full
    edges = IntPolyh.IntPolyh_ArrayOfEdges()
    pts = IntPolyh.IntPolyh_ArrayOfPoints(5)
    pts2 = IntPolyh.IntPolyh_ArrayOfPoints(5, 10)
    assert edges.NbItems() == 0 and pts.NbItems() == 0 and pts2.NbItems() == 0
    sigs = [l for l in IntPolyh.IntPolyh_ArrayOfEdges.__init__.__doc__.splitlines() if l.startswith("__init__")]
    assert sigs[:2] == ["__init__(self) -> None", "__init__(self, aN: int, aIncrement: int = 256) -> None"]
    # a template member whose body does not compile for the element type is skipped by overrides.toml (6c)
    assert not hasattr(IntPolyh.IntPolyh_ArrayOfEdges, "Dump") and hasattr(IntPolyh.IntPolyh_ArrayOfPoints, "Dump")
    lines = REPORT.read_text().splitlines()
    assert any("IntPolyh_Array<IntPolyh_Edge>::IntPolyh_Array<IntPolyh_Edge>(const int): a call with all arguments is ambiguous" in l
               for l in lines)


def test_prelude_header_and_per_overload_undefined_members():
    # IntWalk_PWalking.hxx names handle<IntSurf_LineOn2S> without including or declaring it (R-PRELUDE)
    assert IntWalk.IntWalk_PWalking.__module__ == "nanoocp.IntWalk"
    lines = REPORT.read_text().splitlines()
    assert any(l.startswith("header\tIntWalk\tIntWalk: headers not self-contained, parsed with <IntSurf_LineOn2S.hxx>") for l in lines)
    # R-UNDEFINED per overload: GeomInt_WLApprox::Perform() has no symbol, the two public overloads with parameters do
    doc = GeomInt.GeomInt_WLApprox.Perform.__doc__
    assert doc.count("Perform(self") == 2 and "Perform(self) -> None" not in doc
    assert any(l.startswith("undefined\tGeomInt\tGeomInt_WLApprox::Perform(): declared in the header") for l in lines)
    assert any("GeomFill_SweepSectionGenerator::Init(const occ::handle<Geom_Curve> &, const occ::handle<Geom_Curve> &, "
               "const occ::handle<Geom_Curve> &, const double): declared in the header" in l for l in lines)


def test_skipped_base_chain_is_reported_and_absent():
    # BVH_PrimitiveSet<double, 3> (base BVH_Object<double, 3> unbound) and IntPatch_PolyhedronBVH deriving from it
    assert not hasattr(IntPatch, "IntPatch_PolyhedronBVH") and hasattr(IntPatch, "IntPatch_Polyhedron")
    lines = REPORT.read_text().splitlines()
    assert any(l.endswith("IntPatch_PolyhedronBVH: base class BVH_PrimitiveSet<double, 3> is not bound (skipped) -> class skipped") for l in lines)
    manifest = json.loads((REPORT.parents[1] / "manifest.json").read_text())
    assert "BVH_PrimitiveSet<double, 3>" not in manifest["classes"] and "IntPatch_PolyhedronBVH" not in manifest["classes"]


def test_curve_surface_intersection():
    plane = Geom.Geom_Plane(gp.gp_Pnt(0, 0, 1), gp.gp_Dir(0, 0, 1))
    line = Geom.Geom_Line(gp.gp_Pnt(0.5, 0.5, -1), gp.gp_Dir(0, 0, 1))
    ics = GeomAPI.GeomAPI_IntCS(line, plane)
    assert ics.IsDone() and ics.NbPoints() == 1
    p = ics.Point(1)
    assert (p.X(), p.Y(), p.Z()) == pytest.approx((0.5, 0.5, 1.0))
    # R-COLLISION: Parameters(Index, U&, V&, W&) (a point) and Parameters(Index, U1&, V1&, U2&, V2&) (a segment) have the
    # same inputs; each is bound under the suffix naming its returned out-parameters, there is no plain Parameters
    u, v, w = ics.Parameters__float_float_float(1)
    assert (u, v, w) == pytest.approx((0.5, 0.5, 2.0))
    with pytest.raises(Standard.Standard_OutOfRange):
        ics.Parameters__float_float_float_float(1)              # no segments
    assert not hasattr(GeomAPI.GeomAPI_IntCS, "Parameters")
    assert any("GeomAPI_IntCS::Parameters(const int, double &, double &, double &): same Python signature as another overload "
               "after out-param removal -> bound as Parameters__float_float_float" in l for l in REPORT.read_text().splitlines())
