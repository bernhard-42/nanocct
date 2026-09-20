"""OCCT package MathLin (toolkit TKMath)"""

import enum
from typing import overload

import nanoocp.MathUtils
import nanoocp.math


class LeastSquaresMethod(enum.Enum):
    """Method for solving least squares problems."""

    NormalEquations = 0

    QR = 1

    SVD = 2

class LUResult:
    """Result for LU decomposition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LUResult) -> None: ...

    def IsDone(self) -> bool: ...

    @property
    def Status(self) -> nanoocp.MathUtils.Status: ...

    @Status.setter
    def Status(self, arg: nanoocp.MathUtils.Status, /) -> None: ...

    @property
    def LU(self) -> nanoocp.math.math_Matrix | None:
        """Combined L and U matrices"""

    @LU.setter
    def LU(self, arg: nanoocp.math.math_Matrix | None, /) -> None: ...

    @property
    def Pivot(self) -> nanoocp.math.math_IntegerVector | None:
        """Pivot indices"""

    @Pivot.setter
    def Pivot(self, arg: nanoocp.math.math_IntegerVector | None, /) -> None: ...

    @property
    def Determinant(self) -> float | None: ...

    @Determinant.setter
    def Determinant(self, arg: float | None, /) -> None: ...

    @property
    def Sign(self) -> int:
        """Sign from row interchanges"""

    @Sign.setter
    def Sign(self, arg: int, /) -> None: ...

class CroutResult:
    """
    Result for Crout LDL^T decomposition.
    Specialized for symmetric matrices.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CroutResult) -> None: ...

    def IsDone(self) -> bool: ...

    @property
    def Status(self) -> nanoocp.MathUtils.Status: ...

    @Status.setter
    def Status(self, arg: nanoocp.MathUtils.Status, /) -> None: ...

    @property
    def L(self) -> nanoocp.math.math_Matrix | None:
        """Lower triangular matrix (unit diagonal)"""

    @L.setter
    def L(self, arg: nanoocp.math.math_Matrix | None, /) -> None: ...

    @property
    def D(self) -> nanoocp.math.math_Vector | None:
        """Diagonal elements"""

    @D.setter
    def D(self, arg: nanoocp.math.math_Vector | None, /) -> None: ...

    @property
    def Inverse(self) -> nanoocp.math.math_Matrix | None:
        """Inverse matrix (lower triangle only)"""

    @Inverse.setter
    def Inverse(self, arg: nanoocp.math.math_Matrix | None, /) -> None: ...

    @property
    def Determinant(self) -> float | None:
        """Matrix determinant"""

    @Determinant.setter
    def Determinant(self, arg: float | None, /) -> None: ...

class SVDResult:
    """Result for SVD decomposition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: SVDResult) -> None: ...

    def IsDone(self) -> bool: ...

    @property
    def Status(self) -> nanoocp.MathUtils.Status: ...

    @Status.setter
    def Status(self, arg: nanoocp.MathUtils.Status, /) -> None: ...

    @property
    def U(self) -> nanoocp.math.math_Matrix | None:
        """Left singular vectors (m x n)"""

    @U.setter
    def U(self, arg: nanoocp.math.math_Matrix | None, /) -> None: ...

    @property
    def SingularValues(self) -> nanoocp.math.math_Vector | None:
        """Singular values (n elements)"""

    @SingularValues.setter
    def SingularValues(self, arg: nanoocp.math.math_Vector | None, /) -> None: ...

    @property
    def V(self) -> nanoocp.math.math_Matrix | None:
        """Right singular vectors (n x n)"""

    @V.setter
    def V(self, arg: nanoocp.math.math_Matrix | None, /) -> None: ...

    @property
    def Rank(self) -> int:
        """Numerical rank"""

    @Rank.setter
    def Rank(self, arg: int, /) -> None: ...

class QRResult:
    """Result for QR decomposition using Householder reflections."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: QRResult) -> None: ...

    def IsDone(self) -> bool: ...

    @property
    def Status(self) -> nanoocp.MathUtils.Status: ...

    @Status.setter
    def Status(self, arg: nanoocp.MathUtils.Status, /) -> None: ...

    @property
    def Q(self) -> nanoocp.math.math_Matrix | None:
        """Orthogonal matrix Q (m x m)"""

    @Q.setter
    def Q(self, arg: nanoocp.math.math_Matrix | None, /) -> None: ...

    @property
    def R(self) -> nanoocp.math.math_Matrix | None:
        """Upper triangular matrix R (m x n)"""

    @R.setter
    def R(self, arg: nanoocp.math.math_Matrix | None, /) -> None: ...

    @property
    def Rank(self) -> int:
        """Numerical rank"""

    @Rank.setter
    def Rank(self, arg: int, /) -> None: ...

class LeastSquaresResult:
    """Result for least squares problems."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LeastSquaresResult) -> None: ...

    def IsDone(self) -> bool: ...

    @property
    def Status(self) -> nanoocp.MathUtils.Status: ...

    @Status.setter
    def Status(self, arg: nanoocp.MathUtils.Status, /) -> None: ...

    @property
    def Solution(self) -> nanoocp.math.math_Vector | None:
        """Least squares solution x"""

    @Solution.setter
    def Solution(self, arg: nanoocp.math.math_Vector | None, /) -> None: ...

    @property
    def Residual(self) -> float | None:
        """||Ax - b||_2 (L2 norm of residual)"""

    @Residual.setter
    def Residual(self, arg: float | None, /) -> None: ...

    @property
    def ResidualSq(self) -> float | None:
        """||Ax - b||_2^2 (squared residual)"""

    @ResidualSq.setter
    def ResidualSq(self, arg: float | None, /) -> None: ...

    @property
    def Rank(self) -> int:
        """Numerical rank of A (for SVD)"""

    @Rank.setter
    def Rank(self, arg: int, /) -> None: ...

class EigenResult:
    """Result for eigenvalue decomposition of tridiagonal matrix."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: EigenResult) -> None: ...

    def IsDone(self) -> bool: ...

    @property
    def Status(self) -> nanoocp.MathUtils.Status: ...

    @Status.setter
    def Status(self, arg: nanoocp.MathUtils.Status, /) -> None: ...

    @property
    def EigenValues(self) -> nanoocp.math.math_Vector | None:
        """Computed eigenvalues"""

    @EigenValues.setter
    def EigenValues(self, arg: nanoocp.math.math_Vector | None, /) -> None: ...

    @property
    def EigenVectors(self) -> nanoocp.math.math_Matrix | None:
        """Eigenvectors as columns"""

    @EigenVectors.setter
    def EigenVectors(self, arg: nanoocp.math.math_Matrix | None, /) -> None: ...

    @property
    def Dimension(self) -> int: ...

    @Dimension.setter
    def Dimension(self, arg: int, /) -> None: ...

def LU(theA: nanoocp.math.math_Matrix, theMinPivot: float = 1e-20) -> LUResult:
    """
    Perform LU decomposition of matrix A with partial pivoting.
    Decomposes A into L*U where L is lower triangular with unit diagonal
    and U is upper triangular. The result stores L and U in a combined matrix.

    @param theA input square matrix
    @param theMinPivot minimum pivot value (smaller treated as singular)
    @return LU decomposition result
    """

def Solve(theA: nanoocp.math.math_Matrix, theB: nanoocp.math.math_Vector, theMinPivot: float = 1e-20) -> nanoocp.MathUtils.LinearResult:
    """
    Solve linear system AX = B using LU decomposition.

    @param theA coefficient matrix (square)
    @param theB right-hand side vector
    @param theMinPivot minimum pivot value
    @return result containing solution vector
    """

def SolveMultiple(theA: nanoocp.math.math_Matrix, theB: nanoocp.math.math_Matrix, theMinPivot: float = 1e-20) -> nanoocp.MathUtils.LinearMultipleResult:
    """
    Solve multiple linear systems AX = B where B is a matrix.
    Each column of B is a separate right-hand side.

    @param theA coefficient matrix (square)
    @param theB right-hand side matrix
    @param theMinPivot minimum pivot value
    @return result containing solution matrix
    """

def Determinant(theA: nanoocp.math.math_Matrix, theMinPivot: float = 1e-20) -> nanoocp.MathUtils.LinearResult:
    """
    Compute determinant of matrix A.

    @param theA input square matrix
    @param theMinPivot minimum pivot value
    @return result containing determinant value
    """

def Invert(theA: nanoocp.math.math_Matrix, theMinPivot: float = 1e-20) -> nanoocp.MathUtils.InverseResult:
    """
    Compute inverse of matrix A.

    @param theA input square matrix
    @param theMinPivot minimum pivot value
    @return result containing inverse matrix
    """

def Crout(theA: nanoocp.math.math_Matrix, theMinPivot: float = 1e-20) -> CroutResult:
    """
    Crout decomposition for symmetric matrices: A = L * D * L^T.

    This algorithm decomposes a symmetric matrix A into:
    - L: lower triangular matrix with unit diagonal
    - D: diagonal matrix

    Properties:
    - Only the lower triangle of A is used
    - Faster than general LU for symmetric matrices
    - Computes inverse efficiently
    - Requires positive definiteness for stability

    @param theA input symmetric matrix (only lower triangle used)
    @param theMinPivot minimum pivot value (smaller treated as singular)
    @return Crout decomposition result
    """

def SolveCrout(theA: nanoocp.math.math_Matrix, theB: nanoocp.math.math_Vector, theMinPivot: float = 1e-20) -> nanoocp.MathUtils.LinearResult:
    """
    Solve symmetric linear system Ax = b using Crout decomposition.

    Uses precomputed Crout decomposition to solve for x.
    More efficient than LU for symmetric positive definite matrices.

    @param theA coefficient matrix (symmetric)
    @param theB right-hand side vector
    @param theMinPivot minimum pivot value
    @return result containing solution vector
    """

def InvertCrout(theA: nanoocp.math.math_Matrix, theMinPivot: float = 1e-20) -> nanoocp.MathUtils.InverseResult:
    """
    Compute inverse of symmetric matrix using Crout decomposition.

    @param theA input symmetric matrix
    @param theMinPivot minimum pivot value
    @return result containing full symmetric inverse matrix
    """

def SVD(theA: nanoocp.math.math_Matrix, theTolerance: float = 1e-15) -> SVDResult:
    """
    Singular Value Decomposition: A = U * diag(S) * V^T.

    Decomposes an m x n matrix A into:
    - U: m x n matrix of left singular vectors (orthonormal columns)
    - S: n singular values in descending order
    - V: n x n matrix of right singular vectors (orthonormal)

    Properties:
    - Works for any m x n matrix (m can be less, equal, or greater than n)
    - Singular values are always non-negative
    - Provides the best low-rank approximation of a matrix
    - Useful for solving ill-conditioned linear systems

    @param theA input matrix A (m x n)
    @param theTolerance for rank determination (relative to largest singular value)
    @return SVD decomposition result
    """

def SolveSVD(theA: nanoocp.math.math_Matrix, theB: nanoocp.math.math_Vector, theTolerance: float = 1e-06) -> nanoocp.MathUtils.LinearResult:
    """
    Solve linear system Ax = b using SVD decomposition.
    This is particularly useful for ill-conditioned or singular systems.

    For overdetermined systems (m > n), finds the least squares solution.
    For underdetermined systems (m < n), finds the minimum norm solution.

    @param theA coefficient matrix (m x n)
    @param theB right-hand side vector (length m)
    @param theTolerance for singular value threshold
    @return result containing solution vector
    """

def PseudoInverse(theA: nanoocp.math.math_Matrix, theTolerance: float = 1e-06) -> nanoocp.MathUtils.InverseResult:
    """
    Compute pseudo-inverse (Moore-Penrose inverse) of matrix A.
    A^+ = V * diag(1/w) * U^T where singular values below threshold are set to 0.

    Properties:
    - A * A^+ * A = A
    - A^+ * A * A^+ = A^+
    - (A * A^+)^T = A * A^+
    - (A^+ * A)^T = A^+ * A

    @param theA input matrix (m x n)
    @param theTolerance for singular value threshold
    @return result containing pseudo-inverse matrix (n x m)
    """

def ConditionNumber(theA: nanoocp.math.math_Matrix) -> float:
    """
    Compute condition number of matrix using SVD.
    Condition number = sigma_max / sigma_min (ratio of largest to smallest singular value).

    High condition number (> 1e10) indicates ill-conditioned matrix.

    @param theA input matrix
    @return condition number (infinity if matrix is singular)
    """

def NumericalRank(theA: nanoocp.math.math_Matrix, theTolerance: float = 1e-15) -> int:
    """
    Compute numerical rank of matrix using SVD.
    Rank is the number of singular values above the threshold.

    @param theA input matrix
    @param theTolerance relative tolerance for singular values
    @return numerical rank
    """

def QR(theA: nanoocp.math.math_Matrix, theTolerance: float = 1e-20) -> QRResult:
    """
    QR decomposition using Householder reflections: A = Q * R.

    Decomposes an m x n matrix A (m >= n) into:
    - Q: m x m orthogonal matrix (Q^T * Q = I)
    - R: m x n upper triangular matrix

    The Householder method applies orthogonal transformations
    to reduce A to upper triangular form. It is more numerically
    stable than Gram-Schmidt orthogonalization.

    Uses: Least squares problems, orthogonalization, computing
    determinant sign.

    @param theA input matrix A (m x n, m >= n)
    @param theTolerance for rank determination
    @return QR decomposition result
    """

def SolveQR(theA: nanoocp.math.math_Matrix, theB: nanoocp.math.math_Vector, theTolerance: float = 1e-20) -> nanoocp.MathUtils.LinearResult:
    """
    Solve overdetermined system Ax = b using QR decomposition (least squares).

    For m x n system with m > n, finds x that minimizes ||Ax - b||_2.

    Algorithm:
    1. Decompose A = Q * R
    2. Compute c = Q^T * b
    3. Solve R * x = c[1:n] (back substitution)

    @param theA coefficient matrix (m x n, m >= n)
    @param theB right-hand side vector (length m)
    @param theTolerance for singularity detection
    @return result containing least squares solution
    """

def SolveQRMultiple(theA: nanoocp.math.math_Matrix, theB: nanoocp.math.math_Matrix, theTolerance: float = 1e-20) -> nanoocp.MathUtils.LinearMultipleResult:
    """
    Solve multiple right-hand sides using QR decomposition.

    @param theA coefficient matrix (m x n, m >= n)
    @param theB right-hand side matrix (m x p)
    @param theTolerance for singularity detection
    @return result containing solution matrix (n x p)
    """

def Jacobi(theA: nanoocp.math.math_Matrix, theSortDescending: bool = True) -> nanoocp.MathUtils.EigenResult:
    """
    Compute eigenvalues and eigenvectors of a symmetric matrix
    using the Jacobi iterative method.

    The Jacobi method applies a sequence of plane rotations (Givens rotations)
    to diagonalize the symmetric matrix A:
    A' = R^T * A * R
    where R is a rotation that zeroes one off-diagonal element.

    After convergence, A is diagonal with eigenvalues on the diagonal,
    and the accumulated rotations form the eigenvector matrix.

    Properties:
    - Only works for symmetric matrices
    - Eigenvalues are always real for symmetric matrices
    - Eigenvectors are orthonormal
    - Numerically stable

    Complexity: O(n^3) per sweep, typically needs 5-10 sweeps.

    @param theA input symmetric matrix (n x n)
    @param theSortDescending if true, eigenvalues are sorted in descending order
    @return eigenvalue result
    """

def EigenValues(theA: nanoocp.math.math_Matrix, theSortDescending: bool = True) -> nanoocp.MathUtils.EigenResult:
    """
    Compute only eigenvalues of a symmetric matrix (faster).

    Uses the same Jacobi method but may be optimized to not store
    eigenvectors if not needed.

    @param theA input symmetric matrix (n x n)
    @param theSortDescending if true, eigenvalues are sorted in descending order
    @return eigenvalue result (only EigenValues is set)
    """

def SpectralDecomposition(theA: nanoocp.math.math_Matrix) -> nanoocp.MathUtils.EigenResult:
    """
    Compute spectral decomposition A = V * D * V^T.

    For symmetric matrix A, decomposes into:
    - V: orthogonal matrix of eigenvectors (columns)
    - D: diagonal matrix of eigenvalues

    Such that A = V * D * V^T

    @param theA input symmetric matrix (n x n)
    @return eigenvalue result with EigenValues (diagonal of D) and EigenVectors (V)
    """

def MatrixPower(theA: nanoocp.math.math_Matrix, thePower: float) -> nanoocp.math.math_Matrix | None:
    """
    Compute matrix power A^p for symmetric positive semi-definite matrix.

    Uses spectral decomposition: A^p = V * D^p * V^T
    where D^p is the diagonal matrix with eigenvalues raised to power p.

    @param theA input symmetric positive semi-definite matrix
    @param thePower exponent (can be fractional, e.g., 0.5 for sqrt)
    @return A^p matrix
    """

def MatrixSqrt(theA: nanoocp.math.math_Matrix) -> nanoocp.math.math_Matrix | None:
    """
    Compute matrix square root of symmetric positive semi-definite matrix.

    @param theA input symmetric positive semi-definite matrix
    @return sqrt(A) such that sqrt(A) * sqrt(A) = A
    """

def MatrixInvSqrt(theA: nanoocp.math.math_Matrix) -> nanoocp.math.math_Matrix | None:
    """
    Compute matrix inverse square root of symmetric positive definite matrix.

    @param theA input symmetric positive definite matrix
    @return A^(-1/2) such that A^(-1/2) * A * A^(-1/2) = I
    """

def LeastSquares(theA: nanoocp.math.math_Matrix, theB: nanoocp.math.math_Vector, theMethod: LeastSquaresMethod = LeastSquaresMethod.QR, theTolerance: float = 1e-15) -> LeastSquaresResult:
    """
    Solve overdetermined linear least squares: minimize ||Ax - b||_2.

    Given m x n matrix A (m >= n) and m-vector b, finds n-vector x
    that minimizes the 2-norm of the residual r = Ax - b.

    Methods:
    - NormalEquations: Solves A^T*A*x = A^T*b (fastest, may lose precision)
    - QR: Uses Householder QR decomposition (good general choice)
    - SVD: Most robust, handles rank-deficient systems

    @param theA coefficient matrix (m x n, m >= n)
    @param theB right-hand side vector (length m)
    @param theMethod solution method (default: QR)
    @param theTolerance for rank/singularity detection
    @return least squares result
    """

def WeightedLeastSquares(theA: nanoocp.math.math_Matrix, theB: nanoocp.math.math_Vector, theW: nanoocp.math.math_Vector, theMethod: LeastSquaresMethod = LeastSquaresMethod.QR, theTolerance: float = 1e-15) -> LeastSquaresResult:
    """
    Solve weighted least squares: minimize ||W^{1/2}(Ax - b)||_2.

    Equivalent to minimizing sum of w_i * (a_i^T * x - b_i)^2
    where w_i are the weights.

    @param theA coefficient matrix (m x n)
    @param theB right-hand side vector (length m)
    @param theW weight vector (length m, positive values)
    @param theMethod solution method
    @param theTolerance for rank detection
    @return weighted least squares result
    """

def RegularizedLeastSquares(theA: nanoocp.math.math_Matrix, theB: nanoocp.math.math_Vector, theLambda: float, theTolerance: float = 1e-15) -> LeastSquaresResult:
    """
    Solve regularized least squares (Tikhonov/Ridge regression):
    minimize ||Ax - b||_2^2 + lambda*||x||_2^2

    Adds regularization to stabilize ill-conditioned problems.
    The solution is: x = (A^T*A + lambda*I)^{-1} * A^T * b

    @param theA coefficient matrix (m x n)
    @param theB right-hand side vector (length m)
    @param theLambda regularization parameter (>= 0)
    @param theTolerance for singularity detection
    @return regularized least squares result
    """

def OptimalRegularization(theA: nanoocp.math.math_Matrix, theB: nanoocp.math.math_Vector, theLambdaMin: float = 1e-10, theLambdaMax: float = 100.0, theNbPoints: int = 20) -> float:
    """
    Compute optimal regularization parameter using Leave-One-Out Cross-Validation.

    Minimizes the LOO-CV score: sum_i (a_i^T * x_{-i} - b_i)^2
    where x_{-i} is the solution with the i-th observation removed.

    @param theA coefficient matrix
    @param theB right-hand side vector
    @param theLambdaMin minimum lambda to consider
    @param theLambdaMax maximum lambda to consider
    @param theNbPoints number of lambda values to try
    @return optimal regularization parameter
    """

def EigenTridiagonal(theDiagonal: nanoocp.math.math_Vector, theSubdiagonal: nanoocp.math.math_Vector, theMaxIterations: int = 30) -> EigenResult:
    """
    Eigenvalue decomposition of symmetric tridiagonal matrix using QL algorithm.

    The QL algorithm with implicit Wilkinson shifts finds all eigenvalues and
    eigenvectors of a symmetric tridiagonal matrix T = Q * D * Q^T.

    Properties:
    - All eigenvalues are real (matrix is symmetric)
    - Eigenvectors are orthonormal
    - Numerically stable with implicit shifts

    @param theDiagonal diagonal elements of the tridiagonal matrix
    @param theSubdiagonal subdiagonal elements (one less than diagonal)
    @param theMaxIterations maximum iterations per eigenvalue (default 30)
    @return EigenResult containing eigenvalues and eigenvector matrix
    """

def GetEigenVector(theResult: EigenResult, theIndex: int) -> nanoocp.math.math_Vector:
    """
    Get a single eigenvector from the result.

    @param theResult eigenvalue decomposition result
    @param theIndex 1-based index of eigenvector
    @return eigenvector as math_Vector
    """
