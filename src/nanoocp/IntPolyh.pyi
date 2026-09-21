"""OCCT package IntPolyh (toolkit TKGeomAlgo)"""

from typing import overload

import nanoocp.Adaptor3d
import nanoocp.Bnd
import nanoocp.NCollection
import nanoocp.gp


class IntPolyh_Edge:
    """
    The class represents the edge built between the two IntPolyh points.
    It is linked to two IntPolyh triangles.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, thePoint1: int, thePoint2: int, theTriangle1: int, theTriangle2: int) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: IntPolyh_Edge) -> None: ...

    def FirstPoint(self) -> int:
        """Returns the first point"""

    def SecondPoint(self) -> int:
        """Returns the second point"""

    def FirstTriangle(self) -> int:
        """Returns the first triangle"""

    def SecondTriangle(self) -> int:
        """Returns the second triangle"""

    def SetFirstPoint(self, thePoint: int) -> None:
        """Sets the first point"""

    def SetSecondPoint(self, thePoint: int) -> None:
        """Sets the second point"""

    def SetFirstTriangle(self, theTriangle: int) -> None:
        """Sets the first triangle"""

    def SetSecondTriangle(self, theTriangle: int) -> None:
        """Sets the second triangle"""

    def Dump(self, v: int) -> None: ...

class IntPolyh_ArrayOfEdges:
    """
    Class IntPolyh_Array (dynamic array of objects)

    1. The Array is dynamic array of objects.

    2. The Array uses NCollection_DynamicArray to store objects

    3. The Array can be created:
    3.1.  with initial length Nb=0.
    In this case Array should be initiated by invoke
    the method Init(Nb).
    3.2.  with initial length Nb>0.
    In this case Array is initiated automatically.

    The memory is allocated to store myNbAllocated oblects.

    4. The number of items that are stored in the Array (myNbItems)
    can be increased by calling the method:  IncrementNbItems().
    The objects are stored in already allocated memory if it is
    possible.
    Otherwise the new chunk of memory is allocated to store the
    objects.
    The size of chunk <aIncrement> can be defined during the creation
    of the Array.

    5. The start index of the Array is 0, The end index of the Array
    can be obtained by the method  NbItems();

    6. The contents of the element with index "i" can be queried or
    modified by the methods:  Value(i), ChangeValue(i), operator[](i)
    """

    @overload
    def __init__(self) -> None:
        """
        Constructor.
        @param aIncrement
        size of memory (in terms of Items) to expand the array
        """

    @overload
    def __init__(self, aN: int, aIncrement: int = 256) -> None:
        """
        Constructor.
        @param aN
        size of memory (in terms of Items) to allocate
        @param aIncrement
        size of memory (in terms of Items) to expand the array
        """

    @overload
    def __init__(self, theOther: IntPolyh_ArrayOfEdges) -> None: ...

    def Copy(self, aOther: IntPolyh_ArrayOfEdges) -> IntPolyh_ArrayOfEdges:
        """
        Copy
        @param
        aOther - the array to copy from
        @return
        the array
        """

    def Init(self, aN: int) -> None:
        """
        Init - allocate memory for <aN> items
        @param
        aN - the number of items to allocate the memory
        """

    def IncrementNbItems(self) -> None:
        """IncrementNbItems - increment the number of stored items"""

    def GetN(self) -> int:
        """
        GetN - returns the number of 'allocated' items
        @return
        the number of 'allocated' items
        """

    def NbItems(self) -> int:
        """
        NbItems - returns the number of stored items
        @return
        the number of stored items
        """

    def SetNbItems(self, aNb: int) -> None:
        """
        set the number of stored items
        @param aNb
        the number of stored items
        """

    def Value(self, aIndex: int) -> IntPolyh_Edge:
        """
        query the const value
        @param aIndex
        index
        @return
        the const item
        """

    def ChangeValue(self, aIndex: int) -> IntPolyh_Edge:
        """
        query the value
        @param aIndex
        index
        @return
        the item
        """

    def __getitem__(self, aIndex: int) -> IntPolyh_Edge:
        """
        query the value
        @param aIndex
        index
        @return
        the item
        """

class IntPolyh_Point:
    """
    The class represents the point on the surface with
    both 3D and 2D points.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, x: float, y: float, z: float, u: float, v: float) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: IntPolyh_Point) -> None: ...

    def X(self) -> float:
        """Returns X coordinate of the 3D point"""

    def Y(self) -> float:
        """Returns Y coordinate of the 3D point"""

    def Z(self) -> float:
        """Returns the Z coordinate of the 3D point"""

    def U(self) -> float:
        """Returns the U coordinate of the 2D point"""

    def V(self) -> float:
        """Returns the V coordinate of the 2D point"""

    def PartOfCommon(self) -> int:
        """Returns 0 if the point is not common with the other surface"""

    def Set(self, x: float, y: float, z: float, u: float, v: float, II: int = 1) -> None:
        """Sets the point"""

    def SetX(self, x: float) -> None:
        """Sets the X coordinate for the 3D point"""

    def SetY(self, y: float) -> None:
        """Sets the Y coordinate for the 3D point"""

    def SetZ(self, z: float) -> None:
        """Sets the Z coordinate for the 3D point"""

    def SetU(self, u: float) -> None:
        """Sets the U coordinate for the 2D point"""

    def SetV(self, v: float) -> None:
        """Sets the V coordinate for the 2D point"""

    def SetPartOfCommon(self, ii: int) -> None:
        """Sets the part of common"""

    def Middle(self, MySurface: nanoocp.Adaptor3d.Adaptor3d_Surface | None, P1: IntPolyh_Point, P2: IntPolyh_Point) -> None:
        """Creates middle point from P1 and P2 and stores it to this"""

    def Add(self, P1: IntPolyh_Point) -> IntPolyh_Point:
        """Addition"""

    def __add__(self, P1: IntPolyh_Point) -> IntPolyh_Point: ...

    def Sub(self, P1: IntPolyh_Point) -> IntPolyh_Point:
        """Subtraction"""

    def __sub__(self, P1: IntPolyh_Point) -> IntPolyh_Point: ...

    def Divide(self, rr: float) -> IntPolyh_Point:
        """Division"""

    def __truediv__(self, rr: float) -> IntPolyh_Point: ...

    def Multiplication(self, rr: float) -> IntPolyh_Point:
        """Multiplication"""

    def __mul__(self, rr: float) -> IntPolyh_Point: ...

    def SquareModulus(self) -> float:
        """Square modulus"""

    def SquareDistance(self, P2: IntPolyh_Point) -> float:
        """Square distance to the other point"""

    def Dot(self, P2: IntPolyh_Point) -> float:
        """Dot"""

    def Cross(self, P1: IntPolyh_Point, P2: IntPolyh_Point) -> None:
        """Cross"""

    @overload
    def Dump(self) -> None: ...

    @overload
    def Dump(self, i: int) -> None:
        """Dump"""

    def SetDegenerated(self, theFlag: bool) -> None:
        """Sets the degenerated flag"""

    def Degenerated(self) -> bool:
        """Returns the degenerated flag"""

class IntPolyh_ArrayOfPoints:
    """
    Class IntPolyh_Array (dynamic array of objects)

    1. The Array is dynamic array of objects.

    2. The Array uses NCollection_DynamicArray to store objects

    3. The Array can be created:
    3.1.  with initial length Nb=0.
    In this case Array should be initiated by invoke
    the method Init(Nb).
    3.2.  with initial length Nb>0.
    In this case Array is initiated automatically.

    The memory is allocated to store myNbAllocated oblects.

    4. The number of items that are stored in the Array (myNbItems)
    can be increased by calling the method:  IncrementNbItems().
    The objects are stored in already allocated memory if it is
    possible.
    Otherwise the new chunk of memory is allocated to store the
    objects.
    The size of chunk <aIncrement> can be defined during the creation
    of the Array.

    5. The start index of the Array is 0, The end index of the Array
    can be obtained by the method  NbItems();

    6. The contents of the element with index "i" can be queried or
    modified by the methods:  Value(i), ChangeValue(i), operator[](i)
    """

    @overload
    def __init__(self) -> None:
        """
        Constructor.
        @param aIncrement
        size of memory (in terms of Items) to expand the array
        """

    @overload
    def __init__(self, aN: int, aIncrement: int = 256) -> None:
        """
        Constructor.
        @param aN
        size of memory (in terms of Items) to allocate
        @param aIncrement
        size of memory (in terms of Items) to expand the array
        """

    @overload
    def __init__(self, theOther: IntPolyh_ArrayOfPoints) -> None: ...

    def Copy(self, aOther: IntPolyh_ArrayOfPoints) -> IntPolyh_ArrayOfPoints:
        """
        Copy
        @param
        aOther - the array to copy from
        @return
        the array
        """

    def Init(self, aN: int) -> None:
        """
        Init - allocate memory for <aN> items
        @param
        aN - the number of items to allocate the memory
        """

    def IncrementNbItems(self) -> None:
        """IncrementNbItems - increment the number of stored items"""

    def GetN(self) -> int:
        """
        GetN - returns the number of 'allocated' items
        @return
        the number of 'allocated' items
        """

    def NbItems(self) -> int:
        """
        NbItems - returns the number of stored items
        @return
        the number of stored items
        """

    def SetNbItems(self, aNb: int) -> None:
        """
        set the number of stored items
        @param aNb
        the number of stored items
        """

    def Value(self, aIndex: int) -> IntPolyh_Point:
        """
        query the const value
        @param aIndex
        index
        @return
        the const item
        """

    def ChangeValue(self, aIndex: int) -> IntPolyh_Point:
        """
        query the value
        @param aIndex
        index
        @return
        the item
        """

    def __getitem__(self, aIndex: int) -> IntPolyh_Point:
        """
        query the value
        @param aIndex
        index
        @return
        the item
        """

    def Dump(self) -> None:
        """dump the contents"""

class IntPolyh_PointNormal:
    """
    Auxiliary structure to represent pair of point and
    normal vector in this point on the surface.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntPolyh_PointNormal) -> None: ...

    @property
    def Point(self) -> nanoocp.gp.gp_Pnt: ...

    @Point.setter
    def Point(self, arg: nanoocp.gp.gp_Pnt, /) -> None: ...

    @property
    def Normal(self) -> nanoocp.gp.gp_Vec: ...

    @Normal.setter
    def Normal(self, arg: nanoocp.gp.gp_Vec, /) -> None: ...

class IntPolyh_ArrayOfPointNormal:
    """
    Class IntPolyh_Array (dynamic array of objects)

    1. The Array is dynamic array of objects.

    2. The Array uses NCollection_DynamicArray to store objects

    3. The Array can be created:
    3.1.  with initial length Nb=0.
    In this case Array should be initiated by invoke
    the method Init(Nb).
    3.2.  with initial length Nb>0.
    In this case Array is initiated automatically.

    The memory is allocated to store myNbAllocated oblects.

    4. The number of items that are stored in the Array (myNbItems)
    can be increased by calling the method:  IncrementNbItems().
    The objects are stored in already allocated memory if it is
    possible.
    Otherwise the new chunk of memory is allocated to store the
    objects.
    The size of chunk <aIncrement> can be defined during the creation
    of the Array.

    5. The start index of the Array is 0, The end index of the Array
    can be obtained by the method  NbItems();

    6. The contents of the element with index "i" can be queried or
    modified by the methods:  Value(i), ChangeValue(i), operator[](i)
    """

    @overload
    def __init__(self) -> None:
        """
        Constructor.
        @param aIncrement
        size of memory (in terms of Items) to expand the array
        """

    @overload
    def __init__(self, aN: int, aIncrement: int = 256) -> None:
        """
        Constructor.
        @param aN
        size of memory (in terms of Items) to allocate
        @param aIncrement
        size of memory (in terms of Items) to expand the array
        """

    @overload
    def __init__(self, theOther: IntPolyh_ArrayOfPointNormal) -> None: ...

    def Copy(self, aOther: IntPolyh_ArrayOfPointNormal) -> IntPolyh_ArrayOfPointNormal:
        """
        Copy
        @param
        aOther - the array to copy from
        @return
        the array
        """

    def Init(self, aN: int) -> None:
        """
        Init - allocate memory for <aN> items
        @param
        aN - the number of items to allocate the memory
        """

    def IncrementNbItems(self) -> None:
        """IncrementNbItems - increment the number of stored items"""

    def GetN(self) -> int:
        """
        GetN - returns the number of 'allocated' items
        @return
        the number of 'allocated' items
        """

    def NbItems(self) -> int:
        """
        NbItems - returns the number of stored items
        @return
        the number of stored items
        """

    def SetNbItems(self, aNb: int) -> None:
        """
        set the number of stored items
        @param aNb
        the number of stored items
        """

    def Value(self, aIndex: int) -> IntPolyh_PointNormal:
        """
        query the const value
        @param aIndex
        index
        @return
        the const item
        """

    def ChangeValue(self, aIndex: int) -> IntPolyh_PointNormal:
        """
        query the value
        @param aIndex
        index
        @return
        the item
        """

    def __getitem__(self, aIndex: int) -> IntPolyh_PointNormal:
        """
        query the value
        @param aIndex
        index
        @return
        the item
        """

class IntPolyh_StartPoint:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, xx: float, yy: float, zz: float, uu1: float, vv1: float, uu2: float, vv2: float, T1: int, E1: int, LAM1: float, T2: int, E2: int, LAM2: float, List: int) -> None: ...

    @overload
    def __init__(self, theOther: IntPolyh_StartPoint) -> None: ...

    def X(self) -> float: ...

    def Y(self) -> float: ...

    def Z(self) -> float: ...

    def U1(self) -> float: ...

    def V1(self) -> float: ...

    def U2(self) -> float: ...

    def V2(self) -> float: ...

    def T1(self) -> int: ...

    def E1(self) -> int: ...

    def Lambda1(self) -> float: ...

    def T2(self) -> int: ...

    def E2(self) -> int: ...

    def Lambda2(self) -> float: ...

    def GetAngle(self) -> float: ...

    def ChainList(self) -> int: ...

    def GetEdgePoints(self, Triangle: IntPolyh_Triangle) -> tuple[int, int, int, int]: ...

    def SetXYZ(self, XX: float, YY: float, ZZ: float) -> None: ...

    def SetUV1(self, UU1: float, VV1: float) -> None: ...

    def SetUV2(self, UU2: float, VV2: float) -> None: ...

    def SetEdge1(self, IE1: int) -> None: ...

    def SetLambda1(self, LAM1: float) -> None: ...

    def SetEdge2(self, IE2: int) -> None: ...

    def SetLambda2(self, LAM2: float) -> None: ...

    def SetCoupleValue(self, IT1: int, IT2: int) -> None: ...

    def SetAngle(self, ang: float) -> None: ...

    def SetChainList(self, ChList: int) -> None: ...

    def CheckSameSP(self, SP: IntPolyh_StartPoint) -> int: ...

    @overload
    def Dump(self) -> None: ...

    @overload
    def Dump(self, i: int) -> None: ...

class IntPolyh_SectionLine:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, nn: int) -> None: ...

    @overload
    def __init__(self, theOther: IntPolyh_SectionLine) -> None: ...

    def Init(self, nn: int) -> None: ...

    def Value(self, nn: int) -> IntPolyh_StartPoint: ...

    def ChangeValue(self, nn: int) -> IntPolyh_StartPoint: ...

    def __getitem__(self, nn: int) -> IntPolyh_StartPoint: ...

    def Copy(self, Other: IntPolyh_SectionLine) -> IntPolyh_SectionLine: ...

    def GetN(self) -> int: ...

    def NbStartPoints(self) -> int: ...

    def IncrementNbStartPoints(self) -> None: ...

    def Destroy(self) -> None: ...

    def Dump(self) -> None: ...

    def Prepend(self, SP: IntPolyh_StartPoint) -> None: ...

class IntPolyh_ArrayOfSectionLines:
    """
    Class IntPolyh_Array (dynamic array of objects)

    1. The Array is dynamic array of objects.

    2. The Array uses NCollection_DynamicArray to store objects

    3. The Array can be created:
    3.1.  with initial length Nb=0.
    In this case Array should be initiated by invoke
    the method Init(Nb).
    3.2.  with initial length Nb>0.
    In this case Array is initiated automatically.

    The memory is allocated to store myNbAllocated oblects.

    4. The number of items that are stored in the Array (myNbItems)
    can be increased by calling the method:  IncrementNbItems().
    The objects are stored in already allocated memory if it is
    possible.
    Otherwise the new chunk of memory is allocated to store the
    objects.
    The size of chunk <aIncrement> can be defined during the creation
    of the Array.

    5. The start index of the Array is 0, The end index of the Array
    can be obtained by the method  NbItems();

    6. The contents of the element with index "i" can be queried or
    modified by the methods:  Value(i), ChangeValue(i), operator[](i)
    """

    @overload
    def __init__(self) -> None:
        """
        Constructor.
        @param aIncrement
        size of memory (in terms of Items) to expand the array
        """

    @overload
    def __init__(self, aN: int, aIncrement: int = 256) -> None:
        """
        Constructor.
        @param aN
        size of memory (in terms of Items) to allocate
        @param aIncrement
        size of memory (in terms of Items) to expand the array
        """

    @overload
    def __init__(self, theOther: IntPolyh_ArrayOfSectionLines) -> None: ...

    def Copy(self, aOther: IntPolyh_ArrayOfSectionLines) -> IntPolyh_ArrayOfSectionLines:
        """
        Copy
        @param
        aOther - the array to copy from
        @return
        the array
        """

    def Init(self, aN: int) -> None:
        """
        Init - allocate memory for <aN> items
        @param
        aN - the number of items to allocate the memory
        """

    def IncrementNbItems(self) -> None:
        """IncrementNbItems - increment the number of stored items"""

    def GetN(self) -> int:
        """
        GetN - returns the number of 'allocated' items
        @return
        the number of 'allocated' items
        """

    def NbItems(self) -> int:
        """
        NbItems - returns the number of stored items
        @return
        the number of stored items
        """

    def SetNbItems(self, aNb: int) -> None:
        """
        set the number of stored items
        @param aNb
        the number of stored items
        """

    def Value(self, aIndex: int) -> IntPolyh_SectionLine:
        """
        query the const value
        @param aIndex
        index
        @return
        the const item
        """

    def ChangeValue(self, aIndex: int) -> IntPolyh_SectionLine:
        """
        query the value
        @param aIndex
        index
        @return
        the item
        """

    def __getitem__(self, aIndex: int) -> IntPolyh_SectionLine:
        """
        query the value
        @param aIndex
        index
        @return
        the item
        """

    def Dump(self) -> None:
        """dump the contents"""

class IntPolyh_ArrayOfTangentZones:
    """
    Class IntPolyh_Array (dynamic array of objects)

    1. The Array is dynamic array of objects.

    2. The Array uses NCollection_DynamicArray to store objects

    3. The Array can be created:
    3.1.  with initial length Nb=0.
    In this case Array should be initiated by invoke
    the method Init(Nb).
    3.2.  with initial length Nb>0.
    In this case Array is initiated automatically.

    The memory is allocated to store myNbAllocated oblects.

    4. The number of items that are stored in the Array (myNbItems)
    can be increased by calling the method:  IncrementNbItems().
    The objects are stored in already allocated memory if it is
    possible.
    Otherwise the new chunk of memory is allocated to store the
    objects.
    The size of chunk <aIncrement> can be defined during the creation
    of the Array.

    5. The start index of the Array is 0, The end index of the Array
    can be obtained by the method  NbItems();

    6. The contents of the element with index "i" can be queried or
    modified by the methods:  Value(i), ChangeValue(i), operator[](i)
    """

    @overload
    def __init__(self) -> None:
        """
        Constructor.
        @param aIncrement
        size of memory (in terms of Items) to expand the array
        """

    @overload
    def __init__(self, aN: int, aIncrement: int = 256) -> None:
        """
        Constructor.
        @param aN
        size of memory (in terms of Items) to allocate
        @param aIncrement
        size of memory (in terms of Items) to expand the array
        """

    @overload
    def __init__(self, theOther: IntPolyh_ArrayOfTangentZones) -> None: ...

    def Copy(self, aOther: IntPolyh_ArrayOfTangentZones) -> IntPolyh_ArrayOfTangentZones:
        """
        Copy
        @param
        aOther - the array to copy from
        @return
        the array
        """

    def Init(self, aN: int) -> None:
        """
        Init - allocate memory for <aN> items
        @param
        aN - the number of items to allocate the memory
        """

    def IncrementNbItems(self) -> None:
        """IncrementNbItems - increment the number of stored items"""

    def GetN(self) -> int:
        """
        GetN - returns the number of 'allocated' items
        @return
        the number of 'allocated' items
        """

    def NbItems(self) -> int:
        """
        NbItems - returns the number of stored items
        @return
        the number of stored items
        """

    def SetNbItems(self, aNb: int) -> None:
        """
        set the number of stored items
        @param aNb
        the number of stored items
        """

    def Value(self, aIndex: int) -> IntPolyh_StartPoint:
        """
        query the const value
        @param aIndex
        index
        @return
        the const item
        """

    def ChangeValue(self, aIndex: int) -> IntPolyh_StartPoint:
        """
        query the value
        @param aIndex
        index
        @return
        the item
        """

    def __getitem__(self, aIndex: int) -> IntPolyh_StartPoint:
        """
        query the value
        @param aIndex
        index
        @return
        the item
        """

    def Dump(self) -> None:
        """dump the contents"""

class IntPolyh_ArrayOfTriangles:
    """
    Class IntPolyh_Array (dynamic array of objects)

    1. The Array is dynamic array of objects.

    2. The Array uses NCollection_DynamicArray to store objects

    3. The Array can be created:
    3.1.  with initial length Nb=0.
    In this case Array should be initiated by invoke
    the method Init(Nb).
    3.2.  with initial length Nb>0.
    In this case Array is initiated automatically.

    The memory is allocated to store myNbAllocated oblects.

    4. The number of items that are stored in the Array (myNbItems)
    can be increased by calling the method:  IncrementNbItems().
    The objects are stored in already allocated memory if it is
    possible.
    Otherwise the new chunk of memory is allocated to store the
    objects.
    The size of chunk <aIncrement> can be defined during the creation
    of the Array.

    5. The start index of the Array is 0, The end index of the Array
    can be obtained by the method  NbItems();

    6. The contents of the element with index "i" can be queried or
    modified by the methods:  Value(i), ChangeValue(i), operator[](i)
    """

    @overload
    def __init__(self) -> None:
        """
        Constructor.
        @param aIncrement
        size of memory (in terms of Items) to expand the array
        """

    @overload
    def __init__(self, aN: int, aIncrement: int = 256) -> None:
        """
        Constructor.
        @param aN
        size of memory (in terms of Items) to allocate
        @param aIncrement
        size of memory (in terms of Items) to expand the array
        """

    @overload
    def __init__(self, theOther: IntPolyh_ArrayOfTriangles) -> None: ...

    def Copy(self, aOther: IntPolyh_ArrayOfTriangles) -> IntPolyh_ArrayOfTriangles:
        """
        Copy
        @param
        aOther - the array to copy from
        @return
        the array
        """

    def Init(self, aN: int) -> None:
        """
        Init - allocate memory for <aN> items
        @param
        aN - the number of items to allocate the memory
        """

    def IncrementNbItems(self) -> None:
        """IncrementNbItems - increment the number of stored items"""

    def GetN(self) -> int:
        """
        GetN - returns the number of 'allocated' items
        @return
        the number of 'allocated' items
        """

    def NbItems(self) -> int:
        """
        NbItems - returns the number of stored items
        @return
        the number of stored items
        """

    def SetNbItems(self, aNb: int) -> None:
        """
        set the number of stored items
        @param aNb
        the number of stored items
        """

    def Value(self, aIndex: int) -> IntPolyh_Triangle:
        """
        query the const value
        @param aIndex
        index
        @return
        the const item
        """

    def ChangeValue(self, aIndex: int) -> IntPolyh_Triangle:
        """
        query the value
        @param aIndex
        index
        @return
        the item
        """

    def __getitem__(self, aIndex: int) -> IntPolyh_Triangle:
        """
        query the value
        @param aIndex
        index
        @return
        the item
        """

class IntPolyh_Couple:
    """
    The class represents the couple of indices with additional
    characteristics such as analyzed flag and an angle.
    In IntPolyh_MaillageAffinage algorithm the class is used as a
    couple of interfering triangles with the intersection angle.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theTriangle1: int, theTriangle2: int, theAngle: float = -2.0) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: IntPolyh_Couple) -> None: ...

    def FirstValue(self) -> int:
        """Returns the first index"""

    def SecondValue(self) -> int:
        """Returns the second index"""

    def IsAnalyzed(self) -> bool:
        """Returns TRUE if the couple has been analyzed"""

    def Angle(self) -> float:
        """Returns the angle"""

    def SetCoupleValue(self, theInd1: int, theInd2: int) -> None:
        """Sets the triangles"""

    def SetAnalyzed(self, theAnalyzed: bool) -> None:
        """Sets the analyzed flag"""

    def SetAngle(self, theAngle: float) -> None:
        """Sets the angle"""

    def IsEqual(self, theOther: IntPolyh_Couple) -> bool:
        """Returns true if the Couple is equal to <theOther>"""

    def __eq__(self, theOther: IntPolyh_Couple) -> bool:
        """Returns true if the Couple is equal to <theOther>"""

    def Dump(self, v: int) -> None: ...

    def __hash__(self) -> int: ...

class IntPolyh_Intersection:
    """
    API algorithm for intersection of two surfaces by intersection
    of their triangulations.

    Algorithm provides possibility to intersect surfaces as without
    the precomputed sampling as with it.

    If the numbers of sampling points are not given, it will build the
    net of 10x10 sampling points for each surface.

    The intersection is done inside constructors.
    Before obtaining the results of intersection it is necessary to check
    if intersection has been performed correctly. It can be done by calling
    the *IsDone()* method.

    The results of intersection are the intersection lines and points.
    """

    @overload
    def __init__(self, theS1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theS2: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None:
        """
        @name Constructors
        Constructor for intersection of two surfaces with default parameters.
        Performs intersection.
        """

    @overload
    def __init__(self, theS1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theNbSU1: int, theNbSV1: int, theS2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theNbSU2: int, theNbSV2: int) -> None:
        """
        Constructor for intersection of two surfaces with the given
        size of the sampling nets:
        - <theNbSU1> x <theNbSV1> - for the first surface <theS1>;
        - <theNbSU2> x <theNbSV2> - for the second surface <theS2>.
        Performs intersection.
        """

    @overload
    def __init__(self, theS1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theUPars1: nanoocp.NCollection.NCollection_Array1[float], theVPars1: nanoocp.NCollection.NCollection_Array1[float], theS2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theUPars2: nanoocp.NCollection.NCollection_Array1[float], theVPars2: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Constructor for intersection of two surfaces with the precomputed sampling.
        Performs intersection.
        """

    @overload
    def __init__(self, theOther: IntPolyh_Intersection) -> None: ...

    def IsDone(self) -> bool:
        """
        @name Getting the results
        Returns state of the operation
        """

    def IsParallel(self) -> bool:
        """Returns state of the operation"""

    def NbSectionLines(self) -> int:
        """Returns the number of section lines"""

    def NbPointsInLine(self, IndexLine: int) -> int:
        """Returns the number of points in the given line"""

    def NbTangentZones(self) -> int: ...

    def NbPointsInTangentZone(self, arg0: int) -> int:
        """Returns number of points in tangent zone"""

    def GetLinePoint(self, IndexLine: int, IndexPoint: int) -> tuple[float, float, float, float, float, float, float, float]:
        """Gets the parameters of the point in section line"""

    def GetTangentZonePoint(self, IndexLine: int, IndexPoint: int) -> tuple[float, float, float, float, float, float, float]:
        """Gets the parameters of the point in tangent zone"""

class IntPolyh_MaillageAffinage:
    """
    Low-level algorithm to compute intersection of the surfaces
    by computing the intersection of their triangulations.
    """

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, PRINT: int) -> None: ...

    @overload
    def __init__(self, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, NbSU1: int, NbSV1: int, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, NbSU2: int, NbSV2: int, PRINT: int) -> None: ...

    @overload
    def __init__(self, theOther: IntPolyh_MaillageAffinage) -> None: ...

    def MakeSampling(self, SurfID: int, theUPars: nanoocp.NCollection.NCollection_Array1[float], theVPars: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Makes the sampling of the surface -
        Fills the arrays with the parametric values of the sampling points (triangulation nodes).
        """

    @overload
    def FillArrayOfPnt(self, SurfID: int) -> None:
        """
        Computes points on one surface and fills an array of points;
        standard (default) method
        """

    @overload
    def FillArrayOfPnt(self, SurfID: int, isShiftFwd: bool) -> None:
        """
        isShiftFwd flag is added. The purpose is to define shift
        of points along normal to the surface in this point. The
        shift length represents maximal deflection of triangulation.
        The direction (forward or reversed regarding to normal
        direction) is defined by isShiftFwd flag.
        Compute points on one surface and fill an array of points;
        advanced method
        """

    @overload
    def FillArrayOfPnt(self, SurfID: int, isShiftFwd: bool, thePoints: IntPolyh_ArrayOfPointNormal, theUPars: nanoocp.NCollection.NCollection_Array1[float], theVPars: nanoocp.NCollection.NCollection_Array1[float], theDeflTol: float) -> None:
        """
        Fills the array of points for the surface taking into account the shift
        """

    @overload
    def CommonBox(self) -> None:
        """
        Looks for the common box of the surfaces and marks the points
        of the surfaces inside that common box for possible intersection
        """

    @overload
    def CommonBox(self, B1: nanoocp.Bnd.Bnd_Box, B2: nanoocp.Bnd.Bnd_Box) -> tuple[float, float, float, float, float, float]:
        """
        Compute the common box which is the intersection
        of the two bounding boxes, and mark the points of
        the two surfaces that are inside.
        """

    def FillArrayOfEdges(self, SurfID: int) -> None:
        """Compute edges from the array of points"""

    def FillArrayOfTriangles(self, SurfID: int) -> None:
        """
        Compute triangles from the array of points, and
        mark the triangles that use marked points by the
        CommonBox function.
        """

    def CommonPartRefinement(self) -> None:
        """Refine systematicaly all marked triangles of both surfaces"""

    def LocalSurfaceRefinement(self, SurfId: int) -> None:
        """Refine systematicaly all marked triangles of ONE surface"""

    def ComputeDeflections(self, SurfID: int) -> None:
        """
        Compute deflection for all triangles of one
        surface,and sort min and max of deflections
        """

    def TrianglesDeflectionsRefinementBSB(self) -> None:
        """
        Refine both surfaces using BoundSortBox as
        rejection. The criterions used to refine a
        triangle are: The deflection The size of the
        bounding boxes (one surface may be very small
        compared to the other)
        """

    def TriContact(self, P1: IntPolyh_Point, P2: IntPolyh_Point, P3: IntPolyh_Point, Q1: IntPolyh_Point, Q2: IntPolyh_Point, Q3: IntPolyh_Point) -> tuple[int, float]:
        """
        This function checks if two triangles are in contact or not,
        return 1 if yes, return 0 if not.
        """

    def TriangleEdgeContact(self, TriSurfID: int, EdgeIndice: int, Tri1: IntPolyh_Triangle, Tri2: IntPolyh_Triangle, P1: IntPolyh_Point, P2: IntPolyh_Point, P3: IntPolyh_Point, C1: IntPolyh_Point, C2: IntPolyh_Point, C3: IntPolyh_Point, Pe1: IntPolyh_Point, Pe2: IntPolyh_Point, E: IntPolyh_Point, N: IntPolyh_Point, SP1: IntPolyh_StartPoint, SP2: IntPolyh_StartPoint) -> int: ...

    def StartingPointsResearch(self, T1: int, T2: int, SP1: IntPolyh_StartPoint, SP2: IntPolyh_StartPoint) -> int:
        """
        From two triangles compute intersection points.
        If we found more than two intersection points
        that means that those triangles are coplanar
        """

    def NextStartingPointsResearch(self, T1: int, T2: int, SPInit: IntPolyh_StartPoint, SPNext: IntPolyh_StartPoint) -> int:
        """
        from two triangles and an intersection point I
        search the other point (if it exists).
        This function is used by StartPointChain
        """

    def TriangleCompare(self) -> int:
        """
        Analyse each couple of triangles from the two -- array of triangles,
        to see if they are in contact, and compute the incidence.
        Then put couples in contact in the array of couples
        """

    def StartPointsChain(self, TSectionLines: IntPolyh_ArrayOfSectionLines, TTangentZones: IntPolyh_ArrayOfTangentZones) -> int:
        """
        Loop on the array of couples. Compute StartPoints.
        Try to chain the StartPoints into SectionLines or
        put the point in the ArrayOfTangentZones if
        chaining it, is not possible.
        """

    def GetNextChainStartPoint(self, SPInit: IntPolyh_StartPoint, SPNext: IntPolyh_StartPoint, MySectionLine: IntPolyh_SectionLine, TTangentZones: IntPolyh_ArrayOfTangentZones, Prepend: bool = False) -> int:
        """
        Mainly used by StartPointsChain(), this function
        try to compute the next StartPoint.
        """

    def GetArrayOfPoints(self, SurfID: int) -> IntPolyh_ArrayOfPoints: ...

    def GetArrayOfEdges(self, SurfID: int) -> IntPolyh_ArrayOfEdges: ...

    def GetArrayOfTriangles(self, SurfID: int) -> IntPolyh_ArrayOfTriangles: ...

    def GetBox(self, SurfID: int) -> nanoocp.Bnd.Bnd_Box: ...

    def GetCouples(self) -> nanoocp.NCollection.NCollection_List[nanoocp.IntPolyh.IntPolyh_Couple]:
        """This method returns list of couples of contact triangles."""

    def SetEnlargeZone(self, EnlargeZone: bool) -> None: ...

    def GetEnlargeZone(self) -> bool: ...

    def GetMinDeflection(self, SurfID: int) -> float:
        """returns FlecheMin"""

    def GetMaxDeflection(self, SurfID: int) -> float:
        """returns FlecheMax"""

class IntPolyh_Tools:
    """The class provides tools for surface sampling."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntPolyh_Tools) -> None: ...

    @staticmethod
    def IsEnlargePossible(theSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> tuple[bool, bool]:
        """Checks if the surface can be enlarged in U or V direction."""

    @staticmethod
    def MakeSampling(theSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theNbSU: int, theNbSV: int, theEnlargeZone: bool, theUPars: nanoocp.NCollection.NCollection_Array1[float], theVPars: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Makes the sampling of the given surface <theSurf>
        making the net of <theNbSU> x <theNbSV> sampling points.
        The flag <theEnlargeZone> controls the enlargement of the
        sampling zone on the surface.
        The parameters of the sampling points are stored into
        <theUPars> and <theVPars> arrays.
        """

    @staticmethod
    def ComputeDeflection(theSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theUPars: nanoocp.NCollection.NCollection_Array1[float], theVPars: nanoocp.NCollection.NCollection_Array1[float]) -> float:
        """
        Computes the deflection tolerance on the surface for the given sampling.
        """

    @staticmethod
    def FillArrayOfPointNormal(theSurf: nanoocp.Adaptor3d.Adaptor3d_Surface | None, theUPars: nanoocp.NCollection.NCollection_Array1[float], theVPars: nanoocp.NCollection.NCollection_Array1[float], thePoints: IntPolyh_ArrayOfPointNormal) -> None:
        """
        Fills the array <thePoints> with the points (triangulation nodes) on the surface
        and normal directions of the surface in these points.
        """

class IntPolyh_Triangle:
    """
    The class represents the triangle built from three IntPolyh points
    and three IntPolyh edges.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, thePoint1: int, thePoint2: int, thePoint3: int) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: IntPolyh_Triangle) -> None: ...

    def FirstPoint(self) -> int:
        """Returns the first point"""

    def SecondPoint(self) -> int:
        """Returns the second point"""

    def ThirdPoint(self) -> int:
        """Returns the third point"""

    def FirstEdge(self) -> int:
        """Returns the first edge"""

    def FirstEdgeOrientation(self) -> int:
        """Returns the orientation of the first edge"""

    def SecondEdge(self) -> int:
        """Returns the second edge"""

    def SecondEdgeOrientation(self) -> int:
        """Returns the orientation of the second edge"""

    def ThirdEdge(self) -> int:
        """Returns the third edge"""

    def ThirdEdgeOrientation(self) -> int:
        """Returns the orientation of the third edge"""

    def Deflection(self) -> float:
        """Returns the deflection of the triangle"""

    def IsIntersectionPossible(self) -> bool:
        """Returns possibility of the intersection"""

    def HasIntersection(self) -> bool:
        """Returns true if the triangle has interfered the other triangle"""

    def IsDegenerated(self) -> bool:
        """Returns the Degenerated flag"""

    def SetFirstPoint(self, thePoint: int) -> None:
        """Sets the first point"""

    def SetSecondPoint(self, thePoint: int) -> None:
        """Sets the second point"""

    def SetThirdPoint(self, thePoint: int) -> None:
        """Sets the third point"""

    def SetFirstEdge(self, theEdge: int, theEdgeOrientation: int) -> None:
        """Sets the first edge"""

    def SetSecondEdge(self, theEdge: int, theEdgeOrientation: int) -> None:
        """Sets the second edge"""

    def SetThirdEdge(self, theEdge: int, theEdgeOrientation: int) -> None:
        """Sets the third edge"""

    def SetDeflection(self, theDeflection: float) -> None:
        """Sets the deflection"""

    def SetIntersectionPossible(self, theIP: bool) -> None:
        """Sets the flag of possibility of intersection"""

    def SetIntersection(self, theInt: bool) -> None:
        """Sets the flag of intersection"""

    def SetDegenerated(self, theDegFlag: bool) -> None:
        """Sets the degenerated flag"""

    def GetEdgeNumber(self, theEdgeIndex: int) -> int:
        """Gets the edge number by the index"""

    def SetEdge(self, theEdgeIndex: int, theEdgeNumber: int) -> None:
        """Sets the edge by the index"""

    def GetEdgeOrientation(self, theEdgeIndex: int) -> int:
        """Gets the edges orientation by the index"""

    def SetEdgeOrientation(self, theEdgeIndex: int, theEdgeOrientation: int) -> None:
        """Sets the edges orientation by the index"""

    def ComputeDeflection(self, theSurface: nanoocp.Adaptor3d.Adaptor3d_Surface | None, thePoints: IntPolyh_ArrayOfPoints) -> float:
        """Computes the deflection for the triangle"""

    def GetNextTriangle(self, theTriangle: int, theEdgeNum: int, TEdges: IntPolyh_ArrayOfEdges) -> int:
        """Gets the adjacent triangle"""

    def MiddleRefinement(self, theTriangleNumber: int, theSurface: nanoocp.Adaptor3d.Adaptor3d_Surface | None, TPoints: IntPolyh_ArrayOfPoints, TTriangles: IntPolyh_ArrayOfTriangles, TEdges: IntPolyh_ArrayOfEdges) -> None:
        """Splits the triangle on two to decrease its deflection"""

    def MultipleMiddleRefinement(self, theRefineCriterion: float, theBox: nanoocp.Bnd.Bnd_Box, theTriangleNumber: int, theSurface: nanoocp.Adaptor3d.Adaptor3d_Surface | None, TPoints: IntPolyh_ArrayOfPoints, TTriangles: IntPolyh_ArrayOfTriangles, TEdges: IntPolyh_ArrayOfEdges) -> None:
        """
        Splits the current triangle and new triangles until the refinement
        criterion is not achieved
        """

    def LinkEdges2Triangle(self, TEdges: IntPolyh_ArrayOfEdges, theEdge1: int, theEdge2: int, theEdge3: int) -> None:
        """Links edges to triangle"""

    def SetEdgeAndOrientation(self, theEdge: IntPolyh_Edge, theEdgeIndex: int) -> None:
        """Sets the appropriate edge and orientation for the triangle."""

    def BoundingBox(self, thePoints: IntPolyh_ArrayOfPoints) -> nanoocp.Bnd.Bnd_Box:
        """Returns the bounding box of the triangle."""

    def Dump(self, v: int) -> None:
        """Dumps the contents of the triangle."""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.IntPolyh
IntPolyh_ListOfCouples = nanoocp.NCollection.NCollection_List[nanoocp.IntPolyh.IntPolyh_Couple]
