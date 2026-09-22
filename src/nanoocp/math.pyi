"""OCCT package math (toolkit TKMath)"""

import enum
from typing import overload

import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp


class math_Status(enum.IntEnum):
    math_OK = 0

    math_TooManyIterations = 1

    math_FunctionError = 2

    math_DirectionSearchError = 3

    math_NotBracketed = 4

math_OK: math_Status = math_Status.math_OK

math_TooManyIterations: math_Status = math_Status.math_TooManyIterations

math_FunctionError: math_Status = math_Status.math_FunctionError

math_DirectionSearchError: math_Status = math_Status.math_DirectionSearchError

math_NotBracketed: math_Status = math_Status.math_NotBracketed

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
        """Change element at (theRowIndex, theColIndex)"""

    def SetValue(self, theRowIndex: int, theColIndex: int, theValue: float) -> None:
        """
        Python addition: sets the value Value(theRowIndex, theColIndex) returns by reference in C++.
        """

    def __call__(self, theRowIndex: int, theColIndex: int) -> float:
        """Operator() - alias to ChangeValue"""

    def __getitem__(self, arg: tuple[int, int], /) -> float:
        """Python addition: alias to operator()."""

    def __setitem__(self, arg0: tuple[int, int], arg1: float, /) -> None:
        """
        Python addition: sets the value operator()(theRowIndex, theColIndex) returns by reference in C++.
        """

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
    def Multiply(self, Left: math_Vector, Right: math_Vector) -> None:
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
    def Multiplied(self, Right: math_Vector) -> math_Vector:
        """
        Returns the product of a matrix by a vector.
        An exception is raised if the dimensions are different.
        """

    @overload
    def __mul__(self, Right: float) -> math_Matrix: ...

    @overload
    def __mul__(self, Right: math_Matrix) -> math_Matrix: ...

    @overload
    def __mul__(self, Right: math_Vector) -> math_Vector: ...

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

    def SetRow(self, Row: int, V: math_Vector) -> None:
        """
        Sets the row of index Row of a matrix to the vector <V>.
        An exception is raised if the dimensions are different.
        An exception is raises if <Row> is inferior to the lower
        row of the matrix or <Row> is superior to the upper row.
        """

    def SetCol(self, Col: int, V: math_Vector) -> None:
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

    def Row(self, Row: int) -> math_Vector:
        """Returns the row of index Row of a matrix."""

    def Col(self, Col: int) -> math_Vector:
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
        Accesses (in read or write mode) the value of index <Row>
        and <Col> of a matrix.
        An exception is raised if <Row> and <Col> are not
        in the correct range.
        """

    def SetValue(self, Row: int, Col: int, theValue: float) -> None:
        """
        Python addition: sets the value Value(Row, Col) returns by reference in C++.
        """

    def __call__(self, Row: int, Col: int) -> float: ...

    def __getitem__(self, arg: tuple[int, int], /) -> float:
        """Python addition: alias to operator()."""

    def __setitem__(self, arg0: tuple[int, int], arg1: float, /) -> None:
        """
        Python addition: sets the value operator()(Row, Col) returns by reference in C++.
        """

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

    def Dump(self) -> object:
        """
        Prints information on the current state of the object.
        Is used to redefine the operator <<.
        """

    def __rmul__(self, arg: float, /) -> math_Matrix: ...

class math_NotSquare(nanoocp.Standard.Standard_DimensionError):
    pass

class math_Vector:
    """
    This class implements the real vector abstract data type.
    Vectors can have an arbitrary range which must be defined at
    the declaration and cannot be changed after this declaration.
    @code
    math_VectorBase<TheItemType> V1(-3, 5); // a vector with range [-3..5]
    @endcode

    Vector are copied through assignment:
    @code
    math_VectorBase<TheItemType> V2( 1, 9);
    ....
    V2 = V1;
    V1(1) = 2.0; // the vector V2 will not be modified.
    @endcode

    The Exception RangeError is raised when trying to access outside
    the range of a vector :
    @code
    V1(11) = 0.0 // --> will raise RangeError;
    @endcode

    The Exception DimensionError is raised when the dimensions of two
    vectors are not compatible :
    @code
    math_VectorBase<TheItemType> V3(1, 2);
    V3 = V1;    // --> will raise DimensionError;
    V1.Add(V3)  // --> will raise DimensionError;
    @endcode
    """

    @overload
    def __init__(self, Other: nanoocp.gp.gp_XY) -> None:
        """Constructor for converting gp_XY to math_VectorBase"""

    @overload
    def __init__(self, Other: nanoocp.gp.gp_XYZ) -> None:
        """Constructor for converting gp_XYZ to math_VectorBase"""

    @overload
    def __init__(self, theOther: math_Vector) -> None:
        """Constructs a copy for initialization."""

    @overload
    def __init__(self, theLower: int, theUpper: int) -> None:
        """
        Constructs a non-initialized vector in the range [theLower..theUpper]
        "theLower" and "theUpper" are the indexes of the lower and upper bounds of the constructed
        vector.
        """

    @overload
    def __init__(self, theLower: int, theUpper: int, theInitialValue: float) -> None:
        """
        Constructs a vector in the range [theLower..theUpper]
        whose values are all initialized with the value "theInitialValue\"
        """

    def Init(self, theInitialValue: float) -> None:
        """Initialize all the elements of a vector with "theInitialValue"."""

    def Length(self) -> int:
        """Returns the length of a vector"""

    def Lower(self) -> int:
        """Returns the lower index of the vector"""

    def Upper(self) -> int:
        """Returns the upper index of the vector"""

    def Norm(self) -> float:
        """Returns the value or the square of the norm of this vector."""

    def Norm2(self) -> float:
        """Returns the value of the square of the norm of a vector."""

    def Max(self) -> int:
        """Returns the index of the maximum element of a vector. (first found)"""

    def Min(self) -> int:
        """Returns the index of the minimum element of a vector. (first found)"""

    def Normalize(self) -> None:
        """
        Normalizes this vector (the norm of the result
        is equal to 1.0) and assigns the result to this vector
        Exceptions
        Standard_NullValue if this vector is null (i.e. if its norm is
        less than or equal to double::RealEpsilon().
        """

    def Normalized(self) -> math_Vector:
        """
        Normalizes this vector (the norm of the result
        is equal to 1.0) and creates a new vector
        Exceptions
        Standard_NullValue if this vector is null (i.e. if its norm is
        less than or equal to double::RealEpsilon().
        """

    def Invert(self) -> None:
        """Inverts this vector and assigns the result to this vector."""

    def Inverse(self) -> math_Vector:
        """Inverts this vector and creates a new vector."""

    def Set(self, theI1: int, theI2: int, theV: math_Vector) -> None:
        """
        sets a vector from "theI1" to "theI2" to the vector "theV";
        An exception is raised if "theI1" is less than "LowerIndex" or "theI2" is greater than
        "UpperIndex" or "theI1" is greater than "theI2". An exception is raised if "theI2-theI1+1" is
        different from the "Length" of "theV".
        """

    def Slice(self, theI1: int, theI2: int) -> math_Vector:
        """
        Creates a new vector by inverting the values of this vector
        between indexes "theI1" and "theI2".
        If the values of this vector were (1., 2., 3., 4.,5., 6.),
        by slicing it between indexes 2 and 5 the values
        of the resulting vector are (1., 5., 4., 3., 2., 6.)
        """

    @overload
    def Multiply(self, theRight: float) -> None:
        """Updates current vector by multiplying each element on current value."""

    @overload
    def Multiply(self, theLeft: math_Vector, theRight: math_Matrix) -> None:
        """
        sets a vector to the product of the vector "theLeft"
        with the matrix "theRight".
        """

    @overload
    def Multiply(self, theLeft: math_Matrix, theRight: math_Vector) -> None:
        """
        sets a vector to the product of the matrix "theLeft"
        with the vector "theRight".
        """

    @overload
    def Multiply(self, theLeft: float, theRight: math_Vector) -> None:
        """
        returns the multiplication of a real by a vector.
        "me" = "theLeft" * "theRight\"
        """

    def __imul__(self, theRight: float) -> math_Vector: ...

    @overload
    def Multiplied(self, theRight: float) -> math_Vector:
        """returns the product of a vector and a real value."""

    @overload
    def Multiplied(self, theRight: math_Vector) -> float:
        """
        returns the inner product of 2 vectors.
        An exception is raised if the lengths are not equal.
        """

    @overload
    def Multiplied(self, theRight: math_Matrix) -> math_Vector:
        """returns the product of a vector by a matrix."""

    @overload
    def __mul__(self, theRight: float) -> math_Vector: ...

    @overload
    def __mul__(self, theRight: math_Vector) -> float: ...

    @overload
    def __mul__(self, theRight: math_Matrix) -> math_Vector: ...

    def TMultiplied(self, theRight: float) -> math_Vector:
        """returns the product of a vector and a real value."""

    def Divide(self, theRight: float) -> None:
        """
        divides a vector by the value "theRight".
        An exception is raised if "theRight" = 0.
        """

    def __itruediv__(self, theRight: float) -> math_Vector: ...

    def Divided(self, theRight: float) -> math_Vector:
        """
        Returns new vector as dividing current vector with the value "theRight".
        An exception is raised if "theRight" = 0.
        """

    def __truediv__(self, theRight: float) -> math_Vector: ...

    @overload
    def Add(self, theRight: math_Vector) -> None:
        """
        adds the vector "theRight" to a vector.
        An exception is raised if the vectors have not the same length.
        Warning
        In order to avoid time-consuming copying of vectors, it
        is preferable to use operator += or the function Add whenever possible.
        """

    @overload
    def Add(self, theLeft: math_Vector, theRight: math_Vector) -> None:
        """
        sets a vector to the sum of the vector "theLeft"
        and the vector "theRight".
        An exception is raised if the lengths are different.
        """

    def __iadd__(self, theRight: math_Vector) -> math_Vector: ...

    def Added(self, theRight: math_Vector) -> math_Vector:
        """
        Returns new vector as adding current vector with the value "theRight".
        An exception is raised if the vectors do not have the same length.
        An exception is raised if the lengths are not equal.
        """

    def __add__(self, theRight: math_Vector) -> math_Vector: ...

    @overload
    def TMultiply(self, theTLeft: math_Matrix, theRight: math_Vector) -> None:
        """
        sets a vector to the product of the transpose
        of the matrix "theTLeft" by the vector "theRight".
        """

    @overload
    def TMultiply(self, theLeft: math_Vector, theTRight: math_Matrix) -> None:
        """
        sets a vector to the product of the vector
        "theLeft" by the transpose of the matrix "theTRight".
        """

    @overload
    def Subtract(self, theLeft: math_Vector, theRight: math_Vector) -> None:
        """
        sets a vector to the Subtraction of the
        vector theRight from the vector theLeft.
        An exception is raised if the vectors have not the same length.
        Warning
        In order to avoid time-consuming copying of vectors, it
        is preferable to use operator -= or the function
        Subtract whenever possible.
        """

    @overload
    def Subtract(self, theRight: math_Vector) -> None:
        """
        returns the subtraction of "theRight" from "me".
        An exception is raised if the vectors have not the same length.
        """

    def Value(self, theNum: int) -> float:
        """
        accesses (in read or write mode) the value of index "theNum" of a vector.
        """

    def SetValue(self, theNum: int, theValue: float) -> None:
        """
        Python addition: sets the value Value(theNum) returns by reference in C++.
        """

    def __call__(self, theNum: int) -> float: ...

    def __getitem__(self, arg: int, /) -> float:
        """Python addition: alias to operator()."""

    def __setitem__(self, arg0: int, arg1: float, /) -> None:
        """
        Python addition: sets the value operator()(theNum) returns by reference in C++.
        """

    def Initialized(self, theOther: math_Vector) -> math_Vector:
        """
        Initialises a vector by copying "theOther".
        An exception is raised if the Lengths are different.
        """

    def Opposite(self) -> math_Vector:
        """returns the opposite of a vector."""

    def __neg__(self) -> math_Vector: ...

    def __isub__(self, theRight: math_Vector) -> math_Vector: ...

    def Subtracted(self, theRight: math_Vector) -> math_Vector:
        """
        returns the subtraction of "theRight" from "me".
        An exception is raised if the vectors have not the same length.
        """

    def __sub__(self, theRight: math_Vector) -> math_Vector: ...

    def Dump(self) -> object:
        """
        Prints information on the current state of the object.
        Is used to redefine the operator <<.
        """

    def Array1(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """
        Returns the underlying array for interoperability with legacy APIs.
        Allows passing math_Vector data to functions expecting NCollection_Array1.
        """

    def Resize(self, theSize: int) -> None:
        """
        Resizes the vector to a new size, keeping the same lower bound.
        Existing data within the new range is preserved.
        The method optimizes memory usage:
        - If new size fits in stack buffer (<=32), uses stack allocation
        - If new size requires heap and was already on heap, resizes in place
        - Transitions between stack and heap as needed
        @param theSize new size of the vector
        """

    def __rmul__(self, arg: float, /) -> math_Vector: ...

class math:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: math) -> None: ...

    @staticmethod
    def GaussPointsMax() -> int: ...

    @staticmethod
    def GaussPoints(Index: int, Points: math_Vector) -> None: ...

    @staticmethod
    def GaussWeights(Index: int, Weights: math_Vector) -> None: ...

    @staticmethod
    def KronrodPointsMax() -> int:
        """
        Returns the maximal number of points for that the values
        are stored in the table. If the number is greater then
        KronrodPointsMax, the points will be computed.
        """

    @staticmethod
    def OrderedGaussPointsAndWeights(Index: int, Points: math_Vector, Weights: math_Vector) -> bool:
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
    def KronrodPointsAndWeights(Index: int, Points: math_Vector, Weights: math_Vector) -> bool:
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

    @overload
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

    @overload
    def __init__(self, theOther: math_BFGS) -> None: ...

    def SetBoundary(self, theLeftBorder: math_Vector, theRightBorder: math_Vector) -> None:
        """
        Set boundaries for conditional optimization.
        The expected indices range of vectors is [1, NbVariables].
        """

    def Perform(self, F: math_MultipleVarFunctionWithGradient, StartingPoint: math_Vector) -> None:
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
    def Location(self) -> math_Vector:
        """
        returns the location vector of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    @overload
    def Location(self, Loc: math_Vector) -> None:
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
    def Gradient(self) -> math_Vector:
        """
        Returns the gradient vector at the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    @overload
    def Gradient(self, Grad: math_Vector) -> None:
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

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.
        Is used to redefine the operator <<.
        """

class math_BissecNewton:
    """
    This class implements a combination of Newton-Raphson and bissection
    methods to find the root of the function between two bounds.
    Knowledge of the derivative is required.
    """

    @overload
    def __init__(self, theXTolerance: float) -> None:
        """
        Constructor.
        @param theXTolerance - algorithm tolerance.
        """

    @overload
    def __init__(self, theOther: math_BissecNewton) -> None: ...

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

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.
        Is used to redefine the operator <<.
        """

class math_BracketedRoot:
    """
    This class implements the Brent method to find the root of a function
    located within two bounds. No knowledge of the derivative is required.
    """

    @overload
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

    @overload
    def __init__(self, theOther: math_BracketedRoot) -> None: ...

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

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.
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

    @overload
    def __init__(self, theOther: math_BracketMinimum) -> None: ...

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

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.
        Is used to redefine the operator <<.
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

    @overload
    def __init__(self, theOther: math_BrentMinimum) -> None: ...

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

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.
        Is used to redefine the operator <<.
        """

class math_BullardGenerator:
    """
    Fast random number generator (the algorithm proposed by Ian C. Bullard).
    """

    @overload
    def __init__(self, theSeed: int = 1) -> None:
        """Creates new Xorshift 64-bit RNG."""

    @overload
    def __init__(self, theOther: math_BullardGenerator) -> None: ...

    def SetSeed(self, theSeed: int = 1) -> None:
        """Setup new seed / reset defaults."""

    def NextInt(self) -> int:
        """Generates new 64-bit integer value."""

    def NextReal(self) -> float:
        """Generates new floating-point value."""

class math_ComputeGaussPointsAndWeights:
    @overload
    def __init__(self, Number: int) -> None: ...

    @overload
    def __init__(self, theOther: math_ComputeGaussPointsAndWeights) -> None: ...

    def IsDone(self) -> bool: ...

    def Points(self) -> math_Vector: ...

    def Weights(self) -> math_Vector: ...

class math_ComputeKronrodPointsAndWeights:
    @overload
    def __init__(self, Number: int) -> None: ...

    @overload
    def __init__(self, theOther: math_ComputeKronrodPointsAndWeights) -> None: ...

    def IsDone(self) -> bool: ...

    def Points(self) -> math_Vector: ...

    def Weights(self) -> math_Vector: ...

class math_Crout:
    """
    This class implements the Crout algorithm used to solve a
    system A*X = B where A is a symmetric matrix. It can be used to
    invert a symmetric matrix.
    This algorithm is similar to Gauss but is faster than Gauss.
    Only the inferior triangle of A and the diagonal can be given.
    """

    @overload
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

    @overload
    def __init__(self, theOther: math_Crout) -> None: ...

    def IsDone(self) -> bool:
        """Returns True if all has been correctly done."""

    def Solve(self, B: math_Vector, X: math_Vector) -> None:
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

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.
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

    @overload
    def __init__(self, theOther: math_DirectPolynomialRoots) -> None: ...

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

    def Dump(self) -> object:
        """
        Prints diagnostic information about the current state of the solver.
        Outputs computation status, number of roots, and individual root values.
        This method is used to redefine the operator << for debugging purposes.

        @param theStream output stream for diagnostic information
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

    @overload
    def __init__(self, theDiagonal: nanoocp.NCollection.NCollection_Array1[float], theSubdiagonal: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    @overload
    def __init__(self, theOther: math_EigenValuesSearcher) -> None: ...

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

    def EigenVector(self, theIndex: int) -> math_Vector:
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

    @overload
    def __init__(self, theFunction: math_MultipleVarFunctionWithGradient, theTolerance: float, theNbIterations: int = 200, theZEPS: float = 1e-12) -> None:
        """
        Initializes the computation of the minimum of F.
        Warning: constructor does not perform computations.
        """

    @overload
    def __init__(self, theOther: math_FRPR) -> None: ...

    def Perform(self, theFunction: math_MultipleVarFunctionWithGradient, theStartingPoint: math_Vector) -> None:
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
    def Location(self) -> math_Vector:
        """
        returns the location vector of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    @overload
    def Location(self, Loc: math_Vector) -> None:
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
    def Gradient(self) -> math_Vector:
        """
        returns the gradient vector at the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    @overload
    def Gradient(self, Grad: math_Vector) -> None:
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

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.
        Is used to redefine the operator <<.
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

    @overload
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

    @overload
    def __init__(self, theOther: math_FunctionAllRoots) -> None: ...

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

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.
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

    @overload
    def __init__(self, theOther: math_FunctionRoot) -> None: ...

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

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.
        Is used to redefine the operator <<.
        """

class math_FunctionRoots:
    """
    This class implements an algorithm which finds all the real roots of
    a function with derivative within a given range.
    Knowledge of the derivative is required.
    """

    @overload
    def __init__(self, F: math_FunctionWithDerivative, A: float, B: float, NbSample: int, EpsX: float = 0.0, EpsF: float = 0.0, EpsNull: float = 0.0, K: float = 0.0) -> None:
        """
        Calculates all the real roots of a function F-K within the range
        A..B. without conditions on A and B
        A solution X is found when
        abs(Xi - Xi-1) <= Epsx and abs(F(Xi)-K) <= EpsF.
        The function is considered as null between A and B if
        abs(F-K) <= EpsNull within this range.
        """

    @overload
    def __init__(self, theOther: math_FunctionRoots) -> None: ...

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

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.
        """

class math_FunctionSample:
    """
    This class gives a default sample (constant difference
    of parameter) for a function defined between
    two bound A,B.
    """

    @overload
    def __init__(self, A: float, B: float, N: int) -> None: ...

    @overload
    def __init__(self, theOther: math_FunctionSample) -> None: ...

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

    def Value(self, X: math_Vector, F: math_Vector) -> bool:
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

class math_IntegerVector:
    """
    This class implements the real vector abstract data type.
    Vectors can have an arbitrary range which must be defined at
    the declaration and cannot be changed after this declaration.
    @code
    math_VectorBase<TheItemType> V1(-3, 5); // a vector with range [-3..5]
    @endcode

    Vector are copied through assignment:
    @code
    math_VectorBase<TheItemType> V2( 1, 9);
    ....
    V2 = V1;
    V1(1) = 2.0; // the vector V2 will not be modified.
    @endcode

    The Exception RangeError is raised when trying to access outside
    the range of a vector :
    @code
    V1(11) = 0.0 // --> will raise RangeError;
    @endcode

    The Exception DimensionError is raised when the dimensions of two
    vectors are not compatible :
    @code
    math_VectorBase<TheItemType> V3(1, 2);
    V3 = V1;    // --> will raise DimensionError;
    V1.Add(V3)  // --> will raise DimensionError;
    @endcode
    """

    @overload
    def __init__(self, Other: nanoocp.gp.gp_XY) -> None:
        """Constructor for converting gp_XY to math_VectorBase"""

    @overload
    def __init__(self, Other: nanoocp.gp.gp_XYZ) -> None:
        """Constructor for converting gp_XYZ to math_VectorBase"""

    @overload
    def __init__(self, theOther: math_IntegerVector) -> None:
        """Constructs a copy for initialization."""

    @overload
    def __init__(self, theLower: int, theUpper: int) -> None:
        """
        Constructs a non-initialized vector in the range [theLower..theUpper]
        "theLower" and "theUpper" are the indexes of the lower and upper bounds of the constructed
        vector.
        """

    @overload
    def __init__(self, theLower: int, theUpper: int, theInitialValue: int) -> None:
        """
        Constructs a vector in the range [theLower..theUpper]
        whose values are all initialized with the value "theInitialValue\"
        """

    def Init(self, theInitialValue: int) -> None:
        """Initialize all the elements of a vector with "theInitialValue"."""

    def Length(self) -> int:
        """Returns the length of a vector"""

    def Lower(self) -> int:
        """Returns the lower index of the vector"""

    def Upper(self) -> int:
        """Returns the upper index of the vector"""

    def Norm(self) -> float:
        """Returns the value or the square of the norm of this vector."""

    def Norm2(self) -> float:
        """Returns the value of the square of the norm of a vector."""

    def Max(self) -> int:
        """Returns the index of the maximum element of a vector. (first found)"""

    def Min(self) -> int:
        """Returns the index of the minimum element of a vector. (first found)"""

    def Normalize(self) -> None:
        """
        Normalizes this vector (the norm of the result
        is equal to 1.0) and assigns the result to this vector
        Exceptions
        Standard_NullValue if this vector is null (i.e. if its norm is
        less than or equal to double::RealEpsilon().
        """

    def Normalized(self) -> math_IntegerVector:
        """
        Normalizes this vector (the norm of the result
        is equal to 1.0) and creates a new vector
        Exceptions
        Standard_NullValue if this vector is null (i.e. if its norm is
        less than or equal to double::RealEpsilon().
        """

    def Invert(self) -> None:
        """Inverts this vector and assigns the result to this vector."""

    def Inverse(self) -> math_IntegerVector:
        """Inverts this vector and creates a new vector."""

    def Set(self, theI1: int, theI2: int, theV: math_IntegerVector) -> None:
        """
        sets a vector from "theI1" to "theI2" to the vector "theV";
        An exception is raised if "theI1" is less than "LowerIndex" or "theI2" is greater than
        "UpperIndex" or "theI1" is greater than "theI2". An exception is raised if "theI2-theI1+1" is
        different from the "Length" of "theV".
        """

    def Slice(self, theI1: int, theI2: int) -> math_IntegerVector:
        """
        Creates a new vector by inverting the values of this vector
        between indexes "theI1" and "theI2".
        If the values of this vector were (1., 2., 3., 4.,5., 6.),
        by slicing it between indexes 2 and 5 the values
        of the resulting vector are (1., 5., 4., 3., 2., 6.)
        """

    @overload
    def Multiply(self, theRight: int) -> None:
        """Updates current vector by multiplying each element on current value."""

    @overload
    def Multiply(self, theLeft: math_IntegerVector, theRight: math_Matrix) -> None:
        """
        sets a vector to the product of the vector "theLeft"
        with the matrix "theRight".
        """

    @overload
    def Multiply(self, theLeft: math_Matrix, theRight: math_IntegerVector) -> None:
        """
        sets a vector to the product of the matrix "theLeft"
        with the vector "theRight".
        """

    @overload
    def Multiply(self, theLeft: int, theRight: math_IntegerVector) -> None:
        """
        returns the multiplication of a real by a vector.
        "me" = "theLeft" * "theRight\"
        """

    def __imul__(self, theRight: int) -> math_IntegerVector: ...

    @overload
    def Multiplied(self, theRight: int) -> math_IntegerVector:
        """returns the product of a vector and a real value."""

    @overload
    def Multiplied(self, theRight: math_IntegerVector) -> int:
        """
        returns the inner product of 2 vectors.
        An exception is raised if the lengths are not equal.
        """

    @overload
    def Multiplied(self, theRight: math_Matrix) -> math_IntegerVector:
        """returns the product of a vector by a matrix."""

    @overload
    def __mul__(self, theRight: int) -> math_IntegerVector: ...

    @overload
    def __mul__(self, theRight: math_IntegerVector) -> int: ...

    @overload
    def __mul__(self, theRight: math_Matrix) -> math_IntegerVector: ...

    def TMultiplied(self, theRight: int) -> math_IntegerVector:
        """returns the product of a vector and a real value."""

    def Divide(self, theRight: int) -> None:
        """
        divides a vector by the value "theRight".
        An exception is raised if "theRight" = 0.
        """

    def __itruediv__(self, theRight: int) -> math_IntegerVector: ...

    def Divided(self, theRight: int) -> math_IntegerVector:
        """
        Returns new vector as dividing current vector with the value "theRight".
        An exception is raised if "theRight" = 0.
        """

    def __truediv__(self, theRight: int) -> math_IntegerVector: ...

    @overload
    def Add(self, theRight: math_IntegerVector) -> None:
        """
        adds the vector "theRight" to a vector.
        An exception is raised if the vectors have not the same length.
        Warning
        In order to avoid time-consuming copying of vectors, it
        is preferable to use operator += or the function Add whenever possible.
        """

    @overload
    def Add(self, theLeft: math_IntegerVector, theRight: math_IntegerVector) -> None:
        """
        sets a vector to the sum of the vector "theLeft"
        and the vector "theRight".
        An exception is raised if the lengths are different.
        """

    def __iadd__(self, theRight: math_IntegerVector) -> math_IntegerVector: ...

    def Added(self, theRight: math_IntegerVector) -> math_IntegerVector:
        """
        Returns new vector as adding current vector with the value "theRight".
        An exception is raised if the vectors do not have the same length.
        An exception is raised if the lengths are not equal.
        """

    def __add__(self, theRight: math_IntegerVector) -> math_IntegerVector: ...

    @overload
    def TMultiply(self, theTLeft: math_Matrix, theRight: math_IntegerVector) -> None:
        """
        sets a vector to the product of the transpose
        of the matrix "theTLeft" by the vector "theRight".
        """

    @overload
    def TMultiply(self, theLeft: math_IntegerVector, theTRight: math_Matrix) -> None:
        """
        sets a vector to the product of the vector
        "theLeft" by the transpose of the matrix "theTRight".
        """

    @overload
    def Subtract(self, theLeft: math_IntegerVector, theRight: math_IntegerVector) -> None:
        """
        sets a vector to the Subtraction of the
        vector theRight from the vector theLeft.
        An exception is raised if the vectors have not the same length.
        Warning
        In order to avoid time-consuming copying of vectors, it
        is preferable to use operator -= or the function
        Subtract whenever possible.
        """

    @overload
    def Subtract(self, theRight: math_IntegerVector) -> None:
        """
        returns the subtraction of "theRight" from "me".
        An exception is raised if the vectors have not the same length.
        """

    def Value(self, theNum: int) -> int:
        """
        accesses (in read or write mode) the value of index "theNum" of a vector.
        """

    def SetValue(self, theNum: int, theValue: int) -> None:
        """
        Python addition: sets the value Value(theNum) returns by reference in C++.
        """

    def __call__(self, theNum: int) -> int: ...

    def __getitem__(self, arg: int, /) -> int:
        """Python addition: alias to operator()."""

    def __setitem__(self, arg0: int, arg1: int, /) -> None:
        """
        Python addition: sets the value operator()(theNum) returns by reference in C++.
        """

    def Initialized(self, theOther: math_IntegerVector) -> math_IntegerVector:
        """
        Initialises a vector by copying "theOther".
        An exception is raised if the Lengths are different.
        """

    def Opposite(self) -> math_IntegerVector:
        """returns the opposite of a vector."""

    def __neg__(self) -> math_IntegerVector: ...

    def __isub__(self, theRight: math_IntegerVector) -> math_IntegerVector: ...

    def Subtracted(self, theRight: math_IntegerVector) -> math_IntegerVector:
        """
        returns the subtraction of "theRight" from "me".
        An exception is raised if the vectors have not the same length.
        """

    def __sub__(self, theRight: math_IntegerVector) -> math_IntegerVector: ...

    def Dump(self) -> object:
        """
        Prints information on the current state of the object.
        Is used to redefine the operator <<.
        """

    def Array1(self) -> nanoocp.NCollection.NCollection_Array1[int]:
        """
        Returns the underlying array for interoperability with legacy APIs.
        Allows passing math_Vector data to functions expecting NCollection_Array1.
        """

    def Resize(self, theSize: int) -> None:
        """
        Resizes the vector to a new size, keeping the same lower bound.
        Existing data within the new range is preserved.
        The method optimizes memory usage:
        - If new size fits in stack buffer (<=32), uses stack allocation
        - If new size requires heap and was already on heap, resizes in place
        - Transitions between stack and heap as needed
        @param theSize new size of the vector
        """

    def __rmul__(self, arg: int, /) -> math_IntegerVector: ...

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
    def __init__(self, F: math_FunctionSetWithDerivatives, Tolerance: math_Vector, NbIterations: int = 100) -> None:
        """
        is used in a sub-class to initialize correctly all the fields
        of this class.
        The range (1, F.NbVariables()) must be especially
        respected for all vectors and matrix declarations.
        """

    @overload
    def __init__(self, theOther: math_FunctionSetRoot) -> None: ...

    def SetTolerance(self, Tolerance: math_Vector) -> None:
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
    def Perform(self, theFunction: math_FunctionSetWithDerivatives, theStartingPoint: math_Vector, theStopOnDivergent: bool = False) -> None:
        """
        Improves the root of function from the initial guess point.
        The infinum and supremum may be given to constrain the solution.
        In this case, the solution is found when: abs(Xi - Xi-1)(j) <= Tolerance(j)
        for all unknowns.
        """

    @overload
    def Perform(self, theFunction: math_FunctionSetWithDerivatives, theStartingPoint: math_Vector, theInfBound: math_Vector, theSupBound: math_Vector, theStopOnDivergent: bool = False) -> None:
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
    def Root(self) -> math_Vector:
        """
        Returns the value of the root of function F.
        Exception NotDone is raised if the root was not found.
        """

    @overload
    def Root(self, Root: math_Vector) -> None:
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
    def FunctionSetErrors(self) -> math_Vector:
        """
        returns the vector value of the error done
        on the functions at the root.
        Exception NotDone is raised if the root was not found.
        """

    @overload
    def FunctionSetErrors(self, Err: math_Vector) -> None:
        """
        outputs the vector value of the error done
        on the functions at the root in Err.
        Exception NotDone is raised if the root was not found.
        Exception DimensionError is raised if the range of Err
        is not equal to the range of the StartingPoint.
        """

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.
        Is used to redefine the operator <<.
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

    def Value(self, X: math_Vector, F: math_Vector) -> bool:
        """
        Computes the values <F> of the Functions for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool:
        """
        Returns the values <D> of the derivatives for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool:
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

    @overload
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

    @overload
    def __init__(self, theOther: math_Gauss) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false
        """

    @overload
    def Solve(self, B: math_Vector, X: math_Vector) -> None:
        """
        Given the input Vector B this routine returns the solution X of the set
        of linear equations A . X = B.
        Exception NotDone is raised if the decomposition of A was not done
        successfully.
        Exception DimensionError is raised if the range of B is not
        equal to the number of rows of A.
        """

    @overload
    def Solve(self, B: math_Vector) -> None:
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

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.
        Is used to redefine the operator <<.
        """

class math_GaussLeastSquare:
    """
    This class implements the least square solution of a set of
    n linear equations of m unknowns (n >= m) using the gauss LU
    decomposition algorithm.
    This algorithm is more likely subject to numerical instability
    than math_SVD.
    """

    @overload
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

    @overload
    def __init__(self, theOther: math_GaussLeastSquare) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.e
        """

    def Solve(self, B: math_Vector, X: math_Vector) -> None:
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

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.
        Is used to redefine the operator <<.
        """

class math_GaussMultipleIntegration:
    """
    This class implements the integration of a function of multiple
    variables between the parameter bounds Lower[a..b] and Upper[a..b].
    Warning: Each element of Order must be inferior or equal to 61.
    """

    @overload
    def __init__(self, F: math_MultipleVarFunction, Lower: math_Vector, Upper: math_Vector, Order: math_IntegerVector) -> None:
        """
        The Gauss-Legendre integration with Order = points of
        integration for each unknown, is done on the function F
        between the bounds Lower and Upper.
        """

    @overload
    def __init__(self, theOther: math_GaussMultipleIntegration) -> None: ...

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def Value(self) -> float:
        """returns the value of the integral."""

    def Dump(self) -> object:
        """Prints information on the current state of the object."""

class math_GaussSetIntegration:
    """
    This class implements the integration of a set of N
    functions of M variables variables between the
    parameter bounds Lower[a..b] and Upper[a..b].
    Warning: The case M>1 is not implemented.
    """

    @overload
    def __init__(self, F: math_FunctionSet, Lower: math_Vector, Upper: math_Vector, Order: math_IntegerVector) -> None:
        """
        The Gauss-Legendre integration with Order = points of
        integration for each unknown, is done on the function F
        between the bounds Lower and Upper.
        """

    @overload
    def __init__(self, theOther: math_GaussSetIntegration) -> None: ...

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def Value(self) -> math_Vector:
        """returns the value of the integral."""

    def Dump(self) -> object:
        """Prints information on the current state of the object."""

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

    @overload
    def __init__(self, theOther: math_GaussSingleIntegration) -> None: ...

    def IsDone(self) -> bool:
        """returns True if all has been correctly done."""

    def Value(self) -> float:
        """returns the value of the integral."""

    def Dump(self) -> object:
        """Prints information on the current state of the object."""

class math_MultipleVarFunction:
    """
    Describes the virtual functions associated with a multiple variable function.
    """

    def NbVariables(self) -> int:
        """Returns the number of variables of the function"""

    def Value(self, X: math_Vector) -> tuple[bool, float]:
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

class math_GlobOptMin:
    """
    This class represents Evtushenko's algorithm of global optimization based on non-uniform mesh.
    Article: Yu. Evtushenko. Numerical methods for finding global extreme (case of a non-uniform
    mesh). U.S.S.R. Comput. Maths. Math. Phys., Vol. 11, N 6, pp. 38-54.

    This method performs search on non-uniform mesh. The search space is a box in R^n space.
    The default behavior is to find all minimums in that box. Computation of maximums is not
    supported.

    The search box can be split into smaller boxes by discontinuity criteria.
    This functionality is covered by SetGlobalParams and SetLocalParams API.

    It is possible to set continuity of the local boxes.
    Such option can forcibly change local extrema search.
    In other words if theFunc can be casted to the function with Hessian but, continuity is set to 1
    Gradient based local optimization method will be used, not Hessian based method.
    This functionality is covered by SetContinuity and GetContinuity API.

    It is possible to freeze Lipschitz const to avoid internal modifications on it.
    This functionality is covered by SetLipConstState and GetLipConstState API.

    It is possible to perform single solution search.
    This functionality is covered by first parameter in Perform method.

    It is possible to set / get minimal value of the functional.
    It works well together with single solution search.
    This functionality is covered by SetFunctionalMinimalValue and GetFunctionalMinimalValue API.
    """

    def __init__(self, theFunc: math_MultipleVarFunction, theLowerBorder: math_Vector, theUpperBorder: math_Vector, theC: float = 9.0, theDiscretizationTol: float = 0.01, theSameTol: float = 1e-07) -> None:
        """
        Constructor. Perform method is not called from it.
        @param theFunc - objective functional.
        @param theLowerBorder - lower corner of the search box.
        @param theUpperBorder - upper corner of the search box.
        @param theC - Lipschitz constant.
        @param theDiscretizationTol - parameter space discretization tolerance.
        @param theSameTol - functional value space indifference tolerance.
        """

    def SetGlobalParams(self, theFunc: math_MultipleVarFunction, theLowerBorder: math_Vector, theUpperBorder: math_Vector, theC: float = 9.0, theDiscretizationTol: float = 0.01, theSameTol: float = 1e-07) -> None:
        """
        @param theFunc - objective functional.
        @param theLowerBorder - lower corner of the search box.
        @param theUpperBorder - upper corner of the search box.
        @param theC - Lipschitz constant.
        @param theDiscretizationTol - parameter space discretization tolerance.
        @param theSameTol - functional value space indifference tolerance.
        """

    def SetLocalParams(self, theLocalA: math_Vector, theLocalB: math_Vector) -> None:
        """
        Method to reduce bounding box. Perform will use this box.
        @param theLocalA - lower corner of the local box.
        @param theLocalB - upper corner of the local box.
        """

    def SetTol(self, theDiscretizationTol: float, theSameTol: float) -> None:
        """
        Method to set tolerances.
        @param theDiscretizationTol - parameter space discretization tolerance.
        @param theSameTol - functional value space indifference tolerance.
        """

    def GetTol(self) -> tuple[float, float]:
        """
        Method to get tolerances.
        @param theDiscretizationTol - parameter space discretization tolerance.
        @param theSameTol - functional value space indifference tolerance.
        """

    def Perform(self, isFindSingleSolution: bool = False) -> None:
        """
        @param isFindSingleSolution - defines whether to find single solution or all solutions.
        """

    def Points(self, theIndex: int, theSol: math_Vector) -> None:
        """Return solution theIndex, 1 <= theIndex <= NbExtrema."""

    def SetContinuity(self, theCont: int) -> None:
        """Set / Get continuity of local borders splits (0 ~ C0, 1 ~ C1, 2 ~ C2)."""

    def GetContinuity(self) -> int: ...

    def SetFunctionalMinimalValue(self, theMinimalValue: float) -> None:
        """Set / Get functional minimal value."""

    def GetFunctionalMinimalValue(self) -> float: ...

    def SetLipConstState(self, theFlag: bool) -> None:
        """
        Set / Get Lipchitz constant modification state.
        True means that the constant is locked and unlocked otherwise.
        """

    def GetLipConstState(self) -> bool: ...

    def isDone(self) -> bool:
        """Return computation state of the algorithm."""

    def GetF(self) -> float:
        """Get best functional value."""

    def NbExtrema(self) -> int:
        """Return count of global extremas."""

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
    def __init__(self, A: math_Matrix, B: math_Vector, EPS: float = 1e-20) -> None:
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

    @overload
    def __init__(self, theOther: math_Householder) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def Value(self, sol: math_Vector, Index: int = 1) -> None:
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

    def Dump(self) -> object:
        """Prints information on the current state of the object."""

class math_Jacobi:
    """
    This class implements the Jacobi method to find the eigenvalues and
    the eigenvectors of a real symmetric square matrix.
    A sort of eigenvalues is done.
    """

    @overload
    def __init__(self, A: math_Matrix) -> None:
        """
        Given a Real n X n matrix A, this constructor computes all its
        eigenvalues and eigenvectors using the Jacobi method.
        The exception NotSquare is raised if the matrix is not square.
        No verification that the matrix A is really symmetric is done.
        """

    @overload
    def __init__(self, theOther: math_Jacobi) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def Values(self) -> math_Vector:
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

    def Vector(self, Num: int, V: math_Vector) -> None:
        """
        Returns the eigenvector V of number Num.
        Eigenvectors are in the range (1..n).
        Exception NotDone is raised if calculation is not done successfully.
        """

    def Dump(self) -> object:
        """
        Prints information on the current state of the object.
        Is used to redefine the operator <<.
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
    def __init__(self, theOther: math_KronrodSingleIntegration) -> None: ...

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
    def GKRule(theFunction: math_Function, theLower: float, theUpper: float, theGaussP: math_Vector, theGaussW: math_Vector, theKronrodP: math_Vector, theKronrodW: math_Vector) -> tuple[bool, float, float]: ...

class math_MultipleVarFunctionWithGradient(math_MultipleVarFunction):
    """
    The abstract class MultipleVarFunctionWithGradient
    describes the virtual functions associated with a multiple variable function.
    """

    def NbVariables(self) -> int:
        """Returns the number of variables of the function."""

    def Value(self, X: math_Vector) -> tuple[bool, float]:
        """
        Computes the values of the Functions <F> for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Gradient(self, X: math_Vector, G: math_Vector) -> bool:
        """
        Computes the gradient <G> of the functions for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Values(self, X: math_Vector, G: math_Vector) -> tuple[bool, float]:
        """
        computes the value <F> and the gradient <G> of the
        functions for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

class math_MultipleVarFunctionWithHessian(math_MultipleVarFunctionWithGradient):
    def NbVariables(self) -> int:
        """returns the number of variables of the function."""

    def Value(self, X: math_Vector) -> tuple[bool, float]:
        """
        computes the values of the Functions <F> for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    def Gradient(self, X: math_Vector, G: math_Vector) -> bool:
        """
        computes the gradient <G> of the functions for the
        variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    @overload
    def Values(self, X: math_Vector, G: math_Vector) -> tuple[bool, float]:
        """
        computes the value <F> and the gradient <G> of the
        functions for the variable <X>.
        Returns True if the computation was done successfully,
        False otherwise.
        """

    @overload
    def Values(self, X: math_Vector, G: math_Vector, H: math_Matrix) -> tuple[bool, float]:
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

    @overload
    def __init__(self, theOther: math_NewtonFunctionRoot) -> None: ...

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

    def Dump(self) -> object:
        """Prints information on the current state of the object."""

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
    def __init__(self, theFunction: math_FunctionSetWithDerivatives, theXTolerance: math_Vector, theFTolerance: float, theNbIterations: int = 100) -> None:
        """
        Initialize correctly all the fields of this class.
        The range (1, F.NbVariables()) must be especially respected for
        all vectors and matrix declarations.
        """

    @overload
    def __init__(self, theOther: math_NewtonFunctionSetRoot) -> None: ...

    def SetTolerance(self, XTol: math_Vector) -> None:
        """Initializes the tolerance values for the unknowns."""

    @overload
    def Perform(self, theFunction: math_FunctionSetWithDerivatives, theStartingPoint: math_Vector) -> None:
        """
        The Newton method is done to improve the root of the function
        from the initial guess point. The solution is found when:
        abs(Xj - Xj-1)(i) <= XTol(i) and abs(Fi) <= FTol for all i;
        """

    @overload
    def Perform(self, theFunction: math_FunctionSetWithDerivatives, theStartingPoint: math_Vector, theInfBound: math_Vector, theSupBound: math_Vector) -> None:
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
    def Root(self) -> math_Vector:
        """
        Returns the value of the root of function F.
        Exceptions
        StdFail_NotDone if the algorithm fails (and IsDone returns false).
        """

    @overload
    def Root(self, Root: math_Vector) -> None:
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
    def FunctionSetErrors(self) -> math_Vector:
        """
        Returns the vector value of the error done on the
        functions at the root.
        Exception NotDone is raised if the root was not found.
        """

    @overload
    def FunctionSetErrors(self, Err: math_Vector) -> None:
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

    def Dump(self) -> object:
        """
        Prints information on the current state of the object.
        Is used to redefine the operator <<.
        """

class math_NewtonMinimum:
    @overload
    def __init__(self, theFunction: math_MultipleVarFunctionWithHessian, theTolerance: float = 1e-07, theNbIterations: int = 40, theConvexity: float = 1e-06, theWithSingularity: bool = True) -> None:
        """
        The tolerance required on the solution is given by Tolerance.
        Iteration are stopped if (!WithSingularity) and H(F(Xi)) is not definite
        positive (if the smaller eigenvalue of H < Convexity)
        or IsConverged() returns True for 2 successives Iterations.
        Warning: This constructor does not perform computation.
        """

    @overload
    def __init__(self, theOther: math_NewtonMinimum) -> None: ...

    def Perform(self, theFunction: math_MultipleVarFunctionWithHessian, theStartingPoint: math_Vector) -> None:
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
    def Location(self) -> math_Vector:
        """
        returns the location vector of the minimum.
        Exception NotDone is raised if an error has occurred.
        """

    @overload
    def Location(self, Loc: math_Vector) -> None:
        """
        outputs the location vector of the minimum in Loc.
        Exception NotDone is raised if an error has occurred.
        Exception DimensionError is raised if the range of Loc is not
        equal to the range of the StartingPoint.
        """

    def SetBoundary(self, theLeftBorder: math_Vector, theRightBorder: math_Vector) -> None:
        """Set boundaries."""

    def Minimum(self) -> float:
        """
        returns the value of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    @overload
    def Gradient(self) -> math_Vector:
        """
        returns the gradient vector at the minimum.
        Exception NotDone is raised if an error has occurred.
        The minimum was not found.
        """

    @overload
    def Gradient(self, Grad: math_Vector) -> None:
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

    def Dump(self) -> object:
        """
        Prints on the stream o information on the current state
        of the object.
        Is used to redefine the operator <<.
        """

class math_Powell:
    """
    This class implements the Powell method to find the minimum of
    function of multiple variables (the gradient does not have to be known).
    """

    @overload
    def __init__(self, theFunction: math_MultipleVarFunction, theTolerance: float, theNbIterations: int = 200, theZEPS: float = 1e-12) -> None:
        """Constructor. Initialize new entity."""

    @overload
    def __init__(self, theOther: math_Powell) -> None: ...

    def Perform(self, theFunction: math_MultipleVarFunction, theStartingPoint: math_Vector, theStartingDirections: math_Matrix) -> None:
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
    def Location(self) -> math_Vector:
        """
        returns the location vector of the minimum.
        Exception NotDone is raised if the minimum was not found.
        """

    @overload
    def Location(self, Loc: math_Vector) -> None:
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

    def Dump(self) -> object:
        """
        Prints information on the current state of the object.
        Is used to redefine the operator <<.
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

    @overload
    def __init__(self, theFunc: math_MultipleVarFunction, theLowBorder: math_Vector, theUppBorder: math_Vector, theSteps: math_Vector, theNbParticles: int = 32, theNbIter: int = 100) -> None:
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
    def __init__(self, theOther: math_PSO) -> None: ...

    @overload
    def Perform(self, theSteps: math_Vector, theOutPnt: math_Vector, theNbIter: int = 100) -> float:
        """
        Perform computations, particles array is constructed inside of this function.
        """

    @overload
    def Perform(self, theParticles: math_PSOParticlesPool, theNbParticles: int, theOutPnt: math_Vector, theNbIter: int = 100) -> float:
        """Perform computations with given particles array."""

class PSO_Particle:
    """
    Describes particle pool for using in PSO algorithm.
    Indexes:
    0 <= aDimidx <= myDimensionCount - 1
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: PSO_Particle) -> None: ...

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
    @overload
    def __init__(self, theParticlesCount: int, theDimensionCount: int) -> None: ...

    @overload
    def __init__(self, theOther: math_PSOParticlesPool) -> None: ...

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

    @overload
    def __init__(self, A: math_Matrix) -> None:
        """
        Given as input an n X m matrix A with n < m, n = m or n > m
        this constructor performs the Singular Value Decomposition.
        """

    @overload
    def __init__(self, theOther: math_SVD) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def Solve(self, B: math_Vector, X: math_Vector, Eps: float = 1e-06) -> None:
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

    def Dump(self) -> object:
        """
        Prints information on the current state of the object.
        Is used to redefine the operator <<.
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

    @overload
    def __init__(self, theOther: math_TrigonometricFunctionRoots) -> None: ...

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

    def Dump(self) -> object:
        """Prints information on the current state of the object."""

class math_TrigonometricEquationFunction(math_FunctionWithDerivative):
    """
    This is function, which corresponds trigonometric equation
    a*std::cos(x)*std::cos(x) + 2*b*std::cos(x)*Sin(x) + c*std::cos(x) + d*Sin(x) + e = 0
    See class math_TrigonometricFunctionRoots
    """

    @overload
    def __init__(self, A: float, B: float, C: float, D: float, E: float) -> None: ...

    @overload
    def __init__(self, theOther: math_TrigonometricEquationFunction) -> None: ...

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
    def __init__(self, Cont: math_Matrix, Secont: math_Vector, StartingPoint: math_Vector, EpsLix: float = 1e-06, EpsLic: float = 1e-06, NbIterations: int = 500) -> None:
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
    def __init__(self, Cont: math_Matrix, Secont: math_Vector, StartingPoint: math_Vector, Nci: int, Nce: int, EpsLix: float = 1e-06, EpsLic: float = 1e-06, NbIterations: int = 500) -> None:
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

    @overload
    def __init__(self, theOther: math_Uzawa) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns true if the computations are successful, otherwise returns false.
        """

    def Value(self) -> math_Vector:
        """
        Returns the vector solution of the system above.
        An exception is raised if NotDone.
        """

    def InitialError(self) -> math_Vector:
        """
        Returns the initial error Cont*StartingPoint-Secont.
        An exception is raised if NotDone.
        """

    def Duale(self, V: math_Vector) -> None:
        """returns the duale variables V of the systeme."""

    def Error(self) -> math_Vector:
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

    def Dump(self) -> object:
        """Prints information on the current state of the object."""

class math_ValueAndWeight:
    """Simple container storing two reals: value and weight"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theValue: float, theWeight: float) -> None: ...

    @overload
    def __init__(self, theOther: math_ValueAndWeight) -> None: ...

    def Value(self) -> float: ...

    def Weight(self) -> float: ...

    def __lt__(self, arg: math_ValueAndWeight, /) -> bool: ...

@overload
def LU_Decompose(a: math_Matrix, indx: math_IntegerVector, TINY: float = 1e-20, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[int, float]: ...

@overload
def LU_Decompose(a: math_Matrix, indx: math_IntegerVector, vv: math_Vector, TINY: float = 1e-30, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[int, float]: ...

def LU_Solve(a: math_Matrix, indx: math_IntegerVector, b: math_Vector) -> None: ...

def LU_Invert(a: math_Matrix) -> int: ...

@overload
def SVD_Decompose(a: math_Matrix, w: math_Vector, v: math_Matrix) -> int: ...

@overload
def SVD_Decompose(a: math_Matrix, w: math_Vector, v: math_Matrix, rv1: math_Vector) -> int: ...

def SVD_Solve(u: math_Matrix, w: math_Vector, v: math_Matrix, b: math_Vector, x: math_Vector) -> None: ...

def DACTCL_Decompose(a: math_Vector, indx: math_IntegerVector, MinPivot: float = 1e-20) -> int: ...

def DACTCL_Solve(a: math_Vector, b: math_Vector, indx: math_IntegerVector, MinPivot: float = 1e-20) -> int: ...

def Jacobi(a: math_Matrix, d: math_Vector, v: math_Matrix) -> tuple[int, int]: ...
