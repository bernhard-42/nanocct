"""OCCT package TopOpeBRepBuild (toolkit TKBool)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TopAbs
import nanoocp.TopOpeBRepDS
import nanoocp.TopOpeBRepTool
import nanoocp.TopoDS
import nanoocp.gp


class TopOpeBRepBuild_LoopEnum(enum.IntEnum):
    TopOpeBRepBuild_ANYLOOP = 0

    TopOpeBRepBuild_BOUNDARY = 1

    TopOpeBRepBuild_BLOCK = 2

TopOpeBRepBuild_ANYLOOP: TopOpeBRepBuild_LoopEnum = TopOpeBRepBuild_LoopEnum.TopOpeBRepBuild_ANYLOOP

TopOpeBRepBuild_BOUNDARY: TopOpeBRepBuild_LoopEnum = TopOpeBRepBuild_LoopEnum.TopOpeBRepBuild_BOUNDARY

TopOpeBRepBuild_BLOCK: TopOpeBRepBuild_LoopEnum = TopOpeBRepBuild_LoopEnum.TopOpeBRepBuild_BLOCK

class TopOpeBRepBuild_BlockIterator:
    """Iterator on the elements of a block."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Lower: int, Upper: int) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_BlockIterator) -> None: ...

    def __iter__(self) -> TopOpeBRepBuild_BlockIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> int:
        """Python addition: see __iter__."""

    def Initialize(self) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Value(self) -> int: ...

    def Extent(self) -> int: ...

class TopOpeBRepBuild_Loop(nanoocp.Standard.Standard_Transient):
    """
    a Loop is an existing shape (Shell,Wire) or a set
    of shapes (Faces,Edges) which are connex.
    a set of connex shape is represented by a BlockIterator
    """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, BI: TopOpeBRepBuild_BlockIterator) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_Loop) -> None: ...

    def IsShape(self) -> bool: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def BlockIterator(self) -> TopOpeBRepBuild_BlockIterator: ...

    def Dump(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepBuild_AreaBuilder:
    """
    The AreaBuilder algorithm is used to
    reconstruct complex topological objects as Faces
    or Solids.
    * Loop is the composite topological object of
    the boundary. Wire for a Face. Shell for a Solid.
    * LoopSet is a tool describing the object to
    build. It gives an iteration on Loops. For each
    Loop it tells if it is on the boundary or if it is
    an interference.
    * LoopClassifier is an algorithm used to test
    if a Loop is inside another Loop.
    The result of the reconstruction is an iteration
    on the reconstructed areas. An area is described
    by a set of Loops.
    A AreaBuilder is built with:
    - a LoopSet describing the object to reconstruct.
    - a LoopClassifier providing the classification algorithm.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, LS: TopOpeBRepBuild_LoopSet, LC: TopOpeBRepBuild_LoopClassifier, ForceClass: bool = False) -> None:
        """
        Creates a AreaBuilder to build the areas on
        the shapes described by <LS> using the classifier <LC>.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_AreaBuilder) -> None: ...

    def InitAreaBuilder(self, LS: TopOpeBRepBuild_LoopSet, LC: TopOpeBRepBuild_LoopClassifier, ForceClass: bool = False) -> None:
        """
        Sets a AreaBuilder to find the areas on
        the shapes described by <LS> using the classifier <LC>.
        """

    def InitArea(self) -> int:
        """Initialize iteration on areas."""

    def MoreArea(self) -> bool: ...

    def NextArea(self) -> None: ...

    def InitLoop(self) -> int:
        """Initialize iteration on loops of current Area."""

    def MoreLoop(self) -> bool: ...

    def NextLoop(self) -> None: ...

    def Loop(self) -> TopOpeBRepBuild_Loop:
        """Returns the current Loop in the current area."""

    def ADD_Loop_TO_LISTOFLoop(self, L: TopOpeBRepBuild_Loop | None, LOL: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Loop]) -> None: ...

    def REM_Loop_FROM_LISTOFLoop(self, ITLOL: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Loop].Iterator, LOL: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Loop]) -> None: ...

    def ADD_LISTOFLoop_TO_LISTOFLoop(self, LOL1: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Loop], LOL2: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Loop]) -> None: ...

class TopOpeBRepBuild_Area1dBuilder(TopOpeBRepBuild_AreaBuilder):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, LS: TopOpeBRepBuild_PaveSet, LC: TopOpeBRepBuild_PaveClassifier, ForceClass: bool = False) -> None:
        """
        Creates a Area1dBuilder to find the areas of
        the shapes described by <LS> using the classifier <LC>.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_Area1dBuilder) -> None: ...

    def InitAreaBuilder(self, LS: TopOpeBRepBuild_LoopSet, LC: TopOpeBRepBuild_LoopClassifier, ForceClass: bool = False) -> None:
        """
        Sets a Area1dBuilder to find the areas of
        the shapes described by <LS> using the classifier <LC>.
        """

    def ADD_Loop_TO_LISTOFLoop(self, L: TopOpeBRepBuild_Loop | None, LOL: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Loop]) -> None: ...

    def REM_Loop_FROM_LISTOFLoop(self, ITLOL: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Loop].Iterator, LOL: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Loop]) -> None: ...

    def ADD_LISTOFLoop_TO_LISTOFLoop(self, LOL1: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Loop], LOL2: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Loop]) -> None: ...

    @staticmethod
    def DumpList(L: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Loop]) -> None: ...

class TopOpeBRepBuild_Area2dBuilder(TopOpeBRepBuild_AreaBuilder):
    """
    The Area2dBuilder algorithm is used to construct Faces from a LoopSet,
    where the Loop is the composite topological object of the boundary,
    here wire or block of edges.
    The LoopSet gives an iteration on Loops.
    For each Loop it indicates if it is on the boundary (wire) or if it
    results from an interference (block of edges).
    The result of the Area2dBuilder is an iteration on areas.
    An area is described by a set of Loops.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, LS: TopOpeBRepBuild_LoopSet, LC: TopOpeBRepBuild_LoopClassifier, ForceClass: bool = False) -> None:
        """
        Creates a Area2dBuilder to build faces on
        the (wires,blocks of edge) of <LS>, using the classifier <LC>.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_Area2dBuilder) -> None: ...

    def InitAreaBuilder(self, LS: TopOpeBRepBuild_LoopSet, LC: TopOpeBRepBuild_LoopClassifier, ForceClass: bool = False) -> None:
        """
        Sets a Area1dBuilder to find the areas of
        the shapes described by <LS> using the classifier <LC>.
        """

class TopOpeBRepBuild_Area3dBuilder(TopOpeBRepBuild_AreaBuilder):
    """
    The Area3dBuilder algorithm is used to construct Solids from a LoopSet,
    where the Loop is the composite topological object of the boundary,
    here wire or block of edges.
    The LoopSet gives an iteration on Loops.
    For each Loop it indicates if it is on the boundary (wire) or if it
    results from an interference (block of edges).
    The result of the Area3dBuilder is an iteration on areas.
    An area is described by a set of Loops.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, LS: TopOpeBRepBuild_LoopSet, LC: TopOpeBRepBuild_LoopClassifier, ForceClass: bool = False) -> None:
        """
        Creates a Area3dBuilder to build Solids on
        the (shells,blocks of face) of <LS>, using the classifier <LC>.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_Area3dBuilder) -> None: ...

    def InitAreaBuilder(self, LS: TopOpeBRepBuild_LoopSet, LC: TopOpeBRepBuild_LoopClassifier, ForceClass: bool = False) -> None:
        """
        Sets a Area1dBuilder to find the areas of
        the shapes described by <LS> using the classifier <LC>.
        """

class TopOpeBRepBuild_BlockBuilder:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, SS: TopOpeBRepBuild_ShapeSet) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_BlockBuilder) -> None: ...

    def MakeBlock(self, SS: TopOpeBRepBuild_ShapeSet) -> None: ...

    def InitBlock(self) -> None: ...

    def MoreBlock(self) -> bool: ...

    def NextBlock(self) -> None: ...

    def BlockIterator(self) -> TopOpeBRepBuild_BlockIterator: ...

    @overload
    def Element(self, BI: TopOpeBRepBuild_BlockIterator) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the current element of <BI>."""

    @overload
    def Element(self, I: int) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def Element(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    @overload
    def ElementIsValid(self, BI: TopOpeBRepBuild_BlockIterator) -> bool: ...

    @overload
    def ElementIsValid(self, I: int) -> bool: ...

    def AddElement(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    @overload
    def SetValid(self, BI: TopOpeBRepBuild_BlockIterator, isvalid: bool) -> None: ...

    @overload
    def SetValid(self, I: int, isvalid: bool) -> None: ...

    def CurrentBlockIsRegular(self) -> bool: ...

class TopOpeBRepBuild_Builder:
    """
    The Builder algorithm constructs topological
    objects from an existing topology and new
    geometries attached to the topology. It is used to
    construct the result of a topological operation;
    the existing topologies are the parts involved in
    the topological operation and the new geometries
    are the intersection lines and points.
    """

    @overload
    def __init__(self, BT: nanoocp.TopOpeBRepDS.TopOpeBRepDS_BuildTool) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_Builder) -> None: ...

    def ChangeBuildTool(self) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_BuildTool: ...

    def BuildTool(self) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_BuildTool: ...

    @overload
    def Perform(self, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None:
        """
        Stores the data structure <HDS>,
        Create shapes from the new geometries.
        """

    @overload
    def Perform(self, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Stores the data structure <HDS>,
        Create shapes from the new geometries,
        Evaluates if an operation performed on shapes S1,S2
        is a particular case.
        """

    def DataStructure(self) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure:
        """returns the DS handled by this builder"""

    def Clear(self) -> None:
        """
        Removes all splits and merges already performed.
        Does NOT clear the handled DS.
        """

    def MergeEdges(self, L1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], TB1: nanoocp.TopAbs.TopAbs_State, L2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], TB2: nanoocp.TopAbs.TopAbs_State, onA: bool = False, onB: bool = False, onAB: bool = False) -> None:
        """
        Merges the two edges <S1> and <S2> keeping the
        parts in each edge of states <TB1> and <TB2>.
        Booleans onA, onB, onAB indicate whether parts of edges
        found as state ON respectively on first, second, and both
        shapes must be (or not) built.
        """

    def MergeFaces(self, S1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], TB1: nanoocp.TopAbs.TopAbs_State, S2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], TB2: nanoocp.TopAbs.TopAbs_State, onA: bool = False, onB: bool = False, onAB: bool = False) -> None:
        """
        Merges the two faces <S1> and <S2> keeping the
        parts in each face of states <TB1> and <TB2>.
        """

    def MergeSolids(self, S1: nanoocp.TopoDS.TopoDS_Shape, TB1: nanoocp.TopAbs.TopAbs_State, S2: nanoocp.TopoDS.TopoDS_Shape, TB2: nanoocp.TopAbs.TopAbs_State) -> None:
        """
        Merges the two solids <S1> and <S2> keeping the
        parts in each solid of states <TB1> and <TB2>.
        """

    def MergeShapes(self, S1: nanoocp.TopoDS.TopoDS_Shape, TB1: nanoocp.TopAbs.TopAbs_State, S2: nanoocp.TopoDS.TopoDS_Shape, TB2: nanoocp.TopAbs.TopAbs_State) -> None:
        """
        Merges the two shapes <S1> and <S2> keeping the
        parts of states <TB1>,<TB2> in <S1>,<S2>.
        """

    def End(self) -> None: ...

    def Classify(self) -> bool: ...

    def ChangeClassify(self, B: bool) -> None: ...

    def MergeSolid(self, S: nanoocp.TopoDS.TopoDS_Shape, TB: nanoocp.TopAbs.TopAbs_State) -> None:
        """
        Merges the solid <S> keeping the
        parts of state <TB>.
        """

    def NewVertex(self, I: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the vertex created on point <I>."""

    def NewEdges(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the edges created on curve <I>."""

    def NewFaces(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the faces created on surface <I>."""

    def IsSplit(self, S: nanoocp.TopoDS.TopoDS_Shape, TB: nanoocp.TopAbs.TopAbs_State) -> bool:
        """Returns True if the shape <S> has been split."""

    def Splits(self, S: nanoocp.TopoDS.TopoDS_Shape, TB: nanoocp.TopAbs.TopAbs_State) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the split parts <TB> of shape <S>."""

    def IsMerged(self, S: nanoocp.TopoDS.TopoDS_Shape, TB: nanoocp.TopAbs.TopAbs_State) -> bool:
        """Returns True if the shape <S> has been merged."""

    def Merged(self, S: nanoocp.TopoDS.TopoDS_Shape, TB: nanoocp.TopAbs.TopAbs_State) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the merged parts <TB> of shape <S>."""

    def InitSection(self) -> None: ...

    def SplitSectionEdges(self) -> None:
        """create parts ON solid of section edges"""

    def SplitSectionEdge(self, E: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """create parts ON solid of section edges"""

    def SectionCurves(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """return the section edges built on new curves."""

    def SectionEdges(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        return the parts of edges found ON the boundary
        of the two arguments S1,S2 of Perform()
        """

    def FillSecEdgeAncestorMap(self, aShapeRank: int, aMapON: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], anAncMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        Fills anAncMap with pairs (edge,ancestor edge) for each
        split from the map aMapON for the shape object identified
        by ShapeRank
        """

    @overload
    def Section(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """return all section edges."""

    @overload
    def Section(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def BuildVertices(self, DS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None:
        """
        update the DS by creating new geometries.
        create vertices on DS points.
        """

    def BuildEdges(self, DS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None:
        """
        update the DS by creating new geometries.
        create shapes from the new geometries.
        """

    def MSplit(self, s: nanoocp.TopAbs.TopAbs_State) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ListOfShapeOn1State, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    def ChangeMSplit(self, s: nanoocp.TopAbs.TopAbs_State) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ListOfShapeOn1State, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    def MakeEdges(self, E: nanoocp.TopoDS.TopoDS_Shape, B: TopOpeBRepBuild_EdgeBuilder, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def MakeFaces(self, F: nanoocp.TopoDS.TopoDS_Shape, B: TopOpeBRepBuild_FaceBuilder, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def MakeSolids(self, B: TopOpeBRepBuild_SolidBuilder, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def MakeShells(self, B: TopOpeBRepBuild_SolidBuilder, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def ChangeSplit(self, S: nanoocp.TopoDS.TopoDS_Shape, TB: nanoocp.TopAbs.TopAbs_State) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns a ref.on the list of shapes connected to <S> as
        <TB> split parts of <S>.
        Mark <S> as split in <TB> parts.
        """

    def Opec12(self) -> bool: ...

    def Opec21(self) -> bool: ...

    def Opecom(self) -> bool: ...

    def Opefus(self) -> bool: ...

    def ShapePosition(self, S: nanoocp.TopoDS.TopoDS_Shape, LS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> nanoocp.TopAbs.TopAbs_State: ...

    def KeepShape(self, S: nanoocp.TopoDS.TopoDS_Shape, LS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], T: nanoocp.TopAbs.TopAbs_State) -> bool: ...

    @staticmethod
    def TopType(S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_ShapeEnum: ...

    @staticmethod
    def Reverse(T1: nanoocp.TopAbs.TopAbs_State, T2: nanoocp.TopAbs.TopAbs_State) -> bool: ...

    @staticmethod
    def Orient(O: nanoocp.TopAbs.TopAbs_Orientation, R: bool) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def FindSameDomain(self, L1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], L2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def FindSameDomainSameOrientation(self, LSO: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LDO: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def MapShapes(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def ClearMaps(self) -> None: ...

    def FindSameRank(self, L1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], R: int, L2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def ShapeRank(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    def IsShapeOf(self, S: nanoocp.TopoDS.TopoDS_Shape, I12: int) -> bool: ...

    @staticmethod
    def Contains(S: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

    def FindIsKPart(self) -> int: ...

    def IsKPart(self) -> int: ...

    @overload
    def MergeKPart(self) -> None: ...

    @overload
    def MergeKPart(self, TB1: nanoocp.TopAbs.TopAbs_State, TB2: nanoocp.TopAbs.TopAbs_State) -> None: ...

    def MergeKPartiskole(self) -> None: ...

    def MergeKPartiskoletge(self) -> None: ...

    def MergeKPartisdisj(self) -> None: ...

    def MergeKPartisfafa(self) -> None: ...

    def MergeKPartissoso(self) -> None: ...

    def KPiskole(self) -> int: ...

    def KPiskoletge(self) -> int: ...

    def KPisdisj(self) -> int: ...

    def KPisfafa(self) -> int: ...

    def KPissoso(self) -> int: ...

    def KPClearMaps(self) -> None: ...

    @overload
    def KPlhg(self, S: nanoocp.TopoDS.TopoDS_Shape, T: nanoocp.TopAbs.TopAbs_ShapeEnum, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> int: ...

    @overload
    def KPlhg(self, S: nanoocp.TopoDS.TopoDS_Shape, T: nanoocp.TopAbs.TopAbs_ShapeEnum) -> int: ...

    @overload
    def KPlhsd(self, S: nanoocp.TopoDS.TopoDS_Shape, T: nanoocp.TopAbs.TopAbs_ShapeEnum, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> int: ...

    @overload
    def KPlhsd(self, S: nanoocp.TopoDS.TopoDS_Shape, T: nanoocp.TopAbs.TopAbs_ShapeEnum) -> int: ...

    @overload
    def KPclasSS(self, S1: nanoocp.TopoDS.TopoDS_Shape, exceptLS1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], S2: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_State: ...

    @overload
    def KPclasSS(self, S1: nanoocp.TopoDS.TopoDS_Shape, exceptS1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_State: ...

    @overload
    def KPclasSS(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_State: ...

    def KPiskolesh(self, S: nanoocp.TopoDS.TopoDS_Shape, LS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

    def KPiskoletgesh(self, S: nanoocp.TopoDS.TopoDS_Shape, LS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

    def KPSameDomain(self, L1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], L2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def KPisdisjsh(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    def KPisfafash(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    def KPissososh(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    def KPiskoleanalyse(self, FT1: nanoocp.TopAbs.TopAbs_State, FT2: nanoocp.TopAbs.TopAbs_State, ST1: nanoocp.TopAbs.TopAbs_State, ST2: nanoocp.TopAbs.TopAbs_State) -> tuple[int, int, int]: ...

    def KPiskoletgeanalyse(self, Conf: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Config, ST1: nanoocp.TopAbs.TopAbs_State, ST2: nanoocp.TopAbs.TopAbs_State) -> int: ...

    def KPisdisjanalyse(self, ST1: nanoocp.TopAbs.TopAbs_State, ST2: nanoocp.TopAbs.TopAbs_State) -> tuple[int, int, int]: ...

    @overload
    @staticmethod
    def KPls(S: nanoocp.TopoDS.TopoDS_Shape, T: nanoocp.TopAbs.TopAbs_ShapeEnum, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> int: ...

    @overload
    @staticmethod
    def KPls(S: nanoocp.TopoDS.TopoDS_Shape, T: nanoocp.TopAbs.TopAbs_ShapeEnum) -> int: ...

    def KPclassF(self, F1: nanoocp.TopoDS.TopoDS_Shape, F2: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_State: ...

    def KPclassFF(self, F1: nanoocp.TopoDS.TopoDS_Shape, F2: nanoocp.TopoDS.TopoDS_Shape) -> tuple[nanoocp.TopAbs.TopAbs_State, nanoocp.TopAbs.TopAbs_State]: ...

    def KPiskoleFF(self, F1: nanoocp.TopoDS.TopoDS_Shape, F2: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, nanoocp.TopAbs.TopAbs_State, nanoocp.TopAbs.TopAbs_State]: ...

    @staticmethod
    def KPContains(S: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

    def KPmakeface(self, F1: nanoocp.TopoDS.TopoDS_Shape, LF2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], T1: nanoocp.TopAbs.TopAbs_State, T2: nanoocp.TopAbs.TopAbs_State, R1: bool, R2: bool) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @staticmethod
    def KPreturn(KP: int) -> int: ...

    def SplitEvisoONperiodicF(self) -> None: ...

    def GMergeSolids(self, LSO1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LSO2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo) -> None: ...

    def GFillSolidsSFS(self, LSO1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LSO2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, SFS: TopOpeBRepBuild_ShellFaceSet) -> None: ...

    def GFillSolidSFS(self, SO1: nanoocp.TopoDS.TopoDS_Shape, LSO2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, SFS: TopOpeBRepBuild_ShellFaceSet) -> None: ...

    @overload
    def GFillSurfaceTopologySFS(self, SO1: nanoocp.TopoDS.TopoDS_Shape, G: TopOpeBRepBuild_GTopo, SFS: TopOpeBRepBuild_ShellFaceSet) -> None: ...

    @overload
    def GFillSurfaceTopologySFS(self, IT: nanoocp.TopOpeBRepDS.TopOpeBRepDS_SurfaceIterator, G: TopOpeBRepBuild_GTopo, SFS: TopOpeBRepBuild_ShellFaceSet) -> None: ...

    def GFillShellSFS(self, SH1: nanoocp.TopoDS.TopoDS_Shape, LSO2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, SFS: TopOpeBRepBuild_ShellFaceSet) -> None: ...

    def GFillFaceSFS(self, F1: nanoocp.TopoDS.TopoDS_Shape, LSO2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, SFS: TopOpeBRepBuild_ShellFaceSet) -> None: ...

    def GSplitFaceSFS(self, F1: nanoocp.TopoDS.TopoDS_Shape, LSclass: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, SFS: TopOpeBRepBuild_ShellFaceSet) -> None: ...

    def GMergeFaceSFS(self, F: nanoocp.TopoDS.TopoDS_Shape, G: TopOpeBRepBuild_GTopo, SFS: TopOpeBRepBuild_ShellFaceSet) -> None: ...

    def GSplitFace(self, F: nanoocp.TopoDS.TopoDS_Shape, G: TopOpeBRepBuild_GTopo, LSclass: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def AddONPatchesSFS(self, G: TopOpeBRepBuild_GTopo, SFS: TopOpeBRepBuild_ShellFaceSet) -> None: ...

    def FillOnPatches(self, anEdgesON: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], aBaseFace: nanoocp.TopoDS.TopoDS_Shape, avoidMap: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def FindFacesTouchingEdge(self, aFace: nanoocp.TopoDS.TopoDS_Shape, anEdge: nanoocp.TopoDS.TopoDS_Shape, aShRank: int, aFaces: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def GMergeFaces(self, LF1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LF2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo) -> None: ...

    def GFillFacesWES(self, LF1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LF2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    def GFillFacesWESK(self, LF1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LF2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet, K: int) -> None: ...

    def GFillFacesWESMakeFaces(self, LF1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LF2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LSO: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo) -> None: ...

    def GFillFaceWES(self, F: nanoocp.TopoDS.TopoDS_Shape, LF2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    @overload
    def GFillCurveTopologyWES(self, F: nanoocp.TopoDS.TopoDS_Shape, G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    @overload
    def GFillCurveTopologyWES(self, IT: nanoocp.TopOpeBRepDS.TopOpeBRepDS_CurveIterator, G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    def GFillONPartsWES(self, F: nanoocp.TopoDS.TopoDS_Shape, G: TopOpeBRepBuild_GTopo, LSclass: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    def GFillWireWES(self, W: nanoocp.TopoDS.TopoDS_Shape, LF2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    def GFillEdgeWES(self, E: nanoocp.TopoDS.TopoDS_Shape, LF2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    def GSplitEdgeWES(self, E: nanoocp.TopoDS.TopoDS_Shape, LF2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    def GMergeEdgeWES(self, E: nanoocp.TopoDS.TopoDS_Shape, G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    def GSplitEdge(self, E: nanoocp.TopoDS.TopoDS_Shape, G: TopOpeBRepBuild_GTopo, LSclass: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def GMergeEdges(self, LE1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LE2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo) -> None: ...

    def GFillEdgesPVS(self, LE1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LE2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, PVS: TopOpeBRepBuild_PaveSet) -> None: ...

    def GFillEdgePVS(self, E: nanoocp.TopoDS.TopoDS_Shape, LE2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, PVS: TopOpeBRepBuild_PaveSet) -> None: ...

    @overload
    def GFillPointTopologyPVS(self, E: nanoocp.TopoDS.TopoDS_Shape, G: TopOpeBRepBuild_GTopo, PVS: TopOpeBRepBuild_PaveSet) -> None: ...

    @overload
    def GFillPointTopologyPVS(self, E: nanoocp.TopoDS.TopoDS_Shape, IT: nanoocp.TopOpeBRepDS.TopOpeBRepDS_PointIterator, G: TopOpeBRepBuild_GTopo, PVS: TopOpeBRepBuild_PaveSet) -> None: ...

    def GParamOnReference(self, V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float]: ...

    def GKeepShape(self, S: nanoocp.TopoDS.TopoDS_Shape, Lref: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], T: nanoocp.TopAbs.TopAbs_State) -> bool: ...

    def GKeepShape1(self, S: nanoocp.TopoDS.TopoDS_Shape, Lref: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], T: nanoocp.TopAbs.TopAbs_State) -> tuple[bool, nanoocp.TopAbs.TopAbs_State]:
        """return True if S is classified <T> / Lref shapes"""

    def GKeepShapes(self, S: nanoocp.TopoDS.TopoDS_Shape, Lref: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], T: nanoocp.TopAbs.TopAbs_State, Lin: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], Lou: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        add to Lou the shapes of Lin classified <T> / Lref shapes.
        Lou is not cleared. (S is a dummy trace argument)
        """

    def GSFSMakeSolids(self, SOF: nanoocp.TopoDS.TopoDS_Shape, SFS: TopOpeBRepBuild_ShellFaceSet, LOSO: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def GSOBUMakeSolids(self, SOF: nanoocp.TopoDS.TopoDS_Shape, SOBU: TopOpeBRepBuild_SolidBuilder, LOSO: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def GWESMakeFaces(self, FF: nanoocp.TopoDS.TopoDS_Shape, WES: TopOpeBRepBuild_WireEdgeSet, LOF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def GFABUMakeFaces(self, FF: nanoocp.TopoDS.TopoDS_Shape, FABU: TopOpeBRepBuild_FaceBuilder, LOF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], MWisOld: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, int, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    def RegularizeFaces(self, FF: nanoocp.TopoDS.TopoDS_Shape, lnewFace: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LOF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def RegularizeFace(self, FF: nanoocp.TopoDS.TopoDS_Shape, newFace: nanoocp.TopoDS.TopoDS_Shape, LOF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def RegularizeSolids(self, SS: nanoocp.TopoDS.TopoDS_Shape, lnewSolid: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LOS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def RegularizeSolid(self, SS: nanoocp.TopoDS.TopoDS_Shape, newSolid: nanoocp.TopoDS.TopoDS_Shape, LOS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def GPVSMakeEdges(self, EF: nanoocp.TopoDS.TopoDS_Shape, PVS: TopOpeBRepBuild_PaveSet, LOE: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def GEDBUMakeEdges(self, EF: nanoocp.TopoDS.TopoDS_Shape, EDBU: TopOpeBRepBuild_EdgeBuilder, LOE: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def GToSplit(self, S: nanoocp.TopoDS.TopoDS_Shape, TB: nanoocp.TopAbs.TopAbs_State) -> bool: ...

    def GToMerge(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    @staticmethod
    def GTakeCommonOfSame(G: TopOpeBRepBuild_GTopo) -> bool: ...

    @staticmethod
    def GTakeCommonOfDiff(G: TopOpeBRepBuild_GTopo) -> bool: ...

    @overload
    def GFindSamDom(self, S: nanoocp.TopoDS.TopoDS_Shape, L1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], L2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    @overload
    def GFindSamDom(self, L1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], L2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    @overload
    def GFindSamDomSODO(self, S: nanoocp.TopoDS.TopoDS_Shape, LSO: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LDO: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    @overload
    def GFindSamDomSODO(self, LSO: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LDO: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def GMapShapes(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def GClearMaps(self) -> None: ...

    def GFindSameRank(self, L1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], R: int, L2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def GShapeRank(self, S: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    def GIsShapeOf(self, S: nanoocp.TopoDS.TopoDS_Shape, I12: int) -> bool: ...

    @staticmethod
    def GContains(S: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool: ...

    @overload
    @staticmethod
    def GCopyList(Lin: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], i1: int, i2: int, Lou: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    @overload
    @staticmethod
    def GCopyList(Lin: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], Lou: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def GdumpLS(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    @staticmethod
    def GdumpPNT(P: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def GdumpORIPARPNT(o: nanoocp.TopAbs.TopAbs_Orientation, p: float, Pnt: nanoocp.gp.gp_Pnt) -> None: ...

    def GdumpSHA(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def GdumpSHAORI(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def GdumpSHAORIGEO(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def GdumpSHASTA(self, iS: int, T: nanoocp.TopAbs.TopAbs_State, a: nanoocp.TCollection.TCollection_AsciiString = ..., b: nanoocp.TCollection.TCollection_AsciiString = ...) -> None: ...

    @overload
    def GdumpSHASTA(self, S: nanoocp.TopoDS.TopoDS_Shape, T: nanoocp.TopAbs.TopAbs_State, a: nanoocp.TCollection.TCollection_AsciiString = ..., b: nanoocp.TCollection.TCollection_AsciiString = ...) -> None: ...

    @overload
    def GdumpSHASTA(self, iS: int, T: nanoocp.TopAbs.TopAbs_State, SS: TopOpeBRepBuild_ShapeSet, a: nanoocp.TCollection.TCollection_AsciiString = ..., b: nanoocp.TCollection.TCollection_AsciiString = ..., c: nanoocp.TCollection.TCollection_AsciiString = ...) -> None: ...

    def GdumpEDG(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def GdumpEDGVER(self, E: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def GdumpSAMDOM(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def GdumpEXP(self, E: nanoocp.TopOpeBRepTool.TopOpeBRepTool_ShapeExplorer) -> None: ...

    def GdumpSOBU(self, SB: TopOpeBRepBuild_SolidBuilder) -> None: ...

    def GdumpFABU(self, FB: TopOpeBRepBuild_FaceBuilder) -> None: ...

    def GdumpEDBU(self, EB: TopOpeBRepBuild_EdgeBuilder) -> None: ...

    @overload
    def GtraceSPS(self, iS: int) -> bool: ...

    @overload
    def GtraceSPS(self, iS: int, jS: int) -> bool: ...

    @overload
    def GtraceSPS(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def GtraceSPS__int(self, S: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, int]:
        """
        GtraceSPS__int: the C++ overload GtraceSPS(const TopoDS_Shape &, int &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        """

    def GdumpSHASETreset(self) -> None: ...

    def GdumpSHASETindex(self) -> int: ...

    @staticmethod
    def PrintGeo(S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @staticmethod
    def PrintSur(F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @staticmethod
    def PrintCur(E: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    @staticmethod
    def PrintPnt(V: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @staticmethod
    def PrintOri(S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @staticmethod
    def StringState(S: nanoocp.TopAbs.TopAbs_State) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @staticmethod
    def GcheckNBOUNDS(E: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

class TopOpeBRepBuild_Builder1(TopOpeBRepBuild_Builder):
    """
    extension of the class TopOpeBRepBuild_Builder dedicated
    to avoid bugs in "Rebuilding Result" algorithm for the
    case of SOLID/SOLID Boolean Operations
    """

    @overload
    def __init__(self, BT: nanoocp.TopOpeBRepDS.TopOpeBRepDS_BuildTool) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_Builder1) -> None: ...

    def Clear(self) -> None:
        """
        Removes all splits and merges already performed.
        Does NOT clear the handled DS (except ShapeWithStatesMaps).
        """

    @overload
    def Perform(self, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None: ...

    @overload
    def Perform(self, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def MergeKPart(self) -> None: ...

    @overload
    def MergeKPart(self, TB1: nanoocp.TopAbs.TopAbs_State, TB2: nanoocp.TopAbs.TopAbs_State) -> None: ...

    def GFillSolidSFS(self, SO1: nanoocp.TopoDS.TopoDS_Shape, LSO2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, SFS: TopOpeBRepBuild_ShellFaceSet) -> None: ...

    def GFillShellSFS(self, SH1: nanoocp.TopoDS.TopoDS_Shape, LSO2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, SFS: TopOpeBRepBuild_ShellFaceSet) -> None: ...

    def GWESMakeFaces(self, FF: nanoocp.TopoDS.TopoDS_Shape, WES: TopOpeBRepBuild_WireEdgeSet, LOF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def GFillFaceNotSameDomSFS(self, F1: nanoocp.TopoDS.TopoDS_Shape, LSO2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, SFS: TopOpeBRepBuild_ShellFaceSet) -> None: ...

    def GFillFaceNotSameDomWES(self, F1: nanoocp.TopoDS.TopoDS_Shape, LSO2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    def GFillWireNotSameDomWES(self, W1: nanoocp.TopoDS.TopoDS_Shape, LSO2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    def GFillEdgeNotSameDomWES(self, E1: nanoocp.TopoDS.TopoDS_Shape, LSO2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    def GFillFaceSameDomSFS(self, F1: nanoocp.TopoDS.TopoDS_Shape, LSO2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, SFS: TopOpeBRepBuild_ShellFaceSet) -> None: ...

    def GFillFaceSameDomWES(self, F1: nanoocp.TopoDS.TopoDS_Shape, LSO2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    def GFillWireSameDomWES(self, W1: nanoocp.TopoDS.TopoDS_Shape, LSO2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    def GFillEdgeSameDomWES(self, E1: nanoocp.TopoDS.TopoDS_Shape, LSO2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    def PerformONParts(self, F: nanoocp.TopoDS.TopoDS_Shape, SDfaces: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], G: TopOpeBRepBuild_GTopo, WES: TopOpeBRepBuild_WireEdgeSet) -> None: ...

    def PerformPieceIn2D(self, aPieceToPerform: nanoocp.TopoDS.TopoDS_Edge, aOriginalEdge: nanoocp.TopoDS.TopoDS_Edge, edgeFace: nanoocp.TopoDS.TopoDS_Face, toFace: nanoocp.TopoDS.TopoDS_Face, G: TopOpeBRepBuild_GTopo) -> bool: ...

    def PerformPieceOn2D(self, aPieceObj: nanoocp.TopoDS.TopoDS_Shape, aFaceObj: nanoocp.TopoDS.TopoDS_Shape, aEdgeObj: nanoocp.TopoDS.TopoDS_Shape, aListOfPieces: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], aListOfFaces: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], aListOfPiecesOut2d: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> int: ...

    def TwoPiecesON(self, aSeq: nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape], aListOfPieces: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], aListOfFaces: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], aListOfPiecesOut2d: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> int: ...

    def CorrectResult2d(self, aResult: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

class TopOpeBRepBuild_BuilderON:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_BuilderON) -> None: ...

    def GFillONCheckI(self, I: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference | None) -> bool: ...

    def GFillONPartsWES1(self, I: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference | None) -> None: ...

    def GFillONPartsWES2(self, I: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference | None, EspON: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def GFillONParts2dWES2(self, I: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Interference | None, EspON: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

class TopOpeBRepBuild_LoopClassifier:
    """classify loops in order to build Areas"""

    def Compare(self, L1: TopOpeBRepBuild_Loop | None, L2: TopOpeBRepBuild_Loop | None) -> nanoocp.TopAbs.TopAbs_State:
        """Returns the state of loop <L1> compared with loop <L2>."""

class TopOpeBRepBuild_CompositeClassifier(TopOpeBRepBuild_LoopClassifier):
    """
    classify composite Loops, i.e, loops that can be either a Shape, or
    a block of Elements.
    """

    def Compare(self, L1: TopOpeBRepBuild_Loop | None, L2: TopOpeBRepBuild_Loop | None) -> nanoocp.TopAbs.TopAbs_State: ...

    def CompareShapes(self, B1: nanoocp.TopoDS.TopoDS_Shape, B2: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_State:
        """classify shape <B1> with shape <B2>"""

    def CompareElementToShape(self, E: nanoocp.TopoDS.TopoDS_Shape, B: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_State:
        """classify element <E> with shape <B>"""

    def ResetShape(self, B: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        prepare classification involving shape <B>
        calls ResetElement on first element of <B>
        """

    def ResetElement(self, E: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """prepare classification involving element <E>."""

    def CompareElement(self, E: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Add element <E> in the set of elements used in classification.
        Returns FALSE if the element <E> has been already added to the set of elements,
        otherwise returns TRUE.
        """

    def State(self) -> nanoocp.TopAbs.TopAbs_State:
        """
        Returns state of classification of 2D point, defined by
        ResetElement, with the current set of elements, defined by Compare.
        """

class TopOpeBRepBuild_CorrectFace2d:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aFace: nanoocp.TopoDS.TopoDS_Face, anAvoidMap: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape], aMap: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_CorrectFace2d) -> None: ...

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def Perform(self) -> None: ...

    def IsDone(self) -> bool: ...

    def ErrorStatus(self) -> int: ...

    def CorrectedFace(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def SetMapOfTrans2dInfo(self, aMap: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    def MapOfTrans2dInfo(self) -> nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    @staticmethod
    def GetP2dFL(aFace: nanoocp.TopoDS.TopoDS_Face, anEdge: nanoocp.TopoDS.TopoDS_Edge, P2dF: nanoocp.gp.gp_Pnt2d, P2dL: nanoocp.gp.gp_Pnt2d) -> None: ...

    @staticmethod
    def CheckList(aFace: nanoocp.TopoDS.TopoDS_Face, aHeadList: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

class TopOpeBRepBuild_ShapeSet:
    """
    Auxiliary class providing an exploration of a set
    of shapes to build faces or solids.
    To build faces  : shapes are wires, elements are edges.
    To build solids : shapes are shells, elements are faces.
    The ShapeSet stores a list of shapes, a list of elements
    to start reconstructions, and a map to search neighbours.
    The map stores the connection between elements through
    subshapes of type <SubShapeType> given in constructor.
    <SubShapeType> is:
    - TopAbs_VERTEX to connect edges
    - TopAbs_EDGE to connect faces

    Signature needed by the BlockBuilder:
    InitStartElements(me : in out)
    MoreStartElements(me) returns Boolean;
    NextStartElement(me : in out);
    StartElement(me) returns Shape; ---C++: return const &
    InitNeighbours(me : in out; S : Shape);
    MoreNeighbours(me) returns Boolean;
    NextNeighbour(me : in out);
    Neighbour(me) returns Shape; ---C++: return const &
    """

    def __init__(self, SubShapeType: nanoocp.TopAbs.TopAbs_ShapeEnum, checkshape: bool = True) -> None:
        """
        Creates a ShapeSet in order to build shapes connected
        by <SubShapeType> shapes.
        <checkshape>:check (or not) the shapes, startelements, elements added.
        """

    def AddShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Adds <S> to the list of shapes. (wires or shells)."""

    def AddStartElement(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        (S is a face or edge)
        Add S to the list of starting shapes used for reconstructions.
        apply AddElement(S).
        """

    def AddElement(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        for each subshape SE of S of type mySubShapeType
        - Add subshapes of S to the map of subshapes (mySubShapeMap)
        - Add S to the list of shape incident to subshapes of S.
        """

    def StartElements(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """return a reference on myStartShapes"""

    def InitShapes(self) -> None: ...

    def MoreShapes(self) -> bool: ...

    def NextShape(self) -> None: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def InitStartElements(self) -> None: ...

    def MoreStartElements(self) -> bool: ...

    def NextStartElement(self) -> None: ...

    def StartElement(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def InitNeighbours(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def MoreNeighbours(self) -> bool: ...

    def NextNeighbour(self) -> None: ...

    def Neighbour(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def ChangeStartShapes(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def FindNeighbours(self) -> None:
        """
        Build the list of neighbour shapes of myCurrentShape
        (neighbour shapes and myCurrentShapes are of type t)
        Initialize myIncidentShapesIter on neighbour shapes.
        """

    def MakeNeighboursList(self, E: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def MaxNumberSubShape(self, Shape: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    @overload
    def CheckShape(self, checkshape: bool) -> None: ...

    @overload
    def CheckShape(self) -> bool: ...

    @overload
    def CheckShape(self, S: nanoocp.TopoDS.TopoDS_Shape, checkgeom: bool = False) -> bool: ...

    def DumpName(self, str: nanoocp.TCollection.TCollection_AsciiString) -> object: ...

    def DumpCheck(self, str: nanoocp.TCollection.TCollection_AsciiString, S: nanoocp.TopoDS.TopoDS_Shape, chk: bool) -> object: ...

    def DumpSS(self) -> None: ...

    def DumpBB(self) -> None: ...

    @overload
    def DEBName(self, N: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    @overload
    def DEBName(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def DEBNumber(self, I: int) -> None: ...

    @overload
    def DEBNumber(self) -> int: ...

    @overload
    def SName(self, S: nanoocp.TopoDS.TopoDS_Shape, sb: nanoocp.TCollection.TCollection_AsciiString = ..., sa: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def SName(self, S: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], sb: nanoocp.TCollection.TCollection_AsciiString = ..., sa: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def SNameori(self, S: nanoocp.TopoDS.TopoDS_Shape, sb: nanoocp.TCollection.TCollection_AsciiString = ..., sa: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def SNameori(self, S: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], sb: nanoocp.TCollection.TCollection_AsciiString = ..., sa: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString: ...

class TopOpeBRepBuild_WireEdgeSet(TopOpeBRepBuild_ShapeSet):
    """
    a bound is a wire, a boundelement is an edge.
    The ShapeSet stores :
    - a list of wire (bounds),
    - a list of edge (boundelements) to start reconstructions,
    - a map of vertex giving the list of edge incident to a vertex.
    """

    def __init__(self, F: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Creates a WireEdgeSet to build edges connected by vertices
        on face F. Edges of the WireEdgeSet must have a representation
        on surface of face F.
        """

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """value of field myFace"""

    def AddShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def AddStartElement(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def AddElement(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def InitNeighbours(self, E: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def FindNeighbours(self) -> None:
        """
        Build the list of neighbour edges of edge myCurrentShape
        Initialize iterator of neighbour edges to edge myCurrentShape
        """

    def MakeNeighboursList(self, E: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    @staticmethod
    def IsUVISO(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, bool]: ...

    def DumpSS(self) -> None: ...

    @overload
    def SName(self, S: nanoocp.TopoDS.TopoDS_Shape, sb: nanoocp.TCollection.TCollection_AsciiString = ..., sa: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def SName(self, S: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], sb: nanoocp.TCollection.TCollection_AsciiString = ..., sa: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def SNameori(self, S: nanoocp.TopoDS.TopoDS_Shape, sb: nanoocp.TCollection.TCollection_AsciiString = ..., sa: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def SNameori(self, S: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], sb: nanoocp.TCollection.TCollection_AsciiString = ..., sa: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString: ...

class TopOpeBRepBuild_ShellFaceSet(TopOpeBRepBuild_ShapeSet):
    """
    a bound is a shell, a boundelement is a face.
    The ShapeSet stores :
    - a list of shell (bounds),
    - a list of face (boundelements) to start reconstructions,
    - a map of edge giving the list of face incident to an edge.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Creates a ShellFaceSet to build blocks of faces
        connected by edges.
        """

    def Solid(self) -> nanoocp.TopoDS.TopoDS_Solid: ...

    def AddShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def AddStartElement(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def AddElement(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def DumpSS(self) -> None: ...

    @overload
    def SName(self, S: nanoocp.TopoDS.TopoDS_Shape, sb: nanoocp.TCollection.TCollection_AsciiString = ..., sa: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def SName(self, S: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], sb: nanoocp.TCollection.TCollection_AsciiString = ..., sa: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def SNameori(self, S: nanoocp.TopoDS.TopoDS_Shape, sb: nanoocp.TCollection.TCollection_AsciiString = ..., sa: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def SNameori(self, S: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], sb: nanoocp.TCollection.TCollection_AsciiString = ..., sa: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString: ...

class TopOpeBRepBuild_GTopo:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, II: bool, IN: bool, IO: bool, NI: bool, NN: bool, NO: bool, OI: bool, ON: bool, OO: bool, t1: nanoocp.TopAbs.TopAbs_ShapeEnum, t2: nanoocp.TopAbs.TopAbs_ShapeEnum, C1: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Config, C2: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Config) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_GTopo) -> None: ...

    def Reset(self) -> None: ...

    def Set(self, II: bool, IN: bool, IO: bool, NI: bool, NN: bool, NO: bool, OI: bool, ON: bool, OO: bool) -> None: ...

    def Type(self) -> tuple[nanoocp.TopAbs.TopAbs_ShapeEnum, nanoocp.TopAbs.TopAbs_ShapeEnum]: ...

    def ChangeType(self, t1: nanoocp.TopAbs.TopAbs_ShapeEnum, t2: nanoocp.TopAbs.TopAbs_ShapeEnum) -> None: ...

    def Config1(self) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Config: ...

    def Config2(self) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Config: ...

    def ChangeConfig(self, C1: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Config, C2: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Config) -> None: ...

    @overload
    def Value(self, s1: nanoocp.TopAbs.TopAbs_State, s2: nanoocp.TopAbs.TopAbs_State) -> bool: ...

    @overload
    def Value(self, I1: int, I2: int) -> bool: ...

    @overload
    def Value(self, II: int) -> bool: ...

    @overload
    def ChangeValue(self, i1: int, i2: int, b: bool) -> None: ...

    @overload
    def ChangeValue(self, s1: nanoocp.TopAbs.TopAbs_State, s2: nanoocp.TopAbs.TopAbs_State, b: bool) -> None: ...

    def GIndex(self, S: nanoocp.TopAbs.TopAbs_State) -> int: ...

    def GState(self, I: int) -> nanoocp.TopAbs.TopAbs_State: ...

    def Index(self, II: int) -> tuple[int, int]: ...

    def DumpVal(self, s1: nanoocp.TopAbs.TopAbs_State, s2: nanoocp.TopAbs.TopAbs_State) -> object: ...

    def DumpType(self) -> object: ...

    @staticmethod
    def DumpSSB(s1: nanoocp.TopAbs.TopAbs_State, s2: nanoocp.TopAbs.TopAbs_State, b: bool) -> object: ...

    def Dump(self) -> object: ...

    def StatesON(self) -> tuple[nanoocp.TopAbs.TopAbs_State, nanoocp.TopAbs.TopAbs_State]: ...

    def IsToReverse1(self) -> bool: ...

    def IsToReverse2(self) -> bool: ...

    def SetReverse(self, rev: bool) -> None: ...

    def Reverse(self) -> bool: ...

    def CopyPermuted(self) -> TopOpeBRepBuild_GTopo: ...

class TopOpeBRepBuild_PaveClassifier(TopOpeBRepBuild_LoopClassifier):
    """
    This class compares vertices on an edge.

    A vertex V1 is inside a vertex V2 if V1 is on the
    part of the curve defined by V2.

    If V2 is FORWARD V1 must be after V2 on the curve.
    If V2 is REVERSED V1 must be before V2 on the curve.
    If V2 is INTERNAL V1 is always inside.
    If V2 is EXTERNAL V1 is never inside.
    """

    @overload
    def __init__(self, E: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Create a Pave classifier to compare vertices on edge <E>."""

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_PaveClassifier) -> None: ...

    def Compare(self, L1: TopOpeBRepBuild_Loop | None, L2: TopOpeBRepBuild_Loop | None) -> nanoocp.TopAbs.TopAbs_State:
        """Returns state of vertex <L1> compared with <L2>."""

    def SetFirstParameter(self, P: float) -> None: ...

    def ClosedVertices(self, B: bool) -> None: ...

    @staticmethod
    def AdjustCase(p1: float, o: nanoocp.TopAbs.TopAbs_Orientation, first: float, period: float, tol: float) -> tuple[float, int]: ...

class TopOpeBRepBuild_Pave(TopOpeBRepBuild_Loop):
    @overload
    def __init__(self, V: nanoocp.TopoDS.TopoDS_Shape, P: float, bound: bool) -> None:
        """
        V = vertex, P = parameter of vertex <V>
        bound = True if <V> is an old vertex
        bound = False if <V> is a new vertex
        """

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_Pave) -> None: ...

    @overload
    def HasSameDomain(self, b: bool) -> None: ...

    @overload
    def HasSameDomain(self) -> bool: ...

    @overload
    def SameDomain(self, VSD: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def SameDomain(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def ChangeVertex(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def Parameter(self) -> float: ...

    @overload
    def Parameter(self, Par: float) -> None: ...

    def InterferenceType(self) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_Kind: ...

    def SetInterferenceType(self, theValue: nanoocp.TopOpeBRepDS.TopOpeBRepDS_Kind) -> None:
        """
        Python addition: sets the value InterferenceType() returns by reference in C++.
        """

    def IsShape(self) -> bool: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Dump(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepBuild_LoopSet:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_LoopSet) -> None: ...

    def ChangeListOfLoop(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Loop]: ...

    def InitLoop(self) -> None: ...

    def MoreLoop(self) -> bool: ...

    def NextLoop(self) -> None: ...

    def Loop(self) -> TopOpeBRepBuild_Loop: ...

class TopOpeBRepBuild_PaveSet(TopOpeBRepBuild_LoopSet):
    """
    class providing an exploration of a set of vertices to build edges.
    It is similar to LoopSet from TopOpeBRepBuild where Loop is Pave.
    """

    @overload
    def __init__(self, E: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Create a Pave set on edge <E>. It contains <E> vertices."""

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_PaveSet) -> None: ...

    def RemovePV(self, B: bool) -> None: ...

    def Append(self, PV: TopOpeBRepBuild_Pave | None) -> None:
        """Add <PV> in the Pave set."""

    def InitLoop(self) -> None: ...

    def MoreLoop(self) -> bool: ...

    def NextLoop(self) -> None: ...

    def Loop(self) -> TopOpeBRepBuild_Loop: ...

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def HasEqualParameters(self) -> bool: ...

    def EqualParameters(self) -> float: ...

    def ClosedVertices(self) -> bool: ...

    @staticmethod
    def SortPave(Lin: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Pave], Lout: nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Pave]) -> None: ...

class TopOpeBRepBuild_SolidAreaBuilder(TopOpeBRepBuild_Area3dBuilder):
    """
    The SolidAreaBuilder algorithm is used to construct Solids from a LoopSet,
    where the Loop is the composite topological object of the boundary,
    here wire or block of edges.
    The LoopSet gives an iteration on Loops.
    For each Loop it indicates if it is on the boundary (wire) or if it
    results from an interference (block of edges).
    The result of the SolidAreaBuilder is an iteration on areas.
    An area is described by a set of Loops.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, LS: TopOpeBRepBuild_LoopSet, LC: TopOpeBRepBuild_LoopClassifier, ForceClass: bool = False) -> None:
        """
        Creates a SolidAreaBuilder to build Solids on
        the (shells,blocks of face) of <LS>, using the classifier <LC>.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_SolidAreaBuilder) -> None: ...

    def InitSolidAreaBuilder(self, LS: TopOpeBRepBuild_LoopSet, LC: TopOpeBRepBuild_LoopClassifier, ForceClass: bool = False) -> None: ...

class TopOpeBRepBuild_SolidBuilder:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, FS: TopOpeBRepBuild_ShellFaceSet, ForceClass: bool = False) -> None:
        """
        Create a SolidBuilder to build the areas on
        the shapes (shells, blocks of faces) described by <LS>.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_SolidBuilder) -> None: ...

    def InitSolidBuilder(self, FS: TopOpeBRepBuild_ShellFaceSet, ForceClass: bool) -> None: ...

    def InitSolid(self) -> int: ...

    def MoreSolid(self) -> bool: ...

    def NextSolid(self) -> None: ...

    def InitShell(self) -> int: ...

    def MoreShell(self) -> bool: ...

    def NextShell(self) -> None: ...

    def IsOldShell(self) -> bool: ...

    def OldShell(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns current shell
        This shell may be :
        * an old shell OldShell(), which has not been reconstructed;
        * a new shell made of faces described by ...NewFace() methods.
        """

    def InitFace(self) -> int: ...

    def MoreFace(self) -> bool: ...

    def NextFace(self) -> None: ...

    def Face(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns current new face of current new shell."""

class TopOpeBRepBuild_FaceAreaBuilder(TopOpeBRepBuild_Area2dBuilder):
    """
    The FaceAreaBuilder algorithm is used to construct Faces from a LoopSet,
    where the Loop is the composite topological object of the boundary,
    here wire or block of edges.
    The LoopSet gives an iteration on Loops.
    For each Loop it indicates if it is on the boundary (wire) or if it
    results from an interference (block of edges).
    The result of the FaceAreaBuilder is an iteration on areas.
    An area is described by a set of Loops.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, LS: TopOpeBRepBuild_LoopSet, LC: TopOpeBRepBuild_LoopClassifier, ForceClass: bool = False) -> None:
        """
        Creates a FaceAreaBuilder to build faces on
        the (wires,blocks of edge) of <LS>, using the classifier <LC>.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_FaceAreaBuilder) -> None: ...

    def InitFaceAreaBuilder(self, LS: TopOpeBRepBuild_LoopSet, LC: TopOpeBRepBuild_LoopClassifier, ForceClass: bool = False) -> None: ...

class TopOpeBRepBuild_FaceBuilder:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, ES: TopOpeBRepBuild_WireEdgeSet, F: nanoocp.TopoDS.TopoDS_Shape, ForceClass: bool = False) -> None:
        """
        Create a FaceBuilder to build the faces on
        the shapes (wires, blocks of edge) described by <LS>.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_FaceBuilder) -> None: ...

    def InitFaceBuilder(self, ES: TopOpeBRepBuild_WireEdgeSet, F: nanoocp.TopoDS.TopoDS_Shape, ForceClass: bool) -> None: ...

    def DetectUnclosedWire(self, mapVVsameG: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], mapVon1Edge: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        Removes are non 3d-closed wires.
        Fills up maps <mapVVsameG> and <mapVon1Edge>, in order to
        correct 3d-closed but unclosed (topologic connexity) wires.
        modifies myBlockBuilder
        """

    def CorrectGclosedWire(self, mapVVref: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], mapVon1Edge: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        Using the given maps, change the topology of the 3d-closed
        wires, in order to get closed wires.
        """

    def DetectPseudoInternalEdge(self, mapE: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        Removes edges appearing twice (FORWARD,REVERSED) with a bounding
        vertex not connected to any other edge.
        mapE contains edges found.
        modifies myBlockBuilder.
        """

    def Face(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """return myFace"""

    def InitFace(self) -> int: ...

    def MoreFace(self) -> bool: ...

    def NextFace(self) -> None: ...

    def InitWire(self) -> int: ...

    def MoreWire(self) -> bool: ...

    def NextWire(self) -> None: ...

    def IsOldWire(self) -> bool: ...

    def OldWire(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns current wire
        This wire may be :
        * an old wire OldWire(), which has not been reconstructed;
        * a new wire made of edges described by ...NewEdge() methods.
        """

    def FindNextValidElement(self) -> None:
        """Iterates on myBlockIterator until finding a valid element"""

    def InitEdge(self) -> int: ...

    def MoreEdge(self) -> bool: ...

    def NextEdge(self) -> None: ...

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns current new edge of current new wire."""

    def EdgeConnexity(self, E: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    def AddEdgeWire(self, E: nanoocp.TopoDS.TopoDS_Shape, W: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

class TopOpeBRepBuild_EdgeBuilder(TopOpeBRepBuild_Area1dBuilder):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, LS: TopOpeBRepBuild_PaveSet, LC: TopOpeBRepBuild_PaveClassifier, ForceClass: bool = False) -> None:
        """
        Creates a EdgeBuilder to find the areas of
        the shapes described by <LS> using the classifier <LC>.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_EdgeBuilder) -> None: ...

    def InitEdgeBuilder(self, LS: TopOpeBRepBuild_LoopSet, LC: TopOpeBRepBuild_LoopClassifier, ForceClass: bool = False) -> None: ...

    def InitEdge(self) -> None: ...

    def MoreEdge(self) -> bool: ...

    def NextEdge(self) -> None: ...

    def InitVertex(self) -> None: ...

    def MoreVertex(self) -> bool: ...

    def NextVertex(self) -> None: ...

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Parameter(self) -> float: ...

class TopOpeBRepBuild_ShapeListOfShape:
    """represent shape + a list of shape"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_ShapeListOfShape) -> None: ...

    def List(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def ChangeList(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def ChangeShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

class TopOpeBRepBuild_HBuilder(nanoocp.Standard.Standard_Transient):
    """
    The HBuilder algorithm constructs topological
    objects from an existing topology and new
    geometries attached to the topology. It is used to
    construct the result of a topological operation;
    the existing topologies are the parts involved in
    the topological operation and the new geometries
    are the intersection lines and points.
    """

    @overload
    def __init__(self, BT: nanoocp.TopOpeBRepDS.TopOpeBRepDS_BuildTool) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_HBuilder) -> None: ...

    def BuildTool(self) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_BuildTool: ...

    @overload
    def Perform(self, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None) -> None:
        """
        Stores the data structure <HDS>,
        Create shapes from the new geometries described in <HDS>.
        """

    @overload
    def Perform(self, HDS: nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure | None, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Same as previous + evaluates if an operation performed on shapes S1,S2
        is a particular case.
        """

    def Clear(self) -> None:
        """
        Removes all split and merge already performed.
        Does NOT clear the handled DS.
        """

    def DataStructure(self) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_HDataStructure:
        """returns the DS handled by this builder"""

    def ChangeBuildTool(self) -> nanoocp.TopOpeBRepDS.TopOpeBRepDS_BuildTool: ...

    def MergeShapes(self, S1: nanoocp.TopoDS.TopoDS_Shape, TB1: nanoocp.TopAbs.TopAbs_State, S2: nanoocp.TopoDS.TopoDS_Shape, TB2: nanoocp.TopAbs.TopAbs_State) -> None:
        """
        Merges the two shapes <S1> and <S2> keeping the
        parts of states <TB1>,<TB2> in <S1>,<S2>.
        """

    def MergeSolids(self, S1: nanoocp.TopoDS.TopoDS_Shape, TB1: nanoocp.TopAbs.TopAbs_State, S2: nanoocp.TopoDS.TopoDS_Shape, TB2: nanoocp.TopAbs.TopAbs_State) -> None:
        """
        Merges the two solids <S1> and <S2> keeping the
        parts in each solid of states <TB1> and <TB2>.
        """

    def MergeSolid(self, S: nanoocp.TopoDS.TopoDS_Shape, TB: nanoocp.TopAbs.TopAbs_State) -> None:
        """
        Merges the solid <S> keeping the
        parts of state <TB>.
        """

    def IsSplit(self, S: nanoocp.TopoDS.TopoDS_Shape, ToBuild: nanoocp.TopAbs.TopAbs_State) -> bool:
        """Returns True if the shape <S> has been split."""

    def Splits(self, S: nanoocp.TopoDS.TopoDS_Shape, ToBuild: nanoocp.TopAbs.TopAbs_State) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the split parts <ToBuild> of shape <S>."""

    def IsMerged(self, S: nanoocp.TopoDS.TopoDS_Shape, ToBuild: nanoocp.TopAbs.TopAbs_State) -> bool:
        """Returns True if the shape <S> has been merged."""

    def Merged(self, S: nanoocp.TopoDS.TopoDS_Shape, ToBuild: nanoocp.TopAbs.TopAbs_State) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the merged parts <ToBuild> of shape <S>."""

    def NewVertex(self, I: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the vertex created on point <I>."""

    def NewEdges(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the edges created on curve <I>."""

    def ChangeNewEdges(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the edges created on curve <I>."""

    def NewFaces(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the faces created on surface <I>."""

    def Section(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def InitExtendedSectionDS(self, k: int = 3) -> None: ...

    def InitSection(self, k: int = 3) -> None: ...

    def MoreSection(self) -> bool: ...

    def NextSection(self) -> None: ...

    def CurrentSection(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def GetDSEdgeFromSectEdge(self, E: nanoocp.TopoDS.TopoDS_Shape, rank: int) -> int: ...

    def GetDSFaceFromDSEdge(self, indexEdg: int, rank: int) -> nanoocp.NCollection.NCollection_List[int]: ...

    def GetDSCurveFromSectEdge(self, SectEdge: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    def GetDSFaceFromDSCurve(self, indexCur: int, rank: int) -> int: ...

    def GetDSPointFromNewVertex(self, NewVert: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    def EdgeCurveAncestors(self, E: nanoocp.TopoDS.TopoDS_Shape, F1: nanoocp.TopoDS.TopoDS_Shape, F2: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, int]:
        """
        search for the couple of face F1,F2
        (from arguments of supra Perform(S1,S2,HDS)) method which
        intersection gives section edge E built on an intersection curve.
        returns True if F1,F2 have been valued.
        returns False if E is not a section edge built
        on intersection curve IC.
        """

    def EdgeSectionAncestors(self, E: nanoocp.TopoDS.TopoDS_Shape, LF1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LF2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LE1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LE2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        search for the couple of face F1,F2
        (from arguments of supra Perform(S1,S2,HDS)) method which
        intersection gives section edge E built on at least one edge.
        returns True if F1,F2 have been valued.
        returns False if E is not a section edge built
        on at least one edge of S1 and/or S2.
        LE1,LE2 are edges of S1,S2 which common part is edge E.
        LE1 or LE2 may be empty() but not both.
        """

    def IsKPart(self) -> int:
        """Returns 0 is standard operation, != 0 if particular case"""

    def MergeKPart(self, TB1: nanoocp.TopAbs.TopAbs_State, TB2: nanoocp.TopAbs.TopAbs_State) -> None: ...

    def ChangeBuilder(self) -> TopOpeBRepBuild_Builder: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopOpeBRepBuild_FuseFace:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, LIF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LRF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], CXM: int) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_FuseFace) -> None: ...

    def Init(self, LIF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LRF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], CXM: int) -> None: ...

    def PerformFace(self) -> None: ...

    def PerformEdge(self) -> None: ...

    def ClearEdge(self) -> None: ...

    def ClearVertex(self) -> None: ...

    def IsDone(self) -> bool: ...

    def IsModified(self) -> bool: ...

    def LFuseFace(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def LInternEdge(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def LExternEdge(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def LModifEdge(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def LInternVertex(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def LExternVertex(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def LModifVertex(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

class TopOpeBRepBuild_GIter:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, G: TopOpeBRepBuild_GTopo) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_GIter) -> None: ...

    @overload
    def Init(self) -> None: ...

    @overload
    def Init(self, G: TopOpeBRepBuild_GTopo) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Current(self) -> tuple[nanoocp.TopAbs.TopAbs_State, nanoocp.TopAbs.TopAbs_State]: ...

    def Dump(self) -> object: ...

class TopOpeBRepBuild_GTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_GTool) -> None: ...

    @staticmethod
    def GFusUnsh(s1: nanoocp.TopAbs.TopAbs_ShapeEnum, s2: nanoocp.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: ...

    @staticmethod
    def GFusSame(s1: nanoocp.TopAbs.TopAbs_ShapeEnum, s2: nanoocp.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: ...

    @staticmethod
    def GFusDiff(s1: nanoocp.TopAbs.TopAbs_ShapeEnum, s2: nanoocp.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: ...

    @staticmethod
    def GCutUnsh(s1: nanoocp.TopAbs.TopAbs_ShapeEnum, s2: nanoocp.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: ...

    @staticmethod
    def GCutSame(s1: nanoocp.TopAbs.TopAbs_ShapeEnum, s2: nanoocp.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: ...

    @staticmethod
    def GCutDiff(s1: nanoocp.TopAbs.TopAbs_ShapeEnum, s2: nanoocp.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: ...

    @staticmethod
    def GComUnsh(s1: nanoocp.TopAbs.TopAbs_ShapeEnum, s2: nanoocp.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: ...

    @staticmethod
    def GComSame(s1: nanoocp.TopAbs.TopAbs_ShapeEnum, s2: nanoocp.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: ...

    @staticmethod
    def GComDiff(s1: nanoocp.TopAbs.TopAbs_ShapeEnum, s2: nanoocp.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepBuild_GTopo: ...

    @staticmethod
    def Dump() -> object: ...

class TopOpeBRepBuild_ShellFaceClassifier(TopOpeBRepBuild_CompositeClassifier):
    """
    Classify faces and shells.
    shapes are Shells, Elements are Faces.
    """

    @overload
    def __init__(self, BB: TopOpeBRepBuild_BlockBuilder) -> None:
        """
        Creates a classifier in 3D space, to compare :
        a face with a set of faces
        a shell with a set of faces
        a shell with a shell
        """

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_ShellFaceClassifier) -> None: ...

    def Clear(self) -> None: ...

    def CompareShapes(self, B1: nanoocp.TopoDS.TopoDS_Shape, B2: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_State:
        """classify shell <B1> with shell <B2>"""

    def CompareElementToShape(self, F: nanoocp.TopoDS.TopoDS_Shape, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_State:
        """classify face <F> with shell <S>"""

    def ResetShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        prepare classification involving shell <S>
        calls ResetElement on first face of <S>
        """

    def ResetElement(self, F: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        prepare classification involving face <F>
        define 3D point (later used in Compare()) on first vertex of face <F>.
        """

    def CompareElement(self, F: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Add the face <F> in the set of faces used in 3D point
        classification. Returns FALSE if the face <F> has been already
        added to the set of faces, otherwise returns TRUE.
        """

    def State(self) -> nanoocp.TopAbs.TopAbs_State:
        """
        Returns state of classification of 3D point, defined by
        ResetElement, with the current set of faces, defined by Compare.
        """

class TopOpeBRepBuild_ShellToSolid:
    """This class builds solids from a set of shells SSh and a solid F."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_ShellToSolid) -> None: ...

    def Init(self) -> None: ...

    def AddShell(self, Sh: nanoocp.TopoDS.TopoDS_Shell) -> None: ...

    def MakeSolids(self, So: nanoocp.TopoDS.TopoDS_Solid, LSo: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

class TopOpeBRepBuild_Tools:
    """Auxiliary methods used in TopOpeBRepBuild_Builder1 class"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_Tools) -> None: ...

    @staticmethod
    def FindState(aVertex: nanoocp.TopoDS.TopoDS_Shape, aState: nanoocp.TopAbs.TopAbs_State, aShapeEnum: nanoocp.TopAbs.TopAbs_ShapeEnum, aMapVertexEdges: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], aMapProcessedVertices: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], aMapVs: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopAbs.TopAbs_State, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    @staticmethod
    def PropagateState(aSplEdgesState: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopAbs.TopAbs_State, nanoocp.TopTools.TopTools_ShapeMapHasher], anEdgesToRestMap: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], aShapeEnum1: nanoocp.TopAbs.TopAbs_ShapeEnum, aShapeEnum2: nanoocp.TopAbs.TopAbs_ShapeEnum, aShapeClassifier: nanoocp.TopOpeBRepTool.TopOpeBRepTool_ShapeClassifier, aMapOfShapeWithState: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ShapeWithState, nanoocp.TopTools.TopTools_ShapeMapHasher], anUnkStateShapes: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    @staticmethod
    def FindStateThroughVertex(aShape: nanoocp.TopoDS.TopoDS_Shape, aShapeClassifier: nanoocp.TopOpeBRepTool.TopOpeBRepTool_ShapeClassifier, aMapOfShapeWithState: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ShapeWithState, nanoocp.TopTools.TopTools_ShapeMapHasher], anAvoidSubshMap: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> nanoocp.TopAbs.TopAbs_State: ...

    @staticmethod
    def PropagateStateForWires(aFacesToRestMap: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], aMapOfShapeWithState: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ShapeWithState, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    @staticmethod
    def SpreadStateToChild(aShape: nanoocp.TopoDS.TopoDS_Shape, aState: nanoocp.TopAbs.TopAbs_State, aMapOfShapeWithState: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepDS.TopOpeBRepDS_ShapeWithState, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    @staticmethod
    def FindState1(anEdge: nanoocp.TopoDS.TopoDS_Shape, aState: nanoocp.TopAbs.TopAbs_State, aMapEdgesFaces: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], aMapProcessedVertices: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], aMapVs: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopAbs.TopAbs_State, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    @staticmethod
    def FindState2(anEdge: nanoocp.TopoDS.TopoDS_Shape, aState: nanoocp.TopAbs.TopAbs_State, aMapEdgesFaces: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], aMapProcessedEdges: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], aMapVs: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopAbs.TopAbs_State, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    @staticmethod
    def GetAdjacentFace(aFaceObj: nanoocp.TopoDS.TopoDS_Shape, anEObj: nanoocp.TopoDS.TopoDS_Shape, anEdgeFaceMap: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], anAdjFaceObj: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    @staticmethod
    def GetNormalToFaceOnEdge(aFObj: nanoocp.TopoDS.TopoDS_Face, anEdgeObj: nanoocp.TopoDS.TopoDS_Edge, aDirNormal: nanoocp.gp.gp_Vec) -> None: ...

    @staticmethod
    def GetNormalInNearestPoint(aFace: nanoocp.TopoDS.TopoDS_Face, anEdge: nanoocp.TopoDS.TopoDS_Edge, aNormal: nanoocp.gp.gp_Vec) -> None:
        """
        This function used to compute normal in point which is located
        near the point with param UV (used for computation of normals where the normal
        in the point UV equal to zero).
        """

    @staticmethod
    def GetTangentToEdgeEdge(aFObj: nanoocp.TopoDS.TopoDS_Face, anEdgeObj: nanoocp.TopoDS.TopoDS_Edge, aOriEObj: nanoocp.TopoDS.TopoDS_Edge, aTangent: nanoocp.gp.gp_Vec) -> bool: ...

    @staticmethod
    def GetTangentToEdge(anEdgeObj: nanoocp.TopoDS.TopoDS_Edge, aTangent: nanoocp.gp.gp_Vec) -> bool: ...

    @staticmethod
    def UpdatePCurves(aWire: nanoocp.TopoDS.TopoDS_Wire, fromFace: nanoocp.TopoDS.TopoDS_Face, toFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Recompute PCurves of the all edges from the wire on the <toFace>"""

    @staticmethod
    def UpdateEdgeOnPeriodicalFace(aEdgeToUpdate: nanoocp.TopoDS.TopoDS_Edge, OldFace: nanoocp.TopoDS.TopoDS_Face, NewFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Recompute PCurves of the closing (SIM, with 2 PCurves) edge on the NewFace
        """

    @staticmethod
    def UpdateEdgeOnFace(aEdgeToUpdate: nanoocp.TopoDS.TopoDS_Edge, OldFace: nanoocp.TopoDS.TopoDS_Face, NewFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Recompute PCurve of the edge on the NewFace"""

    @staticmethod
    def IsDegEdgesTheSame(anE1: nanoocp.TopoDS.TopoDS_Shape, anE2: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    @staticmethod
    def NormalizeFace(oldFace: nanoocp.TopoDS.TopoDS_Shape, corrFace: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        test if <oldFace> does not contain INTERNAL or EXTERNAL edges
        and remove such edges in case of its presence. The result is stored in <corrFace>
        """

    @staticmethod
    def CorrectFace2d(oldFace: nanoocp.TopoDS.TopoDS_Shape, corrFace: nanoocp.TopoDS.TopoDS_Shape, aSourceShapes: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape], aMapOfCorrect2dEdges: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        test if UV representation of <oldFace> is good (i.e. face is closed in 2d).
        if face is not closed, this method will try to close such face and will
        return corrected edges in the <aMapOfCorrect2dEdges>. Parameter <aSourceShapes>
        used to fix the edge (or wires) which should be correct (Corrector used it as a
        start shapes). NOTE: Parameter corrFace doesn't mean anything. If you want to use
        this method, rebuild resulting face after by yourself using corrected edges.
        """

    @staticmethod
    def CorrectTolerances(aS: nanoocp.TopoDS.TopoDS_Shape, aTolMax: float = 0.0001) -> None: ...

    @staticmethod
    def CorrectCurveOnSurface(aS: nanoocp.TopoDS.TopoDS_Shape, aTolMax: float = 0.0001) -> None: ...

    @staticmethod
    def CorrectPointOnCurve(aS: nanoocp.TopoDS.TopoDS_Shape, aTolMax: float = 0.0001) -> None: ...

    @staticmethod
    def CheckFaceClosed2d(theFace: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """Checks if <theFace> has the properly closed in 2D boundary(ies)"""

class TopOpeBRepBuild_VertexInfo:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_VertexInfo) -> None: ...

    def SetVertex(self, aV: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def SetSmart(self, aFlag: bool) -> None: ...

    def Smart(self) -> bool: ...

    def NbCases(self) -> int: ...

    def FoundOut(self) -> int: ...

    def AddIn(self, anE: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    def AddOut(self, anE: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    def SetCurrentIn(self, anE: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    def EdgesIn(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape]: ...

    def EdgesOut(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape]: ...

    def ChangeEdgesOut(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape]: ...

    def Dump(self) -> None: ...

    def CurrentOut(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def AppendPassed(self, anE: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    def RemovePassed(self) -> None: ...

    def ListPassed(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def Prepare(self, aL: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

class TopOpeBRepBuild_Tools2d:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_Tools2d) -> None: ...

    @staticmethod
    def MakeMapOfShapeVertexInfo(aWire: nanoocp.TopoDS.TopoDS_Wire, aMap: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_VertexInfo, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    @staticmethod
    def DumpMapOfShapeVertexInfo(aMap: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_VertexInfo, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None: ...

    @staticmethod
    def Path(aWire: nanoocp.TopoDS.TopoDS_Wire, aResList: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

class TopOpeBRepBuild_WireEdgeClassifier(TopOpeBRepBuild_CompositeClassifier):
    """
    Classify edges and wires.
    shapes are Wires, Element are Edge.
    """

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Shape, BB: TopOpeBRepBuild_BlockBuilder) -> None:
        """
        Creates a classifier on edge <F>.
        Used to compare edges and wires on the edge <F>.
        """

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_WireEdgeClassifier) -> None: ...

    def Compare(self, L1: TopOpeBRepBuild_Loop | None, L2: TopOpeBRepBuild_Loop | None) -> nanoocp.TopAbs.TopAbs_State: ...

    def LoopToShape(self, L: TopOpeBRepBuild_Loop | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def CompareShapes(self, B1: nanoocp.TopoDS.TopoDS_Shape, B2: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_State:
        """classify wire <B1> with wire <B2>"""

    def CompareElementToShape(self, E: nanoocp.TopoDS.TopoDS_Shape, B: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_State:
        """classify edge <E> with wire <B>"""

    def ResetShape(self, B: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        prepare classification involving wire <B>
        calls ResetElement on first edge of <B>
        """

    def ResetElement(self, E: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        prepare classification involving edge <E>
        define 2D point (later used in Compare()) on first vertex of edge <E>.
        """

    def CompareElement(self, E: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Add the edge <E> in the set of edges used in 2D point
        classification.
        """

    def State(self) -> nanoocp.TopAbs.TopAbs_State:
        """
        Returns state of classification of 2D point, defined by
        ResetElement, with the current set of edges, defined by Compare.
        """

class TopOpeBRepBuild_WireToFace:
    """
    This class builds faces from a set of wires SW and a face F.
    The face must have and underlying surface, say S.
    All of the edges of all of the wires must have a 2d representation
    on surface S (except if S is planar)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopOpeBRepBuild_WireToFace) -> None: ...

    def Init(self) -> None: ...

    def AddWire(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None: ...

    def MakeFaces(self, F: nanoocp.TopoDS.TopoDS_Face, LF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.TopOpeBRepBuild
import nanoocp.TopTools
TopOpeBRepBuild_IndexedDataMapOfShapeVertexInfo = nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_VertexInfo, nanoocp.TopTools.TopTools_ShapeMapHasher]
TopOpeBRepBuild_ListOfLoop = nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Loop]
TopOpeBRepBuild_ListOfPave = nanoocp.NCollection.NCollection_List[nanoocp.TopOpeBRepBuild.TopOpeBRepBuild_Pave]
