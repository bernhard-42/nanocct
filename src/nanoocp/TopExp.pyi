"""OCCT package TopExp (toolkit TKBRep)"""

from typing import overload

import nanoocp.NCollection
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.TopTools


class TopExp:
    """
    This package provides basic tools to explore the
    topological data structures.

    * Explorer: A tool to find all sub-shapes of a given
    type. e.g. all faces of a solid.

    * Package methods to map sub-shapes of a shape.

    Level : Public
    All methods of all classes will be public.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopExp) -> None: ...

    @overload
    @staticmethod
    def MapShapes(S: nanoocp.TopoDS.TopoDS_Shape, T: nanoocp.TopAbs.TopAbs_ShapeEnum, M: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        Tool to explore a topological data structure.
        Stores in the map <M> all the sub-shapes of <S>
        of type <T>.

        Warning: The map is not cleared at first.
        """

    @overload
    @staticmethod
    def MapShapes(S: nanoocp.TopoDS.TopoDS_Shape, M: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], cumOri: bool = True, cumLoc: bool = True) -> None: ...

    @overload
    @staticmethod
    def MapShapes(S: nanoocp.TopoDS.TopoDS_Shape, M: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], cumOri: bool = True, cumLoc: bool = True) -> None:
        """
        Stores in the map <M> all the sub-shapes of <S>.
        - If cumOri is true, the function composes all
        sub-shapes with the orientation of S.
        - If cumLoc is true, the function multiplies all
        sub-shapes by the location of S, i.e. it applies to
        each sub-shape the transformation that is associated with S.
        """

    @staticmethod
    def MapShapesAndAncestors(S: nanoocp.TopoDS.TopoDS_Shape, TS: nanoocp.TopAbs.TopAbs_ShapeEnum, TA: nanoocp.TopAbs.TopAbs_ShapeEnum, M: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        Stores in the map <M> all the subshape of <S> of
        type <TS> for each one append to the list all
        the ancestors of type <TA>. For example map all
        the edges and bind the list of faces.
        Warning: The map is not cleared at first.
        """

    @staticmethod
    def MapShapesAndUniqueAncestors(S: nanoocp.TopoDS.TopoDS_Shape, TS: nanoocp.TopAbs.TopAbs_ShapeEnum, TA: nanoocp.TopAbs.TopAbs_ShapeEnum, M: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], useOrientation: bool = False) -> None:
        """
        Stores in the map <M> all the subshape of <S> of
        type <TS> for each one append to the list all
        unique ancestors of type <TA>. For example map all
        the edges and bind the list of faces.
        useOrientation = True : taking account the ancestor orientation
        Warning: The map is not cleared at first.
        """

    @staticmethod
    def FirstVertex(E: nanoocp.TopoDS.TopoDS_Edge, CumOri: bool = False) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Returns the Vertex of orientation FORWARD in E. If
        there is none returns a Null Shape.
        CumOri = True : taking account the edge orientation
        """

    @staticmethod
    def LastVertex(E: nanoocp.TopoDS.TopoDS_Edge, CumOri: bool = False) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Returns the Vertex of orientation REVERSED in E. If
        there is none returns a Null Shape.
        CumOri = True : taking account the edge orientation
        """

    @overload
    @staticmethod
    def Vertices(E: nanoocp.TopoDS.TopoDS_Edge, Vfirst: nanoocp.TopoDS.TopoDS_Vertex, Vlast: nanoocp.TopoDS.TopoDS_Vertex, CumOri: bool = False) -> None:
        """
        Returns in Vfirst, Vlast the FORWARD and REVERSED
        vertices of the edge <E>. May be null shapes.
        CumOri = True : taking account the edge orientation
        """

    @overload
    @staticmethod
    def Vertices(W: nanoocp.TopoDS.TopoDS_Wire, Vfirst: nanoocp.TopoDS.TopoDS_Vertex, Vlast: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        Returns in Vfirst, Vlast the first and last
        vertices of the open wire <W>. May be null shapes.
        if <W> is closed Vfirst and Vlast are a same
        vertex on <W>.
        if <W> is no manifold. VFirst and VLast are null
        shapes.
        """

    @staticmethod
    def CommonVertex(E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, V: nanoocp.TopoDS.TopoDS_Vertex) -> bool:
        """
        Finds the vertex <V> common to the two edges
        <E1,E2>, returns True if this vertex exists.

        Warning: <V> has sense only if the value <True> is returned
        """

class TopExp_Explorer:
    """
    An Explorer is a Tool to visit a Topological Data
    Structure from the TopoDS package.

    An Explorer is built with:

    * The Shape to explore.

    * The type of Shapes to find: e.g VERTEX, EDGE.
    This type cannot be SHAPE.

    * The type of Shapes to avoid. e.g SHELL, EDGE.
    By default this type is SHAPE which means no
    restriction on the exploration.

    The Explorer visits all the structure to find
    shapes of the requested type which are not
    contained in the type to avoid.

    Example to find all the Faces in the Shape S :

    TopExp_Explorer Ex;
    for (Ex.Init(S,TopAbs_FACE); Ex.More(); Ex.Next()) {
    ProcessFace(Ex.Current());
    }

    // an other way
    TopExp_Explorer Ex(S,TopAbs_FACE);
    while (Ex.More()) {
    ProcessFace(Ex.Current());
    Ex.Next();
    }

    To find all the vertices which are not in an edge :

    for (Ex.Init(S,TopAbs_VERTEX,TopAbs_EDGE); ...)

    To find all the faces in a SHELL, then all the
    faces not in a SHELL :

    TopExp_Explorer Ex1, Ex2;

    for (Ex1.Init(S,TopAbs_SHELL),...) {
    // visit all shells
    for (Ex2.Init(Ex1.Current(),TopAbs_FACE),...) {
    // visit all the faces of the current shell
    }
    }

    for (Ex1.Init(S,TopAbs_FACE,TopAbs_SHELL),...) {
    // visit all faces not in a shell
    }

    If the type to avoid is the same or is less
    complex than the type to find it has no effect.

    For example searching edges not in a vertex does
    not make a difference.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty explorer, becomes useful after Init."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, ToFind: nanoocp.TopAbs.TopAbs_ShapeEnum, ToAvoid: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> None:
        """
        Creates an Explorer on the Shape <S>.

        <ToFind> is the type of shapes to search.
        TopAbs_VERTEX, TopAbs_EDGE, ...

        <ToAvoid> is the type of shape to skip in the
        exploration. If <ToAvoid> is equal or less
        complex than <ToFind> or if <ToAVoid> is SHAPE it
        has no effect on the exploration.
        """

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape, ToFind: nanoocp.TopAbs.TopAbs_ShapeEnum, ToAvoid: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> None:
        """
        Resets this explorer on the shape S. It is initialized to
        search the shape S, for shapes of type ToFind, that
        are not part of a shape ToAvoid.
        If the shape ToAvoid is equal to TopAbs_SHAPE, or
        if it is the same as, or less complex than, the shape
        ToFind it has no effect on the search.
        """

    def More(self) -> bool:
        """Returns True if there are more shapes in the exploration."""

    def Next(self) -> None:
        """Moves to the next Shape in the exploration."""

    def Value(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the current shape in the exploration."""

    def Current(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the current shape in the exploration."""

    def ReInit(self) -> None:
        """Reinitialize the exploration with the original arguments."""

    def ExploredShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return explored shape."""

    def Depth(self) -> int:
        """
        Returns the current depth of the exploration. 0 is
        the shape to explore itself.
        """

    def Clear(self) -> None:
        """Clears the content of the explorer."""

    def end(self) -> nanoocp.NCollection.NCollection_ForwardRangeSentinel:
        """Returns a sentinel marking the end of iteration."""

class NCollection_ForwardRangeIterator__TopExp_Explorer:
    """
    @brief STL input iterator that wraps an OCCT More()/Next() iterator.

    Holds a non-owning pointer to the host iterator/explorer.
    The host must outlive this iterator (guaranteed by range-for semantics).

    @tparam HostType OCCT iterator/explorer with More(), Next(), and a value accessor.
    """

    @overload
    def __init__(self, theHost: TopExp_Explorer) -> None:
        """Construct from a pointer to the host iterator."""

    @overload
    def __init__(self, theOther: NCollection_ForwardRangeIterator__TopExp_Explorer) -> None: ...
