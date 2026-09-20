"""OCCT package Adaptor3d (toolkit TKG3d)"""

from typing import overload

import nanoocp.Adaptor2d
import nanoocp.Geom
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.gp
import nanoocp.math


class Adaptor3d_Curve(nanoocp.Standard.Standard_Transient):
    """
    Root class for 3D curves on which geometric
    algorithms work.
    An adapted curve is an interface between the
    services provided by a curve and those required of
    the curve by algorithms which use it.
    Two derived concrete classes are provided:
    - GeomAdaptor_Curve for a curve from the Geom package
    - Adaptor3d_CurveOnSurface for a curve lying on
    a surface from the Geom package.

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

    def ShallowCopy(self) -> Adaptor3d_Curve:
        """Shallow copy of adaptor"""

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_Curve:
        """
        Returns a curve equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def IsClosed(self) -> bool: ...

    def IsPeriodic(self) -> bool: ...

    def Period(self) -> float: ...

    def Value(self, theU: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point of parameter U on the curve."""

    def D0(self, theU: float, theP: nanoocp.gp.gp_Pnt) -> None:
        """Computes the point of parameter U on the curve."""

    def D1(self, theU: float, theP: nanoocp.gp.gp_Pnt, theV: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point of parameter U on the curve with its
        first derivative.
        Raised if the continuity of the current interval
        is not C1.
        """

    def D2(self, theU: float, theP: nanoocp.gp.gp_Pnt, theV1: nanoocp.gp.gp_Vec, theV2: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the point P of parameter U, the first and second
        derivatives V1 and V2.
        Raised if the continuity of the current interval
        is not C2.
        """

    def D3(self, theU: float, theP: nanoocp.gp.gp_Pnt, theV1: nanoocp.gp.gp_Vec, theV2: nanoocp.gp.gp_Vec, theV3: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the point P of parameter U, the first, the second
        and the third derivative.
        Raised if the continuity of the current interval
        is not C3.
        """

    def DN(self, theU: float, theN: int) -> nanoocp.gp.gp_Vec:
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

    def Line(self) -> nanoocp.gp.gp_Lin: ...

    def Circle(self) -> nanoocp.gp.gp_Circ: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab: ...

    def Degree(self) -> int: ...

    def IsRational(self) -> bool: ...

    def NbPoles(self) -> int: ...

    def NbKnots(self) -> int: ...

    def Bezier(self) -> nanoocp.Geom.Geom_BezierCurve: ...

    def BSpline(self) -> nanoocp.Geom.Geom_BSplineCurve: ...

    def OffsetCurve(self) -> nanoocp.Geom.Geom_OffsetCurve: ...

    def EvalD0(self, theU: float) -> nanoocp.gp.gp_Pnt:
        """
        Computes the point of parameter U on the curve.
        Raises an exception on failure.
        """

    def EvalD1(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD1:
        """
        Computes the point and first derivative at parameter U.
        Raises an exception on failure.
        """

    def EvalD2(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD2:
        """
        Computes the point and first two derivatives at parameter U.
        Raises an exception on failure.
        """

    def EvalD3(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD3:
        """
        Computes the point and first three derivatives at parameter U.
        Raises an exception on failure.
        """

    def EvalDN(self, theU: float, theN: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the Nth derivative at parameter U.
        Raises an exception on failure.
        """

class Adaptor3d_Surface(nanoocp.Standard.Standard_Transient):
    """
    Root class for surfaces on which geometric algorithms work.
    An adapted surface is an interface between the
    services provided by a surface and those required of
    the surface by algorithms which use it.
    A derived concrete class is provided:
    GeomAdaptor_Surface for a surface from the Geom package.
    The Surface class describes the standard behaviour
    of a surface for generic algorithms.

    The Surface can be decomposed in intervals of any
    continuity in U and V using the method NbIntervals.
    A current interval can be set.
    Most of the methods apply to the current interval.
    Warning: All the methods are virtual and implemented with a
    raise to allow to redefined only the methods really used.

    Polynomial coefficients of BSpline surfaces used for their evaluation are cached for better
    performance. Therefore these evaluations are not thread-safe and parallel evaluations need to be
    prevented.
    """

    def __init__(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> Adaptor3d_Surface:
        """Shallow copy of adaptor"""

    def FirstUParameter(self) -> float: ...

    def LastUParameter(self) -> float: ...

    def FirstVParameter(self) -> float: ...

    def LastVParameter(self) -> float: ...

    def UContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def VContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbUIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of U intervals for continuity
        <S>. May be one if UContinuity(me) >= <S>
        """

    def NbVIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of V intervals for continuity
        <S>. May be one if VContinuity(me) >= <S>
        """

    def UIntervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Returns the intervals with the requested continuity
        in the U direction.
        """

    def VIntervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Returns the intervals with the requested continuity
        in the V direction.
        """

    def UTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_Surface:
        """
        Returns a surface trimmed in the U direction
        equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def VTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_Surface:
        """
        Returns a surface trimmed in the V direction between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def IsUClosed(self) -> bool: ...

    def IsVClosed(self) -> bool: ...

    def IsUPeriodic(self) -> bool: ...

    def UPeriod(self) -> float: ...

    def IsVPeriodic(self) -> bool: ...

    def VPeriod(self) -> float: ...

    def Value(self, theU: float, theV: float) -> nanoocp.gp.gp_Pnt:
        """
        Computes the point of parameters U,V on the surface.
        Tip: use GeomLib::NormEstim() to calculate surface normal at specified (U, V) point.
        """

    def D0(self, theU: float, theV: float, theP: nanoocp.gp.gp_Pnt) -> None:
        """Computes the point of parameters U,V on the surface."""

    def D1(self, theU: float, theV: float, theP: nanoocp.gp.gp_Pnt, theD1U: nanoocp.gp.gp_Vec, theD1V: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point and the first derivatives on the surface.
        Raised if the continuity of the current intervals is not C1.

        Tip: use GeomLib::NormEstim() to calculate surface normal at specified (U, V) point.
        """

    def D2(self, theU: float, theV: float, theP: nanoocp.gp.gp_Pnt, theD1U: nanoocp.gp.gp_Vec, theD1V: nanoocp.gp.gp_Vec, theD2U: nanoocp.gp.gp_Vec, theD2V: nanoocp.gp.gp_Vec, theD2UV: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point, the first and second
        derivatives on the surface.
        Raised if the continuity of the current
        intervals is not C2.
        """

    def D3(self, theU: float, theV: float, theP: nanoocp.gp.gp_Pnt, theD1U: nanoocp.gp.gp_Vec, theD1V: nanoocp.gp.gp_Vec, theD2U: nanoocp.gp.gp_Vec, theD2V: nanoocp.gp.gp_Vec, theD2UV: nanoocp.gp.gp_Vec, theD3U: nanoocp.gp.gp_Vec, theD3V: nanoocp.gp.gp_Vec, theD3UUV: nanoocp.gp.gp_Vec, theD3UVV: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point, the first, second and third
        derivatives on the surface.
        Raised if the continuity of the current
        intervals is not C3.
        """

    def DN(self, theU: float, theV: float, theNu: int, theNv: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of order Nu in the direction U and Nv
        in the direction V at the point P(U, V).
        Raised if the current U interval is not not CNu
        and the current V interval is not CNv.
        Raised if Nu + Nv < 1 or Nu < 0 or Nv < 0.
        """

    def UResolution(self, R3d: float) -> float:
        """
        Returns the parametric U resolution corresponding
        to the real space resolution <R3d>.
        """

    def VResolution(self, R3d: float) -> float:
        """
        Returns the parametric V resolution corresponding
        to the real space resolution <R3d>.
        """

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_SurfaceType:
        """
        Returns the type of the surface: Plane, Cylinder,
        Cone, Sphere, Torus, BezierSurface,
        BSplineSurface, SurfaceOfRevolution,
        SurfaceOfExtrusion, OtherSurface
        """

    def Plane(self) -> nanoocp.gp.gp_Pln: ...

    def Cylinder(self) -> nanoocp.gp.gp_Cylinder: ...

    def Cone(self) -> nanoocp.gp.gp_Cone: ...

    def Sphere(self) -> nanoocp.gp.gp_Sphere: ...

    def Torus(self) -> nanoocp.gp.gp_Torus: ...

    def UDegree(self) -> int: ...

    def NbUPoles(self) -> int: ...

    def VDegree(self) -> int: ...

    def NbVPoles(self) -> int: ...

    def NbUKnots(self) -> int: ...

    def NbVKnots(self) -> int: ...

    def IsURational(self) -> bool: ...

    def IsVRational(self) -> bool: ...

    def Bezier(self) -> nanoocp.Geom.Geom_BezierSurface: ...

    def BSpline(self) -> nanoocp.Geom.Geom_BSplineSurface: ...

    def AxeOfRevolution(self) -> nanoocp.gp.gp_Ax1: ...

    def Direction(self) -> nanoocp.gp.gp_Dir: ...

    def BasisCurve(self) -> Adaptor3d_Curve: ...

    def BasisSurface(self) -> Adaptor3d_Surface: ...

    def OffsetValue(self) -> float: ...

    def EvalD0(self, theU: float, theV: float) -> nanoocp.gp.gp_Pnt:
        """
        Computes the point of parameters (U, V) on the surface.
        Raises an exception on failure.
        """

    def EvalD1(self, theU: float, theV: float) -> nanoocp.Geom.Geom_Surface.ResD1:
        """
        Computes the point and first partial derivatives at (U, V).
        Raises an exception on failure.
        """

    def EvalD2(self, theU: float, theV: float) -> nanoocp.Geom.Geom_Surface.ResD2:
        """
        Computes the point and partial derivatives up to 2nd order at (U, V).
        Raises an exception on failure.
        """

    def EvalD3(self, theU: float, theV: float) -> nanoocp.Geom.Geom_Surface.ResD3:
        """
        Computes the point and partial derivatives up to 3rd order at (U, V).
        Raises an exception on failure.
        """

    def EvalDN(self, theU: float, theV: float, theNu: int, theNv: int) -> nanoocp.gp.gp_Vec:
        """
        Computes the derivative of order Nu in U and Nv in V at (U, V).
        Raises an exception on failure.
        """

class Adaptor3d_CurveOnSurface(Adaptor3d_Curve):
    """
    An interface between the services provided by a curve
    lying on a surface from the package Geom and those
    required of the curve by algorithms which use it. The
    curve is defined as a 2D curve from the Geom2d
    package, in the parametric space of the surface.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: Adaptor3d_Surface) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, S: Adaptor3d_Surface) -> None:
        """
        Creates a CurveOnSurface from the 2d curve <C> and
        the surface <S>.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> Adaptor3d_Curve:
        """Shallow copy of adaptor"""

    @overload
    def Load(self, S: Adaptor3d_Surface) -> None:
        """Changes the surface."""

    @overload
    def Load(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None:
        """Changes the 2d curve."""

    @overload
    def Load(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, S: Adaptor3d_Surface) -> None:
        """Load both curve and surface."""

    def GetCurve(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d: ...

    def GetSurface(self) -> Adaptor3d_Surface: ...

    def ChangeCurve(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d: ...

    def ChangeSurface(self) -> Adaptor3d_Surface: ...

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_Curve:
        """
        Returns a curve equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def IsClosed(self) -> bool: ...

    def IsPeriodic(self) -> bool: ...

    def Period(self) -> float: ...

    def EvalD0(self, theU: float) -> nanoocp.gp.gp_Pnt:
        """Point evaluation. Raises an exception on failure."""

    def EvalD1(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD1:
        """D1 evaluation. Raises an exception on failure."""

    def EvalD2(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD2:
        """D2 evaluation. Raises an exception on failure."""

    def EvalD3(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD3:
        """D3 evaluation. Raises an exception on failure."""

    def EvalDN(self, theU: float, theN: int) -> nanoocp.gp.gp_Vec:
        """DN evaluation. Raises an exception on failure."""

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

    def Line(self) -> nanoocp.gp.gp_Lin: ...

    def Circle(self) -> nanoocp.gp.gp_Circ: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab: ...

    def Degree(self) -> int: ...

    def IsRational(self) -> bool: ...

    def NbPoles(self) -> int: ...

    def NbKnots(self) -> int: ...

    def Bezier(self) -> nanoocp.Geom.Geom_BezierCurve: ...

    def BSpline(self) -> nanoocp.Geom.Geom_BSplineCurve: ...

class Adaptor3d_HSurfaceTool:
    def __init__(self) -> None: ...

    @staticmethod
    def FirstUParameter(theSurf: Adaptor3d_Surface) -> float: ...

    @staticmethod
    def FirstVParameter(theSurf: Adaptor3d_Surface) -> float: ...

    @staticmethod
    def LastUParameter(theSurf: Adaptor3d_Surface) -> float: ...

    @staticmethod
    def LastVParameter(theSurf: Adaptor3d_Surface) -> float: ...

    @staticmethod
    def NbUIntervals(theSurf: Adaptor3d_Surface, theSh: nanoocp.GeomAbs.GeomAbs_Shape) -> int: ...

    @staticmethod
    def NbVIntervals(theSurf: Adaptor3d_Surface, theSh: nanoocp.GeomAbs.GeomAbs_Shape) -> int: ...

    @staticmethod
    def UIntervals(theSurf: Adaptor3d_Surface, theTab: nanoocp.NCollection.NCollection_Array1[float], theSh: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    @staticmethod
    def VIntervals(theSurf: Adaptor3d_Surface, theTab: nanoocp.NCollection.NCollection_Array1[float], theSh: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    @staticmethod
    def UTrim(theSurf: Adaptor3d_Surface, theFirst: float, theLast: float, theTol: float) -> Adaptor3d_Surface:
        """If <First> >= <Last>"""

    @staticmethod
    def VTrim(theSurf: Adaptor3d_Surface, theFirst: float, theLast: float, theTol: float) -> Adaptor3d_Surface:
        """If <First> >= <Last>"""

    @staticmethod
    def IsUClosed(theSurf: Adaptor3d_Surface) -> bool: ...

    @staticmethod
    def IsVClosed(theSurf: Adaptor3d_Surface) -> bool: ...

    @staticmethod
    def IsUPeriodic(theSurf: Adaptor3d_Surface) -> bool: ...

    @staticmethod
    def UPeriod(theSurf: Adaptor3d_Surface) -> float: ...

    @staticmethod
    def IsVPeriodic(theSurf: Adaptor3d_Surface) -> bool: ...

    @staticmethod
    def VPeriod(theSurf: Adaptor3d_Surface) -> float: ...

    @staticmethod
    def Value(theSurf: Adaptor3d_Surface, theU: float, theV: float) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def D0(theSurf: Adaptor3d_Surface, theU: float, theV: float, thePnt: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def D1(theSurf: Adaptor3d_Surface, theU: float, theV: float, thePnt: nanoocp.gp.gp_Pnt, theD1U: nanoocp.gp.gp_Vec, theD1V: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def D2(theSurf: Adaptor3d_Surface, theU: float, theV: float, thePnt: nanoocp.gp.gp_Pnt, theD1U: nanoocp.gp.gp_Vec, theD1V: nanoocp.gp.gp_Vec, theD2U: nanoocp.gp.gp_Vec, theD2V: nanoocp.gp.gp_Vec, theD2UV: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def D3(theSurf: Adaptor3d_Surface, theU: float, theV: float, thePnt: nanoocp.gp.gp_Pnt, theD1U: nanoocp.gp.gp_Vec, theD1V: nanoocp.gp.gp_Vec, theD2U: nanoocp.gp.gp_Vec, theD2V: nanoocp.gp.gp_Vec, theD2UV: nanoocp.gp.gp_Vec, theD3U: nanoocp.gp.gp_Vec, theD3V: nanoocp.gp.gp_Vec, theD3UUV: nanoocp.gp.gp_Vec, theD3UVV: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def DN(theSurf: Adaptor3d_Surface, theU: float, theV: float, theNU: int, theNV: int) -> nanoocp.gp.gp_Vec: ...

    @staticmethod
    def UResolution(theSurf: Adaptor3d_Surface, theR3d: float) -> float: ...

    @staticmethod
    def VResolution(theSurf: Adaptor3d_Surface, theR3d: float) -> float: ...

    @staticmethod
    def GetType(theSurf: Adaptor3d_Surface) -> nanoocp.GeomAbs.GeomAbs_SurfaceType: ...

    @staticmethod
    def Plane(theSurf: Adaptor3d_Surface) -> nanoocp.gp.gp_Pln: ...

    @staticmethod
    def Cylinder(theSurf: Adaptor3d_Surface) -> nanoocp.gp.gp_Cylinder: ...

    @staticmethod
    def Cone(theSurf: Adaptor3d_Surface) -> nanoocp.gp.gp_Cone: ...

    @staticmethod
    def Torus(theSurf: Adaptor3d_Surface) -> nanoocp.gp.gp_Torus: ...

    @staticmethod
    def Sphere(theSurf: Adaptor3d_Surface) -> nanoocp.gp.gp_Sphere: ...

    @staticmethod
    def Bezier(theSurf: Adaptor3d_Surface) -> nanoocp.Geom.Geom_BezierSurface: ...

    @staticmethod
    def BSpline(theSurf: Adaptor3d_Surface) -> nanoocp.Geom.Geom_BSplineSurface: ...

    @staticmethod
    def AxeOfRevolution(theSurf: Adaptor3d_Surface) -> nanoocp.gp.gp_Ax1: ...

    @staticmethod
    def Direction(theSurf: Adaptor3d_Surface) -> nanoocp.gp.gp_Dir: ...

    @staticmethod
    def BasisCurve(theSurf: Adaptor3d_Surface) -> Adaptor3d_Curve: ...

    @staticmethod
    def BasisSurface(theSurf: Adaptor3d_Surface) -> Adaptor3d_Surface: ...

    @staticmethod
    def OffsetValue(theSurf: Adaptor3d_Surface) -> float: ...

    @staticmethod
    def IsSurfG1(theSurf: Adaptor3d_Surface, theAlongU: bool, theAngTol: float = 1e-12) -> bool: ...

    @overload
    @staticmethod
    def NbSamplesU(S: Adaptor3d_Surface) -> int: ...

    @overload
    @staticmethod
    def NbSamplesU(S: Adaptor3d_Surface, u1: float, u2: float) -> int: ...

    @overload
    @staticmethod
    def NbSamplesV(S: Adaptor3d_Surface) -> int: ...

    @overload
    @staticmethod
    def NbSamplesV(arg0: Adaptor3d_Surface, v1: float, v2: float) -> int: ...

class Adaptor3d_HVertex(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt2d, Ori: nanoocp.TopAbs.TopAbs_Orientation, Resolution: float) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Pnt2d: ...

    def Parameter(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> float: ...

    def Resolution(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> float:
        """Parametric resolution (2d)."""

    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def IsSame(self, Other: Adaptor3d_HVertex) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Adaptor3d_InterFunc(nanoocp.math.math_FunctionWithDerivative):
    """
    Used to find the points U(t) = U0 or V(t) = V0 in
    order to determine the Cn discontinuities of an
    Adpator_CurveOnSurface relatively to the
    discontinuities of the surface. Used to
    find the roots of the functions
    """

    def __init__(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d, FixVal: float, Fix: int) -> None:
        """
        build the function U(t)=FixVal if Fix =1 or
        V(t)=FixVal if Fix=2
        """

    def Value(self, X: float) -> tuple[bool, float]:
        """
        computes the value <F>of the function for the variable <X>.
        Returns True if the calculation were successfully done,
        False otherwise.
        """

    def Derivative(self, X: float) -> tuple[bool, float]:
        """
        computes the derivative <D> of the function
        for the variable <X>.
        Returns True if the calculation were successfully done,
        False otherwise.
        """

    def Values(self, X: float) -> tuple[bool, float, float]:
        """
        computes the value <F> and the derivative <D> of the
        function for the variable <X>.
        Returns True if the calculation were successfully done,
        False otherwise.
        """

class Adaptor3d_IsoCurve(Adaptor3d_Curve):
    """
    Defines an isoparametric curve on a surface. The
    type of isoparametric curve (U or V) is defined
    with the enumeration IsoType from GeomAbs if
    NoneIso is given an error is raised.
    """

    @overload
    def __init__(self) -> None:
        """The iso is set to NoneIso."""

    @overload
    def __init__(self, S: Adaptor3d_Surface) -> None:
        """The surface is loaded. The iso is set to NoneIso."""

    @overload
    def __init__(self, S: Adaptor3d_Surface, Iso: nanoocp.GeomAbs.GeomAbs_IsoType, Param: float) -> None:
        """
        Creates an IsoCurve curve. Iso defines the type
        (isoU or isoU) Param defines the value of the
        iso. The bounds of the iso are the bounds of
        the surface.
        """

    @overload
    def __init__(self, S: Adaptor3d_Surface, Iso: nanoocp.GeomAbs.GeomAbs_IsoType, Param: float, WFirst: float, WLast: float) -> None:
        """
        Create an IsoCurve curve. Iso defines the type
        (isoU or isov). Param defines the value of the
        iso. WFirst,WLast define the bounds of the iso.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ShallowCopy(self) -> Adaptor3d_Curve:
        """Shallow copy of adaptor"""

    @overload
    def Load(self, S: Adaptor3d_Surface) -> None:
        """Changes the surface. The iso is reset to NoneIso."""

    @overload
    def Load(self, Iso: nanoocp.GeomAbs.GeomAbs_IsoType, Param: float) -> None: ...

    @overload
    def Load(self, Iso: nanoocp.GeomAbs.GeomAbs_IsoType, Param: float, WFirst: float, WLast: float) -> None:
        """Changes the iso on the current surface."""

    def Surface(self) -> Adaptor3d_Surface: ...

    def Iso(self) -> nanoocp.GeomAbs.GeomAbs_IsoType: ...

    def Parameter(self) -> float: ...

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def NbIntervals(self, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    def Intervals(self, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_Curve:
        """
        Returns a curve equivalent of <me> between
        parameters <First> and <Last>. <Tol> is used to
        test for 3d points confusion.
        If <First> >= <Last>
        """

    def IsClosed(self) -> bool: ...

    def IsPeriodic(self) -> bool: ...

    def Period(self) -> float: ...

    def EvalD0(self, theU: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point of parameter theU on the curve."""

    def EvalD1(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD1:
        """
        Computes the point of parameter theU on the curve with its first derivative.
        Raised if the continuity of the current interval is not C1.
        """

    def EvalD2(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD2:
        """
        Returns the point and the first and second derivatives at parameter theU.
        Raised if the continuity of the current interval is not C2.
        """

    def EvalD3(self, theU: float) -> nanoocp.Geom.Geom_Curve.ResD3:
        """
        Returns the point and the first, second and third derivatives at parameter theU.
        Raised if the continuity of the current interval is not C3.
        """

    def EvalDN(self, theU: float, theN: int) -> nanoocp.gp.gp_Vec:
        """
        Returns the derivative of order theN at parameter theU.
        Raised if the continuity of the current interval is not CN.
        Raised if theN < 1.
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

    def Line(self) -> nanoocp.gp.gp_Lin: ...

    def Circle(self) -> nanoocp.gp.gp_Circ: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab: ...

    def Degree(self) -> int: ...

    def IsRational(self) -> bool: ...

    def NbPoles(self) -> int: ...

    def NbKnots(self) -> int: ...

    def Bezier(self) -> nanoocp.Geom.Geom_BezierCurve: ...

    def BSpline(self) -> nanoocp.Geom.Geom_BSplineCurve: ...

class Adaptor3d_TopolTool(nanoocp.Standard.Standard_Transient):
    """
    This class provides a default topological tool,
    based on the Umin,Vmin,Umax,Vmax of an HSurface from Adaptor3d.
    All methods and fields may be redefined when inheriting from this class.
    This class is used to instantiate algorithms as Intersection, outlines,...
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Surface: Adaptor3d_Surface) -> None: ...

    @overload
    def Initialize(self) -> None: ...

    @overload
    def Initialize(self, S: Adaptor3d_Surface) -> None: ...

    @overload
    def Initialize(self, Curve: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None: ...

    def Init(self) -> None: ...

    def More(self) -> bool: ...

    def Value(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d: ...

    def Next(self) -> None: ...

    def InitVertexIterator(self) -> None: ...

    def MoreVertex(self) -> bool: ...

    def Vertex(self) -> Adaptor3d_HVertex: ...

    def NextVertex(self) -> None: ...

    def Classify(self, P: nanoocp.gp.gp_Pnt2d, Tol: float, ReacdreOnPeriodic: bool = True) -> nanoocp.TopAbs.TopAbs_State: ...

    def IsThePointOn(self, P: nanoocp.gp.gp_Pnt2d, Tol: float, ReacdreOnPeriodic: bool = True) -> bool: ...

    @overload
    def Orientation(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> nanoocp.TopAbs.TopAbs_Orientation:
        """
        If the function returns the orientation of the arc.
        If the orientation is FORWARD or REVERSED, the arc is
        a "real" limit of the surface.
        If the orientation is INTERNAL or EXTERNAL, the arc is
        considered as an arc on the surface.
        """

    @overload
    def Orientation(self, V: Adaptor3d_HVertex) -> nanoocp.TopAbs.TopAbs_Orientation:
        """
        Returns the orientation of the vertex V.
        The vertex has been found with an exploration on
        a given arc. The orientation is the orientation
        of the vertex on this arc.
        """

    def Identical(self, V1: Adaptor3d_HVertex, V2: Adaptor3d_HVertex) -> bool:
        """
        Returns True if the vertices V1 and V2 are identical.
        This method does not take the orientation of the
        vertices in account.
        """

    def Has3d(self) -> bool:
        """
        answers if arcs and vertices may have 3d representations,
        so that we could use Tol3d and Pnt methods.
        """

    @overload
    def Tol3d(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> float:
        """returns 3d tolerance of the arc C"""

    @overload
    def Tol3d(self, V: Adaptor3d_HVertex) -> float:
        """returns 3d tolerance of the vertex V"""

    def Pnt(self, V: Adaptor3d_HVertex) -> nanoocp.gp.gp_Pnt:
        """returns 3d point of the vertex V"""

    def ComputeSamplePoints(self) -> None: ...

    def NbSamplesU(self) -> int:
        """compute the sample-points for the intersections algorithms"""

    def NbSamplesV(self) -> int:
        """compute the sample-points for the intersections algorithms"""

    def NbSamples(self) -> int:
        """compute the sample-points for the intersections algorithms"""

    def UParameters(self, theArray: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        return the set of U parameters on the surface
        obtained by the method SamplePnts
        """

    def VParameters(self, theArray: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        return the set of V parameters on the surface
        obtained by the method SamplePnts
        """

    def SamplePoint(self, Index: int, P2d: nanoocp.gp.gp_Pnt2d, P3d: nanoocp.gp.gp_Pnt) -> None: ...

    def DomainIsInfinite(self) -> bool: ...

    def SamplePnts(self, theDefl: float, theNUmin: int, theNVmin: int) -> None:
        """
        Compute the sample-points for the intersections algorithms by adaptive algorithm for BSpline
        surfaces. For other surfaces algorithm is the same as in method ComputeSamplePoints(), but
        only fill arrays of U and V sample parameters;
        @param[in] theDefl   a required deflection
        @param[in] theNUmin  minimal nb points for U
        @param[in] theNVmin  minimal nb points for V
        """

    def BSplSamplePnts(self, theDefl: float, theNUmin: int, theNVmin: int) -> None:
        """
        Compute the sample-points for the intersections algorithms
        by adaptive algorithm for BSpline surfaces - is used in SamplePnts
        @param[in] theDefl   required deflection
        @param[in] theNUmin  minimal nb points for U
        @param[in] theNVmin  minimal nb points for V
        """

    def IsUniformSampling(self) -> bool:
        """Returns true if provide uniform sampling of points."""

    @staticmethod
    def GetConeApexParam(theC: nanoocp.gp.gp_Cone) -> tuple[float, float]:
        """
        Computes the cone's apex parameters.
        @param[in] theC conical surface
        @param[in] theU U parameter of cone's apex
        @param[in] theV V parameter of cone's apex
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
