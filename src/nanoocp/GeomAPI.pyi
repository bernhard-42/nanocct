"""OCCT package GeomAPI (toolkit TKGeomAlgo)"""

from typing import overload

import nanoocp.Approx
import nanoocp.Extrema
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.gp


class GeomAPI:
    """
    The GeomAPI package provides an Application
    Programming Interface for the Geometry.

    The API is a set of classes and methods aiming to
    provide :

    * High level and simple calls for the most common
    operations.

    * Keeping an access on the low-level
    implementation of high-level calls.

    The API provides classes to call the algorithms
    of the Geometry

    * The constructors of the classes provides the
    different constructions methods.

    * The class keeps as fields the different tools
    used by the algorithms

    * The class provides a casting method to get
    automatically the result with a function-like
    call.

    For example to evaluate the distance <D> between a
    point <P> and a curve <C>, one can writes :

    D = GeomAPI_ProjectPointOnCurve(P,C);

    or

    GeomAPI_ProjectPointOnCurve PonC(P,C);
    D = PonC.LowerDistance();
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomAPI) -> None: ...

    @staticmethod
    def To2d(C: nanoocp.Geom.Geom_Curve | None, P: nanoocp.gp.gp_Pln) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        This function builds (in the
        parametric space of the plane P) a 2D curve equivalent to the 3D curve
        C. The 3D curve C is considered to be located in the plane P.
        Warning
        The 3D curve C must be of one of the following types:
        -      a line
        -      a circle
        -      an ellipse
        -      a hyperbola
        -      a parabola
        -      a Bezier curve
        -      a BSpline curve
        Exceptions Standard_NoSuchObject if C is not a defined type curve.
        """

    @staticmethod
    def To3d(C: nanoocp.Geom2d.Geom2d_Curve | None, P: nanoocp.gp.gp_Pln) -> nanoocp.Geom.Geom_Curve:
        """
        Builds a 3D curve equivalent to the 2D curve C
        described in the parametric space defined by the local
        coordinate system of plane P.
        The resulting 3D curve is of the same nature as that of the curve C.
        """

class GeomAPI_ExtremaCurveCurve:
    """
    Describes functions for computing all the extrema
    between two 3D curves.
    An ExtremaCurveCurve algorithm minimizes or
    maximizes the distance between a point on the first
    curve and a point on the second curve. Thus, it
    computes start and end points of perpendiculars
    common to the two curves (an intersection point is
    not an extremum unless the two curves are tangential at this point).
    Solutions consist of pairs of points, and an extremum
    is considered to be a segment joining the two points of a solution.
    An ExtremaCurveCurve object provides a framework for:
    -   defining the construction of the extrema,
    -   implementing the construction algorithm, and
    -   consulting the results.
    Warning
    In some cases, the nearest points between two
    curves do not correspond to one of the computed
    extrema. Instead, they may be given by:
    -   a limit point of one curve and one of the following:
    -   its orthogonal projection on the other curve,
    -   a limit point of the other curve; or
    -   an intersection point between the two curves.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty algorithm for computing
        extrema between two curves. Use an Init function
        to define the curves on which it is going to work.
        """

    @overload
    def __init__(self, C1: nanoocp.Geom.Geom_Curve | None, C2: nanoocp.Geom.Geom_Curve | None) -> None:
        """Computes the extrema between the curves C1 and C2."""

    @overload
    def __init__(self, C1: nanoocp.Geom.Geom_Curve | None, C2: nanoocp.Geom.Geom_Curve | None, U1min: float, U1max: float, U2min: float, U2max: float) -> None:
        """
        Computes the portion of the curve C1 limited by the two
        points of parameter (U1min,U1max), and
        -   the portion of the curve C2 limited by the two
        points of parameter (U2min,U2max).
        Warning
        Use the function NbExtrema to obtain the number
        of solutions. If this algorithm fails, NbExtrema returns 0.
        """

    @overload
    def Init(self, C1: nanoocp.Geom.Geom_Curve | None, C2: nanoocp.Geom.Geom_Curve | None) -> None:
        """
        Initializes this algorithm with the given arguments
        and computes the extrema between the curves C1 and C2
        """

    @overload
    def Init(self, C1: nanoocp.Geom.Geom_Curve | None, C2: nanoocp.Geom.Geom_Curve | None, U1min: float, U1max: float, U2min: float, U2max: float) -> None:
        """
        Initializes this algorithm with the given arguments
        and computes the extrema between :
        -   the portion of the curve C1 limited by the two
        points of parameter (U1min,U1max), and
        -   the portion of the curve C2 limited by the two
        points of parameter (U2min,U2max).
        Warning
        Use the function NbExtrema to obtain the number
        of solutions. If this algorithm fails, NbExtrema returns 0.
        """

    def NbExtrema(self) -> int:
        """
        Returns the number of extrema computed by this algorithm.
        Note: if this algorithm fails, NbExtrema returns 0.
        """

    def Points(self, Index: int, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None:
        """
        Returns the points P1 on the first curve and P2 on
        the second curve, which are the ends of the
        extremum of index Index computed by this algorithm.
        Exceptions
        Standard_OutOfRange if Index is not in the range [
        1,NbExtrema ], where NbExtrema is the
        number of extrema computed by this algorithm.
        """

    def Parameters(self, Index: int) -> tuple[float, float]:
        """
        Returns the parameters U1 of the point on the first
        curve and U2 of the point on the second curve, which
        are the ends of the extremum of index Index computed by this algorithm.
        Exceptions
        Standard_OutOfRange if Index is not in the range [
        1,NbExtrema ], where NbExtrema is the
        number of extrema computed by this algorithm.
        """

    def Distance(self, Index: int) -> float:
        """
        Computes the distance between the end points of the
        extremum of index Index computed by this algorithm.
        Exceptions
        Standard_OutOfRange if Index is not in the range [
        1,NbExtrema ], where NbExtrema is the
        number of extrema computed by this algorithm.
        """

    def IsParallel(self) -> bool:
        """Returns True if the two curves are parallel."""

    def NearestPoints(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None:
        """
        Returns the points P1 on the first curve and P2 on
        the second curve, which are the ends of the shortest
        extremum computed by this algorithm.
        Exceptions StdFail_NotDone if this algorithm fails.
        """

    def LowerDistanceParameters(self) -> tuple[float, float]:
        """
        Returns the parameters U1 of the point on the first
        curve and U2 of the point on the second curve, which
        are the ends of the shortest extremum computed by this algorithm.
        Exceptions StdFail_NotDone if this algorithm fails.
        """

    def LowerDistance(self) -> float:
        """
        Computes the distance between the end points of the
        shortest extremum computed by this algorithm.
        Exceptions StdFail_NotDone if this algorithm fails.
        """

    def Extrema(self) -> nanoocp.Extrema.Extrema_ExtCC:
        """return the algorithmic object from Extrema"""

    def TotalNearestPoints(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> bool:
        """
        set in <P1> and <P2> the couple solution points
        such a the distance [P1,P2] is the minimum. taking in account
        extremity points of curves.
        """

    def TotalLowerDistanceParameters(self) -> tuple[bool, float, float]:
        """
        set in <U1> and <U2> the parameters of the couple
        solution points which represents the total nearest
        solution.
        """

    def TotalLowerDistance(self) -> float:
        """
        return the distance of the total nearest couple solution
        point.
        if <myExtCC> is not done
        """

    def __int__(self) -> int: ...

    def __float__(self) -> float: ...

class GeomAPI_ExtremaCurveSurface:
    """
    Describes functions for computing all the extrema
    between a curve and a surface.
    An ExtremaCurveSurface algorithm minimizes or
    maximizes the distance between a point on the curve
    and a point on the surface. Thus, it computes start
    and end points of perpendiculars common to the
    curve and the surface (an intersection point is not an
    extremum except where the curve and the surface
    are tangential at this point).
    Solutions consist of pairs of points, and an extremum
    is considered to be a segment joining the two points of a solution.
    An ExtremaCurveSurface object provides a framework for:
    -   defining the construction of the extrema,
    -   implementing the construction algorithm, and
    -   consulting the results.
    Warning
    In some cases, the nearest points between a curve
    and a surface do not correspond to one of the
    computed extrema. Instead, they may be given by:
    -   a point of a bounding curve of the surface and one of the following:
    -   its orthogonal projection on the curve,
    -   a limit point of the curve; or
    -   a limit point of the curve and its projection on the surface; or
    -   an intersection point between the curve and the surface.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty algorithm for computing
        extrema between a curve and a surface. Use an
        Init function to define the curve and the surface on
        which it is going to work.
        """

    @overload
    def __init__(self, Curve: nanoocp.Geom.Geom_Curve | None, Surface: nanoocp.Geom.Geom_Surface | None) -> None:
        """
        Computes the extrema distances between the
        curve <C> and the surface <S>.
        """

    @overload
    def __init__(self, Curve: nanoocp.Geom.Geom_Curve | None, Surface: nanoocp.Geom.Geom_Surface | None, Wmin: float, Wmax: float, Umin: float, Umax: float, Vmin: float, Vmax: float) -> None:
        """
        Computes the extrema distances between the
        curve <C> and the surface <S>. The solution
        point are computed in the domain [Wmin,Wmax] of
        the curve and in the domain [Umin,Umax]
        [Vmin,Vmax] of the surface.
        Warning
        Use the function NbExtrema to obtain the number
        of solutions. If this algorithm fails, NbExtrema returns 0.
        """

    @overload
    def Init(self, Curve: nanoocp.Geom.Geom_Curve | None, Surface: nanoocp.Geom.Geom_Surface | None) -> None:
        """
        Computes the extrema distances between the
        curve <C> and the surface <S>.
        """

    @overload
    def Init(self, Curve: nanoocp.Geom.Geom_Curve | None, Surface: nanoocp.Geom.Geom_Surface | None, Wmin: float, Wmax: float, Umin: float, Umax: float, Vmin: float, Vmax: float) -> None:
        """
        Computes the extrema distances between the
        curve <C> and the surface <S>. The solution
        point are computed in the domain [Wmin,Wmax] of
        the curve and in the domain [Umin,Umax]
        [Vmin,Vmax] of the surface.
        Warning
        Use the function NbExtrema to obtain the number
        of solutions. If this algorithm fails, NbExtrema returns 0.
        """

    def NbExtrema(self) -> int:
        """
        Returns the number of extrema computed by this algorithm.
        Note: if this algorithm fails, NbExtrema returns 0.
        """

    def Points(self, Index: int, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None:
        """
        Returns the points P1 on the curve and P2 on the
        surface, which are the ends of the extremum of index
        Index computed by this algorithm.
        Exceptions
        Standard_OutOfRange if Index is not in the range [
        1,NbExtrema ], where NbExtrema is the
        number of extrema computed by this algorithm.
        """

    def Parameters(self, Index: int) -> tuple[float, float, float]:
        """
        Returns the parameters W of the point on the curve,
        and (U,V) of the point on the surface, which are the
        ends of the extremum of index Index computed by this algorithm.
        Exceptions
        Standard_OutOfRange if Index is not in the range [
        1,NbExtrema ], where NbExtrema is the
        number of extrema computed by this algorithm.
        """

    def Distance(self, Index: int) -> float:
        """
        Computes the distance between the end points of the
        extremum of index Index computed by this algorithm.
        Exceptions
        Standard_OutOfRange if index is not in the range [
        1,NbExtrema ], where NbExtrema is the
        number of extrema computed by this algorithm.
        """

    def IsParallel(self) -> bool:
        """Returns True if the curve is on a parallel surface."""

    def NearestPoints(self, PC: nanoocp.gp.gp_Pnt, PS: nanoocp.gp.gp_Pnt) -> None:
        """
        Returns the points PC on the curve and PS on the
        surface, which are the ends of the shortest extremum computed by this algorithm.
        Exceptions - StdFail_NotDone if this algorithm fails.
        """

    def LowerDistanceParameters(self) -> tuple[float, float, float]:
        """
        Returns the parameters W of the point on the curve
        and (U,V) of the point on the surface, which are the
        ends of the shortest extremum computed by this algorithm.
        Exceptions - StdFail_NotDone if this algorithm fails.
        """

    def LowerDistance(self) -> float:
        """
        Computes the distance between the end points of the
        shortest extremum computed by this algorithm.
        Exceptions - StdFail_NotDone if this algorithm fails.
        """

    def Extrema(self) -> nanoocp.Extrema.Extrema_ExtCS:
        """Returns the algorithmic object from Extrema"""

    def __int__(self) -> int: ...

    def __float__(self) -> float: ...

class GeomAPI_ExtremaSurfaceSurface:
    """
    Describes functions for computing all the extrema
    between two surfaces.
    An ExtremaSurfaceSurface algorithm minimizes or
    maximizes the distance between a point on the first
    surface and a point on the second surface. Results
    are start and end points of perpendiculars common to the two surfaces.
    Solutions consist of pairs of points, and an extremum
    is considered to be a segment joining the two points of a solution.
    An ExtremaSurfaceSurface object provides a framework for:
    -   defining the construction of the extrema,
    -   implementing the construction algorithm, and
    -   consulting the results.
    Warning
    In some cases, the nearest points between the two
    surfaces do not correspond to one of the computed
    extrema. Instead, they may be given by:
    -   a point of a bounding curve of one surface and one of the following:
    -   its orthogonal projection on the other surface,
    -   a point of a bounding curve of the other surface; or
    -   any point on intersection curves between the two surfaces.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty algorithm for computing
        extrema between two surfaces. Use an Init function
        to define the surfaces on which it is going to work.
        """

    @overload
    def __init__(self, S1: nanoocp.Geom.Geom_Surface | None, S2: nanoocp.Geom.Geom_Surface | None) -> None:
        """
        Computes the extrema distances between the
        surfaces <S1> and <S2>
        """

    @overload
    def __init__(self, S1: nanoocp.Geom.Geom_Surface | None, S2: nanoocp.Geom.Geom_Surface | None, U1min: float, U1max: float, V1min: float, V1max: float, U2min: float, U2max: float, V2min: float, V2max: float) -> None:
        """
        Computes the extrema distances between
        the portion of the surface S1 limited by the
        two values of parameter (U1min,U1max) in
        the u parametric direction, and by the two
        values of parameter (V1min,V1max) in the v
        parametric direction, and
        -   the portion of the surface S2 limited by the
        two values of parameter (U2min,U2max) in
        the u parametric direction, and by the two
        values of parameter (V2min,V2max) in the v
        parametric direction.
        """

    @overload
    def __init__(self, theOther: GeomAPI_ExtremaSurfaceSurface) -> None: ...

    @overload
    def Init(self, S1: nanoocp.Geom.Geom_Surface | None, S2: nanoocp.Geom.Geom_Surface | None) -> None:
        """
        Initializes this algorithm with the given arguments
        and computes the extrema distances between the
        surfaces <S1> and <S2>
        """

    @overload
    def Init(self, S1: nanoocp.Geom.Geom_Surface | None, S2: nanoocp.Geom.Geom_Surface | None, U1min: float, U1max: float, V1min: float, V1max: float, U2min: float, U2max: float, V2min: float, V2max: float) -> None:
        """
        Initializes this algorithm with the given arguments
        and computes the extrema distances between -
        the portion of the surface S1 limited by the two
        values of parameter (U1min,U1max) in the u
        parametric direction, and by the two values of
        parameter (V1min,V1max) in the v parametric direction, and
        -   the portion of the surface S2 limited by the two
        values of parameter (U2min,U2max) in the u
        parametric direction, and by the two values of
        parameter (V2min,V2max) in the v parametric direction.
        """

    def NbExtrema(self) -> int:
        """
        Returns the number of extrema computed by this algorithm.
        Note: if this algorithm fails, NbExtrema returns 0.
        """

    def Points(self, Index: int, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None:
        """
        Returns the points P1 on the first surface and P2 on
        the second surface, which are the ends of the
        extremum of index Index computed by this algorithm.
        Exceptions
        Standard_OutOfRange if Index is not in the range [
        1,NbExtrema ], where NbExtrema is the
        number of extrema computed by this algorithm.
        """

    def Parameters(self, Index: int) -> tuple[float, float, float, float]:
        """
        Returns the parameters (U1,V1) of the point on the
        first surface, and (U2,V2) of the point on the second
        surface, which are the ends of the extremum of index
        Index computed by this algorithm.
        Exceptions
        Standard_OutOfRange if Index is not in the range [
        1,NbExtrema ], where NbExtrema is the
        number of extrema computed by this algorithm.
        """

    def Distance(self, Index: int) -> float:
        """
        Computes the distance between the end points of the
        extremum of index Index computed by this algorithm.
        Exceptions
        Standard_OutOfRange if Index is not in the range [
        1,NbExtrema ], where NbExtrema is the
        number of extrema computed by this algorithm.
        """

    def IsParallel(self) -> bool:
        """Returns True if the surfaces are parallel"""

    def NearestPoints(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None:
        """
        Returns the points P1 on the first surface and P2 on
        the second surface, which are the ends of the
        shortest extremum computed by this algorithm.
        Exceptions StdFail_NotDone if this algorithm fails.
        """

    def LowerDistanceParameters(self) -> tuple[float, float, float, float]:
        """
        Returns the parameters (U1,V1) of the point on the
        first surface and (U2,V2) of the point on the second
        surface, which are the ends of the shortest extremum
        computed by this algorithm.
        Exceptions - StdFail_NotDone if this algorithm fails.
        """

    def LowerDistance(self) -> float:
        """
        Computes the distance between the end points of the
        shortest extremum computed by this algorithm.
        Exceptions StdFail_NotDone if this algorithm fails.
        """

    def Extrema(self) -> nanoocp.Extrema.Extrema_ExtSS:
        """return the algorithmic object from Extrema"""

    def __int__(self) -> int: ...

    def __float__(self) -> float: ...

class GeomAPI_IntCS:
    """
    This class implements methods for
    computing intersection points and segments between a
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an empty object. Use the
        function Perform for further initialization of the algorithm by
        the curve and the surface.
        """

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_Curve | None, S: nanoocp.Geom.Geom_Surface | None) -> None:
        """
        Computes the intersections between
        the curve C and the surface S.
        Warning
        Use function IsDone to verify that the intersections are computed successfully.
        """

    @overload
    def __init__(self, theOther: GeomAPI_IntCS) -> None: ...

    def Perform(self, C: nanoocp.Geom.Geom_Curve | None, S: nanoocp.Geom.Geom_Surface | None) -> None:
        """
        This function Initializes an algorithm with the curve C and the
        surface S and computes the intersections between C and S.
        Warning
        Use function IsDone to verify that the intersections are computed successfully.
        """

    def IsDone(self) -> bool:
        """Returns true if the intersections are successfully computed."""

    def NbPoints(self) -> int:
        """
        Returns the number of Intersection Points
        if IsDone returns True.
        else NotDone is raised.
        """

    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        Returns the Intersection Point of range <Index>in case of cross intersection.
        Raises NotDone if the computation has failed or if
        the computation has not been done
        raises OutOfRange if Index is not in the range <1..NbPoints>
        """

    def Parameters__float_float_float(self, Index: int) -> tuple[float, float, float]:
        """
        Parameters__float_float_float: the C++ overload Parameters(const int, double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns parameter W on the curve
        and (parameters U,V) on the surface of the computed intersection point
        of index Index in case of cross intersection.
        Exceptions
        StdFail_NotDone if intersection algorithm fails or is not initialized.
        Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where
        NbPoints is the number of computed intersection points.
        """

    def NbSegments(self) -> int:
        """
        Returns the number of computed
        intersection segments in case of tangential intersection.
        Exceptions
        StdFail_NotDone if the intersection algorithm fails or is not initialized.
        """

    def Segment(self, Index: int) -> nanoocp.Geom.Geom_Curve:
        """
        Returns the computed intersection
        segment of index Index in case of tangential intersection.
        Intersection segment is a portion of the initial curve tangent to surface.
        Exceptions
        StdFail_NotDone if intersection algorithm fails or is not initialized.
        Standard_OutOfRange if Index is not in the range [ 1,NbSegments ],
        where NbSegments is the number of computed intersection segments.
        """

    def Parameters__float_float_float_float(self, Index: int) -> tuple[float, float, float, float]:
        """
        Parameters__float_float_float_float: the C++ overload Parameters(const int, double &, double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns the parameters of the first (U1,V1) and the last (U2,V2) points
        of curve's segment on the surface in case of tangential intersection.
        Index is the number of computed intersection segments.
        Exceptions
        StdFail_NotDone if intersection algorithm fails or is not initialized.
        Standard_OutOfRange if Index is not in the range [ 1,NbSegments ],
        where NbSegments is the number of computed intersection segments.
        """

class GeomAPI_Interpolate:
    """
    This class is used to interpolate a BsplineCurve
    passing through an array of points, with a C2
    Continuity if tangency is not requested at the point.
    If tangency is requested at the point the continuity will
    be C1. If Perodicity is requested the curve will be closed
    and the junction will be the first point given. The curve
    will than be only C1
    Describes functions for building a constrained 3D BSpline curve.
    The curve is defined by a table of points
    through which it passes, and if required:
    -   by a parallel table of reals which gives the
    value of the parameter of each point through
    which the resulting BSpline curve passes, and
    -   by vectors tangential to these points.
    An Interpolate object provides a framework for:
    -   defining the constraints of the BSpline curve,
    -   implementing the interpolation algorithm, and
    -   consulting the results.
    """

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt] | None, PeriodicFlag: bool, Tolerance: float) -> None:
        """
        Initializes an algorithm for constructing a
        constrained BSpline curve passing through the points of the table Points.
        Tangential vectors can then be assigned, using the function Load.
        If PeriodicFlag is true, the constrained BSpline
        curve will be periodic and closed. In this case,
        the junction point is the first point of the table Points.
        The tolerance value Tolerance is used to check that:
        -   points are not too close to each other, or
        -   tangential vectors (defined using the
        function Load) are not too small.
        The resulting BSpline curve will be "C2"
        continuous, except where a tangency
        constraint is defined on a point through which
        the curve passes (by using the Load function).
        In this case, it will be only "C1" continuous.
        Once all the constraints are defined, use the
        function Perform to compute the curve.
        Warning
        -   There must be at least 2 points in the table Points.
        -   If PeriodicFlag is false, there must be as
        many parameters in the array Parameters as
        there are points in the array Points.
        -   If PeriodicFlag is true, there must be one
        more parameter in the table Parameters: this
        is used to give the parameter on the
        resulting BSpline curve of the junction point
        of the curve (which is also the first point of the table Points).
        Exceptions
        -   Standard_ConstructionError if the
        distance between two consecutive points in
        the table Points is less than or equal to Tolerance.
        -   Standard_OutOfRange if:
        -   there are less than two points in the table Points, or
        -   conditions relating to the respective
        number of elements in the parallel tables
        Points and Parameters are not respected.
        """

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt] | None, Parameters: nanoocp.NCollection.NCollection_HArray1[float] | None, PeriodicFlag: bool, Tolerance: float) -> None:
        """
        Initializes an algorithm for constructing a
        constrained BSpline curve passing through the points of the table
        Points, where the parameters of each of its
        points are given by the parallel table Parameters.
        Tangential vectors can then be assigned, using the function Load.
        If PeriodicFlag is true, the constrained BSpline
        curve will be periodic and closed. In this case,
        the junction point is the first point of the table Points.
        The tolerance value Tolerance is used to check that:
        -   points are not too close to each other, or
        -   tangential vectors (defined using the
        function Load) are not too small.
        The resulting BSpline curve will be "C2"
        continuous, except where a tangency
        constraint is defined on a point through which
        the curve passes (by using the Load function).
        In this case, it will be only "C1" continuous.
        Once all the constraints are defined, use the
        function Perform to compute the curve.
        Warning
        -   There must be at least 2 points in the table Points.
        -   If PeriodicFlag is false, there must be as
        many parameters in the array Parameters as
        there are points in the array Points.
        -   If PeriodicFlag is true, there must be one
        more parameter in the table Parameters: this
        is used to give the parameter on the
        resulting BSpline curve of the junction point
        of the curve (which is also the first point of the table Points).
        Exceptions
        -   Standard_ConstructionError if the
        distance between two consecutive points in
        the table Points is less than or equal to Tolerance.
        -   Standard_OutOfRange if:
        -   there are less than two points in the table Points, or
        -   conditions relating to the respective
        number of elements in the parallel tables
        Points and Parameters are not respected.
        """

    @overload
    def __init__(self, theOther: GeomAPI_Interpolate) -> None: ...

    @overload
    def Load(self, InitialTangent: nanoocp.gp.gp_Vec, FinalTangent: nanoocp.gp.gp_Vec, Scale: bool = True) -> None:
        """
        Assigns this constrained BSpline curve to be
        tangential to vectors InitialTangent and FinalTangent
        at its first and last points respectively (i.e.
        the first and last points of the table of
        points through which the curve passes, as
        defined at the time of initialization).
        """

    @overload
    def Load(self, Tangents: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec], TangentFlags: nanoocp.NCollection.NCollection_HArray1[bool] | None, Scale: bool = True) -> None:
        """
        Assigns this constrained BSpline curve to be
        tangential to vectors defined in the table Tangents,
        which is parallel to the table of points
        through which the curve passes, as
        defined at the time of initialization. Vectors
        in the table Tangents are defined only if
        the flag given in the parallel table
        TangentFlags is true: only these vectors
        are set as tangency constraints.
        """

    def Perform(self) -> None:
        """
        Computes the constrained BSpline curve.
        Use the function IsDone to verify that the
        computation is successful, and then the function Curve to obtain the result.
        """

    def Curve(self) -> nanoocp.Geom.Geom_BSplineCurve:
        """
        Returns the computed BSpline curve.
        Raises StdFail_NotDone if the interpolation fails.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the constrained BSpline curve is successfully constructed.
        Note: in this case, the result is given by the function Curve.
        """

class GeomAPI_IntSS:
    """
    This class implements methods for
    computing the intersection curves between two surfaces.
    The result is curves from Geom. The "domain" used for
    a surface is the natural parametric domain
    unless the surface is a RectangularTrimmedSurface
    from Geom.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty object. Use the
        function Perform for further initialization algorithm by two surfaces.
        """

    @overload
    def __init__(self, S1: nanoocp.Geom.Geom_Surface | None, S2: nanoocp.Geom.Geom_Surface | None, Tol: float) -> None:
        """
        Computes the intersection curves
        between the two surfaces S1 and S2. Parameter Tol defines the precision
        of curves computation. For most cases the value 1.0e-7 is recommended to use.
        Warning
        Use the function IsDone to verify that the intersections are successfully computed.I
        """

    @overload
    def __init__(self, theOther: GeomAPI_IntSS) -> None: ...

    def Perform(self, S1: nanoocp.Geom.Geom_Surface | None, S2: nanoocp.Geom.Geom_Surface | None, Tol: float) -> None:
        """
        Initializes an algorithm with the
        given arguments and computes the intersection curves between the two surfaces S1 and S2.
        Parameter Tol defines the precision of curves computation. For most
        cases the value 1.0e-7 is recommended to use.
        Warning
        Use function IsDone to verify that the intersections are successfully computed.
        """

    def IsDone(self) -> bool:
        """Returns True if the intersection was successful."""

    def NbLines(self) -> int:
        """
        Returns the number of computed intersection curves.
        Exceptions
        StdFail_NotDone if the computation fails.
        """

    def Line(self, Index: int) -> nanoocp.Geom.Geom_Curve:
        """
        Returns the computed intersection curve of index Index.
        Exceptions
        StdFail_NotDone if the computation fails.
        Standard_OutOfRange if Index is out of range [1, NbLines] where NbLines
        is the number of computed intersection curves.
        """

class GeomAPI_PointsToBSpline:
    """
    This class is used to approximate a BsplineCurve
    passing through an array of points, with a given Continuity.
    Describes functions for building a 3D BSpline
    curve which approximates a set of points.
    A PointsToBSpline object provides a framework for:
    -   defining the data of the BSpline curve to be built,
    -   implementing the approximation algorithm, and consulting the results.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty approximation algorithm.
        Use an Init function to define and build the BSpline curve.
        """

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None: ...

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], ParType: nanoocp.Approx.Approx_ParametrizationType, DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None:
        """
        Approximate a BSpline Curve passing through an
        array of Point. The resulting BSpline will have
        the following properties:
        1- his degree will be in the range [Degmin,Degmax]
        2- his continuity will be at least <Continuity>
        3- the distance from the point <Points> to the
        BSpline will be lower to Tol3D
        """

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Parameters: nanoocp.NCollection.NCollection_Array1[float], DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None:
        """
        Approximate a BSpline Curve passing through an
        array of Point, which parameters are given by the
        array <Parameters>.
        The resulting BSpline will have the following
        properties:
        1- his degree will be in the range [Degmin,Degmax]
        2- his continuity will be at least <Continuity>
        3- the distance from the point <Points> to the
        BSpline will be lower to Tol3D
        """

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weight1: float, Weight2: float, Weight3: float, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None:
        """
        Approximate a BSpline Curve passing through an
        array of Point using variational smoothing algorithm,
        which tries to minimize additional criterium:
        Weight1*CurveLength + Weight2*Curvature + Weight3*Torsion
        """

    @overload
    def __init__(self, theOther: GeomAPI_PointsToBSpline) -> None: ...

    @overload
    def Init(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None: ...

    @overload
    def Init(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], ParType: nanoocp.Approx.Approx_ParametrizationType, DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None:
        """
        Approximate a BSpline Curve passing through an
        array of Point. The resulting BSpline will have
        the following properties:
        1- his degree will be in the range [Degmin,Degmax]
        2- his continuity will be at least <Continuity>
        3- the distance from the point <Points> to the
        BSpline will be lower to Tol3D
        """

    @overload
    def Init(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Parameters: nanoocp.NCollection.NCollection_Array1[float], DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None:
        """
        Approximate a BSpline Curve passing through an
        array of Point, which parameters are given by the
        array <Parameters>.
        The resulting BSpline will have the following
        properties:
        1- his degree will be in the range [Degmin,Degmax]
        2- his continuity will be at least <Continuity>
        3- the distance from the point <Points> to the
        BSpline will be lower to Tol3D
        """

    @overload
    def Init(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weight1: float, Weight2: float, Weight3: float, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None:
        """
        Approximate a BSpline Curve passing through an
        array of Point using variational smoothing algorithm,
        which tries to minimize additional criterium:
        Weight1*CurveLength + Weight2*Curvature + Weight3*Torsion
        """

    def Curve(self) -> nanoocp.Geom.Geom_BSplineCurve:
        """
        Returns the computed BSpline curve.
        Raises StdFail_NotDone if the curve is not built.
        """

    def IsDone(self) -> bool: ...

class GeomAPI_PointsToBSplineSurface:
    """
    This class is used to approximate or interpolate
    a BSplineSurface passing through an Array2 of
    points, with a given continuity.
    Describes functions for building a BSpline
    surface which approximates or interpolates a set of points.
    A PointsToBSplineSurface object provides a framework for:
    -   defining the data of the BSpline surface to be built,
    -   implementing the approximation algorithm
    or the interpolation algorithm, and consulting the results.
    In fact, class contains 3 algorithms, 2 for approximation and 1
    for interpolation.
    First approximation algorithm is based on usual least square criterium:
    minimization of square distance between samplimg points and result surface.
    Second approximation algorithm uses least square criterium and additional
    minimization of some local characteristic of surface (first, second and third
    partial derivative), which allows managing shape of surface.
    Interpolation algorithm produces surface, which passes through sampling points.

    There is accordance between parametrization of result surface S(U, V) and
    indexes of array Points(i, j): first index corresponds U parameter of surface,
    second - V parameter of surface.
    So, points of any j-th column Points(*, j) represent any V isoline of surface,
    points of any i-th row Point(i, *) represent any U isoline of surface.

    For each sampling point parameters U, V are calculated according to
    type of parametrization, which can be Approx_ChordLength, Approx_Centripetal
    or Approx_IsoParametric. Default value is Approx_ChordLength.
    For ChordLength parametrisation U(i) = U(i-1) + P(i).Distance(P(i-1)),
    For Centripetal type U(i) = U(i-1) + std::sqrt(P(i).Distance(P(i-1))).
    Centripetal type can get better result for irregular distances between points.

    Approximation and interpolation algorithms can build periodical surface along U
    direction, which corresponds columns of array Points(i, j),
    if corresponding parameter (thePeriodic, see comments below) of called
    methods is set to True. Algorithm uses first row Points(1, *) as periodic boundary,
    so to avoid getting wrong surface it is necessary to keep distance between
    corresponding points of first and last rows of Points:
    Points(1, *) != Points(Upper, *).
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty algorithm for
        approximation or interpolation of a surface.
        Use:
        -   an Init function to define and build the
        BSpline surface by approximation, or
        -   an Interpolate function to define and build
        the BSpline surface by interpolation.
        """

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None: ...

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], ParType: nanoocp.Approx.Approx_ParametrizationType, DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None:
        """
        Approximates a BSpline Surface passing through an
        array of Points. The resulting BSpline will have
        the following properties:
        1- his degree will be in the range [Degmin,Degmax]
        2- his continuity will be at least <Continuity>
        3- the distance from the point <Points> to the
        BSpline will be lower to Tol3D.
        """

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], Weight1: float, Weight2: float, Weight3: float, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None:
        """
        Approximates a BSpline Surface passing through an
        array of points using variational smoothing algorithm,
        which tries to minimize additional criterium:
        Weight1*CurveLength + Weight2*Curvature + Weight3*Torsion.
        """

    @overload
    def __init__(self, ZPoints: nanoocp.NCollection.NCollection_Array2[float], X0: float, dX: float, Y0: float, dY: float, DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None:
        """
        Approximates a BSpline Surface passing through an
        array of Points.

        The points will be constructed as follow:
        P(i,j) = gp_Pnt( X0 + (i-1)*dX, Y0 + (j-1)*dY, ZPoints(i,j) )

        The resulting BSpline will have the following
        properties:
        1- his degree will be in the range [Degmin,Degmax]
        2- his continuity will be at least <Continuity>
        3- the distance from the point <Points> to the
        BSpline will be lower to Tol3D
        4- the parametrization of the surface will verify:
        S->Value( U, V) = gp_Pnt( U, V, Z(U,V) );
        """

    @overload
    def __init__(self, theOther: GeomAPI_PointsToBSplineSurface) -> None: ...

    @overload
    def Init(self, Points: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None: ...

    @overload
    def Init(self, ZPoints: nanoocp.NCollection.NCollection_Array2[float], X0: float, dX: float, Y0: float, dY: float, DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None:
        """
        Approximates a BSpline Surface passing through an
        array of Points.

        The points will be constructed as follow:
        P(i,j) = gp_Pnt( X0 + (i-1)*dX, Y0 + (j-1)*dY, ZPoints(i,j) )

        The resulting BSpline will have the following
        properties:
        1- his degree will be in the range [Degmin,Degmax]
        2- his continuity will be at least <Continuity>
        3- the distance from the point <Points> to the
        BSpline will be lower to Tol3D
        4- the parametrization of the surface will verify:
        S->Value( U, V) = gp_Pnt( U, V, Z(U,V) );
        """

    @overload
    def Init(self, Points: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], ParType: nanoocp.Approx.Approx_ParametrizationType, DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001, thePeriodic: bool = False) -> None:
        """
        Approximates a BSpline Surface passing through an
        array of Point. The resulting BSpline will have
        the following properties:
        1- his degree will be in the range [Degmin,Degmax]
        2- his continuity will be at least <Continuity>
        3- the distance from the point <Points> to the
        BSpline will be lower to Tol3D.
        """

    @overload
    def Init(self, Points: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], Weight1: float, Weight2: float, Weight3: float, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None:
        """
        Approximates a BSpline Surface passing through an
        array of point using variational smoothing algorithm,
        which tries to minimize additional criterium:
        Weight1*CurveLength + Weight2*Curvature + Weight3*Torsion.
        """

    @overload
    def Interpolate(self, Points: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], thePeriodic: bool = False) -> None: ...

    @overload
    def Interpolate(self, Points: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], ParType: nanoocp.Approx.Approx_ParametrizationType, thePeriodic: bool = False) -> None:
        """
        Interpolates a BSpline Surface passing through an
        array of Point. The resulting BSpline will have
        the following properties:
        1- his degree will be 3.
        2- his continuity will be C2.
        """

    @overload
    def Interpolate(self, ZPoints: nanoocp.NCollection.NCollection_Array2[float], X0: float, dX: float, Y0: float, dY: float) -> None:
        """
        Interpolates a BSpline Surface passing through an
        array of Points.

        The points will be constructed as follow:
        P(i,j) = gp_Pnt( X0 + (i-1)*dX, Y0 + (j-1)*dY, ZPoints(i,j) )

        The resulting BSpline will have the following
        properties:
        1- his degree will be 3
        2- his continuity will be C2.
        4- the parametrization of the surface will verify:
        S->Value( U, V) = gp_Pnt( U, V, Z(U,V) );
        """

    def Surface(self) -> nanoocp.Geom.Geom_BSplineSurface:
        """Returns the approximate BSpline Surface"""

    def IsDone(self) -> bool: ...

class GeomAPI_ProjectPointOnCurve:
    """
    This class implements methods for computing all the orthogonal
    projections of a 3D point onto a 3D curve.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an empty object. Use an
        Init function for further initialization.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, Curve: nanoocp.Geom.Geom_Curve | None) -> None:
        """
        Create the projection of a point <P> on a curve
        <Curve>
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, Curve: nanoocp.Geom.Geom_Curve | None, Umin: float, Usup: float) -> None:
        """
        Create the projection of a point <P> on a curve
        <Curve> limited by the two points of parameter Umin and Usup.
        """

    @overload
    def __init__(self, theOther: GeomAPI_ProjectPointOnCurve) -> None: ...

    @overload
    def Init(self, P: nanoocp.gp.gp_Pnt, Curve: nanoocp.Geom.Geom_Curve | None) -> None:
        """
        Init the projection of a point <P> on a curve
        <Curve>
        """

    @overload
    def Init(self, P: nanoocp.gp.gp_Pnt, Curve: nanoocp.Geom.Geom_Curve | None, Umin: float, Usup: float) -> None: ...

    @overload
    def Init(self, Curve: nanoocp.Geom.Geom_Curve | None, Umin: float, Usup: float) -> None:
        """
        Init the projection of a point <P> on a curve
        <Curve> limited by the two points of parameter Umin and Usup.
        """

    def Perform(self, P: nanoocp.gp.gp_Pnt) -> None:
        """Performs the projection of a point on the current curve."""

    def NbPoints(self) -> int:
        """
        Returns the number of computed
        orthogonal projection points.
        Note: if this algorithm fails, NbPoints returns 0.
        """

    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        Returns the orthogonal projection
        on the curve. Index is a number of a computed point.
        Exceptions
        Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where
        NbPoints is the number of solution points.
        """

    def Parameter(self, Index: int) -> float:
        """
        Returns the parameter on the curve
        of the point, which is the orthogonal projection. Index is a
        number of a computed point.
        Exceptions
        Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where
        NbPoints is the number of solution points.
        """

    def Parameter__float(self, Index: int) -> float:
        """
        Parameter__float: the C++ overload Parameter(const int, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns the parameter on the curve
        of the point, which is the orthogonal projection. Index is a
        number of a computed point.
        Exceptions
        Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where
        NbPoints is the number of solution points.-
        """

    def Distance(self, Index: int) -> float:
        """
        Computes the distance between the
        point and its orthogonal projection on the curve. Index is a number of a computed point.
        Exceptions
        Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where
        NbPoints is the number of solution points.
        """

    def NearestPoint(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the nearest orthogonal
        projection of the point on the curve.
        Exceptions: StdFail_NotDone if this algorithm fails.
        """

    def LowerDistanceParameter(self) -> float:
        """
        Returns the parameter on the curve
        of the nearest orthogonal projection of the point.
        Exceptions: StdFail_NotDone if this algorithm fails.
        """

    def LowerDistance(self) -> float:
        """
        Computes the distance between the
        point and its nearest orthogonal projection on the curve.
        Exceptions: StdFail_NotDone if this algorithm fails.
        """

    def Extrema(self) -> nanoocp.Extrema.Extrema_ExtPC:
        """return the algorithmic object from Extrema"""

    def __int__(self) -> int: ...

    def __float__(self) -> float: ...

class GeomAPI_ProjectPointOnSurf:
    """
    This class implements methods for computing all the orthogonal
    projections of a point onto a surface.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an empty object. Use the
        Init function for further initialization.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, Surface: nanoocp.Geom.Geom_Surface | None, Algo: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None:
        """
        Create the projection of a point <P> on a surface
        <Surface>
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, Surface: nanoocp.Geom.Geom_Surface | None, Tolerance: float, Algo: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None:
        """
        Create the projection of a point <P> on a surface
        <Surface>
        Create the projection of a point <P> on a surface
        <Surface>. The solution are computed in the domain
        [Umin,Usup] [Vmin,Vsup] of the surface.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, Surface: nanoocp.Geom.Geom_Surface | None, Umin: float, Usup: float, Vmin: float, Vsup: float, Algo: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None:
        """
        Init the projection of a point <P> on a surface
        <Surface>
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, Surface: nanoocp.Geom.Geom_Surface | None, Umin: float, Usup: float, Vmin: float, Vsup: float, Tolerance: float, Algo: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...

    @overload
    def Init(self, P: nanoocp.gp.gp_Pnt, Surface: nanoocp.Geom.Geom_Surface | None, Tolerance: float, Algo: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...

    @overload
    def Init(self, P: nanoocp.gp.gp_Pnt, Surface: nanoocp.Geom.Geom_Surface | None, Algo: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None:
        """
        Init the projection of a point <P> on a surface
        <Surface>. The solution are computed in the domain
        [Umin,Usup] [Vmin,Vsup] of the surface.
        """

    @overload
    def Init(self, P: nanoocp.gp.gp_Pnt, Surface: nanoocp.Geom.Geom_Surface | None, Umin: float, Usup: float, Vmin: float, Vsup: float, Tolerance: float, Algo: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...

    @overload
    def Init(self, P: nanoocp.gp.gp_Pnt, Surface: nanoocp.Geom.Geom_Surface | None, Umin: float, Usup: float, Vmin: float, Vsup: float, Algo: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None:
        """
        Init the projection for many points on a surface
        <Surface>. The solutions will be computed in the domain
        [Umin,Usup] [Vmin,Vsup] of the surface.
        """

    @overload
    def Init(self, Surface: nanoocp.Geom.Geom_Surface | None, Umin: float, Usup: float, Vmin: float, Vsup: float, Tolerance: float, Algo: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...

    @overload
    def Init(self, Surface: nanoocp.Geom.Geom_Surface | None, Umin: float, Usup: float, Vmin: float, Vsup: float, Algo: nanoocp.Extrema.Extrema_ExtAlgo = Extrema_ExtAlgo.Extrema_ExtAlgo_Grad) -> None: ...

    def SetExtremaAlgo(self, theAlgo: nanoocp.Extrema.Extrema_ExtAlgo) -> None:
        """
        Sets the Extrema search algorithm - Grad or Tree.
        By default the Extrema is initialized with Grad algorithm.
        """

    def SetExtremaFlag(self, theExtFlag: nanoocp.Extrema.Extrema_ExtFlag) -> None:
        """
        Sets the Extrema search flag - MIN or MAX or MINMAX.
        By default the Extrema is set to search the MinMax solutions.
        """

    def Perform(self, P: nanoocp.gp.gp_Pnt) -> None:
        """Performs the projection of a point on the current surface."""

    def IsDone(self) -> bool: ...

    def NbPoints(self) -> int:
        """
        Returns the number of computed orthogonal projection points.
        Note: if projection fails, NbPoints returns 0.
        """

    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        Returns the orthogonal projection
        on the surface. Index is a number of a computed point.
        Exceptions
        Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where
        NbPoints is the number of solution points.
        """

    def Parameters(self, Index: int) -> tuple[float, float]:
        """
        Returns the parameters (U,V) on the
        surface of the orthogonal projection. Index is a number of a
        computed point.
        Exceptions
        Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where
        NbPoints is the number of solution points.
        """

    def Distance(self, Index: int) -> float:
        """
        Computes the distance between the
        point and its orthogonal projection on the surface. Index is a number
        of a computed point.
        Exceptions
        Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where
        NbPoints is the number of solution points.
        """

    def NearestPoint(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the nearest orthogonal projection of the point
        on the surface.
        Exceptions
        StdFail_NotDone if projection fails.
        """

    def LowerDistanceParameters(self) -> tuple[float, float]:
        """
        Returns the parameters (U,V) on the
        surface of the nearest computed orthogonal projection of the point.
        Exceptions
        StdFail_NotDone if projection fails.
        """

    def LowerDistance(self) -> float:
        """
        Computes the distance between the
        point and its nearest orthogonal projection on the surface.
        Exceptions
        StdFail_NotDone if projection fails.
        """

    def Extrema(self) -> nanoocp.Extrema.Extrema_ExtPS:
        """return the algorithmic object from Extrema"""

    def __int__(self) -> int: ...

    def __float__(self) -> float: ...
