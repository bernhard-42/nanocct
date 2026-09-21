"""Generated bindings for TKG3d: Geom curves/surfaces, adaptors, TopAbs, the GeomGridEval typedef aliases of nested
result structs, and namespaces GeomEval_RepCurveDesc/GeomEval_RepSurfaceDesc."""
import importlib
import math

import pytest

from nanoocp import Adaptor3d, Geom, GeomAdaptor, GeomAbs, GeomGridEval, GeomHash, NCollection, Standard, TopAbs, gp
from nanoocp.GeomEval.GeomEval_RepSurfaceDesc import Base as SurfaceBase, Full as SurfaceFull

PACKAGES = ["Geom", "GeomAdaptor", "AdvApprox", "Adaptor3d", "TopAbs", "GeomGridEval", "GeomHash", "GeomEval"]


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def _circle(radius: float = 2.0) -> Geom.Geom_Circle:
    return Geom.Geom_Circle(gp.gp_Ax2(), radius)


def _bspline() -> Geom.Geom_BSplineCurve:
    poles = NCollection.NCollection_Array1[gp.gp_Pnt](1, 3)
    for i, xyz in enumerate([(0.0, 0.0, 0.0), (1.0, 1.0, 0.0), (2.0, 0.0, 0.0)], start=1):
        poles.SetValue(i, gp.gp_Pnt(*xyz))
    knots = NCollection.NCollection_Array1[float](1, 2)
    knots.SetValue(1, 0.0)
    knots.SetValue(2, 1.0)
    mults = NCollection.NCollection_Array1[int](1, 2)
    mults.SetValue(1, 3)
    mults.SetValue(2, 3)
    return Geom.Geom_BSplineCurve(poles, knots, mults, 2)


def test_curves():
    c = _circle()
    assert c.Value(math.pi / 2).Coord() == pytest.approx((0.0, 2.0, 0.0))
    t = Geom.Geom_TrimmedCurve(c, 0.0, math.pi / 2)
    assert t.EndPoint().Coord() == pytest.approx((0.0, 2.0, 0.0))
    assert type(t.BasisCurve()) is Geom.Geom_Circle
    copy = c.Copy()                                                # handle<Geom_Geometry> -> dynamic type
    assert type(copy) is Geom.Geom_Circle and copy is not c
    bs = _bspline()
    assert (bs.Degree(), bs.NbPoles(), bs.Knots().Length()) == (2, 3, 2)
    assert bs.Value(0.5).Coord() == (1.0, 0.5, 0.0)
    assert type(bs.EvalD2(0.5)) is Geom.Geom_Curve.ResD2


def test_surfaces_and_nested_result_structs():
    s = Geom.Geom_SphericalSurface(gp.gp_Ax3(), 1.0)
    r = s.EvalD1(0.0, 0.0)                                         # Geom_Surface::ResD1 { Point; D1U; D1V }
    assert type(r) is Geom.Geom_Surface.ResD1
    assert r.Point.Coord() == (1.0, 0.0, 0.0)
    assert r.D1U.Coord() == pytest.approx((0.0, 1.0, 0.0))
    assert r.D1V.Coord() == pytest.approx((0.0, 0.0, 1.0))
    poles = NCollection.NCollection_Array2[gp.gp_Pnt](1, 2, 1, 2)
    for i in (1, 2):
        for j in (1, 2):
            poles.SetValue(i, j, gp.gp_Pnt(i, j, 0.0))
    bz = Geom.Geom_BezierSurface(poles)
    assert bz.Value(0.5, 0.5).Coord() == (1.5, 1.5, 0.0)
    ext = Geom.Geom_SurfaceOfLinearExtrusion(_circle(), gp.gp_Dir(0.0, 0.0, 1.0))
    assert ext.Value(0.0, 3.0).Coord() == (2.0, 0.0, 3.0)
    assert type(ext.BasisCurve()) is Geom.Geom_Circle
    rev = Geom.Geom_SurfaceOfRevolution(Geom.Geom_Line(gp.gp_Pnt(1.0, 0.0, 0.0), gp.gp_Dir(0.0, 0.0, 1.0)), gp.gp_Ax1())
    assert rev.Value(math.pi / 2, 1.0).Coord() == pytest.approx((0.0, 1.0, 1.0))


def test_typedef_aliases_of_nested_classes():
    assert GeomGridEval.CurveD1 is Geom.Geom_Curve.ResD1           # using CurveD1 = Geom_Curve::ResD1 (namespace GeomGridEval)
    assert GeomGridEval.SurfD3 is Geom.Geom_Surface.ResD3
    line = Geom.Geom_Line(gp.gp_Pnt(), gp.gp_Dir(0.0, 0.0, 1.0))
    params = NCollection.NCollection_Array1[float](1, 2)
    params.SetValue(1, 1.0)
    params.SetValue(2, 2.0)
    grid = GeomGridEval.GeomGridEval_Line(line).EvaluateGridD1(params)   # GeomGridEval_Line.hxx is not self-contained (gp_Lin)
    assert type(grid) is NCollection.NCollection_Array1[GeomGridEval.CurveD1]
    assert [g.Point.Z() for g in grid] == [1.0, 2.0]


def test_adaptors():
    a = GeomAdaptor.GeomAdaptor_Curve(_bspline())
    assert isinstance(a, Adaptor3d.Adaptor3d_Curve)
    assert a.GetType() == GeomAbs.GeomAbs_CurveType.GeomAbs_BSplineCurve
    assert (a.FirstParameter(), a.LastParameter()) == (0.0, 1.0)
    assert type(a.BSpline()) is Geom.Geom_BSplineCurve
    s = GeomAdaptor.GeomAdaptor_Surface(Geom.Geom_SphericalSurface(gp.gp_Ax3(), 1.0))
    assert s.GetType() == GeomAbs.GeomAbs_SurfaceType.GeomAbs_Sphere and s.Sphere().Radius() == 1.0
    with pytest.raises(Standard.Standard_NotImplemented):          # concrete base class with throwing methods
        Adaptor3d.Adaptor3d_Curve().Value(0.0)


def test_topabs_static_class_and_enums():
    fwd = TopAbs.TopAbs_Orientation.TopAbs_FORWARD
    assert TopAbs.TopAbs.Reverse(fwd) == TopAbs.TopAbs_Orientation.TopAbs_REVERSED
    assert TopAbs.TopAbs.Compose(fwd, TopAbs.TopAbs_Orientation.TopAbs_REVERSED) == TopAbs.TopAbs_Orientation.TopAbs_REVERSED
    assert TopAbs.TopAbs.ShapeTypeToString(TopAbs.TopAbs_ShapeEnum.TopAbs_FACE) == "FACE"
    # ShapeTypeFromString(const char*) and (const char*, TopAbs_ShapeEnum&) collide after out-param removal: the
    # overload with the scalar (enum) result and no out-params wins (Design.md 6), the bool/tuple variant is unreachable (reported)
    assert TopAbs.TopAbs.ShapeTypeFromString("EDGE") == TopAbs.TopAbs_ShapeEnum.TopAbs_EDGE
    assert TopAbs.TopAbs.ShapeTypeFromString("nonsense") == TopAbs.TopAbs_ShapeEnum.TopAbs_SHAPE


def test_surface_descriptor_namespace():
    assert SurfaceBase.__module__ == "nanoocp.GeomEval.GeomEval_RepSurfaceDesc"
    desc = SurfaceFull()
    assert desc.GetKind() == SurfaceBase.Kind.Full
    assert _bspline().EvalRepresentation() is None
    assert GeomHash.GeomHash_CurveHasher()(_circle()) == GeomHash.GeomHash_CurveHasher()(_circle())
