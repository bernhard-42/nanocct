"""OCCT package Extrema (toolkit TKGeomBase)"""

import enum
from typing import TypeAlias, overload

import nanoocp.Adaptor2d
import nanoocp.Adaptor3d
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.GeomAdaptor
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp
import nanoocp.math
from nanoocp.math import math_Vector as math_Vector


class Extrema_ElementType(enum.IntEnum):
    Extrema_Node = 0

    Extrema_UIsoEdge = 1

    Extrema_VIsoEdge = 2

    Extrema_Face = 3

Extrema_Node: Extrema_ElementType = Extrema_ElementType.Extrema_Node

Extrema_UIsoEdge: Extrema_ElementType = Extrema_ElementType.Extrema_UIsoEdge

Extrema_VIsoEdge: Extrema_ElementType = Extrema_ElementType.Extrema_VIsoEdge

Extrema_Face: Extrema_ElementType = Extrema_ElementType.Extrema_Face

class Extrema_ExtAlgo(enum.IntEnum):
    Extrema_ExtAlgo_Grad = 0

    Extrema_ExtAlgo_Tree = 1

Extrema_ExtAlgo_Grad: Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad

Extrema_ExtAlgo_Tree: Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Tree

class Extrema_ExtFlag(enum.IntEnum):
    Extrema_ExtFlag_MIN = 0

    Extrema_ExtFlag_MAX = 1

    Extrema_ExtFlag_MINMAX = 2

Extrema_ExtFlag_MIN: Extrema_ExtFlag = Extrema_ExtFlag.Extrema_ExtFlag_MIN

Extrema_ExtFlag_MAX: Extrema_ExtFlag = Extrema_ExtFlag.Extrema_ExtFlag_MAX

Extrema_ExtFlag_MINMAX: Extrema_ExtFlag = Extrema_ExtFlag.Extrema_ExtFlag_MINMAX

class Extrema_CurveTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Extrema_CurveTool) -> None: ...

    @staticmethod
    def FirstParameter(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> float: ...

    @staticmethod
    def LastParameter(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> float: ...

    @staticmethod
    def Continuity(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    @staticmethod
    def NbIntervals(theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theS: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity <S>.
        May be one if Continuity(me) >= <S>
        """

    @staticmethod
    def Intervals(theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theT: nanoocp.NCollection.NCollection_Array1[float], theS: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        The array must provide enough room to accommodate for the parameters.
        i.e. T.Length() > NbIntervals()
        """

    @staticmethod
    def DeflCurvIntervals(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns the parameters bounding the intervals of subdivision of curve
        according to Curvature deflection. Value of deflection is defined in method.
        """

    @staticmethod
    def IsPeriodic(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> bool: ...

    @staticmethod
    def Period(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> float: ...

    @staticmethod
    def Resolution(theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theR3d: float) -> float: ...

    @staticmethod
    def GetType(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> nanoocp.GeomAbs.GeomAbs_CurveType: ...

    @staticmethod
    def Value(theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theU: float) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def D0(theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theU: float, theP: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def D1(theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theU: float, theP: nanoocp.gp.gp_Pnt, theV: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def D2(theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theU: float, theP: nanoocp.gp.gp_Pnt, theV1: nanoocp.gp.gp_Vec, theV2: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def D3(theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theU: float, theP: nanoocp.gp.gp_Pnt, theV1: nanoocp.gp.gp_Vec, theV2: nanoocp.gp.gp_Vec, theV3: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def DN(theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theU: float, theN: int) -> nanoocp.gp.gp_Vec: ...

    @staticmethod
    def Line(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> nanoocp.gp.gp_Lin: ...

    @staticmethod
    def Circle(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> nanoocp.gp.gp_Circ: ...

    @staticmethod
    def Ellipse(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> nanoocp.gp.gp_Elips: ...

    @staticmethod
    def Hyperbola(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> nanoocp.gp.gp_Hypr: ...

    @staticmethod
    def Parabola(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> nanoocp.gp.gp_Parab: ...

    @staticmethod
    def Degree(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> int: ...

    @staticmethod
    def IsRational(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> bool: ...

    @staticmethod
    def NbPoles(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> int: ...

    @staticmethod
    def NbKnots(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> int: ...

    @staticmethod
    def Bezier(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> nanoocp.Geom.Geom_BezierCurve: ...

    @staticmethod
    def BSpline(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> nanoocp.Geom.Geom_BSplineCurve: ...

class Extrema_POnCurv:
    """Definition of a point on curve."""

    @overload
    def __init__(self) -> None:
        """Creation of an indefinite point on curve."""

    @overload
    def __init__(self, theU: float, theP: nanoocp.gp.gp_Pnt) -> None:
        """
        Creation of a point on curve with a parameter
        value on the curve and a Pnt from gp.
        """

    @overload
    def __init__(self, theOther: Extrema_POnCurv) -> None: ...

    def SetValues(self, theU: float, theP: nanoocp.gp.gp_Pnt) -> None:
        """Sets the point and parameter values."""

    def Value(self) -> nanoocp.gp.gp_Pnt:
        """Returns the point."""

    def Parameter(self) -> float:
        """Returns the parameter on the curve."""

class Extrema_CCLocFOfLocECC(nanoocp.math.math_FunctionSetWithDerivatives):
    """
    Template class for function used to find extremal distance between two curves.
    This class inherits from math_FunctionSetWithDerivatives and is used by
    the algorithm math_FunctionSetRoot.

    @tparam TheCurve1 Type of the first curve (e.g., Adaptor3d_Curve)
    @tparam TheCurveTool1 Tool class for the first curve
    @tparam TheCurve2 Type of the second curve
    @tparam TheCurveTool2 Tool class for the second curve
    @tparam ThePOnC Point on curve type (e.g., Extrema_POnCurv)
    @tparam ThePoint Point type (e.g., gp_Pnt)
    @tparam TheVector Vector type (e.g., gp_Vec)
    @tparam TheSequenceOfPOnC Sequence of points on curve
    """

    @overload
    def __init__(self, theTol: float = 1e-10) -> None:
        """Default constructor with tolerance."""

    @overload
    def __init__(self, theC1: nanoocp.Adaptor3d.Adaptor3d_Curve, theC2: nanoocp.Adaptor3d.Adaptor3d_Curve, theTol: float = 1e-10) -> None:
        """Constructor with curves."""

    @overload
    def __init__(self, theOther: Extrema_CCLocFOfLocECC) -> None: ...

    def SetCurve(self, theRank: int, theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None:
        """Sets the curve for the specified rank (1 or 2)."""

    def SetTolerance(self, theTol: float) -> None:
        """Sets the tolerance."""

    def NbVariables(self) -> int:
        """Returns the number of variables (2)."""

    def NbEquations(self) -> int:
        """Returns the number of equations (2)."""

    def Value(self, theUV: nanoocp.math.math_Vector, theF: nanoocp.math.math_Vector) -> bool:
        """Calculate Fi(U,V)."""

    def Derivatives(self, theUV: nanoocp.math.math_Vector, theDF: nanoocp.math.math_Matrix) -> bool:
        """Calculate Fi'(U,V)."""

    def Values(self, theUV: nanoocp.math.math_Vector, theF: nanoocp.math.math_Vector, theDF: nanoocp.math.math_Matrix) -> bool:
        """Calculate Fi(U,V) and Fi'(U,V)."""

    def GetStateNumber(self) -> int:
        """Save the found extremum."""

    def NbExt(self) -> int:
        """Return the number of found extrema."""

    def SquareDistance(self, theN: int) -> float:
        """Return the value of the Nth distance."""

    def Points(self, theN: int, theP1: Extrema_POnCurv, theP2: Extrema_POnCurv) -> None:
        """Return the points of the Nth extreme distance."""

    def Tolerance(self) -> float:
        """
        Returns a tolerance specified in the constructor or in SetTolerance() method.
        """

    def SubIntervalInitialize(self, theUfirst: nanoocp.math.math_Vector, theUlast: nanoocp.math.math_Vector) -> None:
        """Determines boundaries of subinterval for find of root."""

class Extrema_Curve2dTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Extrema_Curve2dTool) -> None: ...

    @staticmethod
    def FirstParameter(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> float: ...

    @staticmethod
    def LastParameter(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> float: ...

    @staticmethod
    def Continuity(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    @staticmethod
    def NbIntervals(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theS: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        If necessary, breaks the curve in intervals of continuity <S>.
        And returns the number of intervals.
        """

    @staticmethod
    def Intervals(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theT: nanoocp.NCollection.NCollection_Array1[float], theS: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """Stores in <T> the parameters bounding the intervals of continuity <S>."""

    @staticmethod
    def DeflCurvIntervals(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns the parameters bounding the intervals of subdivision of curve
        according to Curvature deflection. Value of deflection is defined in method.
        """

    @staticmethod
    def IsClosed(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> bool: ...

    @staticmethod
    def IsPeriodic(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> bool: ...

    @staticmethod
    def Period(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> float: ...

    @staticmethod
    def Value(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theU: float) -> nanoocp.gp.gp_Pnt2d:
        """Computes the point of parameter U on the curve."""

    @staticmethod
    def D0(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theU: float, theP: nanoocp.gp.gp_Pnt2d) -> None:
        """Computes the point of parameter U on the curve."""

    @staticmethod
    def D1(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theU: float, theP: nanoocp.gp.gp_Pnt2d, theV: nanoocp.gp.gp_Vec2d) -> None:
        """
        Computes the point of parameter U on the curve with its first derivative.
        """

    @staticmethod
    def D2(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theU: float, theP: nanoocp.gp.gp_Pnt2d, theV1: nanoocp.gp.gp_Vec2d, theV2: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2.
        """

    @staticmethod
    def D3(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theU: float, theP: nanoocp.gp.gp_Pnt2d, theV1: nanoocp.gp.gp_Vec2d, theV2: nanoocp.gp.gp_Vec2d, theV3: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first, the second and the third derivative.
        """

    @staticmethod
    def DN(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theU: float, theN: int) -> nanoocp.gp.gp_Vec2d:
        """
        The returned vector gives the value of the derivative for the order of derivation N.
        """

    @staticmethod
    def Resolution(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theR3d: float) -> float:
        """
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """

    @staticmethod
    def GetType(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """
        Returns the type of the curve in the current interval:
        Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """

    @staticmethod
    def Line(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.gp.gp_Lin2d: ...

    @staticmethod
    def Circle(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.gp.gp_Circ2d: ...

    @staticmethod
    def Ellipse(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.gp.gp_Elips2d: ...

    @staticmethod
    def Hyperbola(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.gp.gp_Hypr2d: ...

    @staticmethod
    def Parabola(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.gp.gp_Parab2d: ...

    @staticmethod
    def Degree(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> int: ...

    @staticmethod
    def IsRational(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> bool: ...

    @staticmethod
    def NbPoles(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> int: ...

    @staticmethod
    def NbKnots(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> int: ...

    @staticmethod
    def Bezier(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.Geom2d.Geom2d_BezierCurve: ...

    @staticmethod
    def BSpline(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

class Extrema_POnCurv2d:
    """Definition of a point on 2D curve."""

    @overload
    def __init__(self) -> None:
        """Creation of an indefinite point on curve."""

    @overload
    def __init__(self, theU: float, theP: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Creation of a point on curve with a parameter
        value on the curve and a Pnt from gp.
        """

    @overload
    def __init__(self, theOther: Extrema_POnCurv2d) -> None: ...

    def SetValues(self, theU: float, theP: nanoocp.gp.gp_Pnt2d) -> None:
        """Sets the point and parameter values."""

    def Value(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns the point."""

    def Parameter(self) -> float:
        """Returns the parameter on the curve."""

class Extrema_CCLocFOfLocECC2d(nanoocp.math.math_FunctionSetWithDerivatives):
    """
    Template class for function used to find extremal distance between two curves.
    This class inherits from math_FunctionSetWithDerivatives and is used by
    the algorithm math_FunctionSetRoot.

    @tparam TheCurve1 Type of the first curve (e.g., Adaptor3d_Curve)
    @tparam TheCurveTool1 Tool class for the first curve
    @tparam TheCurve2 Type of the second curve
    @tparam TheCurveTool2 Tool class for the second curve
    @tparam ThePOnC Point on curve type (e.g., Extrema_POnCurv)
    @tparam ThePoint Point type (e.g., gp_Pnt)
    @tparam TheVector Vector type (e.g., gp_Vec)
    @tparam TheSequenceOfPOnC Sequence of points on curve
    """

    @overload
    def __init__(self, theTol: float = 1e-10) -> None:
        """Default constructor with tolerance."""

    @overload
    def __init__(self, theC1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theC2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theTol: float = 1e-10) -> None:
        """Constructor with curves."""

    @overload
    def __init__(self, theOther: Extrema_CCLocFOfLocECC2d) -> None: ...

    def SetCurve(self, theRank: int, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None:
        """Sets the curve for the specified rank (1 or 2)."""

    def SetTolerance(self, theTol: float) -> None:
        """Sets the tolerance."""

    def NbVariables(self) -> int:
        """Returns the number of variables (2)."""

    def NbEquations(self) -> int:
        """Returns the number of equations (2)."""

    def Value(self, theUV: nanoocp.math.math_Vector, theF: nanoocp.math.math_Vector) -> bool:
        """Calculate Fi(U,V)."""

    def Derivatives(self, theUV: nanoocp.math.math_Vector, theDF: nanoocp.math.math_Matrix) -> bool:
        """Calculate Fi'(U,V)."""

    def Values(self, theUV: nanoocp.math.math_Vector, theF: nanoocp.math.math_Vector, theDF: nanoocp.math.math_Matrix) -> bool:
        """Calculate Fi(U,V) and Fi'(U,V)."""

    def GetStateNumber(self) -> int:
        """Save the found extremum."""

    def NbExt(self) -> int:
        """Return the number of found extrema."""

    def SquareDistance(self, theN: int) -> float:
        """Return the value of the Nth distance."""

    def Points(self, theN: int, theP1: Extrema_POnCurv2d, theP2: Extrema_POnCurv2d) -> None:
        """Return the points of the Nth extreme distance."""

    def Tolerance(self) -> float:
        """
        Returns a tolerance specified in the constructor or in SetTolerance() method.
        """

    def SubIntervalInitialize(self, theUfirst: nanoocp.math.math_Vector, theUlast: nanoocp.math.math_Vector) -> None:
        """Determines boundaries of subinterval for find of root."""

class Extrema_PCFOfEPCOfExtPC(nanoocp.math.math_FunctionWithDerivative):
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
    def __init__(self, theP: nanoocp.gp.gp_Pnt, theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None:
        """
        Constructor with point and curve initialization.
        @param theP Point to compute distance from
        @param theC Curve to compute distance to
        """

    @overload
    def __init__(self, theOther: Extrema_PCFOfEPCOfExtPC) -> None: ...

    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None:
        """
        Sets the curve field.
        @param theC Curve to set
        """

    def SetPoint(self, theP: nanoocp.gp.gp_Pnt) -> None:
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

    def Point(self, theN: int) -> Extrema_POnCurv:
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

class Extrema_EPCOfExtPC:
    """
    Generic class for finding extremal distances between a point and a curve.

    This template class searches for all parameter values u where the distance
    function F(u) = distance(P, C(u)) has an extremum, i.e., where dF/du = 0.

    @tparam TheCurve   The curve type (e.g., Adaptor3d_Curve, Adaptor2d_Curve2d)
    @tparam TheTool    The curve tool providing static methods (FirstParameter, LastParameter)
    @tparam ThePOnC    The point-on-curve type (e.g., Extrema_POnCurv, Extrema_POnCurv2d)
    @tparam ThePoint   The point type (e.g., gp_Pnt, gp_Pnt2d)
    @tparam ThePCF     The point-curve function type for extremum computation
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theNbSample: int, theTolU: float, theTolF: float) -> None:
        """
        Calculates all extremum distances between point P and curve C.
        @param theP       The point
        @param theC       The curve
        @param theNbSample Number of sample points for root finding
        @param theTolU    Tolerance on parameter u
        @param theTolF    Tolerance on function value
        """

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theNbSample: int, theUmin: float, theUsup: float, theTolU: float, theTolF: float) -> None:
        """
        Calculates all extremum distances in a given parameter range.
        @param theP       The point
        @param theC       The curve
        @param theNbSample Number of sample points for root finding
        @param theUmin    Lower bound of parameter range
        @param theUsup    Upper bound of parameter range
        @param theTolU    Tolerance on parameter u
        @param theTolF    Tolerance on function value
        """

    @overload
    def __init__(self, theOther: Extrema_EPCOfExtPC) -> None: ...

    @overload
    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theNbU: int, theTolU: float, theTolF: float) -> None:
        """
        Initializes the algorithm with the full curve parameter range.
        @param theC       The curve
        @param theNbU     Number of sample points
        @param theTolU    Tolerance on parameter u
        @param theTolF    Tolerance on function value
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theNbU: int, theUmin: float, theUsup: float, theTolU: float, theTolF: float) -> None:
        """
        Initializes the algorithm with a specified parameter range.
        @param theC       The curve
        @param theNbU     Number of sample points
        @param theUmin    Lower bound of parameter range
        @param theUsup    Upper bound of parameter range
        @param theTolU    Tolerance on parameter u
        @param theTolF    Tolerance on function value
        """

    @overload
    def Initialize(self, theNbU: int, theUmin: float, theUsup: float, theTolU: float, theTolF: float) -> None:
        """
        Initializes only the parameter range and tolerances.
        @param theNbU     Number of sample points
        @param theUmin    Lower bound of parameter range
        @param theUsup    Upper bound of parameter range
        @param theTolU    Tolerance on parameter u
        @param theTolF    Tolerance on function value
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None:
        """
        Initializes the curve for the function.
        @param theC The curve
        """

    def Perform(self, theP: nanoocp.gp.gp_Pnt) -> None:
        """
        Performs the extremum search for the given point.
        @param theP The point to find extrema from
        """

    def IsDone(self) -> bool:
        """Returns true if the distances are found."""

    def NbExt(self) -> int:
        """
        Returns the number of extremum distances.
        @return Number of extrema found
        """

    def SquareDistance(self, theN: int) -> float:
        """
        Returns the Nth extremum square distance.
        @param theN Index of the extremum (1-based)
        @return Square distance value
        """

    def IsMin(self, theN: int) -> bool:
        """
        Returns true if the Nth extremum distance is a minimum.
        @param theN Index of the extremum (1-based)
        @return true if minimum, false if maximum
        """

    def Point(self, theN: int) -> Extrema_POnCurv:
        """
        Returns the point of the Nth extremum distance.
        @param theN Index of the extremum (1-based)
        @return The point on curve
        """

class Extrema_ExtPElC:
    """
    It calculates all the distances between a point
    and an elementary curve.
    These distances can be minimum or maximum.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, C: nanoocp.gp.gp_Lin, Tol: float, Uinf: float, Usup: float) -> None:
        """
        Calculates the extremum distance between the
        point P and the segment [Uinf,Usup] of the line C.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, C: nanoocp.gp.gp_Circ, Tol: float, Uinf: float, Usup: float) -> None:
        """
        Calculates the 2 extremum distances between the
        point P and the segment [Uinf,Usup] of the circle C.
        Tol is used to determine
        if P is on the axis of the circle or
        if an extremum is on an endpoint of the segment.
        If P is on the axis of the circle,
        there are infinite solution then IsDone(me)=False.
        The conditions on the Uinf and Usup are:
        0. <= Uinf <= 2.*PI and Usup > Uinf.
        If Usup > Uinf + 2.*PI, then only the solutions in
        the range [Uinf,Uinf+2.*PI[ are computed.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, C: nanoocp.gp.gp_Elips, Tol: float, Uinf: float, Usup: float) -> None:
        """
        Calculates the 4 extremum distances between the
        point P and the segment [Uinf,Usup] of the ellipse C.
        Tol is used to determine
        if the point is on the axis of the ellipse and
        if the major radius is equal to the minor radius or
        if an extremum is on an endpoint of the segment.
        If P is on the axis of the ellipse,
        there are infinite solution then IsDone(me)=False.
        The conditions on the Uinf and Usup are:
        0. <= Uinf <= 2.*PI and Usup > Uinf.
        If Usup > Uinf + 2.*PI, then only the solutions in
        the range [Uinf,Uinf+2.*PI[ are computed.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, C: nanoocp.gp.gp_Hypr, Tol: float, Uinf: float, Usup: float) -> None:
        """
        Calculates the extremum distances between the
        point P and the segment [Uinf,Usup] of the hyperbola
        C.
        Tol is used to determine if two solutions u and v
        are identical; the condition is:
        dist(C(u),C(v)) < Tol.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, C: nanoocp.gp.gp_Parab, Tol: float, Uinf: float, Usup: float) -> None:
        """
        Calculates the 4 extremum distances between the
        point P and the segment [Uinf,Usup] of the parabola
        C.
        Tol is used to determine if two solutions u and v
        are identical; the condition is:
        dist(C(u),C(v)) < Tol.
        """

    @overload
    def __init__(self, theOther: Extrema_ExtPElC) -> None: ...

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pnt, C: nanoocp.gp.gp_Lin, Tol: float, Uinf: float, Usup: float) -> None: ...

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pnt, C: nanoocp.gp.gp_Circ, Tol: float, Uinf: float, Usup: float) -> None: ...

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pnt, C: nanoocp.gp.gp_Elips, Tol: float, Uinf: float, Usup: float) -> None: ...

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pnt, C: nanoocp.gp.gp_Hypr, Tol: float, Uinf: float, Usup: float) -> None: ...

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pnt, C: nanoocp.gp.gp_Parab, Tol: float, Uinf: float, Usup: float) -> None: ...

    def IsDone(self) -> bool:
        """True if the distances are found."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the Nth extremum square distance."""

    def IsMin(self, N: int) -> bool:
        """
        Returns True if the Nth extremum distance is a
        minimum.
        """

    def Point(self, N: int) -> Extrema_POnCurv:
        """Returns the point of the Nth extremum distance."""

class Extrema_ExtPC:
    """
    Generic class for computing extremal distances between a point and a curve.

    This template class provides comprehensive extremum search functionality,
    handling different curve types (lines, circles, ellipses, parabolas,
    hyperbolas, Bezier, BSpline, and general curves) with optimized algorithms.

    @tparam TheCurve       The curve type (e.g., Adaptor3d_Curve, Adaptor2d_Curve2d)
    @tparam TheCurveTool   The curve tool providing static methods
    @tparam TheExtPElC     The elementary curve extremum class
    @tparam ThePoint       The point type (e.g., gp_Pnt, gp_Pnt2d)
    @tparam TheVector      The vector type (e.g., gp_Vec, gp_Vec2d)
    @tparam ThePOnC        The point-on-curve type
    @tparam TheSequenceOfPOnC The sequence of points on curve
    @tparam TheEPC         The general extremum point-curve class
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theTolF: float = 1e-10) -> None:
        """
        Calculates all extremum distances between point P and curve C
        using the full curve parameter range.
        @param theP    The point
        @param theC    The curve
        @param theTolF Tolerance on function value (default 1.0e-10)
        """

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theUinf: float, theUsup: float, theTolF: float = 1e-10) -> None:
        """
        Calculates all extremum distances between point P and curve C
        within the specified parameter range.
        @param theP    The point
        @param theC    The curve
        @param theUinf Lower bound of parameter range
        @param theUsup Upper bound of parameter range
        @param theTolF Tolerance on function value (default 1.0e-10)
        """

    @overload
    def __init__(self, theOther: Extrema_ExtPC) -> None: ...

    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theUinf: float, theUsup: float, theTolF: float = 1e-10) -> None:
        """
        Initializes the algorithm with curve and parameter range.
        @param theC    The curve
        @param theUinf Lower bound of parameter range
        @param theUsup Upper bound of parameter range
        @param theTolF Tolerance on function value (default 1.0e-10)
        """

    def Perform(self, theP: nanoocp.gp.gp_Pnt) -> None:
        """
        Performs the extremum computation for the given point.
        @param theP The point to find extrema from
        """

    def IsDone(self) -> bool:
        """Returns true if the distances are found."""

    def SquareDistance(self, theN: int) -> float:
        """
        Returns the Nth extremum square distance.
        @param theN Index of the extremum (1-based)
        @return Square distance value
        """

    def NbExt(self) -> int:
        """
        Returns the number of extremum distances.
        @return Number of extrema found
        """

    def IsMin(self, theN: int) -> bool:
        """
        Returns true if the Nth extremum distance is a minimum.
        @param theN Index of the extremum (1-based)
        @return true if minimum, false if maximum
        """

    def Point(self, theN: int) -> Extrema_POnCurv:
        """
        Returns the point of the Nth extremum distance.
        @param theN Index of the extremum (1-based)
        @return The point on curve
        """

    def TrimmedSquareDistances(self, theP1: nanoocp.gp.gp_Pnt, theP2: nanoocp.gp.gp_Pnt) -> tuple[float, float]:
        """
        Returns the distances at curve endpoints.
        @param[out] theDist1 Square distance to first point
        @param[out] theDist2 Square distance to last point
        @param[out] theP1 First point on curve
        @param[out] theP2 Last point on curve
        """

class Extrema_GlobOptFuncCCC0(nanoocp.math.math_MultipleVarFunction):
    """
    This class implements function which calculate Eucluidean distance
    between point on curve and point on other curve in case of C1 and C2 continuity is C0.
    """

    @overload
    def __init__(self, C1: nanoocp.Adaptor3d.Adaptor3d_Curve, C2: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None: ...

    @overload
    def __init__(self, theOther: Extrema_GlobOptFuncCCC0) -> None: ...

    def NbVariables(self) -> int: ...

    def Value(self, X: nanoocp.math.math_Vector) -> tuple[bool, float]: ...

class Extrema_GlobOptFuncCCC1(nanoocp.math.math_MultipleVarFunctionWithGradient):
    """
    This class implements function which calculate Eucluidean distance
    between point on curve and point on other curve in case of C1 and C2 continuity is C1.
    """

    @overload
    def __init__(self, C1: nanoocp.Adaptor3d.Adaptor3d_Curve, C2: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None: ...

    @overload
    def __init__(self, theOther: Extrema_GlobOptFuncCCC1) -> None: ...

    def NbVariables(self) -> int: ...

    def Value(self, X: nanoocp.math.math_Vector) -> tuple[bool, float]: ...

    def Gradient(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> bool: ...

    def Values(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> tuple[bool, float]: ...

class Extrema_GlobOptFuncCCC2(nanoocp.math.math_MultipleVarFunctionWithHessian):
    """
    This class implements function which calculate Eucluidean distance
    between point on curve and point on other curve in case of C1 and C2 continuity is C2.
    """

    @overload
    def __init__(self, C1: nanoocp.Adaptor3d.Adaptor3d_Curve, C2: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None: ...

    @overload
    def __init__(self, theOther: Extrema_GlobOptFuncCCC2) -> None: ...

    def NbVariables(self) -> int: ...

    def Value(self, X: nanoocp.math.math_Vector) -> tuple[bool, float]: ...

    def Gradient(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> bool: ...

    @overload
    def Values(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> tuple[bool, float]: ...

    @overload
    def Values(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector, H: nanoocp.math.math_Matrix) -> tuple[bool, float]: ...

class Extrema_ECC:
    """
    Template class for computing extremal distances between two curves.
    The function F(u,v)=distance(C1(u),C2(v)) has an extremum when gradient(f)=0.
    The algorithm uses Evtushenko's global optimization solver.

    @tparam TheCurve1 Type of the first curve (e.g., Adaptor3d_Curve)
    @tparam TheCurveTool1 Tool class for the first curve
    @tparam TheCurve2 Type of the second curve
    @tparam TheCurveTool2 Tool class for the second curve
    @tparam ThePOnC Point on curve type (e.g., Extrema_POnCurv)
    @tparam ThePoint Point type (e.g., gp_Pnt)
    @tparam TheExtPC Point-to-curve extremum class (e.g., Extrema_ExtPC)
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theC1: nanoocp.Adaptor3d.Adaptor3d_Curve, theC2: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None:
        """Constructor with two curves."""

    @overload
    def __init__(self, theC1: nanoocp.Adaptor3d.Adaptor3d_Curve, theC2: nanoocp.Adaptor3d.Adaptor3d_Curve, theUinf: float, theUsup: float, theVinf: float, theVsup: float) -> None:
        """Constructor with two curves and parameter bounds."""

    @overload
    def __init__(self, theOther: Extrema_ECC) -> None: ...

    def SetParams(self, theC1: nanoocp.Adaptor3d.Adaptor3d_Curve, theC2: nanoocp.Adaptor3d.Adaptor3d_Curve, theUinf: float, theUsup: float, theVinf: float, theVsup: float) -> None:
        """Sets parameters for computation."""

    def SetTolerance(self, theTol: float) -> None:
        """Sets the tolerance."""

    def SetSingleSolutionFlag(self, theFlag: bool) -> None:
        """Set flag for single extrema computation."""

    def GetSingleSolutionFlag(self) -> bool:
        """Get flag for single extrema computation."""

    def Perform(self) -> None:
        """Performs calculations."""

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def IsParallel(self) -> bool:
        """Returns state of myParallel flag."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, theN: int = 1) -> float:
        """Returns the value of the Nth square extremum distance."""

    def Points(self, theN: int, theP1: Extrema_POnCurv, theP2: Extrema_POnCurv) -> None:
        """Returns the points of the Nth extremum distance."""

class Extrema_PCFOfEPCOfExtPC2d(nanoocp.math.math_FunctionWithDerivative):
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
    def __init__(self, theOther: Extrema_PCFOfEPCOfExtPC2d) -> None: ...

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

    def Point(self, theN: int) -> Extrema_POnCurv2d:
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

class Extrema_EPCOfExtPC2d:
    """
    Generic class for finding extremal distances between a point and a curve.

    This template class searches for all parameter values u where the distance
    function F(u) = distance(P, C(u)) has an extremum, i.e., where dF/du = 0.

    @tparam TheCurve   The curve type (e.g., Adaptor3d_Curve, Adaptor2d_Curve2d)
    @tparam TheTool    The curve tool providing static methods (FirstParameter, LastParameter)
    @tparam ThePOnC    The point-on-curve type (e.g., Extrema_POnCurv, Extrema_POnCurv2d)
    @tparam ThePoint   The point type (e.g., gp_Pnt, gp_Pnt2d)
    @tparam ThePCF     The point-curve function type for extremum computation
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt2d, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theNbSample: int, theTolU: float, theTolF: float) -> None:
        """
        Calculates all extremum distances between point P and curve C.
        @param theP       The point
        @param theC       The curve
        @param theNbSample Number of sample points for root finding
        @param theTolU    Tolerance on parameter u
        @param theTolF    Tolerance on function value
        """

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt2d, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theNbSample: int, theUmin: float, theUsup: float, theTolU: float, theTolF: float) -> None:
        """
        Calculates all extremum distances in a given parameter range.
        @param theP       The point
        @param theC       The curve
        @param theNbSample Number of sample points for root finding
        @param theUmin    Lower bound of parameter range
        @param theUsup    Upper bound of parameter range
        @param theTolU    Tolerance on parameter u
        @param theTolF    Tolerance on function value
        """

    @overload
    def __init__(self, theOther: Extrema_EPCOfExtPC2d) -> None: ...

    @overload
    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theNbU: int, theTolU: float, theTolF: float) -> None:
        """
        Initializes the algorithm with the full curve parameter range.
        @param theC       The curve
        @param theNbU     Number of sample points
        @param theTolU    Tolerance on parameter u
        @param theTolF    Tolerance on function value
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theNbU: int, theUmin: float, theUsup: float, theTolU: float, theTolF: float) -> None:
        """
        Initializes the algorithm with a specified parameter range.
        @param theC       The curve
        @param theNbU     Number of sample points
        @param theUmin    Lower bound of parameter range
        @param theUsup    Upper bound of parameter range
        @param theTolU    Tolerance on parameter u
        @param theTolF    Tolerance on function value
        """

    @overload
    def Initialize(self, theNbU: int, theUmin: float, theUsup: float, theTolU: float, theTolF: float) -> None:
        """
        Initializes only the parameter range and tolerances.
        @param theNbU     Number of sample points
        @param theUmin    Lower bound of parameter range
        @param theUsup    Upper bound of parameter range
        @param theTolU    Tolerance on parameter u
        @param theTolF    Tolerance on function value
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None:
        """
        Initializes the curve for the function.
        @param theC The curve
        """

    def Perform(self, theP: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Performs the extremum search for the given point.
        @param theP The point to find extrema from
        """

    def IsDone(self) -> bool:
        """Returns true if the distances are found."""

    def NbExt(self) -> int:
        """
        Returns the number of extremum distances.
        @return Number of extrema found
        """

    def SquareDistance(self, theN: int) -> float:
        """
        Returns the Nth extremum square distance.
        @param theN Index of the extremum (1-based)
        @return Square distance value
        """

    def IsMin(self, theN: int) -> bool:
        """
        Returns true if the Nth extremum distance is a minimum.
        @param theN Index of the extremum (1-based)
        @return true if minimum, false if maximum
        """

    def Point(self, theN: int) -> Extrema_POnCurv2d:
        """
        Returns the point of the Nth extremum distance.
        @param theN Index of the extremum (1-based)
        @return The point on curve
        """

class Extrema_ExtPElC2d:
    """
    It calculates all the distances between a point
    and an elementary curve.
    These distances can be minimum or maximum.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt2d, C: nanoocp.gp.gp_Lin2d, Tol: float, Uinf: float, Usup: float) -> None:
        """
        Calculates the extremum distance between the
        point P and the segment [Uinf,Usup] of the line L.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt2d, C: nanoocp.gp.gp_Circ2d, Tol: float, Uinf: float, Usup: float) -> None:
        """
        Calculates the 2 extremum distances between the
        point P and the segment [Uinf,Usup] of the circle C.
        Tol is used to determine
        if P is on the axis of the circle or
        if an extremum is on an endpoint of the segment.
        If P is on the axis of the circle,
        there are infinite solution then IsDone(me)=False.
        The conditions on the Uinf and Usup are:
        0. <= Uinf <= 2.*PI and Usup > Uinf.
        If Usup > Uinf + 2.*PI, then only the solutions in
        the range [Uinf,Uinf+2.*PI[ are computed.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt2d, C: nanoocp.gp.gp_Elips2d, Tol: float, Uinf: float, Usup: float) -> None:
        """
        Calculates the 4 extremum distances between the
        point P and the segment [Uinf,Usup] of the ellipse C.
        Tol is used to determine
        if the point is on the axis of the ellipse and
        if the major radius is equal to the minor radius or
        if an extremum is on an endpoint of the segment.
        If P is on the axis of the ellipse,
        there are infinite solution then IsDone(me)=False.
        The conditions on the Uinf and Usup are:
        0. <= Uinf <= 2.*PI and Usup > Uinf.
        If Usup > Uinf + 2.*PI, then only the solutions in
        the range [Uinf,Uinf+2.*PI[ are computed.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt2d, C: nanoocp.gp.gp_Hypr2d, Tol: float, Uinf: float, Usup: float) -> None:
        """
        Calculates the extremum distances between the
        point P and the segment [Uinf,Usup] of the hyperbola
        C.
        Tol is used to determine if two solutions u and v
        are identical; the condition is:
        dist(C(u),C(v)) < Tol.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt2d, C: nanoocp.gp.gp_Parab2d, Tol: float, Uinf: float, Usup: float) -> None:
        """
        Calculates the 4 extremum distances between the
        point P and the segment [Uinf,Usup] of the parabola
        C.
        Tol is used to determine if two solutions u and v
        are identical; the condition is:
        dist(C(u),C(v)) < Tol.
        """

    @overload
    def __init__(self, theOther: Extrema_ExtPElC2d) -> None: ...

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pnt2d, L: nanoocp.gp.gp_Lin2d, Tol: float, Uinf: float, Usup: float) -> None: ...

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pnt2d, C: nanoocp.gp.gp_Circ2d, Tol: float, Uinf: float, Usup: float) -> None: ...

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pnt2d, C: nanoocp.gp.gp_Elips2d, Tol: float, Uinf: float, Usup: float) -> None: ...

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pnt2d, C: nanoocp.gp.gp_Hypr2d, Tol: float, Uinf: float, Usup: float) -> None: ...

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pnt2d, C: nanoocp.gp.gp_Parab2d, Tol: float, Uinf: float, Usup: float) -> None: ...

    def IsDone(self) -> bool:
        """True if the distances are found."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the Nth extremum square distance."""

    def IsMin(self, N: int) -> bool:
        """
        Returns True if the Nth extremum distance is a
        minimum.
        """

    def Point(self, N: int) -> Extrema_POnCurv2d:
        """Returns the point of the Nth extremum distance."""

class Extrema_ExtPC2d:
    """
    Generic class for computing extremal distances between a point and a curve.

    This template class provides comprehensive extremum search functionality,
    handling different curve types (lines, circles, ellipses, parabolas,
    hyperbolas, Bezier, BSpline, and general curves) with optimized algorithms.

    @tparam TheCurve       The curve type (e.g., Adaptor3d_Curve, Adaptor2d_Curve2d)
    @tparam TheCurveTool   The curve tool providing static methods
    @tparam TheExtPElC     The elementary curve extremum class
    @tparam ThePoint       The point type (e.g., gp_Pnt, gp_Pnt2d)
    @tparam TheVector      The vector type (e.g., gp_Vec, gp_Vec2d)
    @tparam ThePOnC        The point-on-curve type
    @tparam TheSequenceOfPOnC The sequence of points on curve
    @tparam TheEPC         The general extremum point-curve class
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt2d, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theTolF: float = 1e-10) -> None:
        """
        Calculates all extremum distances between point P and curve C
        using the full curve parameter range.
        @param theP    The point
        @param theC    The curve
        @param theTolF Tolerance on function value (default 1.0e-10)
        """

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt2d, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theUinf: float, theUsup: float, theTolF: float = 1e-10) -> None:
        """
        Calculates all extremum distances between point P and curve C
        within the specified parameter range.
        @param theP    The point
        @param theC    The curve
        @param theUinf Lower bound of parameter range
        @param theUsup Upper bound of parameter range
        @param theTolF Tolerance on function value (default 1.0e-10)
        """

    @overload
    def __init__(self, theOther: Extrema_ExtPC2d) -> None: ...

    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theUinf: float, theUsup: float, theTolF: float = 1e-10) -> None:
        """
        Initializes the algorithm with curve and parameter range.
        @param theC    The curve
        @param theUinf Lower bound of parameter range
        @param theUsup Upper bound of parameter range
        @param theTolF Tolerance on function value (default 1.0e-10)
        """

    def Perform(self, theP: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Performs the extremum computation for the given point.
        @param theP The point to find extrema from
        """

    def IsDone(self) -> bool:
        """Returns true if the distances are found."""

    def SquareDistance(self, theN: int) -> float:
        """
        Returns the Nth extremum square distance.
        @param theN Index of the extremum (1-based)
        @return Square distance value
        """

    def NbExt(self) -> int:
        """
        Returns the number of extremum distances.
        @return Number of extrema found
        """

    def IsMin(self, theN: int) -> bool:
        """
        Returns true if the Nth extremum distance is a minimum.
        @param theN Index of the extremum (1-based)
        @return true if minimum, false if maximum
        """

    def Point(self, theN: int) -> Extrema_POnCurv2d:
        """
        Returns the point of the Nth extremum distance.
        @param theN Index of the extremum (1-based)
        @return The point on curve
        """

    def TrimmedSquareDistances(self, theP1: nanoocp.gp.gp_Pnt2d, theP2: nanoocp.gp.gp_Pnt2d) -> tuple[float, float]:
        """
        Returns the distances at curve endpoints.
        @param[out] theDist1 Square distance to first point
        @param[out] theDist2 Square distance to last point
        @param[out] theP1 First point on curve
        @param[out] theP2 Last point on curve
        """

class Extrema_ECC2d:
    """
    Template class for computing extremal distances between two curves.
    The function F(u,v)=distance(C1(u),C2(v)) has an extremum when gradient(f)=0.
    The algorithm uses Evtushenko's global optimization solver.

    @tparam TheCurve1 Type of the first curve (e.g., Adaptor3d_Curve)
    @tparam TheCurveTool1 Tool class for the first curve
    @tparam TheCurve2 Type of the second curve
    @tparam TheCurveTool2 Tool class for the second curve
    @tparam ThePOnC Point on curve type (e.g., Extrema_POnCurv)
    @tparam ThePoint Point type (e.g., gp_Pnt)
    @tparam TheExtPC Point-to-curve extremum class (e.g., Extrema_ExtPC)
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theC1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theC2: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None:
        """Constructor with two curves."""

    @overload
    def __init__(self, theC1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theC2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theUinf: float, theUsup: float, theVinf: float, theVsup: float) -> None:
        """Constructor with two curves and parameter bounds."""

    @overload
    def __init__(self, theOther: Extrema_ECC2d) -> None: ...

    def SetParams(self, theC1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theC2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theUinf: float, theUsup: float, theVinf: float, theVsup: float) -> None:
        """Sets parameters for computation."""

    def SetTolerance(self, theTol: float) -> None:
        """Sets the tolerance."""

    def SetSingleSolutionFlag(self, theFlag: bool) -> None:
        """Set flag for single extrema computation."""

    def GetSingleSolutionFlag(self) -> bool:
        """Get flag for single extrema computation."""

    def Perform(self) -> None:
        """Performs calculations."""

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def IsParallel(self) -> bool:
        """Returns state of myParallel flag."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, theN: int = 1) -> float:
        """Returns the value of the Nth square extremum distance."""

    def Points(self, theN: int, theP1: Extrema_POnCurv2d, theP2: Extrema_POnCurv2d) -> None:
        """Returns the points of the Nth extremum distance."""

class Extrema_ExtCC:
    """
    It calculates all the distance between two curves.
    These distances can be maximum or minimum.
    """

    @overload
    def __init__(self, TolC1: float = 1e-10, TolC2: float = 1e-10) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Adaptor3d.Adaptor3d_Curve, C2: nanoocp.Adaptor3d.Adaptor3d_Curve, TolC1: float = 1e-10, TolC2: float = 1e-10) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Adaptor3d.Adaptor3d_Curve, C2: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, V1: float, V2: float, TolC1: float = 1e-10, TolC2: float = 1e-10) -> None:
        """It calculates all the distances."""

    @overload
    def Initialize(self, C1: nanoocp.Adaptor3d.Adaptor3d_Curve, C2: nanoocp.Adaptor3d.Adaptor3d_Curve, TolC1: float = 1e-10, TolC2: float = 1e-10) -> None: ...

    @overload
    def Initialize(self, C1: nanoocp.Adaptor3d.Adaptor3d_Curve, C2: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, V1: float, V2: float, TolC1: float = 1e-10, TolC2: float = 1e-10) -> None:
        """Initializes but does not perform algorithm."""

    @overload
    def SetCurve(self, theRank: int, C: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None: ...

    @overload
    def SetCurve(self, theRank: int, C: nanoocp.Adaptor3d.Adaptor3d_Curve, Uinf: float, Usup: float) -> None: ...

    def SetRange(self, theRank: int, Uinf: float, Usup: float) -> None: ...

    def SetTolerance(self, theRank: int, Tol: float) -> None: ...

    def Perform(self) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def IsParallel(self) -> bool:
        """Returns True if the two curves are parallel."""

    def SquareDistance(self, N: int = 1) -> float:
        """Returns the value of the Nth extremum square distance."""

    def Points(self, N: int, P1: Extrema_POnCurv, P2: Extrema_POnCurv) -> None:
        """
        Returns the points of the Nth extremum distance.
        P1 is on the first curve, P2 on the second one.
        """

    def TrimmedSquareDistances(self, P11: nanoocp.gp.gp_Pnt, P12: nanoocp.gp.gp_Pnt, P21: nanoocp.gp.gp_Pnt, P22: nanoocp.gp.gp_Pnt) -> tuple[float, float, float, float]:
        """
        if the curve is a trimmed curve,
        dist11 is a square distance between the point on C1
        of parameter FirstParameter and the point of
        parameter FirstParameter on C2.
        """

    def SetSingleSolutionFlag(self, theSingleSolutionFlag: bool) -> None:
        """
        Set flag for single extrema computation. Works on parametric solver only.
        """

    def GetSingleSolutionFlag(self) -> bool:
        """
        Get flag for single extrema computation. Works on parametric solver only.
        """

class Extrema_ExtCC2d:
    """
    It calculates all the distance between two curves.
    These distances can be maximum or minimum.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, TolC1: float = 1e-10, TolC2: float = 1e-10) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, U1: float, U2: float, V1: float, V2: float, TolC1: float = 1e-10, TolC2: float = 1e-10) -> None:
        """It calculates all the distances."""

    @overload
    def __init__(self, theOther: Extrema_ExtCC2d) -> None: ...

    def Initialize(self, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, V1: float, V2: float, TolC1: float = 1e-10, TolC2: float = 1e-10) -> None:
        """initializes the fields."""

    def Perform(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, U1: float, U2: float) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def IsParallel(self) -> bool:
        """Returns True if the two curves are parallel."""

    def SquareDistance(self, N: int = 1) -> float:
        """Returns the value of the Nth extremum square distance."""

    def Points(self, N: int, P1: Extrema_POnCurv2d, P2: Extrema_POnCurv2d) -> None:
        """
        Returns the points of the Nth extremum distance.
        P1 is on the first curve, P2 on the second one.
        """

    def TrimmedSquareDistances(self, P11: nanoocp.gp.gp_Pnt2d, P12: nanoocp.gp.gp_Pnt2d, P21: nanoocp.gp.gp_Pnt2d, P22: nanoocp.gp.gp_Pnt2d) -> tuple[float, float, float, float]:
        """
        if the curve is a trimmed curve,
        dist11 is a square distance between the point on C1
        of parameter FirstParameter and the point of
        parameter FirstParameter on C2.
        """

    def SetSingleSolutionFlag(self, theSingleSolutionFlag: bool) -> None:
        """
        Set flag for single extrema computation. Works on parametric solver only.
        """

    def GetSingleSolutionFlag(self) -> bool:
        """
        Get flag for single extrema computation. Works on parametric solver only.
        """

class Extrema_POnSurf:
    """Definition of a point on surface."""

    @overload
    def __init__(self) -> None:
        """Creation of an indefinite point on surface."""

    @overload
    def __init__(self, theU: float, theV: float, theP: nanoocp.gp.gp_Pnt) -> None:
        """
        Creation of a point on surface with parameter
        values on the surface and a Pnt from gp.
        """

    @overload
    def __init__(self, theOther: Extrema_POnSurf) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Pnt:
        """Returns the 3d point."""

    def SetParameters(self, theU: float, theV: float, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """
        Sets the params of current POnSurf instance.
        (e.g. to the point to be projected).
        """

    def Parameter(self) -> tuple[float, float]:
        """Returns the parameter values on the surface."""

class Extrema_ExtElCS:
    """
    It calculates all the distances between a curve and
    a surface.
    These distances can be maximum or minimum.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Lin, S: nanoocp.gp.gp_Pln) -> None:
        """
        Calculates the distances between a line and a
        plane. The line can be on the plane or on a parallel
        plane.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Lin, S: nanoocp.gp.gp_Cylinder) -> None:
        """
        Calculates the distances between a line and a
        cylinder.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Lin, S: nanoocp.gp.gp_Cone) -> None:
        """Calculates the distances between a line and a cone."""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Lin, S: nanoocp.gp.gp_Sphere) -> None:
        """
        Calculates the distances between a line and a
        sphere.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Lin, S: nanoocp.gp.gp_Torus) -> None:
        """
        Calculates the distances between a line and a
        torus.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ, S: nanoocp.gp.gp_Pln) -> None:
        """
        Calculates the distances between a circle and a
        plane.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ, S: nanoocp.gp.gp_Cylinder) -> None:
        """
        Calculates the distances between a circle and a
        cylinder.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ, S: nanoocp.gp.gp_Cone) -> None:
        """
        Calculates the distances between a circle and a
        cone.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ, S: nanoocp.gp.gp_Sphere) -> None:
        """
        Calculates the distances between a circle and a
        sphere.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ, S: nanoocp.gp.gp_Torus) -> None:
        """
        Calculates the distances between a circle and a
        torus.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Hypr, S: nanoocp.gp.gp_Pln) -> None:
        """
        Calculates the distances between a hyperbola and a
        plane.
        """

    @overload
    def __init__(self, theOther: Extrema_ExtElCS) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Lin, S: nanoocp.gp.gp_Pln) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Lin, S: nanoocp.gp.gp_Cylinder) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Lin, S: nanoocp.gp.gp_Cone) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Lin, S: nanoocp.gp.gp_Sphere) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Lin, S: nanoocp.gp.gp_Torus) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Circ, S: nanoocp.gp.gp_Pln) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Circ, S: nanoocp.gp.gp_Cylinder) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Circ, S: nanoocp.gp.gp_Cone) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Circ, S: nanoocp.gp.gp_Sphere) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Circ, S: nanoocp.gp.gp_Torus) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Hypr, S: nanoocp.gp.gp_Pln) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def IsParallel(self) -> bool:
        """Returns True if the curve is on a parallel surface."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int = 1) -> float:
        """Returns the value of the Nth extremum square distance."""

    def Points(self, N: int, P1: Extrema_POnCurv, P2: Extrema_POnSurf) -> None:
        """
        Returns the points of the Nth extremum distance.
        P1 is on the curve, P2 on the surface.
        """

class Extrema_ExtCS:
    """
    It calculates all the extremum distances
    between a curve and a surface.
    These distances can be minimum or maximum.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface, TolC: float, TolS: float) -> None:
        """It calculates all the distances between C and S."""

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface, UCinf: float, UCsup: float, Uinf: float, Usup: float, Vinf: float, Vsup: float, TolC: float, TolS: float) -> None:
        """
        It calculates all the distances between C and S.
        UCinf and UCmax are the start and end parameters
        of the curve.
        """

    @overload
    def Initialize(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface, TolC: float, TolS: float) -> None: ...

    @overload
    def Initialize(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface, Uinf: float, Usup: float, Vinf: float, Vsup: float, TolC: float, TolS: float) -> None:
        """Initializes the fields of the algorithm."""

    def Perform(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, Uinf: float, Usup: float) -> None:
        """
        Computes the distances.
        An exception is raised if the fields have not been
        initialized.
        """

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def IsParallel(self) -> bool:
        """Returns True if the curve is on a parallel surface."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the Nth resulting square distance."""

    def Points(self, N: int, P1: Extrema_POnCurv, P2: Extrema_POnSurf) -> None:
        """Returns the point of the Nth resulting distance."""

class Extrema_ExtElC:
    """
    It calculates all the distance between two elementary
    curves.
    These distances can be maximum or minimum.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Lin, C2: nanoocp.gp.gp_Elips) -> None:
        """
        Calculates the distance between a line and an
        ellipse.
        """

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Lin, C2: nanoocp.gp.gp_Hypr) -> None:
        """
        Calculates the distance between a line and a
        hyperbola.
        """

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Lin, C2: nanoocp.gp.gp_Parab) -> None:
        """
        Calculates the distance between a line and a
        parabola.
        """

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Circ, C2: nanoocp.gp.gp_Circ) -> None:
        """
        Calculates the distance between two circles.
        The circles can be parallel or identical.
        """

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Lin, C2: nanoocp.gp.gp_Lin, AngTol: float) -> None:
        """
        Calculates the distance between two lines.
        AngTol is used to test if the lines are parallel:
        Angle(C1,C2) < AngTol.
        """

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Lin, C2: nanoocp.gp.gp_Circ, Tol: float) -> None:
        """
        Calculates the distance between a line and a
        circle.
        """

    @overload
    def __init__(self, theOther: Extrema_ExtElC) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def IsParallel(self) -> bool:
        """Returns True if the two curves are parallel."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int = 1) -> float:
        """Returns the value of the Nth extremum square distance."""

    def Points(self, N: int, P1: Extrema_POnCurv, P2: Extrema_POnCurv) -> None:
        """
        Returns the points of the Nth extremum distance.
        P1 is on the first curve, P2 on the second one.
        """

class Extrema_ExtElC2d:
    """
    It calculates all the distance between two elementary
    curves.
    These distances can be maximum or minimum.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Lin2d, C2: nanoocp.gp.gp_Elips2d) -> None:
        """
        Calculates the distance between a line and an
        ellipse.
        """

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Lin2d, C2: nanoocp.gp.gp_Hypr2d) -> None:
        """
        Calculates the distance between a line and a
        hyperbola.
        """

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Lin2d, C2: nanoocp.gp.gp_Parab2d) -> None:
        """
        Calculates the distance between a line and a
        parabola.
        """

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Circ2d, C2: nanoocp.gp.gp_Circ2d) -> None:
        """
        Calculates the distance between two circles.
        The circles can be parallel or identical.
        """

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Circ2d, C2: nanoocp.gp.gp_Elips2d) -> None:
        """
        Calculates the distance between a circle and an
        ellipse.
        """

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Circ2d, C2: nanoocp.gp.gp_Hypr2d) -> None:
        """
        Calculates the distance between a circle and a
        hyperbola.
        """

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Circ2d, C2: nanoocp.gp.gp_Parab2d) -> None:
        """
        Calculates the distance between a circle and a
        parabola.
        """

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Lin2d, C2: nanoocp.gp.gp_Lin2d, AngTol: float) -> None:
        """
        Calculates the distance between two lines.
        AngTol is used to test if the lines are parallel:
        Angle(C1,C2) < AngTol.
        """

    @overload
    def __init__(self, C1: nanoocp.gp.gp_Lin2d, C2: nanoocp.gp.gp_Circ2d, Tol: float) -> None:
        """
        Calculates the distance between a line and a
        circle.
        """

    @overload
    def __init__(self, theOther: Extrema_ExtElC2d) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def IsParallel(self) -> bool:
        """Returns True if the two curves are parallel."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int = 1) -> float:
        """Returns the value of the Nth extremum square distance."""

    def Points(self, N: int, P1: Extrema_POnCurv2d, P2: Extrema_POnCurv2d) -> None:
        """
        Returns the points of the Nth extremum distance.
        P1 is on the first curve, P2 on the second one.
        """

class Extrema_ExtElSS:
    """
    It calculates all the distances between 2 elementary
    surfaces.
    These distances can be maximum or minimum.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S1: nanoocp.gp.gp_Pln, S2: nanoocp.gp.gp_Pln) -> None:
        """
        Calculates the distances between 2 planes.
        These planes can be parallel.
        """

    @overload
    def __init__(self, S1: nanoocp.gp.gp_Pln, S2: nanoocp.gp.gp_Sphere) -> None:
        """
        Calculates the distances between a plane
        and a sphere.
        """

    @overload
    def __init__(self, S1: nanoocp.gp.gp_Sphere, S2: nanoocp.gp.gp_Sphere) -> None:
        """
        Calculates the distances between 2 spheres.
        These spheres can be parallel.
        """

    @overload
    def __init__(self, S1: nanoocp.gp.gp_Sphere, S2: nanoocp.gp.gp_Cylinder) -> None:
        """
        Calculates the distances between a sphere
        and a cylinder.
        """

    @overload
    def __init__(self, S1: nanoocp.gp.gp_Sphere, S2: nanoocp.gp.gp_Cone) -> None:
        """
        Calculates the distances between a sphere
        and a cone.
        """

    @overload
    def __init__(self, S1: nanoocp.gp.gp_Sphere, S2: nanoocp.gp.gp_Torus) -> None:
        """
        Calculates the distances between a sphere
        and a torus.
        """

    @overload
    def __init__(self, theOther: Extrema_ExtElSS) -> None: ...

    @overload
    def Perform(self, S1: nanoocp.gp.gp_Pln, S2: nanoocp.gp.gp_Pln) -> None: ...

    @overload
    def Perform(self, S1: nanoocp.gp.gp_Pln, S2: nanoocp.gp.gp_Sphere) -> None: ...

    @overload
    def Perform(self, S1: nanoocp.gp.gp_Sphere, S2: nanoocp.gp.gp_Sphere) -> None: ...

    @overload
    def Perform(self, S1: nanoocp.gp.gp_Sphere, S2: nanoocp.gp.gp_Cylinder) -> None: ...

    @overload
    def Perform(self, S1: nanoocp.gp.gp_Sphere, S2: nanoocp.gp.gp_Cone) -> None: ...

    @overload
    def Perform(self, S1: nanoocp.gp.gp_Sphere, S2: nanoocp.gp.gp_Torus) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def IsParallel(self) -> bool:
        """Returns True if the two surfaces are parallel."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int = 1) -> float:
        """Returns the value of the Nth extremum square distance."""

    def Points(self, N: int, P1: Extrema_POnSurf, P2: Extrema_POnSurf) -> None:
        """
        Returns the points for the Nth resulting distance.
        P1 is on the first surface, P2 on the second one.
        """

class Extrema_ExtPElS:
    """
    It calculates all the extremum distances
    between a point and a surface.
    These distances can be minimum or maximum.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.gp.gp_Cylinder, Tol: float) -> None:
        """
        It calculates all the distances between a point
        and a cylinder from gp.
        Tol is used to test if the point is on the axis.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.gp.gp_Pln, Tol: float) -> None:
        """
        It calculates all the distances between a point
        and a plane from gp.
        Tol is used to test if the point is on the plane.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.gp.gp_Cone, Tol: float) -> None:
        """
        It calculates all the distances between a point
        and a cone from gp.
        Tol is used to test if the point is at the apex or
        on the axis.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.gp.gp_Torus, Tol: float) -> None:
        """
        It calculates all the distances between a point
        and a torus from gp.
        Tol is used to test if the point is on the axis.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.gp.gp_Sphere, Tol: float) -> None:
        """
        It calculates all the distances between a point
        and a sphere from gp.
        Tol is used to test if the point is at the center.
        """

    @overload
    def __init__(self, theOther: Extrema_ExtPElS) -> None: ...

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.gp.gp_Cylinder, Tol: float) -> None: ...

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.gp.gp_Pln, Tol: float) -> None: ...

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.gp.gp_Cone, Tol: float) -> None: ...

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.gp.gp_Torus, Tol: float) -> None: ...

    @overload
    def Perform(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.gp.gp_Sphere, Tol: float) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the Nth resulting square distance."""

    def Point(self, N: int) -> Extrema_POnSurf:
        """Returns the point of the Nth resulting distance."""

class Extrema_POnSurfParams(Extrema_POnSurf):
    """
    Data container for point on surface parameters. These parameters
    are required to compute an initial approximation for extrema
    computation.
    """

    @overload
    def __init__(self) -> None:
        """empty constructor"""

    @overload
    def __init__(self, theU: float, theV: float, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """
        Creation of a point on surface with parameter
        values on the surface and a Pnt from gp.
        """

    @overload
    def __init__(self, theOther: Extrema_POnSurfParams) -> None: ...

    def SetSqrDistance(self, theSqrDistance: float) -> None:
        """
        Sets the square distance from this point to another one
        (e.g. to the point to be projected).
        """

    def GetSqrDistance(self) -> float:
        """Query the square distance from this point to another one."""

    def SetElementType(self, theElementType: Extrema_ElementType) -> None:
        """Sets the element type on which this point is situated."""

    def GetElementType(self) -> Extrema_ElementType:
        """Query the element type on which this point is situated."""

    def SetIndices(self, theIndexU: int, theIndexV: int) -> None:
        """
        Sets the U and V indices of an element that contains
        this point.
        """

    def GetIndices(self) -> tuple[int, int]:
        """
        Query the U and V indices of an element that contains
        this point.
        """

class Extrema_FuncPSNorm(nanoocp.math.math_FunctionSetWithDerivatives):
    """
    Functional for search of extremum of the distance between point P and
    surface S, starting from approximate solution (u0, v0).

    The class inherits math_FunctionSetWithDerivatives and thus is intended
    for use in math_FunctionSetRoot algorithm .

    Denoting derivatives of the surface S(u,v) by u and v, respectively, as
    Su and Sv, the two functions to be nullified are:

    F1(u,v) = (S - P) * Su
    F2(u,v) = (S - P) * Sv

    The derivatives of the functional are:

    Duf1(u,v) = Su^2    + (S-P) * Suu;
    Dvf1(u,v) = Su * Sv + (S-P) * Suv
    Duf2(u,v) = Sv * Su + (S-P) * Suv = Dvf1
    Dvf2(u,v) = Sv^2    + (S-P) * Svv

    Here * denotes scalar product, and ^2 is square power.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None: ...

    @overload
    def __init__(self, theOther: Extrema_FuncPSNorm) -> None: ...

    def Initialize(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None:
        """sets the field mysurf of the function."""

    def SetPoint(self, P: nanoocp.gp.gp_Pnt) -> None:
        """sets the field mysurf of the function."""

    def NbVariables(self) -> int: ...

    def NbEquations(self) -> int: ...

    def Value(self, UV: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """Calculate Fi(U,V)."""

    def Derivatives(self, UV: nanoocp.math.math_Vector, DF: nanoocp.math.math_Matrix) -> bool:
        """Calculate Fi'(U,V)."""

    def Values(self, UV: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, DF: nanoocp.math.math_Matrix) -> bool:
        """Calculate Fi(U,V) and Fi'(U,V)."""

    def GetStateNumber(self) -> int:
        """Save the found extremum."""

    def NbExt(self) -> int:
        """Return the number of found extrema."""

    def SquareDistance(self, N: int) -> float:
        """Return the value of the Nth distance."""

    def Point(self, N: int) -> Extrema_POnSurf:
        """Returns the Nth extremum."""

class Extrema_GenExtPS:
    """
    It calculates all the extremum distances
    between a point and a surface.
    These distances can be minimum or maximum.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.Adaptor3d.Adaptor3d_Surface, NbU: int, NbV: int, TolU: float, TolV: float, F: Extrema_ExtFlag = Extrema_ExtFlag.Extrema_ExtFlag_MINMAX, A: Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.Adaptor3d.Adaptor3d_Surface, NbU: int, NbV: int, Umin: float, Usup: float, Vmin: float, Vsup: float, TolU: float, TolV: float, F: Extrema_ExtFlag = Extrema_ExtFlag.Extrema_ExtFlag_MINMAX, A: Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None:
        """
        It calculates all the distances.
        The function F(u,v)=distance(P,S(u,v)) has an
        extremum when gradient(F)=0. The algorithm searches
        all the zeros inside the definition ranges of the
        surface.
        NbU and NbV are used to locate the close points
        to find the zeros. They must be great enough
        such that if there is N extrema, there will
        be N extrema between P and the grid.
        TolU et TolV are used to determine the conditions
        to stop the iterations; at the iteration number n:
        (Un - Un-1) < TolU and (Vn - Vn-1) < TolV .
        """

    @overload
    def Initialize(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface, NbU: int, NbV: int, TolU: float, TolV: float) -> None: ...

    @overload
    def Initialize(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface, NbU: int, NbV: int, Umin: float, Usup: float, Vmin: float, Vsup: float, TolU: float, TolV: float) -> None: ...

    def Perform(self, P: nanoocp.gp.gp_Pnt) -> None:
        """
        the algorithm is done with the point P.
        An exception is raised if the fields have not
        been initialized.
        """

    def SetFlag(self, F: Extrema_ExtFlag) -> None: ...

    def SetAlgo(self, A: Extrema_ExtAlgo) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the Nth resulting square distance."""

    def Point(self, N: int) -> Extrema_POnSurf:
        """Returns the point of the Nth resulting distance."""

class Extrema_ExtPExtS(nanoocp.Standard.Standard_Transient):
    """
    It calculates all the extremum (minimum and
    maximum) distances between a point and a linear
    extrusion surface.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.GeomAdaptor.GeomAdaptor_SurfaceOfLinearExtrusion | None, TolU: float, TolV: float) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.GeomAdaptor.GeomAdaptor_SurfaceOfLinearExtrusion | None, Umin: float, Usup: float, Vmin: float, Vsup: float, TolU: float, TolV: float) -> None:
        """
        It calculates all the distances between a point
        from gp and a Surface.
        """

    def Initialize(self, S: nanoocp.GeomAdaptor.GeomAdaptor_SurfaceOfLinearExtrusion | None, Uinf: float, Usup: float, Vinf: float, Vsup: float, TolU: float, TolV: float) -> None:
        """Initializes the fields of the algorithm."""

    def Perform(self, P: nanoocp.gp.gp_Pnt) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the Nth resulting square distance."""

    def Point(self, N: int) -> Extrema_POnSurf:
        """Returns the point of the Nth resulting distance."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Extrema_ExtPRevS(nanoocp.Standard.Standard_Transient):
    """
    It calculates all the extremum (minimum and
    maximum) distances between a point and a surface
    of revolution.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.GeomAdaptor.GeomAdaptor_SurfaceOfRevolution | None, TolU: float, TolV: float) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.GeomAdaptor.GeomAdaptor_SurfaceOfRevolution | None, Umin: float, Usup: float, Vmin: float, Vsup: float, TolU: float, TolV: float) -> None:
        """
        It calculates all the distances between a point
        from gp and a SurfacePtr from Adaptor3d.
        """

    def Initialize(self, S: nanoocp.GeomAdaptor.GeomAdaptor_SurfaceOfRevolution | None, Umin: float, Usup: float, Vmin: float, Vsup: float, TolU: float, TolV: float) -> None: ...

    def Perform(self, P: nanoocp.gp.gp_Pnt) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the Nth resulting square distance."""

    def Point(self, N: int) -> Extrema_POnSurf:
        """Returns the point of the Nth resulting distance."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Extrema_ExtPS:
    """
    It calculates all the extremum distances
    between a point and a surface.
    These distances can be minimum or maximum.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.Adaptor3d.Adaptor3d_Surface, TolU: float, TolV: float, F: Extrema_ExtFlag = Extrema_ExtFlag.Extrema_ExtFlag_MINMAX, A: Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, S: nanoocp.Adaptor3d.Adaptor3d_Surface, Uinf: float, Usup: float, Vinf: float, Vsup: float, TolU: float, TolV: float, F: Extrema_ExtFlag = Extrema_ExtFlag.Extrema_ExtFlag_MINMAX, A: Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None:
        """
        It calculates all the distances.
        NbU and NbV are used to locate the close points
        to find the zeros. They must be great enough
        such that if there is N extrema, there will
        be N extrema between P and the grid.
        TolU et TolV are used to determine the conditions
        to stop the iterations; at the iteration number n:
        (Un - Un-1) < TolU and (Vn - Vn-1) < TolV .
        """

    def Initialize(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface, Uinf: float, Usup: float, Vinf: float, Vsup: float, TolU: float, TolV: float) -> None:
        """Initializes the fields of the algorithm."""

    def Perform(self, P: nanoocp.gp.gp_Pnt) -> None:
        """
        Computes the distances.
        An exception is raised if the fields have not been
        initialized.
        """

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the Nth resulting square distance."""

    def Point(self, N: int) -> Extrema_POnSurf:
        """Returns the point of the Nth resulting distance."""

    def TrimmedSquareDistances(self, PUfVf: nanoocp.gp.gp_Pnt, PUfVl: nanoocp.gp.gp_Pnt, PUlVf: nanoocp.gp.gp_Pnt, PUlVl: nanoocp.gp.gp_Pnt) -> tuple[float, float, float, float]:
        """
        if the surface is a trimmed surface,
        dUfVf is a square distance between <P> and the point
        of parameter FirstUParameter and FirstVParameter <PUfVf>.
        dUfVl is a square distance between <P> and the point
        of parameter FirstUParameter and LastVParameter <PUfVl>.
        dUlVf is a square distance between <P> and the point
        of parameter LastUParameter and FirstVParameter <PUlVf>.
        dUlVl is a square distance between <P> and the point
        of parameter LastUParameter and LastVParameter <PUlVl>.
        """

    def SetFlag(self, F: Extrema_ExtFlag) -> None: ...

    def SetAlgo(self, A: Extrema_ExtAlgo) -> None: ...

class Extrema_ExtSS:
    """
    It calculates all the extremum distances
    between two surfaces.
    These distances can be minimum or maximum.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface, S2: nanoocp.Adaptor3d.Adaptor3d_Surface, TolS1: float, TolS2: float) -> None: ...

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface, S2: nanoocp.Adaptor3d.Adaptor3d_Surface, Uinf1: float, Usup1: float, Vinf1: float, Vsup1: float, Uinf2: float, Usup2: float, Vinf2: float, Vsup2: float, TolS1: float, TolS2: float) -> None:
        """It calculates all the distances between S1 and S2."""

    @overload
    def __init__(self, theOther: Extrema_ExtSS) -> None: ...

    def Initialize(self, S2: nanoocp.Adaptor3d.Adaptor3d_Surface, Uinf2: float, Usup2: float, Vinf2: float, Vsup2: float, TolS1: float) -> None:
        """Initializes the fields of the algorithm."""

    def Perform(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface, Uinf1: float, Usup1: float, Vinf1: float, Vsup1: float, TolS1: float) -> None:
        """
        Computes the distances.
        An exception is raised if the fields have not been
        initialized.
        """

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def IsParallel(self) -> bool:
        """Returns True if the surfaces are parallel"""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the Nth resulting square distance."""

    def Points(self, N: int, P1: Extrema_POnSurf, P2: Extrema_POnSurf) -> None:
        """Returns the point of the Nth resulting distance."""

class Extrema_FuncExtCS(nanoocp.math.math_FunctionSetWithDerivatives):
    """
    Function to find extrema of the
    distance between a curve and a surface.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None: ...

    @overload
    def __init__(self, theOther: Extrema_FuncExtCS) -> None: ...

    def Initialize(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None:
        """sets the field mysurf of the function."""

    def NbVariables(self) -> int: ...

    def NbEquations(self) -> int: ...

    def Value(self, UV: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """Calculation of Fi(U,V)."""

    def Derivatives(self, UV: nanoocp.math.math_Vector, DF: nanoocp.math.math_Matrix) -> bool:
        """Calculation of Fi'(U,V)."""

    def Values(self, UV: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, DF: nanoocp.math.math_Matrix) -> bool:
        """Calculation of Fi(U,V) and Fi'(U,V)."""

    def GetStateNumber(self) -> int:
        """Save the found extremum."""

    def NbExt(self) -> int:
        """Return the number of found extrema."""

    def SquareDistance(self, N: int) -> float:
        """Return the value of the Nth distance."""

    def PointOnCurve(self, N: int) -> Extrema_POnCurv:
        """Returns the Nth extremum on C."""

    def PointOnSurface(self, N: int) -> Extrema_POnSurf:
        """Return the Nth extremum on S."""

    def SquareDistances(self) -> nanoocp.NCollection.NCollection_Sequence[float]:
        """Change Sequence of SquareDistance"""

    def PointsOnCurve(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Extrema.Extrema_POnCurv]:
        """Change Sequence of PointOnCurv"""

    def PointsOnSurf(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Extrema.Extrema_POnSurf]:
        """Change Sequence of PointOnSurf"""

class Extrema_FuncPSDist(nanoocp.math.math_MultipleVarFunctionWithGradient):
    """
    Functional for search of extremum of the square Euclidean distance between point P and
    surface S, starting from approximate solution (u0, v0).

    The class inherits math_MultipleVarFunctionWithGradient and thus is intended
    for use in math_BFGS algorithm.

    The criteria is:
    F = SquareDist(P, S(u, v)) - > min

    The first derivative are:
    F1(u,v) = (S(u,v) - P) * Su
    F2(u,v) = (S(u,v) - P) * Sv

    Su and Sv are first derivatives of the surface, * symbol means dot product.
    """

    def __init__(self, theS: nanoocp.Adaptor3d.Adaptor3d_Surface, theP: nanoocp.gp.gp_Pnt) -> None:
        """Constructor."""

    def NbVariables(self) -> int:
        """Number of variables."""

    def Value(self, X: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """Value."""

    def Gradient(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> bool:
        """Gradient."""

    def Values(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """Value and gradient."""

class Extrema_FuncExtSS(nanoocp.math.math_FunctionSetWithDerivatives):
    """
    Function to find extrema of the
    distance between two surfaces.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface, S2: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None: ...

    @overload
    def __init__(self, theOther: Extrema_FuncExtSS) -> None: ...

    def Initialize(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface, S2: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None:
        """sets the field mysurf of the function."""

    def NbVariables(self) -> int: ...

    def NbEquations(self) -> int: ...

    def Value(self, UV: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """Calculate Fi(U,V)."""

    def Derivatives(self, UV: nanoocp.math.math_Vector, DF: nanoocp.math.math_Matrix) -> bool:
        """Calculate Fi'(U,V)."""

    def Values(self, UV: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, DF: nanoocp.math.math_Matrix) -> bool:
        """Calculate Fi(U,V) and Fi'(U,V)."""

    def GetStateNumber(self) -> int:
        """Save the found extremum."""

    def NbExt(self) -> int:
        """Return the number of found extrema."""

    def SquareDistance(self, N: int) -> float:
        """Return the value of the Nth distance."""

    def PointOnS1(self, N: int) -> Extrema_POnSurf:
        """Return the Nth extremum on S1."""

    def PointOnS2(self, N: int) -> Extrema_POnSurf:
        """Renvoie le Nieme extremum sur S2."""

class Extrema_GenExtCS:
    """
    It calculates all the extremum distances
    between acurve and a surface.
    These distances can be minimum or maximum.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface, NbT: int, NbU: int, NbV: int, Tol1: float, Tol2: float) -> None:
        """
        It calculates all the distances.
        The function F(u,v)=distance(S1(u1,v1),S2(u2,v2)) has an
        extremum when gradient(F)=0. The algorithm searches
        all the zeros inside the definition ranges of the
        surfaces.
        NbU and NbV are used to locate the close points on the
        surface and NbT on the curve to find the zeros.
        """

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface, NbT: int, NbU: int, NbV: int, tmin: float, tsup: float, Umin: float, Usup: float, Vmin: float, Vsup: float, Tol1: float, Tol2: float) -> None:
        """
        It calculates all the distances.
        The function F(u,v)=distance(P,S(u,v)) has an
        extremum when gradient(F)=0. The algorithm searches
        all the zeros inside the definition ranges of the
        surface.
        NbT,NbU and NbV are used to locate the close points
        to find the zeros.
        """

    @overload
    def Initialize(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface, NbU: int, NbV: int, Tol2: float) -> None: ...

    @overload
    def Initialize(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface, NbU: int, NbV: int, Umin: float, Usup: float, Vmin: float, Vsup: float, Tol2: float) -> None: ...

    @overload
    def Perform(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, NbT: int, Tol1: float) -> None:
        """
        the algorithm is done with S
        An exception is raised if the fields have not
        been initialized.
        """

    @overload
    def Perform(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, NbT: int, tmin: float, tsup: float, Tol1: float) -> None:
        """
        the algorithm is done with C
        An exception is raised if the fields have not
        been initialized.
        """

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the Nth resulting square distance."""

    def PointOnCurve(self, N: int) -> Extrema_POnCurv:
        """Returns the point of the Nth resulting distance."""

    def PointOnSurface(self, N: int) -> Extrema_POnSurf:
        """Returns the point of the Nth resulting distance."""

class Extrema_GenExtSS:
    """
    It calculates all the extremum distances
    between two surfaces.
    These distances can be minimum or maximum.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface, S2: nanoocp.Adaptor3d.Adaptor3d_Surface, NbU: int, NbV: int, Tol1: float, Tol2: float) -> None:
        """
        It calculates all the distances.
        The function F(u,v)=distance(S1(u1,v1),S2(u2,v2)) has an
        extremum when gradient(F)=0. The algorithm searches
        all the zeros inside the definition ranges of the
        surfaces.
        NbU and NbV are used to locate the close points
        to find the zeros.
        """

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface, S2: nanoocp.Adaptor3d.Adaptor3d_Surface, NbU: int, NbV: int, U1min: float, U1sup: float, V1min: float, V1sup: float, U2min: float, U2sup: float, V2min: float, V2sup: float, Tol1: float, Tol2: float) -> None:
        """
        It calculates all the distances.
        The function F(u,v)=distance(P,S(u,v)) has an
        extremum when gradient(F)=0. The algorithm searches
        all the zeros inside the definition ranges of the
        surface.
        NbU and NbV are used to locate the close points
        to find the zeros.
        """

    @overload
    def Initialize(self, S2: nanoocp.Adaptor3d.Adaptor3d_Surface, NbU: int, NbV: int, Tol2: float) -> None: ...

    @overload
    def Initialize(self, S2: nanoocp.Adaptor3d.Adaptor3d_Surface, NbU: int, NbV: int, U2min: float, U2sup: float, V2min: float, V2sup: float, Tol2: float) -> None: ...

    @overload
    def Perform(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface, Tol1: float) -> None:
        """
        the algorithm is done with S1
        An exception is raised if the fields have not
        been initialized.
        """

    @overload
    def Perform(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface, U1min: float, U1sup: float, V1min: float, V1sup: float, Tol1: float) -> None:
        """
        the algorithm is done withS1
        An exception is raised if the fields have not
        been initialized.
        """

    def IsDone(self) -> bool:
        """Returns True if the distances are found."""

    def NbExt(self) -> int:
        """Returns the number of extremum distances."""

    def SquareDistance(self, N: int) -> float:
        """Returns the value of the Nth resulting square distance."""

    def PointOnS1(self, N: int) -> Extrema_POnSurf:
        """Returns the point of the Nth resulting distance."""

    def PointOnS2(self, N: int) -> Extrema_POnSurf:
        """Returns the point of the Nth resulting distance."""

class Extrema_GenLocateExtCS:
    """
    With two close points it calculates the distance
    between two surfaces.
    This distance can be a minimum or a maximum.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface, T: float, U: float, V: float, Tol1: float, Tol2: float) -> None:
        """
        Calculates the distance with two close points.
        The close points are defined by the parameter values
        T for C and (U,V) for S.
        The function F(t,u,v)=distance(C(t),S(u,v))
        has an extremun when gradient(F)=0. The algorithm searches
        a zero near the close points.
        """

    @overload
    def __init__(self, theOther: Extrema_GenLocateExtCS) -> None: ...

    def Perform(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface, T: float, U: float, V: float, Tol1: float, Tol2: float) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distance is found."""

    def SquareDistance(self) -> float:
        """Returns the value of the extremum square distance."""

    def PointOnCurve(self) -> Extrema_POnCurv:
        """Returns the point of the extremum distance on C."""

    def PointOnSurface(self) -> Extrema_POnSurf:
        """Returns the point of the extremum distance on S."""

class Extrema_GenLocateExtPS:
    """
    With a close point, it calculates the distance
    between a point and a surface.
    Criteria type is defined in "Perform" method.
    """

    def __init__(self, theS: nanoocp.Adaptor3d.Adaptor3d_Surface, theTolU: float = 1e-09, theTolV: float = 1e-09) -> None:
        """Constructor."""

    def Perform(self, theP: nanoocp.gp.gp_Pnt, theU0: float, theV0: float, isDistanceCriteria: bool = False) -> None:
        """
        Calculates the extrema between the point and the surface using a close point.
        The close point is defined by the parameter values theU0 and theV0.
        Type of the algorithm depends on the isDistanceCriteria flag.
        If flag value is false - normal projection criteria will be used.
        If flag value is true - distance criteria will be used.
        """

    def IsDone(self) -> bool:
        """Returns True if the distance is found."""

    def SquareDistance(self) -> float:
        """Returns the value of the extremum square distance."""

    def Point(self) -> Extrema_POnSurf:
        """Returns the point of the extremum distance."""

    @staticmethod
    def IsMinDist(theP: nanoocp.gp.gp_Pnt, theS: nanoocp.Adaptor3d.Adaptor3d_Surface, theU0: float, theV0: float) -> bool:
        """
        Returns True if UV point theU0, theV0 is point of local minimum of square distance between
        point theP and points theS(U, V), U, V are in small area around theU0, theV0
        """

class Extrema_GenLocateExtSS:
    """
    With two close points it calculates the distance
    between two surfaces.
    This distance can be a minimum or a maximum.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface, S2: nanoocp.Adaptor3d.Adaptor3d_Surface, U1: float, V1: float, U2: float, V2: float, Tol1: float, Tol2: float) -> None:
        """
        Calculates the distance with two close points.
        The close points are defined by the parameter values
        (U1,V1) for S1 and (U2,V2) for S2.
        The function F(u1,v1,u2,v2)=distance(S1(u1,v1),S2(u2,v2))
        has an extremun when gradient(F)=0. The algorithm searches
        a zero near the close points.
        """

    @overload
    def __init__(self, theOther: Extrema_GenLocateExtSS) -> None: ...

    def Perform(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface, S2: nanoocp.Adaptor3d.Adaptor3d_Surface, U1: float, V1: float, U2: float, V2: float, Tol1: float, Tol2: float) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distance is found."""

    def SquareDistance(self) -> float:
        """Returns the value of the extremum square distance."""

    def PointOnS1(self) -> Extrema_POnSurf:
        """Returns the point of the extremum distance on S1."""

    def PointOnS2(self) -> Extrema_POnSurf:
        """Returns the point of the extremum distance on S2."""

class Extrema_GlobOptFuncCS(nanoocp.math.math_MultipleVarFunctionWithHessian):
    """
    This class implements function which calculate square Eucluidean distance
    between point on curve and point on surface in case of continuity is C2.
    """

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None:
        """
        Curve and surface should exist during all the lifetime of Extrema_GlobOptFuncCS.
        """

    @overload
    def __init__(self, theOther: Extrema_GlobOptFuncCS) -> None: ...

    def NbVariables(self) -> int: ...

    def Value(self, theX: nanoocp.math.math_Vector) -> tuple[bool, float]: ...

    def Gradient(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> bool: ...

    @overload
    def Values(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> tuple[bool, float]: ...

    @overload
    def Values(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector, theH: nanoocp.math.math_Matrix) -> tuple[bool, float]: ...

class Extrema_GlobOptFuncConicS(nanoocp.math.math_MultipleVarFunction):
    """
    This class implements function which calculate square Eucluidean distance
    between point on surface and nearest point on Conic.
    """

    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None:
        """
        Curve and surface should exist during all the lifetime of Extrema_GlobOptFuncConicS.
        """

    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface, theUf: float, theUl: float, theVf: float, theVl: float) -> None: ...

    @overload
    def __init__(self, theOther: Extrema_GlobOptFuncConicS) -> None: ...

    def LoadConic(self, S: nanoocp.Adaptor3d.Adaptor3d_Curve, theTf: float, theTl: float) -> None: ...

    def NbVariables(self) -> int: ...

    def Value(self, theX: nanoocp.math.math_Vector) -> tuple[bool, float]: ...

    def ConicParameter(self, theUV: nanoocp.math.math_Vector) -> float:
        """Parameter of conic for point on surface defined by theUV"""

class Extrema_GlobOptFuncCQuadric(nanoocp.math.math_MultipleVarFunction):
    """
    This class implements function which calculate square Eucluidean distance
    between point on surface and nearest point on Conic.
    """

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None:
        """
        Curve and surface should exist during all the lifetime of Extrema_GlobOptFuncCQuadric.
        """

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, S: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Adaptor3d.Adaptor3d_Curve, theTf: float, theTl: float) -> None: ...

    @overload
    def __init__(self, theOther: Extrema_GlobOptFuncCQuadric) -> None: ...

    def LoadQuad(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface, theUf: float, theUl: float, theVf: float, theVl: float) -> None: ...

    def NbVariables(self) -> int: ...

    def Value(self, theX: nanoocp.math.math_Vector) -> tuple[bool, float]: ...

    def QuadricParameters(self, theCT: nanoocp.math.math_Vector, theUV: nanoocp.math.math_Vector) -> None:
        """Parameters of quadric for point on curve defined by theCT"""

class Extrema_LocateExtCC:
    """
    It calculates the distance between two curves with
    a close point; these distances can be maximum or
    minimum.
    """

    @overload
    def __init__(self, C1: nanoocp.Adaptor3d.Adaptor3d_Curve, C2: nanoocp.Adaptor3d.Adaptor3d_Curve, U0: float, V0: float) -> None:
        """
        Calculates the distance with a close point. The
        close point is defined by a parameter value on each
        curve.
        The function F(u,v)=distance(C1(u),C2(v)) has an
        extremun when gradient(f)=0. The algorithm searches
        the zero near the close point.
        """

    @overload
    def __init__(self, theOther: Extrema_LocateExtCC) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distance is found."""

    def SquareDistance(self) -> float:
        """Returns the value of the extremum square distance."""

    def Point(self, P1: Extrema_POnCurv, P2: Extrema_POnCurv) -> None:
        """
        Returns the points of the extremum distance.
        P1 is on the first curve, P2 on the second one.
        """

class Extrema_LocateExtCC2d:
    """
    It calculates the distance between two curves with
    a close point; these distances can be maximum or
    minimum.
    """

    @overload
    def __init__(self, C1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, C2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, U0: float, V0: float) -> None:
        """
        Calculates the distance with a close point. The
        close point is defined by a parameter value on each
        curve.
        The function F(u,v)=distance(C1(u),C2(v)) has an
        extremun when gradient(f)=0. The algorithm searches
        the zero near the close point.
        """

    @overload
    def __init__(self, theOther: Extrema_LocateExtCC2d) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distance is found."""

    def SquareDistance(self) -> float:
        """Returns the value of the extremum square distance."""

    def Point(self, P1: Extrema_POnCurv2d, P2: Extrema_POnCurv2d) -> None:
        """
        Returns the points of the extremum distance.
        P1 is on the first curve, P2 on the second one.
        """

class Extrema_LocEPCOfLocateExtPC:
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
    def __init__(self, theP: nanoocp.gp.gp_Pnt, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theU0: float, theTolU: float) -> None:
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
    def __init__(self, theP: nanoocp.gp.gp_Pnt, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theU0: float, theUmin: float, theUsup: float, theTolU: float) -> None:
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
    def __init__(self, theOther: Extrema_LocEPCOfLocateExtPC) -> None: ...

    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theUmin: float, theUsup: float, theTolU: float) -> None:
        """Sets the fields of the algorithm."""

    def Perform(self, theP: nanoocp.gp.gp_Pnt, theU0: float) -> None:
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

    def Point(self) -> Extrema_POnCurv:
        """Returns the point of the extremum distance."""

class Extrema_LocateExtPC:
    """
    Template class for locating extremum of distance between a point and a curve.
    Calculates the distance with a close point. The close point is defined by
    the parameter value U0. The function F(u)=distance(P,C(u)) has an extremum
    when g(u)=dF/du=0. The algorithm searches a zero near the close point.

    @tparam TheCurve    Curve type (e.g., Adaptor3d_Curve, Adaptor2d_Curve2d)
    @tparam TheCurveTool Tool for curve operations
    @tparam ThePoint    Point type (e.g., gp_Pnt, gp_Pnt2d)
    @tparam TheVector   Vector type (e.g., gp_Vec, gp_Vec2d)
    @tparam ThePOnC     Point on curve type
    @tparam TheELPC     Extended local projection curve type
    @tparam TheLocEPC   Local extremum point curve type
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theU0: float, theTolF: float) -> None:
        """
        Calculates the distance with a close point.
        The close point is defined by the parameter value U0.
        TolF is used to decide to stop the iterations.
        At the nth iteration, the criteria is: abs(Un - Un-1) < TolF.
        """

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theU0: float, theUmin: float, theUsup: float, theTolF: float) -> None:
        """
        Calculates the distance with a close point.
        The close point is defined by the parameter value U0.
        Zeros are searched between Umin and Usup.
        TolF is used to decide to stop the iterations.
        At the nth iteration, the criteria is: abs(Un - Un-1) < TolF.
        """

    @overload
    def __init__(self, theOther: Extrema_LocateExtPC) -> None: ...

    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theUmin: float, theUsup: float, theTolF: float) -> None:
        """Sets the fields of the algorithm."""

    def Perform(self, theP: nanoocp.gp.gp_Pnt, theU0: float) -> None:
        """Performs the algorithm with point P and initial parameter U0."""

    def IsDone(self) -> bool:
        """Returns True if the distance is found."""

    def SquareDistance(self) -> float:
        """Returns the value of the extremum square distance."""

    def IsMin(self) -> bool:
        """Returns True if the extremum distance is a minimum."""

    def Point(self) -> Extrema_POnCurv:
        """Returns the point of the extremum distance."""

class Extrema_LocEPCOfLocateExtPC2d:
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
    def __init__(self, theOther: Extrema_LocEPCOfLocateExtPC2d) -> None: ...

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

    def Point(self) -> Extrema_POnCurv2d:
        """Returns the point of the extremum distance."""

class Extrema_LocateExtPC2d:
    """
    Template class for locating extremum of distance between a point and a curve.
    Calculates the distance with a close point. The close point is defined by
    the parameter value U0. The function F(u)=distance(P,C(u)) has an extremum
    when g(u)=dF/du=0. The algorithm searches a zero near the close point.

    @tparam TheCurve    Curve type (e.g., Adaptor3d_Curve, Adaptor2d_Curve2d)
    @tparam TheCurveTool Tool for curve operations
    @tparam ThePoint    Point type (e.g., gp_Pnt, gp_Pnt2d)
    @tparam TheVector   Vector type (e.g., gp_Vec, gp_Vec2d)
    @tparam ThePOnC     Point on curve type
    @tparam TheELPC     Extended local projection curve type
    @tparam TheLocEPC   Local extremum point curve type
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt2d, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theU0: float, theTolF: float) -> None:
        """
        Calculates the distance with a close point.
        The close point is defined by the parameter value U0.
        TolF is used to decide to stop the iterations.
        At the nth iteration, the criteria is: abs(Un - Un-1) < TolF.
        """

    @overload
    def __init__(self, theP: nanoocp.gp.gp_Pnt2d, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theU0: float, theUmin: float, theUsup: float, theTolF: float) -> None:
        """
        Calculates the distance with a close point.
        The close point is defined by the parameter value U0.
        Zeros are searched between Umin and Usup.
        TolF is used to decide to stop the iterations.
        At the nth iteration, the criteria is: abs(Un - Un-1) < TolF.
        """

    @overload
    def __init__(self, theOther: Extrema_LocateExtPC2d) -> None: ...

    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theUmin: float, theUsup: float, theTolF: float) -> None:
        """Sets the fields of the algorithm."""

    def Perform(self, theP: nanoocp.gp.gp_Pnt2d, theU0: float) -> None:
        """Performs the algorithm with point P and initial parameter U0."""

    def IsDone(self) -> bool:
        """Returns True if the distance is found."""

    def SquareDistance(self) -> float:
        """Returns the value of the extremum square distance."""

    def IsMin(self) -> bool:
        """Returns True if the extremum distance is a minimum."""

    def Point(self) -> Extrema_POnCurv2d:
        """Returns the point of the extremum distance."""

class Extrema_LocECC:
    """
    Template class for locating local extremum of distance between two curves.
    Searches for a pair of parameter values (U,V) such that dist(C1(u),C2(v))
    passes through an extremum, and (U,V) is the solution closest to (U0,V0).

    @tparam TheCurve   Curve type (e.g., Adaptor3d_Curve, Adaptor2d_Curve2d)
    @tparam TheTool    Tool for curve operations
    @tparam ThePOnC    Point on curve type
    @tparam TheCCLocF  Function type for curve-curve local extremum
    """

    @overload
    def __init__(self, theC1: nanoocp.Adaptor3d.Adaptor3d_Curve, theC2: nanoocp.Adaptor3d.Adaptor3d_Curve, theU0: float, theV0: float, theTolU: float, theTolV: float) -> None:
        """
        Calculates the distance between two curves C1 and C2.
        Searches for a local extremum starting from initial parameters (U0, V0).
        @param theC1   First curve
        @param theC2   Second curve
        @param theU0   Initial parameter on first curve
        @param theV0   Initial parameter on second curve
        @param theTolU Tolerance on parameter of first curve
        @param theTolV Tolerance on parameter of second curve
        """

    @overload
    def __init__(self, theOther: Extrema_LocECC) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distance is found."""

    def SquareDistance(self) -> float:
        """Returns the value of the extremum square distance."""

    def Point(self, theP1: Extrema_POnCurv, theP2: Extrema_POnCurv) -> None:
        """
        Returns the points of the extremum distance.
        @param theP1 Point on first curve
        @param theP2 Point on second curve
        """

class Extrema_LocECC2d:
    """
    Template class for locating local extremum of distance between two curves.
    Searches for a pair of parameter values (U,V) such that dist(C1(u),C2(v))
    passes through an extremum, and (U,V) is the solution closest to (U0,V0).

    @tparam TheCurve   Curve type (e.g., Adaptor3d_Curve, Adaptor2d_Curve2d)
    @tparam TheTool    Tool for curve operations
    @tparam ThePOnC    Point on curve type
    @tparam TheCCLocF  Function type for curve-curve local extremum
    """

    @overload
    def __init__(self, theC1: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theC2: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theU0: float, theV0: float, theTolU: float, theTolV: float) -> None:
        """
        Calculates the distance between two curves C1 and C2.
        Searches for a local extremum starting from initial parameters (U0, V0).
        @param theC1   First curve
        @param theC2   Second curve
        @param theU0   Initial parameter on first curve
        @param theV0   Initial parameter on second curve
        @param theTolU Tolerance on parameter of first curve
        @param theTolV Tolerance on parameter of second curve
        """

    @overload
    def __init__(self, theOther: Extrema_LocECC2d) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if the distance is found."""

    def SquareDistance(self) -> float:
        """Returns the value of the extremum square distance."""

    def Point(self, theP1: Extrema_POnCurv2d, theP2: Extrema_POnCurv2d) -> None:
        """
        Returns the points of the extremum distance.
        @param theP1 Point on first curve
        @param theP2 Point on second curve
        """

Extrema_PCFOfEPCOfELPCOfLocateExtPC: TypeAlias = Extrema_PCFOfEPCOfExtPC

Extrema_EPCOfELPCOfLocateExtPC: TypeAlias = Extrema_EPCOfExtPC

Extrema_ELPCOfLocateExtPC: TypeAlias = Extrema_ExtPC

Extrema_PCFOfEPCOfELPCOfLocateExtPC2d: TypeAlias = Extrema_PCFOfEPCOfExtPC2d

Extrema_EPCOfELPCOfLocateExtPC2d: TypeAlias = Extrema_EPCOfExtPC2d

Extrema_ELPCOfLocateExtPC2d: TypeAlias = Extrema_ExtPC2d

Extrema_PCLocFOfLocEPCOfLocateExtPC: TypeAlias = Extrema_PCFOfEPCOfExtPC

Extrema_PCLocFOfLocEPCOfLocateExtPC2d: TypeAlias = Extrema_PCFOfEPCOfExtPC2d

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.Extrema
Extrema_SequenceOfPOnCurv = nanoocp.NCollection.NCollection_Sequence[nanoocp.Extrema.Extrema_POnCurv]
Extrema_SequenceOfPOnCurv2d = nanoocp.NCollection.NCollection_Sequence[nanoocp.Extrema.Extrema_POnCurv2d]
Extrema_SequenceOfPOnSurf = nanoocp.NCollection.NCollection_Sequence[nanoocp.Extrema.Extrema_POnSurf]
