"""C++ namespace BRepGraph_DefsIterator (OCCT package BRepGraph)"""

from typing import overload

import nanoocp.BRepGraph
import nanoocp.BRepGraphInc
import nanoocp.NCollection


class DefsVertexOfEdge:
    """
    @brief Direct active boundary vertex children of an edge.

    Iteration order is start vertex, then end vertex.
    """

    @overload
    def __init__(self, theGraph: nanoocp.BRepGraph.BRepGraph, theEdgeId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>") -> None: ...

    @overload
    def __init__(self, theOther: DefsVertexOfEdge) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)5>": ...

    def Current(self) -> nanoocp.BRepGraphInc.VertexDef: ...

    def CurrentRefId(self) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)3>":
        """
        Returns the start/end vertex reference entry that carries the current child relation.
        """

    def Index(self) -> int: ...

    def begin(self) -> "NCollection_ForwardRangeIterator<BRepGraph_DefsIterator::DefsVertexOfEdge>":
        """Returns an STL-compatible iterator for range-based for loops."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""
