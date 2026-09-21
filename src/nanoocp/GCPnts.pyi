"""OCCT package GCPnts (toolkit TKGeomBase)"""

import enum
from typing import overload

import nanoocp.Adaptor2d
import nanoocp.Adaptor3d
import nanoocp.GeomAbs
import nanoocp.gp
import nanoocp.math


class GCPnts_AbscissaType(enum.IntEnum):
    GCPnts_LengthParametrized = 0

    GCPnts_Parametrized = 1

    GCPnts_AbsComposite = 2

GCPnts_LengthParametrized: GCPnts_AbscissaType = GCPnts_AbscissaType.GCPnts_LengthParametrized

GCPnts_Parametrized: GCPnts_AbscissaType = GCPnts_AbscissaType.GCPnts_Parametrized

GCPnts_AbsComposite: GCPnts_AbscissaType = GCPnts_AbscissaType.GCPnts_AbsComposite

class GCPnts_DeflectionType(enum.IntEnum):
    GCPnts_Linear = 0

    GCPnts_Circular = 1

    GCPnts_Curved = 2

    GCPnts_DefComposite = 3

GCPnts_Linear: GCPnts_DeflectionType = GCPnts_DeflectionType.GCPnts_Linear

GCPnts_Circular: GCPnts_DeflectionType = GCPnts_DeflectionType.GCPnts_Circular

GCPnts_Curved: GCPnts_DeflectionType = GCPnts_DeflectionType.GCPnts_Curved

GCPnts_DefComposite: GCPnts_DeflectionType = GCPnts_DeflectionType.GCPnts_DefComposite

class GCPnts_AbscissaPoint:
    """
    Provides an algorithm to compute a point on a curve
    situated at a given distance from another point on the curve,
    the distance being measured along the curve (curvilinear abscissa on the curve).
    This algorithm is also used to compute the length of a curve.
    An AbscissaPoint object provides a framework for:
    -   defining the point to compute
    -   implementing the construction algorithm
    -   consulting the result.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theAbscissa: float, theU0: float) -> None: ...

    @overload
    def __init__(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theAbscissa: float, theU0: float) -> None:
        """
        The algorithm computes a point on a curve at the
        distance theAbscissa from the point of parameter theU0.
        """

    @overload
    def __init__(self, theTol: float, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theAbscissa: float, theU0: float) -> None: ...

    @overload
    def __init__(self, theTol: float, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theAbscissa: float, theU0: float) -> None:
        """
        The algorithm computes a point on a curve at
        the distance theAbscissa from the point of parameter
        theU0 with the given tolerance.
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theAbscissa: float, theU0: float, theUi: float) -> None:
        """
        The algorithm computes a point on a curve at the
        distance theAbscissa from the point of parameter theU0.
        theUi is the starting value used in the iterative process
        which find the solution, it must be close to the final solution.
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theAbscissa: float, theU0: float, theUi: float) -> None:
        """
        The algorithm computes a point on a curve at the
        distance theAbscissa from the point of parameter theU0.
        theUi is the starting value used in the iterative process
        which find the solution, it must be closed to the final solution
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theAbscissa: float, theU0: float, theUi: float, theTol: float) -> None: ...

    @overload
    def __init__(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theAbscissa: float, theU0: float, theUi: float, theTol: float) -> None:
        """
        The algorithm computes a point on a curve at the
        distance theAbscissa from the point of parameter theU0.
        theUi is the starting value used in the iterative process
        which find the solution, it must be close to the final solution
        """

    @overload
    def __init__(self, theOther: GCPnts_AbscissaPoint) -> None: ...

    @overload
    @staticmethod
    def Length(theC: nanoocp.Adaptor3d.Adaptor3d_Curve) -> float: ...

    @overload
    @staticmethod
    def Length(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> float: ...

    @overload
    @staticmethod
    def Length(theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theTol: float) -> float: ...

    @overload
    @staticmethod
    def Length(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theTol: float) -> float:
        """Computes the length of the 2D Curve with the given tolerance."""

    @overload
    @staticmethod
    def Length(theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theU1: float, theU2: float) -> float:
        """Computes the length of the 3D Curve."""

    @overload
    @staticmethod
    def Length(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theU1: float, theU2: float) -> float:
        """Computes the length of the 2D Curve."""

    @overload
    @staticmethod
    def Length(theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theU1: float, theU2: float, theTol: float) -> float:
        """Computes the length of the 3D Curve with the given tolerance."""

    @overload
    @staticmethod
    def Length(theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theU1: float, theU2: float, theTol: float) -> float:
        """Computes the length of the Curve with the given tolerance."""

    def IsDone(self) -> bool:
        """
        True if the computation was successful, False otherwise.
        IsDone is a protection against:
        -   non-convergence of the algorithm
        -   querying the results before computation.
        """

    def Parameter(self) -> float:
        """
        Returns the parameter on the curve of the point
        solution of this algorithm.
        Exceptions
        StdFail_NotDone if the computation was not
        successful, or was not done.
        """

class GCPnts_QuasiUniformAbscissa:
    """
    This class provides an algorithm to compute a uniform abscissa
    distribution of points on a curve, i.e. a sequence of equidistant points.
    The distance between two consecutive points is measured along the curve.

    The distribution is defined by a number of points.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty algorithm.
        To define the problem to be solved, use the function Initialize.
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theNbPoints: int) -> None:
        """
        Computes a uniform abscissa distribution of points
        -   on the curve where Abscissa is the curvilinear distance between
        two consecutive points of the distribution.
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theNbPoints: int) -> None:
        """
        Computes a uniform abscissa distribution of points on the 2D curve.
        @param[in] theC  input 2D curve
        @param[in] theNbPoints  defines the number of desired points
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theNbPoints: int, theU1: float, theU2: float) -> None:
        """
        Computes a uniform abscissa distribution of points
        on the part of curve limited by the two parameter values theU1 and theU2,
        where Abscissa is the curvilinear distance between
        two consecutive points of the distribution.
        The first point of the distribution is either the origin of
        curve or the point of parameter theU1.
        The following points are computed such that the curvilinear
        distance between two consecutive points is equal to Abscissa.
        The last point of the distribution is either the end
        point of curve or the point of parameter theU2.
        However the curvilinear distance between this last
        point and the point just preceding it in the distribution is,
        of course, generally not equal to Abscissa.
        Use the function IsDone() to verify that the computation was successful,
        the function NbPoints() to obtain the number of points of the computed distribution,
        and the function Parameter() to read the parameter of each point.

        Warning
        The roles of theU1 and theU2 are inverted if theU1 > theU2.
        Warning
        theC is an adapted curve, that is, an object which is an interface between:
        -   the services provided by either a 2D curve from
        the package Geom2d (in the case of an Adaptor2d_Curve2d curve)
        or a 3D curve from the package Geom (in the case of an Adaptor3d_Curve curve),
        -   and those required on the curve by the computation algorithm.
        @param[in] theC  input 3D curve
        @param[in] theNbPoints  defines the number of desired points
        @param[in] theU1  first parameter on curve
        @param[in] theU2  last  parameter on curve
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theNbPoints: int, theU1: float, theU2: float) -> None:
        """
        Computes a Uniform abscissa distribution of points on a part of the 2D curve.
        @param[in] theC  input 2D curve
        @param[in] theNbPoints  defines the number of desired points
        @param[in] theU1  first parameter on curve
        @param[in] theU2  last  parameter on curve
        """

    @overload
    def __init__(self, theOther: GCPnts_QuasiUniformAbscissa) -> None: ...

    @overload
    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theNbPoints: int) -> None:
        """
        Initialize the algorithms with 3D curve and target number of points.
        @param[in] theC  input 3D curve
        @param[in] theNbPoints  defines the number of desired points
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theNbPoints: int, theU1: float, theU2: float) -> None:
        """
        Initialize the algorithms with 3D curve, target number of points and curve parameter range.
        @param[in] theC  input 3D curve
        @param[in] theNbPoints  defines the number of desired points
        @param[in] theU1  first parameter on curve
        @param[in] theU2  last  parameter on curve
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theNbPoints: int) -> None:
        """
        Initialize the algorithms with 2D curve and target number of points.
        @param[in] theC  input 2D curve
        @param[in] theNbPoints  defines the number of desired points
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theNbPoints: int, theU1: float, theU2: float) -> None:
        """
        Initialize the algorithms with 2D curve, target number of points and curve parameter range.
        @param[in] theC  input 2D curve
        @param[in] theNbPoints  defines the number of desired points
        @param[in] theU1  first parameter on curve
        @param[in] theU2  last  parameter on curve
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computation was successful.
        IsDone is a protection against:
        -   non-convergence of the algorithm
        -   querying the results before computation.
        """

    def NbPoints(self) -> int:
        """
        Returns the number of points of the distribution
        computed by this algorithm.
        This value is either:
        -   the one imposed on the algorithm at the time of
        construction (or initialization), or
        -   the one computed by the algorithm when the
        curvilinear distance between two consecutive
        points of the distribution is imposed on the
        algorithm at the time of construction (or initialization).
        Exceptions
        StdFail_NotDone if this algorithm has not been
        initialized, or if the computation was not successful.
        """

    def Parameter(self, Index: int) -> float:
        """
        Returns the parameter of the point of index Index in
        the distribution computed by this algorithm.
        Warning
        Index must be greater than or equal to 1, and less
        than or equal to the number of points of the
        distribution. However, pay particular attention as this
        condition is not checked by this function.
        Exceptions
        StdFail_NotDone if this algorithm has not been
        initialized, or if the computation was not successful.
        """

class GCPnts_QuasiUniformDeflection:
    """
    This class computes a distribution of points on a curve.
    The points may respect the deflection.
    The algorithm is not based on the classical prediction (with second derivative of curve),
    but either on the evaluation of the distance between the mid point
    and the point of mid parameter of the two points,
    or the distance between the mid point and the point at parameter 0.5
    on the cubic interpolation of the two points and their tangents.

    Note: this algorithm is faster than a GCPnts_UniformDeflection algorithm,
    and is able to work with non-"C2" continuous curves.
    However, it generates more points in the distribution.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty algorithm.
        To define the problem to be solved, use the function Initialize().
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theDeflection: float, theContinuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None: ...

    @overload
    def __init__(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theDeflection: float, theContinuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None:
        """
        Computes a QuasiUniform Deflection distribution of points on the Curve.
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theDeflection: float, theU1: float, theU2: float, theContinuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None:
        """
        Computes a QuasiUniform Deflection distribution of points on a part of the Curve.
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theDeflection: float, theU1: float, theU2: float, theContinuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None:
        """
        Computes a QuasiUniform Deflection distribution of points on a part of the Curve.
        This and the above algorithms compute a distribution of points:
        -   on the curve theC, or
        -   on the part of curve theC limited by the two parameter values theU1 and theU2,
        where the deflection resulting from the distributed
        points is not greater than theDeflection.

        The first point of the distribution is either the origin of
        curve theC or the point of parameter theU1.
        The last point of the distribution is either the end point
        of curve theC or the point of parameter theU2.

        Intermediate points of the distribution are built such
        that the deflection is not greater than theDeflection.
        Using the following evaluation of the deflection:
        if Pi and Pj are two consecutive points of the
        distribution, respectively of parameter ui and uj on the curve,
        the deflection is the distance between:
        -   the mid-point of Pi and Pj (the center of the chord joining these two points)
        -   and the point of mid-parameter of these two
        points (the point of parameter [(ui+uj) / 2] on curve theC).
        theContinuity, defaulted to GeomAbs_C1, gives the degree of continuity of the curve theC.
        (Note that C is an Adaptor3d_Curve or an Adaptor2d_Curve2d object,
        and does not know the degree of continuity of the underlying curve).
        Use the function IsDone() to verify that the computation was successful,
        the function NbPoints() to obtain the number of points of the computed distribution,
        and the function Parameter() to read the parameter of each point.

        Warning
        -   The roles of theU1 and theU2 are inverted if theU1 > theU2.
        -   Derivative functions on the curve are called according to theContinuity.
        An error may occur if theContinuity is greater than
        the real degree of continuity of the curve.

        Warning
        theC is an adapted curve, i.e. an object which is an interface between:
        -   the services provided by either a 2D curve from
        the package Geom2d (in the case of an Adaptor2d_Curve2d curve)
        or a 3D curve from the package Geom (in the case of an Adaptor3d_Curve curve),
        -   and those required on the curve by the computation algorithm.
        """

    @overload
    def __init__(self, theOther: GCPnts_QuasiUniformDeflection) -> None: ...

    @overload
    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theDeflection: float, theContinuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None:
        """Initialize the algorithms with 3D curve and deflection."""

    @overload
    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theDeflection: float, theContinuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None:
        """Initialize the algorithms with 2D curve and deflection."""

    @overload
    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theDeflection: float, theU1: float, theU2: float, theContinuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None:
        """
        Initialize the algorithms with 3D curve, deflection and parameter range.
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theDeflection: float, theU1: float, theU2: float, theContinuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None:
        """
        Initialize the algorithms with theC, theDeflection, theU1, theU2.
        This and the above algorithms initialize (or reinitialize)
        this algorithm and compute a distribution of points:
        -   on the curve theC, or
        -   on the part of curve theC limited by the two parameter values theU1 and theU2,
        where the deflection resulting from the distributed
        points is not greater than theDeflection.

        The first point of the distribution is either the origin
        of curve theC or the point of parameter theU1.
        The last point of the distribution is either the end point of
        curve theC or the point of parameter theU2.

        Intermediate points of the distribution are built in
        such a way that the deflection is not greater than theDeflection.
        Using the following evaluation of the deflection:
        if Pi and Pj are two consecutive points of the distribution,
        respectively of parameter ui and uj on the curve,
        the deflection is the distance between:
        -   the mid-point of Pi and Pj (the center of the chord joining these two points)
        -   and the point of mid-parameter of these two
        points (the point of parameter [(ui+uj) / 2] on curve theC).
        theContinuity, defaulted to GeomAbs_C1, gives the degree of continuity of the curve theC.
        (Note that C is an Adaptor3d_Curve or an Adaptor2d_Curve2d object,
        and does not know the degree of continuity of the underlying curve).
        Use the function IsDone to verify that the computation was successful,
        the function NbPoints() to obtain the number of points of the computed distribution,
        and the function Parameter() to read the parameter of each point.

        Warning
        -   The roles of theU1 and theU2 are inverted if theU1 > theU2.
        -   Derivative functions on the curve are called according to theContinuity.
        An error may occur if theContinuity is greater than
        the real degree of continuity of the curve.

        Warning
        theC is an adapted curve, i.e. an object which is an interface between:
        -   the services provided by either a 2D curve from
        the package Geom2d (in the case of an Adaptor2d_Curve2d curve)
        or a 3D curve from the package Geom (in the case of an Adaptor3d_Curve curve),
        and those required on the curve by the computation algorithm.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computation was successful.
        IsDone is a protection against:
        -   non-convergence of the algorithm
        -   querying the results before computation.
        """

    def NbPoints(self) -> int:
        """
        Returns the number of points of the distribution
        computed by this algorithm.
        Exceptions
        StdFail_NotDone if this algorithm has not been
        initialized, or if the computation was not successful.
        """

    def Parameter(self, Index: int) -> float:
        """
        Returns the parameter of the point of index Index in
        the distribution computed by this algorithm.
        Warning
        Index must be greater than or equal to 1, and less
        than or equal to the number of points of the
        distribution. However, pay particular attention as this
        condition is not checked by this function.
        Exceptions
        StdFail_NotDone if this algorithm has not been
        initialized, or if the computation was not successful.
        """

    def Value(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        Returns the point of index Index in the distribution
        computed by this algorithm.
        Warning
        Index must be greater than or equal to 1, and less
        than or equal to the number of points of the
        distribution. However, pay particular attention as this
        condition is not checked by this function.
        Exceptions
        StdFail_NotDone if this algorithm has not been
        initialized, or if the computation was not successful.
        """

    def Deflection(self) -> float:
        """
        Returns the deflection between the curve and the
        polygon resulting from the points of the distribution
        computed by this algorithm.
        This is the value given to the algorithm at the time
        of construction (or initialization).
        Exceptions
        StdFail_NotDone if this algorithm has not been
        initialized, or if the computation was not successful.
        """

class GCPnts_TangentialDeflection:
    """
    Computes a set of points on a curve from package
    Adaptor3d such as between two successive points
    P1(u1)and P2(u2) :
    @code
    . ||P1P3^P3P2||/||P1P3||*||P3P2||<AngularDeflection
    . ||P1P2^P1P3||/||P1P2||<CurvatureDeflection
    @endcode
    where P3 is the point of abscissa ((u1+u2)/2), with
    u1 the abscissa of the point P1 and u2 the abscissa
    of the point P2.

    ^ is the cross product of two vectors, and ||P1P2||
    the magnitude of the vector P1P2.

    The conditions AngularDeflection > gp::Resolution()
    and CurvatureDeflection > gp::Resolution() must be
    satisfied at the construction time.

    A minimum number of points can be fixed for a linear or circular element.
    Example:
    @code
    occ::handle<Geom_BezierCurve> aCurve = new Geom_BezierCurve (thePoles);
    GeomAdaptor_Curve aCurveAdaptor (aCurve);
    double aCDeflect  = 0.01; // Curvature deflection
    double anADeflect = 0.09; // Angular   deflection

    GCPnts_TangentialDeflection aPointsOnCurve;
    aPointsOnCurve.Initialize (aCurveAdaptor, anADeflect, aCDeflect);
    for (int i = 1; i <= aPointsOnCurve.NbPoints(); ++i)
    {
    double aU   = aPointsOnCurve.Parameter (i);
    gp_Pnt aPnt = aPointsOnCurve.Value (i);
    }
    @endcode
    """

    @overload
    def __init__(self) -> None:
        """
        Empty constructor.
        @sa Initialize()
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theAngularDeflection: float, theCurvatureDeflection: float, theMinimumOfPoints: int = 2, theUTol: float = 1e-09, theMinLen: float = 1e-07) -> None:
        """
        Constructor for 3D curve.
        @param[in] theC  3d curve
        @param[in] theAngularDeflection    angular deflection in radians
        @param[in] theCurvatureDeflection  linear deflection
        @param[in] theMinimumOfPoints  minimum number of points
        @param[in] theUTol    tolerance in curve parametric scope
        @param[in] theMinLen  minimal length
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theAngularDeflection: float, theCurvatureDeflection: float, theMinimumOfPoints: int = 2, theUTol: float = 1e-09, theMinLen: float = 1e-07) -> None:
        """
        Constructor for 2D curve.
        @param[in] theC  2d curve
        @param[in] theAngularDeflection    angular deflection in radians
        @param[in] theCurvatureDeflection  linear deflection
        @param[in] theMinimumOfPoints  minimum number of points
        @param[in] theUTol    tolerance in curve parametric scope
        @param[in] theMinLen  minimal length
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theFirstParameter: float, theLastParameter: float, theAngularDeflection: float, theCurvatureDeflection: float, theMinimumOfPoints: int = 2, theUTol: float = 1e-09, theMinLen: float = 1e-07) -> None:
        """
        Constructor for 3D curve with restricted range.
        @param[in] theC  3d curve
        @param[in] theFirstParameter  first parameter on curve
        @param[in] theLastParameter   last  parameter on curve
        @param[in] theAngularDeflection    angular deflection in radians
        @param[in] theCurvatureDeflection  linear deflection
        @param[in] theMinimumOfPoints  minimum number of points
        @param theUTo  l[in]  tolerance in curve parametric scope
        @param[in] theMinLen  minimal length
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theFirstParameter: float, theLastParameter: float, theAngularDeflection: float, theCurvatureDeflection: float, theMinimumOfPoints: int = 2, theUTol: float = 1e-09, theMinLen: float = 1e-07) -> None:
        """
        Constructor for 2D curve with restricted range.
        @param[in] theC  2d curve
        @param[in] theFirstParameter  first parameter on curve
        @param[in] theLastParameter   last  parameter on curve
        @param[in] theAngularDeflection    angular deflection in radians
        @param[in] theCurvatureDeflection  linear deflection
        @param[in] theMinimumOfPoints  minimum number of points
        @param[in] theUTol    tolerance in curve parametric scope
        @param[in] theMinLen  minimal length
        """

    @overload
    def __init__(self, theOther: GCPnts_TangentialDeflection) -> None: ...

    @overload
    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theAngularDeflection: float, theCurvatureDeflection: float, theMinimumOfPoints: int = 2, theUTol: float = 1e-09, theMinLen: float = 1e-07) -> None:
        """
        Initialize algorithm for 3D curve.
        @param[in] theC  3d curve
        @param[in] theAngularDeflection    angular deflection in radians
        @param[in] theCurvatureDeflection  linear deflection
        @param[in] theMinimumOfPoints  minimum number of points
        @param[in] theUTol    tolerance in curve parametric scope
        @param[in] theMinLen  minimal length
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theFirstParameter: float, theLastParameter: float, theAngularDeflection: float, theCurvatureDeflection: float, theMinimumOfPoints: int = 2, theUTol: float = 1e-09, theMinLen: float = 1e-07) -> None:
        """
        Initialize algorithm for 3D curve with restricted range.
        @param[in] theC  3d curve
        @param[in] theFirstParameter  first parameter on curve
        @param[in] theLastParameter   last  parameter on curve
        @param[in] theAngularDeflection    angular deflection in radians
        @param[in] theCurvatureDeflection  linear deflection
        @param[in] theMinimumOfPoints  minimum number of points
        @param[in] theUTol    tolerance in curve parametric scope
        @param[in] theMinLen  minimal length
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theAngularDeflection: float, theCurvatureDeflection: float, theMinimumOfPoints: int = 2, theUTol: float = 1e-09, theMinLen: float = 1e-07) -> None:
        """
        Initialize algorithm for 2D curve.
        @param[in] theC  2d curve
        @param[in] theAngularDeflection    angular deflection in radians
        @param[in] theCurvatureDeflection  linear deflection
        @param[in] theMinimumOfPoints  minimum number of points
        @param[in] theUTol    tolerance in curve parametric scope
        @param[in] theMinLen  minimal length
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theFirstParameter: float, theLastParameter: float, theAngularDeflection: float, theCurvatureDeflection: float, theMinimumOfPoints: int = 2, theUTol: float = 1e-09, theMinLen: float = 1e-07) -> None:
        """
        Initialize algorithm for 2D curve with restricted range.
        @param[in] theC  2d curve
        @param[in] theFirstParameter  first parameter on curve
        @param[in] theLastParameter   last  parameter on curve
        @param[in] theAngularDeflection    angular deflection in radians
        @param[in] theCurvatureDeflection  linear deflection
        @param[in] theMinimumOfPoints  minimum number of points
        @param[in] theUTol    tolerance in curve parametric scope
        @param[in] theMinLen  minimal length
        """

    def AddPoint(self, thePnt: nanoocp.gp.gp_Pnt, theParam: float, theIsReplace: bool = True) -> int:
        """
        Add point to already calculated points (or replace existing)
        Returns index of new added point
        or founded with parametric tolerance (replaced if theIsReplace is true)
        """

    def NbPoints(self) -> int: ...

    def Parameter(self, I: int) -> float: ...

    def Value(self, I: int) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def ArcAngularStep(theRadius: float, theLinearDeflection: float, theAngularDeflection: float, theMinLength: float) -> float:
        """Computes angular step for the arc using the given parameters."""

class GCPnts_DistFunctionMV(nanoocp.math.math_MultipleVarFunction):
    """
    The same as class GCPnts_DistFunction, but it can be used in minimization algorithms that
    requires multi variable function
    """

    @overload
    def __init__(self, theCurvLinDist: "GCPnts_DistFunction") -> None: ...

    @overload
    def __init__(self, theOther: GCPnts_DistFunctionMV) -> None: ...

    def Value(self, X: nanoocp.math.math_Vector) -> tuple[bool, float]: ...

    def NbVariables(self) -> int: ...

class GCPnts_DistFunction2dMV(nanoocp.math.math_MultipleVarFunction):
    """
    The same as class GCPnts_DistFunction2d,
    but it can be used in minimization algorithms that
    requires multi variable function
    """

    @overload
    def __init__(self, theCurvLinDist: "GCPnts_DistFunction2d") -> None: ...

    @overload
    def __init__(self, theOther: GCPnts_DistFunction2dMV) -> None: ...

    def Value(self, X: nanoocp.math.math_Vector) -> tuple[bool, float]: ...

    def NbVariables(self) -> int: ...

class GCPnts_TCurveTypes__Adaptor3d_Curve:
    """Auxiliary tool to resolve 3D curve classes."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GCPnts_TCurveTypes__Adaptor3d_Curve) -> None: ...

class GCPnts_TCurveTypes__Adaptor2d_Curve2d:
    """Auxiliary tool to resolve 2D curve classes."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GCPnts_TCurveTypes__Adaptor2d_Curve2d) -> None: ...

class GCPnts_UniformAbscissa:
    """
    This class allows to compute a uniform distribution of points
    on a curve (i.e. the points will all be equally distant).
    """

    @overload
    def __init__(self) -> None:
        """creation of a indefinite UniformAbscissa"""

    @overload
    def __init__(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theAbscissa: float, theToler: float = -1.0) -> None:
        """
        Computes a uniform abscissa distribution of points on the 3D curve.
        @param[in] theC  input curve
        @param[in] theAbscissa  abscissa (distance between two consecutive points)
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theNbPoints: int, theToler: float = -1.0) -> None:
        """
        Computes a uniform abscissa distribution of points on the 3D Curve.
        @param[in] theC  input curve
        @param[in] theNbPoints  defines the number of desired points
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theAbscissa: float, theToler: float = -1.0) -> None:
        """
        Computes a uniform abscissa distribution of points on the 2D curve.
        @param[in] theC  input curve
        @param[in] theAbscissa  abscissa (distance between two consecutive points)
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theNbPoints: int, theToler: float = -1.0) -> None:
        """
        Computes a uniform abscissa distribution of points on the 2D Curve.
        @param[in] theC  input curve
        @param[in] theNbPoints  defines the number of desired points
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theAbscissa: float, theU1: float, theU2: float, theToler: float = -1.0) -> None:
        """
        Computes a Uniform abscissa distribution of points on a part of the 3D Curve.
        @param[in] theC  input curve
        @param[in] theAbscissa  abscissa (distance between two consecutive points)
        @param[in] theU1  first parameter on curve
        @param[in] theU2  last  parameter on curve
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theNbPoints: int, theU1: float, theU2: float, theToler: float = -1.0) -> None:
        """
        Computes a Uniform abscissa distribution of points on a part of the 3D Curve.
        @param[in] theC  input curve
        @param[in] theNbPoints  defines the number of desired points
        @param[in] theU1  first parameter on curve
        @param[in] theU2  last  parameter on curve
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theAbscissa: float, theU1: float, theU2: float, theToler: float = -1.0) -> None:
        """
        Computes a Uniform abscissa distribution of points on a part of the 2D Curve.
        @param[in] theC  input curve
        @param[in] theAbscissa  abscissa (distance between two consecutive points)
        @param[in] theU1  first parameter on curve
        @param[in] theU2  last  parameter on curve
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theNbPoints: int, theU1: float, theU2: float, theToler: float = -1.0) -> None:
        """
        Computes a Uniform abscissa distribution of points on a part of the 2D Curve.
        @param[in] theC  input curve
        @param[in] theNbPoints  defines the number of desired points
        @param[in] theU1  first parameter on curve
        @param[in] theU2  last  parameter on curve
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    @overload
    def __init__(self, theOther: GCPnts_UniformAbscissa) -> None: ...

    @overload
    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theAbscissa: float, theToler: float = -1.0) -> None:
        """
        Initialize the algorithms with 3D curve, Abscissa, and Tolerance.
        @param[in] theC  input curve
        @param[in] theAbscissa  abscissa (distance between two consecutive points)
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theAbscissa: float, theU1: float, theU2: float, theToler: float = -1.0) -> None:
        """
        Initialize the algorithms with 3D curve, Abscissa, Tolerance, and parameter range.
        @param[in] theC  input curve
        @param[in] theAbscissa  abscissa (distance between two consecutive points)
        @param[in] theU1  first parameter on curve
        @param[in] theU2  last  parameter on curve
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theNbPoints: int, theToler: float = -1.0) -> None:
        """
        Initialize the algorithms with 3D curve, number of points, and Tolerance.
        @param[in] theC  input curve
        @param[in] theNbPoints  defines the number of desired points
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theNbPoints: int, theU1: float, theU2: float, theToler: float = -1.0) -> None:
        """
        Initialize the algorithms with 3D curve, number of points, Tolerance, and parameter range.
        @param[in] theC  input curve
        @param[in] theNbPoints  defines the number of desired points
        @param[in] theU1  first parameter on curve
        @param[in] theU2  last  parameter on curve
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theAbscissa: float, theToler: float = -1.0) -> None:
        """
        Initialize the algorithms with 2D curve, Abscissa, and Tolerance.
        @param[in] theC  input curve
        @param[in] theAbscissa  abscissa (distance between two consecutive points)
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theAbscissa: float, theU1: float, theU2: float, theToler: float = -1.0) -> None:
        """
        Initialize the algorithms with 2D curve, Abscissa, Tolerance, and parameter range.
        @param[in] theC  input curve
        @param[in] theAbscissa  abscissa (distance between two consecutive points)
        @param[in] theU1  first parameter on curve
        @param[in] theU2  last  parameter on curve
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theNbPoints: int, theToler: float = -1.0) -> None:
        """
        Initialize the algorithms with 2D curve, number of points, and Tolerance.
        @param[in] theC  input curve
        @param[in] theNbPoints  defines the number of desired points
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    @overload
    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theNbPoints: int, theU1: float, theU2: float, theToler: float = -1.0) -> None:
        """
        Initialize the algorithms with 2D curve, number of points, Tolerance, and parameter range.
        @param[in] theC  input curve
        @param[in] theNbPoints  defines the number of desired points
        @param[in] theU1  first parameter on curve
        @param[in] theU2  last  parameter on curve
        @param[in] theToler  used for more precise calculation of curve length
        (Precision::Confusion() by default)
        """

    def IsDone(self) -> bool: ...

    def NbPoints(self) -> int: ...

    def Parameter(self, Index: int) -> float:
        """returns the computed Parameter of index <Index>."""

    def Abscissa(self) -> float:
        """
        Returns the current abscissa, i.e. the distance between two consecutive points.
        """

class GCPnts_UniformDeflection:
    """
    Provides an algorithm to compute a distribution of
    points on a 'C2' continuous curve.
    The algorithm respects a criterion of maximum deflection between
    the curve and the polygon that results from the computed points.
    Note: This algorithm is relatively time consuming.
    A GCPnts_QuasiUniformDeflection algorithm is quicker;
    it can also work with non-'C2' continuous curves,
    but it generates more points in the distribution.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty algorithm.
        To define the problem to be solved, use the function Initialize.
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theDeflection: float, theWithControl: bool = True) -> None:
        """
        Computes a uniform Deflection distribution of points on the curve.
        @param[in] theC  input 3D curve
        @param[in] theDeflection  target deflection
        @param[in] theWithControl  when TRUE, the algorithm controls the estimate deflection
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theDeflection: float, theWithControl: bool = True) -> None:
        """
        Computes a uniform Deflection distribution of points on the curve.
        @param[in] theC  input 2D curve
        @param[in] theDeflection  target deflection
        @param[in] theWithControl  when TRUE, the algorithm controls the estimate deflection
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theDeflection: float, theU1: float, theU2: float, theWithControl: bool = True) -> None:
        """
        Computes a Uniform Deflection distribution of points on a part of the curve.
        @param[in] theC  input 3D curve
        @param[in] theDeflection  target deflection
        @param[in] theU1  first parameter on curve
        @param[in] theU2  last  parameter on curve
        @param[in] theWithControl  when TRUE, the algorithm controls the estimate deflection
        """

    @overload
    def __init__(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theDeflection: float, theU1: float, theU2: float, theWithControl: bool = True) -> None:
        """
        Computes a Uniform Deflection distribution of points on a part of the curve.
        @param[in] theC  input 2D curve
        @param[in] theDeflection  target deflection
        @param[in] theU1  first parameter on curve
        @param[in] theU2  last  parameter on curve
        @param[in] theWithControl  when TRUE, the algorithm controls the estimate deflection
        """

    @overload
    def __init__(self, theOther: GCPnts_UniformDeflection) -> None: ...

    @overload
    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theDeflection: float, theWithControl: bool = True) -> None:
        """Initialize the algorithms with 3D curve and deflection."""

    @overload
    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theDeflection: float, theWithControl: bool = True) -> None:
        """Initialize the algorithms with 2D curve and deflection."""

    @overload
    def Initialize(self, theC: nanoocp.Adaptor3d.Adaptor3d_Curve, theDeflection: float, theU1: float, theU2: float, theWithControl: bool = True) -> None:
        """Initialize the algorithms with 3D curve, deflection, parameter range."""

    @overload
    def Initialize(self, theC: nanoocp.Adaptor2d.Adaptor2d_Curve2d, theDeflection: float, theU1: float, theU2: float, theWithControl: bool = True) -> None:
        """
        Initialize the algorithms with curve, deflection, parameter range.
        This and the above methods initialize (or reinitialize) this algorithm and
        compute a distribution of points:
        -   on the curve theC, or
        -   on the part of curve theC limited by the two parameter values theU1 and theU2,
        where the maximum distance between theC and the
        polygon that results from the points of the
        distribution is not greater than theDeflection.
        The first point of the distribution is either the origin
        of curve theC or the point of parameter theU1.
        The last point of the distribution is either the end point of
        curve theC or the point of parameter theU2.
        Intermediate points of the distribution are built using
        interpolations of segments of the curve limited at the 2nd degree.
        The construction ensures, in a first step,
        that the chordal deviation for this
        interpolation of the curve is less than or equal to theDeflection.
        However, it does not ensure that the chordal deviation
        for the curve itself is less than or equal to theDeflection.
        To do this a check is necessary,
        which may generate (second step) additional intermediate points.
        This check is time consuming, and can be avoided by setting theWithControl to false.
        Note that by default theWithControl is true and check is performed.
        Use the function IsDone to verify that the computation was successful,
        the function NbPoints() to obtain the number of points of the computed distribution,
        and the function Parameter to read the parameter of each point.

        Warning
        -   theC is necessary, 'C2' continuous.
        This property is not checked at construction time.
        -   The roles of theU1 and theU2 are inverted if theU1 > theU2.

        Warning
        theC is an adapted curve, i.e. an object which is an interface between:
        -   the services provided by either a 2D curve from
        the package Geom2d (in the case of an Adaptor2d_Curve2d curve)
        or a 3D curve from the package Geom (in the case of an Adaptor3d_Curve curve),
        -   and those required on the curve by the computation algorithm.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computation was successful.
        IsDone is a protection against:
        -   non-convergence of the algorithm
        -   querying the results before computation.
        """

    def NbPoints(self) -> int:
        """
        Returns the number of points of the distribution
        computed by this algorithm.
        Exceptions
        StdFail_NotDone if this algorithm has not been
        initialized, or if the computation was not successful.
        """

    def Parameter(self, Index: int) -> float:
        """
        Returns the parameter of the point of index Index in
        the distribution computed by this algorithm.
        Warning
        Index must be greater than or equal to 1, and less
        than or equal to the number of points of the
        distribution. However, pay particular attention as this
        condition is not checked by this function.
        Exceptions
        StdFail_NotDone if this algorithm has not been
        initialized, or if the computation was not successful.
        """

    def Value(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        Returns the point of index Index in the distribution
        computed by this algorithm.
        Warning
        Index must be greater than or equal to 1, and less
        than or equal to the number of points of the
        distribution. However, pay particular attention as this
        condition is not checked by this function.
        Exceptions
        StdFAil_NotDone if this algorithm has not been
        initialized, or if the computation was not successful.
        """

    def Deflection(self) -> float:
        """
        Returns the deflection between the curve and the
        polygon resulting from the points of the distribution
        computed by this algorithm.
        This value is the one given to the algorithm at the
        time of construction (or initialization).
        Exceptions
        StdFail_NotDone if this algorithm has not been
        initialized, or if the computation was not successful.
        """
