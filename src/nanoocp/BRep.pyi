"""OCCT package BRep (toolkit TKBRep)"""

from typing import overload

import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.gp


class BRep_Builder(nanoocp.TopoDS.TopoDS_Builder):
    """
    A framework providing advanced tolerance control.
    It is used to build Shapes.
    If tolerance control is required, you are advised to:
    1. build a default precision for topology, using the
    classes provided in the BRepAPI package
    2. update the tolerance of the resulting shape.
    Note that only vertices, edges and faces have
    meaningful tolerance control. The tolerance value
    must always comply with the condition that face
    tolerances are more restrictive than edge tolerances
    which are more restrictive than vertex tolerances. In
    other words: Tol(Vertex) >= Tol(Edge) >= Tol(Face).
    Other rules in setting tolerance include:
    - you can open up tolerance but should never restrict it
    - an edge cannot be included within the fusion of the
    tolerance spheres of two vertices
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRep_Builder) -> None: ...

    @overload
    def MakeFace(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Makes an undefined Face."""

    @overload
    def MakeFace(self, F: nanoocp.TopoDS.TopoDS_Face, S: nanoocp.Geom.Geom_Surface, Tol: float) -> None:
        """Makes a Face with a surface."""

    @overload
    def MakeFace(self, F: nanoocp.TopoDS.TopoDS_Face, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location, Tol: float) -> None:
        """Makes a Face with a surface and a location."""

    @overload
    def MakeFace(self, theFace: nanoocp.TopoDS.TopoDS_Face, theTriangulation: nanoocp.Poly.Poly_Triangulation) -> None:
        """
        Makes a theFace with a single triangulation. The triangulation
        is in the same reference system than the TFace.
        """

    @overload
    def MakeFace(self, theFace: nanoocp.TopoDS.TopoDS_Face, theTriangulations: nanoocp.NCollection.NCollection_List[nanoocp.Poly.Poly_Triangulation], theActiveTriangulation: nanoocp.Poly.Poly_Triangulation = None) -> None:
        """
        Makes a Face with a list of triangulations and active one.
        Use NULL active triangulation to set the first triangulation in list as active.
        The triangulations is in the same reference system than the TFace.
        """

    @overload
    def UpdateFace(self, F: nanoocp.TopoDS.TopoDS_Face, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location, Tol: float) -> None:
        """
        Updates the face F using the tolerance value Tol,
        surface S and location Location.
        """

    @overload
    def UpdateFace(self, theFace: nanoocp.TopoDS.TopoDS_Face, theTriangulation: nanoocp.Poly.Poly_Triangulation, theToReset: bool = True) -> None:
        """
        Changes a face triangulation.
        A NULL theTriangulation removes face triangulations.
        If theToReset is TRUE face triangulations will be reset to new list with only one input
        triangulation that will be active. Else if theTriangulation is contained in internal
        triangulations list it will be made active,
        else the active triangulation will be replaced to theTriangulation one.
        """

    @overload
    def UpdateFace(self, F: nanoocp.TopoDS.TopoDS_Face, Tol: float) -> None:
        """Updates the face Tolerance."""

    def NaturalRestriction(self, F: nanoocp.TopoDS.TopoDS_Face, N: bool) -> None:
        """Sets the NaturalRestriction flag of the face."""

    @overload
    def MakeEdge(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Makes an undefined Edge (no geometry)."""

    @overload
    def MakeEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, C: nanoocp.Geom.Geom_Curve, Tol: float) -> None:
        """Makes an Edge with a curve."""

    @overload
    def MakeEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, C: nanoocp.Geom.Geom_Curve, L: nanoocp.TopLoc.TopLoc_Location, Tol: float) -> None:
        """Makes an Edge with a curve and a location."""

    @overload
    def MakeEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, P: nanoocp.Poly.Poly_Polygon3D) -> None:
        """Makes an Edge with a polygon 3d."""

    @overload
    def MakeEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, N: nanoocp.Poly.Poly_PolygonOnTriangulation, T: nanoocp.Poly.Poly_Triangulation) -> None: ...

    @overload
    def MakeEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, N: nanoocp.Poly.Poly_PolygonOnTriangulation, T: nanoocp.Poly.Poly_Triangulation, L: nanoocp.TopLoc.TopLoc_Location) -> None:
        """makes an Edge polygon on Triangulation."""

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, C: nanoocp.Geom.Geom_Curve, Tol: float) -> None: ...

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, C: nanoocp.Geom.Geom_Curve, L: nanoocp.TopLoc.TopLoc_Location, Tol: float) -> None:
        """
        Sets a 3D curve for the edge.
        If <C> is a null handle, remove any existing 3d curve.
        """

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, C: nanoocp.Geom2d.Geom2d_Curve, F: nanoocp.TopoDS.TopoDS_Face, Tol: float) -> None: ...

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, C1: nanoocp.Geom2d.Geom2d_Curve, C2: nanoocp.Geom2d.Geom2d_Curve, F: nanoocp.TopoDS.TopoDS_Face, Tol: float) -> None:
        """
        Sets pcurves for the edge on the closed face. If
        <C1> or <C2> is a null handle, remove any existing
        pcurve.
        """

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, C: nanoocp.Geom2d.Geom2d_Curve, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location, Tol: float) -> None:
        """
        Sets a pcurve for the edge on the face.
        If <C> is a null handle, remove any existing pcurve.
        """

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, C: nanoocp.Geom2d.Geom2d_Curve, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location, Tol: float, Pf: nanoocp.gp.gp_Pnt2d, Pl: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Sets a pcurve for the edge on the face.
        If <C> is a null handle, remove any existing pcurve.
        Sets UV bounds for curve repsentation
        """

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, C1: nanoocp.Geom2d.Geom2d_Curve, C2: nanoocp.Geom2d.Geom2d_Curve, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location, Tol: float) -> None:
        """
        Sets pcurves for the edge on the closed surface.
        <C1> or <C2> is a null handle, remove any existing
        pcurve.
        """

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, C1: nanoocp.Geom2d.Geom2d_Curve, C2: nanoocp.Geom2d.Geom2d_Curve, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location, Tol: float, Pf: nanoocp.gp.gp_Pnt2d, Pl: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Sets pcurves for the edge on the closed surface.
        <C1> or <C2> is a null handle, remove any existing
        pcurve.
        Sets UV bounds for curve repsentation
        """

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, P: nanoocp.Poly.Poly_Polygon3D) -> None: ...

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, P: nanoocp.Poly.Poly_Polygon3D, L: nanoocp.TopLoc.TopLoc_Location) -> None:
        """
        Changes an Edge 3D polygon.
        A null Polygon removes the 3d Polygon.
        """

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, N: nanoocp.Poly.Poly_PolygonOnTriangulation, T: nanoocp.Poly.Poly_Triangulation) -> None: ...

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, N: nanoocp.Poly.Poly_PolygonOnTriangulation, T: nanoocp.Poly.Poly_Triangulation, L: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, N1: nanoocp.Poly.Poly_PolygonOnTriangulation, N2: nanoocp.Poly.Poly_PolygonOnTriangulation, T: nanoocp.Poly.Poly_Triangulation) -> None: ...

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, N1: nanoocp.Poly.Poly_PolygonOnTriangulation, N2: nanoocp.Poly.Poly_PolygonOnTriangulation, T: nanoocp.Poly.Poly_Triangulation, L: nanoocp.TopLoc.TopLoc_Location) -> None:
        """Changes an Edge polygon on Triangulation."""

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, P: nanoocp.Poly.Poly_Polygon2D, S: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, P: nanoocp.Poly.Poly_Polygon2D, S: nanoocp.Geom.Geom_Surface, T: nanoocp.TopLoc.TopLoc_Location) -> None:
        """Changes Edge polygon on a face."""

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, P1: nanoocp.Poly.Poly_Polygon2D, P2: nanoocp.Poly.Poly_Polygon2D, S: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, P1: nanoocp.Poly.Poly_Polygon2D, P2: nanoocp.Poly.Poly_Polygon2D, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> None:
        """
        Changes Edge polygons on a face.

        A null Polygon removes the 2d Polygon.
        """

    @overload
    def UpdateEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, Tol: float) -> None:
        """Updates the edge tolerance."""

    @overload
    def Continuity(self, E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, C: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    @overload
    def Continuity(self, E: nanoocp.TopoDS.TopoDS_Edge, S1: nanoocp.Geom.Geom_Surface, S2: nanoocp.Geom.Geom_Surface, L1: nanoocp.TopLoc.TopLoc_Location, L2: nanoocp.TopLoc.TopLoc_Location, C: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """Sets the geometric continuity on the edge."""

    def SameParameter(self, E: nanoocp.TopoDS.TopoDS_Edge, S: bool) -> None:
        """Sets the same parameter flag for the edge <E>."""

    def SameRange(self, E: nanoocp.TopoDS.TopoDS_Edge, S: bool) -> None:
        """Sets the same range flag for the edge <E>."""

    def Degenerated(self, E: nanoocp.TopoDS.TopoDS_Edge, D: bool) -> None:
        """Sets the degenerated flag for the edge <E>."""

    @overload
    def Range(self, E: nanoocp.TopoDS.TopoDS_Edge, First: float, Last: float, Only3d: bool = False) -> None:
        """
        Sets the range of the 3d curve if Only3d=TRUE,
        otherwise sets the range to all the representations
        """

    @overload
    def Range(self, E: nanoocp.TopoDS.TopoDS_Edge, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location, First: float, Last: float) -> None:
        """
        Sets the range of the edge on the pcurve on the
        surface.
        """

    @overload
    def Range(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, First: float, Last: float) -> None:
        """Sets the range of the edge on the pcurve on the face."""

    @overload
    def Transfert(self, Ein: nanoocp.TopoDS.TopoDS_Edge, Eout: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Add to <Eout> the geometric representations of <Ein>."""

    @overload
    def Transfert(self, Ein: nanoocp.TopoDS.TopoDS_Edge, Eout: nanoocp.TopoDS.TopoDS_Edge, Vin: nanoocp.TopoDS.TopoDS_Vertex, Vout: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        Transfert the parameters of Vin on Ein as the
        parameter of Vout on Eout.
        """

    @overload
    def MakeVertex(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """Makes an udefined vertex without geometry."""

    @overload
    def MakeVertex(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: nanoocp.gp.gp_Pnt, Tol: float) -> None:
        """Makes a vertex from a 3D point."""

    @overload
    def UpdateVertex(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: nanoocp.gp.gp_Pnt, Tol: float) -> None:
        """Sets a 3D point on the vertex."""

    @overload
    def UpdateVertex(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: float, E: nanoocp.TopoDS.TopoDS_Edge, Tol: float) -> None:
        """Sets the parameter for the vertex on the edge curves."""

    @overload
    def UpdateVertex(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: float, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, Tol: float) -> None:
        """
        Sets the parameter for the vertex on the edge
        pcurve on the face.
        """

    @overload
    def UpdateVertex(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: float, E: nanoocp.TopoDS.TopoDS_Edge, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location, Tol: float) -> None:
        """
        Sets the parameter for the vertex on the edge
        pcurve on the surface.
        """

    @overload
    def UpdateVertex(self, Ve: nanoocp.TopoDS.TopoDS_Vertex, U: float, V: float, F: nanoocp.TopoDS.TopoDS_Face, Tol: float) -> None:
        """Sets the parameters for the vertex on the face."""

    @overload
    def UpdateVertex(self, V: nanoocp.TopoDS.TopoDS_Vertex, Tol: float) -> None:
        """Updates the vertex tolerance."""

class BRep_TFace(nanoocp.TopoDS.TopoDS_TFace):
    """
    The Tface from BRep is based on the TFace from
    TopoDS. The TFace contains:

    * A surface, a tolerance and a Location.

    * A NaturalRestriction flag, when this flag is
    True the boundary of the face is known to be the
    parametric space (Umin, UMax, VMin, VMax).

    * An optional list of triangulations. If there are any
    triangulations the surface can be absent.

    The Location is used for the Surface.

    The triangulation is in the same reference system
    than the TFace. A point on mySurface must be
    transformed with myLocation, but not a point on
    the triangulation.

    The Surface may be shared by different TFaces but
    not the Triangulation, because the Triangulation
    may be modified by the edges.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty TFace."""

    @overload
    def __init__(self, theOther: BRep_TFace) -> None: ...

    @overload
    def Surface(self) -> nanoocp.Geom.Geom_Surface:
        """Returns face surface."""

    @overload
    def Surface(self, theSurface: nanoocp.Geom.Geom_Surface) -> None:
        """Sets surface for this face."""

    @overload
    def Location(self) -> nanoocp.TopLoc.TopLoc_Location:
        """Returns the face location."""

    @overload
    def Location(self, theLocation: nanoocp.TopLoc.TopLoc_Location) -> None:
        """Sets the location for this face."""

    @overload
    def Tolerance(self) -> float:
        """Returns the face tolerance."""

    @overload
    def Tolerance(self, theTolerance: float) -> None:
        """Sets the tolerance for this face."""

    @overload
    def NaturalRestriction(self) -> bool:
        """
        Returns TRUE if the boundary of this face is known to be the parametric space (Umin, UMax,
        VMin, VMax).
        """

    @overload
    def NaturalRestriction(self, theRestriction: bool) -> None:
        """
        Sets the flag that is TRUE if the boundary of this face is known to be the parametric space.
        """

    @overload
    def Triangulation(self, thePurpose: int = 0) -> nanoocp.Poly.Poly_Triangulation:
        """
        Returns the triangulation of this face according to the mesh purpose.
        @param[in] thePurpose a mesh purpose to find appropriate triangulation (NONE by default).
        @return an active triangulation in case of NONE purpose,
        the first triangulation appropriate for the input purpose,
        just the first triangulation if none matching other criteria and input purpose is
        AnyFallback or null handle if there is no any suitable triangulation.
        """

    @overload
    def Triangulation(self, theTriangulation: nanoocp.Poly.Poly_Triangulation, theToReset: bool = True) -> None:
        """
        Sets input triangulation for this face.
        @param[in] theTriangulation  triangulation to be set
        @param[in] theToReset  flag to reset triangulations list to new list with only one input
        triangulation. If theTriangulation is NULL internal list of triangulations will be cleared and
        active triangulation will be nullified. If theToReset is TRUE internal list of triangulations
        will be reset to new list with only one input triangulation that will be active. Else if input
        triangulation is contained in internal triangulations list it will be made active,
        else the active triangulation will be replaced to input one.
        """

    def EmptyCopy(self) -> nanoocp.TopoDS.TopoDS_TShape:
        """
        Returns a copy of the TShape with no sub-shapes.
        The new Face has no triangulation.
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @overload
    def Triangulations(self) -> nanoocp.NCollection.NCollection_List[nanoocp.Poly.Poly_Triangulation]:
        """Returns the list of available face triangulations."""

    @overload
    def Triangulations(self, theTriangulations: nanoocp.NCollection.NCollection_List[nanoocp.Poly.Poly_Triangulation], theActiveTriangulation: nanoocp.Poly.Poly_Triangulation) -> None:
        """
        Sets input list of triangulations and currently active triangulation for this face.
        If list is empty internal list of triangulations will be cleared and active triangulation will
        be nullified. Else this list will be saved and the input active triangulation be saved as
        active. Use NULL active triangulation to set the first triangulation in list as active. Note:
        the method throws exception if there is any NULL triangulation in input list or
        if this list doesn't contain input active triangulation.
        """

    def NbTriangulations(self) -> int:
        """Returns number of available face triangulations."""

    def ActiveTriangulation(self) -> nanoocp.Poly.Poly_Triangulation:
        """Returns current active triangulation."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_PointRepresentation(nanoocp.Standard.Standard_Transient):
    """
    Root class for the points representations.
    Contains a location and a parameter.
    """

    def __init__(self, theOther: BRep_PointRepresentation) -> None: ...

    @overload
    def IsPointOnCurve(self) -> bool:
        """A point on a 3d curve."""

    @overload
    def IsPointOnCurve(self, C: nanoocp.Geom.Geom_Curve, L: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """A point on the curve <C>."""

    @overload
    def IsPointOnCurveOnSurface(self) -> bool:
        """A point on a 2d curve on a surface."""

    @overload
    def IsPointOnCurveOnSurface(self, PC: nanoocp.Geom2d.Geom2d_Curve, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """A point on the 2d curve <PC> on the surface <S>."""

    @overload
    def IsPointOnSurface(self) -> bool:
        """A point on a surface."""

    @overload
    def IsPointOnSurface(self, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """A point on the surface <S>."""

    @overload
    def Location(self) -> nanoocp.TopLoc.TopLoc_Location: ...

    @overload
    def Location(self, L: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    @overload
    def Parameter(self) -> float: ...

    @overload
    def Parameter(self, P: float) -> None: ...

    @overload
    def Parameter2(self) -> float: ...

    @overload
    def Parameter2(self, P: float) -> None: ...

    @overload
    def Curve(self) -> nanoocp.Geom.Geom_Curve: ...

    @overload
    def Curve(self, C: nanoocp.Geom.Geom_Curve) -> None: ...

    @overload
    def PCurve(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    @overload
    def PCurve(self, C: nanoocp.Geom2d.Geom2d_Curve) -> None: ...

    @overload
    def Surface(self) -> nanoocp.Geom.Geom_Surface: ...

    @overload
    def Surface(self, S: nanoocp.Geom.Geom_Surface) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_TVertex(nanoocp.TopoDS.TopoDS_TVertex):
    """
    The TVertex from BRep inherits from the TVertex
    from TopoDS. It contains the geometric data.

    The TVertex contains a 3d point, location and a tolerance.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRep_TVertex) -> None: ...

    @overload
    def Tolerance(self) -> float: ...

    @overload
    def Tolerance(self, T: float) -> None: ...

    def UpdateTolerance(self, T: float) -> None:
        """
        Sets the tolerance to the max of <T> and the
        current tolerance.
        """

    @overload
    def Pnt(self) -> nanoocp.gp.gp_Pnt: ...

    @overload
    def Pnt(self, P: nanoocp.gp.gp_Pnt) -> None: ...

    def Points(self) -> nanoocp.NCollection.NCollection_List[nanoocp.BRep.BRep_PointRepresentation]: ...

    def ChangePoints(self) -> nanoocp.NCollection.NCollection_List[nanoocp.BRep.BRep_PointRepresentation]: ...

    def EmptyCopy(self) -> nanoocp.TopoDS.TopoDS_TShape:
        """Returns a copy of the TShape with no sub-shapes."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_Tool:
    """
    Provides class methods to access to the geometry
    of BRep shapes.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRep_Tool) -> None: ...

    @overload
    @staticmethod
    def IsClosed(S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        If S is Shell, returns True if it has no free boundaries (edges).
        If S is Wire, returns True if it has no free ends (vertices).
        (Internal and External sub-shepes are ignored in these checks)
        If S is Edge, returns True if its vertices are the same.
        For other shape types returns S.Closed().
        """

    @overload
    @staticmethod
    def IsClosed(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """
        Returns True if <E> has two PCurves in the
        parametric space of <F>. i.e. <F> is on a closed
        surface and <E> is on the closing curve.
        """

    @overload
    @staticmethod
    def IsClosed(E: nanoocp.TopoDS.TopoDS_Edge, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """
        Returns True if <E> has two PCurves in the
        parametric space of <S>. i.e. <S> is a closed
        surface and <E> is on the closing curve.
        """

    @overload
    @staticmethod
    def IsClosed(E: nanoocp.TopoDS.TopoDS_Edge, T: nanoocp.Poly.Poly_Triangulation, L: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """
        Returns True if <E> has two arrays of indices in
        the triangulation <T>.
        """

    @overload
    @staticmethod
    def Surface(F: nanoocp.TopoDS.TopoDS_Face, L: nanoocp.TopLoc.TopLoc_Location) -> nanoocp.Geom.Geom_Surface:
        """
        Returns the geometric surface of the face. Returns
        in <L> the location for the surface.
        """

    @overload
    @staticmethod
    def Surface(F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.Geom.Geom_Surface:
        """
        Returns the geometric  surface of the face. It can
        be a copy if there is a Location.
        """

    @staticmethod
    def Triangulation(theFace: nanoocp.TopoDS.TopoDS_Face, theLocation: nanoocp.TopLoc.TopLoc_Location, theMeshPurpose: int = 0) -> nanoocp.Poly.Poly_Triangulation:
        """
        Returns the triangulation of the face according to the mesh purpose.
        @param[in] theFace  the input face to find triangulation.
        @param[out] theLocation  the face location.
        @param[in] theMeshPurpose  a mesh purpose to find appropriate triangulation (NONE by default).
        @return an active triangulation in case of NONE purpose,
        the first triangulation appropriate for the input purpose,
        just the first triangulation if none matching other criteria and input purpose is
        AnyFallback or null handle if there is no any suitable triangulation.
        """

    @staticmethod
    def Triangulations(theFace: nanoocp.TopoDS.TopoDS_Face, theLocation: nanoocp.TopLoc.TopLoc_Location) -> nanoocp.NCollection.NCollection_List[nanoocp.Poly.Poly_Triangulation]:
        """
        Returns all triangulations of the face.
        @param[in] theFace  the input face.
        @param[out] theLocation  the face location.
        @return list of all available face triangulations.
        """

    @overload
    @staticmethod
    def Tolerance(F: nanoocp.TopoDS.TopoDS_Face) -> float:
        """Returns the tolerance of the face."""

    @overload
    @staticmethod
    def Tolerance(E: nanoocp.TopoDS.TopoDS_Edge) -> float:
        """Returns the tolerance for <E>."""

    @overload
    @staticmethod
    def Tolerance(V: nanoocp.TopoDS.TopoDS_Vertex) -> float:
        """Returns the tolerance."""

    @staticmethod
    def NaturalRestriction(F: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """Returns the NaturalRestriction flag of the face."""

    @overload
    @staticmethod
    def IsGeometric(F: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """Returns True if <F> has a surface, false otherwise."""

    @overload
    @staticmethod
    def IsGeometric(E: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """Returns True if <E> is a 3d curve or a curve on surface."""

    @overload
    @staticmethod
    def Curve(E: nanoocp.TopoDS.TopoDS_Edge, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[nanoocp.Geom.Geom_Curve, float, float]:
        """
        Returns the 3D curve of the edge. May be a Null
        handle. Returns in <L> the location for the curve.
        In <First> and <Last> the parameter range.
        """

    @overload
    @staticmethod
    def Curve(E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[nanoocp.Geom.Geom_Curve, float, float]:
        """
        Returns the 3D curve of the edge. May be a Null handle.
        In <First> and <Last> the parameter range.
        It can be a copy if there is a Location.
        """

    @staticmethod
    def Polygon3D(E: nanoocp.TopoDS.TopoDS_Edge, L: nanoocp.TopLoc.TopLoc_Location) -> nanoocp.Poly.Poly_Polygon3D:
        """
        Returns the 3D polygon of the edge. May be a Null
        handle. Returns in <L> the location for the polygon.
        """

    @staticmethod
    def CurveOnPlane(E: nanoocp.TopoDS.TopoDS_Edge, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[nanoocp.Geom2d.Geom2d_Curve, float, float]:
        """
        For the planar surface builds the 2d curve for the edge
        by projection of the edge on plane.
        Returns a NULL handle if the surface is not planar or
        the projection failed.
        """

    @overload
    @staticmethod
    def CurveOnSurface(E: nanoocp.TopoDS.TopoDS_Edge, C: nanoocp.Geom2d.Geom2d_Curve, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[float, float]:
        """
        Returns in <C>, <S>, <L> a 2d curve, a surface and
        a location for the edge <E>. <C> and <S> are null
        if the edge has no curve on surface. Returns in
        <First> and <Last> the parameter range.
        """

    @overload
    @staticmethod
    def CurveOnSurface(E: nanoocp.TopoDS.TopoDS_Edge, C: nanoocp.Geom2d.Geom2d_Curve, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location, Index: int) -> tuple[float, float]:
        """
        Returns in <C>, <S>, <L> the 2d curve, the surface
        and the location for the edge <E> of rank <Index>.
        <C> and <S> are null if the index is out of range.
        Returns in <First> and <Last> the parameter range.
        """

    @overload
    @staticmethod
    def PolygonOnSurface(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.Poly.Poly_Polygon2D:
        """
        Returns the polygon associated to the edge in the
        parametric space of the face. Returns a NULL
        handle if this polygon does not exist.
        """

    @overload
    @staticmethod
    def PolygonOnSurface(E: nanoocp.TopoDS.TopoDS_Edge, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> nanoocp.Poly.Poly_Polygon2D:
        """
        Returns the polygon associated to the edge in the
        parametric space of the surface. Returns a NULL
        handle if this polygon does not exist.
        """

    @overload
    @staticmethod
    def PolygonOnSurface(E: nanoocp.TopoDS.TopoDS_Edge, C: nanoocp.Poly.Poly_Polygon2D, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> None:
        """
        Returns in <C>, <S>, <L> a 2d curve, a surface and
        a location for the edge <E>. <C> and <S> are null
        if the edge has no polygon on surface.
        """

    @overload
    @staticmethod
    def PolygonOnSurface(E: nanoocp.TopoDS.TopoDS_Edge, C: nanoocp.Poly.Poly_Polygon2D, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location, Index: int) -> None:
        """
        Returns in <C>, <S>, <L> the 2d curve, the surface
        and the location for the edge <E> of rank <Index>.
        <C> and <S> are null if the index is out of range.
        """

    @overload
    @staticmethod
    def PolygonOnTriangulation(E: nanoocp.TopoDS.TopoDS_Edge, T: nanoocp.Poly.Poly_Triangulation, L: nanoocp.TopLoc.TopLoc_Location) -> nanoocp.Poly.Poly_PolygonOnTriangulation:
        """
        Returns the polygon associated to the edge in the
        parametric space of the face. Returns a NULL
        handle if this polygon does not exist.
        """

    @overload
    @staticmethod
    def PolygonOnTriangulation(E: nanoocp.TopoDS.TopoDS_Edge, P: nanoocp.Poly.Poly_PolygonOnTriangulation, T: nanoocp.Poly.Poly_Triangulation, L: nanoocp.TopLoc.TopLoc_Location) -> None:
        """
        Returns in <P>, <T>, <L> a polygon on triangulation, a
        triangulation and a location for the edge <E>.
        <P> and <T> are null if the edge has no
        polygon on triangulation.
        """

    @overload
    @staticmethod
    def PolygonOnTriangulation(E: nanoocp.TopoDS.TopoDS_Edge, P: nanoocp.Poly.Poly_PolygonOnTriangulation, T: nanoocp.Poly.Poly_Triangulation, L: nanoocp.TopLoc.TopLoc_Location, Index: int) -> None:
        """
        Returns in <P>, <T>, <L> a polygon on
        triangulation, a triangulation and a location for
        the edge <E> for the range index. <C> and <S> are
        null if the edge has no polygon on triangulation.
        """

    @staticmethod
    def SameParameter(E: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """Returns the SameParameter flag for the edge."""

    @staticmethod
    def SameRange(E: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """Returns the SameRange flag for the edge."""

    @staticmethod
    def Degenerated(E: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """Returns True if the edge is degenerated."""

    @overload
    @staticmethod
    def Range(E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[float, float]:
        """Gets the range of the 3d curve."""

    @overload
    @staticmethod
    def Range(E: nanoocp.TopoDS.TopoDS_Edge, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[float, float]:
        """Gets the range of the edge on the pcurve on the surface."""

    @overload
    @staticmethod
    def Range(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[float, float]:
        """Gets the range of the edge on the pcurve on the face."""

    @overload
    @staticmethod
    def UVPoints(E: nanoocp.TopoDS.TopoDS_Edge, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location, PFirst: nanoocp.gp.gp_Pnt2d, PLast: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    @staticmethod
    def UVPoints(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, PFirst: nanoocp.gp.gp_Pnt2d, PLast: nanoocp.gp.gp_Pnt2d) -> None:
        """Gets the UV locations of the extremities of the edge."""

    @overload
    @staticmethod
    def SetUVPoints(E: nanoocp.TopoDS.TopoDS_Edge, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location, PFirst: nanoocp.gp.gp_Pnt2d, PLast: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    @staticmethod
    def SetUVPoints(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, PFirst: nanoocp.gp.gp_Pnt2d, PLast: nanoocp.gp.gp_Pnt2d) -> None:
        """Sets the UV locations of the extremities of the edge."""

    @overload
    @staticmethod
    def HasContinuity(E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """
        Returns True if the edge is on the surfaces of the
        two faces.
        """

    @overload
    @staticmethod
    def HasContinuity(E: nanoocp.TopoDS.TopoDS_Edge, S1: nanoocp.Geom.Geom_Surface, S2: nanoocp.Geom.Geom_Surface, L1: nanoocp.TopLoc.TopLoc_Location, L2: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """Returns True if the edge is on the surfaces."""

    @overload
    @staticmethod
    def HasContinuity(E: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """Returns True if the edge has regularity on some two surfaces."""

    @overload
    @staticmethod
    def Continuity(E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    @overload
    @staticmethod
    def Continuity(E: nanoocp.TopoDS.TopoDS_Edge, S1: nanoocp.Geom.Geom_Surface, S2: nanoocp.Geom.Geom_Surface, L1: nanoocp.TopLoc.TopLoc_Location, L2: nanoocp.TopLoc.TopLoc_Location) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Returns the continuity."""

    @staticmethod
    def MaxContinuity(theEdge: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Returns the max continuity of edge between some surfaces or GeomAbs_C0
        if there are no such surfaces.
        """

    @staticmethod
    def Pnt(V: nanoocp.TopoDS.TopoDS_Vertex) -> nanoocp.gp.gp_Pnt:
        """Returns the 3d point."""

    @overload
    @staticmethod
    def Parameter(V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> float:
        """
        Returns the parameter of <V> on <E>.
        Throws Standard_NoSuchObject if no parameter on edge
        """

    @overload
    @staticmethod
    def Parameter(theV: nanoocp.TopoDS.TopoDS_Vertex, theE: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float]:
        """
        Finds the parameter of <theV> on <theE>.
        @param[in] theV  input vertex
        @param[in] theE  input edge
        @param[out] theParam   calculated parameter on the curve
        @return TRUE if done
        """

    @overload
    @staticmethod
    def Parameter(V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> float:
        """
        Returns the parameters of the vertex on the
        pcurve of the edge on the face.
        """

    @overload
    @staticmethod
    def Parameter(V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> float:
        """
        Returns the parameters of the vertex on the
        pcurve of the edge on the surface.
        """

    @staticmethod
    def Parameters(V: nanoocp.TopoDS.TopoDS_Vertex, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.gp.gp_Pnt2d:
        """Returns the parameters of the vertex on the face."""

    @staticmethod
    def MaxTolerance(theShape: nanoocp.TopoDS.TopoDS_Shape, theSubShape: nanoocp.TopAbs.TopAbs_ShapeEnum) -> float: ...

class BRep_CurveRepresentation(nanoocp.Standard.Standard_Transient):
    """
    Root class for the curve representations. Contains
    a location.
    """

    def IsCurve3D(self) -> bool:
        """A 3D curve representation."""

    @overload
    def IsCurveOnSurface(self) -> bool:
        """A curve in the parametric space of a surface."""

    @overload
    def IsCurveOnSurface(self, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """
        Is it a curve in the parametric space of <S> with
        location <L>.
        """

    @overload
    def IsRegularity(self) -> bool:
        """A continuity between two surfaces."""

    @overload
    def IsRegularity(self, S1: nanoocp.Geom.Geom_Surface, S2: nanoocp.Geom.Geom_Surface, L1: nanoocp.TopLoc.TopLoc_Location, L2: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """
        Is it a regularity between <S1> and <S2> with
        location <L1> and <L2>.
        """

    def IsCurveOnClosedSurface(self) -> bool:
        """
        A curve with two parametric curves on the same
        surface.
        """

    def IsPolygon3D(self) -> bool:
        """A 3D polygon representation."""

    @overload
    def IsPolygonOnTriangulation(self) -> bool:
        """
        A representation by an array of nodes on a
        triangulation.
        """

    @overload
    def IsPolygonOnTriangulation(self, T: nanoocp.Poly.Poly_Triangulation, L: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """
        Is it a polygon in the definition of <T> with
        location <L>.
        """

    def IsPolygonOnClosedTriangulation(self) -> bool:
        """
        A representation by two arrays of nodes on a
        triangulation.
        """

    @overload
    def IsPolygonOnSurface(self) -> bool:
        """A polygon in the parametric space of a surface."""

    @overload
    def IsPolygonOnSurface(self, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """
        Is it a polygon in the parametric space of <S> with
        location <L>.
        """

    def IsPolygonOnClosedSurface(self) -> bool:
        """
        Two 2D polygon representations in the parametric
        space of a surface.
        """

    @overload
    def Location(self) -> nanoocp.TopLoc.TopLoc_Location: ...

    @overload
    def Location(self, L: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    @overload
    def Curve3D(self) -> nanoocp.Geom.Geom_Curve: ...

    @overload
    def Curve3D(self, C: nanoocp.Geom.Geom_Curve) -> None: ...

    def Surface(self) -> nanoocp.Geom.Geom_Surface: ...

    @overload
    def PCurve(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    @overload
    def PCurve(self, C: nanoocp.Geom2d.Geom2d_Curve) -> None: ...

    @overload
    def PCurve2(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    @overload
    def PCurve2(self, C: nanoocp.Geom2d.Geom2d_Curve) -> None: ...

    @overload
    def Polygon3D(self) -> nanoocp.Poly.Poly_Polygon3D: ...

    @overload
    def Polygon3D(self, P: nanoocp.Poly.Poly_Polygon3D) -> None: ...

    @overload
    def Polygon(self) -> nanoocp.Poly.Poly_Polygon2D: ...

    @overload
    def Polygon(self, P: nanoocp.Poly.Poly_Polygon2D) -> None: ...

    @overload
    def Polygon2(self) -> nanoocp.Poly.Poly_Polygon2D: ...

    @overload
    def Polygon2(self, P: nanoocp.Poly.Poly_Polygon2D) -> None: ...

    def Triangulation(self) -> nanoocp.Poly.Poly_Triangulation: ...

    @overload
    def PolygonOnTriangulation(self) -> nanoocp.Poly.Poly_PolygonOnTriangulation: ...

    @overload
    def PolygonOnTriangulation(self, P: nanoocp.Poly.Poly_PolygonOnTriangulation) -> None: ...

    @overload
    def PolygonOnTriangulation2(self) -> nanoocp.Poly.Poly_PolygonOnTriangulation: ...

    @overload
    def PolygonOnTriangulation2(self, P2: nanoocp.Poly.Poly_PolygonOnTriangulation) -> None: ...

    def Surface2(self) -> nanoocp.Geom.Geom_Surface: ...

    def Location2(self) -> nanoocp.TopLoc.TopLoc_Location: ...

    @overload
    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    @overload
    def Continuity(self, C: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    def Copy(self) -> BRep_CurveRepresentation:
        """Return a copy of this representation."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_GCurve(BRep_CurveRepresentation):
    """
    Root class for the geometric curves
    representation. Contains a range.
    Contains a first and a last parameter.
    """

    def SetRange(self, First: float, Last: float) -> None: ...

    def Range(self) -> tuple[float, float]: ...

    @overload
    def First(self) -> float: ...

    @overload
    def First(self, F: float) -> None: ...

    @overload
    def Last(self) -> float: ...

    @overload
    def Last(self, L: float) -> None: ...

    def D0(self, U: float, P: nanoocp.gp.gp_Pnt) -> None:
        """Computes the point at parameter U."""

    def Update(self) -> None:
        """
        Recomputes any derived data after a modification.
        This is called when the range is modified.
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_Curve3D(BRep_GCurve):
    """Representation of a curve by a 3D curve."""

    @overload
    def __init__(self, C: nanoocp.Geom.Geom_Curve, L: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    @overload
    def __init__(self, theOther: BRep_Curve3D) -> None: ...

    def D0(self, U: float, P: nanoocp.gp.gp_Pnt) -> None:
        """Computes the point at parameter U."""

    def IsCurve3D(self) -> bool:
        """Returns True."""

    @overload
    def Curve3D(self) -> nanoocp.Geom.Geom_Curve: ...

    @overload
    def Curve3D(self, C: nanoocp.Geom.Geom_Curve) -> None: ...

    def Copy(self) -> BRep_CurveRepresentation:
        """Return a copy of this representation."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_CurveOn2Surfaces(BRep_CurveRepresentation):
    """Defines a continuity between two surfaces."""

    @overload
    def __init__(self, S1: nanoocp.Geom.Geom_Surface, S2: nanoocp.Geom.Geom_Surface, L1: nanoocp.TopLoc.TopLoc_Location, L2: nanoocp.TopLoc.TopLoc_Location, C: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    @overload
    def __init__(self, theOther: BRep_CurveOn2Surfaces) -> None: ...

    @overload
    def IsRegularity(self) -> bool:
        """Returns True."""

    @overload
    def IsRegularity(self, S1: nanoocp.Geom.Geom_Surface, S2: nanoocp.Geom.Geom_Surface, L1: nanoocp.TopLoc.TopLoc_Location, L2: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """A curve on two surfaces (continuity)."""

    def D0(self, U: float, P: nanoocp.gp.gp_Pnt) -> None:
        """Raises an error."""

    def Surface(self) -> nanoocp.Geom.Geom_Surface: ...

    def Surface2(self) -> nanoocp.Geom.Geom_Surface: ...

    def Location2(self) -> nanoocp.TopLoc.TopLoc_Location: ...

    @overload
    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    @overload
    def Continuity(self, C: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    def Copy(self) -> BRep_CurveRepresentation:
        """Return a copy of this representation."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_CurveOnSurface(BRep_GCurve):
    """
    Representation of a curve by a curve in the
    parametric space of a surface.
    """

    @overload
    def __init__(self, PC: nanoocp.Geom2d.Geom2d_Curve, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    @overload
    def __init__(self, theOther: BRep_CurveOnSurface) -> None: ...

    def SetUVPoints(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    def UVPoints(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    def D0(self, U: float, P: nanoocp.gp.gp_Pnt) -> None:
        """Computes the point at parameter U."""

    @overload
    def IsCurveOnSurface(self) -> bool:
        """Returns True."""

    @overload
    def IsCurveOnSurface(self, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """A curve in the parametric space of a surface."""

    def Surface(self) -> nanoocp.Geom.Geom_Surface: ...

    @overload
    def PCurve(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    @overload
    def PCurve(self, C: nanoocp.Geom2d.Geom2d_Curve) -> None: ...

    def Copy(self) -> BRep_CurveRepresentation:
        """Return a copy of this representation."""

    def Update(self) -> None:
        """
        Recomputes any derived data after a modification.
        This is called when the range is modified.
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_CurveOnClosedSurface(BRep_CurveOnSurface):
    """
    Representation of a curve by two pcurves on
    a closed surface.
    """

    @overload
    def __init__(self, PC1: nanoocp.Geom2d.Geom2d_Curve, PC2: nanoocp.Geom2d.Geom2d_Curve, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location, C: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    @overload
    def __init__(self, theOther: BRep_CurveOnClosedSurface) -> None: ...

    def SetUVPoints2(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    def UVPoints2(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    def IsCurveOnClosedSurface(self) -> bool:
        """Returns True."""

    @overload
    def IsRegularity(self) -> bool:
        """Returns True"""

    @overload
    def IsRegularity(self, S1: nanoocp.Geom.Geom_Surface, S2: nanoocp.Geom.Geom_Surface, L1: nanoocp.TopLoc.TopLoc_Location, L2: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """A curve on two surfaces (continuity)."""

    @overload
    def PCurve2(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    @overload
    def PCurve2(self, C: nanoocp.Geom2d.Geom2d_Curve) -> None: ...

    def Surface2(self) -> nanoocp.Geom.Geom_Surface:
        """Returns Surface()"""

    def Location2(self) -> nanoocp.TopLoc.TopLoc_Location:
        """Returns Location()"""

    @overload
    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    @overload
    def Continuity(self, C: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    def Copy(self) -> BRep_CurveRepresentation:
        """Return a copy of this representation."""

    def Update(self) -> None:
        """
        Recomputes any derived data after a modification.
        This is called when the range is modified.
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_PointOnCurve(BRep_PointRepresentation):
    """Representation by a parameter on a 3D curve."""

    @overload
    def __init__(self, P: float, C: nanoocp.Geom.Geom_Curve, L: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    @overload
    def __init__(self, theOther: BRep_PointOnCurve) -> None: ...

    @overload
    def IsPointOnCurve(self) -> bool:
        """Returns True"""

    @overload
    def IsPointOnCurve(self, C: nanoocp.Geom.Geom_Curve, L: nanoocp.TopLoc.TopLoc_Location) -> bool: ...

    @overload
    def Curve(self) -> nanoocp.Geom.Geom_Curve: ...

    @overload
    def Curve(self, C: nanoocp.Geom.Geom_Curve) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_PointsOnSurface(BRep_PointRepresentation):
    """Root for points on surface."""

    def __init__(self, theOther: BRep_PointsOnSurface) -> None: ...

    @overload
    def Surface(self) -> nanoocp.Geom.Geom_Surface: ...

    @overload
    def Surface(self, S: nanoocp.Geom.Geom_Surface) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_PointOnCurveOnSurface(BRep_PointsOnSurface):
    """
    Representation by a parameter on a curve on a
    surface.
    """

    @overload
    def __init__(self, P: float, C: nanoocp.Geom2d.Geom2d_Curve, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    @overload
    def __init__(self, theOther: BRep_PointOnCurveOnSurface) -> None: ...

    @overload
    def IsPointOnCurveOnSurface(self) -> bool:
        """Returns True"""

    @overload
    def IsPointOnCurveOnSurface(self, PC: nanoocp.Geom2d.Geom2d_Curve, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> bool: ...

    @overload
    def PCurve(self) -> nanoocp.Geom2d.Geom2d_Curve: ...

    @overload
    def PCurve(self, C: nanoocp.Geom2d.Geom2d_Curve) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_PointOnSurface(BRep_PointsOnSurface):
    """Representation by two parameters on a surface."""

    @overload
    def __init__(self, P1: float, P2: float, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    @overload
    def __init__(self, theOther: BRep_PointOnSurface) -> None: ...

    @overload
    def IsPointOnSurface(self) -> bool: ...

    @overload
    def IsPointOnSurface(self, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> bool: ...

    @overload
    def Parameter2(self) -> float: ...

    @overload
    def Parameter2(self, P: float) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_Polygon3D(BRep_CurveRepresentation):
    """Representation by a 3D polygon."""

    @overload
    def __init__(self, P: nanoocp.Poly.Poly_Polygon3D, L: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    @overload
    def __init__(self, theOther: BRep_Polygon3D) -> None: ...

    def IsPolygon3D(self) -> bool:
        """Returns True."""

    @overload
    def Polygon3D(self) -> nanoocp.Poly.Poly_Polygon3D: ...

    @overload
    def Polygon3D(self, P: nanoocp.Poly.Poly_Polygon3D) -> None: ...

    def Copy(self) -> BRep_CurveRepresentation:
        """Return a copy of this representation."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_PolygonOnSurface(BRep_CurveRepresentation):
    """
    Representation of a 2D polygon in the parametric
    space of a surface.
    """

    @overload
    def __init__(self, P: nanoocp.Poly.Poly_Polygon2D, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    @overload
    def __init__(self, theOther: BRep_PolygonOnSurface) -> None: ...

    @overload
    def IsPolygonOnSurface(self) -> bool: ...

    @overload
    def IsPolygonOnSurface(self, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """
        A 2D polygon representation in the parametric
        space of a surface.
        """

    def Surface(self) -> nanoocp.Geom.Geom_Surface: ...

    @overload
    def Polygon(self) -> nanoocp.Poly.Poly_Polygon2D: ...

    @overload
    def Polygon(self, P: nanoocp.Poly.Poly_Polygon2D) -> None: ...

    def Copy(self) -> BRep_CurveRepresentation:
        """Return a copy of this representation."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_PolygonOnClosedSurface(BRep_PolygonOnSurface):
    """
    Representation by two 2d polygons in the parametric
    space of a surface.
    """

    @overload
    def __init__(self, P1: nanoocp.Poly.Poly_Polygon2D, P2: nanoocp.Poly.Poly_Polygon2D, S: nanoocp.Geom.Geom_Surface, L: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    @overload
    def __init__(self, theOther: BRep_PolygonOnClosedSurface) -> None: ...

    def IsPolygonOnClosedSurface(self) -> bool:
        """returns True."""

    @overload
    def Polygon2(self) -> nanoocp.Poly.Poly_Polygon2D: ...

    @overload
    def Polygon2(self, P: nanoocp.Poly.Poly_Polygon2D) -> None: ...

    def Copy(self) -> BRep_CurveRepresentation:
        """Return a copy of this representation."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_PolygonOnTriangulation(BRep_CurveRepresentation):
    """
    A representation by an array of nodes on a
    triangulation.
    """

    @overload
    def __init__(self, P: nanoocp.Poly.Poly_PolygonOnTriangulation, T: nanoocp.Poly.Poly_Triangulation, L: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    @overload
    def __init__(self, theOther: BRep_PolygonOnTriangulation) -> None: ...

    @overload
    def IsPolygonOnTriangulation(self) -> bool:
        """returns True."""

    @overload
    def IsPolygonOnTriangulation(self, T: nanoocp.Poly.Poly_Triangulation, L: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """
        Is it a polygon in the definition of <T> with
        location <L>.
        """

    @overload
    def PolygonOnTriangulation(self, P: nanoocp.Poly.Poly_PolygonOnTriangulation) -> None:
        """returns True."""

    @overload
    def PolygonOnTriangulation(self) -> nanoocp.Poly.Poly_PolygonOnTriangulation: ...

    def Triangulation(self) -> nanoocp.Poly.Poly_Triangulation: ...

    def Copy(self) -> BRep_CurveRepresentation:
        """Return a copy of this representation."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_PolygonOnClosedTriangulation(BRep_PolygonOnTriangulation):
    """
    A representation by two arrays of nodes on a
    triangulation.
    """

    @overload
    def __init__(self, P1: nanoocp.Poly.Poly_PolygonOnTriangulation, P2: nanoocp.Poly.Poly_PolygonOnTriangulation, Tr: nanoocp.Poly.Poly_Triangulation, L: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    @overload
    def __init__(self, theOther: BRep_PolygonOnClosedTriangulation) -> None: ...

    def IsPolygonOnClosedTriangulation(self) -> bool:
        """Returns True."""

    @overload
    def PolygonOnTriangulation2(self, P2: nanoocp.Poly.Poly_PolygonOnTriangulation) -> None: ...

    @overload
    def PolygonOnTriangulation2(self) -> nanoocp.Poly.Poly_PolygonOnTriangulation: ...

    def Copy(self) -> BRep_CurveRepresentation:
        """Return a copy of this representation."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRep_TEdge(nanoocp.TopoDS.TopoDS_TEdge):
    """
    The TEdge from BRep is inherited from the TEdge
    from TopoDS. It contains the geometric data.

    The TEdge contains a:

    * tolerance.
    * same parameter flag.
    * same range flag.
    * Degenerated flag.
    * list of curve representation.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty TEdge."""

    @overload
    def __init__(self, theOther: BRep_TEdge) -> None: ...

    @overload
    def Tolerance(self) -> float: ...

    @overload
    def Tolerance(self, T: float) -> None: ...

    def UpdateTolerance(self, T: float) -> None:
        """
        Sets the tolerance to the max of <T> and the
        current tolerance.
        """

    @overload
    def SameParameter(self) -> bool: ...

    @overload
    def SameParameter(self, S: bool) -> None: ...

    @overload
    def SameRange(self) -> bool: ...

    @overload
    def SameRange(self, S: bool) -> None: ...

    @overload
    def Degenerated(self) -> bool: ...

    @overload
    def Degenerated(self, S: bool) -> None: ...

    def Curves(self) -> nanoocp.NCollection.NCollection_List[nanoocp.BRep.BRep_CurveRepresentation]: ...

    def ChangeCurves(self) -> nanoocp.NCollection.NCollection_List[nanoocp.BRep.BRep_CurveRepresentation]: ...

    def EmptyCopy(self) -> nanoocp.TopoDS.TopoDS_TShape:
        """Returns a copy of the TShape with no sub-shapes."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.BRep
BRep_ListOfCurveRepresentation = nanoocp.NCollection.NCollection_List[nanoocp.BRep.BRep_CurveRepresentation]
BRep_ListOfPointRepresentation = nanoocp.NCollection.NCollection_List[nanoocp.BRep.BRep_PointRepresentation]
