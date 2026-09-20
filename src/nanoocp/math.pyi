"""OCCT package math (toolkit TKMath)"""

import enum
from typing import overload

import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard


class math_Status(enum.IntEnum):
    math_OK = 0

    math_TooManyIterations = 1

    math_FunctionError = 2

    math_DirectionSearchError = 3

    math_NotBracketed = 4

class math_DoubleTab:
    @overload
    def __init__(self, theOther: math_DoubleTab) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, theLowerRow: int, theUpperRow: int, theLowerCol: int, theUpperCol: int) -> None:
        """
        Constructor for ranges [theLowerRow..theUpperRow, theLowerCol..theUpperCol]
        """

    def Init(self, theInitValue: float) -> None:
        """Initialize all elements with theInitValue"""

    def Copy(self, theOther: math_DoubleTab) -> None:
        """Copy data to theOther"""

    def IsDeletable(self) -> bool:
        """Returns true if the internal array is deletable (heap-allocated)"""

    def SetLowerRow(self, theLowerRow: int) -> None:
        """Set lower row index"""

    def SetLowerCol(self, theLowerCol: int) -> None:
        """Set lower column index"""

    def LowerRow(self) -> int:
        """Get lower row index"""

    def UpperRow(self) -> int:
        """Get upper row index"""

    def LowerCol(self) -> int:
        """Get lower column index"""

    def UpperCol(self) -> int:
        """Get upper column index"""

    def NbRows(self) -> int:
        """Get number of rows"""

    def NbColumns(self) -> int:
        """Get number of columns"""

    def Value(self, theRowIndex: int, theColIndex: int) -> float:
        """Access element at (theRowIndex, theColIndex)"""

    def __call__(self, theRowIndex: int, theColIndex: int) -> float:
        """Operator() - alias to Value"""

class math_Matrix:
    """
    This class implements the real matrix abstract data type.
    Matrixes can have an arbitrary range which must be defined
    at the declaration and cannot be changed after this declaration
    math_Matrix(-3,5,2,4); //a vector with range [-3..5, 2..4]
    Matrix values may be initialized and
    retrieved using indexes which must lie within the range
    of definition of the matrix.
    Matrix objects follow "value semantics", that is, they
    cannot be shared and are copied through assignment
    Matrices are copied through assignment:
    @code
    math_Matrix M2(1, 9, 1, 3);
    ...
    M2 = M1;
    M1(1) = 2.0;//the matrix M2 will not be modified.
    @endcode
    The exception RangeError is raised when trying to access
    outside the range of a matrix :
    @code
    M1(11, 1)=0.0// --> will raise RangeError.
    @endcode

    The exception DimensionError is raised when the dimensions of
    two matrices or vectors are not compatible.
    @code
    math_Matrix M3(1, 2, 1, 2);
    M3 = M1;   // will raise DimensionError
    M1.Add(M3) // --> will raise DimensionError.
    @endcode
    A Matrix can be constructed with a pointer to "c array".
    It allows to carry the bounds inside the matrix.
    Example :
    @code
    double tab1[10][20];
    double tab2[200];

    math_Matrix A (tab1[0][0], 1, 10, 1, 20);
    math_Matrix B (tab2[0],    1, 10, 1, 20);
    @endcode
    """

    @overload
    def __init__(self, Other: math_Matrix) -> None:
        """
        constructs a matrix for copy in initialization.
        An exception is raised if the matrixes have not the same dimensions.
        """

    @overload
    def __init__(self, LowerRow: int, UpperRow: int, LowerCol: int, UpperCol: int) -> None:
        """
        Constructs a non-initialized matrix of range [LowerRow..UpperRow,
        LowerCol..UpperCol]
        For the constructed matrix:
        -   LowerRow and UpperRow are the indexes of the
        lower and upper bounds of a row, and
        -   LowerCol and UpperCol are the indexes of the
        lower and upper bounds of a column.
        """

    @overload
    def __init__(self, LowerRow: int, UpperRow: int, LowerCol: int, UpperCol: int, InitialValue: float) -> None:
        """
        constructs a non-initialized matrix of range [LowerRow..UpperRow,
        LowerCol..UpperCol]
        whose values are all initialized with the value InitialValue.
        """

    def Init(self, InitialValue: float) -> None:
        """Initialize all the elements of a matrix to InitialValue."""

    def RowNumber(self) -> int:
        """
        Returns the number of rows of this matrix.
        Note that for a matrix A you always have the following relations:
        - A.RowNumber() = A.UpperRow() -   A.LowerRow() + 1
        - A.ColNumber() = A.UpperCol() -   A.LowerCol() + 1
        - the length of a row of A is equal to the number of columns of A,
        - the length of a column of A is equal to the number of
        rows of A.returns the row range of a matrix.
        """

    def ColNumber(self) -> int:
        """
        Returns the number of rows of this matrix.
        Note that for a matrix A you always have the following relations:
        - A.RowNumber() = A.UpperRow() -   A.LowerRow() + 1
        - A.ColNumber() = A.UpperCol() -   A.LowerCol() + 1
        - the length of a row of A is equal to the number of columns of A,
        - the length of a column of A is equal to the number of
        rows of A.returns the row range of a matrix.
        """

    def LowerRow(self) -> int:
        """
        Returns the value of the Lower index of the row
        range of a matrix.
        """

    def UpperRow(self) -> int:
        """
        Returns the Upper index of the row range
        of a matrix.
        """

    def LowerCol(self) -> int:
        """
        Returns the value of the Lower index of the
        column range of a matrix.
        """

    def UpperCol(self) -> int:
        """
        Returns the value of the upper index of the
        column range of a matrix.
        """

    def Determinant(self) -> float:
        """
        Computes the determinant of a matrix.
        An exception is raised if the matrix is not a square matrix.
        """

    def Transpose(self) -> None:
        """
        Transposes a given matrix.
        An exception is raised if the matrix is not a square matrix.
        """

    def Invert(self) -> None:
        """
        Inverts a matrix using Gauss algorithm.
        Exception NotSquare is raised if the matrix is not square.
        Exception SingularMatrix is raised if the matrix is singular.
        """

    @overload
    def Multiply(self, Right: float) -> None:
        """
        Sets this matrix to the product of the matrix Left, and the matrix Right.
        Example
        math_Matrix A (1, 3, 1, 3);
        math_Matrix B (1, 3, 1, 3);
        // A = ... , B = ...
        math_Matrix C (1, 3, 1, 3);
        C.Multiply(A, B);
        Exceptions
        Standard_DimensionError if matrices are of incompatible dimensions, i.e. if:
        -   the number of columns of matrix Left, or the number of
        rows of matrix TLeft is not equal to the number of rows
        of matrix Right, or
        -   the number of rows of matrix Left, or the number of
        columns of matrix TLeft is not equal to the number of
        rows of this matrix, or
        -   the number of columns of matrix Right is not equal to
        the number of columns of this matrix.
        """

    @overload
    def Multiply(self, Left: "math_VectorBase<double>", Right: "math_VectorBase<double>") -> None:
        """
        Computes a matrix as the product of 2 vectors.
        An exception is raised if the dimensions are different.
        <me> = <Left> * <Right>.
        """

    @overload
    def Multiply(self, Left: math_Matrix, Right: math_Matrix) -> None:
        """
        Computes a matrix as the product of 2 matrixes.
        An exception is raised if the dimensions are different.
        """

    @overload
    def Multiply(self, Right: math_Matrix) -> None:
        """
        Returns the product of 2 matrices.
        An exception is raised if the dimensions are different.
        """

    @overload
    def __imul__(self, Right: float) -> math_Matrix: ...

    @overload
    def __imul__(self, Right: math_Matrix) -> math_Matrix: ...

    @overload
    def Multiplied(self, Right: float) -> math_Matrix:
        """
        multiplies all the elements of a matrix by the
        value <Right>.
        """

    @overload
    def Multiplied(self, Right: math_Matrix) -> math_Matrix:
        """
        Returns the product of 2 matrices.
        An exception is raised if the dimensions are different.
        """

    @overload
    def Multiplied(self, Right: "math_VectorBase<double>") -> "math_VectorBase<double>":
        """
        Returns the product of a matrix by a vector.
        An exception is raised if the dimensions are different.
        """

    @overload
    def __mul__(self, Right: float) -> math_Matrix: ...

    @overload
    def __mul__(self, Right: math_Matrix) -> math_Matrix: ...

    @overload
    def __mul__(self, Right: "math_VectorBase<double>") -> "math_VectorBase<double>": ...

    def TMultiplied(self, Right: float) -> math_Matrix:
        """
        Sets this matrix to the product of the
        transposed matrix TLeft, and the matrix Right.
        Example
        math_Matrix A (1, 3, 1, 3);
        math_Matrix B (1, 3, 1, 3);
        // A = ... , B = ...
        math_Matrix C (1, 3, 1, 3);
        C.Multiply(A, B);
        Exceptions
        Standard_DimensionError if matrices are of incompatible dimensions, i.e. if:
        -   the number of columns of matrix Left, or the number of
        rows of matrix TLeft is not equal to the number of rows
        of matrix Right, or
        -   the number of rows of matrix Left, or the number of
        columns of matrix TLeft is not equal to the number of
        rows of this matrix, or
        -   the number of columns of matrix Right is not equal to
        the number of columns of this matrix.
        """

    def Divide(self, Right: float) -> None:
        """
        divides all the elements of a matrix by the value <Right>.
        An exception is raised if <Right> = 0.
        """

    def __itruediv__(self, Right: float) -> math_Matrix: ...

    def Divided(self, Right: float) -> math_Matrix:
        """
        divides all the elements of a matrix by the value <Right>.
        An exception is raised if <Right> = 0.
        """

    def __truediv__(self, Right: float) -> math_Matrix: ...

    @overload
    def Add(self, Right: math_Matrix) -> None:
        """
        adds the matrix <Right> to a matrix.
        An exception is raised if the dimensions are different.
        Warning
        In order to save time when copying matrices, it is
        preferable to use operator += or the function Add
        whenever possible.
        """

    @overload
    def Add(self, Left: math_Matrix, Right: math_Matrix) -> None:
        """
        sets a matrix to the addition of <Left> and <Right>.
        An exception is raised if the dimensions are different.
        """

    def __iadd__(self, Right: math_Matrix) -> math_Matrix: ...

    def Added(self, Right: math_Matrix) -> math_Matrix:
        """
        adds the matrix <Right> to a matrix.
        An exception is raised if the dimensions are different.
        """

    def __add__(self, Right: math_Matrix) -> math_Matrix: ...

    @overload
    def Subtract(self, Right: math_Matrix) -> None:
        """
        Subtracts the matrix <Right> from <me>.
        An exception is raised if the dimensions are different.
        Warning
        In order to avoid time-consuming copying of matrices, it
        is preferable to use operator -= or the function
        Subtract whenever possible.
        """

    @overload
    def Subtract(self, Left: math_Matrix, Right: math_Matrix) -> None:
        """
        Sets a matrix to the Subtraction of the matrix <Right>
        from the matrix <Left>.
        An exception is raised if the dimensions are different.
        """

    def __isub__(self, Right: math_Matrix) -> math_Matrix: ...

    def Subtracted(self, Right: math_Matrix) -> math_Matrix:
        """
        Returns the result of the subtraction of <Right> from <me>.
        An exception is raised if the dimensions are different.
        """

    def __sub__(self, Right: math_Matrix) -> math_Matrix: ...

    def Set(self, I1: int, I2: int, J1: int, J2: int, M: math_Matrix) -> None:
        """
        Sets the values of this matrix,
        -   from index I1 to index I2 on the row dimension, and
        -   from index J1 to index J2 on the column dimension,
        to those of matrix M.
        Exceptions
        Standard_DimensionError if:
        -   I1 is less than the index of the lower row bound of this matrix, or
        -   I2 is greater than the index of the upper row bound of this matrix, or
        -   J1 is less than the index of the lower column bound of this matrix, or
        -   J2 is greater than the index of the upper column bound of this matrix, or
        -   I2 - I1 + 1 is not equal to the number of rows of matrix M, or
        -   J2 - J1 + 1 is not equal to the number of columns of matrix M.
        """

    def SetRow(self, Row: int, V: "math_VectorBase<double>") -> None:
        """
        Sets the row of index Row of a matrix to the vector <V>.
        An exception is raised if the dimensions are different.
        An exception is raises if <Row> is inferior to the lower
        row of the matrix or <Row> is superior to the upper row.
        """

    def SetCol(self, Col: int, V: "math_VectorBase<double>") -> None:
        """
        Sets the column of index Col of a matrix to the vector <V>.
        An exception is raised if the dimensions are different.
        An exception is raises if <Col> is inferior to the lower
        column of the matrix or <Col> is superior to the upper
        column.
        """

    def SetDiag(self, Value: float) -> None:
        """
        Sets the diagonal of a matrix to the value <Value>.
        An exception is raised if the matrix is not square.
        """

    def Row(self, Row: int) -> "math_VectorBase<double>":
        """Returns the row of index Row of a matrix."""

    def Col(self, Col: int) -> "math_VectorBase<double>":
        """Returns the column of index <Col> of a matrix."""

    def SwapRow(self, Row1: int, Row2: int) -> None:
        """
        Swaps the rows of index Row1 and Row2.
        An exception is raised if <Row1> or <Row2> is out of range.
        """

    def SwapCol(self, Col1: int, Col2: int) -> None:
        """
        Swaps the columns of index <Col1> and <Col2>.
        An exception is raised if <Col1> or <Col2> is out of range.
        """

    def Transposed(self) -> math_Matrix:
        """
        Teturns the transposed of a matrix.
        An exception is raised if the matrix is not a square matrix.
        """

    def Inverse(self) -> math_Matrix:
        """
        Returns the inverse of a matrix.
        Exception NotSquare is raised if the matrix is not square.
        Exception SingularMatrix is raised if the matrix is singular.
        """

    @overload
    def TMultiply(self, Right: math_Matrix) -> math_Matrix:
        """
        Returns the product of the transpose of a matrix with
        the matrix <Right>.
        An exception is raised if the dimensions are different.
        """

    @overload
    def TMultiply(self, TLeft: math_Matrix, Right: math_Matrix) -> None:
        """
        Computes a matrix to the product of the transpose of
        the matrix <TLeft> with the matrix <Right>.
        An exception is raised if the dimensions are different.
        """

    def Value(self, Row: int, Col: int) -> float:
        """
        Accesses the value of index <Row>
        and <Col> of a matrix.
        An exception is raised if <Row> and <Col> are not
        in the correct range.
        """

    def __call__(self, Row: int, Col: int) -> float: ...

    def Initialized(self, Other: math_Matrix) -> math_Matrix:
        """
        Matrixes are copied through assignment.
        An exception is raised if the dimensions are different.
        """

    def Opposite(self) -> math_Matrix:
        """
        Returns the opposite of a matrix.
        An exception is raised if the dimensions are different.
        """

    def __neg__(self) -> math_Matrix: ...

class math_NotSquare(nanoocp.Standard.Standard_DimensionError):
    pass

class math:
    def __init__(self) -> None: ...

    @staticmethod
    def GaussPointsMax() -> int: ...

    @staticmethod
    def GaussPoints(Index: int, Points: "math_VectorBase<double>") -> None: ...

    @staticmethod
    def GaussWeights(Index: int, Weights: "math_VectorBase<double>") -> None: ...

    @staticmethod
    def KronrodPointsMax() -> int:
        """
        Returns the maximal number of points for that the values
        are stored in the table. If the number is greater then
        KronrodPointsMax, the points will be computed.
        """

    @staticmethod
    def OrderedGaussPointsAndWeights(Index: int, Points: "math_VectorBase<double>", Weights: "math_VectorBase<double>") -> bool:
        """
        Returns a vector of Gauss points and a vector of their weights.
        The difference with the
        method GaussPoints is the following:
        - the points are returned in increasing order.
        - if Index is greater then GaussPointsMax, the points are
        computed.
        Returns true if Index is positive, Points' and Weights'
        length is equal to Index, Points and Weights are successfully computed.
        """

    @staticmethod
    def KronrodPointsAndWeights(Index: int, Points: "math_VectorBase<double>", Weights: "math_VectorBase<double>") -> bool:
        """
        Returns a vector of Kronrod points and a vector of their
        weights for Gauss-Kronrod computation method.
        Index should be odd and greater then or equal to 3,
        as the number of Kronrod points is equal to 2*N + 1,
        where N is a number of Gauss points. Points and Weights should
        have the size equal to Index. Each even element of Points
        represents a Gauss point value of N-th Gauss quadrature.
        The values from Index equal to 3 to 123 are stored in a
        table (see the file math_Kronrod.cxx). If Index is greater,
        then points and weights will be computed. Returns true
        if Index is odd, it is equal to the size of Points and Weights
        and the computation of Points and Weights is performed successfully.
        Otherwise this method returns false.
        """

class math_BFGS:
    """
    This class implements the Broyden-Fletcher-Goldfarb-Shanno variant of
    Davidson-Fletcher-Powell minimization algorithm of a function of
    multiple variables.Knowledge of the function's gradient is required.

    It is possible to solve conditional optimization problem on hyperparallelepiped.
    Method SetBoundary is used to define hyperparallelepiped borders. With boundaries
    defined, the algorithm will not make evaluations of the function outside of the
    borders.
    """

    def __init__(self, NbVariables: int, Tolerance: float = 1e-08, NbIterations: int = 200, ZEPS: float = 1e-12) -> None:
        """
        Initializes the computation of the minimum of a function with
        NbVariables.
        Tolerance, ZEPS and NbIterations are described in the method Perform.
        Warning:
        A call to the Perform method must be made after this
        initialization to effectively compute the minimum of the
        function F.
        """

    def SetBoundary(self, theLeftBorder: "math_VectorBase<double>", theRightBorder: "math_VectorBase<double>") -> None:
        """
        Set boundaries for conditional optimization.
        The expected indices range of vectors is [1, NbVariables].
        """

    def Perform(self, F: math_MultipleVarFunctionWithGradient, StartingPoint: "math_VectorBase<double>") -> None:
        """
        Given the starting point StartingPoint,
        minimization is done on the function F.
        The solution F = Fi is found when :
        2.0 * abs(Fi - Fi-1) <= Tolerance * (abs(Fi) + abs(Fi-1) + ZEPS).
        Tolerance, ZEPS and maximum number of iterations are given
        in the constructor.
        """

    def IsSolutionReached(self, F: math_MultipleVarFunctionWithGradient) -> bool:
        """
        This method is called at the end of each iteration to check if the
        solution is found.
        It can be redefined in a sub-class to implement a specific test to
        stop the iterations.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    @overload
    def Location(self) -> "math_VectorBase<double>":
        """
        returns the location vector of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    @overload
    def Location(self, Loc: "math_VectorBase<double>") -> None:
        """
        outputs the location vector of the minimum in Loc.
        Exception NotDone is raised if the minimum was not found.
        Exception DimensionError is raised if the range of Loc is not
        equal to the range of the StartingPoint.
        """

    def Minimum(self) -> float:
        """
        returns the value of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    @overload
    def Gradient(self) -> "math_VectorBase<double>":
        """
        Returns the gradient vector at the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    @overload
    def Gradient(self, Grad: "math_VectorBase<double>") -> None:
        """
        Returns the value of the gradient vector at the minimum in Grad.
        Exception NotDone is raised if the minimum was not found.
        Exception DimensionError is raised if the range of Grad is not
        equal to the range of the StartingPoint.
        """

    def NbIterations(self) -> int:
        """
        Returns the number of iterations really done in the
        calculation of the minimum.
        The exception NotDone is raised if the minimum was not found.
        """

class math_BissecNewton:
    """
    This class implements a combination of Newton-Raphson and bissection
    methods to find the root of the function between two bounds.
    Knowledge of the derivative is required.
    """

    def __init__(self, theXTolerance: float) -> None:
        """
        Constructor.
        @param theXTolerance - algorithm tolerance.
        """

    def Perform(self, F: math_FunctionWithDerivative, Bound1: float, Bound2: float, NbIterations: int = 100) -> None:
        """
        A combination of Newton-Raphson and bissection methods is done to find
        the root of the function F between the bounds Bound1 and Bound2
        on the function F.
        The tolerance required on the root is given by TolX.
        The solution is found when:
        abs(Xi - Xi-1) <= TolX and F(Xi) * F(Xi-1) <= 0
        The maximum number of iterations allowed is given by NbIterations.
        """

    def IsSolutionReached(self, theFunction: math_FunctionWithDerivative) -> bool:
        """
        This method is called at the end of each iteration to check if the
        solution has been found.
        It can be redefined in a sub-class to implement a specific test to
        stop the iterations.
        """

    def IsDone(self) -> bool:
        """Tests is the root has been successfully found."""

    def Root(self) -> float:
        """
        returns the value of the root.
        Exception NotDone is raised if the minimum was not found.
        """

    def Derivative(self) -> float:
        """
        returns the value of the derivative at the root.
        Exception NotDone is raised if the minimum was not found.
        """

    def Value(self) -> float:
        """
        returns the value of the function at the root.
        Exception NotDone is raised if the minimum was not found.
        """

class math_BracketedRoot:
    """
    This class implements the Brent method to find the root of a function
    located within two bounds. No knowledge of the derivative is required.
    """

    def __init__(self, F: math_Function, Bound1: float, Bound2: float, Tolerance: float, NbIterations: int = 100, ZEPS: float = 1e-12) -> None:
        """
        The Brent method is used to find the root of the function F between
        the bounds Bound1 and Bound2 on the function F.
        If F(Bound1)*F(Bound2) >0 the Brent method fails.
        The tolerance required for the root is given by Tolerance.
        The solution is found when :
        abs(Xi - Xi-1) <= Tolerance;
        The maximum number of iterations allowed is given by NbIterations.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def Root(self) -> float:
        """
        returns the value of the root.
        Exception NotDone is raised if the minimum was not found.
        """

    def Value(self) -> float:
        """
        returns the value of the function at the root.
        Exception NotDone is raised if the minimum was not found.
        """

    def NbIterations(self) -> int:
        """
        returns the number of iterations really done during the
        computation of the Root.
        Exception NotDone is raised if the minimum was not found.
        """

class math_BracketMinimum:
    """
    Given two distinct initial points, BracketMinimum
    implements the computation of three points (a, b, c) which
    bracket the minimum of the function and verify A less than
    B, B less than C and F(B) less than F(A), F(B) less than F(C).

    The algorithm supports conditional optimization. By default no limits are
    applied to the parameter change. The method SetLimits defines the allowed range.
    If no minimum is found in limits then IsDone() will return false. The user
    is in charge of providing A and B to be in limits.
    """

    @overload
    def __init__(self, A: float, B: float) -> None:
        """
        Constructor preparing A and B parameters only. It does not perform the job.
        """

    @overload
    def __init__(self, F: math_Function, A: float, B: float) -> None:
        """
        Given two initial values this class computes a
        bracketing triplet of abscissae Ax, Bx, Cx
        (such that Bx is between Ax and Cx, F(Bx) is
        less than both F(Bx) and F(Cx)) the Brent minimization is done
        on the function F.
        """

    @overload
    def __init__(self, F: math_Function, A: float, B: float, FA: float) -> None:
        """
        Given two initial values this class computes a
        bracketing triplet of abscissae Ax, Bx, Cx
        (such that Bx is between Ax and Cx, F(Bx) is
        less than both F(Bx) and F(Cx)) the Brent minimization is done
        on the function F.
        This constructor has to be used if F(A) is known.
        """

    @overload
    def __init__(self, F: math_Function, A: float, B: float, FA: float, FB: float) -> None:
        """
        Given two initial values this class computes a
        bracketing triplet of abscissae Ax, Bx, Cx
        (such that Bx is between Ax and Cx, F(Bx) is
        less than both F(Bx) and F(Cx)) the Brent minimization is done
        on the function F.
        This constructor has to be used if F(A) and F(B) are known.
        """

    def SetLimits(self, theLeft: float, theRight: float) -> None:
        """
        Set limits of the parameter. By default no limits are applied to the parameter change.
        If no minimum is found in limits then IsDone() will return false. The user
        is in charge of providing A and B to be in limits.
        """

    def SetFA(self, theValue: float) -> None:
        """Set function value at A"""

    def SetFB(self, theValue: float) -> None:
        """Set function value at B"""

    def Perform(self, F: math_Function) -> None:
        """
        The method performing the job. It is called automatically by constructors with the function.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def Values(self) -> tuple[float, float, float]:
        """
        Returns the bracketed triplet of abscissae.
        Exceptions
        StdFail_NotDone if the algorithm fails (and IsDone returns false).
        """

    def FunctionValues(self) -> tuple[float, float, float]:
        """
        returns the bracketed triplet function values.
        Exceptions
        StdFail_NotDone if the algorithm fails (and IsDone returns false).
        """

class math_BrentMinimum:
    """
    This class implements the Brent's method to find the minimum of
    a function of a single variable.
    No knowledge of the derivative is required.
    """

    @overload
    def __init__(self, TolX: float, NbIterations: int = 100, ZEPS: float = 1e-12) -> None:
        """
        This constructor should be used in a sub-class to initialize
        correctly all the fields of this class.
        """

    @overload
    def __init__(self, TolX: float, Fbx: float, NbIterations: int = 100, ZEPS: float = 1e-12) -> None:
        """
        This constructor should be used in a sub-class to initialize
        correctly all the fields of this class.
        It has to be used if F(Bx) is known.
        """

    def Perform(self, F: math_Function, Ax: float, Bx: float, Cx: float) -> None:
        """
        Brent minimization is performed on function F from a given
        bracketing triplet of abscissas Ax, Bx, Cx (such that Bx is
        between Ax and Cx, F(Bx) is less than both F(Bx) and F(Cx))
        The solution is found when: abs(Xi - Xi-1) <= TolX * abs(Xi) + ZEPS;
        """

    def IsSolutionReached(self, theFunction: math_Function) -> bool:
        """
        This method is called at the end of each iteration to check if the
        solution is found.
        It can be redefined in a sub-class to implement a specific test to
        stop the iterations.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def Location(self) -> float:
        """
        returns the location value of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    def Minimum(self) -> float:
        """
        returns the value of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    def NbIterations(self) -> int:
        """
        returns the number of iterations really done during the
        computation of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

class math_BullardGenerator:
    """
    Fast random number generator (the algorithm proposed by Ian C. Bullard).
    """

    def __init__(self, theSeed: int = 1) -> None:
        """Creates new Xorshift 64-bit RNG."""

    def SetSeed(self, theSeed: int = 1) -> None:
        """Setup new seed / reset defaults."""

    def NextInt(self) -> int:
        """Generates new 64-bit integer value."""

    def NextReal(self) -> float:
        """Generates new floating-point value."""

class math_ComputeGaussPointsAndWeights:
    def __init__(self, Number: int) -> None: ...

    def IsDone(self) -> bool: ...

    def Points(self) -> "math_VectorBase<double>": ...

    def Weights(self) -> "math_VectorBase<double>": ...

class math_ComputeKronrodPointsAndWeights:
    def __init__(self, Number: int) -> None: ...

    def IsDone(self) -> bool: ...

    def Points(self) -> "math_VectorBase<double>": ...

    def Weights(self) -> "math_VectorBase<double>": ...

class math_Crout:
    """
    This class implements the Crout algorithm used to solve a
    system A*X = B where A is a symmetric matrix. It can be used to
    invert a symmetric matrix.
    This algorithm is similar to Gauss but is faster than Gauss.
    Only the inferior triangle of A and the diagonal can be given.
    """

    def __init__(self, A: math_Matrix, MinPivot: float = 1e-20) -> None:
        """
        Given an input matrix A, this algorithm inverts A by the
        Crout algorithm. The user can give only the inferior
        triangle for the implementation.
        A can be decomposed like this:
        A = L * D * T(L) where L is triangular inferior and D is
        diagonal.
        If one element of A is less than MinPivot, A is
        considered as singular.
        Exception NotSquare is raised if A is not a square matrix.
        """

    def IsDone(self) -> bool:
        """Returns True if all has been correctly done."""

    def Solve(self, B: "math_VectorBase<double>", X: "math_VectorBase<double>") -> None:
        """
        Given an input vector <B>, this routine returns the
        solution of the set of linear equations A . X = B.
        Exception NotDone is raised if the decomposition was not
        done successfully.
        Exception DimensionError is raised if the range of B is
        not equal to the rowrange of A.
        """

    def Inverse(self) -> math_Matrix:
        """
        returns the inverse matrix of A. Only the inferior
        triangle is returned.
        Exception NotDone is raised if NotDone.
        """

    def Invert(self, Inv: math_Matrix) -> None:
        """
        returns in Inv the inverse matrix of A. Only the inferior
        triangle is returned.
        Exception NotDone is raised if NotDone.
        """

    def Determinant(self) -> float:
        """
        Returns the value of the determinant of the previously LU
        decomposed matrix A. Zero is returned if the matrix A is considered as singular.
        Exceptions
        StdFail_NotDone if the algorithm fails (and IsDone returns false).
        """

class math_DirectPolynomialRoots:
    """
    This class implements the calculation of all the real roots of a real
    polynomial of degree <= 4 using direct algebraic methods. The implementation
    uses Ferrari's method for quartics, Cardano's formula for cubics, and
    numerically stable algorithms for quadratics and linear equations.

    Key features:
    - Robust numerical algorithms with coefficient scaling
    - Newton-Raphson root refinement for improved accuracy
    - Proper handling of degenerate and edge cases
    - Multiple root detection and infinite solution handling
    - Scientific reference ordering for deterministic results

    Once found, all roots are polished using the Newton-Raphson method
    to achieve maximum numerical precision.
    """

    @overload
    def __init__(self, theA: float, theB: float) -> None:
        """
        Computes the real root of the linear equation Ax + B = 0.

        Handles all cases:
        - A != 0: unique solution x = -B/A
        - A = 0, B != 0: no solution (inconsistent)
        - A = 0, B = 0: infinite solutions (identity)

        @param theA coefficient of x term
        @param theB constant term
        """

    @overload
    def __init__(self, theA: float, theB: float, theC: float) -> None:
        """
        Computes all the real roots of the quadratic polynomial
        Ax^2 + Bx + C = 0 using numerically stable formulas.

        The algorithm avoids catastrophic cancellation by using:
        - Discriminant with error bounds: Delta = B^2 - 4AC
        - Stable root formulas based on sign of B
        - Newton-Raphson refinement for improved accuracy

        @param theA coefficient of x^2 term
        @param theB coefficient of x term
        @param theC constant term
        """

    @overload
    def __init__(self, theA: float, theB: float, theC: float, theD: float) -> None:
        """
        Computes all the real roots of the cubic polynomial
        Ax^3 + Bx^2 + Cx + D = 0 using Cardano's method with Vieta substitution.

        The algorithm:
        1. Transforms to depressed cubic t^3 + Pt + Q = 0
        2. Computes discriminant Delta = -4P^3/27 - Q^2/4
        3. Uses trigonometric method for Delta < 0 (three real roots)
        4. Uses Cardano's formula for Delta > 0 (one real root)
        5. Handles multiple roots when Delta = 0
        6. Applies Newton-Raphson refinement

        @param theA coefficient of x^3 term
        @param theB coefficient of x^2 term
        @param theC coefficient of x term
        @param theD constant term
        """

    @overload
    def __init__(self, theA: float, theB: float, theC: float, theD: float, theE: float) -> None:
        """
        Computes all the real roots of the quartic polynomial
        Ax^4 + Bx^3 + Cx^2 + Dx + E = 0 using Ferrari's method.

        The algorithm:
        1. Checks for degree reduction (A ~= 0)
        2. Normalizes and scales coefficients for numerical stability
        3. Solves Ferrari's resolvent cubic equation
        4. Factors quartic into two quadratic equations
        5. Solves both quadratics independently
        6. Refines all roots using Newton-Raphson method

        @param theA coefficient of x^4 term
        @param theB coefficient of x^3 term
        @param theC coefficient of x^2 term
        @param theD coefficient of x term
        @param theE constant term
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        Computations may fail due to numerical issues or overflow conditions.
        """

    def InfiniteRoots(self) -> bool:
        """
        Returns true if there is an infinity of roots, otherwise returns false.
        This occurs only for the degenerate linear case 0*x + 0 = 0.
        """

    def NbSolutions(self) -> int:
        """
        Returns the number of distinct real roots found.
        An exception is raised if there are an infinity of roots.
        For multiple roots, this counts each root according to its multiplicity.
        """

    def Value(self, theIndex: int) -> float:
        """
        Returns the value of the Nth root in default ordering.
        The default ordering may vary depending on the algorithm used.
        An exception is raised if there are an infinity of roots.
        Exception RangeError is raised if theIndex is < 1
        or theIndex > NbSolutions.

        @param theIndex root index (1-based)
        @return root value
        """

class math_EigenValuesSearcher:
    """
    This class finds eigenvalues and eigenvectors of real symmetric tridiagonal matrices.

    The implementation uses the QR algorithm with implicit shifts for numerical stability.
    All computed eigenvalues are real (since the matrix is symmetric), and eigenvectors
    are orthonormal. The class handles the complete eigendecomposition:
    A * V = V * D, where A is the input matrix, V contains eigenvectors as columns,
    and D is diagonal with eigenvalues.

    Key features:
    - Robust QR algorithm implementation
    - Numerical stability through implicit shifts
    - Complete eigenvalue/eigenvector computation
    - Proper handling of degenerate cases
    """

    def __init__(self, theDiagonal: nanoocp.NCollection.NCollection_Array1__double, theSubdiagonal: nanoocp.NCollection.NCollection_Array1__double) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns true if computation is performed successfully.
        Computation may fail due to numerical issues or invalid input.
        """

    def Dimension(self) -> int:
        """Returns the dimension of the tridiagonal matrix."""

    def EigenValue(self, theIndex: int) -> float:
        """
        Returns the specified eigenvalue.
        Eigenvalues are returned in the order they were computed by the algorithm,
        which may not be sorted. Use sorting if ordered eigenvalues are needed.

        @param theIndex index of the desired eigenvalue (1-based indexing)
        @return the eigenvalue at the specified index
        """

    def EigenVector(self, theIndex: int) -> "math_VectorBase<double>":
        """
        Returns the specified eigenvector.
        The returned eigenvector is normalized and orthogonal to all other eigenvectors.
        The eigenvector satisfies: A * v = lambda * v, where A is the original matrix,
        v is the eigenvector, and lambda is the corresponding eigenvalue.

        @param theIndex index of the desired eigenvector (1-based indexing)
        @return the normalized eigenvector corresponding to EigenValue(theIndex)
        """

class math_FRPR:
    """
    this class implements the Fletcher-Reeves-Polak_Ribiere minimization
    algorithm of a function of multiple variables.
    Knowledge of the function's gradient is required.
    """

    def __init__(self, theFunction: math_MultipleVarFunctionWithGradient, theTolerance: float, theNbIterations: int = 200, theZEPS: float = 1e-12) -> None:
        """
        Initializes the computation of the minimum of F.
        Warning: constructor does not perform computations.
        """

    def Perform(self, theFunction: math_MultipleVarFunctionWithGradient, theStartingPoint: "math_VectorBase<double>") -> None:
        """
        The solution F = Fi is found when
        2.0 * abs(Fi - Fi-1) <= Tolerance * (abs(Fi) + abs(Fi-1) + ZEPS).
        """

    def IsSolutionReached(self, theFunction: math_MultipleVarFunctionWithGradient) -> bool:
        """
        The solution F = Fi is found when:
        2.0 * abs(Fi - Fi-1) <= Tolerance * (abs(Fi) + abs(Fi-1)) + ZEPS.
        The maximum number of iterations allowed is given by NbIterations.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    @overload
    def Location(self) -> "math_VectorBase<double>":
        """
        returns the location vector of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    @overload
    def Location(self, Loc: "math_VectorBase<double>") -> None:
        """
        outputs the location vector of the minimum in Loc.
        Exception NotDone is raised if the minimum was not found.
        Exception DimensionError is raised if the range of Loc is not
        equal to the range of the StartingPoint.
        """

    def Minimum(self) -> float:
        """
        returns the value of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    @overload
    def Gradient(self) -> "math_VectorBase<double>":
        """
        returns the gradient vector at the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    @overload
    def Gradient(self, Grad: "math_VectorBase<double>") -> None:
        """
        outputs the gradient vector at the minimum in Grad.
        Exception NotDone is raised if the minimum was not found.
        Exception DimensionError is raised if the range of Grad is not
        equal to the range of the StartingPoint.
        """

    def NbIterations(self) -> int:
        """
        returns the number of iterations really done during the
        computation of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

class math_Function:
    """
    This abstract class describes the virtual functions
    associated with a Function of a single variable.
    """

    def Value(self, X: float) -> tuple[bool, float]:
        """
        Computes the value of the function <F> for a given value of
        variable <X>.
        returns True if the computation was done successfully,
        False otherwise.
        """

    def GetStateNumber(self) -> int:
        """
        returns the state of the function corresponding to the
        latest call of any methods associated with the function.
        This function is called by each of the algorithms
        described later which defined the function Integer
        Algorithm::StateNumber(). The algorithm has the
        responsibility to call this function when it has found
        a solution (i.e. a root or a minimum) and has to maintain
        the association between the solution found and this
        StateNumber.
        Byu default, this method returns 0 (which means for the
        algorithm: no state has been saved). It is the
        responsibility of the programmer to decide if he needs
        to save the current state of the function and to return
        an Integer that allows retrieval of the state.
        """

class math_FunctionAllRoots:
    """
    This algorithm uses a sample of the function to find
    all intervals on which the function is null, and afterwards
    uses the FunctionRoots algorithm to find the points
    where the function is null outside the "null intervals".
    Knowledge of the derivative is required.
    """

    def __init__(self, F: math_FunctionWithDerivative, S: math_FunctionSample, EpsX: float, EpsF: float, EpsNul: float) -> None:
        """
        The algorithm uses the sample to find intervals on which
        the function is null. An interval is found if, for at least
        two consecutive points of the sample, Ui and Ui+1, we get
        |F(Ui)|<=EpsNul and |F(Ui+1)|<=EpsNul. The real bounds of
        an interval are computed with the FunctionRoots.
        algorithm.
        Between two intervals, the roots of the function F are
        calculated using the FunctionRoots algorithm.
        """

    def IsDone(self) -> bool:
        """Returns True if the computation has been done successfully."""

    def NbIntervals(self) -> int:
        """
        Returns the number of intervals on which the function
        is Null.
        An exception is raised if IsDone returns False.
        """

    def GetInterval(self, Index: int) -> tuple[float, float]:
        """
        Returns the interval of parameter of range Index.
        An exception is raised if IsDone returns False;
        An exception is raised if Index<=0 or Index >Nbintervals.
        """

    def GetIntervalState(self, Index: int) -> tuple[int, int]:
        """
        returns the State Number associated to the interval Index.
        An exception is raised if IsDone returns False;
        An exception is raised if Index<=0 or Index >Nbintervals.
        """

    def NbPoints(self) -> int:
        """
        returns the number of points where the function is Null.
        An exception is raised if IsDone returns False.
        """

    def GetPoint(self, Index: int) -> float:
        """
        Returns the parameter of the point of range Index.
        An exception is raised if IsDone returns False;
        An exception is raised if Index<=0 or Index >NbPoints.
        """

    def GetPointState(self, Index: int) -> int:
        """
        returns the State Number associated to the point Index.
        An exception is raised if IsDone returns False;
        An exception is raised if Index<=0 or Index >Nbintervals.
        """

class math_FunctionRoot:
    """
    This class implements the computation of a root of a function of
    a single variable which is near an initial guess using a minimization
    algorithm.Knowledge of the derivative is required. The
    algorithm used is the same as in
    """

    @overload
    def __init__(self, F: math_FunctionWithDerivative, Guess: float, Tolerance: float, NbIterations: int = 100) -> None:
        """
        The Newton-Raphson method is done to find the root of the function F
        from the initial guess Guess.The tolerance required on
        the root is given by Tolerance. Iterations are stopped if
        the expected solution does not stay in the range A..B.
        The solution is found when abs(Xi - Xi-1) <= Tolerance;
        The maximum number of iterations allowed is given by NbIterations.
        """

    @overload
    def __init__(self, F: math_FunctionWithDerivative, Guess: float, Tolerance: float, A: float, B: float, NbIterations: int = 100) -> None:
        """
        The Newton-Raphson method is done to find the root of the function F
        from the initial guess Guess.
        The tolerance required on the root is given by Tolerance.
        Iterations are stopped if the expected solution does not stay in the
        range A..B
        The solution is found when abs(Xi - Xi-1) <= Tolerance;
        The maximum number of iterations allowed is given by NbIterations.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def Root(self) -> float:
        """
        returns the value of the root.
        Exception NotDone is raised if the root was not found.
        """

    def Derivative(self) -> float:
        """
        returns the value of the derivative at the root.
        Exception NotDone is raised if the root was not found.
        """

    def Value(self) -> float:
        """
        returns the value of the function at the root.
        Exception NotDone is raised if the root was not found.
        """

    def NbIterations(self) -> int:
        """
        returns the number of iterations really done on the
        computation of the Root.
        Exception NotDone is raised if the root was not found.
        """

class math_FunctionRoots:
    """
    This class implements an algorithm which finds all the real roots of
    a function with derivative within a given range.
    Knowledge of the derivative is required.
    """

    def __init__(self, F: math_FunctionWithDerivative, A: float, B: float, NbSample: int, EpsX: float = 0.0, EpsF: float = 0.0, EpsNull: float = 0.0, K: float = 0.0) -> None:
        """
        Calculates all the real roots of a function F-K within the range
        A..B. without conditions on A and B
        A solution X is found when
        abs(Xi - Xi-1) <= Epsx and abs(F(Xi)-K) <= EpsF.
        The function is considered as null between A and B if
        abs(F-K) <= EpsNull within this range.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def IsAllNull(self) -> bool:
        """
        returns true if the function is considered as null between A and B.
        Exceptions
        StdFail_NotDone if the algorithm fails (and IsDone returns false).
        """

    def NbSolutions(self) -> int:
        """
        Returns the number of solutions found.
        Exceptions
        StdFail_NotDone if the algorithm fails (and IsDone returns false).
        """

    def Value(self, Nieme: int) -> float:
        """
        Returns the Nth value of the root of function F.
        Exceptions
        StdFail_NotDone if the algorithm fails (and IsDone returns false).
        """

    def StateNumber(self, Nieme: int) -> int:
        """
        returns the StateNumber of the Nieme root.
        Exception RangeError is raised if Nieme is < 1
        or Nieme > NbSolutions.
        """

class math_FunctionSample:
    """
    This class gives a default sample (constant difference
    of parameter) for a function defined between
    two bound A,B.
    """

    def __init__(self, A: float, B: float, N: int) -> None: ...

    def Bounds(self) -> tuple[float, float]:
        """Returns the bounds of parameters."""

    def NbPoints(self) -> int:
        """Returns the number of sample points."""

    def GetParameter(self, Index: int) -> float:
        """
        Returns the value of parameter of the point of
        range Index : A + ((Index-1)/(NbPoints-1))*B.
        An exception is raised if Index<=0 or Index>NbPoints.
        """

class math_FunctionSet:
    """
    This abstract class describes the virtual functions associated to
    a set on N Functions of M independent variables.
    """

    def NbVariables(self) -> int:
        """Returns the number of variables of the function."""

    def NbEquations(self) -> int:
        """Returns the number of equations of the function."""

    def Value(self, X: "math_VectorBase<double>", F: "math_VectorBase<double>") -> bool:
        """
        Computes the values <F> of the functions for the
        variable <X>.
        returns True if the computation was done successfully,
        False otherwise.
        """

    def GetStateNumber(self) -> int:
        """
        Returns the state of the function corresponding to the
        latestcall of any methods associated with the function.
        This function is called by each of the algorithms
        described later which define the function Integer
        Algorithm::StateNumber(). The algorithm has the
        responsibility to call this function when it has found
        a solution (i.e. a root or a minimum) and has to maintain
        the association between the solution found and this
        StateNumber.
        Byu default, this method returns 0 (which means for the
        algorithm: no state has been saved). It is the
        responsibility of the programmer to decide if he needs
        to save the current state of the function and to return
        an Integer that allows retrieval of the state.
        """

class math_FunctionSetRoot:
    """
    The math_FunctionSetRoot class calculates the root
    of a set of N functions of M variables (N<M, N=M or N>M). Knowing
    an initial guess of the solution and using a minimization algorithm, a search
    is made in the Newton direction and then in the Gradient direction if there
    is no success in the Newton direction. This algorithm can also be
    used for functions minimization. Knowledge of all the partial
    derivatives (the Jacobian) is required.
    """

    @overload
    def __init__(self, F: math_FunctionSetWithDerivatives, NbIterations: int = 100) -> None:
        """
        is used in a sub-class to initialize correctly all the fields
        of this class.
        The range (1, F.NbVariables()) must be especially
        respected for all vectors and matrix declarations.
        The method SetTolerance must be called after this
        constructor.
        """

    @overload
    def __init__(self, F: math_FunctionSetWithDerivatives, Tolerance: "math_VectorBase<double>", NbIterations: int = 100) -> None:
        """
        is used in a sub-class to initialize correctly all the fields
        of this class.
        The range (1, F.NbVariables()) must be especially
        respected for all vectors and matrix declarations.
        """

    def SetTolerance(self, Tolerance: "math_VectorBase<double>") -> None:
        """Initializes the tolerance values."""

    def IsSolutionReached(self, arg0: math_FunctionSetWithDerivatives) -> bool:
        """
        This routine is called at the end of each iteration
        to check if the solution was found. It can be redefined
        in a sub-class to implement a specific test to stop the iterations.
        In this case, the solution is found when: abs(Xi - Xi-1) <= Tolerance
        for all unknowns.
        """

    @overload
    def Perform(self, theFunction: math_FunctionSetWithDerivatives, theStartingPoint: "math_VectorBase<double>", theStopOnDivergent: bool = False) -> None:
        """
        Improves the root of function from the initial guess point.
        The infinum and supremum may be given to constrain the solution.
        In this case, the solution is found when: abs(Xi - Xi-1)(j) <= Tolerance(j)
        for all unknowns.
        """

    @overload
    def Perform(self, theFunction: math_FunctionSetWithDerivatives, theStartingPoint: "math_VectorBase<double>", theInfBound: "math_VectorBase<double>", theSupBound: "math_VectorBase<double>", theStopOnDivergent: bool = False) -> None:
        """
        Improves the root of function from the initial guess point.
        The infinum and supremum may be given to constrain the solution.
        In this case, the solution is found when: abs(Xi - Xi-1) <= Tolerance
        for all unknowns.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def NbIterations(self) -> int:
        """
        Returns the number of iterations really done
        during the computation of the root.
        Exception NotDone is raised if the root was not found.
        """

    def StateNumber(self) -> int:
        """
        returns the stateNumber (as returned by
        F.GetStateNumber()) associated to the root found.
        """

    @overload
    def Root(self) -> "math_VectorBase<double>":
        """
        Returns the value of the root of function F.
        Exception NotDone is raised if the root was not found.
        """

    @overload
    def Root(self, Root: "math_VectorBase<double>") -> None:
        """
        Outputs the root vector in Root.
        Exception NotDone is raised if the root was not found.
        Exception DimensionError is raised if the range of Root
        is not equal to the range of the StartingPoint.
        """

    @overload
    def Derivative(self) -> math_Matrix:
        """
        Returns the matrix value of the derivative at the root.
        Exception NotDone is raised if the root was not found.
        """

    @overload
    def Derivative(self, Der: math_Matrix) -> None:
        """
        outputs the matrix value of the derivative
        at the root in Der.
        Exception NotDone is raised if the root was not found.
        Exception DimensionError is raised if the column range
        of <Der> is not equal to the range of the startingPoint.
        """

    @overload
    def FunctionSetErrors(self) -> "math_VectorBase<double>":
        """
        returns the vector value of the error done
        on the functions at the root.
        Exception NotDone is raised if the root was not found.
        """

    @overload
    def FunctionSetErrors(self, Err: "math_VectorBase<double>") -> None:
        """
        outputs the vector value of the error done
        on the functions at the root in Err.
        Exception NotDone is raised if the root was not found.
        Exception DimensionError is raised if the range of Err
        is not equal to the range of the StartingPoint.
        """

    def IsDivergent(self) -> bool: ...

class math_FunctionSetWithDerivatives(math_FunctionSet):
    """
    This abstract class describes the virtual functions associated
    with a set of N Functions each of M independent variables.
    """

    def NbVariables(self) -> int:
        """Returns the number of variables of the function."""

    def NbEquations(self) -> int:
        """Returns the number of equations of the function."""

    def Value(self, X: "math_VectorBase<double>", F: "math_VectorBase<double>") -> bool:
        """
        Computes the values <F> of the Functions for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Derivatives(self, X: "math_VectorBase<double>", D: math_Matrix) -> bool:
        """
        Returns the values <D> of the derivatives for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: "math_VectorBase<double>", F: "math_VectorBase<double>", D: math_Matrix) -> bool:
        """
        returns the values <F> of the functions and the derivatives
        <D> for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

class math_FunctionWithDerivative(math_Function):
    """
    This abstract class describes the virtual functions associated with
    a function of a single variable for which the first derivative is
    available.
    """

    def Value(self, X: float) -> tuple[bool, float]:
        """
        Computes the value <F>of the function for the variable <X>.
        Returns True if the calculation were successfully done,
        False otherwise.
        """

    def Derivative(self, X: float) -> tuple[bool, float]:
        """
        Computes the derivative <D> of the function
        for the variable <X>.
        Returns True if the calculation were successfully done,
        False otherwise.
        """

    def Values(self, X: float) -> tuple[bool, float, float]:
        """
        Computes the value <F> and the derivative <D> of the
        function for the variable <X>.
        Returns True if the calculation were successfully done,
        False otherwise.
        """

class math_Gauss:
    """
    This class implements the Gauss LU decomposition (Crout algorithm)
    with partial pivoting (rows interchange) of a square matrix and
    the different possible derived calculation :
    - solution of a set of linear equations.
    - inverse of a matrix.
    - determinant of a matrix.
    """

    def __init__(self, A: math_Matrix, MinPivot: float = 1e-20, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Given an input n X n matrix A this constructor performs its LU
        decomposition with partial pivoting (interchange of rows).
        This LU decomposition is stored internally and may be used to
        do subsequent calculation.
        If the largest pivot found is less than MinPivot the matrix A is
        considered as singular.
        Exception NotSquare is raised if A is not a square matrix.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false
        """

    @overload
    def Solve(self, B: "math_VectorBase<double>", X: "math_VectorBase<double>") -> None:
        """
        Given the input Vector B this routine returns the solution X of the set
        of linear equations A . X = B.
        Exception NotDone is raised if the decomposition of A was not done
        successfully.
        Exception DimensionError is raised if the range of B is not
        equal to the number of rows of A.
        """

    @overload
    def Solve(self, B: "math_VectorBase<double>") -> None:
        """
        Given the input Vector B this routine solves the set of linear
        equations A . X = B. B is replaced by the vector solution X.
        Exception NotDone is raised if the decomposition of A was not done
        successfully.
        Exception DimensionError is raised if the range of B is not
        equal to the number of rows of A.
        """

    def Determinant(self) -> float:
        """
        This routine returns the value of the determinant of the previously LU
        decomposed matrix A.
        Exception NotDone may be raised if the decomposition of A was not done
        successfully, zero is returned if the matrix A was considered as singular.
        """

    def Invert(self, Inv: math_Matrix) -> None:
        """
        This routine outputs Inv the inverse of the previously LU decomposed
        matrix A.
        Exception DimensionError is raised if the ranges of B are not
        equal to the ranges of A.
        """

class math_GaussLeastSquare:
    """
    This class implements the least square solution of a set of
    n linear equations of m unknowns (n >= m) using the gauss LU
    decomposition algorithm.
    This algorithm is more likely subject to numerical instability
    than math_SVD.
    """

    def __init__(self, A: math_Matrix, MinPivot: float = 1e-20) -> None:
        """
        Given an input n X m matrix A with n >= m this constructor
        performs the LU decomposition with partial pivoting
        (interchange of rows) of the matrix AA = A.Transposed() * A;
        This LU decomposition is stored internally and may be used
        to do subsequent calculation.
        If the largest pivot found is less than MinPivot the matrix <A>
        is considered as singular.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.e
        """

    def Solve(self, B: "math_VectorBase<double>", X: "math_VectorBase<double>") -> None:
        """
        Given the input Vector <B> this routine solves the set
        of linear equations A . X = B.
        Exception NotDone is raised if the decomposition of A was
        not done successfully.
        Exception DimensionError is raised if the range of B Inv is
        not equal to the rowrange of A.
        Exception DimensionError is raised if the range of X Inv is
        not equal to the colrange of A.
        """

class math_GaussMultipleIntegration:
    """
    This class implements the integration of a function of multiple
    variables between the parameter bounds Lower[a..b] and Upper[a..b].
    Warning: Each element of Order must be inferior or equal to 61.
    """

    def __init__(self, F: math_MultipleVarFunction, Lower: "math_VectorBase<double>", Upper: "math_VectorBase<double>", Order: "math_VectorBase<int>") -> None:
        """
        The Gauss-Legendre integration with Order = points of
        integration for each unknown, is done on the function F
        between the bounds Lower and Upper.
        """

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def Value(self) -> float:
        """returns the value of the integral."""

class math_GaussSetIntegration:
    """
    This class implements the integration of a set of N
    functions of M variables variables between the
    parameter bounds Lower[a..b] and Upper[a..b].
    Warning: The case M>1 is not implemented.
    """

    def __init__(self, F: math_FunctionSet, Lower: "math_VectorBase<double>", Upper: "math_VectorBase<double>", Order: "math_VectorBase<int>") -> None:
        """
        The Gauss-Legendre integration with Order = points of
        integration for each unknown, is done on the function F
        between the bounds Lower and Upper.
        """

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def Value(self) -> "math_VectorBase<double>":
        """returns the value of the integral."""

class math_GaussSingleIntegration:
    """
    This class implements the integration of a function of a single variable
    between the parameter bounds Lower and Upper.
    Warning: Order must be inferior or equal to 61.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, F: math_Function, Lower: float, Upper: float, Order: int) -> None:
        """
        The Gauss-Legendre integration with N = Order points of integration,
        is done on the function F between the bounds Lower and Upper.
        """

    @overload
    def __init__(self, F: math_Function, Lower: float, Upper: float, Order: int, Tol: float) -> None:
        """
        The Gauss-Legendre integration with N = Order points of integration and
        given tolerance = Tol is done on the function F between the bounds
        Lower and Upper.
        """

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def Value(self) -> float:
        """returns the value of the integral."""

class math_MultipleVarFunction:
    """
    Describes the virtual functions associated with a multiple variable function.
    """

    def NbVariables(self) -> int:
        """Returns the number of variables of the function"""

    def Value(self, X: "math_VectorBase<double>") -> tuple[bool, float]:
        """
        Computes the values of the Functions <F> for the
        variable <X>.
        returns True if the computation was done successfully,
        otherwise false.
        """

    def GetStateNumber(self) -> int:
        """
        return the state of the function corresponding to the latestt
        call of any methods associated to the function. This
        function is called by each of the algorithms described
        later which define the function Integer
        Algorithm::StateNumber(). The algorithm has the
        responsibility to call this function when it has found
        a solution (i.e. a root or a minimum) and has to maintain
        the association between the solution found and this
        StateNumber.
        Byu default, this method returns 0 (which means for the
        algorithm: no state has been saved). It is the
        responsibility of the programmer to decide if he needs
        to save the current state of the function and to return
        an Integer that allows retrieval of the state.
        """

class math_Householder:
    """
    This class implements the least square solution of a set of
    linear equations of m unknowns (n >= m) using the Householder
    method. It solves A.X = B.
    This algorithm has more numerical stability than
    GaussLeastSquare but is longer.
    It must be used if the matrix is singular or nearly singular.
    It is about 16% longer than GaussLeastSquare if there is only
    one member B to solve.
    It is about 30% longer if there are twenty B members to solve.
    """

    @overload
    def __init__(self, A: math_Matrix, B: math_Matrix, EPS: float = 1e-20) -> None: ...

    @overload
    def __init__(self, A: math_Matrix, B: "math_VectorBase<double>", EPS: float = 1e-20) -> None:
        """
        Given an input matrix A with n>= m, given an input vector B
        this constructor performs the least square resolution of
        the set of linear equations A.X = B.
        If a column norm is less than EPS, the resolution can't
        be done.
        Exception DimensionError is raised if the length of B
        is different from the A row number.
        """

    @overload
    def __init__(self, A: math_Matrix, B: math_Matrix, lowerArow: int, upperArow: int, lowerAcol: int, upperAcol: int, EPS: float = 1e-20) -> None:
        """
        Given an input matrix A with n>= m, given an input matrix B
        this constructor performs the least square resolution of
        the set of linear equations A.X = B for each column of B.
        If a column norm is less than EPS, the resolution can't
        be done.
        Exception DimensionError is raised if the row number of B
        is different from the A row number.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def Value(self, sol: "math_VectorBase<double>", Index: int = 1) -> None:
        """
        Given the integer Index, this routine returns the
        corresponding least square solution sol.
        Exception NotDone is raised if the resolution has not be
        done.
        Exception OutOfRange is raised if Index <=0 or
        Index is more than the number of columns of B.
        """

    def AllValues(self) -> math_Matrix:
        """
        Returns the matrix sol of all the solutions of the system
        A.X = B.
        Exception NotDone is raised is the resolution has not be
        done.
        """

class math_Jacobi:
    """
    This class implements the Jacobi method to find the eigenvalues and
    the eigenvectors of a real symmetric square matrix.
    A sort of eigenvalues is done.
    """

    def __init__(self, A: math_Matrix) -> None:
        """
        Given a Real n X n matrix A, this constructor computes all its
        eigenvalues and eigenvectors using the Jacobi method.
        The exception NotSquare is raised if the matrix is not square.
        No verification that the matrix A is really symmetric is done.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def Values(self) -> "math_VectorBase<double>":
        """
        Returns the eigenvalues vector.
        Exception NotDone is raised if calculation is not done successfully.
        """

    def Value(self, Num: int) -> float:
        """
        returns the eigenvalue number Num.
        Eigenvalues are in the range (1..n).
        Exception NotDone is raised if calculation is not done successfully.
        """

    def Vectors(self) -> math_Matrix:
        """
        returns the eigenvectors matrix.
        Exception NotDone is raised if calculation is not done successfully.
        """

    def Vector(self, Num: int, V: "math_VectorBase<double>") -> None:
        """
        Returns the eigenvector V of number Num.
        Eigenvectors are in the range (1..n).
        Exception NotDone is raised if calculation is not done successfully.
        """

class math_KronrodSingleIntegration:
    """
    This class implements the Gauss-Kronrod method of
    integral computation.
    """

    @overload
    def __init__(self) -> None:
        """An empty constructor."""

    @overload
    def __init__(self, theFunction: math_Function, theLower: float, theUpper: float, theNbPnts: int) -> None:
        """
        Constructor. Takes the function, the lower and upper bound
        values, the initial number of Kronrod points
        """

    @overload
    def __init__(self, theFunction: math_Function, theLower: float, theUpper: float, theNbPnts: int, theTolerance: float, theMaxNbIter: int) -> None:
        """
        Constructor. Takes the function, the lower and upper bound
        values, the initial number of Kronrod points, the
        tolerance value and the maximal number of iterations as
        parameters.
        """

    @overload
    def Perform(self, theFunction: math_Function, theLower: float, theUpper: float, theNbPnts: int) -> None:
        """
        Computation of the integral. Takes the function,
        the lower and upper bound values, the initial number
        of Kronrod points, the relative tolerance value and the
        maximal number of iterations as parameters.
        theNbPnts should be odd and greater then or equal to 3.
        """

    @overload
    def Perform(self, theFunction: math_Function, theLower: float, theUpper: float, theNbPnts: int, theTolerance: float, theMaxNbIter: int) -> None:
        """
        Computation of the integral. Takes the function,
        the lower and upper bound values, the initial number
        of Kronrod points, the relative tolerance value and the
        maximal number of iterations as parameters.
        theNbPnts should be odd and greater then or equal to 3.
        Note that theTolerance is relative, i.e. the criterion of
        solution reaching is:
        std::abs(Kronrod - Gauss)/std::abs(Kronrod) < theTolerance.
        theTolerance should be positive.
        """

    def IsDone(self) -> bool:
        """
        Returns true if computation is performed
        successfully.
        """

    def Value(self) -> float:
        """Returns the value of the integral."""

    def ErrorReached(self) -> float:
        """Returns the value of the relative error reached."""

    def AbsolutError(self) -> float:
        """Returns the value of the relative error reached."""

    def OrderReached(self) -> int:
        """
        Returns the number of Kronrod points
        for which the result is computed.
        """

    def NbIterReached(self) -> int:
        """
        Returns the number of iterations
        that were made to compute result.
        """

    @staticmethod
    def GKRule(theFunction: math_Function, theLower: float, theUpper: float, theGaussP: "math_VectorBase<double>", theGaussW: "math_VectorBase<double>", theKronrodP: "math_VectorBase<double>", theKronrodW: "math_VectorBase<double>") -> tuple[bool, float, float]: ...

class math_MultipleVarFunctionWithGradient(math_MultipleVarFunction):
    """
    The abstract class MultipleVarFunctionWithGradient
    describes the virtual functions associated with a multiple variable function.
    """

    def NbVariables(self) -> int:
        """Returns the number of variables of the function."""

    def Value(self, X: "math_VectorBase<double>") -> tuple[bool, float]:
        """
        Computes the values of the Functions <F> for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Gradient(self, X: "math_VectorBase<double>", G: "math_VectorBase<double>") -> bool:
        """
        Computes the gradient <G> of the functions for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: "math_VectorBase<double>", G: "math_VectorBase<double>") -> tuple[bool, float]:
        """
        computes the value <F> and the gradient <G> of the
        functions for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

class math_MultipleVarFunctionWithHessian(math_MultipleVarFunctionWithGradient):
    def NbVariables(self) -> int:
        """returns the number of variables of the function."""

    def Value(self, X: "math_VectorBase<double>") -> tuple[bool, float]:
        """
        computes the values of the Functions <F> for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Gradient(self, X: "math_VectorBase<double>", G: "math_VectorBase<double>") -> bool:
        """
        computes the gradient <G> of the functions for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    @overload
    def Values(self, X: "math_VectorBase<double>", G: "math_VectorBase<double>") -> tuple[bool, float]:
        """
        computes the value <F> and the gradient <G> of the
        functions for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    @overload
    def Values(self, X: "math_VectorBase<double>", G: "math_VectorBase<double>", H: math_Matrix) -> tuple[bool, float]:
        """
        computes the value <F>, the gradient <G> and the
        hessian <H> of the functions for the variable <X>.
        Returns True if the computation was done
        successfully, False otherwise.
        """

class math_NewtonFunctionRoot:
    """
    This class implements the calculation of a root of a function of
    a single variable starting from an initial near guess using the
    Newton algorithm. Knowledge of the derivative is required.
    """

    @overload
    def __init__(self, F: math_FunctionWithDerivative, Guess: float, EpsX: float, EpsF: float, NbIterations: int = 100) -> None:
        """
        The Newton method is done to find the root of the function F
        from the initial guess Guess.
        The tolerance required on the root is given by Tolerance.
        The solution is found when :
        abs(Xi - Xi-1) <= EpsX and abs(F(Xi))<= EpsF
        The maximum number of iterations allowed is given by NbIterations.
        """

    @overload
    def __init__(self, A: float, B: float, EpsX: float, EpsF: float, NbIterations: int = 100) -> None:
        """
        is used in a sub-class to initialize correctly all the fields
        of this class.
        """

    @overload
    def __init__(self, F: math_FunctionWithDerivative, Guess: float, EpsX: float, EpsF: float, A: float, B: float, NbIterations: int = 100) -> None:
        """
        The Newton method is done to find the root of the function F
        from the initial guess Guess.
        The solution must be inside the interval [A, B].
        The tolerance required on the root is given by Tolerance.
        The solution is found when :
        abs(Xi - Xi-1) <= EpsX and abs(F(Xi))<= EpsF
        The maximum number of iterations allowed is given by NbIterations.
        """

    def Perform(self, F: math_FunctionWithDerivative, Guess: float) -> None:
        """is used internally by the constructors."""

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def Root(self) -> float:
        """
        Returns the value of the root of function <F>.
        Exception NotDone is raised if the root was not found.
        """

    def Derivative(self) -> float:
        """
        returns the value of the derivative at the root.
        Exception NotDone is raised if the root was not found.
        """

    def Value(self) -> float:
        """
        returns the value of the function at the root.
        Exception NotDone is raised if the root was not found.
        """

    def NbIterations(self) -> int:
        """
        Returns the number of iterations really done on the
        computation of the Root.
        Exception NotDone is raised if the root was not found.
        """

class math_NewtonFunctionSetRoot:
    """
    This class computes the root of a set of N functions of N variables,
    knowing an initial guess at the solution and using the
    Newton Raphson algorithm. Knowledge of all the partial
    derivatives (Jacobian) is required.
    """

    @overload
    def __init__(self, theFunction: math_FunctionSetWithDerivatives, theFTolerance: float, theNbIterations: int = 100) -> None:
        """
        This constructor should be used in a sub-class to initialize
        correctly all the fields of this class.
        The range (1, F.NbVariables()) must be especially respected for
        all vectors and matrix declarations.
        The method SetTolerance must be called before performing the algorithm.
        """

    @overload
    def __init__(self, theFunction: math_FunctionSetWithDerivatives, theXTolerance: "math_VectorBase<double>", theFTolerance: float, theNbIterations: int = 100) -> None:
        """
        Initialize correctly all the fields of this class.
        The range (1, F.NbVariables()) must be especially respected for
        all vectors and matrix declarations.
        """

    def SetTolerance(self, XTol: "math_VectorBase<double>") -> None:
        """Initializes the tolerance values for the unknowns."""

    @overload
    def Perform(self, theFunction: math_FunctionSetWithDerivatives, theStartingPoint: "math_VectorBase<double>") -> None:
        """
        The Newton method is done to improve the root of the function
        from the initial guess point. The solution is found when:
        abs(Xj - Xj-1)(i) <= XTol(i) and abs(Fi) <= FTol for all i;
        """

    @overload
    def Perform(self, theFunction: math_FunctionSetWithDerivatives, theStartingPoint: "math_VectorBase<double>", theInfBound: "math_VectorBase<double>", theSupBound: "math_VectorBase<double>") -> None:
        """
        The Newton method is done to improve the root of the function
        from the initial guess point. Bounds may be given, to constrain the solution.
        The solution is found when:
        abs(Xj - Xj-1)(i) <= XTol(i) and abs(Fi) <= FTol for all i;
        """

    def IsSolutionReached(self, F: math_FunctionSetWithDerivatives) -> bool:
        """
        This method is called at the end of each iteration to check if the
        solution is found.
        Vectors DeltaX, Fvalues and Jacobian Matrix are consistent with the
        possible solution Vector Sol and can be inspected to decide whether
        the solution is reached or not.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    @overload
    def Root(self) -> "math_VectorBase<double>":
        """
        Returns the value of the root of function F.
        Exceptions
        StdFail_NotDone if the algorithm fails (and IsDone returns false).
        """

    @overload
    def Root(self, Root: "math_VectorBase<double>") -> None:
        """
        outputs the root vector in Root.
        Exception NotDone is raised if the root was not found.
        Exception DimensionError is raised if the range of Root is
        not equal to the range of the StartingPoint.
        """

    @overload
    def Derivative(self) -> math_Matrix:
        """
        Returns the matrix value of the derivative at the root.
        Exception NotDone is raised if the root was not found.
        """

    @overload
    def Derivative(self, Der: math_Matrix) -> None:
        """
        Outputs the matrix value of the derivative at the root in
        Der.
        Exception NotDone is raised if the root was not found.
        Exception DimensionError is raised if the range of Der is
        not equal to the range of the StartingPoint.
        """

    @overload
    def FunctionSetErrors(self) -> "math_VectorBase<double>":
        """
        Returns the vector value of the error done on the
        functions at the root.
        Exception NotDone is raised if the root was not found.
        """

    @overload
    def FunctionSetErrors(self, Err: "math_VectorBase<double>") -> None:
        """
        Outputs the vector value of the error done on the
        functions at the root in Err.
        Exception NotDone is raised if the root was not found.
        Exception DimensionError is raised if the range of Err is
        not equal to the range of the StartingPoint.
        """

    def NbIterations(self) -> int:
        """
        Returns the number of iterations really done
        during the computation of the Root.
        Exception NotDone is raised if the root was not found.
        """

class math_NewtonMinimum:
    def __init__(self, theFunction: math_MultipleVarFunctionWithHessian, theTolerance: float = 1e-07, theNbIterations: int = 40, theConvexity: float = 1e-06, theWithSingularity: bool = True) -> None:
        """
        The tolerance required on the solution is given by Tolerance.
        Iteration are stopped if (!WithSingularity) and H(F(Xi)) is not definite
        positive (if the smaller eigenvalue of H < Convexity)
        or IsConverged() returns True for 2 successives Iterations.
        Warning: This constructor does not perform computation.
        """

    def Perform(self, theFunction: math_MultipleVarFunctionWithHessian, theStartingPoint: "math_VectorBase<double>") -> None:
        """Search the solution."""

    def IsConverged(self) -> bool:
        """
        This method is called at the end of each iteration to check the convergence:
        || Xi+1 - Xi || < Tolerance or || F(Xi+1) - F(Xi)|| < Tolerance * || F(Xi) ||
        It can be redefined in a sub-class to implement a specific test.
        """

    def IsDone(self) -> bool:
        """Tests if an error has occurred."""

    @overload
    def Location(self) -> "math_VectorBase<double>":
        """
        returns the location vector of the minimum.
        Exception NotDone is raised if an error has occurred.
        """

    @overload
    def Location(self, Loc: "math_VectorBase<double>") -> None:
        """
        outputs the location vector of the minimum in Loc.
        Exception NotDone is raised if an error has occurred.
        Exception DimensionError is raised if the range of Loc is not
        equal to the range of the StartingPoint.
        """

    def SetBoundary(self, theLeftBorder: "math_VectorBase<double>", theRightBorder: "math_VectorBase<double>") -> None:
        """Set boundaries."""

    def Minimum(self) -> float:
        """
        returns the value of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    @overload
    def Gradient(self) -> "math_VectorBase<double>":
        """
        returns the gradient vector at the minimum.
        Exception NotDone is raised if an error has occurred.
        The minimum was not found.
        """

    @overload
    def Gradient(self, Grad: "math_VectorBase<double>") -> None:
        """
        outputs the gradient vector at the minimum in Grad.
        Exception NotDone is raised if the minimum was not found.
        Exception DimensionError is raised if the range of Grad is not
        equal to the range of the StartingPoint.
        """

    def NbIterations(self) -> int:
        """
        returns the number of iterations really done in the
        calculation of the minimum.
        The exception NotDone is raised if an error has occurred.
        """

    def GetStatus(self) -> math_Status:
        """
        Returns the Status of computation.
        The exception NotDone is raised if an error has occurred.
        """

class math_Powell:
    """
    This class implements the Powell method to find the minimum of
    function of multiple variables (the gradient does not have to be known).
    """

    def __init__(self, theFunction: math_MultipleVarFunction, theTolerance: float, theNbIterations: int = 200, theZEPS: float = 1e-12) -> None:
        """Constructor. Initialize new entity."""

    def Perform(self, theFunction: math_MultipleVarFunction, theStartingPoint: "math_VectorBase<double>", theStartingDirections: math_Matrix) -> None:
        """
        Computes Powell minimization on the function F given
        theStartingPoint, and an initial matrix theStartingDirection
        whose columns contain the initial set of directions.
        The solution F = Fi is found when:
        2.0 * abs(Fi - Fi-1) =< Tolerance * (abs(Fi) + abs(Fi-1) + ZEPS).
        """

    def IsSolutionReached(self, theFunction: math_MultipleVarFunction) -> bool:
        """
        Solution F = Fi is found when:
        2.0 * abs(Fi - Fi-1) <= Tolerance * (abs(Fi) + abs(Fi-1)) + ZEPS.
        The maximum number of iterations allowed is given by NbIterations.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    @overload
    def Location(self) -> "math_VectorBase<double>":
        """
        returns the location vector of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    @overload
    def Location(self, Loc: "math_VectorBase<double>") -> None:
        """
        outputs the location vector of the minimum in Loc.
        Exception NotDone is raised if the minimum was not found.
        Exception DimensionError is raised if the range of Loc is not
        equal to the range of the StartingPoint.
        """

    def Minimum(self) -> float:
        """
        Returns the value of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    def NbIterations(self) -> int:
        """
        Returns the number of iterations really done during the
        computation of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

class math_PSO:
    """
    In this class implemented variation of Particle Swarm Optimization (PSO) method.
    A. Ismael F. Vaz, L. N. Vicente
    "A particle swarm pattern search method for bound constrained global optimization"

    Algorithm description:
    Init Section:
    At start of computation a number of "particles" are placed in the search space.
    Each particle is assigned a random velocity.

    Computational loop:
    The particles are moved in cycle, simulating some "social" behavior, so that new position of
    a particle on each step depends not only on its velocity and previous path, but also on the
    position of the best particle in the pool and best obtained position for current particle.
    The velocity of the particles is decreased on each step, so that convergence is guaranteed.

    Algorithm output:
    Best point in param space (position of the best particle) and value of objective function.

    Pros:
    One of the fastest algorithms.
    Work over functions with a lot local extremums.
    Does not require calculation of derivatives of the functional.

    Cons:
    Convergence to global minimum not proved, which is a typical drawback for all stochastic
    algorithms. The result depends on random number generator.

    Warning: PSO is effective to walk into optimum surrounding, not to get strict optimum.
    Run local optimization from pso output point.
    Warning: In PSO used fixed seed in RNG, so results are reproducible.
    """

    def __init__(self, theFunc: math_MultipleVarFunction, theLowBorder: "math_VectorBase<double>", theUppBorder: "math_VectorBase<double>", theSteps: "math_VectorBase<double>", theNbParticles: int = 32, theNbIter: int = 100) -> None:
        """
        Constructor.

        @param theFunc defines the objective function. It should exist during all lifetime of class
        instance.
        @param theLowBorder defines lower border of search space.
        @param theUppBorder defines upper border of search space.
        @param theSteps defines steps of regular grid, used for particle generation.
        This parameter used to define stop condition (TerminalVelocity).
        @param theNbParticles defines number of particles.
        @param theNbIter defines maximum number of iterations.
        """

    @overload
    def Perform(self, theSteps: "math_VectorBase<double>", theOutPnt: "math_VectorBase<double>", theNbIter: int = 100) -> float:
        """
        Perform computations, particles array is constructed inside of this function.
        """

    @overload
    def Perform(self, theParticles: math_PSOParticlesPool, theNbParticles: int, theOutPnt: "math_VectorBase<double>", theNbIter: int = 100) -> float:
        """Perform computations with given particles array."""

class PSO_Particle:
    """
    Describes particle pool for using in PSO algorithm.
    Indexes:
    0 <= aDimidx <= myDimensionCount - 1
    """

    def __init__(self) -> None: ...

    def __lt__(self, thePnt: PSO_Particle) -> bool:
        """Compares the particles according to their distances."""

    @property
    def Distance(self) -> float: ...

    @Distance.setter
    def Distance(self, arg: float, /) -> None: ...

    @property
    def BestDistance(self) -> float: ...

    @BestDistance.setter
    def BestDistance(self, arg: float, /) -> None: ...

class math_PSOParticlesPool:
    def __init__(self, theParticlesCount: int, theDimensionCount: int) -> None: ...

    def GetParticle(self, theIdx: int) -> PSO_Particle: ...

    def GetBestParticle(self) -> PSO_Particle: ...

    def GetWorstParticle(self) -> PSO_Particle: ...

class math_SingularMatrix(nanoocp.Standard.Standard_Failure):
    pass

class math_SVD:
    """
    SVD implements the solution of a set of N linear equations
    of M unknowns without condition on N or M. The Singular
    Value Decomposition algorithm is used. For singular or
    nearly singular matrices SVD is a better choice than Gauss
    or GaussLeastSquare.
    """

    def __init__(self, A: math_Matrix) -> None:
        """
        Given as input an n X m matrix A with n < m, n = m or n > m
        this constructor performs the Singular Value Decomposition.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def Solve(self, B: "math_VectorBase<double>", X: "math_VectorBase<double>", Eps: float = 1e-06) -> None:
        """
        Given the input Vector B this routine solves the set of linear
        equations A . X = B.
        Exception NotDone is raised if the decomposition of A was not done
        successfully.
        Exception DimensionError is raised if the range of B is not
        equal to the rowrange of A.
        Exception DimensionError is raised if the range of X is not
        equal to the colrange of A.
        """

    def PseudoInverse(self, Inv: math_Matrix, Eps: float = 1e-06) -> None:
        """
        Computes the inverse Inv of matrix A such as A * Inverse = Identity.
        Exceptions
        StdFail_NotDone if the algorithm fails (and IsDone returns false).
        Standard_DimensionError if the ranges of Inv are
        compatible with the ranges of A.
        """

class math_TrigonometricFunctionRoots:
    """
    This class implements the solutions of the equation
    a*std::cos(x)*std::cos(x) + 2*b*std::cos(x)*Sin(x) + c*std::cos(x) + d*Sin(x) + e
    The degree of this equation can be 4, 3 or 2.
    """

    @overload
    def __init__(self, D: float, E: float, InfBound: float, SupBound: float) -> None:
        """
        Given the two coefficients d and e, it performs
        the resolution of d*sin(x) + e = 0.
        The solutions must be contained in [InfBound, SupBound].
        InfBound and SupBound can be set by default to 0 and 2*PI.
        """

    @overload
    def __init__(self, C: float, D: float, E: float, InfBound: float, SupBound: float) -> None:
        """
        Given the three coefficients c, d and e, it performs
        the resolution of c*std::cos(x) + d*sin(x) + e = 0.
        The solutions must be contained in [InfBound, SupBound].
        InfBound and SupBound can be set by default to 0 and 2*PI.
        """

    @overload
    def __init__(self, A: float, B: float, C: float, D: float, E: float, InfBound: float, SupBound: float) -> None:
        """
        Given coefficients a, b, c, d , e, this constructor
        performs the resolution of the equation above.
        The solutions must be contained in [InfBound, SupBound].
        InfBound and SupBound can be set by default to 0 and 2*PI.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def InfiniteRoots(self) -> bool:
        """
        Returns true if there is an infinity of roots, otherwise returns false.
        """

    def Value(self, Index: int) -> float:
        """
        Returns the solution of range Index.
        An exception is raised if NotDone.
        An exception is raised if Index>NbSolutions.
        An exception is raised if there is an infinity of solutions.
        """

    def NbSolutions(self) -> int:
        """
        Returns the number of solutions found.
        An exception is raised if NotDone.
        An exception is raised if there is an infinity of solutions.
        """

class math_TrigonometricEquationFunction(math_FunctionWithDerivative):
    """
    This is function, which corresponds trigonometric equation
    a*std::cos(x)*std::cos(x) + 2*b*std::cos(x)*Sin(x) + c*std::cos(x) + d*Sin(x) + e = 0
    See class math_TrigonometricFunctionRoots
    """

    def __init__(self, A: float, B: float, C: float, D: float, E: float) -> None: ...

    def Value(self, X: float) -> tuple[bool, float]: ...

    def Derivative(self, X: float) -> tuple[bool, float]: ...

    def Values(self, X: float) -> tuple[bool, float, float]: ...

class math_Uzawa:
    """
    This class implements a system resolution C*X = B with
    an approach solution X0. There are no conditions on the
    number of equations. The algorithm used is the Uzawa
    algorithm. It is possible to have equal or inequal (<)
    equations to solve. The resolution is done with a
    minimization of Norm(X-X0).
    If there are only equal equations, the resolution is directly
    done and is similar to Gauss resolution with an optimisation
    because the matrix is a symmetric matrix.
    (The resolution is done with Crout algorithm)
    """

    @overload
    def __init__(self, Cont: math_Matrix, Secont: "math_VectorBase<double>", StartingPoint: "math_VectorBase<double>", EpsLix: float = 1e-06, EpsLic: float = 1e-06, NbIterations: int = 500) -> None:
        """
        Given an input matrix Cont, two input vectors Secont
        and StartingPoint, it solves Cont*X = Secont (only
        = equations) with a minimization of Norme(X-X0).
        The maximum iterations number allowed is fixed to
        NbIterations.
        The tolerance EpsLic is fixed for the dual variable
        convergence. The tolerance EpsLix is used for the
        convergence of X.
        Exception ConstructionError is raised if the line number
        of Cont is different from the length of Secont.
        """

    @overload
    def __init__(self, Cont: math_Matrix, Secont: "math_VectorBase<double>", StartingPoint: "math_VectorBase<double>", Nci: int, Nce: int, EpsLix: float = 1e-06, EpsLic: float = 1e-06, NbIterations: int = 500) -> None:
        """
        Given an input matrix Cont, two input vectors Secont
        and StartingPoint, it solves Cont*X = Secont (the Nce
        first equations are equal equations and the Nci last
        equations are inequalities <) with a minimization
        of Norme(X-X0).
        The maximum iterations number allowed is fixed to
        NbIterations.
        The tolerance EpsLic is fixed for the dual variable
        convergence. The tolerance EpsLix is used for the
        convergence of X.
        There are no conditions on Nce and Nci.
        Exception ConstructionError is raised if the line number
        of Cont is different from the length of Secont and from
        Nce + Nci.
        """

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def Value(self) -> "math_VectorBase<double>":
        """
        Returns the vector solution of the system above.
        An exception is raised if NotDone.
        """

    def InitialError(self) -> "math_VectorBase<double>":
        """
        Returns the initial error Cont*StartingPoint-Secont.
        An exception is raised if NotDone.
        """

    def Duale(self, V: "math_VectorBase<double>") -> None:
        """returns the duale variables V of the systeme."""

    def Error(self) -> "math_VectorBase<double>":
        """
        Returns the difference between X solution and the
        StartingPoint.
        An exception is raised if NotDone.
        """

    def NbIterations(self) -> int:
        """
        returns the number of iterations really done.
        An exception is raised if NotDone.
        """

    def InverseCont(self) -> math_Matrix:
        """
        returns the inverse matrix of (C * Transposed(C)).
        This result is needed for the computation of the gradient
        when approximating a curve.
        """

class math_ValueAndWeight:
    """Simple container storing two reals: value and weight"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theValue: float, theWeight: float) -> None: ...

    def Value(self) -> float: ...

    def Weight(self) -> float: ...

    def __lt__(self, arg: math_ValueAndWeight, /) -> bool: ...

@overload
def LU_Decompose(a: math_Matrix, indx: "math_VectorBase<int>", d: float, TINY: float = 1e-20, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> int: ...

@overload
def LU_Decompose(a: math_Matrix, indx: "math_VectorBase<int>", d: float, vv: "math_VectorBase<double>", TINY: float = 1e-30, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> int: ...

def LU_Solve(a: math_Matrix, indx: "math_VectorBase<int>", b: "math_VectorBase<double>") -> None: ...

def LU_Invert(a: math_Matrix) -> int: ...

@overload
def SVD_Decompose(a: math_Matrix, w: "math_VectorBase<double>", v: math_Matrix) -> int: ...

@overload
def SVD_Decompose(a: math_Matrix, w: "math_VectorBase<double>", v: math_Matrix, rv1: "math_VectorBase<double>") -> int: ...

def SVD_Solve(u: math_Matrix, w: "math_VectorBase<double>", v: math_Matrix, b: "math_VectorBase<double>", x: "math_VectorBase<double>") -> None: ...

def DACTCL_Decompose(a: "math_VectorBase<double>", indx: "math_VectorBase<int>", MinPivot: float = 1e-20) -> int: ...

def DACTCL_Solve(a: "math_VectorBase<double>", b: "math_VectorBase<double>", indx: "math_VectorBase<int>", MinPivot: float = 1e-20) -> int: ...

def Jacobi(a: math_Matrix, d: "math_VectorBase<double>", v: math_Matrix, nrot: int) -> int: ...
