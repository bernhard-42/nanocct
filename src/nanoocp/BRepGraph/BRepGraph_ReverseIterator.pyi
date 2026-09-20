"""C++ namespace BRepGraph_ReverseIterator (OCCT package BRepGraph)"""

from typing import overload

import nanoocp.BRepGraph
import nanoocp.BRepGraphInc


class WireOfCoEdgeUsageTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: WireOfCoEdgeUsageTraits) -> None: ...

    @staticmethod
    def FindRef(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_WireId, theChild: nanoocp.BRepGraph.BRepGraph_CoEdgeId) -> nanoocp.BRepGraph.BRepGraph_CoEdgeId: ...

class WireFromEdgeCoEdgeTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: WireFromEdgeCoEdgeTraits) -> None: ...

    @staticmethod
    def ParentIdOf(theCoEdge: nanoocp.BRepGraphInc.CoEdgeDef) -> nanoocp.BRepGraph.BRepGraph_WireId: ...

    @staticmethod
    def NbParents(theGraph: nanoocp.BRepGraph.BRepGraph) -> int: ...

class FaceFromEdgeCoEdgeTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: FaceFromEdgeCoEdgeTraits) -> None: ...

    @staticmethod
    def ParentIdOf(theCoEdge: nanoocp.BRepGraphInc.CoEdgeDef) -> nanoocp.BRepGraph.BRepGraph_FaceId: ...

    @staticmethod
    def NbParents(theGraph: nanoocp.BRepGraph.BRepGraph) -> int: ...

class EdgeOfVertexRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: EdgeOfVertexRefTraits) -> None: ...

    @staticmethod
    def FindRef(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: nanoocp.BRepGraph.BRepGraph_EdgeId, theChild: nanoocp.BRepGraph.BRepGraph_VertexId) -> nanoocp.BRepGraph.BRepGraph_VertexRefId: ...

class FaceFromWireRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: FaceFromWireRefTraits) -> None: ...

    @staticmethod
    def Id(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: nanoocp.BRepGraph.BRepGraph_WireRefId) -> nanoocp.BRepGraph.BRepGraph_FaceId: ...

class ShellFromFaceRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShellFromFaceRefTraits) -> None: ...

    @staticmethod
    def Id(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: nanoocp.BRepGraph.BRepGraph_FaceRefId) -> nanoocp.BRepGraph.BRepGraph_ShellId: ...

class SolidFromShellRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: SolidFromShellRefTraits) -> None: ...

    @staticmethod
    def Id(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: nanoocp.BRepGraph.BRepGraph_ShellRefId) -> nanoocp.BRepGraph.BRepGraph_SolidId: ...

class CompSolidFromSolidRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CompSolidFromSolidRefTraits) -> None: ...

    @staticmethod
    def Id(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: nanoocp.BRepGraph.BRepGraph_SolidRefId) -> nanoocp.BRepGraph.BRepGraph_CompSolidId: ...

class CompoundFromChildRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CompoundFromChildRefTraits) -> None: ...

    @staticmethod
    def Id(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: nanoocp.BRepGraph.BRepGraph_ChildRefId) -> nanoocp.BRepGraph.BRepGraph_CompoundId: ...

class OccurrenceFromOccurrenceRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OccurrenceFromOccurrenceRefTraits) -> None: ...

    @staticmethod
    def Id(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: nanoocp.BRepGraph.BRepGraph_OccurrenceRefId) -> nanoocp.BRepGraph.BRepGraph_OccurrenceId: ...

class ProductFromOccurrenceRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ProductFromOccurrenceRefTraits) -> None: ...

    @staticmethod
    def Id(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: nanoocp.BRepGraph.BRepGraph_OccurrenceRefId) -> nanoocp.BRepGraph.BRepGraph_ProductId: ...
