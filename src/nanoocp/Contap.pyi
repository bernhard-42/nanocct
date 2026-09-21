"""OCCT package Contap (toolkit TKHLR)"""

import enum
from typing import overload

import nanoocp.Adaptor2d
import nanoocp.Adaptor3d
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.IntSurf
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp
import nanoocp.math


class Contap_TFunction(enum.IntEnum):
    Contap_ContourStd = 0

    Contap_ContourPrs = 1

    Contap_DraftStd = 2

    Contap_DraftPrs = 3

Contap_ContourStd: Contap_TFunction = Contap_TFunction.Contap_ContourStd

Contap_ContourPrs: Contap_TFunction = Contap_TFunction.Contap_ContourPrs

Contap_DraftStd: Contap_TFunction = Contap_TFunction.Contap_DraftStd

Contap_DraftPrs: Contap_TFunction = Contap_TFunction.Contap_DraftPrs

class Contap_IType(enum.IntEnum):
    Contap_Lin = 0

    Contap_Circle = 1

    Contap_Walking = 2

    Contap_Restriction = 3

Contap_Lin: Contap_IType = Contap_IType.Contap_Lin

Contap_Circle: Contap_IType = Contap_IType.Contap_Circle

Contap_Walking: Contap_IType = Contap_IType.Contap_Walking

Contap_Restriction: Contap_IType = Contap_IType.Contap_Restriction

class Contap_ArcFunction(nanoocp.math.math_FunctionWithDerivative):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Contap_ArcFunction) -> None: ...

    @overload
    def Set(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None: ...

    @overload
    def Set(self, Direction: nanoocp.gp.gp_Dir) -> None: ...

    @overload
    def Set(self, Direction: nanoocp.gp.gp_Dir, Angle: float) -> None: ...

    @overload
    def Set(self, Eye: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Set(self, Eye: nanoocp.gp.gp_Pnt, Angle: float) -> None: ...

    @overload
    def Set(self, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    def Value(self, X: float) -> tuple[bool, float]: ...

    def Derivative(self, X: float) -> tuple[bool, float]: ...

    def Values(self, X: float) -> tuple[bool, float, float]: ...

    def NbSamples(self) -> int: ...

    def GetStateNumber(self) -> int: ...

    def Valpoint(self, Index: int) -> nanoocp.gp.gp_Pnt: ...

    def Quadric(self) -> nanoocp.IntSurf.IntSurf_Quadric: ...

    def Surface(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """Returns mySurf field"""

    def LastComputedPoint(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the point, which has been computed
        while the last calling Value() method
        """

class Contap_ContAna:
    """
    This class provides the computation of the contours
    for quadric surfaces.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Contap_ContAna) -> None: ...

    @overload
    def Perform(self, S: nanoocp.gp.gp_Sphere, D: nanoocp.gp.gp_Dir) -> None: ...

    @overload
    def Perform(self, S: nanoocp.gp.gp_Sphere, D: nanoocp.gp.gp_Dir, Ang: float) -> None: ...

    @overload
    def Perform(self, S: nanoocp.gp.gp_Sphere, Eye: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Cylinder, D: nanoocp.gp.gp_Dir) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Cylinder, D: nanoocp.gp.gp_Dir, Ang: float) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Cylinder, Eye: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Cone, D: nanoocp.gp.gp_Dir) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Cone, D: nanoocp.gp.gp_Dir, Ang: float) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Cone, Eye: nanoocp.gp.gp_Pnt) -> None: ...

    def IsDone(self) -> bool: ...

    def NbContours(self) -> int: ...

    def TypeContour(self) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """
        Returns GeomAbs_Line or GeomAbs_Circle, when
        IsDone() returns True.
        """

    def Circle(self) -> nanoocp.gp.gp_Circ: ...

    def Line(self, Index: int) -> nanoocp.gp.gp_Lin: ...

class Contap_Point:
    """
    Definition of a vertex on the contour line.
    Most of the time, such a point is an intersection
    between the contour and a restriction of the surface.
    When it is not the method IsOnArc return False.
    Such a point is contains geometrical information (see
    the Value method) and logical information.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, Pt: nanoocp.gp.gp_Pnt, U: float, V: float) -> None:
        """Creates a point."""

    @overload
    def __init__(self, theOther: Contap_Point) -> None: ...

    def SetValue(self, Pt: nanoocp.gp.gp_Pnt, U: float, V: float) -> None:
        """Sets the values for a point."""

    def SetParameter(self, Para: float) -> None:
        """Set the value of the parameter on the intersection line."""

    def SetVertex(self, V: nanoocp.Adaptor3d.Adaptor3d_HVertex | None) -> None:
        """
        Sets the values of a point which is a vertex on
        the initial facet of restriction of one
        of the surface.
        """

    def SetArc(self, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Param: float, TLine: nanoocp.IntSurf.IntSurf_Transition, TArc: nanoocp.IntSurf.IntSurf_Transition) -> None:
        """
        Sets the value of the arc and of the parameter on
        this arc of the point.
        """

    def SetMultiple(self) -> None: ...

    def SetInternal(self) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Pnt:
        """Returns the intersection point (geometric information)."""

    def ParameterOnLine(self) -> float:
        """
        This method returns the parameter of the point
        on the intersection line.
        If the points does not belong to an intersection line,
        the value returned does not have any sens.
        """

    def Parameters(self) -> tuple[float, float]:
        """Returns the parameters on the surface of the point."""

    def IsOnArc(self) -> bool:
        """
        Returns True when the point is an intersection between
        the contour and a restriction.
        """

    def Arc(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """
        Returns the arc of restriction containing the
        vertex.
        """

    def ParameterOnArc(self) -> float:
        """
        Returns the parameter of the point on the
        arc returned by the method Arc().
        """

    def TransitionOnLine(self) -> nanoocp.IntSurf.IntSurf_Transition:
        """Returns the transition of the point on the contour."""

    def TransitionOnArc(self) -> nanoocp.IntSurf.IntSurf_Transition:
        """Returns the transition of the point on the arc."""

    def IsVertex(self) -> bool:
        """
        Returns TRUE if the point is a vertex on the initial
        restriction facet of the surface.
        """

    def Vertex(self) -> nanoocp.Adaptor3d.Adaptor3d_HVertex:
        """
        Returns the information about the point when it is
        on the domain of the patch, i-e when the function
        IsVertex returns True.
        Otherwise, an exception is raised.
        """

    def IsMultiple(self) -> bool:
        """
        Returns True if the point belongs to several
        lines.
        """

    def IsInternal(self) -> bool:
        """
        Returns True if the point is an internal one, i.e
        if the tangent to the line on the point and the
        eye direction are parallel.
        """

class Contap_Line:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Contap_Line) -> None: ...

    def SetLineOn2S(self, L: nanoocp.IntSurf.IntSurf_LineOn2S | None) -> None: ...

    def Clear(self) -> None: ...

    def LineOn2S(self) -> nanoocp.IntSurf.IntSurf_LineOn2S: ...

    def ResetSeqOfVertex(self) -> None: ...

    @overload
    def Add(self, P: nanoocp.IntSurf.IntSurf_PntOn2S) -> None: ...

    @overload
    def Add(self, P: Contap_Point) -> None: ...

    @overload
    def SetValue(self, L: nanoocp.gp.gp_Lin) -> None: ...

    @overload
    def SetValue(self, C: nanoocp.gp.gp_Circ) -> None: ...

    @overload
    def SetValue(self, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    def NbVertex(self) -> int: ...

    def Vertex(self, Index: int) -> Contap_Point: ...

    def TypeContour(self) -> Contap_IType:
        """
        Returns Contap_Lin for a line, Contap_Circle for
        a circle, and Contap_Walking for a Walking line,
        Contap_Restriction for a part of boundary.
        """

    def NbPnts(self) -> int: ...

    def Point(self, Index: int) -> nanoocp.IntSurf.IntSurf_PntOn2S: ...

    def Line(self) -> nanoocp.gp.gp_Lin: ...

    def Circle(self) -> nanoocp.gp.gp_Circ: ...

    def Arc(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d: ...

    def SetTransitionOnS(self, T: nanoocp.IntSurf.IntSurf_TypeTrans) -> None:
        """Set The Transition of the line."""

    def TransitionOnS(self) -> nanoocp.IntSurf.IntSurf_TypeTrans:
        """
        returns IN if at the "left" of the line, the normale of the
        surface is oriented to the observator.
        """

class Contap_ThePathPointOfTheSearch:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, Tol: float, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Parameter: float) -> None: ...

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, Tol: float, V: nanoocp.Adaptor3d.Adaptor3d_HVertex | None, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Parameter: float) -> None: ...

    @overload
    def __init__(self, theOther: Contap_ThePathPointOfTheSearch) -> None: ...

    @overload
    def SetValue(self, P: nanoocp.gp.gp_Pnt, Tol: float, V: nanoocp.Adaptor3d.Adaptor3d_HVertex | None, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Parameter: float) -> None: ...

    @overload
    def SetValue(self, P: nanoocp.gp.gp_Pnt, Tol: float, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Parameter: float) -> None: ...

    def Value(self) -> nanoocp.gp.gp_Pnt: ...

    def Tolerance(self) -> float: ...

    def IsNew(self) -> bool: ...

    def Vertex(self) -> nanoocp.Adaptor3d.Adaptor3d_HVertex: ...

    def Arc(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d: ...

    def Parameter(self) -> float: ...

class Contap_TheSegmentOfTheSearch:
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Contap_TheSegmentOfTheSearch) -> None: ...

    def SetValue(self, A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None:
        """Defines the concerned arc."""

    def SetLimitPoint(self, V: Contap_ThePathPointOfTheSearch, First: bool) -> None:
        """
        Defines the first point or the last point,
        depending on the value of the boolean First.
        """

    def Curve(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """
        Returns the geometric curve on the surface 's domain
        which is solution.
        """

    def HasFirstPoint(self) -> bool:
        """
        Returns True if there is a vertex (ThePathPoint) defining
        the lowest valid parameter on the arc.
        """

    def FirstPoint(self) -> Contap_ThePathPointOfTheSearch:
        """Returns the first point."""

    def HasLastPoint(self) -> bool:
        """
        Returns True if there is a vertex (ThePathPoint) defining
        the greatest valid parameter on the arc.
        """

    def LastPoint(self) -> Contap_ThePathPointOfTheSearch:
        """Returns the last point."""

class Contap_TheSearch:
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Contap_TheSearch) -> None: ...

    def Perform(self, F: Contap_ArcFunction, Domain: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, TolBoundary: float, TolTangency: float, RecheckOnRegularity: bool = False) -> None:
        """
        Algorithm to find the points and parts of curves of Domain
        (domain of of restriction of a surface) which verify
        F = 0.
        TolBoundary defines if a curve is on Q.
        TolTangency defines if a point is on Q.
        """

    def IsDone(self) -> bool:
        """Returns True if the calculus was successful."""

    def AllArcSolution(self) -> bool:
        """
        Returns true if all arc of the Arcs are solution (inside
        the surface).
        An exception is raised if IsDone returns False.
        """

    def NbPoints(self) -> int:
        """
        Returns the number of resulting points.
        An exception is raised if IsDone returns False (NotDone).
        """

    def Point(self, Index: int) -> Contap_ThePathPointOfTheSearch:
        """
        Returns the resulting point of range Index.
        The exception NotDone is raised if IsDone() returns
        False.
        The exception OutOfRange is raised if
        Index <= 0 or Index > NbPoints.
        """

    def NbSegments(self) -> int:
        """
        Returns the number of the resulting segments.
        An exception is raised if IsDone returns False (NotDone).
        """

    def Segment(self, Index: int) -> Contap_TheSegmentOfTheSearch:
        """
        Returns the resulting segment of range Index.
        The exception NotDone is raised if IsDone() returns
        False.
        The exception OutOfRange is raised if
        Index <= 0 or Index > NbPoints.
        """

class Contap_TheSearchInside:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, F: Contap_SurfFunction, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, T: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Epsilon: float) -> None: ...

    @overload
    def __init__(self, theOther: Contap_TheSearchInside) -> None: ...

    @overload
    def Perform(self, F: Contap_SurfFunction, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, T: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Epsilon: float) -> None: ...

    @overload
    def Perform(self, F: Contap_SurfFunction, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, UStart: float, VStart: float) -> None: ...

    def IsDone(self) -> bool: ...

    def NbPoints(self) -> int:
        """
        Returns the number of points.
        The exception NotDone if raised if IsDone
        returns False.
        """

    def Value(self, Index: int) -> nanoocp.IntSurf.IntSurf_InteriorPoint:
        """
        Returns the point of range Index.
        The exception NotDone if raised if IsDone
        returns False.
        The exception OutOfRange if raised if
        Index <= 0 or Index > NbPoints.
        """

class Contap_SurfFunction(nanoocp.math.math_FunctionSetWithDerivatives):
    """
    This class describes the function on a parametric surface.
    the form of the function is F(u,v) = 0 where u and v are
    the parametric coordinates of a point on the surface,
    to compute the contours of the surface.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Contap_SurfFunction) -> None: ...

    @overload
    def Set(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None: ...

    @overload
    def Set(self, Eye: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Set(self, Dir: nanoocp.gp.gp_Dir) -> None: ...

    @overload
    def Set(self, Dir: nanoocp.gp.gp_Dir, Angle: float) -> None: ...

    @overload
    def Set(self, Eye: nanoocp.gp.gp_Pnt, Angle: float) -> None: ...

    @overload
    def Set(self, Tolerance: float) -> None: ...

    def NbVariables(self) -> int:
        """This method has to return 2."""

    def NbEquations(self) -> int:
        """This method has to return 1."""

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool:
        """The dimension of F is 1."""

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool:
        """The dimension of D is (1,2)."""

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool: ...

    def Root(self) -> float:
        """
        Root is the value of the function at the solution.
        It is a vector of dimension 1, i-e a real.
        """

    def Tolerance(self) -> float:
        """
        Returns the value Tol so that if std::abs(Func.Root())<Tol
        the function is considered null.
        """

    def Point(self) -> nanoocp.gp.gp_Pnt:
        """Returns the value of the solution point on the surface."""

    def IsTangent(self) -> bool: ...

    def Direction3d(self) -> nanoocp.gp.gp_Vec: ...

    def Direction2d(self) -> nanoocp.gp.gp_Dir2d: ...

    def FunctionType(self) -> Contap_TFunction: ...

    def Eye(self) -> nanoocp.gp.gp_Pnt: ...

    def Direction(self) -> nanoocp.gp.gp_Dir: ...

    def Angle(self) -> float: ...

    def Surface(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    def PSurface(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface:
        """Method is entered for compatibility with IntPatch_TheSurfFunction."""

class Contap_Contour:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Direction: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def __init__(self, Eye: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, Direction: nanoocp.gp.gp_Vec, Angle: float) -> None: ...

    @overload
    def __init__(self, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Direction: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def __init__(self, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Eye: nanoocp.gp.gp_Pnt) -> None:
        """Creates the contour for a perspective view."""

    @overload
    def __init__(self, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Direction: nanoocp.gp.gp_Vec, Angle: float) -> None:
        """Creates the contour in a given direction."""

    @overload
    def __init__(self, theOther: Contap_Contour) -> None: ...

    @overload
    def Perform(self, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None) -> None: ...

    @overload
    def Perform(self, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Direction: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def Perform(self, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Direction: nanoocp.gp.gp_Vec, Angle: float) -> None:
        """Creates the contour in a given direction."""

    @overload
    def Perform(self, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Domain: nanoocp.Adaptor3d.Adaptor3d_TopolTool | None, Eye: nanoocp.gp.gp_Pnt) -> None:
        """Creates the contour for a perspective view."""

    @overload
    def Init(self, Direction: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def Init(self, Direction: nanoocp.gp.gp_Vec, Angle: float) -> None: ...

    @overload
    def Init(self, Eye: nanoocp.gp.gp_Pnt) -> None: ...

    def IsDone(self) -> bool: ...

    def IsEmpty(self) -> bool:
        """Returns true if the is no line."""

    def NbLines(self) -> int: ...

    def Line(self, Index: int) -> Contap_Line: ...

    def SurfaceFunction(self) -> Contap_SurfFunction:
        """
        Returns a reference on the internal SurfaceFunction.
        This is used to compute tangents on the lines.
        """

class Contap_HContTool:
    """
    Tool for the intersection between 2 surfaces.
    Regroupe pour l instant les methodes hors Adaptor3d...
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Contap_HContTool) -> None: ...

    @staticmethod
    def NbSamplesU(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, u1: float, u2: float) -> int: ...

    @staticmethod
    def NbSamplesV(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, v1: float, v2: float) -> int: ...

    @staticmethod
    def NbSamplePoints(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> int: ...

    @staticmethod
    def SamplePoint(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Index: int) -> tuple[float, float]: ...

    @staticmethod
    def HasBeenSeen(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> bool:
        """
        Returns True if all the intersection point and edges
        are known on the Arc.
        The intersection point are given as vertices.
        The intersection edges are given as intervals between
        two vertices.
        """

    @staticmethod
    def NbSamplesOnArc(A: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> int:
        """
        returns the number of points which is used to make
        a sample on the arc. this number is a function of
        the Surface and the CurveOnSurface complexity.
        """

    @staticmethod
    def Bounds(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> tuple[float, float]:
        """
        Returns the parametric limits on the arc C.
        These limits must be finite : they are either
        the real limits of the arc, for a finite arc,
        or a bounding box for an infinite arc.
        """

    @staticmethod
    def Project(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, P: nanoocp.gp.gp_Pnt2d, Ptproj: nanoocp.gp.gp_Pnt2d) -> tuple[bool, float]:
        """
        Projects the point P on the arc C.
        If the methods returns true, the projection is
        successful, and Paramproj is the parameter on the arc
        of the projected point, Ptproj is the projected Point.
        If the method returns false, Param proj and Ptproj
        are not significant.
        """

    @staticmethod
    def Tolerance(V: nanoocp.Adaptor3d.Adaptor3d_HVertex | None, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> float:
        """
        Returns the parametric tolerance used to consider
        that the vertex and another point meet, i-e
        if std::abs(parameter(Vertex) - parameter(OtherPnt))<=
        Tolerance, the points are "merged".
        """

    @staticmethod
    def Parameter(V: nanoocp.Adaptor3d.Adaptor3d_HVertex | None, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> float:
        """Returns the parameter of the vertex V on the arc A."""

    @staticmethod
    def NbPoints(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> int:
        """Returns the number of intersection points on the arc A."""

    @staticmethod
    def Value(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Index: int, Pt: nanoocp.gp.gp_Pnt) -> tuple[float, float]:
        """
        Returns the value (Pt), the tolerance (Tol), and
        the parameter (U) on the arc A , of the intersection
        point of range Index.
        """

    @staticmethod
    def IsVertex(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Index: int) -> bool:
        """
        Returns True if the intersection point of range Index
        corresponds with a vertex on the arc A.
        """

    @staticmethod
    def Vertex(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Index: int) -> nanoocp.Adaptor3d.Adaptor3d_HVertex:
        """
        When IsVertex returns True, this method returns the
        vertex on the arc A.
        """

    @staticmethod
    def NbSegments(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> int:
        """
        returns the number of part of A solution of the
        of intersection problem.
        """

    @staticmethod
    def HasFirstPoint(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Index: int) -> tuple[bool, int]:
        """
        Returns True when the segment of range Index is not
        open at the left side. In that case, IndFirst is the
        range in the list intersection points (see NbPoints)
        of the one which defines the left bound of the segment.
        Otherwise, the method has to return False, and IndFirst
        has no meaning.
        """

    @staticmethod
    def HasLastPoint(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, Index: int) -> tuple[bool, int]:
        """
        Returns True when the segment of range Index is not
        open at the right side. In that case, IndLast is the
        range in the list intersection points (see NbPoints)
        of the one which defines the right bound of the segment.
        Otherwise, the method has to return False, and IndLast
        has no meaning.
        """

    @staticmethod
    def IsAllSolution(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> bool:
        """
        Returns True when the whole restriction is solution
        of the intersection problem.
        """

class Contap_HCurve2dTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Contap_HCurve2dTool) -> None: ...

    @staticmethod
    def FirstParameter(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> float: ...

    @staticmethod
    def LastParameter(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> float: ...

    @staticmethod
    def Continuity(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    @staticmethod
    def NbIntervals(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(myclass) >= <S>
        """

    @staticmethod
    def Intervals(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    @staticmethod
    def IsClosed(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> bool: ...

    @staticmethod
    def IsPeriodic(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> bool: ...

    @staticmethod
    def Period(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> float: ...

    @staticmethod
    def Value(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, U: float) -> nanoocp.gp.gp_Pnt2d:
        """Computes the point of parameter U on the curve."""

    @staticmethod
    def D0(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, U: float, P: nanoocp.gp.gp_Pnt2d) -> None:
        """Computes the point of parameter U on the curve."""

    @staticmethod
    def D1(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, U: float, P: nanoocp.gp.gp_Pnt2d, V: nanoocp.gp.gp_Vec2d) -> None:
        """
        Computes the point of parameter U on the curve with its
        first derivative.
        Raised if the continuity of the current interval
        is not C1.
        """

    @staticmethod
    def D2(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first and second
        derivatives V1 and V2.
        Raised if the continuity of the current interval
        is not C2.
        """

    @staticmethod
    def D3(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d, V3: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point P of parameter U, the first, the second
        and the third derivative.
        Raised if the continuity of the current interval
        is not C3.
        """

    @staticmethod
    def DN(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, U: float, N: int) -> nanoocp.gp.gp_Vec2d:
        """
        The returned vector gives the value of the derivative for the
        order of derivation N.
        Raised if the continuity of the current interval
        is not CN.
        Raised if N < 1.
        """

    @staticmethod
    def Resolution(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, R3d: float) -> float:
        """
        Returns the parametric resolution corresponding
        to the real space resolution <R3d>.
        """

    @staticmethod
    def GetType(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """
        Returns the type of the curve in the current
        interval: Line, Circle, Ellipse, Hyperbola,
        Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """

    @staticmethod
    def Line(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.gp.gp_Lin2d: ...

    @staticmethod
    def Circle(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.gp.gp_Circ2d: ...

    @staticmethod
    def Ellipse(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.gp.gp_Elips2d: ...

    @staticmethod
    def Hyperbola(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.gp.gp_Hypr2d: ...

    @staticmethod
    def Parabola(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.gp.gp_Parab2d: ...

    @staticmethod
    def Bezier(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.Geom2d.Geom2d_BezierCurve: ...

    @staticmethod
    def BSpline(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    @staticmethod
    def NbSamples(C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, U0: float, U1: float) -> int: ...

class Contap_SurfProps:
    """
    Internal tool used to compute the normal and its
    derivatives.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Contap_SurfProps) -> None: ...

    @staticmethod
    def Normale(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, U: float, V: float, P: nanoocp.gp.gp_Pnt, N: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point <P>, and normal vector <N> on
        <S> at parameters U,V.
        """

    @staticmethod
    def DerivAndNorm(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, U: float, V: float, P: nanoocp.gp.gp_Pnt, d1u: nanoocp.gp.gp_Vec, d1v: nanoocp.gp.gp_Vec, N: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point <P>, and normal vector <N> on
        <S> at parameters U,V.
        """

    @staticmethod
    def NormAndDn(S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, U: float, V: float, P: nanoocp.gp.gp_Pnt, N: nanoocp.gp.gp_Vec, Dnu: nanoocp.gp.gp_Vec, Dnv: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point <P>, normal vector <N>, and its
        derivatives <Dnu> and <Dnv> on <S> at parameters U,V.
        """

class Contap_TheIWLineOfTheIWalking(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None = None) -> None: ...

    @overload
    def __init__(self, theOther: Contap_TheIWLineOfTheIWalking) -> None: ...

    def Reverse(self) -> None:
        """reverse the points in the line. Hasfirst, HasLast are kept."""

    def Cut(self, Index: int) -> None:
        """Cut the line at the point of rank Index."""

    def AddPoint(self, P: nanoocp.IntSurf.IntSurf_PntOn2S) -> None:
        """Add a point in the line."""

    @overload
    def AddStatusFirst(self, Closed: bool, HasFirst: bool) -> None: ...

    @overload
    def AddStatusFirst(self, Closed: bool, HasLast: bool, Index: int, P: nanoocp.IntSurf.IntSurf_PathPoint) -> None: ...

    def AddStatusFirstLast(self, Closed: bool, HasFirst: bool, HasLast: bool) -> None: ...

    @overload
    def AddStatusLast(self, HasLast: bool) -> None: ...

    @overload
    def AddStatusLast(self, HasLast: bool, Index: int, P: nanoocp.IntSurf.IntSurf_PathPoint) -> None: ...

    def AddIndexPassing(self, Index: int) -> None:
        """
        associate the index of the point on the line with the index of the point
        passing through the starting iterator
        """

    def SetTangentVector(self, V: nanoocp.gp.gp_Vec, Index: int) -> None: ...

    def SetTangencyAtBegining(self, IsTangent: bool) -> None: ...

    def SetTangencyAtEnd(self, IsTangent: bool) -> None: ...

    def NbPoints(self) -> int:
        """
        Returns the number of points of the line (including first
        point and end point : see HasLastPoint and HasFirstPoint).
        """

    def Value(self, Index: int) -> nanoocp.IntSurf.IntSurf_PntOn2S:
        """
        Returns the point of range Index.
        If index <= 0 or Index > NbPoints, an exception is raised.
        """

    def Line(self) -> nanoocp.IntSurf.IntSurf_LineOn2S:
        """Returns the LineOn2S contained in the walking line."""

    def IsClosed(self) -> bool:
        """Returns True if the line is closed."""

    def HasFirstPoint(self) -> bool:
        """
        Returns True if the first point of the line is a
        marching point. when is HasFirstPoint==False ,the line
        begins on the natural bound of the surface. The line can
        be too long
        """

    def HasLastPoint(self) -> bool:
        """
        Returns True if the end point of the line is a
        marching point (Point from IntWS).
        when is HasFirstPoint==False the line ends
        on the natural bound of the surface. The line can be
        too long.
        """

    def FirstPoint(self) -> nanoocp.IntSurf.IntSurf_PathPoint:
        """
        Returns the first point of the line when it is a
        marching point.
        An exception is raised if HasFirstPoint returns False.
        """

    def FirstPointIndex(self) -> int:
        """
        Returns the Index of first point of the line when it is a
        marching point. This index is the index in the
        PointStartIterator.
        An exception is raised if HasFirstPoint returns False.
        """

    def LastPoint(self) -> nanoocp.IntSurf.IntSurf_PathPoint:
        """
        Returns the last point of the line when it is a
        marching point.
        An exception is raised if HasLastPoint returns False.
        """

    def LastPointIndex(self) -> int:
        """
        Returns the index of last point of the line when it is a
        marching point. This index is the index in the
        PointStartIterator.
        An exception is raised if HasLastPoint returns False.
        """

    def NbPassingPoint(self) -> int:
        """
        returns the number of points belonging to Pnts1 which are
        passing point.
        """

    def PassingPoint(self, Index: int) -> tuple[int, int]:
        """
        returns the index of the point belonging to the line which
        is associated to the passing point belonging to Pnts1
        an exception is raised if Index > NbPassingPoint()
        """

    def TangentVector(self) -> tuple[nanoocp.gp.gp_Vec, int]: ...

    def IsTangentAtBegining(self) -> bool: ...

    def IsTangentAtEnd(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Contap_TheIWalking:
    @overload
    def __init__(self, Epsilon: float, Deflection: float, Step: float, theToFillHoles: bool = False) -> None:
        """
        Deflection is the maximum deflection admitted between two
        consecutive points on a resulting polyline.
        Step is the maximum increment admitted between two
        consecutive points (in 2d space).
        Epsilon is the tolerance beyond which 2 points
        are confused.
        theToFillHoles is the flag defining whether possible holes
        between resulting curves are filled or not
        in case of Contap walking theToFillHoles is True
        """

    @overload
    def __init__(self, theOther: Contap_TheIWalking) -> None: ...

    def SetTolerance(self, Epsilon: float, Deflection: float, Step: float) -> None:
        """
        Deflection is the maximum deflection admitted between two
        consecutive points on a resulting polyline.
        Step is the maximum increment admitted between two
        consecutive points (in 2d space).
        Epsilon is the tolerance beyond which 2 points
        are confused
        """

    @overload
    def Perform(self, Pnts1: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntSurf.IntSurf_PathPoint], Pnts2: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntSurf.IntSurf_InteriorPoint], Func: Contap_SurfFunction, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Reversed: bool = False) -> None:
        """
        Searches a set of polylines starting on a point of Pnts1
        or Pnts2.
        Each point on a resulting polyline verifies F(u,v)=0
        """

    @overload
    def Perform(self, Pnts1: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntSurf.IntSurf_PathPoint], Func: Contap_SurfFunction, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Reversed: bool = False) -> None:
        """
        Searches a set of polylines starting on a point of Pnts1.
        Each point on a resulting polyline verifies F(u,v)=0
        """

    def IsDone(self) -> bool:
        """Returns true if the calculus was successful."""

    def NbLines(self) -> int:
        """
        Returns the number of resulting polylines.
        An exception is raised if IsDone returns False.
        """

    def Value(self, Index: int) -> Contap_TheIWLineOfTheIWalking:
        """
        Returns the polyline of range Index.
        An exception is raised if IsDone is False.
        An exception is raised if Index<=0 or Index>NbLines.
        """

    def NbSinglePnts(self) -> int:
        """
        Returns the number of points belonging to Pnts on which no
        line starts or ends.
        An exception is raised if IsDone returns False.
        """

    def SinglePnt(self, Index: int) -> nanoocp.IntSurf.IntSurf_PathPoint:
        """
        Returns the point of range Index .
        An exception is raised if IsDone returns False.
        An exception is raised if Index<=0 or
        Index > NbSinglePnts.
        """
