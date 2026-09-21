"""OCCT package GeomConvert (toolkit TKGeomBase)"""

import enum
from typing import overload

import nanoocp.Adaptor3d
import nanoocp.Convert
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.gp
import nanoocp.math


class GeomConvert_ConvType(enum.IntEnum):
    GeomConvert_Target = 0

    GeomConvert_Simplest = 1

    GeomConvert_MinGap = 2

GeomConvert_Target: GeomConvert_ConvType = GeomConvert_ConvType.GeomConvert_Target

GeomConvert_Simplest: GeomConvert_ConvType = GeomConvert_ConvType.GeomConvert_Simplest

GeomConvert_MinGap: GeomConvert_ConvType = GeomConvert_ConvType.GeomConvert_MinGap

class GeomConvert:
    """
    The GeomConvert package provides some global functions as follows
    -   converting classical Geom curves into BSpline curves,
    -   segmenting BSpline curves, particularly at knots
    values: this function may be used in conjunction with the
    GeomConvert_BSplineCurveKnotSplitting
    class to segment a BSpline curve into arcs which
    comply with required continuity levels,
    -   converting classical Geom surfaces into BSpline surfaces, and
    -   segmenting BSpline surfaces, particularly at
    knots values: this function may be used in conjunction with the
    GeomConvert_BSplineSurfaceKnotSplitting
    class to segment a BSpline surface into patches
    which comply with required continuity levels.
    All geometric entities used in this package are bounded.

    References :
    . Generating the Bezier Points of B-spline curves and surfaces
    (Wolfgang Bohm) CAGD volume 13 number 6 november 1981
    . On NURBS: A Survey (Leslie Piegl) IEEE Computer Graphics and
    Application January 1991
    . Curve and surface construction using rational B-splines
    (Leslie Piegl and Wayne Tiller) CAD Volume 19 number 9 november
    1987
    . A survey of curve and surface methods in CAGD (Wolfgang BOHM)
    CAGD 1 1984
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomConvert) -> None: ...

    @overload
    @staticmethod
    def SplitBSplineCurve(C: nanoocp.Geom.Geom_BSplineCurve | None, FromK1: int, ToK2: int, SameOrientation: bool = True) -> nanoocp.Geom.Geom_BSplineCurve:
        """
        Convert a curve from Geom by an approximation method

        This method computes the arc of B-spline curve between the two
        knots FromK1 and ToK2. If C is periodic the arc has the same
        orientation as C if SameOrientation = true.
        If C is not periodic SameOrientation is not used for the
        computation and C is oriented from the knot fromK1 to the knot toK2.
        We just keep the local definition of C between the knots
        FromK1 and ToK2. The returned B-spline curve has its first
        and last knots with a multiplicity equal to degree + 1, where
        degree is the polynomial degree of C.
        The indexes of the knots FromK1 and ToK2 doesn't include the
        repetition of multiple knots in their definition.
        Raised if FromK1 = ToK2
        Raised if FromK1 or ToK2 are out of the bounds
        [FirstUKnotIndex, LastUKnotIndex]
        """

    @overload
    @staticmethod
    def SplitBSplineCurve(C: nanoocp.Geom.Geom_BSplineCurve | None, FromU1: float, ToU2: float, ParametricTolerance: float, SameOrientation: bool = True) -> nanoocp.Geom.Geom_BSplineCurve:
        """
        This function computes the segment of B-spline curve between the
        parametric values FromU1, ToU2.
        If C is periodic the arc has the same orientation as C if
        SameOrientation = True.
        If C is not periodic SameOrientation is not used for the
        computation and C is oriented fromU1 toU2.
        If U1 and U2 and two parametric values we consider that
        U1 = U2 if Abs (U1 - U2) <= ParametricTolerance and
        ParametricTolerance must be greater or equal to Resolution
        from package gp.

        Raised if FromU1 or ToU2 are out of the parametric bounds of the
        curve (The tolerance criterion is ParametricTolerance).
        Raised if Abs (FromU1 - ToU2) <= ParametricTolerance
        Raised if ParametricTolerance < Resolution from gp.
        """

    @overload
    @staticmethod
    def SplitBSplineSurface(S: nanoocp.Geom.Geom_BSplineSurface | None, FromUK1: int, ToUK2: int, FromVK1: int, ToVK2: int, SameUOrientation: bool = True, SameVOrientation: bool = True) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        Computes the B-spline surface patche between the knots values
        FromUK1, ToUK2, FromVK1, ToVK2.
        If S is periodic in one direction the patche has the same
        orientation as S in this direction if the flag is true in this
        direction (SameUOrientation, SameVOrientation).
        If S is not periodic SameUOrientation and SameVOrientation are not
        used for the computation and S is oriented FromUK1 ToUK2 and
        FromVK1 ToVK2.
        Raised if
        FromUK1 = ToUK2 or FromVK1 = ToVK2
        FromUK1 or ToUK2 are out of the bounds
        [FirstUKnotIndex, LastUKnotIndex]
        FromVK1 or ToVK2 are out of the bounds
        [FirstVKnotIndex, LastVKnotIndex]
        """

    @overload
    @staticmethod
    def SplitBSplineSurface(S: nanoocp.Geom.Geom_BSplineSurface | None, FromK1: int, ToK2: int, USplit: bool, SameOrientation: bool = True) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        This method splits a B-spline surface patche between the
        knots values FromK1, ToK2 in one direction.
        If USplit = True then the splitting direction is the U parametric
        direction else it is the V parametric direction.
        If S is periodic in the considered direction the patche has the
        same orientation as S in this direction if SameOrientation is True
        If S is not periodic in this direction SameOrientation is not used
        for the computation and S is oriented FromK1 ToK2.
        Raised if FromK1 = ToK2 or if
        FromK1 or ToK2 are out of the bounds
        [FirstUKnotIndex, LastUKnotIndex] in the
        considered parametric direction.
        """

    @overload
    @staticmethod
    def SplitBSplineSurface(S: nanoocp.Geom.Geom_BSplineSurface | None, FromU1: float, ToU2: float, FromV1: float, ToV2: float, ParametricTolerance: float, SameUOrientation: bool = True, SameVOrientation: bool = True) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        This method computes the B-spline surface patche between the
        parametric values FromU1, ToU2, FromV1, ToV2.
        If S is periodic in one direction the patche has the same
        orientation as S in this direction if the flag is True in this
        direction (SameUOrientation, SameVOrientation).
        If S is not periodic SameUOrientation and SameVOrientation are not
        used for the computation and S is oriented FromU1 ToU2 and
        FromV1 ToV2.
        If U1 and U2 and two parametric values we consider that U1 = U2 if
        Abs (U1 - U2) <= ParametricTolerance and ParametricTolerance must
        be greater or equal to Resolution from package gp.

        Raised if FromU1 or ToU2 or FromV1 or ToU2 are out of the
        parametric bounds of the surface (the tolerance criterion is
        ParametricTolerance).
        Raised if Abs (FromU1 - ToU2) <= ParametricTolerance or
        Abs (FromV1 - ToV2) <= ParametricTolerance.
        Raised if ParametricTolerance < Resolution.
        """

    @overload
    @staticmethod
    def SplitBSplineSurface(S: nanoocp.Geom.Geom_BSplineSurface | None, FromParam1: float, ToParam2: float, USplit: bool, ParametricTolerance: float, SameOrientation: bool = True) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        This method splits the B-spline surface S in one direction
        between the parametric values FromParam1, ToParam2.
        If USplit = True then the Splitting direction is the U parametric
        direction else it is the V parametric direction.
        If S is periodic in the considered direction the patche has
        the same orientation as S in this direction if SameOrientation
        is true.
        If S is not periodic in the considered direction SameOrientation
        is not used for the computation and S is oriented FromParam1
        ToParam2.
        If U1 and U2 and two parametric values we consider that U1 = U2
        if Abs (U1 - U2) <= ParametricTolerance and ParametricTolerance
        must be greater or equal to Resolution from package gp.

        Raises if FromParam1 or ToParam2 are out of the parametric bounds
        of the surface in the considered direction.
        Raises if Abs (FromParam1 - ToParam2) <= ParametricTolerance.
        """

    @staticmethod
    def CurveToBSplineCurve(C: nanoocp.Geom.Geom_Curve | None, Parameterisation: nanoocp.Convert.Convert_ParameterisationType = ...) -> nanoocp.Geom.Geom_BSplineCurve:
        """
        This function converts a non infinite curve from
        Geom into a B-spline curve. C must be an ellipse or a
        circle or a trimmed conic or a trimmed line or a Bezier
        curve or a trimmed Bezier curve or a BSpline curve or a
        trimmed BSpline curve or an OffsetCurve. The returned B-spline is
        not periodic except if C is a Circle or an Ellipse. If
        the Parameterisation is QuasiAngular than the returned
        curve is NOT periodic in case a periodic Geom_Circle or
        Geom_Ellipse. For TgtThetaOver2_1 and TgtThetaOver2_2 the
        method raises an exception in case of a periodic
        Geom_Circle or a Geom_Ellipse ParameterisationType applies
        only if the curve is a Circle or an ellipse:
        TgtThetaOver2, TgtThetaOver2_1, TgtThetaOver2_2,
        TgtThetaOver2_3, TgtThetaOver2_4,

        Purpose: this is the classical rational parameterisation
        2
        1 - t
        cos(theta) = ------
        2
        1 + t

        2t
        sin(theta) = ------
        2
        1 + t

        t = tan (theta/2)

        with TgtThetaOver2 the routine will compute the number of spans
        using the rule num_spans = [ (ULast - UFirst) / 1.2 ] + 1
        with TgtThetaOver2_N, N spans will be forced: an error will
        be raized if (ULast - UFirst) >= PI and N = 1,
        ULast - UFirst >= 2 PI and N = 2

        QuasiAngular,
        here t is a rational function that approximates
        theta ----> tan(theta/2).
        Nevetheless the composing with above function yields exact
        functions whose square sum up to 1
        RationalC1 ;
        t is replaced by a polynomial function of u so as to grant
        C1 contiuity across knots.
        Exceptions
        Standard_DomainError:
        -   if the curve C is infinite, or
        -   if C is a (complete) circle or ellipse, and Parameterisation is equal to
        Convert_TgtThetaOver2_1 or Convert_TgtThetaOver2_2.
        Standard_ConstructionError:
        -   if C is a (complete) circle or ellipse, and if Parameterisation is not equal to
        Convert_TgtThetaOver2, Convert_RationalC1,
        Convert_QuasiAngular (the curve is converted
        in these three cases) or to Convert_TgtThetaOver2_1 or
        Convert_TgtThetaOver2_2 (another exception is raised in these two cases).
        -   if C is a trimmed circle or ellipse, if Parameterisation is equal to
        Convert_TgtThetaOver2_1 and if U2 - U1 > 0.9999 * Pi, where U1 and U2 are
        respectively the first and the last parameters of the
        trimmed curve (this method of parameterization
        cannot be used to convert a half-circle or a half-ellipse, for example), or
        -   if C is a trimmed circle or ellipse, if
        Parameterisation is equal to Convert_TgtThetaOver2_2 and U2 - U1 >
        1.9999 * Pi where U1 and U2 are
        respectively the first and the last parameters of the
        trimmed curve (this method of parameterization
        cannot be used to convert a quasi-complete circle or ellipse).
        """

    @staticmethod
    def SurfaceToBSplineSurface(S: nanoocp.Geom.Geom_Surface | None) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        This algorithm converts a non infinite surface from Geom
        into a B-spline surface.
        S must be a trimmed plane or a trimmed cylinder or a trimmed cone
        or a trimmed sphere or a trimmed torus or a sphere or a torus or
        a Bezier surface of a trimmed Bezier surface or a trimmed swept
        surface with a corresponding basis curve which can be turned into
        a B-spline curve (see the method CurveToBSplineCurve).
        Raises DomainError if the type of the surface is not previously defined.
        """

    @staticmethod
    def ConcatG1(ArrayOfCurves: nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_BSplineCurve], ArrayOfToler: nanoocp.NCollection.NCollection_Array1[float], ClosedTolerance: float) -> tuple[nanoocp.NCollection.NCollection_HArray1[nanoocp.Geom.Geom_BSplineCurve], bool]:
        """
        This Method concatenates G1 the ArrayOfCurves as far
        as it is possible.
        ArrayOfCurves[0..N-1]
        ArrayOfToler contains the biggest tolerance of the two
        points shared by two consecutives curves.
        Its dimension: [0..N-2]
        ClosedFlag indicates if the ArrayOfCurves is closed.
        In this case ClosedTolerance contains the biggest tolerance
        of the two points which are at the closure.
        Otherwise its value is 0.0
        ClosedFlag becomes False on the output
        if it is impossible to build closed curve.
        """

    @overload
    @staticmethod
    def ConcatC1(ArrayOfCurves: nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_BSplineCurve], ArrayOfToler: nanoocp.NCollection.NCollection_Array1[float], ClosedTolerance: float) -> tuple[nanoocp.NCollection.NCollection_HArray1[int], nanoocp.NCollection.NCollection_HArray1[nanoocp.Geom.Geom_BSplineCurve], bool]: ...

    @overload
    @staticmethod
    def ConcatC1(ArrayOfCurves: nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_BSplineCurve], ArrayOfToler: nanoocp.NCollection.NCollection_Array1[float], ClosedTolerance: float, AngularTolerance: float) -> tuple[nanoocp.NCollection.NCollection_HArray1[int], nanoocp.NCollection.NCollection_HArray1[nanoocp.Geom.Geom_BSplineCurve], bool]:
        """
        This Method concatenates C1 the ArrayOfCurves as far
        as it is possible.
        ArrayOfCurves[0..N-1]
        ArrayOfToler contains the biggest tolerance of the two
        points shared by two consecutives curves.
        Its dimension: [0..N-2]
        ClosedFlag indicates if the ArrayOfCurves is closed.
        In this case ClosedTolerance contains the biggest tolerance
        of the two points which are at the closure.
        Otherwise its value is 0.0
        ClosedFlag becomes False on the output
        if it is impossible to build closed curve.
        """

    @staticmethod
    def C0BSplineToC1BSplineCurve(BS: nanoocp.Geom.Geom_BSplineCurve | None, tolerance: float, AngularTolerance: float = 1e-07) -> nanoocp.Geom.Geom_BSplineCurve:
        """
        This Method reduces as far as it is possible the
        multiplicities of the knots of the BSpline BS.(keeping the
        geometry). It returns a new BSpline which could still be C0.
        tolerance is a geometrical tolerance.
        The Angular toleranceis in radians and measures the angle of
        the tangents on the left and on the right to decide if the
        curve is G1 or not at a given point
        """

    @overload
    @staticmethod
    def C0BSplineToArrayOfC1BSplineCurve(BS: nanoocp.Geom.Geom_BSplineCurve | None, tolerance: float) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Geom.Geom_BSplineCurve]:
        """
        This Method reduces as far as it is possible the
        multiplicities of the knots of the BSpline BS.(keeping the geometry).
        It returns an array of BSpline C1. tolerance is a geometrical tolerance.
        """

    @overload
    @staticmethod
    def C0BSplineToArrayOfC1BSplineCurve(BS: nanoocp.Geom.Geom_BSplineCurve | None, AngularTolerance: float, tolerance: float) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Geom.Geom_BSplineCurve]:
        """
        This Method reduces as far as it is possible the
        multiplicities of the knots of the BSpline BS.(keeping the
        geometry). It returns an array of BSpline C1. tolerance is a
        geometrical tolerance : it allows for the maximum deformation
        The Angular tolerance is in radians and measures the angle of
        the tangents on the left and on the right to decide if the curve
        is C1 or not at a given point
        """

class GeomConvert_ApproxCurve:
    """
    A framework to convert a 3D curve to a 3D BSpline.
    This is done by approximation to a BSpline curve within a given tolerance.
    """

    @overload
    def __init__(self, Curve: nanoocp.Geom.Geom_Curve | None, Tol3d: float, Order: nanoocp.GeomAbs.GeomAbs_Shape, MaxSegments: int, MaxDegree: int) -> None:
        """
        Constructs a curve approximation framework defined by -
        -      the conic Curve,
        -      the tolerance value Tol3d,
        -      the degree of continuity Order,
        -      the maximum number of segments
        MaxSegments allowed in the resulting BSpline curve, and
        -      the highest degree MaxDeg which the
        polynomial defining the BSpline curve may have.
        """

    @overload
    def __init__(self, Curve: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Tol3d: float, Order: nanoocp.GeomAbs.GeomAbs_Shape, MaxSegments: int, MaxDegree: int) -> None:
        """
        Constructs a curve approximation framework defined by -
        -      the Curve,
        -      the tolerance value Tol3d,
        -      the degree of continuity Order,
        -      the maximum number of segments
        MaxSegments allowed in the resulting BSpline curve, and
        -      the highest degree MaxDeg which the
        polynomial defining the BSpline curve may have.
        """

    @overload
    def __init__(self, theOther: GeomConvert_ApproxCurve) -> None: ...

    def Curve(self) -> nanoocp.Geom.Geom_BSplineCurve:
        """Returns the BSpline curve resulting from the approximation algorithm."""

    def IsDone(self) -> bool:
        """
        returns true if the approximation has
        been done within required tolerance
        """

    def HasResult(self) -> bool:
        """
        Returns true if the approximation did come out
        with a result that is not NECESSARELY within the required tolerance
        """

    def MaxError(self) -> float:
        """
        Returns the greatest distance between a point on the
        source conic and the BSpline curve resulting from the
        approximation. (>0 when an approximation
        has been done, 0 if no approximation)
        """

    def Dump(self) -> object:
        """Print on the stream o information about the object"""

class GeomConvert_ApproxSurface:
    """
    A framework to convert a surface to a BSpline
    surface. This is done by approximation to a BSpline
    surface within a given tolerance.
    """

    @overload
    def __init__(self, Surf: nanoocp.Geom.Geom_Surface | None, Tol3d: float, UContinuity: nanoocp.GeomAbs.GeomAbs_Shape, VContinuity: nanoocp.GeomAbs.GeomAbs_Shape, MaxDegU: int, MaxDegV: int, MaxSegments: int, PrecisCode: int) -> None:
        """
        Constructs a surface approximation framework defined by
        -   the conic Surf
        -   the tolerance value Tol3d
        -   the degree of continuity UContinuity, VContinuity
        in the directions of the U and V parameters
        -   the highest degree MaxDegU, MaxDegV which
        the polynomial defining the BSpline curve may
        have in the directions of the U and V parameters
        -   the maximum number of segments MaxSegments
        allowed in the resulting BSpline curve
        -   the index of precision PrecisCode.
        """

    @overload
    def __init__(self, Surf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Tol3d: float, UContinuity: nanoocp.GeomAbs.GeomAbs_Shape, VContinuity: nanoocp.GeomAbs.GeomAbs_Shape, MaxDegU: int, MaxDegV: int, MaxSegments: int, PrecisCode: int) -> None:
        """
        Constructs a surface approximation framework defined by
        -   the Surf
        -   the tolerance value Tol3d
        -   the degree of continuity UContinuity, VContinuity
        in the directions of the U and V parameters
        -   the highest degree MaxDegU, MaxDegV which
        the polynomial defining the BSpline curve may
        have in the directions of the U and V parameters
        -   the maximum number of segments MaxSegments
        allowed in the resulting BSpline curve
        -   the index of precision PrecisCode.
        """

    @overload
    def __init__(self, theOther: GeomConvert_ApproxSurface) -> None: ...

    def Surface(self) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        Returns the BSpline surface resulting from the approximation algorithm.
        """

    def IsDone(self) -> bool:
        """Returns true if the approximation has be done"""

    def HasResult(self) -> bool:
        """
        Returns true if the approximation did come out with a result that
        is not NECESSARILY within the required tolerance or a result
        that is not recognized with the wished continuities.
        """

    def MaxError(self) -> float:
        """
        Returns the greatest distance between a point on the
        source conic surface and the BSpline surface
        resulting from the approximation (>0 when an approximation
        has been done, 0 if no  approximation )
        """

    def Dump(self) -> object:
        """Prints on the stream o information on the current state of the object."""

class GeomConvert_BSplineCurveKnotSplitting:
    """
    An algorithm to determine points at which a BSpline
    curve should be split in order to obtain arcs of the same continuity.
    If you require curves with a minimum continuity for
    your computation, it is useful to know the points
    between which an arc has a continuity of a given
    order. The continuity order is given at the construction time.
    For a BSpline curve, the discontinuities are
    localized at the knot values. Between two knot values
    the BSpline is infinitely and continuously
    differentiable. At a given knot, the continuity is equal
    to: Degree - Mult, where Degree is the
    degree of the BSpline curve and Mult is the multiplicity of the knot.
    It is possible to compute the arcs which correspond to
    this splitting using the global function
    SplitBSplineCurve provided by the package GeomConvert.
    A BSplineCurveKnotSplitting object provides a framework for:
    -   defining the curve to be analyzed and the
    required degree of continuity,
    -   implementing the computation algorithm, and
    -   consulting the results.
    """

    @overload
    def __init__(self, BasisCurve: nanoocp.Geom.Geom_BSplineCurve | None, ContinuityRange: int) -> None:
        """
        Determines points at which the BSpline curve
        BasisCurve should be split in order to obtain arcs
        with a degree of continuity equal to ContinuityRange.
        These points are knot values of BasisCurve. They
        are identified by indices in the knots table of BasisCurve.
        Use the available interrogation functions to access
        computed values, followed by the global function
        SplitBSplineCurve (provided by the package GeomConvert) to split the curve.
        Exceptions
        Standard_RangeError if ContinuityRange is less than zero.
        """

    @overload
    def __init__(self, theOther: GeomConvert_BSplineCurveKnotSplitting) -> None: ...

    def NbSplits(self) -> int:
        """
        Returns the number of points at which the analyzed
        BSpline curve should be split, in order to obtain arcs
        with the continuity required by this framework.
        All these points correspond to knot values. Note that
        the first and last points of the curve, which bound the
        first and last arcs, are counted among these splitting points.
        """

    def Splitting(self, SplitValues: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """
        Loads the SplitValues table with the split knots
        values computed in this framework. Each value in the
        table is an index in the knots table of the BSpline
        curve analyzed by this algorithm.
        The values in SplitValues are given in ascending
        order and comprise the indices of the knots which
        give the first and last points of the curve. Use two
        consecutive values from the table as arguments of the
        global function SplitBSplineCurve (provided by the
        package GeomConvert) to split the curve.
        Exceptions
        Standard_DimensionError if the array SplitValues
        was not created with the following bounds:
        -   1, and
        -   the number of split points computed in this
        framework (as given by the function NbSplits).
        """

    def SplitValue(self, Index: int) -> int:
        """
        Returns the split knot of index Index to the split knots
        table computed in this framework. The returned value
        is an index in the knots table of the BSpline curve
        analyzed by this algorithm.
        Notes:
        -   If Index is equal to 1, the corresponding knot
        gives the first point of the curve.
        -   If Index is equal to the number of split knots
        computed in this framework, the corresponding
        point is the last point of the curve.
        Exceptions
        Standard_RangeError if Index is less than 1 or
        greater than the number of split knots computed in this framework.
        """

class GeomConvert_BSplineCurveToBezierCurve:
    """
    An algorithm to convert a BSpline curve into a series
    of adjacent Bezier curves.
    A BSplineCurveToBezierCurve object provides a framework for:
    -   defining the BSpline curve to be converted
    -   implementing the construction algorithm, and
    -   consulting the results.
    References :
    Generating the Bezier points of B-spline curves and surfaces
    (Wolfgang Bohm) CAD volume 13 number 6 november 1981
    """

    @overload
    def __init__(self, BasisCurve: nanoocp.Geom.Geom_BSplineCurve | None) -> None:
        """
        Computes all the data needed to convert the
        BSpline curve BasisCurve into a series of adjacent Bezier arcs.
        """

    @overload
    def __init__(self, BasisCurve: nanoocp.Geom.Geom_BSplineCurve | None, U1: float, U2: float, ParametricTolerance: float) -> None:
        """
        Computes all the data needed to convert
        the portion of the BSpline curve BasisCurve
        limited by the two parameter values U1 and U2 into a series of adjacent Bezier arcs.
        The result consists of a series of BasisCurve arcs
        limited by points corresponding to knot values of the curve.
        Use the available interrogation functions to ascertain
        the number of computed Bezier arcs, and then to
        construct each individual Bezier curve (or all Bezier curves).
        Note: ParametricTolerance is not used.
        Raises DomainError if U1 or U2 are out of the parametric bounds of the basis
        curve [FirstParameter, LastParameter]. The Tolerance criterion
        is ParametricTolerance.
        Raised if Abs (U2 - U1) <= ParametricTolerance.
        """

    @overload
    def __init__(self, theOther: GeomConvert_BSplineCurveToBezierCurve) -> None: ...

    def Arc(self, Index: int) -> nanoocp.Geom.Geom_BezierCurve:
        """
        Constructs and returns the Bezier curve of index
        Index to the table of adjacent Bezier arcs
        computed by this algorithm.
        This Bezier curve has the same orientation as the
        BSpline curve analyzed in this framework.
        Exceptions
        Standard_OutOfRange if Index is less than 1 or
        greater than the number of adjacent Bezier arcs
        computed by this algorithm.
        """

    def Arcs(self, Curves: nanoocp.NCollection.NCollection_Array1[nanoocp.Geom.Geom_BezierCurve]) -> None:
        """
        Constructs all the Bezier curves whose data is
        computed by this algorithm and loads these curves into the Curves table.
        The Bezier curves have the same orientation as the
        BSpline curve analyzed in this framework.
        Exceptions
        Standard_DimensionError if the Curves array was
        not created with the following bounds:
        -   1 , and
        -   the number of adjacent Bezier arcs computed by
        this algorithm (as given by the function NbArcs).
        """

    def Knots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        This methode returns the bspline's knots associated to
        the converted arcs
        Raised if the length of Curves is not equal to
        NbArcs + 1
        """

    def NbArcs(self) -> int:
        """
        Returns the number of BezierCurve arcs.
        If at the creation time you have decomposed the basis curve
        between the parametric values UFirst, ULast the number of
        BezierCurve arcs depends on the number of knots included inside
        the interval [UFirst, ULast].
        If you have decomposed the whole basis B-spline curve the number
        of BezierCurve arcs NbArcs is equal to the number of knots less
        one.
        """

class GeomConvert_BSplineSurfaceKnotSplitting:
    """
    An algorithm to determine isoparametric curves along
    which a BSpline surface should be split in order to
    obtain patches of the same continuity. The continuity order is given at the
    construction time. It is possible to compute the surface patches
    corresponding to the splitting with the method of package
    SplitBSplineSurface.
    For a B-spline surface the discontinuities are localised at
    the knot values. Between two knots values the B-spline is
    infinitely continuously differentiable. For each parametric
    direction at a knot of range index the continuity in this
    direction is equal to: Degree - Mult (Index) where Degree
    is the degree of the basis B-spline functions and Mult the
    multiplicity of the knot of range Index in the given direction.
    If for your computation you need to have B-spline surface with a
    minima of continuity it can be interesting to know between which
    knot values, a B-spline patch, has a continuity of given order.
    This algorithm computes the indexes of the knots where you should
    split the surface, to obtain patches with a constant continuity
    given at the construction time. If you just want to compute the
    local derivatives on the surface you don't need to create the
    BSpline patches, you can use the functions LocalD1, LocalD2,
    LocalD3, LocalDN of the class BSplineSurface from package Geom.
    """

    @overload
    def __init__(self, BasisSurface: nanoocp.Geom.Geom_BSplineSurface | None, UContinuityRange: int, VContinuityRange: int) -> None:
        """
        Determines the u- and v-isoparametric curves
        along which the BSpline surface BasisSurface
        should be split in order to obtain patches with a
        degree of continuity equal to UContinuityRange in
        the u parametric direction, and to
        VContinuityRange in the v parametric direction.
        These isoparametric curves are defined by
        parameters, which are BasisSurface knot values in
        the u or v parametric direction. They are identified
        by indices in the BasisSurface knots table in the
        corresponding parametric direction.
        Use the available interrogation functions to access
        computed values, followed by the global function
        SplitBSplineSurface (provided by the package
        GeomConvert) to split the surface.
        Exceptions
        Standard_RangeError if UContinuityRange or
        VContinuityRange is less than zero.
        """

    @overload
    def __init__(self, theOther: GeomConvert_BSplineSurfaceKnotSplitting) -> None: ...

    def NbUSplits(self) -> int:
        """
        Returns the number of u-isoparametric curves
        along which the analysed BSpline surface should be
        split in order to obtain patches with the continuity
        required by this framework.
        The parameters which define these curves are knot
        values in the corresponding parametric direction.
        Note that the four curves which bound the surface are
        counted among these splitting curves.
        """

    def NbVSplits(self) -> int:
        """
        Returns the number of v-isoparametric curves
        along which the analysed BSpline surface should be
        split in order to obtain patches with the continuity
        required by this framework.
        The parameters which define these curves are knot
        values in the corresponding parametric direction.
        Note that the four curves which bound the surface are
        counted among these splitting curves.
        """

    def Splitting(self, USplit: nanoocp.NCollection.NCollection_Array1[int], VSplit: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """
        Loads the USplit and VSplit tables with the split
        knots values computed in this framework. Each value
        in these tables is an index in the knots table
        corresponding to the u or v parametric direction of
        the BSpline surface analysed by this algorithm.
        The USplit and VSplit values are given in ascending
        order and comprise the indices of the knots which
        give the first and last isoparametric curves of the
        surface in the corresponding parametric direction.
        Use two consecutive values from the USplit table and
        two consecutive values from the VSplit table as
        arguments of the global function
        SplitBSplineSurface (provided by the package
        GeomConvert) to split the surface.
        Exceptions
        Standard_DimensionError if:
        -   the array USplit was not created with the following bounds:
        -   1 , and
        -   the number of split knots in the u parametric
        direction computed in this framework (as given
        by the function NbUSplits); or
        -   the array VSplit was not created with the following bounds:
        -   1 , and
        -   the number of split knots in the v parametric
        direction computed in this framework (as given
        by the function NbVSplits).
        """

    def USplitValue(self, UIndex: int) -> int:
        """
        Returns the split knot of index UIndex
        to the split knots table for the u parametric direction
        computed in this framework. The returned value is
        an index in the knots table relative to the u
        parametric direction of the BSpline surface analysed by this algorithm.
        Note: If UIndex is equal to 1, or to the number of split knots for the u
        parametric direction computed in
        this framework, the corresponding knot gives the
        parameter of one of the bounding curves of the surface.
        Exceptions
        Standard_RangeError if UIndex is less than 1 or greater than the number
        of split knots for the u parametric direction computed in this framework.
        """

    def VSplitValue(self, VIndex: int) -> int:
        """
        Returns the split knot of index VIndex
        to the split knots table for the v parametric direction
        computed in this framework. The returned value is
        an index in the knots table relative to the v
        parametric direction of the BSpline surface analysed by this algorithm.
        Note: If UIndex is equal to 1, or to the number of split knots for the v
        parametric direction computed in
        this framework, the corresponding knot gives the
        parameter of one of the bounding curves of the surface.
        Exceptions
        Standard_RangeError if VIndex is less than 1 or greater than the number
        of split knots for the v parametric direction computed in this framework.
        """

class GeomConvert_BSplineSurfaceToBezierSurface:
    """
    This algorithm converts a B-spline surface into several
    Bezier surfaces. It uses an algorithm of knot insertion.
    A BSplineSurfaceToBezierSurface object provides a framework for:
    -   defining the BSpline surface to be converted,
    -   implementing the construction algorithm, and
    -   consulting the results.
    References :
    Generating the Bezier points of B-spline curves and surfaces
    (Wolfgang Bohm) CAD volume 13 number 6 november 1981
    """

    @overload
    def __init__(self, BasisSurface: nanoocp.Geom.Geom_BSplineSurface | None) -> None:
        """
        Computes all the data needed to convert
        -   the BSpline surface BasisSurface into a series of adjacent Bezier surfaces.
        The result consists of a grid of BasisSurface patches
        limited by isoparametric curves corresponding to knot
        values, both in the u and v parametric directions of
        the surface. A row in the grid corresponds to a series
        of adjacent patches, all limited by the same two
        u-isoparametric curves. A column in the grid
        corresponds to a series of adjacent patches, all
        limited by the same two v-isoparametric curves.
        Use the available interrogation functions to ascertain
        the number of computed Bezier patches, and then to
        construct each individual Bezier surface (or all Bezier surfaces).
        Note: ParametricTolerance is not used.
        """

    @overload
    def __init__(self, BasisSurface: nanoocp.Geom.Geom_BSplineSurface | None, U1: float, U2: float, V1: float, V2: float, ParametricTolerance: float) -> None:
        """
        Computes all the data needed to convert
        the patch of the BSpline surface BasisSurface
        limited by the two parameter values U1 and U2 in
        the u parametric direction, and by the two
        parameter values V1 and V2 in the v parametric
        direction, into a series of adjacent Bezier surfaces.
        The result consists of a grid of BasisSurface patches
        limited by isoparametric curves corresponding to knot
        values, both in the u and v parametric directions of
        the surface. A row in the grid corresponds to a series
        of adjacent patches, all limited by the same two
        u-isoparametric curves. A column in the grid
        corresponds to a series of adjacent patches, all
        limited by the same two v-isoparametric curves.
        Use the available interrogation functions to ascertain
        the number of computed Bezier patches, and then to
        construct each individual Bezier surface (or all Bezier surfaces).
        Note: ParametricTolerance is not used. Raises DomainError
        if U1 or U2 or V1 or V2 are out of the parametric bounds
        of the basis surface [FirstUKnotIndex, LastUKnotIndex] ,
        [FirstVKnotIndex, LastVKnotIndex] The tolerance criterion is
        ParametricTolerance.
        Raised if U2 - U1 <= ParametricTolerance or
        V2 - V1 <= ParametricTolerance.
        """

    @overload
    def __init__(self, theOther: GeomConvert_BSplineSurfaceToBezierSurface) -> None: ...

    def Patch(self, UIndex: int, VIndex: int) -> nanoocp.Geom.Geom_BezierSurface:
        """
        Constructs and returns the Bezier surface of indices
        (UIndex, VIndex) to the patch grid computed on the
        BSpline surface analyzed by this algorithm.
        This Bezier surface has the same orientation as the
        BSpline surface analyzed in this framework.
        UIndex is an index common to a row in the patch
        grid. A row in the grid corresponds to a series of
        adjacent patches, all limited by the same two
        u-isoparametric curves of the surface. VIndex is an
        index common to a column in the patch grid. A column
        in the grid corresponds to a series of adjacent
        patches, all limited by the same two v-isoparametric
        curves of the surface.
        Exceptions
        Standard_OutOfRange if:
        -   UIndex is less than 1 or greater than the number
        of rows in the patch grid computed on the BSpline
        surface analyzed by this algorithm (as returned by
        the function NbUPatches); or if
        -   VIndex is less than 1 or greater than the number
        of columns in the patch grid computed on the
        BSpline surface analyzed by this algorithm (as
        returned by the function NbVPatches).
        """

    def Patches(self, Surfaces: nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_BezierSurface]) -> None:
        """
        Constructs all the Bezier surfaces whose data is
        computed by this algorithm, and loads them into the Surfaces table.
        These Bezier surfaces have the same orientation as
        the BSpline surface analyzed in this framework.
        The Surfaces array is organised in the same way as
        the patch grid computed on the BSpline surface
        analyzed by this algorithm. A row in the array
        corresponds to a series of adjacent patches, all
        limited by the same two u-isoparametric curves of
        the surface. A column in the array corresponds to a
        series of adjacent patches, all limited by the same two
        v-isoparametric curves of the surface.
        Exceptions
        Standard_DimensionError if the Surfaces array
        was not created with the following bounds:
        -   1, and the number of adjacent patch series in the
        u parametric direction of the patch grid computed
        on the BSpline surface, analyzed by this algorithm
        (as given by the function NbUPatches) as row bounds,
        -   1, and the number of adjacent patch series in the
        v parametric direction of the patch grid computed
        on the BSpline surface, analyzed by this algorithm
        (as given by the function NbVPatches) as column bounds.
        """

    def UKnots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        This methode returns the bspline's u-knots associated to
        the converted Patches
        Raised if the length of Curves is not equal to
        NbUPatches + 1
        """

    def VKnots(self, TKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        This methode returns the bspline's v-knots associated to
        the converted Patches
        Raised if the length of Curves is not equal to
        NbVPatches + 1
        """

    def NbUPatches(self) -> int:
        """
        Returns the number of Bezier surfaces in the U direction.
        If at the creation time you have decomposed the basis Surface
        between the parametric values UFirst, ULast the number of
        Bezier surfaces in the U direction depends on the number of
        knots included inside the interval [UFirst, ULast].
        If you have decomposed the whole basis B-spline surface the
        number of Bezier surfaces NbUPatches is equal to the number of
        UKnots less one.
        """

    def NbVPatches(self) -> int:
        """
        Returns the number of Bezier surfaces in the V direction.
        If at the creation time you have decomposed the basis surface
        between the parametric values VFirst, VLast the number of
        Bezier surfaces in the V direction depends on the number of
        knots included inside the interval [VFirst, VLast].
        If you have decomposed the whole basis B-spline surface the
        number of Bezier surfaces NbVPatches is equal to the number of
        VKnots less one.
        """

class GeomConvert_CompBezierSurfacesToBSplineSurface:
    """
    An algorithm to convert a grid of adjacent
    non-rational Bezier surfaces (with continuity CM) into a
    BSpline surface (with continuity CM).
    A CompBezierSurfacesToBSplineSurface object
    provides a framework for:
    -   defining the grid of adjacent Bezier surfaces
    which is to be converted into a BSpline surface,
    -   implementing the computation algorithm, and
    -   consulting the results.
    Warning
    Do not attempt to convert rational Bezier surfaces using such an algorithm.
    Input is array of Bezier patch
    1    2    3     4  -> VIndex [1, NbVPatches] -> VDirection
    -----------------------
    1    |    |    |    |      |
    -----------------------
    2    |    |    |    |      |
    -----------------------
    3    |    |    |    |      |
    -----------------------
    UIndex [1, NbUPatches] Udirection

    Warning! Patches must have compatible parametrization
    """

    @overload
    def __init__(self, Beziers: nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_BezierSurface]) -> None:
        """
        Computes all the data needed to build a "C0"
        continuous BSpline surface equivalent to the grid of
        adjacent non-rational Bezier surfaces Beziers.
        Each surface in the Beziers grid becomes a natural
        patch, limited by knots values, on the BSpline surface
        whose data is computed. Surfaces in the grid must
        satisfy the following conditions:
        -   Coincident bounding curves between two
        consecutive surfaces in a row of the Beziers grid
        must be u-isoparametric bounding curves of these two surfaces.
        -   Coincident bounding curves between two
        consecutive surfaces in a column of the Beziers
        grid must be v-isoparametric bounding curves of these two surfaces.
        The BSpline surface whose data is computed has the
        following characteristics:
        -   Its degree in the u (respectively v) parametric
        direction is equal to that of the Bezier surface
        which has the highest degree in the u
        (respectively v) parametric direction in the Beziers grid.
        -   It is a "Piecewise Bezier" in both u and v
        parametric directions, i.e.:
        -   the knots are regularly spaced in each
        parametric direction (i.e. the difference between
        two consecutive knots is a constant), and
        -   all the multiplicities of the surface knots in a
        given parametric direction are equal to
        Degree, which is the degree of the BSpline
        surface in this parametric direction, except for
        the first and last knots for which the multiplicity is
        equal to Degree + 1.
        -   Coincident bounding curves between two
        consecutive columns of Bezier surfaces in the
        Beziers grid become u-isoparametric curves,
        corresponding to knots values of the BSpline surface.
        -   Coincident bounding curves between two
        consecutive rows of Bezier surfaces in the Beziers
        grid become v-isoparametric curves
        corresponding to knots values of the BSpline surface.
        Use the available consultation functions to access the
        computed data. This data may be used to construct the BSpline surface.
        Warning
        The surfaces in the Beziers grid must be adjacent, i.e.
        two consecutive Bezier surfaces in the grid (in a row
        or column) must have a coincident bounding curve. In
        addition, the location of the parameterization on each
        of these surfaces (i.e. the relative location of u and v
        isoparametric curves on the surface) is of importance
        with regard to the positioning of the surfaces in the
        Beziers grid. Care must be taken with respect to the
        above, as these properties are not checked and an
        error may occur if they are not satisfied.
        Exceptions
        Standard_NotImplemented if one of the Bezier
        surfaces of the Beziers grid is rational.
        """

    @overload
    def __init__(self, Beziers: nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_BezierSurface], Tolerance: float, RemoveKnots: bool = True) -> None:
        """
        Build an Ci uniform (Rational) BSpline surface
        The highest Continuity Ci is imposed, like the
        maximal deformation is lower than <Tolerance>.
        Warning: The Continuity C0 is imposed without any check.
        """

    @overload
    def __init__(self, Beziers: nanoocp.NCollection.NCollection_Array2[nanoocp.Geom.Geom_BezierSurface], UKnots: nanoocp.NCollection.NCollection_Array1[float], VKnots: nanoocp.NCollection.NCollection_Array1[float], UContinuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C0, VContinuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C0, Tolerance: float = 0.0001) -> None:
        """
        Computes all the data needed to construct a BSpline
        surface equivalent to the adjacent non-rational
        Bezier surfaces Beziers grid.
        Each surface in the Beziers grid becomes a natural
        patch, limited by knots values, on the BSpline surface
        whose data is computed. Surfaces in the grid must
        satisfy the following conditions:
        -   Coincident bounding curves between two
        consecutive surfaces in a row of the Beziers grid
        must be u-isoparametric bounding curves of these two surfaces.
        -   Coincident bounding curves between two
        consecutive surfaces in a column of the Beziers
        grid must be v-isoparametric bounding curves of these two surfaces.
        The BSpline surface whose data is computed has the
        following characteristics:
        -   Its degree in the u (respectively v) parametric
        direction is equal to that of the Bezier surface
        which has the highest degree in the u
        (respectively v) parametric direction in the Beziers grid.
        -   Coincident bounding curves between two
        consecutive columns of Bezier surfaces in the
        Beziers grid become u-isoparametric curves
        corresponding to knots values of the BSpline surface.
        -   Coincident bounding curves between two
        consecutive rows of Bezier surfaces in the Beziers
        grid become v-isoparametric curves
        corresponding to knots values of the BSpline surface.
        Knots values of the BSpline surface are given in the two tables:
        -   UKnots for the u parametric direction (which
        corresponds to the order of Bezier surface columns in the Beziers grid), and
        -   VKnots for the v parametric direction (which
        corresponds to the order of Bezier surface rows in the Beziers grid).
        The dimensions of UKnots (respectively VKnots)
        must be equal to the number of columns (respectively,
        rows) of the Beziers grid, plus 1 .
        UContinuity and VContinuity, which are both
        defaulted to GeomAbs_C0, specify the required
        continuity on the BSpline surface. If the required
        degree of continuity is greater than 0 in a given
        parametric direction, a deformation is applied locally
        on the initial surface (as defined by the Beziers grid)
        to satisfy this condition. This local deformation is not
        applied however, if it is greater than Tolerance
        (defaulted to 1.0 e-7). In such cases, the
        continuity condition is not satisfied, and the function
        IsDone will return false. A small tolerance value
        prevents any modification of the surface and a large
        tolerance value "smoothes" the surface.
        Use the available consultation functions to access the
        computed data. This data may be used to construct the BSpline surface.
        Warning
        The surfaces in the Beziers grid must be adjacent, i.e.
        two consecutive Bezier surfaces in the grid (in a row
        or column) must have a coincident bounding curve. In
        addition, the location of the parameterization on each
        of these surfaces (i.e. the relative location of u and v
        isoparametric curves on the surface) is of importance
        with regard to the positioning of the surfaces in the
        Beziers grid. Care must be taken with respect to the
        above, as these properties are not checked and an
        error may occur if they are not satisfied.
        Exceptions
        Standard_DimensionMismatch:
        -   if the number of knots in the UKnots table (i.e. the
        length of the UKnots array) is not equal to the
        number of columns of Bezier surfaces in the
        Beziers grid plus 1, or
        -   if the number of knots in the VKnots table (i.e. the
        length of the VKnots array) is not equal to the
        number of rows of Bezier surfaces in the Beziers grid, plus 1.
        Standard_ConstructionError:
        -   if UContinuity and VContinuity are not equal to
        one of the following values: GeomAbs_C0,
        GeomAbs_C1, GeomAbs_C2 and GeomAbs_C3; or
        -   if the number of columns in the Beziers grid is
        greater than 1, and the required degree of
        continuity in the u parametric direction is greater
        than that of the Bezier surface with the highest
        degree in the u parametric direction (in the Beziers grid), minus 1; or
        -   if the number of rows in the Beziers grid is
        greater than 1, and the required degree of
        continuity in the v parametric direction is greater
        than that of the Bezier surface with the highest
        degree in the v parametric direction (in the Beziers grid), minus 1 .
        Standard_NotImplemented if one of the Bezier
        surfaces in the Beziers grid is rational.
        """

    @overload
    def __init__(self, theOther: GeomConvert_CompBezierSurfacesToBSplineSurface) -> None: ...

    def NbUKnots(self) -> int:
        """
        Returns the number of knots in the U direction
        of the BSpline surface whose data is computed in this framework.
        """

    def NbUPoles(self) -> int:
        """
        Returns number of poles in the U direction
        of the BSpline surface whose data is computed in this framework.
        """

    def NbVKnots(self) -> int:
        """
        Returns the number of knots in the V direction
        of the BSpline surface whose data is computed in this framework.
        """

    def NbVPoles(self) -> int:
        """
        Returns the number of poles in the V direction
        of the BSpline surface whose data is computed in this framework.
        """

    def Poles(self) -> nanoocp.NCollection.NCollection_HArray2[nanoocp.gp.gp_Pnt]:
        """
        Returns the table of poles of the BSpline surface
        whose data is computed in this framework.
        """

    def UKnots(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns the knots table for the u parametric
        direction of the BSpline surface whose data is computed in this framework.
        """

    def UDegree(self) -> int:
        """
        Returns the degree for the u parametric
        direction of the BSpline surface whose data is computed in this framework.
        """

    def VKnots(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns the knots table for the v parametric
        direction of the BSpline surface whose data is computed in this framework.
        """

    def VDegree(self) -> int:
        """
        Returns the degree for the v parametric
        direction of the BSpline surface whose data is computed in this framework.
        """

    def UMultiplicities(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """
        Returns the multiplicities table for the u
        parametric direction of the knots of the BSpline
        surface whose data is computed in this framework.
        """

    def VMultiplicities(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """
        -- Returns the multiplicities table for the v
        parametric direction of the knots of the BSpline
        surface whose data is computed in this framework.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the conversion was successful.
        Unless an exception was raised at the time of
        construction, the conversion of the Bezier surface
        grid assigned to this algorithm is always carried out.
        IsDone returns false if the constraints defined at the
        time of construction cannot be respected. This occurs
        when there is an incompatibility between a required
        degree of continuity on the BSpline surface, and the
        maximum tolerance accepted for local deformations
        of the surface. In such a case the computed data
        does not satisfy all the initial constraints.
        """

class GeomConvert_CompCurveToBSplineCurve:
    """Algorithm converts and concat several curve in an BSplineCurve"""

    @overload
    def __init__(self, Parameterisation: nanoocp.Convert.Convert_ParameterisationType = ...) -> None:
        """
        Initialize the algorithm
        - Parameterisation is used to convert
        """

    @overload
    def __init__(self, BasisCurve: nanoocp.Geom.Geom_BoundedCurve | None, Parameterisation: nanoocp.Convert.Convert_ParameterisationType = ...) -> None:
        """
        Initialize the algorithm with one curve
        - Parameterisation is used to convert
        """

    @overload
    def __init__(self, theOther: GeomConvert_CompCurveToBSplineCurve) -> None: ...

    def Add(self, NewCurve: nanoocp.Geom.Geom_BoundedCurve | None, Tolerance: float, After: bool = False, WithRatio: bool = True, MinM: int = 0) -> bool:
        """
        Append a curve in the BSpline Return False if the
        curve is not G0 with the BSplineCurve. Tolerance
        is used to check continuity and decrease
        Multiplicity at the common Knot until MinM
        if MinM = 0, the common Knot can be removed

        WithRatio defines whether the resulting curve should have a uniform
        parameterization. Setting WithRatio to false may greatly
        decrease the speed of algorithms like CPnts_AbscissaPoint::AdvPerform
        when applied to the resulting curve.
        """

    def BSplineCurve(self) -> nanoocp.Geom.Geom_BSplineCurve: ...

    def Clear(self) -> None:
        """Clear a result curve"""

class GeomConvert_Units:
    """Class contains conversion methods for 2d geom objects"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomConvert_Units) -> None: ...

    @staticmethod
    def RadianToDegree(theCurve: nanoocp.Geom2d.Geom2d_Curve | None, theSurface: nanoocp.Geom.Geom_Surface | None, theLengthFactor: float, theFactorRadianDegree: float) -> nanoocp.Geom2d.Geom2d_Curve:
        """Convert 2d curve for change angle unit from radian to degree"""

    @staticmethod
    def DegreeToRadian(theCurve: nanoocp.Geom2d.Geom2d_Curve | None, theSurface: nanoocp.Geom.Geom_Surface | None, theLengthFactor: float, theFactorRadianDegree: float) -> nanoocp.Geom2d.Geom2d_Curve:
        """Convert 2d curve for change angle unit from degree to radian"""

    @staticmethod
    def MirrorPCurve(theCurve: nanoocp.Geom2d.Geom2d_Curve | None) -> nanoocp.Geom2d.Geom2d_Curve:
        """return 2d curve as 'mirror' for given"""

class GeomConvert_CurveToAnaCurve:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomConvert_CurveToAnaCurve) -> None: ...

    def Init(self, C: nanoocp.Geom.Geom_Curve | None) -> None: ...

    def ConvertToAnalytical(self, theTol: float, F: float, L: float) -> tuple[bool, nanoocp.Geom.Geom_Curve, float, float]:
        """
        Converts me to analytical if possible with given
        tolerance. The new first and last parameters are
        returned to newF, newL
        """

    @staticmethod
    def ComputeCurve(curve: nanoocp.Geom.Geom_Curve | None, tolerance: float, c1: float, c2: float, theCurvType: GeomConvert_ConvType = GeomConvert_ConvType.GeomConvert_MinGap, theTarget: nanoocp.GeomAbs.GeomAbs_CurveType = GeomAbs_CurveType.GeomAbs_Line) -> tuple[nanoocp.Geom.Geom_Curve, float, float, float]: ...

    @staticmethod
    def ComputeCircle(curve: nanoocp.Geom.Geom_Curve | None, tolerance: float, c1: float, c2: float) -> tuple[nanoocp.Geom.Geom_Curve, float, float, float]:
        """
        Tries to convert the given curve to circle with given
        tolerance. Returns NULL curve if conversion is
        not possible.
        """

    @staticmethod
    def ComputeEllipse(curve: nanoocp.Geom.Geom_Curve | None, tolerance: float, c1: float, c2: float) -> tuple[nanoocp.Geom.Geom_Curve, float, float, float]:
        """
        Tries to convert the given curve to ellipse with given
        tolerance. Returns NULL curve if conversion is
        not possible.
        """

    @staticmethod
    def ComputeLine(curve: nanoocp.Geom.Geom_Curve | None, tolerance: float, c1: float, c2: float) -> tuple[nanoocp.Geom.Geom_Line, float, float, float]:
        """
        Tries to convert the given curve to line with given
        tolerance. Returns NULL curve if conversion is
        not possible.
        """

    @staticmethod
    def IsLinear(aPoints: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], tolerance: float) -> tuple[bool, float]:
        """
        Returns true if the set of points is linear with given
        tolerance
        """

    @staticmethod
    def GetLine(P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> tuple[nanoocp.gp.gp_Lin, float, float]:
        """
        Creates line on two points.
        Resulting parameters returned
        """

    @staticmethod
    def GetCircle(Circ: nanoocp.gp.gp_Circ, P0: nanoocp.gp.gp_Pnt, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> bool:
        """Creates circle on points. Returns true if OK."""

    def Gap(self) -> float:
        """
        Returns maximal deviation of converted surface from the original
        one computed by last call to ConvertToAnalytical
        """

    def GetConvType(self) -> GeomConvert_ConvType:
        """Returns conversion type"""

    def SetConvType(self, theConvType: GeomConvert_ConvType) -> None:
        """Sets type of conversion"""

    def GetTarget(self) -> nanoocp.GeomAbs.GeomAbs_CurveType:
        """Returns target curve type"""

    def SetTarget(self, theTarget: nanoocp.GeomAbs.GeomAbs_CurveType) -> None:
        """Sets target curve type"""

class GeomConvert_SurfToAnaSurf:
    """
    Converts a surface to the analytical form with given
    precision. Conversion is done only the surface is bspline
    of bezier and this can be approximated by some analytical
    surface with that precision.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_Surface | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomConvert_SurfToAnaSurf) -> None: ...

    def Init(self, S: nanoocp.Geom.Geom_Surface | None) -> None: ...

    def SetConvType(self, theConvType: GeomConvert_ConvType = GeomConvert_ConvType.GeomConvert_Simplest) -> None: ...

    def SetTarget(self, theSurfType: nanoocp.GeomAbs.GeomAbs_SurfaceType = GeomAbs_SurfaceType.GeomAbs_Plane) -> None: ...

    def Gap(self) -> float:
        """
        Returns maximal deviation of converted surface from the original
        one computed by last call to ConvertToAnalytical
        """

    @overload
    def ConvertToAnalytical(self, InitialToler: float) -> nanoocp.Geom.Geom_Surface:
        """
        Tries to convert the Surface to an Analytic form
        Returns the result
        In case of failure, returns a Null Handle
        """

    @overload
    def ConvertToAnalytical(self, InitialToler: float, Umin: float, Umax: float, Vmin: float, Vmax: float) -> nanoocp.Geom.Geom_Surface: ...

    @staticmethod
    def IsSame(S1: nanoocp.Geom.Geom_Surface | None, S2: nanoocp.Geom.Geom_Surface | None, tol: float) -> bool:
        """Returns true if surfaces is same with the given tolerance"""

    @staticmethod
    def IsCanonical(S: nanoocp.Geom.Geom_Surface | None) -> bool:
        """Returns true, if surface is canonical"""

class GeomConvert_FuncSphereLSDist(nanoocp.math.math_MultipleVarFunctionWithGradient):
    """
    Function for search of sphere canonic parameters: coordinates of center and radius from set of
    moints by least square method.
    //!
    The class inherits math_MultipleVarFunctionWithGradient and thus is intended
    for use in math_BFGS algorithm.

    The criteria is:
    F(x0, y0, z0, R) = Sum[(x(i) - x0)^2 + (y(i) - y0)^2 + (z(i) - z0)^2 - R^2]^2 => min,
    x(i), y(i), z(i) - coordinates of sample points, x0, y0, z0, R - coordinates of center and
    radius of sphere, which must be defined

    The first derivative are:
    dF/dx0 : G1(x0, y0, z0, R) = -4*Sum{[...]*(x(i) - x0)}
    dF/dy0 : G2(x0, y0, z0, R) = -4*Sum{[...]*(y(i) - y0)}
    dF/dz0 : G3(x0, y0, z0, R) = -4*Sum{[...]*(z(i) - z0)}
    dF/dR : G4(x0, y0, z0, R) = -4*R*Sum[...]
    [...] = [(x(i) - x0)^2 + (y(i) - y0)^2 + (z(i) - z0)^2 - R^2]
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, thePoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ] | None) -> None: ...

    @overload
    def __init__(self, theOther: GeomConvert_FuncSphereLSDist) -> None: ...

    def SetPoints(self, thePoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ] | None) -> None: ...

    def NbVariables(self) -> int:
        """Number of variables."""

    def Value(self, X: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """Value."""

    def Gradient(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> bool:
        """Gradient."""

    def Values(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """Value and gradient."""

class GeomConvert_FuncCylinderLSDist(nanoocp.math.math_MultipleVarFunctionWithGradient):
    """
    Function for search of cylinder canonic parameters: coordinates of center local coordinate
    system, direction of axis and radius from set of points by least square method.

    The class inherits math_MultipleVarFunctionWithGradient and thus is intended
    for use in math_BFGS algorithm.

    Parametrisation:
    Cylinder is defined by its axis and radius. Axis is defined by 3 cartesian coordinates at
    location x0, y0, z0 and direction, which is constant and set by user: dir.x, dir.y, dir.z The
    criteria is: F(x0, y0, z0, theta, phi, R) = Sum[|(P(i) - Loc)^dir|^2 - R^2]^2 => min P(i) is
    i-th sample point, Loc, dir - axis location and direction, R - radius

    The square vector product |(P(i) - Loc)^dir|^2 is:

    [(y - y0)*dir.z - (z - z0)*dir.y]^2 +
    [(z - z0)*dir.x - (x - x0)*dir.z]^2 +
    [(x - x0)*dir.y - (y - y0)*dir.x]^2

    First derivative of square vector product are:
    Dx0 =  2*[(z - z0)*dir.x - (x - x0)*dir.z]*dir.z
    -2*[(x - x0)*dir.y - (y - y0)*dir.x]*dir.y
    Dy0 = -2*[(y - y0)*dir.z - (z - z0)*dir.y]*dir.z
    +2*[(x - x0)*dir.y - (y - y0)*dir.x]*dir.x
    Dz0 =  2*[(y - y0)*dir.z - (z - z0)*dir.y]*dir.y
    -2*[(z - z0)*dir.x - (x - x0)*dir.z]*dir.x

    dF/dx0 : G1(...) = 2*Sum{[...]*Dx0}
    dF/dy0 : G2(...) = 2*Sum{[...]*Dy0}
    dF/dz0 : G3(...) = 2*Sum{[...]*Dz0}
    dF/dR : G4(...) = -4*R*Sum[...]
    [...] = [|(P(i) - Loc)^dir|^2 - R^2]
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, thePoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ] | None, theDir: nanoocp.gp.gp_Dir) -> None: ...

    @overload
    def __init__(self, theOther: GeomConvert_FuncCylinderLSDist) -> None: ...

    def SetPoints(self, thePoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ] | None) -> None: ...

    def SetDir(self, theDir: nanoocp.gp.gp_Dir) -> None: ...

    def NbVariables(self) -> int:
        """Number of variables."""

    def Value(self, X: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """Value."""

    def Gradient(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> bool:
        """Gradient."""

    def Values(self, X: nanoocp.math.math_Vector, G: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """Value and gradient."""

class GeomConvert_FuncConeLSDist(nanoocp.math.math_MultipleVarFunction):
    """
    Function for search of Cone canonic parameters: coordinates of center local coordinate system,
    direction of axis, radius and semi-angle from set of points
    by least square method.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, thePoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ] | None, theDir: nanoocp.gp.gp_Dir) -> None: ...

    @overload
    def __init__(self, theOther: GeomConvert_FuncConeLSDist) -> None: ...

    def SetPoints(self, thePoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ] | None) -> None: ...

    def SetDir(self, theDir: nanoocp.gp.gp_Dir) -> None: ...

    def NbVariables(self) -> int:
        """Number of variables."""

    def Value(self, X: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """Value."""
