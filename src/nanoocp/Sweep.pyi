"""OCCT package Sweep (toolkit TKPrim)"""

from typing import overload

import nanoocp.TopAbs


class Sweep_NumShape:
    """
    Gives a simple indexed representation of a
    Directing Edge topology.
    """

    @overload
    def __init__(self) -> None:
        """Creates a dummy indexed edge."""

    @overload
    def __init__(self, Index: int, Type: nanoocp.TopAbs.TopAbs_ShapeEnum, Closed: bool = False, BegInf: bool = False, EndInf: bool = False) -> None:
        """
        Creates a new simple indexed edge.

        For an Edge : Index is the number of vertices (0,
        1 or 2),Type is TopAbs_EDGE, Closed is true if it
        is a closed edge, BegInf is true if the Edge is
        infinite at the beginning, EndInf is true if the
        edge is infinite at the end.

        For a Vertex : Index is the index of the vertex in
        the edge (1 or 2), Type is TopAbsVERTEX, all the
        other fields have no meanning.
        """

    @overload
    def __init__(self, theOther: Sweep_NumShape) -> None: ...

    def Init(self, Index: int, Type: nanoocp.TopAbs.TopAbs_ShapeEnum, Closed: bool = False, BegInf: bool = False, EndInf: bool = False) -> None:
        """
        Reinitialize a simple indexed edge.

        For an Edge : Index is the number of vertices (0,
        1 or 2),Type is TopAbs_EDGE, Closed is true if it
        is a closed edge, BegInf is true if the Edge is
        infinite at the beginning, EndInf is true if the
        edge is infinite at the end.

        For a Vertex : Index is the index of the vertex in
        the edge (1 or 2), Type is TopAbsVERTEX, Closed is
        true if it is the vertex of a closed edge, all the
        other fields have no meanning.
        """

    def Index(self) -> int: ...

    def Type(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum: ...

    def Closed(self) -> bool: ...

    def BegInfinite(self) -> bool: ...

    def EndInfinite(self) -> bool: ...

    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

class Sweep_NumShapeIterator:
    """
    This class provides iteration services required by
    the Swept Primitives for a Directing NumShape
    Line.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Sweep_NumShapeIterator) -> None: ...

    def __iter__(self) -> Sweep_NumShapeIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> Sweep_NumShape:
        """Python addition: see __iter__."""

    def Init(self, aShape: Sweep_NumShape) -> None:
        """Reset the NumShapeIterator on sub-shapes of <aShape>."""

    def More(self) -> bool:
        """Returns True if there is a current sub-shape."""

    def Next(self) -> None:
        """Moves to the next sub-shape."""

    def Value(self) -> Sweep_NumShape:
        """Returns the current sub-shape."""

    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Returns the orientation of the current sub-shape."""

class Sweep_NumShapeTool:
    """
    This class provides the indexation and type analysis
    services required by the NumShape Directing Shapes of
    Swept Primitives.
    """

    @overload
    def __init__(self, aShape: Sweep_NumShape) -> None:
        """
        Create a new NumShapeTool with <aShape>. The Tool
        must prepare an indexation for all the subshapes
        of this shape.
        """

    @overload
    def __init__(self, theOther: Sweep_NumShapeTool) -> None: ...

    def NbShapes(self) -> int:
        """Returns the number of subshapes in the shape."""

    def Index(self, aShape: Sweep_NumShape) -> int:
        """Returns the index of <aShape>."""

    def Shape(self, anIndex: int) -> Sweep_NumShape:
        """Returns the Shape at index anIndex"""

    def Type(self, aShape: Sweep_NumShape) -> nanoocp.TopAbs.TopAbs_ShapeEnum:
        """Returns the type of <aShape>."""

    def Orientation(self, aShape: Sweep_NumShape) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Returns the orientation of <aShape>."""

    def HasFirstVertex(self) -> bool:
        """Returns true if there is a First Vertex in the Shape."""

    def HasLastVertex(self) -> bool:
        """Returns true if there is a Last Vertex in the Shape."""

    def FirstVertex(self) -> Sweep_NumShape:
        """Returns the first vertex."""

    def LastVertex(self) -> Sweep_NumShape:
        """Returns the last vertex."""
