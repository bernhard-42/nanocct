"""OCCT package BSplSLib (toolkit TKMath)"""

from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp


class BSplSLib_EvaluatorFunction:
    def Evaluate(self, theDerivativeRequest: int, theUParameter: float, theVParameter: float) -> tuple[float, int]:
        """Function evaluation method to be defined by descendant"""

    def __call__(self, theDerivativeRequest: int, theUParameter: float, theVParameter: float) -> tuple[float, int]:
        """Shortcut for function-call style usage"""

class BSplSLib:
    """
    BSplSLib B-spline surface Library
    This package provides an implementation of geometric
    functions for rational and non rational, periodic and non
    periodic B-spline surface computation.

    this package uses the multi-dimensions splines methods
    provided in the package BSplCLib.

    In this package the B-spline surface is defined with:
    . its control points :  Array2OfPnt     Poles
    . its weights        :  Array2OfReal    Weights
    . its knots and their multiplicity in the two parametric
    direction U and V: Array1OfReal UKnots, VKnots and
    Array1OfInteger UMults, VMults.
    . the degree of the normalized Spline functions:
    UDegree, VDegree

    . the Booleans URational, VRational to know if the weights
    are constant in the U or V direction.

    . the Booleans UPeriodic, VRational to know if the surface
    is periodic in the U or V direction.

    Warnings: The bounds of UKnots and UMults should be the
    same, the bounds of VKnots and VMults should be the same,
    the bounds of Poles and Weights should be the same.

    The Control points representation is:
    Poles(Uorigin,Vorigin) ...................Poles(Uorigin,Vend)
    .                                     .
    .                                     .
    Poles(Uend, Vorigin) .....................Poles(Uend, Vend)

    For the double array the row indice corresponds to the
    parametric U direction and the columns indice corresponds
    to the parametric V direction.

    Note: weight and multiplicity arrays can be passed by pointer for
    some functions so that NULL pointer is valid.
    That means no weights/no multiplicities passed.

    KeyWords :
    B-spline surface, Functions, Library

    References :
    . A survey of curve and surface methods in CADG Wolfgang BOHM
    CAGD 1 (1984)
    . On de Boor-like algorithms and blossoming Wolfgang BOEHM
    cagd 5 (1988)
    . Blossoming and knot insertion algorithms for B-spline curves
    Ronald N. GOLDMAN
    . Modelisation des surfaces en CAO, Henri GIAUME Peugeot SA
    . Curves and Surfaces for Computer Aided Geometric Design,
    a practical guide Gerald Farin
    """

    def __init__(self) -> None: ...

    @staticmethod
    def RationalDerivative(UDeg: int, VDeg: int, N: int, M: int, All: bool = True) -> tuple[float, float]:
        """
        this is a one dimensional function
        typedef  void (*EvaluatorFunction)  (
        int     // Derivative Request
        double    *   // StartEnd[2][2]
        //  [0] = U
        //  [1] = V
        //        [0] = start
        //        [1] = end
        double        // UParameter
        double        // VParamerer
        double    &   // Result
        int &) ;// Error Code
        serves to multiply a given vectorial BSpline by a function
        Computes the derivatives of a ratio of two-variables
        functions x(u,v) / w(u,v) at orders
        <N,M>, x(u,v) is a vector in dimension <3>.

        <Ders> is an array containing the values of the
        input derivatives from 0 to std::min(<N>,<UDeg>), 0 to
        std::min(<M>,<VDeg>). For orders higher than
        <UDeg,VDeg> the input derivatives are assumed to
        be 0.

        The <Ders> is a 2d array and the dimension of the
        lines is always (<VDeg>+1) * (<3>+1), even
        if <N> is smaller than <Udeg> (the derivatives
        higher than <N> are not used).

        Content of <Ders>:

        x(i,j)[k] means: the composant k of x derivated
        (i) times in u and (j) times in v.

        ... First line ...

        x[1],x[2],...,x[3],w
        x(0,1)[1],...,x(0,1)[3],w(1,0)
        ...
        x(0,VDeg)[1],...,x(0,VDeg)[3],w(0,VDeg)

        ... Then second line ...

        x(1,0)[1],...,x(1,0)[3],w(1,0)
        x(1,1)[1],...,x(1,1)[3],w(1,1)
        ...
        x(1,VDeg)[1],...,x(1,VDeg)[3],w(1,VDeg)

        ...

        ... Last line ...

        x(UDeg,0)[1],...,x(UDeg,0)[3],w(UDeg,0)
        x(UDeg,1)[1],...,x(UDeg,1)[3],w(UDeg,1)
        ...
        x(Udeg,VDeg)[1],...,x(UDeg,VDeg)[3],w(Udeg,VDeg)

        If <All> is false, only the derivative at order
        <N,M> is computed. <RDers> is an array of length
        3 which will contain the result :

        x(1)/w , x(2)/w ,  ... derivated <N> <M> times

        If <All> is true multiples derivatives are
        computed. All the derivatives (i,j) with 0 <= i+j
        <= std::max(N,M) are computed. <RDers> is an array of
        length 3 * (<N>+1) * (<M>+1) which will contains:

        x(1)/w , x(2)/w ,  ...
        x(1)/w , x(2)/w ,  ... derivated <0,1> times
        x(1)/w , x(2)/w ,  ... derivated <0,2> times
        ...
        x(1)/w , x(2)/w ,  ... derivated <0,N> times

        x(1)/w , x(2)/w ,  ... derivated <1,0> times
        x(1)/w , x(2)/w ,  ... derivated <1,1> times
        ...
        x(1)/w , x(2)/w ,  ... derivated <1,N> times

        x(1)/w , x(2)/w ,  ... derivated <N,0> times
        ....
        Warning: <RDers> must be dimensioned properly.
        """

    @staticmethod
    def D0(U: float, V: float, UIndex: int, VIndex: int, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, UKnots: nanoocp.NCollection.NCollection_Array1__double, VKnots: nanoocp.NCollection.NCollection_Array1__double, UMults: nanoocp.NCollection.NCollection_Array1__int, VMults: nanoocp.NCollection.NCollection_Array1__int, UDegree: int, VDegree: int, URat: bool, VRat: bool, UPer: bool, VPer: bool, P: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def D1(U: float, V: float, UIndex: int, VIndex: int, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, UKnots: nanoocp.NCollection.NCollection_Array1__double, VKnots: nanoocp.NCollection.NCollection_Array1__double, UMults: nanoocp.NCollection.NCollection_Array1__int, VMults: nanoocp.NCollection.NCollection_Array1__int, Degree: int, VDegree: int, URat: bool, VRat: bool, UPer: bool, VPer: bool, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def D2(U: float, V: float, UIndex: int, VIndex: int, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, UKnots: nanoocp.NCollection.NCollection_Array1__double, VKnots: nanoocp.NCollection.NCollection_Array1__double, UMults: nanoocp.NCollection.NCollection_Array1__int, VMults: nanoocp.NCollection.NCollection_Array1__int, UDegree: int, VDegree: int, URat: bool, VRat: bool, UPer: bool, VPer: bool, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def D3(U: float, V: float, UIndex: int, VIndex: int, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, UKnots: nanoocp.NCollection.NCollection_Array1__double, VKnots: nanoocp.NCollection.NCollection_Array1__double, UMults: nanoocp.NCollection.NCollection_Array1__int, VMults: nanoocp.NCollection.NCollection_Array1__int, UDegree: int, VDegree: int, URat: bool, VRat: bool, UPer: bool, VPer: bool, P: nanoocp.gp.gp_Pnt, Vu: nanoocp.gp.gp_Vec, Vv: nanoocp.gp.gp_Vec, Vuu: nanoocp.gp.gp_Vec, Vvv: nanoocp.gp.gp_Vec, Vuv: nanoocp.gp.gp_Vec, Vuuu: nanoocp.gp.gp_Vec, Vvvv: nanoocp.gp.gp_Vec, Vuuv: nanoocp.gp.gp_Vec, Vuvv: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def DN(U: float, V: float, Nu: int, Nv: int, UIndex: int, VIndex: int, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, UKnots: nanoocp.NCollection.NCollection_Array1__double, VKnots: nanoocp.NCollection.NCollection_Array1__double, UMults: nanoocp.NCollection.NCollection_Array1__int, VMults: nanoocp.NCollection.NCollection_Array1__int, UDegree: int, VDegree: int, URat: bool, VRat: bool, UPer: bool, VPer: bool, Vn: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def Iso(Param: float, IsU: bool, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, Knots: nanoocp.NCollection.NCollection_Array1__double, Mults: nanoocp.NCollection.NCollection_Array1__int, Degree: int, Periodic: bool, CPoles: nanoocp.NCollection.NCollection_Array1__gp_Pnt, CWeights: nanoocp.NCollection.NCollection_Array1__double) -> None:
        """
        Computes the poles and weights of an isoparametric
        curve at parameter <Param> (UIso if <IsU> is True,
        VIso else).
        """

    @overload
    @staticmethod
    def Reverse(Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Last: int, UDirection: bool) -> None:
        """
        Reverses the array of poles. Last is the Index of
        the new first Row( Col) of Poles.
        On a non periodic surface Last is
        Poles.Upper().
        On a periodic curve last is
        (number of flat knots - degree - 1)
        or
        (sum of multiplicities(but for the last) + degree
        - 1)
        """

    @overload
    @staticmethod
    def Reverse(Weights: nanoocp.NCollection.NCollection_Array2__double, Last: int, UDirection: bool) -> None:
        """Reverses the array of weights."""

    @staticmethod
    def HomogeneousD0(U: float, V: float, UIndex: int, VIndex: int, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, UKnots: nanoocp.NCollection.NCollection_Array1__double, VKnots: nanoocp.NCollection.NCollection_Array1__double, UMults: nanoocp.NCollection.NCollection_Array1__int, VMults: nanoocp.NCollection.NCollection_Array1__int, UDegree: int, VDegree: int, URat: bool, VRat: bool, UPer: bool, VPer: bool, P: nanoocp.gp.gp_Pnt) -> float:
        """
        Makes an homogeneous evaluation of Poles and Weights
        any and returns in P the Numerator value and
        in W the Denominator value if Weights are present
        otherwise returns 1.0e0
        """

    @staticmethod
    def HomogeneousD1(U: float, V: float, UIndex: int, VIndex: int, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, UKnots: nanoocp.NCollection.NCollection_Array1__double, VKnots: nanoocp.NCollection.NCollection_Array1__double, UMults: nanoocp.NCollection.NCollection_Array1__int, VMults: nanoocp.NCollection.NCollection_Array1__int, UDegree: int, VDegree: int, URat: bool, VRat: bool, UPer: bool, VPer: bool, N: nanoocp.gp.gp_Pnt, Nu: nanoocp.gp.gp_Vec, Nv: nanoocp.gp.gp_Vec) -> tuple[float, float, float]:
        """
        Makes an homogeneous evaluation of Poles and Weights
        any and returns in P the Numerator value and
        in W the Denominator value if Weights are present
        otherwise returns 1.0e0
        """

    @staticmethod
    def IsRational(Weights: nanoocp.NCollection.NCollection_Array2__double, I1: int, I2: int, J1: int, J2: int, Epsilon: float = 0.0) -> bool:
        """
        Returns False if all the weights of the array <Weights>
        in the area [I1,I2] * [J1,J2] are identic.
        Epsilon is used for comparing weights.
        If Epsilon is 0. the Epsilon of the first weight is used.
        """

    @overload
    @staticmethod
    def SetPoles(Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, FP: nanoocp.NCollection.NCollection_Array1__double, UDirection: bool) -> None: ...

    @overload
    @staticmethod
    def SetPoles(Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, FP: nanoocp.NCollection.NCollection_Array1__double, UDirection: bool) -> None:
        """Copy in FP the coordinates of the poles."""

    @overload
    @staticmethod
    def GetPoles(FP: nanoocp.NCollection.NCollection_Array1__double, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, UDirection: bool) -> None: ...

    @overload
    @staticmethod
    def GetPoles(FP: nanoocp.NCollection.NCollection_Array1__double, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, UDirection: bool) -> None:
        """Get from FP the coordinates of the poles."""

    @staticmethod
    def MovePoint(U: float, V: float, Displ: nanoocp.gp.gp_Vec, UIndex1: int, UIndex2: int, VIndex1: int, VIndex2: int, UDegree: int, VDegree: int, Rational: bool, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, UFlatKnots: nanoocp.NCollection.NCollection_Array1__double, VFlatKnots: nanoocp.NCollection.NCollection_Array1__double, NewPoles: nanoocp.NCollection.NCollection_Array2__gp_Pnt) -> tuple[int, int, int, int]:
        """
        Find the new poles which allows an old point (with a
        given u,v as parameters) to reach a new position
        UIndex1,UIndex2 indicate the range of poles we can
        move for U
        (1, UNbPoles-1) or (2, UNbPoles) -> no constraint
        for one side in U
        (2, UNbPoles-1) -> the ends are enforced for U
        don't enter (1,NbPoles) and (1,VNbPoles)
        -> error: rigid move
        if problem in BSplineBasis calculation, no change
        for the curve and
        UFirstIndex, VLastIndex = 0
        VFirstIndex, VLastIndex = 0
        """

    @staticmethod
    def InsertKnots(UDirection: bool, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, Knots: nanoocp.NCollection.NCollection_Array1__double, Mults: nanoocp.NCollection.NCollection_Array1__int, AddKnots: nanoocp.NCollection.NCollection_Array1__double, AddMults: nanoocp.NCollection.NCollection_Array1__int, NewPoles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, NewWeights: nanoocp.NCollection.NCollection_Array2__double, NewKnots: nanoocp.NCollection.NCollection_Array1__double, NewMults: nanoocp.NCollection.NCollection_Array1__int, Epsilon: float, Add: bool = True) -> None: ...

    @staticmethod
    def RemoveKnot(UDirection: bool, Index: int, Mult: int, Degree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, Knots: nanoocp.NCollection.NCollection_Array1__double, Mults: nanoocp.NCollection.NCollection_Array1__int, NewPoles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, NewWeights: nanoocp.NCollection.NCollection_Array2__double, NewKnots: nanoocp.NCollection.NCollection_Array1__double, NewMults: nanoocp.NCollection.NCollection_Array1__int, Tolerance: float) -> bool: ...

    @staticmethod
    def IncreaseDegree(UDirection: bool, Degree: int, NewDegree: int, Periodic: bool, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, Knots: nanoocp.NCollection.NCollection_Array1__double, Mults: nanoocp.NCollection.NCollection_Array1__int, NewPoles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, NewWeights: nanoocp.NCollection.NCollection_Array2__double, NewKnots: nanoocp.NCollection.NCollection_Array1__double, NewMults: nanoocp.NCollection.NCollection_Array1__int) -> None: ...

    @staticmethod
    def Unperiodize(UDirection: bool, Degree: int, Mults: nanoocp.NCollection.NCollection_Array1__int, Knots: nanoocp.NCollection.NCollection_Array1__double, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, NewMults: nanoocp.NCollection.NCollection_Array1__int, NewKnots: nanoocp.NCollection.NCollection_Array1__double, NewPoles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, NewWeights: nanoocp.NCollection.NCollection_Array2__double) -> None: ...

    @staticmethod
    def NoWeights() -> nanoocp.NCollection.NCollection_Array2__double:
        """Used as argument for a non rational curve."""

    @overload
    @staticmethod
    def BuildCache(U: float, V: float, USpanDomain: float, VSpanDomain: float, UPeriodicFlag: bool, VPeriodicFlag: bool, UDegree: int, VDegree: int, UIndex: int, VIndex: int, UFlatKnots: nanoocp.NCollection.NCollection_Array1__double, VFlatKnots: nanoocp.NCollection.NCollection_Array1__double, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, CachePoles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, CacheWeights: nanoocp.NCollection.NCollection_Array2__double) -> None:
        """
        Perform the evaluation of the Taylor expansion
        of the Bspline normalized between 0 and 1.
        If rational computes the homogeneous Taylor expansion
        for the numerator and stores it in CachePoles
        """

    @overload
    @staticmethod
    def BuildCache(theU: float, theV: float, theUSpanDomain: float, theVSpanDomain: float, theUPeriodic: bool, theVPeriodic: bool, theUDegree: int, theVDegree: int, theUIndex: int, theVIndex: int, theUFlatKnots: nanoocp.NCollection.NCollection_Array1__double, theVFlatKnots: nanoocp.NCollection.NCollection_Array1__double, thePoles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, theWeights: nanoocp.NCollection.NCollection_Array2__double, theCacheArray: nanoocp.NCollection.NCollection_Array2__double) -> None:
        """
        Perform the evaluation of the Taylor expansion
        of the Bspline normalized between 0 and 1.
        Structure of result optimized for BSplSLib_Cache.
        """

    @staticmethod
    def CacheD0(U: float, V: float, UDegree: int, VDegree: int, UCacheParameter: float, VCacheParameter: float, USpanLenght: float, VSpanLength: float, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, Point: nanoocp.gp.gp_Pnt) -> None:
        """
        Perform the evaluation of the of the cache
        the parameter must be normalized between
        the 0 and 1 for the span.
        The Cache must be valid when calling this
        routine. Geom Package will insure that.
        and then multiplies by the weights
        this just evaluates the current point
        the CacheParameter is where the Cache was
        constructed the SpanLength is to normalize
        the polynomial in the cache to avoid bad conditioning
        effects
        """

    @staticmethod
    def CoefsD0(U: float, V: float, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, Point: nanoocp.gp.gp_Pnt) -> None:
        """
        Calls CacheD0 for Bezier Surfaces Arrays computed with
        the method PolesCoefficients.
        Warning: To be used for BezierSurfaces ONLY!!!
        """

    @staticmethod
    def CacheD1(U: float, V: float, UDegree: int, VDegree: int, UCacheParameter: float, VCacheParameter: float, USpanLenght: float, VSpanLength: float, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, Point: nanoocp.gp.gp_Pnt, VecU: nanoocp.gp.gp_Vec, VecV: nanoocp.gp.gp_Vec) -> None:
        """
        Perform the evaluation of the of the cache
        the parameter must be normalized between
        the 0 and 1 for the span.
        The Cache must be valid when calling this
        routine. Geom Package will insure that.
        and then multiplies by the weights
        this just evaluates the current point
        the CacheParameter is where the Cache was
        constructed the SpanLength is to normalize
        the polynomial in the cache to avoid bad conditioning
        effects
        """

    @staticmethod
    def CoefsD1(U: float, V: float, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, Point: nanoocp.gp.gp_Pnt, VecU: nanoocp.gp.gp_Vec, VecV: nanoocp.gp.gp_Vec) -> None:
        """
        Calls CacheD0 for Bezier Surfaces Arrays computed with
        the method PolesCoefficients.
        Warning: To be used for BezierSurfaces ONLY!!!
        """

    @staticmethod
    def CacheD2(U: float, V: float, UDegree: int, VDegree: int, UCacheParameter: float, VCacheParameter: float, USpanLenght: float, VSpanLength: float, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, Point: nanoocp.gp.gp_Pnt, VecU: nanoocp.gp.gp_Vec, VecV: nanoocp.gp.gp_Vec, VecUU: nanoocp.gp.gp_Vec, VecUV: nanoocp.gp.gp_Vec, VecVV: nanoocp.gp.gp_Vec) -> None:
        """
        Perform the evaluation of the of the cache
        the parameter must be normalized between
        the 0 and 1 for the span.
        The Cache must be valid when calling this
        routine. Geom Package will insure that.
        and then multiplies by the weights
        this just evaluates the current point
        the CacheParameter is where the Cache was
        constructed the SpanLength is to normalize
        the polynomial in the cache to avoid bad conditioning
        effects
        """

    @staticmethod
    def CoefsD2(U: float, V: float, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, Point: nanoocp.gp.gp_Pnt, VecU: nanoocp.gp.gp_Vec, VecV: nanoocp.gp.gp_Vec, VecUU: nanoocp.gp.gp_Vec, VecUV: nanoocp.gp.gp_Vec, VecVV: nanoocp.gp.gp_Vec) -> None:
        """
        Calls CacheD0 for Bezier Surfaces Arrays computed with
        the method PolesCoefficients.
        Warning: To be used for BezierSurfaces ONLY!!!
        """

    @overload
    @staticmethod
    def PolesCoefficients(Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, CachePoles: nanoocp.NCollection.NCollection_Array2__gp_Pnt) -> None:
        """Warning! To be used for BezierSurfaces ONLY!!!"""

    @overload
    @staticmethod
    def PolesCoefficients(Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, CachePoles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, CacheWeights: nanoocp.NCollection.NCollection_Array2__double) -> None:
        """
        Encapsulation of BuildCache to perform the
        evaluation of the Taylor expansion for beziersurfaces
        at parameters 0.,0.;
        Warning: To be used for BezierSurfaces ONLY!!!
        """

    @staticmethod
    def Resolution(Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, UKnots: nanoocp.NCollection.NCollection_Array1__double, VKnots: nanoocp.NCollection.NCollection_Array1__double, UMults: nanoocp.NCollection.NCollection_Array1__int, VMults: nanoocp.NCollection.NCollection_Array1__int, UDegree: int, VDegree: int, URat: bool, VRat: bool, UPer: bool, VPer: bool, Tolerance3D: float) -> tuple[float, float]:
        """
        Given a tolerance in 3D space returns two
        tolerances, one in U one in V such that for
        all (u1,v1) and (u0,v0) in the domain of
        the surface f(u,v) we have :
        | u1 - u0 | < UTolerance and
        | v1 - v0 | < VTolerance
        we have |f (u1,v1) - f (u0,v0)| < Tolerance3D
        """

    @overload
    @staticmethod
    def Interpolate(UDegree: int, VDegree: int, UFlatKnots: nanoocp.NCollection.NCollection_Array1__double, VFlatKnots: nanoocp.NCollection.NCollection_Array1__double, UParameters: nanoocp.NCollection.NCollection_Array1__double, VParameters: nanoocp.NCollection.NCollection_Array1__double, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double) -> int:
        """
        Performs the interpolation of the data points given in
        the Poles array in the form
        [1,...,RL][1,...,RC][1...PolesDimension]. The
        ColLength CL and the Length of UParameters must be the
        same. The length of VFlatKnots is VDegree + CL + 1.

        The RowLength RL and the Length of VParameters must be
        the same. The length of VFlatKnots is Degree + RL + 1.

        Warning: the method used to do that interpolation
        is gauss elimination WITHOUT pivoting. Thus if the
        diagonal is not dominant there is no guarantee that
        the algorithm will work. Nevertheless for Cubic
        interpolation at knots or interpolation at Scheonberg
        points the method will work. The InversionProblem
        will report 0 if there was no problem else it will
        give the index of the faulty pivot
        """

    @overload
    @staticmethod
    def Interpolate(UDegree: int, VDegree: int, UFlatKnots: nanoocp.NCollection.NCollection_Array1__double, VFlatKnots: nanoocp.NCollection.NCollection_Array1__double, UParameters: nanoocp.NCollection.NCollection_Array1__double, VParameters: nanoocp.NCollection.NCollection_Array1__double, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt) -> int:
        """
        Performs the interpolation of the data points given in
        the Poles array.
        The ColLength CL and the Length of UParameters must be
        the same. The length of VFlatKnots is VDegree + CL + 1.

        The RowLength RL and the Length of VParameters must be
        the same. The length of VFlatKnots is Degree + RL + 1.

        Warning: the method used to do that interpolation
        is gauss elimination WITHOUT pivoting. Thus if the
        diagonal is not dominant there is no guarantee that
        the algorithm will work. Nevertheless for Cubic
        interpolation at knots or interpolation at Scheonberg
        points the method will work. The InversionProblem
        will report 0 if there was no problem else it will
        give the index of the faulty pivot
        """

    @staticmethod
    def FunctionMultiply(Function: BSplSLib_EvaluatorFunction, UBSplineDegree: int, VBSplineDegree: int, UBSplineKnots: nanoocp.NCollection.NCollection_Array1__double, VBSplineKnots: nanoocp.NCollection.NCollection_Array1__double, UMults: nanoocp.NCollection.NCollection_Array1__int, VMults: nanoocp.NCollection.NCollection_Array1__int, Poles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, Weights: nanoocp.NCollection.NCollection_Array2__double, UFlatKnots: nanoocp.NCollection.NCollection_Array1__double, VFlatKnots: nanoocp.NCollection.NCollection_Array1__double, UNewDegree: int, VNewDegree: int, NewNumerator: nanoocp.NCollection.NCollection_Array2__gp_Pnt, NewDenominator: nanoocp.NCollection.NCollection_Array2__double) -> int:
        """
        this will multiply a given BSpline numerator N(u,v)
        and denominator D(u,v) defined by its
        U/VBSplineDegree and U/VBSplineKnots, and
        U/VMults. Its Poles and Weights are arrays which are
        coded as array2 of the form
        [1..UNumPoles][1..VNumPoles] by a function a(u,v)
        which is assumed to satisfy the following:
        1. a(u,v) * N(u,v) and a(u,v) * D(u,v) is a polynomial
        BSpline that can be expressed exactly as a BSpline of
        degree U/VNewDegree on the knots U/VFlatKnots
        2. the range of a(u,v) is the same as the range of
        N(u,v) or D(u,v)
        Warning: it is the caller's responsibility to
        insure that conditions 1. and 2. above are satisfied
        no check whatsoever is made in this method
        theStatus will return 0 if OK else it will return the
        pivot index of the matrix that was inverted to
        compute the multiplied BSpline : the method used
        is interpolation at Schoenenberg points of
        a(u,v)* N(u,v) and a(u,v) * D(u,v)
        theStatus will return 0 if OK else it will return the pivot index
        of the matrix that was inverted to compute the multiplied
        BSpline: the method used is interpolation at Schoenenberg
        points of a(u,v)*F(u,v)
        --
        """

    @staticmethod
    def UnitWeights(theNbUPoles: int, theNbVPoles: int) -> nanoocp.NCollection.NCollection_Array2__double:
        """
        Returns an NCollection_Array2<double> filled with 1.0 values.
        If theNbUPoles * theNbVPoles <= BSplCLib::MaxUnitWeightsSize(),
        references a pre-allocated global array (zero allocation).
        Otherwise, allocates a new array and fills with 1.0.
        @warning The returned array may reference global static memory -- do NOT modify elements.
        @param[in] theNbUPoles number of poles in U direction
        @param[in] theNbVPoles number of poles in V direction
        @return array of unit weights with bounds [1, theNbUPoles] x [1, theNbVPoles]
        """

class BSplSLib_Cache(nanoocp.Standard.Standard_Transient):
    """
    \\brief A cache class for Bezier and B-spline surfaces.

    Defines all data, that can be cached on a span of the surface.
    The data should be recalculated in going from span to span.
    """

    def __init__(self, theDegreeU: int, thePeriodicU: bool, theFlatKnotsU: nanoocp.NCollection.NCollection_Array1__double, theDegreeV: int, thePeriodicV: bool, theFlatKnotsV: nanoocp.NCollection.NCollection_Array1__double, theWeights: nanoocp.NCollection.NCollection_Array2__double = None) -> None:
        """
        Constructor for caching of the span for the surface
        \\param theDegreeU    degree along the first parameter (U) of the surface
        \\param thePeriodicU  identify the surface is periodical along U axis
        \\param theFlatKnotsU knots of the surface (with repetition) along U axis
        \\param theDegreeV    degree along the second parameter (V) of the surface
        \\param thePeriodicV  identify the surface is periodical along V axis
        \\param theFlatKnotsV knots of the surface (with repetition) along V axis
        \\param theWeights    array of weights of corresponding poles
        """

    def IsCacheValid(self, theParameterU: float, theParameterV: float) -> bool:
        """
        Verifies validity of the cache using parameters of the point
        \\param theParameterU  first parameter of the point placed in the span
        \\param theParameterV  second parameter of the point placed in the span
        """

    def BuildCache(self, theParameterU: float, theParameterV: float, theFlatKnotsU: nanoocp.NCollection.NCollection_Array1__double, theFlatKnotsV: nanoocp.NCollection.NCollection_Array1__double, thePoles: nanoocp.NCollection.NCollection_Array2__gp_Pnt, theWeights: nanoocp.NCollection.NCollection_Array2__double = None) -> None:
        """
        Recomputes the cache data. Does not verify validity of the cache
        \\param theParameterU  the parametric value on the U axis to identify the span
        \\param theParameterV  the parametric value on the V axis to identify the span
        \\param theDegreeU     degree along U axis
        \\param thePeriodicU   identify whether the surface is periodic along U axis
        \\param theFlatKnotsU  flat knots of the surface along U axis
        \\param theDegreeV     degree along V axis
        \\param thePeriodicV   identify whether the surface is periodic along V axis
        \\param theFlatKnotsV  flat knots of the surface along V axis
        \\param thePoles       array of poles of the surface
        \\param theWeights     array of weights of corresponding poles
        """

    def D0(self, theU: float, theV: float, thePoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Calculates the point on the surface for specified parameters
        \\param[in]  theU      first parameter for calculation of the value
        \\param[in]  theV      second parameter for calculation of the value
        \\param[out] thePoint  the result of calculation (the point on the surface)
        """

    def D1(self, theU: float, theV: float, thePoint: nanoocp.gp.gp_Pnt, theTangentU: nanoocp.gp.gp_Vec, theTangentV: nanoocp.gp.gp_Vec) -> None:
        """
        Calculates the point on the surface and its first derivative
        \\param[in]  theU         first parameter of calculation of the value
        \\param[in]  theV         second parameter of calculation of the value
        \\param[out] thePoint     the result of calculation (the point on the surface)
        \\param[out] theTangentU  tangent vector along U axis in the calculated point
        \\param[out] theTangentV  tangent vector along V axis in the calculated point
        """

    def D2(self, theU: float, theV: float, thePoint: nanoocp.gp.gp_Pnt, theTangentU: nanoocp.gp.gp_Vec, theTangentV: nanoocp.gp.gp_Vec, theCurvatureU: nanoocp.gp.gp_Vec, theCurvatureV: nanoocp.gp.gp_Vec, theCurvatureUV: nanoocp.gp.gp_Vec) -> None:
        """
        Calculates the point on the surface and derivatives till second order
        \\param[in]  theU            first parameter of calculation of the value
        \\param[in]  theV            second parameter of calculation of the value
        \\param[out] thePoint        the result of calculation (the point on the surface)
        \\param[out] theTangentU     tangent vector along U axis in the calculated point
        \\param[out] theTangentV     tangent vector along V axis in the calculated point
        \\param[out] theCurvatureU   curvature vector (2nd derivative on U) along U axis
        \\param[out] theCurvatureV   curvature vector (2nd derivative on V) along V axis
        \\param[out] theCurvatureUV  2nd mixed derivative on U anv V
        """

    def D0Local(self, theLocalU: float, theLocalV: float, thePoint: nanoocp.gp.gp_Pnt) -> None:
        """
        Calculates the point using pre-computed local parameters in [-1, 1] range.
        This bypasses periodic normalization and local parameter calculation.
        @param[in]  theLocalU pre-computed local U parameter: (U - SpanMid) / SpanHalfLen
        @param[in]  theLocalV pre-computed local V parameter: (V - SpanMid) / SpanHalfLen
        @param[out] thePoint  the result of calculation (the point on the surface)
        """

    def D1Local(self, theLocalU: float, theLocalV: float, thePoint: nanoocp.gp.gp_Pnt, theTangentU: nanoocp.gp.gp_Vec, theTangentV: nanoocp.gp.gp_Vec) -> None:
        """
        Calculates the point and first derivatives using pre-computed local parameters in [-1, 1]
        range. This bypasses periodic normalization and local parameter calculation.
        @param[in]  theLocalU   pre-computed local U parameter: (U - SpanMid) / SpanHalfLen
        @param[in]  theLocalV   pre-computed local V parameter: (V - SpanMid) / SpanHalfLen
        @param[out] thePoint    the result of calculation (the point on the surface)
        @param[out] theTangentU tangent vector along U axis in the calculated point
        @param[out] theTangentV tangent vector along V axis in the calculated point
        """

    def D2Local(self, theLocalU: float, theLocalV: float, thePoint: nanoocp.gp.gp_Pnt, theTangentU: nanoocp.gp.gp_Vec, theTangentV: nanoocp.gp.gp_Vec, theCurvatureU: nanoocp.gp.gp_Vec, theCurvatureV: nanoocp.gp.gp_Vec, theCurvatureUV: nanoocp.gp.gp_Vec) -> None:
        """
        Calculates the point and derivatives till second order using pre-computed local parameters.
        This bypasses periodic normalization and local parameter calculation.
        @param[in]  theLocalU      pre-computed local U parameter: (U - SpanMid) / SpanHalfLen
        @param[in]  theLocalV      pre-computed local V parameter: (V - SpanMid) / SpanHalfLen
        @param[out] thePoint       the result of calculation (the point on the surface)
        @param[out] theTangentU    tangent vector along U axis in the calculated point
        @param[out] theTangentV    tangent vector along V axis in the calculated point
        @param[out] theCurvatureU  curvature vector (2nd derivative on U) along U axis
        @param[out] theCurvatureV  curvature vector (2nd derivative on V) along V axis
        @param[out] theCurvatureUV 2nd mixed derivative on U and V
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
