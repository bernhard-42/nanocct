"""Generated bindings for the remaining TKMath packages."""
import importlib
import math

import pytest

from nanocct import BVH, Bnd, BSplCLib, ElCLib, MathUtils, NCollection, PLib, Poly, TopLoc, gp
from nanocct import math as occ_math

PACKAGES = ["math", "MathUtils", "MathPoly", "MathLin", "MathOpt", "MathRoot", "MathInteg", "MathSys", "ElCLib", "ElSLib",
            "BSplCLib", "BSplSLib", "PLib", "GeomAbs", "gp", "Poly", "CSLib", "Convert", "Bnd", "BVH", "TopLoc"]


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanocct.{pkg}").__name__ == f"nanocct.{pkg}"


def test_nested_struct_in_std_optional():
    bounds = Bnd.Bnd_Range(1.0, 2.0).Get()                            # std::optional<Bnd_Range::Bounds>
    assert type(bounds) is Bnd.Bnd_Range.Bounds and (bounds.Min, bounds.Max) == (1.0, 2.0)
    assert Bnd.Bnd_Range().Get() is None                              # void range -> nullopt


def test_bnd_box():
    b = Bnd.Bnd_Box()
    b.Add(gp.gp_Pnt(0.0, 0.0, 0.0))
    b.Add(gp.gp_Pnt(1.0, 2.0, 3.0))
    assert b.CornerMax().Coord__float__float__float() == (1.0, 2.0, 3.0)
    assert b.Get__float__float__float__float__float__float() == (0.0, 0.0, 0.0, 1.0, 2.0, 3.0)                 # six double& out-params -> tuple
    assert b.IsOut(gp.gp_Pnt(5.0, 5.0, 5.0)) is True


def test_elclib_static_only_class():
    c = gp.gp_Circ(gp.gp_Ax2(), 2.0)
    assert ElCLib.ElCLib.Value_s(0.0, c).Coord__float__float__float() == (2.0, 0.0, 0.0)
    assert ElCLib.ElCLib.Parameter_s(c, gp.gp_Pnt(0.0, 2.0, 0.0)) == pytest.approx(1.5707963267948966)


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
    assert t.Node(2).Coord__float__float__float() == (1.0, 0.0, 0.0)
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
    from nanocct import BVH, Bnd, TColStd
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
    from nanocct import MathLin
    assert MathUtils.DepressCubic(3.0, 3.0, 1.0) == (0.0, 0.0, 1.0)     # namespace MathUtils == package: module function; double& -> tuple
    a = occ_math.math_Matrix(1, 2, 1, 2, 0.0)
    a.SetDiag(2.0)
    assert MathLin.Determinant(a).Determinant == 4.0
    b = occ_math.math_Vector(1, 2, 3.0)
    r = MathLin.LeastSquares(a, b)                                      # theMethod defaults to LeastSquaresMethod::QR (qualified by the generator)
    assert r.IsDone() and (r.Solution.Value(1), r.Solution.Value(2)) == (1.5, 1.5)
    assert MathLin.LeastSquares(a, b, MathLin.LeastSquaresMethod.SVD).Solution.Value(2) == pytest.approx(1.5)
    assert not hasattr(MathLin, "Internal") and not hasattr(importlib.import_module("nanocct.MathSys"), "detail")   # overrides [skip] namespaces
    from nanocct import BVH
    assert isinstance(BVH.BVH_Constants_MaxTreeDepth, int)              # anonymous enum -> integer constant


def test_glob_opt_min_through_noncopyable_wrapper():
    import math
    from nanocct import Extrema, Geom, GeomAdaptor
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
    from nanocct import Poly
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


def test_a_null_pointer_default_can_be_omitted_or_passed_as_none():
    """R-PTR-NULL: BSplCLib_Cache(..., const NCollection_Array1<double>* theWeights = nullptr) and
    BuildCache(..., theWeights = nullptr). Without .none() nanobind refused None -- the default itself included -- so the
    non-rational cache could not be built at all. (The 2D BuildCache has no default in OCCT: see the next test.)"""
    knots = NCollection.NCollection_Array1[float](1, 4)
    for i, v in enumerate((0.0, 0.0, 1.0, 1.0), start=1):
        knots.SetValue(i, v)
    poles = NCollection.NCollection_Array1[gp.gp_Pnt](1, 2)
    poles.SetValue(1, gp.gp_Pnt(0.0, 0.0, 0.0))
    poles.SetValue(2, gp.gp_Pnt(2.0, 0.0, 0.0))
    for cache in (BSplCLib.BSplCLib_Cache(1, False, knots, poles), BSplCLib.BSplCLib_Cache(1, False, knots, poles, None)):
        for build in ((0.25, knots, poles), (0.25, knots, poles, None)):
            cache.BuildCache(*build)
            p = gp.gp_Pnt()
            cache.D0(0.25, p)
            assert p.Coord__float__float__float() == (0.5, 0.0, 0.0)


def test_a_class_pointer_without_a_default_takes_none():
    """R-PTR-NULL: OCCT documents a NULL weights/mults pointer as "non-rational" / "flat knots"
    (BSplCLib.hxx, BSplCLib::NoWeights() returns that nullptr), also where the parameter has no default: the 2D
    BSplCLib_Cache::BuildCache, BSplCLib::D0, PLib::CoefficientsPoles. Without .none() nanobind refused None there,
    so the non-rational form of these functions was unreachable."""
    assert BSplCLib.BSplCLib.NoWeights_s() is None and BSplCLib.BSplCLib.NoMults_s() is None
    knots = NCollection.NCollection_Array1[float](1, 4)
    for i, v in enumerate((0.0, 0.0, 1.0, 1.0), start=1):
        knots.SetValue(i, v)
    poles2d = NCollection.NCollection_Array1[gp.gp_Pnt2d](1, 2)
    poles2d.SetValue(1, gp.gp_Pnt2d(0.0, 0.0))
    poles2d.SetValue(2, gp.gp_Pnt2d(2.0, 4.0))
    cache = BSplCLib.BSplCLib_Cache(1, False, knots, poles2d)
    cache.BuildCache(0.25, knots, poles2d, None)
    p2 = gp.gp_Pnt2d()
    cache.D0(0.25, p2)
    assert p2.Coord__float__float() == (0.5, 1.0)

    poles = NCollection.NCollection_Array1[gp.gp_Pnt](1, 2)
    poles.SetValue(1, gp.gp_Pnt(0.0, 0.0, 0.0))
    poles.SetValue(2, gp.gp_Pnt(2.0, 0.0, 0.0))
    p = gp.gp_Pnt()
    BSplCLib.BSplCLib.D0_s(0.25, 2, 1, False, poles, BSplCLib.BSplCLib.NoWeights_s(), knots, None, p)   # flat knots, no mults
    assert p.Coord__float__float__float() == (0.5, 0.0, 0.0)

    coefs, out = NCollection.NCollection_Array1[gp.gp_Pnt](1, 2), NCollection.NCollection_Array1[gp.gp_Pnt](1, 2)
    coefs.SetValue(1, gp.gp_Pnt(1.0, 0.0, 0.0))                          # c0 + c1 t
    coefs.SetValue(2, gp.gp_Pnt(2.0, 0.0, 0.0))
    PLib.PLib.CoefficientsPoles_s(coefs, None, out, None)
    assert [out.Value(i).Coord__float__float__float() for i in (1, 2)] == [(1.0, 0.0, 0.0), (3.0, 0.0, 0.0)]


def test_an_overload_taking_a_derived_class_is_not_shadowed_by_the_base_one():
    """R-OVERLOAD-ORDER: NCollection_Array2 derives from NCollection_Array1, and nanobind calls the first
    registered overload that accepts the arguments. PLib::CoefficientsPoles for surfaces (Array2) is declared after the
    curve overloads (Array1), so Array2 arguments ran the curve algorithm on the flat data. The bilinear polynomial
    c11 + c21 u + c12 v + c22 uv with the constant weight 1 has the poles c11, c11 + c21, c11 + c12 and the sum of all
    four (PLib.cxx, the Array2 overload)."""
    points, reals = NCollection.NCollection_Array2[gp.gp_Pnt], NCollection.NCollection_Array2[float]
    coefs, poles, wcoefs, weights = points(1, 2, 1, 2), points(1, 2, 1, 2), reals(1, 2, 1, 2), reals(1, 2, 1, 2)
    for (i, j), xyz in {(1, 1): (0.0, 0.0, 0.0), (2, 1): (1.0, 0.0, 0.0), (1, 2): (0.0, 1.0, 0.0), (2, 2): (0.0, 0.0, 1.0)}.items():
        coefs.SetValue(i, j, gp.gp_Pnt(*xyz))
        wcoefs.SetValue(i, j, 1.0 if (i, j) == (1, 1) else 0.0)
    PLib.PLib.CoefficientsPoles_s(coefs, wcoefs, poles, weights)
    got = {(i, j): poles.Value(i, j).Coord__float__float__float() for i in (1, 2) for j in (1, 2)}
    assert got == {(1, 1): (0.0, 0.0, 0.0), (2, 1): (1.0, 0.0, 0.0), (1, 2): (0.0, 1.0, 0.0), (2, 2): (1.0, 1.0, 1.0)}


def test_inout_parameters_read_their_incoming_value():
    """[inout] (2026-09-30): these read the caller's value of a double&/bool& before writing it; bound as pure outputs,
    Python could not pass it and OCCT computed from an uninitialised value."""
    two_pi = 2 * math.pi
    u1, u2 = ElCLib.ElCLib.AdjustPeriodic_s(0.0, two_pi, 1e-9, 7.0, 8.0)     # moved into [0, 2pi) from 7 and 8
    assert (u1, u2) == (pytest.approx(7.0 - two_pi), pytest.approx(8.0 - two_pi))
    sphere = Bnd.Bnd_Sphere(gp.gp_XYZ(0, 0, 0), 1.0, 0, 0)
    assert sphere.IsOut(gp.gp_XYZ(5, 0, 0), 2.0) == (True, 2.0)              # min distance 4 > the given 2
    queue = BVH.BVH_BuildQueue()
    queue.Enqueue(1)
    first = queue.Fetch(False)                                               # (item, wasBusy)
    assert first == (1, True) and queue.HasBusyThreads()
    assert queue.Fetch(first[1]) == (-1, False) and not queue.HasBusyThreads()   # the busy count goes back to 0


def test_arrays_passed_by_their_first_element_are_not_bound():
    """overrides.toml [skip] methods (2026-09-30): PLib/BSplCLib functions whose `double&` is really the first element of
    an array made OCCT read and write past a single double. They are not bound; the NCollection_Array1 overloads of the
    same names stay (Excluded.md)."""
    assert not hasattr(PLib.PLib, "EvalPolynomial_s") and not hasattr(PLib.PLib, "EvalLagrange_s")
    assert not hasattr(PLib.PLib_JacobiPolynomial, "MaxError") and hasattr(PLib.PLib_JacobiPolynomial, "ToCoefficients")
    assert "NCollection_Array1" in BSplCLib.BSplCLib.Eval_s.__doc__             # the array overloads of Eval remain
    assert "double &" not in "".join(l for l in BSplCLib.BSplCLib.Eval_s.__doc__.splitlines() if l.startswith("Eval_s("))
