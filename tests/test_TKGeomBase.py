"""Generated bindings for TKGeomBase: GC/gce makers, GCPnts, Extrema (6c alias instantiations Extrema_ExtPC/ExtCC),
GeomLProp_CLProps, BndLib, GeomConvert, IntAna, the ExtremaPC namespace, deprecated GCE2d class aliases."""
import importlib
import math

import pytest

from nanoocp import (GC, GCE2d, BndLib, Bnd, Extrema, ExtremaPC, GCPnts, Geom, Geom2d, GeomAdaptor, GeomConvert, GeomLProp,
                     GeomBndLib, IntAna, gce, gp)

PACKAGES = ["ProjLib", "GeomProjLib", "GCPnts", "CPnts", "Approx", "AppParCurves", "FEmTool", "AppCont", "Extrema", "ExtremaPC",
            "IntAna", "IntAna2d", "GeomConvert", "AdvApp2Var", "GeomLib", "Geom2dConvert", "Hermit", "BndLib", "GeomBndLib",
            "AppDef", "GeomTools", "GC", "GCE2d", "gce", "LProp", "GeomLProp", "GProp"]


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def _circle(radius: float = 1.0) -> Geom.Geom_Circle:
    return Geom.Geom_Circle(gp.gp_Ax2(), radius)


def test_gc_makers():
    seg = GC.GC_MakeSegment(gp.gp_Pnt(0.0, 0.0, 0.0), gp.gp_Pnt(3.0, 4.0, 0.0))
    assert seg.IsDone()
    curve = seg.Value()                                            # handle<Geom_TrimmedCurve>
    assert type(curve) is Geom.Geom_TrimmedCurve
    assert (curve.FirstParameter(), curve.LastParameter()) == (0.0, 5.0)
    arc = GC.GC_MakeArcOfCircle(gp.gp_Pnt(1.0, 0.0, 0.0), gp.gp_Pnt(0.0, 1.0, 0.0), gp.gp_Pnt(-1.0, 0.0, 0.0)).Value()
    assert arc.LastParameter() == pytest.approx(math.pi)
    assert gce.gce_MakeLin(gp.gp_Pnt(), gp.gp_Dir(1.0, 0.0, 0.0)).Value().Direction().Coord() == (1.0, 0.0, 0.0)
    assert type(GC.GC_MakeSegment2d(gp.gp_Pnt2d(0.0, 0.0), gp.gp_Pnt2d(1.0, 1.0)).Value()) is Geom2d.Geom2d_TrimmedCurve
    assert GCE2d.GCE2d_MakeSegment is GC.GC_MakeSegment2d              # deprecated `using` alias (OCCT 8 renamed the 2d makers)


def test_gcpnts_and_lprops():
    ad = GeomAdaptor.GeomAdaptor_Curve(_circle())
    assert GCPnts.GCPnts_AbscissaPoint.Length(ad) == pytest.approx(2 * math.pi)
    ap = GCPnts.GCPnts_AbscissaPoint(ad, math.pi / 2, 0.0)
    assert ap.IsDone() and ap.Parameter() == pytest.approx(math.pi / 2)
    lp = GeomLProp.GeomLProp_CLProps(_circle(), 0.0, 2, 1e-9)         # alias of GeomLProp_CLPropsBase<...> (6c)
    assert lp.Curvature() == pytest.approx(1.0)
    assert lp.Value().Coord() == (1.0, 0.0, 0.0)


def test_extrema_alias_instantiations():
    ext = Extrema.Extrema_ExtPC(gp.gp_Pnt(5.0, 0.0, 0.0), GeomAdaptor.GeomAdaptor_Curve(_circle()))   # Extrema_GGExtPC<Adaptor3d_Curve, ...>
    assert ext.IsDone() and ext.NbExt() == 2
    assert sorted(ext.SquareDistance(i) for i in (1, 2)) == [16.0, 36.0]
    assert ext.Point(1).Value().Coord() == pytest.approx((1.0, 0.0, 0.0))
    line = Geom.Geom_Line(gp.gp_Pnt(0.0, 5.0, 0.0), gp.gp_Dir(1.0, 0.0, 0.0))
    ecc = Extrema.Extrema_ExtCC(GeomAdaptor.GeomAdaptor_Curve(_circle()), GeomAdaptor.GeomAdaptor_Curve(line))
    assert ecc.IsDone() and ecc.SquareDistance(1) == pytest.approx(16.0)
    p1, p2 = Extrema.Extrema_POnCurv(), Extrema.Extrema_POnCurv()     # class-typed out-params, mutated in place
    ecc.Points(1, p1, p2)
    assert p1.Value().Coord() == pytest.approx((0.0, 1.0, 0.0))
    assert p2.Value().Coord() == pytest.approx((0.0, 5.0, 0.0))
    assert ExtremaPC.THE_DEFAULT_TOLERANCE > 0.0                       # namespace ExtremaPC == package
    assert ExtremaPC.Config().Tolerance == ExtremaPC.THE_DEFAULT_TOLERANCE


def test_bndlib_geomconvert_intana():
    box = Bnd.Bnd_Box()
    BndLib.BndLib_Add3dCurve.Add(GeomAdaptor.GeomAdaptor_Curve(_circle()), 1e-6, box)
    assert box.Get() == pytest.approx((-1.0, -1.0, 0.0, 1.0, 1.0, 0.0), abs=1e-5)
    assert not hasattr(GeomBndLib, "GeomBndLib_Curve")                 # header skipped (uninstalled .pxx), see overrides.toml
    assert GeomBndLib.GeomBndLib_Circle.Box_s(gp.gp_Circ(gp.gp_Ax2(), 2.0), 1e-6).CornerMax().X() == pytest.approx(2.0, abs=1e-5)
    bs = GeomConvert.GeomConvert.CurveToBSplineCurve(_circle())
    assert type(bs) is Geom.Geom_BSplineCurve and bs.NbPoles() == 6
    ia = IntAna.IntAna_IntConicQuad(gp.gp_Lin(gp.gp_Pnt(0.0, 0.0, -5.0), gp.gp_Dir(0.0, 0.0, 1.0)), gp.gp_Pln(), 1e-9)
    assert ia.IsDone() and ia.NbPoints() == 1 and ia.Point(1).Coord() == (0.0, 0.0, 0.0)


def test_classes_with_undefined_copy_constructor_are_skipped():
    assert not hasattr(GCPnts, "GCPnts_DistFunction")                  # copy ctor declared, never defined in libTKGeomBase
