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


def test_bnd_box():
    b = Bnd.Bnd_Box()
    b.Add(gp.gp_Pnt(0.0, 0.0, 0.0))
    b.Add(gp.gp_Pnt(1.0, 2.0, 3.0))
    assert b.CornerMax().Coord() == (1.0, 2.0, 3.0)
    assert b.Get() == (0.0, 0.0, 0.0, 1.0, 2.0, 3.0)                 # six double& out-params -> tuple
    assert b.IsOut(gp.gp_Pnt(5.0, 5.0, 5.0)) is True


def test_elclib_static_only_class():
    c = gp.gp_Circ(gp.gp_Ax2(), 2.0)
    assert ElCLib.ElCLib.Value(0.0, c).Coord() == (2.0, 0.0, 0.0)
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
    assert t.Node(2).Coord() == (1.0, 0.0, 0.0)
    assert t.Triangle(1).Get() == (1, 2, 3)


def test_toploc_and_math():
    assert TopLoc.TopLoc_Location().IsIdentity() is True
    assert TopLoc.TopLoc_Location(gp.gp_Trsf()).IsIdentity() is False   # OCCT always creates a datum item from a gp_Trsf
    # math_Vector = math_VectorBase<double> is an alias of an OCCT class template: not bound yet (Design.md 8.1)
    assert not hasattr(occ_math, "math_Vector")
    m = occ_math.math_Matrix(1, 2, 1, 2)
    m.Init(0.0)
    m.SetDiag(3.0)
    assert m.Determinant() == 9.0 and m(1, 1) == 3.0 and m.Value(2, 2) == 3.0


def test_namespace_constants_and_anonymous_enums():
    assert MathUtils.THE_NEWTON_MAX_ITER == 100                         # constexpr in namespace MathUtils
    assert MathUtils.THE_NEWTON_FTOL_SQ == 1e-32
    from nanoocp import BVH
    assert isinstance(BVH.BVH_Constants_MaxTreeDepth, int)              # anonymous enum -> integer constant
