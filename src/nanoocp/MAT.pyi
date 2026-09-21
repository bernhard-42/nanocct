"""OCCT package MAT (toolkit TKTopAlgo)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard


class MAT_Side(enum.IntEnum):
    """Definition on the Left and the Right on the Fig."""

    MAT_Left = 0

    MAT_Right = 1

MAT_Left: MAT_Side = MAT_Side.MAT_Left

MAT_Right: MAT_Side = MAT_Side.MAT_Right

class MAT_Arc(nanoocp.Standard.Standard_Transient):
    """An Arc is associated to each Bisecting of the mat."""

    @overload
    def __init__(self, ArcIndex: int, GeomIndex: int, FirstElement: MAT_BasicElt | None, SecondElement: MAT_BasicElt | None) -> None: ...

    @overload
    def __init__(self, theOther: MAT_Arc) -> None: ...

    def Index(self) -> int:
        """Returns the index of <me> in Graph.theArcs."""

    def GeomIndex(self) -> int:
        """
        Returns the index associated of the geometric
        representation of <me>.
        """

    def FirstElement(self) -> MAT_BasicElt:
        """Returns one of the BasicElt equidistant from <me>."""

    def SecondElement(self) -> MAT_BasicElt:
        """Returns the other BasicElt equidistant from <me>."""

    def FirstNode(self) -> MAT_Node:
        """Returns one Node extremity of <me>."""

    def SecondNode(self) -> MAT_Node:
        """Returns the other Node extremity of <me>."""

    def TheOtherNode(self, aNode: MAT_Node | None) -> MAT_Node:
        """
        An Arc has two Node, if <aNode> equals one
        Returns the other.

        if <aNode> is not oh <me>
        """

    def HasNeighbour(self, aNode: MAT_Node | None, aSide: MAT_Side) -> bool:
        """
        Returns True if there is an arc linked to
        the Node <aNode> located on the side <aSide> of <me>;
        if <aNode> is not on <me>
        """

    def Neighbour(self, aNode: MAT_Node | None, aSide: MAT_Side) -> MAT_Arc:
        """
        Returns the first arc linked to the Node <aNode>
        located on the side <aSide> of <me>;
        if HasNeighbour() returns FALSE.
        """

    def SetIndex(self, anInteger: int) -> None: ...

    def SetGeomIndex(self, anInteger: int) -> None: ...

    def SetFirstElement(self, aBasicElt: MAT_BasicElt | None) -> None: ...

    def SetSecondElement(self, aBasicElt: MAT_BasicElt | None) -> None: ...

    def SetFirstNode(self, aNode: MAT_Node | None) -> None: ...

    def SetSecondNode(self, aNode: MAT_Node | None) -> None: ...

    def SetFirstArc(self, aSide: MAT_Side, anArc: MAT_Arc | None) -> None: ...

    def SetSecondArc(self, aSide: MAT_Side, anArc: MAT_Arc | None) -> None: ...

    def SetNeighbour(self, aSide: MAT_Side, aNode: MAT_Node | None, anArc: MAT_Arc | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MAT_BasicElt(nanoocp.Standard.Standard_Transient):
    """
    A BasicELt is associated to each elementary
    constituent of the figure.
    """

    @overload
    def __init__(self, anInteger: int) -> None:
        """Constructor, <anInteger> is the <index> of <me>."""

    @overload
    def __init__(self, theOther: MAT_BasicElt) -> None: ...

    def StartArc(self) -> MAT_Arc:
        """
        Return <startArcLeft> or <startArcRight> corresponding
        to <aSide>.
        """

    def EndArc(self) -> MAT_Arc:
        """
        Return <endArcLeft> or <endArcRight> corresponding
        to <aSide>.
        """

    def Index(self) -> int:
        """Return the <index> of <me> in Graph.TheBasicElts."""

    def GeomIndex(self) -> int:
        """Return the <GeomIndex> of <me>."""

    def SetStartArc(self, anArc: MAT_Arc | None) -> None: ...

    def SetEndArc(self, anArc: MAT_Arc | None) -> None: ...

    def SetIndex(self, anInteger: int) -> None: ...

    def SetGeomIndex(self, anInteger: int) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MAT_Bisector(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MAT_Bisector) -> None: ...

    def AddBisector(self, abisector: MAT_Bisector | None) -> None: ...

    def List(self) -> MAT_ListOfBisector: ...

    def FirstBisector(self) -> MAT_Bisector: ...

    def LastBisector(self) -> MAT_Bisector: ...

    @overload
    def BisectorNumber(self, anumber: int) -> None: ...

    @overload
    def BisectorNumber(self) -> int: ...

    @overload
    def IndexNumber(self, anumber: int) -> None: ...

    @overload
    def IndexNumber(self) -> int: ...

    @overload
    def FirstEdge(self, anedge: MAT_Edge | None) -> None: ...

    @overload
    def FirstEdge(self) -> MAT_Edge: ...

    @overload
    def SecondEdge(self, anedge: MAT_Edge | None) -> None: ...

    @overload
    def SecondEdge(self) -> MAT_Edge: ...

    @overload
    def IssuePoint(self, apoint: int) -> None: ...

    @overload
    def IssuePoint(self) -> int: ...

    @overload
    def EndPoint(self, apoint: int) -> None: ...

    @overload
    def EndPoint(self) -> int: ...

    @overload
    def DistIssuePoint(self, areal: float) -> None: ...

    @overload
    def DistIssuePoint(self) -> float: ...

    @overload
    def FirstVector(self, avector: int) -> None: ...

    @overload
    def FirstVector(self) -> int: ...

    @overload
    def SecondVector(self, avector: int) -> None: ...

    @overload
    def SecondVector(self) -> int: ...

    @overload
    def Sense(self, asense: float) -> None: ...

    @overload
    def Sense(self) -> float: ...

    @overload
    def FirstParameter(self, aparameter: float) -> None: ...

    @overload
    def FirstParameter(self) -> float: ...

    @overload
    def SecondParameter(self, aparameter: float) -> None: ...

    @overload
    def SecondParameter(self) -> float: ...

    def Dump(self, ashift: int, alevel: int) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MAT_Edge(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MAT_Edge) -> None: ...

    @overload
    def EdgeNumber(self, anumber: int) -> None: ...

    @overload
    def EdgeNumber(self) -> int: ...

    @overload
    def FirstBisector(self, abisector: MAT_Bisector | None) -> None: ...

    @overload
    def FirstBisector(self) -> MAT_Bisector: ...

    @overload
    def SecondBisector(self, abisector: MAT_Bisector | None) -> None: ...

    @overload
    def SecondBisector(self) -> MAT_Bisector: ...

    @overload
    def Distance(self, adistance: float) -> None: ...

    @overload
    def Distance(self) -> float: ...

    @overload
    def IntersectionPoint(self, apoint: int) -> None: ...

    @overload
    def IntersectionPoint(self) -> int: ...

    def Dump(self, ashift: int, alevel: int) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MAT_Node(nanoocp.Standard.Standard_Transient):
    """Node of Graph."""

    @overload
    def __init__(self, GeomIndex: int, LinkedArc: MAT_Arc | None, Distance: float) -> None: ...

    @overload
    def __init__(self, theOther: MAT_Node) -> None: ...

    def GeomIndex(self) -> int:
        """
        Returns the index associated of the geometric
        representation of <me>.
        """

    def Index(self) -> int:
        """Returns the index associated of the node"""

    def LinkedArcs(self, S: nanoocp.NCollection.NCollection_Sequence[nanoocp.MAT.MAT_Arc]) -> None:
        """Returns in <S> the Arcs linked to <me>."""

    def NearElts(self, S: nanoocp.NCollection.NCollection_Sequence[nanoocp.MAT.MAT_BasicElt]) -> None:
        """
        Returns in <S> the BasicElts equidistant
        to <me>.
        """

    def Distance(self) -> float: ...

    def PendingNode(self) -> bool:
        """
        Returns True if <me> is a pending Node.
        (ie : the number of Arc Linked = 1)
        """

    def OnBasicElt(self) -> bool:
        """Returns True if <me> belongs to the figure."""

    def Infinite(self) -> bool:
        """Returns True if the distance of <me> is Infinite"""

    def SetIndex(self, anIndex: int) -> None:
        """Set the index associated of the node"""

    def SetLinkedArc(self, anArc: MAT_Arc | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MAT_Graph(nanoocp.Standard.Standard_Transient):
    """
    The Class Graph permits the exploration of the
    Bisector Locus.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: MAT_Graph) -> None: ...

    def Perform(self, SemiInfinite: bool, TheRoots: MAT_ListOfBisector | None, NbBasicElts: int, NbArcs: int) -> None:
        """
        Construct <me> from the result of the method
        <CreateMat> of the class <MAT> from <MAT>.

        <SemiInfinite> : if some bisector are infinites.
        <TheRoots>     : Set of the bisectors.
        <NbBasicElts>  : Number of Basic Elements.
        <NbArcs>       : Number of Arcs = Number of Bisectors.
        """

    def Arc(self, Index: int) -> MAT_Arc:
        """Return the Arc of index <Index> in <theArcs>."""

    def BasicElt(self, Index: int) -> MAT_BasicElt:
        """Return the BasicElt of index <Index> in <theBasicElts>."""

    def Node(self, Index: int) -> MAT_Node:
        """Return the Node of index <Index> in <theNodes>."""

    def NumberOfArcs(self) -> int:
        """Return the number of arcs of <me>."""

    def NumberOfNodes(self) -> int:
        """Return the number of nodes of <me>."""

    def NumberOfBasicElts(self) -> int:
        """Return the number of basic elements of <me>."""

    def NumberOfInfiniteNodes(self) -> int:
        """Return the number of infinites nodes of <me>."""

    def FusionOfBasicElts(self, IndexElt1: int, IndexElt2: int) -> tuple[bool, int, int, bool, int, int]:
        """
        Merge two BasicElts. The End of the BasicElt Elt1
        of IndexElt1 becomes The End of the BasicElt Elt2
        of IndexElt2. Elt2 is replaced in the arcs by
        Elt1, Elt2 is eliminated.

        <MergeArc1> is True if the fusion of the BasicElts =>
        a fusion of two Arcs which separated the same elements.
        In this case <GeomIndexArc1> and <GeomIndexArc2> are the
        Geometric Index of this arcs.

        If the BasicElt corresponds to a close line,
        the StartArc and the EndArc of Elt1 can separate the same
        elements.
        In this case there is a fusion of this arcs, <MergeArc2>
        is true and <GeomIndexArc3> and <GeomIndexArc4> are the
        Geometric Index of this arcs.
        """

    def CompactArcs(self) -> None: ...

    def CompactNodes(self) -> None: ...

    def ChangeBasicElts(self, NewMap: nanoocp.NCollection.NCollection_DataMap[int, nanoocp.MAT.MAT_BasicElt]) -> None: ...

    def ChangeBasicElt(self, Index: int) -> MAT_BasicElt: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MAT_ListOfBisector(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MAT_ListOfBisector) -> None: ...

    def __iter__(self) -> MAT_ListOfBisector:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> MAT_Bisector:
        """Python addition: see __iter__."""

    def First(self) -> None: ...

    def Last(self) -> None: ...

    def Init(self, aniten: MAT_Bisector | None) -> None: ...

    def Next(self) -> None: ...

    def Previous(self) -> None: ...

    def More(self) -> bool: ...

    @overload
    def Current(self) -> MAT_Bisector: ...

    @overload
    def Current(self, anitem: MAT_Bisector | None) -> None: ...

    def FirstItem(self) -> MAT_Bisector: ...

    def LastItem(self) -> MAT_Bisector: ...

    def PreviousItem(self) -> MAT_Bisector: ...

    def NextItem(self) -> MAT_Bisector: ...

    def Number(self) -> int: ...

    def Index(self) -> int: ...

    def Brackets(self, anindex: int) -> MAT_Bisector: ...

    def __call__(self, anindex: int) -> MAT_Bisector: ...

    def Unlink(self) -> None: ...

    def LinkBefore(self, anitem: MAT_Bisector | None) -> None: ...

    def LinkAfter(self, anitem: MAT_Bisector | None) -> None: ...

    def FrontAdd(self, anitem: MAT_Bisector | None) -> None: ...

    def BackAdd(self, anitem: MAT_Bisector | None) -> None: ...

    def Permute(self) -> None: ...

    def Loop(self) -> None: ...

    def IsEmpty(self) -> bool: ...

    def Dump(self, ashift: int, alevel: int) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MAT_ListOfEdge(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MAT_ListOfEdge) -> None: ...

    def __iter__(self) -> MAT_ListOfEdge:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> MAT_Edge:
        """Python addition: see __iter__."""

    def First(self) -> None: ...

    def Last(self) -> None: ...

    def Init(self, aniten: MAT_Edge | None) -> None: ...

    def Next(self) -> None: ...

    def Previous(self) -> None: ...

    def More(self) -> bool: ...

    @overload
    def Current(self) -> MAT_Edge: ...

    @overload
    def Current(self, anitem: MAT_Edge | None) -> None: ...

    def FirstItem(self) -> MAT_Edge: ...

    def LastItem(self) -> MAT_Edge: ...

    def PreviousItem(self) -> MAT_Edge: ...

    def NextItem(self) -> MAT_Edge: ...

    def Number(self) -> int: ...

    def Index(self) -> int: ...

    def Brackets(self, anindex: int) -> MAT_Edge: ...

    def __call__(self, anindex: int) -> MAT_Edge: ...

    def Unlink(self) -> None: ...

    def LinkBefore(self, anitem: MAT_Edge | None) -> None: ...

    def LinkAfter(self, anitem: MAT_Edge | None) -> None: ...

    def FrontAdd(self, anitem: MAT_Edge | None) -> None: ...

    def BackAdd(self, anitem: MAT_Edge | None) -> None: ...

    def Permute(self) -> None: ...

    def Loop(self) -> None: ...

    def IsEmpty(self) -> bool: ...

    def Dump(self, ashift: int, alevel: int) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MAT_TListNodeOfListOfBisector(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, anitem: MAT_Bisector | None) -> None: ...

    @overload
    def __init__(self, theOther: MAT_TListNodeOfListOfBisector) -> None: ...

    def GetItem(self) -> MAT_Bisector: ...

    @overload
    def Next(self) -> MAT_TListNodeOfListOfBisector: ...

    @overload
    def Next(self, atlistnode: MAT_TListNodeOfListOfBisector | None) -> None: ...

    @overload
    def Previous(self) -> MAT_TListNodeOfListOfBisector: ...

    @overload
    def Previous(self, atlistnode: MAT_TListNodeOfListOfBisector | None) -> None: ...

    def SetItem(self, anitem: MAT_Bisector | None) -> None: ...

    def Dummy(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MAT_TListNodeOfListOfEdge(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, anitem: MAT_Edge | None) -> None: ...

    @overload
    def __init__(self, theOther: MAT_TListNodeOfListOfEdge) -> None: ...

    def GetItem(self) -> MAT_Edge: ...

    @overload
    def Next(self) -> MAT_TListNodeOfListOfEdge: ...

    @overload
    def Next(self, atlistnode: MAT_TListNodeOfListOfEdge | None) -> None: ...

    @overload
    def Previous(self) -> MAT_TListNodeOfListOfEdge: ...

    @overload
    def Previous(self, atlistnode: MAT_TListNodeOfListOfEdge | None) -> None: ...

    def SetItem(self, anitem: MAT_Edge | None) -> None: ...

    def Dummy(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MAT_Zone(nanoocp.Standard.Standard_Transient):
    """
    Definition of Zone of Proximity of a BasicElt :
    ----------------------------------------------
    A Zone of proximity is the set of the points which are
    more near from the BasicElt than any other.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aBasicElt: MAT_BasicElt | None) -> None:
        """Compute the frontier of the Zone of proximity."""

    @overload
    def __init__(self, theOther: MAT_Zone) -> None: ...

    def Perform(self, aBasicElt: MAT_BasicElt | None) -> None:
        """Compute the frontier of the Zone of proximity."""

    def NumberOfArcs(self) -> int:
        """Return the number Of Arcs On the frontier of <me>."""

    def ArcOnFrontier(self, Index: int) -> MAT_Arc:
        """
        Return the Arc number <Index> on the frontier.
        of <me>.
        """

    def NoEmptyZone(self) -> bool:
        """Return TRUE if <me> is not empty ."""

    def Limited(self) -> bool:
        """Return TRUE if <me> is Limited."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.MAT
MAT_SequenceOfArc = nanoocp.NCollection.NCollection_Sequence[nanoocp.MAT.MAT_Arc]
MAT_SequenceOfBasicElt = nanoocp.NCollection.NCollection_Sequence[nanoocp.MAT.MAT_BasicElt]
