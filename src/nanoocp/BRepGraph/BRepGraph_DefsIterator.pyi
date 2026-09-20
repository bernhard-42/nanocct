"""C++ namespace BRepGraph_DefsIterator (OCCT package BRepGraph)"""

from typing import overload

import nanoocp.BRepGraph
import nanoocp.BRepGraphInc
import nanoocp.NCollection


class ShellOfSolidTraits(nanoocp.BRepGraph.BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Solid__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Shell__BRepGraphInc_ShellRef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Shell__BRepGraphInc_ShellDef):
    """Traits for iterating over shell children of a solid."""

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

    @staticmethod
    def Child(theGraph: nanoocp.BRepGraph.BRepGraph, theChildId: nanoocp.BRepGraph.BRepGraph_ShellId) -> nanoocp.BRepGraphInc.ShellDef: ...

class FaceOfShellTraits(nanoocp.BRepGraph.BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Shell__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Face__BRepGraphInc_FaceRef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face__BRepGraphInc_FaceDef):
    """Traits for iterating over face children of a shell."""

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

    @staticmethod
    def Child(theGraph: nanoocp.BRepGraph.BRepGraph, theChildId: nanoocp.BRepGraph.BRepGraph_FaceId) -> nanoocp.BRepGraphInc.FaceDef: ...

class WireOfFaceTraits(nanoocp.BRepGraph.BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Wire__BRepGraphInc_WireRef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire__BRepGraphInc_WireDef):
    """Traits for iterating over wire children of a face."""

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

    @staticmethod
    def Child(theGraph: nanoocp.BRepGraph.BRepGraph, theChildId: nanoocp.BRepGraph.BRepGraph_WireId) -> nanoocp.BRepGraphInc.WireDef: ...

class CoEdgeOfWireTraits(nanoocp.BRepGraph.BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge__BRepGraphInc_CoEdgeDef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge__BRepGraphInc_CoEdgeDef):
    """
    Traits for iterating over coedge children of a wire (direct, no ref indirection).
    """

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

    @staticmethod
    def Child(theGraph: nanoocp.BRepGraph.BRepGraph, theChildId: nanoocp.BRepGraph.BRepGraph_CoEdgeId) -> nanoocp.BRepGraphInc.CoEdgeDef: ...

class EdgeOfWireTraits(nanoocp.BRepGraph.BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge__BRepGraphInc_CoEdgeDef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Edge__BRepGraphInc_EdgeDef):
    """
    Traits for iterating over edge children of a wire (via coedge indirection).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: EdgeOfWireTraits) -> None: ...

    @staticmethod
    def IsParentValid(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_WireId) -> bool: ...

    @staticmethod
    def RefIds(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_WireId) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BRepGraph.BRepGraph_CoEdgeId]: ...

    @staticmethod
    def Ref(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: nanoocp.BRepGraph.BRepGraph_CoEdgeId) -> nanoocp.BRepGraphInc.CoEdgeDef: ...

    @staticmethod
    def ChildIdOf(theGraph: nanoocp.BRepGraph.BRepGraph, theRef: nanoocp.BRepGraphInc.CoEdgeDef) -> nanoocp.BRepGraph.BRepGraph_EdgeId: ...

    @staticmethod
    def Child(theGraph: nanoocp.BRepGraph.BRepGraph, theChildId: nanoocp.BRepGraph.BRepGraph_EdgeId) -> nanoocp.BRepGraphInc.EdgeDef: ...

class SolidOfCompSolidTraits(nanoocp.BRepGraph.BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CompSolid__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Solid__BRepGraphInc_SolidRef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Solid__BRepGraphInc_SolidDef):
    """Traits for iterating over solid children of a compsolid."""

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

    @staticmethod
    def Child(theGraph: nanoocp.BRepGraph.BRepGraph, theChildId: nanoocp.BRepGraph.BRepGraph_SolidId) -> nanoocp.BRepGraphInc.SolidDef: ...

class ChildOfCompoundTraits(nanoocp.BRepGraph.BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Compound__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Child__BRepGraphInc_ChildRef__BRepGraph_NodeId__BRepGraphInc_BaseDef):
    """Traits for iterating over child nodes of a compound."""

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

    @staticmethod
    def Child(theGraph: nanoocp.BRepGraph.BRepGraph, theChildId: nanoocp.BRepGraph.BRepGraph_NodeId) -> nanoocp.BRepGraphInc.BaseDef: ...

class OccurrenceOfProductTraits(nanoocp.BRepGraph.BRepGraph_DefsIterator_BaseTraits__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Product__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Occurrence__BRepGraphInc_OccurrenceRef__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Occurrence__BRepGraphInc_OccurrenceDef):
    """Traits for iterating over occurrence children of a product."""

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

    @staticmethod
    def Child(theGraph: nanoocp.BRepGraph.BRepGraph, theChildId: nanoocp.BRepGraph.BRepGraph_OccurrenceId) -> nanoocp.BRepGraphInc.OccurrenceDef: ...

class DefsVertexOfEdge:
    """
    @brief Direct active boundary vertex children of an edge.

    Iteration order is start vertex, then end vertex.
    """

    @overload
    def __init__(self, theGraph: nanoocp.BRepGraph.BRepGraph, theEdgeId: nanoocp.BRepGraph.BRepGraph_EdgeId) -> None: ...

    @overload
    def __init__(self, theOther: DefsVertexOfEdge) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> nanoocp.BRepGraph.BRepGraph_VertexId: ...

    def Current(self) -> nanoocp.BRepGraphInc.VertexDef: ...

    def CurrentRefId(self) -> nanoocp.BRepGraph.BRepGraph_VertexRefId:
        """
        Returns the start/end vertex reference entry that carries the current child relation.
        """

    def Index(self) -> int: ...

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""
