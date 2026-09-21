"""OCCT package IMeshData (toolkit TKMesh)"""

import enum
from typing import TypeAlias, overload

import nanoocp.BRepAdaptor
import nanoocp.BRepMesh
import nanoocp.Bnd
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp
import nanoocp.IMeshData
import nanoocp.TColStd
import nanoocp.TopTools


MEMORY_BLOCK_SIZE_HUGE: int = 524288

class IMeshData_Status(enum.IntEnum):
    """Enumerates statuses used to notify state of discrete model."""

    IMeshData_NoError = 0

    IMeshData_OpenWire = 1

    IMeshData_SelfIntersectingWire = 2

    IMeshData_Failure = 4

    IMeshData_ReMesh = 8

    IMeshData_UnorientedWire = 16

    IMeshData_TooFewPoints = 32

    IMeshData_Outdated = 64

    IMeshData_Reused = 128

    IMeshData_UserBreak = 256

IMeshData_NoError: IMeshData_Status = IMeshData_Status.IMeshData_NoError

IMeshData_OpenWire: IMeshData_Status = IMeshData_Status.IMeshData_OpenWire

IMeshData_SelfIntersectingWire: IMeshData_Status = IMeshData_Status.IMeshData_SelfIntersectingWire

IMeshData_Failure: IMeshData_Status = IMeshData_Status.IMeshData_Failure

IMeshData_ReMesh: IMeshData_Status = IMeshData_Status.IMeshData_ReMesh

IMeshData_UnorientedWire: IMeshData_Status = IMeshData_Status.IMeshData_UnorientedWire

IMeshData_TooFewPoints: IMeshData_Status = IMeshData_Status.IMeshData_TooFewPoints

IMeshData_Outdated: IMeshData_Status = IMeshData_Status.IMeshData_Outdated

IMeshData_Reused: IMeshData_Status = IMeshData_Status.IMeshData_Reused

IMeshData_UserBreak: IMeshData_Status = IMeshData_Status.IMeshData_UserBreak

class IMeshData_ParametersList(nanoocp.Standard.Standard_Transient):
    """Interface class representing list of parameters on curve."""

    def GetParameter(self, theIndex: int) -> float:
        """Returns parameter with the given index."""

    def SetGetParameter(self, theIndex: int, theValue: float) -> None:
        """
        Python addition: sets the value GetParameter(theIndex) returns by reference in C++.
        """

    def ParametersNb(self) -> int:
        """Returns number of parameters."""

    def Clear(self, isKeepEndPoints: bool) -> None:
        """Clears parameters list."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshData_Curve(IMeshData_ParametersList):
    """
    Interface class representing discrete 3d curve of edge.
    Indexation of points starts from zero.
    """

    def InsertPoint(self, thePosition: int, thePoint: nanoocp.gp.gp_Pnt, theParamOnPCurve: float) -> None:
        """Inserts new discretization point at the given position."""

    def AddPoint(self, thePoint: nanoocp.gp.gp_Pnt, theParamOnCurve: float) -> None:
        """Adds new discretization point to curve."""

    def GetPoint(self, theIndex: int) -> nanoocp.gp.gp_Pnt:
        """Returns discretization point with the given index."""

    def RemovePoint(self, theIndex: int) -> None:
        """Removes point with the given index."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshData_Shape(nanoocp.Standard.Standard_Transient):
    """
    Interface class representing model with associated TopoDS_Shape.
    Intended for inheritance by structures and algorithms keeping
    reference TopoDS_Shape.
    """

    def __init__(self, theOther: IMeshData_Shape) -> None: ...

    def SetShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Assigns shape to discrete shape."""

    def GetShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns shape assigned to discrete shape."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshData_TessellatedShape(IMeshData_Shape):
    """Interface class representing shaped model with deflection."""

    def __init__(self, theOther: IMeshData_TessellatedShape) -> None: ...

    def GetDeflection(self) -> float:
        """Gets deflection value for the discrete model."""

    def SetDeflection(self, theValue: float) -> None:
        """Sets deflection value for the discrete model."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshData_StatusOwner:
    """Extension interface class providing status functionality."""

    def __init__(self, theOther: IMeshData_StatusOwner) -> None: ...

    def IsEqual(self, theValue: IMeshData_Status) -> bool:
        """Returns true in case if status is strictly equal to the given value."""

    def IsSet(self, theValue: IMeshData_Status) -> bool:
        """Returns true in case if status is set."""

    def SetStatus(self, theValue: IMeshData_Status) -> None:
        """Adds status to status flags of a face."""

    def UnsetStatus(self, theValue: IMeshData_Status) -> None:
        """Adds status to status flags of a face."""

    def GetStatusMask(self) -> int:
        """Returns complete status mask."""

class IMeshData_Face(IMeshData_TessellatedShape):
    """
    Interface class representing discrete model of a face.
    Face model contains one or several wires.
    First wire is always outer one.
    """

    def WiresNb(self) -> int:
        """Returns number of wires."""

    def AddWire(self, theWire: nanoocp.TopoDS.TopoDS_Wire, theEdgeNb: int = 0) -> IMeshData_Wire:
        """Adds wire to discrete model of face."""

    def GetWire(self, theIndex: int) -> IMeshData_Wire:
        """Returns discrete edge with the given index."""

    def GetSurface(self) -> nanoocp.BRepAdaptor.BRepAdaptor_Surface:
        """Returns face's surface."""

    def GetFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns TopoDS_Face attached to model."""

    def IsValid(self) -> bool:
        """Returns whether the face discrete model is valid."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshData_PCurve(IMeshData_ParametersList):
    """
    Interface class representing pcurve of edge associated with discrete face.
    Indexation of points starts from zero.
    """

    def InsertPoint(self, thePosition: int, thePoint: nanoocp.gp.gp_Pnt2d, theParamOnPCurve: float) -> None:
        """Inserts new discretization point at the given position."""

    def AddPoint(self, thePoint: nanoocp.gp.gp_Pnt2d, theParamOnPCurve: float) -> None:
        """Adds new discretization point to pcurve."""

    def GetPoint(self, theIndex: int) -> nanoocp.gp.gp_Pnt2d:
        """Returns discretization point with the given index."""

    def GetIndex(self, theIndex: int) -> int:
        """
        Returns index in mesh corresponded to discretization point with the given index.
        """

    def SetGetIndex(self, theIndex: int, theValue: int) -> None:
        """
        Python addition: sets the value GetIndex(theIndex) returns by reference in C++.
        """

    def RemovePoint(self, theIndex: int) -> None:
        """Removes point with the given index."""

    def IsForward(self) -> bool:
        """Returns forward flag of this pcurve."""

    def IsInternal(self) -> bool:
        """Returns internal flag of this pcurve."""

    def GetOrientation(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Returns orientation of the edge associated with current pcurve."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshData_Edge(IMeshData_TessellatedShape):
    """Interface class representing discrete model of an edge."""

    def GetEdge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns TopoDS_Edge attached to model."""

    def PCurvesNb(self) -> int:
        """Returns number of pcurves assigned to current edge."""

    def GetPCurve(self, theIndex: int) -> IMeshData_PCurve:
        """Returns pcurve with the given index."""

    def Clear(self, isKeepEndPoints: bool) -> None:
        """Clears curve and all pcurves assigned to the edge from discretization."""

    def IsFree(self) -> bool:
        """
        Returns true in case if the edge is free one, i.e. it does not have pcurves.
        """

    def SetCurve(self, theCurve: IMeshData_Curve | None) -> None:
        """Sets 3d curve associated with current edge."""

    def GetCurve(self) -> IMeshData_Curve:
        """Returns 3d curve associated with current edge."""

    def GetAngularDeflection(self) -> float:
        """Gets value of angular deflection for the discrete model."""

    def SetAngularDeflection(self, theValue: float) -> None:
        """Sets value of angular deflection for the discrete model."""

    def GetSameParam(self) -> bool:
        """
        Returns same param flag.
        By default equals to flag stored in topological shape.
        """

    def SetSameParam(self, theValue: bool) -> None:
        """Updates same param flag."""

    def GetSameRange(self) -> bool:
        """
        Returns same range flag.
        By default equals to flag stored in topological shape.
        """

    def SetSameRange(self, theValue: bool) -> None:
        """Updates same range flag."""

    def GetDegenerated(self) -> bool:
        """
        Returns degenerative flag.
        By default equals to flag stored in topological shape.
        """

    def SetDegenerated(self, theValue: bool) -> None:
        """Updates degenerative flag."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshData_Model(IMeshData_Shape):
    """Interface class representing discrete model of a shape."""

    def GetMaxSize(self) -> float:
        """Returns maximum size of shape model."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def FacesNb(self) -> int:
        """
        @name discrete faces
        Returns number of faces in discrete model.
        """

    def AddFace(self, theFace: nanoocp.TopoDS.TopoDS_Face) -> IMeshData_Face:
        """Adds new face to shape model."""

    def GetFace(self, theIndex: int) -> IMeshData_Face:
        """Gets model's face with the given index."""

    def EdgesNb(self) -> int:
        """
        @name discrete edges
        Returns number of edges in discrete model.
        """

    def AddEdge(self, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> IMeshData_Edge:
        """Adds new edge to shape model."""

    def GetEdge(self, theIndex: int) -> IMeshData_Edge:
        """Gets model's edge with the given index."""

class IMeshData_Wire(IMeshData_TessellatedShape):
    """
    Interface class representing discrete model of a wire.
    Wire should represent an ordered set of edges.
    """

    def GetWire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns TopoDS_Face attached to model."""

    def EdgesNb(self) -> int:
        """Returns number of edges."""

    def GetEdgeOrientation(self, theIndex: int) -> nanoocp.TopAbs.TopAbs_Orientation:
        """
        Returns True if orientation of discrete edge with the given index is forward.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshData_ParametersListArrayAdaptor__Handle_IMeshData_Curve(nanoocp.Standard.Standard_Transient):
    """
    Auxiliary tool representing adaptor interface for child classes of
    IMeshData_ParametersList to be used in tools working on NCollection_Array structure.
    """

    def __init__(self, theParameters: IMeshData_Curve) -> None:
        """Constructor. Initializes tool by the given parameters."""

    def Lower(self) -> int:
        """Returns lower index in parameters array."""

    def Upper(self) -> int:
        """Returns upper index in parameters array."""

    def Value(self, theIndex: int) -> float:
        """Returns value of the given index."""

class NCollection_UBTreeFiller__int__Bnd_Box2d:
    """
    This class is used to fill an UBTree in a random order.
    The quality of a tree is much better (from the point of view of
    the search time) if objects are added to it in a random order to
    avoid adding a chain of neerby objects one following each other.

    This class collects objects to be added, and then add them to the tree
    in a random order.
    """

    @overload
    def __init__(self, theTree: "NCollection_UBTree<int, Bnd_Box2d>", theAlloc: nanoocp.NCollection.NCollection_BaseAllocator | None = None, isFullRandom: bool = True) -> None:
        """
        Constructor.
        @param theTree
        Tree instance that is to be filled.
        @param theAlloc
        Allocator for the Filler data.
        @param isFullRandom
        Takes effect when the number of items is large (order of 50,000). When
        it is True, the code uses the maximal randomization allowing a better
        balanced tree. If False, the randomization/tree balance are worse but
        the tree filling is faster due to better utilisation of CPU L1/L2 cache.
        """

    @overload
    def __init__(self, theOther: NCollection_UBTreeFiller__int__Bnd_Box2d) -> None: ...

    def Add(self, theObj: int, theBnd: nanoocp.Bnd.Bnd_Box2d) -> None:
        """Adds a pair (theObj, theBnd) to my sequence"""

    def Fill(self) -> int:
        """
        Fills the tree with the objects from my sequence. This method clears
        the internal buffer of added items making sure that no item would be added
        twice.
        @return
        the number of objects added to the tree.
        """

    def Reset(self) -> None:
        """
        Remove all data from Filler, partculary if the Tree no more needed
        so the destructor of this Filler should not populate the useless Tree.
        """

    def CheckTree(self) -> tuple[int, object]:
        """
        Check the filled tree for the total number of items and the balance
        outputting these results to std::ostream.
        @return
        the tree size (the same value is returned by method Fill()).
        """

class NCollection_OccAllocator__gp_Pnt:
    """
    Implements allocator requirements as defined in ISO C++ Standard 2003, section 20.1.5.
    The allocator uses a standard OCCT mechanism for memory
    allocation and deallocation. It can be used with standard
    containers (std::vector, std::map, etc.) to take advantage of OCCT memory optimizations.

    Example of use:
    \\code
    NCollection_OccAllocator<TopoDS_Shape> anSAllocator();
    std::list<TopoDS_Shape, NCollection_OccAllocator<TopoDS_Shape>> aList(anSAllocator);
    TopoDS_Solid aSolid = BRepPrimAPI_MakeBox(10., 20., 30.);
    aList.push_back(aSolid);
    \\endcode
    """

    @overload
    def __init__(self) -> None:
        """
        Constructor.
        Creates an object using the default Open CASCADE allocation mechanism, i.e., which uses
        Standard::Allocate() and Standard::Free() underneath.
        """

    @overload
    def __init__(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: NCollection_OccAllocator__gp_Pnt) -> None:
        """Constructor."""

    def SetAllocator(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    def Allocator(self) -> nanoocp.NCollection.NCollection_BaseAllocator: ...

    def deallocate(self, thePnt: nanoocp.gp.gp_Pnt, arg1: int) -> None:
        """Frees previously allocated memory."""

    def max_size(self) -> int:
        """Estimate maximum array size"""

    def __eq__(self, theOther: NCollection_OccAllocator__gp_Pnt) -> bool: ...

    def __ne__(self, theOther: NCollection_OccAllocator__gp_Pnt) -> bool: ...

class NCollection_OccAllocator__gp_Pnt2d:
    """
    Implements allocator requirements as defined in ISO C++ Standard 2003, section 20.1.5.
    The allocator uses a standard OCCT mechanism for memory
    allocation and deallocation. It can be used with standard
    containers (std::vector, std::map, etc.) to take advantage of OCCT memory optimizations.

    Example of use:
    \\code
    NCollection_OccAllocator<TopoDS_Shape> anSAllocator();
    std::list<TopoDS_Shape, NCollection_OccAllocator<TopoDS_Shape>> aList(anSAllocator);
    TopoDS_Solid aSolid = BRepPrimAPI_MakeBox(10., 20., 30.);
    aList.push_back(aSolid);
    \\endcode
    """

    @overload
    def __init__(self) -> None:
        """
        Constructor.
        Creates an object using the default Open CASCADE allocation mechanism, i.e., which uses
        Standard::Allocate() and Standard::Free() underneath.
        """

    @overload
    def __init__(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: NCollection_OccAllocator__gp_Pnt2d) -> None:
        """Constructor."""

    def SetAllocator(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    def Allocator(self) -> nanoocp.NCollection.NCollection_BaseAllocator: ...

    def deallocate(self, thePnt: nanoocp.gp.gp_Pnt2d, arg1: int) -> None:
        """Frees previously allocated memory."""

    def max_size(self) -> int:
        """Estimate maximum array size"""

    def __eq__(self, theOther: NCollection_OccAllocator__gp_Pnt2d) -> bool: ...

    def __ne__(self, theOther: NCollection_OccAllocator__gp_Pnt2d) -> bool: ...

class NCollection_OccAllocator__double:
    """
    Implements allocator requirements as defined in ISO C++ Standard 2003, section 20.1.5.
    The allocator uses a standard OCCT mechanism for memory
    allocation and deallocation. It can be used with standard
    containers (std::vector, std::map, etc.) to take advantage of OCCT memory optimizations.

    Example of use:
    \\code
    NCollection_OccAllocator<TopoDS_Shape> anSAllocator();
    std::list<TopoDS_Shape, NCollection_OccAllocator<TopoDS_Shape>> aList(anSAllocator);
    TopoDS_Solid aSolid = BRepPrimAPI_MakeBox(10., 20., 30.);
    aList.push_back(aSolid);
    \\endcode
    """

    @overload
    def __init__(self) -> None:
        """
        Constructor.
        Creates an object using the default Open CASCADE allocation mechanism, i.e., which uses
        Standard::Allocate() and Standard::Free() underneath.
        """

    @overload
    def __init__(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: NCollection_OccAllocator__double) -> None:
        """Constructor."""

    def SetAllocator(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    def Allocator(self) -> nanoocp.NCollection.NCollection_BaseAllocator: ...

    def deallocate(self, thePnt: float, arg1: int) -> None:
        """Frees previously allocated memory."""

    def max_size(self) -> int:
        """Estimate maximum array size"""

    def __eq__(self, theOther: NCollection_OccAllocator__double) -> bool: ...

    def __ne__(self, theOther: NCollection_OccAllocator__double) -> bool: ...

class NCollection_OccAllocator__int:
    """
    Implements allocator requirements as defined in ISO C++ Standard 2003, section 20.1.5.
    The allocator uses a standard OCCT mechanism for memory
    allocation and deallocation. It can be used with standard
    containers (std::vector, std::map, etc.) to take advantage of OCCT memory optimizations.

    Example of use:
    \\code
    NCollection_OccAllocator<TopoDS_Shape> anSAllocator();
    std::list<TopoDS_Shape, NCollection_OccAllocator<TopoDS_Shape>> aList(anSAllocator);
    TopoDS_Solid aSolid = BRepPrimAPI_MakeBox(10., 20., 30.);
    aList.push_back(aSolid);
    \\endcode
    """

    @overload
    def __init__(self) -> None:
        """
        Constructor.
        Creates an object using the default Open CASCADE allocation mechanism, i.e., which uses
        Standard::Allocate() and Standard::Free() underneath.
        """

    @overload
    def __init__(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: NCollection_OccAllocator__int) -> None:
        """Constructor."""

    def SetAllocator(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    def Allocator(self) -> nanoocp.NCollection.NCollection_BaseAllocator: ...

    def deallocate(self, thePnt: int, arg1: int) -> None:
        """Frees previously allocated memory."""

    def max_size(self) -> int:
        """Estimate maximum array size"""

    def __eq__(self, theOther: NCollection_OccAllocator__int) -> bool: ...

    def __ne__(self, theOther: NCollection_OccAllocator__int) -> bool: ...

class NCollection_CellFilter__BRepMesh_CircleInspector:
    """
    A data structure for sorting geometric objects (called targets) in
    n-dimensional space into cells, with associated algorithm for fast checking
    of coincidence (overlapping, intersection, etc.) with other objects
    (called here bullets).

    Description

    The algorithm is based on hash map, thus it has linear time of initialization
    (O(N) where N is number of cells covered by added targets) and constant-time
    search for one bullet (more precisely, O(M) where M is number of cells covered
    by the bullet).

    The idea behind the algorithm is to separate each coordinate of the space
    into equal-size cells. Note that this works well when cell size is
    approximately equal to the characteristic size of the involved objects
    (targets and bullets; including tolerance eventually used for coincidence
    check).

    Usage

    The target objects to be searched are added to the tool by methods Add();
    each target is classified as belonging to some cell(s). The data on cells
    (list of targets found in each one) are stored in the hash map with key being
    cumulative index of the cell by all coordinates.
    Thus the time needed to find targets in some cell is O(1) * O(number of
    targets in the cell).

    As soon as all the targets are added, the algorithm is ready to check for
    coincidence.
    To find the targets coincident with any given bullet, it checks all the
    candidate targets in the cell(s) covered by the bullet object
    (methods Inspect()).

    The methods Add() and Inspect() have two flavours each: one accepts
    single point identifying one cell, another accept two points specifying
    the range of cells. It should be noted that normally at least one of these
    methods is called as for range of cells: either due to objects having non-
    zero size, or in order to account for the tolerance when objects are points.

    The set of targets can be modified during the process: new targets can be
    added by Add(), existing targets can be removed by Remove().

    Implementation

    The algorithm is implemented as template class, thus it is capable to
    work with objects of any type. The only argument of the template should be
    the specific class providing all necessary features required by the
    algorithm:

    - typedef "Target" defining type of target objects.
    This type must have copy constructor

    - typedef "Point" defining type of geometrical points used

    - static constexpr int Dimension whose value must be dimension of the point

    - method Coord() returning value of the i-th coordinate of the point:

    static double Coord (int i, const Point& thePnt);

    Note that index i is from 0 to Dimension-1.

    - method IsEqual() used by Remove() to identify objects to be removed:

    bool IsEqual (const Target& theT1, const Target& theT2);

    - method Inspect() performing necessary actions on the candidate target
    object (usually comparison with the currently checked bullet object):

    NCollection_CellFilter_Action Inspect (const Target& theObject);

    The returned value can be used to command CellFilter
    to remove the inspected item from the current cell; this allows
    to exclude the items that has been processed and are not needed any
    more in further search (for better performance).

    Note that method Inspect() can be const and/or virtual.
    """

    @overload
    def __init__(self, theCellSize: float = 0.0, theAlloc: nanoocp.NCollection.NCollection_IncAllocator | None = None) -> None:
        """Constructor when dimension count is known at compilation time."""

    @overload
    def __init__(self, theDim: int, theCellSize: float = 0.0, theAlloc: nanoocp.NCollection.NCollection_IncAllocator | None = None) -> None:
        """
        Constructor; initialized by dimension count and cell size.

        Note: the cell size must be ensured to be greater than
        maximal coordinate of the involved points divided by INT_MAX,
        in order to avoid integer overflow of cell index.

        By default cell size is 0, which is invalid; thus if default
        constructor is used, the tool must be initialized later with
        appropriate cell size by call to Reset()
        Constructor when dimension count is unknown at compilation time.
        """

    @overload
    def Reset(self, theCellSize: float, theAlloc: nanoocp.NCollection.NCollection_IncAllocator | None = None) -> None:
        """Clear the data structures, set new cell size and allocator"""

    @overload
    def Reset(self, theCellSize: nanoocp.NCollection.NCollection_Array1[float], theAlloc: nanoocp.NCollection.NCollection_IncAllocator | None = None) -> None:
        """Clear the data structures and set new cell sizes and allocator"""

    @overload
    def Add(self, theTarget: int, thePnt: nanoocp.gp.gp_XY) -> None:
        """
        Adds a target object for further search at a point (into only one cell)
        """

    @overload
    def Add(self, theTarget: int, thePntMin: nanoocp.gp.gp_XY, thePntMax: nanoocp.gp.gp_XY) -> None:
        """
        Adds a target object for further search in the range of cells
        defined by two points (the first point must have all coordinates equal or
        less than the same coordinate of the second point)
        """

    @overload
    def Remove(self, theTarget: int, thePnt: nanoocp.gp.gp_XY) -> None:
        """
        Find a target object at a point and remove it from the structures.
        For usage of this method "operator ==" should be defined for Target.
        """

    @overload
    def Remove(self, theTarget: int, thePntMin: nanoocp.gp.gp_XY, thePntMax: nanoocp.gp.gp_XY) -> None:
        """
        Find a target object in the range of cells defined by two points and
        remove it from the structures
        (the first point must have all coordinates equal or
        less than the same coordinate of the second point).
        For usage of this method "operator ==" should be defined for Target.
        """

    @overload
    def Inspect(self, thePnt: nanoocp.gp.gp_XY, theInspector: nanoocp.BRepMesh.BRepMesh_CircleInspector) -> None:
        """Inspect all targets in the cell corresponding to the given point"""

    @overload
    def Inspect(self, thePntMin: nanoocp.gp.gp_XY, thePntMax: nanoocp.gp.gp_XY, theInspector: nanoocp.BRepMesh.BRepMesh_CircleInspector) -> None:
        """
        Inspect all targets in the cells range limited by two given points
        (the first point must have all coordinates equal or
        less than the same coordinate of the second point)
        """

class NCollection_CellFilter__BRepMesh_VertexInspector:
    """
    A data structure for sorting geometric objects (called targets) in
    n-dimensional space into cells, with associated algorithm for fast checking
    of coincidence (overlapping, intersection, etc.) with other objects
    (called here bullets).

    Description

    The algorithm is based on hash map, thus it has linear time of initialization
    (O(N) where N is number of cells covered by added targets) and constant-time
    search for one bullet (more precisely, O(M) where M is number of cells covered
    by the bullet).

    The idea behind the algorithm is to separate each coordinate of the space
    into equal-size cells. Note that this works well when cell size is
    approximately equal to the characteristic size of the involved objects
    (targets and bullets; including tolerance eventually used for coincidence
    check).

    Usage

    The target objects to be searched are added to the tool by methods Add();
    each target is classified as belonging to some cell(s). The data on cells
    (list of targets found in each one) are stored in the hash map with key being
    cumulative index of the cell by all coordinates.
    Thus the time needed to find targets in some cell is O(1) * O(number of
    targets in the cell).

    As soon as all the targets are added, the algorithm is ready to check for
    coincidence.
    To find the targets coincident with any given bullet, it checks all the
    candidate targets in the cell(s) covered by the bullet object
    (methods Inspect()).

    The methods Add() and Inspect() have two flavours each: one accepts
    single point identifying one cell, another accept two points specifying
    the range of cells. It should be noted that normally at least one of these
    methods is called as for range of cells: either due to objects having non-
    zero size, or in order to account for the tolerance when objects are points.

    The set of targets can be modified during the process: new targets can be
    added by Add(), existing targets can be removed by Remove().

    Implementation

    The algorithm is implemented as template class, thus it is capable to
    work with objects of any type. The only argument of the template should be
    the specific class providing all necessary features required by the
    algorithm:

    - typedef "Target" defining type of target objects.
    This type must have copy constructor

    - typedef "Point" defining type of geometrical points used

    - static constexpr int Dimension whose value must be dimension of the point

    - method Coord() returning value of the i-th coordinate of the point:

    static double Coord (int i, const Point& thePnt);

    Note that index i is from 0 to Dimension-1.

    - method IsEqual() used by Remove() to identify objects to be removed:

    bool IsEqual (const Target& theT1, const Target& theT2);

    - method Inspect() performing necessary actions on the candidate target
    object (usually comparison with the currently checked bullet object):

    NCollection_CellFilter_Action Inspect (const Target& theObject);

    The returned value can be used to command CellFilter
    to remove the inspected item from the current cell; this allows
    to exclude the items that has been processed and are not needed any
    more in further search (for better performance).

    Note that method Inspect() can be const and/or virtual.
    """

    @overload
    def __init__(self, theCellSize: float = 0.0, theAlloc: nanoocp.NCollection.NCollection_IncAllocator | None = None) -> None:
        """Constructor when dimension count is known at compilation time."""

    @overload
    def __init__(self, theDim: int, theCellSize: float = 0.0, theAlloc: nanoocp.NCollection.NCollection_IncAllocator | None = None) -> None:
        """
        Constructor; initialized by dimension count and cell size.

        Note: the cell size must be ensured to be greater than
        maximal coordinate of the involved points divided by INT_MAX,
        in order to avoid integer overflow of cell index.

        By default cell size is 0, which is invalid; thus if default
        constructor is used, the tool must be initialized later with
        appropriate cell size by call to Reset()
        Constructor when dimension count is unknown at compilation time.
        """

    @overload
    def Reset(self, theCellSize: float, theAlloc: nanoocp.NCollection.NCollection_IncAllocator | None = None) -> None:
        """Clear the data structures, set new cell size and allocator"""

    @overload
    def Reset(self, theCellSize: nanoocp.NCollection.NCollection_Array1[float], theAlloc: nanoocp.NCollection.NCollection_IncAllocator | None = None) -> None:
        """Clear the data structures and set new cell sizes and allocator"""

    @overload
    def Add(self, theTarget: int, thePnt: nanoocp.gp.gp_XY) -> None:
        """
        Adds a target object for further search at a point (into only one cell)
        """

    @overload
    def Add(self, theTarget: int, thePntMin: nanoocp.gp.gp_XY, thePntMax: nanoocp.gp.gp_XY) -> None:
        """
        Adds a target object for further search in the range of cells
        defined by two points (the first point must have all coordinates equal or
        less than the same coordinate of the second point)
        """

    @overload
    def Remove(self, theTarget: int, thePnt: nanoocp.gp.gp_XY) -> None:
        """
        Find a target object at a point and remove it from the structures.
        For usage of this method "operator ==" should be defined for Target.
        """

    @overload
    def Remove(self, theTarget: int, thePntMin: nanoocp.gp.gp_XY, thePntMax: nanoocp.gp.gp_XY) -> None:
        """
        Find a target object in the range of cells defined by two points and
        remove it from the structures
        (the first point must have all coordinates equal or
        less than the same coordinate of the second point).
        For usage of this method "operator ==" should be defined for Target.
        """

    @overload
    def Inspect(self, thePnt: nanoocp.gp.gp_XY, theInspector: nanoocp.BRepMesh.BRepMesh_VertexInspector) -> None:
        """Inspect all targets in the cell corresponding to the given point"""

    @overload
    def Inspect(self, thePntMin: nanoocp.gp.gp_XY, thePntMax: nanoocp.gp.gp_XY, theInspector: nanoocp.BRepMesh.BRepMesh_VertexInspector) -> None:
        """
        Inspect all targets in the cells range limited by two given points
        (the first point must have all coordinates equal or
        less than the same coordinate of the second point)
        """

ICurveArrayAdaptor: TypeAlias = IMeshData_ParametersListArrayAdaptor__Handle_IMeshData_Curve

BndBox2dTreeFiller: TypeAlias = NCollection_UBTreeFiller__int__Bnd_Box2d

CircleCellFilter: TypeAlias = NCollection_CellFilter__BRepMesh_CircleInspector

VertexCellFilter: TypeAlias = NCollection_CellFilter__BRepMesh_VertexInspector

# C++ typedef aliases
VectorOfIFaceHandles = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[nanoocp.IMeshData.IMeshData_Face]]
VectorOfIWireHandles = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[nanoocp.IMeshData.IMeshData_Wire]]
VectorOfIEdgeHandles = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[nanoocp.IMeshData.IMeshData_Edge]]
VectorOfIPCurveHandles = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[nanoocp.IMeshData.IMeshData_PCurve]]
VectorOfBoolean = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[bool]]
VectorOfInteger = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[int]]
VectorOfOrientation = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[nanoocp.TopAbs.TopAbs_Orientation]]
VectorOfElements = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BRepMesh.BRepMesh_Triangle]]
VectorOfCircle = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BRepMesh.BRepMesh_Circle]]
Array1OfVertexOfDelaun = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_Array1[nanoocp.BRepMesh.BRepMesh_Vertex]]
VectorOfVertex = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BRepMesh.BRepMesh_Vertex]]
SequenceOfBndB2d = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_Sequence[nanoocp.Bnd.Bnd_B2d]]
SequenceOfInteger = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_Sequence[int]]
SequenceOfReal = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_Sequence[float]]
ListOfInteger = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_List[int]]
ListOfPnt2d = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_List[nanoocp.gp.gp_Pnt2d]]
ListOfIPCurves = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_List[nanoocp.IMeshData.IMeshData_PCurve]]
MapOfInteger = nanoocp.NCollection.NCollection_Shared[nanoocp.TColStd.TColStd_PackedMapOfInteger]
DMapOfShapeInteger = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, int, nanoocp.TopTools.TopTools_ShapeMapHasher]]
MapOfOrientedEdges = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_Map[nanoocp.BRepMesh.BRepMesh_OrientedEdge]]
MapOfReal = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_Map[float]]
IDMapOfLink = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.BRepMesh.BRepMesh_Edge, nanoocp.BRepMesh.BRepMesh_PairOfIndex]]
DMapOfIntegerListOfInteger = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DataMap[int, nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_List[int]]]]
MapOfIntegerInteger = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DataMap[int, bool]]
IMapOfReal = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_IndexedMap[float]]
Array1OfInteger = nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_Array1[int]]
