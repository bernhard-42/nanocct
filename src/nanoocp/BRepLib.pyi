"""OCCT package BRepLib (toolkit TKTopAlgo)"""

import enum
from typing import overload

import nanoocp.Adaptor3d
import nanoocp.BRepTools
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.gp
import nanoocp.TopTools


class BRepLib_EdgeError(enum.IntEnum):
    """
    Errors that can occur at edge construction.
    no error
    """

    BRepLib_EdgeDone = 0

    BRepLib_PointProjectionFailed = 1

    BRepLib_ParameterOutOfRange = 2

    BRepLib_DifferentPointsOnClosedCurve = 3

    BRepLib_PointWithInfiniteParameter = 4

    BRepLib_DifferentsPointAndParameter = 5

    BRepLib_LineThroughIdenticPoints = 6

BRepLib_EdgeDone: BRepLib_EdgeError = BRepLib_EdgeError.BRepLib_EdgeDone

BRepLib_PointProjectionFailed: BRepLib_EdgeError = BRepLib_EdgeError.BRepLib_PointProjectionFailed

BRepLib_ParameterOutOfRange: BRepLib_EdgeError = BRepLib_EdgeError.BRepLib_ParameterOutOfRange

BRepLib_DifferentPointsOnClosedCurve: BRepLib_EdgeError = ...

BRepLib_PointWithInfiniteParameter: BRepLib_EdgeError = ...

BRepLib_DifferentsPointAndParameter: BRepLib_EdgeError = ...

BRepLib_LineThroughIdenticPoints: BRepLib_EdgeError = ...

class BRepLib_FaceError(enum.IntEnum):
    """
    Errors that can occur at face construction.
    no error
    not initialised
    """

    BRepLib_FaceDone = 0

    BRepLib_NoFace = 1

    BRepLib_NotPlanar = 2

    BRepLib_CurveProjectionFailed = 3

    BRepLib_ParametersOutOfRange = 4

BRepLib_FaceDone: BRepLib_FaceError = BRepLib_FaceError.BRepLib_FaceDone

BRepLib_NoFace: BRepLib_FaceError = BRepLib_FaceError.BRepLib_NoFace

BRepLib_NotPlanar: BRepLib_FaceError = BRepLib_FaceError.BRepLib_NotPlanar

BRepLib_CurveProjectionFailed: BRepLib_FaceError = BRepLib_FaceError.BRepLib_CurveProjectionFailed

BRepLib_ParametersOutOfRange: BRepLib_FaceError = BRepLib_FaceError.BRepLib_ParametersOutOfRange

class BRepLib_ShapeModification(enum.IntEnum):
    """Modification type after a topologic operation."""

    BRepLib_Preserved = 0

    BRepLib_Deleted = 1

    BRepLib_Trimmed = 2

    BRepLib_Merged = 3

    BRepLib_BoundaryModified = 4

BRepLib_Preserved: BRepLib_ShapeModification = BRepLib_ShapeModification.BRepLib_Preserved

BRepLib_Deleted: BRepLib_ShapeModification = BRepLib_ShapeModification.BRepLib_Deleted

BRepLib_Trimmed: BRepLib_ShapeModification = BRepLib_ShapeModification.BRepLib_Trimmed

BRepLib_Merged: BRepLib_ShapeModification = BRepLib_ShapeModification.BRepLib_Merged

BRepLib_BoundaryModified: BRepLib_ShapeModification = ...

class BRepLib_ShellError(enum.IntEnum):
    """Errors that can occur at shell construction."""

    BRepLib_ShellDone = 0

    BRepLib_EmptyShell = 1

    BRepLib_DisconnectedShell = 2

    BRepLib_ShellParametersOutOfRange = 3

BRepLib_ShellDone: BRepLib_ShellError = BRepLib_ShellError.BRepLib_ShellDone

BRepLib_EmptyShell: BRepLib_ShellError = BRepLib_ShellError.BRepLib_EmptyShell

BRepLib_DisconnectedShell: BRepLib_ShellError = BRepLib_ShellError.BRepLib_DisconnectedShell

BRepLib_ShellParametersOutOfRange: BRepLib_ShellError = ...

class BRepLib_WireError(enum.IntEnum):
    """
    Errors that can occur at wire construction.
    no error
    """

    BRepLib_WireDone = 0

    BRepLib_EmptyWire = 1

    BRepLib_DisconnectedWire = 2

    BRepLib_NonManifoldWire = 3

BRepLib_WireDone: BRepLib_WireError = BRepLib_WireError.BRepLib_WireDone

BRepLib_EmptyWire: BRepLib_WireError = BRepLib_WireError.BRepLib_EmptyWire

BRepLib_DisconnectedWire: BRepLib_WireError = BRepLib_WireError.BRepLib_DisconnectedWire

BRepLib_NonManifoldWire: BRepLib_WireError = BRepLib_WireError.BRepLib_NonManifoldWire

class BRepLib:
    """
    The BRepLib package provides general utilities for
    BRep.

    * FindSurface : Class to compute a surface through
    a set of edges.

    * Compute missing 3d curve on an edge.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepLib) -> None: ...

    @overload
    @staticmethod
    def Precision(P: float) -> None:
        """
        Computes the max distance between edge
        and its 2d representation on the face.
        Sets the default precision. The current Precision
        is returned.
        """

    @overload
    @staticmethod
    def Precision() -> float:
        """Returns the default precision."""

    @overload
    @staticmethod
    def Plane(P: nanoocp.Geom.Geom_Plane | None) -> None:
        """Sets the current plane to P."""

    @overload
    @staticmethod
    def Plane() -> nanoocp.Geom.Geom_Plane:
        """Returns the current plane."""

    @staticmethod
    def CheckSameRange(E: nanoocp.TopoDS.TopoDS_Edge, Confusion: float = 1e-12) -> bool:
        """
        checks if the Edge is same range IGNORING
        the same range flag of the edge
        Confusion argument is to compare real numbers
        idenpendently of any model space tolerance
        """

    @staticmethod
    def SameRange(E: nanoocp.TopoDS.TopoDS_Edge, Tolerance: float = 1e-05) -> None:
        """
        will make all the curve representation have
        the same range domain for the parameters.
        This will IGNORE the same range flag value
        to proceed.
        If there is a 3D curve there it will the
        range of that curve. If not the first curve representation
        encountered in the list will give its range to
        the all the other curves.
        """

    @staticmethod
    def BuildCurve3d(E: nanoocp.TopoDS.TopoDS_Edge, Tolerance: float = 1e-05, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1, MaxDegree: int = 14, MaxSegment: int = 0) -> bool:
        """
        Computes the 3d curve for the edge <E> if it does
        not exist. Returns True if the curve was computed
        or existed. Returns False if there is no planar
        pcurve or the computation failed.
        <MaxSegment> >= 30 in approximation
        """

    @overload
    @staticmethod
    def BuildCurves3d(S: nanoocp.TopoDS.TopoDS_Shape, Tolerance: float, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1, MaxDegree: int = 14, MaxSegment: int = 0) -> bool:
        """
        Computes the 3d curves for all the edges of <S>
        return False if one of the computation failed.
        <MaxSegment> >= 30 in approximation
        """

    @overload
    @staticmethod
    def BuildCurves3d(S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Computes the 3d curves for all the edges of <S>
        return False if one of the computation failed.
        """

    @staticmethod
    def BuildPCurveForEdgeOnPlane(theE: nanoocp.TopoDS.TopoDS_Edge, theF: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Builds pcurve of edge on face if the surface is plane, and updates the edge.
        """

    @staticmethod
    def BuildPCurveForEdgeOnPlane__Geom2d_Curve__bool(theE: nanoocp.TopoDS.TopoDS_Edge, theF: nanoocp.TopoDS.TopoDS_Face) -> tuple[nanoocp.Geom2d.Geom2d_Curve, bool]:
        """
        BuildPCurveForEdgeOnPlane__Geom2d_Curve__bool: the C++ overload BuildPCurveForEdgeOnPlane(const TopoDS_Edge &, const TopoDS_Face &, occ::handle<Geom2d_Curve> &, bool &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Builds pcurve of edge on face if the surface is plane, but does not update the edge.
        The output are the pcurve and the flag telling that pcurve was built.
        """

    @staticmethod
    def UpdateEdgeTol(E: nanoocp.TopoDS.TopoDS_Edge, MinToleranceRequest: float, MaxToleranceToCheck: float) -> bool:
        """
        Checks if the edge has a Tolerance smaller than
        MaxToleranceToCheck if so it will compute the
        radius of the cylindrical pipe surface that
        MinToleranceRequest is the minimum tolerance before it
        is useful to start testing.
        Usually it should be around 10e-5
        contains all the curve representation of the edge
        returns True if the Edge tolerance had to be updated
        """

    @staticmethod
    def UpdateEdgeTolerance(S: nanoocp.TopoDS.TopoDS_Shape, MinToleranceRequest: float, MaxToleranceToCheck: float) -> bool:
        """
        Checks all the edges of the shape whose
        Tolerance is smaller than MaxToleranceToCheck
        Returns True if at least one edge was updated
        MinToleranceRequest is the minimum tolerance before
        it is useful to start testing.
        Usually it should be around 10e-5

        Warning: The method is very slow as it checks all.
        Use only in interfaces or processing assimilate batch
        """

    @overload
    @staticmethod
    def SameParameter(theEdge: nanoocp.TopoDS.TopoDS_Edge, Tolerance: float = 1e-05) -> None:
        """
        Computes new 2d curve(s) for the edge <theEdge> to have
        the same parameter as the 3d curve.
        The algorithm is not done if the flag SameParameter
        was True on the Edge.
        """

    @overload
    @staticmethod
    def SameParameter(theEdge: nanoocp.TopoDS.TopoDS_Edge, theTolerance: float, IsUseOldEdge: bool) -> tuple[nanoocp.TopoDS.TopoDS_Edge, float]:
        """
        Computes new 2d curve(s) for the edge <theEdge> to have
        the same parameter as the 3d curve.
        The algorithm is not done if the flag SameParameter
        was True on the Edge.
        theNewTol is a new tolerance of vertices of the input edge
        (not applied inside the algorithm, but pre-computed).
        If IsUseOldEdge is true then the input edge will be modified,
        otherwise the new copy of input edge will be created.
        Returns the new edge as a result, can be ignored if IsUseOldEdge is true.
        """

    @overload
    @staticmethod
    def SameParameter(S: nanoocp.TopoDS.TopoDS_Shape, Tolerance: float = 1e-05, forced: bool = False) -> None:
        """
        Computes new 2d curve(s) for all the edges of <S>
        to have the same parameter as the 3d curve.
        The algorithm is not done if the flag SameParameter
        was True on an Edge.
        """

    @overload
    @staticmethod
    def SameParameter(S: nanoocp.TopoDS.TopoDS_Shape, theReshaper: nanoocp.BRepTools.BRepTools_ReShape, Tolerance: float = 1e-05, forced: bool = False) -> None:
        """
        Computes new 2d curve(s) for all the edges of <S>
        to have the same parameter as the 3d curve.
        The algorithm is not done if the flag SameParameter
        was True on an Edge.
        theReshaper is used to record the modifications of input shape <S> to prevent any
        modifications on the shape itself.
        Thus the input shape (and its subshapes) will not be modified, instead the reshaper will
        contain a modified empty-copies of original subshapes as substitutions.
        """

    @overload
    @staticmethod
    def UpdateTolerances(S: nanoocp.TopoDS.TopoDS_Shape, verifyFaceTolerance: bool = False) -> None:
        """
        Replaces tolerance of FACE EDGE VERTEX by the
        tolerance Max of their connected handling shapes.
        It is not necessary to use this call after
        SameParameter. (called in)
        """

    @overload
    @staticmethod
    def UpdateTolerances(S: nanoocp.TopoDS.TopoDS_Shape, theReshaper: nanoocp.BRepTools.BRepTools_ReShape, verifyFaceTolerance: bool = False) -> None:
        """
        Replaces tolerance of FACE EDGE VERTEX by the
        tolerance Max of their connected handling shapes.
        It is not necessary to use this call after
        SameParameter. (called in)
        theReshaper is used to record the modifications of input shape <S> to prevent any
        modifications on the shape itself.
        Thus the input shape (and its subshapes) will not be modified, instead the reshaper will
        contain a modified empty-copies of original subshapes as substitutions.
        """

    @staticmethod
    def UpdateInnerTolerances(S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Checks tolerances of edges (including inner points) and vertices
        of a shape and updates them to satisfy "SameParameter" condition
        """

    @staticmethod
    def OrientClosedSolid(solid: nanoocp.TopoDS.TopoDS_Solid) -> bool:
        """
        Orients the solid forward and the shell with the
        orientation to have matter in the solid. Returns
        False if the solid is unOrientable (open or incoherent)
        """

    @staticmethod
    def ContinuityOfFaces(theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace1: nanoocp.TopoDS.TopoDS_Face, theFace2: nanoocp.TopoDS.TopoDS_Face, theAngleTol: float) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Returns the order of continuity between two faces
        connected by an edge
        """

    @overload
    @staticmethod
    def EncodeRegularity(S: nanoocp.TopoDS.TopoDS_Shape, TolAng: float = 1e-10) -> None:
        """
        Encodes the Regularity of edges on a Shape.
        Warning: <TolAng> is an angular tolerance, expressed in Rad.
        Warning: If the edges's regularity are coded before, nothing
        is done.
        """

    @overload
    @staticmethod
    def EncodeRegularity(S: nanoocp.TopoDS.TopoDS_Shape, LE: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], TolAng: float = 1e-10) -> None:
        """
        Encodes the Regularity of edges in list <LE> on the shape <S>
        Warning: <TolAng> is an angular tolerance, expressed in Rad.
        Warning: If the edges's regularity are coded before, nothing
        is done.
        """

    @overload
    @staticmethod
    def EncodeRegularity(E: nanoocp.TopoDS.TopoDS_Edge, F1: nanoocp.TopoDS.TopoDS_Face, F2: nanoocp.TopoDS.TopoDS_Face, TolAng: float = 1e-10) -> None:
        """
        Encodes the Regularity between <F1> and <F2> by <E>
        Warning: <TolAng> is an angular tolerance, expressed in Rad.
        Warning: If the edge's regularity is coded before, nothing
        is done.
        """

    @staticmethod
    def SortFaces(S: nanoocp.TopoDS.TopoDS_Shape, LF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Sorts in LF the Faces of S on the complexity of
        their surfaces
        (Plane,Cylinder,Cone,Sphere,Torus,other)
        """

    @staticmethod
    def ReverseSortFaces(S: nanoocp.TopoDS.TopoDS_Shape, LF: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Sorts in LF the Faces of S on the reverse
        complexity of their surfaces
        (other,Torus,Sphere,Cone,Cylinder,Plane)
        """

    @staticmethod
    def EnsureNormalConsistency(S: nanoocp.TopoDS.TopoDS_Shape, theAngTol: float = 0.001, ForceComputeNormals: bool = False) -> bool:
        """
        Corrects the normals in Poly_Triangulation of faces,
        in such way that normals at nodes lying along smooth
        edges have the same value on both adjacent triangulations.
        Returns TRUE if any correction is done.
        """

    @staticmethod
    def UpdateDeflection(S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Updates value of deflection in Poly_Triangulation of faces
        by the maximum deviation measured on existing triangulation.
        """

    @staticmethod
    def BoundingVertex(theLV: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theNewCenter: nanoocp.gp.gp_Pnt) -> float:
        """
        Calculates the bounding sphere around the set of vertexes from the theLV list.
        Returns the center (theNewCenter) and the radius (theNewTol) of this sphere.
        This can be used to construct the new vertex which covers the given set of
        other vertices.
        """

    @overload
    @staticmethod
    def FindValidRange(theCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, theTolE: float, theParV1: float, thePntV1: nanoocp.gp.gp_Pnt, theTolV1: float, theParV2: float, thePntV2: nanoocp.gp.gp_Pnt, theTolV2: float) -> tuple[bool, float, float]:
        """
        For an edge defined by 3d curve and tolerance and vertices defined by points,
        parameters on curve and tolerances,
        finds a range of curve between vertices not covered by vertices tolerances.
        Returns false if there is no such range. Otherwise, sets theFirst and
        theLast as its bounds.
        """

    @overload
    @staticmethod
    def FindValidRange(theEdge: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]:
        """
        Finds a range of 3d curve of the edge not covered by vertices tolerances.
        Returns false if there is no such range. Otherwise, sets theFirst and
        theLast as its bounds.
        """

    @staticmethod
    def ExtendFace(theF: nanoocp.TopoDS.TopoDS_Face, theExtVal: float, theExtUMin: bool, theExtUMax: bool, theExtVMin: bool, theExtVMax: bool, theFExtended: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Enlarges the face on the given value.
        @param[in] theF  The face to extend
        @param[in] theExtVal  The extension value
        @param[in] theExtUMin  Defines whether to extend the face in UMin direction
        @param[in] theExtUMax  Defines whether to extend the face in UMax direction
        @param[in] theExtVMin  Defines whether to extend the face in VMin direction
        @param[in] theExtVMax  Defines whether to extend the face in VMax direction
        @param[in] theFExtended  The extended face
        """

class BRepLib_CheckCurveOnSurface:
    """
    Computes the max distance between edge and its 2d representation on the face.
    This class is not intended to process non-sameparameter edges.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BRepLib_CheckCurveOnSurface) -> None: ...

    def Init(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Sets the data for the algorithm"""

    def Perform(self) -> None:
        """
        Performs the calculation
        If myIsParallel == true then computation will be performed in parallel.
        """

    def IsDone(self) -> bool:
        """Returns true if the max distance has been found"""

    def SetParallel(self, theIsParallel: bool) -> None:
        """Sets parallel flag"""

    def IsParallel(self) -> bool:
        """Returns true if parallel flag is set"""

    def ErrorStatus(self) -> int:
        """
        Returns error status
        The possible values are:
        0 - OK;
        1 - null curve or surface or 2d curve;
        2 - invalid parametric range;
        3 - error in calculations.
        """

    def MaxDistance(self) -> float:
        """Returns max distance"""

    def MaxParameter(self) -> float:
        """Returns parameter in which the distance is maximal"""

class BRepLib_Command:
    """
    Root class for all commands in BRepLib.

    Provides :

    * Managements of the notDone flag.

    * Catching of exceptions (not implemented).

    * Logging (not implemented).
    """

    def __init__(self, theOther: BRepLib_Command) -> None: ...

    def IsDone(self) -> bool: ...

    def Check(self) -> None:
        """Raises NotDone if done is false."""

class BRepLib_FindSurface:
    """
    Provides an algorithm to find a Surface through a
    set of edges.

    The edges of the shape given as argument are
    explored if they are not coplanar at the required
    tolerance the method Found returns false.

    If a null tolerance is given the max of the edges
    tolerances is used.

    The method Tolerance returns the true distance of
    the edges to the Surface.

    The method Surface returns the Surface if found.

    The method Existed returns True if the
    Surface was already attached to some of the edges.

    When Existed returns True the Surface may have a
    location given by the Location method.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, Tol: float = -1.0, OnlyPlane: bool = False, OnlyClosed: bool = False) -> None:
        """
        Computes the Surface from the edges of <S> with the
        given tolerance.
        if <OnlyPlane> is true, the computed surface will be
        a plane. If it is not possible to find a plane, the
        flag NotDone will be set.
        If <OnlyClosed> is true, then S should be a wire
        and the existing surface, on which wire S is not
        closed in 2D, will be ignored.
        """

    @overload
    def __init__(self, theOther: BRepLib_FindSurface) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape, Tol: float = -1.0, OnlyPlane: bool = False, OnlyClosed: bool = False) -> None:
        """
        Computes the Surface from the edges of <S> with the
        given tolerance.
        if <OnlyPlane> is true, the computed surface will be
        a plane. If it is not possible to find a plane, the
        flag NotDone will be set.
        If <OnlyClosed> is true, then S should be a wire
        and the existing surface, on which wire S is not
        closed in 2D, will be ignored.
        """

    def Found(self) -> bool: ...

    def Surface(self) -> nanoocp.Geom.Geom_Surface: ...

    def Tolerance(self) -> float: ...

    def ToleranceReached(self) -> float: ...

    def Existed(self) -> bool: ...

    def Location(self) -> nanoocp.TopLoc.TopLoc_Location: ...

class BRepLib_FuseEdges:
    """
    This class can detect vertices in a face that can
    be considered useless and then perform the fuse of
    the edges and remove the useless vertices. By
    useles vertices, we mean:
    * vertices that have exactly two connex edges
    * the edges connex to the vertex must have
    exactly the same 2 connex faces.
    * The edges connex to the vertex must have the
    same geometric support.
    """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape, PerformNow: bool = False) -> None:
        """
        Initialise members and build construction of map
        of ancestors.
        """

    @overload
    def __init__(self, theOther: BRepLib_FuseEdges) -> None: ...

    def AvoidEdges(self, theMapEdg: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """set edges to avoid being fused"""

    def SetConcatBSpl(self, theConcatBSpl: bool = True) -> None:
        """
        set mode to enable concatenation G1 BSpline edges in one
        End Modified by IFV 19.04.07
        """

    def Edges(self, theMapLstEdg: nanoocp.NCollection.NCollection_DataMap[int, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]]) -> None:
        """
        returns all the list of edges to be fused
        each list of the map represent a set of connex edges
        that can be fused.
        """

    def ResultEdges(self, theMapEdg: nanoocp.NCollection.NCollection_DataMap[int, nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        returns all the fused edges. each integer entry in
        the map corresponds to the integer in the
        DataMapOfIntegerListOfShape we get in method
        Edges. That is to say, to the list of edges in
        theMapLstEdg(i) corresponds the resulting edge theMapEdge(i)
        """

    def Faces(self, theMapFac: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """returns the map of modified faces."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        returns myShape modified with the list of internal
        edges removed from it.
        """

    def NbVertices(self) -> int:
        """returns the number of vertices candidate to be removed"""

    def Perform(self) -> None:
        """
        Using map of list of connex edges, fuse each list to
        one edge and then update myShape
        """

class BRepLib_MakeShape(BRepLib_Command):
    """
    This is the root class for all shape
    constructions. It stores the result.

    It provides deferred methods to trace the history
    of sub-shapes.
    """

    def __init__(self, theOther: BRepLib_MakeShape) -> None: ...

    def Build(self) -> None:
        """
        This is called by Shape(). It does nothing but
        may be redefined.
        """

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def FaceStatus(self, F: nanoocp.TopoDS.TopoDS_Face) -> BRepLib_ShapeModification:
        """
        returns the status of the Face after
        the shape creation.
        """

    def HasDescendants(self, F: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """Returns True if the Face generates new topology."""

    def DescendantFaces(self, F: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """returns the list of generated Faces."""

    def NbSurfaces(self) -> int:
        """
        returns the number of surfaces
        after the shape creation.
        """

    def NewFaces(self, I: int) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Return the faces created for surface I."""

    def FacesFromEdges(self, E: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        returns a list of the created faces
        from the edge <E>.
        """

class BRepLib_MakeEdge(BRepLib_MakeShape):
    """
    Provides methods to build edges.

    The methods have the following syntax, where
    TheCurve is one of Lin, Circ, ...

    Create(C : TheCurve)

    Makes an edge on the whole curve. Add vertices
    on finite curves.

    Create(C : TheCurve; p1,p2 : Real)

    Make an edge on the curve between parameters p1
    and p2. if p2 < p1 the edge will be REVERSED. If
    p1 or p2 is infinite the curve will be open in
    that direction. Vertices are created for finite
    values of p1 and p2.

    Create(C : TheCurve; P1, P2 : Pnt from gp)

    Make an edge on the curve between the points P1
    and P2. The points are projected on the curve
    and the previous method is used. An error is
    raised if the points are not on the curve.

    Create(C : TheCurve; V1, V2 : Vertex from TopoDS)

    Make an edge on the curve between the vertices
    V1 and V2. Same as the previous but no vertices
    are created. If a vertex is Null the curve will
    be open in this direction.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom.Geom_Curve | None) -> None: ...

    @overload
    def __init__(self, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom.Geom_Curve | None, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom.Geom_Curve | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom.Geom_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom.Geom_Curve | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom.Geom_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, theOther: BRepLib_MakeEdge) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom.Geom_Curve | None) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom.Geom_Curve | None, p1: float, p2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom.Geom_Curve | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom.Geom_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom.Geom_Curve | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, p1: float, p2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom.Geom_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, p1: float, p2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, p1: float, p2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, p1: float, p2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, S: nanoocp.Geom.Geom_Surface | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, p1: float, p2: float) -> None: ...

    def Error(self) -> BRepLib_EdgeError:
        """Returns the error description when NotDone."""

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def Vertex1(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the first vertex of the edge. May be Null."""

    def Vertex2(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the second vertex of the edge. May be Null."""

class BRepLib_MakeEdge2d(BRepLib_MakeShape):
    """
    Provides methods to build edges.

    The methods have the following syntax, where
    TheCurve is one of Lin2d, Circ2d, ...

    Create(C : TheCurve)

    Makes an edge on the whole curve. Add vertices
    on finite curves.

    Create(C : TheCurve; p1,p2 : Real)

    Make an edge on the curve between parameters p1
    and p2. if p2 < p1 the edge will be REVERSED. If
    p1 or p2 is infinite the curve will be open in
    that direction. Vertices are created for finite
    values of p1 and p2.

    Create(C : TheCurve; P1, P2 : Pnt2d from gp)

    Make an edge on the curve between the points P1
    and P2. The points are projected on the curve
    and the previous method is used. An error is
    raised if the points are not on the curve.

    Create(C : TheCurve; V1, V2 : Vertex from TopoDS)

    Make an edge on the curve between the vertices
    V1 and V2. Same as the previous but no vertices
    are created. If a vertex is Null the curve will
    be open in this direction.
    """

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None) -> None: ...

    @overload
    def __init__(self, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ2d, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ2d, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Circ2d, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips2d, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips2d, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Elips2d, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr2d, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr2d, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Hypr2d, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab2d, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab2d, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Parab2d, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, L: nanoocp.Geom2d.Geom2d_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, p1: float, p2: float) -> None: ...

    @overload
    def __init__(self, theOther: BRepLib_MakeEdge2d) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, p1: float, p2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d, p1: float, p2: float) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, p1: float, p2: float) -> None: ...

    def Error(self) -> BRepLib_EdgeError:
        """Returns the error description when NotDone."""

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def Vertex1(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the first vertex of the edge. May be Null."""

    def Vertex2(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the second vertex of the edge. May be Null."""

class BRepLib_MakeFace(BRepLib_MakeShape):
    """
    Provides methods to build faces.

    A face may be built :

    * From a surface.

    - Elementary surface from gp.

    - Surface from Geom.

    * From a surface and U,V values.

    * From a wire.

    - Find the surface automatically if possible.

    * From a surface and a wire.

    - A flag Inside is given, when this flag is True
    the wire is oriented to bound a finite area on
    the surface.

    * From a face and a wire.

    - The new wire is a perforation.
    """

    @overload
    def __init__(self) -> None:
        """Not done."""

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Load a face. Useful to add wires."""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pln) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cylinder) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cone) -> None: ...

    @overload
    def __init__(self, S: nanoocp.gp.gp_Sphere) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Torus) -> None: ...

    @overload
    def __init__(self, W: nanoocp.TopoDS.TopoDS_Wire, OnlyPlane: bool = False) -> None:
        """
        Find a surface from the wire and make a face.
        if <OnlyPlane> is true, the computed surface will be
        a plane. If it is not possible to find a plane, the
        flag NotDone will be set.
        """

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_Surface | None, TolDegen: float) -> None:
        """
        Make a face from a Surface. Accepts tolerance value (TolDegen)
        for resolution of degenerated edges.
        """

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pln, W: nanoocp.TopoDS.TopoDS_Wire, Inside: bool = True) -> None:
        """Make a face from a plane and a wire."""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cylinder, W: nanoocp.TopoDS.TopoDS_Wire, Inside: bool = True) -> None:
        """Make a face from a cylinder and a wire."""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cone, W: nanoocp.TopoDS.TopoDS_Wire, Inside: bool = True) -> None:
        """Make a face from a cone and a wire."""

    @overload
    def __init__(self, S: nanoocp.gp.gp_Sphere, W: nanoocp.TopoDS.TopoDS_Wire, Inside: bool = True) -> None:
        """Make a face from a sphere and a wire."""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Torus, W: nanoocp.TopoDS.TopoDS_Wire, Inside: bool = True) -> None:
        """Make a face from a torus and a wire."""

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_Surface | None, W: nanoocp.TopoDS.TopoDS_Wire, Inside: bool = True) -> None:
        """Make a face from a Surface and a wire."""

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face, W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Adds the wire <W> in the face <F>"""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pln, UMin: float, UMax: float, VMin: float, VMax: float) -> None:
        """Make a face from a plane."""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cylinder, UMin: float, UMax: float, VMin: float, VMax: float) -> None:
        """Make a face from a cylinder."""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Cone, UMin: float, UMax: float, VMin: float, VMax: float) -> None:
        """Make a face from a cone."""

    @overload
    def __init__(self, S: nanoocp.gp.gp_Sphere, UMin: float, UMax: float, VMin: float, VMax: float) -> None:
        """Make a face from a sphere."""

    @overload
    def __init__(self, C: nanoocp.gp.gp_Torus, UMin: float, UMax: float, VMin: float, VMax: float) -> None:
        """Make a face from a torus."""

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_Surface | None, UMin: float, UMax: float, VMin: float, VMax: float, TolDegen: float) -> None:
        """
        Make a face from a Surface. Accepts min & max parameters
        to construct the face's bounds. Also accepts tolerance value (TolDegen)
        for resolution of degenerated edges.
        """

    @overload
    def __init__(self, theOther: BRepLib_MakeFace) -> None: ...

    @overload
    def Init(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Load the face."""

    @overload
    def Init(self, S: nanoocp.Geom.Geom_Surface | None, Bound: bool, TolDegen: float) -> None:
        """
        Creates the face from the surface. If Bound is
        True a wire is made from the natural bounds.
        Accepts tolerance value (TolDegen) for resolution
        of degenerated edges.
        """

    @overload
    def Init(self, S: nanoocp.Geom.Geom_Surface | None, UMin: float, UMax: float, VMin: float, VMax: float, TolDegen: float) -> None:
        """
        Creates the face from the surface and the min-max
        values. Accepts tolerance value (TolDegen) for resolution
        of degenerated edges.
        """

    def Add(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Adds the wire <W> in the current face."""

    def Error(self) -> BRepLib_FaceError: ...

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns the new face."""

    @staticmethod
    def IsDegenerated(theCurve: nanoocp.Geom.Geom_Curve | None, theMaxTol: float) -> tuple[bool, float]:
        """
        Checks the specified curve is degenerated
        according to specified tolerance.
        Returns <theActTol> less than <theMaxTol>, which shows
        actual tolerance to decide the curve is degenerated.
        Warning: For internal use of BRepLib_MakeFace and BRepLib_MakeShell.
        """

class BRepLib_MakePolygon(BRepLib_MakeShape):
    """
    Class to build polygonal wires.

    A polygonal wire may be build from

    - 2,4,3 points.

    - 2,3,4 vertices.

    - any number of points.

    - any number of vertices.

    When a point or vertex is added to the polygon if
    it is identic to the previous point no edge is
    built. The method added can be used to test it.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty MakePolygon."""

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, P3: nanoocp.gp.gp_Pnt, Close: bool = False) -> None: ...

    @overload
    def __init__(self, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, V3: nanoocp.TopoDS.TopoDS_Vertex, Close: bool = False) -> None: ...

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, P3: nanoocp.gp.gp_Pnt, P4: nanoocp.gp.gp_Pnt, Close: bool = False) -> None: ...

    @overload
    def __init__(self, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, V3: nanoocp.TopoDS.TopoDS_Vertex, V4: nanoocp.TopoDS.TopoDS_Vertex, Close: bool = False) -> None: ...

    @overload
    def __init__(self, theOther: BRepLib_MakePolygon) -> None: ...

    @overload
    def Add(self, P: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Add(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    def Added(self) -> bool:
        """
        Returns True if the last vertex or point was
        successfully added.
        """

    def Close(self) -> None: ...

    def FirstVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def LastVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns the last edge added to the polygon."""

    def Wire(self) -> nanoocp.TopoDS.TopoDS_Wire: ...

class BRepLib_MakeShell(BRepLib_MakeShape):
    """
    Provides methods to build shells.

    Build a shell from a set of faces.
    Build untied shell from a non C2 surface
    splitting it into C2-continuous parts.
    """

    @overload
    def __init__(self) -> None:
        """Not done."""

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_Surface | None, Segment: bool = False) -> None: ...

    @overload
    def __init__(self, S: nanoocp.Geom.Geom_Surface | None, UMin: float, UMax: float, VMin: float, VMax: float, Segment: bool = False) -> None: ...

    @overload
    def __init__(self, theOther: BRepLib_MakeShell) -> None: ...

    def Init(self, S: nanoocp.Geom.Geom_Surface | None, UMin: float, UMax: float, VMin: float, VMax: float, Segment: bool = False) -> None:
        """
        Creates the shell from the surface and the min-max
        values.
        """

    def Error(self) -> BRepLib_ShellError: ...

    def Shell(self) -> nanoocp.TopoDS.TopoDS_Shell:
        """Returns the new Shell."""

class BRepLib_MakeSolid(BRepLib_MakeShape):
    """Makes a solid from compsolid or shells."""

    @overload
    def __init__(self) -> None:
        """Solid covers whole space."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_CompSolid) -> None:
        """Make a solid from a CompSolid."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shell) -> None:
        """Make a solid from a shell."""

    @overload
    def __init__(self, So: nanoocp.TopoDS.TopoDS_Solid) -> None:
        """Make a solid from a solid. Useful for adding later."""

    @overload
    def __init__(self, S1: nanoocp.TopoDS.TopoDS_Shell, S2: nanoocp.TopoDS.TopoDS_Shell) -> None:
        """Make a solid from two shells."""

    @overload
    def __init__(self, So: nanoocp.TopoDS.TopoDS_Solid, S: nanoocp.TopoDS.TopoDS_Shell) -> None:
        """Add a shell to a solid."""

    @overload
    def __init__(self, S1: nanoocp.TopoDS.TopoDS_Shell, S2: nanoocp.TopoDS.TopoDS_Shell, S3: nanoocp.TopoDS.TopoDS_Shell) -> None:
        """Make a solid from three shells."""

    @overload
    def __init__(self, theOther: BRepLib_MakeSolid) -> None: ...

    def Add(self, S: nanoocp.TopoDS.TopoDS_Shell) -> None:
        """Add the shell to the current solid."""

    def Solid(self) -> nanoocp.TopoDS.TopoDS_Solid:
        """Returns the new Solid."""

    def FaceStatus(self, F: nanoocp.TopoDS.TopoDS_Face) -> BRepLib_ShapeModification:
        """
        returns the status of the Face after
        the shape creation.
        """

class BRepLib_MakeVertex(BRepLib_MakeShape):
    """Provides methods to build vertices."""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, theOther: BRepLib_MakeVertex) -> None: ...

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

class BRepLib_MakeWire(BRepLib_MakeShape):
    """
    Provides methods to build wires.

    A wire may be built:

    * From a single edge.

    * From a wire and an edge.

    - A new wire is created with the edges of the
    wire + the edge.

    - If the edge is not connected to the wire the
    flag NotDone is set and the method Wire will
    raise an error.

    - The connection may be:

    . Through an existing vertex. The edge is shared.

    . Through a geometric coincidence of vertices.
    The edge is copied and the vertices from the
    edge are replaced by the vertices from the
    wire.

    . The new edge and the connection vertices are
    kept by the algorithm.

    * From 2, 3, 4 edges.

    - A wire is created from the first edge, the
    following edges are added.

    * From many edges.

    - The following syntax may be used :

    BRepLib_MakeWire MW;

    // for all the edges ...
    MW.Add(anEdge);

    TopoDS_Wire W = MW;
    """

    @overload
    def __init__(self) -> None:
        """NotDone MakeWire."""

    @overload
    def __init__(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Make a Wire from an edge."""

    @overload
    def __init__(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Make a Wire from a Wire. Useful for adding later."""

    @overload
    def __init__(self, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Make a Wire from two edges."""

    @overload
    def __init__(self, W: nanoocp.TopoDS.TopoDS_Wire, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Add an edge to a wire."""

    @overload
    def __init__(self, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, E3: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Make a Wire from three edges."""

    @overload
    def __init__(self, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, E3: nanoocp.TopoDS.TopoDS_Edge, E4: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Make a Wire from four edges."""

    @overload
    def __init__(self, theOther: BRepLib_MakeWire) -> None: ...

    @overload
    def Add(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Add the edge <E> to the current wire."""

    @overload
    def Add(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Add the edges of <W> to the current wire."""

    @overload
    def Add(self, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Add the edges of <L> to the current wire.
        The edges are not to be consecutive. But they are
        to be all connected geometrically or topologically.
        """

    def Error(self) -> BRepLib_WireError: ...

    def Wire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns the new wire."""

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns the last edge added to the wire."""

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Returns the last connecting vertex."""

class BRepLib_PointCloudShape:
    """
    This tool is intended to get points from shape with specified distance from shape along normal.
    Can be used to simulation of points obtained in result of laser scan of shape.
    There are 2 ways for generation points by shape:
    1. Generation points with specified density
    2. Generation points using triangulation Nodes
    Generation of points by density using the GeneratePointsByDensity() function is not thread safe.
    """

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return loaded shape."""

    def SetShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Set shape."""

    def Tolerance(self) -> float:
        """Return tolerance."""

    def SetTolerance(self, theTol: float) -> None:
        """Set tolerance."""

    def GetDistance(self) -> float:
        """
        Returns value of the distance to define deflection of points from shape along normal to shape;
        0.0 by default.
        """

    def SetDistance(self, theDist: float) -> None:
        """
        Sets value of the distance to define deflection of points from shape along normal to shape.
        Negative values of theDist parameter are ignored.
        """

    def NbPointsByDensity(self, theDensity: float = 0.0) -> int:
        """Returns size of the point cloud for specified density."""

    def NbPointsByTriangulation(self) -> int:
        """Returns size of the point cloud for using triangulation."""

    def GeneratePointsByDensity(self, theDensity: float = 0.0) -> bool:
        """
        Computes points with specified density for initial shape.
        If parameter Density is equal to 0 then density will be computed automatically by criterion:
        - 10 points per minimal unreduced face area.

        Note: this function should not be called from concurrent threads without external lock.
        """

    def GeneratePointsByTriangulation(self) -> bool:
        """Get points from triangulation existing in the shape."""

class BRepLib_ToolTriangulatedShape:
    """
    Provides methods for calculating normals to Poly_Triangulation of TopoDS_Face.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepLib_ToolTriangulatedShape) -> None: ...

    @overload
    @staticmethod
    def ComputeNormals(theFace: nanoocp.TopoDS.TopoDS_Face, theTris: nanoocp.Poly.Poly_Triangulation | None) -> None:
        """
        Computes nodal normals for Poly_Triangulation structure using UV coordinates and surface.
        Does nothing if triangulation already defines normals.
        @param[in] theFace the face
        @param[in] theTris the definition of a face triangulation
        """

    @overload
    @staticmethod
    def ComputeNormals(theFace: nanoocp.TopoDS.TopoDS_Face, theTris: nanoocp.Poly.Poly_Triangulation | None, thePolyConnect: nanoocp.Poly.Poly_Connect) -> None:
        """
        Computes nodal normals for Poly_Triangulation structure using UV coordinates and surface.
        Does nothing if triangulation already defines normals.
        @param[in] theFace the face
        @param[in] theTris the definition of a face triangulation
        @param[in,out] thePolyConnect optional, initialized tool for exploring triangulation
        """

class BRepLib_ValidateEdge:
    """
    Computes the max distance between 3D-curve and curve on surface.
    This class uses 2 methods: approximate using finite
    number of points (default) and exact
    """

    @overload
    def __init__(self, theReferenceCurve: nanoocp.Adaptor3d.Adaptor3d_Curve | None, theOtherCurve: nanoocp.Adaptor3d.Adaptor3d_CurveOnSurface | None, theSameParameter: bool) -> None:
        """Initialization constructor"""

    @overload
    def __init__(self, theOther: BRepLib_ValidateEdge) -> None: ...

    def SetExactMethod(self, theIsExact: bool) -> None:
        """
        Sets method to calculate distance: Calculating in finite number of points (if theIsExact
        is false, faster, but possible not correct result) or exact calculating by using
        BRepLib_CheckCurveOnSurface class (if theIsExact is true, slowly, but more correctly).
        Exact method is used only when edge is SameParameter.
        Default method is calculating in finite number of points
        """

    def IsExactMethod(self) -> bool:
        """Returns true if exact method selected"""

    def SetParallel(self, theIsMultiThread: bool) -> None:
        """Sets parallel flag"""

    def IsParallel(self) -> bool:
        """Returns true if parallel flag is set"""

    def SetControlPointsNumber(self, theControlPointsNumber: int) -> None:
        """Set control points number (if you need a value other than 22)"""

    def SetExitIfToleranceExceeded(self, theToleranceForChecking: float) -> None:
        """
        Sets limit to compute a distance in the Process() function. If the distance greater than
        theToleranceForChecking the Process() function stopped. Use this in case checking of
        tolerance for best performcnce. Has no effect in case using exact method.
        """

    def Process(self) -> None:
        """
        Computes the max distance for the 3d curve <myReferenceCurve>
        and curve on surface <myOtherCurve>. If the SetExitIfToleranceExceeded()
        function was called before <myCalculatedDistance> contains first
        greater than SetExitIfToleranceExceeded() parameter value. In case
        using exact method always computes real max distance.
        """

    def IsDone(self) -> bool:
        """Returns true if the distance has been found for all points"""

    def CheckTolerance(self, theToleranceToCheck: float) -> bool:
        """Returns true if computed distance is less than <theToleranceToCheck>"""

    def GetMaxDistance(self) -> float:
        """Returns max distance"""

    def UpdateTolerance(self) -> float:
        """
        Increase <theToleranceToUpdate> if max distance is greater than <theToleranceToUpdate>
        """
