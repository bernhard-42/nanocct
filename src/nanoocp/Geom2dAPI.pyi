"""OCCT package Geom2dAPI (toolkit TKGeomAlgo)"""

from typing import overload

import nanoocp.Approx
import nanoocp.Extrema
import nanoocp.Geom2d
import nanoocp.Geom2dInt
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.gp


class Geom2dAPI_ExtremaCurveCurve:
    """
    Describes functions for computing all the extrema
    between two 2D curves.
    An ExtremaCurveCurve algorithm minimizes or
    maximizes the distance between a point on the first
    curve and a point on the second curve. Thus, it
    computes the start point and end point of
    perpendiculars common to the two curves (an
    intersection point is not an extremum except where
    the two curves are tangential at this point).
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
    def __init__(self, C1: nanoocp.Geom2d.Geom2d_Curve | None, C2: nanoocp.Geom2d.Geom2d_Curve | None, U1min: float, U1max: float, U2min: float, U2max: float) -> None:
        """
        Computes the extrema between
        -   the portion of the curve C1 limited by the two
        points of parameter (U1min,U1max), and
        -   the portion of the curve C2 limited by the two
        points of parameter (U2min,U2max).
        Warning
        Use the function NbExtrema to obtain the number
        of solutions. If this algorithm fails, NbExtrema returns 0.
        """

    @overload
    def __init__(self, theOther: Geom2dAPI_ExtremaCurveCurve) -> None: ...

    def NbExtrema(self) -> int:
        """
        Returns the number of extrema computed by this algorithm.
        Note: if this algorithm fails, NbExtrema returns 0.
        """

    def Points(self, Index: int, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None:
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
        are the ends of the extremum of index Index
        computed by this algorithm.
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

    def NearestPoints(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None:
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
        Exceptions
        StdFail_NotDone if this algorithm fails.
        """

    def LowerDistance(self) -> float:
        """
        Computes the distance between the end points of the
        shortest extremum computed by this algorithm.
        Exceptions - StdFail_NotDone if this algorithm fails.
        """

    def Extrema(self) -> nanoocp.Extrema.Extrema_ExtCC2d: ...

    def __int__(self) -> int: ...

    def __float__(self) -> float: ...

class Geom2dAPI_InterCurveCurve:
    """
    This class implements methods for computing
    -       the intersections between two 2D curves,
    -       the self-intersections of a 2D curve.
    Using the InterCurveCurve algorithm allows to get the following results:
    -      intersection points in the case of cross intersections,
    -      intersection segments in the case of tangential intersections,
    -       nothing in the case of no intersections.
    """

    @overload
    def __init__(self) -> None:
        """
        Create an empty intersector. Use the
        function Init for further initialization of the intersection
        algorithm by curves or curve.
        """

    @overload
    def __init__(self, C1: nanoocp.Geom2d.Geom2d_Curve | None, Tol: float = 1e-06) -> None:
        """
        Creates an object and computes self-intersections of the curve C1.
        Tolerance value Tol, defaulted to 1.0e-6, defines the precision of
        computing the intersection points.
        In case of a tangential intersection, Tol also defines the
        size of intersection segments (limited portions of the curves)
        where the distance between all points from two curves (or a curve
        in case of self-intersection) is less than Tol.
        Warning
        Use functions NbPoints and NbSegments to obtain the number of
        solutions. If the algorithm finds no intersections NbPoints and
        NbSegments return 0.
        """

    @overload
    def __init__(self, C1: nanoocp.Geom2d.Geom2d_Curve | None, C2: nanoocp.Geom2d.Geom2d_Curve | None, Tol: float = 1e-06) -> None:
        """
        Creates an object and computes the
        intersections between the curves C1 and C2.
        """

    @overload
    def __init__(self, theOther: Geom2dAPI_InterCurveCurve) -> None: ...

    @overload
    def Init(self, C1: nanoocp.Geom2d.Geom2d_Curve | None, C2: nanoocp.Geom2d.Geom2d_Curve | None, Tol: float = 1e-06) -> None:
        """
        Initializes an algorithm with the
        given arguments and computes the intersections between the curves C1. and C2.
        """

    @overload
    def Init(self, C1: nanoocp.Geom2d.Geom2d_Curve | None, Tol: float = 1e-06) -> None:
        """
        Initializes an algorithm with the
        given arguments and computes the self-intersections of the curve C1.
        Tolerance value Tol, defaulted to 1.0e-6, defines the precision of
        computing the intersection points. In case of a tangential
        intersection, Tol also defines the size of intersection segments
        (limited portions of the curves) where the distance between all
        points from two curves (or a curve in case of self-intersection) is less than Tol.
        Warning
        Use functions NbPoints and NbSegments to obtain the number
        of solutions. If the algorithm finds no intersections NbPoints
        and NbSegments return 0.
        """

    def NbPoints(self) -> int:
        """
        Returns the number of intersection-points in case of cross intersections.
        NbPoints returns 0 if no intersections were found.
        """

    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the intersection point of index Index.
        Intersection points are computed in case of cross intersections with a
        precision equal to the tolerance value assigned at the time of
        construction or in the function Init (this value is defaulted to 1.0e-6).
        Exceptions
        Standard_OutOfRange if index is not in the range [ 1,NbPoints ], where
        NbPoints is the number of computed intersection points
        """

    def NbSegments(self) -> int:
        """
        Returns the number of tangential intersections.
        NbSegments returns 0 if no intersections were found
        """

    def Segment(self, Index: int) -> tuple[nanoocp.Geom2d.Geom2d_Curve, nanoocp.Geom2d.Geom2d_Curve]:
        """
        Use this syntax only to get
        solutions of tangential intersection between two curves.
        Output values Curve1 and Curve2 are the intersection segments on the
        first curve and on the second curve accordingly. Parameter Index
        defines a number of computed solution.
        An intersection segment is a portion of an initial curve limited
        by two points. The distance from each point of this segment to the
        other curve is less or equal to the tolerance value assigned at the
        time of construction or in function Init (this value is defaulted to 1.0e-6).
        Exceptions
        Standard_OutOfRange if Index is not in the range [ 1,NbSegments ],
        where NbSegments is the number of computed tangential intersections.
        Standard_NullObject if the algorithm is initialized for the
        computing of self-intersections on a curve.
        """

    def Intersector(self) -> nanoocp.Geom2dInt.Geom2dInt_GInter:
        """return the algorithmic object from Intersection."""

class Geom2dAPI_Interpolate:
    """
    This class is used to interpolate a BsplineCurve
    passing through an array of points, with a C2
    Continuity if tangency is not requested at the point.
    If tangency is requested at the point the continuity will
    be C1. If Perodicity is requested the curve will be closed
    and the junction will be the first point given. The curve will than be only C1
    The curve is defined by a table of points through which it passes, and if required
    by a parallel table of reals which gives the value of the parameter of each point through
    which the resulting BSpline curve passes, and by vectors tangential to these points.
    An Interpolate object provides a framework for: defining the constraints of the BSpline curve,
    -   implementing the interpolation algorithm, and consulting the results.
    """

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt2d] | None, PeriodicFlag: bool, Tolerance: float) -> None:
        """
        Tolerance is to check if the points are not too close to one an other
        It is also used to check if the tangent vector is not too small.
        There should be at least 2 points
        if PeriodicFlag is True then the curve will be periodic.
        """

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt2d] | None, Parameters: nanoocp.NCollection.NCollection_HArray1[float] | None, PeriodicFlag: bool, Tolerance: float) -> None:
        """
        if PeriodicFlag is True then the curve will be periodic
        Warning:
        There should be as many parameters as there are points
        except if PeriodicFlag is True : then there should be one more
        parameter to close the curve
        """

    @overload
    def __init__(self, theOther: Geom2dAPI_Interpolate) -> None: ...

    @overload
    def Load(self, InitialTangent: nanoocp.gp.gp_Vec2d, FinalTangent: nanoocp.gp.gp_Vec2d, Scale: bool = True) -> None:
        """
        Assigns this constrained BSpline curve to be
        tangential to vectors InitialTangent and FinalTangent
        at its first and last points respectively (i.e.
        the first and last points of the table of
        points through which the curve passes, as
        defined at the time of initialization).
        <Scale> - boolean flag defining whether tangent vectors are to
        be scaled according to derivatives of lagrange interpolation.
        """

    @overload
    def Load(self, Tangents: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], TangentFlags: nanoocp.NCollection.NCollection_HArray1[bool] | None, Scale: bool = True) -> None:
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
        <Scale> - boolean flag defining whether tangent vectors are to
        be scaled according to derivatives of lagrange interpolation.
        """

    def Perform(self) -> None:
        """
        Computes the constrained BSpline curve. Use the function IsDone to verify that the
        computation is successful, and then the function Curve to obtain the result.
        """

    def Curve(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """
        Returns the computed BSpline curve. Raises StdFail_NotDone if the interpolation fails.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the constrained BSpline curve is successfully constructed.
        Note: in this case, the result is given by the function Curve.
        """

class Geom2dAPI_PointsToBSpline:
    """
    This class is used to approximate a BsplineCurve
    passing through an array of points, with a given
    Continuity.
    Describes functions for building a 2D BSpline
    curve which approximates a set of points.
    A PointsToBSpline object provides a framework for:
    -   defining the data of the BSpline curve to be built,
    -   implementing the approximation algorithm, and
    -   consulting the results
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty approximation algorithm.
        Use an Init function to define and build the BSpline curve.
        """

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol2D: float = 1e-06) -> None: ...

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], ParType: nanoocp.Approx.Approx_ParametrizationType, DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol2D: float = 0.001) -> None:
        """
        Approximate a BSpline Curve passing through an
        array of Point. The resulting BSpline will have
        the following properties:
        1- his degree will be in the range [Degmin,Degmax]
        2- his continuity will be at least <Continuity>
        3- the distance from the point <Points> to the
        BSpline will be lower to Tol2D
        """

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Parameters: nanoocp.NCollection.NCollection_Array1[float], DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol2D: float = 0.001) -> None:
        """
        Approximate a BSpline Curve passing through an
        array of Point, which parameters are given by the
        array <Parameters>.
        The resulting BSpline will have the following
        properties:
        1- his degree will be in the range [Degmin,Degmax]
        2- his continuity will be at least <Continuity>
        3- the distance from the point <Points> to the
        BSpline will be lower to Tol2D
        """

    @overload
    def __init__(self, YValues: nanoocp.NCollection.NCollection_Array1[float], X0: float, DX: float, DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol2D: float = 1e-06) -> None:
        """
        Approximate a BSpline Curve passing through an
        array of Point. Of coordinates :

        X = X0 + DX * (i-YValues.Lower())
        Y = YValues(i)

        With i in the range YValues.Lower(), YValues.Upper()

        The BSpline will be parametrized from t = X0 to
        X0 + DX * (YValues.Upper() - YValues.Lower())

        And will satisfy X(t) = t

        The resulting BSpline will have
        the following properties:
        1- his degree will be in the range [Degmin,Degmax]
        2- his continuity will be at least <Continuity>
        3- the distance from the point <Points> to the
        BSpline will be lower to Tol2D
        """

    @overload
    def __init__(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weight1: float, Weight2: float, Weight3: float, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol3D: float = 0.001) -> None:
        """
        Approximate a BSpline Curve passing through an
        array of Point using variational smoothing algorithm,
        which tries to minimize additional criterium:
        Weight1*CurveLength + Weight2*Curvature + Weight3*Torsion
        """

    @overload
    def __init__(self, theOther: Geom2dAPI_PointsToBSpline) -> None: ...

    @overload
    def Init(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol2D: float = 1e-06) -> None: ...

    @overload
    def Init(self, YValues: nanoocp.NCollection.NCollection_Array1[float], X0: float, DX: float, DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol2D: float = 1e-06) -> None:
        """
        Approximate a BSpline Curve passing through an
        array of Point. Of coordinates :

        X = X0 + DX * (i-YValues.Lower())
        Y = YValues(i)

        With i in the range YValues.Lower(), YValues.Upper()

        The BSpline will be parametrized from t = X0 to
        X0 + DX * (YValues.Upper() - YValues.Lower())

        And will satisfy X(t) = t

        The resulting BSpline will have
        the following properties:
        1- his degree will be in the range [Degmin,Degmax]
        2- his continuity will be at least <Continuity>
        3- the distance from the point <Points> to the
        BSpline will be lower to Tol2D
        """

    @overload
    def Init(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], ParType: nanoocp.Approx.Approx_ParametrizationType, DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol2D: float = 0.001) -> None:
        """
        Approximate a BSpline Curve passing through an
        array of Point. The resulting BSpline will have
        the following properties:
        1- his degree will be in the range [Degmin,Degmax]
        2- his continuity will be at least <Continuity>
        3- the distance from the point <Points> to the
        BSpline will be lower to Tol2D
        """

    @overload
    def Init(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Parameters: nanoocp.NCollection.NCollection_Array1[float], DegMin: int = 3, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol2D: float = 0.001) -> None:
        """
        Approximate a BSpline Curve passing through an
        array of Point, which parameters are given by the
        array <Parameters>.
        The resulting BSpline will have the following
        properties:
        1- his degree will be in the range [Degmin,Degmax]
        2- his continuity will be at least <Continuity>
        3- the distance from the point <Points> to the
        BSpline will be lower to Tol2D
        """

    @overload
    def Init(self, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weight1: float, Weight2: float, Weight3: float, DegMax: int = 8, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Tol2D: float = 0.001) -> None:
        """
        Approximate a BSpline Curve passing through an
        array of Point using variational smoothing algorithm,
        which tries to minimize additional criterium:
        Weight1*CurveLength + Weight2*Curvature + Weight3*Torsion
        """

    def Curve(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """Returns the approximate BSpline Curve"""

    def IsDone(self) -> bool: ...

class Geom2dAPI_ProjectPointOnCurve:
    """
    This class implements methods for computing all the orthogonal
    projections of a 2D point onto a 2D curve.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty projector algorithm. Use an Init
        function to define the point and the curve on which it is going to work.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt2d, Curve: nanoocp.Geom2d.Geom2d_Curve | None) -> None:
        """
        Create the projection of a point <P> on a curve
        <Curve>
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt2d, Curve: nanoocp.Geom2d.Geom2d_Curve | None, Umin: float, Usup: float) -> None:
        """
        Create the projection of a point <P> on a curve
        <Curve> limited by the two points of parameter Umin and Usup.
        Warning
        Use the function NbPoints to obtain the number of solutions. If
        projection fails, NbPoints returns 0.
        """

    @overload
    def __init__(self, theOther: Geom2dAPI_ProjectPointOnCurve) -> None: ...

    @overload
    def Init(self, P: nanoocp.gp.gp_Pnt2d, Curve: nanoocp.Geom2d.Geom2d_Curve | None) -> None:
        """
        Initializes this algorithm with the given arguments, and
        computes the orthogonal projections of a point <P> on a curve <Curve>
        """

    @overload
    def Init(self, P: nanoocp.gp.gp_Pnt2d, Curve: nanoocp.Geom2d.Geom2d_Curve | None, Umin: float, Usup: float) -> None:
        """
        Initializes this algorithm with the given arguments, and
        computes the orthogonal projections of the point P onto the portion
        of the curve Curve limited by the two points of parameter Umin and Usup.
        """

    def NbPoints(self) -> int:
        """
        return the number of of computed
        orthogonal projectionn points.
        """

    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt2d:
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
        of a point which is the orthogonal projection. Index is a number of a
        computed projected point.
        Exceptions
        Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where
        NbPoints is the number of solution points.
        """

    def Parameter__float(self, Index: int) -> float:
        """
        Parameter__float: the C++ overload Parameter(const int, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns the parameter on the curve
        of a point which is the orthogonal projection. Index is a number of a
        computed projected point.
        Exceptions
        Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where
        NbPoints is the number of solution points
        """

    def Distance(self, Index: int) -> float:
        """
        Computes the distance between the
        point and its computed orthogonal projection on the curve. Index is a
        number of computed projected point.
        Exceptions
        Standard_OutOfRange if Index is not in the range [ 1,NbPoints ], where
        NbPoints is the number of solution points.
        """

    def NearestPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the nearest orthogonal projection of the point on the curve.
        Exceptions
        StdFail_NotDone if this algorithm fails.
        """

    def LowerDistanceParameter(self) -> float:
        """
        Returns the parameter on the curve
        of the nearest orthogonal projection of the point.
        Exceptions
        StdFail_NotDone if this algorithm fails.
        """

    def LowerDistance(self) -> float:
        """
        Computes the distance between the
        point and its nearest orthogonal projection on the curve.
        Exceptions
        StdFail_NotDone if this algorithm fails.
        """

    def Extrema(self) -> nanoocp.Extrema.Extrema_ExtPC2d:
        """return the algorithmic object from Extrema"""

    def __int__(self) -> int: ...

    def __float__(self) -> float: ...
