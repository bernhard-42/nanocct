"""OCCT package GeomLib (toolkit TKGeomBase)"""

import enum
from typing import overload

import nanoocp.Adaptor2d
from nanoocp.Adaptor2d import Adaptor2d_Curve2d as Adaptor2d_Curve2d
import nanoocp.Adaptor3d
import nanoocp.AdvApprox
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.Geom2dAdaptor
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.gp
import nanoocp.math


class GeomLib_InterpolationErrors(enum.IntEnum):
    """
    in case the interpolation errors out, this
    tells what happened
    """

    GeomLib_NoError = 0

    GeomLib_NotEnoughtPoints = 1

    GeomLib_DegreeSmallerThan3 = 2

    GeomLib_InversionProblem = 3

GeomLib_NoError: GeomLib_InterpolationErrors = GeomLib_InterpolationErrors.GeomLib_NoError

GeomLib_NotEnoughtPoints: GeomLib_InterpolationErrors = ...

GeomLib_DegreeSmallerThan3: GeomLib_InterpolationErrors = ...

GeomLib_InversionProblem: GeomLib_InterpolationErrors = ...

class GeomLib:
    """
    Geom Library. This package provides an
    implementation of functions for basic computation
    on geometric entity from packages Geom and Geom2d.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomLib) -> None: ...

    @staticmethod
    def To3d(Position: nanoocp.gp.gp_Ax2, Curve2d: nanoocp.Geom2d.Geom2d_Curve | None) -> nanoocp.Geom.Geom_Curve:
        """
        Computes the curve 3d from package Geom
        corresponding to curve 2d from package Geom2d, on
        the plan defined with the local coordinate system
        Position.
        """

    @staticmethod
    def GTransform(Curve: nanoocp.Geom2d.Geom2d_Curve | None, GTrsf: nanoocp.gp.gp_GTrsf2d) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        Computes the curve 3d from package Geom
        corresponding to the curve 3d from package Geom,
        transformed with the transformation <GTrsf>
        WARNING : this method may return a null Handle if
        it's impossible to compute the transformation of
        a curve. It's not implemented when :
        1) the curve is an infinite parabola or hyperbola
        2) the curve is an offsetcurve
        """

    @staticmethod
    def SameRange(Tolerance: float, Curve2dPtr: nanoocp.Geom2d.Geom2d_Curve | None, First: float, Last: float, RequestedFirst: float, RequestedLast: float) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        Make the curve Curve2dPtr have the imposed
        range First to List the most economic way,
        that is if it can change the range without
        changing the nature of the curve it will try
        to do that. Otherwise it will produce a Bspline
        curve that has the required range
        """

    @staticmethod
    def BuildCurve3d(Tolerance: float, CurvePtr: nanoocp.Adaptor3d.Adaptor3d_CurveOnSurface, FirstParameter: float, LastParameter: float, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1, MaxDegree: int = 14, MaxSegment: int = 30) -> tuple[nanoocp.Geom.Geom_Curve, float, float]: ...

    @staticmethod
    def AdjustExtremity(Curve: nanoocp.Geom.Geom_BoundedCurve | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, T1: nanoocp.gp.gp_Vec, T2: nanoocp.gp.gp_Vec) -> nanoocp.Geom.Geom_BoundedCurve: ...

    @staticmethod
    def ExtendCurveToPoint(Curve: nanoocp.Geom.Geom_BoundedCurve | None, Point: nanoocp.gp.gp_Pnt, Cont: int, After: bool) -> nanoocp.Geom.Geom_BoundedCurve:
        """
        Extends the bounded curve Curve to the point Point.
        The extension is built:
        -      at the end of the curve if After equals true, or
        -      at the beginning of the curve if After equals false.
        The extension is performed according to a degree of
        continuity equal to Cont, which in its turn must be equal to 1, 2 or 3.
        This function converts the bounded curve Curve into a BSpline curve.
        Warning
        -   Nothing is done, and Curve is not modified if Cont is
        not equal to 1, 2 or 3.
        -   It is recommended that the extension should not be
        too large with respect to the size of the bounded
        curve Curve: Point must not be located too far from
        one of the extremities of Curve.
        """

    @staticmethod
    def ExtendSurfByLength(Surf: nanoocp.Geom.Geom_BoundedSurface | None, Length: float, Cont: int, InU: bool, After: bool) -> nanoocp.Geom.Geom_BoundedSurface:
        """
        Extends the bounded surface Surf along one of its
        boundaries. The chord length of the extension is equal to Length.
        The direction of the extension is given as:
        -   the u parametric direction of Surf, if InU equals true, or
        -   the v parametric direction of Surf, if InU equals false.
        In this parametric direction, the extension is built on the side of:
        -   the last parameter of Surf, if After equals true, or
        -   the first parameter of Surf, if After equals false.
        The extension is performed according to a degree of
        continuity equal to Cont, which in its turn must be equal to 1, 2 or 3.
        This function converts the bounded surface Surf into a BSpline surface.
        Warning
        -   Nothing is done, and Surf is not modified if Cont is
        not equal to 1, 2 or 3.
        -   It is recommended that Length, the size of the
        extension should not be too large with respect to the
        size of the bounded surface Surf.
        -   Surf must not be a periodic BSpline surface in the
        parametric direction corresponding to the direction of extension.
        """

    @staticmethod
    def AxeOfInertia(Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Axe: nanoocp.gp.gp_Ax2, Tol: float = 1e-07) -> bool:
        """
        Compute axes of inertia, of some points
        <Axe>.Location() is the BaryCentre
        <Axe>.XDirection is the axe of upper inertia
        <Axe>.Direction is the Normal to the average plane
        IsSingular is True if points are on line
        Tol is used to determine singular cases.
        """

    @staticmethod
    def Inertia(Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Bary: nanoocp.gp.gp_Pnt, XDir: nanoocp.gp.gp_Dir, YDir: nanoocp.gp.gp_Dir) -> tuple[float, float, float]:
        """
        Compute principale axes of inertia, and dispersion
        value of some points.
        """

    @staticmethod
    def RemovePointsFromArray(NumPoints: int, InParameters: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Warning! This assume that the InParameter is an increasing sequence
        of real number and it will not check for that : Unpredictable
        result can happen if this is not satisfied. It is the caller
        responsibility to check for that property.

        This method makes uniform NumPoints segments S1,...SNumPoints out
        of the segment defined by the first parameter and the
        last parameter of the InParameter ; keeps only one
        point of the InParameters set of parameter in each of
        the uniform segments taking care of the first and the
        last parameters. For the ith segment the element of
        the InParameter is the one that is the first to exceed
        the midpoint of the segment and to fall before the
        midpoint of the next segment
        There will be at the end at most NumPoints + 1
        if NumPoints > 2 in the OutParameters Array
        """

    @staticmethod
    def DensifyArray1OfReal(MinNumPoints: int, InParameters: nanoocp.NCollection.NCollection_Array1[float]) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        this makes sure that there is at least MinNumPoints
        in OutParameters taking into account the parameters in
        the InParameters array provided those are in order,
        that is the sequence of real in the InParameter is strictly
        non decreasing
        """

    @staticmethod
    def FuseIntervals(Interval1: nanoocp.NCollection.NCollection_Array1[float], Interval2: nanoocp.NCollection.NCollection_Array1[float], Fusion: nanoocp.NCollection.NCollection_Sequence[float], Confusion: float = 1e-09, IsAdjustToFirstInterval: bool = False) -> None:
        """
        This method fuse intervals Interval1 and Interval2 with specified Confusion
        @param[in] Interval1  first interval to fuse
        @param[in] Interval2  second interval to fuse
        @param[in] Confision  tolerance to compare intervals
        @param[in] IsAdjustToFirstInterval  flag to set method of fusion, if intervals are close
        if false, intervals are fusing by half-division method
        if true, intervals are fusing by selecting value from Interval1
        @param[out] Fusion  output interval
        """

    @staticmethod
    def EvalMaxParametricDistance(Curve: nanoocp.Adaptor3d.Adaptor3d_Curve, AReferenceCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, Tolerance: float, Parameters: nanoocp.NCollection.NCollection_Array1[float]) -> float:
        """
        this will compute the maximum distance at the
        parameters given in the Parameters array by
        evaluating each parameter the two curves and taking
        the maximum of the evaluated distance
        """

    @staticmethod
    def EvalMaxDistanceAlongParameter(Curve: nanoocp.Adaptor3d.Adaptor3d_Curve, AReferenceCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, Tolerance: float, Parameters: nanoocp.NCollection.NCollection_Array1[float]) -> float:
        """
        this will compute the maximum distance at the parameters
        given in the Parameters array by projecting from the Curve
        to the reference curve and taking the minimum distance
        Than the maximum will be taken on those minimas.
        """

    @staticmethod
    def CancelDenominatorDerivative(BSurf: nanoocp.Geom.Geom_BSplineSurface | None, UDirection: bool, VDirection: bool) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        Cancel,on the boundaries,the denominator first derivative
        in the directions wished by the user and set its value to 1.
        """

    @staticmethod
    def NormEstim(theSurf: nanoocp.Geom.Geom_Surface | None, theUV: nanoocp.gp.gp_Pnt2d, theTol: float, theNorm: nanoocp.gp.gp_Dir) -> int:
        """
        Estimate surface normal at the given (U, V) point.
        @param[in]  theSurf input surface
        @param[in]  theUV   (U, V) point coordinates on the surface
        @param[in]  theTol  estimation tolerance
        @param[out] theNorm computed normal
        @return 0 if normal estimated from D1,
        1 if estimated from D2 (quasysingular),
        >=2 in case of failure (undefined or infinite solutions)
        """

    @staticmethod
    def IsClosed(S: nanoocp.Geom.Geom_Surface | None, Tol: float) -> tuple[bool, bool]:
        """
        This method defines if opposite boundaries of surface
        coincide with given tolerance
        """

    @staticmethod
    def IsBSplUClosed(S: nanoocp.Geom.Geom_BSplineSurface | None, U1: float, U2: float, Tol: float) -> bool:
        """
        Returns true if the poles of U1 isoline and the poles of
        U2 isoline of surface are identical according to tolerance criterion.
        For rational surfaces Weights(i)*Poles(i) are checked.
        """

    @staticmethod
    def IsBSplVClosed(S: nanoocp.Geom.Geom_BSplineSurface | None, V1: float, V2: float, Tol: float) -> bool:
        """
        Returns true if the poles of V1 isoline and the poles of
        V2 isoline of surface are identical according to tolerance criterion.
        For rational surfaces Weights(i)*Poles(i) are checked.
        """

    @staticmethod
    def IsBzUClosed(S: nanoocp.Geom.Geom_BezierSurface | None, U1: float, U2: float, Tol: float) -> bool:
        """
        Returns true if the poles of U1 isoline and the poles of
        U2 isoline of surface are identical according to tolerance criterion.
        """

    @staticmethod
    def IsBzVClosed(S: nanoocp.Geom.Geom_BezierSurface | None, V1: float, V2: float, Tol: float) -> bool:
        """
        Returns true if the poles of V1 isoline and the poles of
        V2 isoline of surface are identical according to tolerance criterion.
        """

    @staticmethod
    def isIsoLine(theC2D: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> tuple[bool, bool, float, bool]:
        """
        Checks whether the 2d curve is a isoline. It can be represented by b-spline, bezier,
        or geometric line. This line should have natural parameterization.
        @param theC2D       Trimmed curve to be checked.
        @param theIsU       Flag indicating that line is u const.
        @param theParam     Line parameter.
        @param theIsForward Flag indicating forward parameterization on a isoline.
        @return true when 2d curve is a line and false otherwise.
        """

    @staticmethod
    def buildC3dOnIsoLine(theC2D: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, theSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theFirst: float, theLast: float, theTolerance: float, theIsU: bool, theParam: float, theIsForward: bool) -> nanoocp.Geom.Geom_Curve:
        """
        Builds 3D curve for a isoline. This method takes corresponding isoline from
        the input surface.
        @param theC2D   Trimmed curve to be approximated.
        @param theIsU   Flag indicating that line is u const.
        @param theParam Line parameter.
        @param theIsForward Flag indicating forward parameterization on a isoline.
        @return true when 3d curve is built and false otherwise.
        """

class GeomLib_Check2dBSplineCurve:
    """
    Checks for the end tangents : whether or not those
    are reversed
    """

    @overload
    def __init__(self, Curve: nanoocp.Geom2d.Geom2d_BSplineCurve | None, Tolerance: float, AngularTolerance: float) -> None: ...

    @overload
    def __init__(self, theOther: GeomLib_Check2dBSplineCurve) -> None: ...

    def IsDone(self) -> bool: ...

    def NeedTangentFix(self) -> tuple[bool, bool]: ...

    def FixTangent(self, FirstFlag: bool, LastFlag: bool) -> None: ...

    def FixedTangent(self, FirstFlag: bool, LastFlag: bool) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """
        modifies the curve
        by fixing the first or the last tangencies

        if Index3D not in the Range [1,Nb3dSpaces]
        if the Approx is not Done
        """

class GeomLib_CheckCurveOnSurface:
    """
    Computes the max distance between 3D-curve and 2D-curve
    in some surface.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theCurve: nanoocp.Adaptor3d.Adaptor3d_Curve | None, theTolRange: float = 1e-09) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: GeomLib_CheckCurveOnSurface) -> None: ...

    @overload
    def Init(self, theCurve: nanoocp.Adaptor3d.Adaptor3d_Curve | None, theTolRange: float = 1e-09) -> None:
        """Sets the data for the algorithm"""

    @overload
    def Init(self) -> None:
        """Initializes all members by default values"""

    def Perform(self, theCurveOnSurface: nanoocp.Adaptor3d.Adaptor3d_CurveOnSurface | None) -> None:
        """
        Computes the max distance for the 3d curve <myCurve>
        and 2d curve <theCurveOnSurface>
        If isMultiThread == true then computation will be performed in parallel.
        """

    def SetParallel(self, theIsParallel: bool) -> None:
        """Sets parallel flag"""

    def IsParallel(self) -> bool:
        """Returns true if parallel flag is set"""

    def IsDone(self) -> bool:
        """Returns true if the max distance has been found"""

    def ErrorStatus(self) -> int:
        """
        Returns error status
        The possible values are:
        0 - OK;
        1 - null curve or surface or 2d curve;
        2 - invalid parametric range;
        3 - error in calculations.
        """

    def MaxDistance(self) -> float:
        """Returns max distance"""

    def MaxParameter(self) -> float:
        """Returns parameter in which the distance is maximal"""

class GeomLib_CheckBSplineCurve:
    """
    Checks for the end tangents : whether or not those
    are reversed regarding the third or n-3rd control
    """

    @overload
    def __init__(self, Curve: nanoocp.Geom.Geom_BSplineCurve | None, Tolerance: float, AngularTolerance: float) -> None: ...

    @overload
    def __init__(self, theOther: GeomLib_CheckBSplineCurve) -> None: ...

    def IsDone(self) -> bool: ...

    def NeedTangentFix(self) -> tuple[bool, bool]: ...

    def FixTangent(self, FirstFlag: bool, LastFlag: bool) -> None: ...

    def FixedTangent(self, FirstFlag: bool, LastFlag: bool) -> nanoocp.Geom.Geom_BSplineCurve:
        """
        modifies the curve
        by fixing the first or the last tangencies

        if Index3D not in the Range [1,Nb3dSpaces]
        if the Approx is not Done
        """

class GeomLib_DenominatorMultiplier:
    """
    this defines an evaluator for a function of 2 variables
    that will be used by CancelDenominatorDerivative in one
    direction.
    """

    @overload
    def __init__(self, Surface: nanoocp.Geom.Geom_BSplineSurface | None, KnotVector: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        if the surface is rational this will define the evaluator
        of a real function of 2 variables a(u,v) such that
        if we define a new surface by :
        a(u,v) * N(u,v)
        NewF(u,v) = ----------------
        a(u,v) * D(u,v)
        """

    @overload
    def __init__(self, theOther: GeomLib_DenominatorMultiplier) -> None: ...

    def Value(self, UParameter: float, VParameter: float) -> float:
        """
        Returns the value of
        a(UParameter,VParameter)=

        H0(UParameter)/Denominator(Umin,Vparameter)

        D Denominator(Umin,Vparameter)
        - ------------------------------[H1(u)]/(Denominator(Umin,Vparameter)^2)
        D U

        + H3(UParameter)/Denominator(Umax,Vparameter)

        D Denominator(Umax,Vparameter)
        - ------------------------------[H2(u)]/(Denominator(Umax,Vparameter)^2)
        D U
        """

class GeomLib_Interpolate:
    """
    This class is used to construct a BSpline curve by
    interpolation of points at given parameters. The
    continuity of the curve is degree - 1 and the
    method used when boundary conditions are not given
    is to use odd degrees and null the derivatives on
    both sides from degree -1 down to (degree+1) / 2
    When even degree is given the returned curve is of
    degree - 1 so that the degree of the curve is odd
    """

    @overload
    def __init__(self, Degree: int, NumPoints: int, Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Parameters: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def __init__(self, theOther: GeomLib_Interpolate) -> None: ...

    def IsDone(self) -> bool:
        """returns if everything went OK"""

    def Error(self) -> GeomLib_InterpolationErrors:
        """returns the error type if any"""

    def Curve(self) -> nanoocp.Geom.Geom_BSplineCurve:
        """returns the interpolated curve of the requested degree"""

class GeomLib_IsPlanarSurface:
    """Find if a surface is a planar surface."""

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_Surface | None, Tol: float = 1e-07) -> None: ...

    @overload
    def __init__(self, theOther: GeomLib_IsPlanarSurface) -> None: ...

    def IsPlanar(self) -> bool:
        """Return if the Surface is a plan"""

    def Plan(self) -> nanoocp.gp.gp_Pln:
        """Return the plan definition"""

class GeomLib_LogSample(nanoocp.math.math_FunctionSample):
    @overload
    def __init__(self, A: float, B: float, N: int) -> None: ...

    @overload
    def __init__(self, theOther: GeomLib_LogSample) -> None: ...

    def GetParameter(self, Index: int) -> float:
        """
        Returns the value of parameter of the point of
        range Index : A + ((Index-1)/(NbPoints-1))*B.
        An exception is raised if Index<=0 or Index>NbPoints.
        """

class GeomLib_MakeCurvefromApprox:
    """
    this class is used to construct the BSpline curve
    from an Approximation (ApproxAFunction from AdvApprox).
    """

    @overload
    def __init__(self, Approx: nanoocp.AdvApprox.AdvApprox_ApproxAFunction) -> None: ...

    @overload
    def __init__(self, theOther: GeomLib_MakeCurvefromApprox) -> None: ...

    def IsDone(self) -> bool: ...

    def Nb1DSpaces(self) -> int:
        """returns the number of 1D spaces of the Approx"""

    def Nb2DSpaces(self) -> int:
        """returns the number of 3D spaces of the Approx"""

    def Nb3DSpaces(self) -> int:
        """returns the number of 3D spaces of the Approx"""

    @overload
    def Curve2d(self, Index2d: int) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """
        returns a polynomial curve whose poles correspond to
        the Index2d 2D space
        if Index2d not in the Range [1,Nb2dSpaces]
        if the Approx is not Done
        """

    @overload
    def Curve2d(self, Index1d: int, Index2d: int) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """
        returns a rational curve whose poles correspond to
        the index2d of the 2D space and whose weights correspond
        to one dimensional space of index 1d
        if Index1d not in the Range [1,Nb1dSpaces]
        if Index2d not in the Range [1,Nb2dSpaces]
        if the Approx is not Done
        """

    def Curve2dFromTwo1d(self, Index1d: int, Index2d: int) -> nanoocp.Geom2d.Geom2d_BSplineCurve:
        """
        returns a 2D curve building it from the 1D curve
        in x at Index1d and y at Index2d amongst the
        1D curves
        if Index1d not in the Range [1,Nb1dSpaces]
        if Index2d not in the Range [1,Nb1dSpaces]
        if the Approx is not Done
        """

    @overload
    def Curve(self, Index3d: int) -> nanoocp.Geom.Geom_BSplineCurve:
        """
        returns a polynomial curve whose poles correspond to
        the Index3D 3D space
        if Index3D not in the Range [1,Nb3dSpaces]
        if the Approx is not Done
        """

    @overload
    def Curve(self, Index1D: int, Index3D: int) -> nanoocp.Geom.Geom_BSplineCurve:
        """
        returns a rational curve whose poles correspond to
        the index3D of the 3D space and whose weights correspond
        to the index1d 1D space.
        if Index1D not in the Range [1,Nb1dSpaces]
        if Index3D not in the Range [1,Nb3dSpaces]
        if the Approx is not Done
        """

class GeomLib_PolyFunc(nanoocp.math.math_FunctionWithDerivative):
    """Polynomial Function"""

    @overload
    def __init__(self, Coeffs: nanoocp.math.math_Vector) -> None: ...

    @overload
    def __init__(self, theOther: GeomLib_PolyFunc) -> None: ...

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

class GeomLib_Tool:
    """
    Provides various methods with Geom2d and Geom curves and surfaces.
    The methods of this class compute the parameter(s) of a given point on a
    curve or a surface. To get the valid result the point must be located rather close
    to the curve (surface) or at least to allow getting unambiguous result
    (do not put point at center of circle...),
    but choice of "trust" distance between curve/surface and point is
    responsibility of user (parameter MaxDist).
    Return FALSE if the point is beyond the MaxDist
    limit or if computation fails.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GeomLib_Tool) -> None: ...

    @overload
    @staticmethod
    def Parameter(Curve: nanoocp.Geom.Geom_Curve | None, Point: nanoocp.gp.gp_Pnt, MaxDist: float) -> tuple[bool, float]:
        """
        Extracts the parameter of a 3D point lying on a 3D curve
        or at a distance less than the MaxDist value.
        """

    @overload
    @staticmethod
    def Parameter(Curve: nanoocp.Geom2d.Geom2d_Curve | None, Point: nanoocp.gp.gp_Pnt2d, MaxDist: float) -> tuple[bool, float]:
        """
        Extracts the parameter of a 2D point lying on a 2D curve
        or at a distance less than the MaxDist value.
        """

    @staticmethod
    def Parameters(Surface: nanoocp.Geom.Geom_Surface | None, Point: nanoocp.gp.gp_Pnt, MaxDist: float) -> tuple[bool, float, float]:
        """
        Extracts the parameter of a 3D point lying on a surface
        or at a distance less than the MaxDist value.
        """

    @overload
    @staticmethod
    def ComputeDeviation(theCurve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, theFPar: float, theLPar: float, theStartParameter: float, theNbIters: int = 100, thePtOnCurve: nanoocp.gp.gp_Pnt2d = None, theVecCurvLine: nanoocp.gp.gp_Vec2d = None, theLine: nanoocp.gp.gp_Lin2d = None) -> float:
        """
        Computes parameter in theCurve (*thePrmOnCurve) where maximal deviation
        between theCurve and the linear segment joining its points with
        the parameters theFPar and theLPar is obtained.
        Returns the (positive) value of deviation. Returns negative value if
        the deviation cannot be computed.
        The returned parameter (in case of successful) will always be in
        the range [theFPar, theLPar].
        Iterative method is used for computation. So, theStartParameter is
        needed to be set. Recommend value of theStartParameter can be found with
        the overloaded method.
        Additionally, following values can be returned (optionally):
        @param thePtOnCurve - the point on curve where maximal deviation is achieved;
        @param thePrmOnCurve - the parameter of thePtOnCurve;
        @param theVecCurvLine - the vector along which is computed (this vector is always
        perpendicular theLine);
        @param theLine - the linear segment joining the point of theCurve having parameters
        theFPar and theLPar.
        """

    @overload
    @staticmethod
    def ComputeDeviation(theCurve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, theFPar: float, theLPar: float, theNbSubIntervals: int, theNbIters: int = 10) -> float:
        """
        Computes parameter in theCurve (*thePrmOnCurve) where maximal deviation
        between theCurve and the linear segment joining its points with
        the parameters theFPar and theLPar is obtained.
        Returns the (positive) value of deviation. Returns negative value if
        the deviation cannot be computed.
        The returned parameter (in case of successful) will always be in
        the range [theFPar, theLPar].
        theNbSubIntervals defines discretization of the given interval [theFPar, theLPar]
        to provide better search condition. This value should be chosen taking into
        account complexity of the curve in considered interval. E.g. if there are many
        oscillations of the curve in the interval then theNbSubIntervals mus be
        great number. However, the greater value of theNbSubIntervals the slower the
        algorithm will compute.
        theNbIters sets number of iterations.
        ATTENTION!!!
        This algorithm cannot compute deviation precisely (so, there is no point in
        setting big value of theNbIters). But it can give some start point for
        the overloaded method.
        """
