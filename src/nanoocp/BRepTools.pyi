"""OCCT package BRepTools (toolkit TKBRep)"""

import enum
from typing import TextIO, overload

import nanoocp.BRep
import nanoocp.Bnd
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.OSD
import nanoocp.Poly
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopTools
import nanoocp.TopoDS
import nanoocp.gp


class BRepTools:
    """
    The BRepTools package provides utilities for BRep
    data structures.

    * WireExplorer: Tool to explore the topology of
    a wire in the order of the edges.

    * ShapeSet: Tools used for dumping, writing and
    reading.

    * UVBounds: Methods to compute the limits of the
    boundary of a face, a wire or an edge in the
    parametric space of a face.

    * Update: Methods to call when a topology has been
    created to compute all missing data.

    * UpdateFaceUVPoints: Method to update the UV points
    stored with the edges on a face.

    * Compare: Method to compare two vertices.

    * Compare: Method to compare two edges.

    * OuterWire: Method to find the outer wire of a
    face.

    * Map3DEdges: Method to map all the 3D Edges of
    a Shape.

    * Dump: Method to dump a BRep object.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepTools) -> None: ...

    @overload
    @staticmethod
    def UVBounds(F: nanoocp.TopoDS.TopoDS_Face) -> tuple[float, float, float, float]:
        """
        Returns in UMin, UMax, VMin, VMax the bounding
        values in the parametric space of F.
        """

    @overload
    @staticmethod
    def UVBounds(F: nanoocp.TopoDS.TopoDS_Face, W: nanoocp.TopoDS.TopoDS_Wire) -> tuple[float, float, float, float]:
        """
        Returns in UMin, UMax, VMin, VMax the bounding
        values of the wire in the parametric space of F.
        """

    @overload
    @staticmethod
    def UVBounds(F: nanoocp.TopoDS.TopoDS_Face, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[float, float, float, float]:
        """
        Returns in UMin, UMax, VMin, VMax the bounding
        values of the edge in the parametric space of F.
        """

    @overload
    @staticmethod
    def AddUVBounds(F: nanoocp.TopoDS.TopoDS_Face, B: nanoocp.Bnd.Bnd_Box2d) -> None:
        """
        Adds to the box <B> the bounding values in the
        parametric space of F.
        """

    @overload
    @staticmethod
    def AddUVBounds(F: nanoocp.TopoDS.TopoDS_Face, W: nanoocp.TopoDS.TopoDS_Wire, B: nanoocp.Bnd.Bnd_Box2d) -> None:
        """
        Adds to the box <B> the bounding values of the
        wire in the parametric space of F.
        """

    @overload
    @staticmethod
    def AddUVBounds(F: nanoocp.TopoDS.TopoDS_Face, E: nanoocp.TopoDS.TopoDS_Edge, B: nanoocp.Bnd.Bnd_Box2d) -> None:
        """
        Adds to the box <B> the bounding values of the
        edge in the parametric space of F.
        """

    @overload
    @staticmethod
    def Update(V: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """Update a vertex (nothing is done)"""

    @overload
    @staticmethod
    def Update(E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Update an edge, compute 2d bounding boxes."""

    @overload
    @staticmethod
    def Update(W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Update a wire (nothing is done)"""

    @overload
    @staticmethod
    def Update(F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Update a Face, update UV points."""

    @overload
    @staticmethod
    def Update(S: nanoocp.TopoDS.TopoDS_Shell) -> None:
        """Update a shell (nothing is done)"""

    @overload
    @staticmethod
    def Update(S: nanoocp.TopoDS.TopoDS_Solid) -> None:
        """Update a solid (nothing is done)"""

    @overload
    @staticmethod
    def Update(C: nanoocp.TopoDS.TopoDS_CompSolid) -> None:
        """Update a composite solid (nothing is done)"""

    @overload
    @staticmethod
    def Update(C: nanoocp.TopoDS.TopoDS_Compound) -> None:
        """Update a compound (nothing is done)"""

    @overload
    @staticmethod
    def Update(S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Update a shape, call the correct update."""

    @staticmethod
    def UpdateFaceUVPoints(theF: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        For each edge of the face <F> reset the UV points
        to the bounding points of the parametric curve of the
        edge on the face.
        """

    @staticmethod
    def Clean(theShape: nanoocp.TopoDS.TopoDS_Shape, theForce: bool = False) -> None:
        """
        Removes all cached polygonal representation of the shape,
        i.e. the triangulations of the faces of <S> and polygons on
        triangulations and polygons 3d of the edges.
        In case polygonal representation is the only available representation
        for the shape (shape does not have geometry) it is not removed.
        @param[in] theShape   the shape to clean
        @param[in] theForce   allows removing all polygonal representations from the shape,
        including polygons on triangulations irrelevant for the faces of the
        given shape.
        """

    @staticmethod
    def CleanGeometry(theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Removes geometry (curves and surfaces) from all edges and faces of the shape
        """

    @staticmethod
    def RemoveUnusedPCurves(S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Removes all the pcurves of the edges of <S> that
        refer to surfaces not belonging to any face of <S>
        """

    @staticmethod
    def Triangulation(theShape: nanoocp.TopoDS.TopoDS_Shape, theLinDefl: float, theToCheckFreeEdges: bool = False) -> bool:
        """
        Verifies that each Face from the shape has got a triangulation with a deflection smaller or
        equal to specified one and the Edges a discretization on this triangulation.
        @param[in] theShape    shape to verify
        @param[in] theLinDefl  maximum allowed linear deflection
        @param[in] theToCheckFreeEdges  if TRUE, then free Edges are required to have 3D polygon
        @return FALSE if input Shape contains Faces without triangulation,
        or that triangulation has worse (greater) deflection than specified one,
        or Edges in Shape lack polygons on triangulation
        or free Edges in Shape lack 3D polygons
        """

    @staticmethod
    def LoadTriangulation(theShape: nanoocp.TopoDS.TopoDS_Shape, theTriangulationIdx: int = -1, theToSetAsActive: bool = False, theFileSystem: nanoocp.OSD.OSD_FileSystem | None = None) -> bool:
        """
        Loads triangulation data for each face of the shape
        from some deferred storage using specified shared input file system
        @param[in] theShape             shape to load triangulations
        @param[in] theTriangulationIdx  index defining what triangulation should be loaded. Starts
        from 0.
        -1 is used in specific case to load currently already active triangulation.
        If some face doesn't contain triangulation with this index, nothing will be loaded for
        it. Exception will be thrown in case of invalid negative index
        @param[in] theToSetAsActive     flag to activate triangulation after its loading
        @param[in] theFileSystem        shared file system
        @return TRUE if at least one triangulation is loaded.
        """

    @staticmethod
    def UnloadTriangulation(theShape: nanoocp.TopoDS.TopoDS_Shape, theTriangulationIdx: int = -1) -> bool:
        """
        Releases triangulation data for each face of the shape if there is deferred storage to load it
        later
        @param[in] theShape             shape to unload triangulations
        @param[in] theTriangulationIdx  index defining what triangulation should be unloaded. Starts
        from 0.
        -1 is used in specific case to unload currently already active triangulation.
        If some face doesn't contain triangulation with this index, nothing will be unloaded
        for it. Exception will be thrown in case of invalid negative index
        @return TRUE if at least one triangulation is unloaded.
        """

    @staticmethod
    def ActivateTriangulation(theShape: nanoocp.TopoDS.TopoDS_Shape, theTriangulationIdx: int, theToActivateStrictly: bool = False) -> bool:
        """
        Activates triangulation data for each face of the shape
        from some deferred storage using specified shared input file system
        @param[in] theShape               shape to activate triangulations
        @param[in] theTriangulationIdx    index defining what triangulation should be activated.
        Starts from 0.
        Exception will be thrown in case of invalid negative index
        @param[in] theToActivateStrictly  flag to activate exactly triangulation with defined
        theTriangulationIdx index.
        In TRUE case if some face doesn't contain triangulation with this index, active
        triangulation will not be changed for it. Else the last available triangulation will be
        activated.
        @return TRUE if at least one active triangulation was changed.
        """

    @staticmethod
    def LoadAllTriangulations(theShape: nanoocp.TopoDS.TopoDS_Shape, theFileSystem: nanoocp.OSD.OSD_FileSystem | None = None) -> bool:
        """
        Loads all available triangulations for each face of the shape
        from some deferred storage using specified shared input file system
        @param[in] theShape       shape to load triangulations
        @param[in] theFileSystem  shared file system
        @return TRUE if at least one triangulation is loaded.
        """

    @staticmethod
    def UnloadAllTriangulations(theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Releases all available triangulations for each face of the shape if there is deferred storage
        to load them later
        @param[in] theShape       shape to unload triangulations
        @return TRUE if at least one triangulation is unloaded.
        """

    @overload
    @staticmethod
    def Compare(V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> bool:
        """
        Returns True if the distance between the two
        vertices is lower than their tolerance.
        """

    @overload
    @staticmethod
    def Compare(E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """
        Returns True if the distance between the two
        edges is lower than their tolerance.
        """

    @staticmethod
    def OuterWire(F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.TopoDS.TopoDS_Wire:
        """
        Returns the outer most wire of <F>. Returns a Null
        wire if <F> has no wires.
        """

    @staticmethod
    def Map3DEdges(S: nanoocp.TopoDS.TopoDS_Shape, M: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        Stores in the map <M> all the 3D topology edges
        of <S>.
        """

    @staticmethod
    def IsReallyClosed(E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """
        Verifies that the edge <E> is found two times on
        the face <F> before calling BRep_Tool::IsClosed.
        """

    @staticmethod
    def DetectClosedness(theFace: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, bool]:
        """Detect closedness of face in U and V directions"""

    @staticmethod
    def Dump(Sh: nanoocp.TopoDS.TopoDS_Shape) -> str:
        """
        Dumps the topological structure and the geometry
        of <Sh> on the stream <S>.
        """

    @overload
    @staticmethod
    def Write(theShape: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> str:
        """
        Writes the shape to the stream in an ASCII format TopTools_FormatVersion_VERSION_1.
        This alias writes shape with triangulation data.
        @param[in] theShape        the shape to write
        @param[in][out] theStream  the stream to output shape into
        @param theRange            the range of progress indicator to fill in
        """

    @overload
    @staticmethod
    def Write(theShape: nanoocp.TopoDS.TopoDS_Shape, theWithTriangles: bool, theWithNormals: bool, theVersion: nanoocp.TopTools.TopTools_FormatVersion, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> str:
        """
        Writes the shape to the stream in an ASCII format of specified version.
        @param[in] theShape          the shape to write
        @param[in][out] theStream    the stream to output shape into
        @param[in] theWithTriangles  flag which specifies whether to save shape with (TRUE) or without
        (FALSE) triangles;
        has no effect on triangulation-only geometry
        @param[in] theWithNormals    flag which specifies whether to save triangulation with (TRUE) or
        without (FALSE) normals;
        has no effect on triangulation-only geometry
        @param[in] theVersion        the TopTools format version
        @param theProgress the range of progress indicator to fill in
        """

    @overload
    @staticmethod
    def Write(theShape: nanoocp.TopoDS.TopoDS_Shape, theFile: str, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Writes the shape to the file in an ASCII format TopTools_FormatVersion_VERSION_1.
        This alias writes shape with triangulation data.
        @param[in] theShape  the shape to write
        @param[in] theFile   the path to file to output shape into
        @param theProgress the range of progress indicator to fill in
        """

    @overload
    @staticmethod
    def Write(theShape: nanoocp.TopoDS.TopoDS_Shape, theFile: str, theWithTriangles: bool, theWithNormals: bool, theVersion: nanoocp.TopTools.TopTools_FormatVersion, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Writes the shape to the file in an ASCII format of specified version.
        @param[in] theShape          the shape to write
        @param[in] theFile           the path to file to output shape into
        @param[in] theWithTriangles  flag which specifies whether to save shape with (TRUE) or without
        (FALSE) triangles;
        has no effect on triangulation-only geometry
        @param[in] theWithNormals    flag which specifies whether to save triangulation with (TRUE) or
        without (FALSE) normals;
        has no effect on triangulation-only geometry
        @param[in] theVersion        the TopTools format version
        @param theProgress the range of progress indicator to fill in
        """

    @overload
    @staticmethod
    def Read(Sh: nanoocp.TopoDS.TopoDS_Shape, S: TextIO, B: nanoocp.BRep.BRep_Builder, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads a Shape from <S> in returns it in <Sh>.
        <B> is used to build the shape.
        """

    @overload
    @staticmethod
    def Read(Sh: nanoocp.TopoDS.TopoDS_Shape, File: str, B: nanoocp.BRep.BRep_Builder, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Reads a Shape from <File>, returns it in <Sh>.
        <B> is used to build the shape.
        """

    @staticmethod
    def EvalAndUpdateTol(theE: nanoocp.TopoDS.TopoDS_Edge, theC3d: nanoocp.Geom.Geom_Curve | None, theC2d: nanoocp.Geom2d.Geom2d_Curve | None, theS: nanoocp.Geom.Geom_Surface | None, theF: float, theL: float) -> float:
        """
        Evals real tolerance of edge <theE>.
        <theC3d>, <theC2d>, <theS>, <theF>, <theL> are
        correspondently 3d curve of edge, 2d curve on surface <theS> and
        rang of edge
        If calculated tolerance is more then current edge tolerance, edge is updated.
        Method returns actual tolerance of edge
        """

    @staticmethod
    def OriEdgeInFace(theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.TopAbs.TopAbs_Orientation:
        """
        returns the cumul of the orientation of <Edge>
        and the containing wire in <Face>
        """

    @staticmethod
    def RemoveInternals(theS: nanoocp.TopoDS.TopoDS_Shape, theForce: bool = False) -> None:
        """
        Removes internal sub-shapes from the shape.
        The check on internal status is based on orientation of sub-shapes,
        classification is not performed.
        Before removal of internal sub-shapes the algorithm checks if such
        removal is not going to break topological connectivity between sub-shapes.
        The flag <theForce> if set to true disables the connectivity check and clears
        the given shape from all sub-shapes with internal orientation.
        """

    @staticmethod
    def CheckLocations(theS: nanoocp.TopoDS.TopoDS_Shape, theProblemShapes: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Check all locations of shape according criterium:
        aTrsf.IsNegative() || (std::abs(std::abs(aTrsf.ScaleFactor()) - 1.) >
        TopLoc_Location::ScalePrec()) All sub-shapes having such locations are put in list
        theProblemShapes
        """

class BRepTools_Modification(nanoocp.Standard.Standard_Transient):
    """
    Defines geometric modifications to a shape, i.e.
    changes to faces, edges and vertices.
    """

    def NewSurface(self, F: nanoocp.TopoDS.TopoDS_Face, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Surface, float, bool, bool]:
        """
        Returns true if the face, F, has been modified.
        If the face has been modified:
        - S is the new geometry of the face,
        - L is its new location, and
        - Tol is the new tolerance.
        The flag, RevWires, is set to true when the
        modification reverses the normal of the surface, (i.e.
        the wires have to be reversed).
        The flag, RevFace, is set to true if the orientation of
        the modified face changes in the shells which contain it.
        If the face has not been modified this function returns
        false, and the values of S, L, Tol, RevWires and
        RevFace are not significant.
        """

    def NewTriangulation(self, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Poly.Poly_Triangulation]:
        """
        Returns true if the face has been modified according to changed triangulation.
        If the face has been modified:
        - T is a new triangulation on the face
        """

    def NewCurve(self, E: nanoocp.TopoDS.TopoDS_Edge, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Curve, float]:
        """
        Returns true if the edge, E, has been modified.
        If the edge has been modified:
        - C is the new geometry associated with the edge,
        - L is its new location, and
        - Tol is the new tolerance.
        If the edge has not been modified, this function
        returns false, and the values of C, L and Tol are not significant.
        """

    def NewPolygon(self, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, nanoocp.Poly.Poly_Polygon3D]:
        """
        Returns true if the edge has been modified according to changed polygon.
        If the edge has been modified:
        - P is a new polygon
        """

    def NewPolygonOnTriangulation(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Poly.Poly_PolygonOnTriangulation]:
        """
        Returns true if the edge has been modified according to changed polygon on triangulation.
        If the edge has been modified:
        - P is a new polygon on triangulation
        """

    def NewPoint(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """
        Returns true if the vertex V has been modified.
        If V has been modified:
        - P is the new geometry of the vertex, and
        - Tol is the new tolerance.
        If the vertex has not been modified this function
        returns false, and the values of P and Tol are not significant.
        """

    def NewCurve2d(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Returns true if the edge, E, has a new curve on
        surface on the face, F.
        If a new curve exists:
        - C is the new geometry of the edge,
        - L is the new location, and
        - Tol is the new tolerance.
        NewE is the new edge created from E, and NewF is
        the new face created from F.
        If there is no new curve on the face, this function
        returns false, and the values of C, L and Tol are not significant.
        """

    def NewParameter(self, V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]:
        """
        Returns true if the vertex V has a new parameter on the edge E.
        If a new parameter exists:
        - P is the parameter, and
        - Tol is the new tolerance.
        If there is no new parameter this function returns
        false, and the values of P and Tol are not significant.
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

class BRepTools_CopyModification(BRepTools_Modification):
    """
    Tool class implementing necessary functionality for copying geometry and triangulation.
    """

    @overload
    def __init__(self, theCopyGeom: bool = True, theCopyMesh: bool = True) -> None:
        """
        Constructor.
        \\param[in] theCopyGeom  indicates that the geometry (surfaces and curves) should be copied
        \\param[in] theCopyMesh  indicates that the triangulation should be copied
        """

    @overload
    def __init__(self, theOther: BRepTools_CopyModification) -> None: ...

    def NewSurface(self, theFace: nanoocp.TopoDS.TopoDS_Face, theLoc: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Surface, float, bool, bool]:
        """
        Returns true if theFace has been modified.
        If the face has been modified:
        - theSurf is the new geometry of the face,
        - theLoc is its new location, and
        - theTol is the new tolerance.
        theRevWires, theRevFace are always set to false, because the orientation is not changed.
        """

    def NewCurve(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theLoc: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Curve, float]:
        """
        Returns true if theEdge has been modified.
        If the edge has been modified:
        - theCurve is the new geometric support of the edge,
        - theLoc is the new location, and
        - theTol is the new tolerance.
        If the edge has not been modified, this function
        returns false, and the values of theCurve, theLoc and theTol are not significant.
        """

    def NewPoint(self, theVertex: nanoocp.TopoDS.TopoDS_Vertex, thePnt: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """
        Returns true if theVertex has been modified.
        If the vertex has been modified:
        - thePnt is the new geometry of the vertex, and
        - theTol is the new tolerance.
        If the vertex has not been modified this function
        returns false, and the values of thePnt and theTol are not significant.
        """

    def NewCurve2d(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face, theNewEdge: nanoocp.TopoDS.TopoDS_Edge, theNewFace: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Returns true if theEdge has a new curve on surface on theFace.
        If a new curve exists:
        - theCurve is the new geometric support of the edge,
        - theTol the new tolerance.
        If no new curve exists, this function returns false, and
        the values of theCurve and theTol are not significant.
        """

    def NewParameter(self, theVertex: nanoocp.TopoDS.TopoDS_Vertex, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]:
        """
        Returns true if theVertex has a new parameter on theEdge.
        If a new parameter exists:
        - thePnt is the parameter, and
        - theTol is the new tolerance.
        If no new parameter exists, this function returns false,
        and the values of thePnt and theTol are not significant.
        """

    def Continuity(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace1: nanoocp.TopoDS.TopoDS_Face, theFace2: nanoocp.TopoDS.TopoDS_Face, theNewEdge: nanoocp.TopoDS.TopoDS_Edge, theNewFace1: nanoocp.TopoDS.TopoDS_Face, theNewFace2: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Returns the continuity of theNewEdge between theNewFace1 and theNewFace2.

        theNewEdge is the new edge created from theEdge. theNewFace1
        (resp. theNewFace2) is the new face created from theFace1 (resp. theFace2).
        """

    def NewTriangulation(self, theFace: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Poly.Poly_Triangulation]:
        """
        Returns true if the face has been modified according to changed triangulation.
        If the face has been modified:
        - theTri is a new triangulation on the face
        """

    def NewPolygon(self, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, nanoocp.Poly.Poly_Polygon3D]:
        """
        Returns true if the edge has been modified according to changed polygon.
        If the edge has been modified:
        - thePoly is a new polygon
        """

    def NewPolygonOnTriangulation(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Poly.Poly_PolygonOnTriangulation]:
        """
        Returns true if the edge has been modified according to changed polygon on triangulation.
        If the edge has been modified:
        - thePoly is a new polygon on triangulation
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepTools_GTrsfModification(BRepTools_Modification):
    """
    Defines a modification of the geometry by a GTrsf
    from gp. All methods return True and transform the
    geometry.
    """

    @overload
    def __init__(self, T: nanoocp.gp.gp_GTrsf) -> None: ...

    @overload
    def __init__(self, theOther: BRepTools_GTrsfModification) -> None: ...

    def GTrsf(self) -> nanoocp.gp.gp_GTrsf:
        """Gives an access on the GTrsf."""

    def NewSurface(self, F: nanoocp.TopoDS.TopoDS_Face, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Surface, float, bool, bool]:
        """
        Returns true if the face <F> has been
        modified. In this case, <S> is the new geometric
        support of the face, <L> the new location,<Tol>
        the new tolerance.<RevWires> has to be set to
        true when the modification reverses the
        normal of the surface. (the wires have to be
        reversed). <RevFace> has to be set to
        true if the orientation of the modified
        face changes in the shells which contain it.
        Here, <RevFace> will return true if the
        - gp_Trsf is negative.
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

    def NewTriangulation(self, theFace: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Poly.Poly_Triangulation]:
        """
        Returns true if the face has been modified according to changed triangulation.
        If the face has been modified:
        - theTri is a new triangulation on the face
        """

    def NewPolygon(self, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, nanoocp.Poly.Poly_Polygon3D]:
        """
        Returns true if the edge has been modified according to changed polygon.
        If the edge has been modified:
        - thePoly is a new polygon
        """

    def NewPolygonOnTriangulation(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Poly.Poly_PolygonOnTriangulation]:
        """
        Returns true if the edge has been modified according to changed polygon on triangulation.
        If the edge has been modified:
        - thePoly is a new polygon on triangulation
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepTools_History(nanoocp.Standard.Standard_Transient):
    """
    The history keeps the following relations between the input shapes
    (S1, ..., Sm) and output shapes (T1, ..., Tn):
    1) an output shape Tj is generated from an input shape Si: Tj <= G(Si);
    2) a output shape Tj is modified from an input shape Si: Tj <= M(Si);
    3) an input shape (Si) is removed: R(Si) == 1.

    The relations are kept only for shapes of types vertex, edge, face, and
    solid.

    The last relation means that:
    1) shape Si is not an output shape and
    2) no any shape is modified (produced) from shape Si:
    R(Si) == 1 ==> Si != Tj, M(Si) == 0.

    It means that the input shape cannot be removed and modified
    simultaneously. However, the shapes may be generated from the
    removed shape. For instance, in Fillet operation the edges
    generate faces and then are removed.

    No any shape could be generated and modified from the same shape
    simultaneously: sets G(Si) and M(Si) are not intersected
    (G(Si) ^ M(Si) == 0).

    Each output shape should be:
    1) an input shape or
    2) generated or modified from an input shape (even generated from the
    implicit null shape if necessary):
    Tj == Si V (exists Si that Tj <= G(Si) U M(Si)).

    Recommendations to choose between relations 'generated' and 'modified':
    1) a shape is generated from input shapes if it dimension is greater or
    smaller than the dimensions of the input shapes;
    2) a shape is generated from input shapes if these shapes are also output
    shapes;
    3) a shape is generated from input shapes of the same dimension if it is
    produced by joining shapes generated from these shapes;
    4) a shape is modified from an input shape if it replaces the input shape by
    changes of the location, the tolerance, the bounds of the parametric
    space (the faces for a solid), the parametrization and/or by applying of
    an approximation;
    5) a shape is modified from input shapes of the same dimension if it is
    produced by joining shapes modified from these shapes.

    Two sequential histories:
    - one history (H12) of shapes S1, ..., Sm to shapes T1, ..., Tn and
    - another history (H23) of shapes T1, ..., Tn to shapes Q1, ..., Ql
    could be merged to the single history (H13) of shapes S1, ..., Sm to shapes
    Q1, ..., Ql.

    During the merge:
    1) if shape Tj is generated from shape Si then each shape generated or
    modified from shape Tj is considered as a shape generated from shape Si
    among shapes Q1, ..., Ql:
    Tj <= G12(Si), Qk <= G23(Tj) U M23(Tj) ==> Qk <= G13(Si).
    2) if shape Tj is modified from shape Si, shape Qk is generated from shape
    Tj then shape Qk is considered as a shape generated from shape Si among
    shapes Q1, ..., Ql:
    Tj <= M12(Si), Qk <= G23(Tj) ==> Qk <= G13(Si);
    3) if shape Tj is modified from shape Si, shape Qk is modified from shape
    Tj then shape Qk is considered as a shape modified from shape Si among
    shapes Q1, ..., Ql:
    Tj <= M12(Si), Qk <= M23(Tj) ==> Qk <= M13(Si);
    """

    @overload
    def __init__(self) -> None:
        """
        @name Constructors for History creation
        Empty constructor
        """

    @overload
    def __init__(self, theOther: BRepTools_History) -> None: ...

    class TRelationType(enum.IntEnum):
        """The types of the historical relations."""

        TRelationType_Removed = 0

        TRelationType_Generated = 1

        TRelationType_Modified = 2

    TRelationType_Removed: BRepTools_History.TRelationType = TRelationType.TRelationType_Removed

    TRelationType_Generated: BRepTools_History.TRelationType = TRelationType.TRelationType_Generated

    TRelationType_Modified: BRepTools_History.TRelationType = TRelationType.TRelationType_Modified

    @staticmethod
    def IsSupportedType(theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns 'true' if the type of the shape is supported by the history."""

    def AddGenerated(self, theInitial: nanoocp.TopoDS.TopoDS_Shape, theGenerated: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Methods to set the history.
        Set the second shape as generated one from the first shape.
        """

    def AddModified(self, theInitial: nanoocp.TopoDS.TopoDS_Shape, theModified: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Set the second shape as modified one from the first shape."""

    def Remove(self, theRemoved: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Set the shape as removed one."""

    def ReplaceGenerated(self, theInitial: nanoocp.TopoDS.TopoDS_Shape, theGenerated: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Set the second shape as the only generated one from the first one."""

    def ReplaceModified(self, theInitial: nanoocp.TopoDS.TopoDS_Shape, theModified: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Set the second shape as the only modified one from the first one."""

    def Clear(self) -> None:
        """Clears the history."""

    def Generated(self, theInitial: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Methods to read the history.
        Returns all shapes generated from the shape.
        """

    def Modified(self, theInitial: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns all shapes modified from the shape."""

    def IsRemoved(self, theInitial: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns 'true' if the shape is removed."""

    def HasGenerated(self) -> bool:
        """Returns 'true' if there any shapes with Generated elements present"""

    def HasModified(self) -> bool:
        """Returns 'true' if there any Modified shapes present"""

    def HasRemoved(self) -> bool:
        """Returns 'true' if there any removed shapes present"""

    @overload
    def Merge(self, theHistory23: BRepTools_History | None) -> None:
        """
        A method to merge a next history to this history.
        Merges the next history to this history.
        """

    @overload
    def Merge(self, theHistory23: BRepTools_History) -> None:
        """Merges the next history to this history."""

    def Dump(self) -> str:
        """
        A method to dump a history
        Prints the brief description of the history into a stream
        """

    @staticmethod
    def get_type_name() -> str:
        """Define the OCCT RTTI for the type."""

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type:
        """Define the OCCT RTTI for the type."""

    def DynamicType(self) -> nanoocp.Standard.Standard_Type:
        """Define the OCCT RTTI for the type."""

class BRepTools_Modifier:
    """Performs geometric modifications on a shape."""

    @overload
    def __init__(self, theMutableInput: bool = False) -> None:
        """Creates an empty Modifier."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Creates a modifier on the shape <S>."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, M: BRepTools_Modification | None) -> None:
        """
        Creates a modifier on the shape <S>, and performs
        the modifications described by <M>.
        """

    @overload
    def __init__(self, theOther: BRepTools_Modifier) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initializes the modifier with the shape <S>."""

    def Perform(self, M: BRepTools_Modification | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Performs the modifications described by <M>."""

    def IsDone(self) -> bool:
        """
        Returns true if the modification has
        been computed successfully.
        """

    def IsMutableInput(self) -> bool:
        """Returns the current mutable input state"""

    def SetMutableInput(self, theMutableInput: bool) -> None:
        """
        Sets the mutable input state
        If true then the input (original) shape can be modified
        during modification process
        """

    def ModifiedShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the modified shape corresponding to <S>."""

class BRepTools_NurbsConvertModification(BRepTools_CopyModification):
    """
    Defines a modification of the geometry by a Trsf
    from gp. All methods return True and transform the
    geometry.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepTools_NurbsConvertModification) -> None: ...

    def NewSurface(self, F: nanoocp.TopoDS.TopoDS_Face, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Surface, float, bool, bool]:
        """
        Returns true if the face <F> has been
        modified. In this case, <S> is the new geometric
        support of the face, <L> the new location,<Tol>
        the new tolerance.<RevWires> has to be set to
        true when the modification reverses the
        normal of the surface. (the wires have to be
        reversed). <RevFace> has to be set to
        true if the orientation of the modified
        face changes in the shells which contain it.
        Here, <RevFace> will return true if the
        - gp_Trsf is negative.
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

    def NewTriangulation(self, theFace: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Poly.Poly_Triangulation]:
        """
        Returns true if the face has been modified according to changed triangulation.
        If the face has been modified:
        - theTri is a new triangulation on the face
        """

    def NewPolygon(self, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, nanoocp.Poly.Poly_Polygon3D]:
        """
        Returns true if the edge has been modified according to changed polygon.
        If the edge has been modified:
        - thePoly is a new polygon
        """

    def NewPolygonOnTriangulation(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Poly.Poly_PolygonOnTriangulation]:
        """
        Returns true if the edge has been modified according to changed polygon on triangulation.
        If the edge has been modified:
        - thePoly is a new polygon on triangulation
        """

    def GetUpdatedEdges(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepTools_Quilt:
    """
    A Tool to glue faces at common edges and reconstruct shells.

    The user designate pairs of common edges using the method Bind.
    One edge is designated as the edge to use in place of the other one
    (they are supposed to be geometrically confused, but this not checked).
    They can be of opposite directions, this is specified by the orientations.

    The user can add shapes with the Add method, all the faces are registered and copies of faces
    and edges are made to glue at the bound edges.

    The user can call the Shells methods to compute a compound of shells from the current set of
    faces.

    If no binding is made this class can be used to make shell from faces already sharing their
    edges.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepTools_Quilt) -> None: ...

    @overload
    def Bind(self, Eold: nanoocp.TopoDS.TopoDS_Edge, Enew: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """
        Binds <Enew> to be the new edge instead of <Eold>.

        The faces of the added shape containing <Eold>
        will be copied to substitute <Eold> by <Enew>.

        The vertices of <Eold> will be bound to the
        vertices of <Enew> with the same orientation.

        If <Eold> and <Enew> have different orientations
        the curves are considered to be opposite and the
        pcurves of <Eold> will be copied and reversed in
        the new faces.

        <Eold> must belong to the next added shape, <Enew> must belong
        to a Shape added before.
        """

    @overload
    def Bind(self, Vold: nanoocp.TopoDS.TopoDS_Vertex, Vnew: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        Binds <VNew> to be a new vertex instead of <Vold>.

        The faces of the added shape containing <Vold>
        will be copied to substitute <Vold> by <Vnew>.
        """

    def Add(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Add the faces of <S> to the Quilt, the faces
        containing bounded edges are copied.
        """

    def IsCopied(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Returns True if <S> has been copied (<S> is a
        vertex, an edge or a face)
        """

    def Copy(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the shape substituted to <S> in the Quilt."""

    def Shells(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns a Compound of shells made from the current
        set of faces. The shells will be flagged as closed
        or not closed.
        """

class BRepTools_ReShape(nanoocp.Standard.Standard_Transient):
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

    Supports the 'BRepTools_History' history by method 'History'.
    """

    @overload
    def __init__(self) -> None:
        """Returns an empty Reshape"""

    @overload
    def __init__(self, theOther: BRepTools_ReShape) -> None: ...

    def Clear(self) -> None:
        """Clears all substitutions requests"""

    def Remove(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Sets a request to Remove a Shape whatever the orientation"""

    def Replace(self, shape: nanoocp.TopoDS.TopoDS_Shape, newshape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Sets a request to Replace a Shape by a new one."""

    def IsRecorded(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Tells if a shape is recorded for Replace/Remove"""

    def Value(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the new value for an individual shape
        If not recorded, returns the original shape itself
        If to be Removed, returns a Null Shape
        Else, returns the replacing item
        """

    def ValueLeaf(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Follows the replacement chain for @p theShape to its leaf without descending into sub-shapes.
        Iterates Value() until a fixpoint is reached. Unlike Apply(), this does not rebuild
        the shape from its children, so it is safe to call on edges/wires whose sub-shapes
        have their own pending replacements (avoids cascading sub-shape re-expansion).
        @return the final replacement, or the original shape if not recorded,
        or a Null shape if the chain terminates in a Remove.
        """

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

    def Apply(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theUntil: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Applies the substitutions requests to a shape.

        theUntil gives the level of type until which requests are taken into account.
        For subshapes of the type <until> no rebuild and further exploring are done.

        NOTE: each subshape can be replaced by shape of the same type
        or by shape containing only shapes of that type
        (for example, TopoDS_Edge can be replaced by TopoDS_Edge,
        TopoDS_Wire or TopoDS_Compound containing TopoDS_Edges).
        If incompatible shape type is encountered, it is ignored and flag FAIL1 is set in Status.
        """

    def ModeConsiderLocation(self) -> bool:
        """
        Returns (modifiable) the flag which defines whether Location of shape take into account
        during replacing shapes.
        """

    def SetModeConsiderLocation(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModeConsiderLocation() returns by reference in C++.
        """

    @overload
    def CopyVertex(self, theV: nanoocp.TopoDS.TopoDS_Vertex, theTol: float = -1.0) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    @overload
    def CopyVertex(self, theV: nanoocp.TopoDS.TopoDS_Vertex, theNewPos: nanoocp.gp.gp_Pnt, aTol: float) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def IsNewShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def History(self) -> BRepTools_History:
        """Returns the history of the substituted shapes."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepTools_ShapeSet(nanoocp.TopTools.TopTools_ShapeSet):
    """
    Contains a Shape and all its subshapes, locations
    and geometries.

    The topology is inherited from TopTools.
    """

    @overload
    def __init__(self, theWithTriangles: bool = True, theWithNormals: bool = False) -> None: ...

    @overload
    def __init__(self, theBuilder: nanoocp.BRep.BRep_Builder, theWithTriangles: bool = True, theWithNormals: bool = False) -> None:
        """
        Builds an empty ShapeSet.
        @param theWithTriangles flag to write triangulation data
        """

    @overload
    def __init__(self, theOther: BRepTools_ShapeSet) -> None: ...

    def IsWithTriangles(self) -> bool:
        """Return true if shape should be stored with triangles."""

    def IsWithNormals(self) -> bool:
        """Return true if shape should be stored triangulation with normals."""

    def SetWithTriangles(self, theWithTriangles: bool) -> None:
        """
        Define if shape will be stored with triangles.
        Ignored (always written) if face defines only triangulation (no surface).
        """

    def SetWithNormals(self, theWithNormals: bool) -> None:
        """
        Define if shape will be stored triangulation with normals.
        Ignored (always written) if face defines only triangulation (no surface).
        """

    def Clear(self) -> None:
        """Clears the content of the set."""

    def AddGeometry(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Stores the geometry of <S>."""

    @overload
    def DumpGeometry(self) -> str:
        """Dumps the geometry of me on the stream <OS>."""

    @overload
    def DumpGeometry(self, S: nanoocp.TopoDS.TopoDS_Shape) -> str:
        """Dumps the geometry of <S> on the stream <OS>."""

    @overload
    def WriteGeometry(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> str:
        """
        Writes the geometry of me on the stream <OS> in a
        format that can be read back by Read.
        """

    @overload
    def WriteGeometry(self, S: nanoocp.TopoDS.TopoDS_Shape) -> str:
        """
        Writes the geometry of <S> on the stream <OS> in a
        format that can be read back by Read.
        """

    @overload
    def ReadGeometry(self, IS: TextIO, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Reads the geometry of me from the stream <IS>."""

    @overload
    def ReadGeometry(self, T: nanoocp.TopAbs.TopAbs_ShapeEnum, IS: TextIO, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Reads the geometry of a shape of type <T> from the
        stream <IS> and returns it in <S>.
        """

    def AddShapes(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Inserts the shape <S2> in the shape <S1>. This
        method must be redefined to use the correct
        builder.
        """

    def Check(self, T: nanoocp.TopAbs.TopAbs_ShapeEnum, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def ReadPolygon3D(self, IS: TextIO, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the 3d polygons of me
        from the stream <IS>.
        """

    def WritePolygon3D(self, Compact: bool = True, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> str:
        """
        Writes the 3d polygons
        on the stream <OS> in a format that can
        be read back by Read.
        """

    def DumpPolygon3D(self) -> str:
        """
        Dumps the 3d polygons
        on the stream <OS>.
        """

    def ReadTriangulation(self, IS: TextIO, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the triangulation of me
        from the stream <IS>.
        """

    def WriteTriangulation(self, Compact: bool = True, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> str:
        """
        Writes the triangulation
        on the stream <OS> in a format that can
        be read back by Read.
        """

    def DumpTriangulation(self) -> str:
        """
        Dumps the triangulation
        on the stream <OS>.
        """

    def ReadPolygonOnTriangulation(self, IS: TextIO, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Reads the polygons on triangulation of me
        from the stream <IS>.
        """

    def WritePolygonOnTriangulation(self, Compact: bool = True, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> str:
        """
        Writes the polygons on triangulation
        on the stream <OS> in a format that can
        be read back by Read.
        """

    def DumpPolygonOnTriangulation(self) -> str:
        """
        Dumps the polygons on triangulation
        on the stream <OS>.
        """

class BRepTools_Substitution:
    """
    A tool to substitute subshapes by other shapes.

    The user use the method Substitute to define the
    modifications.
    A set of shapes is designated to replace a initial
    shape.

    The method Build reconstructs a new Shape with the
    modifications.The Shape and the new shape are
    registered.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepTools_Substitution) -> None: ...

    def Clear(self) -> None:
        """Reset all the fields."""

    def Substitute(self, OldShape: nanoocp.TopoDS.TopoDS_Shape, NewShapes: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        <Oldshape> will be replaced by <NewShapes>.

        <NewShapes> can be empty, in this case <OldShape>
        will disparate from its ancestors.

        if an item of <NewShapes> is oriented FORWARD.
        it will be oriented as <OldShape> in its ancestors.
        else it will be reversed.
        """

    def Build(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Build NewShape from <S> if its subshapes has modified.

        The methods <IsCopied> and <Copy> allows you to keep
        the resul of <Build>
        """

    def IsCopied(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns True if <S> has been replaced."""

    def Copy(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the set of shapes substituted to <S>."""

class BRepTools_TrsfModification(BRepTools_Modification):
    """
    Describes a modification that uses a gp_Trsf to
    change the geometry of a shape. All functions return
    true and transform the geometry of the shape.
    """

    @overload
    def __init__(self, T: nanoocp.gp.gp_Trsf) -> None: ...

    @overload
    def __init__(self, theOther: BRepTools_TrsfModification) -> None: ...

    def Trsf(self) -> nanoocp.gp.gp_Trsf:
        """
        Provides access to the gp_Trsf associated with this
        modification. The transformation can be changed.
        """

    def IsCopyMesh(self) -> bool:
        """Sets a flag to indicate the need to copy mesh."""

    def SetIsCopyMesh(self, theValue: bool) -> None:
        """
        Python addition: sets the value IsCopyMesh() returns by reference in C++.
        """

    def NewSurface(self, F: nanoocp.TopoDS.TopoDS_Face, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Surface, float, bool, bool]:
        """
        Returns true if the face F has been modified.
        If the face has been modified:
        - S is the new geometry of the face,
        - L is its new location, and
        - Tol is the new tolerance.
        RevWires is set to true when the modification
        reverses the normal of the surface (the wires have to be reversed).
        RevFace is set to true if the orientation of the
        modified face changes in the shells which contain it.
        For this class, RevFace returns true if the gp_Trsf
        associated with this modification is negative.
        """

    def NewTriangulation(self, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Poly.Poly_Triangulation]:
        """
        Returns true if the face has been modified according to changed triangulation.
        If the face has been modified:
        - T is a new triangulation on the face
        """

    def NewPolygon(self, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, nanoocp.Poly.Poly_Polygon3D]:
        """
        Returns true if the edge has been modified according to changed polygon.
        If the edge has been modified:
        - P is a new polygon
        """

    def NewPolygonOnTriangulation(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Poly.Poly_PolygonOnTriangulation]:
        """
        Returns true if the edge has been modified according to changed polygon on triangulation.
        If the edge has been modified:
        - P is a new polygon on triangulation
        """

    def NewCurve(self, E: nanoocp.TopoDS.TopoDS_Edge, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Curve, float]:
        """
        Always returns true indicating that the edge E is always modified.
        - C is the new geometric support of the edge,
        - L is the new location, and
        - Tol is the new tolerance.
        """

    def NewPoint(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """
        Returns true if the vertex V has been modified.
        If the vertex has been modified:
        - P is the new geometry of the vertex, and
        - Tol is the new tolerance.
        If the vertex has not been modified this function
        returns false, and the values of P and Tol are not significant.
        """

    def NewCurve2d(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Returns true if the edge E has a new curve on surface on the face F.
        If a new curve exists:
        - C is the new geometric support of the edge,
        - L is the new location, and
        - Tol the new tolerance.
        If no new curve exists, this function returns false, and
        the values of C, L and Tol are not significant.
        """

    def NewParameter(self, V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]:
        """
        Returns true if the Vertex V has a new parameter on the edge E.
        If a new parameter exists:
        - P is the parameter, and
        - Tol is the new tolerance.
        If no new parameter exists, this function returns false,
        and the values of P and Tol are not significant.
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

class BRepTools_WireExplorer:
    """
    The WireExplorer is a tool to explore the edges of
    a wire in a connection order.

    i.e. each edge is connected to the previous one by
    its origin.
    If a wire is not closed returns only a segment of edges which
    length depends on started in exploration edge.
    Algorithm suggests that wire is valid and has no any defects, which
    can stop edge exploration. Such defects can be loops, wrong orientation of edges
    (two edges go in to shared vertex or go out from shared vertex), branching of edges,
    the presens of edges with INTERNAL or EXTERNAL orientation. If wire has
    such kind of defects WireExplorer can return not all
    edges in a wire. it depends on type of defect and position of starting edge.
    """

    @overload
    def __init__(self) -> None:
        """Constructs an empty explorer (which can be initialized using Init)"""

    @overload
    def __init__(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """IInitializes an exploration of the wire <W>."""

    @overload
    def __init__(self, W: nanoocp.TopoDS.TopoDS_Wire, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Initializes an exploration of the wire <W>.
        F is used to select the edge connected to the
        previous in the parametric representation of <F>.
        """

    @overload
    def __init__(self, theOther: BRepTools_WireExplorer) -> None: ...

    def __iter__(self) -> BRepTools_WireExplorer:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Python addition: see __iter__."""

    @overload
    def Init(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Initializes an exploration of the wire <W>."""

    @overload
    def Init(self, W: nanoocp.TopoDS.TopoDS_Wire, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Initializes an exploration of the wire <W>.
        F is used to select the edge connected to the
        previous in the parametric representation of <F>.
        """

    @overload
    def Init(self, W: nanoocp.TopoDS.TopoDS_Wire, F: nanoocp.TopoDS.TopoDS_Face, UMin: float, UMax: float, VMin: float, VMax: float) -> None:
        """
        Initializes an exploration of the wire <W>.
        F is used to select the edge connected to the
        previous in the parametric representation of <F>.
        <UMIn>, <UMax>, <VMin>, <VMax> - the UV bounds of the face <F>.
        """

    def More(self) -> bool:
        """Returns True if there is a current edge."""

    def Next(self) -> None:
        """Proceeds to the next edge."""

    def Current(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns the current edge."""

    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Returns an Orientation for the current edge."""

    def CurrentVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Returns the vertex connecting the current edge to
        the previous one.
        """

    def Clear(self) -> None:
        """Clears the content of the explorer."""

class BRepTools_PurgeLocations:
    """
    Removes location datums, which satisfy conditions:
    aTrsf.IsNegative() || (std::abs(std::abs(aTrsf.ScaleFactor()) - 1.) >
    TopLoc_Location::ScalePrec()) from all locations of shape and its subshapes
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepTools_PurgeLocations) -> None: ...

    def Perform(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Removes all locations correspondingly to criterium from theShape."""

    def GetResult(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns shape with removed locations."""

    def IsDone(self) -> bool: ...

    def ModifiedShape(self, theInitShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns modified shape obtained from initial shape."""
