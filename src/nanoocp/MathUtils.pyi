"""OCCT package MathUtils (toolkit TKMath)"""

from collections.abc import Sequence
import enum
from typing import overload

import nanoocp.math


THE_NEWTON_FTOL_SQ: float = 1e-32

THE_NEWTON_STEP_TOL_FACTOR: float = 1e-16

THE_NEWTON_MAX_ITER: int = 100

THE_NEWTON2D_SINGULAR_DET: float = 1e-25

THE_NEWTON2D_CRITICAL_GRAD_SQ: float = 1e-60

THE_NEWTON2D_MAX_STEP_RATIO: float = 0.5

THE_NEWTON2D_DOMAIN_EXT: float = 0.0001

THE_NEWTON2D_STAGNATION_RATIO: float = 0.999

THE_NEWTON2D_STAGNATION_COUNT: int = 3

THE_NEWTON2D_LINE_SEARCH_MAX: int = 8

THE_NEWTON2D_SKIP_LINESEARCH_SQ: float = 0.01

THE_NEWTON2D_STAGNATION_RELAX: float = 10.0

THE_NEWTON2D_BACKTRACK_TRIGGER: float = 1.5

THE_NEWTON2D_BACKTRACK_ACCEPT: float = 1.2

THE_NEWTON2D_MAXITER_RELAX: float = 10.0

THE_HESSIAN_DEGENERACY_REL: float = 1e-08

THE_HESSIAN_DEGENERACY_ABS: float = 1e-20

THE_ARMIJO_C1: float = 0.0001

THE_EPSILON: float = 2.220446049250313e-16

THE_ZERO_TOL: float = 1e-15

THE_PI: float = 3.141592653589793

THE_2PI: float = 6.283185307179586

THE_GOLDEN_RATIO: float = 1.618033988749895

THE_GOLDEN_SECTION: float = 0.381966011250105

class Status(enum.Enum):
    """
    Computation status for all math solvers.
    Provides detailed information about solver outcome.
    """

    OK = 0

    NotConverged = 1

    MaxIterations = 2

    NumericalError = 3

    InvalidInput = 4

    InfiniteSolutions = 5

    NoSolution = 6

    NotPositiveDefinite = 7

    Singular = 8

    NonDescentDirection = 9

class ScalarResult:
    """
    Result for scalar (1D) root finding and minimization.
    Contains the found root/minimum location and diagnostic information.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ScalarResult) -> None: ...

    def IsDone(self) -> bool:
        """Returns true if computation succeeded."""

    def __bool__(self) -> bool:
        """
        Conversion to bool for convenient checking.
        Example: if (aResult) { use *aResult.Root; }
        """

    @property
    def Status(self) -> Status:
        """Computation status"""

    @Status.setter
    def Status(self, arg: Status, /) -> None: ...

    @property
    def NbIterations(self) -> int:
        """Number of iterations performed"""

    @NbIterations.setter
    def NbIterations(self, arg: int, /) -> None: ...

    @property
    def Root(self) -> float | None:
        """Found root or minimum location"""

    @Root.setter
    def Root(self, arg: float | None, /) -> None: ...

    @property
    def Value(self) -> float | None:
        """Function value at root/minimum"""

    @Value.setter
    def Value(self, arg: float | None, /) -> None: ...

    @property
    def Derivative(self) -> float | None:
        """Derivative at root (if computed)"""

    @Derivative.setter
    def Derivative(self, arg: float | None, /) -> None: ...

class PolyResult:
    """
    Result for polynomial root finding.
    Supports up to 4 real roots (for quartic equations).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: PolyResult) -> None: ...

    def IsDone(self) -> bool:
        """Returns true if computation succeeded."""

    def __getitem__(self, theIndex: int) -> float:
        """
        Access root by index (0-based).
        @param theIndex root index (0 to NbRoots-1)
        @return root value
        """

    def __bool__(self) -> bool:
        """Conversion to bool for convenient checking."""

    @property
    def Status(self) -> Status:
        """Computation status"""

    @Status.setter
    def Status(self, arg: Status, /) -> None: ...

    @property
    def NbRoots(self) -> int:
        """Number of real roots found"""

    @NbRoots.setter
    def NbRoots(self, arg: int, /) -> None: ...

    @property
    def Roots(self) -> list[float]:
        """Array of real roots (sorted)"""

    @Roots.setter
    def Roots(self, arg: Sequence[float], /) -> None: ...

class VectorResult:
    """
    Result for N-dimensional optimization and system solving.
    Contains the solution vector and optional gradient/Jacobian information.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: VectorResult) -> None: ...

    def IsDone(self) -> bool:
        """Returns true if computation succeeded."""

    def __bool__(self) -> bool:
        """Conversion to bool for convenient checking."""

    @property
    def Status(self) -> Status:
        """Computation status"""

    @Status.setter
    def Status(self, arg: Status, /) -> None: ...

    @property
    def NbIterations(self) -> int:
        """Number of iterations performed"""

    @NbIterations.setter
    def NbIterations(self, arg: int, /) -> None: ...

    @property
    def Solution(self) -> nanoocp.math.math_Vector | None:
        """Solution vector (set by solver on success)"""

    @Solution.setter
    def Solution(self, arg: nanoocp.math.math_Vector | None, /) -> None: ...

    @property
    def Value(self) -> float | None:
        """Function value at solution (if computed)"""

    @Value.setter
    def Value(self, arg: float | None, /) -> None: ...

    @property
    def Gradient(self) -> nanoocp.math.math_Vector | None:
        """Gradient at solution (if computed)"""

    @Gradient.setter
    def Gradient(self, arg: nanoocp.math.math_Vector | None, /) -> None: ...

    @property
    def Jacobian(self) -> nanoocp.math.math_Matrix | None:
        """Jacobian at solution (if computed)"""

    @Jacobian.setter
    def Jacobian(self, arg: nanoocp.math.math_Matrix | None, /) -> None: ...

class LinearResult:
    """
    Result for linear system solving (Ax = b).
    Contains the solution vector and matrix determinant if computed.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LinearResult) -> None: ...

    def IsDone(self) -> bool:
        """Returns true if computation succeeded."""

    def __bool__(self) -> bool:
        """Conversion to bool for convenient checking."""

    @property
    def Status(self) -> Status:
        """Computation status"""

    @Status.setter
    def Status(self, arg: Status, /) -> None: ...

    @property
    def Solution(self) -> nanoocp.math.math_Vector | None:
        """Solution vector X in AX = B (set by solver)"""

    @Solution.setter
    def Solution(self, arg: nanoocp.math.math_Vector | None, /) -> None: ...

    @property
    def Determinant(self) -> float | None:
        """Determinant of matrix (if computed)"""

    @Determinant.setter
    def Determinant(self, arg: float | None, /) -> None: ...

class LinearMultipleResult:
    """
    Result for multiple linear systems solving (AX = B with matrix RHS).
    Contains the full solution matrix and determinant if computed.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LinearMultipleResult) -> None: ...

    def IsDone(self) -> bool:
        """Returns true if computation succeeded."""

    def __bool__(self) -> bool:
        """Conversion to bool for convenient checking."""

    @property
    def Status(self) -> Status:
        """Computation status"""

    @Status.setter
    def Status(self, arg: Status, /) -> None: ...

    @property
    def Solutions(self) -> nanoocp.math.math_Matrix | None:
        """Solution matrix X in AX = B (set by solver)"""

    @Solutions.setter
    def Solutions(self, arg: nanoocp.math.math_Matrix | None, /) -> None: ...

    @property
    def Determinant(self) -> float | None:
        """Determinant of matrix (if computed)"""

    @Determinant.setter
    def Determinant(self, arg: float | None, /) -> None: ...

class EigenResult:
    """
    Result for eigenvalue/eigenvector computation.
    Contains eigenvalues and optionally eigenvectors.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: EigenResult) -> None: ...

    def IsDone(self) -> bool:
        """Returns true if computation succeeded."""

    def __bool__(self) -> bool:
        """Conversion to bool for convenient checking."""

    @property
    def Status(self) -> Status:
        """Computation status"""

    @Status.setter
    def Status(self, arg: Status, /) -> None: ...

    @property
    def NbIterations(self) -> int:
        """Number of iterations performed"""

    @NbIterations.setter
    def NbIterations(self, arg: int, /) -> None: ...

    @property
    def EigenValues(self) -> nanoocp.math.math_Vector | None:
        """Computed eigenvalues (set by solver)"""

    @EigenValues.setter
    def EigenValues(self, arg: nanoocp.math.math_Vector | None, /) -> None: ...

    @property
    def EigenVectors(self) -> nanoocp.math.math_Matrix | None:
        """Computed eigenvectors (set by solver)"""

    @EigenVectors.setter
    def EigenVectors(self, arg: nanoocp.math.math_Matrix | None, /) -> None: ...

class DecompResult:
    """
    Result for matrix decomposition (LU, SVD, QR).
    Structure depends on decomposition type.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DecompResult) -> None: ...

    def IsDone(self) -> bool:
        """Returns true if decomposition succeeded."""

    def __bool__(self) -> bool:
        """Conversion to bool for convenient checking."""

    @property
    def Status(self) -> Status:
        """Computation status"""

    @Status.setter
    def Status(self, arg: Status, /) -> None: ...

    @property
    def L(self) -> nanoocp.math.math_Matrix | None:
        """Lower triangular (LU) or left singular vectors (SVD)"""

    @L.setter
    def L(self, arg: nanoocp.math.math_Matrix | None, /) -> None: ...

    @property
    def U(self) -> nanoocp.math.math_Matrix | None:
        """Upper triangular (LU) or right singular vectors (SVD)"""

    @U.setter
    def U(self, arg: nanoocp.math.math_Matrix | None, /) -> None: ...

    @property
    def D(self) -> nanoocp.math.math_Vector | None:
        """Diagonal elements or singular values"""

    @D.setter
    def D(self, arg: nanoocp.math.math_Vector | None, /) -> None: ...

    @property
    def Determinant(self) -> float | None:
        """Matrix determinant (if computed)"""

    @Determinant.setter
    def Determinant(self, arg: float | None, /) -> None: ...

class IntegResult:
    """
    Result for numerical integration.
    Contains integral value and error estimates.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntegResult) -> None: ...

    def IsDone(self) -> bool:
        """Returns true if integration succeeded."""

    def __bool__(self) -> bool:
        """Conversion to bool for convenient checking."""

    @property
    def Status(self) -> Status:
        """Computation status"""

    @Status.setter
    def Status(self, arg: Status, /) -> None: ...

    @property
    def NbIterations(self) -> int:
        """Number of adaptive iterations"""

    @NbIterations.setter
    def NbIterations(self, arg: int, /) -> None: ...

    @property
    def NbPoints(self) -> int:
        """Total number of quadrature points used"""

    @NbPoints.setter
    def NbPoints(self, arg: int, /) -> None: ...

    @property
    def Value(self) -> float | None:
        """Computed integral value"""

    @Value.setter
    def Value(self, arg: float | None, /) -> None: ...

    @property
    def AbsoluteError(self) -> float | None:
        """Estimated absolute error (if computed)"""

    @AbsoluteError.setter
    def AbsoluteError(self, arg: float | None, /) -> None: ...

    @property
    def RelativeError(self) -> float | None:
        """Estimated relative error (if computed)"""

    @RelativeError.setter
    def RelativeError(self, arg: float | None, /) -> None: ...

class InverseResult:
    """
    Result for matrix inverse computation.
    Contains the inverse matrix if computation succeeded.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: InverseResult) -> None: ...

    def IsDone(self) -> bool:
        """Returns true if inversion succeeded."""

    def __bool__(self) -> bool:
        """Conversion to bool for convenient checking."""

    @property
    def Status(self) -> Status:
        """Computation status"""

    @Status.setter
    def Status(self, arg: Status, /) -> None: ...

    @property
    def Inverse(self) -> nanoocp.math.math_Matrix | None:
        """Computed inverse matrix"""

    @Inverse.setter
    def Inverse(self, arg: nanoocp.math.math_Matrix | None, /) -> None: ...

    @property
    def Determinant(self) -> float | None:
        """Determinant of matrix (if computed)"""

    @Determinant.setter
    def Determinant(self, arg: float | None, /) -> None: ...

class Config:
    """
    Configuration for iterative solvers.
    Provides common settings for convergence criteria and iteration limits.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor with standard tolerances."""

    @overload
    def __init__(self, theTolerance: float, theMaxIter: int = 100) -> None:
        """
        Constructor with custom tolerance (sets all tolerances to same value).
        @param theTolerance convergence tolerance
        @param theMaxIter maximum iterations
        """

    @overload
    def __init__(self, theOther: Config) -> None: ...

    @property
    def MaxIterations(self) -> int:
        """Maximum number of iterations allowed"""

    @MaxIterations.setter
    def MaxIterations(self, arg: int, /) -> None: ...

    @property
    def Tolerance(self) -> float:
        """General convergence tolerance"""

    @Tolerance.setter
    def Tolerance(self, arg: float, /) -> None: ...

    @property
    def XTolerance(self) -> float:
        """Tolerance for solution change |x_{n+1} - x_n|"""

    @XTolerance.setter
    def XTolerance(self, arg: float, /) -> None: ...

    @property
    def FTolerance(self) -> float:
        """Tolerance for function value |f(x)|"""

    @FTolerance.setter
    def FTolerance(self, arg: float, /) -> None: ...

    @property
    def StepMin(self) -> float:
        """Minimum step size before declaring convergence or failure."""

    @StepMin.setter
    def StepMin(self, arg: float, /) -> None: ...

class BoundedConfig(Config):
    """
    Configuration for bounded 1D optimization and root finding.
    Extends Config with interval bounds.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theLower: float, theUpper: float, theTolerance: float = 1e-10, theMaxIter: int = 100) -> None:
        """
        Constructor with bounds.
        @param theLower lower bound
        @param theUpper upper bound
        @param theTolerance convergence tolerance
        @param theMaxIter maximum iterations
        """

    @overload
    def __init__(self, theOther: BoundedConfig) -> None: ...

    @property
    def LowerBound(self) -> float:
        """Lower bound of search interval"""

    @LowerBound.setter
    def LowerBound(self, arg: float, /) -> None: ...

    @property
    def UpperBound(self) -> float:
        """Upper bound of search interval"""

    @UpperBound.setter
    def UpperBound(self, arg: float, /) -> None: ...

class NDimConfig(Config):
    """
    Configuration for N-dimensional optimization with optional bounds.
    Bounds are passed separately as math_Vector for flexibility.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theTolerance: float, theMaxIter: int = 100, theUseBounds: bool = False) -> None:
        """
        Constructor with tolerance.
        @param theTolerance convergence tolerance
        @param theMaxIter maximum iterations
        @param theUseBounds whether to use bounds
        """

    @overload
    def __init__(self, theOther: NDimConfig) -> None: ...

    @property
    def UseBounds(self) -> bool:
        """Whether to enforce bounds during optimization"""

    @UseBounds.setter
    def UseBounds(self, arg: bool, /) -> None: ...

class IntegConfig:
    """
    Configuration for numerical integration.
    Provides settings for quadrature order and adaptive refinement.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theTolerance: float, theMaxIter: int = 100) -> None:
        """
        Constructor with custom tolerance.
        @param theTolerance relative tolerance
        @param theMaxIter maximum adaptive iterations
        """

    @overload
    def __init__(self, theOther: IntegConfig) -> None: ...

    @property
    def InitialOrder(self) -> int:
        """Initial number of quadrature points"""

    @InitialOrder.setter
    def InitialOrder(self, arg: int, /) -> None: ...

    @property
    def MaxOrder(self) -> int:
        """Maximum quadrature order (Gauss-Legendre limit)"""

    @MaxOrder.setter
    def MaxOrder(self, arg: int, /) -> None: ...

    @property
    def MaxIterations(self) -> int:
        """Maximum adaptive subdivision iterations"""

    @MaxIterations.setter
    def MaxIterations(self, arg: int, /) -> None: ...

    @property
    def Tolerance(self) -> float:
        """Relative tolerance for error estimation"""

    @Tolerance.setter
    def Tolerance(self, arg: float, /) -> None: ...

class LinConfig:
    """
    Configuration for linear algebra solvers.
    Provides settings for singularity detection and pivoting.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theOther: LinConfig) -> None: ...

    @property
    def SingularityTolerance(self) -> float:
        """Tolerance for detecting singular matrices"""

    @SingularityTolerance.setter
    def SingularityTolerance(self, arg: float, /) -> None: ...

    @property
    def UsePivoting(self) -> bool:
        """Whether to use pivoting for stability"""

    @UsePivoting.setter
    def UsePivoting(self, arg: bool, /) -> None: ...

class Domain1D:
    """
    @brief 1D parameter domain for curves.

    Represents a parameter range [Min, Max] with utility methods for:
    - Bounds checking (Contains)
    - Parameter clamping (Clamp)
    - Domain analysis (IsLarge, IsFullPeriod)

    @note This is a lightweight value type designed for efficiency.
    All methods are inline and constexpr where possible.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor - creates empty domain [0, 0]."""

    @overload
    def __init__(self, theMin: float, theMax: float) -> None:
        """
        Construct from bounds.
        @param theMin lower bound
        @param theMax upper bound
        """

    @overload
    def __init__(self, theOther: Domain1D) -> None: ...

    def Length(self) -> float:
        """Returns the length of the domain."""

    def Mid(self) -> float:
        """Returns the midpoint of the domain."""

    def Contains(self, theU: float, theTol: float = 0.0) -> bool:
        """
        Check if value is within domain.
        @param theU parameter value to check
        @param theTol tolerance for boundary check
        @return true if theU is in [Min - theTol, Max + theTol]
        """

    def Clamp(self, theU: float) -> float:
        """
        Clamp value to domain bounds.
        @param theU parameter value to clamp
        @return clamped value in [Min, Max]
        """

    def IsLarge(self, theThreshold: float = 1000.0) -> bool:
        """
        Check if domain is "large" (effectively unbounded for optimization).
        Large domains allow skipping bounds checking for performance.
        @param theThreshold size threshold (default 1000)
        @return true if Length() > theThreshold
        """

    def IsFullPeriod(self, thePeriod: float, theTol: float = 1e-10) -> bool:
        """
        Check if domain covers a full periodic range.
        @param thePeriod period of the parameter (e.g., 2*PI for angles)
        @param theTol tolerance
        @return true if domain covers at least one full period
        """

    def Lerp(self, theT: float) -> float:
        """
        Interpolate within domain.
        @param theT interpolation parameter in [0, 1]
        @return Min + theT * Length()
        """

    def Normalize(self, theU: float) -> float:
        """
        Normalize parameter to [0, 1] range.
        @param theU parameter value
        @return (theU - Min) / Length(), or 0.5 if Length() == 0
        """

    def IsFinite(self, theInfLimit: float = 1e+100) -> bool:
        """
        Check if domain has finite bounds (not effectively infinite).
        @param theInfLimit threshold for "infinity" (default 1e100)
        @return true if both Min and Max are within finite range
        """

    def IsEqual(self, theOther: Domain1D, theTol: float = 1e-10) -> bool:
        """
        Check if this domain equals another within tolerance.
        @param theOther domain to compare with
        @param theTol tolerance for comparison
        @return true if domains are equal within tolerance
        """

    @property
    def Min(self) -> float:
        """Lower bound of the domain"""

    @Min.setter
    def Min(self, arg: float, /) -> None: ...

    @property
    def Max(self) -> float:
        """Upper bound of the domain"""

    @Max.setter
    def Max(self, arg: float, /) -> None: ...

class Domain2D:
    """
    @brief 2D parameter domain for surfaces.

    Represents a rectangular parameter domain [UMin, UMax] x [VMin, VMax]
    with utility methods for:
    - Bounds checking (Contains)
    - Parameter clamping (Clamp)
    - Domain analysis (IsLarge, IsFullPeriod)
    - Access to U and V subdomains

    @note This is a lightweight value type designed for efficiency.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor - creates empty domain."""

    @overload
    def __init__(self, theUDomain: Domain1D, theVDomain: Domain1D) -> None:
        """
        Construct from two 1D domains.
        @param theUDomain U parameter domain
        @param theVDomain V parameter domain
        """

    @overload
    def __init__(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float) -> None:
        """
        Construct from bounds.
        @param theUMin lower U bound
        @param theUMax upper U bound
        @param theVMin lower V bound
        @param theVMax upper V bound
        """

    @overload
    def __init__(self, theOther: Domain2D) -> None: ...

    def U(self) -> Domain1D:
        """Returns the U subdomain."""

    def V(self) -> Domain1D:
        """Returns the V subdomain."""

    def ULength(self) -> float:
        """Returns U length."""

    def VLength(self) -> float:
        """Returns V length."""

    def UMid(self) -> float:
        """Returns U midpoint."""

    def VMid(self) -> float:
        """Returns V midpoint."""

    def Contains(self, theU: float, theV: float, theTol: float = 0.0) -> bool:
        """
        Check if UV point is within domain.
        @param theU U parameter
        @param theV V parameter
        @param theTol tolerance for boundary check
        @return true if (theU, theV) is in domain
        """

    def Clamp(self) -> tuple[float, float]:
        """
        Clamp UV to domain bounds.
        @param theU U parameter (modified in place)
        @param theV V parameter (modified in place)
        """

    def IsLarge(self, theThreshold: float = 1000.0) -> bool:
        """
        Check if both U and V domains are "large".
        @param theThreshold size threshold (default 1000)
        @return true if both U and V lengths exceed threshold
        """

    def IsUFullPeriod(self, thePeriod: float, theTol: float = 1e-10) -> bool:
        """
        Check if U domain covers a full period.
        @param thePeriod period of U parameter
        @param theTol tolerance
        """

    def IsVFullPeriod(self, thePeriod: float, theTol: float = 1e-10) -> bool:
        """
        Check if V domain covers a full period.
        @param thePeriod period of V parameter
        @param theTol tolerance
        """

    def IsFinite(self, theInfLimit: float = 1e+100) -> bool:
        """
        Check if domain has finite bounds (not effectively infinite).
        @param theInfLimit threshold for "infinity" (default 1e100)
        """

    @property
    def UMin(self) -> float:
        """Lower U bound"""

    @UMin.setter
    def UMin(self, arg: float, /) -> None: ...

    @property
    def UMax(self) -> float:
        """Upper U bound"""

    @UMax.setter
    def UMax(self, arg: float, /) -> None: ...

    @property
    def VMin(self) -> float:
        """Lower V bound"""

    @VMin.setter
    def VMin(self, arg: float, /) -> None: ...

    @property
    def VMax(self) -> float:
        """Upper V bound"""

    @VMax.setter
    def VMax(self, arg: float, /) -> None: ...

class RandomGenerator:
    """
    High-quality pseudo-random number generator based on xoshiro256**.

    xoshiro256** is a general-purpose PRNG designed by David Blackman
    and Sebastiano Vigna. It has:
    - 256-bit state (period 2^256 - 1)
    - Passes all BigCrush statistical tests
    - Very fast on 64-bit hardware
    - Equidistributed to 4 dimensions

    Suitable for Monte Carlo methods, stochastic optimization,
    and any application requiring high-quality randomness.
    """

    @overload
    def __init__(self, theSeed: int = 1) -> None:
        """
        Initialize with a seed value.
        Uses SplitMix64 to expand a single seed into the full 256-bit state,
        ensuring good initialization even from poor seeds.
        @param theSeed seed value (default 1)
        """

    @overload
    def __init__(self, theOther: RandomGenerator) -> None: ...

    def SetSeed(self, theSeed: int) -> None:
        """
        Re-seed the generator.
        @param theSeed seed value
        """

    def NextInt(self) -> int:
        """
        Generate next 64-bit unsigned integer.
        @return pseudo-random value in [0, 2^64)
        """

    def NextReal(self) -> float:
        """
        Generate next double in [0, 1).
        Uses 53 bits of randomness for full double precision.
        @return pseudo-random value in [0, 1)
        """

class BracketResult:
    """Result of root bracketing operation."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BracketResult) -> None: ...

    @property
    def IsValid(self) -> bool:
        """True if valid bracket found"""

    @IsValid.setter
    def IsValid(self, arg: bool, /) -> None: ...

    @property
    def A(self) -> float:
        """Lower bound"""

    @A.setter
    def A(self, arg: float, /) -> None: ...

    @property
    def B(self) -> float:
        """Upper bound"""

    @B.setter
    def B(self, arg: float, /) -> None: ...

    @property
    def Fa(self) -> float:
        """Function value at A"""

    @Fa.setter
    def Fa(self, arg: float, /) -> None: ...

    @property
    def Fb(self) -> float:
        """Function value at B"""

    @Fb.setter
    def Fb(self, arg: float, /) -> None: ...

class MinBracketResult:
    """Result of minimum bracketing operation."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MinBracketResult) -> None: ...

    @property
    def IsValid(self) -> bool:
        """True if valid bracket found (Fb < Fa and Fb < Fc)"""

    @IsValid.setter
    def IsValid(self, arg: bool, /) -> None: ...

    @property
    def A(self) -> float:
        """Left bound"""

    @A.setter
    def A(self, arg: float, /) -> None: ...

    @property
    def B(self) -> float:
        """Middle point (minimum location estimate)"""

    @B.setter
    def B(self, arg: float, /) -> None: ...

    @property
    def C(self) -> float:
        """Right bound"""

    @C.setter
    def C(self, arg: float, /) -> None: ...

    @property
    def Fa(self) -> float:
        """Function value at A"""

    @Fa.setter
    def Fa(self, arg: float, /) -> None: ...

    @property
    def Fb(self) -> float:
        """Function value at B"""

    @Fb.setter
    def Fb(self, arg: float, /) -> None: ...

    @property
    def Fc(self) -> float:
        """Function value at C"""

    @Fc.setter
    def Fc(self, arg: float, /) -> None: ...

class MinBracketOptions:
    """Options for minimum bracketing."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MinBracketOptions) -> None: ...

    @property
    def MaxIterations(self) -> int:
        """Maximum iterations"""

    @MaxIterations.setter
    def MaxIterations(self, arg: int, /) -> None: ...

    @property
    def UseLimits(self) -> bool:
        """Enable hard limits for parameter"""

    @UseLimits.setter
    def UseLimits(self, arg: bool, /) -> None: ...

    @property
    def LeftLimit(self) -> float:
        """Left hard limit (inclusive)"""

    @LeftLimit.setter
    def LeftLimit(self, arg: float, /) -> None: ...

    @property
    def RightLimit(self) -> float:
        """Right hard limit (inclusive)"""

    @RightLimit.setter
    def RightLimit(self, arg: float, /) -> None: ...

    @property
    def HasFA(self) -> bool:
        """True if FA is precomputed"""

    @HasFA.setter
    def HasFA(self, arg: bool, /) -> None: ...

    @property
    def HasFB(self) -> bool:
        """True if FB is precomputed"""

    @HasFB.setter
    def HasFB(self, arg: bool, /) -> None: ...

    @property
    def FA(self) -> float:
        """Precomputed f(A)"""

    @FA.setter
    def FA(self, arg: float, /) -> None: ...

    @property
    def FB(self) -> float:
        """Precomputed f(B)"""

    @FB.setter
    def FB(self, arg: float, /) -> None: ...

class LineSearchResult:
    """Result of line search operation."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LineSearchResult) -> None: ...

    @property
    def IsValid(self) -> bool:
        """True if line search succeeded"""

    @IsValid.setter
    def IsValid(self, arg: bool, /) -> None: ...

    @property
    def Alpha(self) -> float:
        """Step size found"""

    @Alpha.setter
    def Alpha(self, arg: float, /) -> None: ...

    @property
    def FNew(self) -> float:
        """Function value at new point"""

    @FNew.setter
    def FNew(self, arg: float, /) -> None: ...

    @property
    def NbEvals(self) -> int:
        """Number of function evaluations"""

    @NbEvals.setter
    def NbEvals(self, arg: int, /) -> None: ...

class Polynomial:
    """
    Polynomial functor: f(x) = sum(a[i] * x^i).
    Coefficients are stored in order: a[0] + a[1]*x + a[2]*x^2 + ...

    Usage:
    @code
    // x^2 - 2 (find sqrt(2))
    Polynomial aPoly({-2.0, 0.0, 1.0});

    // x^3 - 6x^2 + 11x - 6 = (x-1)(x-2)(x-3)
    Polynomial aCubic({-6.0, 11.0, -6.0, 1.0});
    @endcode
    """

    @overload
    def __init__(self, theCoeffs: nanoocp.math.math_Vector) -> None:
        """
        Constructor from math_Vector.
        @param theCoeffs coefficients in ascending power order
        """

    @overload
    def __init__(self, theOther: Polynomial) -> None: ...

    def Value(self, theX: float) -> tuple[bool, float]:
        """
        Evaluates polynomial at theX using Horner's method.
        @param[in] theX input value
        @param[out] theY polynomial value p(theX)
        @return true (always succeeds for polynomials)
        """

    def Values(self, theX: float) -> tuple[bool, float, float]:
        """
        Evaluates polynomial and its derivative at theX.
        @param[in] theX input value
        @param[out] theY polynomial value p(theX)
        @param[out] theDY derivative value p'(theX)
        @return true (always succeeds for polynomials)
        """

    def Degree(self) -> int:
        """
        Returns the degree of the polynomial.
        @return polynomial degree (number of coefficients - 1)
        """

    def Coefficient(self, theIndex: int) -> float:
        """
        Returns coefficient by index.
        @param theIndex coefficient index (0 = constant term)
        @return coefficient value
        """

class Rational:
    """
    Rational function functor: f(x) = P(x) / Q(x).
    Both numerator P and denominator Q are polynomials.

    Usage:
    @code
    // (x + 1) / (x^2 + 1)
    Rational aRat({1.0, 1.0}, {1.0, 0.0, 1.0});
    @endcode
    """

    @overload
    def __init__(self, theNum: nanoocp.math.math_Vector, theDenom: nanoocp.math.math_Vector) -> None:
        """
        Constructor from math_Vector.
        @param theNum numerator coefficients (ascending power order)
        @param theDenom denominator coefficients (ascending power order)
        """

    @overload
    def __init__(self, theOther: Rational) -> None: ...

    def Value(self, theX: float) -> tuple[bool, float]:
        """
        Evaluates rational function at theX.
        @param[in] theX input value
        @param[out] theY function value P(theX)/Q(theX)
        @return false if denominator is zero
        """

class Constant:
    """Constant function functor: f(x) = c."""

    @overload
    def __init__(self, theValue: float) -> None:
        """
        Constructor from constant value.
        @param theValue constant value
        """

    @overload
    def __init__(self, theOther: Constant) -> None: ...

    def Value(self, arg0: float) -> tuple[bool, float]:
        """
        Evaluates constant function.
        @param[in] theX input value (ignored)
        @param[out] theY constant value
        @return true (always succeeds)
        """

    def Values(self, arg0: float) -> tuple[bool, float, float]:
        """
        Evaluates constant and derivative (derivative is always 0).
        @param[in] theX input value (ignored)
        @param[out] theY constant value
        @param[out] theDY derivative (always 0)
        @return true (always succeeds)
        """

class Linear:
    """Linear function functor: f(x) = a*x + b."""

    @overload
    def __init__(self, theSlope: float, theIntercept: float) -> None:
        """
        Constructor from slope and intercept.
        @param theSlope coefficient a (slope)
        @param theIntercept coefficient b (y-intercept)
        """

    @overload
    def __init__(self, theOther: Linear) -> None: ...

    def Value(self, theX: float) -> tuple[bool, float]:
        """
        Evaluates linear function a*x + b.
        @param[in] theX input value
        @param[out] theY function value
        @return true (always succeeds)
        """

    def Values(self, theX: float) -> tuple[bool, float, float]:
        """
        Evaluates linear function and derivative.
        @param[in] theX input value
        @param[out] theY function value
        @param[out] theDY derivative (= slope)
        @return true (always succeeds)
        """

class Sine:
    """Sine function functor: f(x) = a * sin(b*x + c) + d."""

    @overload
    def __init__(self, theAmplitude: float = 1.0, theFrequency: float = 1.0, thePhase: float = 0.0, theOffset: float = 0.0) -> None:
        """
        Constructor with full parameters.
        @param theAmplitude amplitude a
        @param theFrequency angular frequency b
        @param thePhase phase shift c
        @param theOffset vertical offset d
        """

    @overload
    def __init__(self, theOther: Sine) -> None: ...

    def Value(self, theX: float) -> tuple[bool, float]:
        """
        Evaluates sine function.
        @param[in] theX input value
        @param[out] theY function value
        @return true (always succeeds)
        """

    def Values(self, theX: float) -> tuple[bool, float, float]:
        """
        Evaluates sine function and derivative.
        @param[in] theX input value
        @param[out] theY function value
        @param[out] theDY derivative value
        @return true (always succeeds)
        """

class Cosine:
    """Cosine function functor: f(x) = a * cos(b*x + c) + d."""

    @overload
    def __init__(self, theAmplitude: float = 1.0, theFrequency: float = 1.0, thePhase: float = 0.0, theOffset: float = 0.0) -> None:
        """
        Constructor with full parameters.
        @param theAmplitude amplitude a
        @param theFrequency angular frequency b
        @param thePhase phase shift c
        @param theOffset vertical offset d
        """

    @overload
    def __init__(self, theOther: Cosine) -> None: ...

    def Value(self, theX: float) -> tuple[bool, float]:
        """
        Evaluates cosine function.
        @param[in] theX input value
        @param[out] theY function value
        @return true (always succeeds)
        """

    def Values(self, theX: float) -> tuple[bool, float, float]:
        """
        Evaluates cosine function and derivative.
        @param[in] theX input value
        @param[out] theY function value
        @param[out] theDY derivative value
        @return true (always succeeds)
        """

class Exponential:
    """Exponential function functor: f(x) = a * exp(b*x) + c."""

    @overload
    def __init__(self, theScale: float = 1.0, theRate: float = 1.0, theOffset: float = 0.0) -> None:
        """
        Constructor with full parameters.
        @param theScale scale factor a
        @param theRate rate b
        @param theOffset vertical offset c
        """

    @overload
    def __init__(self, theOther: Exponential) -> None: ...

    def Value(self, theX: float) -> tuple[bool, float]:
        """
        Evaluates exponential function.
        @param[in] theX input value
        @param[out] theY function value
        @return true (always succeeds)
        """

    def Values(self, theX: float) -> tuple[bool, float, float]:
        """
        Evaluates exponential function and derivative.
        @param[in] theX input value
        @param[out] theY function value
        @param[out] theDY derivative value
        @return true (always succeeds)
        """

class Power:
    """Power function functor: f(x) = a * x^n + b."""

    @overload
    def __init__(self, theExponent: float, theScale: float = 1.0, theOffset: float = 0.0) -> None:
        """
        Constructor with full parameters.
        @param theExponent power n
        @param theScale scale factor a
        @param theOffset vertical offset b
        """

    @overload
    def __init__(self, theOther: Power) -> None: ...

    def Value(self, theX: float) -> tuple[bool, float]:
        """
        Evaluates power function.
        @param[in] theX input value
        @param[out] theY function value
        @return false if x < 0 and exponent is non-integer
        """

    def Values(self, theX: float) -> tuple[bool, float, float]:
        """
        Evaluates power function and derivative.
        @param[in] theX input value
        @param[out] theY function value
        @param[out] theDY derivative value
        @return false if x < 0 and exponent is non-integer
        """

class Gaussian:
    """Gaussian function functor: f(x) = a * exp(-((x-mu)^2)/(2*sigma^2))."""

    @overload
    def __init__(self, theAmplitude: float = 1.0, theMean: float = 0.0, theSigma: float = 1.0) -> None:
        """
        Constructor with full parameters.
        @param theAmplitude amplitude a (peak height)
        @param theMean mean mu (center)
        @param theSigma standard deviation sigma (width)
        """

    @overload
    def __init__(self, theOther: Gaussian) -> None: ...

    def Value(self, theX: float) -> tuple[bool, float]:
        """
        Evaluates Gaussian function.
        @param[in] theX input value
        @param[out] theY function value
        @return false if sigma is zero
        """

    def Values(self, theX: float) -> tuple[bool, float, float]:
        """
        Evaluates Gaussian function and derivative.
        @param[in] theX input value
        @param[out] theY function value
        @param[out] theDY derivative value
        @return false if sigma is zero
        """

class QuadraticForm:
    """
    Quadratic form functor: f(x) = x^T A x + b^T x + c.
    Commonly used for testing optimization algorithms.

    Usage:
    @code
    math_Matrix A(1, 2, 1, 2);
    A(1,1) = 2.0; A(1,2) = 0.0;
    A(2,1) = 0.0; A(2,2) = 2.0;
    math_Vector b(1, 2);
    b(1) = -4.0; b(2) = -4.0;
    QuadraticForm aFunc(A, b, 8.0);  // f(x) = 2*x1^2 + 2*x2^2 - 4*x1 - 4*x2 + 8
    // Minimum at (1, 1) with value 4
    @endcode
    """

    @overload
    def __init__(self, theA: nanoocp.math.math_Matrix, theB: nanoocp.math.math_Vector, theC: float) -> None:
        """
        Constructor from matrix, vector, and constant.
        @param theA quadratic coefficient matrix (must be square)
        @param theB linear coefficient vector
        @param theC constant term
        """

    @overload
    def __init__(self, theOther: QuadraticForm) -> None: ...

    def Value(self, theX: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates the quadratic form f(x) = x^T A x + b^T x + c.
        @param[in] theX input vector
        @param[out] theY function value
        @return true if evaluation succeeded
        """

    def Gradient(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> bool:
        """
        Evaluates the gradient: g = 2*A*x + b.
        @param[in] theX input vector
        @param[out] theG gradient vector
        @return true if evaluation succeeded
        """

    def Values(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates both value and gradient.
        @param[in] theX input vector
        @param[out] theY function value
        @param[out] theG gradient vector
        @return true if evaluation succeeded
        """

class Rosenbrock:
    """
    Rosenbrock function functor (for testing optimization).
    f(x,y) = (a - x)^2 + b*(y - x^2)^2
    Default: a = 1, b = 100
    Global minimum at (a, a^2) = (1, 1) with f = 0.

    Usage:
    @code
    Rosenbrock aRosen;  // Default a=1, b=100
    math_Vector aStart(1, 2);
    aStart(1) = -1.0; aStart(2) = 1.0;
    auto aResult = MathOpt::BFGS(aRosen, aStart);
    // Should converge to (1, 1)
    @endcode
    """

    @overload
    def __init__(self, theA: float = 1.0, theB: float = 100.0) -> None:
        """
        Constructor with parameters.
        @param theA parameter a (default 1.0)
        @param theB parameter b (default 100.0)
        """

    @overload
    def __init__(self, theOther: Rosenbrock) -> None: ...

    def Value(self, theX: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates the Rosenbrock function.
        @param[in] theX input vector (must have length 2)
        @param[out] theY function value
        @return true if evaluation succeeded
        """

    def Gradient(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> bool:
        """
        Evaluates the gradient of the Rosenbrock function.
        @param[in] theX input vector
        @param[out] theG gradient vector
        @return true if evaluation succeeded
        """

    def Values(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates both value and gradient.
        @param[in] theX input vector
        @param[out] theY function value
        @param[out] theG gradient vector
        @return true if evaluation succeeded
        """

class Sphere:
    """
    Sphere function functor (for testing optimization).
    f(x) = sum(x[i]^2) for all i.
    Global minimum at origin with f = 0.

    Usage:
    @code
    Sphere aSphere;
    math_Vector aStart(1, 3);
    aStart.Init(1.0);  // Start at (1, 1, 1)
    auto aResult = MathOpt::Powell(aSphere, aStart);
    // Should converge to (0, 0, 0)
    @endcode
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Sphere) -> None: ...

    def Value(self, theX: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates the sphere function.
        @param[in] theX input vector
        @param[out] theY function value
        @return true (always succeeds)
        """

    def Gradient(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> bool:
        """
        Evaluates the gradient of the sphere function.
        @param[in] theX input vector
        @param[out] theG gradient vector
        @return true (always succeeds)
        """

    def Values(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates both value and gradient.
        @param[in] theX input vector
        @param[out] theY function value
        @param[out] theG gradient vector
        @return true (always succeeds)
        """

class Booth:
    """
    Booth function functor (for testing optimization).
    f(x,y) = (x + 2y - 7)^2 + (2x + y - 5)^2
    Global minimum at (1, 3) with f = 0.

    Usage:
    @code
    Booth aBooth;
    math_Vector aStart(1, 2);
    aStart(1) = 0.0; aStart(2) = 0.0;
    auto aResult = MathOpt::BFGS(aBooth, aStart);
    // Should converge to (1, 3)
    @endcode
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Booth) -> None: ...

    def Value(self, theX: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates the Booth function.
        @param[in] theX input vector (must have length 2)
        @param[out] theY function value
        @return true (always succeeds)
        """

    def Gradient(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> bool:
        """
        Evaluates the gradient of the Booth function.
        @param[in] theX input vector
        @param[out] theG gradient vector
        @return true (always succeeds)
        """

    def Values(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates both value and gradient.
        @param[in] theX input vector
        @param[out] theY function value
        @param[out] theG gradient vector
        @return true (always succeeds)
        """

class Beale:
    """
    Beale function functor (for testing optimization).
    f(x,y) = (1.5 - x + xy)^2 + (2.25 - x + xy^2)^2 + (2.625 - x + xy^3)^2
    Global minimum at (3, 0.5) with f = 0.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Beale) -> None: ...

    def Value(self, theX: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates the Beale function.
        @param[in] theX input vector (must have length 2)
        @param[out] theY function value
        @return true (always succeeds)
        """

    def Gradient(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> bool:
        """
        Evaluates the gradient of the Beale function.
        @param[in] theX input vector
        @param[out] theG gradient vector
        @return true (always succeeds)
        """

    def Values(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates both value and gradient.
        @param[in] theX input vector
        @param[out] theY function value
        @param[out] theG gradient vector
        @return true (always succeeds)
        """

class Himmelblau:
    """
    Himmelblau function functor (for testing optimization).
    f(x,y) = (x^2 + y - 11)^2 + (x + y^2 - 7)^2
    Has four local minima, all with f = 0:
    (3.0, 2.0), (-2.805118, 3.131312), (-3.779310, -3.283186), (3.584428, -1.848126)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Himmelblau) -> None: ...

    def Value(self, theX: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates the Himmelblau function.
        @param[in] theX input vector (must have length 2)
        @param[out] theY function value
        @return true (always succeeds)
        """

    def Gradient(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> bool:
        """
        Evaluates the gradient of the Himmelblau function.
        @param[in] theX input vector
        @param[out] theG gradient vector
        @return true (always succeeds)
        """

    def Values(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates both value and gradient.
        @param[in] theX input vector
        @param[out] theY function value
        @param[out] theG gradient vector
        @return true (always succeeds)
        """

class Rastrigin:
    """
    Rastrigin function functor (for testing global optimization).
    f(x) = A*n + sum(x[i]^2 - A*cos(2*pi*x[i])) for all i
    Default: A = 10
    Global minimum at origin with f = 0.
    Highly multimodal - challenging for local optimizers.
    """

    @overload
    def __init__(self, theA: float = 10.0) -> None:
        """
        Constructor with parameter.
        @param theA parameter A (default 10.0)
        """

    @overload
    def __init__(self, theOther: Rastrigin) -> None: ...

    def Value(self, theX: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates the Rastrigin function.
        @param[in] theX input vector
        @param[out] theY function value
        @return true (always succeeds)
        """

    def Gradient(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> bool:
        """
        Evaluates the gradient of the Rastrigin function.
        @param[in] theX input vector
        @param[out] theG gradient vector
        @return true (always succeeds)
        """

    def Values(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates both value and gradient.
        @param[in] theX input vector
        @param[out] theY function value
        @param[out] theG gradient vector
        @return true (always succeeds)
        """

class Ackley:
    """
    Ackley function functor (for testing global optimization).
    f(x) = -a*exp(-b*sqrt(sum(x[i]^2)/n)) - exp(sum(cos(c*x[i]))/n) + a + e
    Default: a = 20, b = 0.2, c = 2*pi
    Global minimum at origin with f = 0.
    """

    @overload
    def __init__(self, theA: float = 20.0, theB: float = 0.2, theC: float = 6.283185307179586) -> None:
        """
        Constructor with parameters.
        @param theA parameter a (default 20.0)
        @param theB parameter b (default 0.2)
        @param theC parameter c (default 2*pi)
        """

    @overload
    def __init__(self, theOther: Ackley) -> None: ...

    def Value(self, theX: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates the Ackley function.
        @param[in] theX input vector
        @param[out] theY function value
        @return true (always succeeds)
        """

class LinearResidual:
    """
    Linear system residual functor: f(x) = ||Ax - b||^2.
    Useful for solving overdetermined linear systems via optimization.

    Usage:
    @code
    math_Matrix A(1, 3, 1, 2);  // 3x2 overdetermined system
    math_Vector b(1, 3);
    // ... fill A and b ...
    LinearResidual aRes(A, b);
    math_Vector aStart(1, 2);
    aStart.Init(0.0);
    auto aResult = MathOpt::BFGS(aRes, aStart);
    @endcode
    """

    @overload
    def __init__(self, theA: nanoocp.math.math_Matrix, theB: nanoocp.math.math_Vector) -> None:
        """
        Constructor from matrix and right-hand side.
        @param theA coefficient matrix (m x n)
        @param theB right-hand side vector (m)
        """

    @overload
    def __init__(self, theOther: LinearResidual) -> None: ...

    def Value(self, theX: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates the residual ||Ax - b||^2.
        @param[in] theX solution vector (n)
        @param[out] theY squared residual norm
        @return true (always succeeds)
        """

    def Gradient(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> bool:
        """
        Evaluates the gradient: g = 2 * A^T * (Ax - b).
        @param[in] theX solution vector
        @param[out] theG gradient vector
        @return true (always succeeds)
        """

    def Values(self, theX: nanoocp.math.math_Vector, theG: nanoocp.math.math_Vector) -> tuple[bool, float]:
        """
        Evaluates both value and gradient.
        @param[in] theX solution vector
        @param[out] theY squared residual norm
        @param[out] theG gradient vector
        @return true (always succeeds)
        """

def Clamp(theValue: float, theLower: float, theUpper: float) -> float:
    """
    Clamp value to range [theLower, theUpper].
    @param theValue value to clamp
    @param theLower lower bound
    @param theUpper upper bound
    @return clamped value
    """

def IsZero(theValue: float, theTolerance: float = 1e-15) -> bool:
    """
    Check if value is effectively zero.
    @param theValue value to check
    @param theTolerance tolerance for zero comparison
    @return true if |theValue| < theTolerance
    """

def IsEqual(theA: float, theB: float, theTolerance: float = 1e-15) -> bool:
    """
    Check if two values are approximately equal.
    @param theA first value
    @param theB second value
    @param theTolerance relative tolerance
    @return true if values are approximately equal
    """

def SafeDiv(theNumerator: float, theDenominator: float, theDefault: float = 0.0) -> float:
    """
    Safe division avoiding division by zero.
    @param theNumerator numerator
    @param theDenominator denominator
    @param theDefault default value if denominator is zero
    @return theNumerator / theDenominator or theDefault
    """

def Sign(theValue: float) -> int:
    """
    Sign function.
    @param theValue input value
    @return -1 if negative, 0 if zero, +1 if positive
    """

def SignTransfer(theA: float, theB: float) -> float:
    """
    Sign transfer function: returns |theA| with sign of theB.
    Equivalent to copysign but avoids edge cases with zero.
    @param theA value whose magnitude is used
    @param theB value whose sign is used
    @return |theA| * sign(theB)
    """

def Sqr(theValue: float) -> float:
    """
    Square of a value.
    @param theValue input value
    @return theValue * theValue
    """

def Cube(theValue: float) -> float:
    """
    Cube of a value.
    @param theValue input value
    @return theValue^3
    """

def CubeRoot(theValue: float) -> float:
    """
    Cube root with proper sign handling.
    Unlike std::cbrt, this handles negative values correctly on all platforms.
    @param theValue input value
    @return cube root of theValue
    """

def IsFinite(theValue: float) -> bool:
    """
    Check if value is finite (not NaN or Inf).
    @param theValue value to check
    @return true if finite
    """

def DotProduct(theA: nanoocp.math.math_Vector, theB: nanoocp.math.math_Vector) -> float:
    """
    Compute dot product of two vectors.
    @param theA first vector
    @param theB second vector
    @return dot product sum(A[i] * B[i])
    """

def VectorNorm(theVec: nanoocp.math.math_Vector) -> float:
    """
    Compute Euclidean norm of a vector.
    @param theVec input vector
    @return sqrt(sum(V[i]^2))
    """

def VectorInfNorm(theVec: nanoocp.math.math_Vector) -> float:
    """
    Compute infinity norm (maximum absolute value) of a vector.
    @param theVec input vector
    @return max(|V[i]|)
    """

def IsXConverged(theXOld: float, theXNew: float, theTolerance: float) -> bool:
    """
    Check convergence based on relative change in X.
    Uses relative tolerance scaled by current value magnitude.
    @param theXOld previous X value
    @param theXNew current X value
    @param theTolerance relative tolerance
    @return true if converged
    """

def IsFConverged(theFValue: float, theTolerance: float) -> bool:
    """
    Check convergence based on absolute function value.
    @param theFValue function value f(x)
    @param theTolerance absolute tolerance
    @return true if |f(x)| < tolerance
    """

def IsConverged(theXOld: float, theXNew: float, theFValue: float, theConfig: Config) -> bool:
    """
    Combined convergence test for scalar root finders.
    Checks both X convergence and function value convergence.
    @param theXOld previous X value
    @param theXNew current X value
    @param theFValue function value at theXNew
    @param theConfig solver configuration
    @return true if either criterion is satisfied
    """

def IsMinConverged(theXOld: float, theXNew: float, theFOld: float, theFNew: float, theConfig: Config) -> bool:
    """
    Convergence test for minimization (checks both X and F change).
    @param theXOld previous X value
    @param theXNew current X value
    @param theFOld previous function value
    @param theFNew current function value
    @param theConfig solver configuration
    @return true if converged
    """

def IsVectorConverged(theOld: nanoocp.math.math_Vector, theNew: nanoocp.math.math_Vector, theTolerance: float) -> bool:
    """
    Convergence test for vector solvers using infinity norm.
    @param theOld previous solution vector
    @param theNew current solution vector
    @param theTolerance relative tolerance
    @return true if max|new_i - old_i| / max(1, |new_i|) < tolerance
    """

def IsGradientConverged(theGradient: nanoocp.math.math_Vector, theTolerance: float) -> bool:
    """
    Convergence test using gradient norm for minimization.
    @param theGradient gradient vector
    @param theTolerance tolerance for gradient norm
    @return true if ||gradient|| < tolerance
    """

def InfinityNorm(theVector: nanoocp.math.math_Vector) -> float:
    """
    Compute infinity norm of a vector.
    @param theVector input vector
    @return max|v_i|
    """

def EuclideanNorm(theVector: nanoocp.math.math_Vector) -> float:
    """
    Compute Euclidean (L2) norm of a vector.
    @param theVector input vector
    @return sqrt(sum(v_i^2))
    """

def DepressCubic(theB: float, theC: float, theD: float) -> tuple[float, float, float]:
    """
    Compute depressed cubic coefficients.
    Transforms x^3 + bx^2 + cx + d to t^3 + pt + q via x = t - b/3.
    @param theB coefficient of x^2 (after dividing by leading coeff)
    @param theC coefficient of x
    @param theD constant term
    @param[out] theP coefficient of t in depressed form
    @param[out] theQ constant term in depressed form
    @param[out] theShift substitution shift (b/3)
    """

def DepressQuartic(theB: float, theC: float, theD: float, theE: float) -> tuple[float, float, float, float]:
    """
    Compute depressed quartic coefficients.
    Transforms x^4 + bx^3 + cx^2 + dx + e to t^4 + pt^2 + qt + r via x = t - b/4.
    @param theB coefficient of x^3 (after dividing by leading coeff)
    @param theC coefficient of x^2
    @param theD coefficient of x
    @param theE constant term
    @param[out] theP coefficient of t^2 in depressed form
    @param[out] theQ coefficient of t in depressed form
    @param[out] theR constant term in depressed form
    @param[out] theShift substitution shift (b/4)
    """

def GetGaussPointsAndWeights(theOrder: int, thePoints: nanoocp.math.math_Vector, theWeights: nanoocp.math.math_Vector) -> bool:
    """
    Get ordered Gauss-Legendre points and weights for given order.
    Points are returned in ascending order on [-1, 1].
    @param theOrder number of quadrature points (>= 1)
    @param[out] thePoints points array
    @param[out] theWeights weights array
    @return true if points/weights are available
    """

def QuadraticInterpolation(thePhi0: float, thePhi0Prime: float, theAlpha1: float, thePhi1: float) -> float:
    """
    Quadratic interpolation step for line search.
    Given phi(0), phi'(0), and phi(alpha1), finds minimum of quadratic fit.

    @param thePhi0 function value at 0
    @param thePhi0Prime directional derivative at 0
    @param theAlpha1 current step size
    @param thePhi1 function value at alpha1
    @return interpolated step size
    """

def GetKronrodPointsAndWeights(theNbKronrod: int, thePoints: nanoocp.math.math_Vector, theWeights: nanoocp.math.math_Vector) -> bool:
    """
    Get Gauss-Kronrod points and weights.
    @param theNbKronrod number of Kronrod points (should be 2n+1)
    @param thePoints output vector for points
    @param theWeights output vector for weights
    @return true if successful
    """

def GetOrderedGaussPointsAndWeights(theNbGauss: int, thePoints: nanoocp.math.math_Vector, theWeights: nanoocp.math.math_Vector) -> bool:
    """
    Get ordered Gauss points and weights.
    @param theNbGauss number of Gauss points
    @param thePoints output vector for points
    @param theWeights output vector for weights
    @return true if successful
    """
