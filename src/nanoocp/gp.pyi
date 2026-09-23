"""OCCT package gp (toolkit TKMath)"""

import enum
from typing import TextIO, overload

import nanoocp.Geom2dAPI
import nanoocp.GeomAPI
import nanoocp.NCollection
import nanoocp.Select3D
import nanoocp.Standard
import nanoocp.TopLoc
import nanoocp.gce


class gp_TrsfForm(enum.IntEnum):
    """Identifies the type of a geometric transformation."""

    gp_Identity = 0

    gp_Rotation = 1

    gp_Translation = 2

    gp_PntMirror = 3

    gp_Ax1Mirror = 4

    gp_Ax2Mirror = 5

    gp_Scale = 6

    gp_CompoundTrsf = 7

    gp_Other = 8

gp_Identity: gp_TrsfForm = gp_TrsfForm.gp_Identity

gp_Rotation: gp_TrsfForm = gp_TrsfForm.gp_Rotation

gp_Translation: gp_TrsfForm = gp_TrsfForm.gp_Translation

gp_PntMirror: gp_TrsfForm = gp_TrsfForm.gp_PntMirror

gp_Ax1Mirror: gp_TrsfForm = gp_TrsfForm.gp_Ax1Mirror

gp_Ax2Mirror: gp_TrsfForm = gp_TrsfForm.gp_Ax2Mirror

gp_Scale: gp_TrsfForm = gp_TrsfForm.gp_Scale

gp_CompoundTrsf: gp_TrsfForm = gp_TrsfForm.gp_CompoundTrsf

gp_Other: gp_TrsfForm = gp_TrsfForm.gp_Other

class gp_EulerSequence(enum.IntEnum):
    """
    Enumerates all 24 possible variants of generalized
    Euler angles, defining general 3d rotation by three
    rotations around main axes of coordinate system,
    in different possible orders.

    The name of the enumeration
    corresponds to order of rotations, prefixed by type
    of coordinate system used:
    - Intrinsic: rotations are made around axes of rotating
    coordinate system associated with the object
    - Extrinsic: rotations are made around axes of fixed
    (static) coordinate system

    Two specific values are provided for most frequently used
    conventions: classic Euler angles (intrinsic ZXZ) and
    yaw-pitch-roll (intrinsic ZYX).
    """

    gp_EulerAngles = 0

    gp_YawPitchRoll = 1

    gp_Extrinsic_XYZ = 2

    gp_Extrinsic_XZY = 3

    gp_Extrinsic_YZX = 4

    gp_Extrinsic_YXZ = 5

    gp_Extrinsic_ZXY = 6

    gp_Extrinsic_ZYX = 7

    gp_Intrinsic_XYZ = 8

    gp_Intrinsic_XZY = 9

    gp_Intrinsic_YZX = 10

    gp_Intrinsic_YXZ = 11

    gp_Intrinsic_ZXY = 12

    gp_Intrinsic_ZYX = 13

    gp_Extrinsic_XYX = 14

    gp_Extrinsic_XZX = 15

    gp_Extrinsic_YZY = 16

    gp_Extrinsic_YXY = 17

    gp_Extrinsic_ZYZ = 18

    gp_Extrinsic_ZXZ = 19

    gp_Intrinsic_XYX = 20

    gp_Intrinsic_XZX = 21

    gp_Intrinsic_YZY = 22

    gp_Intrinsic_YXY = 23

    gp_Intrinsic_ZXZ = 24

    gp_Intrinsic_ZYZ = 25

gp_EulerAngles: gp_EulerSequence = gp_EulerSequence.gp_EulerAngles

gp_YawPitchRoll: gp_EulerSequence = gp_EulerSequence.gp_YawPitchRoll

gp_Extrinsic_XYZ: gp_EulerSequence = gp_EulerSequence.gp_Extrinsic_XYZ

gp_Extrinsic_XZY: gp_EulerSequence = gp_EulerSequence.gp_Extrinsic_XZY

gp_Extrinsic_YZX: gp_EulerSequence = gp_EulerSequence.gp_Extrinsic_YZX

gp_Extrinsic_YXZ: gp_EulerSequence = gp_EulerSequence.gp_Extrinsic_YXZ

gp_Extrinsic_ZXY: gp_EulerSequence = gp_EulerSequence.gp_Extrinsic_ZXY

gp_Extrinsic_ZYX: gp_EulerSequence = gp_EulerSequence.gp_Extrinsic_ZYX

gp_Intrinsic_XYZ: gp_EulerSequence = gp_EulerSequence.gp_Intrinsic_XYZ

gp_Intrinsic_XZY: gp_EulerSequence = gp_EulerSequence.gp_Intrinsic_XZY

gp_Intrinsic_YZX: gp_EulerSequence = gp_EulerSequence.gp_Intrinsic_YZX

gp_Intrinsic_YXZ: gp_EulerSequence = gp_EulerSequence.gp_Intrinsic_YXZ

gp_Intrinsic_ZXY: gp_EulerSequence = gp_EulerSequence.gp_Intrinsic_ZXY

gp_Intrinsic_ZYX: gp_EulerSequence = gp_EulerSequence.gp_Intrinsic_ZYX

gp_Extrinsic_XYX: gp_EulerSequence = gp_EulerSequence.gp_Extrinsic_XYX

gp_Extrinsic_XZX: gp_EulerSequence = gp_EulerSequence.gp_Extrinsic_XZX

gp_Extrinsic_YZY: gp_EulerSequence = gp_EulerSequence.gp_Extrinsic_YZY

gp_Extrinsic_YXY: gp_EulerSequence = gp_EulerSequence.gp_Extrinsic_YXY

gp_Extrinsic_ZYZ: gp_EulerSequence = gp_EulerSequence.gp_Extrinsic_ZYZ

gp_Extrinsic_ZXZ: gp_EulerSequence = gp_EulerSequence.gp_Extrinsic_ZXZ

gp_Intrinsic_XYX: gp_EulerSequence = gp_EulerSequence.gp_Intrinsic_XYX

gp_Intrinsic_XZX: gp_EulerSequence = gp_EulerSequence.gp_Intrinsic_XZX

gp_Intrinsic_YZY: gp_EulerSequence = gp_EulerSequence.gp_Intrinsic_YZY

gp_Intrinsic_YXY: gp_EulerSequence = gp_EulerSequence.gp_Intrinsic_YXY

gp_Intrinsic_ZXZ: gp_EulerSequence = gp_EulerSequence.gp_Intrinsic_ZXZ

gp_Intrinsic_ZYZ: gp_EulerSequence = gp_EulerSequence.gp_Intrinsic_ZYZ

class gp:
    """
    The geometric processor package, called gp, provides an
    implementation of entities used:
    . for algebraic calculation such as "XYZ" coordinates, "Mat"
    matrix
    . for basis analytic geometry such as Transformations, point,
    vector, line, plane, axis placement, conics, and elementary
    surfaces.
    These entities are defined in 2d and 3d space.
    All the classes of this package are non-persistent.
    This is a utility class that cannot be instantiated.
    """

    @staticmethod
    def Resolution() -> float:
        """
        Method of package gp

        In geometric computations, defines the tolerance criterion
        used to determine when two numbers can be considered equal.
        Many class functions use this tolerance criterion, for
        example, to avoid division by zero in geometric
        computations. In the documentation, tolerance criterion is
        always referred to as gp::Resolution().
        """

    @staticmethod
    def Origin() -> gp_Pnt:
        """Identifies a Cartesian point with coordinates X = Y = Z = 0.0.0"""

    @staticmethod
    def DX() -> gp_Dir:
        """Returns a unit vector with the combination (1,0,0)"""

    @staticmethod
    def DY() -> gp_Dir:
        """Returns a unit vector with the combination (0,1,0)"""

    @staticmethod
    def DZ() -> gp_Dir:
        """Returns a unit vector with the combination (0,0,1)"""

    @staticmethod
    def OX() -> gp_Ax1:
        """
        Identifies an axis where its origin is Origin
        and its unit vector coordinates X = 1.0, Y = Z = 0.0
        """

    @staticmethod
    def OY() -> gp_Ax1:
        """
        Identifies an axis where its origin is Origin
        and its unit vector coordinates Y = 1.0, X = Z = 0.0
        """

    @staticmethod
    def OZ() -> gp_Ax1:
        """
        Identifies an axis where its origin is Origin
        and its unit vector coordinates Z = 1.0, Y = X = 0.0
        """

    @staticmethod
    def XOY() -> gp_Ax2:
        """
        Identifies a coordinate system where its origin is Origin,
        and its "main Direction" and "X Direction" coordinates
        Z = 1.0, X = Y =0.0 and X direction coordinates X = 1.0, Y = Z = 0.0
        """

    @staticmethod
    def ZOX() -> gp_Ax2:
        """
        Identifies a coordinate system where its origin is Origin,
        and its "main Direction" and "X Direction" coordinates
        Y = 1.0, X = Z =0.0 and X direction coordinates Z = 1.0, X = Y = 0.0
        """

    @staticmethod
    def YOZ() -> gp_Ax2:
        """
        Identifies a coordinate system where its origin is Origin,
        and its "main Direction" and "X Direction" coordinates
        X = 1.0, Z = Y =0.0 and X direction coordinates Y = 1.0, X = Z = 0.0
        In 2D space
        """

    @staticmethod
    def Origin2d() -> gp_Pnt2d:
        """Identifies a Cartesian point with coordinates X = Y = 0.0"""

    @staticmethod
    def DX2d() -> gp_Dir2d:
        """Returns a unit vector with the combinations (1,0)"""

    @staticmethod
    def DY2d() -> gp_Dir2d:
        """Returns a unit vector with the combinations (0,1)"""

    @staticmethod
    def OX2d() -> gp_Ax2d:
        """
        Identifies an axis where its origin is Origin2d
        and its unit vector coordinates are: X = 1.0, Y = 0.0
        """

    @staticmethod
    def OY2d() -> gp_Ax2d:
        """
        Identifies an axis where its origin is Origin2d
        and its unit vector coordinates are Y = 1.0, X = 0.0
        """

class gp_Mat:
    """
    Describes a three column, three row matrix.
    This sort of object is used in various vectorial or matrix computations.
    """

    @overload
    def __init__(self) -> None:
        """Creates a matrix with null coefficients."""

    @overload
    def __init__(self, theCol1: gp_XYZ, theCol2: gp_XYZ, theCol3: gp_XYZ) -> None:
        """
        Creates a matrix.
        theCol1, theCol2, theCol3 are the 3 columns of the matrix.
        """

    @overload
    def __init__(self, theA11: float, theA12: float, theA13: float, theA21: float, theA22: float, theA23: float, theA31: float, theA32: float, theA33: float) -> None: ...

    @overload
    def __init__(self, theOther: gp_Mat) -> None: ...

    def SetCol(self, theCol: int, theValue: gp_XYZ) -> None:
        """
        Assigns the three coordinates of theValue to the column of index
        theCol of this matrix.
        Raises OutOfRange if theCol < 1 or theCol > 3.
        """

    def SetCols(self, theCol1: gp_XYZ, theCol2: gp_XYZ, theCol3: gp_XYZ) -> None:
        """
        Assigns the number triples theCol1, theCol2, theCol3 to the three
        columns of this matrix.
        """

    def SetCross(self, theRef: gp_XYZ) -> None:
        """
        Modifies the matrix M so that applying it to any number
        triple (X, Y, Z) produces the same result as the cross
        product of theRef and the number triple (X, Y, Z):
        i.e.: M * {X,Y,Z}t = theRef.Cross({X, Y ,Z})
        this matrix is anti symmetric. To apply this matrix to the
        triplet {XYZ} is the same as to do the cross product between the
        triplet theRef and the triplet {XYZ}.
        Note: this matrix is anti-symmetric.
        """

    def SetDiagonal(self, theX1: float, theX2: float, theX3: float) -> None:
        """
        Modifies the main diagonal of the matrix.
        @code
        <me>.Value (1, 1) = theX1
        <me>.Value (2, 2) = theX2
        <me>.Value (3, 3) = theX3
        @endcode
        The other coefficients of the matrix are not modified.
        """

    def SetDot(self, theRef: gp_XYZ) -> None:
        """
        Modifies this matrix so that applying it to any number
        triple (X, Y, Z) produces the same result as the scalar
        product of theRef and the number triple (X, Y, Z):
        this * (X,Y,Z) = theRef.(X,Y,Z)
        Note: this matrix is symmetric.
        """

    def SetIdentity(self) -> None:
        """Modifies this matrix so that it represents the Identity matrix."""

    def SetRotation(self, theAxis: gp_XYZ, theAng: float) -> None:
        """
        Modifies this matrix so that it represents a rotation. theAng is the angular value in
        radians and the XYZ axis gives the direction of the
        rotation.
        Raises ConstructionError if XYZ.Modulus() <= Resolution()
        """

    def SetRow(self, theRow: int, theValue: gp_XYZ) -> None:
        """
        Assigns the three coordinates of Value to the row of index
        theRow of this matrix. Raises OutOfRange if theRow < 1 or theRow > 3.
        """

    def SetRows(self, theRow1: gp_XYZ, theRow2: gp_XYZ, theRow3: gp_XYZ) -> None:
        """
        Assigns the number triples theRow1, theRow2, theRow3 to the three
        rows of this matrix.
        """

    def SetScale(self, theS: float) -> None:
        """
        Modifies the matrix so that it represents
        a scaling transformation, where theS is the scale factor. :
        @code
        | theS    0.0  0.0 |
        <me> =  | 0.0   theS   0.0 |
        | 0.0  0.0   theS  |
        @endcode
        """

    def SetValue(self, theRow: int, theCol: int, theValue: float) -> None:
        """
        Assigns <theValue> to the coefficient of row theRow, column theCol of this matrix.
        Raises OutOfRange if theRow < 1 or theRow > 3 or theCol < 1 or theCol > 3
        """

    def Column(self, theCol: int) -> gp_XYZ:
        """
        Returns the column of theCol index.
        Raises OutOfRange if theCol < 1 or theCol > 3
        """

    def Determinant(self) -> float:
        """Computes the determinant of the matrix."""

    def Diagonal(self) -> gp_XYZ:
        """Returns the main diagonal of the matrix."""

    def Row(self, theRow: int) -> gp_XYZ:
        """
        returns the row of theRow index.
        Raises OutOfRange if theRow < 1 or theRow > 3
        """

    def Value(self, theRow: int, theCol: int) -> float:
        """
        Returns the coefficient of range (theRow, theCol)
        Raises OutOfRange if theRow < 1 or theRow > 3 or theCol < 1 or theCol > 3
        """

    def ChangeValue(self, theRow: int, theCol: int) -> float:
        """
        Returns the coefficient of range (theRow, theCol)
        Raises OutOfRange if theRow < 1 or theRow > 3 or theCol < 1 or theCol > 3
        """

    def __call__(self, theRow: int, theCol: int) -> float: ...

    def __getitem__(self, arg: tuple[int, int], /) -> float:
        """Python addition: alias to operator()."""

    def __setitem__(self, arg0: tuple[int, int], arg1: float, /) -> None:
        """
        Python addition: sets the value operator()(theRow, theCol) returns by reference in C++.
        """

    def IsSingular(self) -> bool:
        """
        The Gauss LU decomposition is used to invert the matrix
        (see Math package) so the matrix is considered as singular if
        the largest pivot found is lower or equal to Resolution from gp.
        """

    def Add(self, theOther: gp_Mat) -> None: ...

    def __iadd__(self, theOther: gp_Mat) -> gp_Mat: ...

    def Added(self, theOther: gp_Mat) -> gp_Mat:
        """
        Computes the sum of this matrix and
        the matrix theOther for each coefficient of the matrix :
        <me>.Coef(i,j) + <theOther>.Coef(i,j)
        """

    def __add__(self, theOther: gp_Mat) -> gp_Mat: ...

    def Divide(self, theScalar: float) -> None: ...

    def __itruediv__(self, theScalar: float) -> gp_Mat: ...

    def Divided(self, theScalar: float) -> gp_Mat:
        """Divides all the coefficients of the matrix by Scalar"""

    def __truediv__(self, theScalar: float) -> gp_Mat: ...

    def Invert(self) -> None: ...

    def Inverted(self) -> gp_Mat:
        """
        Inverses the matrix and raises if the matrix is singular.
        -   Invert assigns the result to this matrix, while
        -   Inverted creates a new one.
        Warning
        The Gauss LU decomposition is used to invert the matrix.
        Consequently, the matrix is considered as singular if the
        largest pivot found is less than or equal to gp::Resolution().
        Exceptions
        Standard_ConstructionError if this matrix is singular,
        and therefore cannot be inverted.
        """

    @overload
    def Multiplied(self, theOther: gp_Mat) -> gp_Mat:
        """Computes the product of two matrices <me> * <Other>"""

    @overload
    def Multiplied(self, theScalar: float) -> gp_Mat: ...

    @overload
    def __mul__(self, theOther: gp_Mat) -> gp_Mat: ...

    @overload
    def __mul__(self, theScalar: float) -> gp_Mat: ...

    @overload
    def __mul__(self, arg: gp_XYZ, /) -> gp_XYZ: ...

    @overload
    def Multiply(self, theOther: gp_Mat) -> None:
        """Computes the product of two matrices <me> = <Other> * <me>."""

    @overload
    def Multiply(self, theScalar: float) -> None:
        """Multiplies all the coefficients of the matrix by Scalar"""

    @overload
    def __imul__(self, theOther: gp_Mat) -> gp_Mat: ...

    @overload
    def __imul__(self, theScalar: float) -> gp_Mat: ...

    def PreMultiply(self, theOther: gp_Mat) -> None: ...

    def Power(self, N: int) -> None: ...

    def Powered(self, theN: int) -> gp_Mat:
        """
        Computes <me> = <me> * <me> * .......* <me>, theN time.
        if theN = 0 <me> = Identity
        if theN < 0 <me> = <me>.Invert() *...........* <me>.Invert().
        If theN < 0 an exception will be raised if the matrix is not
        inversible
        """

    def Subtract(self, theOther: gp_Mat) -> None: ...

    def __isub__(self, theOther: gp_Mat) -> gp_Mat: ...

    def Subtracted(self, theOther: gp_Mat) -> gp_Mat:
        """
        cOmputes for each coefficient of the matrix :
        <me>.Coef(i,j) - <theOther>.Coef(i,j)
        """

    def __sub__(self, theOther: gp_Mat) -> gp_Mat: ...

    def Transpose(self) -> None: ...

    def Transposed(self) -> gp_Mat:
        """Transposes the matrix. A(j, i) -> A (i, j)"""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def __rmul__(self, arg: float, /) -> gp_Mat: ...

class gp_XYZ:
    """
    This class describes a cartesian coordinate entity in
    3D space {X,Y,Z}. This entity is used for algebraic
    calculation. This entity can be transformed
    with a "Trsf" or a "GTrsf" from package "gp".
    It is used in vectorial computations or for holding this type
    of information in data structures.
    """

    @overload
    def __init__(self) -> None:
        """Creates an XYZ object with zero coordinates (0,0,0)"""

    @overload
    def __init__(self, theX: float, theY: float, theZ: float) -> None:
        """creates an XYZ with given coordinates"""

    @overload
    def __init__(self, theOther: gp_XYZ) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.Select3D.Select3D_Pnt) -> None: ...

    @overload
    def SetCoord(self, theX: float, theY: float, theZ: float) -> None:
        """
        For this XYZ object, assigns
        the values theX, theY and theZ to its three coordinates
        """

    @overload
    def SetCoord(self, theIndex: int, theXi: float) -> None:
        """
        modifies the coordinate of range theIndex
        theIndex = 1 => X is modified
        theIndex = 2 => Y is modified
        theIndex = 3 => Z is modified
        Raises OutOfRange if theIndex != {1, 2, 3}.
        """

    def SetX(self, theX: float) -> None:
        """Assigns the given value to the X coordinate"""

    def SetY(self, theY: float) -> None:
        """Assigns the given value to the Y coordinate"""

    def SetZ(self, theZ: float) -> None:
        """Assigns the given value to the Z coordinate"""

    @overload
    def Coord(self, theIndex: int) -> float:
        """
        returns the coordinate of range theIndex :
        theIndex = 1 => X is returned
        theIndex = 2 => Y is returned
        theIndex = 3 => Z is returned

        Raises OutOfRange if theIndex != {1, 2, 3}.
        """

    @overload
    def Coord(self) -> tuple[float, float, float]: ...

    def ChangeCoord(self, theIndex: int) -> float: ...

    def X(self) -> float:
        """Returns the X coordinate"""

    def Y(self) -> float:
        """Returns the Y coordinate"""

    def Z(self) -> float:
        """Returns the Z coordinate"""

    def Modulus(self) -> float:
        """
        Computes std::sqrt(X*X + Y*Y + Z*Z) where X, Y and Z are the three coordinates of this XYZ
        object.
        """

    def SquareModulus(self) -> float:
        """
        Computes X*X + Y*Y + Z*Z where X, Y and Z are the three coordinates of this XYZ object.
        """

    def IsEqual(self, theOther: gp_XYZ, theTolerance: float) -> bool:
        """
        Returns True if he coordinates of this XYZ object are
        equal to the respective coordinates Other,
        within the specified tolerance theTolerance.
        """

    def Add(self, theOther: gp_XYZ) -> None:
        """
        @code
        <me>.X() = <me>.X() + theOther.X()
        <me>.Y() = <me>.Y() + theOther.Y()
        <me>.Z() = <me>.Z() + theOther.Z()
        @endcode
        """

    def __iadd__(self, theOther: gp_XYZ) -> gp_XYZ: ...

    def Added(self, theOther: gp_XYZ) -> gp_XYZ:
        """
        @code
        new.X() = <me>.X() + theOther.X()
        new.Y() = <me>.Y() + theOther.Y()
        new.Z() = <me>.Z() + theOther.Z()
        @endcode
        """

    def __add__(self, theOther: gp_XYZ) -> gp_XYZ: ...

    def Cross(self, theOther: gp_XYZ) -> None:
        """
        @code
        <me>.X() = <me>.Y() * theOther.Z() - <me>.Z() * theOther.Y()
        <me>.Y() = <me>.Z() * theOther.X() - <me>.X() * theOther.Z()
        <me>.Z() = <me>.X() * theOther.Y() - <me>.Y() * theOther.X()
        @endcode
        """

    def __ixor__(self, theOther: gp_XYZ) -> gp_XYZ: ...

    def Crossed(self, theOther: gp_XYZ) -> gp_XYZ:
        """
        @code
        new.X() = <me>.Y() * theOther.Z() - <me>.Z() * theOther.Y()
        new.Y() = <me>.Z() * theOther.X() - <me>.X() * theOther.Z()
        new.Z() = <me>.X() * theOther.Y() - <me>.Y() * theOther.X()
        @endcode
        """

    def __xor__(self, theOther: gp_XYZ) -> gp_XYZ: ...

    def CrossMagnitude(self, theRight: gp_XYZ) -> float:
        """
        Computes the magnitude of the cross product between <me> and
        theRight. Returns || <me> ^ theRight ||
        """

    def CrossSquareMagnitude(self, theRight: gp_XYZ) -> float:
        """
        Computes the square magnitude of the cross product between <me> and
        theRight. Returns || <me> ^ theRight ||**2
        """

    def CrossCross(self, theCoord1: gp_XYZ, theCoord2: gp_XYZ) -> None:
        """
        Triple vector product
        Computes <me> = <me>.Cross(theCoord1.Cross(theCoord2))
        """

    def CrossCrossed(self, theCoord1: gp_XYZ, theCoord2: gp_XYZ) -> gp_XYZ:
        """
        Triple vector product
        computes New = <me>.Cross(theCoord1.Cross(theCoord2))
        """

    def Divide(self, theScalar: float) -> None:
        """divides <me> by a real."""

    def __itruediv__(self, theScalar: float) -> gp_XYZ: ...

    def Divided(self, theScalar: float) -> gp_XYZ:
        """divides <me> by a real."""

    def __truediv__(self, theScalar: float) -> gp_XYZ: ...

    def Dot(self, theOther: gp_XYZ) -> float:
        """Computes the scalar product between <me> and theOther."""

    @overload
    def __mul__(self, theOther: gp_XYZ) -> float: ...

    @overload
    def __mul__(self, theScalar: float) -> gp_XYZ: ...

    @overload
    def __mul__(self, theMatrix: gp_Mat) -> gp_XYZ: ...

    def DotCross(self, theCoord1: gp_XYZ, theCoord2: gp_XYZ) -> float:
        """Computes the triple scalar product."""

    @overload
    def Multiply(self, theScalar: float) -> None:
        """
        @code
        <me>.X() = <me>.X() * theScalar;
        <me>.Y() = <me>.Y() * theScalar;
        <me>.Z() = <me>.Z() * theScalar;
        @endcode
        """

    @overload
    def Multiply(self, theOther: gp_XYZ) -> None:
        """
        @code
        <me>.X() = <me>.X() * theOther.X();
        <me>.Y() = <me>.Y() * theOther.Y();
        <me>.Z() = <me>.Z() * theOther.Z();
        @endcode
        """

    @overload
    def Multiply(self, theMatrix: gp_Mat) -> None:
        """<me> = theMatrix * <me>"""

    @overload
    def __imul__(self, theScalar: float) -> gp_XYZ: ...

    @overload
    def __imul__(self, theOther: gp_XYZ) -> gp_XYZ: ...

    @overload
    def __imul__(self, theMatrix: gp_Mat) -> gp_XYZ: ...

    @overload
    def Multiplied(self, theScalar: float) -> gp_XYZ:
        """
        @code
        New.X() = <me>.X() * theScalar;
        New.Y() = <me>.Y() * theScalar;
        New.Z() = <me>.Z() * theScalar;
        @endcode
        """

    @overload
    def Multiplied(self, theOther: gp_XYZ) -> gp_XYZ:
        """
        @code
        new.X() = <me>.X() * theOther.X();
        new.Y() = <me>.Y() * theOther.Y();
        new.Z() = <me>.Z() * theOther.Z();
        @endcode
        """

    @overload
    def Multiplied(self, theMatrix: gp_Mat) -> gp_XYZ:
        """New = theMatrix * <me>"""

    def Normalize(self) -> None:
        """
        @code
        <me>.X() = <me>.X()/ <me>.Modulus()
        <me>.Y() = <me>.Y()/ <me>.Modulus()
        <me>.Z() = <me>.Z()/ <me>.Modulus()
        @endcode
        Raised if <me>.Modulus() <= Resolution from gp
        """

    def Normalized(self) -> gp_XYZ:
        """
        @code
        New.X() = <me>.X()/ <me>.Modulus()
        New.Y() = <me>.Y()/ <me>.Modulus()
        New.Z() = <me>.Z()/ <me>.Modulus()
        @endcode
        Raised if <me>.Modulus() <= Resolution from gp
        """

    def Reverse(self) -> None:
        """
        @code
        <me>.X() = -<me>.X()
        <me>.Y() = -<me>.Y()
        <me>.Z() = -<me>.Z()
        @endcode
        """

    def Reversed(self) -> gp_XYZ:
        """
        @code
        New.X() = -<me>.X()
        New.Y() = -<me>.Y()
        New.Z() = -<me>.Z()
        @endcode
        """

    def Subtract(self, theOther: gp_XYZ) -> None:
        """
        @code
        <me>.X() = <me>.X() - theOther.X()
        <me>.Y() = <me>.Y() - theOther.Y()
        <me>.Z() = <me>.Z() - theOther.Z()
        @endcode
        """

    def __isub__(self, theOther: gp_XYZ) -> gp_XYZ: ...

    def Subtracted(self, theOther: gp_XYZ) -> gp_XYZ:
        """
        @code
        new.X() = <me>.X() - theOther.X()
        new.Y() = <me>.Y() - theOther.Y()
        new.Z() = <me>.Z() - theOther.Z()
        @endcode
        """

    def __sub__(self, theOther: gp_XYZ) -> gp_XYZ: ...

    @overload
    def SetLinearForm(self, theA1: float, theXYZ1: gp_XYZ, theA2: float, theXYZ2: gp_XYZ, theA3: float, theXYZ3: gp_XYZ, theXYZ4: gp_XYZ) -> None:
        """
        <me> is set to the following linear form :
        @code
        theA1 * theXYZ1 + theA2 * theXYZ2 + theA3 * theXYZ3 + theXYZ4
        @endcode
        """

    @overload
    def SetLinearForm(self, theA1: float, theXYZ1: gp_XYZ, theA2: float, theXYZ2: gp_XYZ, theA3: float, theXYZ3: gp_XYZ) -> None:
        """
        <me> is set to the following linear form :
        @code
        theA1 * theXYZ1 + theA2 * theXYZ2 + theA3 * theXYZ3
        @endcode
        """

    @overload
    def SetLinearForm(self, theA1: float, theXYZ1: gp_XYZ, theA2: float, theXYZ2: gp_XYZ, theXYZ3: gp_XYZ) -> None:
        """
        <me> is set to the following linear form :
        @code
        theA1 * theXYZ1 + theA2 * theXYZ2 + theXYZ3
        @endcode
        """

    @overload
    def SetLinearForm(self, theA1: float, theXYZ1: gp_XYZ, theA2: float, theXYZ2: gp_XYZ) -> None:
        """
        <me> is set to the following linear form :
        @code
        theA1 * theXYZ1 + theA2 * theXYZ2
        @endcode
        """

    @overload
    def SetLinearForm(self, theA1: float, theXYZ1: gp_XYZ, theXYZ2: gp_XYZ) -> None:
        """
        <me> is set to the following linear form :
        @code
        theA1 * theXYZ1 + theXYZ2
        @endcode
        """

    @overload
    def SetLinearForm(self, theXYZ1: gp_XYZ, theXYZ2: gp_XYZ) -> None:
        """
        <me> is set to the following linear form :
        @code
        theXYZ1 + theXYZ2
        @endcode
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def InitFromJson(self, theSStream: TextIO, theStreamPos: int) -> tuple[bool, int]:
        """Inits the content of me from the stream"""

    def __rmul__(self, arg: float, /) -> gp_XYZ: ...

class gp_Pnt:
    """Defines a 3D cartesian point."""

    @overload
    def __init__(self) -> None:
        """Creates a point with zero coordinates."""

    @overload
    def __init__(self, theCoord: gp_XYZ) -> None:
        """Creates a point from a XYZ object."""

    @overload
    def __init__(self, theXp: float, theYp: float, theZp: float) -> None:
        """
        Creates a point with its 3 cartesian's coordinates: theXp, theYp, theZp.
        """

    @overload
    def __init__(self, theOther: gp_Pnt) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.GeomAPI.GeomAPI_ProjectPointOnCurve) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.GeomAPI.GeomAPI_ProjectPointOnSurf) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.Select3D.Select3D_Pnt) -> None: ...

    @overload
    def SetCoord(self, theIndex: int, theXi: float) -> None:
        """
        Changes the coordinate of range theIndex:
        theIndex = 1 => X is modified
        theIndex = 2 => Y is modified
        theIndex = 3 => Z is modified
        Raised if theIndex != {1, 2, 3}.
        """

    @overload
    def SetCoord(self, theXp: float, theYp: float, theZp: float) -> None:
        """
        For this point, assigns the values theXp, theYp and theZp to its three coordinates.
        """

    def SetX(self, theX: float) -> None:
        """Assigns the given value to the X coordinate of this point."""

    def SetY(self, theY: float) -> None:
        """Assigns the given value to the Y coordinate of this point."""

    def SetZ(self, theZ: float) -> None:
        """Assigns the given value to the Z coordinate of this point."""

    def SetXYZ(self, theCoord: gp_XYZ) -> None:
        """Assigns the three coordinates of theCoord to this point."""

    @overload
    def Coord(self, theIndex: int) -> float:
        """
        Returns the coordinate of corresponding to the value of theIndex :
        theIndex = 1 => X is returned
        theIndex = 2 => Y is returned
        theIndex = 3 => Z is returned
        Raises OutOfRange if theIndex != {1, 2, 3}.
        Raised if theIndex != {1, 2, 3}.
        """

    @overload
    def Coord(self) -> gp_XYZ:
        """For this point, returns its three coordinates as a XYZ object."""

    def Coord__float__float__float(self) -> tuple[float, float, float]:
        """
        Coord__float__float__float: the C++ overload Coord(double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        For this point gives its three coordinates theXp, theYp and theZp.
        """

    def X(self) -> float:
        """For this point, returns its X coordinate."""

    def Y(self) -> float:
        """For this point, returns its Y coordinate."""

    def Z(self) -> float:
        """For this point, returns its Z coordinate."""

    def XYZ(self) -> gp_XYZ:
        """For this point, returns its three coordinates as a XYZ object."""

    def ChangeCoord(self) -> gp_XYZ:
        """
        Returns the coordinates of this point.
        Note: This syntax allows direct modification of the returned value.
        """

    def BaryCenter(self, theAlpha: float, theP: gp_Pnt, theBeta: float) -> None:
        """
        Assigns the result of the following expression to this point
        (theAlpha*this + theBeta*theP) / (theAlpha + theBeta)
        """

    def IsEqual(self, theOther: gp_Pnt, theLinearTolerance: float) -> bool:
        """
        Comparison
        Returns True if the distance between the two points is
        lower or equal to theLinearTolerance.
        """

    def Distance(self, theOther: gp_Pnt) -> float:
        """Computes the distance between two points."""

    def SquareDistance(self, theOther: gp_Pnt) -> float:
        """Computes the square distance between two points."""

    @overload
    def Mirror(self, theP: gp_Pnt) -> None:
        """
        Performs the symmetrical transformation of a point
        with respect to the point theP which is the center of
        the symmetry.
        """

    @overload
    def Mirror(self, theA1: gp_Ax1) -> None: ...

    @overload
    def Mirror(self, theA2: gp_Ax2) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt) -> gp_Pnt:
        """
        Performs the symmetrical transformation of a point
        with respect to an axis placement which is the axis
        of the symmetry.
        """

    @overload
    def Mirrored(self, theA1: gp_Ax1) -> gp_Pnt:
        """
        Performs the symmetrical transformation of a point
        with respect to a plane. The axis placement theA2 locates
        the plane of the symmetry : (Location, XDirection, YDirection).
        """

    @overload
    def Mirrored(self, theA2: gp_Ax2) -> gp_Pnt:
        """
        Rotates a point. theA1 is the axis of the rotation.
        theAng is the angular value of the rotation in radians.
        """

    def Rotate(self, theA1: gp_Ax1, theAng: float) -> None: ...

    def Rotated(self, theA1: gp_Ax1, theAng: float) -> gp_Pnt: ...

    def Scale(self, theP: gp_Pnt, theS: float) -> None:
        """Scales a point. theS is the scaling value."""

    def Scaled(self, theP: gp_Pnt, theS: float) -> gp_Pnt: ...

    def Transform(self, theT: gp_Trsf) -> None:
        """Transforms a point with the transformation T."""

    def Transformed(self, theT: gp_Trsf) -> gp_Pnt: ...

    @overload
    def Translate(self, theV: gp_Vec) -> None:
        """
        Translates a point in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translate(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None:
        """Translates a point from the point theP1 to the point theP2."""

    @overload
    def Translated(self, theV: gp_Vec) -> gp_Pnt: ...

    @overload
    def Translated(self, theP1: gp_Pnt, theP2: gp_Pnt) -> gp_Pnt: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def InitFromJson(self, theSStream: TextIO, theStreamPos: int) -> tuple[bool, int]:
        """Inits the content of me from the stream"""

    def __hash__(self) -> int: ...

class gp_Trsf:
    """
    Defines a non-persistent transformation in 3D space.
    The following transformations are implemented :
    . Translation, Rotation, Scale
    . Symmetry with respect to a point, a line, a plane.
    Complex transformations can be obtained by combining the
    previous elementary transformations using the method
    Multiply.
    The transformations can be represented as follow :
    @code
    V1   V2   V3    T       XYZ        XYZ
    | a11  a12  a13   a14 |   | x |      | x'|
    | a21  a22  a23   a24 |   | y |      | y'|
    | a31  a32  a33   a34 |   | z |   =  | z'|
    |  0    0    0     1  |   | 1 |      | 1 |
    @endcode
    where {V1, V2, V3} defines the vectorial part of the
    transformation and T defines the translation part of the
    transformation.
    This transformation never change the nature of the objects.
    """

    @overload
    def __init__(self) -> None:
        """Returns the identity transformation."""

    @overload
    def __init__(self, theT: gp_Trsf2d) -> None:
        """
        Creates a 3D transformation from the 2D transformation theT.
        The resulting transformation has a homogeneous
        vectorial part, V3, and a translation part, T3, built from theT:
        a11    a12
        0             a13
        V3 =    a21    a22    0       T3
        =   a23
        0    0    1.
        0
        It also has the same scale factor as theT. This
        guarantees (by projection) that the transformation
        which would be performed by theT in a plane (2D space)
        is performed by the resulting transformation in the xOy
        plane of the 3D space, (i.e. in the plane defined by the
        origin (0., 0., 0.) and the vectors DX (1., 0., 0.), and DY
        (0., 1., 0.)). The scale factor is applied to the entire space.
        """

    @overload
    def __init__(self, theOther: gp_Trsf) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeMirror) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeRotation) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeScale) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeTranslation) -> None: ...

    @overload
    def SetMirror(self, theP: gp_Pnt) -> None:
        """
        Makes the transformation into a symmetrical transformation.
        theP is the center of the symmetry.
        """

    @overload
    def SetMirror(self, theA1: gp_Ax1) -> None:
        """
        Makes the transformation into a symmetrical transformation.
        theA1 is the center of the axial symmetry.
        """

    @overload
    def SetMirror(self, theA2: gp_Ax2) -> None:
        """
        Makes the transformation into a symmetrical transformation.
        theA2 is the center of the planar symmetry
        and defines the plane of symmetry by its origin, "X
        Direction" and "Y Direction".
        """

    @overload
    def SetRotation(self, theA1: gp_Ax1, theAng: float) -> None:
        """
        Changes the transformation into a rotation.
        theA1 is the rotation axis and theAng is the angular value of the
        rotation in radians.
        """

    @overload
    def SetRotation(self, theR: gp_Quaternion) -> None:
        """
        Changes the transformation into a rotation defined by quaternion.
        Note that rotation is performed around origin, i.e.
        no translation is involved.
        """

    def SetRotationPart(self, theR: gp_Quaternion) -> None:
        """Replaces the rotation part with specified quaternion."""

    def SetScale(self, theP: gp_Pnt, theS: float) -> None:
        """
        Changes the transformation into a scale.
        theP is the center of the scale and theS is the scaling value.
        Raises ConstructionError If <theS> is null.
        """

    def SetDisplacement(self, theFromSystem1: gp_Ax3, theToSystem2: gp_Ax3) -> None:
        """
        Modifies this transformation so that it transforms the
        coordinate system defined by theFromSystem1 into the
        one defined by theToSystem2. After this modification, this
        transformation transforms:
        -   the origin of theFromSystem1 into the origin of theToSystem2,
        -   the "X Direction" of theFromSystem1 into the "X
        Direction" of theToSystem2,
        -   the "Y Direction" of theFromSystem1 into the "Y
        Direction" of theToSystem2, and
        -   the "main Direction" of theFromSystem1 into the "main
        Direction" of theToSystem2.
        Warning
        When you know the coordinates of a point in one
        coordinate system and you want to express these
        coordinates in another one, do not use the
        transformation resulting from this function. Use the
        transformation that results from SetTransformation instead.
        SetDisplacement and SetTransformation create
        related transformations: the vectorial part of one is the
        inverse of the vectorial part of the other.
        """

    @overload
    def SetTransformation(self, theFromSystem1: gp_Ax3, theToSystem2: gp_Ax3) -> None:
        """
        Modifies this transformation so that it transforms the
        coordinates of any point, (x, y, z), relative to a source
        coordinate system into the coordinates (x', y', z') which
        are relative to a target coordinate system, but which
        represent the same point
        The transformation is from the coordinate
        system "theFromSystem1" to the coordinate system "theToSystem2".
        Example :
        @code
        gp_Ax3 theFromSystem1, theToSystem2;
        double x1, y1, z1;  // are the coordinates of a point in the local system theFromSystem1
        double x2, y2, z2;  // are the coordinates of a point in the local system theToSystem2
        gp_Pnt P1 (x1, y1, z1)
        gp_Trsf T;
        T.SetTransformation (theFromSystem1, theToSystem2);
        gp_Pnt P2 = P1.Transformed (T);
        P2.Coord (x2, y2, z2);
        @endcode
        """

    @overload
    def SetTransformation(self, theToSystem: gp_Ax3) -> None:
        """
        Modifies this transformation so that it transforms the
        coordinates of any point, (x, y, z), relative to a source
        coordinate system into the coordinates (x', y', z') which
        are relative to a target coordinate system, but which
        represent the same point
        The transformation is from the default coordinate system
        @code
        {P(0.,0.,0.), VX (1.,0.,0.), VY (0.,1.,0.), VZ (0., 0. ,1.) }
        @endcode
        to the local coordinate system defined with the Ax3 theToSystem.
        Use in the same way as the previous method. FromSystem1 is
        defaulted to the absolute coordinate system.
        """

    @overload
    def SetTransformation(self, R: gp_Quaternion, theT: gp_Vec) -> None:
        """Sets transformation by directly specified rotation and translation."""

    @overload
    def SetTranslation(self, theV: gp_Vec) -> None:
        """
        Changes the transformation into a translation.
        theV is the vector of the translation.
        """

    @overload
    def SetTranslation(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None:
        """
        Makes the transformation into a translation where the translation vector
        is the vector (theP1, theP2) defined from point theP1 to point theP2.
        """

    def SetTranslationPart(self, theV: gp_Vec) -> None:
        """Replaces the translation vector with the vector theV."""

    def SetScaleFactor(self, theS: float) -> None:
        """
        Modifies the scale factor.
        Raises ConstructionError If theS is null.
        """

    def SetForm(self, theP: gp_TrsfForm) -> None: ...

    def SetValues(self, a11: float, a12: float, a13: float, a14: float, a21: float, a22: float, a23: float, a24: float, a31: float, a32: float, a33: float, a34: float) -> None:
        """
        Sets the coefficients of the transformation. The
        transformation of the point x,y,z is the point
        x',y',z' with :
        @code
        x' = a11 x + a12 y + a13 z + a14
        y' = a21 x + a22 y + a23 z + a24
        z' = a31 x + a32 y + a33 z + a34
        @endcode
        The method Value(i,j) will return aij.
        Raises ConstructionError if the determinant of the aij is null.
        The matrix is orthogonalized before future using.
        """

    def IsNegative(self) -> bool:
        """
        Returns true if the determinant of the vectorial part of
        this transformation is negative.
        """

    def Form(self) -> gp_TrsfForm:
        """
        Returns the nature of the transformation. It can be: an
        identity transformation, a rotation, a translation, a mirror
        transformation (relative to a point, an axis or a plane), a
        scaling transformation, or a compound transformation.
        """

    def ScaleFactor(self) -> float:
        """Returns the scale factor."""

    def TranslationPart(self) -> gp_XYZ:
        """Returns the translation part of the transformation's matrix"""

    @overload
    def GetRotation(self, theAxis: gp_XYZ) -> tuple[bool, float]:
        """
        Returns the boolean True if there is non-zero rotation.
        In the presence of rotation, the output parameters store the axis
        and the angle of rotation. The method always returns positive
        value "theAngle", i.e., 0. < theAngle <= PI.
        Note that this rotation is defined only by the vectorial part of
        the transformation; generally you would need to check also the
        translational part to obtain the axis (gp_Ax1) of rotation.
        """

    @overload
    def GetRotation(self) -> gp_Quaternion:
        """Returns quaternion representing rotational part of the transformation."""

    def VectorialPart(self) -> gp_Mat:
        """
        Returns the vectorial part of the transformation. It is
        a 3*3 matrix which includes the scale factor.
        """

    def HVectorialPart(self) -> gp_Mat:
        """
        Computes the homogeneous vectorial part of the transformation.
        It is a 3*3 matrix which doesn't include the scale factor.
        In other words, the vectorial part of this transformation is equal
        to its homogeneous vectorial part, multiplied by the scale factor.
        The coefficients of this matrix must be multiplied by the
        scale factor to obtain the coefficients of the transformation.
        """

    def Value(self, theRow: int, theCol: int) -> float:
        """
        Returns the coefficients of the transformation's matrix.
        It is a 3 rows * 4 columns matrix.
        This coefficient includes the scale factor.
        Raises OutOfRanged if theRow < 1 or theRow > 3 or theCol < 1 or theCol > 4
        """

    def Invert(self) -> None: ...

    def Inverted(self) -> gp_Trsf:
        """
        Computes the reverse transformation
        Raises an exception if the matrix of the transformation
        is not inversible, it means that the scale factor is lower
        or equal to Resolution from package gp.
        Computes the transformation composed with T and <me>.
        In a C++ implementation you can also write Tcomposed = <me> * T.
        Example :
        @code
        gp_Trsf T1, T2, Tcomp; ...............
        Tcomp = T2.Multiplied(T1);         // or   (Tcomp = T2 * T1)
        gp_Pnt P1(10.,3.,4.);
        gp_Pnt P2 = P1.Transformed(Tcomp); // using Tcomp
        gp_Pnt P3 = P1.Transformed(T1);    // using T1 then T2
        P3.Transform(T2);                  // P3 = P2 !!!
        @endcode
        """

    def Multiplied(self, theT: gp_Trsf) -> gp_Trsf: ...

    def __mul__(self, theT: gp_Trsf) -> gp_Trsf: ...

    def Multiply(self, theT: gp_Trsf) -> None:
        """
        Computes the transformation composed with <me> and theT.
        <me> = <me> * theT
        """

    def __imul__(self, theT: gp_Trsf) -> gp_Trsf: ...

    def PreMultiply(self, theT: gp_Trsf) -> None:
        """
        Computes the transformation composed with <me> and T.
        <me> = theT * <me>
        """

    def Power(self, theN: int) -> None: ...

    def Powered(self, theN: int) -> gp_Trsf:
        """
        Computes the following composition of transformations
        <me> * <me> * .......* <me>, theN time.
        if theN = 0 <me> = Identity
        if theN < 0 <me> = <me>.Inverse() *...........* <me>.Inverse().

        Raises if theN < 0 and if the matrix of the transformation not
        inversible.
        """

    @overload
    def Transforms(self, theX: float, theY: float, theZ: float) -> tuple[float, float, float]: ...

    @overload
    def Transforms(self, theCoord: gp_XYZ) -> None:
        """Transformation of a triplet XYZ with a Trsf"""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def InitFromJson(self, theSStream: TextIO, theStreamPos: int) -> tuple[bool, int]:
        """Inits the content of me from the stream"""

class gp_Mat2d:
    """
    Describes a two column, two row matrix.
    This sort of object is used in various vectorial or matrix computations.
    """

    @overload
    def __init__(self) -> None:
        """Creates a matrix with null coefficients."""

    @overload
    def __init__(self, theCol1: gp_XY, theCol2: gp_XY) -> None:
        """theCol1, theCol2 are the 2 columns of the matrix."""

    @overload
    def __init__(self, theOther: gp_Mat2d) -> None: ...

    def SetCol(self, theCol: int, theValue: gp_XY) -> None:
        """
        Assigns the two coordinates of theValue to the column of range
        theCol of this matrix
        Raises OutOfRange if theCol < 1 or theCol > 2.
        """

    def SetCols(self, theCol1: gp_XY, theCol2: gp_XY) -> None:
        """
        Assigns the number pairs theCol1, theCol2 to the two columns of this matrix
        """

    def SetDiagonal(self, theX1: float, theX2: float) -> None:
        """
        Modifies the main diagonal of the matrix.
        @code
        <me>.Value (1, 1) = theX1
        <me>.Value (2, 2) = theX2
        @endcode
        The other coefficients of the matrix are not modified.
        """

    def SetIdentity(self) -> None:
        """Modifies this matrix, so that it represents the Identity matrix."""

    def SetRotation(self, theAng: float) -> None:
        """
        Modifies this matrix, so that it represents a rotation. theAng is the angular
        value in radian of the rotation.
        """

    def SetRow(self, theRow: int, theValue: gp_XY) -> None:
        """
        Assigns the two coordinates of theValue to the row of index theRow of this matrix.
        Raises OutOfRange if theRow < 1 or theRow > 2.
        """

    def SetRows(self, theRow1: gp_XY, theRow2: gp_XY) -> None:
        """
        Assigns the number pairs theRow1, theRow2 to the two rows of this matrix.
        """

    def SetScale(self, theS: float) -> None:
        """
        Modifies the matrix such that it
        represents a scaling transformation, where theS is the scale factor:
        @code
        | theS    0.0 |
        <me> =  | 0.0   theS  |
        @endcode
        """

    def SetValue(self, theRow: int, theCol: int, theValue: float) -> None:
        """
        Assigns <theValue> to the coefficient of row theRow, column theCol of this matrix.
        Raises OutOfRange if theRow < 1 or theRow > 2 or theCol < 1 or theCol > 2
        """

    def Column(self, theCol: int) -> gp_XY:
        """
        Returns the column of theCol index.
        Raises OutOfRange if theCol < 1 or theCol > 2
        """

    def Determinant(self) -> float:
        """Computes the determinant of the matrix."""

    def Diagonal(self) -> gp_XY:
        """Returns the main diagonal of the matrix."""

    def Row(self, theRow: int) -> gp_XY:
        """
        Returns the row of index theRow.
        Raised if theRow < 1 or theRow > 2
        """

    def Value(self, theRow: int, theCol: int) -> float:
        """
        Returns the coefficient of range (ttheheRow, theCol)
        Raises OutOfRange
        if theRow < 1 or theRow > 2 or theCol < 1 or theCol > 2
        """

    def ChangeValue(self, theRow: int, theCol: int) -> float:
        """
        Returns the coefficient of range (theRow, theCol)
        Raises OutOfRange
        if theRow < 1 or theRow > 2 or theCol < 1 or theCol > 2
        """

    def __call__(self, theRow: int, theCol: int) -> float: ...

    def __getitem__(self, arg: tuple[int, int], /) -> float:
        """Python addition: alias to operator()."""

    def __setitem__(self, arg0: tuple[int, int], arg1: float, /) -> None:
        """
        Python addition: sets the value operator()(theRow, theCol) returns by reference in C++.
        """

    def IsSingular(self) -> bool:
        """
        Returns true if this matrix is singular (and therefore, cannot be inverted).
        The Gauss LU decomposition is used to invert the matrix
        so the matrix is considered as singular if the largest
        pivot found is lower or equal to Resolution from gp.
        """

    def Add(self, Other: gp_Mat2d) -> None: ...

    def __iadd__(self, theOther: gp_Mat2d) -> gp_Mat2d: ...

    def Added(self, theOther: gp_Mat2d) -> gp_Mat2d:
        """
        Computes the sum of this matrix and the matrix
        theOther.for each coefficient of the matrix :
        @code
        <me>.Coef(i,j) + <theOther>.Coef(i,j)
        @endcode
        Note:
        -   operator += assigns the result to this matrix, while
        -   operator + creates a new one.
        """

    def __add__(self, theOther: gp_Mat2d) -> gp_Mat2d: ...

    def Divide(self, theScalar: float) -> None: ...

    def __itruediv__(self, theScalar: float) -> gp_Mat2d: ...

    def Divided(self, theScalar: float) -> gp_Mat2d:
        """Divides all the coefficients of the matrix by a scalar."""

    def __truediv__(self, theScalar: float) -> gp_Mat2d: ...

    def Invert(self) -> None: ...

    def Inverted(self) -> gp_Mat2d:
        """
        Inverses the matrix and raises exception if the matrix
        is singular.
        """

    @overload
    def Multiplied(self, theOther: gp_Mat2d) -> gp_Mat2d: ...

    @overload
    def Multiplied(self, theScalar: float) -> gp_Mat2d: ...

    @overload
    def __mul__(self, theOther: gp_Mat2d) -> gp_Mat2d: ...

    @overload
    def __mul__(self, theScalar: float) -> gp_Mat2d: ...

    @overload
    def __mul__(self, arg: gp_XY, /) -> gp_XY: ...

    @overload
    def Multiply(self, theOther: gp_Mat2d) -> None:
        """Computes the product of two matrices <me> * <theOther>"""

    @overload
    def Multiply(self, theScalar: float) -> None:
        """Multiplies all the coefficients of the matrix by a scalar."""

    def PreMultiply(self, theOther: gp_Mat2d) -> None:
        """
        Modifies this matrix by premultiplying it by the matrix Other
        <me> = theOther * <me>.
        """

    def __imul__(self, theScalar: float) -> gp_Mat2d: ...

    def Power(self, theN: int) -> None: ...

    def Powered(self, theN: int) -> gp_Mat2d:
        """
        computes <me> = <me> * <me> * .......* <me>, theN time.
        if theN = 0 <me> = Identity
        if theN < 0 <me> = <me>.Invert() *...........* <me>.Invert().
        If theN < 0 an exception can be raised if the matrix is not
        inversible
        """

    def Subtract(self, theOther: gp_Mat2d) -> None: ...

    def __isub__(self, theOther: gp_Mat2d) -> gp_Mat2d: ...

    def Subtracted(self, theOther: gp_Mat2d) -> gp_Mat2d:
        """
        Computes for each coefficient of the matrix :
        @code
        <me>.Coef(i,j) - <theOther>.Coef(i,j)
        @endcode
        """

    def __sub__(self, theOther: gp_Mat2d) -> gp_Mat2d: ...

    def Transpose(self) -> None: ...

    def Transposed(self) -> gp_Mat2d:
        """Transposes the matrix. A(j, i) -> A (i, j)"""

    def __rmul__(self, arg: float, /) -> gp_Mat2d: ...

class gp_XY:
    """
    This class describes a cartesian coordinate entity in 2D
    space {X,Y}. This class is non persistent. This entity used
    for algebraic calculation. An XY can be transformed with a
    Trsf2d or a GTrsf2d from package gp.
    It is used in vectorial computations or for holding this type
    of information in data structures.
    """

    @overload
    def __init__(self) -> None:
        """Creates XY object with zero coordinates (0,0)."""

    @overload
    def __init__(self, theX: float, theY: float) -> None:
        """a number pair defined by the XY coordinates"""

    @overload
    def __init__(self, theOther: gp_XY) -> None: ...

    @overload
    def SetCoord(self, theIndex: int, theXi: float) -> None:
        """
        modifies the coordinate of range theIndex
        theIndex = 1 => X is modified
        theIndex = 2 => Y is modified
        Raises OutOfRange if theIndex != {1, 2}.
        """

    @overload
    def SetCoord(self, theX: float, theY: float) -> None:
        """
        For this number pair, assigns
        the values theX and theY to its coordinates
        """

    def SetX(self, theX: float) -> None:
        """Assigns the given value to the X coordinate of this number pair."""

    def SetY(self, theY: float) -> None:
        """Assigns the given value to the Y coordinate of this number pair."""

    @overload
    def Coord(self, theIndex: int) -> float:
        """
        returns the coordinate of range theIndex :
        theIndex = 1 => X is returned
        theIndex = 2 => Y is returned
        Raises OutOfRange if theIndex != {1, 2}.
        """

    @overload
    def Coord(self) -> tuple[float, float]:
        """For this number pair, returns its coordinates X and Y."""

    def ChangeCoord(self, theIndex: int) -> float: ...

    def X(self) -> float:
        """Returns the X coordinate of this number pair."""

    def Y(self) -> float:
        """Returns the Y coordinate of this number pair."""

    def Modulus(self) -> float:
        """
        Computes std::sqrt(X*X + Y*Y) where X and Y are the two coordinates of this number pair.
        """

    def SquareModulus(self) -> float:
        """
        Computes X*X + Y*Y where X and Y are the two coordinates of this number pair.
        """

    def IsEqual(self, theOther: gp_XY, theTolerance: float) -> bool:
        """
        Returns true if the coordinates of this number pair are
        equal to the respective coordinates of the number pair
        theOther, within the specified tolerance theTolerance.
        """

    def Add(self, theOther: gp_XY) -> None:
        """
        Computes the sum of this number pair and number pair theOther
        @code
        <me>.X() = <me>.X() + theOther.X()
        <me>.Y() = <me>.Y() + theOther.Y()
        @endcode
        """

    def __iadd__(self, theOther: gp_XY) -> gp_XY: ...

    def Added(self, theOther: gp_XY) -> gp_XY:
        """
        Computes the sum of this number pair and number pair theOther
        @code
        new.X() = <me>.X() + theOther.X()
        new.Y() = <me>.Y() + theOther.Y()
        @endcode
        """

    def __add__(self, theOther: gp_XY) -> gp_XY: ...

    def Crossed(self, theOther: gp_XY) -> float:
        """
        @code
        double D = <me>.X() * theOther.Y() - <me>.Y() * theOther.X()
        @endcode
        """

    def __xor__(self, theOther: gp_XY) -> float: ...

    def CrossMagnitude(self, theRight: gp_XY) -> float:
        """
        computes the magnitude of the cross product between <me> and
        theRight. Returns || <me> ^ theRight ||
        """

    def CrossSquareMagnitude(self, theRight: gp_XY) -> float:
        """
        computes the square magnitude of the cross product between <me> and
        theRight. Returns || <me> ^ theRight ||**2
        """

    def Divide(self, theScalar: float) -> None:
        """divides <me> by a real."""

    def __itruediv__(self, theScalar: float) -> gp_XY: ...

    def Divided(self, theScalar: float) -> gp_XY:
        """Divides <me> by a real."""

    def __truediv__(self, theScalar: float) -> gp_XY: ...

    def Dot(self, theOther: gp_XY) -> float:
        """Computes the scalar product between <me> and theOther"""

    @overload
    def __mul__(self, theOther: gp_XY) -> float: ...

    @overload
    def __mul__(self, theScalar: float) -> gp_XY: ...

    @overload
    def __mul__(self, theMatrix: gp_Mat2d) -> gp_XY: ...

    @overload
    def Multiply(self, theScalar: float) -> None:
        """
        @code
        <me>.X() = <me>.X() * theScalar;
        <me>.Y() = <me>.Y() * theScalar;
        @endcode
        """

    @overload
    def Multiply(self, theOther: gp_XY) -> None:
        """
        @code
        <me>.X() = <me>.X() * theOther.X();
        <me>.Y() = <me>.Y() * theOther.Y();
        @endcode
        """

    @overload
    def Multiply(self, theMatrix: gp_Mat2d) -> None:
        """<me> = theMatrix * <me>"""

    @overload
    def __imul__(self, theScalar: float) -> gp_XY: ...

    @overload
    def __imul__(self, theOther: gp_XY) -> gp_XY: ...

    @overload
    def __imul__(self, theMatrix: gp_Mat2d) -> gp_XY: ...

    @overload
    def Multiplied(self, theScalar: float) -> gp_XY:
        """
        @code
        New.X() = <me>.X() * theScalar;
        New.Y() = <me>.Y() * theScalar;
        @endcode
        """

    @overload
    def Multiplied(self, theOther: gp_XY) -> gp_XY:
        """
        @code
        new.X() = <me>.X() * theOther.X();
        new.Y() = <me>.Y() * theOther.Y();
        @endcode
        """

    @overload
    def Multiplied(self, theMatrix: gp_Mat2d) -> gp_XY:
        """New = theMatrix * <me>"""

    def Normalize(self) -> None:
        """
        @code
        <me>.X() = <me>.X()/ <me>.Modulus()
        <me>.Y() = <me>.Y()/ <me>.Modulus()
        @endcode
        Raises ConstructionError if <me>.Modulus() <= Resolution from gp
        """

    def Normalized(self) -> gp_XY:
        """
        @code
        New.X() = <me>.X()/ <me>.Modulus()
        New.Y() = <me>.Y()/ <me>.Modulus()
        @endcode
        Raises ConstructionError if <me>.Modulus() <= Resolution from gp
        """

    def Reverse(self) -> None:
        """
        @code
        <me>.X() = -<me>.X()
        <me>.Y() = -<me>.Y()
        """

    def Reversed(self) -> gp_XY:
        """
        @code
        New.X() = -<me>.X()
        New.Y() = -<me>.Y()
        @endcode
        """

    def __neg__(self) -> gp_XY: ...

    @overload
    def SetLinearForm(self, theA1: float, theXY1: gp_XY, theA2: float, theXY2: gp_XY) -> None:
        """
        Computes the following linear combination and
        assigns the result to this number pair:
        @code
        theA1 * theXY1 + theA2 * theXY2
        @endcode
        """

    @overload
    def SetLinearForm(self, theA1: float, theXY1: gp_XY, theA2: float, theXY2: gp_XY, theXY3: gp_XY) -> None:
        """
        Computes the following linear combination and
        assigns the result to this number pair:
        @code
        theA1 * theXY1 + theA2 * theXY2 + theXY3
        @endcode
        """

    @overload
    def SetLinearForm(self, theA1: float, theXY1: gp_XY, theXY2: gp_XY) -> None:
        """
        Computes the following linear combination and
        assigns the result to this number pair:
        @code
        theA1 * theXY1 + theXY2
        @endcode
        """

    @overload
    def SetLinearForm(self, theXY1: gp_XY, theXY2: gp_XY) -> None:
        """
        Computes the following linear combination and
        assigns the result to this number pair:
        @code
        theXY1 + theXY2
        @endcode
        """

    def Subtract(self, theOther: gp_XY) -> None:
        """
        @code
        <me>.X() = <me>.X() - theOther.X()
        <me>.Y() = <me>.Y() - theOther.Y()
        @endcode
        """

    def __isub__(self, theOther: gp_XY) -> gp_XY: ...

    def Subtracted(self, theOther: gp_XY) -> gp_XY:
        """
        @code
        new.X() = <me>.X() - theOther.X()
        new.Y() = <me>.Y() - theOther.Y()
        @endcode
        """

    def __sub__(self, theOther: gp_XY) -> gp_XY: ...

    def __rmul__(self, arg: float, /) -> gp_XY: ...

class gp_Trsf2d:
    """
    Defines a non-persistent transformation in 2D space.
    The following transformations are implemented :
    - Translation, Rotation, Scale
    - Symmetry with respect to a point and a line.
    Complex transformations can be obtained by combining the
    previous elementary transformations using the method Multiply.
    The transformations can be represented as follow :
    @code
    V1   V2   T       XY        XY
    | a11  a12  a13 |   | x |     | x'|
    | a21  a22  a23 |   | y |     | y'|
    |  0    0    1  |   | 1 |     | 1 |
    @endcode
    where {V1, V2} defines the vectorial part of the transformation
    and T defines the translation part of the transformation.
    This transformation never change the nature of the objects.
    """

    @overload
    def __init__(self) -> None:
        """Returns identity transformation."""

    @overload
    def __init__(self, theT: gp_Trsf) -> None:
        """
        Creates a 2d transformation in the XY plane from a
        3d transformation .
        """

    @overload
    def __init__(self, theOther: gp_Trsf2d) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeMirror2d) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeRotation2d) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeScale2d) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeTranslation2d) -> None: ...

    @overload
    def SetMirror(self, theP: gp_Pnt2d) -> None:
        """
        Changes the transformation into a symmetrical transformation.
        theP is the center of the symmetry.
        """

    @overload
    def SetMirror(self, theA: gp_Ax2d) -> None:
        """
        Changes the transformation into a symmetrical transformation.
        theA is the center of the axial symmetry.
        """

    def SetRotation(self, theP: gp_Pnt2d, theAng: float) -> None:
        """
        Changes the transformation into a rotation.
        theP is the rotation's center and theAng is the angular value of the
        rotation in radian.
        """

    def SetScale(self, theP: gp_Pnt2d, theS: float) -> None:
        """
        Changes the transformation into a scale.
        theP is the center of the scale and theS is the scaling value.
        """

    @overload
    def SetTransformation(self, theFromSystem1: gp_Ax2d, theToSystem2: gp_Ax2d) -> None:
        """
        Changes a transformation allowing passage from the coordinate
        system "theFromSystem1" to the coordinate system "theToSystem2".
        """

    @overload
    def SetTransformation(self, theToSystem: gp_Ax2d) -> None:
        """
        Changes the transformation allowing passage from the basic
        coordinate system
        {P(0.,0.,0.), VX (1.,0.,0.), VY (0.,1.,0.)}
        to the local coordinate system defined with the Ax2d theToSystem.
        """

    @overload
    def SetTranslation(self, theV: gp_Vec2d) -> None:
        """
        Changes the transformation into a translation.
        theV is the vector of the translation.
        """

    @overload
    def SetTranslation(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> None:
        """
        Makes the transformation into a translation from
        the point theP1 to the point theP2.
        """

    def SetTranslationPart(self, theV: gp_Vec2d) -> None:
        """Replaces the translation vector with theV."""

    def SetScaleFactor(self, theS: float) -> None:
        """Modifies the scale factor."""

    def IsNegative(self) -> bool:
        """
        Returns true if the determinant of the vectorial part of
        this transformation is negative..
        """

    def Form(self) -> gp_TrsfForm:
        """
        Returns the nature of the transformation. It can be an
        identity transformation, a rotation, a translation, a mirror
        (relative to a point or an axis), a scaling transformation,
        or a compound transformation.
        """

    def ScaleFactor(self) -> float:
        """Returns the scale factor."""

    def TranslationPart(self) -> gp_XY:
        """Returns the translation part of the transformation's matrix"""

    def VectorialPart(self) -> gp_Mat2d:
        """
        Returns the vectorial part of the transformation. It is a
        2*2 matrix which includes the scale factor.
        """

    def HVectorialPart(self) -> gp_Mat2d:
        """
        Returns the homogeneous vectorial part of the transformation.
        It is a 2*2 matrix which doesn't include the scale factor.
        The coefficients of this matrix must be multiplied by the
        scale factor to obtain the coefficients of the transformation.
        """

    def RotationPart(self) -> float:
        """
        Returns the angle corresponding to the rotational component
        of the transformation matrix (operation opposite to SetRotation()).
        """

    def Value(self, theRow: int, theCol: int) -> float:
        """
        Returns the coefficients of the transformation's matrix.
        It is a 2 rows * 3 columns matrix.
        Raises OutOfRange if theRow < 1 or theRow > 2 or theCol < 1 or theCol > 3
        """

    def Invert(self) -> None: ...

    def Inverted(self) -> gp_Trsf2d:
        """
        Computes the reverse transformation.
        Raises an exception if the matrix of the transformation
        is not inversible, it means that the scale factor is lower
        or equal to Resolution from package gp.
        """

    def Multiplied(self, theT: gp_Trsf2d) -> gp_Trsf2d: ...

    def __mul__(self, theT: gp_Trsf2d) -> gp_Trsf2d: ...

    def Multiply(self, theT: gp_Trsf2d) -> None:
        """
        Computes the transformation composed from <me> and theT.
        <me> = <me> * theT
        """

    def __imul__(self, theT: gp_Trsf2d) -> gp_Trsf2d: ...

    def PreMultiply(self, theT: gp_Trsf2d) -> None:
        """
        Computes the transformation composed from <me> and theT.
        <me> = theT * <me>
        """

    def Power(self, theN: int) -> None: ...

    def Powered(self, theN: int) -> gp_Trsf2d:
        """
        Computes the following composition of transformations
        <me> * <me> * .......* <me>, theN time.
        if theN = 0 <me> = Identity
        if theN < 0 <me> = <me>.Inverse() *...........* <me>.Inverse().

        Raises if theN < 0 and if the matrix of the transformation not
        inversible.
        """

    @overload
    def Transforms(self, theX: float, theY: float) -> tuple[float, float]: ...

    @overload
    def Transforms(self, theCoord: gp_XY) -> None:
        """Transforms a doublet XY with a Trsf2d"""

    def SetValues(self, a11: float, a12: float, a13: float, a21: float, a22: float, a23: float) -> None:
        """
        Sets the coefficients of the transformation. The
        transformation of the point x,y is the point
        x',y' with :
        @code
        x' = a11 x + a12 y + a13
        y' = a21 x + a22 y + a23
        @endcode
        The method Value(i,j) will return aij.
        Raises ConstructionError if the determinant of the aij is null.
        If the matrix as not a uniform scale it will be orthogonalized before future using.
        """

class gp_Pnt2d:
    """Defines a non-persistent 2D cartesian point."""

    @overload
    def __init__(self) -> None:
        """Creates a point with zero coordinates."""

    @overload
    def __init__(self, theCoord: gp_XY) -> None:
        """Creates a point with a doublet of coordinates."""

    @overload
    def __init__(self, theXp: float, theYp: float) -> None:
        """Creates a point with its 2 cartesian's coordinates: theXp, theYp."""

    @overload
    def __init__(self, theOther: gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.Geom2dAPI.Geom2dAPI_ProjectPointOnCurve) -> None: ...

    @overload
    def SetCoord(self, theIndex: int, theXi: float) -> None:
        """
        Assigns the value Xi to the coordinate that corresponds to theIndex:
        theIndex = 1 => X is modified
        theIndex = 2 => Y is modified
        Raises OutOfRange if theIndex != {1, 2}.
        """

    @overload
    def SetCoord(self, theXp: float, theYp: float) -> None:
        """
        For this point, assigns the values theXp and theYp to its two coordinates
        """

    def SetX(self, theX: float) -> None:
        """Assigns the given value to the X coordinate of this point."""

    def SetY(self, theY: float) -> None:
        """Assigns the given value to the Y coordinate of this point."""

    def SetXY(self, theCoord: gp_XY) -> None:
        """Assigns the two coordinates of Coord to this point."""

    @overload
    def Coord(self, theIndex: int) -> float:
        """
        Returns the coordinate of range theIndex :
        theIndex = 1 => X is returned
        theIndex = 2 => Y is returned
        Raises OutOfRange if theIndex != {1, 2}.
        """

    @overload
    def Coord(self) -> gp_XY:
        """For this point, returns its two coordinates as a number pair."""

    def Coord__float__float(self) -> tuple[float, float]:
        """
        Coord__float__float: the C++ overload Coord(double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        For this point returns its two coordinates as a number pair.
        """

    def X(self) -> float:
        """For this point, returns its X coordinate."""

    def Y(self) -> float:
        """For this point, returns its Y coordinate."""

    def XY(self) -> gp_XY:
        """For this point, returns its two coordinates as a number pair."""

    def ChangeCoord(self) -> gp_XY:
        """
        Returns the coordinates of this point.
        Note: This syntax allows direct modification of the returned value.
        """

    def IsEqual(self, theOther: gp_Pnt2d, theLinearTolerance: float) -> bool:
        """
        Comparison
        Returns True if the distance between the two
        points is lower or equal to theLinearTolerance.
        """

    def Distance(self, theOther: gp_Pnt2d) -> float:
        """Computes the distance between two points."""

    def SquareDistance(self, theOther: gp_Pnt2d) -> float:
        """Computes the square distance between two points."""

    @overload
    def Mirror(self, theP: gp_Pnt2d) -> None:
        """
        Performs the symmetrical transformation of a point
        with respect to the point theP which is the center of
        the symmetry.
        """

    @overload
    def Mirror(self, theA: gp_Ax2d) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt2d) -> gp_Pnt2d:
        """
        Performs the symmetrical transformation of a point
        with respect to an axis placement which is the axis
        """

    @overload
    def Mirrored(self, theA: gp_Ax2d) -> gp_Pnt2d: ...

    def Rotate(self, theP: gp_Pnt2d, theAng: float) -> None:
        """
        Rotates a point. theA1 is the axis of the rotation.
        Ang is the angular value of the rotation in radians.
        """

    def Rotated(self, theP: gp_Pnt2d, theAng: float) -> gp_Pnt2d: ...

    def Scale(self, theP: gp_Pnt2d, theS: float) -> None:
        """Scales a point. theS is the scaling value."""

    def Scaled(self, theP: gp_Pnt2d, theS: float) -> gp_Pnt2d: ...

    def Transform(self, theT: gp_Trsf2d) -> None:
        """Transforms a point with the transformation theT."""

    def Transformed(self, theT: gp_Trsf2d) -> gp_Pnt2d: ...

    @overload
    def Translate(self, theV: gp_Vec2d) -> None:
        """
        Translates a point in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translate(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> None:
        """Translates a point from the point theP1 to the point theP2."""

    @overload
    def Translated(self, theV: gp_Vec2d) -> gp_Pnt2d: ...

    @overload
    def Translated(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> gp_Pnt2d: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class gp_VectorWithNullMagnitude(nanoocp.Standard.Standard_DomainError):
    pass

class gp_Vec2d:
    """Defines a non-persistent vector in 2D space."""

    @overload
    def __init__(self) -> None:
        """Creates a zero vector."""

    @overload
    def __init__(self, theV: gp_Dir2d) -> None:
        """Creates a unitary vector from a direction theV."""

    @overload
    def __init__(self, theCoord: gp_XY) -> None:
        """Creates a vector with a doublet of coordinates."""

    @overload
    def __init__(self, theXv: float, theYv: float) -> None:
        """Creates a point with its two Cartesian coordinates."""

    @overload
    def __init__(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> None:
        """
        Creates a vector from two points. The length of the vector
        is the distance between theP1 and theP2
        """

    @overload
    def __init__(self, theOther: gp_Vec2d) -> None: ...

    @overload
    def SetCoord(self, theIndex: int, theXi: float) -> None:
        """
        Changes the coordinate of range theIndex
        theIndex = 1 => X is modified
        theIndex = 2 => Y is modified
        Raises OutOfRange if theIndex != {1, 2}.
        """

    @overload
    def SetCoord(self, theXv: float, theYv: float) -> None:
        """
        For this vector, assigns
        the values theXv and theYv to its two coordinates
        """

    def SetX(self, theX: float) -> None:
        """Assigns the given value to the X coordinate of this vector."""

    def SetY(self, theY: float) -> None:
        """Assigns the given value to the Y coordinate of this vector."""

    def SetXY(self, theCoord: gp_XY) -> None:
        """Assigns the two coordinates of theCoord to this vector."""

    @overload
    def Coord(self, theIndex: int) -> float:
        """
        Returns the coordinate of range theIndex :
        theIndex = 1 => X is returned
        theIndex = 2 => Y is returned
        Raised if theIndex != {1, 2}.
        """

    @overload
    def Coord(self) -> tuple[float, float]:
        """For this vector, returns its two coordinates theXv and theYv"""

    def X(self) -> float:
        """For this vector, returns its X coordinate."""

    def Y(self) -> float:
        """For this vector, returns its Y coordinate."""

    def XY(self) -> gp_XY:
        """For this vector, returns its two coordinates as a number pair"""

    def IsEqual(self, theOther: gp_Vec2d, theLinearTolerance: float, theAngularTolerance: float) -> bool:
        """
        Returns True if the two vectors have the same magnitude value
        and the same direction. The precision values are theLinearTolerance
        for the magnitude and theAngularTolerance for the direction.
        """

    def IsNormal(self, theOther: gp_Vec2d, theAngularTolerance: float) -> bool:
        """
        Returns True if abs(std::abs(<me>.Angle(theOther)) - PI/2.)
        <= theAngularTolerance
        Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or
        theOther.Magnitude() <= Resolution from gp.
        """

    def IsOpposite(self, theOther: gp_Vec2d, theAngularTolerance: float) -> bool:
        """
        Returns True if PI - std::abs(<me>.Angle(theOther)) <= theAngularTolerance
        Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or
        theOther.Magnitude() <= Resolution from gp.
        """

    def IsParallel(self, theOther: gp_Vec2d, theAngularTolerance: float) -> bool:
        """
        Returns true if std::abs(Angle(<me>, theOther)) <= theAngularTolerance or
        PI - std::abs(Angle(<me>, theOther)) <= theAngularTolerance
        Two vectors with opposite directions are considered as parallel.
        Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or
        theOther.Magnitude() <= Resolution from gp
        """

    def Angle(self, theOther: gp_Vec2d) -> float:
        """
        Computes the angular value between <me> and <theOther>
        returns the angle value between -PI and PI in radian.
        The orientation is from <me> to theOther. The positive sense is the
        trigonometric sense.
        Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution from gp or
        theOther.Magnitude() <= Resolution because the angular value is
        indefinite if one of the vectors has a null magnitude.
        """

    def Magnitude(self) -> float:
        """Computes the magnitude of this vector."""

    def SquareMagnitude(self) -> float:
        """Computes the square magnitude of this vector."""

    def Add(self, theOther: gp_Vec2d) -> None: ...

    def __iadd__(self, theOther: gp_Vec2d) -> gp_Vec2d: ...

    def Added(self, theOther: gp_Vec2d) -> gp_Vec2d:
        """Adds two vectors"""

    def __add__(self, theOther: gp_Vec2d) -> gp_Vec2d: ...

    def Crossed(self, theRight: gp_Vec2d) -> float:
        """Computes the crossing product between two vectors"""

    def __xor__(self, theRight: gp_Vec2d) -> float: ...

    def CrossMagnitude(self, theRight: gp_Vec2d) -> float:
        """
        Computes the magnitude of the cross product between <me> and
        theRight. Returns || <me> ^ theRight ||
        """

    def CrossSquareMagnitude(self, theRight: gp_Vec2d) -> float:
        """
        Computes the square magnitude of the cross product between <me> and
        theRight. Returns || <me> ^ theRight ||**2
        """

    def Divide(self, theScalar: float) -> None: ...

    def __itruediv__(self, theScalar: float) -> gp_Vec2d: ...

    def Divided(self, theScalar: float) -> gp_Vec2d:
        """divides a vector by a scalar"""

    def __truediv__(self, theScalar: float) -> gp_Vec2d: ...

    def Dot(self, theOther: gp_Vec2d) -> float:
        """Computes the scalar product"""

    @overload
    def __mul__(self, theOther: gp_Vec2d) -> float: ...

    @overload
    def __mul__(self, theScalar: float) -> gp_Vec2d: ...

    def GetNormal(self) -> gp_Vec2d: ...

    def Multiply(self, theScalar: float) -> None: ...

    def __imul__(self, theScalar: float) -> gp_Vec2d: ...

    def Multiplied(self, theScalar: float) -> gp_Vec2d:
        """
        Normalizes a vector
        Raises an exception if the magnitude of the vector is
        lower or equal to Resolution from package gp.
        """

    def Normalize(self) -> None: ...

    def Normalized(self) -> gp_Vec2d:
        """
        Normalizes a vector
        Raises an exception if the magnitude of the vector is
        lower or equal to Resolution from package gp.
        Reverses the direction of a vector
        """

    def Reverse(self) -> None: ...

    def Reversed(self) -> gp_Vec2d:
        """Reverses the direction of a vector"""

    def __neg__(self) -> gp_Vec2d: ...

    def Subtract(self, theRight: gp_Vec2d) -> None:
        """Subtracts two vectors"""

    def __isub__(self, theRight: gp_Vec2d) -> gp_Vec2d: ...

    def Subtracted(self, theRight: gp_Vec2d) -> gp_Vec2d:
        """Subtracts two vectors"""

    def __sub__(self, theRight: gp_Vec2d) -> gp_Vec2d: ...

    @overload
    def SetLinearForm(self, theA1: float, theV1: gp_Vec2d, theA2: float, theV2: gp_Vec2d, theV3: gp_Vec2d) -> None:
        """
        <me> is set to the following linear form :
        theA1 * theV1 + theA2 * theV2 + theV3
        """

    @overload
    def SetLinearForm(self, theA1: float, theV1: gp_Vec2d, theA2: float, theV2: gp_Vec2d) -> None:
        """
        <me> is set to the following linear form : theA1 * theV1 + theA2 * theV2
        """

    @overload
    def SetLinearForm(self, theA1: float, theV1: gp_Vec2d, theV2: gp_Vec2d) -> None:
        """<me> is set to the following linear form : theA1 * theV1 + theV2"""

    @overload
    def SetLinearForm(self, theV1: gp_Vec2d, theV2: gp_Vec2d) -> None:
        """<me> is set to the following linear form : theV1 + theV2"""

    @overload
    def Mirror(self, theV: gp_Vec2d) -> None:
        """
        Performs the symmetrical transformation of a vector
        with respect to the vector theV which is the center of
        the symmetry.
        """

    @overload
    def Mirror(self, theA1: gp_Ax2d) -> None:
        """
        Performs the symmetrical transformation of a vector
        with respect to an axis placement which is the axis
        of the symmetry.
        """

    @overload
    def Mirrored(self, theV: gp_Vec2d) -> gp_Vec2d:
        """
        Performs the symmetrical transformation of a vector
        with respect to the vector theV which is the center of
        the symmetry.
        """

    @overload
    def Mirrored(self, theA1: gp_Ax2d) -> gp_Vec2d:
        """
        Performs the symmetrical transformation of a vector
        with respect to an axis placement which is the axis
        of the symmetry.
        """

    def Rotate(self, theAng: float) -> None: ...

    def Rotated(self, theAng: float) -> gp_Vec2d:
        """
        Rotates a vector. theAng is the angular value of the
        rotation in radians.
        """

    def Scale(self, theS: float) -> None: ...

    def Scaled(self, theS: float) -> gp_Vec2d:
        """Scales a vector. theS is the scaling value."""

    def Transform(self, theT: gp_Trsf2d) -> None: ...

    def Transformed(self, theT: gp_Trsf2d) -> gp_Vec2d:
        """Transforms a vector with a Trsf from gp."""

    def __rmul__(self, arg: float, /) -> gp_Vec2d: ...

class gp_Dir2d:
    """
    Describes a unit vector in the plane (2D space). This unit
    vector is also called "Direction".
    See Also
    gce_MakeDir2d which provides functions for more
    complex unit vector constructions
    Geom2d_Direction which provides additional functions
    for constructing unit vectors and works, in particular, with
    the parametric equations of unit vectors
    """

    @overload
    def __init__(self) -> None:
        """Creates a direction corresponding to X axis."""

    @overload
    def __init__(self, theDir: gp_Dir2d.D) -> None:
        """Creates a direction from a standard direction enumeration."""

    @overload
    def __init__(self, theV: gp_Vec2d) -> None:
        """
        Normalizes the vector theV and creates a Direction. Raises ConstructionError if
        theV.Magnitude() <= Resolution from gp.
        @note Constexpr-compatible when input is already normalized.
        """

    @overload
    def __init__(self, theCoord: gp_XY) -> None:
        """
        Creates a Direction from a doublet of coordinates. Raises ConstructionError if
        theCoord.Modulus() <= Resolution from gp.
        @note Constexpr-compatible when input is already normalized.
        """

    @overload
    def __init__(self, theXv: float, theYv: float) -> None:
        """
        Creates a Direction with its 2 cartesian coordinates. Raises ConstructionError if
        std::sqrt(theXv*theXv + theYv*theYv) <= Resolution from gp.
        @note Constexpr-compatible when input is already normalized.
        """

    @overload
    def __init__(self, theOther: gp_Dir2d) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeDir2d) -> None: ...

    class D(enum.Enum):
        """Standard directions in 2D space for optimized constexpr construction"""

        X = 0

        Y = 1

        NX = 2

        NY = 3

    @overload
    def SetCoord(self, theIndex: int, theXi: float) -> None:
        """
        For this unit vector, assigns:
        the value theXi to:
        -   the X coordinate if theIndex is 1, or
        -   the Y coordinate if theIndex is 2, and then normalizes it.
        Warning
        Remember that all the coordinates of a unit vector are
        implicitly modified when any single one is changed directly.
        Exceptions
        Standard_OutOfRange if theIndex is not 1 or 2.
        Standard_ConstructionError if either of the following
        is less than or equal to gp::Resolution():
        -   std::sqrt(theXv*theXv + theYv*theYv), or
        -   the modulus of the number pair formed by the new
        value theXi and the other coordinate of this vector that
        was not directly modified.
        Raises OutOfRange if theIndex != {1, 2}.
        @note Constexpr-compatible when result is already normalized.
        """

    @overload
    def SetCoord(self, theXv: float, theYv: float) -> None:
        """
        For this unit vector, assigns:
        -   the values theXv and theYv to its two coordinates,
        Warning
        Remember that all the coordinates of a unit vector are
        implicitly modified when any single one is changed directly.
        Exceptions
        Standard_OutOfRange if theIndex is not 1 or 2.
        Standard_ConstructionError if either of the following
        is less than or equal to gp::Resolution():
        -   std::sqrt(theXv*theXv + theYv*theYv), or
        -   the modulus of the number pair formed by the new
        value Xi and the other coordinate of this vector that
        was not directly modified.
        Raises OutOfRange if theIndex != {1, 2}.
        @note Constexpr-compatible when input is already normalized.
        """

    def SetX(self, theX: float) -> None:
        """
        Assigns the given value to the X coordinate of this unit vector,
        and then normalizes it.
        Warning
        Remember that all the coordinates of a unit vector are
        implicitly modified when any single one is changed directly.
        Exceptions
        Standard_ConstructionError if either of the following
        is less than or equal to gp::Resolution():
        -   the modulus of Coord, or
        -   the modulus of the number pair formed from the new
        X or Y coordinate and the other coordinate of this
        vector that was not directly modified.
        @note Constexpr-compatible when result is already normalized.
        """

    def SetY(self, theY: float) -> None:
        """
        Assigns the given value to the Y coordinate of this unit vector,
        and then normalizes it.
        Warning
        Remember that all the coordinates of a unit vector are
        implicitly modified when any single one is changed directly.
        Exceptions
        Standard_ConstructionError if either of the following
        is less than or equal to gp::Resolution():
        -   the modulus of Coord, or
        -   the modulus of the number pair formed from the new
        X or Y coordinate and the other coordinate of this
        vector that was not directly modified.
        @note Constexpr-compatible when result is already normalized.
        """

    def SetXY(self, theCoord: gp_XY) -> None:
        """
        Assigns:
        -   the two coordinates of theCoord to this unit vector,
        and then normalizes it.
        Warning
        Remember that all the coordinates of a unit vector are
        implicitly modified when any single one is changed directly.
        Exceptions
        Standard_ConstructionError if either of the following
        is less than or equal to gp::Resolution():
        -   the modulus of theCoord, or
        -   the modulus of the number pair formed from the new
        X or Y coordinate and the other coordinate of this
        vector that was not directly modified.
        @note Constexpr-compatible when input is already normalized.
        """

    @overload
    def Coord(self, theIndex: int) -> float:
        """
        For this unit vector returns the coordinate of range theIndex :
        theIndex = 1 => X is returned
        theIndex = 2 => Y is returned
        Raises OutOfRange if theIndex != {1, 2}.
        """

    @overload
    def Coord(self) -> tuple[float, float]:
        """
        For this unit vector returns its two coordinates theXv and theYv.
        Raises OutOfRange if theIndex != {1, 2}.
        """

    def X(self) -> float:
        """For this unit vector, returns its X coordinate."""

    def Y(self) -> float:
        """For this unit vector, returns its Y coordinate."""

    def XY(self) -> gp_XY:
        """
        For this unit vector, returns its two coordinates as a number pair.
        Comparison between Directions
        The precision value is an input data.
        """

    def IsEqual(self, theOther: gp_Dir2d, theAngularTolerance: float) -> bool:
        """
        Returns True if the two vectors have the same direction
        i.e. the angle between this unit vector and the
        unit vector theOther is less than or equal to theAngularTolerance.
        """

    def IsNormal(self, theOther: gp_Dir2d, theAngularTolerance: float) -> bool:
        """
        Returns True if the angle between this unit vector and the
        unit vector theOther is equal to Pi/2 or -Pi/2 (normal)
        i.e. std::abs(std::abs(<me>.Angle(theOther)) - PI/2.) <= theAngularTolerance
        """

    def IsOpposite(self, theOther: gp_Dir2d, theAngularTolerance: float) -> bool:
        """
        Returns True if the angle between this unit vector and the
        unit vector theOther is equal to Pi or -Pi (opposite).
        i.e.  PI - std::abs(<me>.Angle(theOther)) <= theAngularTolerance
        """

    def IsParallel(self, theOther: gp_Dir2d, theAngularTolerance: float) -> bool:
        """
        Returns True if the angle between this unit vector and unit
        vector theOther is equal to 0, Pi or -Pi.
        i.e.  std::abs(Angle(<me>, theOther)) <= theAngularTolerance or
        PI - std::abs(Angle(<me>, theOther)) <= theAngularTolerance
        """

    def Angle(self, theOther: gp_Dir2d) -> float:
        """
        Computes the angular value in radians between <me> and
        <theOther>. Returns the angle in the range [-PI, PI].
        """

    def Crossed(self, theRight: gp_Dir2d) -> float:
        """Computes the cross product between two directions."""

    def __xor__(self, theRight: gp_Dir2d) -> float: ...

    def Dot(self, theOther: gp_Dir2d) -> float:
        """Computes the scalar product"""

    def __mul__(self, theOther: gp_Dir2d) -> float: ...

    def Reverse(self) -> None: ...

    def Reversed(self) -> gp_Dir2d:
        """Reverses the orientation of a direction"""

    def __neg__(self) -> gp_Dir2d: ...

    @overload
    def Mirror(self, theV: gp_Dir2d) -> None: ...

    @overload
    def Mirror(self, theA: gp_Ax2d) -> None: ...

    @overload
    def Mirrored(self, theV: gp_Dir2d) -> gp_Dir2d:
        """
        Performs the symmetrical transformation of a direction
        with respect to the direction theV which is the center of
        the symmetry.
        """

    @overload
    def Mirrored(self, theA: gp_Ax2d) -> gp_Dir2d:
        """
        Performs the symmetrical transformation of a direction
        with respect to an axis placement which is the axis
        of the symmetry.
        """

    def Rotate(self, Ang: float) -> None: ...

    def Rotated(self, theAng: float) -> gp_Dir2d:
        """
        Rotates a direction. theAng is the angular value of
        the rotation in radians.
        """

    def Transform(self, theT: gp_Trsf2d) -> None: ...

    def Transformed(self, theT: gp_Trsf2d) -> gp_Dir2d:
        """
        Transforms a direction with the "Trsf" theT.
        Warnings :
        If the scale factor of the "Trsf" theT is negative then the
        direction <me> is reversed.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class gp_Ax2d:
    """
    Describes an axis in the plane (2D space).
    An axis is defined by:
    -   its origin (also referred to as its "Location point"), and
    -   its unit vector (referred to as its "Direction").
    An axis implicitly defines a direct, right-handed
    coordinate system in 2D space by:
    -   its origin,
    - its "Direction" (giving the "X Direction" of the coordinate system), and
    -   the unit vector normal to "Direction" (positive angle
    measured in the trigonometric sense).
    An axis is used:
    -   to describe 2D geometric entities (for example, the
    axis which defines angular coordinates on a circle).
    It serves for the same purpose as the STEP function
    "axis placement one axis", or
    -   to define geometric transformations (axis of
    symmetry, axis of rotation, and so on).
    Note: to define a left-handed 2D coordinate system, use gp_Ax22d.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an axis object representing X axis of the reference coordinate system.
        """

    @overload
    def __init__(self, theDir: gp_Dir2d.D) -> None:
        """
        Creates an axis at the origin with the given standard direction.
        Replaces gp::OX2d(), gp::OY2d() static functions.
        """

    @overload
    def __init__(self, theP: gp_Pnt2d, theV: gp_Dir2d) -> None:
        """
        Creates an Ax2d.
        <theP> is the "Location" point of the axis placement
        and theV is the "Direction" of the axis placement.
        """

    @overload
    def __init__(self, theP: gp_Pnt2d, theDir: gp_Dir2d.D) -> None:
        """Creates an axis with the given location point and standard direction."""

    @overload
    def __init__(self, theOther: gp_Ax2d) -> None: ...

    def SetLocation(self, theP: gp_Pnt2d) -> None:
        """Changes the "Location" point (origin) of <me>."""

    def SetDirection(self, theV: gp_Dir2d) -> None:
        """Changes the direction of <me>."""

    def Location(self) -> gp_Pnt2d:
        """Returns the origin of <me>."""

    def Direction(self) -> gp_Dir2d:
        """Returns the direction of <me>."""

    def IsCoaxial(self, Other: gp_Ax2d, AngularTolerance: float, LinearTolerance: float) -> bool:
        """
        Returns True if:
        . the angle between <me> and <Other> is lower or equal
        to <AngularTolerance> and
        . the distance between <me>.Location() and <Other> is lower
        or equal to <LinearTolerance> and
        . the distance between <Other>.Location() and <me> is lower
        or equal to LinearTolerance.
        """

    def IsNormal(self, theOther: gp_Ax2d, theAngularTolerance: float) -> bool:
        """
        Returns true if this axis and the axis theOther are normal to each other.
        That is, if the angle between the two axes is equal to Pi/2 or -Pi/2.
        Note: the tolerance criterion is given by theAngularTolerance.
        """

    def IsOpposite(self, theOther: gp_Ax2d, theAngularTolerance: float) -> bool:
        """
        Returns true if this axis and the axis theOther are parallel, and have opposite orientations.
        That is, if the angle between the two axes is equal to Pi or -Pi.
        Note: the tolerance criterion is given by theAngularTolerance.
        """

    def IsParallel(self, theOther: gp_Ax2d, theAngularTolerance: float) -> bool:
        """
        Returns true if this axis and the axis theOther are parallel,
        and have either the same or opposite orientations.
        That is, if the angle between the two axes is equal to 0, Pi or -Pi.
        Note: the tolerance criterion is given by theAngularTolerance.
        """

    def Angle(self, theOther: gp_Ax2d) -> float:
        """
        Computes the angle, in radians, between this axis and the axis theOther.
        The value of the angle is between -Pi and Pi.
        """

    def Reverse(self) -> None:
        """Reverses the direction of <me> and assigns the result to this axis."""

    def Reversed(self) -> gp_Ax2d:
        """
        Computes a new axis placement with a direction opposite to the direction of <me>.
        """

    @overload
    def Mirror(self, P: gp_Pnt2d) -> None: ...

    @overload
    def Mirror(self, A: gp_Ax2d) -> None: ...

    @overload
    def Mirrored(self, P: gp_Pnt2d) -> gp_Ax2d:
        """
        Performs the symmetrical transformation of an axis
        placement with respect to the point P which is the
        center of the symmetry.
        """

    @overload
    def Mirrored(self, A: gp_Ax2d) -> gp_Ax2d:
        """
        Performs the symmetrical transformation of an axis
        placement with respect to an axis placement which
        is the axis of the symmetry.
        """

    def Rotate(self, theP: gp_Pnt2d, theAng: float) -> None: ...

    def Rotated(self, theP: gp_Pnt2d, theAng: float) -> gp_Ax2d:
        """
        Rotates an axis placement. <theP> is the center of the rotation.
        theAng is the angular value of the rotation in radians.
        """

    def Scale(self, P: gp_Pnt2d, S: float) -> None: ...

    def Scaled(self, theP: gp_Pnt2d, theS: float) -> gp_Ax2d:
        """
        Applies a scaling transformation on the axis placement.
        The "Location" point of the axisplacement is modified.
        The "Direction" is reversed if the scale is negative.
        """

    def Transform(self, theT: gp_Trsf2d) -> None: ...

    def Transformed(self, theT: gp_Trsf2d) -> gp_Ax2d:
        """Transforms an axis placement with a Trsf."""

    @overload
    def Translate(self, theV: gp_Vec2d) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec2d) -> gp_Ax2d:
        """
        Translates an axis placement in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> gp_Ax2d:
        """Translates an axis placement from the point theP1 to the point theP2."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class gp_Vec:
    """Defines a non-persistent vector in 3D space."""

    @overload
    def __init__(self) -> None:
        """Creates a zero vector."""

    @overload
    def __init__(self, theV: gp_Dir) -> None:
        """Creates a unitary vector from a direction theV."""

    @overload
    def __init__(self, theCoord: gp_XYZ) -> None:
        """Creates a vector with a triplet of coordinates."""

    @overload
    def __init__(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None:
        """
        Creates a vector from two points. The length of the vector
        is the distance between theP1 and theP2
        """

    @overload
    def __init__(self, theXv: float, theYv: float, theZv: float) -> None:
        """Creates a point with its three cartesian coordinates."""

    @overload
    def __init__(self, theOther: gp_Vec) -> None: ...

    @overload
    def SetCoord(self, theIndex: int, theXi: float) -> None:
        """
        Changes the coordinate of range theIndex
        theIndex = 1 => X is modified
        theIndex = 2 => Y is modified
        theIndex = 3 => Z is modified
        Raised if theIndex != {1, 2, 3}.
        """

    @overload
    def SetCoord(self, theXv: float, theYv: float, theZv: float) -> None:
        """
        For this vector, assigns
        -   the values theXv, theYv and theZv to its three coordinates.
        """

    def SetX(self, theX: float) -> None:
        """Assigns the given value to the X coordinate of this vector."""

    def SetY(self, theY: float) -> None:
        """Assigns the given value to the X coordinate of this vector."""

    def SetZ(self, theZ: float) -> None:
        """Assigns the given value to the X coordinate of this vector."""

    def SetXYZ(self, theCoord: gp_XYZ) -> None:
        """Assigns the three coordinates of theCoord to this vector."""

    @overload
    def Coord(self, theIndex: int) -> float:
        """
        Returns the coordinate of range theIndex :
        theIndex = 1 => X is returned
        theIndex = 2 => Y is returned
        theIndex = 3 => Z is returned
        Raised if theIndex != {1, 2, 3}.
        """

    @overload
    def Coord(self) -> tuple[float, float, float]:
        """
        For this vector returns its three coordinates theXv, theYv, and theZv inline
        """

    def X(self) -> float:
        """For this vector, returns its X coordinate."""

    def Y(self) -> float:
        """For this vector, returns its Y coordinate."""

    def Z(self) -> float:
        """For this vector, returns its Z coordinate."""

    def XYZ(self) -> gp_XYZ:
        """
        For this vector, returns
        -   its three coordinates as a number triple
        """

    def IsEqual(self, theOther: gp_Vec, theLinearTolerance: float, theAngularTolerance: float) -> bool:
        """
        Returns True if the two vectors have the same magnitude value
        and the same direction. The precision values are theLinearTolerance
        for the magnitude and theAngularTolerance for the direction.
        """

    def IsNormal(self, theOther: gp_Vec, theAngularTolerance: float) -> bool:
        """
        Returns True if abs(<me>.Angle(theOther) - PI/2.) <= theAngularTolerance
        Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or
        theOther.Magnitude() <= Resolution from gp
        """

    def IsOpposite(self, theOther: gp_Vec, theAngularTolerance: float) -> bool:
        """
        Returns True if PI - <me>.Angle(theOther) <= theAngularTolerance
        Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or
        Other.Magnitude() <= Resolution from gp
        """

    def IsParallel(self, theOther: gp_Vec, theAngularTolerance: float) -> bool:
        """
        Returns True if Angle(<me>, theOther) <= theAngularTolerance or
        PI - Angle(<me>, theOther) <= theAngularTolerance
        This definition means that two parallel vectors cannot define
        a plane but two vectors with opposite directions are considered
        as parallel. Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution or
        Other.Magnitude() <= Resolution from gp
        """

    def Angle(self, theOther: gp_Vec) -> float:
        """
        Computes the angular value between <me> and <theOther>
        Returns the angle value between 0 and PI in radian.
        Raises VectorWithNullMagnitude if <me>.Magnitude() <= Resolution from gp or
        theOther.Magnitude() <= Resolution because the angular value is
        indefinite if one of the vectors has a null magnitude.
        """

    def AngleWithRef(self, theOther: gp_Vec, theVRef: gp_Vec) -> float:
        """
        Computes the angle, in radians, between this vector and
        vector theOther. The result is a value between -Pi and Pi.
        For this, theVRef defines the positive sense of rotation: the
        angular value is positive, if the cross product this ^ theOther
        has the same orientation as theVRef relative to the plane
        defined by the vectors this and theOther. Otherwise, the
        angular value is negative.
        Exceptions
        gp_VectorWithNullMagnitude if the magnitude of this
        vector, the vector theOther, or the vector theVRef is less than or
        equal to gp::Resolution().
        Standard_DomainError if this vector, the vector theOther,
        and the vector theVRef are coplanar, unless this vector and
        the vector theOther are parallel.
        """

    def Magnitude(self) -> float:
        """Computes the magnitude of this vector."""

    def SquareMagnitude(self) -> float:
        """Computes the square magnitude of this vector."""

    def Add(self, theOther: gp_Vec) -> None:
        """Adds two vectors"""

    def __iadd__(self, theOther: gp_Vec) -> gp_Vec: ...

    def Added(self, theOther: gp_Vec) -> gp_Vec:
        """Adds two vectors"""

    def __add__(self, theOther: gp_Vec) -> gp_Vec: ...

    def Subtract(self, theRight: gp_Vec) -> None:
        """Subtracts two vectors"""

    def __isub__(self, theRight: gp_Vec) -> gp_Vec: ...

    def Subtracted(self, theRight: gp_Vec) -> gp_Vec:
        """Subtracts two vectors"""

    def __sub__(self, theRight: gp_Vec) -> gp_Vec: ...

    def Multiply(self, theScalar: float) -> None:
        """Multiplies a vector by a scalar"""

    def __imul__(self, theScalar: float) -> gp_Vec: ...

    def Multiplied(self, theScalar: float) -> gp_Vec:
        """Multiplies a vector by a scalar"""

    @overload
    def __mul__(self, theScalar: float) -> gp_Vec: ...

    @overload
    def __mul__(self, theOther: gp_Vec) -> float: ...

    def Divide(self, theScalar: float) -> None:
        """Divides a vector by a scalar"""

    def __itruediv__(self, theScalar: float) -> gp_Vec: ...

    def Divided(self, theScalar: float) -> gp_Vec:
        """Divides a vector by a scalar"""

    def __truediv__(self, theScalar: float) -> gp_Vec: ...

    def Cross(self, theRight: gp_Vec) -> None:
        """computes the cross product between two vectors"""

    def __ixor__(self, theRight: gp_Vec) -> gp_Vec: ...

    def Crossed(self, theRight: gp_Vec) -> gp_Vec:
        """computes the cross product between two vectors"""

    def __xor__(self, theRight: gp_Vec) -> gp_Vec: ...

    def CrossMagnitude(self, theRight: gp_Vec) -> float:
        """
        Computes the magnitude of the cross
        product between <me> and theRight.
        Returns || <me> ^ theRight ||
        """

    def CrossSquareMagnitude(self, theRight: gp_Vec) -> float:
        """
        Computes the square magnitude of
        the cross product between <me> and theRight.
        Returns || <me> ^ theRight ||**2
        """

    def CrossCross(self, theV1: gp_Vec, theV2: gp_Vec) -> None:
        """
        Computes the triple vector product.
        <me> ^= (theV1 ^ theV2)
        """

    def CrossCrossed(self, theV1: gp_Vec, theV2: gp_Vec) -> gp_Vec:
        """
        Computes the triple vector product.
        <me> ^ (theV1 ^ theV2)
        """

    def Dot(self, theOther: gp_Vec) -> float:
        """computes the scalar product"""

    def DotCross(self, theV1: gp_Vec, theV2: gp_Vec) -> float:
        """Computes the triple scalar product <me> * (theV1 ^ theV2)."""

    def Normalize(self) -> None:
        """
        normalizes a vector
        Raises an exception if the magnitude of the vector is
        lower or equal to Resolution from gp.
        """

    def Normalized(self) -> gp_Vec:
        """
        normalizes a vector
        Raises an exception if the magnitude of the vector is
        lower or equal to Resolution from gp.
        """

    def Reverse(self) -> None:
        """Reverses the direction of a vector"""

    def Reversed(self) -> gp_Vec:
        """Reverses the direction of a vector"""

    def __neg__(self) -> gp_Vec: ...

    @overload
    def SetLinearForm(self, theA1: float, theV1: gp_Vec, theA2: float, theV2: gp_Vec, theA3: float, theV3: gp_Vec, theV4: gp_Vec) -> None:
        """
        <me> is set to the following linear form :
        theA1 * theV1 + theA2 * theV2 + theA3 * theV3 + theV4
        """

    @overload
    def SetLinearForm(self, theA1: float, theV1: gp_Vec, theA2: float, theV2: gp_Vec, theA3: float, theV3: gp_Vec) -> None:
        """
        <me> is set to the following linear form :
        theA1 * theV1 + theA2 * theV2 + theA3 * theV3
        """

    @overload
    def SetLinearForm(self, theA1: float, theV1: gp_Vec, theA2: float, theV2: gp_Vec, theV3: gp_Vec) -> None:
        """
        <me> is set to the following linear form :
        theA1 * theV1 + theA2 * theV2 + theV3
        """

    @overload
    def SetLinearForm(self, theA1: float, theV1: gp_Vec, theA2: float, theV2: gp_Vec) -> None:
        """
        <me> is set to the following linear form :
        theA1 * theV1 + theA2 * theV2
        """

    @overload
    def SetLinearForm(self, theA1: float, theV1: gp_Vec, theV2: gp_Vec) -> None:
        """<me> is set to the following linear form : theA1 * theV1 + theV2"""

    @overload
    def SetLinearForm(self, theV1: gp_Vec, theV2: gp_Vec) -> None:
        """<me> is set to the following linear form : theV1 + theV2"""

    @overload
    def Mirror(self, theV: gp_Vec) -> None: ...

    @overload
    def Mirror(self, theA1: gp_Ax1) -> None: ...

    @overload
    def Mirror(self, theA2: gp_Ax2) -> None: ...

    @overload
    def Mirrored(self, theV: gp_Vec) -> gp_Vec:
        """
        Performs the symmetrical transformation of a vector
        with respect to the vector theV which is the center of
        the symmetry.
        """

    @overload
    def Mirrored(self, theA1: gp_Ax1) -> gp_Vec:
        """
        Performs the symmetrical transformation of a vector
        with respect to an axis placement which is the axis
        of the symmetry.
        """

    @overload
    def Mirrored(self, theA2: gp_Ax2) -> gp_Vec:
        """
        Performs the symmetrical transformation of a vector
        with respect to a plane. The axis placement theA2 locates
        the plane of the symmetry : (Location, XDirection, YDirection).
        """

    def Rotate(self, theA1: gp_Ax1, theAng: float) -> None: ...

    def Rotated(self, theA1: gp_Ax1, theAng: float) -> gp_Vec:
        """
        Rotates a vector. theA1 is the axis of the rotation.
        theAng is the angular value of the rotation in radians.
        """

    def Scale(self, theS: float) -> None: ...

    def Scaled(self, theS: float) -> gp_Vec:
        """Scales a vector. theS is the scaling value."""

    def Transform(self, theT: gp_Trsf) -> None:
        """Transforms a vector with the transformation theT."""

    def Transformed(self, theT: gp_Trsf) -> gp_Vec:
        """Transforms a vector with the transformation theT."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def __rmul__(self, arg: float, /) -> gp_Vec: ...

class gp_Dir:
    """
    Describes a unit vector in 3D space. This unit vector is also called "Direction".
    See Also
    gce_MakeDir which provides functions for more complex
    unit vector constructions
    Geom_Direction which provides additional functions for
    constructing unit vectors and works, in particular, with the
    parametric equations of unit vectors.
    """

    @overload
    def __init__(self) -> None:
        """Creates a direction corresponding to X axis."""

    @overload
    def __init__(self, theDir: gp_Dir.D) -> None:
        """Creates a direction from a standard direction enumeration."""

    @overload
    def __init__(self, theV: gp_Vec) -> None:
        """
        Normalizes the vector theV and creates a direction. Raises ConstructionError if
        theV.Magnitude() <= Resolution.
        @note Constexpr-compatible when input is already normalized.
        """

    @overload
    def __init__(self, theCoord: gp_XYZ) -> None:
        """
        Creates a direction from a triplet of coordinates. Raises ConstructionError if
        theCoord.Modulus() <= Resolution from gp.
        @note Constexpr-compatible when input is already normalized.
        """

    @overload
    def __init__(self, arg0: gp_Dir) -> None: ...

    @overload
    def __init__(self, theXv: float, theYv: float, theZv: float) -> None:
        """
        Creates a direction with its 3 cartesian coordinates. Raises ConstructionError if
        std::sqrt(theXv*theXv + theYv*theYv + theZv*theZv) <= Resolution Modification of the
        direction's coordinates If std::sqrt (theXv*theXv + theYv*theYv + theZv*theZv) <= Resolution
        from gp where theXv, theYv ,theZv are the new coordinates it is not possible to construct the
        direction and the method raises the exception ConstructionError.
        @note Constexpr-compatible when input is already normalized.
        """

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeDir) -> None: ...

    class D(enum.Enum):
        """Standard directions in 3D space for optimized constexpr construction"""

        X = 0

        Y = 1

        Z = 2

        NX = 3

        NY = 4

        NZ = 5

    @overload
    def SetCoord(self, theIndex: int, theXi: float) -> None:
        """
        For this unit vector, assigns the value Xi to:
        -   the X coordinate if theIndex is 1, or
        -   the Y coordinate if theIndex is 2, or
        -   the Z coordinate if theIndex is 3,
        and then normalizes it.
        Warning:
        Remember that all the coordinates of a unit vector are
        implicitly modified when any single one is changed directly.
        Exceptions
        Standard_OutOfRange if theIndex is not 1, 2, or 3.
        Standard_ConstructionError if either of the following
        is less than or equal to gp::Resolution():
        -   std::sqrt(Xv*Xv + Yv*Yv + Zv*Zv), or
        -   the modulus of the number triple formed by the new
        value theXi and the two other coordinates of this vector
        that were not directly modified.
        @note Constexpr-compatible when result is already normalized.
        """

    @overload
    def SetCoord(self, theXv: float, theYv: float, theZv: float) -> None:
        """
        For this unit vector, assigns the values theXv, theYv and theZv to its three coordinates.
        Remember that all the coordinates of a unit vector are
        implicitly modified when any single one is changed directly.
        @note Constexpr-compatible when input is already normalized.
        """

    def SetX(self, theX: float) -> None:
        """
        Assigns the given value to the X coordinate of this unit vector.
        @note Constexpr-compatible when result is already normalized.
        """

    def SetY(self, theY: float) -> None:
        """
        Assigns the given value to the Y coordinate of this unit vector.
        @note Constexpr-compatible when result is already normalized.
        """

    def SetZ(self, theZ: float) -> None:
        """
        Assigns the given value to the Z coordinate of this unit vector.
        @note Constexpr-compatible when result is already normalized.
        """

    def SetXYZ(self, theCoord: gp_XYZ) -> None:
        """
        Assigns the three coordinates of theCoord to this unit vector.
        @note Constexpr-compatible when input is already normalized.
        """

    @overload
    def Coord(self, theIndex: int) -> float:
        """
        Returns the coordinate of range theIndex :
        theIndex = 1 => X is returned
        theIndex = 2 => Y is returned
        theIndex = 3 => Z is returned
        Exceptions
        Standard_OutOfRange if theIndex is not 1, 2, or 3.
        """

    @overload
    def Coord(self) -> tuple[float, float, float]:
        """
        Returns for the unit vector its three coordinates theXv, theYv, and theZv.
        """

    def X(self) -> float:
        """Returns the X coordinate for a unit vector."""

    def Y(self) -> float:
        """Returns the Y coordinate for a unit vector."""

    def Z(self) -> float:
        """Returns the Z coordinate for a unit vector."""

    def XYZ(self) -> gp_XYZ:
        """
        for this unit vector, returns its three coordinates as a number triple.
        """

    def IsEqual(self, theOther: gp_Dir, theAngularTolerance: float) -> bool:
        """
        Returns True if the angle between the two directions is
        lower or equal to theAngularTolerance.
        """

    def IsNormal(self, theOther: gp_Dir, theAngularTolerance: float) -> bool:
        """
        Returns True if the angle between this unit vector and the unit vector theOther is equal to
        Pi/2 (normal).
        """

    def IsOpposite(self, theOther: gp_Dir, theAngularTolerance: float) -> bool:
        """
        Returns True if the angle between this unit vector and the unit vector theOther is equal to
        Pi (opposite).
        """

    def IsParallel(self, theOther: gp_Dir, theAngularTolerance: float) -> bool:
        """
        Returns true if the angle between this unit vector and the
        unit vector theOther is equal to 0 or to Pi.
        Note: the tolerance criterion is given by theAngularTolerance.
        """

    def Angle(self, theOther: gp_Dir) -> float:
        """
        Computes the angular value in radians between <me> and
        <theOther>. This value is always positive in 3D space.
        Returns the angle in the range [0, PI]
        """

    def AngleWithRef(self, theOther: gp_Dir, theVRef: gp_Dir) -> float:
        """
        Computes the angular value between <me> and <theOther>.
        <theVRef> is the direction of reference normal to <me> and <theOther>
        and its orientation gives the positive sense of rotation.
        If the cross product <me> ^ <theOther> has the same orientation
        as <theVRef> the angular value is positive else negative.
        Returns the angular value in the range -PI and PI (in radians). Raises DomainError if <me>
        and <theOther> are not parallel this exception is raised when <theVRef> is in the same plane
        as <me> and <theOther> The tolerance criterion is Resolution from package gp.
        """

    def Cross(self, theRight: gp_Dir) -> None:
        """
        Computes the cross product between two directions
        Raises the exception ConstructionError if the two directions
        are parallel because the computed vector cannot be normalized
        to create a direction.
        @note Constexpr-compatible when result is already normalized.
        """

    def __ixor__(self, theRight: gp_Dir) -> gp_Dir: ...

    def Crossed(self, theRight: gp_Dir) -> gp_Dir:
        """
        Computes the triple vector product.
        <me> ^ (V1 ^ V2)
        Raises the exception ConstructionError if V1 and V2 are parallel
        or <me> and (V1^V2) are parallel because the computed vector
        can't be normalized to create a direction.
        @note Constexpr-compatible when result is already normalized.
        """

    def __xor__(self, theRight: gp_Dir) -> gp_Dir: ...

    def CrossCross(self, theV1: gp_Dir, theV2: gp_Dir) -> None:
        """@note Constexpr-compatible when result is already normalized."""

    def CrossCrossed(self, theV1: gp_Dir, theV2: gp_Dir) -> gp_Dir:
        """
        Computes the double vector product this ^ (theV1 ^ theV2).
        -   CrossCrossed creates a new unit vector.
        Exceptions
        Standard_ConstructionError if:
        -   theV1 and theV2 are parallel, or
        -   this unit vector and (theV1 ^ theV2) are parallel.
        This is because, in these conditions, the computed vector
        is null and cannot be normalized.
        @note Constexpr-compatible when result is already normalized.
        """

    def Dot(self, theOther: gp_Dir) -> float:
        """Computes the scalar product"""

    def __mul__(self, theOther: gp_Dir) -> float: ...

    def DotCross(self, theV1: gp_Dir, theV2: gp_Dir) -> float:
        """
        Computes the triple scalar product <me> * (theV1 ^ theV2).
        Warnings :
        The computed vector theV1' = theV1 ^ theV2 is not normalized
        to create a unitary vector. So this method never
        raises an exception even if theV1 and theV2 are parallel.
        """

    def Reverse(self) -> None: ...

    def Reversed(self) -> gp_Dir:
        """
        Reverses the orientation of a direction
        geometric transformations
        Performs the symmetrical transformation of a direction
        with respect to the direction V which is the center of
        the symmetry.
        """

    def __neg__(self) -> gp_Dir: ...

    @overload
    def Mirror(self, theV: gp_Dir) -> None: ...

    @overload
    def Mirror(self, theA1: gp_Ax1) -> None: ...

    @overload
    def Mirror(self, theA2: gp_Ax2) -> None: ...

    @overload
    def Mirrored(self, theV: gp_Dir) -> gp_Dir:
        """
        Performs the symmetrical transformation of a direction
        with respect to the direction theV which is the center
        of the symmetry.
        """

    @overload
    def Mirrored(self, theA1: gp_Ax1) -> gp_Dir:
        """
        Performs the symmetrical transformation of a direction
        with respect to an axis placement which is the axis
        of the symmetry.
        """

    @overload
    def Mirrored(self, theA2: gp_Ax2) -> gp_Dir:
        """
        Performs the symmetrical transformation of a direction
        with respect to a plane. The axis placement theA2 locates
        the plane of the symmetry : (Location, XDirection, YDirection).
        """

    def Rotate(self, theA1: gp_Ax1, theAng: float) -> None: ...

    def Rotated(self, theA1: gp_Ax1, theAng: float) -> gp_Dir:
        """
        Rotates a direction. theA1 is the axis of the rotation.
        theAng is the angular value of the rotation in radians.
        """

    def Transform(self, theT: gp_Trsf) -> None: ...

    def Transformed(self, theT: gp_Trsf) -> gp_Dir:
        """
        Transforms a direction with a "Trsf" from gp.
        Warnings :
        If the scale factor of the "Trsf" theT is negative then the
        direction <me> is reversed.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def InitFromJson(self, theSStream: TextIO, theStreamPos: int) -> tuple[bool, int]:
        """Inits the content of me from the stream"""

class gp_Ax1:
    """
    Describes an axis in 3D space.
    An axis is defined by:
    -   its origin (also referred to as its "Location point"), and
    -   its unit vector (referred to as its "Direction" or "main   Direction").
    An axis is used:
    -   to describe 3D geometric entities (for example, the
    axis of a revolution entity). It serves the same purpose
    as the STEP function "axis placement one axis", or
    -   to define geometric transformations (axis of
    symmetry, axis of rotation, and so on).
    For example, this entity can be used to locate a geometric entity
    or to define a symmetry axis.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an axis object representing Z axis of
        the reference coordinate system.
        """

    @overload
    def __init__(self, theDir: gp_Dir.D) -> None:
        """
        Creates an axis at the origin with the given standard direction.
        Replaces gp::OX(), gp::OY(), gp::OZ() static functions.
        """

    @overload
    def __init__(self, theP: gp_Pnt, theV: gp_Dir) -> None:
        """P is the location point and V is the direction of <me>."""

    @overload
    def __init__(self, theP: gp_Pnt, theDir: gp_Dir.D) -> None:
        """Creates an axis with the given location point and standard direction."""

    @overload
    def __init__(self, theOther: gp_Ax1) -> None: ...

    def SetDirection(self, theV: gp_Dir) -> None:
        """Assigns V as the "Direction" of this axis."""

    def SetLocation(self, theP: gp_Pnt) -> None:
        """Assigns P as the origin of this axis."""

    def Direction(self) -> gp_Dir:
        """Returns the direction of <me>."""

    def Location(self) -> gp_Pnt:
        """Returns the location point of <me>."""

    def IsCoaxial(self, Other: gp_Ax1, AngularTolerance: float, LinearTolerance: float) -> bool:
        """
        Returns True if:
        . the angle between <me> and <Other> is lower or equal
        to <AngularTolerance> and
        . the distance between <me>.Location() and <Other> is lower
        or equal to <LinearTolerance> and
        . the distance between <Other>.Location() and <me> is lower
        or equal to LinearTolerance.
        """

    def IsNormal(self, theOther: gp_Ax1, theAngularTolerance: float) -> bool:
        """
        Returns True if the direction of this and another axis are normal to each other.
        That is, if the angle between the two axes is equal to Pi/2.
        Note: the tolerance criterion is given by theAngularTolerance.
        """

    def IsOpposite(self, theOther: gp_Ax1, theAngularTolerance: float) -> bool:
        """
        Returns True if the direction of this and another axis are parallel with opposite orientation.
        That is, if the angle between the two axes is equal to Pi.
        Note: the tolerance criterion is given by theAngularTolerance.
        """

    def IsParallel(self, theOther: gp_Ax1, theAngularTolerance: float) -> bool:
        """
        Returns True if the direction of this and another axis are parallel with same orientation or
        opposite orientation. That is, if the angle between the two axes is equal to 0 or Pi. Note:
        the tolerance criterion is given by theAngularTolerance.
        """

    def Angle(self, theOther: gp_Ax1) -> float:
        """
        Computes the angular value, in radians, between this.Direction() and theOther.Direction().
        Returns the angle between 0 and 2*PI radians.
        """

    def Reverse(self) -> None:
        """
        Reverses the unit vector of this axis and assigns the result to this axis.
        """

    def Reversed(self) -> gp_Ax1:
        """Reverses the unit vector of this axis and creates a new one."""

    @overload
    def Mirror(self, P: gp_Pnt) -> None:
        """
        Performs the symmetrical transformation of an axis
        placement with respect to the point P which is the
        center of the symmetry and assigns the result to this axis.
        """

    @overload
    def Mirror(self, A1: gp_Ax1) -> None:
        """
        Performs the symmetrical transformation of an axis
        placement with respect to an axis placement which
        is the axis of the symmetry and assigns the result to this axis.
        """

    @overload
    def Mirror(self, A2: gp_Ax2) -> None:
        """
        Performs the symmetrical transformation of an axis
        placement with respect to a plane. The axis placement
        <A2> locates the plane of the symmetry :
        (Location, XDirection, YDirection) and assigns the result to this axis.
        """

    @overload
    def Mirrored(self, P: gp_Pnt) -> gp_Ax1:
        """
        Performs the symmetrical transformation of an axis
        placement with respect to the point P which is the
        center of the symmetry and creates a new axis.
        """

    @overload
    def Mirrored(self, A1: gp_Ax1) -> gp_Ax1:
        """
        Performs the symmetrical transformation of an axis
        placement with respect to an axis placement which
        is the axis of the symmetry and creates a new axis.
        """

    @overload
    def Mirrored(self, A2: gp_Ax2) -> gp_Ax1:
        """
        Performs the symmetrical transformation of an axis
        placement with respect to a plane. The axis placement
        <A2> locates the plane of the symmetry :
        (Location, XDirection, YDirection) and creates a new axis.
        """

    def Rotate(self, theA1: gp_Ax1, theAngRad: float) -> None:
        """
        Rotates this axis at an angle theAngRad (in radians) about the axis theA1
        and assigns the result to this axis.
        """

    def Rotated(self, theA1: gp_Ax1, theAngRad: float) -> gp_Ax1:
        """
        Rotates this axis at an angle theAngRad (in radians) about the axis theA1
        and creates a new one.
        """

    def Scale(self, theP: gp_Pnt, theS: float) -> None:
        """
        Applies a scaling transformation to this axis with:
        - scale factor theS, and
        - center theP and assigns the result to this axis.
        """

    def Scaled(self, theP: gp_Pnt, theS: float) -> gp_Ax1:
        """
        Applies a scaling transformation to this axis with:
        - scale factor theS, and
        - center theP and creates a new axis.
        """

    def Transform(self, theT: gp_Trsf) -> None:
        """
        Applies the transformation theT to this axis and assigns the result to this axis.
        """

    def Transformed(self, theT: gp_Trsf) -> gp_Ax1:
        """
        Applies the transformation theT to this axis and creates a new one.

        Translates an axis plaxement in the direction of the vector <V>.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translate(self, theV: gp_Vec) -> None:
        """
        Translates this axis by the vector theV, and assigns the result to this axis.
        """

    @overload
    def Translate(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None:
        """
        Translates this axis by:
        the vector (theP1, theP2) defined from point theP1 to point theP2.
        and assigns the result to this axis.
        """

    @overload
    def Translated(self, theV: gp_Vec) -> gp_Ax1:
        """
        Translates this axis by the vector theV,
        and creates a new one.
        """

    @overload
    def Translated(self, theP1: gp_Pnt, theP2: gp_Pnt) -> gp_Ax1:
        """
        Translates this axis by:
        the vector (theP1, theP2) defined from point theP1 to point theP2.
        and creates a new one.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def InitFromJson(self, theSStream: TextIO, theStreamPos: int) -> tuple[bool, int]:
        """Inits the content of me from the stream"""

class gp_Ax2:
    """
    Describes a right-handed coordinate system in 3D space.
    A coordinate system is defined by:
    -   its origin (also referred to as its "Location point"), and
    -   three orthogonal unit vectors, termed respectively the
    "X Direction", the "Y Direction" and the "Direction" (also
    referred to as the "main Direction").
    The "Direction" of the coordinate system is called its
    "main Direction" because whenever this unit vector is
    modified, the "X Direction" and the "Y Direction" are
    recomputed. However, when we modify either the "X
    Direction" or the "Y Direction", "Direction" is not modified.
    The "main Direction" is also the "Z Direction".
    Since an Ax2 coordinate system is right-handed, its
    "main Direction" is always equal to the cross product of
    its "X Direction" and "Y Direction". (To define a
    left-handed coordinate system, use gp_Ax3.)
    A coordinate system is used:
    -   to describe geometric entities, in particular to position
    them. The local coordinate system of a geometric
    entity serves the same purpose as the STEP function
    "axis placement two axes", or
    -   to define geometric transformations.
    Note: we refer to the "X Axis", "Y Axis" and "Z Axis",
    respectively, as to axes having:
    - the origin of the coordinate system as their origin, and
    -   the unit vectors "X Direction", "Y Direction" and "main
    Direction", respectively, as their unit vectors.
    The "Z Axis" is also the "main Axis".
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an object corresponding to the reference
        coordinate system (OXYZ).
        """

    @overload
    def __init__(self, theV: gp_Dir.D) -> None:
        """
        Creates a coordinate system at the origin with the given standard main direction.
        Replaces gp::XOY(), gp::YOZ(), gp::ZOX() static functions.
        """

    @overload
    def __init__(self, P: gp_Pnt, V: gp_Dir) -> None:
        """
        Creates a coordinate system with an origin P, where V
        gives the "main Direction" (here, "X Direction" and "Y
        Direction" are defined automatically).
        """

    @overload
    def __init__(self, theP: gp_Pnt, theV: gp_Dir.D) -> None:
        """
        Creates a coordinate system with an origin P and standard main direction.
        """

    @overload
    def __init__(self, P: gp_Pnt, N: gp_Dir, Vx: gp_Dir) -> None:
        """
        Creates an axis placement with an origin P such that:
        -   N is the Direction, and
        -   the "X Direction" is normal to N, in the plane
        defined by the vectors (N, Vx): "X
        Direction" = (N ^ Vx) ^ N,
        Exception: raises ConstructionError if N and Vx are parallel (same or opposite orientation).
        """

    @overload
    def __init__(self, theP: gp_Pnt, theN: gp_Dir.D, theVx: gp_Dir.D) -> None:
        """Creates an axis placement with standard directions."""

    @overload
    def __init__(self, theOther: gp_Ax2) -> None: ...

    def SetAxis(self, A1: gp_Ax1) -> None:
        """
        Assigns the origin and "main Direction" of the axis A1 to
        this coordinate system, then recomputes its "X Direction" and "Y Direction".
        Note: The new "X Direction" is computed as follows:
        new "X Direction" = V1 ^(previous "X Direction" ^ V)
        where V is the "Direction" of A1.
        Exceptions
        Standard_ConstructionError if A1 is parallel to the "X
        Direction" of this coordinate system.
        """

    def SetDirection(self, V: gp_Dir) -> None:
        """
        Changes the "main Direction" of this coordinate system,
        then recomputes its "X Direction" and "Y Direction".
        Note: the new "X Direction" is computed as follows:
        new "X Direction" = V ^ (previous "X Direction" ^ V)
        Exceptions
        Standard_ConstructionError if V is parallel to the "X
        Direction" of this coordinate system.
        """

    def SetLocation(self, theP: gp_Pnt) -> None:
        """Changes the "Location" point (origin) of <me>."""

    def SetXDirection(self, theVx: gp_Dir) -> None:
        """
        Changes the "Xdirection" of <me>. The main direction
        "Direction" is not modified, the "Ydirection" is modified.
        If <Vx> is not normal to the main direction then <XDirection>
        is computed as follows XDirection = Direction ^ (Vx ^ Direction).
        Exceptions
        Standard_ConstructionError if Vx or Vy is parallel to
        the "main Direction" of this coordinate system.
        """

    def SetYDirection(self, theVy: gp_Dir) -> None:
        """
        Changes the "Ydirection" of <me>. The main direction is not
        modified but the "Xdirection" is changed.
        If <Vy> is not normal to the main direction then "YDirection"
        is computed as follows
        YDirection = Direction ^ (<Vy> ^ Direction).
        Exceptions
        Standard_ConstructionError if Vx or Vy is parallel to
        the "main Direction" of this coordinate system.
        """

    def Angle(self, theOther: gp_Ax2) -> float:
        """
        Computes the angular value, in radians, between the main direction of
        <me> and the main direction of <theOther>. Returns the angle
        between 0 and PI in radians.
        """

    def Axis(self) -> gp_Ax1:
        """
        Returns the main axis of <me>. It is the "Location" point
        and the main "Direction".
        """

    def Direction(self) -> gp_Dir:
        """Returns the main direction of <me>."""

    def Location(self) -> gp_Pnt:
        """Returns the "Location" point (origin) of <me>."""

    def XDirection(self) -> gp_Dir:
        """Returns the "XDirection" of <me>."""

    def YDirection(self) -> gp_Dir:
        """Returns the "YDirection" of <me>."""

    @overload
    def IsCoplanar(self, Other: gp_Ax2, LinearTolerance: float, AngularTolerance: float) -> bool: ...

    @overload
    def IsCoplanar(self, A1: gp_Ax1, LinearTolerance: float, AngularTolerance: float) -> bool:
        """
        Returns True if:
        . the distance between <me> and the "Location" point of A1
        is lower of equal to LinearTolerance and
        . the main direction of <me> and the direction of A1 are normal.
        Note: the tolerance criterion for angular equality is given by AngularTolerance.
        """

    @overload
    def Mirror(self, P: gp_Pnt) -> None:
        """
        Performs a symmetrical transformation of this coordinate
        system with respect to:
        -   the point P, and assigns the result to this coordinate system.
        Warning
        This transformation is always performed on the origin.
        In case of a reflection with respect to a point:
        - the main direction of the coordinate system is not changed, and
        - the "X Direction" and the "Y Direction" are simply reversed
        In case of a reflection with respect to an axis or a plane:
        -   the transformation is applied to the "X Direction"
        and the "Y Direction", then
        -   the "main Direction" is recomputed as the cross
        product "X Direction" ^ "Y Direction".
        This maintains the right-handed property of the
        coordinate system.
        """

    @overload
    def Mirror(self, A1: gp_Ax1) -> None:
        """
        Performs a symmetrical transformation of this coordinate
        system with respect to:
        -   the axis A1, and assigns the result to this coordinate system.
        Warning
        This transformation is always performed on the origin.
        In case of a reflection with respect to a point:
        - the main direction of the coordinate system is not changed, and
        - the "X Direction" and the "Y Direction" are simply reversed
        In case of a reflection with respect to an axis or a plane:
        -   the transformation is applied to the "X Direction"
        and the "Y Direction", then
        -   the "main Direction" is recomputed as the cross
        product "X Direction" ^ "Y Direction".
        This maintains the right-handed property of the
        coordinate system.
        """

    @overload
    def Mirror(self, A2: gp_Ax2) -> None:
        """
        Performs a symmetrical transformation of this coordinate
        system with respect to:
        -   the plane defined by the origin, "X Direction" and "Y
        Direction" of coordinate system A2 and assigns the result to this coordinate system.
        Warning
        This transformation is always performed on the origin.
        In case of a reflection with respect to a point:
        - the main direction of the coordinate system is not changed, and
        - the "X Direction" and the "Y Direction" are simply reversed
        In case of a reflection with respect to an axis or a plane:
        -   the transformation is applied to the "X Direction"
        and the "Y Direction", then
        -   the "main Direction" is recomputed as the cross
        product "X Direction" ^ "Y Direction".
        This maintains the right-handed property of the
        coordinate system.
        """

    @overload
    def Mirrored(self, P: gp_Pnt) -> gp_Ax2:
        """
        Performs a symmetrical transformation of this coordinate
        system with respect to:
        -   the point P, and creates a new one.
        Warning
        This transformation is always performed on the origin.
        In case of a reflection with respect to a point:
        - the main direction of the coordinate system is not changed, and
        - the "X Direction" and the "Y Direction" are simply reversed
        In case of a reflection with respect to an axis or a plane:
        -   the transformation is applied to the "X Direction"
        and the "Y Direction", then
        -   the "main Direction" is recomputed as the cross
        product "X Direction" ^ "Y Direction".
        This maintains the right-handed property of the
        coordinate system.
        """

    @overload
    def Mirrored(self, A1: gp_Ax1) -> gp_Ax2:
        """
        Performs a symmetrical transformation of this coordinate
        system with respect to:
        -   the axis A1, and creates a new one.
        Warning
        This transformation is always performed on the origin.
        In case of a reflection with respect to a point:
        - the main direction of the coordinate system is not changed, and
        - the "X Direction" and the "Y Direction" are simply reversed
        In case of a reflection with respect to an axis or a plane:
        -   the transformation is applied to the "X Direction"
        and the "Y Direction", then
        -   the "main Direction" is recomputed as the cross
        product "X Direction" ^ "Y Direction".
        This maintains the right-handed property of the
        coordinate system.
        """

    @overload
    def Mirrored(self, A2: gp_Ax2) -> gp_Ax2:
        """
        Performs a symmetrical transformation of this coordinate
        system with respect to:
        -   the plane defined by the origin, "X Direction" and "Y
        Direction" of coordinate system A2 and creates a new one.
        Warning
        This transformation is always performed on the origin.
        In case of a reflection with respect to a point:
        - the main direction of the coordinate system is not changed, and
        - the "X Direction" and the "Y Direction" are simply reversed
        In case of a reflection with respect to an axis or a plane:
        -   the transformation is applied to the "X Direction"
        and the "Y Direction", then
        -   the "main Direction" is recomputed as the cross
        product "X Direction" ^ "Y Direction".
        This maintains the right-handed property of the
        coordinate system.
        """

    def Rotate(self, theA1: gp_Ax1, theAng: float) -> None: ...

    def Rotated(self, theA1: gp_Ax1, theAng: float) -> gp_Ax2:
        """
        Rotates an axis placement. <theA1> is the axis of the rotation.
        theAng is the angular value of the rotation in radians.
        """

    def Scale(self, theP: gp_Pnt, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt, theS: float) -> gp_Ax2:
        """
        Applies a scaling transformation on the axis placement.
        The "Location" point of the axisplacement is modified.
        Warnings:
        If the scale <S> is negative:
        . the main direction of the axis placement is not changed.
        . The "XDirection" and the "YDirection" are reversed.
        So the axis placement stay right handed.
        """

    def Transform(self, theT: gp_Trsf) -> None: ...

    def Transformed(self, theT: gp_Trsf) -> gp_Ax2:
        """
        Transforms an axis placement with a Trsf.
        The "Location" point, the "XDirection" and the "YDirection" are transformed with theT.
        The resulting main "Direction" of <me> is the cross product between
        the "XDirection" and the "YDirection" after transformation.
        """

    @overload
    def Translate(self, theV: gp_Vec) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec) -> gp_Ax2:
        """
        Translates an axis plaxement in the direction of the vector <theV>.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt, theP2: gp_Pnt) -> gp_Ax2:
        """
        Translates an axis placement from the point <theP1> to the point <theP2>.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def InitFromJson(self, theSStream: TextIO, theStreamPos: int) -> tuple[bool, int]:
        """Inits the content of me from the stream"""

class gp_Ax3:
    """
    Describes a coordinate system in 3D space. Unlike a
    gp_Ax2 coordinate system, a gp_Ax3 can be
    right-handed ("direct sense") or left-handed ("indirect sense").
    A coordinate system is defined by:
    -   its origin (also referred to as its "Location point"), and
    -   three orthogonal unit vectors, termed the "X
    Direction", the "Y Direction" and the "Direction" (also
    referred to as the "main Direction").
    The "Direction" of the coordinate system is called its
    "main Direction" because whenever this unit vector is
    modified, the "X Direction" and the "Y Direction" are
    recomputed. However, when we modify either the "X
    Direction" or the "Y Direction", "Direction" is not modified.
    "Direction" is also the "Z Direction".
    The "main Direction" is always parallel to the cross
    product of its "X Direction" and "Y Direction".
    If the coordinate system is right-handed, it satisfies the equation:
    "main Direction" = "X Direction" ^ "Y Direction"
    and if it is left-handed, it satisfies the equation:
    "main Direction" = -"X Direction" ^ "Y Direction"
    A coordinate system is used:
    -   to describe geometric entities, in particular to position
    them. The local coordinate system of a geometric
    entity serves the same purpose as the STEP function
    "axis placement three axes", or
    -   to define geometric transformations.
    Note:
    -   We refer to the "X Axis", "Y Axis" and "Z Axis",
    respectively, as the axes having:
    -   the origin of the coordinate system as their origin, and
    -   the unit vectors "X Direction", "Y Direction" and
    "main Direction", respectively, as their unit vectors.
    -   The "Z Axis" is also the "main Axis".
    -   gp_Ax2 is used to define a coordinate system that must be always right-handed.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an object corresponding to the reference
        coordinate system (OXYZ).
        """

    @overload
    def __init__(self, theA: gp_Ax2) -> None:
        """
        Creates a coordinate system from a right-handed
        coordinate system.
        """

    @overload
    def __init__(self, theV: gp_Dir.D) -> None:
        """
        Creates an axis placement at the origin with the given standard direction.
        """

    @overload
    def __init__(self, theP: gp_Pnt, theV: gp_Dir) -> None:
        """
        Creates an axis placement with the "Location" point <theP>
        and the normal direction <theV>.
        """

    @overload
    def __init__(self, theP: gp_Pnt, theV: gp_Dir.D) -> None:
        """
        Creates an axis placement with the given location point and standard direction.
        """

    @overload
    def __init__(self, theP: gp_Pnt, theN: gp_Dir, theVx: gp_Dir) -> None:
        """
        Creates a right handed axis placement with the
        "Location" point theP and two directions, theN gives the
        "Direction" and theVx gives the "XDirection".
        Raises ConstructionError if theN and theVx are parallel (same or opposite orientation).
        """

    @overload
    def __init__(self, theP: gp_Pnt, theN: gp_Dir.D, theVx: gp_Dir.D) -> None:
        """
        Creates an axis placement with standard directions.
        This constructor allows constexpr and noexcept construction when using standard directions.
        """

    @overload
    def __init__(self, theOther: gp_Ax3) -> None: ...

    def XReverse(self) -> None:
        """Reverses the X direction of <me>."""

    def YReverse(self) -> None:
        """Reverses the Y direction of <me>."""

    def ZReverse(self) -> None:
        """Reverses the Z direction of <me>."""

    def SetAxis(self, theA1: gp_Ax1) -> None:
        """
        Assigns the origin and "main Direction" of the axis theA1 to
        this coordinate system, then recomputes its "X Direction" and "Y Direction".
        Note:
        -   The new "X Direction" is computed as follows:
        new "X Direction" = V1 ^(previous "X Direction" ^ V)
        where V is the "Direction" of theA1.
        -   The orientation of this coordinate system
        (right-handed or left-handed) is not modified.
        Raises ConstructionError if the "Direction" of <theA1> and the "XDirection" of <me>
        are parallel (same or opposite orientation) because it is
        impossible to calculate the new "XDirection" and the new
        "YDirection".
        """

    def SetDirection(self, theV: gp_Dir) -> None:
        """
        Changes the main direction of this coordinate system,
        then recomputes its "X Direction" and "Y Direction".
        Note:
        -   The new "X Direction" is computed as follows:
        new "X Direction" = theV ^ (previous "X Direction" ^ theV).
        -   The orientation of this coordinate system (left- or right-handed) is not modified.
        Raises ConstructionError if <theV> and the previous "XDirection" are parallel
        because it is impossible to calculate the new "XDirection"
        and the new "YDirection".
        """

    def SetLocation(self, theP: gp_Pnt) -> None:
        """Changes the "Location" point (origin) of <me>."""

    def SetXDirection(self, theVx: gp_Dir) -> None:
        """
        Changes the "Xdirection" of <me>. The main direction
        "Direction" is not modified, the "Ydirection" is modified.
        If <theVx> is not normal to the main direction then <XDirection>
        is computed as follows XDirection = Direction ^ (theVx ^ Direction).
        Raises ConstructionError if <theVx> is parallel (same or opposite
        orientation) to the main direction of <me>
        """

    def SetYDirection(self, theVy: gp_Dir) -> None:
        """
        Changes the "Ydirection" of <me>. The main direction is not
        modified but the "Xdirection" is changed.
        If <theVy> is not normal to the main direction then "YDirection"
        is computed as follows
        YDirection = Direction ^ (<theVy> ^ Direction).
        Raises ConstructionError if <theVy> is parallel to the main direction of <me>
        """

    def Angle(self, theOther: gp_Ax3) -> float:
        """
        Computes the angular value between the main direction of
        <me> and the main direction of <theOther>. Returns the angle
        between 0 and PI in radians.
        """

    def Axis(self) -> gp_Ax1:
        """
        Returns the main axis of <me>. It is the "Location" point
        and the main "Direction".
        """

    def Ax2(self) -> gp_Ax2:
        """
        Computes a right-handed coordinate system with the
        same "X Direction" and "Y Direction" as those of this
        coordinate system, then recomputes the "main Direction".
        If this coordinate system is right-handed, the result
        returned is the same coordinate system. If this
        coordinate system is left-handed, the result is reversed.
        """

    def Direction(self) -> gp_Dir:
        """Returns the main direction of <me>."""

    def Location(self) -> gp_Pnt:
        """Returns the "Location" point (origin) of <me>."""

    def XDirection(self) -> gp_Dir:
        """Returns the "XDirection" of <me>."""

    def YDirection(self) -> gp_Dir:
        """Returns the "YDirection" of <me>."""

    def Direct(self) -> bool:
        """
        Returns True if the coordinate system is right-handed. i.e.
        XDirection().Crossed(YDirection()).Dot(Direction()) > 0
        """

    @overload
    def IsCoplanar(self, theOther: gp_Ax3, theLinearTolerance: float, theAngularTolerance: float) -> bool:
        """
        Returns True if
        . the distance between the "Location" point of <me> and
        <theOther> is lower or equal to theLinearTolerance and
        . the distance between the "Location" point of <theOther> and
        <me> is lower or equal to theLinearTolerance and
        . the main direction of <me> and the main direction of
        <theOther> are parallel (same or opposite orientation).
        """

    @overload
    def IsCoplanar(self, theA1: gp_Ax1, theLinearTolerance: float, theAngularTolerance: float) -> bool:
        """
        Returns True if
        . the distance between <me> and the "Location" point of theA1
        is lower of equal to theLinearTolerance and
        . the distance between theA1 and the "Location" point of <me>
        is lower or equal to theLinearTolerance and
        . the main direction of <me> and the direction of theA1 are normal.
        """

    @overload
    def Mirror(self, theP: gp_Pnt) -> None: ...

    @overload
    def Mirror(self, theA1: gp_Ax1) -> None: ...

    @overload
    def Mirror(self, theA2: gp_Ax2) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt) -> gp_Ax3:
        """
        Performs the symmetrical transformation of an axis
        placement with respect to the point theP which is the
        center of the symmetry.
        Warnings :
        The main direction of the axis placement is not changed.
        The "XDirection" and the "YDirection" are reversed.
        So the axis placement stay right handed.
        """

    @overload
    def Mirrored(self, theA1: gp_Ax1) -> gp_Ax3:
        """
        Performs the symmetrical transformation of an axis
        placement with respect to an axis placement which
        is the axis of the symmetry.
        The transformation is performed on the "Location"
        point, on the "XDirection" and "YDirection".
        The resulting main "Direction" is the cross product between
        the "XDirection" and the "YDirection" after transformation.
        """

    @overload
    def Mirrored(self, theA2: gp_Ax2) -> gp_Ax3:
        """
        Performs the symmetrical transformation of an axis
        placement with respect to a plane.
        The axis placement <theA2> locates the plane of the symmetry:
        (Location, XDirection, YDirection).
        The transformation is performed on the "Location"
        point, on the "XDirection" and "YDirection".
        The resulting main "Direction" is the cross product between
        the "XDirection" and the "YDirection" after transformation.
        """

    def Rotate(self, theA1: gp_Ax1, theAng: float) -> None: ...

    def Rotated(self, theA1: gp_Ax1, theAng: float) -> gp_Ax3:
        """
        Rotates an axis placement. <theA1> is the axis of the
        rotation. theAng is the angular value of the rotation
        in radians.
        """

    def Scale(self, theP: gp_Pnt, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt, theS: float) -> gp_Ax3:
        """
        Applies a scaling transformation on the axis placement.
        The "Location" point of the axisplacement is modified.
        Warnings:
        If the scale <theS> is negative :
        . the main direction of the axis placement is not changed.
        . The "XDirection" and the "YDirection" are reversed.
        So the axis placement stay right handed.
        """

    def Transform(self, theT: gp_Trsf) -> None: ...

    def Transformed(self, theT: gp_Trsf) -> gp_Ax3:
        """
        Transforms an axis placement with a Trsf.
        The "Location" point, the "XDirection" and the
        "YDirection" are transformed with theT. The resulting
        main "Direction" of <me> is the cross product between
        the "XDirection" and the "YDirection" after transformation.
        """

    @overload
    def Translate(self, theV: gp_Vec) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec) -> gp_Ax3:
        """
        Translates an axis plaxement in the direction of the vector
        <theV>. The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt, theP2: gp_Pnt) -> gp_Ax3:
        """
        Translates an axis placement from the point <theP1> to the
        point <theP2>.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def InitFromJson(self, theSStream: TextIO, theStreamPos: int) -> tuple[bool, int]:
        """Inits the content of me from the stream"""

class gp_Ax22d:
    """
    Describes a coordinate system in a plane (2D space).
    A coordinate system is defined by:
    -   its origin (also referred to as its "Location point"), and
    -   two orthogonal unit vectors, respectively, called the "X
    Direction" and the "Y Direction".
    A gp_Ax22d may be right-handed ("direct sense") or
    left-handed ("inverse" or "indirect sense").
    You use a gp_Ax22d to:
    - describe 2D geometric entities, in particular to position
    them. The local coordinate system of a geometric
    entity serves for the same purpose as the STEP
    function "axis placement two axes", or
    -   define geometric transformations.
    Note: we refer to the "X Axis" and "Y Axis" as the axes having:
    -   the origin of the coordinate system as their origin, and
    -   the unit vectors "X Direction" and "Y Direction",
    respectively, as their unit vectors.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an object representing the reference
        coordinate system (OXY).
        """

    @overload
    def __init__(self, theA: gp_Ax2d, theIsSense: bool = True) -> None:
        """
        Creates a coordinate system where its origin is the origin of
        theA and its "X Direction" is the unit vector of theA, which is:
        -   right-handed if theIsSense is true (default value), or
        -   left-handed if theIsSense is false.
        """

    @overload
    def __init__(self, theP: gp_Pnt2d, theV: gp_Dir2d, theIsSense: bool = True) -> None:
        """
        Creates a coordinate system with origin theP and "X Direction"
        theV, which is:
        -   right-handed if theIsSense is true (default value), or
        -   left-handed if theIsSense is false
        """

    @overload
    def __init__(self, theP: gp_Pnt2d, theVx: gp_Dir2d, theVy: gp_Dir2d) -> None:
        """
        Creates a coordinate system with origin theP and where:
        -   theVx is the "X Direction", and
        -   the "Y Direction" is orthogonal to theVx and
        oriented so that the cross products theVx^"Y
        Direction" and theVx^theVy have the same sign.
        Raises ConstructionError if theVx and theVy are parallel (same or opposite orientation).
        """

    @overload
    def __init__(self, theOther: gp_Ax22d) -> None: ...

    def SetAxis(self, theA1: gp_Ax22d) -> None:
        """
        Assigns the origin and the two unit vectors of the
        coordinate system theA1 to this coordinate system.
        """

    def SetXAxis(self, theA1: gp_Ax2d) -> None:
        """
        Changes the XAxis and YAxis ("Location" point and "Direction")
        of <me>.
        The "YDirection" is recomputed in the same sense as before.
        """

    def SetYAxis(self, theA1: gp_Ax2d) -> None:
        """
        Changes the XAxis and YAxis ("Location" point and "Direction") of <me>.
        The "XDirection" is recomputed in the same sense as before.
        """

    def SetLocation(self, theP: gp_Pnt2d) -> None:
        """Changes the "Location" point (origin) of <me>."""

    def SetXDirection(self, theVx: gp_Dir2d) -> None:
        """
        Assigns theVx to the "X Direction" of
        this coordinate system. The other unit vector of this
        coordinate system is recomputed, normal to theVx ,
        without modifying the orientation (right-handed or
        left-handed) of this coordinate system.
        """

    def SetYDirection(self, theVy: gp_Dir2d) -> None:
        """
        Assigns theVy to the "Y Direction" of
        this coordinate system. The other unit vector of this
        coordinate system is recomputed, normal to theVy,
        without modifying the orientation (right-handed or
        left-handed) of this coordinate system.
        """

    def XAxis(self) -> gp_Ax2d:
        """
        Returns an axis, for which
        -   the origin is that of this coordinate system, and
        -   the unit vector is either the "X Direction" of this coordinate system.
        Note: the result is the "X Axis" of this coordinate system.
        """

    def YAxis(self) -> gp_Ax2d:
        """
        Returns an axis, for which
        -   the origin is that of this coordinate system, and
        - the unit vector is either the "Y Direction" of this coordinate system.
        Note: the result is the "Y Axis" of this coordinate system.
        """

    def Location(self) -> gp_Pnt2d:
        """Returns the "Location" point (origin) of <me>."""

    def XDirection(self) -> gp_Dir2d:
        """Returns the "XDirection" of <me>."""

    def YDirection(self) -> gp_Dir2d:
        """Returns the "YDirection" of <me>."""

    @overload
    def Mirror(self, theP: gp_Pnt2d) -> None: ...

    @overload
    def Mirror(self, theA: gp_Ax2d) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt2d) -> gp_Ax22d:
        """
        Performs the symmetrical transformation of an axis
        placement with respect to the point theP which is the
        center of the symmetry.
        Warnings :
        The main direction of the axis placement is not changed.
        The "XDirection" and the "YDirection" are reversed.
        So the axis placement stay right handed.
        """

    @overload
    def Mirrored(self, theA: gp_Ax2d) -> gp_Ax22d:
        """
        Performs the symmetrical transformation of an axis
        placement with respect to an axis placement which
        is the axis of the symmetry.
        The transformation is performed on the "Location"
        point, on the "XDirection" and "YDirection".
        The resulting main "Direction" is the cross product between
        the "XDirection" and the "YDirection" after transformation.
        """

    def Rotate(self, theP: gp_Pnt2d, theAng: float) -> None: ...

    def Rotated(self, theP: gp_Pnt2d, theAng: float) -> gp_Ax22d:
        """
        Rotates an axis placement. <theA1> is the axis of the
        rotation. theAng is the angular value of the rotation
        in radians.
        """

    def Scale(self, theP: gp_Pnt2d, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt2d, theS: float) -> gp_Ax22d:
        """
        Applies a scaling transformation on the axis placement.
        The "Location" point of the axisplacement is modified.
        Warnings:
        If the scale <theS> is negative:
        . the main direction of the axis placement is not changed.
        . The "XDirection" and the "YDirection" are reversed.
        So the axis placement stay right handed.
        """

    def Transform(self, theT: gp_Trsf2d) -> None: ...

    def Transformed(self, theT: gp_Trsf2d) -> gp_Ax22d:
        """
        Transforms an axis placement with a Trsf.
        The "Location" point, the "XDirection" and the
        "YDirection" are transformed with theT. The resulting
        main "Direction" of <me> is the cross product between
        the "XDirection" and the "YDirection" after transformation.
        """

    @overload
    def Translate(self, theV: gp_Vec2d) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec2d) -> gp_Ax22d:
        """
        Translates an axis plaxement in the direction of the vector
        <theV>. The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> gp_Ax22d:
        """
        Translates an axis placement from the point <theP1> to the
        point <theP2>.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class gp_Circ:
    """
    Describes a circle in 3D space.
    A circle is defined by its radius and positioned in space
    with a coordinate system (a gp_Ax2 object) as follows:
    -   the origin of the coordinate system is the center of the circle, and
    -   the origin, "X Direction" and "Y Direction" of the
    coordinate system define the plane of the circle.
    This positioning coordinate system is the "local
    coordinate system" of the circle. Its "main Direction"
    gives the normal vector to the plane of the circle. The
    "main Axis" of the coordinate system is referred to as
    the "Axis" of the circle.
    Note: when a gp_Circ circle is converted into a
    Geom_Circle circle, some implicit properties of the
    circle are used explicitly:
    -   the "main Direction" of the local coordinate system
    gives an implicit orientation to the circle (and defines
    its trigonometric sense),
    -   this orientation corresponds to the direction in
    which parameter values increase,
    -   the starting point for parameterization is that of the
    "X Axis" of the local coordinate system (i.e. the "X Axis" of the circle).
    See Also
    gce_MakeCirc which provides functions for more complex circle constructions
    Geom_Circle which provides additional functions for
    constructing circles and works, in particular, with the
    parametric equations of circles
    """

    @overload
    def __init__(self) -> None:
        """Creates an indefinite circle."""

    @overload
    def __init__(self, theA2: gp_Ax2, theRadius: float) -> None:
        """
        A2 locates the circle and gives its orientation in 3D space.
        Warnings:
        It is not forbidden to create a circle with theRadius = 0.0
        Raises ConstructionError if theRadius < 0.0
        """

    @overload
    def __init__(self, theOther: gp_Circ) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeCirc) -> None: ...

    def SetAxis(self, theA1: gp_Ax1) -> None:
        """
        Changes the main axis of the circle. It is the axis
        perpendicular to the plane of the circle.
        Raises ConstructionError if the direction of theA1
        is parallel to the "XAxis" of the circle.
        """

    def SetLocation(self, theP: gp_Pnt) -> None:
        """Changes the "Location" point (center) of the circle."""

    def SetPosition(self, theA2: gp_Ax2) -> None:
        """Changes the position of the circle."""

    def SetRadius(self, theRadius: float) -> None:
        """
        Modifies the radius of this circle.
        Warning: This class does not prevent the creation of a circle where theRadius is null.
        Exceptions
        Standard_ConstructionError if theRadius is negative.
        """

    def Area(self) -> float:
        """Computes the area of the circle."""

    def Axis(self) -> gp_Ax1:
        """
        Returns the main axis of the circle.
        It is the axis perpendicular to the plane of the circle,
        passing through the "Location" point (center) of the circle.
        """

    def Length(self) -> float:
        """Computes the circumference of the circle."""

    def Location(self) -> gp_Pnt:
        """
        Returns the center of the circle. It is the
        "Location" point of the local coordinate system
        of the circle
        """

    def Position(self) -> gp_Ax2:
        """
        Returns the position of the circle.
        It is the local coordinate system of the circle.
        """

    def Radius(self) -> float:
        """Returns the radius of this circle."""

    def XAxis(self) -> gp_Ax1:
        """
        Returns the "XAxis" of the circle.
        This axis is perpendicular to the axis of the conic.
        This axis and the "Yaxis" define the plane of the conic.
        """

    def YAxis(self) -> gp_Ax1:
        """
        Returns the "YAxis" of the circle.
        This axis and the "Xaxis" define the plane of the conic.
        The "YAxis" is perpendicular to the "Xaxis".
        """

    def Distance(self, theP: gp_Pnt) -> float:
        """
        Computes the minimum of distance between the point theP and
        any point on the circumference of the circle.
        """

    def SquareDistance(self, theP: gp_Pnt) -> float:
        """Computes the square distance between <me> and the point theP."""

    def Contains(self, theP: gp_Pnt, theLinearTolerance: float) -> bool:
        """
        Returns True if the point theP is on the circumference.
        The distance between <me> and <theP> must be lower or
        equal to theLinearTolerance.
        """

    @overload
    def Mirror(self, theP: gp_Pnt) -> None: ...

    @overload
    def Mirror(self, theA1: gp_Ax1) -> None: ...

    @overload
    def Mirror(self, theA2: gp_Ax2) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt) -> gp_Circ:
        """
        Performs the symmetrical transformation of a circle
        with respect to the point theP which is the center of the
        symmetry.
        """

    @overload
    def Mirrored(self, theA1: gp_Ax1) -> gp_Circ:
        """
        Performs the symmetrical transformation of a circle with
        respect to an axis placement which is the axis of the
        symmetry.
        """

    @overload
    def Mirrored(self, theA2: gp_Ax2) -> gp_Circ:
        """
        Performs the symmetrical transformation of a circle with respect
        to a plane. The axis placement theA2 locates the plane of the
        of the symmetry : (Location, XDirection, YDirection).
        """

    def Rotate(self, theA1: gp_Ax1, theAng: float) -> None: ...

    def Rotated(self, theA1: gp_Ax1, theAng: float) -> gp_Circ:
        """
        Rotates a circle. theA1 is the axis of the rotation.
        theAng is the angular value of the rotation in radians.
        """

    def Scale(self, theP: gp_Pnt, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt, theS: float) -> gp_Circ:
        """
        Scales a circle. theS is the scaling value.
        Warnings :
        If theS is negative the radius stay positive but
        the "XAxis" and the "YAxis" are reversed as for
        an ellipse.
        """

    def Transform(self, theT: gp_Trsf) -> None: ...

    def Transformed(self, theT: gp_Trsf) -> gp_Circ:
        """Transforms a circle with the transformation theT from class Trsf."""

    @overload
    def Translate(self, theV: gp_Vec) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec) -> gp_Circ:
        """
        Translates a circle in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt, theP2: gp_Pnt) -> gp_Circ:
        """Translates a circle from the point theP1 to the point theP2."""

class gp_Circ2d:
    """
    Describes a circle in the plane (2D space).
    A circle is defined by its radius and positioned in the
    plane with a coordinate system (a gp_Ax22d object) as follows:
    -   the origin of the coordinate system is the center of the circle, and
    -   the orientation (direct or indirect) of the coordinate
    system gives an implicit orientation to the circle (and
    defines its trigonometric sense).
    This positioning coordinate system is the "local
    coordinate system" of the circle.
    Note: when a gp_Circ2d circle is converted into a
    Geom2d_Circle circle, some implicit properties of the
    circle are used explicitly:
    -   the implicit orientation corresponds to the direction in
    which parameter values increase,
    -   the starting point for parameterization is that of the "X
    Axis" of the local coordinate system (i.e. the "X Axis" of the circle).
    See Also
    GccAna and Geom2dGcc packages which provide
    functions for constructing circles defined by geometric constraints
    gce_MakeCirc2d which provides functions for more
    complex circle constructions
    Geom2d_Circle which provides additional functions for
    constructing circles and works, with the parametric
    equations of circles in particular gp_Ax22d
    """

    @overload
    def __init__(self) -> None:
        """creates an indefinite circle."""

    @overload
    def __init__(self, theXAxis: gp_Ax2d, theRadius: float, theIsSense: bool = True) -> None:
        """
        The location point of theXAxis is the center of the circle.
        Warnings:
        It is not forbidden to create a circle with theRadius = 0.0
        Raises ConstructionError if theRadius < 0.0.
        """

    @overload
    def __init__(self, theAxis: gp_Ax22d, theRadius: float) -> None:
        """
        theAxis defines the Xaxis and Yaxis of the circle which defines
        the origin and the sense of parametrization.
        The location point of theAxis is the center of the circle.
        Warnings:
        It is not forbidden to create a circle with theRadius = 0.0
        Raises ConstructionError if theRadius < 0.0.
        """

    @overload
    def __init__(self, theOther: gp_Circ2d) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeCirc2d) -> None: ...

    def SetLocation(self, theP: gp_Pnt2d) -> None:
        """Changes the location point (center) of the circle."""

    def SetXAxis(self, theA: gp_Ax2d) -> None:
        """Changes the X axis of the circle."""

    def SetAxis(self, theA: gp_Ax22d) -> None:
        """Changes the X axis of the circle."""

    def SetYAxis(self, theA: gp_Ax2d) -> None:
        """Changes the Y axis of the circle."""

    def SetRadius(self, theRadius: float) -> None:
        """
        Modifies the radius of this circle.
        This class does not prevent the creation of a circle where
        theRadius is null.
        Exceptions
        Standard_ConstructionError if theRadius is negative.
        """

    def Area(self) -> float:
        """Computes the area of the circle."""

    def Coefficients(self) -> tuple[float, float, float, float, float, float]:
        """
        Returns the normalized coefficients from the implicit equation
        of the circle :
        theA * (X**2) + theB * (Y**2) + 2*theC*(X*Y) + 2*theD*X + 2*theE*Y + theF = 0.0
        """

    def Contains(self, theP: gp_Pnt2d, theLinearTolerance: float) -> bool:
        """
        Does <me> contain theP ?
        Returns True if the distance between theP and any point on
        the circumference of the circle is lower of equal to
        <theLinearTolerance>.
        """

    def Distance(self, theP: gp_Pnt2d) -> float:
        """
        Computes the minimum of distance between the point theP and any
        point on the circumference of the circle.
        """

    def SquareDistance(self, theP: gp_Pnt2d) -> float:
        """Computes the square distance between <me> and the point theP."""

    def Length(self) -> float:
        """computes the circumference of the circle."""

    def Location(self) -> gp_Pnt2d:
        """Returns the location point (center) of the circle."""

    def Radius(self) -> float:
        """Returns the radius value of the circle."""

    def Axis(self) -> gp_Ax22d:
        """returns the position of the circle."""

    def Position(self) -> gp_Ax22d:
        """returns the position of the circle. Idem Axis(me)."""

    def XAxis(self) -> gp_Ax2d:
        """returns the X axis of the circle."""

    def YAxis(self) -> gp_Ax2d:
        """
        Returns the Y axis of the circle.
        Reverses the direction of the circle.
        """

    def Reverse(self) -> None:
        """
        Reverses the orientation of the local coordinate system
        of this circle (the "Y Direction" is reversed) and therefore
        changes the implicit orientation of this circle.
        Reverse assigns the result to this circle,
        """

    def Reversed(self) -> gp_Circ2d:
        """
        Reverses the orientation of the local coordinate system
        of this circle (the "Y Direction" is reversed) and therefore
        changes the implicit orientation of this circle.
        Reversed creates a new circle.
        """

    def IsDirect(self) -> bool:
        """
        Returns true if the local coordinate system is direct
        and false in the other case.
        """

    @overload
    def Mirror(self, theP: gp_Pnt2d) -> None: ...

    @overload
    def Mirror(self, theA: gp_Ax2d) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt2d) -> gp_Circ2d:
        """
        Performs the symmetrical transformation of a circle with respect
        to the point theP which is the center of the symmetry
        """

    @overload
    def Mirrored(self, theA: gp_Ax2d) -> gp_Circ2d:
        """
        Performs the symmetrical transformation of a circle with respect
        to an axis placement which is the axis of the symmetry.
        """

    def Rotate(self, theP: gp_Pnt2d, theAng: float) -> None: ...

    def Rotated(self, theP: gp_Pnt2d, theAng: float) -> gp_Circ2d:
        """
        Rotates a circle. theP is the center of the rotation.
        Ang is the angular value of the rotation in radians.
        """

    def Scale(self, theP: gp_Pnt2d, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt2d, theS: float) -> gp_Circ2d:
        """
        Scales a circle. theS is the scaling value.
        Warnings:
        If theS is negative the radius stay positive but
        the "XAxis" and the "YAxis" are reversed as for
        an ellipse.
        """

    def Transform(self, theT: gp_Trsf2d) -> None: ...

    def Transformed(self, theT: gp_Trsf2d) -> gp_Circ2d:
        """Transforms a circle with the transformation theT from class Trsf2d."""

    @overload
    def Translate(self, theV: gp_Vec2d) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec2d) -> gp_Circ2d:
        """
        Translates a circle in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> gp_Circ2d:
        """Translates a circle from the point theP1 to the point theP2."""

class gp_Cone:
    """
    Defines an infinite conical surface.
    A cone is defined by its half-angle (can be negative) at the apex and
    positioned in space with a coordinate system (a gp_Ax3
    object) and a "reference radius" where:
    -   the "main Axis" of the coordinate system is the axis of revolution of the cone,
    -   the plane defined by the origin, the "X Direction" and
    the "Y Direction" of the coordinate system is the
    reference plane of the cone; the intersection of the
    cone with this reference plane is a circle of radius
    equal to the reference radius,
    if the half-angle is positive, the apex of the cone is on
    the negative side of the "main Axis" of the coordinate
    system. If the half-angle is negative, the apex is on the positive side.
    This coordinate system is the "local coordinate system" of the cone.
    Note: when a gp_Cone cone is converted into a
    Geom_ConicalSurface cone, some implicit properties of
    its local coordinate system are used explicitly:
    -   its origin, "X Direction", "Y Direction" and "main
    Direction" are used directly to define the parametric
    directions on the cone and the origin of the parameters,
    -   its implicit orientation (right-handed or left-handed)
    gives the orientation (direct or indirect) of the
    Geom_ConicalSurface cone.
    See Also
    gce_MakeCone which provides functions for more
    complex cone constructions
    Geom_ConicalSurface which provides additional
    functions for constructing cones and works, in particular,
    with the parametric equations of cones gp_Ax3
    """

    @overload
    def __init__(self) -> None:
        """Creates an indefinite Cone."""

    @overload
    def __init__(self, theA3: gp_Ax3, theAng: float, theRadius: float) -> None:
        """
        Creates an infinite conical surface. theA3 locates the cone
        in the space and defines the reference plane of the surface.
        Ang is the conical surface semi-angle. Its absolute value is in range
        ]0, PI/2[.
        theRadius is the radius of the circle in the reference plane of
        the cone.
        theRaises ConstructionError
        * if theRadius is lower than 0.0
        * std::abs(theAng) < Resolution from gp or std::abs(theAng) >= (PI/2) - Resolution.
        """

    @overload
    def __init__(self, theOther: gp_Cone) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeCone) -> None: ...

    def SetAxis(self, theA1: gp_Ax1) -> None:
        """
        Changes the symmetry axis of the cone. Raises ConstructionError
        the direction of theA1 is parallel to the "XDirection"
        of the coordinate system of the cone.
        """

    def SetLocation(self, theLoc: gp_Pnt) -> None:
        """Changes the location of the cone."""

    def SetPosition(self, theA3: gp_Ax3) -> None:
        """
        Changes the local coordinate system of the cone.
        This coordinate system defines the reference plane of the cone.
        """

    def SetRadius(self, theR: float) -> None:
        """
        Changes the radius of the cone in the reference plane of
        the cone.
        Raised if theR < 0.0
        """

    def SetSemiAngle(self, theAng: float) -> None:
        """
        Changes the semi-angle of the cone.
        Semi-angle can be negative. Its absolute value
        std::abs(theAng) is in range ]0,PI/2[.
        Raises ConstructionError if std::abs(theAng) < Resolution from gp or std::abs(theAng) >= PI/2
        - Resolution
        """

    def Apex(self) -> gp_Pnt:
        """
        Computes the cone's top. The Apex of the cone is on the
        negative side of the symmetry axis of the cone.
        """

    def UReverse(self) -> None:
        """
        Reverses the U parametrization of the cone
        reversing the YAxis.
        """

    def VReverse(self) -> None:
        """Reverses the V parametrization of the cone reversing the ZAxis."""

    def Direct(self) -> bool:
        """
        Returns true if the local coordinate system of this cone is right-handed.
        """

    def Axis(self) -> gp_Ax1:
        """returns the symmetry axis of the cone."""

    def Coefficients(self) -> tuple[float, float, float, float, float, float, float, float, float, float]:
        """
        Computes the coefficients of the implicit equation of the quadric
        in the absolute cartesian coordinates system :
        theA1.X**2 + theA2.Y**2 + theA3.Z**2 + 2.(theB1.X.Y + theB2.X.Z + theB3.Y.Z) +
        2.(theC1.X + theC2.Y + theC3.Z) + theD = 0.0
        """

    def Location(self) -> gp_Pnt:
        """returns the "Location" point of the cone."""

    def Position(self) -> gp_Ax3:
        """Returns the local coordinates system of the cone."""

    def RefRadius(self) -> float:
        """Returns the radius of the cone in the reference plane."""

    def SemiAngle(self) -> float:
        """
        Returns the half-angle at the apex of this cone.
        Attention! Semi-angle can be negative.
        """

    def XAxis(self) -> gp_Ax1:
        """Returns the XAxis of the reference plane."""

    def YAxis(self) -> gp_Ax1:
        """Returns the YAxis of the reference plane."""

    @overload
    def Mirror(self, theP: gp_Pnt) -> None: ...

    @overload
    def Mirror(self, theA1: gp_Ax1) -> None: ...

    @overload
    def Mirror(self, theA2: gp_Ax2) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt) -> gp_Cone:
        """
        Performs the symmetrical transformation of a cone
        with respect to the point theP which is the center of the
        symmetry.
        """

    @overload
    def Mirrored(self, theA1: gp_Ax1) -> gp_Cone:
        """
        Performs the symmetrical transformation of a cone with
        respect to an axis placement which is the axis of the
        symmetry.
        """

    @overload
    def Mirrored(self, theA2: gp_Ax2) -> gp_Cone:
        """
        Performs the symmetrical transformation of a cone with respect
        to a plane. The axis placement theA2 locates the plane of the
        of the symmetry : (Location, XDirection, YDirection).
        """

    def Rotate(self, theA1: gp_Ax1, theAng: float) -> None: ...

    def Rotated(self, theA1: gp_Ax1, theAng: float) -> gp_Cone:
        """
        Rotates a cone. theA1 is the axis of the rotation.
        Ang is the angular value of the rotation in radians.
        """

    def Scale(self, theP: gp_Pnt, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt, theS: float) -> gp_Cone:
        """
        Scales a cone. theS is the scaling value.
        The absolute value of theS is used to scale the cone
        """

    def Transform(self, theT: gp_Trsf) -> None: ...

    def Transformed(self, theT: gp_Trsf) -> gp_Cone:
        """Transforms a cone with the transformation theT from class Trsf."""

    @overload
    def Translate(self, theV: gp_Vec) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec) -> gp_Cone:
        """
        Translates a cone in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt, theP2: gp_Pnt) -> gp_Cone:
        """Translates a cone from the point P1 to the point P2."""

class gp_Cylinder:
    """
    Describes an infinite cylindrical surface.
    A cylinder is defined by its radius and positioned in space
    with a coordinate system (a gp_Ax3 object), the "main
    Axis" of which is the axis of the cylinder. This coordinate
    system is the "local coordinate system" of the cylinder.
    Note: when a gp_Cylinder cylinder is converted into a
    Geom_CylindricalSurface cylinder, some implicit
    properties of its local coordinate system are used explicitly:
    -   its origin, "X Direction", "Y Direction" and "main
    Direction" are used directly to define the parametric
    directions on the cylinder and the origin of the parameters,
    -   its implicit orientation (right-handed or left-handed)
    gives an orientation (direct or indirect) to the
    Geom_CylindricalSurface cylinder.
    See Also
    gce_MakeCylinder which provides functions for more
    complex cylinder constructions
    Geom_CylindricalSurface which provides additional
    functions for constructing cylinders and works, in
    particular, with the parametric equations of cylinders gp_Ax3
    """

    @overload
    def __init__(self) -> None:
        """Creates a indefinite cylinder."""

    @overload
    def __init__(self, theA3: gp_Ax3, theRadius: float) -> None:
        """
        Creates a cylinder of radius Radius, whose axis is the "main
        Axis" of theA3. theA3 is the local coordinate system of the cylinder.
        Raises ConstructionErrord if theRadius < 0.0
        """

    @overload
    def __init__(self, theOther: gp_Cylinder) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeCylinder) -> None: ...

    def SetAxis(self, theA1: gp_Ax1) -> None:
        """
        Changes the symmetry axis of the cylinder. Raises ConstructionError if the direction of theA1
        is parallel to the "XDirection" of the coordinate system of the cylinder.
        """

    def SetLocation(self, theLoc: gp_Pnt) -> None:
        """Changes the location of the surface."""

    def SetPosition(self, theA3: gp_Ax3) -> None:
        """Change the local coordinate system of the surface."""

    def SetRadius(self, theR: float) -> None:
        """
        Modifies the radius of this cylinder.
        Exceptions
        Standard_ConstructionError if theR is negative.
        """

    def UReverse(self) -> None:
        """
        Reverses the U parametrization of the cylinder
        reversing the YAxis.
        """

    def VReverse(self) -> None:
        """
        Reverses the V parametrization of the plane
        reversing the Axis.
        """

    def Direct(self) -> bool:
        """
        Returns true if the local coordinate system of this cylinder is right-handed.
        """

    def Axis(self) -> gp_Ax1:
        """Returns the symmetry axis of the cylinder."""

    def Coefficients(self) -> tuple[float, float, float, float, float, float, float, float, float, float]:
        """
        Computes the coefficients of the implicit equation of the quadric
        in the absolute cartesian coordinate system :
        theA1.X**2 + theA2.Y**2 + theA3.Z**2 + 2.(theB1.X.Y + theB2.X.Z + theB3.Y.Z) +
        2.(theC1.X + theC2.Y + theC3.Z) + theD = 0.0
        """

    def Location(self) -> gp_Pnt:
        """Returns the "Location" point of the cylinder."""

    def Position(self) -> gp_Ax3:
        """Returns the local coordinate system of the cylinder."""

    def Radius(self) -> float:
        """Returns the radius of the cylinder."""

    def XAxis(self) -> gp_Ax1:
        """Returns the axis X of the cylinder."""

    def YAxis(self) -> gp_Ax1:
        """Returns the axis Y of the cylinder."""

    @overload
    def Mirror(self, theP: gp_Pnt) -> None: ...

    @overload
    def Mirror(self, theA1: gp_Ax1) -> None: ...

    @overload
    def Mirror(self, theA2: gp_Ax2) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt) -> gp_Cylinder:
        """
        Performs the symmetrical transformation of a cylinder
        with respect to the point theP which is the center of the
        symmetry.
        """

    @overload
    def Mirrored(self, theA1: gp_Ax1) -> gp_Cylinder:
        """
        Performs the symmetrical transformation of a cylinder with
        respect to an axis placement which is the axis of the
        symmetry.
        """

    @overload
    def Mirrored(self, theA2: gp_Ax2) -> gp_Cylinder:
        """
        Performs the symmetrical transformation of a cylinder with respect
        to a plane. The axis placement theA2 locates the plane of the
        of the symmetry : (Location, XDirection, YDirection).
        """

    def Rotate(self, theA1: gp_Ax1, theAng: float) -> None: ...

    def Rotated(self, theA1: gp_Ax1, theAng: float) -> gp_Cylinder:
        """
        Rotates a cylinder. theA1 is the axis of the rotation.
        theAng is the angular value of the rotation in radians.
        """

    def Scale(self, theP: gp_Pnt, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt, theS: float) -> gp_Cylinder:
        """
        Scales a cylinder. theS is the scaling value.
        The absolute value of theS is used to scale the cylinder
        """

    def Transform(self, theT: gp_Trsf) -> None: ...

    def Transformed(self, theT: gp_Trsf) -> gp_Cylinder:
        """Transforms a cylinder with the transformation theT from class Trsf."""

    @overload
    def Translate(self, theV: gp_Vec) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec) -> gp_Cylinder:
        """
        Translates a cylinder in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt, theP2: gp_Pnt) -> gp_Cylinder:
        """Translates a cylinder from the point theP1 to the point theP2."""

class gp_Elips:
    """
    Describes an ellipse in 3D space.
    An ellipse is defined by its major and minor radii and
    positioned in space with a coordinate system (a gp_Ax2 object) as follows:
    -   the origin of the coordinate system is the center of the ellipse,
    -   its "X Direction" defines the major axis of the ellipse, and
    - its "Y Direction" defines the minor axis of the ellipse.
    Together, the origin, "X Direction" and "Y Direction" of
    this coordinate system define the plane of the ellipse.
    This coordinate system is the "local coordinate system"
    of the ellipse. In this coordinate system, the equation of
    the ellipse is:
    @code
    X*X / (MajorRadius**2) + Y*Y / (MinorRadius**2) = 1.0
    @endcode
    The "main Direction" of the local coordinate system gives
    the normal vector to the plane of the ellipse. This vector
    gives an implicit orientation to the ellipse (definition of the
    trigonometric sense). We refer to the "main Axis" of the
    local coordinate system as the "Axis" of the ellipse.
    See Also
    gce_MakeElips which provides functions for more
    complex ellipse constructions
    Geom_Ellipse which provides additional functions for
    constructing ellipses and works, in particular, with the
    parametric equations of ellipses
    """

    @overload
    def __init__(self) -> None:
        """Creates an indefinite ellipse."""

    @overload
    def __init__(self, theA2: gp_Ax2, theMajorRadius: float, theMinorRadius: float) -> None:
        """
        The major radius of the ellipse is on the "XAxis" and the
        minor radius is on the "YAxis" of the ellipse. The "XAxis"
        is defined with the "XDirection" of theA2 and the "YAxis" is
        defined with the "YDirection" of theA2.
        Warnings :
        It is not forbidden to create an ellipse with theMajorRadius =
        theMinorRadius.
        Raises ConstructionError if theMajorRadius < theMinorRadius or theMinorRadius < 0.
        """

    @overload
    def __init__(self, theOther: gp_Elips) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeElips) -> None: ...

    def SetAxis(self, theA1: gp_Ax1) -> None:
        """
        Changes the axis normal to the plane of the ellipse.
        It modifies the definition of this plane.
        The "XAxis" and the "YAxis" are recomputed.
        The local coordinate system is redefined so that:
        -   its origin and "main Direction" become those of the
        axis theA1 (the "X Direction" and "Y Direction" are then
        recomputed in the same way as for any gp_Ax2), or
        Raises ConstructionError if the direction of theA1
        is parallel to the direction of the "XAxis" of the ellipse.
        """

    def SetLocation(self, theP: gp_Pnt) -> None:
        """
        Modifies this ellipse, by redefining its local coordinate
        so that its origin becomes theP.
        """

    def SetMajorRadius(self, theMajorRadius: float) -> None:
        """
        The major radius of the ellipse is on the "XAxis" (major axis)
        of the ellipse.
        Raises ConstructionError if theMajorRadius < MinorRadius.
        """

    def SetMinorRadius(self, theMinorRadius: float) -> None:
        """
        The minor radius of the ellipse is on the "YAxis" (minor axis)
        of the ellipse.
        Raises ConstructionError if theMinorRadius > MajorRadius or MinorRadius < 0.
        """

    def SetPosition(self, theA2: gp_Ax2) -> None:
        """
        Modifies this ellipse, by redefining its local coordinate
        so that it becomes theA2.
        """

    def Area(self) -> float:
        """Computes the area of the Ellipse."""

    def Axis(self) -> gp_Ax1:
        """Computes the axis normal to the plane of the ellipse."""

    def Directrix1(self) -> gp_Ax1:
        """
        Computes the first or second directrix of this ellipse.
        These are the lines, in the plane of the ellipse, normal to
        the major axis, at a distance equal to
        MajorRadius/e from the center of the ellipse, where
        e is the eccentricity of the ellipse.
        The first directrix (Directrix1) is on the positive side of
        the major axis. The second directrix (Directrix2) is on
        the negative side.
        The directrix is returned as an axis (gp_Ax1 object), the
        origin of which is situated on the "X Axis" of the local
        coordinate system of this ellipse.
        Exceptions
        Standard_ConstructionError if the eccentricity is null
        (the ellipse has degenerated into a circle).
        """

    def Directrix2(self) -> gp_Ax1:
        """
        This line is obtained by the symmetrical transformation
        of "Directrix1" with respect to the "YAxis" of the ellipse.
        Exceptions
        Standard_ConstructionError if the eccentricity is null
        (the ellipse has degenerated into a circle).
        """

    def Eccentricity(self) -> float:
        """
        Returns the eccentricity of the ellipse between 0.0 and 1.0
        If f is the distance between the center of the ellipse and
        the Focus1 then the eccentricity e = f / MajorRadius.
        Raises ConstructionError if MajorRadius = 0.0
        """

    def Focal(self) -> float:
        """
        Computes the focal distance. It is the distance between the
        two focus focus1 and focus2 of the ellipse.
        """

    def Focus1(self) -> gp_Pnt:
        """
        Returns the first focus of the ellipse. This focus is on the
        positive side of the "XAxis" of the ellipse.
        """

    def Focus2(self) -> gp_Pnt:
        """
        Returns the second focus of the ellipse. This focus is on the
        negative side of the "XAxis" of the ellipse.
        """

    def Location(self) -> gp_Pnt:
        """
        Returns the center of the ellipse. It is the "Location"
        point of the coordinate system of the ellipse.
        """

    def MajorRadius(self) -> float:
        """Returns the major radius of the ellipse."""

    def MinorRadius(self) -> float:
        """Returns the minor radius of the ellipse."""

    def Parameter(self) -> float:
        """
        Returns p = (1 - e * e) * MajorRadius where e is the eccentricity
        of the ellipse.
        Returns 0 if MajorRadius = 0
        """

    def Position(self) -> gp_Ax2:
        """Returns the coordinate system of the ellipse."""

    def XAxis(self) -> gp_Ax1:
        """
        Returns the "XAxis" of the ellipse whose origin
        is the center of this ellipse. It is the major axis of the
        ellipse.
        """

    def YAxis(self) -> gp_Ax1:
        """
        Returns the "YAxis" of the ellipse whose unit vector is the "X Direction" or the "Y Direction"
        of the local coordinate system of this ellipse.
        This is the minor axis of the ellipse.
        """

    @overload
    def Mirror(self, theP: gp_Pnt) -> None: ...

    @overload
    def Mirror(self, theA1: gp_Ax1) -> None: ...

    @overload
    def Mirror(self, theA2: gp_Ax2) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt) -> gp_Elips:
        """
        Performs the symmetrical transformation of an ellipse with
        respect to the point theP which is the center of the symmetry.
        """

    @overload
    def Mirrored(self, theA1: gp_Ax1) -> gp_Elips:
        """
        Performs the symmetrical transformation of an ellipse with
        respect to an axis placement which is the axis of the symmetry.
        """

    @overload
    def Mirrored(self, theA2: gp_Ax2) -> gp_Elips:
        """
        Performs the symmetrical transformation of an ellipse with
        respect to a plane. The axis placement theA2 locates the plane
        of the symmetry (Location, XDirection, YDirection).
        """

    def Rotate(self, theA1: gp_Ax1, theAng: float) -> None: ...

    def Rotated(self, theA1: gp_Ax1, theAng: float) -> gp_Elips:
        """
        Rotates an ellipse. theA1 is the axis of the rotation.
        theAng is the angular value of the rotation in radians.
        """

    def Scale(self, theP: gp_Pnt, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt, theS: float) -> gp_Elips:
        """Scales an ellipse. theS is the scaling value."""

    def Transform(self, theT: gp_Trsf) -> None: ...

    def Transformed(self, theT: gp_Trsf) -> gp_Elips:
        """Transforms an ellipse with the transformation theT from class Trsf."""

    @overload
    def Translate(self, theV: gp_Vec) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec) -> gp_Elips:
        """
        Translates an ellipse in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt, theP2: gp_Pnt) -> gp_Elips:
        """Translates an ellipse from the point theP1 to the point theP2."""

class gp_Elips2d:
    """
    Describes an ellipse in the plane (2D space).
    An ellipse is defined by its major and minor radii and
    positioned in the plane with a coordinate system (a
    gp_Ax22d object) as follows:
    -   the origin of the coordinate system is the center of the ellipse,
    -   its "X Direction" defines the major axis of the ellipse, and
    -   its "Y Direction" defines the minor axis of the ellipse.
    This coordinate system is the "local coordinate system"
    of the ellipse. Its orientation (direct or indirect) gives an
    implicit orientation to the ellipse. In this coordinate
    system, the equation of the ellipse is:
    @code
    X*X / (MajorRadius**2) + Y*Y / (MinorRadius**2) = 1.0
    @endcode
    See Also
    gce_MakeElips2d which provides functions for more
    complex ellipse constructions
    Geom2d_Ellipse which provides additional functions for
    constructing ellipses and works, in particular, with the
    parametric equations of ellipses
    """

    @overload
    def __init__(self) -> None:
        """Creates an indefinite ellipse."""

    @overload
    def __init__(self, theMajorAxis: gp_Ax2d, theMajorRadius: float, theMinorRadius: float, theIsSense: bool = True) -> None:
        """
        Creates an ellipse with the major axis, the major and the
        minor radius. The location of the theMajorAxis is the center
        of the ellipse.
        The sense of parametrization is given by theIsSense.
        Warnings:
        It is possible to create an ellipse with
        theMajorRadius = theMinorRadius.
        Raises ConstructionError if theMajorRadius < theMinorRadius or theMinorRadius < 0.0
        """

    @overload
    def __init__(self, theA: gp_Ax22d, theMajorRadius: float, theMinorRadius: float) -> None:
        """
        Creates an ellipse with radii MajorRadius and
        MinorRadius, positioned in the plane by coordinate system theA where:
        -   the origin of theA is the center of the ellipse,
        -   the "X Direction" of theA defines the major axis of
        the ellipse, that is, the major radius MajorRadius
        is measured along this axis, and
        -   the "Y Direction" of theA defines the minor axis of
        the ellipse, that is, the minor radius theMinorRadius
        is measured along this axis, and
        -   the orientation (direct or indirect sense) of theA
        gives the orientation of the ellipse.
        Warnings :
        It is possible to create an ellipse with
        theMajorRadius = theMinorRadius.
        Raises ConstructionError if theMajorRadius < theMinorRadius or theMinorRadius < 0.0
        """

    @overload
    def __init__(self, theOther: gp_Elips2d) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeElips2d) -> None: ...

    def SetLocation(self, theP: gp_Pnt2d) -> None:
        """
        Modifies this ellipse, by redefining its local coordinate system so that
        -   its origin becomes theP.
        """

    def SetMajorRadius(self, theMajorRadius: float) -> None:
        """
        Changes the value of the major radius.
        Raises ConstructionError if theMajorRadius < MinorRadius.
        """

    def SetMinorRadius(self, theMinorRadius: float) -> None:
        """
        Changes the value of the minor radius.
        Raises ConstructionError if MajorRadius < theMinorRadius or MinorRadius < 0.0
        """

    def SetAxis(self, theA: gp_Ax22d) -> None:
        """
        Modifies this ellipse, by redefining its local coordinate system so that
        it becomes theA.
        """

    def SetXAxis(self, theA: gp_Ax2d) -> None:
        """
        Modifies this ellipse, by redefining its local coordinate system so that
        its origin and its "X Direction" become those
        of the axis theA. The "Y Direction" is then
        recomputed. The orientation of the local coordinate
        system is not modified.
        """

    def SetYAxis(self, theA: gp_Ax2d) -> None:
        """
        Modifies this ellipse, by redefining its local coordinate system so that
        its origin and its "Y Direction" become those
        of the axis theA. The "X Direction" is then
        recomputed. The orientation of the local coordinate
        system is not modified.
        """

    def Area(self) -> float:
        """Computes the area of the ellipse."""

    def Coefficients(self) -> tuple[float, float, float, float, float, float]:
        """
        Returns the coefficients of the implicit equation of the ellipse.
        theA * (X**2) + theB * (Y**2) + 2*theC*(X*Y) + 2*theD*X + 2*theE*Y + theF = 0.
        """

    def Directrix1(self) -> gp_Ax2d:
        """
        This directrix is the line normal to the XAxis of the ellipse
        in the local plane (Z = 0) at a distance d = MajorRadius / e
        from the center of the ellipse, where e is the eccentricity of
        the ellipse.
        This line is parallel to the "YAxis". The intersection point
        between directrix1 and the "XAxis" is the location point of the
        directrix1. This point is on the positive side of the "XAxis".

        Raised if Eccentricity = 0.0. (The ellipse degenerates into a
        circle)
        """

    def Directrix2(self) -> gp_Ax2d:
        """
        This line is obtained by the symmetrical transformation
        of "Directrix1" with respect to the minor axis of the ellipse.

        Raised if Eccentricity = 0.0. (The ellipse degenerates into a
        circle).
        """

    def Eccentricity(self) -> float:
        """
        Returns the eccentricity of the ellipse between 0.0 and 1.0
        If f is the distance between the center of the ellipse and
        the Focus1 then the eccentricity e = f / MajorRadius.
        Returns 0 if MajorRadius = 0.
        """

    def Focal(self) -> float:
        """
        Returns the distance between the center of the ellipse
        and focus1 or focus2.
        """

    def Focus1(self) -> gp_Pnt2d:
        """
        Returns the first focus of the ellipse. This focus is on the
        positive side of the major axis of the ellipse.
        """

    def Focus2(self) -> gp_Pnt2d:
        """
        Returns the second focus of the ellipse. This focus is on the
        negative side of the major axis of the ellipse.
        """

    def Location(self) -> gp_Pnt2d:
        """Returns the center of the ellipse."""

    def MajorRadius(self) -> float:
        """Returns the major radius of the Ellipse."""

    def MinorRadius(self) -> float:
        """Returns the minor radius of the Ellipse."""

    def Parameter(self) -> float:
        """
        Returns p = (1 - e * e) * MajorRadius where e is the eccentricity
        of the ellipse.
        Returns 0 if MajorRadius = 0
        """

    def Axis(self) -> gp_Ax22d:
        """Returns the major axis of the ellipse."""

    def XAxis(self) -> gp_Ax2d:
        """Returns the major axis of the ellipse."""

    def YAxis(self) -> gp_Ax2d:
        """
        Returns the minor axis of the ellipse.
        Reverses the direction of the circle.
        """

    def Reverse(self) -> None: ...

    def Reversed(self) -> gp_Elips2d: ...

    def IsDirect(self) -> bool:
        """
        Returns true if the local coordinate system is direct
        and false in the other case.
        """

    @overload
    def Mirror(self, theP: gp_Pnt2d) -> None: ...

    @overload
    def Mirror(self, theA: gp_Ax2d) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt2d) -> gp_Elips2d:
        """
        Performs the symmetrical transformation of a ellipse with respect
        to the point theP which is the center of the symmetry
        """

    @overload
    def Mirrored(self, theA: gp_Ax2d) -> gp_Elips2d:
        """
        Performs the symmetrical transformation of a ellipse with respect
        to an axis placement which is the axis of the symmetry.
        """

    def Rotate(self, theP: gp_Pnt2d, theAng: float) -> None: ...

    def Rotated(self, theP: gp_Pnt2d, theAng: float) -> gp_Elips2d: ...

    def Scale(self, theP: gp_Pnt2d, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt2d, theS: float) -> gp_Elips2d:
        """Scales a ellipse. theS is the scaling value."""

    def Transform(self, theT: gp_Trsf2d) -> None: ...

    def Transformed(self, theT: gp_Trsf2d) -> gp_Elips2d:
        """Transforms an ellipse with the transformation theT from class Trsf2d."""

    @overload
    def Translate(self, theV: gp_Vec2d) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec2d) -> gp_Elips2d:
        """
        Translates a ellipse in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> gp_Elips2d:
        """Translates a ellipse from the point theP1 to the point theP2."""

class gp_GTrsf:
    """
    Defines a non-persistent transformation in 3D space.
    This transformation is a general transformation.
    It can be a gp_Trsf, an affinity, or you can define
    your own transformation giving the matrix of transformation.

    With a gp_GTrsf you can transform only a triplet of coordinates gp_XYZ.
    It is not possible to transform other geometric objects
    because these transformations can change the nature of non-elementary geometric objects.
    The transformation gp_GTrsf can be represented as follow:
    @code
    V1   V2   V3    T       XYZ        XYZ
    | a11  a12  a13   a14 |   | x |      | x'|
    | a21  a22  a23   a24 |   | y |      | y'|
    | a31  a32  a33   a34 |   | z |   =  | z'|
    |  0    0    0     1  |   | 1 |      | 1 |
    @endcode
    where {V1, V2, V3} define the vectorial part of the
    transformation and T defines the translation part of the transformation.
    Warning
    A gp_GTrsf transformation is only applicable to coordinates.
    Be careful if you apply such a transformation to all points of a geometric object,
    as this can change the nature of the object and thus render it incoherent!
    Typically, a circle is transformed into an ellipse by an affinity transformation.
    To avoid modifying the nature of an object, use a gp_Trsf transformation instead,
    as objects of this class respect the nature of geometric objects.
    """

    @overload
    def __init__(self) -> None:
        """Returns the Identity transformation."""

    @overload
    def __init__(self, theT: gp_Trsf) -> None:
        """
        Converts the gp_Trsf transformation theT into a
        general transformation, i.e. Returns a GTrsf with
        the same matrix of coefficients as the Trsf theT.
        """

    @overload
    def __init__(self, theM: gp_Mat, theV: gp_XYZ) -> None:
        """
        Creates a transformation based on the matrix theM and the
        vector theV where theM defines the vectorial part of
        the transformation, and V the translation part, or
        """

    @overload
    def __init__(self, theOther: gp_GTrsf) -> None: ...

    @overload
    def SetAffinity(self, theA1: gp_Ax1, theRatio: float) -> None:
        """
        Changes this transformation into an affinity of ratio theRatio
        with respect to the axis theA1.
        Note: an affinity is a point-by-point transformation that
        transforms any point P into a point P' such that if H is
        the orthogonal projection of P on the axis theA1 or the
        plane A2, the vectors HP and HP' satisfy:
        HP' = theRatio * HP.
        """

    @overload
    def SetAffinity(self, theA2: gp_Ax2, theRatio: float) -> None:
        """
        Changes this transformation into an affinity of ratio theRatio
        with respect to the plane defined by the origin, the "X Direction" and
        the "Y Direction" of coordinate system theA2.
        Note: an affinity is a point-by-point transformation that
        transforms any point P into a point P' such that if H is
        the orthogonal projection of P on the axis A1 or the
        plane theA2, the vectors HP and HP' satisfy:
        HP' = theRatio * HP.
        """

    def SetValue(self, theRow: int, theCol: int, theValue: float) -> None:
        """
        Replaces the coefficient (theRow, theCol) of the matrix representing
        this transformation by theValue. Raises OutOfRange
        if theRow < 1 or theRow > 3 or theCol < 1 or theCol > 4
        """

    def SetVectorialPart(self, theMatrix: gp_Mat) -> None:
        """Replaces the vectorial part of this transformation by theMatrix."""

    def SetTranslationPart(self, theCoord: gp_XYZ) -> None:
        """
        Replaces the translation part of
        this transformation by the coordinates of the number triple theCoord.
        """

    def SetTrsf(self, theT: gp_Trsf) -> None:
        """
        Assigns the vectorial and translation parts of theT to this transformation.
        """

    def IsNegative(self) -> bool:
        """
        Returns true if the determinant of the vectorial part of
        this transformation is negative.
        """

    def IsSingular(self) -> bool:
        """
        Returns true if this transformation is singular (and
        therefore, cannot be inverted).
        Note: The Gauss LU decomposition is used to invert the
        transformation matrix. Consequently, the transformation
        is considered as singular if the largest pivot found is less
        than or equal to gp::Resolution().
        Warning
        If this transformation is singular, it cannot be inverted.
        """

    def Form(self) -> gp_TrsfForm:
        """
        Returns the nature of the transformation. It can be an
        identity transformation, a rotation, a translation, a mirror
        transformation (relative to a point, an axis or a plane), a
        scaling transformation, a compound transformation or
        some other type of transformation.
        """

    def SetForm(self) -> None:
        """
        verify and set the shape of the GTrsf Other or CompoundTrsf
        Ex :
        @code
        myGTrsf.SetValue(row1,col1,val1);
        myGTrsf.SetValue(row2,col2,val2);
        ...
        myGTrsf.SetForm();
        @endcode
        """

    def TranslationPart(self) -> gp_XYZ:
        """Returns the translation part of the GTrsf."""

    def VectorialPart(self) -> gp_Mat:
        """
        Computes the vectorial part of the GTrsf. The returned Matrix
        is a 3*3 matrix.
        """

    def Value(self, theRow: int, theCol: int) -> float:
        """
        Returns the coefficients of the global matrix of transformation.
        Raises OutOfRange if theRow < 1 or theRow > 3 or theCol < 1 or theCol > 4
        """

    def __call__(self, theRow: int, theCol: int) -> float: ...

    def Invert(self) -> None: ...

    def Inverted(self) -> gp_GTrsf:
        """
        Computes the reverse transformation.
        Raises an exception if the matrix of the transformation
        is not inversible.
        """

    def Multiplied(self, theT: gp_GTrsf) -> gp_GTrsf:
        """
        Computes the transformation composed from theT and <me>.
        In a C++ implementation you can also write Tcomposed = <me> * theT.
        Example :
        @code
        gp_GTrsf T1, T2, Tcomp; ...............
        //composition :
        Tcomp = T2.Multiplied(T1);         // or   (Tcomp = T2 * T1)
        // transformation of a point
        gp_XYZ P(10.,3.,4.);
        gp_XYZ P1(P);
        Tcomp.Transforms(P1);               //using Tcomp
        gp_XYZ P2(P);
        T1.Transforms(P2);                  //using T1 then T2
        T2.Transforms(P2);                  // P1 = P2 !!!
        @endcode
        """

    def __mul__(self, theT: gp_GTrsf) -> gp_GTrsf: ...

    def Multiply(self, theT: gp_GTrsf) -> None:
        """
        Computes the transformation composed with <me> and theT.
        <me> = <me> * theT
        """

    def __imul__(self, theT: gp_GTrsf) -> gp_GTrsf: ...

    def PreMultiply(self, theT: gp_GTrsf) -> None:
        """
        Computes the product of the transformation theT and this
        transformation and assigns the result to this transformation.
        this = theT * this
        """

    def Power(self, theN: int) -> None: ...

    def Powered(self, theN: int) -> gp_GTrsf:
        """
        Computes:
        -   the product of this transformation multiplied by itself
        theN times, if theN is positive, or
        -   the product of the inverse of this transformation
        multiplied by itself |theN| times, if theN is negative.
        If theN equals zero, the result is equal to the Identity
        transformation.
        I.e.:  <me> * <me> * .......* <me>, theN time.
        if theN =0 <me> = Identity
        if theN < 0 <me> = <me>.Inverse() *...........* <me>.Inverse().

        Raises an exception if N < 0 and if the matrix of the
        transformation not inversible.
        """

    @overload
    def Transforms(self, theCoord: gp_XYZ) -> None: ...

    @overload
    def Transforms(self, theX: float, theY: float, theZ: float) -> tuple[float, float, float]:
        """Transforms a triplet XYZ with a GTrsf."""

    def Trsf(self) -> gp_Trsf: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class gp_GTrsf2d:
    """
    Defines a non persistent transformation in 2D space.
    This transformation is a general transformation.
    It can be a gp_Trsf2d, an affinity, or you can
    define your own transformation giving the corresponding matrix of transformation.

    With a gp_GTrsf2d you can transform only a doublet of coordinates gp_XY.
    It is not possible to transform other geometric objects
    because these transformations can change the nature of non-elementary geometric objects.
    A gp_GTrsf2d is represented with a 2 rows * 3 columns matrix:
    @code
    V1   V2   T        XY         XY
    | a11  a12  a14 |   | x |      | x'|
    | a21  a22  a24 |   | y |   =  | y'|
    |  0    0    1  |   | 1 |      | 1 |
    @endcode
    where {V1, V2} defines the vectorial part of the
    transformation and T defines the translation part of the transformation.
    Warning
    A gp_GTrsf2d transformation is only applicable on coordinates.
    Be careful if you apply such a transformation to all the points of a geometric object,
    as this can change the nature of the object and thus render it incoherent!
    Typically, a circle is transformed into an ellipse by an affinity transformation.
    To avoid modifying the nature of an object, use a gp_Trsf2d transformation instead,
    as objects of this class respect the nature of geometric objects.
    """

    @overload
    def __init__(self) -> None:
        """returns identity transformation."""

    @overload
    def __init__(self, theT: gp_Trsf2d) -> None:
        """
        Converts the gp_Trsf2d transformation theT into a
        general transformation.
        """

    @overload
    def __init__(self, theM: gp_Mat2d, theV: gp_XY) -> None:
        """
        Creates a transformation based on the matrix theM and the
        vector theV where theM defines the vectorial part of the
        transformation, and theV the translation part.
        """

    @overload
    def __init__(self, theOther: gp_GTrsf2d) -> None: ...

    def SetAffinity(self, theA: gp_Ax2d, theRatio: float) -> None:
        """
        Changes this transformation into an affinity of ratio theRatio
        with respect to the axis theA.
        Note: An affinity is a point-by-point transformation that
        transforms any point P into a point P' such that if H is
        the orthogonal projection of P on the axis theA, the vectors
        HP and HP' satisfy: HP' = theRatio * HP.
        """

    def SetValue(self, theRow: int, theCol: int, theValue: float) -> None:
        """
        Replaces the coefficient (theRow, theCol) of the matrix representing
        this transformation by theValue,
        Raises OutOfRange if theRow < 1 or theRow > 2 or theCol < 1 or theCol > 3
        """

    def SetTranslationPart(self, theCoord: gp_XY) -> None:
        """
        Replaces the translation part of this
        transformation by the coordinates of the number pair theCoord.
        """

    def SetTrsf2d(self, theT: gp_Trsf2d) -> None:
        """
        Assigns the vectorial and translation parts of theT to this transformation.
        """

    def SetVectorialPart(self, theMatrix: gp_Mat2d) -> None:
        """Replaces the vectorial part of this transformation by theMatrix."""

    def IsNegative(self) -> bool:
        """
        Returns true if the determinant of the vectorial part of
        this transformation is negative.
        """

    def IsSingular(self) -> bool:
        """
        Returns true if this transformation is singular (and
        therefore, cannot be inverted).
        Note: The Gauss LU decomposition is used to invert the
        transformation matrix. Consequently, the transformation
        is considered as singular if the largest pivot found is less
        than or equal to gp::Resolution().
        Warning
        If this transformation is singular, it cannot be inverted.
        """

    def Form(self) -> gp_TrsfForm:
        """
        Returns the nature of the transformation. It can be
        an identity transformation, a rotation, a translation, a mirror
        transformation (relative to a point or axis), a scaling
        transformation, a compound transformation or some
        other type of transformation.
        """

    def TranslationPart(self) -> gp_XY:
        """Returns the translation part of the GTrsf2d."""

    def VectorialPart(self) -> gp_Mat2d:
        """
        Computes the vectorial part of the GTrsf2d. The returned
        Matrix is a 2*2 matrix.
        """

    def Value(self, theRow: int, theCol: int) -> float:
        """
        Returns the coefficients of the global matrix of transformation.
        Raised OutOfRange if theRow < 1 or theRow > 2 or theCol < 1 or theCol > 3
        """

    def __call__(self, theRow: int, theCol: int) -> float: ...

    def Invert(self) -> None: ...

    def Inverted(self) -> gp_GTrsf2d:
        """
        Computes the reverse transformation.
        Raised an exception if the matrix of the transformation
        is not inversible.
        """

    def Multiplied(self, theT: gp_GTrsf2d) -> gp_GTrsf2d:
        """
        Computes the transformation composed with theT and <me>.
        In a C++ implementation you can also write Tcomposed = <me> * theT.
        Example :
        @code
        gp_GTrsf2d T1, T2, Tcomp; ...............
        //composition :
        Tcomp = T2.Multiplied(T1);         // or   (Tcomp = T2 * T1)
        // transformation of a point
        gp_XY P(10.,3.);
        gp_XY P1(P);
        Tcomp.Transforms(P1);               //using Tcomp
        gp_XY P2(P);
        T1.Transforms(P2);                  //using T1 then T2
        T2.Transforms(P2);                  // P1 = P2 !!!
        @endcode
        """

    def __mul__(self, theT: gp_GTrsf2d) -> gp_GTrsf2d: ...

    def Multiply(self, theT: gp_GTrsf2d) -> None: ...

    def __imul__(self, theT: gp_GTrsf2d) -> gp_GTrsf2d: ...

    def PreMultiply(self, theT: gp_GTrsf2d) -> None:
        """
        Computes the product of the transformation theT and this
        transformation, and assigns the result to this transformation:
        this = theT * this
        """

    def Power(self, theN: int) -> None: ...

    def Powered(self, theN: int) -> gp_GTrsf2d:
        """
        Computes the following composition of transformations
        <me> * <me> * .......* <me>, theN time.
        if theN = 0 <me> = Identity
        if theN < 0 <me> = <me>.Inverse() *...........* <me>.Inverse().

        Raises an exception if theN < 0 and if the matrix of the
        transformation is not inversible.
        """

    @overload
    def Transforms(self, theCoord: gp_XY) -> None: ...

    @overload
    def Transforms(self, theX: float, theY: float) -> tuple[float, float]:
        """
        Applies this transformation to the coordinates:
        -   of the number pair Coord, or
        -   X and Y.

        Note:
        -   Transforms modifies theX, theY, or the coordinate pair Coord, while
        -   Transformed creates a new coordinate pair.
        """

    def Transformed(self, theCoord: gp_XY) -> gp_XY: ...

    def Trsf2d(self) -> gp_Trsf2d:
        """
        Converts this transformation into a gp_Trsf2d transformation.
        Exceptions
        Standard_ConstructionError if this transformation
        cannot be converted, i.e. if its form is gp_Other.
        """

class gp_Hypr:
    """
    Describes a branch of a hyperbola in 3D space.
    A hyperbola is defined by its major and minor radii and
    positioned in space with a coordinate system (a gp_Ax2
    object) of which:
    -   the origin is the center of the hyperbola,
    -   the "X Direction" defines the major axis of the
    hyperbola, and
    - the "Y Direction" defines the minor axis of the hyperbola.
    The origin, "X Direction" and "Y Direction" of this
    coordinate system together define the plane of the
    hyperbola. This coordinate system is the "local
    coordinate system" of the hyperbola. In this coordinate
    system, the equation of the hyperbola is:
    X*X/(MajorRadius**2)-Y*Y/(MinorRadius**2) = 1.0
    The branch of the hyperbola described is the one located
    on the positive side of the major axis.
    The "main Direction" of the local coordinate system is a
    normal vector to the plane of the hyperbola. This vector
    gives an implicit orientation to the hyperbola. We refer to
    the "main Axis" of the local coordinate system as the
    "Axis" of the hyperbola.
    The following schema shows the plane of the hyperbola,
    and in it, the respective positions of the three branches of
    hyperbolas constructed with the functions OtherBranch,
    ConjugateBranch1, and ConjugateBranch2:
    @code
    ^YAxis
    |
    FirstConjugateBranch
    |
    Other            |                Main
    --------------------- C ------------------------------>XAxis
    Branch           |                Branch
    |
    |
    SecondConjugateBranch
    |                  ^YAxis
    @endcode
    Warning
    The major radius can be less than the minor radius.
    See Also
    gce_MakeHypr which provides functions for more
    complex hyperbola constructions
    Geom_Hyperbola which provides additional functions for
    constructing hyperbolas and works, in particular, with the
    parametric equations of hyperbolas
    """

    @overload
    def __init__(self) -> None:
        """Creates of an indefinite hyperbola."""

    @overload
    def __init__(self, theA2: gp_Ax2, theMajorRadius: float, theMinorRadius: float) -> None:
        """
        Creates a hyperbola with radius theMajorRadius and
        theMinorRadius, positioned in the space by the
        coordinate system theA2 such that:
        -   the origin of theA2 is the center of the hyperbola,
        -   the "X Direction" of theA2 defines the major axis of
        the hyperbola, that is, the major radius
        theMajorRadius is measured along this axis, and
        -   the "Y Direction" of theA2 defines the minor axis of
        the hyperbola, that is, the minor radius
        theMinorRadius is measured along this axis.
        Note: This class does not prevent the creation of a
        hyperbola where:
        -   theMajorAxis is equal to theMinorAxis, or
        -   theMajorAxis is less than theMinorAxis.
        Exceptions
        Standard_ConstructionError if theMajorAxis or theMinorAxis is negative.
        Raises ConstructionError if theMajorRadius < 0.0 or theMinorRadius < 0.0
        Raised if theMajorRadius < 0.0 or theMinorRadius < 0.0
        """

    @overload
    def __init__(self, theOther: gp_Hypr) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeHypr) -> None: ...

    def SetAxis(self, theA1: gp_Ax1) -> None:
        """
        Modifies this hyperbola, by redefining its local coordinate
        system so that:
        -   its origin and "main Direction" become those of the
        axis theA1 (the "X Direction" and "Y Direction" are then
        recomputed in the same way as for any gp_Ax2).
        Raises ConstructionError if the direction of theA1 is parallel to the direction of
        the "XAxis" of the hyperbola.
        """

    def SetLocation(self, theP: gp_Pnt) -> None:
        """
        Modifies this hyperbola, by redefining its local coordinate
        system so that its origin becomes theP.
        """

    def SetMajorRadius(self, theMajorRadius: float) -> None:
        """
        Modifies the major radius of this hyperbola.
        Exceptions
        Standard_ConstructionError if theMajorRadius is negative.
        """

    def SetMinorRadius(self, theMinorRadius: float) -> None:
        """
        Modifies the minor radius of this hyperbola.
        Exceptions
        Standard_ConstructionError if theMinorRadius is negative.
        """

    def SetPosition(self, theA2: gp_Ax2) -> None:
        """
        Modifies this hyperbola, by redefining its local coordinate
        system so that it becomes A2.
        """

    def Asymptote1(self) -> gp_Ax1:
        """
        In the local coordinate system of the hyperbola the equation of
        the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0 and the
        equation of the first asymptote is Y = (B/A)*X
        where A is the major radius and B is the minor radius. Raises ConstructionError if MajorRadius
        = 0.0
        """

    def Asymptote2(self) -> gp_Ax1:
        """
        In the local coordinate system of the hyperbola the equation of
        the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0 and the
        equation of the first asymptote is Y = -(B/A)*X.
        where A is the major radius and B is the minor radius. Raises ConstructionError if MajorRadius
        = 0.0
        """

    def Axis(self) -> gp_Ax1:
        """
        Returns the axis passing through the center,
        and normal to the plane of this hyperbola.
        """

    def ConjugateBranch1(self) -> gp_Hypr:
        """
        Computes the branch of hyperbola which is on the positive side of the
        "YAxis" of <me>.
        """

    def ConjugateBranch2(self) -> gp_Hypr:
        """
        Computes the branch of hyperbola which is on the negative side of the
        "YAxis" of <me>.
        """

    def Directrix1(self) -> gp_Ax1:
        """
        This directrix is the line normal to the XAxis of the hyperbola
        in the local plane (Z = 0) at a distance d = MajorRadius / e
        from the center of the hyperbola, where e is the eccentricity of
        the hyperbola.
        This line is parallel to the "YAxis". The intersection point
        between the directrix1 and the "XAxis" is the "Location" point
        of the directrix1. This point is on the positive side of the
        "XAxis".
        """

    def Directrix2(self) -> gp_Ax1:
        """
        This line is obtained by the symmetrical transformation
        of "Directrix1" with respect to the "YAxis" of the hyperbola.
        """

    def Eccentricity(self) -> float:
        """
        Returns the eccentricity of the hyperbola (e > 1).
        If f is the distance between the location of the hyperbola
        and the Focus1 then the eccentricity e = f / MajorRadius. Raises DomainError if MajorRadius =
        0.0
        """

    def Focal(self) -> float:
        """
        Computes the focal distance. It is the distance between the
        the two focus of the hyperbola.
        """

    def Focus1(self) -> gp_Pnt:
        """
        Returns the first focus of the hyperbola. This focus is on the
        positive side of the "XAxis" of the hyperbola.
        """

    def Focus2(self) -> gp_Pnt:
        """
        Returns the second focus of the hyperbola. This focus is on the
        negative side of the "XAxis" of the hyperbola.
        """

    def Location(self) -> gp_Pnt:
        """
        Returns the location point of the hyperbola. It is the
        intersection point between the "XAxis" and the "YAxis".
        """

    def MajorRadius(self) -> float:
        """
        Returns the major radius of the hyperbola. It is the radius
        on the "XAxis" of the hyperbola.
        """

    def MinorRadius(self) -> float:
        """
        Returns the minor radius of the hyperbola. It is the radius
        on the "YAxis" of the hyperbola.
        """

    def OtherBranch(self) -> gp_Hypr:
        """
        Returns the branch of hyperbola obtained by doing the
        symmetrical transformation of <me> with respect to the
        "YAxis" of <me>.
        """

    def Parameter(self) -> float:
        """
        Returns p = (e * e - 1) * MajorRadius where e is the
        eccentricity of the hyperbola.
        Raises DomainError if MajorRadius = 0.0
        """

    def Position(self) -> gp_Ax2:
        """Returns the coordinate system of the hyperbola."""

    def XAxis(self) -> gp_Ax1:
        """
        Computes an axis, whose
        -   the origin is the center of this hyperbola, and
        -   the unit vector is the "X Direction"
        of the local coordinate system of this hyperbola.
        These axes are, the major axis (the "X
        Axis") and of this hyperboReturns the "XAxis" of the hyperbola.
        """

    def YAxis(self) -> gp_Ax1:
        """
        Computes an axis, whose
        -   the origin is the center of this hyperbola, and
        -   the unit vector is the "Y Direction"
        of the local coordinate system of this hyperbola.
        These axes are the minor axis (the "Y Axis") of this hyperbola
        """

    @overload
    def Mirror(self, theP: gp_Pnt) -> None: ...

    @overload
    def Mirror(self, theA1: gp_Ax1) -> None: ...

    @overload
    def Mirror(self, theA2: gp_Ax2) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt) -> gp_Hypr:
        """
        Performs the symmetrical transformation of an hyperbola with
        respect to the point theP which is the center of the symmetry.
        """

    @overload
    def Mirrored(self, theA1: gp_Ax1) -> gp_Hypr:
        """
        Performs the symmetrical transformation of an hyperbola with
        respect to an axis placement which is the axis of the symmetry.
        """

    @overload
    def Mirrored(self, theA2: gp_Ax2) -> gp_Hypr:
        """
        Performs the symmetrical transformation of an hyperbola with
        respect to a plane. The axis placement theA2 locates the plane
        of the symmetry (Location, XDirection, YDirection).
        """

    def Rotate(self, theA1: gp_Ax1, theAng: float) -> None: ...

    def Rotated(self, theA1: gp_Ax1, theAng: float) -> gp_Hypr:
        """
        Rotates an hyperbola. theA1 is the axis of the rotation.
        theAng is the angular value of the rotation in radians.
        """

    def Scale(self, theP: gp_Pnt, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt, theS: float) -> gp_Hypr:
        """Scales an hyperbola. theS is the scaling value."""

    def Transform(self, theT: gp_Trsf) -> None: ...

    def Transformed(self, theT: gp_Trsf) -> gp_Hypr:
        """
        Transforms an hyperbola with the transformation theT from
        class Trsf.
        """

    @overload
    def Translate(self, theV: gp_Vec) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec) -> gp_Hypr:
        """
        Translates an hyperbola in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt, theP2: gp_Pnt) -> gp_Hypr:
        """Translates an hyperbola from the point theP1 to the point theP2."""

class gp_Hypr2d:
    """
    Describes a branch of a hyperbola in the plane (2D space).
    A hyperbola is defined by its major and minor radii, and
    positioned in the plane with a coordinate system (a
    gp_Ax22d object) of which:
    -   the origin is the center of the hyperbola,
    -   the "X Direction" defines the major axis of the hyperbola, and
    -   the "Y Direction" defines the minor axis of the hyperbola.
    This coordinate system is the "local coordinate system"
    of the hyperbola. The orientation of this coordinate
    system (direct or indirect) gives an implicit orientation to
    the hyperbola. In this coordinate system, the equation of
    the hyperbola is:
    X*X/(MajorRadius**2)-Y*Y/(MinorRadius**2) = 1.0
    The branch of the hyperbola described is the one located
    on the positive side of the major axis.
    The following schema shows the plane of the hyperbola,
    and in it, the respective positions of the three branches of
    hyperbolas constructed with the functions OtherBranch,
    ConjugateBranch1, and ConjugateBranch2:
    @code
    ^YAxis
    |
    FirstConjugateBranch
    |
    Other            |                Main
    --------------------- C ------------------------------>XAxis
    Branch           |                Branch
    |
    |
    SecondConjugateBranch
    |
    @endcode
    Warning
    The major radius can be less than the minor radius.
    See Also
    gce_MakeHypr2d which provides functions for more
    complex hyperbola constructions
    Geom2d_Hyperbola which provides additional functions
    for constructing hyperbolas and works, in particular, with
    the parametric equations of hyperbolas
    """

    @overload
    def __init__(self) -> None:
        """Creates of an indefinite hyperbola."""

    @overload
    def __init__(self, theMajorAxis: gp_Ax2d, theMajorRadius: float, theMinorRadius: float, theIsSense: bool = True) -> None:
        """
        Creates a hyperbola with radii theMajorRadius and
        theMinorRadius, centered on the origin of theMajorAxis
        and where the unit vector of theMajorAxis is the "X
        Direction" of the local coordinate system of the
        hyperbola. This coordinate system is direct if theIsSense
        is true (the default value), and indirect if theIsSense is false.
        Warnings:
        It is yet possible to create an Hyperbola with
        theMajorRadius <= theMinorRadius.
        Raises ConstructionError if theMajorRadius < 0.0 or theMinorRadius < 0.0
        """

    @overload
    def __init__(self, theA: gp_Ax22d, theMajorRadius: float, theMinorRadius: float) -> None:
        """
        a hyperbola with radii theMajorRadius and
        theMinorRadius, positioned in the plane by coordinate system theA where:
        -   the origin of theA is the center of the hyperbola,
        -   the "X Direction" of theA defines the major axis of
        the hyperbola, that is, the major radius
        theMajorRadius is measured along this axis, and
        -   the "Y Direction" of theA defines the minor axis of
        the hyperbola, that is, the minor radius
        theMinorRadius is measured along this axis, and
        -   the orientation (direct or indirect sense) of theA
        gives the implicit orientation of the hyperbola.
        Warnings:
        It is yet possible to create an Hyperbola with
        theMajorRadius <= theMinorRadius.
        Raises ConstructionError if theMajorRadius < 0.0 or theMinorRadius < 0.0
        """

    @overload
    def __init__(self, theOther: gp_Hypr2d) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeHypr2d) -> None: ...

    def SetLocation(self, theP: gp_Pnt2d) -> None:
        """
        Modifies this hyperbola, by redefining its local
        coordinate system so that its origin becomes theP.
        """

    def SetMajorRadius(self, theMajorRadius: float) -> None:
        """
        Modifies the major or minor radius of this hyperbola.
        Exceptions
        Standard_ConstructionError if theMajorRadius or
        MinorRadius is negative.
        """

    def SetMinorRadius(self, theMinorRadius: float) -> None:
        """
        Modifies the major or minor radius of this hyperbola.
        Exceptions
        Standard_ConstructionError if MajorRadius or
        theMinorRadius is negative.
        """

    def SetAxis(self, theA: gp_Ax22d) -> None:
        """
        Modifies this hyperbola, by redefining its local
        coordinate system so that it becomes theA.
        """

    def SetXAxis(self, theA: gp_Ax2d) -> None:
        """
        Changes the major axis of the hyperbola. The minor axis is
        recomputed and the location of the hyperbola too.
        """

    def SetYAxis(self, theA: gp_Ax2d) -> None:
        """
        Changes the minor axis of the hyperbola.The minor axis is
        recomputed and the location of the hyperbola too.
        """

    def Asymptote1(self) -> gp_Ax2d:
        """
        In the local coordinate system of the hyperbola the equation of
        the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0 and the
        equation of the first asymptote is Y = (B/A)*X
        where A is the major radius of the hyperbola and B the minor
        radius of the hyperbola.
        Raises ConstructionError if MajorRadius = 0.0
        """

    def Asymptote2(self) -> gp_Ax2d:
        """
        In the local coordinate system of the hyperbola the equation of
        the hyperbola is (X*X)/(A*A) - (Y*Y)/(B*B) = 1.0 and the
        equation of the first asymptote is Y = -(B/A)*X
        where A is the major radius of the hyperbola and B the minor
        radius of the hyperbola.
        Raises ConstructionError if MajorRadius = 0.0
        """

    def Coefficients(self) -> tuple[float, float, float, float, float, float]:
        """
        Computes the coefficients of the implicit equation of
        the hyperbola :
        theA * (X**2) + theB * (Y**2) + 2*theC*(X*Y) + 2*theD*X + 2*theE*Y + theF = 0.
        """

    def ConjugateBranch1(self) -> gp_Hypr2d:
        """
        Computes the branch of hyperbola which is on the positive side of the
        "YAxis" of <me>.
        """

    def ConjugateBranch2(self) -> gp_Hypr2d:
        """
        Computes the branch of hyperbola which is on the negative side of the
        "YAxis" of <me>.
        """

    def Directrix1(self) -> gp_Ax2d:
        """
        Computes the directrix which is the line normal to the XAxis of the hyperbola
        in the local plane (Z = 0) at a distance d = MajorRadius / e
        from the center of the hyperbola, where e is the eccentricity of
        the hyperbola.
        This line is parallel to the "YAxis". The intersection point
        between the "Directrix1" and the "XAxis" is the "Location" point
        of the "Directrix1".
        This point is on the positive side of the "XAxis".
        """

    def Directrix2(self) -> gp_Ax2d:
        """
        This line is obtained by the symmetrical transformation
        of "Directrix1" with respect to the "YAxis" of the hyperbola.
        """

    def Eccentricity(self) -> float:
        """
        Returns the eccentricity of the hyperbola (e > 1).
        If f is the distance between the location of the hyperbola
        and the Focus1 then the eccentricity e = f / MajorRadius. Raises DomainError if MajorRadius =
        0.0.
        """

    def Focal(self) -> float:
        """
        Computes the focal distance. It is the distance between the
        "Location" of the hyperbola and "Focus1" or "Focus2".
        """

    def Focus1(self) -> gp_Pnt2d:
        """
        Returns the first focus of the hyperbola. This focus is on the
        positive side of the "XAxis" of the hyperbola.
        """

    def Focus2(self) -> gp_Pnt2d:
        """
        Returns the second focus of the hyperbola. This focus is on the
        negative side of the "XAxis" of the hyperbola.
        """

    def Location(self) -> gp_Pnt2d:
        """
        Returns the location point of the hyperbola.
        It is the intersection point between the "XAxis" and
        the "YAxis".
        """

    def MajorRadius(self) -> float:
        """
        Returns the major radius of the hyperbola (it is the radius
        corresponding to the "XAxis" of the hyperbola).
        """

    def MinorRadius(self) -> float:
        """
        Returns the minor radius of the hyperbola (it is the radius
        corresponding to the "YAxis" of the hyperbola).
        """

    def OtherBranch(self) -> gp_Hypr2d:
        """
        Returns the branch of hyperbola obtained by doing the
        symmetrical transformation of <me> with respect to the
        "YAxis" of <me>.
        """

    def Parameter(self) -> float:
        """
        Returns p = (e * e - 1) * MajorRadius where e is the
        eccentricity of the hyperbola.
        Raises DomainError if MajorRadius = 0.0
        """

    def Axis(self) -> gp_Ax22d:
        """Returns the axisplacement of the hyperbola."""

    def XAxis(self) -> gp_Ax2d:
        """
        Computes an axis whose
        -   the origin is the center of this hyperbola, and
        -   the unit vector is the "X Direction" or "Y Direction"
        respectively of the local coordinate system of this hyperbola
        Returns the major axis of the hyperbola.
        """

    def YAxis(self) -> gp_Ax2d:
        """
        Computes an axis whose
        -   the origin is the center of this hyperbola, and
        -   the unit vector is the "X Direction" or "Y Direction"
        respectively of the local coordinate system of this hyperbola
        Returns the minor axis of the hyperbola.
        """

    def Reverse(self) -> None: ...

    def Reversed(self) -> gp_Hypr2d:
        """
        Reverses the orientation of the local coordinate system
        of this hyperbola (the "Y Axis" is reversed). Therefore,
        the implicit orientation of this hyperbola is reversed.
        Note:
        -   Reverse assigns the result to this hyperbola, while
        -   Reversed creates a new one.
        """

    def IsDirect(self) -> bool:
        """
        Returns true if the local coordinate system is direct
        and false in the other case.
        """

    @overload
    def Mirror(self, theP: gp_Pnt2d) -> None: ...

    @overload
    def Mirror(self, theA: gp_Ax2d) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt2d) -> gp_Hypr2d:
        """
        Performs the symmetrical transformation of an hyperbola with
        respect to the point theP which is the center of the symmetry.
        """

    @overload
    def Mirrored(self, theA: gp_Ax2d) -> gp_Hypr2d:
        """
        Performs the symmetrical transformation of an hyperbola with
        respect to an axis placement which is the axis of the symmetry.
        """

    def Rotate(self, theP: gp_Pnt2d, theAng: float) -> None: ...

    def Rotated(self, theP: gp_Pnt2d, theAng: float) -> gp_Hypr2d:
        """
        Rotates an hyperbola. theP is the center of the rotation.
        theAng is the angular value of the rotation in radians.
        """

    def Scale(self, theP: gp_Pnt2d, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt2d, theS: float) -> gp_Hypr2d:
        """
        Scales an hyperbola. <theS> is the scaling value.
        If <theS> is positive only the location point is
        modified. But if <theS> is negative the "XAxis" is
        reversed and the "YAxis" too.
        """

    def Transform(self, theT: gp_Trsf2d) -> None: ...

    def Transformed(self, theT: gp_Trsf2d) -> gp_Hypr2d:
        """
        Transforms an hyperbola with the transformation theT from
        class Trsf2d.
        """

    @overload
    def Translate(self, theV: gp_Vec2d) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec2d) -> gp_Hypr2d:
        """
        Translates an hyperbola in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> gp_Hypr2d:
        """Translates an hyperbola from the point theP1 to the point theP2."""

class gp_Lin:
    """
    Describes a line in 3D space.
    A line is positioned in space with an axis (a gp_Ax1
    object) which gives it an origin and a unit vector.
    A line and an axis are similar objects, thus, we can
    convert one into the other. A line provides direct access
    to the majority of the edit and query functions available
    on its positioning axis. In addition, however, a line has
    specific functions for computing distances and positions.
    See Also
    gce_MakeLin which provides functions for more complex
    line constructions
    Geom_Line which provides additional functions for
    constructing lines and works, in particular, with the
    parametric equations of lines
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a Line corresponding to Z axis of the
        reference coordinate system.
        """

    @overload
    def __init__(self, theA1: gp_Ax1) -> None:
        """Creates a line defined by axis theA1."""

    @overload
    def __init__(self, theP: gp_Pnt, theV: gp_Dir) -> None:
        """
        Creates a line passing through point theP and parallel to
        vector theV (theP and theV are, respectively, the origin and
        the unit vector of the positioning axis of the line).
        """

    @overload
    def __init__(self, theOther: gp_Lin) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeLin) -> None: ...

    def Reverse(self) -> None: ...

    def Reversed(self) -> gp_Lin:
        """
        Reverses the direction of the line.
        Note:
        -   Reverse assigns the result to this line, while
        -   Reversed creates a new one.
        """

    def SetDirection(self, theV: gp_Dir) -> None:
        """Changes the direction of the line."""

    def SetLocation(self, theP: gp_Pnt) -> None:
        """Changes the location point (origin) of the line."""

    def SetPosition(self, theA1: gp_Ax1) -> None:
        """
        Complete redefinition of the line.
        The "Location" point of <theA1> is the origin of the line.
        The "Direction" of <theA1> is the direction of the line.
        """

    def Direction(self) -> gp_Dir:
        """Returns the direction of the line."""

    def Location(self) -> gp_Pnt:
        """Returns the location point (origin) of the line."""

    def Position(self) -> gp_Ax1:
        """
        Returns the axis placement one axis with the same
        location and direction as <me>.
        """

    def Angle(self, theOther: gp_Lin) -> float:
        """Computes the angle between two lines in radians."""

    def Contains(self, theP: gp_Pnt, theLinearTolerance: float) -> bool:
        """
        Returns true if this line contains the point theP, that is, if the
        distance between point theP and this line is less than or
        equal to theLinearTolerance..
        """

    @overload
    def Distance(self, theP: gp_Pnt) -> float:
        """Computes the distance between <me> and the point theP."""

    @overload
    def Distance(self, theOther: gp_Lin) -> float:
        """Computes the distance between two lines."""

    @overload
    def SquareDistance(self, theP: gp_Pnt) -> float:
        """Computes the square distance between <me> and the point theP."""

    @overload
    def SquareDistance(self, theOther: gp_Lin) -> float:
        """Computes the square distance between two lines."""

    def Normal(self, theP: gp_Pnt) -> gp_Lin:
        """
        Computes the line normal to the direction of <me>, passing
        through the point theP. Raises ConstructionError
        if the distance between <me> and the point theP is lower
        or equal to Resolution from gp because there is an infinity of
        solutions in 3D space.
        """

    @overload
    def Mirror(self, theP: gp_Pnt) -> None: ...

    @overload
    def Mirror(self, theA1: gp_Ax1) -> None: ...

    @overload
    def Mirror(self, theA2: gp_Ax2) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt) -> gp_Lin:
        """
        Performs the symmetrical transformation of a line
        with respect to the point theP which is the center of
        the symmetry.
        """

    @overload
    def Mirrored(self, theA1: gp_Ax1) -> gp_Lin:
        """
        Performs the symmetrical transformation of a line
        with respect to an axis placement which is the axis
        of the symmetry.
        """

    @overload
    def Mirrored(self, theA2: gp_Ax2) -> gp_Lin:
        """
        Performs the symmetrical transformation of a line
        with respect to a plane. The axis placement <theA2>
        locates the plane of the symmetry:
        (Location, XDirection, YDirection).
        """

    def Rotate(self, theA1: gp_Ax1, theAng: float) -> None: ...

    def Rotated(self, theA1: gp_Ax1, theAng: float) -> gp_Lin:
        """
        Rotates a line. A1 is the axis of the rotation.
        Ang is the angular value of the rotation in radians.
        """

    def Scale(self, theP: gp_Pnt, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt, theS: float) -> gp_Lin:
        """
        Scales a line. theS is the scaling value.
        The "Location" point (origin) of the line is modified.
        The "Direction" is reversed if the scale is negative.
        """

    def Transform(self, theT: gp_Trsf) -> None: ...

    def Transformed(self, theT: gp_Trsf) -> gp_Lin:
        """Transforms a line with the transformation theT from class Trsf."""

    @overload
    def Translate(self, theV: gp_Vec) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec) -> gp_Lin:
        """
        Translates a line in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt, theP2: gp_Pnt) -> gp_Lin:
        """Translates a line from the point theP1 to the point theP2."""

class gp_Lin2d:
    """
    Describes a line in 2D space.
    A line is positioned in the plane with an axis (a gp_Ax2d
    object) which gives the line its origin and unit vector. A
    line and an axis are similar objects, thus, we can convert
    one into the other.
    A line provides direct access to the majority of the edit
    and query functions available on its positioning axis. In
    addition, however, a line has specific functions for
    computing distances and positions.
    See Also
    GccAna and Geom2dGcc packages which provide
    functions for constructing lines defined by geometric
    constraints
    gce_MakeLin2d which provides functions for more
    complex line constructions
    Geom2d_Line which provides additional functions for
    constructing lines and works, in particular, with the
    parametric equations of lines
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a Line corresponding to X axis of the
        reference coordinate system.
        """

    @overload
    def __init__(self, theA: gp_Ax2d) -> None:
        """Creates a line located with theA."""

    @overload
    def __init__(self, theP: gp_Pnt2d, theV: gp_Dir2d) -> None:
        """
        <theP> is the location point (origin) of the line and
        <theV> is the direction of the line.
        """

    @overload
    def __init__(self, theA: float, theB: float, theC: float) -> None:
        """
        Creates the line from the equation theA*X + theB*Y + theC = 0.0 Raises ConstructionError if
        std::sqrt(theA*theA + theB*theB) <= Resolution from gp. Raised if std::sqrt(theA*theA +
        theB*theB) <= Resolution from gp.
        """

    @overload
    def __init__(self, theOther: gp_Lin2d) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeLin2d) -> None: ...

    def Reverse(self) -> None: ...

    def Reversed(self) -> gp_Lin2d:
        """
        Reverses the positioning axis of this line.
        Note:
        -   Reverse assigns the result to this line, while
        -   Reversed creates a new one.
        """

    def SetDirection(self, theV: gp_Dir2d) -> None:
        """Changes the direction of the line."""

    def SetLocation(self, theP: gp_Pnt2d) -> None:
        """Changes the origin of the line."""

    def SetPosition(self, theA: gp_Ax2d) -> None:
        """
        Complete redefinition of the line.
        The "Location" point of <theA> is the origin of the line.
        The "Direction" of <theA> is the direction of the line.
        """

    def Coefficients(self) -> tuple[float, float, float]:
        """
        Returns the normalized coefficients of the line :
        theA * X + theB * Y + theC = 0.
        """

    def Direction(self) -> gp_Dir2d:
        """Returns the direction of the line."""

    def Location(self) -> gp_Pnt2d:
        """Returns the location point (origin) of the line."""

    def Position(self) -> gp_Ax2d:
        """
        Returns the axis placement one axis with the same
        location and direction as <me>.
        """

    def Angle(self, theOther: gp_Lin2d) -> float:
        """Computes the angle between two lines in radians."""

    def Contains(self, theP: gp_Pnt2d, theLinearTolerance: float) -> bool:
        """
        Returns true if this line contains the point theP, that is, if the
        distance between point theP and this line is less than or
        equal to theLinearTolerance.
        """

    @overload
    def Distance(self, theP: gp_Pnt2d) -> float:
        """Computes the distance between <me> and the point <theP>."""

    @overload
    def Distance(self, theOther: gp_Lin2d) -> float:
        """Computes the distance between two lines."""

    @overload
    def SquareDistance(self, theP: gp_Pnt2d) -> float:
        """
        Computes the square distance between <me> and the point
        <theP>.
        """

    @overload
    def SquareDistance(self, theOther: gp_Lin2d) -> float:
        """Computes the square distance between two lines."""

    def Normal(self, theP: gp_Pnt2d) -> gp_Lin2d:
        """
        Computes the line normal to the direction of <me>,
        passing through the point <theP>.
        """

    @overload
    def Mirror(self, theP: gp_Pnt2d) -> None: ...

    @overload
    def Mirror(self, theA: gp_Ax2d) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt2d) -> gp_Lin2d:
        """
        Performs the symmetrical transformation of a line
        with respect to the point <theP> which is the center
        of the symmetry
        """

    @overload
    def Mirrored(self, theA: gp_Ax2d) -> gp_Lin2d:
        """
        Performs the symmetrical transformation of a line
        with respect to an axis placement which is the axis
        of the symmetry.
        """

    def Rotate(self, theP: gp_Pnt2d, theAng: float) -> None: ...

    def Rotated(self, theP: gp_Pnt2d, theAng: float) -> gp_Lin2d:
        """
        Rotates a line. theP is the center of the rotation.
        theAng is the angular value of the rotation in radians.
        """

    def Scale(self, theP: gp_Pnt2d, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt2d, theS: float) -> gp_Lin2d:
        """
        Scales a line. theS is the scaling value. Only the
        origin of the line is modified.
        """

    def Transform(self, theT: gp_Trsf2d) -> None: ...

    def Transformed(self, theT: gp_Trsf2d) -> gp_Lin2d:
        """Transforms a line with the transformation theT from class Trsf2d."""

    @overload
    def Translate(self, theV: gp_Vec2d) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec2d) -> gp_Lin2d:
        """
        Translates a line in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> gp_Lin2d:
        """Translates a line from the point theP1 to the point theP2."""

class gp_Parab:
    """
    Describes a parabola in 3D space.
    A parabola is defined by its focal length (that is, the
    distance between its focus and apex) and positioned in
    space with a coordinate system (a gp_Ax2 object)
    where:
    -   the origin of the coordinate system is on the apex of
    the parabola,
    -   the "X Axis" of the coordinate system is the axis of
    symmetry; the parabola is on the positive side of this axis, and
    -   the origin, "X Direction" and "Y Direction" of the
    coordinate system define the plane of the parabola.
    The equation of the parabola in this coordinate system,
    which is the "local coordinate system" of the parabola, is:
    @code
    Y**2 = (2*P) * X.
    @endcode
    where P, referred to as the parameter of the parabola, is
    the distance between the focus and the directrix (P is
    twice the focal length).
    The "main Direction" of the local coordinate system gives
    the normal vector to the plane of the parabola.
    See Also
    gce_MakeParab which provides functions for more
    complex parabola constructions
    Geom_Parabola which provides additional functions for
    constructing parabolas and works, in particular, with the
    parametric equations of parabolas
    """

    @overload
    def __init__(self) -> None:
        """Creates an indefinite Parabola."""

    @overload
    def __init__(self, theA2: gp_Ax2, theFocal: float) -> None:
        """
        Creates a parabola with its local coordinate system "theA2"
        and it's focal length "Focal".
        The XDirection of theA2 defines the axis of symmetry of the
        parabola. The YDirection of theA2 is parallel to the directrix
        of the parabola. The Location point of theA2 is the vertex of
        the parabola
        Raises ConstructionError if theFocal < 0.0
        Raised if theFocal < 0.0
        """

    @overload
    def __init__(self, theD: gp_Ax1, theF: gp_Pnt) -> None:
        """
        theD is the directrix of the parabola and theF the focus point.
        The symmetry axis (XAxis) of the parabola is normal to the
        directrix and pass through the focus point theF, but its
        location point is the vertex of the parabola.
        The YAxis of the parabola is parallel to theD and its location
        point is the vertex of the parabola. The normal to the plane
        of the parabola is the cross product between the XAxis and the
        YAxis.
        """

    @overload
    def __init__(self, theOther: gp_Parab) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeParab) -> None: ...

    def SetAxis(self, theA1: gp_Ax1) -> None:
        """
        Modifies this parabola by redefining its local coordinate system so that
        -   its origin and "main Direction" become those of the
        axis theA1 (the "X Direction" and "Y Direction" are then
        recomputed in the same way as for any gp_Ax2)
        Raises ConstructionError if the direction of theA1 is parallel to the previous
        XAxis of the parabola.
        """

    def SetFocal(self, theFocal: float) -> None:
        """
        Changes the focal distance of the parabola.
        Raises ConstructionError if theFocal < 0.0
        """

    def SetLocation(self, theP: gp_Pnt) -> None:
        """
        Changes the location of the parabola. It is the vertex of
        the parabola.
        """

    def SetPosition(self, theA2: gp_Ax2) -> None:
        """Changes the local coordinate system of the parabola."""

    def Axis(self) -> gp_Ax1:
        """
        Returns the main axis of the parabola.
        It is the axis normal to the plane of the parabola passing
        through the vertex of the parabola.
        """

    def Directrix(self) -> gp_Ax1:
        """
        Computes the directrix of this parabola.
        The directrix is:
        -   a line parallel to the "Y Direction" of the local
        coordinate system of this parabola, and
        -   located on the negative side of the axis of symmetry,
        at a distance from the apex which is equal to the focal
        length of this parabola.
        The directrix is returned as an axis (a gp_Ax1 object),
        the origin of which is situated on the "X Axis" of this parabola.
        """

    def Focal(self) -> float:
        """
        Returns the distance between the vertex and the focus
        of the parabola.
        """

    def Focus(self) -> gp_Pnt:
        """-   Computes the focus of the parabola."""

    def Location(self) -> gp_Pnt:
        """
        Returns the vertex of the parabola. It is the "Location"
        point of the coordinate system of the parabola.
        """

    def Parameter(self) -> float:
        """
        Computes the parameter of the parabola.
        It is the distance between the focus and the directrix of
        the parabola. This distance is twice the focal length.
        """

    def Position(self) -> gp_Ax2:
        """Returns the local coordinate system of the parabola."""

    def XAxis(self) -> gp_Ax1:
        """
        Returns the symmetry axis of the parabola. The location point
        of the axis is the vertex of the parabola.
        """

    def YAxis(self) -> gp_Ax1:
        """
        It is an axis parallel to the directrix of the parabola.
        The location point of this axis is the vertex of the parabola.
        """

    @overload
    def Mirror(self, theP: gp_Pnt) -> None: ...

    @overload
    def Mirror(self, theA1: gp_Ax1) -> None: ...

    @overload
    def Mirror(self, theA2: gp_Ax2) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt) -> gp_Parab:
        """
        Performs the symmetrical transformation of a parabola
        with respect to the point theP which is the center of the
        symmetry.
        """

    @overload
    def Mirrored(self, theA1: gp_Ax1) -> gp_Parab:
        """
        Performs the symmetrical transformation of a parabola
        with respect to an axis placement which is the axis of
        the symmetry.
        """

    @overload
    def Mirrored(self, theA2: gp_Ax2) -> gp_Parab:
        """
        Performs the symmetrical transformation of a parabola
        with respect to a plane. The axis placement theA2 locates
        the plane of the symmetry (Location, XDirection, YDirection).
        """

    def Rotate(self, theA1: gp_Ax1, theAng: float) -> None: ...

    def Rotated(self, theA1: gp_Ax1, theAng: float) -> gp_Parab:
        """
        Rotates a parabola. theA1 is the axis of the rotation.
        Ang is the angular value of the rotation in radians.
        """

    def Scale(self, theP: gp_Pnt, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt, theS: float) -> gp_Parab:
        """
        Scales a parabola. theS is the scaling value.
        If theS is negative the direction of the symmetry axis
        XAxis is reversed and the direction of the YAxis too.
        """

    def Transform(self, theT: gp_Trsf) -> None: ...

    def Transformed(self, theT: gp_Trsf) -> gp_Parab:
        """Transforms a parabola with the transformation theT from class Trsf."""

    @overload
    def Translate(self, theV: gp_Vec) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec) -> gp_Parab:
        """
        Translates a parabola in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt, theP2: gp_Pnt) -> gp_Parab:
        """Translates a parabola from the point theP1 to the point theP2."""

class gp_Parab2d:
    """
    Describes a parabola in the plane (2D space).
    A parabola is defined by its focal length (that is, the
    distance between its focus and apex) and positioned in
    the plane with a coordinate system (a gp_Ax22d object) where:
    -   the origin of the coordinate system is on the apex of
    the parabola, and
    -   the "X Axis" of the coordinate system is the axis of
    symmetry; the parabola is on the positive side of this axis.
    This coordinate system is the "local coordinate system"
    of the parabola. Its orientation (direct or indirect sense)
    gives an implicit orientation to the parabola.
    In this coordinate system, the equation for the parabola is:
    @code
    Y**2 = (2*P) * X.
    @endcode
    where P, referred to as the parameter of the parabola, is
    the distance between the focus and the directrix (P is
    twice the focal length).
    See Also
    GCE2d_MakeParab2d which provides functions for
    more complex parabola constructions
    Geom2d_Parabola which provides additional functions
    for constructing parabolas and works, in particular, with
    the parametric equations of parabolas
    """

    @overload
    def __init__(self) -> None:
        """Creates an indefinite parabola."""

    @overload
    def __init__(self, theMirrorAxis: gp_Ax2d, theFocalLength: float, theSense: bool = True) -> None:
        """
        Creates a parabola with its vertex point, its axis of symmetry
        ("XAxis") and its focal length.
        The sense of parametrization is given by theSense. If theSense == TRUE
        (by default) then right-handed coordinate system is used,
        otherwise - left-handed.
        Warnings : It is possible to have FocalLength = 0. In this case,
        the parabola looks like a line, which is parallel to the symmetry-axis.
        Raises ConstructionError if FocalLength < 0.0
        """

    @overload
    def __init__(self, theAxes: gp_Ax22d, theFocalLength: float) -> None:
        """
        Creates a parabola with its vertex point, its axis of symmetry
        ("XAxis"), correspond Y-axis and its focal length.
        Warnings : It is possible to have FocalLength = 0. In this case,
        the parabola looks like a line, which is parallel to the symmetry-axis.
        Raises ConstructionError if Focal < 0.0
        """

    @overload
    def __init__(self, theDirectrix: gp_Ax2d, theFocus: gp_Pnt2d, theSense: bool = True) -> None:
        """
        Creates a parabola with the directrix and the focus point.
        Y-axis of the parabola (in User Coordinate System - UCS) is
        the direction of theDirectrix. X-axis always directs from theDirectrix
        to theFocus point and always comes through theFocus.
        Apex of the parabola is a middle point between the theFocus and the
        intersection point of theDirectrix and the X-axis.
        Warnings : It is possible to have FocalLength = 0 (when theFocus lies
        in theDirectrix). In this case, X-direction of the parabola is defined
        by theSense parameter. If theSense == TRUE (by default) then right-handed
        coordinate system is used, otherwise - left-handed. Result parabola will look
        like a line, which is perpendicular to the directrix.
        """

    @overload
    def __init__(self, theOther: gp_Parab2d) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakeParab2d) -> None: ...

    def SetFocal(self, theFocal: float) -> None:
        """
        Changes the focal distance of the parabola
        Warnings : It is possible to have theFocal = 0.
        Raises ConstructionError if theFocal < 0.0
        """

    def SetLocation(self, theP: gp_Pnt2d) -> None:
        """
        Changes the "Location" point of the parabola. It is the
        vertex of the parabola.
        """

    def SetMirrorAxis(self, theA: gp_Ax2d) -> None:
        """
        Modifies this parabola, by redefining its local coordinate system so that
        its origin and "X Direction" become those of the axis
        MA. The "Y Direction" of the local coordinate system is
        then recomputed. The orientation of the local
        coordinate system is not modified.
        """

    def SetAxis(self, theA: gp_Ax22d) -> None:
        """
        Changes the local coordinate system of the parabola.
        The "Location" point of A becomes the vertex of the parabola.
        """

    def Coefficients(self) -> tuple[float, float, float, float, float, float]:
        """
        Computes the coefficients of the implicit equation of the parabola
        (in WCS - World Coordinate System).
        @code
        theA * (X**2) + theB * (Y**2) + 2*theC*(X*Y) + 2*theD*X + 2*theE*Y + theF = 0.
        @endcode
        """

    def Directrix(self) -> gp_Ax2d:
        """
        Computes the directrix of the parabola.
        The directrix is:
        -   a line parallel to the "Y Direction" of the local
        coordinate system of this parabola, and
        -   located on the negative side of the axis of symmetry,
        at a distance from the apex which is equal to the focal length of this parabola.
        The directrix is returned as an axis (a gp_Ax2d object),
        the origin of which is situated on the "X Axis" of this parabola.
        """

    def Focal(self) -> float:
        """
        Returns the distance between the vertex and the focus
        of the parabola.
        """

    def Focus(self) -> gp_Pnt2d:
        """Returns the focus of the parabola."""

    def Location(self) -> gp_Pnt2d:
        """Returns the vertex of the parabola."""

    def MirrorAxis(self) -> gp_Ax2d:
        """
        Returns the symmetry axis of the parabola.
        The "Location" point of this axis is the vertex of the parabola.
        """

    def Axis(self) -> gp_Ax22d:
        """
        Returns the local coordinate system of the parabola.
        The "Location" point of this axis is the vertex of the parabola.
        """

    def Parameter(self) -> float:
        """
        Returns the distance between the focus and the
        directrix of the parabola.
        """

    def Reverse(self) -> None: ...

    def Reversed(self) -> gp_Parab2d:
        """
        Reverses the orientation of the local coordinate system
        of this parabola (the "Y Direction" is reversed).
        Therefore, the implicit orientation of this parabola is reversed.
        Note:
        -   Reverse assigns the result to this parabola, while
        -   Reversed creates a new one.
        """

    def IsDirect(self) -> bool:
        """
        Returns true if the local coordinate system is direct
        and false in the other case.
        """

    @overload
    def Mirror(self, theP: gp_Pnt2d) -> None: ...

    @overload
    def Mirror(self, theA: gp_Ax2d) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt2d) -> gp_Parab2d:
        """
        Performs the symmetrical transformation of a parabola with respect
        to the point theP which is the center of the symmetry
        """

    @overload
    def Mirrored(self, theA: gp_Ax2d) -> gp_Parab2d:
        """
        Performs the symmetrical transformation of a parabola with respect
        to an axis placement which is the axis of the symmetry.
        """

    def Rotate(self, theP: gp_Pnt2d, theAng: float) -> None: ...

    def Rotated(self, theP: gp_Pnt2d, theAng: float) -> gp_Parab2d:
        """
        Rotates a parabola. theP is the center of the rotation.
        theAng is the angular value of the rotation in radians.
        """

    def Scale(self, theP: gp_Pnt2d, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt2d, theS: float) -> gp_Parab2d:
        """
        Scales a parabola. theS is the scaling value.
        If theS is negative the direction of the symmetry axis
        "XAxis" is reversed and the direction of the "YAxis" too.
        """

    def Transform(self, theT: gp_Trsf2d) -> None: ...

    def Transformed(self, theT: gp_Trsf2d) -> gp_Parab2d:
        """Transforms an parabola with the transformation theT from class Trsf2d."""

    @overload
    def Translate(self, theV: gp_Vec2d) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec2d) -> gp_Parab2d:
        """
        Translates a parabola in the direction of the vectorthe theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt2d, theP2: gp_Pnt2d) -> gp_Parab2d:
        """Translates a parabola from the point theP1 to the point theP2."""

class gp_Pln:
    """
    Describes a plane.
    A plane is positioned in space with a coordinate system
    (a gp_Ax3 object), such that the plane is defined by the
    origin, "X Direction" and "Y Direction" of this coordinate
    system, which is the "local coordinate system" of the
    plane. The "main Direction" of the coordinate system is a
    vector normal to the plane. It gives the plane an implicit
    orientation such that the plane is said to be "direct", if the
    coordinate system is right-handed, or "indirect" in the other case.
    Note: when a gp_Pln plane is converted into a
    Geom_Plane plane, some implicit properties of its local
    coordinate system are used explicitly:
    -   its origin defines the origin of the two parameters of
    the planar surface,
    -   its implicit orientation is also that of the Geom_Plane.
    See Also
    gce_MakePln which provides functions for more complex
    plane constructions
    Geom_Plane which provides additional functions for
    constructing planes and works, in particular, with the
    parametric equations of planes
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a plane coincident with OXY plane of the
        reference coordinate system.
        """

    @overload
    def __init__(self, theA3: gp_Ax3) -> None:
        """
        The coordinate system of the plane is defined with the axis
        placement theA3.
        The "Direction" of theA3 defines the normal to the plane.
        The "Location" of theA3 defines the location (origin) of the plane.
        The "XDirection" and "YDirection" of theA3 define the "XAxis" and
        the "YAxis" of the plane used to parametrize the plane.
        """

    @overload
    def __init__(self, theP: gp_Pnt, theV: gp_Dir) -> None:
        """
        Creates a plane with the "Location" point <theP>
        and the normal direction <theV>.
        """

    @overload
    def __init__(self, theA: float, theB: float, theC: float, theD: float) -> None:
        """
        Creates a plane from its cartesian equation :
        @code
        theA * X + theB * Y + theC * Z + theD = 0.0
        @endcode
        Raises ConstructionError if std::sqrt (theA*theA + theB*theB + theC*theC) <= Resolution from
        gp.
        """

    @overload
    def __init__(self, theOther: gp_Pln) -> None: ...

    @overload
    def __init__(self, theFrom: nanoocp.gce.gce_MakePln) -> None: ...

    def Coefficients(self) -> tuple[float, float, float, float]:
        """
        Returns the coefficients of the plane's cartesian equation:
        @code
        theA * X + theB * Y + theC * Z + theD = 0.
        @endcode
        """

    def SetAxis(self, theA1: gp_Ax1) -> None:
        """
        Modifies this plane, by redefining its local coordinate system so that
        -   its origin and "main Direction" become those of the
        axis theA1 (the "X Direction" and "Y Direction" are then recomputed).
        Raises ConstructionError if the theA1 is parallel to the "XAxis" of the plane.
        """

    def SetLocation(self, theLoc: gp_Pnt) -> None:
        """Changes the origin of the plane."""

    def SetPosition(self, theA3: gp_Ax3) -> None:
        """Changes the local coordinate system of the plane."""

    def UReverse(self) -> None:
        """
        Reverses the U parametrization of the plane
        reversing the XAxis.
        """

    def VReverse(self) -> None:
        """
        Reverses the V parametrization of the plane
        reversing the YAxis.
        """

    def Direct(self) -> bool:
        """Returns true if the Ax3 is right handed."""

    def Axis(self) -> gp_Ax1:
        """Returns the plane's normal Axis."""

    def Location(self) -> gp_Pnt:
        """Returns the plane's location (origin)."""

    def Position(self) -> gp_Ax3:
        """Returns the local coordinate system of the plane."""

    @overload
    def Distance(self, theP: gp_Pnt) -> float:
        """Computes the distance between <me> and the point <theP>."""

    @overload
    def Distance(self, theL: gp_Lin) -> float:
        """Computes the distance between <me> and the line <theL>."""

    @overload
    def Distance(self, theOther: gp_Pln) -> float:
        """Computes the distance between two planes."""

    @overload
    def SignedDistance(self, theP: gp_Pnt) -> float:
        """
        Computes the signed distance between <me> and the point <theP>.
        The sign of the distance indicates on which side of the plane the point is located:
        - positive sign: the point is located in the direction of the plane normal,
        - negative sign: the point is located in the opposite direction to the plane normal,
        - zero: the point is located on the plane.
        """

    @overload
    def SignedDistance(self, theL: gp_Lin) -> float:
        """
        Computes the signed distance between <me> and the line <theL>.
        The sign of the distance indicates on which side of the plane the line is located:
        - positive sign: the line is located in the direction of the plane normal,
        - negative sign: the line is located in the opposite direction to the plane normal,
        - zero: the line intersects the plane.
        """

    @overload
    def SignedDistance(self, theOther: gp_Pln) -> float:
        """
        Computes the signed distance between two planes.
        The sign of the distance indicates on which side of <me> the other plane is located:
        - positive sign: the other plane is located in the direction of the plane normal,
        - negative sign: the other plane is located in the opposite direction to the plane normal,
        - zero: the planes intersect.
        """

    @overload
    def SquareDistance(self, theP: gp_Pnt) -> float:
        """Computes the square distance between <me> and the point <theP>."""

    @overload
    def SquareDistance(self, theL: gp_Lin) -> float:
        """Computes the square distance between <me> and the line <theL>."""

    @overload
    def SquareDistance(self, theOther: gp_Pln) -> float:
        """Computes the square distance between two planes."""

    def XAxis(self) -> gp_Ax1:
        """Returns the X axis of the plane."""

    def YAxis(self) -> gp_Ax1:
        """Returns the Y axis of the plane."""

    @overload
    def Contains(self, theP: gp_Pnt, theLinearTolerance: float) -> bool:
        """
        Returns true if this plane contains the point theP. This means that
        -   the distance between point theP and this plane is less
        than or equal to theLinearTolerance, or
        -   line L is normal to the "main Axis" of the local
        coordinate system of this plane, within the tolerance
        AngularTolerance, and the distance between the origin
        of line L and this plane is less than or equal to
        theLinearTolerance.
        """

    @overload
    def Contains(self, theL: gp_Lin, theLinearTolerance: float, theAngularTolerance: float) -> bool:
        """
        Returns true if this plane contains the line theL. This means that
        -   the distance between point P and this plane is less
        than or equal to LinearTolerance, or
        -   line theL is normal to the "main Axis" of the local
        coordinate system of this plane, within the tolerance
        theAngularTolerance, and the distance between the origin
        of line theL and this plane is less than or equal to
        theLinearTolerance.
        """

    @overload
    def Mirror(self, theP: gp_Pnt) -> None: ...

    @overload
    def Mirror(self, theA1: gp_Ax1) -> None: ...

    @overload
    def Mirror(self, theA2: gp_Ax2) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt) -> gp_Pln:
        """
        Performs the symmetrical transformation of a plane with respect
        to the point <theP> which is the center of the symmetry
        Warnings :
        The normal direction to the plane is not changed.
        The "XAxis" and the "YAxis" are reversed.
        """

    @overload
    def Mirrored(self, theA1: gp_Ax1) -> gp_Pln:
        """
        Performs the symmetrical transformation of a plane with
        respect to an axis placement which is the axis of the
        symmetry. The transformation is performed on the "Location"
        point, on the "XAxis" and the "YAxis". The resulting normal
        direction is the cross product between the "XDirection" and
        the "YDirection" after transformation if the initial plane
        was right handed, else it is the opposite.
        """

    @overload
    def Mirrored(self, theA2: gp_Ax2) -> gp_Pln:
        """
        Performs the symmetrical transformation of a plane with
        respect to an axis placement. The axis placement <A2>
        locates the plane of the symmetry. The transformation is
        performed on the "Location" point, on the "XAxis" and the
        "YAxis". The resulting normal direction is the cross product
        between the "XDirection" and the "YDirection" after
        transformation if the initial plane was right handed,
        else it is the opposite.
        """

    def Rotate(self, theA1: gp_Ax1, theAng: float) -> None: ...

    def Rotated(self, theA1: gp_Ax1, theAng: float) -> gp_Pln:
        """
        Rotates a plane. theA1 is the axis of the rotation.
        theAng is the angular value of the rotation in radians.
        """

    def Scale(self, theP: gp_Pnt, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt, theS: float) -> gp_Pln:
        """Scales a plane. theS is the scaling value."""

    def Transform(self, theT: gp_Trsf) -> None: ...

    def Transformed(self, theT: gp_Trsf) -> gp_Pln:
        """
        Transforms a plane with the transformation theT from class Trsf.
        The transformation is performed on the "Location"
        point, on the "XAxis" and the "YAxis".
        The resulting normal direction is the cross product between
        the "XDirection" and the "YDirection" after transformation.
        """

    @overload
    def Translate(self, theV: gp_Vec) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec) -> gp_Pln:
        """
        Translates a plane in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt, theP2: gp_Pnt) -> gp_Pln:
        """Translates a plane from the point theP1 to the point theP2."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class gp_Quaternion:
    """
    Represents operation of rotation in 3d space as quaternion
    and implements operations with rotations basing on
    quaternion mathematics.

    In addition, provides methods for conversion to and from other
    representations of rotation (3*3 matrix, vector and
    angle, Euler angles)
    """

    @overload
    def __init__(self) -> None:
        """Creates an identity quaternion"""

    @overload
    def __init__(self, theMat: gp_Mat) -> None:
        """
        Creates quaternion from rotation matrix 3*3
        (which should be orthonormal skew-symmetric matrix)
        """

    @overload
    def __init__(self, theVecFrom: gp_Vec, theVecTo: gp_Vec) -> None:
        """
        Creates quaternion representing shortest-arc rotation
        operator producing vector theVecTo from vector theVecFrom.
        """

    @overload
    def __init__(self, theAxis: gp_Vec, theAngle: float) -> None:
        """
        Creates quaternion representing rotation on angle
        theAngle around vector theAxis
        """

    @overload
    def __init__(self, theVecFrom: gp_Vec, theVecTo: gp_Vec, theHelpCrossVec: gp_Vec) -> None:
        """
        Creates quaternion representing shortest-arc rotation
        operator producing vector theVecTo from vector theVecFrom.
        Additional vector theHelpCrossVec defines preferred direction for
        rotation and is used when theVecTo and theVecFrom are directed
        oppositely.
        """

    @overload
    def __init__(self, theX: float, theY: float, theZ: float, theW: float) -> None:
        """Creates quaternion directly from component values"""

    @overload
    def __init__(self, theOther: gp_Quaternion) -> None: ...

    def IsEqual(self, theOther: gp_Quaternion) -> bool:
        """Simple equal test without precision"""

    @overload
    def SetRotation(self, theVecFrom: gp_Vec, theVecTo: gp_Vec) -> None:
        """
        Sets quaternion to shortest-arc rotation producing
        vector theVecTo from vector theVecFrom.
        If vectors theVecFrom and theVecTo are opposite then rotation
        axis is computed as theVecFrom ^ (1,0,0) or theVecFrom ^ (0,0,1).
        """

    @overload
    def SetRotation(self, theVecFrom: gp_Vec, theVecTo: gp_Vec, theHelpCrossVec: gp_Vec) -> None:
        """
        Sets quaternion to shortest-arc rotation producing
        vector theVecTo from vector theVecFrom.
        If vectors theVecFrom and theVecTo are opposite then rotation
        axis is computed as theVecFrom ^ theHelpCrossVec.
        """

    def SetVectorAndAngle(self, theAxis: gp_Vec, theAngle: float) -> None:
        """Create a unit quaternion from Axis+Angle representation"""

    def GetVectorAndAngle(self, theAxis: gp_Vec) -> float:
        """
        Convert a quaternion to Axis+Angle representation,
        preserve the axis direction and angle from -PI to +PI
        """

    def SetMatrix(self, theMat: gp_Mat) -> None:
        """
        Create a unit quaternion by rotation matrix
        matrix must contain only rotation (not scale or shear)

        For numerical stability we find first the greatest component of quaternion
        and than search others from this one
        """

    def GetMatrix(self) -> gp_Mat:
        """Returns rotation operation as 3*3 matrix"""

    def SetEulerAngles(self, theOrder: gp_EulerSequence, theAlpha: float, theBeta: float, theGamma: float) -> None:
        """
        Create a unit quaternion representing rotation defined
        by generalized Euler angles
        """

    def GetEulerAngles(self, theOrder: gp_EulerSequence) -> tuple[float, float, float]:
        """Returns Euler angles describing current rotation"""

    @overload
    def Set(self, theX: float, theY: float, theZ: float, theW: float) -> None: ...

    @overload
    def Set(self, theQuaternion: gp_Quaternion) -> None: ...

    def X(self) -> float: ...

    def Y(self) -> float: ...

    def Z(self) -> float: ...

    def W(self) -> float: ...

    def SetIdent(self) -> None:
        """Make identity quaternion (zero-rotation)"""

    def Reverse(self) -> None:
        """Reverse direction of rotation (conjugate quaternion)"""

    def Reversed(self) -> gp_Quaternion:
        """Return rotation with reversed direction (conjugated quaternion)"""

    def Invert(self) -> None:
        """Inverts quaternion (both rotation direction and norm)"""

    def Inverted(self) -> gp_Quaternion:
        """Return inversed quaternion q^-1"""

    def SquareNorm(self) -> float:
        """Returns square norm of quaternion"""

    def Norm(self) -> float:
        """Returns norm of quaternion"""

    def Scale(self, theScale: float) -> None:
        """
        Scale all components by quaternion by theScale; note that
        rotation is not changed by this operation (except 0-scaling)
        """

    @overload
    def __imul__(self, theScale: float) -> gp_Quaternion: ...

    @overload
    def __imul__(self, theOther: gp_Quaternion) -> gp_Quaternion: ...

    def Scaled(self, theScale: float) -> gp_Quaternion:
        """Returns scaled quaternion"""

    @overload
    def __mul__(self, theScale: float) -> gp_Quaternion: ...

    @overload
    def __mul__(self, theOther: gp_Quaternion) -> gp_Quaternion: ...

    @overload
    def __mul__(self, theVec: gp_Vec) -> gp_Vec: ...

    def StabilizeLength(self) -> None:
        """
        Stabilize quaternion length within 1 - 1/4.
        This operation is a lot faster than normalization
        and preserve length goes to 0 or infinity
        """

    def Normalize(self) -> None:
        """
        Scale quaternion that its norm goes to 1.
        The appearing of 0 magnitude or near is a error,
        so we can be sure that can divide by magnitude
        """

    def Normalized(self) -> gp_Quaternion:
        """Returns quaternion scaled so that its norm goes to 1."""

    def Negated(self) -> gp_Quaternion:
        """
        Returns quaternion with all components negated.
        Note that this operation does not affect neither
        rotation operator defined by quaternion nor its norm.
        """

    def __neg__(self) -> gp_Quaternion: ...

    def Added(self, theOther: gp_Quaternion) -> gp_Quaternion:
        """Makes sum of quaternion components; result is "rotations mix\""""

    def __add__(self, theOther: gp_Quaternion) -> gp_Quaternion: ...

    def Subtracted(self, theOther: gp_Quaternion) -> gp_Quaternion:
        """Makes difference of quaternion components; result is "rotations mix\""""

    def __sub__(self, theOther: gp_Quaternion) -> gp_Quaternion: ...

    def Multiplied(self, theOther: gp_Quaternion) -> gp_Quaternion:
        """
        Multiply function - work the same as Matrices multiplying.
        @code
        qq' = (cross(v,v') + wv' + w'v, ww' - dot(v,v'))
        @endcode
        Result is rotation combination: q' than q (here q=this, q'=theQ).
        Notices that:
        @code
        qq' != q'q;
        qq^-1 = q;
        @endcode
        """

    def Add(self, theOther: gp_Quaternion) -> None:
        """Adds components of other quaternion; result is "rotations mix\""""

    def __iadd__(self, theOther: gp_Quaternion) -> gp_Quaternion: ...

    def Subtract(self, theOther: gp_Quaternion) -> None:
        """Subtracts components of other quaternion; result is "rotations mix\""""

    def __isub__(self, theOther: gp_Quaternion) -> gp_Quaternion: ...

    @overload
    def Multiply(self, theOther: gp_Quaternion) -> None:
        """Adds rotation by multiplication"""

    @overload
    def Multiply(self, theVec: gp_Vec) -> gp_Vec:
        """Rotates vector by quaternion as rotation operator"""

    def Dot(self, theOther: gp_Quaternion) -> float:
        """Computes inner product / scalar product / Dot"""

    def GetRotationAngle(self) -> float:
        """Return rotation angle from -PI to PI"""

class gp_QuaternionNLerp:
    """
    Class perform linear interpolation (approximate rotation interpolation),
    result quaternion nonunit, its length lay between. sqrt(2)/2 and 1.0
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor,"""

    @overload
    def __init__(self, theQStart: gp_Quaternion, theQEnd: gp_Quaternion) -> None:
        """Constructor with initialization."""

    @overload
    def __init__(self, theOther: gp_QuaternionNLerp) -> None: ...

    @staticmethod
    def Interpolate_s(theQStart: gp_Quaternion, theQEnd: gp_Quaternion, theT: float) -> gp_Quaternion:
        """
        Compute interpolated quaternion between two quaternions.
        @param theStart first  quaternion
        @param theEnd   second quaternion
        @param theT normalized interpolation coefficient within 0..1 range,
        with 0 pointing to theStart and 1 to theEnd.
        """

    def Init(self, theQStart: gp_Quaternion, theQEnd: gp_Quaternion) -> None:
        """Initialize the tool with Start and End values."""

    def InitFromUnit(self, theQStart: gp_Quaternion, theQEnd: gp_Quaternion) -> None:
        """Initialize the tool with Start and End unit quaternions."""

    def Interpolate(self, theT: float, theResultQ: gp_Quaternion) -> None:
        """Set interpolated quaternion for theT position (from 0.0 to 1.0)"""

class gp_QuaternionSLerp:
    """
    Perform Spherical Linear Interpolation of the quaternions,
    return unit length quaternion.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor,"""

    @overload
    def __init__(self, theQStart: gp_Quaternion, theQEnd: gp_Quaternion) -> None:
        """Constructor with initialization."""

    @overload
    def __init__(self, theOther: gp_QuaternionSLerp) -> None: ...

    @staticmethod
    def Interpolate_s(theQStart: gp_Quaternion, theQEnd: gp_Quaternion, theT: float) -> gp_Quaternion:
        """
        Compute interpolated quaternion between two quaternions.
        @param theStart first  quaternion
        @param theEnd   second quaternion
        @param theT normalized interpolation coefficient within 0..1 range,
        with 0 pointing to theStart and 1 to theEnd.
        """

    def Init(self, theQStart: gp_Quaternion, theQEnd: gp_Quaternion) -> None:
        """Initialize the tool with Start and End values."""

    def InitFromUnit(self, theQStart: gp_Quaternion, theQEnd: gp_Quaternion) -> None:
        """Initialize the tool with Start and End unit quaternions."""

    def Interpolate(self, theT: float, theResultQ: gp_Quaternion) -> None:
        """Set interpolated quaternion for theT position (from 0.0 to 1.0)"""

class gp_Sphere:
    """
    Describes a sphere.
    A sphere is defined by its radius and positioned in space
    with a coordinate system (a gp_Ax3 object). The origin of
    the coordinate system is the center of the sphere. This
    coordinate system is the "local coordinate system" of the sphere.
    Note: when a gp_Sphere sphere is converted into a
    Geom_SphericalSurface sphere, some implicit
    properties of its local coordinate system are used explicitly:
    -   its origin, "X Direction", "Y Direction" and "main
    Direction" are used directly to define the parametric
    directions on the sphere and the origin of the parameters,
    -   its implicit orientation (right-handed or left-handed)
    gives the orientation (direct, indirect) to the
    Geom_SphericalSurface sphere.
    See Also
    gce_MakeSphere which provides functions for more
    complex sphere constructions
    Geom_SphericalSurface which provides additional
    functions for constructing spheres and works, in
    particular, with the parametric equations of spheres.
    """

    @overload
    def __init__(self) -> None:
        """Creates an indefinite sphere."""

    @overload
    def __init__(self, theA3: gp_Ax3, theRadius: float) -> None:
        """
        Constructs a sphere with radius theRadius, centered on the origin
        of theA3. theA3 is the local coordinate system of the sphere.
        Warnings:
        It is not forbidden to create a sphere with null radius.
        Raises ConstructionError if theRadius < 0.0
        """

    @overload
    def __init__(self, theOther: gp_Sphere) -> None: ...

    def SetLocation(self, theLoc: gp_Pnt) -> None:
        """Changes the center of the sphere."""

    def SetPosition(self, theA3: gp_Ax3) -> None:
        """Changes the local coordinate system of the sphere."""

    def SetRadius(self, theR: float) -> None:
        """
        Assigns theR the radius of the Sphere.
        Warnings :
        It is not forbidden to create a sphere with null radius.
        Raises ConstructionError if theR < 0.0
        """

    def Area(self) -> float:
        """Computes the area of the sphere."""

    def Coefficients(self) -> tuple[float, float, float, float, float, float, float, float, float, float]:
        """
        Computes the coefficients of the implicit equation of the quadric
        in the absolute cartesian coordinates system :
        @code
        theA1.X**2 + theA2.Y**2 + theA3.Z**2 + 2.(theB1.X.Y + theB2.X.Z + theB3.Y.Z) +
        2.(theC1.X + theC2.Y + theC3.Z) + theD = 0.0
        @endcode
        """

    def UReverse(self) -> None:
        """
        Reverses the U parametrization of the sphere
        reversing the YAxis.
        """

    def VReverse(self) -> None:
        """
        Reverses the V parametrization of the sphere
        reversing the ZAxis.
        """

    def Direct(self) -> bool:
        """
        Returns true if the local coordinate system of this sphere
        is right-handed.
        """

    def Location(self) -> gp_Pnt:
        """
        --- Purpose ;
        Returns the center of the sphere.
        """

    def Position(self) -> gp_Ax3:
        """Returns the local coordinates system of the sphere."""

    def Radius(self) -> float:
        """Returns the radius of the sphere."""

    def Volume(self) -> float:
        """Computes the volume of the sphere"""

    def XAxis(self) -> gp_Ax1:
        """Returns the axis X of the sphere."""

    def YAxis(self) -> gp_Ax1:
        """Returns the axis Y of the sphere."""

    @overload
    def Mirror(self, theP: gp_Pnt) -> None: ...

    @overload
    def Mirror(self, theA1: gp_Ax1) -> None: ...

    @overload
    def Mirror(self, theA2: gp_Ax2) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt) -> gp_Sphere:
        """
        Performs the symmetrical transformation of a sphere
        with respect to the point theP which is the center of the
        symmetry.
        """

    @overload
    def Mirrored(self, theA1: gp_Ax1) -> gp_Sphere:
        """
        Performs the symmetrical transformation of a sphere with
        respect to an axis placement which is the axis of the
        symmetry.
        """

    @overload
    def Mirrored(self, theA2: gp_Ax2) -> gp_Sphere:
        """
        Performs the symmetrical transformation of a sphere with respect
        to a plane. The axis placement theA2 locates the plane of the
        of the symmetry : (Location, XDirection, YDirection).
        """

    def Rotate(self, theA1: gp_Ax1, theAng: float) -> None: ...

    def Rotated(self, theA1: gp_Ax1, theAng: float) -> gp_Sphere:
        """
        Rotates a sphere. theA1 is the axis of the rotation.
        theAng is the angular value of the rotation in radians.
        """

    def Scale(self, theP: gp_Pnt, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt, theS: float) -> gp_Sphere:
        """
        Scales a sphere. theS is the scaling value.
        The absolute value of S is used to scale the sphere
        """

    def Transform(self, theT: gp_Trsf) -> None: ...

    def Transformed(self, theT: gp_Trsf) -> gp_Sphere:
        """Transforms a sphere with the transformation theT from class Trsf."""

    @overload
    def Translate(self, theV: gp_Vec) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec) -> gp_Sphere:
        """
        Translates a sphere in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt, theP2: gp_Pnt) -> gp_Sphere:
        """Translates a sphere from the point theP1 to the point theP2."""

class gp_Torus:
    """
    Describes a torus.
    A torus is defined by its major and minor radii and
    positioned in space with a coordinate system (a gp_Ax3
    object) as follows:
    -   The origin of the coordinate system is the center of the torus;
    -   The surface is obtained by rotating a circle of radius
    equal to the minor radius of the torus about the "main
    Direction" of the coordinate system. This circle is
    located in the plane defined by the origin, the "X
    Direction" and the "main Direction" of the coordinate
    system. It is centered on the "X Axis" of this coordinate
    system, and located at a distance, from the origin of
    this coordinate system, equal to the major radius of the torus;
    -   The "X Direction" and "Y Direction" define the
    reference plane of the torus.
    The coordinate system described above is the "local
    coordinate system" of the torus.
    Note: when a gp_Torus torus is converted into a
    Geom_ToroidalSurface torus, some implicit properties
    of its local coordinate system are used explicitly:
    -   its origin, "X Direction", "Y Direction" and "main
    Direction" are used directly to define the parametric
    directions on the torus and the origin of the parameters,
    -   its implicit orientation (right-handed or left-handed)
    gives the orientation (direct, indirect) to the
    Geom_ToroidalSurface torus.
    See Also
    gce_MakeTorus which provides functions for more
    complex torus constructions
    Geom_ToroidalSurface which provides additional
    functions for constructing tori and works, in particular,
    with the parametric equations of tori.
    """

    @overload
    def __init__(self) -> None:
        """creates an indefinite Torus."""

    @overload
    def __init__(self, theA3: gp_Ax3, theMajorRadius: float, theMinorRadius: float) -> None:
        """
        a torus centered on the origin of coordinate system
        theA3, with major radius theMajorRadius and minor radius
        theMinorRadius, and with the reference plane defined
        by the origin, the "X Direction" and the "Y Direction" of theA3.
        Warnings :
        It is not forbidden to create a torus with
        theMajorRadius = theMinorRadius = 0.0
        Raises ConstructionError if theMinorRadius < 0.0 or if theMajorRadius < 0.0
        """

    @overload
    def __init__(self, theOther: gp_Torus) -> None: ...

    def SetAxis(self, theA1: gp_Ax1) -> None:
        """
        Modifies this torus, by redefining its local coordinate
        system so that:
        -   its origin and "main Direction" become those of the
        axis theA1 (the "X Direction" and "Y Direction" are then recomputed).
        Raises ConstructionError if the direction of theA1 is parallel to the "XDirection"
        of the coordinate system of the toroidal surface.
        """

    def SetLocation(self, theLoc: gp_Pnt) -> None:
        """Changes the location of the torus."""

    def SetMajorRadius(self, theMajorRadius: float) -> None:
        """
        Assigns value to the major radius of this torus.
        Raises ConstructionError if theMajorRadius - MinorRadius <= Resolution()
        """

    def SetMinorRadius(self, theMinorRadius: float) -> None:
        """
        Assigns value to the minor radius of this torus.
        Raises ConstructionError if theMinorRadius < 0.0 or if
        MajorRadius - theMinorRadius <= Resolution from gp.
        """

    def SetPosition(self, theA3: gp_Ax3) -> None:
        """Changes the local coordinate system of the surface."""

    def Area(self) -> float:
        """Computes the area of the torus."""

    def UReverse(self) -> None:
        """
        Reverses the U parametrization of the torus
        reversing the YAxis.
        """

    def VReverse(self) -> None:
        """
        Reverses the V parametrization of the torus
        reversing the ZAxis.
        """

    def Direct(self) -> bool:
        """
        returns true if the Ax3, the local coordinate system of this torus, is right handed.
        """

    def Axis(self) -> gp_Ax1:
        """returns the symmetry axis of the torus."""

    def Coefficients(self, theCoef: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Computes the coefficients of the implicit equation of the surface
        in the absolute Cartesian coordinate system:
        @code
        Coef(1) * X^4 + Coef(2) * Y^4 + Coef(3) * Z^4 +
        Coef(4) * X^3 * Y + Coef(5) * X^3 * Z + Coef(6) * Y^3 * X +
        Coef(7) * Y^3 * Z + Coef(8) * Z^3 * X + Coef(9) * Z^3 * Y +
        Coef(10) * X^2 * Y^2 + Coef(11) * X^2 * Z^2 +
        Coef(12) * Y^2 * Z^2 + Coef(13) * X^2 * Y * Z +
        Coef(14) * X * Y^2 * Z + Coef(15) * X * Y * Z^2 +
        Coef(16) * X^3 + Coef(17) * Y^3 + Coef(18) * Z^3 +
        Coef(19) * X^2 * Y + Coef(20) * X^2 * Z + Coef(21) * Y^2 * X +
        Coef(22) * Y^2 * Z + Coef(23) * Z^2 * X + Coef(24) * Z^2 * Y +
        Coef(25) * X * Y * Z +
        Coef(26) * X^2 + Coef(27) * Y^2 + Coef(28) * Z^2 +
        Coef(29) * X * Y + Coef(30) * X * Z + Coef(31) * Y * Z +
        Coef(32) * X + Coef(33) * Y + Coef(34) * Z +
        Coef(35) = 0.0
        @endcode
        Raises DimensionError if the length of theCoef is lower than 35.
        """

    def Location(self) -> gp_Pnt:
        """Returns the Torus's location."""

    def Position(self) -> gp_Ax3:
        """Returns the local coordinates system of the torus."""

    def MajorRadius(self) -> float:
        """returns the major radius of the torus."""

    def MinorRadius(self) -> float:
        """returns the minor radius of the torus."""

    def Volume(self) -> float:
        """Computes the volume of the torus."""

    def XAxis(self) -> gp_Ax1:
        """returns the axis X of the torus."""

    def YAxis(self) -> gp_Ax1:
        """returns the axis Y of the torus."""

    @overload
    def Mirror(self, theP: gp_Pnt) -> None: ...

    @overload
    def Mirror(self, theA1: gp_Ax1) -> None: ...

    @overload
    def Mirror(self, theA2: gp_Ax2) -> None: ...

    @overload
    def Mirrored(self, theP: gp_Pnt) -> gp_Torus:
        """
        Performs the symmetrical transformation of a torus
        with respect to the point theP which is the center of the
        symmetry.
        """

    @overload
    def Mirrored(self, theA1: gp_Ax1) -> gp_Torus:
        """
        Performs the symmetrical transformation of a torus with
        respect to an axis placement which is the axis of the
        symmetry.
        """

    @overload
    def Mirrored(self, theA2: gp_Ax2) -> gp_Torus:
        """
        Performs the symmetrical transformation of a torus with respect
        to a plane. The axis placement theA2 locates the plane of the
        of the symmetry : (Location, XDirection, YDirection).
        """

    def Rotate(self, theA1: gp_Ax1, theAng: float) -> None: ...

    def Rotated(self, theA1: gp_Ax1, theAng: float) -> gp_Torus:
        """
        Rotates a torus. theA1 is the axis of the rotation.
        theAng is the angular value of the rotation in radians.
        """

    def Scale(self, theP: gp_Pnt, theS: float) -> None: ...

    def Scaled(self, theP: gp_Pnt, theS: float) -> gp_Torus:
        """
        Scales a torus. S is the scaling value.
        The absolute value of S is used to scale the torus
        """

    def Transform(self, theT: gp_Trsf) -> None: ...

    def Transformed(self, theT: gp_Trsf) -> gp_Torus:
        """Transforms a torus with the transformation theT from class Trsf."""

    @overload
    def Translate(self, theV: gp_Vec) -> None: ...

    @overload
    def Translate(self, theP1: gp_Pnt, theP2: gp_Pnt) -> None: ...

    @overload
    def Translated(self, theV: gp_Vec) -> gp_Torus:
        """
        Translates a torus in the direction of the vector theV.
        The magnitude of the translation is the vector's magnitude.
        """

    @overload
    def Translated(self, theP1: gp_Pnt, theP2: gp_Pnt) -> gp_Torus:
        """Translates a torus from the point theP1 to the point theP2."""

class NCollection_Lerp__gp_Trsf:
    """
    Linear interpolation tool for transformation defined by gp_Trsf.

    In general case, there is a no well-defined interpolation between arbitrary transformations,
    because desired transient values might vary depending on application needs.

    This tool performs independent interpolation of three logical
    transformation parts - rotation (using gp_QuaternionNLerp), translation and scale factor.
    Result of such interpolation might be not what application expects,
    thus this tool might be considered for simple cases or for interpolating between small
    intervals.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theStart: gp_Trsf, theEnd: gp_Trsf) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: NCollection_Lerp__gp_Trsf) -> None: ...

    def Init(self, theStart: gp_Trsf, theEnd: gp_Trsf) -> None:
        """Initialize values."""

    def Interpolate(self, theT: float, theResult: gp_Trsf) -> None:
        """
        Compute interpolated value between two values.
        @param theT normalized interpolation coefficient within [0, 1] range,
        with 0 pointing to first value and 1 to the second value.
        @param[out] theResult  interpolated value
        """

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.Poly
import nanoocp.Quantity
gp_Vec2f = nanoocp.Poly.NCollection_Vec2__float
gp_Vec3f = nanoocp.Quantity.NCollection_Vec3__float
