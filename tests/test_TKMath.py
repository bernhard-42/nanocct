"""Generated bindings for the remaining TKMath packages."""
import importlib

import pytest

from nanoocp import Bnd, ElCLib, MathUtils, NCollection, Poly, TopLoc, gp
from nanoocp import math as occ_math

PACKAGES = ["math", "MathUtils", "MathPoly", "MathLin", "MathOpt", "MathRoot", "MathInteg", "MathSys", "ElCLib", "ElSLib",
            "BSplCLib", "BSplSLib", "PLib", "GeomAbs", "gp", "Poly", "CSLib", "Convert", "Bnd", "BVH", "TopLoc"]


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def test_nested_struct_in_std_optional():
    bounds = Bnd.Bnd_Range(1.0, 2.0).Get()                            # std::optional<Bnd_Range::Bounds>
    assert type(bounds) is Bnd.Bnd_Range.Bounds and (bounds.Min, bounds.Max) == (1.0, 2.0)
    assert Bnd.Bnd_Range().Get() is None                              # void range -> nullopt


def test_bnd_box():
    b = Bnd.Bnd_Box()
    b.Add(gp.gp_Pnt(0.0, 0.0, 0.0))
    b.Add(gp.gp_Pnt(1.0, 2.0, 3.0))
    assert b.CornerMax().Coord__float_float_float() == (1.0, 2.0, 3.0)
    assert b.Get__float_float_float_float_float_float() == (0.0, 0.0, 0.0, 1.0, 2.0, 3.0)                 # six double& out-params -> tuple
    assert b.IsOut(gp.gp_Pnt(5.0, 5.0, 5.0)) is True


def test_elclib_static_only_class():
    c = gp.gp_Circ(gp.gp_Ax2(), 2.0)
    assert ElCLib.ElCLib.Value(0.0, c).Coord__float_float_float() == (2.0, 0.0, 0.0)
    assert ElCLib.ElCLib.Parameter(c, gp.gp_Pnt(0.0, 2.0, 0.0)) == pytest.approx(1.5707963267948966)


def test_poly_triangulation_from_arrays():
    nodes = NCollection.NCollection_Array1[gp.gp_Pnt](1, 3)
    nodes.SetValue(1, gp.gp_Pnt(0.0, 0.0, 0.0))
    nodes.SetValue(2, gp.gp_Pnt(1.0, 0.0, 0.0))
    nodes.SetValue(3, gp.gp_Pnt(0.0, 1.0, 0.0))
    tris = NCollection.NCollection_Array1[Poly.Poly_Triangle](1, 1)
    tris.SetValue(1, Poly.Poly_Triangle(1, 2, 3))
    t = Poly.Poly_Triangulation(nodes, tris)                          # Transient, takes const NCollection_Array1<...>&
    assert (t.NbNodes(), t.NbTriangles()) == (3, 1)
    assert t.GetRefCount() == 1 and t.DynamicType().Name() == "Poly_Triangulation"
    assert t.Node(2).Coord__float_float_float() == (1.0, 0.0, 0.0)
    assert t.Triangle(1).Get() == (1, 2, 3)


def test_toploc_and_math():
    assert TopLoc.TopLoc_Location().IsIdentity() is True
    assert TopLoc.TopLoc_Location(gp.gp_Trsf()).IsIdentity() is False   # OCCT always creates a datum item from a gp_Trsf
    v = occ_math.math_Vector(1, 3)                                     # alias of the class template math_VectorBase<double>
    v.Init(2.0)
    assert type(v).__name__ == "math_Vector" and v.Norm() == pytest.approx(12.0 ** 0.5) and v(2) == 2.0
    assert (v + occ_math.math_Vector(gp.gp_XYZ(1.0, 2.0, 3.0)))(1) == 3.0 and v * v == 12.0
    assert occ_math.math_IntegerVector(1, 2).Length() == 2
    m = occ_math.math_Matrix(1, 2, 1, 2)
    m.Init(0.0)
    m.SetDiag(3.0)
    assert m.Determinant() == 9.0 and m(1, 1) == 3.0 and m.Value(2, 2) == 3.0
    assert type(m.Row(1)).__name__ == "math_Vector"                    # math_VectorBase<double> resolves to the alias class


def test_other_alias_instantiations():
    from nanoocp import BVH, Bnd, TColStd
    vec = BVH.BVH_Vec3d(1.0, 2.0, 3.0)                                  # BVH::VectorType<double, 3>::Type -> NCollection_Vec3<double>
    assert (vec.x(), vec.y(), vec.z()) == (1.0, 2.0, 3.0) and vec.Dot(BVH.BVH_Vec3d(1.0, 0.0, 0.0)) == 1.0
    b = Bnd.Bnd_B3d()
    b.Add(gp.gp_XYZ(0.0, 0.0, 0.0))
    b.Add(gp.gp_XYZ(2.0, 2.0, 2.0))
    assert b.IsOut(gp.gp_XYZ(5.0, 5.0, 5.0)) is True
    pm = TColStd.TColStd_PackedMapOfInteger()                          # NCollection_PackedMap<int>, a real class in TColStd
    pm.Add(3)
    assert pm.Contains(3) is True and pm.Extent() == 1
    assert NCollection.NCollection_Array1[BVH.BVH_Vec3f].__name__ == "NCollection_Array1__NCollection_Vec3__float"


def test_namespace_constants_and_anonymous_enums():
    assert MathUtils.THE_NEWTON_MAX_ITER == 100                         # constexpr in namespace MathUtils
    assert MathUtils.THE_NEWTON_FTOL_SQ == 1e-32


def test_namespace_functions():
    from nanoocp import MathLin
    assert MathUtils.DepressCubic(3.0, 3.0, 1.0) == (0.0, 0.0, 1.0)     # namespace MathUtils == package: module function; double& -> tuple
    a = occ_math.math_Matrix(1, 2, 1, 2, 0.0)
    a.SetDiag(2.0)
    assert MathLin.Determinant(a).Determinant == 4.0
    b = occ_math.math_Vector(1, 2, 3.0)
    r = MathLin.LeastSquares(a, b)                                      # theMethod defaults to LeastSquaresMethod::QR (qualified by the generator)
    assert r.IsDone() and (r.Solution.Value(1), r.Solution.Value(2)) == (1.5, 1.5)
    assert MathLin.LeastSquares(a, b, MathLin.LeastSquaresMethod.SVD).Solution.Value(2) == pytest.approx(1.5)
    assert not hasattr(MathLin, "Internal") and not hasattr(importlib.import_module("nanoocp.MathSys"), "detail")   # overrides [skip] namespaces
    from nanoocp import BVH
    assert isinstance(BVH.BVH_Constants_MaxTreeDepth, int)              # anonymous enum -> integer constant


def test_glob_opt_min_through_noncopyable_wrapper():
    import math
    from nanoocp import Extrema, Geom, GeomAdaptor
    circle = GeomAdaptor.GeomAdaptor_Curve(Geom.Geom_Circle(gp.gp_Ax2(), 1.0))
    line = GeomAdaptor.GeomAdaptor_Curve(Geom.Geom_Line(gp.gp_Pnt(0.0, 3.0, 0.0), gp.gp_Dir(1.0, 0.0, 0.0)), -5.0, 5.0)
    func = Extrema.Extrema_GlobOptFuncCCC0(circle, line)               # a math_MultipleVarFunction (squared distance)

    def vec(a: float, b: float) -> occ_math.math_Vector:
        v = occ_math.math_Vector(1, 2, 0.0)
        v.Set(1, 1, occ_math.math_Vector(1, 1, a))
        v.Set(2, 2, occ_math.math_Vector(1, 1, b))
        return v

    opt = occ_math.math_GlobOptMin(func, vec(0.0, -5.0), vec(2 * math.pi, 5.0))   # overrides.toml [skip] noncopyable
    opt.Perform()
    assert opt.isDone() and opt.NbExtrema() == 1 and opt.GetF() == pytest.approx(2.0)   # distance 2 at (pi/2, 0)
    sol = occ_math.math_Vector(1, 2)
    opt.Points(1, sol)
    assert (sol.Value(1), sol.Value(2)) == pytest.approx((math.pi / 2, 0.0), abs=1e-6)
    assert type(opt).__name__ == "math_GlobOptMin"


def test_primitive_reference_accessors_get_setters():
    from nanoocp import Poly
    a = occ_math.math_Matrix(1, 2, 1, 2, 0.0)
    a.SetValue(1, 2, 5.0)                                              # Python addition for double& Value(Row, Col)
    a[(2, 1)] = 7.0                                                    # ... and __setitem__ for double& operator()(Row, Col)
    assert (a.Value(1, 2), a[(2, 1)], a(2, 1), a.Value(1, 1)) == (5.0, 7.0, 7.0, 0.0)
    v = occ_math.math_Vector(1, 3, 0.0)
    v.SetValue(2, 4.0)
    v[3] = 9.0
    assert list(v.Array1()) == [0.0, 4.0, 9.0]
    m = gp.gp_Mat()
    m[(2, 2)] = 3.0
    assert m.Value(2, 2) == 3.0 and m.ChangeValue(2, 2) == 3.0        # ChangeValue returns the value; SetValue is OCCT's own
    x = gp.gp_XYZ(1.0, 2.0, 3.0)
    x.SetCoord(2, 9.0)                                                 # OCCT's setter; no invented SetChangeCoord
    assert x.ChangeCoord(2) == 9.0 and not hasattr(x, "SetChangeCoord")
    t = Poly.Poly_Triangle(1, 2, 3)
    t.SetValue(2, 7)
    t[3] = 8
    assert t.Get() == (1, 7, 8)
