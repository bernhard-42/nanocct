"""Generated bindings for TKG2d (first ModelingData toolkit): Transient-heavy Geom2d API, nested result structs,
C++ namespaces (Geom2dEval_RepCurveDesc as a Python module), NCollection instantiations of namespaced structs."""
import importlib
import math
import sys

import pytest

from nanoocp import Adaptor2d, Geom2d, Geom2dAdaptor, Geom2dEval, Geom2dGridEval, Geom2dHash, GeomAbs, NCollection, Standard, gp
from nanoocp.Geom2dEval import Geom2dEval_RepCurveDesc
from nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc import Base, Full, Map1d

PACKAGES = ["Geom2d", "Adaptor2d", "Geom2dAdaptor", "Geom2dHash", "Geom2dGridEval", "Geom2dEval"]


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def _circle(radius: float = 2.0) -> Geom2d.Geom2d_Circle:
    return Geom2d.Geom2d_Circle(gp.gp_Ax2d(gp.gp_Pnt2d(0.0, 0.0), gp.gp_Dir2d(1.0, 0.0)), radius)


def test_transient_curves_and_polymorphic_handles():
    c = _circle()
    assert c.Radius() == 2.0
    assert c.Value(math.pi / 2).Coord__float_float() == pytest.approx((0.0, 2.0))
    t = Geom2d.Geom2d_TrimmedCurve(c, 0.0, math.pi)
    assert (t.FirstParameter(), t.LastParameter()) == (0.0, math.pi)
    assert type(t.BasisCurve()) is Geom2d.Geom2d_Circle           # handle<Geom2d_Curve> comes back as the dynamic type
    assert t.BasisCurve().Radius() == 2.0
    assert t.BasisCurve() is not c                                 # Geom2d_TrimmedCurve copies its basis curve


def test_class_typed_out_params_are_mutated_in_place():
    p, v = gp.gp_Pnt2d(), gp.gp_Vec2d()
    _circle().D1(math.pi / 2, p, v)                                # gp_Pnt2d& / gp_Vec2d& stay parameters (Design.md 6)
    assert p.Coord__float_float() == pytest.approx((0.0, 2.0))
    assert v.Coord() == pytest.approx((-2.0, 0.0))


def test_nested_result_struct():
    r = _circle().EvalD1(0.0)                                      # OCCT 8: struct Geom2d_Curve::ResD1 { Point; D1; }
    assert type(r) is Geom2d.Geom2d_Curve.ResD1
    assert r.Point.Coord__float_float() == (2.0, 0.0)
    assert r.D1.Coord() == pytest.approx((0.0, 2.0))
    assert Geom2d.Geom2d_Curve.ResD1.__qualname__ == "Geom2d_Curve.ResD1"
    empty = Geom2d.Geom2d_Curve.ResD3()                            # nested structs are constructible and writable
    empty.Point = gp.gp_Pnt2d(1.0, 1.0)
    assert empty.Point.X() == 1.0


def _bezier() -> Geom2d.Geom2d_BezierCurve:
    poles = NCollection.NCollection_Array1[gp.gp_Pnt2d](1, 3)
    poles.SetValue(1, gp.gp_Pnt2d(0.0, 0.0))
    poles.SetValue(2, gp.gp_Pnt2d(1.0, 1.0))
    poles.SetValue(3, gp.gp_Pnt2d(2.0, 0.0))
    return Geom2d.Geom2d_BezierCurve(poles)


def test_bezier_from_ncollection_array():
    bz = _bezier()
    assert (bz.Degree(), bz.NbPoles()) == (2, 3)
    assert bz.Value(0.5).Coord__float_float() == (1.0, 0.5)
    assert bz.Poles().Length() == 3                                # const Array1& result
    assert not hasattr(bz, "Poles_s")
    # the deprecated out-into-array overload is bound too, with OCCT's message as the docstring's first line (Design.md 6 R-DEPRECATED)
    poles = NCollection.NCollection_Array1[gp.gp_Pnt2d](1, 3)
    bz.Poles(poles)
    assert poles[3].Coord__float_float() == bz.Pole(3).Coord__float_float()
    assert "Deprecated in OCCT: use Poles() returning const reference instead" in bz.Poles.__doc__


def test_adaptor_and_abstract_base():
    a = Geom2dAdaptor.Geom2dAdaptor_Curve(_circle())
    assert isinstance(a, Adaptor2d.Adaptor2d_Curve2d)
    assert a.GetType() == GeomAbs.GeomAbs_CurveType.GeomAbs_Circle
    assert a.Circle().Radius() == 2.0
    with pytest.raises(Standard.Standard_NotImplemented):          # the base class is concrete in OCCT 8, its methods throw
        Adaptor2d.Adaptor2d_Curve2d().Value(0.0)


def test_namespace_is_a_python_module():
    assert Geom2dEval_RepCurveDesc.__name__ == "nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc"
    assert sys.modules["nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc"] is Geom2dEval_RepCurveDesc   # the shim, not the extension
    assert Geom2dEval.Geom2dEval_RepCurveDesc is Geom2dEval_RepCurveDesc
    assert Base.__module__ == "nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc"
    assert Base.__qualname__ == "Base"
    assert Full().GetKind() == Base.Kind.Full                      # enum nested in a class nested in a namespace
    assert isinstance(Full(), Base)
    m = Map1d()
    assert (m.Scale, m.Offset, m.IsIdentity()) == (1.0, 0.0, True)
    m.Scale = 2.0
    assert m.Map(1.5) == 3.0


def test_eval_representation_descriptor_round_trip():
    bz = _bezier()
    assert bz.HasEvalRepresentation() is False
    assert bz.EvalRepresentation() is None                         # null handle<Geom2dEval_RepCurveDesc::Base>
    desc = Full()
    desc.Representation = _circle()                                # handle field of a namespaced Transient class
    bz.SetEvalRepresentation(desc)
    back = bz.EvalRepresentation()
    assert type(back) is Full and back.GetKind() == Base.Kind.Full
    assert type(back.Representation) is Geom2d.Geom2d_Circle
    assert bz.EvalD1(0.0).Point.Coord__float_float() == (2.0, 0.0)              # evaluation now goes through the representation
    bz.ClearEvalRepresentation()
    assert bz.Value(0.0).Coord__float_float() == (0.0, 0.0)


def test_package_named_namespace_folds_into_the_package():
    assert Geom2dGridEval.CurveD1.__module__ == "nanoocp.Geom2dGridEval"    # namespace Geom2dGridEval == package
    ev = Geom2dGridEval.Geom2dGridEval_Circle(_circle())
    params = NCollection.NCollection_Array1[float](1, 3)
    for i, u in enumerate((0.0, math.pi / 2, math.pi), start=1):
        params.SetValue(i, u)
    res = ev.EvaluateGridD1(params)
    assert type(res) is NCollection.NCollection_Array1[Geom2dGridEval.CurveD1]
    assert res.Length() == 3
    assert res.Value(2).Point.Coord__float_float() == pytest.approx((0.0, 2.0))
    assert [r.D1.Coord() for r in res][2] == pytest.approx((0.0, -2.0))


def test_call_operator_defined_in_the_library():
    h = Geom2dHash.Geom2dHash_CurveHasher()                        # operator() overloads found by the nm check
    c = _circle()
    assert h(c) == h(c)
    assert h(c, c) is True
    assert h(c, _circle(3.0)) is False
