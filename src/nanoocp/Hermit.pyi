"""OCCT package Hermit (toolkit TKGeomBase)"""

from typing import overload

import nanoocp.Geom
import nanoocp.Geom2d


class Hermit:
    """
    This is used to reparameterize Rational BSpline
    Curves so that we can concatenate them later to
    build C1 Curves It builds and 1D-reparameterizing
    function starting from an Hermite interpolation and
    adding knots and modifying poles of the 1D BSpline
    obtained that way. The goal is to build a(u) so that
    if we consider a BSpline curve
    N(u)
    f(u) =  -----
    D(u)

    the function a(u)D(u) has value 1 at the umin and umax
    and has 0.0e0 derivative value a umin and umax.
    The details of the computation occurring in this package
    can be found by reading :
    " Etude sur la concatenation de NURBS en vue du
    balayage de surfaces" PFE n S85 Ensam Lille
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Hermit) -> None: ...

    @overload
    @staticmethod
    def Solution(BS: nanoocp.Geom.Geom_BSplineCurve, TolPoles: float = 1e-06, TolKnots: float = 1e-06) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    @overload
    @staticmethod
    def Solution(BS: nanoocp.Geom2d.Geom2d_BSplineCurve, TolPoles: float = 1e-06, TolKnots: float = 1e-06) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """
        returns the correct spline a(u) which will
        be multiplicated with BS later.
        """

    @staticmethod
    def Solutionbis(BS: nanoocp.Geom.Geom_BSplineCurve, TolPoles: float = 1e-06, TolKnots: float = 1e-06) -> tuple[float, float]:
        """
        returns the knots to insert to a(u) to
        stay with a constant sign and in the
        tolerances.
        """
