"""OCCT package AdvApprox (toolkit TKG3d)"""

from typing import overload

import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.PLib
import nanoocp.gp


class AdvApprox_EvaluatorFunction:
    """
    Interface for a class implementing a function to be approximated
    by AdvApprox_ApproxAFunction
    """

class AdvApprox_ApproxAFunction:
    """this approximate a given function"""

    @overload
    def __init__(self, Num1DSS: int, Num2DSS: int, Num3DSS: int, OneDTol: nanoocp.NCollection.NCollection_HArray1[float] | None, TwoDTol: nanoocp.NCollection.NCollection_HArray1[float] | None, ThreeDTol: nanoocp.NCollection.NCollection_HArray1[float] | None, First: float, Last: float, Continuity: nanoocp.GeomAbs.GeomAbs_Shape, MaxDeg: int, MaxSeg: int, Func: AdvApprox_EvaluatorFunction) -> None:
        """
        Constructs approximator tool.

        Warning:
        the Func should be valid reference to object of type
        inherited from class EvaluatorFunction from Approx
        with life time longer than that of the approximator tool;

        the result should be formatted in the following way :
        <--Num1DSS--> <--2 * Num2DSS--> <--3 * Num3DSS-->
        R[0] ....     R[Num1DSS].....                   R[Dimension-1]

        the order in which each Subspace appears should be consistent
        with the tolerances given in the create function and the
        results will be given in that order as well that is :
        Curve2d(n) will correspond to the nth entry
        described by Num2DSS, Curve(n) will correspond to
        the nth entry described by Num3DSS
        The same type of schema applies to the Poles1d, Poles2d and
        Poles.
        """

    @overload
    def __init__(self, Num1DSS: int, Num2DSS: int, Num3DSS: int, OneDTol: nanoocp.NCollection.NCollection_HArray1[float] | None, TwoDTol: nanoocp.NCollection.NCollection_HArray1[float] | None, ThreeDTol: nanoocp.NCollection.NCollection_HArray1[float] | None, First: float, Last: float, Continuity: nanoocp.GeomAbs.GeomAbs_Shape, MaxDeg: int, MaxSeg: int, Func: AdvApprox_EvaluatorFunction, CutTool: AdvApprox_Cutting) -> None:
        """Approximation with user method of cutting"""

    @overload
    def __init__(self, theOther: AdvApprox_ApproxAFunction) -> None: ...

    @staticmethod
    def Approximation(TotalDimension: int, TotalNumSS: int, LocalDimension: nanoocp.NCollection.NCollection_Array1[int], First: float, Last: float, Evaluator: AdvApprox_EvaluatorFunction, CutTool: AdvApprox_Cutting, ContinuityOrder: int, NumMaxCoeffs: int, MaxSegments: int, TolerancesArray: nanoocp.NCollection.NCollection_Array1[float], code_precis: int, NumCoeffPerCurveArray: nanoocp.NCollection.NCollection_Array1[int], LocalCoefficientArray: nanoocp.NCollection.NCollection_Array1[float], IntervalsArray: nanoocp.NCollection.NCollection_Array1[float], ErrorMaxArray: nanoocp.NCollection.NCollection_Array1[float], AverageErrorArray: nanoocp.NCollection.NCollection_Array1[float]) -> tuple[int, int]: ...

    def IsDone(self) -> bool: ...

    def HasResult(self) -> bool: ...

    @overload
    def Poles1d(self) -> nanoocp.NCollection.NCollection_HArray2[float]:
        """returns the poles from the algorithms as is"""

    @overload
    def Poles1d(self, Index: int, P: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """returns the poles at Index from the 1d subspace"""

    @overload
    def Poles2d(self) -> nanoocp.NCollection.NCollection_HArray2[nanoocp.gp.gp_Pnt2d]:
        """returns the poles from the algorithms as is"""

    @overload
    def Poles2d(self, Index: int, P: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """returns the poles at Index from the 2d subspace"""

    @overload
    def Poles(self) -> nanoocp.NCollection.NCollection_HArray2[nanoocp.gp.gp_Pnt]:
        """-- returns the poles from the algorithms as is"""

    @overload
    def Poles(self, Index: int, P: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None:
        """returns the poles at Index from the 3d subspace"""

    def NbPoles(self) -> int:
        """as the name says"""

    def Degree(self) -> int: ...

    def NbKnots(self) -> int: ...

    def NumSubSpaces(self, Dimension: int) -> int: ...

    def Knots(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def Multiplicities(self) -> nanoocp.NCollection.NCollection_HArray1[int]: ...

    @overload
    def MaxError(self, Dimension: int) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """returns the error as is in the algorithms"""

    @overload
    def MaxError(self, Dimension: int, Index: int) -> float: ...

    @overload
    def AverageError(self, Dimension: int) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """returns the error as is in the algorithms"""

    @overload
    def AverageError(self, Dimension: int, Index: int) -> float: ...

    def Dump(self) -> str:
        """display information on approximation."""

class AdvApprox_Cutting:
    """to choose the way of cutting in approximation"""

    def Value(self, a: float, b: float) -> tuple[bool, float]: ...

class AdvApprox_DichoCutting(AdvApprox_Cutting):
    """if Cutting is necessary in [a,b], we cut at (a+b) / 2."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: AdvApprox_DichoCutting) -> None: ...

    def Value(self, a: float, b: float) -> tuple[bool, float]: ...

class AdvApprox_PrefAndRec(AdvApprox_Cutting):
    """
    inherits class Cutting; contains a list of preferential points (pi)i
    and a list of Recommended points used in cutting management.
    if Cutting is necessary in [a,b], we cut at the di nearest from (a+b)/2
    """

    @overload
    def __init__(self, RecomendedCut: nanoocp.NCollection.NCollection_Array1[float], PrefferedCut: nanoocp.NCollection.NCollection_Array1[float], Weight: float = 5.0) -> None: ...

    @overload
    def __init__(self, theOther: AdvApprox_PrefAndRec) -> None: ...

    def Value(self, a: float, b: float) -> tuple[bool, float]:
        """
        cuting value is
        - the recommended point nerest of (a+b)/2
        if pi is in ]a,b[ or else
        -  the preferential point nearest of (a+b) / 2
        if pi is in ](r*a+b)/(r+1) , (a+r*b)/(r+1)[ where r = Weight
        -  or (a+b)/2 else.
        """

class AdvApprox_PrefCutting(AdvApprox_Cutting):
    """
    inherits class Cutting; contains a list of preferential points (di)i
    if Cutting is necessary in [a,b], we cut at the di nearest from (a+b)/2.
    """

    @overload
    def __init__(self, CutPnts: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def __init__(self, theOther: AdvApprox_PrefCutting) -> None: ...

    def Value(self, a: float, b: float) -> tuple[bool, float]: ...

class AdvApprox_SimpleApprox:
    """
    Approximate a function on an interval [First,Last]
    The result is a simple polynomial whose degree is as low as
    possible to satisfy the required tolerance and the
    maximum degree. The maximum error and the average error
    resulting from approximating the function by the polynomial are computed
    """

    @overload
    def __init__(self, TotalDimension: int, TotalNumSS: int, Continuity: nanoocp.GeomAbs.GeomAbs_Shape, WorkDegree: int, NbGaussPoints: int, JacobiBase: nanoocp.PLib.PLib_JacobiPolynomial, Func: AdvApprox_EvaluatorFunction) -> None: ...

    @overload
    def __init__(self, theOther: AdvApprox_SimpleApprox) -> None: ...

    def Perform(self, LocalDimension: nanoocp.NCollection.NCollection_Array1[int], LocalTolerancesArray: nanoocp.NCollection.NCollection_Array1[float], First: float, Last: float, MaxDegree: int) -> None:
        """
        Constructs approximator tool.

        Warning:
        the Func should be valid reference to object of type
        inherited from class EvaluatorFunction from Approx
        with life time longer than that of the approximator tool;
        """

    def IsDone(self) -> bool: ...

    def Degree(self) -> int: ...

    def Coefficients(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """returns the coefficients in the Jacobi Base"""

    def FirstConstr(self) -> nanoocp.NCollection.NCollection_HArray2[float]:
        """returns the constraints at First"""

    def LastConstr(self) -> nanoocp.NCollection.NCollection_HArray2[float]:
        """returns the constraints at Last"""

    def SomTab(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def DifTab(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def MaxError(self, Index: int) -> float: ...

    def AverageError(self, Index: int) -> float: ...

    def Dump(self) -> str:
        """display information on approximation"""
