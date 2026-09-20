"""C++ namespace BRepGraph_RefsIterator (OCCT package BRepGraph)"""

from typing import overload

import nanoocp.BRepGraph
import nanoocp.NCollection


class RefsVertexOfEdge:
    """
    @brief Direct active boundary vertex reference ids of an edge.

    Iteration order is start vertex, then end vertex.
    """

    @overload
    def __init__(self, theGraph: nanoocp.BRepGraph.BRepGraph, theEdgeId: "BRepGraph_NodeId::Typed<(BRepGraph_NodeId::Kind)4>") -> None: ...

    @overload
    def __init__(self, theOther: RefsVertexOfEdge) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def CurrentId(self) -> "BRepGraph_RefId::Typed<(BRepGraph_RefId::Kind)3>": ...

    def Index(self) -> int: ...

    def begin(self) -> "NCollection_ForwardRangeIterator<BRepGraph_RefsIterator::RefsVertexOfEdge>":
        """Returns an STL-compatible iterator for range-based for loops."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""
