"""OCCT package BOPDS (toolkit TKBO)"""

from typing import overload

import nanoocp.Bnd
import nanoocp.IntTools
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp


class BOPDS_CommonBlock(nanoocp.Standard.Standard_Transient):
    """
    The class BOPDS_CommonBlock is to store the information
    about pave blocks that have geometrical coincidence
    (in terms of a tolerance) with:
    a) other pave block(s);
    b) face(s).
    First pave block in the common block (real pave block)
    is always a pave block with the minimal index of the original edge.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator the allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_CommonBlock) -> None: ...

    def AddPaveBlock(self, aPB: BOPDS_PaveBlock | None) -> None:
        """
        Modifier
        Adds the pave block <aPB> to the list of pave blocks
        of the common block
        """

    def SetPaveBlocks(self, aLPB: nanoocp.NCollection.NCollection_List[nanoocp.BOPDS.BOPDS_PaveBlock]) -> None:
        """
        Modifier
        Sets the list of pave blocks for the common block
        """

    def AddFace(self, aF: int) -> None:
        """
        Modifier
        Adds the index of the face <aF>
        to the list of indices of faces
        of the common block
        """

    def SetFaces(self, aLF: nanoocp.NCollection.NCollection_List[int]) -> None:
        """
        Modifier
        Sets the list of indices of faces <aLF>
        of the common block
        """

    def AppendFaces(self, aLF: nanoocp.NCollection.NCollection_List[int]) -> None:
        """
        Modifier
        Appends the list of indices of faces <aLF>
        to the list of indices of faces
        of the common block (the input list is emptied)
        """

    def PaveBlocks(self) -> nanoocp.NCollection.NCollection_List[nanoocp.BOPDS.BOPDS_PaveBlock]:
        """
        Selector
        Returns the list of pave blocks
        of the common block
        """

    def Faces(self) -> nanoocp.NCollection.NCollection_List[int]:
        """
        Selector
        Returns the list of indices of faces
        of the common block
        """

    def PaveBlock1(self) -> BOPDS_PaveBlock:
        """
        Selector
        Returns the first pave block
        of the common block
        """

    def PaveBlockOnEdge(self, theIndex: int) -> BOPDS_PaveBlock:
        """
        Selector
        Returns the pave block that belongs
        to the edge with index <theIx>
        """

    def IsPaveBlockOnFace(self, theIndex: int) -> bool:
        """
        Query
        Returns true if the common block contains
        a pave block that belongs
        to the face with index <theIx>
        """

    def IsPaveBlockOnEdge(self, theIndex: int) -> bool:
        """
        Query
        Returns true if the common block contains
        a pave block that belongs
        to the edge with index <theIx>
        """

    @overload
    def Contains(self, thePB: BOPDS_PaveBlock | None) -> bool:
        """
        Query
        Returns true if the common block contains
        a pave block that is equal to <thePB>
        """

    @overload
    def Contains(self, theF: int) -> bool:
        """
        Query
        Returns true if the common block contains
        the face with index equal to <theF>
        """

    def SetEdge(self, theEdge: int) -> None:
        """
        Modifier
        Assign the index <theEdge> as the edge index
        to all pave blocks of the common block
        """

    def Edge(self) -> int:
        """
        Selector
        Returns the index of the edge
        of all pave blocks of the common block
        """

    def Dump(self) -> None: ...

    def SetRealPaveBlock(self, thePB: BOPDS_PaveBlock | None) -> None:
        """
        Moves the pave blocks in the list to make the given
        pave block to be the first.
        It will be representative for the whole group.
        """

    def SetTolerance(self, theTol: float) -> None:
        """Sets the tolerance for the common block"""

    def Tolerance(self) -> float:
        """Return the tolerance of common block"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPDS_Pave:
    """
    The class BOPDS_Pave is to store
    information about vertex on an edge
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theIndex: int, theParameter: float) -> None:
        """Constructor with index and parameter"""

    @overload
    def __init__(self, theOther: BOPDS_Pave) -> None: ...

    def SetIndex(self, theIndex: int) -> None:
        """
        Modifier
        Sets the index of vertex <theIndex>
        """

    def Index(self) -> int:
        """
        Selector
        Returns the index of vertex
        """

    def SetParameter(self, theParameter: float) -> None:
        """
        Modifier
        Sets the parameter of vertex <theParameter>
        """

    def Parameter(self) -> float:
        """
        Selector
        Returns the parameter of vertex
        """

    def Contents(self) -> tuple[int, float]:
        """
        Selector
        Returns the index of vertex <theIndex>
        Returns the parameter of vertex <theParameter>
        """

    def IsLess(self, theOther: BOPDS_Pave) -> bool:
        """
        Query
        Returns true if the parameter of this is less
        than the parameter of <theOther>
        """

    def __lt__(self, theOther: BOPDS_Pave) -> bool: ...

    def IsEqual(self, theOther: BOPDS_Pave) -> bool:
        """
        Query
        Returns true if the parameter of this is equal
        to the parameter of <theOther>
        """

    def __eq__(self, theOther: BOPDS_Pave) -> bool: ...

    def Dump(self) -> None: ...

    def __hash__(self) -> int: ...

class BOPDS_PaveBlock(nanoocp.Standard.Standard_Transient):
    """
    The class BOPDS_PaveBlock is to store
    the information about pave block on an edge.
    Two adjacent paves on edge make up pave block.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator the allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_PaveBlock) -> None: ...

    def SetPave1(self, thePave: BOPDS_Pave) -> None:
        """
        Modifier
        Sets the first pave <thePave>
        """

    def Pave1(self) -> BOPDS_Pave:
        """
        Selector
        Returns the first pave
        """

    def SetPave2(self, thePave: BOPDS_Pave) -> None:
        """
        Modifier
        Sets the second pave <thePave>
        """

    def Pave2(self) -> BOPDS_Pave:
        """
        Selector
        Returns the second pave
        """

    def SetEdge(self, theEdge: int) -> None:
        """
        Modifier
        Sets the index of edge of pave block <theEdge>
        """

    def Edge(self) -> int:
        """
        Selector
        Returns the index of edge of pave block
        """

    def HasEdge(self) -> bool:
        """
        Query
        Returns true if the pave block has edge
        """

    def HasEdge__int(self) -> tuple[bool, int]:
        """
        HasEdge__int: the C++ overload HasEdge(int &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Query
        Returns true if the pave block has edge
        Returns the index of edge <theEdge>
        """

    def SetOriginalEdge(self, theEdge: int) -> None:
        """
        Modifier
        Sets the index of original edge
        of the pave block <theEdge>
        """

    def OriginalEdge(self) -> int:
        """
        Selector
        Returns the index of original edge of pave block
        """

    def IsSplitEdge(self) -> bool:
        """
        Query
        Returns true if the edge is equal to the original edge
        of the pave block
        """

    def Range(self) -> tuple[float, float]:
        """
        Selector
        Returns the parametric range <theT1,theT2>
        of the pave block
        """

    def HasSameBounds(self, theOther: BOPDS_PaveBlock | None) -> bool:
        """
        Query
        Returns true if the pave block has pave indices
        that equal to the pave indices of the pave block
        <theOther>
        """

    def Indices(self) -> tuple[int, int]:
        """
        Selector
        Returns the pave indices <theIndex1,theIndex2>
        of the pave block
        """

    def IsToUpdate(self) -> bool:
        """
        Query
        Returns true if the pave block contains extra paves
        """

    def AppendExtPave(self, thePave: BOPDS_Pave) -> None:
        """
        Modifier
        Appends extra paves <thePave>
        """

    def AppendExtPave1(self, thePave: BOPDS_Pave) -> None:
        """
        Modifier
        Appends extra pave <thePave>
        """

    def RemoveExtPave(self, theVertNum: int) -> None:
        """
        Modifier
        Removes a pave with the given vertex number from extra paves
        """

    def ExtPaves(self) -> nanoocp.NCollection.NCollection_List[nanoocp.BOPDS.BOPDS_Pave]:
        """
        Selector
        Returns the extra paves
        """

    def ChangeExtPaves(self) -> nanoocp.NCollection.NCollection_List[nanoocp.BOPDS.BOPDS_Pave]:
        """
        Selector / Modifier
        Returns the extra paves
        """

    def Update(self, theLPB: nanoocp.NCollection.NCollection_List[nanoocp.BOPDS.BOPDS_PaveBlock], theFlag: bool = True) -> None:
        """
        Modifier
        Updates the pave block. The extra paves are used
        to create new pave blocks <theLPB>.
        <theFlag> - if true, the first and second
        pave are used to produce new pave blocks.
        """

    def ContainsParameter(self, thePrm: float, theTol: float) -> tuple[bool, int]:
        """
        Query
        Returns true if the extra paves contain the pave
        with given value of the parameter <thePrm>
        <theTol>  - the value of the tolerance to compare
        <theInd>  - index of the found pave
        """

    def SetShrunkData(self, theTS1: float, theTS2: float, theBox: nanoocp.Bnd.Bnd_Box, theIsSplittable: bool) -> None:
        """
        Modifier
        Sets the shrunk data for the pave block
        <theTS1>, <theTS2> - shrunk range
        <theBox> - the bounding box
        <theIsSplittable> - defines whether the edge can be split
        """

    def ShrunkData(self, theBox: nanoocp.Bnd.Bnd_Box) -> tuple[float, float, bool]:
        """
        Selector
        Returns the shrunk data for the pave block
        <theTS1>, <theTS2> - shrunk range
        <theBox> - the bounding box
        <theIsSplittable> - defines whether the edge can be split
        """

    def HasShrunkData(self) -> bool:
        """
        Query
        Returns true if the pave block contains
        the shrunk data
        """

    def Dump(self) -> None: ...

    def IsSplittable(self) -> bool:
        """
        Query
        Returns FALSE if the pave block has a too short
        shrunk range and cannot be split, otherwise returns TRUE
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPDS_CoupleOfPaveBlocks:
    """Stores information about two pave blocks and satellite data."""

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, thePB1: BOPDS_PaveBlock | None, thePB2: BOPDS_PaveBlock | None) -> None:
        """
        Constructor with two pave blocks.
        @param[in] thePB1 first pave block
        @param[in] thePB2 second pave block
        """

    @overload
    def __init__(self, theOther: BOPDS_CoupleOfPaveBlocks) -> None: ...

    def SetIndex(self, theIndex: int) -> None:
        """
        Sets the index.
        @param[in] theIndex the index
        """

    def Index(self) -> int:
        """
        Returns the index.
        @return the index
        """

    def SetIndexInterf(self, theIndex: int) -> None:
        """
        Sets the index of an interference.
        @param[in] theIndex index of an interference
        """

    def IndexInterf(self) -> int:
        """
        Returns the index of an interference.
        @return index of an interference
        """

    def SetPaveBlocks(self, thePB1: BOPDS_PaveBlock | None, thePB2: BOPDS_PaveBlock | None) -> None:
        """
        Sets both pave blocks.
        @param[in] thePB1 first pave block
        @param[in] thePB2 second pave block
        """

    def PaveBlocks(self) -> tuple[BOPDS_PaveBlock, BOPDS_PaveBlock]:
        """
        Deprecated in OCCT: Use PaveBlock1() and PaveBlock2() instead

        @deprecated Use PaveBlock1() and PaveBlock2() instead.
        """

    def SetPaveBlock1(self, thePB: BOPDS_PaveBlock | None) -> None:
        """
        Sets the first pave block.
        @param[in] thePB the first pave block
        """

    def PaveBlock1(self) -> BOPDS_PaveBlock:
        """
        Returns the first pave block.
        @return handle to the first pave block
        """

    def SetPaveBlock2(self, thePB: BOPDS_PaveBlock | None) -> None:
        """
        Sets the second pave block.
        @param[in] thePB the second pave block
        """

    def PaveBlock2(self) -> BOPDS_PaveBlock:
        """
        Returns the second pave block.
        @return handle to the second pave block
        """

    def SetTolerance(self, theTol: float) -> None:
        """
        Sets the tolerance associated with this couple.
        @param[in] theTol the tolerance value
        """

    def Tolerance(self) -> float:
        """
        Returns the tolerance associated with this couple.
        @return the tolerance value
        """

class BOPDS_Curve:
    """
    The class BOPDS_Curve is to store
    the information about intersection curve
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator the allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_Curve) -> None: ...

    def SetCurve(self, theC: nanoocp.IntTools.IntTools_Curve) -> None:
        """
        Modifier
        Sets the curve <theC>
        """

    def Curve(self) -> nanoocp.IntTools.IntTools_Curve:
        """
        Selector
        Returns the curve
        """

    def SetBox(self, theBox: nanoocp.Bnd.Bnd_Box) -> None:
        """
        Modifier
        Sets the bounding box <theBox> of the curve
        """

    def Box(self) -> nanoocp.Bnd.Bnd_Box:
        """
        Selector
        Returns the bounding box of the curve
        """

    def ChangeBox(self) -> nanoocp.Bnd.Bnd_Box:
        """
        Selector/Modifier
        Returns the bounding box of the curve
        """

    def SetPaveBlocks(self, theLPB: nanoocp.NCollection.NCollection_List[nanoocp.BOPDS.BOPDS_PaveBlock]) -> None: ...

    def PaveBlocks(self) -> nanoocp.NCollection.NCollection_List[nanoocp.BOPDS.BOPDS_PaveBlock]:
        """
        Selector
        Returns the list of pave blocks
        of the curve
        """

    def ChangePaveBlocks(self) -> nanoocp.NCollection.NCollection_List[nanoocp.BOPDS.BOPDS_PaveBlock]:
        """
        Selector/Modifier
        Returns the list of pave blocks
        of the curve
        """

    def InitPaveBlock1(self) -> None:
        """
        Creates initial pave block
        of the curve
        """

    def ChangePaveBlock1(self) -> BOPDS_PaveBlock:
        """
        Selector/Modifier
        Returns initial pave block
        of the curve
        """

    def TechnoVertices(self) -> nanoocp.NCollection.NCollection_List[int]:
        """
        Selector
        Returns list of indices of technologic vertices
        of the curve
        """

    def ChangeTechnoVertices(self) -> nanoocp.NCollection.NCollection_List[int]:
        """
        Selector/Modifier
        Returns list of indices of technologic vertices
        of the curve
        """

    def HasEdge(self) -> bool:
        """
        Query
        Returns true if at least one pave block of the curve
        has edge
        """

    def SetTolerance(self, theTol: float) -> None:
        """Sets the tolerance for the curve."""

    def Tolerance(self) -> float:
        """Returns the tolerance of the curve"""

    def TangentialTolerance(self) -> float:
        """Returns the tangential tolerance of the curve"""

class BOPDS_Pair:
    """The class is to provide the pair of indices of interfering shapes."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theIndex1: int, theIndex2: int) -> None: ...

    @overload
    def __init__(self, theOther: BOPDS_Pair) -> None: ...

    def SetIndices(self, theIndex1: int, theIndex2: int) -> None:
        """Sets the indices"""

    def Indices(self) -> tuple[int, int]:
        """Gets the indices"""

    def __lt__(self, theOther: BOPDS_Pair) -> bool:
        """Operator less"""

    def IsEqual(self, theOther: BOPDS_Pair) -> bool:
        """Returns true if the Pair is equal to <the theOther>"""

    def __eq__(self, theOther: BOPDS_Pair) -> bool: ...

    def __hash__(self) -> int: ...

class BOPDS_FaceInfo:
    """
    The class BOPDS_FaceInfo is to store
    handy information about state of face
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator the allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_FaceInfo) -> None: ...

    def Clear(self) -> None:
        """Clears the contents"""

    def SetIndex(self, theI: int) -> None:
        """
        Modifier
        Sets the index of the face <theI>
        """

    def Index(self) -> int:
        """
        Selector
        Returns the index of the face

        In
        """

    def PaveBlocksIn(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.BOPDS.BOPDS_PaveBlock]:
        """
        Selector
        Returns the pave blocks of the face
        that have state In
        """

    def ChangePaveBlocksIn(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.BOPDS.BOPDS_PaveBlock]:
        """
        Selector/Modifier
        Returns the pave blocks
        of the face
        that have state In
        """

    def VerticesIn(self) -> nanoocp.NCollection.NCollection_Map[int]:
        """
        Selector
        Returns the list of indices for vertices
        of the face
        that have state In
        """

    def ChangeVerticesIn(self) -> nanoocp.NCollection.NCollection_Map[int]:
        """
        Selector/Modifier
        Returns the list of indices for vertices
        of the face
        that have state In

        On
        """

    def PaveBlocksOn(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.BOPDS.BOPDS_PaveBlock]:
        """
        Selector
        Returns the pave blocks of the face
        that have state On
        """

    def ChangePaveBlocksOn(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.BOPDS.BOPDS_PaveBlock]:
        """
        Selector/Modifier
        Returns the pave blocks
        of the face
        that have state On
        """

    def VerticesOn(self) -> nanoocp.NCollection.NCollection_Map[int]:
        """
        Selector
        Returns the list of indices for vertices
        of the face
        that have state On
        """

    def ChangeVerticesOn(self) -> nanoocp.NCollection.NCollection_Map[int]:
        """
        Selector/Modifier
        Returns the list of indices for vertices
        of the face
        that have state On

        Sections
        """

    def PaveBlocksSc(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.BOPDS.BOPDS_PaveBlock]:
        """
        Selector
        Returns the pave blocks of the face
        that are pave blocks of section edges
        """

    def ChangePaveBlocksSc(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.BOPDS.BOPDS_PaveBlock]: ...

    def VerticesSc(self) -> nanoocp.NCollection.NCollection_Map[int]:
        """
        Selector
        Returns the list of indices for section vertices
        of the face
        """

    def ChangeVerticesSc(self) -> nanoocp.NCollection.NCollection_Map[int]:
        """
        Selector/Modifier
        Returns the list of indices for section vertices
        of the face

        Others
        """

class BOPDS_IndexRange:
    """
    The class BOPDS_IndexRange is to store
    the information about range of two indices
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theI1: int, theI2: int) -> None:
        """Constructor with initial indices"""

    @overload
    def __init__(self, theOther: BOPDS_IndexRange) -> None: ...

    def SetFirst(self, theI1: int) -> None:
        """
        Modifier
        Sets the first index <theI1> of the range
        """

    def SetLast(self, theI2: int) -> None:
        """
        Modifier
        Sets the second index <theI2> of the range
        """

    def First(self) -> int:
        """
        Selector
        Returns the first index of the range
        """

    def Last(self) -> int:
        """
        Selector
        Returns the second index of the range
        """

    def SetIndices(self, theI1: int, theI2: int) -> None:
        """
        Modifier
        Sets the first index of the range  <theI1>
        Sets the second index of the range <theI2>
        """

    def Indices(self) -> tuple[int, int]:
        """
        Selector
        Returns the first index of the range  <theI1>
        Returns the second index of the range <theI2>
        """

    def Contains(self, theIndex: int) -> bool:
        """
        Query
        Returns true if the range contains <theIndex>
        """

    def Dump(self) -> None: ...

class BOPDS_Point:
    """
    The class BOPDS_Point is to store
    the information about intersection point
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: BOPDS_Point) -> None: ...

    def SetPnt(self, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """
        Modifier
        Sets 3D point <thePnt>
        """

    def Pnt(self) -> nanoocp.gp.gp_Pnt:
        """
        Selector
        Returns 3D point
        """

    def SetPnt2D1(self, thePnt: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Modifier
        Sets 2D point on the first face <thePnt>
        """

    def Pnt2D1(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Selector
        Returns 2D point on the first face <thePnt>
        """

    def SetPnt2D2(self, thePnt: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Modifier
        Sets 2D point on the second face <thePnt>
        """

    def Pnt2D2(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Selector
        Returns 2D point on the second face <thePnt>
        """

    def SetIndex(self, theIndex: int) -> None:
        """
        Modifier
        Sets the index of the vertex <theIndex>
        """

    def Index(self) -> int:
        """
        Selector
        Returns index of the vertex
        """

class BOPDS_Interf:
    """
    The class BOPDS_Interf stores the information about
    the interference between two shapes.
    The class BOPDS_Interf is root class
    """

    def SetIndices(self, theIndex1: int, theIndex2: int) -> None:
        """
        Sets the indices of interferred shapes
        @param theIndex1
        index of the first shape
        @param theIndex2
        index of the second shape
        """

    def Indices(self) -> tuple[int, int]:
        """
        Returns the indices of interferred shapes
        @param theIndex1
        index of the first shape
        @param theIndex2
        index of the second shape
        """

    def SetIndex1(self, theIndex: int) -> None:
        """
        Sets the index of the first interferred shape
        @param theIndex
        index of the first shape
        """

    def SetIndex2(self, theIndex: int) -> None:
        """
        Sets the index of the second interferred shape
        @param theIndex
        index of the second shape
        """

    def Index1(self) -> int:
        """
        Returns the index of the first interferred shape
        @return
        index of the first shape
        """

    def Index2(self) -> int:
        """
        Returns the index of the second interferred shape
        @return
        index of the second shape
        """

    def OppositeIndex(self, theI: int) -> int:
        """
        Returns the index of that are opposite to the given index
        @param theI
        the index
        @return
        index of opposite shape
        """

    def Contains(self, theIndex: int) -> bool:
        """
        Returns true if the interference contains given index
        @param theIndex
        the index
        @return
        true if the interference contains given index
        """

    def SetIndexNew(self, theIndex: int) -> None:
        """
        Sets the index of new shape
        @param theIndex
        the index
        """

    def IndexNew(self) -> int:
        """
        Returns the index of new shape
        @return theIndex
        the index of new shape
        """

    def HasIndexNew__int(self) -> tuple[bool, int]:
        """
        HasIndexNew__int: the C++ overload HasIndexNew(int &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns true if the interference has index of new shape
        that is equal to the given index
        @param theIndex
        the index
        @return true if the interference has index of new shape
        that is equal to the given index
        """

    def HasIndexNew(self) -> bool:
        """
        Returns true if the interference has index of new shape
        the index
        @return true if the interference has index of new shape
        """

    def GetIndexNew(self) -> int | None:
        """
        Returns the index of new shape.
        If the index is not set, returns std::nullopt.
        """

class BOPDS_InterfVV(BOPDS_Interf):
    """
    The class BOPDS_InterfVV stores the information about
    the interference of the type vertex/vertex.
    """

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator
        allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_InterfVV) -> None: ...

class BOPDS_InterfVE(BOPDS_Interf):
    """
    The class BOPDS_InterfVE stores the information about
    the interference of the type vertex/edge.
    """

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator
        allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_InterfVE) -> None: ...

    def SetParameter(self, theT: float) -> None:
        """
        Modifier
        Sets the value of parameter
        of the point of the vertex
        on the curve of the edge
        @param theT
        value of parameter
        """

    def Parameter(self) -> float:
        """
        Selector
        Returrns the value of parameter
        of the point of the vertex
        on the curve of the edge
        @return
        value of parameter
        """

class BOPDS_InterfVF(BOPDS_Interf):
    """
    The class BOPDS_InterfVF stores the information about
    the interference of the type vertex/face
    """

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator
        allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_InterfVF) -> None: ...

    def SetUV(self, theU: float, theV: float) -> None:
        """
        Modifier
        Sets the value of parameters
        of the point of the vertex
        on the surface of of the face
        @param theU
        value of U parameter
        @param theV
        value of U parameter
        """

    def UV(self) -> tuple[float, float]:
        """
        Selector
        Returns the value of parameters
        of the point of the vertex
        on the surface of of the face
        @param theU
        value of U parameter
        @param theV
        value of U parameter
        """

class BOPDS_InterfEE(BOPDS_Interf):
    """
    The class BOPDS_InterfEE stores the information about
    the interference of the type edge/edge.
    """

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator
        allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_InterfEE) -> None: ...

    def SetCommonPart(self, theCP: nanoocp.IntTools.IntTools_CommonPrt) -> None:
        """
        Modifier
        Sets the info of common part
        @param theCP
        common part
        """

    def CommonPart(self) -> nanoocp.IntTools.IntTools_CommonPrt:
        """
        Selector
        Returns the info of common part
        @return
        common part
        """

class BOPDS_InterfEF(BOPDS_Interf):
    """
    The class BOPDS_InterfEF stores the information about
    the interference of the type edge/face.
    """

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator
        allocator to manage the memory


        Constructor
        @param theAllocator
        allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_InterfEF) -> None: ...

    def SetCommonPart(self, theCP: nanoocp.IntTools.IntTools_CommonPrt) -> None:
        """
        Modifier
        Sets the info of common part
        @param theCP
        common part
        """

    def CommonPart(self) -> nanoocp.IntTools.IntTools_CommonPrt:
        """
        Selector
        Returns the info of common part
        @return
        common part
        """

class BOPDS_InterfFF(BOPDS_Interf):
    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BOPDS_InterfFF) -> None: ...

    def Init(self, theNbCurves: int, theNbPoints: int) -> None:
        """
        Initializer
        @param theNbCurves
        number of intersection curves
        @param theNbPoints
        number of intersection points
        """

    def SetTangentFaces(self, theFlag: bool) -> None:
        """
        Modifier
        Sets the flag of whether the faces are tangent
        @param theFlag
        the flag
        """

    def TangentFaces(self) -> bool:
        """
        Selector
        Returns the flag whether the faces are tangent
        @return
        the flag
        """

    def Curves(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_Curve]:
        """
        Selector
        Returns the intersection curves
        @return
        intersection curves
        """

    def ChangeCurves(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_Curve]:
        """
        Selector/Modifier
        Returns the intersection curves
        @return
        intersection curves
        """

    def Points(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_Point]:
        """
        Selector
        Returns the intersection points
        @return
        intersection points
        """

    def ChangePoints(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_Point]:
        """
        Selector/Modifier
        Returns the intersection points
        @return
        intersection points
        """

class BOPDS_InterfVZ(BOPDS_Interf):
    """
    The class BOPDS_InterfVZ stores the information about
    the interference of the type vertex/solid.
    """

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator
        allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_InterfVZ) -> None: ...

class BOPDS_InterfEZ(BOPDS_Interf):
    """
    The class BOPDS_InterfEZ stores the information about
    the interference of the type edge/solid.
    """

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator
        allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_InterfEZ) -> None: ...

class BOPDS_InterfFZ(BOPDS_Interf):
    """
    The class BOPDS_InterfFZ stores the information about
    the interference of the type face/solid.
    """

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator
        allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_InterfFZ) -> None: ...

class BOPDS_InterfZZ(BOPDS_Interf):
    """
    The class BOPDS_InterfZZ stores the information about
    the interference of the type solid/solid.
    """

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator
        allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_InterfZZ) -> None: ...

class BOPDS_ShapeInfo:
    """
    The class BOPDS_ShapeInfo is to store
    handy information about shape
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator the allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_ShapeInfo) -> None: ...

    def SetShape(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Modifier
        Sets the shape <theS>
        """

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Selector
        Returns the shape
        """

    def SetShapeType(self, theType: nanoocp.TopAbs.TopAbs_ShapeEnum) -> None:
        """
        Modifier
        Sets the type of shape theType
        """

    def ShapeType(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum:
        """
        Selector
        Returns the type of shape
        """

    def SetBox(self, theBox: nanoocp.Bnd.Bnd_Box) -> None:
        """
        Modifier
        Sets the boundung box of the shape theBox
        """

    def Box(self) -> nanoocp.Bnd.Bnd_Box:
        """
        Selector
        Returns the boundung box of the shape
        """

    def ChangeBox(self) -> nanoocp.Bnd.Bnd_Box:
        """
        Selector/Modifier
        Returns the boundung box of the shape
        """

    def SubShapes(self) -> nanoocp.NCollection.NCollection_List[int]:
        """
        Selector
        Returns the list of indices of sub-shapes
        """

    def ChangeSubShapes(self) -> nanoocp.NCollection.NCollection_List[int]:
        """
        Selector/ Modifier
        Returns the list of indices of sub-shapes
        """

    def HasSubShape(self, theI: int) -> bool:
        """
        Query
        Returns true if the shape has sub-shape with
        index theI
        """

    def HasReference(self) -> bool: ...

    def SetReference(self, theI: int) -> None:
        """
        Modifier
        Sets the index of a reference information
        """

    def Reference(self) -> int:
        """
        Selector
        Returns the index of a reference information
        """

    def HasBRep(self) -> bool:
        """
        Query
        Returns true if the shape has boundary representation
        """

    def IsInterfering(self) -> bool:
        """
        Returns true if the shape can be participant of
        an interference

        Flag
        """

    def HasFlag(self) -> bool:
        """
        Query
        Returns true if there is flag.
        """

    def HasFlag__int(self) -> tuple[bool, int]:
        """
        HasFlag__int: the C++ overload HasFlag(int &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Query
        Returns true if there is flag.
        Returns the flag theFlag
        """

    def SetFlag(self, theI: int) -> None:
        """
        Modifier
        Sets the flag
        """

    def Flag(self) -> int:
        """Returns the flag"""

    def Dump(self) -> None: ...

class BOPDS_Tools:
    """
    The class BOPDS_Tools contains
    a set auxiliary static functions
    of the package BOPDS
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPDS_Tools) -> None: ...

    @overload
    @staticmethod
    def TypeToInteger(theT1: nanoocp.TopAbs.TopAbs_ShapeEnum, theT2: nanoocp.TopAbs.TopAbs_ShapeEnum) -> int:
        """
        Converts the conmbination of two types
        of shape <theT1>,<theT2>
        to the one integer value, that is returned
        """

    @overload
    @staticmethod
    def TypeToInteger(theT: nanoocp.TopAbs.TopAbs_ShapeEnum) -> int:
        """
        Converts the type of shape <theT>,
        to integer value, that is returned
        """

    @staticmethod
    def HasBRep(theT: nanoocp.TopAbs.TopAbs_ShapeEnum) -> bool:
        """
        Returns true if the type <theT> correspond
        to a shape having boundary representation
        """

    @staticmethod
    def IsInterfering(theT: nanoocp.TopAbs.TopAbs_ShapeEnum) -> bool:
        """
        Returns true if the type <theT> can be participant of
        an interference
        """

class BOPDS_DS:
    """
    The class BOPDS_DS provides the control
    of data structure for the algorithms in the
    Boolean Component such as General Fuse, Boolean operations,
    Section, Maker Volume, Splitter and Cells Builder.

    The data structure has the following contents:
    1. the arguments of an operation [myArguments];
    2. the information about arguments/new shapes
    and their sub-shapes (type of the shape,
    bounding box, etc) [myLines];
    3. each argument shape(and its subshapes)
    has/have own range of indices (rank);
    4. pave blocks on source edges [myPaveBlocksPool];
    5. the state of source faces [myFaceInfoPool];
    6. the collection of same domain shapes [myShapesSD];
    7. the collection of interferences [myInterfTB, myInterfVV,..myInterfFF]
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator the allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_DS) -> None: ...

    def Clear(self) -> None:
        """Clears the contents"""

    def Allocator(self) -> nanoocp.NCollection.NCollection_BaseAllocator:
        """Selector"""

    def SetArguments(self, theLS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Modifier
        Sets the arguments [theLS] of an operation
        """

    def Arguments(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Selector
        Returns the arguments of an operation
        """

    def Init(self, theFuzz: float = 1e-07) -> None:
        """
        Initializes the data structure for
        the arguments
        """

    def NbShapes(self) -> int:
        """
        Selector
        Returns the total number of shapes stored
        """

    def NbSourceShapes(self) -> int:
        """
        Selector
        Returns the total number of source shapes stored
        """

    def NbRanges(self) -> int:
        """
        Selector
        Returns the number of index ranges
        """

    def Range(self, theIndex: int) -> BOPDS_IndexRange:
        """
        Selector
        Returns the index range "i\"
        """

    def Rank(self, theIndex: int) -> int:
        """
        Selector
        Returns the rank of the shape of index "i\"
        """

    def IsNewShape(self, theIndex: int) -> bool:
        """
        Returns true if the shape of index "i" is not
        the source shape/sub-shape
        """

    @overload
    def Append(self, theSI: BOPDS_ShapeInfo) -> int:
        """
        Modifier
        Appends the information about the shape [theSI]
        to the data structure
        Returns the index of theSI in the data structure
        """

    @overload
    def Append(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """
        Modifier
        Appends the default information about the shape [theS]
        to the data structure
        Returns the index of theS in the data structure
        """

    def ShapeInfo(self, theIndex: int) -> BOPDS_ShapeInfo:
        """
        Selector
        Returns the information about the shape
        with index theIndex
        """

    def ChangeShapeInfo(self, theIndex: int) -> BOPDS_ShapeInfo:
        """
        Selector/Modifier
        Returns the information about the shape
        with index theIndex
        """

    def Shape(self, theIndex: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Selector
        Returns the shape
        with index theIndex
        """

    def Index(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """
        Selector
        Returns the index of the shape theS
        """

    def PaveBlocksPool(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.NCollection.NCollection_List[nanoocp.BOPDS.BOPDS_PaveBlock]]:
        """
        Selector
        Returns the information about pave blocks on source edges
        """

    def ChangePaveBlocksPool(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.NCollection.NCollection_List[nanoocp.BOPDS.BOPDS_PaveBlock]]:
        """
        Selector/Modifier
        Returns the information about pave blocks on source edges
        """

    def HasPaveBlocks(self, theIndex: int) -> bool:
        """
        Query
        Returns true if the shape with index theIndex has the
        information about pave blocks
        """

    def PaveBlocks(self, theIndex: int) -> nanoocp.NCollection.NCollection_List[nanoocp.BOPDS.BOPDS_PaveBlock]:
        """
        Selector
        Returns the pave blocks for the shape with index theIndex
        """

    def ChangePaveBlocks(self, theIndex: int) -> nanoocp.NCollection.NCollection_List[nanoocp.BOPDS.BOPDS_PaveBlock]:
        """
        Selector/Modifier
        Returns the pave blocks for the shape with index theIndex
        """

    def UpdatePaveBlocks(self) -> None:
        """Update the pave blocks for the all shapes in data structure"""

    def UpdatePaveBlock(self, thePB: BOPDS_PaveBlock | None) -> None:
        """Update the pave block thePB"""

    def UpdateCommonBlock(self, theCB: BOPDS_CommonBlock | None, theFuzz: float) -> None:
        """Update the common block theCB"""

    def IsCommonBlock(self, thePB: BOPDS_PaveBlock | None) -> bool:
        """
        Query
        Returns true if the pave block is common block
        """

    def CommonBlock(self, thePB: BOPDS_PaveBlock | None) -> BOPDS_CommonBlock:
        """
        Selector
        Returns the common block
        """

    def SetCommonBlock(self, thePB: BOPDS_PaveBlock | None, theCB: BOPDS_CommonBlock | None) -> None:
        """
        Modifier
        Sets the common block <theCB>
        """

    def RealPaveBlock(self, thePB: BOPDS_PaveBlock | None) -> BOPDS_PaveBlock:
        """
        Selector
        Returns the real first pave block
        """

    def IsCommonBlockOnEdge(self, thePB: BOPDS_PaveBlock | None) -> bool:
        """
        Query
        Returns true if common block contains more then one pave block
        """

    def FaceInfoPool(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_FaceInfo]:
        """
        Selector
        Returns the information about state of faces
        """

    def HasFaceInfo(self, theIndex: int) -> bool:
        """
        Query
        Returns true if the shape with index theIndex has the
        information about state of face
        """

    def FaceInfo(self, theIndex: int) -> BOPDS_FaceInfo:
        """
        Selector
        Returns the state of face with index theIndex
        """

    def ChangeFaceInfo(self, theIndex: int) -> BOPDS_FaceInfo:
        """
        Selector/Modifier
        Returns the state of face with index theIndex
        """

    @overload
    def UpdateFaceInfoIn(self, theIndex: int) -> None:
        """Update the state In of face with index theIndex"""

    @overload
    def UpdateFaceInfoIn(self, theFaces: nanoocp.NCollection.NCollection_Map[int]) -> None:
        """Update the state IN for all faces in the given map"""

    @overload
    def UpdateFaceInfoOn(self, theIndex: int) -> None:
        """Update the state On of face with index theIndex"""

    @overload
    def UpdateFaceInfoOn(self, theFaces: nanoocp.NCollection.NCollection_Map[int]) -> None:
        """Update the state ON for all faces in the given map"""

    def FaceInfoOn(self, theIndex: int, theMPB: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.BOPDS.BOPDS_PaveBlock], theMVP: nanoocp.NCollection.NCollection_Map[int]) -> None:
        """
        Selector
        Returns the state On
        [theMPB,theMVP] of face with index theIndex
        """

    def FaceInfoIn(self, theIndex: int, theMPB: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.BOPDS.BOPDS_PaveBlock], theMVP: nanoocp.NCollection.NCollection_Map[int]) -> None:
        """
        Selector
        Returns the state In
        [theMPB,theMVP] of face with index theIndex
        """

    def AloneVertices(self, theFaceIndex: int, theVertexList: nanoocp.NCollection.NCollection_List[int]) -> None:
        """
        Selector
        Returns the indices of alone vertices
        for the face with index @p theFaceIndex
        """

    def RefineFaceInfoOn(self) -> None:
        """
        Refine the state On for the all faces having
        state information

        ++
        """

    def RefineFaceInfoIn(self) -> None:
        """
        Removes any pave block from list of having IN state if it has also the state ON.
        """

    def SubShapesOnIn(self, theFaceIndex1: int, theFaceIndex2: int, theMVOnIn: nanoocp.NCollection.NCollection_Map[int], theMVCommon: nanoocp.NCollection.NCollection_Map[int], thePBOnIn: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.BOPDS.BOPDS_PaveBlock], theCommonPaveBlocks: nanoocp.NCollection.NCollection_Map[nanoocp.BOPDS.BOPDS_PaveBlock]) -> None:
        """
        Returns information about ON/IN sub-shapes of the given faces.
        @param theFaceIndex1  the index of the first face
        @param theFaceIndex2  the index of the second face
        @param theMVOnIn  the indices of ON/IN vertices from both faces
        @param theMVCommon the indices of common vertices for both faces
        @param thePBOnIn  all On/In pave blocks from both faces
        @param theCommonPaveBlocks  the common pave blocks (that are shared by both faces).
        """

    def SharedEdges(self, theFaceIndex1: int, theFaceIndex2: int, theEdgeList: nanoocp.NCollection.NCollection_List[int], theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Returns the indices of edges that are shared
        for the faces with indices @p theFaceIndex1 and @p theFaceIndex2.
        """

    def ShapesSD(self) -> nanoocp.NCollection.NCollection_DataMap[int, int]:
        """
        Selector
        Returns the collection same domain shapes
        """

    def AddShapeSD(self, theIndex: int, theIndexSD: int) -> None:
        """
        Modifier
        Adds the information about same domain shapes
        with indices theIndex, theIndexSD
        """

    def HasShapeSD(self, theIndex: int) -> tuple[bool, int]:
        """
        Query
        Returns true if the shape with index theIndex has the
        same domain shape. In this case theIndexSD will contain
        the index of same domain shape found

        interferences
        """

    def GetSameDomainIndex(self, theIndex: int) -> int:
        """
        Returns the index of same domain shape for the shape
        with index @p theIndex. If there is no same domain shape, returns @p theIndex itself.
        """

    def InterfVV(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfVV]:
        """
        Selector/Modifier
        Returns the collection of interferences Vertex/Vertex
        """

    def InterfVE(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfVE]:
        """
        Selector/Modifier
        Returns the collection of interferences Vertex/Edge
        """

    def InterfVF(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfVF]:
        """
        Selector/Modifier
        Returns the collection of interferences Vertex/Face
        """

    def InterfEE(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfEE]:
        """
        Selector/Modifier
        Returns the collection of interferences Edge/Edge
        """

    def InterfEF(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfEF]:
        """
        Selector/Modifier
        Returns the collection of interferences Edge/Face
        """

    def InterfFF(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfFF]:
        """
        Selector/Modifier
        Returns the collection of interferences Face/Face
        """

    def InterfVZ(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfVZ]:
        """
        Selector/Modifier
        Returns the collection of interferences Vertex/Solid
        """

    def InterfEZ(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfEZ]:
        """
        Selector/Modifier
        Returns the collection of interferences Edge/Solid
        """

    def InterfFZ(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfFZ]:
        """
        Selector/Modifier
        Returns the collection of interferences Face/Solid
        """

    def InterfZZ(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfZZ]:
        """
        Selector/Modifier
        Returns the collection of interferences Solid/Solid
        """

    @staticmethod
    def NbInterfTypes() -> int:
        """Returns the number of types of the interferences"""

    def AddInterf(self, theI1: int, theI2: int) -> bool:
        """
        Modifier
        Adds the information about an interference between
        shapes with indices theI1, theI2 to the summary
        table of interferences
        """

    @overload
    def HasInterf(self, theI: int) -> bool:
        """
        Query
        Returns true if the shape with index theI
        is interferred
        """

    @overload
    def HasInterf(self, theI1: int, theI2: int) -> bool:
        """
        Query
        Returns true if the shapes with indices theI1, theI2
        are interferred
        """

    def HasInterfShapeSubShapes(self, theIndex1: int, theIndex2: int, theAnyInterference: bool = True) -> bool:
        """
        Query
        Returns true if the shape with index theIndex1 is interfered
        with
        any sub-shape of the shape with index theIndex2  (theAnyInterference=true)
        all sub-shapes of the shape with index theIndex2 (theAnyInterference=false)
        """

    def HasInterfSubShapes(self, theIndex1: int, theIndex2: int) -> bool:
        """
        Query
        Returns true if the shapes with indices theIndex1, theIndex2
        have interferred sub-shapes
        """

    def Interferences(self) -> nanoocp.NCollection.NCollection_Map[nanoocp.BOPDS.BOPDS_Pair]:
        """
        Selector
        Returns the table of interferences

        debug
        """

    def Dump(self) -> None: ...

    def IsSubShape(self, theCandidate: int, theParent: int) -> bool:
        """
        Returns true if the shape with index @p theCandidate is a sub-shape
        of the shape with index @p theParent
        """

    def Paves(self, theIndex: int, theLP: nanoocp.NCollection.NCollection_List[nanoocp.BOPDS.BOPDS_Pave]) -> None:
        """
        Fills theLP with sorted paves
        of the shape with index theIndex
        """

    def UpdatePaveBlocksWithSDVertices(self) -> None:
        """Update the pave blocks for all shapes in data structure"""

    def UpdatePaveBlockWithSDVertices(self, thePB: BOPDS_PaveBlock | None) -> None:
        """Update the pave block for all shapes in data structure"""

    def UpdateCommonBlockWithSDVertices(self, theCB: BOPDS_CommonBlock | None) -> None:
        """
        Update the pave block of the common block for all shapes in data structure
        """

    def InitPaveBlocksForVertex(self, theNV: int) -> None: ...

    def ReleasePaveBlocks(self) -> None:
        """Clears information about PaveBlocks for the untouched edges"""

    def IsValidShrunkData(self, thePB: BOPDS_PaveBlock | None) -> bool:
        """
        Checks if the existing shrunk data of the pave block is still valid.
        The shrunk data may become invalid if e.g. the vertices of the pave block
        have been replaced with the new one with bigger tolerances, or the tolerances
        of the existing vertices have been increased.
        """

    def BuildBndBoxSolid(self, theIndex: int, theBox: nanoocp.Bnd.Bnd_Box, theCheckInverted: bool = True) -> None:
        """
        Computes bounding box <theBox> for the solid with DS-index <theIndex>.
        The flag <theCheckInverted> enables/disables the check of the solid
        for inverted status. By default the solids will be checked.
        """

class BOPDS_Iterator:
    """
    The class BOPDS_Iterator is
    1.to compute intersections between BRep sub-shapes
    of arguments of an operation (see the class BOPDS_DS)
    in terms of theirs bounding boxes
    2.provides interface to iterate the pairs of
    intersected sub-shapes of given type
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator the allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_Iterator) -> None: ...

    def DS(self) -> BOPDS_DS:
        """
        Selector
        Returns the data structure
        """

    def Initialize(self, theType1: nanoocp.TopAbs.TopAbs_ShapeEnum, theType2: nanoocp.TopAbs.TopAbs_ShapeEnum) -> None:
        """
        Initializes the iterator
        theType1 - the first type of shape
        theType2 - the second type of shape
        """

    def More(self) -> bool:
        """
        Returns true if still there are pairs
        of intersected shapes
        """

    def Next(self) -> None:
        """Moves iterations ahead"""

    def Value(self) -> tuple[int, int]:
        """
        Returns indices (DS) of intersected shapes
        theIndex1 - the index of the first shape
        theIndex2 - the index of the second shape
        """

    def Prepare(self, theCtx: nanoocp.IntTools.IntTools_Context | None = None, theCheckOBB: bool = False, theFuzzyValue: float = 1e-07) -> None:
        """
        Perform the intersection algorithm and prepare
        the results to be used
        """

    def IntersectExt(self, theIndicies: nanoocp.NCollection.NCollection_Map[int]) -> None:
        """
        Updates the tree of Bounding Boxes with increased boxes and
        intersects such elements with the tree.
        """

    def ExpectedLength(self) -> int:
        """Returns the number of intersections founded"""

    def BlockLength(self) -> int:
        """Returns the block length"""

    def SetRunParallel(self, theFlag: bool) -> None:
        """
        Set the flag of parallel processing
        if <theFlag> is true  the parallel processing is switched on
        if <theFlag> is false the parallel processing is switched off
        """

    def RunParallel(self) -> bool:
        """Returns the flag of parallel processing"""

    @staticmethod
    def NbExtInterfs() -> int:
        """@name Number of extra interfering types"""

class BOPDS_IteratorSI(BOPDS_Iterator):
    """
    The class BOPDS_IteratorSI is
    1.to compute self-intersections between BRep sub-shapes
    of each argument of an operation (see the class BOPDS_DS)
    in terms of theirs bounding boxes
    2.provides interface to iterare the pairs of
    intersected sub-shapes of given type
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        @param theAllocator the allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_IteratorSI) -> None: ...

    def UpdateByLevelOfCheck(self, theLevel: int) -> None:
        """
        Updates the lists of possible intersections
        according to the value of <theLevel>.
        It defines which interferferences will be checked:
        0 - only V/V;
        1 - V/V and V/E;
        2 - V/V, V/E and E/E;
        3 - V/V, V/E, E/E and V/F;
        4 - V/V, V/E, E/E, V/F and E/F;
        other - all interferences.
        """

class BOPDS_SubIterator:
    """
    The class BOPDS_SubIterator is used to compute intersections between
    bounding boxes of two sub-sets of BRep sub-shapes of arguments
    of an operation (see the class BOPDS_DS).
    The class provides interface to iterate the pairs of intersected sub-shapes.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """
        Constructor
        theAllocator - the allocator to manage the memory
        """

    @overload
    def __init__(self, theOther: BOPDS_SubIterator) -> None: ...

    def DS(self) -> BOPDS_DS:
        """Returns the data structure"""

    def SetSubSet1(self, theLI: nanoocp.NCollection.NCollection_List[int]) -> None:
        """Sets the first set of indices <theLI> to process"""

    def SubSet1(self) -> nanoocp.NCollection.NCollection_List[int]:
        """Returns the first set of indices to process"""

    def SetSubSet2(self, theLI: nanoocp.NCollection.NCollection_List[int]) -> None:
        """Sets the second set of indices <theLI> to process"""

    def SubSet2(self) -> nanoocp.NCollection.NCollection_List[int]:
        """Returns the second set of indices to process"""

    def Initialize(self) -> None:
        """Initializes the iterator"""

    def More(self) -> bool:
        """Returns true if there are more pairs of intersected shapes"""

    def Next(self) -> None:
        """Moves iterations ahead"""

    def Value(self) -> tuple[int, int]:
        """
        Returns indices (DS) of intersected shapes
        theIndex1 - the index of the first shape
        theIndex2 - the index of the second shape
        """

    def Prepare(self) -> None:
        """
        Perform the intersection algorithm and prepare
        the results to be used
        """

    def ExpectedLength(self) -> int:
        """Returns the number of interfering pairs"""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.BOPDS
BOPDS_ListOfPave = nanoocp.NCollection.NCollection_List[nanoocp.BOPDS.BOPDS_Pave]
BOPDS_VectorOfCurve = nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_Curve]
BOPDS_VectorOfFaceInfo = nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_FaceInfo]
BOPDS_VectorOfInterfEE = nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfEE]
BOPDS_VectorOfInterfEF = nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfEF]
BOPDS_VectorOfInterfEZ = nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfEZ]
BOPDS_VectorOfInterfFF = nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfFF]
BOPDS_VectorOfInterfFZ = nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfFZ]
BOPDS_VectorOfInterfVE = nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfVE]
BOPDS_VectorOfInterfVF = nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfVF]
BOPDS_VectorOfInterfVV = nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfVV]
BOPDS_VectorOfInterfVZ = nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfVZ]
BOPDS_VectorOfInterfZZ = nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_InterfZZ]
BOPDS_VectorOfPoint = nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BOPDS.BOPDS_Point]
