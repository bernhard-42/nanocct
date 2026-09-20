"""OCCT package MathRoot (toolkit TKMath)"""

from collections.abc import Sequence
from typing import overload

import nanoocp.MathUtils
import nanoocp.NCollection
import nanoocp.MathRoot


class MultipleResult:
    """
    Result for multiple root finding.
    Contains all found roots sorted in ascending order.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MultipleResult) -> None: ...

    def IsDone(self) -> bool:
        """Returns true if computation succeeded."""

    def NbRoots(self) -> int:
        """Returns the number of roots found."""

    def __getitem__(self, theIndex: int) -> float:
        """Access root by index (0-based)."""

    def __bool__(self) -> bool:
        """Conversion to bool for convenient checking."""

    @property
    def Status(self) -> nanoocp.MathUtils.Status:
        """Computation status"""

    @Status.setter
    def Status(self, arg: nanoocp.MathUtils.Status, /) -> None: ...

    @property
    def NbIterations(self) -> int:
        """Total iterations across all roots"""

    @NbIterations.setter
    def NbIterations(self, arg: int, /) -> None: ...

    @property
    def Roots(self) -> nanoocp.NCollection.NCollection_DynamicArray[float]:
        """Found roots (sorted)"""

    @Roots.setter
    def Roots(self, arg: nanoocp.NCollection.NCollection_DynamicArray[float], /) -> None: ...

    @property
    def Values(self) -> nanoocp.NCollection.NCollection_DynamicArray[float]:
        """Function values at roots"""

    @Values.setter
    def Values(self, arg: nanoocp.NCollection.NCollection_DynamicArray[float], /) -> None: ...

    @property
    def IsAllNull(self) -> bool:
        """True if function is essentially zero in range"""

    @IsAllNull.setter
    def IsAllNull(self, arg: bool, /) -> None: ...

class MultipleConfig:
    """Configuration for multiple root finding."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MultipleConfig) -> None: ...

    @property
    def NbSamples(self) -> int:
        """Number of sample points for initial search"""

    @NbSamples.setter
    def NbSamples(self, arg: int, /) -> None: ...

    @property
    def XTolerance(self) -> float:
        """Tolerance on X for convergence"""

    @XTolerance.setter
    def XTolerance(self, arg: float, /) -> None: ...

    @property
    def FTolerance(self) -> float:
        """Tolerance on F(X) for convergence"""

    @FTolerance.setter
    def FTolerance(self, arg: float, /) -> None: ...

    @property
    def NullTolerance(self) -> float:
        """Tolerance to consider function as null"""

    @NullTolerance.setter
    def NullTolerance(self, arg: float, /) -> None: ...

    @property
    def MaxIterations(self) -> int:
        """Max iterations per root refinement"""

    @MaxIterations.setter
    def MaxIterations(self, arg: int, /) -> None: ...

    @property
    def Offset(self) -> float:
        """Find roots of f(x) - Offset = 0"""

    @Offset.setter
    def Offset(self, arg: float, /) -> None: ...

class MultipleGetValueFn:
    """Returns the sampled value at a given index from a math_Vector."""

    def __init__(self, theOther: MultipleGetValueFn) -> None: ...

    def __call__(self, theIndex: int) -> float: ...

class MultipleNoExtraHandler:
    """No-op interval handler for functions without derivative."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MultipleNoExtraHandler) -> None: ...

    def __call__(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: MultipleResult, arg6: float) -> None: ...

class NullInterval:
    """Represents an interval where the function is null (within tolerance)."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: NullInterval) -> None: ...

    @property
    def A(self) -> float:
        """Interval start"""

    @A.setter
    def A(self, arg: float, /) -> None: ...

    @property
    def B(self) -> float:
        """Interval end"""

    @B.setter
    def B(self, arg: float, /) -> None: ...

    @property
    def State(self) -> int:
        """State number (for parametric curves)"""

    @State.setter
    def State(self, arg: int, /) -> None: ...

class AllRootsResult:
    """Result for all roots finder including null intervals."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: AllRootsResult) -> None: ...

    def IsDone(self) -> bool: ...

    def NbRoots(self) -> int: ...

    def NbIntervals(self) -> int: ...

    def __bool__(self) -> bool: ...

    @property
    def Status(self) -> nanoocp.MathUtils.Status: ...

    @Status.setter
    def Status(self, arg: nanoocp.MathUtils.Status, /) -> None: ...

    @property
    def Roots(self) -> nanoocp.NCollection.NCollection_DynamicArray[float]:
        """Isolated root locations"""

    @Roots.setter
    def Roots(self, arg: nanoocp.NCollection.NCollection_DynamicArray[float], /) -> None: ...

    @property
    def RootStates(self) -> nanoocp.NCollection.NCollection_DynamicArray[int]:
        """State numbers for roots"""

    @RootStates.setter
    def RootStates(self, arg: nanoocp.NCollection.NCollection_DynamicArray[int], /) -> None: ...

    @property
    def NullIntervals(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.MathRoot.NullInterval]:
        """Intervals where function is null"""

    @NullIntervals.setter
    def NullIntervals(self, arg: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.MathRoot.NullInterval], /) -> None: ...

class TrigResult:
    """Result for trigonometric equation solver."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TrigResult) -> None: ...

    def IsDone(self) -> bool: ...

    def __bool__(self) -> bool: ...

    @property
    def Status(self) -> nanoocp.MathUtils.Status: ...

    @Status.setter
    def Status(self, arg: nanoocp.MathUtils.Status, /) -> None: ...

    @property
    def Roots(self) -> list[float]: ...

    @Roots.setter
    def Roots(self, arg: Sequence[float], /) -> None: ...

    @property
    def NbRoots(self) -> int: ...

    @NbRoots.setter
    def NbRoots(self, arg: int, /) -> None: ...

    @property
    def InfiniteRoots(self) -> bool: ...

    @InfiniteRoots.setter
    def InfiniteRoots(self, arg: bool, /) -> None: ...

def SortRoots(theResult: MultipleResult) -> None:
    """
    In-place insertion sort of roots and corresponding values by ascending root value.
    """

def AddRoot(theResult: MultipleResult, theEpsX: float, theRoot: float, theValue: float) -> None:
    """
    Helper to add a root if it is not a duplicate of an already found root.
    """

def EffectiveXTolerance(theLower: float, theUpper: float, theXTolerance: float) -> float:
    """
    Compute the minimal X tolerance compatible with the established multi-root behavior.
    """

def Trigonometric(theA: float, theB: float, theC: float, theD: float, theE: float, theInfBound: float = 0.0, theSupBound: float = 6.283185307179586, theEps: float = 1.5e-12) -> TrigResult:
    """
    Solve trigonometric equation: a*cos^2(x) + 2*b*cos(x)*sin(x) + c*cos(x) + d*sin(x) + e = 0.

    Uses half-angle substitution t = tan(x/2) to convert to polynomial:
    - cos(x) = (1-t^2)/(1+t^2)
    - sin(x) = 2t/(1+t^2)

    Resulting polynomial is of degree 4, 3, or 2 depending on coefficients.
    Roots are filtered to lie within [theInfBound, theSupBound].

    @param theA coefficient of cos^2(x)
    @param theB coefficient of cos(x)*sin(x) (equation uses 2*b)
    @param theC coefficient of cos(x)
    @param theD coefficient of sin(x)
    @param theE constant term
    @param theInfBound lower bound for roots (default 0)
    @param theSupBound upper bound for roots (default 2*PI)
    @param theEps tolerance for coefficient comparison
    @return TrigResult containing roots in specified interval
    """

def TrigonometricLinear(theD: float, theE: float, theInfBound: float = 0.0, theSupBound: float = 6.283185307179586) -> TrigResult:
    """
    Solve linear trigonometric equation: d*sin(x) + e = 0.

    @param theD coefficient of sin(x)
    @param theE constant term
    @param theInfBound lower bound for roots
    @param theSupBound upper bound for roots
    @return TrigResult containing roots
    """

def TrigonometricCDE(theC: float, theD: float, theE: float, theInfBound: float = 0.0, theSupBound: float = 6.283185307179586) -> TrigResult:
    """
    Solve trigonometric equation: c*cos(x) + d*sin(x) + e = 0.

    @param theC coefficient of cos(x)
    @param theD coefficient of sin(x)
    @param theE constant term
    @param theInfBound lower bound for roots
    @param theSupBound upper bound for roots
    @return TrigResult containing roots
    """
