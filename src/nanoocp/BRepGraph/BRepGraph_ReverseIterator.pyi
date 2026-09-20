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
    def FindRef(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>", theChild: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>") -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)8>": ...

class WireFromEdgeCoEdgeTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: WireFromEdgeCoEdgeTraits) -> None: ...

    @staticmethod
    def ParentIdOf(theCoEdge: nanoocp.BRepGraphInc.CoEdgeDef) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)3>": ...

    @staticmethod
    def NbParents(theGraph: nanoocp.BRepGraph.BRepGraph) -> int: ...

class FaceFromEdgeCoEdgeTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: FaceFromEdgeCoEdgeTraits) -> None: ...

    @staticmethod
    def ParentIdOf(theCoEdge: nanoocp.BRepGraphInc.CoEdgeDef) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>": ...

    @staticmethod
    def NbParents(theGraph: nanoocp.BRepGraph.BRepGraph) -> int: ...

class EdgeOfVertexRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: EdgeOfVertexRefTraits) -> None: ...

    @staticmethod
    def FindRef(theGraph: nanoocp.BRepGraph.BRepGraph, theParent: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>", theChild: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)5>") -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)3>": ...

class FaceFromWireRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: FaceFromWireRefTraits) -> None: ...

    @staticmethod
    def Id(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)2>") -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)2>": ...

class ShellFromFaceRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShellFromFaceRefTraits) -> None: ...

    @staticmethod
    def Id(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)1>") -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)1>": ...

class SolidFromShellRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: SolidFromShellRefTraits) -> None: ...

    @staticmethod
    def Id(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)0>") -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)0>": ...

class CompSolidFromSolidRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CompSolidFromSolidRefTraits) -> None: ...

    @staticmethod
    def Id(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)4>") -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)7>": ...

class CompoundFromChildRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: CompoundFromChildRefTraits) -> None: ...

    @staticmethod
    def Id(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)5>") -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)6>": ...

class OccurrenceFromOccurrenceRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OccurrenceFromOccurrenceRefTraits) -> None: ...

    @staticmethod
    def Id(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)6>") -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)11>": ...

class ProductFromOccurrenceRefTraits:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ProductFromOccurrenceRefTraits) -> None: ...

    @staticmethod
    def Id(theGraph: nanoocp.BRepGraph.BRepGraph, theRefId: "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)6>") -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)10>": ...
