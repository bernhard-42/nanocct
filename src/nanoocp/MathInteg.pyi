"""OCCT package MathInteg (toolkit TKMath)"""

from typing import overload

import nanoocp.MathUtils
import nanoocp.math


class KronrodConfig(nanoocp.MathUtils.IntegConfig):
    """Configuration for Gauss-Kronrod integration."""

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theTolerance: float, theMaxIter: int = 100) -> None:
        """Constructor with tolerance."""

    @overload
    def __init__(self, theOther: KronrodConfig) -> None: ...

    @property
    def NbGaussPoints(self) -> int:
        """Number of Gauss points (n), Kronrod will use 2n+1 points"""

    @NbGaussPoints.setter
    def NbGaussPoints(self, arg: int, /) -> None: ...

    @property
    def Adaptive(self) -> bool:
        """Whether to use adaptive subdivision"""

    @Adaptive.setter
    def Adaptive(self, arg: bool, /) -> None: ...

class DoubleExpConfig(nanoocp.MathUtils.IntegConfig):
    """Configuration for double exponential integration."""

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theTolerance: float, theMaxIter: int = 100) -> None:
        """Constructor with tolerance."""

    @overload
    def __init__(self, theOther: DoubleExpConfig) -> None: ...

    @property
    def NbLevels(self) -> int:
        """Number of refinement levels (each doubles points)"""

    @NbLevels.setter
    def NbLevels(self, arg: int, /) -> None: ...

    @property
    def StepFactor(self) -> float:
        """Initial step size h = StepFactor / NbPoints"""

    @StepFactor.setter
    def StepFactor(self, arg: float, /) -> None: ...

class MultipleConfig:
    """Configuration for multi-dimensional Gauss integration."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MultipleConfig) -> None: ...

    @property
    def MaxOrder(self) -> int:
        """Maximum integration order per dimension"""

    @MaxOrder.setter
    def MaxOrder(self, arg: int, /) -> None: ...

class SetResult:
    """Result for vector function integration."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: SetResult) -> None: ...

    def IsDone(self) -> bool: ...

    @property
    def Status(self) -> nanoocp.MathUtils.Status: ...

    @Status.setter
    def Status(self, arg: nanoocp.MathUtils.Status, /) -> None: ...

    @property
    def Values(self) -> nanoocp.math.math_Vector | None:
        """Integral of each component"""

    @Values.setter
    def Values(self, arg: nanoocp.math.math_Vector | None, /) -> None: ...

    @property
    def NbEquations(self) -> int: ...

    @NbEquations.setter
    def NbEquations(self, arg: int, /) -> None: ...
