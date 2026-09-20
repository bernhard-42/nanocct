"""OCCT package MathSys (toolkit TKMath)"""

from typing import overload

import nanoocp.MathUtils


class NewtonOptions(nanoocp.MathUtils.Config):
    """Solver options for small-dimension Newton methods."""

    @overload
    def __init__(self) -> None:
        """
        Default constructor with strict residual/step tolerances for specialized Newton.
        """

    @overload
    def __init__(self, theOther: NewtonOptions) -> None: ...

    @property
    def MaxStepRatio(self) -> float:
        """Max step as ratio of largest domain size"""

    @MaxStepRatio.setter
    def MaxStepRatio(self, arg: float, /) -> None: ...

    @property
    def EnableLineSearch(self) -> bool:
        """Enable Armijo backtracking line search"""

    @EnableLineSearch.setter
    def EnableLineSearch(self, arg: bool, /) -> None: ...

    @property
    def AllowSoftBounds(self) -> bool:
        """Allow slight bounds extension"""

    @AllowSoftBounds.setter
    def AllowSoftBounds(self, arg: bool, /) -> None: ...

    @property
    def SoftBoundsExtension(self) -> float:
        """Extension ratio for soft bounds"""

    @SoftBoundsExtension.setter
    def SoftBoundsExtension(self, arg: float, /) -> None: ...

class LMConfig(nanoocp.MathUtils.Config):
    """
    Configuration for Levenberg-Marquardt algorithm.
    Extends base Config with damping parameter settings.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theTolerance: float, theMaxIter: int = 100) -> None:
        """
        Constructor with custom tolerance.
        @param theTolerance convergence tolerance
        @param theMaxIter maximum iterations
        """

    @overload
    def __init__(self, theOther: LMConfig) -> None: ...

    @property
    def LambdaInit(self) -> float:
        """Initial damping parameter"""

    @LambdaInit.setter
    def LambdaInit(self, arg: float, /) -> None: ...

    @property
    def LambdaIncrease(self) -> float:
        """Factor to increase lambda on rejected step"""

    @LambdaIncrease.setter
    def LambdaIncrease(self, arg: float, /) -> None: ...

    @property
    def LambdaDecrease(self) -> float:
        """Factor to decrease lambda on accepted step"""

    @LambdaDecrease.setter
    def LambdaDecrease(self, arg: float, /) -> None: ...

    @property
    def LambdaMax(self) -> float:
        """Maximum lambda value before failing"""

    @LambdaMax.setter
    def LambdaMax(self, arg: float, /) -> None: ...

    @property
    def LambdaMin(self) -> float:
        """Minimum lambda value"""

    @LambdaMin.setter
    def LambdaMin(self, arg: float, /) -> None: ...
