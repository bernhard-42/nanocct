"""OCCT package ShapeBuild (toolkit TKShHealing)"""

from typing import overload

import nanoocp.BRepTools
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.ShapeExtend
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.gp


class ShapeBuild:
    """
    This package provides basic building tools for other packages in ShapeHealing.
    These tools are rather internal for ShapeHealing .
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeBuild) -> None: ...

    @staticmethod
    def PlaneXOY() -> nanoocp.Geom.Geom_Plane:
        """
        Rebuilds a shape with substitution of some components
        Returns a Geom_Surface which is the Plane XOY (Z positive)
        This allows to consider an UV space homologous to a 3D space,
        with this support surface
        """

class ShapeBuild_Edge:
    """
    This class provides low-level operators for building an edge
    3d curve, copying edge with replaced vertices etc.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeBuild_Edge) -> None: ...

    def CopyReplaceVertices(self, edge: nanoocp.TopoDS.TopoDS_Edge, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Copy edge and replace one or both its vertices to a given
        one(s). Vertex V1 replaces FORWARD vertex, and V2 - REVERSED,
        as they are found by TopoDS_Iterator.
        If V1 or V2 is NULL, the original vertex is taken
        """

    def CopyRanges(self, toedge: nanoocp.TopoDS.TopoDS_Edge, fromedge: nanoocp.TopoDS.TopoDS_Edge, alpha: float = 0.0, beta: float = 1.0) -> None:
        """
        Copies ranges for curve3d and all common pcurves from
        edge <fromedge> into edge <toedge>.
        """

    def SetRange3d(self, edge: nanoocp.TopoDS.TopoDS_Edge, first: float, last: float) -> None:
        """Sets range on 3d curve only."""

    def CopyPCurves(self, toedge: nanoocp.TopoDS.TopoDS_Edge, fromedge: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        Makes a copy of pcurves from edge <fromedge> into edge
        <toedge>. Pcurves which are already present in <toedge>,
        are replaced by copies, other are copied. Ranges are also
        copied.
        """

    def Copy(self, edge: nanoocp.TopoDS.TopoDS_Edge, sharepcurves: bool = True) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Make a copy of <edge> by call to CopyReplaceVertices()
        (i.e. construct new TEdge with the same pcurves and vertices).
        If <sharepcurves> is False, pcurves are also replaced by
        their copies with help of method CopyPCurves
        """

    @overload
    def RemovePCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Removes the PCurve(s) which could be recorded in an Edge for
        the given Face
        """

    @overload
    def RemovePCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, surf: nanoocp.Geom.Geom_Surface | None) -> None:
        """
        Removes the PCurve(s) which could be recorded in an Edge for
        the given Surface
        """

    @overload
    def RemovePCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, surf: nanoocp.Geom.Geom_Surface | None, loc: nanoocp.TopLoc.TopLoc_Location) -> None:
        """
        Removes the PCurve(s) which could be recorded in an Edge for
        the given Surface, with given Location
        """

    def ReplacePCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, pcurve: nanoocp.Geom2d.Geom2d_Curve | None, face: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Replace the PCurve in an Edge for the given Face
        In case if edge is seam, i.e. has 2 pcurves on that face,
        only pcurve corresponding to the orientation of the edge is
        replaced
        """

    def ReassignPCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, old: nanoocp.TopoDS.TopoDS_Face, sub: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """
        Reassign edge pcurve lying on face <old> to another face <sub>.
        If edge has two pcurves on <old> face, only one of them will be
        reassigned, and other will left alone. Similarly, if edge already
        had a pcurve on face <sub>, it will have two pcurves on it.
        Returns True if succeeded, False if no pcurve lying on <old> found.
        """

    def TransformPCurve(self, pcurve: nanoocp.Geom2d.Geom2d_Curve | None, trans: nanoocp.gp.gp_Trsf2d, uFact: float) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float, float]:
        """Transforms the PCurve with given matrix and affinity U factor."""

    def RemoveCurve3d(self, edge: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Removes the Curve3D recorded in an Edge"""

    def BuildCurve3d(self, edge: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """Calls BRepTools::BuildCurve3D"""

    @overload
    def MakeEdge(self, edge: nanoocp.TopoDS.TopoDS_Edge, curve: nanoocp.Geom.Geom_Curve | None, L: nanoocp.TopLoc.TopLoc_Location) -> None:
        """Makes edge with curve and location"""

    @overload
    def MakeEdge(self, edge: nanoocp.TopoDS.TopoDS_Edge, curve: nanoocp.Geom.Geom_Curve | None, L: nanoocp.TopLoc.TopLoc_Location, p1: float, p2: float) -> None:
        """Makes edge with curve, location and range [p1, p2]"""

    @overload
    def MakeEdge(self, edge: nanoocp.TopoDS.TopoDS_Edge, pcurve: nanoocp.Geom2d.Geom2d_Curve | None, face: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Makes edge with pcurve and face"""

    @overload
    def MakeEdge(self, edge: nanoocp.TopoDS.TopoDS_Edge, pcurve: nanoocp.Geom2d.Geom2d_Curve | None, face: nanoocp.TopoDS.TopoDS_Face, p1: float, p2: float) -> None:
        """Makes edge with pcurve, face and range [p1, p2]"""

    @overload
    def MakeEdge(self, edge: nanoocp.TopoDS.TopoDS_Edge, pcurve: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, L: nanoocp.TopLoc.TopLoc_Location) -> None:
        """Makes edge with pcurve, surface and location"""

    @overload
    def MakeEdge(self, edge: nanoocp.TopoDS.TopoDS_Edge, pcurve: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, L: nanoocp.TopLoc.TopLoc_Location, p1: float, p2: float) -> None:
        """Makes edge with pcurve, surface, location and range [p1, p2]"""

class ShapeBuild_ReShape(nanoocp.BRepTools.BRepTools_ReShape):
    """
    Rebuilds a Shape by making pre-defined substitutions on some
    of its components

    In a first phase, it records requests to replace or remove
    some individual shapes
    For each shape, the last given request is recorded
    Requests may be applied "Oriented" (i.e. only to an item with
    the SAME orientation) or not (the orientation of replacing
    shape is respectful of that of the original one)

    Then, these requests may be applied to any shape which may
    contain one or more of these individual shapes
    """

    @overload
    def __init__(self) -> None:
        """Returns an empty Reshape"""

    @overload
    def __init__(self, theOther: ShapeBuild_ReShape) -> None: ...

    @overload
    def Apply(self, shape: nanoocp.TopoDS.TopoDS_Shape, until: nanoocp.TopAbs.TopAbs_ShapeEnum, buildmode: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Applies the substitutions requests to a shape

        <until> gives the level of type until which requests are taken
        into account. For subshapes of the type <until> no rebuild
        and further exploring are done.
        ACTUALLY, NOT IMPLEMENTED BELOW TopAbs_FACE

        <buildmode> says how to do on a SOLID,SHELL ... if one of its
        sub-shapes has been changed:
        0: at least one Replace or Remove -> COMPOUND, else as such
        1: at least one Remove (Replace are ignored) -> COMPOUND
        2: Replace and Remove are both ignored
        If Replace/Remove are ignored or absent, the result as same
        type as the starting shape
        """

    @overload
    def Apply(self, shape: nanoocp.TopoDS.TopoDS_Shape, until: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Applies the substitutions requests to a shape.

        <until> gives the level of type until which requests are taken
        into account. For subshapes of the type <until> no rebuild
        and further exploring are done.

        NOTE: each subshape can be replaced by shape of the same type
        or by shape containing only shapes of that type (for
        example, TopoDS_Edge can be replaced by TopoDS_Edge,
        TopoDS_Wire or TopoDS_Compound containing TopoDS_Edges).
        If incompatible shape type is encountered, it is ignored
        and flag FAIL1 is set in Status.
        """

    @overload
    def Status(self, shape: nanoocp.TopoDS.TopoDS_Shape, newsh: nanoocp.TopoDS.TopoDS_Shape, last: bool = False) -> int:
        """
        Returns a complete substitution status for a shape
        0  : not recorded,   <newsh> = original <shape>
        < 0: to be removed,  <newsh> is NULL
        > 0: to be replaced, <newsh> is a new item
        If <last> is False, returns status and new shape recorded in
        the map directly for the shape, if True and status > 0 then
        recursively searches for the last status and new shape.
        """

    @overload
    def Status(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Queries the status of last call to Apply(shape,enum)
        OK   : no (sub)shapes replaced or removed
        DONE1: source (starting) shape replaced
        DONE2: source (starting) shape removed
        DONE3: some subshapes replaced
        DONE4: some subshapes removed
        FAIL1: some replacements not done because of bad type of subshape
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeBuild_Vertex:
    """Provides low-level functions used for constructing vertices"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeBuild_Vertex) -> None: ...

    @overload
    def CombineVertex(self, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, tolFactor: float = 1.0001) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Combines new vertex from two others. This new one is the
        smallest vertex which comprises both of the source vertices.
        The function takes into account the positions and tolerances
        of the source vertices.
        The tolerance of the new vertex will be equal to the minimal
        tolerance that is required to comprise source vertices
        multiplied by tolFactor (in order to avoid errors because
        of discreteness of calculations).
        """

    @overload
    def CombineVertex(self, pnt1: nanoocp.gp.gp_Pnt, pnt2: nanoocp.gp.gp_Pnt, tol1: float, tol2: float, tolFactor: float = 1.0001) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        The same function as above, except that it accepts two points
        and two tolerances instead of vertices
        """
