"""C++ namespace BRepGraph_RefsIterator (OCCT package BRepGraph)"""

from typing import overload

import nanoocp.BRepGraph
import nanoocp.BRepGraphInc
import nanoocp.NCollection


class ShellOfSolidTraits(nanoocp.BRepGraph.BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Solid__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Shell__BRepGraphInc_ShellRef):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShellOfSolidTraits) -> None: ...

    @staticmethod
    def IsParentValid(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_SolidId) -> bool: ...

    @staticmethod
    def RefIds(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_SolidId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_ShellRefId]: ...

    @staticmethod
    def Ref(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: nanoocp.BRepGraph.BRepGraph_ShellRefId) -> nanoocp.BRepGraphInc.ShellRef: ...

    @staticmethod
    def ChildIdOf(arg0: nanoocp.BRepGraph.BRepGraph, theRef: nanoocp.BRepGraphInc.ShellRef) -> nanoocp.BRepGraph.BRepGraph_ShellId: ...

class FaceOfShellTraits(nanoocp.BRepGraph.BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Shell__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Face__BRepGraphInc_FaceRef):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: FaceOfShellTraits) -> None: ...

    @staticmethod
    def IsParentValid(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_ShellId) -> bool: ...

    @staticmethod
    def RefIds(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_ShellId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_FaceRefId]: ...

    @staticmethod
    def Ref(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: nanoocp.BRepGraph.BRepGraph_FaceRefId) -> nanoocp.BRepGraphInc.FaceRef: ...

    @staticmethod
    def ChildIdOf(arg0: nanoocp.BRepGraph.BRepGraph, theRef: nanoocp.BRepGraphInc.FaceRef) -> nanoocp.BRepGraph.BRepGraph_FaceId: ...

class WireOfFaceTraits(nanoocp.BRepGraph.BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Wire__BRepGraphInc_WireRef):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: WireOfFaceTraits) -> None: ...

    @staticmethod
    def IsParentValid(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_FaceId) -> bool: ...

    @staticmethod
    def RefIds(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_FaceId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_WireRefId]: ...

    @staticmethod
    def Ref(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: nanoocp.BRepGraph.BRepGraph_WireRefId) -> nanoocp.BRepGraphInc.WireRef: ...

    @staticmethod
    def ChildIdOf(arg0: nanoocp.BRepGraph.BRepGraph, theRef: nanoocp.BRepGraphInc.WireRef) -> nanoocp.BRepGraph.BRepGraph_WireId: ...

class CoEdgeOfWireTraits(nanoocp.BRepGraph.BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge__BRepGraphInc_CoEdgeDef):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CoEdgeOfWireTraits) -> None: ...

    @staticmethod
    def IsParentValid(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_WireId) -> bool: ...

    @staticmethod
    def RefIds(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_WireId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_CoEdgeId]: ...

    @staticmethod
    def Ref(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: nanoocp.BRepGraph.BRepGraph_CoEdgeId) -> nanoocp.BRepGraphInc.CoEdgeDef: ...

class SolidOfCompSolidTraits(nanoocp.BRepGraph.BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CompSolid__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Solid__BRepGraphInc_SolidRef):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: SolidOfCompSolidTraits) -> None: ...

    @staticmethod
    def IsParentValid(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_CompSolidId) -> bool: ...

    @staticmethod
    def RefIds(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_CompSolidId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_SolidRefId]: ...

    @staticmethod
    def Ref(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: nanoocp.BRepGraph.BRepGraph_SolidRefId) -> nanoocp.BRepGraphInc.SolidRef: ...

    @staticmethod
    def ChildIdOf(arg0: nanoocp.BRepGraph.BRepGraph, theRef: nanoocp.BRepGraphInc.SolidRef) -> nanoocp.BRepGraph.BRepGraph_SolidId: ...

class ChildOfCompoundTraits(nanoocp.BRepGraph.BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Compound__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Child__BRepGraphInc_ChildRef):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ChildOfCompoundTraits) -> None: ...

    @staticmethod
    def IsParentValid(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_CompoundId) -> bool: ...

    @staticmethod
    def RefIds(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_CompoundId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_ChildRefId]: ...

    @staticmethod
    def Ref(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: nanoocp.BRepGraph.BRepGraph_ChildRefId) -> nanoocp.BRepGraphInc.ChildRef: ...

    @staticmethod
    def ChildIdOf(arg0: nanoocp.BRepGraph.BRepGraph, theRef: nanoocp.BRepGraphInc.ChildRef) -> nanoocp.BRepGraph.BRepGraph_NodeId: ...

class OccurrenceOfProductTraits(nanoocp.BRepGraph.BRepGraph_RefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Product__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Occurrence__BRepGraphInc_OccurrenceRef):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OccurrenceOfProductTraits) -> None: ...

    @staticmethod
    def IsParentValid(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_ProductId) -> bool: ...

    @staticmethod
    def RefIds(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_ProductId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_OccurrenceRefId]: ...

    @staticmethod
    def Ref(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: nanoocp.BRepGraph.BRepGraph_OccurrenceRefId) -> nanoocp.BRepGraphInc.OccurrenceRef: ...

    @staticmethod
    def ChildIdOf(arg0: nanoocp.BRepGraph.BRepGraph, theRef: nanoocp.BRepGraphInc.OccurrenceRef) -> nanoocp.BRepGraph.BRepGraph_OccurrenceId: ...

class RefsVertexOfEdge:
    """
    @brief Direct active boundary vertex reference ids of an edge.

    Iteration order is start vertex, then end vertex.
    """

    @overload
    def __init__(self, theGraph: nanoocp.BRepGraph.BRepGraph, theEdgeId: nanoocp.BRepGraph.BRepGraph_EdgeId) -> None: ...

    @overload
    def __init__(self, theOther: RefsVertexOfEdge) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> nanoocp.BRepGraph.BRepGraph_VertexRefId: ...

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""
