"""OCCT package PLib (toolkit TKMath)"""

from typing import overload

import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.math
import nanoocp.gp


class PLib:
    """
    PLib means Polynomial functions library. This pk
    provides basic computation functions for
    polynomial functions.
    Note: weight arrays can be passed by pointer for
    some functions so that NULL pointer is valid.
    That means no weights passed.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: PLib) -> None: ...

    @staticmethod
    def NoWeights() -> nanoocp.NCollection.NCollection_Array1[float]:
        """Used as argument for a non rational functions"""

    @staticmethod
    def NoWeights2() -> nanoocp.NCollection.NCollection_Array2[float]:
        """Used as argument for a non rational functions"""

    @overload
    @staticmethod
    def SetPoles(Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], FP: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def SetPoles(Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float], FP: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def SetPoles(Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], FP: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def SetPoles(Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float], FP: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """Copy in FP the coordinates of the poles."""

    @overload
    @staticmethod
    def GetPoles(FP: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None: ...

    @overload
    @staticmethod
    def GetPoles(FP: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Weights: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def GetPoles(FP: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None: ...

    @overload
    @staticmethod
    def GetPoles(FP: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], Weights: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """Get from FP the coordinates of the poles."""

    @staticmethod
    def Bin(N: int, P: int) -> float:
        """Returns the Binomial Cnp. N should be <= BSplCLib::MaxDegree()."""

    @staticmethod
    def RationalDerivative(Degree: int, N: int, Dimension: int, All: bool = True) -> tuple[float, float]:
        """
        Computes the derivatives of a ratio at order
        <N> in dimension <Dimension>.

        <Ders> is an array containing the values of the
        input derivatives from 0 to std::min(<N>,<Degree>).
        For orders higher than <Degree> the inputcd /s2d1/BMDL/
        derivatives are assumed to be 0.

        Content of <Ders>:

        x(1),x(2),...,x(Dimension),w
        x'(1),x'(2),...,x'(Dimension),w'
        x''(1),x''(2),...,x''(Dimension),w''

        If <All> is false, only the derivative at order
        <N> is computed. <RDers> is an array of length
        Dimension which will contain the result:

        x(1)/w , x(2)/w ,  ... derivated <N> times

        If <All> is true all the derivatives up to order
        <N> are computed. <RDers> is an array of length
        Dimension * (N+1) which will contains:

        x(1)/w , x(2)/w ,  ...
        x(1)/w , x(2)/w ,  ... derivated <1> times
        x(1)/w , x(2)/w ,  ... derivated <2> times
        ...
        x(1)/w , x(2)/w ,  ... derivated <N> times

        Warning: <RDers> must be dimensioned properly.
        """

    @staticmethod
    def RationalDerivatives(DerivativesRequest: int, Dimension: int) -> tuple[float, float, float]:
        """
        Computes DerivativesRequest derivatives of a ratio at
        of a BSpline function of degree <Degree>
        dimension <Dimension>.

        <PolesDerivatives> is an array containing the values
        of the input derivatives from 0 to <DerivativeRequest>
        For orders higher than <Degree> the input
        derivatives are assumed to be 0.

        Content of <PoleasDerivatives> :

        x(1),x(2),...,x(Dimension)
        x'(1),x'(2),...,x'(Dimension)
        x''(1),x''(2),...,x''(Dimension)

        WeightsDerivatives is an array that contains derivatives
        from 0 to <DerivativeRequest>
        After returning from the routine the array
        RationalDerivatives contains the following
        x(1)/w , x(2)/w ,  ...
        x(1)/w , x(2)/w ,  ... derivated once
        x(1)/w , x(2)/w ,  ... twice
        x(1)/w , x(2)/w ,  ... derivated <DerivativeRequest> times

        The array RationalDerivatives and PolesDerivatives
        can be same since the overwrite is non destructive within
        the algorithm

        Warning: <RationalDerivates> must be dimensioned properly.
        """

    @staticmethod
    def EvalPolynomial(U: float, DerivativeOrder: int, Degree: int, Dimension: int, PolynomialCoeff: float) -> float:
        """
        Performs Horner method with synthetic division for derivatives
        parameter <U>, with <Degree> and <Dimension>.
        PolynomialCoeff are stored in the following fashion
        @code
        c0(1)      c0(2) ....       c0(Dimension)
        c1(1)      c1(2) ....       c1(Dimension)

        cDegree(1) cDegree(2) ....  cDegree(Dimension)
        @endcode
        where the polynomial is defined as :
        @code
        2                     Degree
        c0 + c1 X + c2 X  +  ....   cDegree X
        @endcode
        Results stores the result in the following format
        @code
        f(1)             f(2)  ....     f(Dimension)
        (1)           (1)              (1)
        f  (1)        f   (2) ....     f   (Dimension)

        (DerivativeRequest)            (DerivativeRequest)
        f  (1)                         f   (Dimension)
        @endcode
        this just evaluates the point at parameter U

        Warning: <Results> and <PolynomialCoeff> must be dimensioned properly
        """

    @staticmethod
    def NoDerivativeEvalPolynomial(U: float, Degree: int, Dimension: int, DegreeDimension: int, PolynomialCoeff: float) -> float:
        """Same as above with DerivativeOrder = 0;"""

    @staticmethod
    def EvalPoly2Var(U: float, V: float, UDerivativeOrder: int, VDerivativeOrder: int, UDegree: int, VDegree: int, Dimension: int) -> tuple[float, float]:
        """
        Applies EvalPolynomial twice to evaluate the derivative
        of orders UDerivativeOrder in U, VDerivativeOrder in V
        at parameters U,V

        PolynomialCoeff are stored in the following fashion
        @code
        c00(1)  ....       c00(Dimension)
        c10(1)  ....       c10(Dimension)
        ....
        cm0(1)  ....       cm0(Dimension)
        ....
        c01(1)  ....       c01(Dimension)
        c11(1)  ....       c11(Dimension)
        ....
        cm1(1)  ....       cm1(Dimension)
        ....
        c0n(1)  ....       c0n(Dimension)
        c1n(1)  ....       c1n(Dimension)
        ....
        cmn(1)  ....       cmn(Dimension)
        @endcode
        where the polynomial is defined as :
        @code
        2                 m
        c00 + c10 U + c20 U  +  ....  + cm0 U
        2                   m
        + c01 V + c11 UV + c21 U V  +  ....  + cm1 U  V
        n               m n
        + .... + c0n V +  ....  + cmn U V
        @endcode
        with m = UDegree and n = VDegree

        Results stores the result in the following format
        @code
        f(1)             f(2)  ....     f(Dimension)
        @endcode
        Warning: <Results> and <PolynomialCoeff> must be dimensioned properly
        """

    @staticmethod
    def EvalLagrange(U: float, DerivativeOrder: int, Degree: int, Dimension: int) -> tuple[int, float, float, float]:
        """
        Performs the Lagrange Interpolation of
        given series of points with given parameters
        with the requested derivative order
        Results will store things in the following format
        with d = DerivativeOrder
        @code
        [0],             [Dimension-1]              : value
        [Dimension],     [Dimension  + Dimension-1] : first derivative

        [d *Dimension],  [d*Dimension + Dimension-1]: dth   derivative
        @endcode
        """

    @staticmethod
    def EvalCubicHermite(U: float, DerivativeOrder: int, Dimension: int) -> tuple[int, float, float, float, float]:
        """
        Performs the Cubic Hermite Interpolation of
        given series of points with given parameters
        with the requested derivative order.
        ValueArray stores the value at the first and
        last parameter. It has the following format :
        @code
        [0],             [Dimension-1]              : value at first param
        [Dimension],     [Dimension  + Dimension-1] : value at last param
        @endcode
        Derivative array stores the value of the derivatives
        at the first parameter and at the last parameter
        in the following format
        @code
        [0],             [Dimension-1]              : derivative at
        @endcode
        first param
        @code
        [Dimension],     [Dimension  + Dimension-1] : derivative at
        @endcode
        last param

        ParameterArray  stores the first and last parameter
        in the following format :
        @code
        [0] : first parameter
        [1] : last  parameter
        @endcode

        Results will store things in the following format
        with d = DerivativeOrder
        @code
        [0],             [Dimension-1]              : value
        [Dimension],     [Dimension  + Dimension-1] : first derivative

        [d *Dimension],  [d*Dimension + Dimension-1]: dth   derivative
        @endcode
        """

    @staticmethod
    def HermiteCoefficients(FirstParameter: float, LastParameter: float, FirstOrder: int, LastOrder: int, MatrixCoefs: nanoocp.math.math_Matrix) -> bool:
        """
        This build the coefficient of Hermite's polynomes on
        [FirstParameter, LastParameter]

        if j <= FirstOrder+1 then

        MatrixCoefs[i, j] = ith coefficient of the polynome H0,j-1

        else

        MatrixCoefs[i, j] = ith coefficient of the polynome H1,k
        with k = j - FirstOrder - 2

        return false if
        - |FirstParameter| > 100
        - |LastParameter| > 100
        - |FirstParameter| +|LastParameter| < 1/100
        -   |LastParameter - FirstParameter|
        / (|FirstParameter| +|LastParameter|)  < 1/100
        """

    @overload
    @staticmethod
    def CoefficientsPoles(Coefs: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], WCoefs: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], WPoles: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def CoefficientsPoles(Coefs: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], WCoefs: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], WPoles: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def CoefficientsPoles(Coefs: nanoocp.NCollection.NCollection_Array1[float], WCoefs: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[float], WPoles: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def CoefficientsPoles(dim: int, Coefs: nanoocp.NCollection.NCollection_Array1[float], WCoefs: nanoocp.NCollection.NCollection_Array1[float], Poles: nanoocp.NCollection.NCollection_Array1[float], WPoles: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def CoefficientsPoles(Coefs: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], WCoefs: nanoocp.NCollection.NCollection_Array2[float], Poles: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], WPoles: nanoocp.NCollection.NCollection_Array2[float]) -> None: ...

    @overload
    @staticmethod
    def Trimming(U1: float, U2: float, Coeffs: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], WCoeffs: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def Trimming(U1: float, U2: float, Coeffs: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], WCoeffs: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def Trimming(U1: float, U2: float, Coeffs: nanoocp.NCollection.NCollection_Array1[float], WCoeffs: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    @staticmethod
    def Trimming(U1: float, U2: float, dim: int, Coeffs: nanoocp.NCollection.NCollection_Array1[float], WCoeffs: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @staticmethod
    def UTrimming(U1: float, U2: float, Coeffs: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], WCoeffs: nanoocp.NCollection.NCollection_Array2[float]) -> None: ...

    @staticmethod
    def VTrimming(V1: float, V2: float, Coeffs: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], WCoeffs: nanoocp.NCollection.NCollection_Array2[float]) -> None: ...

    @staticmethod
    def HermiteInterpolate(Dimension: int, FirstParameter: float, LastParameter: float, FirstOrder: int, LastOrder: int, FirstConstr: nanoocp.NCollection.NCollection_Array2[float], LastConstr: nanoocp.NCollection.NCollection_Array2[float], Coefficients: nanoocp.NCollection.NCollection_Array1[float]) -> bool:
        """
        Compute the coefficients in the canonical base of the
        polynomial satisfying the given constraints
        at the given parameters
        The array FirstContr(i,j) i=1,Dimension j=0,FirstOrder
        contains the values of the constraint at parameter FirstParameter
        idem for LastConstr
        """

    @staticmethod
    def JacobiParameters(ConstraintOrder: nanoocp.GeomAbs.GeomAbs_Shape, MaxDegree: int, Code: int) -> tuple[int, int]:
        """
        Compute the number of points used for integral
        computations (NbGaussPoints) and the degree of Jacobi
        Polynomial (WorkDegree).
        ConstraintOrder has to be GeomAbs_C0, GeomAbs_C1 or GeomAbs_C2
        Code: Code d' init. des parametres de discretisation.
        = -5
        = -4
        = -3
        = -2
        = -1
        =  1 calcul rapide avec precision moyenne.
        =  2 calcul rapide avec meilleure precision.
        =  3 calcul un peu plus lent avec bonne precision.
        =  4 calcul lent avec la meilleure precision possible.
        """

    @staticmethod
    def NivConstr(ConstraintOrder: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """translates from GeomAbs_Shape to Integer"""

    @staticmethod
    def ConstraintOrder(NivConstr: int) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """translates from Integer to GeomAbs_Shape"""

    @overload
    @staticmethod
    def EvalLength(Degree: int, Dimension: int, U1: float, U2: float) -> tuple[float, float]: ...

    @overload
    @staticmethod
    def EvalLength(Degree: int, Dimension: int, U1: float, U2: float, Tol: float) -> tuple[float, float, float]: ...

class PLib_JacobiPolynomial:
    """
    This class provides method to work with Jacobi Polynomials
    relatively to an order of constraint
    q  = myWorkDegree-2*(myNivConstr+1)
    Jk(t)  for k=0,q compose the Jacobi Polynomial base relatively to the weight W(t)
    iorder is the integer value for the constraints:
    iorder = 0 <=> ConstraintOrder  = GeomAbs_C0
    iorder = 1 <=>  ConstraintOrder = GeomAbs_C1
    iorder = 2 <=> ConstraintOrder = GeomAbs_C2
    P(t) = R(t) + W(t) * Q(t) Where W(t) = (1-t**2)**(2*iordre+2)
    the coefficients JacCoeff represents P(t) JacCoeff are stored as follow:

    c0(1)      c0(2) ....       c0(Dimension)
    c1(1)      c1(2) ....       c1(Dimension)

    cDegree(1) cDegree(2) ....  cDegree(Dimension)

    The coefficients
    c0(1)                  c0(2) ....            c0(Dimension)
    c2*ordre+1(1)                ...          c2*ordre+1(dimension)

    represents the part of the polynomial in the
    canonical base: R(t)
    R(t) = c0 + c1   t + ...+ c2*iordre+1 t**2*iordre+1
    The following coefficients represents the part of the
    polynomial in the Jacobi base ie Q(t)
    Q(t) = c2*iordre+2  J0(t) + ...+ cDegree JDegree-2*iordre-2
    """

    @overload
    def __init__(self, theWorkDegree: int, theConstraintOrder: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Initialize the polynomial class
        Degree has to be <= 30
        ConstraintOrder has to be GeomAbs_C0
        GeomAbs_C1
        GeomAbs_C2
        """

    @overload
    def __init__(self, theOther: PLib_JacobiPolynomial) -> None: ...

    def Points(self, theNbGaussPoints: int, theTabPoints: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        returns the Jacobi Points for Gauss integration ie
        the positive values of the Legendre roots by increasing values
        NbGaussPoints is the number of points chosen for the integral
        computation.
        TabPoints (0,NbGaussPoints/2)
        TabPoints (0) is loaded only for the odd values of NbGaussPoints
        The possible values for NbGaussPoints are : 8, 10,
        15, 20, 25, 30, 35, 40, 50, 61
        NbGaussPoints must be greater than Degree
        """

    def Weights(self, theNbGaussPoints: int, theTabWeights: nanoocp.NCollection.NCollection_Array2[float]) -> None:
        """
        returns the Jacobi weights for Gauss integration only for
        the positive values of the Legendre roots in the order they
        are given by the method Points
        NbGaussPoints is the number of points chosen for the integral
        computation.
        TabWeights (0,NbGaussPoints/2,0,Degree)
        TabWeights (0,.) are only loaded for the odd values of NbGaussPoints
        The possible values for NbGaussPoints are: 8, 10, 15, 20, 25, 30,
        35, 40, 50, 61 NbGaussPoints must be greater than Degree
        """

    def MaxValue(self, theTabMax: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        this method loads for k=0,q the maximum value of
        abs ( W(t)*Jk(t) ) for t bellonging to [-1,1]
        This values are loaded is the array TabMax(0,myWorkDegree-2*(myNivConst+1))
        MaxValue ( me ; TabMaxPointer : in  out  Real );
        """

    def MaxError(self, theDimension: int, theNewDegree: int) -> tuple[float, float]:
        """
        This method computes the maximum error on the polynomial
        W(t) Q(t) obtained by missing the coefficients of JacCoeff from
        NewDegree +1 to Degree
        """

    def ReduceDegree(self, theDimension: int, theMaxDegree: int, theTol: float) -> tuple[float, int, float]:
        """
        Compute NewDegree <= MaxDegree so that MaxError is lower
        than Tol.
        MaxError can be greater than Tol if it is not possible
        to find a NewDegree <= MaxDegree.
        In this case NewDegree = MaxDegree
        """

    def AverageError(self, theDimension: int, theNewDegree: int) -> tuple[float, float]: ...

    def ToCoefficients(self, theDimension: int, theDegree: int, theJacCoeff: nanoocp.NCollection.NCollection_Array1[float], theCoefficients: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """Convert the polynomial P(t) = R(t) + W(t) Q(t) in the canonical base."""

    def D0(self, theU: float, theBasisValue: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """Compute the values of the basis functions in u"""

    def D1(self, theU: float, theBasisValue: nanoocp.NCollection.NCollection_Array1[float], theBasisD1: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the values and the derivatives values of
        the basis functions in u
        """

    def D2(self, theU: float, theBasisValue: nanoocp.NCollection.NCollection_Array1[float], theBasisD1: nanoocp.NCollection.NCollection_Array1[float], theBasisD2: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the values and the derivatives values of
        the basis functions in u
        """

    def D3(self, theU: float, theBasisValue: nanoocp.NCollection.NCollection_Array1[float], theBasisD1: nanoocp.NCollection.NCollection_Array1[float], theBasisD2: nanoocp.NCollection.NCollection_Array1[float], theBasisD3: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the values and the derivatives values of
        the basis functions in u
        """

    def WorkDegree(self) -> int:
        """returns WorkDegree"""

    def NivConstr(self) -> int:
        """returns NivConstr"""

class PLib_HermitJacobi:
    """
    This class provides method to work with Jacobi Polynomials
    relatively to an order of constraint
    q = myWorkDegree-2*(myNivConstr+1)
    Jk(t) for k=0,q compose the Jacobi Polynomial base relatively to the weight W(t)
    iorder is the integer value for the constraints:
    iorder = 0 <=> ConstraintOrder = GeomAbs_C0
    iorder = 1 <=> ConstraintOrder = GeomAbs_C1
    iorder = 2 <=> ConstraintOrder = GeomAbs_C2
    P(t) = H(t) + W(t) * Q(t) Where W(t) = (1-t**2)**(2*iordre+2)
    the coefficients JacCoeff represents P(t) JacCoeff are stored as follow:
    @code
    c0(1)      c0(2) ....       c0(Dimension)
    c1(1)      c1(2) ....       c1(Dimension)

    cDegree(1) cDegree(2) ....  cDegree(Dimension)
    @endcode
    The coefficients
    @code
    c0(1)                  c0(2) ....            c0(Dimension)
    c2*ordre+1(1)                ...          c2*ordre+1(dimension)
    @endcode
    represents the part of the polynomial in the
    Hermit's base: H(t)
    @code
    H(t) = c0H00(t) + c1H01(t) + ...c(iordre)H(0 ;iorder)+ c(iordre+1)H10(t)+...
    @endcode
    The following coefficients represents the part of the
    polynomial in the Jacobi base ie Q(t)
    @code
    Q(t) = c2*iordre+2  J0(t) + ...+ cDegree JDegree-2*iordre-2
    @endcode
    """

    @overload
    def __init__(self, WorkDegree: int, ConstraintOrder: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Initialize the polynomial class
        Degree has to be <= 30
        ConstraintOrder has to be GeomAbs_C0
        GeomAbs_C1
        GeomAbs_C2
        """

    @overload
    def __init__(self, theOther: PLib_HermitJacobi) -> None: ...

    def MaxError(self, Dimension: int, NewDegree: int) -> tuple[float, float]:
        """
        This method computes the maximum error on the polynomial
        W(t) Q(t) obtained by missing the coefficients of JacCoeff from
        NewDegree +1 to Degree
        """

    def ReduceDegree(self, Dimension: int, MaxDegree: int, Tol: float) -> tuple[float, int, float]:
        """
        Compute NewDegree <= MaxDegree so that MaxError is lower
        than Tol.
        MaxError can be greater than Tol if it is not possible
        to find a NewDegree <= MaxDegree.
        In this case NewDegree = MaxDegree
        """

    def AverageError(self, Dimension: int, NewDegree: int) -> tuple[float, float]: ...

    def ToCoefficients(self, Dimension: int, Degree: int, HermJacCoeff: nanoocp.NCollection.NCollection_Array1[float], Coefficients: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """Convert the polynomial P(t) = H(t) + W(t) Q(t) in the canonical base."""

    def D0(self, U: float, BasisValue: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """Compute the values of the basis functions in u"""

    def D1(self, U: float, BasisValue: nanoocp.NCollection.NCollection_Array1[float], BasisD1: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the values and the derivatives values of
        the basis functions in u
        """

    def D2(self, U: float, BasisValue: nanoocp.NCollection.NCollection_Array1[float], BasisD1: nanoocp.NCollection.NCollection_Array1[float], BasisD2: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the values and the derivatives values of
        the basis functions in u
        """

    def D3(self, U: float, BasisValue: nanoocp.NCollection.NCollection_Array1[float], BasisD1: nanoocp.NCollection.NCollection_Array1[float], BasisD2: nanoocp.NCollection.NCollection_Array1[float], BasisD3: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Compute the values and the derivatives values of
        the basis functions in u
        """

    def WorkDegree(self) -> int:
        """returns WorkDegree"""

    def NivConstr(self) -> int:
        """returns NivConstr"""
