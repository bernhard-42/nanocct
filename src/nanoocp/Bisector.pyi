"""OCCT package Bisector (toolkit TKTopAlgo)"""

from typing import overload

import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.IntRes2d
import nanoocp.Standard
import nanoocp.gp
import nanoocp.math


class Bisector:
    """
    This package provides the bisecting line between two
    geometric elements.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Bisector) -> None: ...

    @staticmethod
    def IsConvex(Cu: nanoocp.Geom2d.Geom2d_Curve | None, Sign: float) -> bool: ...

class Bisector_Bisec:
    """
    Bisec provides the bisecting line between two elements
    This line is trimmed by a point <P> and it's contained in the domain
    defined by the two vectors <V1>, <V2> and <Sense>.

    Definition of the domain:
    if <Sense> is true the bisecting line is contained in the sector
    defined by <-V1> and <-V2> in the sense indirect.
    if <Sense> is false the bisecting line is contained in the sector
    defined by <-V1> and <-V2> in the sense direct.

    <Tolerance> is used to define degenerate bisector.
    if the bisector is an hyperbola and one of this radius is smaller
    than <Tolerance>, the bisector is replaced by a line or semi_line
    corresponding to one of hyperbola's axes.
    if the bisector is a parabola on the focal length is smaller than
    <Tolerance>, the bisector is replaced by a semi_line corresponding
    to the axe of symmetry of the parabola.
    if the bisector is an ellipse and the minor radius is smaller than
    <Tolerance>, the bisector is replaced by a segment corresponding
    to the great axe of the ellipse.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Bisector_Bisec) -> None: ...

    @overload
    def Perform(self, Cu1: nanoocp.Geom2d.Geom2d_Curve | None, Cu2: nanoocp.Geom2d.Geom2d_Curve | None, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, Sense: float, ajointype: nanoocp.GeomAbs.GeomAbs_JoinType, Tolerance: float, oncurve: bool = True) -> None:
        """
        Performs the bisecting line between the curves
        <Cu1> and <Cu2>.
        <oncurve> is True if the point <P> is common to <Cu1>
        and <Cu2>.
        """

    @overload
    def Perform(self, Cu: nanoocp.Geom2d.Geom2d_Curve | None, Pnt: nanoocp.Geom2d.Geom2d_Point | None, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, Sense: float, Tolerance: float, oncurve: bool = True) -> None:
        """
        Performs the bisecting line between the curve
        <Cu1> and the point <Pnt>.
        <oncurve> is True if the point <P> is the point <Pnt>.
        """

    @overload
    def Perform(self, Pnt: nanoocp.Geom2d.Geom2d_Point | None, Cu: nanoocp.Geom2d.Geom2d_Curve | None, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, Sense: float, Tolerance: float, oncurve: bool = True) -> None:
        """
        Performs the bisecting line between the curve
        <Cu> and the point <Pnt>.
        <oncurve> is True if the point <P> is the point <Pnt>.
        """

    @overload
    def Perform(self, Pnt1: nanoocp.Geom2d.Geom2d_Point | None, Pnt2: nanoocp.Geom2d.Geom2d_Point | None, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, Sense: float, Tolerance: float = 0.0, oncurve: bool = True) -> None:
        """
        Performs the bisecting line between the two points
        <Pnt1> and <Pnt2>.
        """

    def Value(self) -> nanoocp.Geom2d.Geom2d_TrimmedCurve:
        """Returns the Curve of <me>."""

    def ChangeValue(self) -> nanoocp.Geom2d.Geom2d_TrimmedCurve:
        """Returns the Curve of <me>."""

class Bisector_Curve(nanoocp.Geom2d.Geom2d_Curve):
    def Parameter(self, P: nanoocp.gp.gp_Pnt2d) -> float: ...

    def IsExtendAtStart(self) -> bool: ...

    def IsExtendAtEnd(self) -> bool: ...

    def NbIntervals(self) -> int:
        """
        If necessary, breaks the curve in intervals of
        continuity <C1>. And returns the number of
        intervals.
        """

    def IntervalFirst(self, Index: int) -> float:
        """
        Returns the first parameter of the current
        interval.
        """

    def IntervalLast(self, Index: int) -> float:
        """
        Returns the last parameter of the current
        interval.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Bisector_BisecAna(Bisector_Curve):
    """
    This class provides the bisecting line between two
    geometric elements.The elements are Circles,Lines or
    Points.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Bisector_BisecAna) -> None: ...

    @overload
    def Perform(self, Cu1: nanoocp.Geom2d.Geom2d_Curve | None, Cu2: nanoocp.Geom2d.Geom2d_Curve | None, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, Sense: float, jointype: nanoocp.GeomAbs.GeomAbs_JoinType, Tolerance: float, oncurve: bool = True) -> None:
        """
        Performs the bisecting line between the curves
        <Cu1> and <Cu2>.
        <oncurve> is True if the point <P> is common to <Cu1>
        and <Cu2>.
        """

    @overload
    def Perform(self, Cu: nanoocp.Geom2d.Geom2d_Curve | None, Pnt: nanoocp.Geom2d.Geom2d_Point | None, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, Sense: float, Tolerance: float, oncurve: bool = True) -> None:
        """
        Performs the bisecting line between the curve
        <Cu1> and the point <Pnt>.
        <oncurve> is True if the point <P> is the point <Pnt>.
        """

    @overload
    def Perform(self, Pnt: nanoocp.Geom2d.Geom2d_Point | None, Cu: nanoocp.Geom2d.Geom2d_Curve | None, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, Sense: float, Tolerance: float, oncurve: bool = True) -> None:
        """
        Performs the bisecting line between the curve
        <Cu> and the point <Pnt>.
        <oncurve> is True if the point <P> is the point <Pnt>.
        """

    @overload
    def Perform(self, Pnt1: nanoocp.Geom2d.Geom2d_Point | None, Pnt2: nanoocp.Geom2d.Geom2d_Point | None, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, Sense: float, Tolerance: float = 0.0, oncurve: bool = True) -> None:
        """
        Performs the bisecting line between the two points
        <Pnt1> and <Pnt2>.
        """

    def Init(self, bisector: nanoocp.Geom2d.Geom2d_TrimmedCurve | None) -> None: ...

    def IsExtendAtStart(self) -> bool: ...

    def IsExtendAtEnd(self) -> bool: ...

    @overload
    def SetTrim(self, Cu: nanoocp.Geom2d.Geom2d_Curve | None) -> None:
        """
        Trim <me> by a domain defined by the curve <Cu>.
        This domain is the set of the points which are
        nearest from <Cu> than the extremitis of <Cu>.
        """

    @overload
    def SetTrim(self, uf: float, ul: float) -> None:
        """Trim <me> by a domain defined by uf and ul"""

    def Reverse(self) -> None: ...

    def ReversedParameter(self, U: float) -> float: ...

    def IsCN(self, N: int) -> bool:
        """
        Returns the order of continuity of the curve.
        Raised if N < 0.
        """

    def Copy(self) -> nanoocp.Geom2d.Geom2d_Geometry: ...

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None: ...

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def IsClosed(self) -> bool: ...

    def IsPeriodic(self) -> bool: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d: ...

    def EvalD1(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD1: ...

    def EvalD2(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD2: ...

    def EvalD3(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD3: ...

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d: ...

    def Geom2dCurve(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def Parameter(self, P: nanoocp.gp.gp_Pnt2d) -> float: ...

    def ParameterOfStartPoint(self) -> float: ...

    def ParameterOfEndPoint(self) -> float: ...

    def NbIntervals(self) -> int:
        """
        If necessary, breaks the curve in intervals of
        continuity <C1>. And returns the number of
        intervals.
        """

    def IntervalFirst(self, Index: int) -> float:
        """
        Returns the first parameter of the current
        interval.
        """

    def IntervalLast(self, Index: int) -> float:
        """
        Returns the last parameter of the current
        interval.
        """

    def Dump(self, Deep: int = 0, Offset: int = 0) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Bisector_PointOnBis:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Param1: float, Param2: float, ParamBis: float, Distance: float, Point: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, theOther: Bisector_PointOnBis) -> None: ...

    @overload
    def ParamOnC1(self, Param: float) -> None: ...

    @overload
    def ParamOnC1(self) -> float: ...

    @overload
    def ParamOnC2(self, Param: float) -> None: ...

    @overload
    def ParamOnC2(self) -> float: ...

    @overload
    def ParamOnBis(self, Param: float) -> None: ...

    @overload
    def ParamOnBis(self) -> float: ...

    @overload
    def Distance(self, Distance: float) -> None: ...

    @overload
    def Distance(self) -> float: ...

    @overload
    def IsInfinite(self, Infinite: bool) -> None: ...

    @overload
    def IsInfinite(self) -> bool: ...

    @overload
    def Point(self, P: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def Point(self) -> nanoocp.gp.gp_Pnt2d: ...

    def Dump(self) -> None: ...

class Bisector_PolyBis:
    """Polygon of PointOnBis"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Bisector_PolyBis) -> None: ...

    def Append(self, Point: Bisector_PointOnBis) -> None: ...

    def Length(self) -> int: ...

    def IsEmpty(self) -> bool: ...

    def Value(self, Index: int) -> Bisector_PointOnBis: ...

    def First(self) -> Bisector_PointOnBis: ...

    def Last(self) -> Bisector_PointOnBis: ...

    def Interval(self, U: float) -> int: ...

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None: ...

class Bisector_BisecCC(Bisector_Curve):
    """
    Construct the bisector between two curves.
    The curves can intersect only in their extremities.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Cu1: nanoocp.Geom2d.Geom2d_Curve | None, Cu2: nanoocp.Geom2d.Geom2d_Curve | None, Side1: float, Side2: float, Origin: nanoocp.gp.gp_Pnt2d, DistMax: float = 500.0) -> None:
        """
        Constructs the bisector between the curves <Cu1>
        and <Cu2>.

        <Side1> (resp <Side2>) = 1 if the
        bisector curve is on the left of <Cu1> (resp <Cu2>)
        else <Side1> (resp <Side2>) = -1.

        the Bisector is trimmed by the Point <Origin>.
        <DistMax> is used to trim the bisector.The distance
        between the points of the bisector and <Cu> is smaller
        than <DistMax>.
        """

    @overload
    def __init__(self, theOther: Bisector_BisecCC) -> None: ...

    def Perform(self, Cu1: nanoocp.Geom2d.Geom2d_Curve | None, Cu2: nanoocp.Geom2d.Geom2d_Curve | None, Side1: float, Side2: float, Origin: nanoocp.gp.gp_Pnt2d, DistMax: float = 500.0) -> None:
        """
        Computes the bisector between the curves <Cu1>
        and <Cu2>.

        <Side1> (resp <Side2>) = 1 if the
        bisector curve is on the left of <Cu1> (resp <Cu2>)
        else <Side1> (resp <Side2>) = -1.

        the Bisector is trimmed by the Point <Origin>.

        <DistMax> is used to trim the bisector.The distance
        between the points of the bisector and <Cu> is smaller
        than <DistMax>.
        """

    def IsExtendAtStart(self) -> bool: ...

    def IsExtendAtEnd(self) -> bool: ...

    def Reverse(self) -> None: ...

    def ReversedParameter(self, U: float) -> float: ...

    def IsCN(self, N: int) -> bool:
        """
        Returns the order of continuity of the curve.
        Raised if N < 0.
        """

    def ChangeGuide(self) -> Bisector_BisecCC:
        """
        The parameter on <me> is linked to the parameter
        on the first curve. This method creates the same bisector
        where the curves are inversed.
        """

    def Copy(self) -> nanoocp.Geom2d.Geom2d_Geometry: ...

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """
        Transformation of a geometric object. This transformation
        can be a translation, a rotation, a symmetry, a scaling
        or a complex transformation obtained by combination of
        the previous elementaries transformations.
        """

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self) -> int:
        """
        If necessary, breaks the curve in intervals of
        continuity <C1>. And returns the number of
        intervals.
        """

    def IntervalFirst(self, Index: int) -> float:
        """
        Returns the first parameter of the current
        interval.
        """

    def IntervalLast(self, Index: int) -> float:
        """
        Returns the last parameter of the current
        interval.
        """

    def IntervalContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def IsClosed(self) -> bool: ...

    def IsPeriodic(self) -> bool: ...

    def ValueAndDist(self, U: float) -> tuple[nanoocp.gp.gp_Pnt2d, float, float, float]:
        """
        Returns the point of parameter U.
        Computes the distance between the current point and
        the two curves I separate.
        Computes the parameters on each curve corresponding
        of the projection of the current point.
        """

    def ValueByInt(self, U: float) -> tuple[nanoocp.gp.gp_Pnt2d, float, float, float]:
        """
        Returns the point of parameter U.
        Computes the distance between the current point and
        the two curves I separate.
        Computes the parameters on each curve corresponding
        of the projection of the current point.
        """

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d: ...

    def EvalD1(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD1: ...

    def EvalD2(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD2: ...

    def EvalD3(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD3: ...

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d: ...

    def IsEmpty(self) -> bool: ...

    def LinkBisCurve(self, U: float) -> float:
        """
        Returns the parameter on the curve1 of the projection
        of the point of parameter U on <me>.
        """

    def LinkCurveBis(self, U: float) -> float:
        """Returns the reciproque of LinkBisCurve."""

    def Parameter(self, P: nanoocp.gp.gp_Pnt2d) -> float: ...

    def Curve(self, IndCurve: int) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def Polygon(self) -> Bisector_PolyBis: ...

    def Dump(self, Deep: int = 0, Offset: int = 0) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Bisector_BisecPC(Bisector_Curve):
    """
    Provides the bisector between a point and a curve.
    the curvature on the curve has to be monoton.
    the point can't be on the curve except at the extremities.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Cu: nanoocp.Geom2d.Geom2d_Curve | None, P: nanoocp.gp.gp_Pnt2d, Side: float, DistMax: float = 500.0) -> None:
        """
        Constructs the bisector between the point <P> and
        the curve <Cu>.
        <Side> = 1. if the bisector curve is on the Left of <Cu>
        else <Side> = -1.
        <DistMax> is used to trim the bisector.The distance
        between the points of the bisector and <Cu> is smaller
        than <DistMax>.
        """

    @overload
    def __init__(self, Cu: nanoocp.Geom2d.Geom2d_Curve | None, P: nanoocp.gp.gp_Pnt2d, Side: float, UMin: float, UMax: float) -> None:
        """
        Constructs the bisector between the point <P> and
        the curve <Cu> Trimmed by <UMin> and <UMax>
        <Side> = 1. if the bisector curve is on the Left of <Cu>
        else <Side> = -1.
        Warning: the bisector is supposed all over defined between
        <UMin> and <UMax>.
        """

    @overload
    def __init__(self, theOther: Bisector_BisecPC) -> None: ...

    def Perform(self, Cu: nanoocp.Geom2d.Geom2d_Curve | None, P: nanoocp.gp.gp_Pnt2d, Side: float, DistMax: float = 500.0) -> None:
        """
        Construct the bisector between the point <P> and
        the curve <Cu>.
        <Side> = 1. if the bisector curve is on the Left of <Cu>
        else <Side> = -1.
        <DistMax> is used to trim the bisector.The distance
        between the points of the bisector and <Cu> is smaller
        than <DistMax>.
        """

    def IsExtendAtStart(self) -> bool:
        """Returns True if the bisector is extended at start."""

    def IsExtendAtEnd(self) -> bool:
        """Returns True if the bisector is extended at end."""

    def Reverse(self) -> None:
        """
        Changes the direction of parametrization of <me>.
        The orientation of the curve is modified. If the curve
        is bounded the StartPoint of the initial curve becomes the
        EndPoint of the reversed curve and the EndPoint of the initial
        curve becomes the StartPoint of the reversed curve.
        """

    def ReversedParameter(self, U: float) -> float:
        """
        Returns the parameter on the reversed curve for
        the point of parameter U on <me>.
        """

    def Copy(self) -> nanoocp.Geom2d.Geom2d_Geometry: ...

    def Transform(self, T: nanoocp.gp.gp_Trsf2d) -> None:
        """
        Transformation of a geometric object. This transformation
        can be a translation, a rotation, a symmetry, a scaling
        or a complex transformation obtained by combination of
        the previous elementaries transformations.
        """

    def IsCN(self, N: int) -> bool:
        """
        Returns the order of continuity of the curve.
        Raised if N < 0.
        """

    def FirstParameter(self) -> float:
        """Value of the first parameter."""

    def LastParameter(self) -> float:
        """Value of the last parameter."""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self) -> int:
        """
        If necessary, breaks the curve in intervals of
        continuity <C1>. And returns the number of
        intervals.
        """

    def IntervalFirst(self, Index: int) -> float:
        """
        Returns the first parameter of the current
        interval.
        """

    def IntervalLast(self, Index: int) -> float:
        """
        Returns the last parameter of the current
        interval.
        """

    def IntervalContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def IsClosed(self) -> bool: ...

    def IsPeriodic(self) -> bool: ...

    def Distance(self, U: float) -> float:
        """
        Returns the distance between the point of
        parameter U on <me> and my point or my curve.
        """

    def EvalD0(self, U: float) -> nanoocp.gp.gp_Pnt2d: ...

    def EvalD1(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD1: ...

    def EvalD2(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD2: ...

    def EvalD3(self, U: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD3: ...

    def EvalDN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d: ...

    def Dump(self, Deep: int = 0, Offset: int = 0) -> None: ...

    def LinkBisCurve(self, U: float) -> float:
        """
        Returns the parameter on the curve1 of the projection
        of the point of parameter U on <me>.
        """

    def LinkCurveBis(self, U: float) -> float:
        """Returns the reciproque of LinkBisCurve."""

    def Parameter(self, P: nanoocp.gp.gp_Pnt2d) -> float:
        """Returns the parameter on <me> corresponding to <P>."""

    def IsEmpty(self) -> bool:
        """Returns <True> if the bisector is empty."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Bisector_FunctionH(nanoocp.math.math_FunctionWithDerivative):
    """
    H(v) = (T1.P2(v) - P1) * ||T(v)|| -
    2         2
    (T(v).P2(v) - P1) * ||T1||
    """

    @overload
    def __init__(self, C2: nanoocp.Geom2d.Geom2d_Curve | None, P1: nanoocp.gp.gp_Pnt2d, T1: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    def __init__(self, theOther: Bisector_FunctionH) -> None: ...

    def Value(self, X: float) -> tuple[bool, float]:
        """Computes the values of the Functions for the variable <X>."""

    def Derivative(self, X: float) -> tuple[bool, float]: ...

    def Values(self, X: float) -> tuple[bool, float, float]:
        """
        Returns the values of the functions and the derivatives
        for the variable <X>.
        """

class Bisector_FunctionInter(nanoocp.math.math_FunctionWithDerivative):
    """
    2                      2
    F(u) = (PC(u) - PBis1(u)) + (PC(u) - PBis2(u))
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom2d.Geom2d_Curve | None, Bis1: Bisector_Curve | None, Bis2: Bisector_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: Bisector_FunctionInter) -> None: ...

    def Perform(self, C: nanoocp.Geom2d.Geom2d_Curve | None, Bis1: Bisector_Curve | None, Bis2: Bisector_Curve | None) -> None: ...

    def Value(self, X: float) -> tuple[bool, float]:
        """Computes the values of the Functions for the variable <X>."""

    def Derivative(self, X: float) -> tuple[bool, float]: ...

    def Values(self, X: float) -> tuple[bool, float, float]:
        """
        Returns the values of the functions and the derivatives
        for the variable <X>.
        """

class Bisector_Inter(nanoocp.IntRes2d.IntRes2d_Intersection):
    """Intersection between two <Bisec> from Bisector."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C1: Bisector_Bisec, D1: nanoocp.IntRes2d.IntRes2d_Domain, C2: Bisector_Bisec, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float, ComunElement: bool) -> None:
        """
        Intersection between 2 curves.
        C1 separates the element A and B.
        C2 separates the elements C et D.
        If B an C have the same geometry. <ComunElement>
        Has to be True.
        It Permits an optimization of the computation.
        """

    @overload
    def __init__(self, theOther: Bisector_Inter) -> None: ...

    def Perform(self, C1: Bisector_Bisec, D1: nanoocp.IntRes2d.IntRes2d_Domain, C2: Bisector_Bisec, D2: nanoocp.IntRes2d.IntRes2d_Domain, TolConf: float, Tol: float, ComunElement: bool) -> None:
        """
        Intersection between 2 curves.
        C1 separates the element A and B.
        C2 separates the elements C et D.
        If B an C have the same geometry. <ComunElement>
        Has to be True.
        It Permits an optimization of the computation.
        """
