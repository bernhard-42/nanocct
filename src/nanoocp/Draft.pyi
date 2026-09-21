"""OCCT package Draft (toolkit TKOffset)"""

import enum
from typing import overload

import nanoocp.BRepTools
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.gp


class Draft_ErrorStatus(enum.IntEnum):
    Draft_NoError = 0

    Draft_FaceRecomputation = 1

    Draft_EdgeRecomputation = 2

    Draft_VertexRecomputation = 3

Draft_NoError: Draft_ErrorStatus = Draft_ErrorStatus.Draft_NoError

Draft_FaceRecomputation: Draft_ErrorStatus = Draft_ErrorStatus.Draft_FaceRecomputation

Draft_EdgeRecomputation: Draft_ErrorStatus = Draft_ErrorStatus.Draft_EdgeRecomputation

Draft_VertexRecomputation: Draft_ErrorStatus = Draft_ErrorStatus.Draft_VertexRecomputation

class Draft:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Draft) -> None: ...

    @staticmethod
    def Angle(F: nanoocp.TopoDS.TopoDS_Face, Direction: nanoocp.gp.gp_Dir) -> float:
        """
        Returns the draft angle of the face <F> using the
        direction <Direction>. The method is valid for :
        - Plane faces,
        - Cylindrical or conical faces, when the direction
        of the axis of the surface is colinear with the
        direction.
        Otherwise, the exception DomainError is raised.
        """

class Draft_EdgeInfo:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, HasNewGeometry: bool) -> None: ...

    @overload
    def __init__(self, theOther: Draft_EdgeInfo) -> None: ...

    def Add(self, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def RootFace(self, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def RootFace(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def Tangent(self, P: nanoocp.gp.gp_Pnt) -> None: ...

    def IsTangent(self, P: nanoocp.gp.gp_Pnt) -> bool: ...

    def NewGeometry(self) -> bool: ...

    def SetNewGeometry(self, NewGeom: bool) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_Curve: ...

    def FirstFace(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def SecondFace(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def FirstPC(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def SecondPC(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def ChangeGeometry(self) -> nanoocp.Geom.Geom_Curve: ...

    def ChangeFirstPC(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def ChangeSecondPC(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    @overload
    def Tolerance(self, tol: float) -> None: ...

    @overload
    def Tolerance(self) -> float: ...

class Draft_FaceInfo:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_Surface | None, HasNewGeometry: bool) -> None: ...

    @overload
    def __init__(self, theOther: Draft_FaceInfo) -> None: ...

    @overload
    def RootFace(self, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def RootFace(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def NewGeometry(self) -> bool: ...

    def Add(self, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def FirstFace(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def SecondFace(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def Geometry(self) -> nanoocp.Geom.Geom_Surface: ...

    def ChangeGeometry(self) -> nanoocp.Geom.Geom_Surface: ...

    def ChangeCurve(self) -> nanoocp.Geom.Geom_Curve: ...

    def Curve(self) -> nanoocp.Geom.Geom_Curve: ...

class Draft_VertexInfo:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Draft_VertexInfo) -> None: ...

    def Add(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    def Geometry(self) -> nanoocp.gp.gp_Pnt: ...

    def Parameter(self, E: nanoocp.TopoDS.TopoDS_Edge) -> float: ...

    def InitEdgeIterator(self) -> None: ...

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def NextEdge(self) -> None: ...

    def MoreEdge(self) -> bool: ...

    def ChangeGeometry(self) -> nanoocp.gp.gp_Pnt: ...

    def ChangeParameter(self, E: nanoocp.TopoDS.TopoDS_Edge) -> float: ...

    def SetParameter(self, E: nanoocp.TopoDS.TopoDS_Edge, theValue: float) -> None:
        """
        Python addition: sets the value ChangeParameter(E) returns by reference in C++.
        """

class Draft_Modification(nanoocp.BRepTools.BRepTools_Modification):
    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: Draft_Modification) -> None: ...

    def Clear(self) -> None:
        """Resets on the same shape."""

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Changes the basis shape and resets."""

    def Add(self, F: nanoocp.TopoDS.TopoDS_Face, Direction: nanoocp.gp.gp_Dir, Angle: float, NeutralPlane: nanoocp.gp.gp_Pln, Flag: bool = True) -> bool:
        """
        Adds the face F and propagates the draft
        modification to its neighbour faces if they are
        tangent. If an error occurs, will return False and
        ProblematicShape will return the "bad" face.
        """

    def Remove(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Removes the face F and the neighbour faces if they
        are tangent. It will be necessary to call this
        method if the method Add returns false,
        to unset ProblematicFace.
        """

    def Perform(self) -> None:
        """
        Performs the draft angle modification and sets the
        value returned by the method IsDone. If an error
        occurs, IsDone will return false, and an
        error status will be given by the method Error,
        and the shape on which the problem appeared will
        be given by ProblematicShape
        """

    def IsDone(self) -> bool:
        """
        Returns True if Perform has been successfully
        called. Otherwise more information can be obtained
        using the methods Error() and ProblematicShape().
        """

    def Error(self) -> Draft_ErrorStatus: ...

    def ProblematicShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the shape (Face, Edge or Vertex) on which
        an error occurred.
        """

    def ConnectedFaces(self, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns all the faces which have been added
        together with the face <F>.
        """

    def ModifiedFaces(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns all the faces on which a modification has
        been given.
        """

    def NewSurface(self, F: nanoocp.TopoDS.TopoDS_Face, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Surface, float, bool, bool]:
        """
        Returns true if the face <F> has been
        modified. In this case, <S> is the new geometric
        support of the face, <L> the new location, <Tol>
        the new tolerance.<RevWires> has to be set to
        true when the modification reverses the
        normal of the surface. (the wires have to be
        reversed). <RevFace> has to be set to
        true if the orientation of the modified
        face changes in the shells which contain it. Here
        it will be set to false.

        Otherwise, returns false, and <S>, <L>,
        <Tol> , <RevWires> ,<RevFace> are not significant.
        """

    def NewCurve(self, E: nanoocp.TopoDS.TopoDS_Edge, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Curve, float]:
        """
        Returns true if the edge <E> has been
        modified. In this case, <C> is the new geometric
        support of the edge, <L> the new location, <Tol>
        the new tolerance. Otherwise, returns
        false, and <C>, <L>, <Tol> are not
        significant.
        """

    def NewPoint(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """
        Returns true if the vertex <V> has been
        modified. In this case, <P> is the new geometric
        support of the vertex, <Tol> the new tolerance.
        Otherwise, returns false, and <P>, <Tol>
        are not significant.
        """

    def NewCurve2d(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Returns true if the edge <E> has a new
        curve on surface on the face <F>.In this case, <C>
        is the new geometric support of the edge, <L> the
        new location, <Tol> the new tolerance.

        Otherwise, returns false, and <C>, <L>,
        <Tol> are not significant.

        <NewE> is the new edge created from <E>. <NewF>
        is the new face created from <F>. They may be useful.
        """

    def NewParameter(self, V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]:
        """
        Returns true if the Vertex <V> has a new
        parameter on the edge <E>. In this case, <P> is
        the parameter, <Tol> the new tolerance.
        Otherwise, returns false, and <P>, <Tol>
        are not significant.
        """

    def Continuity(self, E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF1: nanoocp.TopoDS.TopoDS_Face, NewF2: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Returns the continuity of <NewE> between <NewF1>
        and <NewF2>.

        <NewE> is the new edge created from <E>. <NewF1>
        (resp. <NewF2>) is the new face created from <F1>
        (resp. <F2>).
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
