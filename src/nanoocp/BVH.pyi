"""OCCT package BVH (toolkit TKMath)"""

from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.BVH


THE_NODE_MIN_SIZE: float = 1e-05

THE_MORTON_LUT: int = 0

BVH_Constants_MaxTreeDepth: int = 32

BVH_Constants_LeafNodeSizeSingle: int = 1

BVH_Constants_LeafNodeSizeAverage: int = 4

BVH_Constants_LeafNodeSizeDefault: int = 5

BVH_Constants_LeafNodeSizeSmall: int = 8

BVH_Constants_NbBinsOptimal: int = 32

BVH_Constants_NbBinsBest: int = 48

class BVH_Vec2i:
    """
    Defines the 2D-vector template.
    The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor. Construct the zero vector."""

    @overload
    def __init__(self, theXY: int) -> None:
        """Initialize ALL components of vector within specified value."""

    @overload
    def __init__(self, theX: int, theY: int) -> None:
        """Per-component constructor."""

    @overload
    def __init__(self, theOther: BVH_Vec2i) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    def SetValues(self, theX: int, theY: int) -> None:
        """Assign new values to the vector."""

    @overload
    def x(self) -> int: ...

    @overload
    def x(self) -> int:
        """Alias to 1st component as X coordinate in XY."""

    @overload
    def y(self) -> int: ...

    @overload
    def y(self) -> int:
        """Alias to 2nd component as Y coordinate in XY."""

    def xy(self) -> BVH_Vec2i:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def yx(self) -> BVH_Vec2i:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def Setx(self, theValue: int) -> None:
        """Python addition: sets the value x() returns by reference in C++."""

    def Sety(self, theValue: int) -> None:
        """Python addition: sets the value y() returns by reference in C++."""

    def IsEqual(self, theOther: BVH_Vec2i) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __eq__(self, theOther: BVH_Vec2i) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __ne__(self, theOther: BVH_Vec2i) -> bool:
        """
        Check this vector with another vector for non-equality (without tolerance!).
        """

    def __iadd__(self, theAdd: BVH_Vec2i) -> BVH_Vec2i:
        """Compute per-component summary."""

    def __isub__(self, theDec: BVH_Vec2i) -> BVH_Vec2i:
        """Compute per-component subtraction."""

    def __neg__(self) -> BVH_Vec2i:
        """Unary -."""

    @overload
    def __imul__(self, theRight: BVH_Vec2i) -> BVH_Vec2i:
        """Compute per-component multiplication."""

    @overload
    def __imul__(self, theFactor: int) -> BVH_Vec2i:
        """Compute per-component multiplication by scale factor."""

    def Multiply(self, theFactor: int) -> None:
        """Compute per-component multiplication by scale factor."""

    def Multiplied(self, theFactor: int) -> BVH_Vec2i:
        """Compute per-component multiplication by scale factor."""

    def cwiseMin(self, theVec: BVH_Vec2i) -> BVH_Vec2i:
        """Compute component-wise minimum of two vectors."""

    def cwiseMax(self, theVec: BVH_Vec2i) -> BVH_Vec2i:
        """Compute component-wise maximum of two vectors."""

    def cwiseAbs(self) -> BVH_Vec2i:
        """Compute component-wise modulus of the vector."""

    def maxComp(self) -> int:
        """Compute maximum component of the vector."""

    def minComp(self) -> int:
        """Compute minimum component of the vector."""

    @overload
    def __itruediv__(self, theInvFactor: int) -> BVH_Vec2i:
        """Compute per-component division by scale factor."""

    @overload
    def __itruediv__(self, theRight: BVH_Vec2i) -> BVH_Vec2i:
        """Compute per-component division."""

    def __mul__(self, theFactor: int) -> BVH_Vec2i:
        """Compute per-component multiplication by scale factor."""

    def __truediv__(self, theInvFactor: int) -> BVH_Vec2i:
        """Compute per-component division by scale factor."""

    def Dot(self, theOther: BVH_Vec2i) -> int:
        """Computes the dot product."""

    def Modulus(self) -> int:
        """Computes the vector modulus (magnitude, length)."""

    def SquareModulus(self) -> int:
        """
        Computes the square of vector modulus (magnitude, length).
        This method may be used for performance tricks.
        """

    @staticmethod
    def DX() -> BVH_Vec2i:
        """Construct DX unit vector."""

    @staticmethod
    def DY() -> BVH_Vec2i:
        """Construct DY unit vector."""

class BVH_Vec3i:
    """
    Generic 3-components vector.
    To be used as RGB color pixel or XYZ 3D-point.
    The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor. Construct the zero vector."""

    @overload
    def __init__(self, theValue: int) -> None:
        """Initialize ALL components of vector within specified value."""

    @overload
    def __init__(self, theVec2: BVH_Vec2i, theZ: int = 0) -> None:
        """Constructor from 2-components vector + optional 3rd value."""

    @overload
    def __init__(self, theX: int, theY: int, theZ: int) -> None:
        """Per-component constructor."""

    @overload
    def __init__(self, theOther: BVH_Vec3i) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    @overload
    def SetValues(self, theX: int, theY: int, theZ: int) -> None: ...

    @overload
    def SetValues(self, theVec2: BVH_Vec2i, theZ: int) -> None:
        """Assign new values to the vector."""

    @overload
    def x(self) -> int: ...

    @overload
    def x(self) -> int:
        """Alias to 1st component as X coordinate in XYZ."""

    @overload
    def r(self) -> int: ...

    @overload
    def r(self) -> int:
        """Alias to 1st component as RED channel in RGB."""

    @overload
    def y(self) -> int: ...

    @overload
    def y(self) -> int:
        """Alias to 2nd component as Y coordinate in XYZ."""

    @overload
    def g(self) -> int: ...

    @overload
    def g(self) -> int:
        """Alias to 2nd component as GREEN channel in RGB."""

    @overload
    def z(self) -> int: ...

    @overload
    def z(self) -> int:
        """Alias to 3rd component as Z coordinate in XYZ."""

    @overload
    def b(self) -> int: ...

    @overload
    def b(self) -> int:
        """Alias to 3rd component as BLUE channel in RGB."""

    def xy(self) -> BVH_Vec2i:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def yx(self) -> BVH_Vec2i:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def xz(self) -> BVH_Vec2i:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def zx(self) -> BVH_Vec2i:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def yz(self) -> BVH_Vec2i:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def zy(self) -> BVH_Vec2i:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def xyz(self) -> BVH_Vec3i:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def xzy(self) -> BVH_Vec3i:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def yxz(self) -> BVH_Vec3i:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def yzx(self) -> BVH_Vec3i:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def zyx(self) -> BVH_Vec3i:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def zxy(self) -> BVH_Vec3i:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def Setx(self, theValue: int) -> None:
        """Python addition: sets the value x() returns by reference in C++."""

    def Setr(self, theValue: int) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def Sety(self, theValue: int) -> None:
        """Python addition: sets the value y() returns by reference in C++."""

    def Setg(self, theValue: int) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def Setz(self, theValue: int) -> None:
        """Python addition: sets the value z() returns by reference in C++."""

    def Setb(self, theValue: int) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    def IsEqual(self, theOther: BVH_Vec3i) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __eq__(self, theOther: BVH_Vec3i) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __ne__(self, theOther: BVH_Vec3i) -> bool:
        """
        Check this vector with another vector for non-equality (without tolerance!).
        """

    def __iadd__(self, theAdd: BVH_Vec3i) -> BVH_Vec3i:
        """Compute per-component summary."""

    def __neg__(self) -> BVH_Vec3i:
        """Unary -."""

    def __isub__(self, theDec: BVH_Vec3i) -> BVH_Vec3i:
        """Compute per-component subtraction."""

    def Multiply(self, theFactor: int) -> None:
        """Compute per-component multiplication by scale factor."""

    @overload
    def __imul__(self, theRight: BVH_Vec3i) -> BVH_Vec3i:
        """Compute per-component multiplication."""

    @overload
    def __imul__(self, theFactor: int) -> BVH_Vec3i:
        """Compute per-component multiplication by scale factor."""

    def __mul__(self, theFactor: int) -> BVH_Vec3i:
        """Compute per-component multiplication by scale factor."""

    def Multiplied(self, theFactor: int) -> BVH_Vec3i:
        """Compute per-component multiplication by scale factor."""

    def cwiseMin(self, theVec: BVH_Vec3i) -> BVH_Vec3i:
        """Compute component-wise minimum of two vectors."""

    def cwiseMax(self, theVec: BVH_Vec3i) -> BVH_Vec3i:
        """Compute component-wise maximum of two vectors."""

    def cwiseAbs(self) -> BVH_Vec3i:
        """Compute component-wise modulus of the vector."""

    def maxComp(self) -> int:
        """Compute maximum component of the vector."""

    def minComp(self) -> int:
        """Compute minimum component of the vector."""

    @overload
    def __itruediv__(self, theInvFactor: int) -> BVH_Vec3i:
        """Compute per-component division by scale factor."""

    @overload
    def __itruediv__(self, theRight: BVH_Vec3i) -> BVH_Vec3i:
        """Compute per-component division."""

    def __truediv__(self, theInvFactor: int) -> BVH_Vec3i:
        """Compute per-component division by scale factor."""

    def Dot(self, theOther: BVH_Vec3i) -> int:
        """Computes the dot product."""

    def Modulus(self) -> int:
        """Computes the vector modulus (magnitude, length)."""

    def SquareModulus(self) -> int:
        """
        Computes the square of vector modulus (magnitude, length).
        This method may be used for performance tricks.
        """

    def Normalize(self) -> None:
        """Normalize the vector."""

    def Normalized(self) -> BVH_Vec3i:
        """Normalize the vector."""

    @staticmethod
    def Cross(theVec1: BVH_Vec3i, theVec2: BVH_Vec3i) -> BVH_Vec3i:
        """Computes the cross product."""

    @staticmethod
    def GetLERP(theFrom: BVH_Vec3i, theTo: BVH_Vec3i, theT: int) -> BVH_Vec3i:
        """
        Compute linear interpolation between to vectors.
        @param theT - interpolation coefficient 0..1;
        @return interpolation result.
        """

    @staticmethod
    def DX() -> BVH_Vec3i:
        """Construct DX unit vector."""

    @staticmethod
    def DY() -> BVH_Vec3i:
        """Construct DY unit vector."""

    @staticmethod
    def DZ() -> BVH_Vec3i:
        """Construct DZ unit vector."""

class BVH_Vec4i:
    """
    Generic 4-components vector.
    To be used as RGBA color vector or XYZW 3D-point with special W-component
    for operations with projection / model view matrices.
    Use this class for 3D-points carefully because declared W-component may
    results in incorrect results if used without matrices.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor. Construct the zero vector."""

    @overload
    def __init__(self, theValue: int) -> None:
        """Initialize ALL components of vector within specified value."""

    @overload
    def __init__(self, theVec2: BVH_Vec2i) -> None:
        """Constructor from 2-components vector."""

    @overload
    def __init__(self, theVec3: BVH_Vec3i, theW: int = 0) -> None:
        """Constructor from 3-components vector + optional 4th value."""

    @overload
    def __init__(self, theX: int, theY: int, theZ: int, theW: int) -> None:
        """Per-component constructor."""

    @overload
    def __init__(self, theOther: BVH_Vec4i) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    @overload
    def SetValues(self, theX: int, theY: int, theZ: int, theW: int) -> None:
        """Assign new values to the vector."""

    @overload
    def SetValues(self, theVec3: BVH_Vec3i, theW: int) -> None:
        """Assign new values as 3-component vector and a 4-th value."""

    @overload
    def x(self) -> int: ...

    @overload
    def x(self) -> int:
        """Alias to 1st component as X coordinate in XYZW."""

    @overload
    def r(self) -> int: ...

    @overload
    def r(self) -> int:
        """Alias to 1st component as RED channel in RGBA."""

    @overload
    def y(self) -> int: ...

    @overload
    def y(self) -> int:
        """Alias to 2nd component as Y coordinate in XYZW."""

    @overload
    def g(self) -> int: ...

    @overload
    def g(self) -> int:
        """Alias to 2nd component as GREEN channel in RGBA."""

    @overload
    def z(self) -> int: ...

    @overload
    def z(self) -> int:
        """Alias to 3rd component as Z coordinate in XYZW."""

    @overload
    def b(self) -> int: ...

    @overload
    def b(self) -> int:
        """Alias to 3rd component as BLUE channel in RGBA."""

    @overload
    def w(self) -> int: ...

    @overload
    def w(self) -> int:
        """Alias to 4th component as W coordinate in XYZW."""

    @overload
    def a(self) -> int: ...

    @overload
    def a(self) -> int:
        """Alias to 4th component as ALPHA channel in RGBA."""

    def xy(self) -> BVH_Vec2i:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def yx(self) -> BVH_Vec2i:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def xz(self) -> BVH_Vec2i:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def zx(self) -> BVH_Vec2i:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def xw(self) -> BVH_Vec2i:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def wx(self) -> BVH_Vec2i:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def yz(self) -> BVH_Vec2i:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def zy(self) -> BVH_Vec2i:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def yw(self) -> BVH_Vec2i:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def wy(self) -> BVH_Vec2i:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def zw(self) -> BVH_Vec2i:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def wz(self) -> BVH_Vec2i:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def xyz(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xzy(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yxz(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yzx(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zyx(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zxy(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xyw(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xwy(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yxw(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def ywx(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wyx(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wxy(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xzw(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xwz(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zxw(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zwx(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wzx(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wxz(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yzw(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def ywz(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zyw(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zwy(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wzy(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wyz(self) -> BVH_Vec3i:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def rgb(self) -> BVH_Vec3i:
        """@return RGB components as vector"""

    def rbg(self) -> BVH_Vec3i:
        """@return RGB components as vector"""

    def grb(self) -> BVH_Vec3i:
        """@return RGB components as vector"""

    def gbr(self) -> BVH_Vec3i:
        """@return RGB components as vector"""

    def bgr(self) -> BVH_Vec3i:
        """@return RGB components as vector"""

    def brg(self) -> BVH_Vec3i:
        """@return RGB components as vector"""

    def Setx(self, theValue: int) -> None:
        """Python addition: sets the value x() returns by reference in C++."""

    def Setr(self, theValue: int) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def Sety(self, theValue: int) -> None:
        """Python addition: sets the value y() returns by reference in C++."""

    def Setg(self, theValue: int) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def Setz(self, theValue: int) -> None:
        """Python addition: sets the value z() returns by reference in C++."""

    def Setb(self, theValue: int) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    def Setw(self, theValue: int) -> None:
        """Python addition: sets the value w() returns by reference in C++."""

    def Seta(self, theValue: int) -> None:
        """Python addition: sets the value a() returns by reference in C++."""

    def IsEqual(self, theOther: BVH_Vec4i) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __eq__(self, theOther: BVH_Vec4i) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __ne__(self, theOther: BVH_Vec4i) -> bool:
        """
        Check this vector with another vector for non-equality (without tolerance!).
        """

    def __iadd__(self, theAdd: BVH_Vec4i) -> BVH_Vec4i:
        """Compute per-component summary."""

    def __neg__(self) -> BVH_Vec4i:
        """Unary -."""

    def __isub__(self, theDec: BVH_Vec4i) -> BVH_Vec4i:
        """Compute per-component subtraction."""

    @overload
    def __imul__(self, theRight: BVH_Vec4i) -> BVH_Vec4i: ...

    @overload
    def __imul__(self, theFactor: int) -> BVH_Vec4i:
        """Compute per-component multiplication."""

    def Multiply(self, theFactor: int) -> None:
        """Compute per-component multiplication."""

    def __mul__(self, theFactor: int) -> BVH_Vec4i:
        """Compute per-component multiplication."""

    def Multiplied(self, theFactor: int) -> BVH_Vec4i:
        """Compute per-component multiplication."""

    def cwiseMin(self, theVec: BVH_Vec4i) -> BVH_Vec4i:
        """Compute component-wise minimum of two vectors."""

    def cwiseMax(self, theVec: BVH_Vec4i) -> BVH_Vec4i:
        """Compute component-wise maximum of two vectors."""

    def cwiseAbs(self) -> BVH_Vec4i:
        """Compute component-wise modulus of the vector."""

    def maxComp(self) -> int:
        """Compute maximum component of the vector."""

    def minComp(self) -> int:
        """Compute minimum component of the vector."""

    def Dot(self, theOther: BVH_Vec4i) -> int:
        """Computes the dot product."""

    @overload
    def __itruediv__(self, theInvFactor: int) -> BVH_Vec4i:
        """Compute per-component division by scale factor."""

    @overload
    def __itruediv__(self, theRight: BVH_Vec4i) -> BVH_Vec4i:
        """Compute per-component division."""

    def __truediv__(self, theInvFactor: int) -> BVH_Vec4i:
        """Compute per-component division by scale factor."""

class BVH_Vec2f:
    """
    Defines the 2D-vector template.
    The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor. Construct the zero vector."""

    @overload
    def __init__(self, theXY: float) -> None:
        """Initialize ALL components of vector within specified value."""

    @overload
    def __init__(self, theX: float, theY: float) -> None:
        """Per-component constructor."""

    @overload
    def __init__(self, theOther: BVH_Vec2f) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    def SetValues(self, theX: float, theY: float) -> None:
        """Assign new values to the vector."""

    @overload
    def x(self) -> float: ...

    @overload
    def x(self) -> float:
        """Alias to 1st component as X coordinate in XY."""

    @overload
    def y(self) -> float: ...

    @overload
    def y(self) -> float:
        """Alias to 2nd component as Y coordinate in XY."""

    def xy(self) -> BVH_Vec2f:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def yx(self) -> BVH_Vec2f:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def Setx(self, theValue: float) -> None:
        """Python addition: sets the value x() returns by reference in C++."""

    def Sety(self, theValue: float) -> None:
        """Python addition: sets the value y() returns by reference in C++."""

    def IsEqual(self, theOther: BVH_Vec2f) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __eq__(self, theOther: BVH_Vec2f) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __ne__(self, theOther: BVH_Vec2f) -> bool:
        """
        Check this vector with another vector for non-equality (without tolerance!).
        """

    def __iadd__(self, theAdd: BVH_Vec2f) -> BVH_Vec2f:
        """Compute per-component summary."""

    def __isub__(self, theDec: BVH_Vec2f) -> BVH_Vec2f:
        """Compute per-component subtraction."""

    def __neg__(self) -> BVH_Vec2f:
        """Unary -."""

    @overload
    def __imul__(self, theRight: BVH_Vec2f) -> BVH_Vec2f:
        """Compute per-component multiplication."""

    @overload
    def __imul__(self, theFactor: float) -> BVH_Vec2f:
        """Compute per-component multiplication by scale factor."""

    def Multiply(self, theFactor: float) -> None:
        """Compute per-component multiplication by scale factor."""

    def Multiplied(self, theFactor: float) -> BVH_Vec2f:
        """Compute per-component multiplication by scale factor."""

    def cwiseMin(self, theVec: BVH_Vec2f) -> BVH_Vec2f:
        """Compute component-wise minimum of two vectors."""

    def cwiseMax(self, theVec: BVH_Vec2f) -> BVH_Vec2f:
        """Compute component-wise maximum of two vectors."""

    def cwiseAbs(self) -> BVH_Vec2f:
        """Compute component-wise modulus of the vector."""

    def maxComp(self) -> float:
        """Compute maximum component of the vector."""

    def minComp(self) -> float:
        """Compute minimum component of the vector."""

    @overload
    def __itruediv__(self, theInvFactor: float) -> BVH_Vec2f:
        """Compute per-component division by scale factor."""

    @overload
    def __itruediv__(self, theRight: BVH_Vec2f) -> BVH_Vec2f:
        """Compute per-component division."""

    def __mul__(self, theFactor: float) -> BVH_Vec2f:
        """Compute per-component multiplication by scale factor."""

    def __truediv__(self, theInvFactor: float) -> BVH_Vec2f:
        """Compute per-component division by scale factor."""

    def Dot(self, theOther: BVH_Vec2f) -> float:
        """Computes the dot product."""

    def Modulus(self) -> float:
        """Computes the vector modulus (magnitude, length)."""

    def SquareModulus(self) -> float:
        """
        Computes the square of vector modulus (magnitude, length).
        This method may be used for performance tricks.
        """

    @staticmethod
    def DX() -> BVH_Vec2f:
        """Construct DX unit vector."""

    @staticmethod
    def DY() -> BVH_Vec2f:
        """Construct DY unit vector."""

class BVH_Vec3f:
    """
    Generic 3-components vector.
    To be used as RGB color pixel or XYZ 3D-point.
    The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor. Construct the zero vector."""

    @overload
    def __init__(self, theValue: float) -> None:
        """Initialize ALL components of vector within specified value."""

    @overload
    def __init__(self, theVec2: BVH_Vec2f, theZ: float = 0.0) -> None:
        """Constructor from 2-components vector + optional 3rd value."""

    @overload
    def __init__(self, theX: float, theY: float, theZ: float) -> None:
        """Per-component constructor."""

    @overload
    def __init__(self, theOther: BVH_Vec3f) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    @overload
    def SetValues(self, theX: float, theY: float, theZ: float) -> None: ...

    @overload
    def SetValues(self, theVec2: BVH_Vec2f, theZ: float) -> None:
        """Assign new values to the vector."""

    @overload
    def x(self) -> float: ...

    @overload
    def x(self) -> float:
        """Alias to 1st component as X coordinate in XYZ."""

    @overload
    def r(self) -> float: ...

    @overload
    def r(self) -> float:
        """Alias to 1st component as RED channel in RGB."""

    @overload
    def y(self) -> float: ...

    @overload
    def y(self) -> float:
        """Alias to 2nd component as Y coordinate in XYZ."""

    @overload
    def g(self) -> float: ...

    @overload
    def g(self) -> float:
        """Alias to 2nd component as GREEN channel in RGB."""

    @overload
    def z(self) -> float: ...

    @overload
    def z(self) -> float:
        """Alias to 3rd component as Z coordinate in XYZ."""

    @overload
    def b(self) -> float: ...

    @overload
    def b(self) -> float:
        """Alias to 3rd component as BLUE channel in RGB."""

    def xy(self) -> BVH_Vec2f:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def yx(self) -> BVH_Vec2f:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def xz(self) -> BVH_Vec2f:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def zx(self) -> BVH_Vec2f:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def yz(self) -> BVH_Vec2f:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def zy(self) -> BVH_Vec2f:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def xyz(self) -> BVH_Vec3f:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def xzy(self) -> BVH_Vec3f:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def yxz(self) -> BVH_Vec3f:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def yzx(self) -> BVH_Vec3f:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def zyx(self) -> BVH_Vec3f:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def zxy(self) -> BVH_Vec3f:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def Setx(self, theValue: float) -> None:
        """Python addition: sets the value x() returns by reference in C++."""

    def Setr(self, theValue: float) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def Sety(self, theValue: float) -> None:
        """Python addition: sets the value y() returns by reference in C++."""

    def Setg(self, theValue: float) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def Setz(self, theValue: float) -> None:
        """Python addition: sets the value z() returns by reference in C++."""

    def Setb(self, theValue: float) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    def IsEqual(self, theOther: BVH_Vec3f) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __eq__(self, theOther: BVH_Vec3f) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __ne__(self, theOther: BVH_Vec3f) -> bool:
        """
        Check this vector with another vector for non-equality (without tolerance!).
        """

    def __iadd__(self, theAdd: BVH_Vec3f) -> BVH_Vec3f:
        """Compute per-component summary."""

    def __neg__(self) -> BVH_Vec3f:
        """Unary -."""

    def __isub__(self, theDec: BVH_Vec3f) -> BVH_Vec3f:
        """Compute per-component subtraction."""

    def Multiply(self, theFactor: float) -> None:
        """Compute per-component multiplication by scale factor."""

    @overload
    def __imul__(self, theRight: BVH_Vec3f) -> BVH_Vec3f:
        """Compute per-component multiplication."""

    @overload
    def __imul__(self, theFactor: float) -> BVH_Vec3f:
        """Compute per-component multiplication by scale factor."""

    def __mul__(self, theFactor: float) -> BVH_Vec3f:
        """Compute per-component multiplication by scale factor."""

    def Multiplied(self, theFactor: float) -> BVH_Vec3f:
        """Compute per-component multiplication by scale factor."""

    def cwiseMin(self, theVec: BVH_Vec3f) -> BVH_Vec3f:
        """Compute component-wise minimum of two vectors."""

    def cwiseMax(self, theVec: BVH_Vec3f) -> BVH_Vec3f:
        """Compute component-wise maximum of two vectors."""

    def cwiseAbs(self) -> BVH_Vec3f:
        """Compute component-wise modulus of the vector."""

    def maxComp(self) -> float:
        """Compute maximum component of the vector."""

    def minComp(self) -> float:
        """Compute minimum component of the vector."""

    @overload
    def __itruediv__(self, theInvFactor: float) -> BVH_Vec3f:
        """Compute per-component division by scale factor."""

    @overload
    def __itruediv__(self, theRight: BVH_Vec3f) -> BVH_Vec3f:
        """Compute per-component division."""

    def __truediv__(self, theInvFactor: float) -> BVH_Vec3f:
        """Compute per-component division by scale factor."""

    def Dot(self, theOther: BVH_Vec3f) -> float:
        """Computes the dot product."""

    def Modulus(self) -> float:
        """Computes the vector modulus (magnitude, length)."""

    def SquareModulus(self) -> float:
        """
        Computes the square of vector modulus (magnitude, length).
        This method may be used for performance tricks.
        """

    def Normalize(self) -> None:
        """Normalize the vector."""

    def Normalized(self) -> BVH_Vec3f:
        """Normalize the vector."""

    @staticmethod
    def Cross(theVec1: BVH_Vec3f, theVec2: BVH_Vec3f) -> BVH_Vec3f:
        """Computes the cross product."""

    @staticmethod
    def GetLERP(theFrom: BVH_Vec3f, theTo: BVH_Vec3f, theT: float) -> BVH_Vec3f:
        """
        Compute linear interpolation between to vectors.
        @param theT - interpolation coefficient 0..1;
        @return interpolation result.
        """

    @staticmethod
    def DX() -> BVH_Vec3f:
        """Construct DX unit vector."""

    @staticmethod
    def DY() -> BVH_Vec3f:
        """Construct DY unit vector."""

    @staticmethod
    def DZ() -> BVH_Vec3f:
        """Construct DZ unit vector."""

class BVH_Vec4f:
    """
    Generic 4-components vector.
    To be used as RGBA color vector or XYZW 3D-point with special W-component
    for operations with projection / model view matrices.
    Use this class for 3D-points carefully because declared W-component may
    results in incorrect results if used without matrices.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor. Construct the zero vector."""

    @overload
    def __init__(self, theValue: float) -> None:
        """Initialize ALL components of vector within specified value."""

    @overload
    def __init__(self, theVec2: BVH_Vec2f) -> None:
        """Constructor from 2-components vector."""

    @overload
    def __init__(self, theVec3: BVH_Vec3f, theW: float = 0.0) -> None:
        """Constructor from 3-components vector + optional 4th value."""

    @overload
    def __init__(self, theX: float, theY: float, theZ: float, theW: float) -> None:
        """Per-component constructor."""

    @overload
    def __init__(self, theOther: BVH_Vec4f) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    @overload
    def SetValues(self, theX: float, theY: float, theZ: float, theW: float) -> None:
        """Assign new values to the vector."""

    @overload
    def SetValues(self, theVec3: BVH_Vec3f, theW: float) -> None:
        """Assign new values as 3-component vector and a 4-th value."""

    @overload
    def x(self) -> float: ...

    @overload
    def x(self) -> float:
        """Alias to 1st component as X coordinate in XYZW."""

    @overload
    def r(self) -> float: ...

    @overload
    def r(self) -> float:
        """Alias to 1st component as RED channel in RGBA."""

    @overload
    def y(self) -> float: ...

    @overload
    def y(self) -> float:
        """Alias to 2nd component as Y coordinate in XYZW."""

    @overload
    def g(self) -> float: ...

    @overload
    def g(self) -> float:
        """Alias to 2nd component as GREEN channel in RGBA."""

    @overload
    def z(self) -> float: ...

    @overload
    def z(self) -> float:
        """Alias to 3rd component as Z coordinate in XYZW."""

    @overload
    def b(self) -> float: ...

    @overload
    def b(self) -> float:
        """Alias to 3rd component as BLUE channel in RGBA."""

    @overload
    def w(self) -> float: ...

    @overload
    def w(self) -> float:
        """Alias to 4th component as W coordinate in XYZW."""

    @overload
    def a(self) -> float: ...

    @overload
    def a(self) -> float:
        """Alias to 4th component as ALPHA channel in RGBA."""

    def xy(self) -> BVH_Vec2f:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def yx(self) -> BVH_Vec2f:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def xz(self) -> BVH_Vec2f:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def zx(self) -> BVH_Vec2f:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def xw(self) -> BVH_Vec2f:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def wx(self) -> BVH_Vec2f:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def yz(self) -> BVH_Vec2f:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def zy(self) -> BVH_Vec2f:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def yw(self) -> BVH_Vec2f:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def wy(self) -> BVH_Vec2f:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def zw(self) -> BVH_Vec2f:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def wz(self) -> BVH_Vec2f:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def xyz(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xzy(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yxz(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yzx(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zyx(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zxy(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xyw(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xwy(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yxw(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def ywx(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wyx(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wxy(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xzw(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xwz(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zxw(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zwx(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wzx(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wxz(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yzw(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def ywz(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zyw(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zwy(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wzy(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wyz(self) -> BVH_Vec3f:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def rgb(self) -> BVH_Vec3f:
        """@return RGB components as vector"""

    def rbg(self) -> BVH_Vec3f:
        """@return RGB components as vector"""

    def grb(self) -> BVH_Vec3f:
        """@return RGB components as vector"""

    def gbr(self) -> BVH_Vec3f:
        """@return RGB components as vector"""

    def bgr(self) -> BVH_Vec3f:
        """@return RGB components as vector"""

    def brg(self) -> BVH_Vec3f:
        """@return RGB components as vector"""

    def Setx(self, theValue: float) -> None:
        """Python addition: sets the value x() returns by reference in C++."""

    def Setr(self, theValue: float) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def Sety(self, theValue: float) -> None:
        """Python addition: sets the value y() returns by reference in C++."""

    def Setg(self, theValue: float) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def Setz(self, theValue: float) -> None:
        """Python addition: sets the value z() returns by reference in C++."""

    def Setb(self, theValue: float) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    def Setw(self, theValue: float) -> None:
        """Python addition: sets the value w() returns by reference in C++."""

    def Seta(self, theValue: float) -> None:
        """Python addition: sets the value a() returns by reference in C++."""

    def IsEqual(self, theOther: BVH_Vec4f) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __eq__(self, theOther: BVH_Vec4f) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __ne__(self, theOther: BVH_Vec4f) -> bool:
        """
        Check this vector with another vector for non-equality (without tolerance!).
        """

    def __iadd__(self, theAdd: BVH_Vec4f) -> BVH_Vec4f:
        """Compute per-component summary."""

    def __neg__(self) -> BVH_Vec4f:
        """Unary -."""

    def __isub__(self, theDec: BVH_Vec4f) -> BVH_Vec4f:
        """Compute per-component subtraction."""

    @overload
    def __imul__(self, theRight: BVH_Vec4f) -> BVH_Vec4f: ...

    @overload
    def __imul__(self, theFactor: float) -> BVH_Vec4f:
        """Compute per-component multiplication."""

    def Multiply(self, theFactor: float) -> None:
        """Compute per-component multiplication."""

    def __mul__(self, theFactor: float) -> BVH_Vec4f:
        """Compute per-component multiplication."""

    def Multiplied(self, theFactor: float) -> BVH_Vec4f:
        """Compute per-component multiplication."""

    def cwiseMin(self, theVec: BVH_Vec4f) -> BVH_Vec4f:
        """Compute component-wise minimum of two vectors."""

    def cwiseMax(self, theVec: BVH_Vec4f) -> BVH_Vec4f:
        """Compute component-wise maximum of two vectors."""

    def cwiseAbs(self) -> BVH_Vec4f:
        """Compute component-wise modulus of the vector."""

    def maxComp(self) -> float:
        """Compute maximum component of the vector."""

    def minComp(self) -> float:
        """Compute minimum component of the vector."""

    def Dot(self, theOther: BVH_Vec4f) -> float:
        """Computes the dot product."""

    @overload
    def __itruediv__(self, theInvFactor: float) -> BVH_Vec4f:
        """Compute per-component division by scale factor."""

    @overload
    def __itruediv__(self, theRight: BVH_Vec4f) -> BVH_Vec4f:
        """Compute per-component division."""

    def __truediv__(self, theInvFactor: float) -> BVH_Vec4f:
        """Compute per-component division by scale factor."""

class BVH_Vec2d:
    """
    Defines the 2D-vector template.
    The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor. Construct the zero vector."""

    @overload
    def __init__(self, theXY: float) -> None:
        """Initialize ALL components of vector within specified value."""

    @overload
    def __init__(self, theX: float, theY: float) -> None:
        """Per-component constructor."""

    @overload
    def __init__(self, theOther: BVH_Vec2d) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    def SetValues(self, theX: float, theY: float) -> None:
        """Assign new values to the vector."""

    @overload
    def x(self) -> float: ...

    @overload
    def x(self) -> float:
        """Alias to 1st component as X coordinate in XY."""

    @overload
    def y(self) -> float: ...

    @overload
    def y(self) -> float:
        """Alias to 2nd component as Y coordinate in XY."""

    def xy(self) -> BVH_Vec2d:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def yx(self) -> BVH_Vec2d:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def Setx(self, theValue: float) -> None:
        """Python addition: sets the value x() returns by reference in C++."""

    def Sety(self, theValue: float) -> None:
        """Python addition: sets the value y() returns by reference in C++."""

    def IsEqual(self, theOther: BVH_Vec2d) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __eq__(self, theOther: BVH_Vec2d) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __ne__(self, theOther: BVH_Vec2d) -> bool:
        """
        Check this vector with another vector for non-equality (without tolerance!).
        """

    def __iadd__(self, theAdd: BVH_Vec2d) -> BVH_Vec2d:
        """Compute per-component summary."""

    def __isub__(self, theDec: BVH_Vec2d) -> BVH_Vec2d:
        """Compute per-component subtraction."""

    def __neg__(self) -> BVH_Vec2d:
        """Unary -."""

    @overload
    def __imul__(self, theRight: BVH_Vec2d) -> BVH_Vec2d:
        """Compute per-component multiplication."""

    @overload
    def __imul__(self, theFactor: float) -> BVH_Vec2d:
        """Compute per-component multiplication by scale factor."""

    def Multiply(self, theFactor: float) -> None:
        """Compute per-component multiplication by scale factor."""

    def Multiplied(self, theFactor: float) -> BVH_Vec2d:
        """Compute per-component multiplication by scale factor."""

    def cwiseMin(self, theVec: BVH_Vec2d) -> BVH_Vec2d:
        """Compute component-wise minimum of two vectors."""

    def cwiseMax(self, theVec: BVH_Vec2d) -> BVH_Vec2d:
        """Compute component-wise maximum of two vectors."""

    def cwiseAbs(self) -> BVH_Vec2d:
        """Compute component-wise modulus of the vector."""

    def maxComp(self) -> float:
        """Compute maximum component of the vector."""

    def minComp(self) -> float:
        """Compute minimum component of the vector."""

    @overload
    def __itruediv__(self, theInvFactor: float) -> BVH_Vec2d:
        """Compute per-component division by scale factor."""

    @overload
    def __itruediv__(self, theRight: BVH_Vec2d) -> BVH_Vec2d:
        """Compute per-component division."""

    def __mul__(self, theFactor: float) -> BVH_Vec2d:
        """Compute per-component multiplication by scale factor."""

    def __truediv__(self, theInvFactor: float) -> BVH_Vec2d:
        """Compute per-component division by scale factor."""

    def Dot(self, theOther: BVH_Vec2d) -> float:
        """Computes the dot product."""

    def Modulus(self) -> float:
        """Computes the vector modulus (magnitude, length)."""

    def SquareModulus(self) -> float:
        """
        Computes the square of vector modulus (magnitude, length).
        This method may be used for performance tricks.
        """

    @staticmethod
    def DX() -> BVH_Vec2d:
        """Construct DX unit vector."""

    @staticmethod
    def DY() -> BVH_Vec2d:
        """Construct DY unit vector."""

class BVH_Vec3d:
    """
    Generic 3-components vector.
    To be used as RGB color pixel or XYZ 3D-point.
    The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor. Construct the zero vector."""

    @overload
    def __init__(self, theValue: float) -> None:
        """Initialize ALL components of vector within specified value."""

    @overload
    def __init__(self, theVec2: BVH_Vec2d, theZ: float = 0.0) -> None:
        """Constructor from 2-components vector + optional 3rd value."""

    @overload
    def __init__(self, theX: float, theY: float, theZ: float) -> None:
        """Per-component constructor."""

    @overload
    def __init__(self, theOther: BVH_Vec3d) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    @overload
    def SetValues(self, theX: float, theY: float, theZ: float) -> None: ...

    @overload
    def SetValues(self, theVec2: BVH_Vec2d, theZ: float) -> None:
        """Assign new values to the vector."""

    @overload
    def x(self) -> float: ...

    @overload
    def x(self) -> float:
        """Alias to 1st component as X coordinate in XYZ."""

    @overload
    def r(self) -> float: ...

    @overload
    def r(self) -> float:
        """Alias to 1st component as RED channel in RGB."""

    @overload
    def y(self) -> float: ...

    @overload
    def y(self) -> float:
        """Alias to 2nd component as Y coordinate in XYZ."""

    @overload
    def g(self) -> float: ...

    @overload
    def g(self) -> float:
        """Alias to 2nd component as GREEN channel in RGB."""

    @overload
    def z(self) -> float: ...

    @overload
    def z(self) -> float:
        """Alias to 3rd component as Z coordinate in XYZ."""

    @overload
    def b(self) -> float: ...

    @overload
    def b(self) -> float:
        """Alias to 3rd component as BLUE channel in RGB."""

    def xy(self) -> BVH_Vec2d:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def yx(self) -> BVH_Vec2d:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def xz(self) -> BVH_Vec2d:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def zx(self) -> BVH_Vec2d:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def yz(self) -> BVH_Vec2d:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def zy(self) -> BVH_Vec2d:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def xyz(self) -> BVH_Vec3d:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def xzy(self) -> BVH_Vec3d:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def yxz(self) -> BVH_Vec3d:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def yzx(self) -> BVH_Vec3d:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def zyx(self) -> BVH_Vec3d:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def zxy(self) -> BVH_Vec3d:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def Setx(self, theValue: float) -> None:
        """Python addition: sets the value x() returns by reference in C++."""

    def Setr(self, theValue: float) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def Sety(self, theValue: float) -> None:
        """Python addition: sets the value y() returns by reference in C++."""

    def Setg(self, theValue: float) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def Setz(self, theValue: float) -> None:
        """Python addition: sets the value z() returns by reference in C++."""

    def Setb(self, theValue: float) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    def IsEqual(self, theOther: BVH_Vec3d) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __eq__(self, theOther: BVH_Vec3d) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __ne__(self, theOther: BVH_Vec3d) -> bool:
        """
        Check this vector with another vector for non-equality (without tolerance!).
        """

    def __iadd__(self, theAdd: BVH_Vec3d) -> BVH_Vec3d:
        """Compute per-component summary."""

    def __neg__(self) -> BVH_Vec3d:
        """Unary -."""

    def __isub__(self, theDec: BVH_Vec3d) -> BVH_Vec3d:
        """Compute per-component subtraction."""

    def Multiply(self, theFactor: float) -> None:
        """Compute per-component multiplication by scale factor."""

    @overload
    def __imul__(self, theRight: BVH_Vec3d) -> BVH_Vec3d:
        """Compute per-component multiplication."""

    @overload
    def __imul__(self, theFactor: float) -> BVH_Vec3d:
        """Compute per-component multiplication by scale factor."""

    def __mul__(self, theFactor: float) -> BVH_Vec3d:
        """Compute per-component multiplication by scale factor."""

    def Multiplied(self, theFactor: float) -> BVH_Vec3d:
        """Compute per-component multiplication by scale factor."""

    def cwiseMin(self, theVec: BVH_Vec3d) -> BVH_Vec3d:
        """Compute component-wise minimum of two vectors."""

    def cwiseMax(self, theVec: BVH_Vec3d) -> BVH_Vec3d:
        """Compute component-wise maximum of two vectors."""

    def cwiseAbs(self) -> BVH_Vec3d:
        """Compute component-wise modulus of the vector."""

    def maxComp(self) -> float:
        """Compute maximum component of the vector."""

    def minComp(self) -> float:
        """Compute minimum component of the vector."""

    @overload
    def __itruediv__(self, theInvFactor: float) -> BVH_Vec3d:
        """Compute per-component division by scale factor."""

    @overload
    def __itruediv__(self, theRight: BVH_Vec3d) -> BVH_Vec3d:
        """Compute per-component division."""

    def __truediv__(self, theInvFactor: float) -> BVH_Vec3d:
        """Compute per-component division by scale factor."""

    def Dot(self, theOther: BVH_Vec3d) -> float:
        """Computes the dot product."""

    def Modulus(self) -> float:
        """Computes the vector modulus (magnitude, length)."""

    def SquareModulus(self) -> float:
        """
        Computes the square of vector modulus (magnitude, length).
        This method may be used for performance tricks.
        """

    def Normalize(self) -> None:
        """Normalize the vector."""

    def Normalized(self) -> BVH_Vec3d:
        """Normalize the vector."""

    @staticmethod
    def Cross(theVec1: BVH_Vec3d, theVec2: BVH_Vec3d) -> BVH_Vec3d:
        """Computes the cross product."""

    @staticmethod
    def GetLERP(theFrom: BVH_Vec3d, theTo: BVH_Vec3d, theT: float) -> BVH_Vec3d:
        """
        Compute linear interpolation between to vectors.
        @param theT - interpolation coefficient 0..1;
        @return interpolation result.
        """

    @staticmethod
    def DX() -> BVH_Vec3d:
        """Construct DX unit vector."""

    @staticmethod
    def DY() -> BVH_Vec3d:
        """Construct DY unit vector."""

    @staticmethod
    def DZ() -> BVH_Vec3d:
        """Construct DZ unit vector."""

class BVH_Vec4d:
    """
    Generic 4-components vector.
    To be used as RGBA color vector or XYZW 3D-point with special W-component
    for operations with projection / model view matrices.
    Use this class for 3D-points carefully because declared W-component may
    results in incorrect results if used without matrices.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor. Construct the zero vector."""

    @overload
    def __init__(self, theValue: float) -> None:
        """Initialize ALL components of vector within specified value."""

    @overload
    def __init__(self, theVec2: BVH_Vec2d) -> None:
        """Constructor from 2-components vector."""

    @overload
    def __init__(self, theVec3: BVH_Vec3d, theW: float = 0.0) -> None:
        """Constructor from 3-components vector + optional 4th value."""

    @overload
    def __init__(self, theX: float, theY: float, theZ: float, theW: float) -> None:
        """Per-component constructor."""

    @overload
    def __init__(self, theOther: BVH_Vec4d) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    @overload
    def SetValues(self, theX: float, theY: float, theZ: float, theW: float) -> None:
        """Assign new values to the vector."""

    @overload
    def SetValues(self, theVec3: BVH_Vec3d, theW: float) -> None:
        """Assign new values as 3-component vector and a 4-th value."""

    @overload
    def x(self) -> float: ...

    @overload
    def x(self) -> float:
        """Alias to 1st component as X coordinate in XYZW."""

    @overload
    def r(self) -> float: ...

    @overload
    def r(self) -> float:
        """Alias to 1st component as RED channel in RGBA."""

    @overload
    def y(self) -> float: ...

    @overload
    def y(self) -> float:
        """Alias to 2nd component as Y coordinate in XYZW."""

    @overload
    def g(self) -> float: ...

    @overload
    def g(self) -> float:
        """Alias to 2nd component as GREEN channel in RGBA."""

    @overload
    def z(self) -> float: ...

    @overload
    def z(self) -> float:
        """Alias to 3rd component as Z coordinate in XYZW."""

    @overload
    def b(self) -> float: ...

    @overload
    def b(self) -> float:
        """Alias to 3rd component as BLUE channel in RGBA."""

    @overload
    def w(self) -> float: ...

    @overload
    def w(self) -> float:
        """Alias to 4th component as W coordinate in XYZW."""

    @overload
    def a(self) -> float: ...

    @overload
    def a(self) -> float:
        """Alias to 4th component as ALPHA channel in RGBA."""

    def xy(self) -> BVH_Vec2d:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def yx(self) -> BVH_Vec2d:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def xz(self) -> BVH_Vec2d:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def zx(self) -> BVH_Vec2d:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def xw(self) -> BVH_Vec2d:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def wx(self) -> BVH_Vec2d:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def yz(self) -> BVH_Vec2d:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def zy(self) -> BVH_Vec2d:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def yw(self) -> BVH_Vec2d:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def wy(self) -> BVH_Vec2d:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def zw(self) -> BVH_Vec2d:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def wz(self) -> BVH_Vec2d:
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def xyz(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xzy(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yxz(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yzx(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zyx(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zxy(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xyw(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xwy(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yxw(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def ywx(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wyx(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wxy(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xzw(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xwz(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zxw(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zwx(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wzx(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wxz(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yzw(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def ywz(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zyw(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zwy(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wzy(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wyz(self) -> BVH_Vec3d:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def rgb(self) -> BVH_Vec3d:
        """@return RGB components as vector"""

    def rbg(self) -> BVH_Vec3d:
        """@return RGB components as vector"""

    def grb(self) -> BVH_Vec3d:
        """@return RGB components as vector"""

    def gbr(self) -> BVH_Vec3d:
        """@return RGB components as vector"""

    def bgr(self) -> BVH_Vec3d:
        """@return RGB components as vector"""

    def brg(self) -> BVH_Vec3d:
        """@return RGB components as vector"""

    def Setx(self, theValue: float) -> None:
        """Python addition: sets the value x() returns by reference in C++."""

    def Setr(self, theValue: float) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def Sety(self, theValue: float) -> None:
        """Python addition: sets the value y() returns by reference in C++."""

    def Setg(self, theValue: float) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def Setz(self, theValue: float) -> None:
        """Python addition: sets the value z() returns by reference in C++."""

    def Setb(self, theValue: float) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    def Setw(self, theValue: float) -> None:
        """Python addition: sets the value w() returns by reference in C++."""

    def Seta(self, theValue: float) -> None:
        """Python addition: sets the value a() returns by reference in C++."""

    def IsEqual(self, theOther: BVH_Vec4d) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __eq__(self, theOther: BVH_Vec4d) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __ne__(self, theOther: BVH_Vec4d) -> bool:
        """
        Check this vector with another vector for non-equality (without tolerance!).
        """

    def __iadd__(self, theAdd: BVH_Vec4d) -> BVH_Vec4d:
        """Compute per-component summary."""

    def __neg__(self) -> BVH_Vec4d:
        """Unary -."""

    def __isub__(self, theDec: BVH_Vec4d) -> BVH_Vec4d:
        """Compute per-component subtraction."""

    @overload
    def __imul__(self, theRight: BVH_Vec4d) -> BVH_Vec4d: ...

    @overload
    def __imul__(self, theFactor: float) -> BVH_Vec4d:
        """Compute per-component multiplication."""

    def Multiply(self, theFactor: float) -> None:
        """Compute per-component multiplication."""

    def __mul__(self, theFactor: float) -> BVH_Vec4d:
        """Compute per-component multiplication."""

    def Multiplied(self, theFactor: float) -> BVH_Vec4d:
        """Compute per-component multiplication."""

    def cwiseMin(self, theVec: BVH_Vec4d) -> BVH_Vec4d:
        """Compute component-wise minimum of two vectors."""

    def cwiseMax(self, theVec: BVH_Vec4d) -> BVH_Vec4d:
        """Compute component-wise maximum of two vectors."""

    def cwiseAbs(self) -> BVH_Vec4d:
        """Compute component-wise modulus of the vector."""

    def maxComp(self) -> float:
        """Compute maximum component of the vector."""

    def minComp(self) -> float:
        """Compute minimum component of the vector."""

    def Dot(self, theOther: BVH_Vec4d) -> float:
        """Computes the dot product."""

    @overload
    def __itruediv__(self, theInvFactor: float) -> BVH_Vec4d:
        """Compute per-component division by scale factor."""

    @overload
    def __itruediv__(self, theRight: BVH_Vec4d) -> BVH_Vec4d:
        """Compute per-component division."""

    def __truediv__(self, theInvFactor: float) -> BVH_Vec4d:
        """Compute per-component division by scale factor."""

class BVH_Mat4f:
    """
    Generic matrix of 4 x 4 elements.
    To be used in conjunction with NCollection_Vec4 entities.
    Originally introduced for 3D space projection and orientation operations.
    Warning, empty constructor returns an identity matrix.
    """

    @overload
    def __init__(self) -> None:
        """
        Empty constructor.
        Construct the identity matrix.
        """

    @overload
    def __init__(self, theOther: BVH_Mat4f) -> None: ...

    @staticmethod
    def Rows() -> int:
        """
        Get number of rows.
        @return number of rows.
        """

    @staticmethod
    def Cols() -> int:
        """
        Get number of columns.
        @return number of columns.
        """

    @staticmethod
    def Identity() -> BVH_Mat4f:
        """Return identity matrix."""

    @staticmethod
    def Zero() -> BVH_Mat4f:
        """Return zero matrix."""

    def GetValue(self, theRow: int, theCol: int) -> float:
        """
        Get element at the specified row and column.
        @param[in] theRow  the row to address.
        @param[in] theCol  the column to address.
        @return the value of the addressed element.
        """

    def ChangeValue(self, theRow: int, theCol: int) -> float:
        """
        Access element at the specified row and column.
        @param[in] theRow  the row to access.
        @param[in] theCol  the column to access.
        @return reference on the matrix element.
        """

    def SetValue(self, theRow: int, theCol: int, theValue: float) -> None:
        """
        Set value for the element specified by row and columns.
        @param[in] theRow    the row to change.
        @param[in] theCol    the column to change.
        @param[in] theValue  the value to set.
        """

    @overload
    def __call__(self, theRow: int, theCol: int) -> float: ...

    @overload
    def __call__(self, theRow: int, theCol: int) -> float:
        """Return value."""

    def __getitem__(self, arg: tuple[int, int], /) -> float:
        """Python addition: alias to operator()."""

    def __setitem__(self, arg0: tuple[int, int], arg1: float, /) -> None:
        """
        Python addition: sets the value operator()(theRow, theCol) returns by reference in C++.
        """

    def GetRow(self, theRow: int) -> BVH_Vec4f:
        """
        Get vector of elements for the specified row.
        @param[in] theRow  the row to access.
        @return vector of elements.
        """

    @overload
    def SetRow(self, theRow: int, theVec: BVH_Vec3f) -> None:
        """
        Change first 3 row values by the passed vector.
        @param[in] theRow  the row to change.
        @param[in] theVec  the vector of values.
        """

    @overload
    def SetRow(self, theRow: int, theVec: BVH_Vec4f) -> None:
        """
        Set row values by the passed 4 element vector.
        @param[in] theRow  the row to change.
        @param[in] theVec  the vector of values.
        """

    def GetColumn(self, theCol: int) -> BVH_Vec4f:
        """
        Get vector of elements for the specified column.
        @param[in] theCol  the column to access.
        @return vector of elements.
        """

    @overload
    def SetColumn(self, theCol: int, theVec: BVH_Vec3f) -> None:
        """
        Change first 3 column values by the passed vector.
        @param[in] theCol  the column to change.
        @param[in] theVec  the vector of values.
        """

    @overload
    def SetColumn(self, theCol: int, theVec: BVH_Vec4f) -> None:
        """
        Set column values by the passed 4 element vector.
        @param[in] theCol  the column to change.
        @param[in] theVec  the vector of values.
        """

    def GetDiagonal(self) -> BVH_Vec4f:
        """
        Get vector of diagonal elements.
        @return vector of diagonal elements.
        """

    @overload
    def SetDiagonal(self, theVec: BVH_Vec3f) -> None:
        """
        Change first 3 elements of the diagonal matrix.
        @param theVec the vector of values.
        """

    @overload
    def SetDiagonal(self, theVec: BVH_Vec4f) -> None:
        """
        Set diagonal elements of the matrix by the passed vector.
        @param[in] theVec  the vector of values.
        """

    def GetMat3(self) -> "NCollection_Mat3<float>":
        """Return 3x3 sub-matrix."""

    def InitZero(self) -> None:
        """Initialize the zero matrix."""

    def IsZero(self) -> bool:
        """Checks the matrix for zero (without tolerance)."""

    def InitIdentity(self) -> None:
        """Initialize the identity matrix."""

    def IsIdentity(self) -> bool:
        """Checks the matrix for identity (without tolerance)."""

    def IsEqual(self, theOther: BVH_Mat4f) -> bool:
        """
        Check this matrix for equality with another matrix (without tolerance!).
        """

    def __eq__(self, theOther: BVH_Mat4f) -> bool:
        """
        Check this matrix for equality with another matrix (without tolerance!).
        """

    def __ne__(self, theOther: BVH_Mat4f) -> bool:
        """
        Check this matrix for non-equality with another matrix (without tolerance!).
        """

    @overload
    def __mul__(self, theVec: BVH_Vec4f) -> BVH_Vec4f:
        """
        Multiply by the vector (M * V).
        @param[in] theVec  the vector to multiply.
        """

    @overload
    def __mul__(self, theMat: BVH_Mat4f) -> BVH_Mat4f:
        """
        Compute matrix multiplication product.
        @param[in] theMat  the other matrix.
        @return result of multiplication.
        """

    @overload
    def __mul__(self, theFactor: float) -> BVH_Mat4f:
        """
        Compute per-element multiplication.
        @param[in] theFactor  the scale factor.
        @return the result of multiplication.
        """

    @staticmethod
    def Multiply_s(theMatA: BVH_Mat4f, theMatB: BVH_Mat4f) -> BVH_Mat4f:
        """
        Compute matrix multiplication product: A * B.
        @param[in] theMatA  the matrix "A".
        @param[in] theMatB  the matrix "B".
        """

    @overload
    def Multiply(self, theMat: BVH_Mat4f) -> None:
        """
        Compute matrix multiplication.
        @param[in] theMat  the matrix to multiply.
        """

    @overload
    def Multiply(self, theFactor: float) -> None:
        """
        Compute per-component multiplication.
        @param[in] theFactor  the scale factor.
        """

    @overload
    def __imul__(self, theMat: BVH_Mat4f) -> BVH_Mat4f:
        """
        Multiply by the another matrix.
        @param[in] theMat  the other matrix.
        """

    @overload
    def __imul__(self, theFactor: float) -> BVH_Mat4f:
        """
        Compute per-element multiplication.
        @param[in] theFactor  the scale factor.
        """

    @overload
    def Multiplied(self, theMat: BVH_Mat4f) -> BVH_Mat4f:
        """
        Compute matrix multiplication product.
        @param[in] theMat  the other matrix.
        @return result of multiplication.
        """

    @overload
    def Multiplied(self, theFactor: float) -> BVH_Mat4f:
        """
        Compute per-element multiplication.
        @param[in] theFactor  the scale factor.
        @return the result of multiplication.
        """

    def Divide(self, theFactor: float) -> None:
        """
        Compute per-component division.
        @param[in] theFactor  the scale factor.
        """

    def __itruediv__(self, theScalar: float) -> BVH_Mat4f:
        """
        Per-component division.
        @param[in] theScalar  the scale factor.
        """

    def Divided(self, theScalar: float) -> BVH_Mat4f:
        """Divides all the coefficients of the matrix by scalar."""

    def __truediv__(self, theScalar: float) -> BVH_Mat4f:
        """Divides all the coefficients of the matrix by scalar."""

    def Add(self, theMat: BVH_Mat4f) -> None:
        """Per-component addition of another matrix."""

    def __iadd__(self, theMat: BVH_Mat4f) -> BVH_Mat4f:
        """Per-component addition of another matrix."""

    def Subtract(self, theMat: BVH_Mat4f) -> None:
        """Per-component subtraction of another matrix."""

    def __isub__(self, theMat: BVH_Mat4f) -> BVH_Mat4f:
        """Per-component subtraction of another matrix."""

    def Added(self, theMat: BVH_Mat4f) -> BVH_Mat4f:
        """Per-component addition of another matrix."""

    def __add__(self, theMat: BVH_Mat4f) -> BVH_Mat4f:
        """Per-component addition of another matrix."""

    def Subtracted(self, theMat: BVH_Mat4f) -> BVH_Mat4f:
        """Per-component subtraction of another matrix."""

    def __sub__(self, theMat: BVH_Mat4f) -> BVH_Mat4f:
        """Per-component subtraction of another matrix."""

    def Negated(self) -> BVH_Mat4f:
        """Returns matrix with all components negated."""

    def __neg__(self) -> BVH_Mat4f:
        """Returns matrix with all components negated."""

    def Translate(self, theVec: BVH_Vec3f) -> None:
        """
        Translate the matrix on the passed vector.
        @param[in] theVec  the translation vector.
        """

    def Transposed(self) -> BVH_Mat4f:
        """
        Transpose the matrix.
        @return transposed copy of the matrix.
        """

    def Transpose(self) -> None:
        """Transpose the matrix."""

    @overload
    def Inverted(self, theOutMx: BVH_Mat4f, theDet: float) -> bool:
        """
        Compute inverted matrix.
        @param[out] theOutMx  the inverted matrix
        @param[out] theDet    determinant of matrix
        @return true if reversion success
        """

    @overload
    def Inverted(self, theOutMx: BVH_Mat4f) -> bool:
        """
        Compute inverted matrix.
        @param[out] theOutMx  the inverted matrix
        @return true if reversion success
        """

    @overload
    def Inverted(self) -> BVH_Mat4f:
        """Return inverted matrix."""

    def DeterminantMat3(self) -> float:
        """Return determinant of the 3x3 sub-matrix."""

    def Adjoint(self) -> BVH_Mat4f:
        """Return adjoint (adjugate matrix, e.g. conjugate transpose)."""

    @overload
    @staticmethod
    def Map(theData: float) -> BVH_Mat4f: ...

    @overload
    @staticmethod
    def Map(theData: float) -> BVH_Mat4f:
        """Maps plain C array to matrix type."""

class BVH_Mat4d:
    """
    Generic matrix of 4 x 4 elements.
    To be used in conjunction with NCollection_Vec4 entities.
    Originally introduced for 3D space projection and orientation operations.
    Warning, empty constructor returns an identity matrix.
    """

    @overload
    def __init__(self) -> None:
        """
        Empty constructor.
        Construct the identity matrix.
        """

    @overload
    def __init__(self, theOther: BVH_Mat4d) -> None: ...

    @staticmethod
    def Rows() -> int:
        """
        Get number of rows.
        @return number of rows.
        """

    @staticmethod
    def Cols() -> int:
        """
        Get number of columns.
        @return number of columns.
        """

    @staticmethod
    def Identity() -> BVH_Mat4d:
        """Return identity matrix."""

    @staticmethod
    def Zero() -> BVH_Mat4d:
        """Return zero matrix."""

    def GetValue(self, theRow: int, theCol: int) -> float:
        """
        Get element at the specified row and column.
        @param[in] theRow  the row to address.
        @param[in] theCol  the column to address.
        @return the value of the addressed element.
        """

    def ChangeValue(self, theRow: int, theCol: int) -> float:
        """
        Access element at the specified row and column.
        @param[in] theRow  the row to access.
        @param[in] theCol  the column to access.
        @return reference on the matrix element.
        """

    def SetValue(self, theRow: int, theCol: int, theValue: float) -> None:
        """
        Set value for the element specified by row and columns.
        @param[in] theRow    the row to change.
        @param[in] theCol    the column to change.
        @param[in] theValue  the value to set.
        """

    @overload
    def __call__(self, theRow: int, theCol: int) -> float: ...

    @overload
    def __call__(self, theRow: int, theCol: int) -> float:
        """Return value."""

    def __getitem__(self, arg: tuple[int, int], /) -> float:
        """Python addition: alias to operator()."""

    def __setitem__(self, arg0: tuple[int, int], arg1: float, /) -> None:
        """
        Python addition: sets the value operator()(theRow, theCol) returns by reference in C++.
        """

    def GetRow(self, theRow: int) -> BVH_Vec4d:
        """
        Get vector of elements for the specified row.
        @param[in] theRow  the row to access.
        @return vector of elements.
        """

    @overload
    def SetRow(self, theRow: int, theVec: BVH_Vec3d) -> None:
        """
        Change first 3 row values by the passed vector.
        @param[in] theRow  the row to change.
        @param[in] theVec  the vector of values.
        """

    @overload
    def SetRow(self, theRow: int, theVec: BVH_Vec4d) -> None:
        """
        Set row values by the passed 4 element vector.
        @param[in] theRow  the row to change.
        @param[in] theVec  the vector of values.
        """

    def GetColumn(self, theCol: int) -> BVH_Vec4d:
        """
        Get vector of elements for the specified column.
        @param[in] theCol  the column to access.
        @return vector of elements.
        """

    @overload
    def SetColumn(self, theCol: int, theVec: BVH_Vec3d) -> None:
        """
        Change first 3 column values by the passed vector.
        @param[in] theCol  the column to change.
        @param[in] theVec  the vector of values.
        """

    @overload
    def SetColumn(self, theCol: int, theVec: BVH_Vec4d) -> None:
        """
        Set column values by the passed 4 element vector.
        @param[in] theCol  the column to change.
        @param[in] theVec  the vector of values.
        """

    def GetDiagonal(self) -> BVH_Vec4d:
        """
        Get vector of diagonal elements.
        @return vector of diagonal elements.
        """

    @overload
    def SetDiagonal(self, theVec: BVH_Vec3d) -> None:
        """
        Change first 3 elements of the diagonal matrix.
        @param theVec the vector of values.
        """

    @overload
    def SetDiagonal(self, theVec: BVH_Vec4d) -> None:
        """
        Set diagonal elements of the matrix by the passed vector.
        @param[in] theVec  the vector of values.
        """

    def GetMat3(self) -> "NCollection_Mat3<double>":
        """Return 3x3 sub-matrix."""

    def InitZero(self) -> None:
        """Initialize the zero matrix."""

    def IsZero(self) -> bool:
        """Checks the matrix for zero (without tolerance)."""

    def InitIdentity(self) -> None:
        """Initialize the identity matrix."""

    def IsIdentity(self) -> bool:
        """Checks the matrix for identity (without tolerance)."""

    def IsEqual(self, theOther: BVH_Mat4d) -> bool:
        """
        Check this matrix for equality with another matrix (without tolerance!).
        """

    def __eq__(self, theOther: BVH_Mat4d) -> bool:
        """
        Check this matrix for equality with another matrix (without tolerance!).
        """

    def __ne__(self, theOther: BVH_Mat4d) -> bool:
        """
        Check this matrix for non-equality with another matrix (without tolerance!).
        """

    @overload
    def __mul__(self, theVec: BVH_Vec4d) -> BVH_Vec4d:
        """
        Multiply by the vector (M * V).
        @param[in] theVec  the vector to multiply.
        """

    @overload
    def __mul__(self, theMat: BVH_Mat4d) -> BVH_Mat4d:
        """
        Compute matrix multiplication product.
        @param[in] theMat  the other matrix.
        @return result of multiplication.
        """

    @overload
    def __mul__(self, theFactor: float) -> BVH_Mat4d:
        """
        Compute per-element multiplication.
        @param[in] theFactor  the scale factor.
        @return the result of multiplication.
        """

    @staticmethod
    def Multiply_s(theMatA: BVH_Mat4d, theMatB: BVH_Mat4d) -> BVH_Mat4d:
        """
        Compute matrix multiplication product: A * B.
        @param[in] theMatA  the matrix "A".
        @param[in] theMatB  the matrix "B".
        """

    @overload
    def Multiply(self, theMat: BVH_Mat4d) -> None:
        """
        Compute matrix multiplication.
        @param[in] theMat  the matrix to multiply.
        """

    @overload
    def Multiply(self, theFactor: float) -> None:
        """
        Compute per-component multiplication.
        @param[in] theFactor  the scale factor.
        """

    @overload
    def __imul__(self, theMat: BVH_Mat4d) -> BVH_Mat4d:
        """
        Multiply by the another matrix.
        @param[in] theMat  the other matrix.
        """

    @overload
    def __imul__(self, theFactor: float) -> BVH_Mat4d:
        """
        Compute per-element multiplication.
        @param[in] theFactor  the scale factor.
        """

    @overload
    def Multiplied(self, theMat: BVH_Mat4d) -> BVH_Mat4d:
        """
        Compute matrix multiplication product.
        @param[in] theMat  the other matrix.
        @return result of multiplication.
        """

    @overload
    def Multiplied(self, theFactor: float) -> BVH_Mat4d:
        """
        Compute per-element multiplication.
        @param[in] theFactor  the scale factor.
        @return the result of multiplication.
        """

    def Divide(self, theFactor: float) -> None:
        """
        Compute per-component division.
        @param[in] theFactor  the scale factor.
        """

    def __itruediv__(self, theScalar: float) -> BVH_Mat4d:
        """
        Per-component division.
        @param[in] theScalar  the scale factor.
        """

    def Divided(self, theScalar: float) -> BVH_Mat4d:
        """Divides all the coefficients of the matrix by scalar."""

    def __truediv__(self, theScalar: float) -> BVH_Mat4d:
        """Divides all the coefficients of the matrix by scalar."""

    def Add(self, theMat: BVH_Mat4d) -> None:
        """Per-component addition of another matrix."""

    def __iadd__(self, theMat: BVH_Mat4d) -> BVH_Mat4d:
        """Per-component addition of another matrix."""

    def Subtract(self, theMat: BVH_Mat4d) -> None:
        """Per-component subtraction of another matrix."""

    def __isub__(self, theMat: BVH_Mat4d) -> BVH_Mat4d:
        """Per-component subtraction of another matrix."""

    def Added(self, theMat: BVH_Mat4d) -> BVH_Mat4d:
        """Per-component addition of another matrix."""

    def __add__(self, theMat: BVH_Mat4d) -> BVH_Mat4d:
        """Per-component addition of another matrix."""

    def Subtracted(self, theMat: BVH_Mat4d) -> BVH_Mat4d:
        """Per-component subtraction of another matrix."""

    def __sub__(self, theMat: BVH_Mat4d) -> BVH_Mat4d:
        """Per-component subtraction of another matrix."""

    def Negated(self) -> BVH_Mat4d:
        """Returns matrix with all components negated."""

    def __neg__(self) -> BVH_Mat4d:
        """Returns matrix with all components negated."""

    def Translate(self, theVec: BVH_Vec3d) -> None:
        """
        Translate the matrix on the passed vector.
        @param[in] theVec  the translation vector.
        """

    def Transposed(self) -> BVH_Mat4d:
        """
        Transpose the matrix.
        @return transposed copy of the matrix.
        """

    def Transpose(self) -> None:
        """Transpose the matrix."""

    @overload
    def Inverted(self, theOutMx: BVH_Mat4d, theDet: float) -> bool:
        """
        Compute inverted matrix.
        @param[out] theOutMx  the inverted matrix
        @param[out] theDet    determinant of matrix
        @return true if reversion success
        """

    @overload
    def Inverted(self, theOutMx: BVH_Mat4d) -> bool:
        """
        Compute inverted matrix.
        @param[out] theOutMx  the inverted matrix
        @return true if reversion success
        """

    @overload
    def Inverted(self) -> BVH_Mat4d:
        """Return inverted matrix."""

    def DeterminantMat3(self) -> float:
        """Return determinant of the 3x3 sub-matrix."""

    def Adjoint(self) -> BVH_Mat4d:
        """Return adjoint (adjugate matrix, e.g. conjugate transpose)."""

    @overload
    @staticmethod
    def Map(theData: float) -> BVH_Mat4d: ...

    @overload
    @staticmethod
    def Map(theData: float) -> BVH_Mat4d:
        """Maps plain C array to matrix type."""

class BVH_TreeBaseTransient(nanoocp.Standard.Standard_Transient):
    """
    A non-template class for using as base for BVH_TreeBase
    (just to have a named base class).
    """

    def __init__(self, theOther: BVH_TreeBaseTransient) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BVH_QuadTree:
    """Type corresponding to quad BVH."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BVH_QuadTree) -> None: ...

class BVH_BinaryTree:
    """Type corresponding to binary BVH."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BVH_BinaryTree) -> None: ...

class BVH_BuilderTransient(nanoocp.Standard.Standard_Transient):
    """
    A non-template class for using as base for BVH_Builder
    (just to have a named base class).
    """

    def __init__(self, theOther: BVH_BuilderTransient) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def MaxTreeDepth(self) -> int:
        """Returns the maximum depth of constructed BVH."""

    def LeafNodeSize(self) -> int:
        """Returns the maximum number of sub-elements in the leaf."""

    def IsParallel(self) -> bool:
        """Returns parallel flag."""

    def SetParallel(self, isParallel: bool) -> None:
        """Set parallel flag controlling possibility of parallel execution."""

class BVH_BuildQueue:
    """Command-queue for parallel building of BVH nodes."""

    def __init__(self) -> None:
        """Creates new BVH build queue."""

    def Size(self) -> int:
        """
        Returns current size of BVH build queue.
        Uses acquire semantics to synchronize with enqueue/dequeue operations.
        """

    def Enqueue(self, theWorkItem: int) -> None:
        """Enqueues new work-item onto BVH build queue."""

    def Fetch(self) -> tuple[int, bool]:
        """Fetches first work-item from BVH build queue."""

    def HasBusyThreads(self) -> bool:
        """
        Checks if there are active build threads.
        Uses acquire semantics to ensure visibility of thread counter updates.
        This is critical for termination detection: threads check this after
        finding an empty queue to determine if they should exit or wait.
        """

class BVH_BuildTool:
    """Tool object to call BVH builder subroutines."""

    def Perform(self, theNode: int) -> None:
        """Performs splitting of the given BVH node."""

class BVH_BuildThread(nanoocp.Standard.Standard_Transient):
    """Wrapper for BVH build thread."""

    @overload
    def __init__(self, theBuildTool: BVH_BuildTool, theBuildQueue: BVH_BuildQueue) -> None:
        """Creates new BVH build thread."""

    @overload
    def __init__(self, theOther: BVH_BuildThread) -> None: ...

    def Run(self) -> None:
        """Starts execution of BVH build thread."""

    def Wait(self) -> None:
        """Waits till the thread finishes execution."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BVH_Properties(nanoocp.Standard.Standard_Transient):
    """Abstract properties of geometric object."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BVH_ObjectTransient(nanoocp.Standard.Standard_Transient):
    """
    A non-template class for using as base for BVH_Object
    (just to have a named base class).
    """

    def __init__(self, theOther: BVH_ObjectTransient) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Properties(self) -> BVH_Properties:
        """Returns properties of the geometric object."""

    def SetProperties(self, theProperties: BVH_Properties) -> None:
        """Sets properties of the geometric object."""

    def IsDirty(self) -> bool:
        """Returns TRUE if object state should be updated."""

    def MarkDirty(self) -> None:
        """Marks object state as outdated (needs BVH rebuilding)."""

class BVH_Builder3d(BVH_BuilderTransient):
    """
    Performs construction of BVH tree using bounding
    boxes (AABBs) of abstract objects.
    \\tparam T Numeric data type
    \\tparam N Vector dimension
    """

    def Build(self, theSet: "BVH_Set<double, 3>", theBVH: "BVH_Tree<double, 3, BVH_BinaryTree>", theBox: "BVH_Box<double, 3>") -> None:
        """Builds BVH using specific algorithm."""

class BitPredicate:
    @overload
    def __init__(self, theDigit: int) -> None:
        """Creates new radix sort predicate."""

    @overload
    def __init__(self, theOther: BitPredicate) -> None: ...

    def __call__(self, theLink: tuple[int, int]) -> bool:
        """Returns predicate value."""

    @property
    def myBit(self) -> int: ...

    @myBit.setter
    def myBit(self, arg: int, /) -> None: ...

class BitComparator:
    """STL compare tool used in binary search algorithm."""

    @overload
    def __init__(self, theDigit: int) -> None:
        """Creates new STL comparator."""

    @overload
    def __init__(self, theOther: BitComparator) -> None: ...

    def __call__(self, theLink1: tuple[int, int], arg1: tuple[int, int]) -> bool:
        """Checks left value for the given bit."""

    @property
    def myBit(self) -> int: ...

    @myBit.setter
    def myBit(self, arg: int, /) -> None: ...

class RadixSorter:
    """Tool object for sorting link array using radix sort algorithm."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RadixSorter) -> None: ...

def EncodeMortonCode(theVoxelX: int, theVoxelY: int, theVoxelZ: int) -> int:
    """
    Encodes 10-bit voxel coordinates into 30-bit Morton code using LUT.
    @param theVoxelX X coordinate (0-1023)
    @param theVoxelY Y coordinate (0-1023)
    @param theVoxelZ Z coordinate (0-1023)
    @return 30-bit Morton code with interleaved bits
    """

# C++ typedef aliases
BVH_Array2i = nanoocp.NCollection.NCollection_LinearVector[nanoocp.BVH.BVH_Vec2i]
BVH_Array3i = nanoocp.NCollection.NCollection_LinearVector[nanoocp.BVH.BVH_Vec3i]
BVH_Array4i = nanoocp.NCollection.NCollection_LinearVector[nanoocp.BVH.BVH_Vec4i]
BVH_Array2f = nanoocp.NCollection.NCollection_LinearVector[nanoocp.BVH.BVH_Vec2f]
BVH_Array3f = nanoocp.NCollection.NCollection_LinearVector[nanoocp.BVH.BVH_Vec3f]
BVH_Array4f = nanoocp.NCollection.NCollection_LinearVector[nanoocp.BVH.BVH_Vec4f]
BVH_Array2d = nanoocp.NCollection.NCollection_LinearVector[nanoocp.BVH.BVH_Vec2d]
BVH_Array3d = nanoocp.NCollection.NCollection_LinearVector[nanoocp.BVH.BVH_Vec3d]
BVH_Array4d = nanoocp.NCollection.NCollection_LinearVector[nanoocp.BVH.BVH_Vec4d]
