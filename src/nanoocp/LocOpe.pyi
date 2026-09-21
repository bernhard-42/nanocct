"""OCCT package LocOpe (toolkit TKFeat)"""

import enum
from typing import overload

import nanoocp.Geom
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp


class LocOpe_Operation(enum.IntEnum):
    LocOpe_FUSE = 0

    LocOpe_CUT = 1

    LocOpe_INVALID = 2

LocOpe_FUSE: LocOpe_Operation = LocOpe_Operation.LocOpe_FUSE

LocOpe_CUT: LocOpe_Operation = LocOpe_Operation.LocOpe_CUT

LocOpe_INVALID: LocOpe_Operation = LocOpe_Operation.LocOpe_INVALID

class LocOpe:
    """
    Provides tools to implement local topological
    operations on a shape.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LocOpe) -> None: ...

    @overload
    @staticmethod
    def Closed(W: nanoocp.TopoDS.TopoDS_Wire, OnF: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """
        Returns true when the wire <W> is closed
        on the face <OnF>.
        """

    @overload
    @staticmethod
    def Closed(E: nanoocp.TopoDS.TopoDS_Edge, OnF: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """
        Returns true when the edge <E> is closed
        on the face <OnF>.
        """

    @staticmethod
    def TgtFaces(E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """Returns true when the faces are tangent"""

    @staticmethod
    def SampleEdges(S: nanoocp.TopoDS.TopoDS_Shape, Pt: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt]) -> None: ...

class LocOpe_BuildShape:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Builds shape(s) from the list <L>. Uses only the
        faces of <L>.
        """

    @overload
    def __init__(self, theOther: LocOpe_BuildShape) -> None: ...

    def Perform(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Builds shape(s) from the list <L>. Uses only the
        faces of <L>.
        """

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

class LocOpe_BuildWires:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Ledges: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], PW: LocOpe_WiresOnShape | None) -> None: ...

    @overload
    def __init__(self, theOther: LocOpe_BuildWires) -> None: ...

    def Perform(self, Ledges: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], PW: LocOpe_WiresOnShape | None) -> None: ...

    def IsDone(self) -> bool: ...

    def Result(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

class LocOpe_CSIntersector:
    """
    This class provides the intersection between a set
    of axis or a circle and the faces of a shape. The
    intersection points are sorted in increasing
    parameter along each axis or circle.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Creates and performs the intersection between
        <Ax1> and <S>.
        """

    @overload
    def __init__(self, theOther: LocOpe_CSIntersector) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Performs the intersection between <Ax1 and <S>."""

    @overload
    def Perform(self, Slin: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Lin]) -> None: ...

    @overload
    def Perform(self, Scir: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Circ]) -> None: ...

    @overload
    def Perform(self, Scur: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]) -> None: ...

    def IsDone(self) -> bool:
        """
        Returns <true> if the intersection has
        been done.
        """

    def NbPoints(self, I: int) -> int:
        """
        Returns the number of intersection point on the
        element of range <I>.
        """

    def Point(self, I: int, Index: int) -> LocOpe_PntFace:
        """
        Returns the intersection point of range <Index> on
        element of range <I>. The points are sorted in
        increasing order of parameter along the axis.
        """

    @overload
    def LocalizeAfter(self, I: int, From: float, Tol: float) -> tuple[bool, nanoocp.TopAbs.TopAbs_Orientation, int, int]:
        """
        On the element of range <I>, searches the first
        intersection point located after the parameter
        <From>, which orientation is not TopAbs_EXTERNAL.
        If found, returns <true>. <Or> contains
        the orientation of the point, <IndFrom> and
        <IndTo> represents the interval of index in the
        sequence of intersection point corresponding to
        the point. (IndFrom <= IndTo). <Tol> is used to
        determine if 2 parameters are equal.

        Otherwise, returns <false>.
        """

    @overload
    def LocalizeAfter(self, I: int, FromInd: int, Tol: float) -> tuple[bool, nanoocp.TopAbs.TopAbs_Orientation, int, int]:
        """
        On the element of range <I>, searches the first
        intersection point located after the index
        <FromInd> ( >= FromInd + 1), which orientation is
        not TopAbs_EXTERNAL. If found, returns
        <true>. <Or> contains the orientation of
        the point, <IndFrom> and <IndTo> represents the
        interval of index in the sequence of intersection
        point corresponding to the point. (IndFrom <= IndTo).
        <Tol> is used to determine if 2 parameters are equal.

        Otherwise, returns <false>.
        """

    @overload
    def LocalizeBefore(self, I: int, From: float, Tol: float) -> tuple[bool, nanoocp.TopAbs.TopAbs_Orientation, int, int]:
        """
        On the element of range <I>, searches the first
        intersection point located before the parameter
        <From>, which orientation is not TopAbs_EXTERNAL.
        If found, returns <true>. <Or> contains
        the orientation of the point, <IndFrom> and
        <IndTo> represents the interval of index in the
        sequence of intersection point corresponding to
        the point (IndFrom <= IndTo). <Tol> is used to
        determine if 2 parameters are equal.

        Otherwise, returns <false>.
        """

    @overload
    def LocalizeBefore(self, I: int, FromInd: int, Tol: float) -> tuple[bool, nanoocp.TopAbs.TopAbs_Orientation, int, int]:
        """
        On the element of range <I>, searches the first
        intersection point located before the index
        <FromInd> (<= FromInd -1), which orientation is
        not TopAbs_EXTERNAL. If found, returns
        <true>. <Or> contains the orientation of
        the point, <IndFrom> and <IndTo> represents the
        interval of index in the sequence of intersection
        point corresponding to the point (IndFrom <= IndTo).
        <Tol> is used to determine if 2 parameters are equal.

        Otherwise, returns <false>.
        """

    def Destroy(self) -> None: ...

class LocOpe_PntFace:
    @overload
    def __init__(self) -> None:
        """Empty constructor. Useful only for the list."""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, F: nanoocp.TopoDS.TopoDS_Face, Or: nanoocp.TopAbs.TopAbs_Orientation, Param: float, UPar: float, VPar: float) -> None: ...

    @overload
    def __init__(self, theOther: LocOpe_PntFace) -> None: ...

    def Pnt(self) -> nanoocp.gp.gp_Pnt: ...

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def ChangeOrientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def SetOrientation(self, theValue: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Python addition: sets the value ChangeOrientation() returns by reference in C++.
        """

    def Parameter(self) -> float: ...

    def UParameter(self) -> float: ...

    def VParameter(self) -> float: ...

class LocOpe_CurveShapeIntersector:
    """
    This class provides the intersection between an
    axis or a circle and the faces of a shape. The
    intersection points are sorted in increasing
    parameter along the axis.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax1, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Creates and performs the intersection between
        <Ax1> and <S>.
        """

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Creates and performs the intersection between
        <C> and <S>.
        """

    @overload
    def __init__(self, theOther: LocOpe_CurveShapeIntersector) -> None: ...

    @overload
    def Init(self, Axis: nanoocp.gp.gp_Ax1, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Init(self, C: nanoocp.gp.gp_Circ, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Performs the intersection between <Ax1 and <S>."""

    def IsDone(self) -> bool:
        """
        Returns <true> if the intersection has
        been done.
        """

    def NbPoints(self) -> int:
        """Returns the number of intersection point."""

    def Point(self, Index: int) -> LocOpe_PntFace:
        """
        Returns the intersection point of range <Index>.
        The points are sorted in increasing order of
        parameter along the axis.
        """

    @overload
    def LocalizeAfter(self, From: float) -> tuple[bool, nanoocp.TopAbs.TopAbs_Orientation, int, int]:
        """
        Searches the first intersection point located
        after the parameter <From>, which orientation is
        not TopAbs_EXTERNAL. If found, returns
        <true>. <Or> contains the orientation of
        the point, <IndFrom> and <IndTo> represents the
        interval of index in the sequence of intersection
        point corresponding to the point. (IndFrom <= IndTo).

        Otherwise, returns <false>.
        """

    @overload
    def LocalizeAfter(self, FromInd: int) -> tuple[bool, nanoocp.TopAbs.TopAbs_Orientation, int, int]:
        """
        Searches the first intersection point located
        after the index <FromInd> (>= FromInd + 1), which
        orientation is not TopAbs_EXTERNAL. If found,
        returns <true>. <Or> contains the
        orientation of the point, <IndFrom> and <IndTo>
        represents the interval of index in the sequence
        of intersection point corresponding to the point.
        (IndFrom <= IndTo).

        Otherwise, returns <false>.
        """

    @overload
    def LocalizeBefore(self, From: float) -> tuple[bool, nanoocp.TopAbs.TopAbs_Orientation, int, int]:
        """
        Searches the first intersection point located
        before the parameter <From>, which orientation is
        not TopAbs_EXTERNAL. If found, returns
        <true>. <Or> contains the orientation of
        the point, <IndFrom> and <IndTo> represents the
        interval of index in the sequence of intersection
        point corresponding to the point (IndFrom <= IndTo).

        Otherwise, returns <false>.
        """

    @overload
    def LocalizeBefore(self, FromInd: int) -> tuple[bool, nanoocp.TopAbs.TopAbs_Orientation, int, int]:
        """
        Searches the first intersection point located
        before the index <FromInd> ( <= FromInd -1), which
        orientation is not TopAbs_EXTERNAL. If found,
        returns <true>. <Or> contains the
        orientation of the point, <IndFrom> and <IndTo>
        represents the interval of index in the sequence
        of intersection point corresponding to the point
        (IndFrom <= IndTo).

        Otherwise, returns <false>.
        """

class LocOpe_DPrism:
    """
    Defines a pipe (near from Pipe from BRepFill),
    with modifications provided for the Pipe feature.
    """

    @overload
    def __init__(self, Spine: nanoocp.TopoDS.TopoDS_Face, Height: float, Angle: float) -> None: ...

    @overload
    def __init__(self, Spine: nanoocp.TopoDS.TopoDS_Face, Height1: float, Height2: float, Angle: float) -> None: ...

    @overload
    def __init__(self, theOther: LocOpe_DPrism) -> None: ...

    def IsDone(self) -> bool: ...

    def Spine(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Profile(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shapes(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def Curves(self, SCurves: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]) -> None: ...

    def BarycCurve(self) -> nanoocp.Geom.Geom_Curve: ...

class LocOpe_FindEdges:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, FFrom: nanoocp.TopoDS.TopoDS_Shape, FTo: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: LocOpe_FindEdges) -> None: ...

    def Set(self, FFrom: nanoocp.TopoDS.TopoDS_Shape, FTo: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def InitIterator(self) -> None: ...

    def More(self) -> bool: ...

    def EdgeFrom(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def EdgeTo(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def Next(self) -> None: ...

class LocOpe_FindEdgesInFace:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def __init__(self, theOther: LocOpe_FindEdgesInFace) -> None: ...

    def Set(self, S: nanoocp.TopoDS.TopoDS_Shape, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def Init(self) -> None: ...

    def More(self) -> bool: ...

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def Next(self) -> None: ...

class LocOpe_GeneratedShape(nanoocp.Standard.Standard_Transient):
    def GeneratingEdges(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    @overload
    def Generated(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the edge created by the vertex <V>. If
        none, must return a null shape.
        """

    @overload
    def Generated(self, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns the face created by the edge <E>. If none,
        must return a null shape.
        """

    def OrientedFaces(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of correctly oriented generated
        faces.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class LocOpe_Generator:
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Creates the algorithm on the shape <S>."""

    @overload
    def __init__(self, theOther: LocOpe_Generator) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initializes the algorithm on the shape <S>."""

    def Perform(self, G: LocOpe_GeneratedShape | None) -> None: ...

    def IsDone(self) -> bool: ...

    def ResultingShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the new shape"""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the initial shape"""

    def DescendantFace(self, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the descendant face of <F>. <F> may
        belong to the original shape or to the "generated"
        shape. The returned face may be a null shape
        (when <F> disappears).
        """

class LocOpe_GluedShape(LocOpe_GeneratedShape):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: LocOpe_GluedShape) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def GlueOnFace(self, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def GeneratingEdges(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    @overload
    def Generated(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the edge created by the vertex <V>. If
        none, must return a null shape.
        """

    @overload
    def Generated(self, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns the face created by the edge <E>. If none,
        must return a null shape.
        """

    def OrientedFaces(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of correctly oriented generated
        faces.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class LocOpe_Gluer:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Sbase: nanoocp.TopoDS.TopoDS_Shape, Snew: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: LocOpe_Gluer) -> None: ...

    def Init(self, Sbase: nanoocp.TopoDS.TopoDS_Shape, Snew: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Bind(self, Fnew: nanoocp.TopoDS.TopoDS_Face, Fbase: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def Bind(self, Enew: nanoocp.TopoDS.TopoDS_Edge, Ebase: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    def OpeType(self) -> LocOpe_Operation: ...

    def Perform(self) -> None: ...

    def IsDone(self) -> bool: ...

    def ResultingShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def DescendantFaces(self, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def BasisShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def GluedShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Edges(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def TgtEdges(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

class LocOpe_LinearForm:
    """
    Defines a linear form (using Prism from BRepSweep)
    with modifications provided for the LinearForm feature.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Base: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.gp.gp_Vec, Pnt1: nanoocp.gp.gp_Pnt, Pnt2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, Base: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.gp.gp_Vec, Vectra: nanoocp.gp.gp_Vec, Pnt1: nanoocp.gp.gp_Pnt, Pnt2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, theOther: LocOpe_LinearForm) -> None: ...

    @overload
    def Perform(self, Base: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.gp.gp_Vec, Pnt1: nanoocp.gp.gp_Pnt, Pnt2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Perform(self, Base: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.gp.gp_Vec, Vectra: nanoocp.gp.gp_Vec, Pnt1: nanoocp.gp.gp_Pnt, Pnt2: nanoocp.gp.gp_Pnt) -> None: ...

    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shapes(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

class LocOpe_Pipe:
    """
    Defines a pipe (near from Pipe from BRepFill),
    with modifications provided for the Pipe feature.
    """

    @overload
    def __init__(self, Spine: nanoocp.TopoDS.TopoDS_Wire, Profile: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: LocOpe_Pipe) -> None: ...

    def Spine(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Profile(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shapes(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def Curves(self, Spt: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt]) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]: ...

    def BarycCurve(self) -> nanoocp.Geom.Geom_Curve: ...

class LocOpe_Prism:
    """
    Defines a prism (using Prism from BRepSweep)
    with modifications provided for the Prism feature.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Base: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def __init__(self, Base: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.gp.gp_Vec, Vectra: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def __init__(self, theOther: LocOpe_Prism) -> None: ...

    @overload
    def Perform(self, Base: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def Perform(self, Base: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.gp.gp_Vec, Vtra: nanoocp.gp.gp_Vec) -> None: ...

    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shapes(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def Curves(self, SCurves: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]) -> None: ...

    def BarycCurve(self) -> nanoocp.Geom.Geom_Curve: ...

class LocOpe_Revol:
    """
    Defines a prism (using Prism from BRepSweep)
    with modifications provided for the Prism feature.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LocOpe_Revol) -> None: ...

    @overload
    def Perform(self, Base: nanoocp.TopoDS.TopoDS_Shape, Axis: nanoocp.gp.gp_Ax1, Angle: float, angledec: float) -> None: ...

    @overload
    def Perform(self, Base: nanoocp.TopoDS.TopoDS_Shape, Axis: nanoocp.gp.gp_Ax1, Angle: float) -> None: ...

    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shapes(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def Curves(self, SCurves: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]) -> None: ...

    def BarycCurve(self) -> nanoocp.Geom.Geom_Curve: ...

class LocOpe_RevolutionForm:
    """
    Defines a revolution form (using Revol from BRepSweep)
    with modifications provided for the RevolutionForm feature.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LocOpe_RevolutionForm) -> None: ...

    def Perform(self, Base: nanoocp.TopoDS.TopoDS_Shape, Axe: nanoocp.gp.gp_Ax1, Angle: float) -> None: ...

    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shapes(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

class LocOpe_SplitDrafts:
    """
    This class provides a tool to realize the
    following operations on a shape:
    - split a face of the shape with a wire,
    - put draft angle on both side of the wire.
    For each side, the draft angle may be different.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Creates the algorithm on the shape <S>."""

    @overload
    def __init__(self, theOther: LocOpe_SplitDrafts) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initializes the algorithm with the shape <S>."""

    @overload
    def Perform(self, F: nanoocp.TopoDS.TopoDS_Face, W: nanoocp.TopoDS.TopoDS_Wire, Extractg: nanoocp.gp.gp_Dir, NPlg: nanoocp.gp.gp_Pln, Angleg: float, Extractd: nanoocp.gp.gp_Dir, NPld: nanoocp.gp.gp_Pln, Angled: float, ModifyLeft: bool = True, ModifyRight: bool = True) -> None:
        """
        Splits the face <F> of the former given shape with
        the wire <W>. The wire is assumed to lie on the
        face. Puts a draft angle on both parts of the
        wire. <Extractg>, <Nplg>, <Angleg> define the
        arguments for the left part of the wire.
        <Extractd>, <Npld>, <Angled> define the arguments
        for the right part of the wire. The draft angle is
        measured with the direction <Extract>. <Npl>
        defines the neutral plane (points belonging to the
        neutral plane are not modified). <Angle> is the
        value of the draft angle. If <ModifyLeft> is set
        to <false>, no draft angle is applied to
        the left part of the wire. If <ModifyRight> is set
        to <false>,no draft angle is applied to
        the right part of the wire.
        """

    @overload
    def Perform(self, F: nanoocp.TopoDS.TopoDS_Face, W: nanoocp.TopoDS.TopoDS_Wire, Extract: nanoocp.gp.gp_Dir, NPl: nanoocp.gp.gp_Pln, Angle: float) -> None:
        """
        Splits the face <F> of the former given shape with
        the wire <W>. The wire is assumed to lie on the
        face. Puts a draft angle on the left part of the
        wire. The draft angle is measured with the
        direction <Extract>. <Npl> defines the neutral
        plane (points belonging to the neutral plane are
        not modified). <Angle> is the value of the draft
        angle.
        """

    def IsDone(self) -> bool:
        """Returns <true> if the modification has been successfully performed."""

    def OriginalShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the modified shape."""

    def ShapesFromShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Manages the descendant shapes."""

class LocOpe_Spliter:
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Creates the algorithm on the shape <S>."""

    @overload
    def __init__(self, theOther: LocOpe_Spliter) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initializes the algorithm on the shape <S>."""

    def Perform(self, PW: LocOpe_WiresOnShape | None) -> None: ...

    def IsDone(self) -> bool: ...

    def ResultingShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the new shape"""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the initial shape"""

    def DirectLeft(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the faces which are the left of the
        projected wires and which are
        """

    def Left(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the faces of the "left" part on the shape.
        (It is build from DirectLeft, with the faces
        connected to this set, and so on...).
        """

    def DescendantShapes(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of descendant shapes of <S>."""

class LocOpe_SplitShape:
    """
    Provides a tool to cut:
    - edges with a vertices,
    - faces with wires,
    and rebuilds the shape containing the edges and
    the faces.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Creates the process with the shape <S>."""

    @overload
    def __init__(self, theOther: LocOpe_SplitShape) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initializes the process on the shape <S>."""

    def CanSplit(self, E: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """Tests if it is possible to split the edge <E>."""

    @overload
    def Add(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: float, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Adds the vertex <V> on the edge <E>, at parameter <P>."""

    @overload
    def Add(self, W: nanoocp.TopoDS.TopoDS_Wire, F: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """Adds the wire <W> on the face <F>."""

    @overload
    def Add(self, Lwires: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], F: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """Adds the list of wires <Lwires> on the face <F>."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the "original" shape."""

    def DescendantShapes(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of descendant shapes of <S>."""

    def LeftOf(self, W: nanoocp.TopoDS.TopoDS_Wire, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the "left" part defined by the wire <W> on
        the face <F>. The returned list of shape is in
        fact a list of faces. The face <F> is considered
        with its topological orientation in the original
        shape. <W> is considered with its orientation.
        """

class LocOpe_WiresOnShape(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: LocOpe_WiresOnShape) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Add(self, theEdges: nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        Add splitting edges or wires for whole initial shape
        without additional specification edge->face, edge->edge
        This method puts edge on the corresponding faces from initial shape
        """

    def SetCheckInterior(self, ToCheckInterior: bool) -> None:
        """
        Set the flag of check internal intersections
        default value is True (to check)
        """

    @overload
    def Bind(self, W: nanoocp.TopoDS.TopoDS_Wire, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def Bind(self, Comp: nanoocp.TopoDS.TopoDS_Compound, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def Bind(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def Bind(self, EfromW: nanoocp.TopoDS.TopoDS_Edge, EonFace: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    def BindAll(self) -> None: ...

    def IsDone(self) -> bool: ...

    def InitEdgeIterator(self) -> None: ...

    def MoreEdge(self) -> bool: ...

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def OnFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns the face of the shape on which the current
        edge is projected.
        """

    @overload
    def OnEdge(self, E: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """
        If the current edge is projected on an edge,
        returns <true> and sets the value of <E>.
        Otherwise, returns <false>.
        """

    @overload
    def OnEdge(self, V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float]: ...

    @overload
    def OnEdge(self, V: nanoocp.TopoDS.TopoDS_Vertex, EdgeFrom: nanoocp.TopoDS.TopoDS_Edge, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float]:
        """
        If the vertex <V> lies on an edge of the original
        shape, returns <true> and sets the
        concerned edge in <E>, and the parameter on the
        edge in <P>.
        Else returns <false>.
        """

    def NextEdge(self) -> None: ...

    def OnVertex(self, Vwire: nanoocp.TopoDS.TopoDS_Vertex, Vshape: nanoocp.TopoDS.TopoDS_Vertex) -> bool: ...

    def IsFaceWithSection(self, aFace: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """tells is the face to be split by section or not"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
LocOpe_SequenceOfCirc = nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Circ]
LocOpe_SequenceOfLin = nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Lin]
