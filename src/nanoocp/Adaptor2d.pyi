"""OCCT package Adaptor2d (toolkit TKG2d)"""

from typing import overload

import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp


class Adaptor2d_Curve2d(nanoocp.Standard.Standard_Transient):
    """
    Root class for 2D curves on which geometric
    algorithms work.
    An adapted curve is an interface between the
    services provided by a curve, and those required of
    the curve by algorithms, which use it.
    A derived concrete class is provided:
    Geom2dAdaptor_Curve for a curve from the Geom2d package.

    Polynomial coefficients of BSpline curves used for their evaluation are
    cached for better performance. Therefore these evaluations are not
    thread-safe and parallel evaluations need to be prevented.
    """

    def __init__(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> Adaptor2d_Curve2d:
        """Shallow copy of adaptor"""

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        If necessary, breaks the curve in intervals of
        continuity <S>. And returns the number of
        intervals.
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def Trim(self, First: float, Last: float, Tol: float) -> Adaptor2d_Curve2d:
        """
        Returns a curve equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def IsClosed(self) -> bool: ...

    def IsPeriodic(self) -> bool: ...

    def Period(self) -> float: ...

    def Value(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """Computes the point of parameter U on the curve."""

    def D0(self, U: float, P: nanoocp.gp.gp_Pnt2d) -> None:
        """Computes the point of parameter U on the curve."""

    def D1(self, U: float, P: nanoocp.gp.gp_Pnt2d, V: nanoocp.gp.gp_Vec2d) -> None:
        """
        Computes the point of parameter U on the curve with its
        first derivative.
        Raised if the continuity of the current interval
        is not C1.
        """

    def D2(self, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first and second
        derivatives V1 and V2.
        Raised if the continuity of the current interval
        is not C2.
        """

    def D3(self, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first, the second
        and the third derivative.
        Raised if the continuity of the current interval
        is not C3.
        """

    def DN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        The returned vector gives the value of the derivative for the
        order of derivation N.
        Raised if the continuity of the current interval
        is not CN.
        Raised if N < 1.
        """

    def Resolution(self, R3d: float) -> float:
        """
        Returns the parametric resolution corresponding
        to the real space resolution <R3d>.
        """

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """
        Returns the type of the curve in the current
        interval: Line, Circle, Ellipse, Hyperbola,
        Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """

    def Line(self) -> nanoocp.gp.gp_Lin2d: ...

    def Circle(self) -> nanoocp.gp.gp_Circ2d: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips2d: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr2d: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab2d: ...

    def Degree(self) -> int: ...

    def IsRational(self) -> bool: ...

    def NbPoles(self) -> int: ...

    def NbKnots(self) -> int: ...

    def NbSamples(self) -> int: ...

    def Bezier(self) -> nanoocp.Geom2d.Geom2d_BezierCurve: ...

    def BSpline(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    def EvalD0(self, theU: float) -> nanoocp.gp.gp_Pnt2d:
        """
        Computes the point of parameter U on the curve.
        Raises an exception on failure.
        """

    def EvalD1(self, theU: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD1:
        """
        Computes the point and first derivative at parameter U.
        Raises an exception on failure.
        """

    def EvalD2(self, theU: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD2:
        """
        Computes the point and first two derivatives at parameter U.
        Raises an exception on failure.
        """

    def EvalD3(self, theU: float) -> nanoocp.Geom2d.Geom2d_Curve.ResD3:
        """
        Computes the point and first three derivatives at parameter U.
        Raises an exception on failure.
        """

    def EvalDN(self, theU: float, theN: int) -> nanoocp.gp.gp_Vec2d:
        """
        Computes the Nth derivative at parameter U.
        Raises an exception on failure.
        """

class Adaptor2d_Line2d(Adaptor2d_Curve2d):
    """Use by the TopolTool to trim a surface."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt2d, D: nanoocp.gp.gp_Dir2d, UFirst: float, ULast: float) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> Adaptor2d_Curve2d:
        """Shallow copy of adaptor"""

    @overload
    def Load(self, L: nanoocp.gp.gp_Lin2d) -> None: ...

    @overload
    def Load(self, L: nanoocp.gp.gp_Lin2d, UFirst: float, ULast: float) -> None: ...

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        If necessary, breaks the curve in intervals of
        continuity <S>. And returns the number of
        intervals.
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def Trim(self, First: float, Last: float, Tol: float) -> Adaptor2d_Curve2d:
        """
        Returns a curve equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def IsClosed(self) -> bool: ...

    def IsPeriodic(self) -> bool: ...

    def Period(self) -> float: ...

    def Value(self, X: float) -> nanoocp.gp.gp_Pnt2d: ...

    def D0(self, X: float, P: nanoocp.gp.gp_Pnt2d) -> None: ...

    def D1(self, X: float, P: nanoocp.gp.gp_Pnt2d, V: nanoocp.gp.gp_Vec2d) -> None: ...

    def D2(self, X: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None: ...

    def D3(self, X: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None: ...

    def DN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d: ...

    def Resolution(self, R3d: float) -> float: ...

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType: ...

    def Line(self) -> nanoocp.gp.gp_Lin2d: ...

    def Circle(self) -> nanoocp.gp.gp_Circ2d: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips2d: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr2d: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab2d: ...

    def Degree(self) -> int: ...

    def IsRational(self) -> bool: ...

    def NbPoles(self) -> int: ...

    def NbKnots(self) -> int: ...

    def Bezier(self) -> nanoocp.Geom2d.Geom2d_BezierCurve: ...

    def BSpline(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

class Adaptor2d_OffsetCurve(Adaptor2d_Curve2d):
    """Defines an Offset curve (algorithmic 2d curve)."""

    @overload
    def __init__(self) -> None:
        """The Offset is set to 0."""

    @overload
    def __init__(self, C: Adaptor2d_Curve2d) -> None:
        """The curve is loaded. The Offset is set to 0."""

    @overload
    def __init__(self, C: Adaptor2d_Curve2d, Offset: float) -> None:
        """
        Creates an OffsetCurve curve.
        The Offset is set to Offset.
        """

    @overload
    def __init__(self, C: Adaptor2d_Curve2d, Offset: float, WFirst: float, WLast: float) -> None:
        """
        Create an Offset curve.
        WFirst,WLast define the bounds of the Offset curve.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> Adaptor2d_Curve2d:
        """Shallow copy of adaptor."""

    @overload
    def Load(self, S: Adaptor2d_Curve2d) -> None:
        """Changes the curve. The Offset is reset to 0."""

    @overload
    def Load(self, Offset: float) -> None:
        """Changes the Offset on the current Curve."""

    @overload
    def Load(self, Offset: float, WFirst: float, WLast: float) -> None:
        """Changes the Offset Curve on the current Curve."""

    def Curve(self) -> Adaptor2d_Curve2d: ...

    def Offset(self) -> float: ...

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        If necessary, breaks the curve in intervals of
        continuity <S>. And returns the number of
        intervals.
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def Trim(self, First: float, Last: float, Tol: float) -> Adaptor2d_Curve2d:
        """
        Returns a curve equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def IsClosed(self) -> bool: ...

    def IsPeriodic(self) -> bool: ...

    def Period(self) -> float: ...

    def Value(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """Computes the point of parameter U on the curve."""

    def D0(self, U: float, P: nanoocp.gp.gp_Pnt2d) -> None:
        """Computes the point of parameter U on the curve."""

    def D1(self, U: float, P: nanoocp.gp.gp_Pnt2d, V: nanoocp.gp.gp_Vec2d) -> None:
        """
        Computes the point of parameter U on the curve with its
        first derivative.
        Raised if the continuity of the current interval
        is not C1.
        """

    def D2(self, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first and second
        derivatives V1 and V2.
        Raised if the continuity of the current interval
        is not C2.
        """

    def D3(self, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first, the second
        and the third derivative.
        Raised if the continuity of the current interval
        is not C3.
        """

    def DN(self, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        The returned vector gives the value of the derivative for the
        order of derivation N.
        Raised if the continuity of the current interval
        is not CN.
        Raised if N < 1.
        """

    def Resolution(self, R3d: float) -> float:
        """
        Returns the parametric resolution corresponding
        to the real space resolution <R3d>.
        """

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """
        Returns the type of the curve in the current
        interval: Line, Circle, Ellipse, Hyperbola,
        Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """

    def Line(self) -> nanoocp.gp.gp_Lin2d: ...

    def Circle(self) -> nanoocp.gp.gp_Circ2d: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips2d: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr2d: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab2d: ...

    def Degree(self) -> int: ...

    def IsRational(self) -> bool: ...

    def NbPoles(self) -> int: ...

    def NbKnots(self) -> int: ...

    def Bezier(self) -> nanoocp.Geom2d.Geom2d_BezierCurve: ...

    def BSpline(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    def NbSamples(self) -> int: ...
