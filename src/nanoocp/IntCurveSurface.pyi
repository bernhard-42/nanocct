"""OCCT package IntCurveSurface (toolkit TKGeomAlgo)"""

import enum
from typing import overload

import nanoocp.Adaptor3d
import nanoocp.Bnd
import nanoocp.Geom
import nanoocp.GeomAbs
import nanoocp.IntSurf
import nanoocp.Intf
import nanoocp.NCollection
import nanoocp.gp
import nanoocp.math


class IntCurveSurface_TransitionOnCurve(enum.IntEnum):
    """
    \\ Uo     ^        \\ U1     ^
    \\       | n       \\       | n
    Surf  ====\\======|===   ====\\======|===
    \\     .           \\     .
    \\    .            \\    .
    U1  \\   .          Uo \\   .

    ( In )            ( Out )

    \\           /
    \\         /
    \\       /
    \\     /
    Surf =====-----=====

    ( Tangent )
    Crb and Surf are C1
    """

    IntCurveSurface_Tangent = 0

    IntCurveSurface_In = 1

    IntCurveSurface_Out = 2

IntCurveSurface_Tangent: IntCurveSurface_TransitionOnCurve = ...

IntCurveSurface_In: IntCurveSurface_TransitionOnCurve = ...

IntCurveSurface_Out: IntCurveSurface_TransitionOnCurve = ...

class IntCurveSurface_IntersectionPoint:
    """
    Definition of an interserction point between a
    curve and a surface.
    """

    @overload
    def __init__(self) -> None:
        """Empty Constructor."""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, USurf: float, VSurf: float, UCurv: float, TrCurv: IntCurveSurface_TransitionOnCurve) -> None:
        """Create an IntersectionPoint."""

    @overload
    def __init__(self, theOther: IntCurveSurface_IntersectionPoint) -> None: ...

    def SetValues(self, P: nanoocp.gp.gp_Pnt, USurf: float, VSurf: float, UCurv: float, TrCurv: IntCurveSurface_TransitionOnCurve) -> None:
        """Set the fields of the current IntersectionPoint."""

    def Values(self, P: nanoocp.gp.gp_Pnt) -> tuple[float, float, float, IntCurveSurface_TransitionOnCurve]:
        """Get the fields of the current IntersectionPoint."""

    def Pnt(self) -> nanoocp.gp.gp_Pnt:
        """returns the geometric point."""

    def U(self) -> float:
        """returns the U parameter on the surface."""

    def V(self) -> float:
        """returns the V parameter on the surface."""

    def W(self) -> float:
        """returns the parameter on the curve."""

    def Transition(self) -> IntCurveSurface_TransitionOnCurve:
        """returns the Transition of the point."""

    def Dump(self) -> None:
        """Dump all the fields."""

class IntCurveSurface_IntersectionSegment:
    """
    A IntersectionSegment describes a segment of curve
    (w1,w2) where distance(C(w),Surface) is less than a
    given tolerances.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, P1: IntCurveSurface_IntersectionPoint, P2: IntCurveSurface_IntersectionPoint) -> None: ...

    @overload
    def __init__(self, theOther: IntCurveSurface_IntersectionSegment) -> None: ...

    def SetValues(self, P1: IntCurveSurface_IntersectionPoint, P2: IntCurveSurface_IntersectionPoint) -> None: ...

    def Values(self, P1: IntCurveSurface_IntersectionPoint, P2: IntCurveSurface_IntersectionPoint) -> None: ...

    @overload
    def FirstPoint(self, P1: IntCurveSurface_IntersectionPoint) -> None: ...

    @overload
    def FirstPoint(self) -> IntCurveSurface_IntersectionPoint: ...

    @overload
    def SecondPoint(self, P2: IntCurveSurface_IntersectionPoint) -> None: ...

    @overload
    def SecondPoint(self) -> IntCurveSurface_IntersectionPoint: ...

    def Dump(self) -> None: ...

class IntCurveSurface_Intersection:
    def IsDone(self) -> bool:
        """returns the <done> field."""

    def NbPoints(self) -> int:
        """
        returns the number of IntersectionPoint
        if IsDone returns True.
        else NotDone is raised.
        """

    def Point(self, Index: int) -> IntCurveSurface_IntersectionPoint:
        """
        returns the IntersectionPoint of range <Index>
        raises NotDone if the computation has failed or if
        the computation has not been done
        raises OutOfRange if Index is not in the range <1..NbPoints>
        """

    def NbSegments(self) -> int:
        """
        returns the number of IntersectionSegment
        if IsDone returns True.
        else NotDone is raised.
        """

    def Segment(self, Index: int) -> IntCurveSurface_IntersectionSegment:
        """
        returns the IntersectionSegment of range <Index>
        raises NotDone if the computation has failed or if
        the computation has not been done
        raises OutOfRange if Index is not in the range <1..NbSegment>
        """

    def IsParallel(self) -> bool:
        """
        Returns true if curve is parallel or belongs surface
        This case is recognized only for some pairs
        of analytical curves and surfaces (plane - line, ...)
        """

    def Dump(self) -> None:
        """Dump all the fields."""

class IntCurveSurface_HInter(IntCurveSurface_Intersection):
    @overload
    def __init__(self) -> None:
        """Empty Constructor"""

    @overload
    def __init__(self, theOther: IntCurveSurface_HInter) -> None: ...

    @overload
    def Perform(self, Curve: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Surface: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None:
        """
        Compute the Intersection between the curve and the
        surface
        """

    @overload
    def Perform(self, Curve: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Polygon: IntCurveSurface_ThePolygonOfHInter, Surface: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None:
        """
        Compute the Intersection between the curve and
        the surface. The Curve is already sampled and
        its polygon : <Polygon> is given.
        """

    @overload
    def Perform(self, Curve: nanoocp.Adaptor3d.Adaptor3d_Curve | None, ThePolygon: IntCurveSurface_ThePolygonOfHInter, Surface: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Polyhedron: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...

    @overload
    def Perform(self, Curve: nanoocp.Adaptor3d.Adaptor3d_Curve | None, ThePolygon: IntCurveSurface_ThePolygonOfHInter, Surface: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Polyhedron: IntCurveSurface_ThePolyhedronOfHInter, BndBSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None:
        """
        Compute the Intersection between the curve and
        the surface. The Curve is already sampled and
        its polygon : <Polygon> is given. The Surface is
        also sampled and <Polyhedron> is given.
        """

    @overload
    def Perform(self, Curve: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Surface: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Polyhedron: IntCurveSurface_ThePolyhedronOfHInter) -> None:
        """
        Compute the Intersection between the curve and
        the surface. The Surface is already sampled and
        its polyhedron : <Polyhedron> is given.
        """

class IntCurveSurface_TheCSFunctionOfHInter(nanoocp.math.math_FunctionSetWithDerivatives):
    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: IntCurveSurface_TheCSFunctionOfHInter) -> None: ...

    def NbVariables(self) -> int: ...

    def NbEquations(self) -> int: ...

    def Value(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector) -> bool: ...

    def Derivatives(self, X: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool: ...

    def Values(self, X: nanoocp.math.math_Vector, F: nanoocp.math.math_Vector, D: nanoocp.math.math_Matrix) -> bool: ...

    def Point(self) -> nanoocp.gp.gp_Pnt: ...

    def Root(self) -> float: ...

    def AuxillarSurface(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    def AuxillarCurve(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

class IntCurveSurface_TheExactHInter:
    @overload
    def __init__(self, F: IntCurveSurface_TheCSFunctionOfHInter, TolTangency: float) -> None:
        """initialize the parameters to compute the solution"""

    @overload
    def __init__(self, U: float, V: float, W: float, F: IntCurveSurface_TheCSFunctionOfHInter, TolTangency: float, MarginCoef: float = 0.0) -> None:
        """
        compute the solution point with the close point
        MarginCoef is the coefficient for extension of UV bounds.
        Ex., UFirst -= MarginCoef*(ULast-UFirst)
        """

    @overload
    def __init__(self, theOther: IntCurveSurface_TheExactHInter) -> None: ...

    def Perform(self, U: float, V: float, W: float, Rsnld: nanoocp.math.math_FunctionSetRoot, u0: float, v0: float, u1: float, v1: float, w0: float, w1: float) -> None:
        """
        compute the solution
        it's possible to write to optimize:
        IntImp_IntCS inter(S1,C1,Toltangency)
        math_FunctionSetRoot rsnld(Inter.function())
        while ...{
        u=...
        v=...
        w=...
        inter.Perform(u,v,w,rsnld)
        }
        or
        IntImp_IntCS inter(Toltangency)
        inter.SetSurface(S);
        math_FunctionSetRoot rsnld(Inter.function())
        while ...{
        C=...
        inter.SetCurve(C);
        u=...
        v=...
        w=...
        inter.Perform(u,v,w,rsnld)
        }
        """

    def IsDone(self) -> bool:
        """Returns TRUE if the creation completed without failure."""

    def IsEmpty(self) -> bool: ...

    def Point(self) -> nanoocp.gp.gp_Pnt:
        """
        returns the intersection point
        The exception NotDone is raised if IsDone is false.
        The exception DomainError is raised if IsEmpty is true.
        """

    def ParameterOnCurve(self) -> float: ...

    def ParameterOnSurface(self) -> tuple[float, float]: ...

    def Function(self) -> IntCurveSurface_TheCSFunctionOfHInter:
        """
        return the math function which
        is used to compute the intersection
        """

class IntCurveSurface_TheHCurveTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntCurveSurface_TheHCurveTool) -> None: ...

    @staticmethod
    def FirstParameter(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> float: ...

    @staticmethod
    def LastParameter(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> float: ...

    @staticmethod
    def Continuity(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    @staticmethod
    def NbIntervals(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(myclass) >= <S>
        """

    @staticmethod
    def Intervals(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

    @staticmethod
    def IsClosed(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> bool: ...

    @staticmethod
    def IsPeriodic(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> bool: ...

    @staticmethod
    def Period(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> float: ...

    @staticmethod
    def Value(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U: float) -> nanoocp.gp.gp_Pnt:
        """Computes the point of parameter U on the curve."""

    @staticmethod
    def D0(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U: float, P: nanoocp.gp.gp_Pnt) -> None:
        """Computes the point of parameter U on the curve."""

    @staticmethod
    def D1(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U: float, P: nanoocp.gp.gp_Pnt, V: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point of parameter U on the curve with its
        first derivative.
        Raised if the continuity of the current interval
        is not C1.
        """

    @staticmethod
    def D2(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the point P of parameter U, the first and second
        derivatives V1 and V2.
        Raised if the continuity of the current interval
        is not C2.
        """

    @staticmethod
    def D3(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec, V3: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the point P of parameter U, the first, the second
        and the third derivative.
        Raised if the continuity of the current interval
        is not C3.
        """

    @staticmethod
    def DN(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U: float, N: int) -> nanoocp.gp.gp_Vec:
        """
        The returned vector gives the value of the derivative for the
        order of derivation N.
        Raised if the continuity of the current interval
        is not CN.
        Raised if N < 1.
        """

    @staticmethod
    def Resolution(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, R3d: float) -> float:
        """
        Returns the parametric resolution corresponding
        to the real space resolution <R3d>.
        """

    @staticmethod
    def GetType(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """
        Returns the type of the curve in the current
        interval: Line, Circle, Ellipse, Hyperbola,
        Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """

    @staticmethod
    def Line(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.gp.gp_Lin: ...

    @staticmethod
    def Circle(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.gp.gp_Circ: ...

    @staticmethod
    def Ellipse(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.gp.gp_Elips: ...

    @staticmethod
    def Hyperbola(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.gp.gp_Hypr: ...

    @staticmethod
    def Parabola(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.gp.gp_Parab: ...

    @staticmethod
    def Bezier(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.Geom.Geom_BezierCurve: ...

    @staticmethod
    def BSpline(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> nanoocp.Geom.Geom_BSplineCurve: ...

    @staticmethod
    def NbSamples(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U0: float, U1: float) -> int: ...

    @overload
    @staticmethod
    def SamplePars(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U0: float, U1: float, Defl: float, NbMin: int) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns sample parameters for the curve within [U0, U1] range,
        computed based on deflection and minimum number of points.
        @param[in] C the curve adaptor
        @param[in] U0 start parameter
        @param[in] U1 end parameter
        @param[in] Defl deflection tolerance
        @param[in] NbMin minimum number of sample points
        @return array of sample parameter values
        """

    @overload
    @staticmethod
    def SamplePars(C: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U0: float, U1: float, Defl: float, NbMin: int) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Deprecated in OCCT: Use SamplePars() returning handle by value instead

        @deprecated Use SamplePars() returning handle by value instead.
        """

class IntCurveSurface_TheInterferenceOfHInter(nanoocp.Intf.Intf_Interference):
    @overload
    def __init__(self) -> None:
        """
        Constructs an empty interference between Polygon and
        Polyhedron.
        """

    @overload
    def __init__(self, thePolyg: IntCurveSurface_ThePolygonOfHInter, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...

    @overload
    def __init__(self, theLin: nanoocp.gp.gp_Lin, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...

    @overload
    def __init__(self, theLins: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Lin], thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...

    @overload
    def __init__(self, thePolyg: IntCurveSurface_ThePolygonOfHInter, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, theBoundSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None:
        """
        Constructs and computes an interference between the Polygon
        and the Polyhedron.
        """

    @overload
    def __init__(self, theLin: nanoocp.gp.gp_Lin, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, theBoundSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None:
        """
        Constructs and computes an interference between the
        Straight Line and the Polyhedron.
        """

    @overload
    def __init__(self, theLins: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Lin], thePolyh: IntCurveSurface_ThePolyhedronOfHInter, theBoundSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None:
        """
        Constructs and computes an interference between the
        Straight Lines and the Polyhedron.
        """

    @overload
    def __init__(self, theOther: IntCurveSurface_TheInterferenceOfHInter) -> None: ...

    @overload
    def Perform(self, thePolyg: IntCurveSurface_ThePolygonOfHInter, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...

    @overload
    def Perform(self, theLin: nanoocp.gp.gp_Lin, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...

    @overload
    def Perform(self, theLins: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Lin], thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...

    @overload
    def Perform(self, thePolyg: IntCurveSurface_ThePolygonOfHInter, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, theBoundSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None:
        """
        Computes an interference between the Polygon and the
        Polyhedron.
        """

    @overload
    def Perform(self, theLin: nanoocp.gp.gp_Lin, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, theBoundSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None:
        """
        Computes an interference between the Straight Line and the
        Polyhedron.
        """

    @overload
    def Perform(self, theLins: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Lin], thePolyh: IntCurveSurface_ThePolyhedronOfHInter, theBoundSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None:
        """
        Computes an interference between the Straight Lines and
        the Polyhedron.
        """

    @overload
    def Interference(self, thePolyg: IntCurveSurface_ThePolygonOfHInter, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, theBoundSB: nanoocp.Bnd.Bnd_BoundSortBox) -> None: ...

    @overload
    def Interference(self, thePolyg: IntCurveSurface_ThePolygonOfHInter, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None:
        """
        Compares the boundings between the segment of <thePolyg> and
        the facets of <thePolyh>.
        """

class IntCurveSurface_ThePolygonOfHInter:
    @overload
    def __init__(self, Curve: nanoocp.Adaptor3d.Adaptor3d_Curve | None, NbPnt: int) -> None: ...

    @overload
    def __init__(self, Curve: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Upars: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def __init__(self, Curve: nanoocp.Adaptor3d.Adaptor3d_Curve | None, U1: float, U2: float, NbPnt: int) -> None: ...

    @overload
    def __init__(self, theOther: IntCurveSurface_ThePolygonOfHInter) -> None: ...

    def Bounding(self) -> nanoocp.Bnd.Bnd_Box:
        """Give the bounding box of the polygon."""

    def DeflectionOverEstimation(self) -> float: ...

    def SetDeflectionOverEstimation(self, x: float) -> None: ...

    @overload
    def Closed(self, flag: bool) -> None: ...

    @overload
    def Closed(self) -> bool: ...

    def NbSegments(self) -> int:
        """Give the number of Segments in the polyline."""

    def BeginOfSeg(self, theIndex: int) -> nanoocp.gp.gp_Pnt:
        """Give the point of range Index in the Polygon."""

    def EndOfSeg(self, theIndex: int) -> nanoocp.gp.gp_Pnt:
        """Give the point of range Index in the Polygon."""

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

    def ApproxParamOnCurve(self, Index: int, ParamOnLine: float) -> float:
        """
        Give an approximation of the parameter on the curve
        according to the discretization of the Curve.
        """

    def Dump(self) -> None: ...

class IntCurveSurface_ThePolygonToolOfHInter:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntCurveSurface_ThePolygonToolOfHInter) -> None: ...

    @staticmethod
    def Bounding(thePolygon: IntCurveSurface_ThePolygonOfHInter) -> nanoocp.Bnd.Bnd_Box:
        """Give the bounding box of the polygon."""

    @staticmethod
    def DeflectionOverEstimation(thePolygon: IntCurveSurface_ThePolygonOfHInter) -> float: ...

    @staticmethod
    def Closed(thePolygon: IntCurveSurface_ThePolygonOfHInter) -> bool: ...

    @staticmethod
    def NbSegments(thePolygon: IntCurveSurface_ThePolygonOfHInter) -> int: ...

    @staticmethod
    def BeginOfSeg(thePolygon: IntCurveSurface_ThePolygonOfHInter, Index: int) -> nanoocp.gp.gp_Pnt:
        """Give the point of range Index in the Polygon."""

    @staticmethod
    def EndOfSeg(thePolygon: IntCurveSurface_ThePolygonOfHInter, Index: int) -> nanoocp.gp.gp_Pnt:
        """Give the point of range Index in the Polygon."""

    @staticmethod
    def Dump(thePolygon: IntCurveSurface_ThePolygonOfHInter) -> None: ...

class IntCurveSurface_ThePolyhedronOfHInter:
    @overload
    def __init__(self, Surface: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Upars: nanoocp.NCollection.NCollection_Array1[float], Vpars: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def __init__(self, Surface: nanoocp.Adaptor3d.Adaptor3d_Surface | None, nbdU: int, nbdV: int, U1: float, V1: float, U2: float, V2: float) -> None: ...

    @overload
    def __init__(self, theOther: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...

    def Destroy(self) -> None: ...

    @overload
    def DeflectionOverEstimation(self, flec: float) -> None: ...

    @overload
    def DeflectionOverEstimation(self) -> float: ...

    def UMinSingularity(self, Sing: bool) -> None: ...

    def UMaxSingularity(self, Sing: bool) -> None: ...

    def VMinSingularity(self, Sing: bool) -> None: ...

    def VMaxSingularity(self, Sing: bool) -> None: ...

    def Size(self) -> tuple[int, int]:
        """get the size of the discretization."""

    def NbTriangles(self) -> int:
        """Give the number of triangles in this double array of"""

    def Triangle(self, Index: int) -> tuple[int, int, int]:
        """
        Give the 3 points of the triangle of address Index in
        the double array of triangles.
        """

    def TriConnex(self, Triang: int, Pivot: int, Pedge: int) -> tuple[int, int, int]:
        """
        Give the address Tricon of the triangle connexe to the
        triangle of address Triang by the edge Pivot Pedge and
        the third point of this connexe triangle. When we are
        on a free edge TriCon==0 but the function return the
        value of the triangle in the other side of Pivot on
        the free edge. Used to turn around a vertex.
        """

    def NbPoints(self) -> int:
        """
        Give the number of point in the double array of
        triangles ((nbdu+1)*(nbdv+1)).
        """

    @overload
    def Point(self, thePnt: nanoocp.gp.gp_Pnt, lig: int, col: int, U: float, V: float) -> None:
        """
        Set the value of a field of the double array of
        points.
        """

    @overload
    def Point(self, Index: int) -> tuple[nanoocp.gp.gp_Pnt, float, float]: ...

    @overload
    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt: ...

    @overload
    def Point(self, Index: int, P: nanoocp.gp.gp_Pnt) -> None:
        """Give the point of index i in the MaTriangle."""

    def Bounding(self) -> nanoocp.Bnd.Bnd_Box:
        """Give the bounding box of the MaTriangle."""

    def FillBounding(self) -> None:
        """
        Compute the array of boxes. The box <n> corresponding
        to the triangle <n>.
        """

    def ComponentsBounding(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Bnd.Bnd_Box]:
        """
        Give the array of boxes. The box <n> corresponding
        to the triangle <n>.
        """

    def HasUMinSingularity(self) -> bool: ...

    def HasUMaxSingularity(self) -> bool: ...

    def HasVMinSingularity(self) -> bool: ...

    def HasVMaxSingularity(self) -> bool: ...

    def PlaneEquation(self, Triang: int, NormalVector: nanoocp.gp.gp_XYZ) -> float:
        """Give the plane equation of the triangle of address Triang."""

    def Contain(self, Triang: int, ThePnt: nanoocp.gp.gp_Pnt) -> bool:
        """Give the plane equation of the triangle of address Triang."""

    def Parameters(self, Index: int) -> tuple[float, float]: ...

    def IsOnBound(self, Index1: int, Index2: int) -> bool:
        """
        This method returns true if the edge based on points with
        indices Index1 and Index2 represents a boundary edge. It is
        necessary to take into account the boundary deflection for
        this edge.
        """

    def GetBorderDeflection(self) -> float:
        """This method returns a border deflection."""

    def Dump(self) -> None: ...

class IntCurveSurface_ThePolyhedronToolOfHInter:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntCurveSurface_ThePolyhedronToolOfHInter) -> None: ...

    @staticmethod
    def Bounding(thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> nanoocp.Bnd.Bnd_Box:
        """Give the bounding box of the PolyhedronTool."""

    @staticmethod
    def ComponentsBounding(thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Bnd.Bnd_Box]:
        """
        Give the array of boxes. The box <n> corresponding
        to the triangle <n>.
        """

    @staticmethod
    def DeflectionOverEstimation(thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> float:
        """Give the tolerance of the polygon."""

    @staticmethod
    def NbTriangles(thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> int:
        """Give the number of triangles in this polyhedral surface."""

    @staticmethod
    def Triangle(thePolyh: IntCurveSurface_ThePolyhedronOfHInter, Index: int) -> tuple[int, int, int]:
        """
        Give the indices of the 3 points of the triangle of
        address Index in the PolyhedronTool.
        """

    @staticmethod
    def Point(thePolyh: IntCurveSurface_ThePolyhedronOfHInter, Index: int) -> nanoocp.gp.gp_Pnt:
        """Give the point of index i in the polyhedral surface."""

    @staticmethod
    def TriConnex(thePolyh: IntCurveSurface_ThePolyhedronOfHInter, Triang: int, Pivot: int, Pedge: int) -> tuple[int, int, int]:
        """
        Give the address Tricon of the triangle connexe to
        the triangle of address Triang by the edge Pivot Pedge
        and the third point of this connexe triangle. When we
        are on a free edge TriCon==0 but the function return
        the value of the triangle in the other side of Pivot
        on the free edge. Used to turn around a vertex.
        """

    @staticmethod
    def IsOnBound(thePolyh: IntCurveSurface_ThePolyhedronOfHInter, Index1: int, Index2: int) -> bool:
        """
        This method returns true if the edge based on points with
        indices Index1 and Index2 represents a boundary edge. It is
        necessary to take into account the boundary deflection for
        this edge.
        """

    @staticmethod
    def GetBorderDeflection(thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> float:
        """This method returns a border deflection of the polyhedron."""

    @staticmethod
    def Dump(thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...

class IntCurveSurface_TheQuadCurvExactHInter:
    @overload
    def __init__(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None:
        """
        Provides the signed distance function : Q(w)
        and its first derivative dQ(w)/dw
        """

    @overload
    def __init__(self, theOther: IntCurveSurface_TheQuadCurvExactHInter) -> None: ...

    def IsDone(self) -> bool: ...

    def NbRoots(self) -> int: ...

    def Root(self, Index: int) -> float: ...

    def NbIntervals(self) -> int: ...

    def Intervals(self, Index: int) -> tuple[float, float]:
        """
        U1 and U2 are the parameters of
        a segment on the curve.
        """

class IntCurveSurface_TheQuadCurvFuncOfTheQuadCurvExactHInter(nanoocp.math.math_FunctionWithDerivative):
    @overload
    def __init__(self, Q: nanoocp.IntSurf.IntSurf_Quadric, C: nanoocp.Adaptor3d.Adaptor3d_Curve | None) -> None:
        """Create the function."""

    @overload
    def __init__(self, theOther: IntCurveSurface_TheQuadCurvFuncOfTheQuadCurvExactHInter) -> None: ...

    def Value(self, Param: float) -> tuple[bool, float]:
        """
        Computes the value of the signed distance between
        the implicit surface and the point at parameter
        Param on the parametrised curve.
        Value always returns True.
        """

    def Derivative(self, Param: float) -> tuple[bool, float]:
        """
        Computes the derivative of the previous function at
        parameter Param.
        Derivative always returns True.
        """

    def Values(self, Param: float) -> tuple[bool, float, float]:
        """
        Computes the value and the derivative of the function.
        returns True.
        """
