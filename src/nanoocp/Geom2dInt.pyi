"""OCCT package Geom2dInt (toolkit TKGeomAlgo)"""

from typing import overload

import nanoocp.Adaptor2d
import nanoocp.Bnd
import nanoocp.Extrema
import nanoocp.GeomAbs
import nanoocp.IntCurve
import nanoocp.IntRes2d
import nanoocp.Intf
import nanoocp.NCollection
import nanoocp.gp
import nanoocp.math


class Geom2dInt_TheDistBetweenPCurvesOfTheIntPCurvePCurveOfGInter(nanoocp.math.math_FunctionSetWithDerivatives):
    @overload
    def __init__(self, curve1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, curve2: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dInt_TheDistBetweenPCurvesOfTheIntPCurvePCurveOfGInter) -> None: ...

    def NbVariables(self) -> int:
        """returns 2."""

    def NbEquations(self) -> int:
        """returns 2."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """
        computes the values <F> of the Functions for the
        variable <X>.
        returns True if the computation was done successfully,
        False otherwise.
        """

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <D> of the derivatives for the
        variable <X>.
        returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """
        returns the values <F> of the functions and the derivatives
        <D> for the variable <X>.
        returns True if the computation was done successfully,
        False otherwise.
        """

class Geom2dInt_ExactIntersectionPointOfTheIntPCurvePCurveOfGInter:
    @overload
    def __init__(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Tol: float) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dInt_ExactIntersectionPointOfTheIntPCurvePCurveOfGInter) -> None: ...

    @overload
    def Perform(self, Poly1: Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter, Poly2: Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter) -> tuple[int, int, float, float]: ...

    @overload
    def Perform(self, Uo: float, Vo: float, UInf: float, VInf: float, USup: float, VSup: float) -> None: ...

    def NbRoots(self) -> int: ...

    def Roots(self) -> tuple[float, float]: ...

    def AnErrorOccurred(self) -> bool: ...

class Geom2dInt_Geom2dCurveTool:
    """
    This class provides a Geom2dCurveTool as < Geom2dCurveTool from IntCurve >
    from a Tool as < Geom2dCurveTool from Adaptor3d > .
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dInt_Geom2dCurveTool) -> None: ...

    @staticmethod
    def GetType(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.GeomAbs.GeomAbs_CurveType: ...

    @staticmethod
    def Line(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.gp.gp_Lin2d:
        """
        Returns the Lin2d from gp corresponding to the curve C.
        This method is called only when TheType returns
        GeomAbs_Line.
        """

    @staticmethod
    def Circle(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the Circ2d from gp corresponding to the curve C.
        This method is called only when TheType returns
        GeomAbs_Circle.
        """

    @staticmethod
    def Ellipse(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.gp.gp_Elips2d:
        """
        Returns the Elips2d from gp corresponding to the curve C.
        This method is called only when TheType returns
        GeomAbs_Ellipse.
        """

    @staticmethod
    def Parabola(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.gp.gp_Parab2d:
        """
        Returns the Parab2d from gp corresponding to the curve C.
        This method is called only when TheType returns
        GeomAbs_Parabola.
        """

    @staticmethod
    def Hyperbola(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.gp.gp_Hypr2d:
        """
        Returns the Hypr2d from gp corresponding to the curve C.
        This method is called only when TheType returns
        GeomAbs_Hyperbola.
        """

    @overload
    @staticmethod
    def EpsX(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> float: ...

    @overload
    @staticmethod
    def EpsX(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Eps_XYZ: float) -> float: ...

    @overload
    @staticmethod
    def NbSamples(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> int: ...

    @overload
    @staticmethod
    def NbSamples(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, U0: float, U1: float) -> int: ...

    @staticmethod
    def FirstParameter(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> float: ...

    @staticmethod
    def LastParameter(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> float: ...

    @staticmethod
    def Value(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, X: float) -> nanoocp.gp.gp_Pnt2d: ...

    @staticmethod
    def D0(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, U: float, P: nanoocp.gp.gp_Pnt2d) -> None: ...

    @staticmethod
    def D1(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, U: float, P: nanoocp.gp.gp_Pnt2d, T: nanoocp.gp.gp_Vec2d) -> None: ...

    @staticmethod
    def D2(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, U: float, P: nanoocp.gp.gp_Pnt2d, T: nanoocp.gp.gp_Vec2d, N: nanoocp.gp.gp_Vec2d) -> None: ...

    @staticmethod
    def D3(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, U: float, P: nanoocp.gp.gp_Pnt2d, T: nanoocp.gp.gp_Vec2d, N: nanoocp.gp.gp_Vec2d, V: nanoocp.gp.gp_Vec2d) -> None: ...

    @staticmethod
    def DN(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, U: float, N: int) -> nanoocp.gp.gp_Vec2d: ...

    @staticmethod
    def NbIntervals(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> int:
        """
        output the number of interval of continuity C2 of
        the curve
        """

    @staticmethod
    def Intervals(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Tab: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """compute Tab."""

    @staticmethod
    def GetInterval(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Index: int, Tab: nanoocp.NCollection.NCollection_Array1[float]) -> tuple[float, float]:
        """
        output the bounds of interval of index <Index>
        used if Type == Composite.
        """

    @staticmethod
    def Degree(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> int: ...

class Geom2dInt_TheCurveLocatorOfTheProjPCurOfGInter:
    """
    Template class for locating the closest point on a curve to a given point.
    Among a set of sampled points on the curve, finds the one closest to the target.

    @tparam TheCurve the curve type
    @tparam TheCurveTool the curve tool providing curve operations
    @tparam ThePOnC the point-on-curve type
    @tparam ThePoint the point type (gp_Pnt or gp_Pnt2d)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dInt_TheCurveLocatorOfTheProjPCurOfGInter) -> None: ...

    @overload
    @staticmethod
    def Locate(theP: nanoocp.gp.gp_Pnt2d, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theNbU: int, thePapp: nanoocp.Extrema.Extrema_POnCurv2d) -> None:
        """
        Among a set of points {C(ui), i=1,NbU}, locate the point
        P=C(uj) such that:
        distance(P,C) = Min{distance(P,C(ui))}
        @param theP the target point
        @param theC the curve to sample
        @param theNbU the number of sample points
        @param thePapp the result point on curve
        """

    @overload
    @staticmethod
    def Locate(theP: nanoocp.gp.gp_Pnt2d, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theNbU: int, theUmin: float, theUsup: float, thePapp: nanoocp.Extrema.Extrema_POnCurv2d) -> None:
        """
        Among a set of points {C(ui), i=1,NbU}, locate the point
        P=C(uj) such that:
        distance(P,C) = Min{distance(P,C(ui))}
        The search is done between theUmin and theUsup.
        @param theP the target point
        @param theC the curve to sample
        @param theNbU the number of sample points
        @param theUmin the minimum parameter value
        @param theUsup the maximum parameter value
        @param thePapp the result point on curve
        """

class Geom2dInt_TheIntConicCurveOfGInter(nanoocp.IntRes2d.IntRes2d_Intersection):
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between a line and a parametric curve."""

    @overload
    def __init__(self, E: nanoocp.gp.gp_Elips2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between an ellipse and a parametric curve."""

    @overload
    def __init__(self, Prb: nanoocp.gp.gp_Parab2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between a parabola and a parametric curve."""

    @overload
    def __init__(self, H: nanoocp.gp.gp_Hypr2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between the main branch of an hyperbola
        and a parametric curve.
        """

    @overload
    def __init__(self, theOther: Geom2dInt_TheIntConicCurveOfGInter) -> None: ...

    @overload
    def Perform(self, L: nanoocp.gp.gp_Lin2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Circ2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between a line and a parametric curve."""

    @overload
    def Perform(self, E: nanoocp.gp.gp_Elips2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between an ellipse and a parametric curve."""

    @overload
    def Perform(self, Prb: nanoocp.gp.gp_Parab2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between a parabola and a parametric curve."""

    @overload
    def Perform(self, H: nanoocp.gp.gp_Hypr2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between the main branch of an hyperbola
        and a parametric curve.
        """

class Geom2dInt_TheIntersectorOfTheIntConicCurveOfGInter(nanoocp.IntRes2d.IntRes2d_Intersection):
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, ITool: nanoocp.IntCurve.IntCurve_IConicTool, Dom1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Dom2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between an implicit curve and
        a parametrised curve.
        The exception ConstructionError is raised if the domain
        of the parametrised curve does not verify HasFirstPoint
        and HasLastPoint return True.
        """

    @overload
    def __init__(self, theOther: Geom2dInt_TheIntersectorOfTheIntConicCurveOfGInter) -> None: ...

    def Perform(self, ITool: nanoocp.IntCurve.IntCurve_IConicTool, Dom1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Dom2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between an implicit curve and
        a parametrised curve.
        The exception ConstructionError is raised if the domain
        of the parametrised curve does not verify HasFirstPoint
        and HasLastPoint return True.
        """

    def FindU(self, parameter: float, point: nanoocp.gp.gp_Pnt2d, TheParCurev: nanoocp.Adaptor2d.Adaptor2d_Curve2d, IntCurve_IConicTool: nanoocp.IntCurve.IntCurve_IConicTool) -> float: ...

    def FindV(self, parameter: float, point: nanoocp.gp.gp_Pnt2d, IntCurve_IConicTool: nanoocp.IntCurve.IntCurve_IConicTool, ParCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, TheParCurveDomain: nanoocp.IntRes2d.IntRes2d_Domain, V0: float, V1: float, Tolerance: float) -> float: ...

    def And_Domaine_Objet1_Intersections(self, IntCurve_IConicTool: nanoocp.IntCurve.IntCurve_IConicTool, TheParCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, TheImpCurveDomain: nanoocp.IntRes2d.IntRes2d_Domain, TheParCurveDomain: nanoocp.IntRes2d.IntRes2d_Domain, Inter2_And_Domain2: nanoocp.NCollection.NCollection_Array1[float], Inter1: nanoocp.NCollection.NCollection_Array1[float], Resultat1: nanoocp.NCollection.NCollection_Array1[float], Resultat2: nanoocp.NCollection.NCollection_Array1[float], EpsNul: float) -> int: ...

class Geom2dInt_TheIntPCurvePCurveOfGInter(nanoocp.IntRes2d.IntRes2d_Intersection):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dInt_TheIntPCurvePCurveOfGInter) -> None: ...

    @overload
    def Perform(self, Curve1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Domain1: nanoocp.IntRes2d.IntRes2d_Domain, Curve2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Domain2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None: ...

    @overload
    def Perform(self, Curve1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Domain1: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None: ...

    def SetMinNbSamples(self, theMinNbSamples: int) -> None:
        """Set / get minimum number of points in polygon for intersection."""

    def GetMinNbSamples(self) -> int: ...

class Geom2dInt_GInter(nanoocp.IntRes2d.IntRes2d_Intersection):
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, TolConf: float, Tol: float) -> None:
        """Self Intersection of a curve"""

    @overload
    def __init__(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Self Intersection of a curve with a domain."""

    @overload
    def __init__(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, TolConf: float, Tol: float) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, TolConf: float, Tol: float) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between 2 curves."""

    @overload
    def __init__(self, theOther: Geom2dInt_GInter) -> None: ...

    @overload
    def Perform(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None: ...

    @overload
    def Perform(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, TolConf: float, Tol: float) -> None: ...

    @overload
    def Perform(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None: ...

    @overload
    def Perform(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, TolConf: float, Tol: float) -> None: ...

    @overload
    def Perform(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, TolConf: float, Tol: float) -> None: ...

    @overload
    def Perform(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between 2 curves."""

    def ComputeDomain(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, TolDomain: float) -> nanoocp.IntRes2d.IntRes2d_Domain:
        """Create a domain from a curve"""

    def SetMinNbSamples(self, theMinNbSamples: int) -> None:
        """Set / get minimum number of points in polygon intersection."""

    def GetMinNbSamples(self) -> int: ...

class Geom2dInt_IntConicCurveOfGInter(nanoocp.IntRes2d.IntRes2d_Intersection):
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between a line and a parametric curve."""

    @overload
    def __init__(self, E: nanoocp.gp.gp_Elips2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between an ellipse and a parametric curve."""

    @overload
    def __init__(self, Prb: nanoocp.gp.gp_Parab2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between a parabola and a parametric curve."""

    @overload
    def __init__(self, H: nanoocp.gp.gp_Hypr2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between the main branch of an hyperbola
        and a parametric curve.
        """

    @overload
    def __init__(self, theOther: Geom2dInt_IntConicCurveOfGInter) -> None: ...

    @overload
    def Perform(self, L: nanoocp.gp.gp_Lin2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Circ2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between a line and a parametric curve."""

    @overload
    def Perform(self, E: nanoocp.gp.gp_Elips2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between an ellipse and a parametric curve."""

    @overload
    def Perform(self, Prb: nanoocp.gp.gp_Parab2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """Intersection between a parabola and a parametric curve."""

    @overload
    def Perform(self, H: nanoocp.gp.gp_Hypr2d, D1: nanoocp.IntRes2d.IntRes2d_Domain, PCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float) -> None:
        """
        Intersection between the main branch of an hyperbola
        and a parametric curve.
        """

class Geom2dInt_MyImpParToolOfTheIntersectorOfTheIntConicCurveOfGInter(nanoocp.math.math_FunctionWithDerivative):
    @overload
    def __init__(self, IT: nanoocp.IntCurve.IntCurve_IConicTool, PC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None:
        """Constructor of the class."""

    @overload
    def __init__(self, theOther: Geom2dInt_MyImpParToolOfTheIntersectorOfTheIntConicCurveOfGInter) -> None: ...

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

class Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter(nanoocp.math.math_FunctionWithDerivative):
    """
    Template class for computing extremal distance function between a point and a curve.
    Searches for a parameter value u such that dist(P, C(u)) passes through an extremum.
    Inherits from math_FunctionWithDerivative and is used by math_FunctionRoot and
    math_FunctionRoots algorithms.

    If D1c and D2c are the first and second derivatives:
    F(u) = (C(u)-P).D1c(u) / ||D1c||
    DF(u) = ||D1c|| + (C(u)-P).D2c(u)/||D1c|| - F(u)*D2c.D1c/||D1c||^2

    @tparam TheCurve    Curve type (e.g., Adaptor3d_Curve, Adaptor2d_Curve2d)
    @tparam TheCurveTool Tool for curve operations
    @tparam ThePOnC     Point on curve type
    @tparam ThePoint    Point type (e.g., gp_Pnt, gp_Pnt2d)
    @tparam TheVector   Vector type (e.g., gp_Vec, gp_Vec2d)
    @tparam TheSeqPOnC  Sequence of points on curve type
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt2d, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None:
        """
        Constructor with point and curve initialization.
        @param theP Point to compute distance from
        @param theC Curve to compute distance to
        """

    @overload
    def __init__(self, theOther: Geom2dInt_PCLocFOfTheLocateExtPCOfTheProjPCurOfGInter) -> None: ...

    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None:
        """
        Sets the curve field.
        @param theC Curve to set
        """

    def SetPoint(self, theP: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Sets the point field.
        @param theP Point to set
        """

    def Value(self, theU: float) -> tuple[bool, float]:
        """
        Calculation of F(u).
        @param theU Parameter value
        @param theF Output function value
        @return True if computation succeeded
        """

    def Derivative(self, theU: float) -> tuple[bool, float]:
        """
        Calculation of F'(u).
        @param theU Parameter value
        @param theDF Output derivative value
        @return True if computation succeeded
        """

    def Values(self, theU: float) -> tuple[bool, float, float]:
        """
        Calculation of F(u) and F'(u).
        @param theU Parameter value
        @param theF Output function value
        @param theDF Output derivative value
        @return True if computation succeeded
        """

    def GetStateNumber(self) -> int:
        """
        Save the found extremum.
        @return State number
        """

    def NbExt(self) -> int:
        """Return the number of found extrema."""

    def SquareDistance(self, theN: int) -> float:
        """
        Returns the Nth square distance.
        @param theN Index of extremum
        """

    def IsMin(self, theN: int) -> bool:
        """
        Shows if the Nth distance is a minimum.
        @param theN Index of extremum
        """

    def Point(self, theN: int) -> nanoocp.Extrema.Extrema_POnCurv2d:
        """
        Returns the Nth extremum point.
        @param theN Index of extremum
        """

    def SubIntervalInitialize(self, theUfirst: float, theUlast: float) -> None:
        """
        Determines boundaries of subinterval for root finding.
        @param theUfirst First parameter bound
        @param theUlast Last parameter bound
        """

    def SearchOfTolerance(self) -> float:
        """
        Computes a tolerance value. If 1st derivative of curve |D1| < Tol,
        it is considered D1=0.
        """

class Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter:
    """
    Template class for local extremum search between a point and a curve.
    Searches for a local extremum of distance between a point and a curve
    near an initial parameter value.

    @tparam TheCurve   Curve type (e.g., Adaptor3d_Curve, Adaptor2d_Curve2d, void*)
    @tparam TheTool    Tool for curve operations (e.g., Extrema_CurveTool, Extrema_Curve2dTool)
    @tparam ThePOnC    Point on curve type (e.g., Extrema_POnCurv, Extrema_POnCurv2d)
    @tparam ThePnt     Point type (e.g., gp_Pnt, gp_Pnt2d)
    @tparam ThePCLocF  Function type for root finding
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt2d, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theU0: float, theTolU: float) -> None:
        """
        Calculates the distance with a close point.
        The close point is defined by the parameter value U0.
        The function F(u)=distance(P,C(u)) has an extremum
        when g(u)=dF/du=0. The algorithm searches a zero
        near the close point.
        TolU is used to decide to stop the iterations.
        At the nth iteration, the criteria is:
        abs(Un - Un-1) < TolU.
        """

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt2d, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theU0: float, theUmin: float, theUsup: float, theTolU: float) -> None:
        """
        Calculates the distance with a close point.
        The close point is defined by the parameter value U0.
        The function F(u)=distance(P,C(u)) has an extremum
        when g(u)=dF/du=0. The algorithm searches a zero
        near the close point.
        Zeros are searched between Umin and Usup.
        TolU is used to decide to stop the iterations.
        At the nth iteration, the criteria is:
        abs(Un - Un-1) < TolU.
        """

    @overload
    def __init__(self, theOther: Geom2dInt_TheLocateExtPCOfTheProjPCurOfGInter) -> None: ...

    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theUmin: float, theUsup: float, theTolU: float) -> None:
        """Sets the fields of the algorithm."""

    def Perform(self, theP: nanoocp.gp.gp_Pnt2d, theU0: float) -> None:
        """
        The algorithm is done with the point P.
        An exception is raised if the fields have not been initialized.
        """

    def IsDone(self) -> bool:
        """Returns True if the distance is found."""

    def SquareDistance(self) -> float:
        """Returns the value of the extremum square distance."""

    def IsMin(self) -> bool:
        """Returns True if the extremum distance is a minimum."""

    def Point(self) -> nanoocp.Extrema.Extrema_POnCurv2d:
        """Returns the point of the extremum distance."""

class Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter(nanoocp.Intf.Intf_Polygon2d):
    @overload
    def __init__(self, Curve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, NbPnt: int, Domain: nanoocp.IntRes2d.IntRes2d_Domain, Tol: float) -> None:
        """Compute a polygon on the domain of the curve."""

    @overload
    def __init__(self, theOther: Geom2dInt_ThePolygon2dOfTheIntPCurvePCurveOfGInter) -> None: ...

    def ComputeWithBox(self, Curve: nanoocp.Adaptor2d.Adaptor2d_Curve2d, OtherBox: nanoocp.Bnd.Bnd_Box2d) -> None:
        """
        The current polygon is modified if most
        of the points of the polygon are
        outside the box <OtherBox>. In this
        situation, bounds are computed to build
        a polygon inside or near the OtherBox.
        """

    def DeflectionOverEstimation(self) -> float: ...

    def SetDeflectionOverEstimation(self, x: float) -> None: ...

    @overload
    def Closed(self, clos: bool) -> None: ...

    @overload
    def Closed(self) -> bool:
        """Returns True if the polyline is closed."""

    def NbSegments(self) -> int:
        """Give the number of Segments in the polyline."""

    def Segment(self, theIndex: int, theBegin: nanoocp.gp.gp_Pnt2d, theEnd: nanoocp.gp.gp_Pnt2d) -> None:
        """Returns the points of the segment <Index> in the Polygon."""

    def InfParameter(self) -> float:
        """
        Returns the parameter (On the curve)
        of the first point of the Polygon
        """

    def SupParameter(self) -> float:
        """
        Returns the parameter (On the curve)
        of the last point of the Polygon
        """

    def AutoIntersectionIsPossible(self) -> bool: ...

    def ApproxParamOnCurve(self, Index: int, ParamOnLine: float) -> float:
        """
        Give an approximation of the parameter on the curve
        according to the discretization of the Curve.
        """

    def CalculRegion(self, x: float, y: float, x1: float, x2: float, y1: float, y2: float) -> int: ...

    def Dump(self) -> None: ...

class Geom2dInt_TheProjPCurOfGInter:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Geom2dInt_TheProjPCurOfGInter) -> None: ...

    @overload
    @staticmethod
    def FindParameter(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Pnt: nanoocp.gp.gp_Pnt2d, Tol: float) -> float:
        """
        Returns the parameter V of the point on the
        parametric curve corresponding to the Point Pnt.
        The Correspondence between Pnt and the point P(V)
        on the parametric curve must be coherent with the
        way of determination of the signed distance
        between a point and the implicit curve.
        Tol is the tolerance on the distance between a point
        and the parametrised curve.
        In that case, no bounds are given. The research of
        the right parameter has to be made on the natural
        parametric domain of the curve.
        """

    @overload
    @staticmethod
    def FindParameter(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, Pnt: nanoocp.gp.gp_Pnt2d, LowParameter: float, HighParameter: float, Tol: float) -> float:
        """
        Returns the parameter V of the point on the
        parametric curve corresponding to the Point Pnt.
        The Correspondence between Pnt and the point P(V)
        on the parametric curve must be coherent with the
        way of determination of the signed distance
        between a point and the implicit curve.
        Tol is the tolerance on the distance between a point
        and the parametrised curve.
        LowParameter and HighParameter give the
        boundaries of the interval in which the parameter
        certainly lies. These parameters are given to
        implement a more efficient algorithm. So, it is not
        necessary to check that the returned value verifies
        LowParameter <= Value <= HighParameter.
        """
