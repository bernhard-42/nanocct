"""OCCT package ExtremaPC (toolkit TKGeomBase)"""

import enum
from typing import overload

import nanoocp.MathUtils
from nanoocp.MathUtils import Domain1D as Domain1D
import nanoocp.gp


THE_DEFAULT_TOLERANCE: float = 1e-07

THE_PARAM_TOLERANCE: float = 1e-09

THE_NEIGHBOR_STEP_RATIO: float = 0.01

THE_INTERVAL_EXPAND_RATIO: float = 0.05

THE_REFINEMENT_STEP_RATIO: float = 0.001

THE_NEWTON_XTOL_FACTOR: float = 0.01

THE_NEWTON_FTOL_FACTOR: float = 0.001

THE_HINT_SEARCH_RADIUS: float = 0.1

THE_RANGE_NARROWING_FACTOR: float = 0.25

THE_MAX_SKIP_THRESHOLD: float = 0.9

THE_NEAR_ZERO_F_FACTOR: float = 10.0

THE_FALLBACK_F_FACTOR: float = 100.0

THE_MAX_NEWTON_ITERATIONS: int = 20

THE_REFINEMENT_NB_SAMPLES: int = 20

THE_REFINEMENT_NB_PASSES: int = 3

THE_BEZIER_MIN_SAMPLES: int = 24

THE_BEZIER_DEGREE_MULTIPLIER: int = 3

THE_OTHER_CURVE_NB_SAMPLES: int = 64

THE_BSPLINE_FALLBACK_SAMPLES: int = 32

THE_BSPLINE_SPAN_MULTIPLIER: int = 2

class Status(enum.Enum):
    """Status of extrema computation."""

    OK = 0

    NotDone = 1

    InfiniteSolutions = 2

    NoSolution = 3

    NumericalError = 4

class SearchMode(enum.Enum):
    """
    Search mode for extrema computation.
    Controls which extrema to find, enabling performance optimizations.
    """

    MinMax = 0

    Min = 1

    Max = 2

class ExtremumResult:
    """Result of a single extremum computation."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ExtremumResult) -> None: ...

    @property
    def Parameter(self) -> float:
        """Parameter value on curve"""

    @Parameter.setter
    def Parameter(self, arg: float, /) -> None: ...

    @property
    def Point(self) -> nanoocp.gp.gp_Pnt:
        """Point on curve at parameter"""

    @Point.setter
    def Point(self, arg: nanoocp.gp.gp_Pnt, /) -> None: ...

    @property
    def SquareDistance(self) -> float:
        """Square of the distance from query point to curve point"""

    @SquareDistance.setter
    def SquareDistance(self, arg: float, /) -> None: ...

    @property
    def IsMinimum(self) -> bool:
        """True if this is a local minimum, false if maximum"""

    @IsMinimum.setter
    def IsMinimum(self, arg: bool, /) -> None: ...

class Result:
    """
    Result of extrema computation containing all found extrema.
    Non-copyable to enforce use of const reference from Perform().
    """

    def __init__(self) -> None:
        """Default constructor."""

    def IsDone(self) -> bool:
        """Returns true if computation succeeded with finite number of extrema."""

    def IsInfinite(self) -> bool:
        """Returns true if there are infinite solutions."""

    def NbExt(self) -> int:
        """Returns number of extrema found (0 if infinite or failed)."""

    def __getitem__(self, theIndex: int) -> ExtremumResult:
        """Access extremum by 0-based index."""

    def MinSquareDistance(self) -> float:
        """
        Returns the squared distance of the closest extremum.
        Returns infinity if no extrema found.
        """

    def MinIndex(self) -> int:
        """
        Returns the index of the closest extremum (0-based).
        Returns -1 if no extrema found.
        """

    def MaxSquareDistance(self) -> float:
        """
        Returns the squared distance of the farthest extremum.
        Returns 0 if no extrema found.
        """

    def MaxIndex(self) -> int:
        """
        Returns the index of the farthest extremum (0-based).
        Returns -1 if no extrema found.
        """

    def Clear(self) -> None:
        """
        Clear the result for reuse.
        Preserves allocated memory in Extrema vector.
        """

    @property
    def Status(self) -> Status:
        """Computation status"""

    @Status.setter
    def Status(self, arg: Status, /) -> None: ...

    @property
    def Extrema(self) -> "NCollection_DynamicArray<ExtremaPC::ExtremumResult>":
        """Collection of found extrema"""

    @Extrema.setter
    def Extrema(self, arg: "NCollection_DynamicArray<ExtremaPC::ExtremumResult>", /) -> None: ...

    @property
    def InfiniteSquareDistance(self) -> float:
        """
        For infinite solutions, stores the constant squared distance.
        Only meaningful when Status == Status::InfiniteSolutions.
        """

    @InfiniteSquareDistance.setter
    def InfiniteSquareDistance(self, arg: float, /) -> None: ...

class Config:
    """Configuration for extrema computation."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Config) -> None: ...

    @property
    def Tolerance(self) -> float:
        """Tolerance for root finding"""

    @Tolerance.setter
    def Tolerance(self, arg: float, /) -> None: ...

    @property
    def Domain(self) -> nanoocp.MathUtils.Domain1D | None:
        """Parameter domain (nullopt = use natural/unbounded)"""

    @Domain.setter
    def Domain(self, arg: nanoocp.MathUtils.Domain1D | None, /) -> None: ...

    @property
    def NbSamples(self) -> int:
        """Number of samples for numerical methods"""

    @NbSamples.setter
    def NbSamples(self, arg: int, /) -> None: ...

    @property
    def Mode(self) -> SearchMode:
        """Search mode (MinMax, Min, or Max)"""

    @Mode.setter
    def Mode(self, arg: SearchMode, /) -> None: ...

    @property
    def IncludeEndpoints(self) -> bool:
        """Include endpoints as potential extrema"""

    @IncludeEndpoints.setter
    def IncludeEndpoints(self, arg: bool, /) -> None: ...
