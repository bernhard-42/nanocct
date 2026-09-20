"""OCCT package MathOpt (toolkit TKMath)"""

import enum
from typing import overload

import nanoocp.MathUtils
import nanoocp.math


class ConjugateGradientFormula(enum.Enum):
    """Conjugate gradient formula selection."""

    FletcherReeves = 0

    PolakRibiere = 1

    HestenesStiefel = 2

    DaiYuan = 3

class PSOInitMode(enum.Enum):
    """Initialization mode for PSO particles."""

    RandomOnly = 0

    SeededOnly = 1

    SeededPlusRandom = 2

class PSOBoundaryMode(enum.Enum):
    """Boundary handling mode for particles leaving the search space."""

    Clamp = 0

    Reflect = 1

    Wrap = 2

class PSOInertiaSchedule(enum.Enum):
    """Inertia weight schedule."""

    Constant = 0

    LinearDecay = 1

class GlobalStrategy(enum.Enum):
    """Global optimization strategy selection."""

    PSO = 0

    MultiStart = 1

    PSOHybrid = 2

    DifferentialEvolution = 3

class FRPRConfig(nanoocp.MathUtils.Config):
    """Configuration for FRPR conjugate gradient method."""

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theTolerance: float, theMaxIter: int = 100) -> None:
        """Constructor with tolerance."""

    @property
    def Formula(self) -> ConjugateGradientFormula:
        """Beta formula"""

    @Formula.setter
    def Formula(self, arg: ConjugateGradientFormula, /) -> None: ...

    @property
    def RestartInterval(self) -> int:
        """Restart every N iterations (0 = n, where n is dimension)"""

    @RestartInterval.setter
    def RestartInterval(self, arg: int, /) -> None: ...

class NewtonConfig(nanoocp.MathUtils.Config):
    """Configuration for Newton minimization with Hessian."""

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theTolerance: float, theMaxIter: int = 100) -> None:
        """Constructor with tolerance."""

    @property
    def Regularization(self) -> float:
        """Diagonal regularization for non-positive definite Hessian"""

    @Regularization.setter
    def Regularization(self, arg: float, /) -> None: ...

    @property
    def UseLineSearch(self) -> bool:
        """Whether to use line search (recommended)"""

    @UseLineSearch.setter
    def UseLineSearch(self, arg: bool, /) -> None: ...

class PSOSeedParticle:
    """Seed particle for PSO initialization."""

    @overload
    def __init__(self, thePos: nanoocp.math.math_Vector) -> None: ...

    @overload
    def __init__(self, thePos: nanoocp.math.math_Vector, theValue: float) -> None: ...

    @property
    def Position(self) -> nanoocp.math.math_Vector:
        """Initial position (will be clamped to bounds)"""

    @Position.setter
    def Position(self, arg: nanoocp.math.math_Vector, /) -> None: ...

    @property
    def Value(self) -> float | None:
        """Known function value (nullopt = will be evaluated)"""

    @Value.setter
    def Value(self, arg: float | None, /) -> None: ...

    @property
    def Velocity(self) -> nanoocp.math.math_Vector | None:
        """Initial velocity (nullopt = generate bounded random)"""

    @Velocity.setter
    def Velocity(self, arg: nanoocp.math.math_Vector | None, /) -> None: ...

class PSOStats:
    """Statistics collected during PSO execution."""

    def __init__(self) -> None: ...

    @property
    def NbFunctionEvals(self) -> int:
        """Total function evaluations"""

    @NbFunctionEvals.setter
    def NbFunctionEvals(self, arg: int, /) -> None: ...

    @property
    def NbIterations(self) -> int:
        """Iterations performed"""

    @NbIterations.setter
    def NbIterations(self, arg: int, /) -> None: ...

    @property
    def NbBoundaryCorrections(self) -> int:
        """Boundary corrections applied"""

    @NbBoundaryCorrections.setter
    def NbBoundaryCorrections(self, arg: int, /) -> None: ...

    @property
    def NbStagnationEvents(self) -> int:
        """Times stagnation was detected"""

    @NbStagnationEvents.setter
    def NbStagnationEvents(self, arg: int, /) -> None: ...

    @property
    def NbRestarts(self) -> int:
        """Restarts performed"""

    @NbRestarts.setter
    def NbRestarts(self, arg: int, /) -> None: ...

    @property
    def InitialBest(self) -> float:
        """Best value after initialization"""

    @InitialBest.setter
    def InitialBest(self, arg: float, /) -> None: ...

    @property
    def FinalBest(self) -> float:
        """Best value at termination"""

    @FinalBest.setter
    def FinalBest(self, arg: float, /) -> None: ...

class PSOConfig(nanoocp.MathUtils.NDimConfig):
    """Configuration for Particle Swarm Optimization."""

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theNbParticles: int, theMaxIter: int = 100, theTolerance: float = 1e-08) -> None:
        """Constructor with parameters."""

    @property
    def NbParticles(self) -> int:
        """Number of particles in the swarm"""

    @NbParticles.setter
    def NbParticles(self, arg: int, /) -> None: ...

    @property
    def Omega(self) -> float:
        """Inertia weight (velocity decay)"""

    @Omega.setter
    def Omega(self, arg: float, /) -> None: ...

    @property
    def PhiPersonal(self) -> float:
        """Personal best attraction coefficient"""

    @PhiPersonal.setter
    def PhiPersonal(self, arg: float, /) -> None: ...

    @property
    def PhiGlobal(self) -> float:
        """Global best attraction coefficient"""

    @PhiGlobal.setter
    def PhiGlobal(self, arg: float, /) -> None: ...

    @property
    def VelocityClamp(self) -> float:
        """Max velocity as fraction of search space"""

    @VelocityClamp.setter
    def VelocityClamp(self, arg: float, /) -> None: ...

    @property
    def Seed(self) -> int:
        """Random seed for reproducibility"""

    @Seed.setter
    def Seed(self, arg: int, /) -> None: ...

    @property
    def InitMode(self) -> PSOInitMode: ...

    @InitMode.setter
    def InitMode(self, arg: PSOInitMode, /) -> None: ...

    @property
    def BoundaryMode(self) -> PSOBoundaryMode: ...

    @BoundaryMode.setter
    def BoundaryMode(self, arg: PSOBoundaryMode, /) -> None: ...

    @property
    def InertiaSchedule(self) -> PSOInertiaSchedule: ...

    @InertiaSchedule.setter
    def InertiaSchedule(self, arg: PSOInertiaSchedule, /) -> None: ...

    @property
    def OmegaMin(self) -> float:
        """Min inertia for LinearDecay"""

    @OmegaMin.setter
    def OmegaMin(self, arg: float, /) -> None: ...

    @property
    def MinIterations(self) -> int:
        """Minimum iterations before convergence"""

    @MinIterations.setter
    def MinIterations(self, arg: int, /) -> None: ...

    @property
    def TargetValue(self) -> float | None:
        """Early stop if best <= target (nullopt = disabled)"""

    @TargetValue.setter
    def TargetValue(self, arg: float | None, /) -> None: ...

    @property
    def NoImproveTol(self) -> float:
        """Stagnation tolerance (0 = use Tolerance)"""

    @NoImproveTol.setter
    def NoImproveTol(self, arg: float, /) -> None: ...

    @property
    def NoImproveIters(self) -> int:
        """Stagnation iteration threshold"""

    @NoImproveIters.setter
    def NoImproveIters(self, arg: int, /) -> None: ...

    @property
    def RestartFraction(self) -> float:
        """Fraction of particles to reinitialize (0 = no restarts)"""

    @RestartFraction.setter
    def RestartFraction(self, arg: float, /) -> None: ...

    @property
    def MaxRestarts(self) -> int:
        """Maximum restart count (0 = unlimited when fraction > 0)"""

    @MaxRestarts.setter
    def MaxRestarts(self, arg: int, /) -> None: ...

    @property
    def PolishBudgetPerDim(self) -> int:
        """Max polishing evals per dimension (0 = no polishing)"""

    @PolishBudgetPerDim.setter
    def PolishBudgetPerDim(self, arg: int, /) -> None: ...

class GlobalConfig(nanoocp.MathUtils.NDimConfig):
    """Configuration for global optimization."""

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theStrategy: GlobalStrategy, theMaxIter: int = 200) -> None:
        """Constructor with strategy."""

    @property
    def Strategy(self) -> GlobalStrategy:
        """Algorithm to use"""

    @Strategy.setter
    def Strategy(self, arg: GlobalStrategy, /) -> None: ...

    @property
    def NbPopulation(self) -> int:
        """Population/swarm size"""

    @NbPopulation.setter
    def NbPopulation(self, arg: int, /) -> None: ...

    @property
    def NbStarts(self) -> int:
        """Number of random starts (for MultiStart)"""

    @NbStarts.setter
    def NbStarts(self, arg: int, /) -> None: ...

    @property
    def MutationScale(self) -> float:
        """Mutation scale (for DE)"""

    @MutationScale.setter
    def MutationScale(self, arg: float, /) -> None: ...

    @property
    def CrossoverProb(self) -> float:
        """Crossover probability (for DE)"""

    @CrossoverProb.setter
    def CrossoverProb(self, arg: float, /) -> None: ...

    @property
    def Seed(self) -> int:
        """Random seed"""

    @Seed.setter
    def Seed(self, arg: int, /) -> None: ...

    @property
    def PolishBudgetPerDim(self) -> int:
        """Max polishing evals per dimension (0 = no polishing)"""

    @PolishBudgetPerDim.setter
    def PolishBudgetPerDim(self, arg: int, /) -> None: ...

class UzawaResult:
    """Result for Uzawa constrained optimization."""

    def __init__(self) -> None: ...

    def IsDone(self) -> bool: ...

    @property
    def Status(self) -> nanoocp.MathUtils.Status: ...

    @Status.setter
    def Status(self, arg: nanoocp.MathUtils.Status, /) -> None: ...

    @property
    def Solution(self) -> nanoocp.math.math_Vector | None:
        """Solution vector X"""

    @Solution.setter
    def Solution(self, arg: nanoocp.math.math_Vector | None, /) -> None: ...

    @property
    def Dual(self) -> nanoocp.math.math_Vector | None:
        """Dual (Lagrange) variables"""

    @Dual.setter
    def Dual(self, arg: nanoocp.math.math_Vector | None, /) -> None: ...

    @property
    def Error(self) -> nanoocp.math.math_Vector | None:
        """X - X0 (difference from starting point)"""

    @Error.setter
    def Error(self, arg: nanoocp.math.math_Vector | None, /) -> None: ...

    @property
    def InitialError(self) -> nanoocp.math.math_Vector | None:
        """C*X0 - S (initial constraint violation)"""

    @InitialError.setter
    def InitialError(self, arg: nanoocp.math.math_Vector | None, /) -> None: ...

    @property
    def InverseCTC(self) -> nanoocp.math.math_Matrix | None:
        """(C * C^T)^-1 for gradient computation"""

    @InverseCTC.setter
    def InverseCTC(self, arg: nanoocp.math.math_Matrix | None, /) -> None: ...

    @property
    def NbIterations(self) -> int: ...

    @NbIterations.setter
    def NbIterations(self, arg: int, /) -> None: ...

class UzawaConfig:
    """Configuration for Uzawa algorithm."""

    def __init__(self) -> None: ...

    @property
    def EpsLix(self) -> float:
        """Tolerance for X convergence"""

    @EpsLix.setter
    def EpsLix(self, arg: float, /) -> None: ...

    @property
    def EpsLic(self) -> float:
        """Tolerance for dual variable convergence"""

    @EpsLic.setter
    def EpsLic(self, arg: float, /) -> None: ...

    @property
    def MaxIterations(self) -> int:
        """Maximum iterations"""

    @MaxIterations.setter
    def MaxIterations(self, arg: int, /) -> None: ...

def Uzawa(theCont: nanoocp.math.math_Matrix, theSecont: nanoocp.math.math_Vector, theStartingPoint: nanoocp.math.math_Vector, theNce: int, theNci: int, theConfig: UzawaConfig = ...) -> UzawaResult:
    """
    Solve constrained least squares using Uzawa algorithm.

    Solves: min ||X - X0||^2 subject to C*X = S

    For equality constraints only, uses direct Crout decomposition.
    For mixed equality/inequality constraints, uses iterative Uzawa method.

    The Uzawa algorithm is a dual decomposition method that:
    1. Updates primal variables X to minimize Lagrangian
    2. Updates dual variables (Lagrange multipliers) for constraint violations

    @param theCont constraint matrix C (Nce+Nci rows x N cols)
    @param theSecont right-hand side S
    @param theStartingPoint initial point X0
    @param theNce number of equality constraints (first rows)
    @param theNci number of inequality constraints (last rows, C*X <= S)
    @param theConfig algorithm configuration
    @return UzawaResult with solution and auxiliary data
    """

def UzawaEquality(theCont: nanoocp.math.math_Matrix, theSecont: nanoocp.math.math_Vector, theStartingPoint: nanoocp.math.math_Vector, theConfig: UzawaConfig = ...) -> UzawaResult:
    """
    Solve constrained least squares with equality constraints only.

    Convenience function for C*X = S with min ||X - X0||.

    @param theCont constraint matrix C
    @param theSecont right-hand side S
    @param theStartingPoint initial point X0
    @param theConfig algorithm configuration
    @return UzawaResult with solution
    """
