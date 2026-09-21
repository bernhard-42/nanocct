"""OCCT package BRepOffset (toolkit TKOffset)"""

import enum
from typing import overload

import nanoocp.BRepAlgo
import nanoocp.BRepTools
import nanoocp.ChFiDS
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.gp


class BRepOffset_Status(enum.IntEnum):
    """
    status of an offset face
    Good :
    Reversed : e.g. Offset > Radius of a cylinder
    Degenerated : e.g. Offset = Radius of a cylinder
    Unknown : e.g. for a Beziersurf
    """

    BRepOffset_Good = 0

    BRepOffset_Reversed = 1

    BRepOffset_Degenerated = 2

    BRepOffset_Unknown = 3

BRepOffset_Good: BRepOffset_Status = BRepOffset_Status.BRepOffset_Good

BRepOffset_Reversed: BRepOffset_Status = BRepOffset_Status.BRepOffset_Reversed

BRepOffset_Degenerated: BRepOffset_Status = BRepOffset_Status.BRepOffset_Degenerated

BRepOffset_Unknown: BRepOffset_Status = BRepOffset_Status.BRepOffset_Unknown

class BRepOffset_Error(enum.IntEnum):
    BRepOffset_NoError = 0

    BRepOffset_UnknownError = 1

    BRepOffset_BadNormalsOnGeometry = 2

    BRepOffset_C0Geometry = 3

    BRepOffset_NullOffset = 4

    BRepOffset_NotConnectedShell = 5

    BRepOffset_CannotTrimEdges = 6

    BRepOffset_CannotFuseVertices = 7

    BRepOffset_CannotExtentEdge = 8

    BRepOffset_UserBreak = 9

    BRepOffset_MixedConnectivity = 10

BRepOffset_NoError: BRepOffset_Error = BRepOffset_Error.BRepOffset_NoError

BRepOffset_UnknownError: BRepOffset_Error = BRepOffset_Error.BRepOffset_UnknownError

BRepOffset_BadNormalsOnGeometry: BRepOffset_Error = BRepOffset_Error.BRepOffset_BadNormalsOnGeometry

BRepOffset_C0Geometry: BRepOffset_Error = BRepOffset_Error.BRepOffset_C0Geometry

BRepOffset_NullOffset: BRepOffset_Error = BRepOffset_Error.BRepOffset_NullOffset

BRepOffset_NotConnectedShell: BRepOffset_Error = BRepOffset_Error.BRepOffset_NotConnectedShell

BRepOffset_CannotTrimEdges: BRepOffset_Error = BRepOffset_Error.BRepOffset_CannotTrimEdges

BRepOffset_CannotFuseVertices: BRepOffset_Error = BRepOffset_Error.BRepOffset_CannotFuseVertices

BRepOffset_CannotExtentEdge: BRepOffset_Error = BRepOffset_Error.BRepOffset_CannotExtentEdge

BRepOffset_UserBreak: BRepOffset_Error = BRepOffset_Error.BRepOffset_UserBreak

BRepOffset_MixedConnectivity: BRepOffset_Error = BRepOffset_Error.BRepOffset_MixedConnectivity

class BRepOffset_Mode(enum.IntEnum):
    """
    Lists the offset modes. These are the following:
    - BRepOffset_Skin which describes the offset along
    the surface of a solid, used to obtain a manifold topological space,
    - BRepOffset_Pipe which describes the offset of a
    curve, used to obtain a pre-surface,
    - BRepOffset_RectoVerso which describes the offset
    of a given surface shell along both sides of the surface.
    """

    BRepOffset_Skin = 0

    BRepOffset_Pipe = 1

    BRepOffset_RectoVerso = 2

BRepOffset_Skin: BRepOffset_Mode = BRepOffset_Mode.BRepOffset_Skin

BRepOffset_Pipe: BRepOffset_Mode = BRepOffset_Mode.BRepOffset_Pipe

BRepOffset_RectoVerso: BRepOffset_Mode = BRepOffset_Mode.BRepOffset_RectoVerso

class BRepOffsetSimple_Status(enum.IntEnum):
    BRepOffsetSimple_OK = 0

    BRepOffsetSimple_NullInputShape = 1

    BRepOffsetSimple_ErrorOffsetComputation = 2

    BRepOffsetSimple_ErrorWallFaceComputation = 3

    BRepOffsetSimple_ErrorInvalidNbShells = 4

    BRepOffsetSimple_ErrorNonClosedShell = 5

BRepOffsetSimple_OK: BRepOffsetSimple_Status = BRepOffsetSimple_Status.BRepOffsetSimple_OK

BRepOffsetSimple_NullInputShape: BRepOffsetSimple_Status = ...

BRepOffsetSimple_ErrorOffsetComputation: BRepOffsetSimple_Status = ...

BRepOffsetSimple_ErrorWallFaceComputation: BRepOffsetSimple_Status = ...

BRepOffsetSimple_ErrorInvalidNbShells: BRepOffsetSimple_Status = ...

BRepOffsetSimple_ErrorNonClosedShell: BRepOffsetSimple_Status = ...

class BRepOffset:
    """Auxiliary tools for offset algorithms"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepOffset) -> None: ...

    @staticmethod
    def Surface(Surface: nanoocp.Geom.Geom_Surface | None, Offset: float, allowC0: bool = False) -> tuple[nanoocp.Geom.Geom_Surface, BRepOffset_Status]:
        """
        returns the Offset surface computed from the
        surface <Surface> at an OffsetDistance <Offset>.

        If possible, this method returns the real type of
        the surface ( e.g. An Offset of a plane is a plane).

        If no particular case is detected, the returned
        surface will have the Type Geom_OffsetSurface.
        Parameter allowC0 is then passed as last argument to
        constructor of Geom_OffsetSurface.
        """

    @staticmethod
    def CollapseSingularities(theSurface: nanoocp.Geom.Geom_Surface | None, theFace: nanoocp.TopoDS.TopoDS_Face, thePrecision: float) -> nanoocp.Geom.Geom_Surface:
        """
        Preprocess surface to be offset (bspline, bezier, or revolution based on
        bspline or bezier curve), by collapsing each singular side to single point.

        This is to avoid possible flipping of normal at the singularity
        of the surface due to non-zero distance between the poles that
        logically should be in one point (singularity).

        The (parametric) side of the surface is considered to be singularity if face
        has degenerated edge whose vertex encompasses (by its tolerance) all points on that side,
        or if all poles defining that side fit into sphere with radius thePrecision.

        Returns either original surface or its modified copy (if some poles have been moved).
        """

class BRepOffset_Interval:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, U1: float, U2: float, Type: nanoocp.ChFiDS.ChFiDS_TypeOfConcavity) -> None: ...

    @overload
    def __init__(self, theOther: BRepOffset_Interval) -> None: ...

    @overload
    def First(self, U: float) -> None: ...

    @overload
    def First(self) -> float: ...

    @overload
    def Last(self, U: float) -> None: ...

    @overload
    def Last(self) -> float: ...

    @overload
    def Type(self, T: nanoocp.ChFiDS.ChFiDS_TypeOfConcavity) -> None: ...

    @overload
    def Type(self) -> nanoocp.ChFiDS.ChFiDS_TypeOfConcavity: ...

class BRepOffset_Analyse:
    """
    Analyses the shape to find the parts of edges
    connecting the convex, concave or tangent faces.
    """

    @overload
    def __init__(self) -> None:
        """
        @name Constructors
        Empty c-tor
        """

    @overload
    def __init__(self, theS: nanoocp.TopoDS.TopoDS_Shape, theAngle: float) -> None:
        """C-tor performing the job inside"""

    @overload
    def __init__(self, theOther: BRepOffset_Analyse) -> None: ...

    def Perform(self, theS: nanoocp.TopoDS.TopoDS_Shape, theAngle: float, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        @name Performing analysis
        Performs the analysis
        """

    def IsDone(self) -> bool:
        """
        @name Results
        Returns status of the algorithm
        """

    def Type(self, theE: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.NCollection.NCollection_List[nanoocp.BRepOffset.BRepOffset_Interval]:
        """Returns the connectivity type of the edge"""

    @overload
    def Edges(self, theV: nanoocp.TopoDS.TopoDS_Vertex, theType: nanoocp.ChFiDS.ChFiDS_TypeOfConcavity, theL: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Stores in <L> all the edges of Type <T>
        on the vertex <V>.
        """

    @overload
    def Edges(self, theF: nanoocp.TopoDS.TopoDS_Face, theType: nanoocp.ChFiDS.ChFiDS_TypeOfConcavity, theL: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Stores in <L> all the edges of Type <T>
        on the face <F>.
        """

    def TangentEdges(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theVertex: nanoocp.TopoDS.TopoDS_Vertex, theEdges: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        set in <Edges> all the Edges of <Shape> which are
        tangent to <Edge> at the vertex <Vertex>.
        """

    def HasAncestor(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Checks if the given shape has ancestors"""

    def Ancestors(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns ancestors for the shape"""

    @overload
    def Explode(self, theL: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theType: nanoocp.ChFiDS.ChFiDS_TypeOfConcavity) -> None:
        """
        Explode in compounds of faces where
        all the connex edges are of type <Side>
        """

    @overload
    def Explode(self, theL: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theType1: nanoocp.ChFiDS.ChFiDS_TypeOfConcavity, theType2: nanoocp.ChFiDS.ChFiDS_TypeOfConcavity) -> None:
        """
        Explode in compounds of faces where
        all the connex edges are of type <Side1> or <Side2>
        """

    @overload
    def AddFaces(self, theFace: nanoocp.TopoDS.TopoDS_Face, theCo: nanoocp.TopoDS.TopoDS_Compound, theMap: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theType: nanoocp.ChFiDS.ChFiDS_TypeOfConcavity) -> None:
        """
        Add in <CO> the faces of the shell containing <Face>
        where all the connex edges are of type <Side>.
        """

    @overload
    def AddFaces(self, theFace: nanoocp.TopoDS.TopoDS_Face, theCo: nanoocp.TopoDS.TopoDS_Compound, theMap: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theType1: nanoocp.ChFiDS.ChFiDS_TypeOfConcavity, theType2: nanoocp.ChFiDS.ChFiDS_TypeOfConcavity) -> None:
        """
        Add in <CO> the faces of the shell containing <Face>
        where all the connex edges are of type <Side1> or <Side2>.
        """

    def SetOffsetValue(self, theOffset: float) -> None: ...

    def SetFaceOffsetMap(self, theMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, float, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """Sets the face-offset data map to analyze tangential cases"""

    def NewFaces(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the new faces constructed between tangent faces
        having different offset values on the shape
        """

    def Generated(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the new face constructed for the edge connecting
        the two tangent faces having different offset values
        """

    def HasGenerated(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Checks if the edge has generated a new face."""

    def EdgeReplacement(self, theFace: nanoocp.TopoDS.TopoDS_Face, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the replacement of the edge in the face.
        If no replacement exists, returns the edge
        """

    def Descendants(self, theS: nanoocp.TopoDS.TopoDS_Shape, theUpdate: bool = False) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the shape descendants."""

    def Clear(self) -> None:
        """
        @name Clearing the content
        Clears the content of the algorithm
        """

class BRepOffset_Inter2d:
    """
    Computes the intersections between edges on a face
    stores result is SD as AsDes from BRepOffset.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepOffset_Inter2d) -> None: ...

    @staticmethod
    def Compute(AsDes: nanoocp.BRepAlgo.BRepAlgo_AsDes | None, F: nanoocp.TopoDS.TopoDS_Face, NewEdges: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], Tol: float, theEdgeIntEdges: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], theDMVV: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], theRange: nanoocp.Message.Message_ProgressRange) -> None:
        """
        Computes the intersections between the edges stored
        is AsDes as descendants of <F> . Intersections is computed
        between two edges if one of them is bound in NewEdges.
        When all faces of the shape are treated the intersection
        vertices have to be fused using the FuseVertices method.
        theDMVV contains the vertices that should be fused
        """

    @staticmethod
    def ConnexIntByInt(FI: nanoocp.TopoDS.TopoDS_Face, OFI: BRepOffset_Offset, MES: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], Build: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theAsDes: nanoocp.BRepAlgo.BRepAlgo_AsDes | None, AsDes2d: nanoocp.BRepAlgo.BRepAlgo_AsDes | None, Offset: float, Tol: float, Analyse: BRepOffset_Analyse, FacesWithVerts: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theImageVV: nanoocp.BRepAlgo.BRepAlgo_Image, theEdgeIntEdges: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], theDMVV: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], theRange: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Computes the intersection between the offset edges of the <FI>.
        All intersection vertices will be stored in AsDes2d.
        When all faces of the shape are treated the intersection vertices
        have to be fused using the FuseVertices method.
        theDMVV contains the vertices that should be fused.
        """

    @staticmethod
    def ConnexIntByIntInVert(FI: nanoocp.TopoDS.TopoDS_Face, OFI: BRepOffset_Offset, MES: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], Build: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], AsDes: nanoocp.BRepAlgo.BRepAlgo_AsDes | None, AsDes2d: nanoocp.BRepAlgo.BRepAlgo_AsDes | None, Tol: float, Analyse: BRepOffset_Analyse, theDMVV: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], theRange: nanoocp.Message.Message_ProgressRange) -> None:
        """
        Computes the intersection between the offset edges generated
        from vertices and stored into AsDes as descendants of the <FI>.
        All intersection vertices will be stored in AsDes2d.
        When all faces of the shape are treated the intersection vertices
        have to be fused using the FuseVertices method.
        theDMVV contains the vertices that should be fused.
        """

    @staticmethod
    def FuseVertices(theDMVV: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], theAsDes: nanoocp.BRepAlgo.BRepAlgo_AsDes | None, theImageVV: nanoocp.BRepAlgo.BRepAlgo_Image) -> bool:
        """
        Fuses the chains of vertices in the theDMVV
        and updates AsDes by replacing the old vertices
        with the new ones.
        """

    @staticmethod
    def ExtentEdge(E: nanoocp.TopoDS.TopoDS_Edge, NE: nanoocp.TopoDS.TopoDS_Edge, theOffset: float) -> bool:
        """extents the edge"""

class BRepOffset_Offset:
    """
    This class compute elemenary offset surface.
    Evaluate the offset generated :
    1 - from a face.
    2 - from an edge.
    3 - from a vertex.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Face: nanoocp.TopoDS.TopoDS_Face, Offset: float, OffsetOutside: bool = True, JoinType: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc) -> None: ...

    @overload
    def __init__(self, Face: nanoocp.TopoDS.TopoDS_Face, Offset: float, Created: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], OffsetOutside: bool = True, JoinType: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc) -> None:
        """
        This method will be called when you want to share
        the edges soon generated from an other face.
        e.g. when two faces are tangents the common edge
        will generate only one edge ( no pipe).

        The Map will be fill as follow:

        Created(E) = E'
        with:
        E = an edge of <Face>
        E' = the image of E in the offsetting of another
        face sharing E with a continuity at least G1
        """

    @overload
    def __init__(self, Vertex: nanoocp.TopoDS.TopoDS_Vertex, LEdge: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], Offset: float, Polynomial: bool = False, Tol: float = 0.0001, Conti: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None:
        """
        Tol and Conti are only used if Polynomial is True
        (Used to perform the approximation)
        """

    @overload
    def __init__(self, Path: nanoocp.TopoDS.TopoDS_Edge, Edge1: nanoocp.TopoDS.TopoDS_Edge, Edge2: nanoocp.TopoDS.TopoDS_Edge, Offset: float, Polynomial: bool = False, Tol: float = 0.0001, Conti: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None: ...

    @overload
    def __init__(self, Path: nanoocp.TopoDS.TopoDS_Edge, Edge1: nanoocp.TopoDS.TopoDS_Edge, Edge2: nanoocp.TopoDS.TopoDS_Edge, Offset: float, FirstEdge: nanoocp.TopoDS.TopoDS_Edge, LastEdge: nanoocp.TopoDS.TopoDS_Edge, Polynomial: bool = False, Tol: float = 0.0001, Conti: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None: ...

    @overload
    def __init__(self, theOther: BRepOffset_Offset) -> None: ...

    @overload
    def Init(self, Face: nanoocp.TopoDS.TopoDS_Face, Offset: float, OffsetOutside: bool = True, JoinType: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc) -> None: ...

    @overload
    def Init(self, Face: nanoocp.TopoDS.TopoDS_Face, Offset: float, Created: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], OffsetOutside: bool = True, JoinType: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc) -> None: ...

    @overload
    def Init(self, Path: nanoocp.TopoDS.TopoDS_Edge, Edge1: nanoocp.TopoDS.TopoDS_Edge, Edge2: nanoocp.TopoDS.TopoDS_Edge, Offset: float, Polynomial: bool = False, Tol: float = 0.0001, Conti: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None: ...

    @overload
    def Init(self, Path: nanoocp.TopoDS.TopoDS_Edge, Edge1: nanoocp.TopoDS.TopoDS_Edge, Edge2: nanoocp.TopoDS.TopoDS_Edge, Offset: float, FirstEdge: nanoocp.TopoDS.TopoDS_Edge, LastEdge: nanoocp.TopoDS.TopoDS_Edge, Polynomial: bool = False, Tol: float = 0.0001, Conti: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None: ...

    @overload
    def Init(self, Vertex: nanoocp.TopoDS.TopoDS_Vertex, LEdge: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], Offset: float, Polynomial: bool = False, Tol: float = 0.0001, Conti: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None:
        """
        Tol and Conti are only used if Polynomial is True
        (Used to perform the approximation)
        """

    @overload
    def Init(self, Edge: nanoocp.TopoDS.TopoDS_Edge, Offset: float) -> None:
        """Only used in Rolling Ball. Pipe on Free Boundary"""

    def InitialShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def Generated(self, Shape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Status(self) -> BRepOffset_Status: ...

class BRepOffset_Inter3d:
    """
    Computes the connection of the offset and not offset faces
    according to the connection type required.
    Store the result in AsDes tool.
    """

    @overload
    def __init__(self, AsDes: nanoocp.BRepAlgo.BRepAlgo_AsDes | None, Side: nanoocp.TopAbs.TopAbs_State, Tol: float) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BRepOffset_Inter3d) -> None: ...

    def CompletInt(self, SetOfFaces: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], InitOffsetFace: nanoocp.BRepAlgo.BRepAlgo_Image, theRange: nanoocp.Message.Message_ProgressRange) -> None: ...

    def FaceInter(self, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, InitOffsetFace: nanoocp.BRepAlgo.BRepAlgo_Image) -> None:
        """Computes intersection of pair of faces"""

    def ConnexIntByArc(self, SetOfFaces: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], ShapeInit: nanoocp.TopoDS.TopoDS_Shape, Analyse: BRepOffset_Analyse, InitOffsetFace: nanoocp.BRepAlgo.BRepAlgo_Image, theRange: nanoocp.Message.Message_ProgressRange) -> None:
        """
        Computes connections of the offset faces that have to be connected by arcs.
        """

    def ConnexIntByInt(self, SI: nanoocp.TopoDS.TopoDS_Shape, MapSF: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepOffset.BRepOffset_Offset, nanoocp.TopTools.TopTools_ShapeMapHasher], A: BRepOffset_Analyse, MES: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], Build: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], Failed: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theRange: nanoocp.Message.Message_ProgressRange, bIsPlanar: bool = False) -> None:
        """
        Computes intersection of the offset faces that have to be connected by
        sharp edges, i.e. it computes intersection between extended offset faces.
        """

    def ContextIntByInt(self, ContextFaces: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], ExtentContext: bool, MapSF: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepOffset.BRepOffset_Offset, nanoocp.TopTools.TopTools_ShapeMapHasher], A: BRepOffset_Analyse, MES: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], Build: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], Failed: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theRange: nanoocp.Message.Message_ProgressRange, bIsPlanar: bool = False) -> None:
        """Computes intersection with not offset faces ."""

    def ContextIntByArc(self, ContextFaces: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], ExtentContext: bool, Analyse: BRepOffset_Analyse, InitOffsetFace: nanoocp.BRepAlgo.BRepAlgo_Image, InitOffsetEdge: nanoocp.BRepAlgo.BRepAlgo_Image, theRange: nanoocp.Message.Message_ProgressRange) -> None:
        """
        Computes connections of the not offset faces that have to be connected by arcs
        """

    def SetDone(self, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Marks the pair of faces as already intersected"""

    def IsDone(self, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """Checks if the pair of faces has already been treated."""

    def TouchedFaces(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """Returns touched faces"""

    def AsDes(self) -> nanoocp.BRepAlgo.BRepAlgo_AsDes:
        """Returns AsDes tool"""

    def NewEdges(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """Returns new edges"""

class BRepOffset_MakeLoops:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepOffset_MakeLoops) -> None: ...

    def Build(self, LF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], AsDes: nanoocp.BRepAlgo.BRepAlgo_AsDes | None, Image: nanoocp.BRepAlgo.BRepAlgo_Image, theImageVV: nanoocp.BRepAlgo.BRepAlgo_Image, theRange: nanoocp.Message.Message_ProgressRange) -> None: ...

    def BuildOnContext(self, LContext: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], Analyse: BRepOffset_Analyse, AsDes: nanoocp.BRepAlgo.BRepAlgo_AsDes | None, Image: nanoocp.BRepAlgo.BRepAlgo_Image, InSide: bool, theRange: nanoocp.Message.Message_ProgressRange) -> None: ...

    def BuildFaces(self, LF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], AsDes: nanoocp.BRepAlgo.BRepAlgo_AsDes | None, Image: nanoocp.BRepAlgo.BRepAlgo_Image, theRange: nanoocp.Message.Message_ProgressRange) -> None: ...

class BRepOffset_MakeOffset:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, Offset: float, Tol: float, Mode: BRepOffset_Mode = BRepOffset_Mode.BRepOffset_Skin, Intersection: bool = False, SelfInter: bool = False, Join: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, Thickening: bool = False, RemoveIntEdges: bool = False, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def __init__(self, theOther: BRepOffset_MakeOffset) -> None: ...

    def Initialize(self, S: nanoocp.TopoDS.TopoDS_Shape, Offset: float, Tol: float, Mode: BRepOffset_Mode = BRepOffset_Mode.BRepOffset_Skin, Intersection: bool = False, SelfInter: bool = False, Join: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, Thickening: bool = False, RemoveIntEdges: bool = False) -> None: ...

    def Clear(self) -> None: ...

    def AllowLinearization(self, theIsAllowed: bool) -> None:
        """Changes the flag allowing the linearization"""

    def AddFace(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Add Closing Faces, <F> has to be in the initial
        shape S.
        """

    def SetOffsetOnFace(self, F: nanoocp.TopoDS.TopoDS_Face, Off: float) -> None:
        """set the offset <Off> on the Face <F>"""

    def MakeOffsetShape(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    def MakeThickSolid(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    def IsDone(self) -> bool: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def InitShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Error(self) -> BRepOffset_Error:
        """returns information about offset state."""

    def OffsetFacesFromShapes(self) -> nanoocp.BRepAlgo.BRepAlgo_Image:
        """
        Returns <Image> containing links between initials
        shapes and offset faces.
        """

    def GetJoinType(self) -> nanoocp.GeomAbs.GeomAbs_JoinType:
        """Returns myJoin."""

    def OffsetEdgesFromShapes(self) -> nanoocp.BRepAlgo.BRepAlgo_Image:
        """
        Returns <Image> containing links between initials
        shapes and offset edges.
        """

    def ClosingFaces(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """Returns the list of closing faces stores by AddFace"""

    def CheckInputData(self, theRange: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Makes pre analysis of possibility offset perform. Use method Error() to get more information.
        Finds first error. List of checks:
        1) Check for existence object with non-null offset.
        2) Check for connectivity in offset shell.
        3) Check continuity of input surfaces.
        4) Check for normals existence on grid.
        @return True if possible make computations and false otherwise.
        """

    def GetBadShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return bad shape, which obtained in CheckInputData."""

    def Generated(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        @name History methods
        Returns the list of shapes generated from the shape <S>.
        """

    def Modified(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of shapes modified from the shape <S>."""

    def IsDeleted(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns true if the shape S has been deleted."""

class BRepOffset_MakeSimpleOffset:
    """
    Limitations:
    According to the algorithm nature result depends on the smoothness of input data. Smooth
    (G1-continuity) input shape will lead to the good result.

    The possible drawback of the simple algorithm is that it leads, in general case, to tolerance
    increasing. The tolerances have to grow in order to cover the gaps between the neighbor faces in
    the output. It should be noted that the actual tolerance growth depends on the offset distance
    and the quality of joints between the input faces. Anyway the good input shell (smooth
    connections between adjacent faces) will lead to good result.
    """

    @overload
    def __init__(self) -> None:
        """Constructor. Does nothing."""

    @overload
    def __init__(self, theInputShape: nanoocp.TopoDS.TopoDS_Shape, theOffsetValue: float) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: BRepOffset_MakeSimpleOffset) -> None: ...

    def Initialize(self, theInputShape: nanoocp.TopoDS.TopoDS_Shape, theOffsetValue: float) -> None:
        """Initialise shape for modifications."""

    def Perform(self) -> None:
        """Computes offset shape."""

    def GetErrorMessage(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Gets error message."""

    def GetError(self) -> BRepOffsetSimple_Status:
        """Gets error code."""

    def GetBuildSolidFlag(self) -> bool:
        """Gets solid building flag."""

    def SetBuildSolidFlag(self, theBuildFlag: bool) -> None:
        """Sets solid building flag."""

    def GetOffsetValue(self) -> float:
        """Gets offset value."""

    def SetOffsetValue(self, theOffsetValue: float) -> None:
        """Sets offset value."""

    def GetTolerance(self) -> float:
        """Gets tolerance (used for handling singularities)."""

    def SetTolerance(self, theValue: float) -> None:
        """Sets tolerance (used for handling singularities)."""

    def IsDone(self) -> bool:
        """Gets done state."""

    def GetResultShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns result shape."""

    def GetSafeOffset(self, theExpectedToler: float) -> float:
        """Computes max safe offset value for the given tolerance."""

    def Generated(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns result shape for the given one (if exists)."""

    def Modified(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns modified shape for the given one (if exists)."""

class BRepOffset_SimpleOffset(nanoocp.BRepTools.BRepTools_Modification):
    """
    This class represents mechanism of simple offset algorithm
    i.e. topology-preserve offset construction without intersection.

    The list below shows mapping scheme:
    - Each surface is mapped to its geometric offset surface.
    - For each edge, pcurves are mapped to the same pcurves on offset surfaces.
    - For each edge, 3d curve is constructed by re-approximation of pcurve on the first offset face.
    - Position of each vertex in a result shell is computed as average point of all ends of edges
    shared by that vertex.
    - Tolerances are updated according to the resulting geometry.
    """

    def __init__(self, theInputShape: nanoocp.TopoDS.TopoDS_Shape, theOffsetValue: float, theTolerance: float) -> None:
        """
        Constructor.
        @param theInputShape shape to be offset
        @param theOffsetValue offset distance (signed)
        @param theTolerance tolerance for handling singular points
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewSurface(self, F: nanoocp.TopoDS.TopoDS_Face, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Surface, float, bool, bool]:
        """
        Returns true if the face <F> has been
        modified. In this case, <S> is the new geometric
        support of the face, <L> the new location,
        <Tol> the new tolerance. <RevWires> has to be set to
        true when the modification reverses the
        normal of the surface. (the wires have to be
        reversed). <RevFace> has to be set to
        true if the orientation of the modified
        face changes in the shells which contain it.
        Here, <RevFace> will return true if the
        gp_Trsf is negative.
        """

    def NewCurve(self, E: nanoocp.TopoDS.TopoDS_Edge, L: nanoocp.TopLoc.TopLoc_Location) -> tuple[bool, nanoocp.Geom.Geom_Curve, float]:
        """
        Returns true if the edge <E> has been
        modified. In this case, <C> is the new geometric
        support of the edge, <L> the new location,
        <Tol> the new tolerance. Otherwise, returns
        false, and <C>, <L>,
        <Tol> are not significant.
        """

    def NewPoint(self, V: nanoocp.TopoDS.TopoDS_Vertex, P: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """
        Returns true if the vertex <V> has been
        modified. In this case, <P> is the new geometric
        support of the vertex, <Tol> the new tolerance.
        Otherwise, returns false, and <P>,
        <Tol> are not significant.
        """

    def NewCurve2d(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float]:
        """
        Returns true if the edge <E> has a new
        curve on surface on the face <F>. In this case,
        <C> is the new geometric support of the edge,
        <L> the new location, <Tol> the new tolerance.
        Otherwise, returns false, and <C>, <L>,
        <Tol> are not significant.
        """

    def NewParameter(self, V: nanoocp.TopoDS.TopoDS_Vertex, E: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]:
        """
        Returns true if the Vertex <V> has a new
        parameter on the edge <E>. In this case,
        <P> is the parameter, <Tol> the new tolerance.
        Otherwise, returns false, and <P>,
        <Tol> are not significant.
        """

    def Continuity(self, E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, NewE: nanoocp.TopoDS.TopoDS_Edge, NewF1: nanoocp.TopoDS.TopoDS_Face, NewF2: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Returns the continuity of <NewE> between <NewF1>
        and <NewF2>.

        <NewE> is the new edge created from <E>. <NewF1>
        (resp. <NewF2>) is the new face created from <F1>
        (resp. <F2>).
        """

class BRepOffset_Tool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepOffset_Tool) -> None: ...

    @staticmethod
    def EdgeVertices(E: nanoocp.TopoDS.TopoDS_Edge, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        <V1> is the FirstVertex ,<V2> is the Last Vertex of <Edge>
        taking account the orientation of Edge.
        """

    @staticmethod
    def OrientSection(E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face) -> tuple[nanoocp.TopAbs.TopAbs_Orientation, nanoocp.TopAbs.TopAbs_Orientation]:
        """
        <E> is a section between <F1> and <F2>. Computes
        <O1> the orientation of <E> in <F1> influenced by <F2>.
        idem for <O2>.
        """

    @overload
    @staticmethod
    def FindCommonShapes(theF1: nanoocp.TopoDS.TopoDS_Face, theF2: nanoocp.TopoDS.TopoDS_Face, theLE: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theLV: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        Looks for the common Vertices and Edges between faces <theF1> and <theF2>.
        Returns TRUE if common shapes have been found.
        <theLE> will contain the found common edges;
        <theLV> will contain the found common vertices.
        """

    @overload
    @staticmethod
    def FindCommonShapes(theS1: nanoocp.TopoDS.TopoDS_Shape, theS2: nanoocp.TopoDS.TopoDS_Shape, theType: nanoocp.TopAbs.TopAbs_ShapeEnum, theLSC: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        Looks for the common shapes of type <theType> between shapes <theS1> and <theS2>.
        Returns TRUE if common shapes have been found.
        <theLSC> will contain the found common shapes.
        """

    @staticmethod
    def Inter3D(F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, LInt1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LInt2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], Side: nanoocp.TopAbs.TopAbs_State, RefEdge: nanoocp.TopoDS.TopoDS_Edge, RefFace1: nanoocp.TopoDS.TopoDS_Face, RefFace2: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Computes the Section between <F1> and <F2> the
        edges solution are stored in <LInt1> with the
        orientation on <F1>, the sames edges are stored in
        <Lint2> with the orientation on <F2>.
        """

    @staticmethod
    def TryProject(F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, Edges: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LInt1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LInt2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], Side: nanoocp.TopAbs.TopAbs_State, TolConf: float) -> bool:
        """
        Find if the edges <Edges> of the face <F2> are on
        the face <F1>.
        Set in <LInt1> <LInt2> the updated edges.
        If all the edges are computed, returns true.
        """

    @staticmethod
    def PipeInter(F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, LInt1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LInt2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], Side: nanoocp.TopAbs.TopAbs_State) -> None: ...

    @staticmethod
    def Inter2d(F: nanoocp.TopoDS.TopoDS_Face, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, LV: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], Tol: float) -> None: ...

    @staticmethod
    def InterOrExtent(F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, LInt1: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], LInt2: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], Side: nanoocp.TopAbs.TopAbs_State) -> None: ...

    @staticmethod
    def CheckBounds(F: nanoocp.TopoDS.TopoDS_Face, Analyse: BRepOffset_Analyse) -> tuple[bool, bool, bool]: ...

    @staticmethod
    def EnLargeFace(F: nanoocp.TopoDS.TopoDS_Face, NF: nanoocp.TopoDS.TopoDS_Face, ChangeGeom: bool, UpDatePCurve: bool = False, enlargeU: bool = True, enlargeVfirst: bool = True, enlargeVlast: bool = True, theExtensionMode: int = 1, theLenBeforeUfirst: float = -1.0, theLenAfterUlast: float = -1.0, theLenBeforeVfirst: float = -1.0, theLenAfterVlast: float = -1.0) -> bool:
        """
        Returns True if The Surface of <NF> has changed.
        if <ChangeGeom> is TRUE the surface can be
        changed .
        if <UpdatePCurve> is TRUE, update the pcurves of the
        edges of <F> on the new surface if the surface has been changed.
        <enlargeU>, <enlargeVfirst>, <enlargeVlast> allow or forbid
        enlargement in U and V directions correspondingly.
        <theExtensionMode> is a mode of extension of the surface of the face:
        if <theExtensionMode> equals 1, potentially infinite surfaces are extended by maximum value,
        and limited surfaces are extended by 25%.
        if <theExtensionMode> equals 2, potentially infinite surfaces are extended by
        10*(correspondent size of face),
        and limited surfaces are extended by 100%.
        <theLenBeforeUfirst>, <theLenAfterUlast>, <theLenBeforeVfirst>, <theLenAfterVlast>
        set the values of enlargement on correspondent directions.
        If some of them equals -1, the default value of enlargement is used.
        """

    @staticmethod
    def ExtentFace(F: nanoocp.TopoDS.TopoDS_Face, ConstShapes: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], ToBuild: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], Side: nanoocp.TopAbs.TopAbs_State, TolConf: float, NF: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @staticmethod
    def BuildNeighbour(W: nanoocp.TopoDS.TopoDS_Wire, F: nanoocp.TopoDS.TopoDS_Face, NOnV1: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], NOnV2: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        Via the wire explorer store in <NOnV1> for
        an Edge <E> of <W> his Edge neighbour on the first
        vertex <V1> of <E>.
        Store in NOnV2 the Neighbour of <E>on the last
        vertex <V2> of <E>.
        """

    @staticmethod
    def MapVertexEdges(S: nanoocp.TopoDS.TopoDS_Shape, MVE: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        Store in MVE for a vertex <V> in <S> the incident
        edges <E> in <S>.
        An Edge is Store only one Time for a vertex.
        """

    @staticmethod
    def Deboucle3D(S: nanoocp.TopoDS.TopoDS_Shape, Boundary: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Remove the non valid part of an offsetshape
        1 - Remove all the free boundary and the faces
        connex to such edges.
        2 - Remove all the shapes not valid in the result
        (according to the side of offsetting)
        in this version only the first point is implemented.
        """

    @staticmethod
    def CorrectOrientation(SI: nanoocp.TopoDS.TopoDS_Shape, NewEdges: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], AsDes: nanoocp.BRepAlgo.BRepAlgo_AsDes | None, InitOffset: nanoocp.BRepAlgo.BRepAlgo_Image, Offset: float) -> None: ...

    @staticmethod
    def Gabarit(aCurve: nanoocp.Geom.Geom_Curve | None) -> float: ...

    @staticmethod
    def CheckPlanesNormals(theFace1: nanoocp.TopoDS.TopoDS_Face, theFace2: nanoocp.TopoDS.TopoDS_Face, theTolAng: float = 1e-08) -> bool:
        """
        Compares the normal directions of the planar faces and returns
        TRUE if the directions are the same with the given precision.
        """

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.BRepOffset
import nanoocp.TopTools
BRepOffset_DataMapOfShapeOffset = nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepOffset.BRepOffset_Offset, nanoocp.TopTools.TopTools_ShapeMapHasher]
BRepOffset_ListOfInterval = nanoocp.NCollection.NCollection_List[nanoocp.BRepOffset.BRepOffset_Interval]
