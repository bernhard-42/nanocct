"""OCCT package IntCurve (toolkit TKGeomAlgo)"""

from typing import overload

import nanoocp.GeomAbs
import nanoocp.IntRes2d
import nanoocp.NCollection
import nanoocp.gp
import nanoocp.math


class IntCurve_IConicTool:
    """
    Implementation of the ImpTool from IntImpParGen
    for conics of gp.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, IT: IntCurve_IConicTool) -> None: ...

    @overload
    def __init__(self, E: nanoocp.gp.gp_Elips2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ2d) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Parab2d) -> None: ...

    @overload
    def __init__(self, H: nanoocp.gp.gp_Hypr2d) -> None: ...

    def Value(self, X: float) -> nanoocp.gp.gp_Pnt2d: ...

    def D1(self, U: float, P: nanoocp.gp.gp_Pnt2d, T: nanoocp.gp.gp_Vec2d) -> None: ...

    def D2(self, U: float, P: nanoocp.gp.gp_Pnt2d, T: nanoocp.gp.gp_Vec2d, N: nanoocp.gp.gp_Vec2d) -> None: ...

    def Distance(self, P: nanoocp.gp.gp_Pnt2d) -> float:
        """
        Computes the value of the signed distance between
        the point P and the implicit curve.
        """

    def GradDistance(self, P: nanoocp.gp.gp_Pnt2d) -> nanoocp.gp.gp_Vec2d:
        """
        Computes the Gradient of the Signed Distance
        between a point and the implicit curve, at the
        point P.
        """

    def FindParameter(self, P: nanoocp.gp.gp_Pnt2d) -> float:
        """
        Returns the parameter U of the point on the implicit curve corresponding to the point P.
        The correspondence between P and the point P(U) on the
        implicit curve must be coherent with the way of determination of the signed distance.
        """

class IntCurve_IntImpConicParConic(nanoocp.IntRes2d.IntRes2d_Intersection):
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, ITool: IntCurve_IConicTool, Dom1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: IntCurve_PConic, Dom2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between an implicit curve and
        a parametrised curve.
        The exception ConstructionError is raised if the domain
        of the parametrised curve does not verify HasFirstPoint
        and HasLastPoint return True.
        """

    @overload
    def __init__(self, theOther: IntCurve_IntImpConicParConic) -> None: ...

    def Perform(self, ITool: IntCurve_IConicTool, Dom1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: IntCurve_PConic, Dom2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between an implicit curve and
        a parametrised curve.
        The exception ConstructionError is raised if the domain
        of the parametrised curve does not verify HasFirstPoint
        and HasLastPoint return True.
        """

    def FindU(self, parameter: float, point: nanoocp.gp.gp_Pnt2d, TheParCurev: IntCurve_PConic, TheImpTool: IntCurve_IConicTool) -> float: ...

    def FindV(self, parameter: float, point: nanoocp.gp.gp_Pnt2d, TheImpTool: IntCurve_IConicTool, ParCurve: IntCurve_PConic, TheParCurveDomain: nanoocp.IntRes2d.IntRes2d_Domain, V0: float, V1: float, Tolerance: float) -> float: ...

    def And_Domaine_Objet1_Intersections(self, TheImpTool: IntCurve_IConicTool, TheParCurve: IntCurve_PConic, TheImpCurveDomain: nanoocp.IntRes2d.IntRes2d_Domain, TheParCurveDomain: nanoocp.IntRes2d.IntRes2d_Domain, Inter2_And_Domain2: nanoocp.NCollection.NCollection_Array1[float], Inter1: nanoocp.NCollection.NCollection_Array1[float], Resultat1: nanoocp.NCollection.NCollection_Array1[float], Resultat2: nanoocp.NCollection.NCollection_Array1[float], EpsNul: float) -> int: ...

class IntCurve_IntConicConic(nanoocp.IntRes2d.IntRes2d_Intersection):
    """
    Provides methods to intersect two conics.
    The exception ConstructionError is raised in constructors
    or in Perform methods when a domain (Domain from IntRes2d)
    is not correct, i-e when a Circle (Circ2d from gp) or
    an Ellipse (i-e Elips2d from gp) do not have a closed
    domain (use the SetEquivalentParameters method for a domain
    on a circle or an ellipse).
    """

    @overload
    def __init__(self) -> None:
        """Empty Constructor"""

    @overload
    def __init__(self, L1: nanoocp.gp.gp_Lin2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, L2: nanoocp.gp.gp_Lin2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between 2 lines from gp."""

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, DL: nanoocp.IntRes2d.IntRes2d_Domain, C: nanoocp.gp.gp_Circ2d, DC: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between a line and a circle.
        The exception ConstructionError is raised if the method
        IsClosed of the domain of the circle returns False.
        """

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, DL: nanoocp.IntRes2d.IntRes2d_Domain, E: nanoocp.gp.gp_Elips2d, DE: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between a line and an ellipse.
        The exception ConstructionError is raised if the method
        IsClosed of the domain of the ellipse returns False.
        """

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, DL: nanoocp.IntRes2d.IntRes2d_Domain, P: nanoocp.gp.gp_Parab2d, DP: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between a line and a parabola from gp."""

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, DL: nanoocp.IntRes2d.IntRes2d_Domain, H: nanoocp.gp.gp_Hypr2d, DH: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between a line and an hyperbola."""

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Circ2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, C2: nanoocp.gp.gp_Circ2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between 2 circles from gp.
        The exception ConstructionError is raised if the method
        IsClosed of one of the domain returns False.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ2d, DC: nanoocp.IntRes2d.IntRes2d_Domain, E: nanoocp.gp.gp_Elips2d, DE: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between a circle and an ellipse.
        The exception ConstructionError is raised if the method
        IsClosed of one the domain returns False.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ2d, DC: nanoocp.IntRes2d.IntRes2d_Domain, P: nanoocp.gp.gp_Parab2d, DP: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between a circle and a parabola.
        The exception ConstructionError is raised if the method
        IsClosed of the domain of the circle returns False.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ2d, DC: nanoocp.IntRes2d.IntRes2d_Domain, H: nanoocp.gp.gp_Hypr2d, DH: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between a circle and an hyperbola.
        The exception ConstructionError is raised if the method
        IsClosed of the domain of the circle returns False.
        """

    @overload
    def __init__(self, E1: nanoocp.gp.gp_Elips2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, E2: nanoocp.gp.gp_Elips2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between 2 ellipses.
        The exception ConstructionError is raised if the method
        IsClosed of one of the domain returns False.
        """

    @overload
    def __init__(self, E: nanoocp.gp.gp_Elips2d, DE: nanoocp.IntRes2d.IntRes2d_Domain, P: nanoocp.gp.gp_Parab2d, DP: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between an ellipse and a parabola.
        The exception ConstructionError is raised if the method
        IsClosed of the domain of the ellipse returns False.
        """

    @overload
    def __init__(self, E: nanoocp.gp.gp_Elips2d, DE: nanoocp.IntRes2d.IntRes2d_Domain, H: nanoocp.gp.gp_Hypr2d, DH: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between an ellipse and an hyperbola.
        The exception ConstructionError is raised if the method
        IsClosed of the domain of the ellipse returns False.
        """

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Parab2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, P2: nanoocp.gp.gp_Parab2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between 2 parabolas."""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Parab2d, DP: nanoocp.IntRes2d.IntRes2d_Domain, H: nanoocp.gp.gp_Hypr2d, DH: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between a parabola and an hyperbola."""

    @overload
    def __init__(self, H1: nanoocp.gp.gp_Hypr2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, H2: nanoocp.gp.gp_Hypr2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between 2 hyperbolas."""

    @overload
    def __init__(self, theOther: IntCurve_IntConicConic) -> None: ...

    @overload
    def Perform(self, L1: nanoocp.gp.gp_Lin2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, L2: nanoocp.gp.gp_Lin2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between 2 lines from gp."""

    @overload
    def Perform(self, L: nanoocp.gp.gp_Lin2d, DL: nanoocp.IntRes2d.IntRes2d_Domain, C: nanoocp.gp.gp_Circ2d, DC: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between a line and a circle.
        The exception ConstructionError is raised if the method
        IsClosed of the domain of the circle returns False.
        """

    @overload
    def Perform(self, L: nanoocp.gp.gp_Lin2d, DL: nanoocp.IntRes2d.IntRes2d_Domain, E: nanoocp.gp.gp_Elips2d, DE: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between a line and an ellipse.
        The exception ConstructionError is raised if the method
        IsClosed of the domain of the ellipse returns False.
        """

    @overload
    def Perform(self, L: nanoocp.gp.gp_Lin2d, DL: nanoocp.IntRes2d.IntRes2d_Domain, P: nanoocp.gp.gp_Parab2d, DP: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between a line and a parabola from gp."""

    @overload
    def Perform(self, L: nanoocp.gp.gp_Lin2d, DL: nanoocp.IntRes2d.IntRes2d_Domain, H: nanoocp.gp.gp_Hypr2d, DH: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between a line and an hyperbola."""

    @overload
    def Perform(self, C1: nanoocp.gp.gp_Circ2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, C2: nanoocp.gp.gp_Circ2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between 2 circles from gp.
        The exception ConstructionError is raised if the method
        IsClosed of the domain of one of the circle returns False.
        """

    @overload
    def Perform(self, C: nanoocp.gp.gp_Circ2d, DC: nanoocp.IntRes2d.IntRes2d_Domain, E: nanoocp.gp.gp_Elips2d, DE: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between a circle and an ellipse.
        The exception ConstructionError is raised if the method
        IsClosed of one the domain returns False.
        """

    @overload
    def Perform(self, C: nanoocp.gp.gp_Circ2d, DC: nanoocp.IntRes2d.IntRes2d_Domain, P: nanoocp.gp.gp_Parab2d, DP: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between a circle and a parabola.
        The exception ConstructionError is raised if the method
        IsClosed of the domain of the circle returns False.
        """

    @overload
    def Perform(self, C: nanoocp.gp.gp_Circ2d, DC: nanoocp.IntRes2d.IntRes2d_Domain, H: nanoocp.gp.gp_Hypr2d, DH: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between a circle and an hyperbola.
        The exception ConstructionError is raised if the method
        IsClosed of the domain of the circle returns False.
        """

    @overload
    def Perform(self, E1: nanoocp.gp.gp_Elips2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, E2: nanoocp.gp.gp_Elips2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between 2 ellipses.
        The exception ConstructionError is raised if the method
        IsClosed of one of the domain returns False.
        """

    @overload
    def Perform(self, E: nanoocp.gp.gp_Elips2d, DE: nanoocp.IntRes2d.IntRes2d_Domain, P: nanoocp.gp.gp_Parab2d, DP: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between an ellipse and a parabola.
        The exception ConstructionError is raised if the method
        IsClosed of the domain of the ellipse returns False.
        """

    @overload
    def Perform(self, E: nanoocp.gp.gp_Elips2d, DE: nanoocp.IntRes2d.IntRes2d_Domain, H: nanoocp.gp.gp_Hypr2d, DH: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between an ellipse and an hyperbola.
        The exception ConstructionError is raised if the method
        IsClosed of the domain of the ellipse returns False.
        """

    @overload
    def Perform(self, P1: nanoocp.gp.gp_Parab2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, P2: nanoocp.gp.gp_Parab2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between 2 parabolas."""

    @overload
    def Perform(self, P: nanoocp.gp.gp_Parab2d, DP: nanoocp.IntRes2d.IntRes2d_Domain, H: nanoocp.gp.gp_Hypr2d, DH: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between a parabola and an hyperbola."""

    @overload
    def Perform(self, H1: nanoocp.gp.gp_Hypr2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, H2: nanoocp.gp.gp_Hypr2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between 2 hyperbolas."""

class Interval:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Domain: nanoocp.IntRes2d.IntRes2d_Domain) -> None: ...

    @overload
    def __init__(self, a: float, b: float) -> None: ...

    @overload
    def __init__(self, a: float, hf: bool, b: float, hl: bool) -> None: ...

    @overload
    def __init__(self, theOther: Interval) -> None: ...

    def Length(self) -> float: ...

    def IntersectionWithBounded(self, Inter: Interval) -> Interval: ...

    @property
    def Binf(self) -> float: ...

    @Binf.setter
    def Binf(self, arg: float, /) -> None: ...

    @property
    def Bsup(self) -> float: ...

    @Bsup.setter
    def Bsup(self, arg: float, /) -> None: ...

    @property
    def HasFirstBound(self) -> bool: ...

    @HasFirstBound.setter
    def HasFirstBound(self, arg: bool, /) -> None: ...

    @property
    def HasLastBound(self) -> bool: ...

    @HasLastBound.setter
    def HasLastBound(self, arg: bool, /) -> None: ...

    @property
    def IsNull(self) -> bool: ...

    @IsNull.setter
    def IsNull(self, arg: bool, /) -> None: ...

class PeriodicInterval:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Domain: nanoocp.IntRes2d.IntRes2d_Domain) -> None: ...

    @overload
    def __init__(self, a: float, b: float) -> None: ...

    @overload
    def __init__(self, theOther: PeriodicInterval) -> None: ...

    def SetNull(self) -> None: ...

    def IsNull(self) -> bool: ...

    def Complement(self) -> None: ...

    def Length(self) -> float: ...

    def SetValues(self, a: float, b: float) -> None: ...

    def Normalize(self) -> None: ...

    def FirstIntersection(self, I1: PeriodicInterval) -> PeriodicInterval: ...

    def SecondIntersection(self, I2: PeriodicInterval) -> PeriodicInterval: ...

    @property
    def Binf(self) -> float: ...

    @Binf.setter
    def Binf(self, arg: float, /) -> None: ...

    @property
    def Bsup(self) -> float: ...

    @Bsup.setter
    def Bsup(self, arg: float, /) -> None: ...

    @property
    def isnull(self) -> bool: ...

    @isnull.setter
    def isnull(self, arg: bool, /) -> None: ...

class IntCurve_MyImpParToolOfIntImpConicParConic(nanoocp.math.math_FunctionWithDerivative):
    @overload
    def __init__(self, IT: IntCurve_IConicTool, PC: IntCurve_PConic) -> None:
        """Constructor of the class."""

    @overload
    def __init__(self, theOther: IntCurve_MyImpParToolOfIntImpConicParConic) -> None: ...

    def Value(self, Param: float) -> tuple[bool, float]:
        """
        Computes the value of the signed distance between
        the implicit curve and the point at parameter Param
        on the parametrised curve.
        """

    def Derivative(self, Param: float) -> tuple[bool, float]:
        """
        Computes the derivative of the previous function at
        parameter Param.
        """

    def Values(self, Param: float) -> tuple[bool, float, float]:
        """Computes the value and the derivative of the function."""

class IntCurve_PConic:
    """
    This class represents a conic from gp as a
    parametric curve ( in order to be used by the
    class PConicTool from IntCurve).
    """

    @overload
    def __init__(self, PC: IntCurve_PConic) -> None: ...

    @overload
    def __init__(self, E: nanoocp.gp.gp_Elips2d) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ2d) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Parab2d) -> None: ...

    @overload
    def __init__(self, H: nanoocp.gp.gp_Hypr2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d) -> None: ...

    def SetEpsX(self, EpsDist: float) -> None:
        """
        EpsX is a internal tolerance used in math
        algorithms, usually about 1e-10
        (See FunctionAllRoots for more details)
        """

    def SetAccuracy(self, Nb: int) -> None:
        """
        Accuracy is the number of samples used to
        approximate the parametric curve on its domain.
        """

    def Accuracy(self) -> int: ...

    def EpsX(self) -> float: ...

    def TypeCurve(self) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """
        The Conics are manipulated as objects which only
        depend on three parameters : Axis and two Real from Standards.
        Type Curve is used to select the correct Conic.
        """

    def Axis2(self) -> nanoocp.gp.gp_Ax22d: ...

    def Param1(self) -> float: ...

    def Param2(self) -> float: ...

class IntCurve_PConicTool:
    """
    Implementation of the ParTool from IntImpParGen
    for conics of gp, using the class PConic from IntCurve.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntCurve_PConicTool) -> None: ...

    @staticmethod
    def EpsX(C: IntCurve_PConic) -> float: ...

    @overload
    @staticmethod
    def NbSamples(C: IntCurve_PConic) -> int: ...

    @overload
    @staticmethod
    def NbSamples(C: IntCurve_PConic, U0: float, U1: float) -> int: ...

    @staticmethod
    def Value(C: IntCurve_PConic, X: float) -> nanoocp.gp.gp_Pnt2d: ...

    @staticmethod
    def D1(C: IntCurve_PConic, U: float, P: nanoocp.gp.gp_Pnt2d, T: nanoocp.gp.gp_Vec2d) -> None: ...

    @staticmethod
    def D2(C: IntCurve_PConic, U: float, P: nanoocp.gp.gp_Pnt2d, T: nanoocp.gp.gp_Vec2d, N: nanoocp.gp.gp_Vec2d) -> None: ...

class IntCurve_ProjectOnPConicTool:
    """
    This class provides a tool which computes the parameter
    of a point near a parametric conic.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntCurve_ProjectOnPConicTool) -> None: ...

    @overload
    @staticmethod
    def FindParameter(C: IntCurve_PConic, Pnt: nanoocp.gp.gp_Pnt2d, Tol: float) -> float:
        """
        Returns the parameter V of the point on the
        parametric curve corresponding to the Point Pnt. The
        Correspondence between Pnt and the point P(V) on the
        parametric curve must be coherent with the way of
        determination of the signed distance between a point and
        the implicit curve. Tol is the tolerance on the distance
        between a point and the parametrised curve. In that case,
        no bounds are given. The research of the right parameter
        has to be made on the natural parametric domain of the
        curve.
        """

    @overload
    @staticmethod
    def FindParameter(C: IntCurve_PConic, Pnt: nanoocp.gp.gp_Pnt2d, LowParameter: float, HighParameter: float, Tol: float) -> float:
        """
        Returns the parameter V of the point on the
        parametric curve corresponding to the Point Pnt. The
        Correspondence between Pnt and the point P(V) on the
        parametric curve must be coherent with the way of
        determination of the signed distance between a point and
        the implicit curve. Tol is the tolerance on the distance
        between a point and the parametrised curve. LowParameter
        and HighParameter give the boundaries of the interval in
        which the parameter certainly lies. These parameters are
        given to implement a more efficient algorithm. So, it is
        not necessary to check that the returned value verifies
        LowParameter <= Value <= HighParameter.
        """

def Determine_Transition_LC(arg0: nanoocp.IntRes2d.IntRes2d_Position, arg1: nanoocp.gp.gp_Vec2d, arg2: nanoocp.gp.gp_Vec2d, arg3: nanoocp.IntRes2d.IntRes2d_Transition, arg4: nanoocp.IntRes2d.IntRes2d_Position, arg5: nanoocp.gp.gp_Vec2d, arg6: nanoocp.gp.gp_Vec2d, arg7: nanoocp.IntRes2d.IntRes2d_Transition, arg8: float) -> None: ...

def NormalizeOnCircleDomain(Param: float, Domain: nanoocp.IntRes2d.IntRes2d_Domain) -> float: ...
