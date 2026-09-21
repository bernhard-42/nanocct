"""Generated bindings for OCCT package gp (toolkit TKMath)."""
import math

import pytest

from nanoocp import gp


def test_module_identity():
    assert gp.__name__ == "nanoocp.gp"
    assert gp.gp_Pnt.__module__ == "nanoocp.gp"


def test_value_class_ctor_and_accessors():
    p = gp.gp_Pnt(1.0, 2.0, 3.0)
    assert (p.X(), p.Y(), p.Z()) == (1.0, 2.0, 3.0)
    assert p.Coord(2) == 2.0
    assert gp.gp_Pnt().Coord__float__float__float() == (0.0, 0.0, 0.0)


def test_out_params_become_tuple():
    p = gp.gp_Pnt(1.0, 2.0, 3.0)
    assert p.Coord__float__float__float() == (1.0, 2.0, 3.0)                       # Coord(double&, double&, double&) const: R-COLLISION suffix
    assert type(p.Coord()) is gp.gp_XYZ and p.Coord().X() == 1.0                # Coord() -> const gp_XYZ&, as in C++


def test_inout_override_keeps_inputs():
    t = gp.gp_Trsf()
    t.SetRotation(gp.gp_Ax1(gp.gp_Pnt(), gp.gp_Dir(0.0, 0.0, 1.0)), math.pi / 2)
    x, y, z = t.Transforms(1.0, 0.0, 0.0)                     # overrides.toml: inout
    assert (round(x, 12), round(y, 12), round(z, 12)) == (0.0, 1.0, 0.0)


def test_class_out_param_mutated_in_place_and_primitive_out_returned():
    t = gp.gp_Trsf()
    t.SetRotation(gp.gp_Ax1(gp.gp_Pnt(), gp.gp_Dir(0.0, 0.0, 1.0)), math.pi / 2)
    axis = gp.gp_XYZ()
    ok, angle = t.GetRotation(axis)                           # bool GetRotation(gp_XYZ&, double&) const
    assert ok is True
    assert angle == pytest.approx(math.pi / 2)
    assert axis.Coord() == (0.0, 0.0, 1.0)


def test_operators():
    a, b = gp.gp_Vec(1.0, 0.0, 0.0), gp.gp_Vec(0.0, 1.0, 0.0)
    assert (a + b).Coord() == (1.0, 1.0, 0.0)
    assert (a - b).Coord() == (1.0, -1.0, 0.0)
    assert (a * 2.0).Coord() == (2.0, 0.0, 0.0)
    assert (2.0 * a).Coord() == (2.0, 0.0, 0.0)               # free operator*(double, gp_Vec) -> __rmul__
    assert a * b == 0.0                                       # dot product
    assert (a ^ b).Coord() == (0.0, 0.0, 1.0)                 # cross product
    assert (-a).Coord() == (-1.0, 0.0, 0.0)
    assert (a / 2.0).Coord() == (0.5, 0.0, 0.0)
    c = a
    c += b                                                    # void operator+= -> __iadd__ returning self
    assert c is a
    assert a.Coord() == (1.0, 1.0, 0.0)
    m = gp.gp_Mat(2.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 2.0)
    assert (m * gp.gp_XYZ(1.0, 1.0, 1.0)).Coord() == (2.0, 2.0, 2.0)


def test_enums():
    assert int(gp.gp_TrsfForm.gp_Rotation) == 1               # unscoped enum, arithmetic
    d = gp.gp_Dir(gp.gp_Dir.D.Z)                              # nested scoped enum
    assert d.Coord() == (0.0, 0.0, 1.0)


def test_static_methods_and_static_only_class():
    assert gp.gp.Origin().Coord__float__float__float() == (0.0, 0.0, 0.0)
    assert gp.gp.DZ().Coord() == (0.0, 0.0, 1.0)


def test_static_overload_of_instance_method_is_suffixed():
    q = gp.gp_QuaternionNLerp.Interpolate_s(gp.gp_Quaternion(), gp.gp_Quaternion(), 0.5)
    assert q.W() == 1.0


def test_template_specialization_name():
    assert gp.NCollection_Lerp__gp_Trsf.__name__ == "NCollection_Lerp__gp_Trsf"


def test_default_argument():
    assert gp.gp_Pnt(0.0, 0.0, 0.0).IsEqual(gp.gp_Pnt(0.0, 0.0, 1e-9), 1e-7) is True


def test_occt_exception_reaches_python():
    with pytest.raises(RuntimeError, match="zero norm"):
        gp.gp_Dir(0.0, 0.0, 0.0)


def test_docstring_is_occt_comment():
    assert "Computes the distance between two points." in gp.gp_Pnt.Distance.__doc__
