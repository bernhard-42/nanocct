"""OCCT package ShapeAnalysis (toolkit TKShHealing)"""

from typing import overload

import nanoocp.Adaptor3d
import nanoocp.Bnd
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAdaptor
import nanoocp.NCollection
import nanoocp.ShapeExtend
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.gp


class ShapeAnalysis:
    """
    This package is intended to analyze geometrical objects
    and topological shapes. Analysis domain includes both
    exploring geometrical and topological properties of
    shapes and checking their conformance to Open CASCADE requirements.
    The directions of analysis provided by tools of this package are:
    computing quantities of subshapes,
    computing parameters of points on curve and surface,
    computing surface singularities,
    checking edge and wire consistency,
    checking edges order in the wire,
    checking face bounds orientation,
    checking small faces,
    analyzing shape tolerances,
    analyzing of free bounds of the shape.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeAnalysis) -> None: ...

    @staticmethod
    def OuterWire(theFace: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.TopoDS.TopoDS_Wire:
        """
        Returns positively oriented wire in the face.
        If there is no such wire - returns the last wire of the face.
        """

    @staticmethod
    def TotCross2D(sewd: nanoocp.ShapeExtend.ShapeExtend_WireData | None, aFace: nanoocp.TopoDS.TopoDS_Face) -> float:
        """Returns a total area of 2d wire"""

    @staticmethod
    def ContourArea(theWire: nanoocp.TopoDS.TopoDS_Wire) -> float:
        """Returns a total area of 3d wire"""

    @staticmethod
    def IsOuterBound(face: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """Returns True if <F> has outer bound."""

    @staticmethod
    def AdjustByPeriod(Val: float, ToVal: float, Period: float) -> float:
        """
        Returns a shift required to move point
        <Val> to the range [ToVal-Period/2,ToVal+Period/2].
        This shift will be the divisible by Period.
        Intended for adjusting parameters on periodic surfaces.
        """

    @staticmethod
    def AdjustToPeriod(Val: float, ValMin: float, ValMax: float) -> float:
        """
        Returns a shift required to move point
        <Val> to the range [ValMin,ValMax].
        This shift will be the divisible by Period
        with Period = ValMax - ValMin.
        Intended for adjusting parameters on periodic surfaces.
        """

    @staticmethod
    def FindBounds(shape: nanoocp.TopoDS.TopoDS_Shape, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex) -> None:
        """
        Finds the start and end vertices of the shape
        Shape can be of the following type:
        vertex: V1 and V2 are the same and equal to <shape>,
        edge  : V1 is start and V2 is end vertex (see ShapeAnalysis_Edge
        methods FirstVertex and LastVertex),
        wire  : V1 is start vertex of the first edge, V2 is end vertex
        of the last edge (also see ShapeAnalysis_Edge).
        If wire contains no edges V1 and V2 are nullified
        If none of the above V1 and V2 are nullified
        """

    @staticmethod
    def GetFaceUVBounds(F: nanoocp.TopoDS.TopoDS_Face) -> tuple[float, float, float, float]:
        """Computes exact UV bounds of all wires on the face"""

class ShapeAnalysis_CheckSmallFace:
    """Analysis of the face size"""

    @overload
    def __init__(self) -> None:
        """
        Creates an empty tool
        Checks a Shape i.e. each of its faces, records checks as
        diagnostics in the <infos>

        If <infos> has not been set before, no check is done

        For faces which are in a Shell, topological data are recorded
        to allow recovering connectivities after fixing or removing
        the small faces or parts of faces
        Enchains various checks on a face
        inshell : to compute more information, relevant to topology
        """

    @overload
    def __init__(self, theOther: ShapeAnalysis_CheckSmallFace) -> None: ...

    def IsSpotFace(self, F: nanoocp.TopoDS.TopoDS_Face, spot: nanoocp.gp.gp_Pnt, tol: float = -1.0) -> tuple[int, float]:
        """
        Checks if a Face is as a Spot
        Returns 0 if not, 1 if yes, 2 if yes and all vertices are the
        same
        By default, considers the tolerance zone of its vertices
        A given value <tol> may be given to check a spot of this size
        If a Face is a Spot, its location is returned in <spot>, and
        <spotol> returns an equivalent tolerance, which is computed as
        half of max dimension of min-max box of the face
        """

    def CheckSpotFace(self, F: nanoocp.TopoDS.TopoDS_Face, tol: float = -1.0) -> bool:
        """
        Acts as IsSpotFace, but records in <infos> a diagnostic
        "SpotFace" with the Pnt as value (data "Location")
        """

    def IsStripSupport(self, F: nanoocp.TopoDS.TopoDS_Face, tol: float = -1.0) -> bool:
        """
        Checks if a Face lies on a Surface which is a strip
        So the Face is a strip. But a Face may be a strip elsewhere ..

        A given value <tol> may be given to check max width
        By default, considers the tolerance zone of its edges
        Returns 0 if not a strip support, 1 strip in U, 2 strip in V
        """

    def CheckStripEdges(self, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, tol: float) -> tuple[bool, float]:
        """
        Checks if two edges define a strip, i.e. distance maxi below
        tolerance, given or some of those of E1 and E2
        """

    def FindStripEdges(self, F: nanoocp.TopoDS.TopoDS_Face, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, tol: float) -> tuple[bool, float]:
        """
        Searches for two and only two edges up tolerance
        Returns True if OK, false if not 2 edges
        If True, returns the two edges and their maximum distance
        """

    def CheckSingleStrip(self, F: nanoocp.TopoDS.TopoDS_Face, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, tol: float = -1.0) -> bool:
        """
        Checks if a Face is a single strip, i.e. brings two great
        edges which are confused on their whole length, possible other
        edges are small or null length

        Returns 0 if not a strip support, 1 strip in U, 2 strip in V
        Records diagnostic in info if it is a single strip
        """

    def CheckStripFace(self, F: nanoocp.TopoDS.TopoDS_Face, E1: nanoocp.TopoDS.TopoDS_Edge, E2: nanoocp.TopoDS.TopoDS_Edge, tol: float = -1.0) -> bool:
        """
        Checks if a Face is as a Strip
        Returns 0 if not or non determined, 1 if in U, 2 if in V
        By default, considers the tolerance zone of its edges
        A given value <tol> may be given to check a strip of max this width

        If a Face is determined as a Strip, it is delinited by two
        lists of edges. These lists are recorded in diagnostic
        Diagnostic "StripFace" brings data "Direction" (U or V),
        "List1" , "List2" (if they could be computed)
        """

    def CheckSplittingVertices(self, F: nanoocp.TopoDS.TopoDS_Face, MapEdges: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], MapParam: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[float], nanoocp.TopTools.TopTools_ShapeMapHasher], theAllVert: nanoocp.TopoDS.TopoDS_Compound) -> int:
        """
        Checks if a Face brings vertices which split it, either
        confused with non adjacent vertices, or confused with their
        projection on non adjacent edges
        Returns the count of found splitting vertices
        Each vertex then brings a diagnostic "SplittingVertex",
        with data : "Face" for the face, "Edge" for the split edge
        """

    def CheckPin(self, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, int, int]:
        """
        Checks if a Face has a pin, which can be edited
        No singularity : no pin, returns 0
        If there is a pin, checked topics, with returned value :
        - 0 : nothing to do more
        - 1 : "smooth", i.e. not a really sharp pin
        -> diagnostic "SmoothPin"
        - 2 : stretched pin, i.e. is possible to relimit the face by
        another vertex, so that this vertex still gives a pin
        -> diagnostic "StretchedPin" with location of vertex (Pnt)
        """

    def CheckTwisted(self, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, float, float]:
        """
        Checks if a Face is twisted (apart from checking Pin, i.e. it
        does not give information on pin, only "it is twisted")
        """

    def CheckPinFace(self, F: nanoocp.TopoDS.TopoDS_Face, mapEdges: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], toler: float = -1.0) -> bool: ...

    def CheckPinEdges(self, theFirstEdge: nanoocp.TopoDS.TopoDS_Edge, theSecondEdge: nanoocp.TopoDS.TopoDS_Edge, coef1: float, coef2: float, toler: float) -> bool: ...

    def Status(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Returns the status of last call to Perform()
        ShapeExtend_OK   : face was OK, nothing done
        ShapeExtend_DONE1: some wires are fixed
        ShapeExtend_DONE2: orientation of wires fixed
        ShapeExtend_DONE3: missing seam added
        ShapeExtend_DONE4: small area wire removed
        ShapeExtend_DONE5: natural bounds added
        ShapeExtend_FAIL1: some fails during fixing wires
        ShapeExtend_FAIL2: cannot fix orientation of wires
        ShapeExtend_FAIL3: cannot add missing seam
        ShapeExtend_FAIL4: cannot remove small area wire
        """

    def SetTolerance(self, tol: float) -> None:
        """
        Sets a fixed Tolerance to check small face
        By default, local tolerance zone is considered
        Sets a fixed MaxTolerance to check small face
        Sets a fixed Tolerance to check small face
        By default, local tolerance zone is considered
        Unset fixed tolerance, comes back to local tolerance zones
        Unset fixed tolerance, comes back to local tolerance zones
        """

    def Tolerance(self) -> float:
        """
        Returns the tolerance to check small faces, negative value if
        local tolerances zones are to be considered
        """

    def StatusSpot(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusStrip(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusPin(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusTwisted(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusSplitVert(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusPinFace(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusPinEdges(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

class ShapeAnalysis_Curve:
    """
    Analyzing tool for 2d or 3d curve.
    Computes parameters of projected point onto a curve.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeAnalysis_Curve) -> None: ...

    @overload
    def Project(self, C3D: nanoocp.Geom.Geom_Curve | None, P3D: nanoocp.gp.gp_Pnt, preci: float, proj: nanoocp.gp.gp_Pnt, AdjustToEnds: bool = True) -> tuple[float, float]:
        """
        Projects a Point on a Curve.
        Computes the projected point and its parameter on the curve.
        <preci> is used as 3d precision (hence, 0 will produce
        reject unless exact confusion).
        The number of iterations is limited.
        If AdjustToEnds is True, point will be adjusted to the end
        of the curve if distance is less than <preci>

        Returned value is the distance between the given point and
        computed one.
        """

    @overload
    def Project(self, C3D: nanoocp.Adaptor3d.Adaptor3d_Curve, P3D: nanoocp.gp.gp_Pnt, preci: float, proj: nanoocp.gp.gp_Pnt, AdjustToEnds: bool = True) -> tuple[float, float]:
        """
        Projects a Point on a Curve.
        Computes the projected point and its parameter on the curve.
        <preci> is used as 3d precision (hence, 0 will produce
        reject unless exact confusion).
        The number of iterations is limited.

        Returned value is the distance between the given point and
        computed one.
        """

    @overload
    def Project(self, C3D: nanoocp.Geom.Geom_Curve | None, P3D: nanoocp.gp.gp_Pnt, preci: float, proj: nanoocp.gp.gp_Pnt, cf: float, cl: float, AdjustToEnds: bool = True) -> tuple[float, float]:
        """
        Projects a Point on a Curve, but parameters are limited
        between <cf> and <cl>.
        The range [cf, cl] is extended with help of Adaptor3d on the
        basis of 3d precision <preci>.
        If AdjustToEnds is True, point will be adjusted to the end
        of the curve if distance is less than <preci>
        """

    def ProjectAct(self, C3D: nanoocp.Adaptor3d.Adaptor3d_Curve, P3D: nanoocp.gp.gp_Pnt, preci: float, proj: nanoocp.gp.gp_Pnt) -> tuple[float, float]: ...

    @overload
    def NextProject(self, paramPrev: float, C3D: nanoocp.Geom.Geom_Curve | None, P3D: nanoocp.gp.gp_Pnt, preci: float, proj: nanoocp.gp.gp_Pnt, cf: float, cl: float, AdjustToEnds: bool = True) -> tuple[float, float]:
        """
        Projects a Point on a Curve using Newton method.
        <paramPrev> is taken as the first approximation of solution.
        If Newton algorithm fails the method Project() is used.
        If AdjustToEnds is True, point will be adjusted to the end
        of the curve if distance is less than <preci>
        """

    @overload
    def NextProject(self, paramPrev: float, C3D: nanoocp.Adaptor3d.Adaptor3d_Curve, P3D: nanoocp.gp.gp_Pnt, preci: float, proj: nanoocp.gp.gp_Pnt) -> tuple[float, float]:
        """
        Projects a Point on a Curve using Newton method.
        <paramPrev> is taken as the first approximation of solution.
        If Newton algorithm fails the method Project() is used.
        """

    def ValidateRange(self, Crv: nanoocp.Geom.Geom_Curve | None, prec: float) -> tuple[bool, float, float]:
        """
        Validate parameters First and Last for the given curve
        in order to make them valid for creation of edge.
        This includes:
        - limiting range [First,Last] by range of curve
        - adjusting range [First,Last] for periodic (or closed)
        curve if Last < First
        Returns True if parameters are OK or are successfully
        corrected, or False if parameters cannot be corrected.
        In the latter case, parameters are reset to range of curve.
        """

    def FillBndBox(self, C2d: nanoocp.Geom2d.Geom2d_Curve | None, First: float, Last: float, NPoints: int, Exact: bool, Box: nanoocp.Bnd.Bnd_Box2d) -> None:
        """
        Computes a boundary box on segment of curve C2d from First
        to Last. This is done by taking NPoints points from the
        curve and, if Exact is True, by searching for exact
        extrema. All these points are added to Box.
        """

    def SelectForwardSeam(self, C1: nanoocp.Geom2d.Geom2d_Curve | None, C2: nanoocp.Geom2d.Geom2d_Curve | None) -> int:
        """
        Defines which pcurve (C1 or C2) should be chosen for FORWARD
        seam edge.
        """

    @overload
    @staticmethod
    def IsPlanar(pnts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Normal: nanoocp.gp.gp_XYZ, preci: float = 0.0) -> bool:
        """
        Checks if points are planar with given preci. If Normal has not zero
        modulus, checks with given normal
        """

    @overload
    @staticmethod
    def IsPlanar(curve: nanoocp.Geom.Geom_Curve | None, Normal: nanoocp.gp.gp_XYZ, preci: float = 0.0) -> bool:
        """
        Checks if curve is planar with given preci. If Normal has not zero
        modulus, checks with given normal
        """

    @overload
    @staticmethod
    def GetSamplePoints(curve: nanoocp.Geom2d.Geom2d_Curve | None, first: float, last: float, seq: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt2d]) -> bool:
        """
        Returns sample points which will serve as linearisation
        of the2d curve in range (first, last)
        The distribution of sample points is consystent with
        what is used by BRepTopAdaptor_FClass2d
        """

    @overload
    @staticmethod
    def GetSamplePoints(curve: nanoocp.Geom.Geom_Curve | None, first: float, last: float, seq: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt]) -> bool:
        """
        Returns sample points which will serve as linearisation
        of the curve in range (first, last)
        """

    @staticmethod
    def IsClosed(curve: nanoocp.Geom.Geom_Curve | None, preci: float = -1.0) -> bool:
        """
        Tells if the Curve is closed with given precision.
        If <preci> < 0 then Precision::Confusion is used.
        """

    @overload
    @staticmethod
    def IsPeriodic(curve: nanoocp.Geom.Geom_Curve | None) -> bool:
        """
        This method was implemented as fix for changes in trimmed curve
        behaviour. For the moment trimmed curve returns false anyway.
        So it is necessary to adapt all Data exchange tools for this behaviour.
        Current implementation takes into account that curve may be offset.
        """

    @overload
    @staticmethod
    def IsPeriodic(curve: nanoocp.Geom2d.Geom2d_Curve | None) -> bool:
        """The same as for Curve3d."""

class ShapeAnalysis_Edge:
    """
    Tool for analyzing the edge.
    Queries geometrical representations of the edge (3d curve, pcurve
    on the given face or surface) and topological sub-shapes (bounding
    vertices).
    Provides methods for analyzing geometry and topology consistency
    (3d and pcurve(s) consistency, their adjacency to the vertices).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor; initialises Status to OK"""

    @overload
    def __init__(self, theOther: ShapeAnalysis_Edge) -> None: ...

    def HasCurve3d(self, edge: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """Tells if the edge has a 3d curve"""

    def Curve3d(self, edge: nanoocp.TopoDS.TopoDS_Edge, orient: bool = True) -> tuple[bool, nanoocp.Geom.Geom_Curve, float, float]:
        """
        Returns the 3d curve and bounding parameters for the edge
        Returns False if no 3d curve.
        If <orient> is True (default), takes orientation into account:
        if the edge is reversed, cf and cl are toggled
        """

    def IsClosed3d(self, edge: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """
        Gives True if the edge has a 3d curve, this curve is closed,
        and the edge has the same vertex at start and end
        """

    @overload
    def HasPCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face) -> bool:
        """Tells if the Edge has a pcurve on the face."""

    @overload
    def HasPCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, surface: nanoocp.Geom.Geom_Surface | None, location: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """Tells if the edge has a pcurve on the surface (with location)."""

    @overload
    def PCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face, orient: bool = True) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float, float]: ...

    @overload
    def PCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, surface: nanoocp.Geom.Geom_Surface | None, location: nanoocp.TopLoc.TopLoc_Location, orient: bool = True) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, float, float]:
        """
        Returns the pcurve and bounding parameters for the edge
        lying on the surface.
        Returns False if the edge has no pcurve on this surface.
        If <orient> is True (default), takes orientation into account:
        if the edge is reversed, cf and cl are toggled
        """

    @overload
    def BoundUV(self, edge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face, first: nanoocp.gp.gp_Pnt2d, last: nanoocp.gp.gp_Pnt2d) -> bool: ...

    @overload
    def BoundUV(self, edge: nanoocp.TopoDS.TopoDS_Edge, surface: nanoocp.Geom.Geom_Surface | None, location: nanoocp.TopLoc.TopLoc_Location, first: nanoocp.gp.gp_Pnt2d, last: nanoocp.gp.gp_Pnt2d) -> bool:
        """
        Returns the ends of pcurve
        Calls method PCurve with <orient> equal to True
        """

    @overload
    def IsSeam(self, edge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    @overload
    def IsSeam(self, edge: nanoocp.TopoDS.TopoDS_Edge, surface: nanoocp.Geom.Geom_Surface | None, location: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """Returns True if the edge has two pcurves on one surface"""

    def FirstVertex(self, edge: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Returns start vertex of the edge (taking edge orientation
        into account).
        """

    def LastVertex(self, edge: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Returns end vertex of the edge (taking edge orientation
        into account).
        """

    @overload
    def GetEndTangent2d(self, edge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face, atEnd: bool, pos: nanoocp.gp.gp_Pnt2d, tang: nanoocp.gp.gp_Vec2d, dparam: float = 0.0) -> bool: ...

    @overload
    def GetEndTangent2d(self, edge: nanoocp.TopoDS.TopoDS_Edge, surface: nanoocp.Geom.Geom_Surface | None, location: nanoocp.TopLoc.TopLoc_Location, atEnd: bool, pos: nanoocp.gp.gp_Pnt2d, tang: nanoocp.gp.gp_Vec2d, dparam: float = 0.0) -> bool:
        """
        Returns tangent of the edge pcurve at its start (if atEnd is
        False) or end (if True), regarding the orientation of edge.
        If edge is REVERSED, tangent is reversed before return.
        Returns True if pcurve is available and tangent is computed
        and is not null, else False.
        """

    def CheckVerticesWithCurve3d(self, edge: nanoocp.TopoDS.TopoDS_Edge, preci: float = -1.0, vtx: int = 0) -> bool:
        """
        Checks the start and/or end vertex of the edge for matching
        with 3d curve with the given precision.
        <vtx> = 1 : start vertex only
        <vtx> = 2 : end vertex only
        <vtx> = 0 : both (default)
        If preci < 0 the vertices are considered with their own
        tolerances, else with the given <preci>.
        """

    @overload
    def CheckVerticesWithPCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face, preci: float = -1.0, vtx: int = 0) -> bool: ...

    @overload
    def CheckVerticesWithPCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, surface: nanoocp.Geom.Geom_Surface | None, location: nanoocp.TopLoc.TopLoc_Location, preci: float = -1.0, vtx: int = 0) -> bool:
        """
        Checks the start and/or end vertex of the edge for matching
        with pcurve with the given precision.
        <vtx> = 1 : start vertex
        <vtx> = 2 : end vertex
        <vtx> = 0 : both
        If preci < 0 the vertices are considered with their own
        tolerances, else with the given <preci>.
        """

    @overload
    def CheckVertexTolerance(self, edge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face) -> tuple[bool, float, float]: ...

    @overload
    def CheckVertexTolerance(self, edge: nanoocp.TopoDS.TopoDS_Edge) -> tuple[bool, float, float]:
        """
        Checks if it is necessary to increase tolerances of the edge
        vertices to comprise the ends of 3d curve and pcurve on
        the given face (first method) or all pcurves stored in an edge
        (second one)
        toler1 returns necessary tolerance for first vertex,
        toler2 returns necessary tolerance for last vertex.
        """

    @overload
    def CheckCurve3dWithPCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

    @overload
    def CheckCurve3dWithPCurve(self, edge: nanoocp.TopoDS.TopoDS_Edge, surface: nanoocp.Geom.Geom_Surface | None, location: nanoocp.TopLoc.TopLoc_Location) -> bool:
        """
        Checks mutual orientation of 3d curve and pcurve on the
        analysis of curves bounding points
        """

    def Status(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """Returns the status (in the form of True/False) of last Check"""

    @overload
    def CheckSameParameter(self, edge: nanoocp.TopoDS.TopoDS_Edge, NbControl: int = 23) -> tuple[bool, float]: ...

    @overload
    def CheckSameParameter(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face, theNbControl: int = 23) -> tuple[bool, float]:
        """
        Checks the edge to be SameParameter.
        Calculates the maximal deviation between 3d curve and each
        pcurve of the edge on <NbControl> equidistant points (the same
        algorithm as in BRepCheck; default value is 23 as in BRepCheck).
        This deviation is returned in <maxdev> parameter.
        If deviation is greater than tolerance of the edge (i.e.
        incorrect flag) returns False, else returns True.
        """

    def CheckPCurveRange(self, theFirst: float, theLast: float, thePC: nanoocp.Geom2d.Geom2d_Curve | None) -> bool:
        """
        Checks possibility for pcurve thePC to have range [theFirst, theLast] (edge range)
        having respect to real first, last parameters of thePC
        """

    def CheckOverlapping(self, theEdge1: nanoocp.TopoDS.TopoDS_Edge, theEdge2: nanoocp.TopoDS.TopoDS_Edge, theDomainDist: float = 0.0) -> tuple[bool, float]:
        """
        Checks the first edge is overlapped with second edge.
        If distance between two edges is less then theTolOverlap
        edges are overlapped.
        theDomainDis - length of part of edges on which edges are overlapped.
        """

class ShapeAnalysis_FreeBoundData(nanoocp.Standard.Standard_Transient):
    """
    This class is intended to represent free bound and to store
    its properties.

    This class is used by ShapeAnalysis_FreeBoundsProperties
    class when storing each free bound and its properties.

    The properties stored in this class are the following:
    - area of the contour,
    - perimeter of the contour,
    - ratio of average length to average width of the contour,
    - average width of contour,
    - notches (narrow 'V'-like sub-contours) on the contour and
    their maximum width.

    This class provides methods for setting and getting fields
    only.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, freebound: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Creates object with contour given in the form of TopoDS_Wire"""

    @overload
    def __init__(self, theOther: ShapeAnalysis_FreeBoundData) -> None: ...

    def Clear(self) -> None:
        """
        Clears all properties of the contour.
        Contour bound itself is not cleared.
        """

    def SetFreeBound(self, freebound: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Sets contour"""

    def SetArea(self, area: float) -> None:
        """Sets area of the contour"""

    def SetPerimeter(self, perimeter: float) -> None:
        """Sets perimeter of the contour"""

    def SetRatio(self, ratio: float) -> None:
        """Sets ratio of average length to average width of the contour"""

    def SetWidth(self, width: float) -> None:
        """Sets average width of the contour"""

    def AddNotch(self, notch: nanoocp.TopoDS.TopoDS_Wire, width: float) -> None:
        """Adds notch on the contour with its maximum width"""

    def FreeBound(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns contour"""

    def Area(self) -> float:
        """Returns area of the contour"""

    def Perimeter(self) -> float:
        """Returns perimeter of the contour"""

    def Ratio(self) -> float:
        """Returns ratio of average length to average width of the contour"""

    def Width(self) -> float:
        """Returns average width of the contour"""

    def NbNotches(self) -> int:
        """Returns number of notches on the contour"""

    def Notches(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns sequence of notches on the contour"""

    def Notch(self, index: int) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns notch on the contour"""

    @overload
    def NotchWidth(self, index: int) -> float:
        """
        Returns maximum width of notch specified by its rank number
        on the contour
        """

    @overload
    def NotchWidth(self, notch: nanoocp.TopoDS.TopoDS_Wire) -> float:
        """
        Returns maximum width of notch specified as TopoDS_Wire
        on the contour
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeAnalysis_FreeBounds:
    """
    This class is intended to output free bounds of the shape.

    Free bounds are the wires consisting of edges referenced by the faces of the shape
    only once; these are the edges composing the outer boundary of the face or shell
    (as opposed to internal edges between the faces in the shell or seam edges on closed faces).

    This class works on two distinct types of shapes when analyzing
    their free bounds:
    1. compound of faces.
    Analyzer of sewing algorithm (BRepAlgo_Sewing) is used for
    for forecasting free bounds that would be obtained after
    performing sewing
    2. compound of shells.
    Actual free bounds (edges shared by the only face in the shell)
    are output in this case. ShapeAnalysis_Shell is used for that.

    When connecting edges into the wires algorithm tries to build
    wires of maximum length. Two options are provided for a user
    to extract closed sub-contours out of closed and/or open contours.

    Free bounds are returned as two compounds, one for closed and one
    for open wires.

    This class also provides some static methods for advanced use:
    connecting edges/wires to wires, extracting closed sub-wires out
    of wires, dispatching wires into compounds for closed and open
    wires.
    NOTE. Ends of the edge or wire mean hereafter their end vertices.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, shape: nanoocp.TopoDS.TopoDS_Shape, splitclosed: bool = False, splitopen: bool = True, checkinternaledges: bool = False) -> None:
        """
        Builds actual free bounds of the <shape>.
        <shape> should be a compound of shells.
        This constructor is to be used for getting free edges (ones
        referenced by the only face) with help of analyzer
        ShapeAnalysis_Shell.
        Free edges are connected into wires only when they share the
        same vertex.
        If <splitclosed> is True extracts closed sub-wires out of
        built closed wires.
        If <splitopen> is True extracts closed sub-wires out of
        built open wires.
        """

    @overload
    def __init__(self, shape: nanoocp.TopoDS.TopoDS_Shape, toler: float, splitclosed: bool = False, splitopen: bool = True) -> None:
        """
        Builds forecasting free bounds of the <shape>.
        <shape> should be a compound of faces.
        This constructor is to be used for forecasting free edges
        with help of sewing analyzer BRepAlgo_Sewing which is called
        with tolerance <toler>.
        Free edges are connected into wires only when their ends are
        at distance less than <toler>.
        If <splitclosed> is True extracts closed sub-wires out of
        built closed wires.
        If <splitopen> is True extracts closed sub-wires out of
        built open wires.
        """

    @overload
    def __init__(self, theOther: ShapeAnalysis_FreeBounds) -> None: ...

    def GetClosedWires(self) -> nanoocp.TopoDS.TopoDS_Compound:
        """Returns compound of closed wires out of free edges."""

    def GetOpenWires(self) -> nanoocp.TopoDS.TopoDS_Compound:
        """Returns compound of open wires out of free edges."""

    @staticmethod
    def ConnectEdgesToWires(edges: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None, toler: float, shared: bool) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Builds sequence of <wires> out of sequence of not sorted
        <edges>.
        Tries to build wires of maximum length. Building a wire is
        stopped when no edges can be connected to it at its head or
        at its tail.

        Orientation of the edge can change when connecting.
        Edges having INTERNAL or EXTERNAL orientation are ignored.
        If <shared> is True connection is performed only when
        adjacent edges share the same vertex.
        If <shared> is False connection is performed only when
        ends of adjacent edges are at distance less than <toler>.
        Connects edges from the given sequence into wires.
        @param[in] edges the sequence of edges to connect
        @param[in] toler distance tolerance for connection
        @param[in] shared if true, connection uses shared vertices only
        @return sequence of resulting wires
        """

    @staticmethod
    def ConnectEdgesToWires__NCollection_HSequence__TopoDS_Shape(edges: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None, toler: float, shared: bool) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """
        ConnectEdgesToWires__NCollection_HSequence__TopoDS_Shape: the C++ overload ConnectEdgesToWires(const occ::handle<NCollection_HSequence<TopoDS_Shape>> &, const double, const bool, occ::handle<NCollection_HSequence<TopoDS_Shape>> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ConnectEdgesToWires() returning handle by value instead

        @deprecated Use ConnectEdgesToWires() returning handle by value instead.
        """

    @overload
    @staticmethod
    def ConnectWiresToWires(iwires: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None, toler: float, shared: bool) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Connects wires from the given sequence into longer wires.
        @param[in] iwires the sequence of input wires
        @param[in] toler distance tolerance for connection
        @param[in] shared if true, connection uses shared vertices only
        @return sequence of resulting wires
        """

    @overload
    @staticmethod
    def ConnectWiresToWires(iwires: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None, toler: float, shared: bool, vertices: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Builds sequence of <owires> out of sequence of not sorted
        <iwires>.
        Tries to build wires of maximum length. Building a wire is
        stopped when no wires can be connected to it at its head or
        at its tail.

        Orientation of the wire can change when connecting.
        If <shared> is True connection is performed only when
        adjacent wires share the same vertex.
        If <shared> is False connection is performed only when
        ends of adjacent wires are at distance less than <toler>.
        Map <vertices> stores the correspondence between original
        end vertices of the wires and new connecting vertices.
        Connects wires from the given sequence into longer wires.
        Also fills the map of original to new connecting vertices.
        @param[in] iwires the sequence of input wires
        @param[in] toler distance tolerance for connection
        @param[in] shared if true, connection uses shared vertices only
        @param[out] vertices map of original vertices to new connecting vertices
        @return sequence of resulting wires
        """

    @overload
    @staticmethod
    def ConnectWiresToWires__NCollection_HSequence__TopoDS_Shape(iwires: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None, toler: float, shared: bool) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """
        ConnectWiresToWires__NCollection_HSequence__TopoDS_Shape: the C++ overload ConnectWiresToWires(const occ::handle<NCollection_HSequence<TopoDS_Shape>> &, const double, const bool, occ::handle<NCollection_HSequence<TopoDS_Shape>> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ConnectWiresToWires() returning handle by value instead

        @deprecated Use ConnectWiresToWires() returning handle by value instead.
        """

    @overload
    @staticmethod
    def ConnectWiresToWires__NCollection_HSequence__TopoDS_Shape(iwires: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None, toler: float, shared: bool, vertices: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """
        ConnectWiresToWires__NCollection_HSequence__TopoDS_Shape: the C++ overload ConnectWiresToWires(const occ::handle<NCollection_HSequence<TopoDS_Shape>> &, const double, const bool, occ::handle<NCollection_HSequence<TopoDS_Shape>> &, NCollection_DataMap<TopoDS_Shape, TopoDS_Shape, TopTools_ShapeMapHasher> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use ConnectWiresToWires() returning handle by value instead

        @deprecated Use ConnectWiresToWires() returning handle by value instead.
        """

    @staticmethod
    def SplitWires(wires: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None, toler: float, shared: bool) -> tuple[nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape], nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]]:
        """
        Extracts closed sub-wires out of <wires> and adds them
        to <closed>, open wires remained after extraction are put
        into <open>.
        If <shared> is True extraction is performed only when
        edges share the same vertex.
        If <shared> is False connection is performed only when
        ends of the edges are at distance less than <toler>.
        """

    @staticmethod
    def DispatchWires(wires: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None, closed: nanoocp.TopoDS.TopoDS_Compound, open: nanoocp.TopoDS.TopoDS_Compound) -> None:
        """
        Dispatches sequence of <wires> into two compounds
        <closed> for closed wires and <open> for open wires.
        If a compound is not empty wires are added into it.
        """

class ShapeAnalysis_FreeBoundsProperties:
    """
    This class is intended to calculate shape free bounds
    properties.
    This class provides the following functionalities:
    - calculates area of the contour,
    - calculates perimeter of the contour,
    - calculates ratio of average length to average width of the
    contour,
    - estimates average width of contour,
    - finds the notches (narrow 'V'-like sub-contour) on the
    contour.

    For getting free bounds this class uses
    ShapeAnalysis_FreeBounds class.

    For description of parameters used for initializing this
    class refer to CDL of ShapeAnalysis_FreeBounds.

    Properties of each contour are stored in the data structure
    ShapeAnalysis_FreeBoundData.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, shape: nanoocp.TopoDS.TopoDS_Shape, splitclosed: bool = False, splitopen: bool = False) -> None:
        """
        Creates the object and calls corresponding Init.
        <shape> should be a compound of shells.
        """

    @overload
    def __init__(self, shape: nanoocp.TopoDS.TopoDS_Shape, tolerance: float, splitclosed: bool = False, splitopen: bool = False) -> None:
        """
        Creates the object and calls corresponding Init.
        <shape> should be a compound of faces.
        """

    @overload
    def __init__(self, theOther: ShapeAnalysis_FreeBoundsProperties) -> None: ...

    @overload
    def Init(self, shape: nanoocp.TopoDS.TopoDS_Shape, tolerance: float, splitclosed: bool = False, splitopen: bool = False) -> None:
        """
        Initializes the object with given parameters.
        <shape> should be a compound of faces.
        """

    @overload
    def Init(self, shape: nanoocp.TopoDS.TopoDS_Shape, splitclosed: bool = False, splitopen: bool = False) -> None:
        """
        Initializes the object with given parameters.
        <shape> should be a compound of shells.
        """

    def Perform(self) -> bool:
        """
        Builds and analyzes free bounds of the shape.
        First calls ShapeAnalysis_FreeBounds for building free
        bounds.
        Then on each free bound computes its properties:
        - area of the contour,
        - perimeter of the contour,
        - ratio of average length to average width of the contour,
        - average width of contour,
        - notches on the contour and for each notch
        - maximum width of the notch.
        """

    def IsLoaded(self) -> bool:
        """Returns True if shape is loaded"""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns shape"""

    def Tolerance(self) -> float:
        """Returns tolerance"""

    def NbFreeBounds(self) -> int:
        """Returns number of free bounds"""

    def NbClosedFreeBounds(self) -> int:
        """Returns number of closed free bounds"""

    def NbOpenFreeBounds(self) -> int:
        """Returns number of open free bounds"""

    def ClosedFreeBounds(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.ShapeAnalysis.ShapeAnalysis_FreeBoundData]:
        """Returns all closed free bounds"""

    def OpenFreeBounds(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.ShapeAnalysis.ShapeAnalysis_FreeBoundData]:
        """Returns all open free bounds"""

    def ClosedFreeBound(self, index: int) -> ShapeAnalysis_FreeBoundData:
        """
        Returns properties of closed free bound specified by its rank
        number
        """

    def OpenFreeBound(self, index: int) -> ShapeAnalysis_FreeBoundData:
        """
        Returns properties of open free bound specified by its rank
        number
        """

    def DispatchBounds(self) -> bool: ...

    def CheckContours(self, prec: float = 0.0) -> bool: ...

    @overload
    def CheckNotches(self, prec: float = 0.0) -> bool: ...

    @overload
    def CheckNotches(self, freebound: nanoocp.TopoDS.TopoDS_Wire, num: int, notch: nanoocp.TopoDS.TopoDS_Wire, prec: float = 0.0) -> tuple[bool, float]: ...

    def CheckNotches__ShapeAnalysis_FreeBoundData(self, prec: float = 0.0) -> tuple[bool, ShapeAnalysis_FreeBoundData]:
        """
        CheckNotches__ShapeAnalysis_FreeBoundData: the C++ overload CheckNotches(occ::handle<ShapeAnalysis_FreeBoundData> &, const double); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        """

    def FillProperties(self, prec: float = 0.0) -> tuple[bool, ShapeAnalysis_FreeBoundData]: ...

class ShapeAnalysis_Geom:
    """Analyzing tool aimed to work on primitive geometrical objects"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeAnalysis_Geom) -> None: ...

    @staticmethod
    def NearestPlane(Pnts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], aPln: nanoocp.gp.gp_Pln) -> tuple[bool, float]:
        """
        Builds a plane out of a set of points in array
        Returns in <dmax> the maximal distance between the produced
        plane and given points
        """

    @staticmethod
    def PositionTrsf(coefs: nanoocp.NCollection.NCollection_HArray2[float] | None, trsf: nanoocp.gp.gp_Trsf, unit: float, prec: float) -> bool:
        """
        Builds transformation object out of matrix.
        Matrix must be 3 x 4.
        Unit is used as multiplier.
        """

class ShapeAnalysis_ShapeContents:
    """Dumps shape contents"""

    @overload
    def __init__(self) -> None:
        """Initialize fields and call ClearFlags()"""

    @overload
    def __init__(self, theOther: ShapeAnalysis_ShapeContents) -> None: ...

    def Clear(self) -> None:
        """Clears all accumulated statistics"""

    def ClearFlags(self) -> None:
        """Clears all flags"""

    def Perform(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Counts quantities of sun-shapes in shape and
        stores sub-shapes according to flags
        """

    def ModifyBigSplineMode(self) -> bool:
        """
        Returns (modifiable) the flag which defines whether to store faces
        with edges if its 3D curves has more than 8192 poles.
        """

    def SetModifyBigSplineMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModifyBigSplineMode() returns by reference in C++.
        """

    def ModifyIndirectMode(self) -> bool:
        """
        Returns (modifiable) the flag which defines whether to store faces on indirect surfaces.
        """

    def SetModifyIndirectMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModifyIndirectMode() returns by reference in C++.
        """

    def ModifyOffsetSurfaceMode(self) -> bool:
        """
        Returns (modifiable) the flag which defines whether to store faces on offset surfaces.
        """

    def SetModifyOffsetSurfaceMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModifyOffsetSurfaceMode() returns by reference in C++.
        """

    def ModifyTrimmed3dMode(self) -> bool:
        """
        Returns (modifiable) the flag which defines whether to store faces
        with edges if its 3D curves are trimmed curves
        """

    def SetModifyTrimmed3dMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModifyTrimmed3dMode() returns by reference in C++.
        """

    def ModifyOffsetCurveMode(self) -> bool:
        """
        Returns (modifiable) the flag which defines whether to store faces
        with edges if its 3D curves and pcurves are offset curves
        """

    def SetModifyOffsetCurveMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModifyOffsetCurveMode() returns by reference in C++.
        """

    def ModifyTrimmed2dMode(self) -> bool:
        """
        Returns (modifiable) the flag which defines whether to store faces
        with edges if its pcurves are trimmed curves
        """

    def SetModifyTrimmed2dMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModifyTrimmed2dMode() returns by reference in C++.
        """

    def NbSolids(self) -> int: ...

    def NbShells(self) -> int: ...

    def NbFaces(self) -> int: ...

    def NbWires(self) -> int: ...

    def NbEdges(self) -> int: ...

    def NbVertices(self) -> int: ...

    def NbSolidsWithVoids(self) -> int: ...

    def NbBigSplines(self) -> int: ...

    def NbC0Surfaces(self) -> int: ...

    def NbC0Curves(self) -> int: ...

    def NbOffsetSurf(self) -> int: ...

    def NbIndirectSurf(self) -> int: ...

    def NbOffsetCurves(self) -> int: ...

    def NbTrimmedCurve2d(self) -> int: ...

    def NbTrimmedCurve3d(self) -> int: ...

    def NbBSplibeSurf(self) -> int: ...

    def NbBezierSurf(self) -> int: ...

    def NbTrimSurf(self) -> int: ...

    def NbWireWitnSeam(self) -> int: ...

    def NbWireWithSevSeams(self) -> int: ...

    def NbFaceWithSevWires(self) -> int: ...

    def NbNoPCurve(self) -> int: ...

    def NbFreeFaces(self) -> int: ...

    def NbFreeWires(self) -> int: ...

    def NbFreeEdges(self) -> int: ...

    def NbSharedSolids(self) -> int: ...

    def NbSharedShells(self) -> int: ...

    def NbSharedFaces(self) -> int: ...

    def NbSharedWires(self) -> int: ...

    def NbSharedFreeWires(self) -> int: ...

    def NbSharedFreeEdges(self) -> int: ...

    def NbSharedEdges(self) -> int: ...

    def NbSharedVertices(self) -> int: ...

    def BigSplineSec(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]: ...

    def IndirectSec(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]: ...

    def OffsetSurfaceSec(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]: ...

    def Trimmed3dSec(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]: ...

    def OffsetCurveSec(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]: ...

    def Trimmed2dSec(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]: ...

    def ModifyOffestSurfaceMode(self) -> bool:
        """Deprecated in OCCT: ModifyOffsetSurfaceMode() should be used instead"""

    def SetModifyOffestSurfaceMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModifyOffestSurfaceMode() returns by reference in C++.
        """

class ShapeAnalysis_ShapeTolerance:
    """
    Tool for computing shape tolerances (minimal, maximal, average),
    finding shape with tolerance matching given criteria,
    setting or limitating tolerances.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: ShapeAnalysis_ShapeTolerance) -> None: ...

    def Tolerance(self, shape: nanoocp.TopoDS.TopoDS_Shape, mode: int, type: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> float:
        """
        Determines a tolerance from the ones stored in a shape
        Remark : calls InitTolerance and AddTolerance,
        hence, can be used to start a series for cumulating tolerance
        <mode> = 0 : returns the average value between sub-shapes,
        <mode> > 0 : returns the maximal found,
        <mode> < 0 : returns the minimal found.
        <type> defines what kinds of sub-shapes to consider:
        SHAPE (default) : all : VERTEX, EDGE, FACE,
        VERTEX : only vertices,
        EDGE   : only edges,
        FACE   : only faces,
        SHELL  : combined SHELL + FACE, for each face (and containing
        shell), also checks EDGE and VERTEX
        """

    def OverTolerance(self, shape: nanoocp.TopoDS.TopoDS_Shape, value: float, type: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Determines which shapes have a tolerance over the given value
        <type> is interpreted as in the method Tolerance
        """

    def InTolerance(self, shape: nanoocp.TopoDS.TopoDS_Shape, valmin: float, valmax: float, type: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Determines which shapes have a tolerance within a given interval
        <type> is interpreted as in the method Tolerance
        """

    def InitTolerance(self) -> None:
        """Initializes computation of cumulated tolerance"""

    def AddTolerance(self, shape: nanoocp.TopoDS.TopoDS_Shape, type: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE) -> None:
        """
        Adds data on new Shape to compute Cumulated Tolerance
        (prepares three computations : maximal, average, minimal)
        """

    def GlobalTolerance(self, mode: int) -> float:
        """
        Returns the computed tolerance according to the <mode>
        <mode> = 0 : average
        <mode> > 0 : maximal
        <mode> < 0 : minimal
        """

class ShapeAnalysis_Shell:
    """
    This class provides operators to analyze edges orientation
    in the shell.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: ShapeAnalysis_Shell) -> None: ...

    def Clear(self) -> None:
        """Clears data about loaded shells and performed checks"""

    def LoadShells(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Adds shells contained in the <shape> to the list of loaded shells"""

    def CheckOrientedShells(self, shape: nanoocp.TopoDS.TopoDS_Shape, alsofree: bool = False, checkinternaledges: bool = False) -> bool:
        """
        Checks if shells fulfill orientation condition, i.e. if each
        edge is, either present once (free edge) or twice (connected
        edge) but with different orientations (FORWARD/REVERSED)
        Edges which do not fulfill these conditions are bad

        If <alsofree> is True free edges are considered.
        Free edges can be queried but are not bad
        """

    def IsLoaded(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Tells if a shape is loaded (only shells are checked)"""

    def NbLoaded(self) -> int:
        """Returns the actual number of loaded shapes (i.e. shells)"""

    def Loaded(self, num: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns a loaded shape specified by its rank number.
        Returns null shape if <num> is out of range
        """

    def HasBadEdges(self) -> bool:
        """Tells if at least one edge is recorded as bad"""

    def BadEdges(self) -> nanoocp.TopoDS.TopoDS_Compound:
        """
        Returns the list of bad edges as a Compound
        It is empty (not null) if no edge are recorded as bad
        """

    def HasFreeEdges(self) -> bool:
        """Tells if at least one edge is recorded as free (not connected)"""

    def FreeEdges(self) -> nanoocp.TopoDS.TopoDS_Compound:
        """
        Returns the list of free (not connected) edges as a Compound
        It is empty (not null) if no edge are recorded as free
        """

    def HasConnectedEdges(self) -> bool:
        """Tells if at least one edge is connected (shared twice or more)"""

class ShapeAnalysis_Surface(nanoocp.Standard.Standard_Transient):
    """
    Complements standard tool Geom_Surface by providing additional
    functionality for detection surface singularities, checking
    spatial surface closure and computing projections of 3D points
    onto a surface.

    * The singularities
    Each singularity stores the precision with which corresponding
    surface iso-line is considered as degenerated.
    The number of singularities is determined by specifying precision
    and always not greater than 4.

    * The spatial closure
    The check for spatial closure is performed with given precision
    (default value is Precision::Confusion).
    If Geom_Surface says that the surface is closed, this class
    also says this. Otherwise additional analysis is performed.

    * The parameters of 3D point on the surface
    The projection of the point is performed with given precision.
    This class tries to find a solution taking into account possible
    singularities.
    Additional method for searching the solution from already built
    one is also provided.

    This tool is optimised: computes most information only once
    """

    def __init__(self, S: nanoocp.Geom.Geom_Surface | None) -> None:
        """Creates an analyzer object on the basis of existing surface"""

    @overload
    def Init(self, S: nanoocp.Geom.Geom_Surface | None) -> None:
        """Loads existing surface"""

    @overload
    def Init(self, other: ShapeAnalysis_Surface | None) -> None:
        """Reads all the data from another Surface, without recomputing"""

    def SetDomain(self, U1: float, U2: float, V1: float, V2: float) -> None: ...

    def Surface(self) -> nanoocp.Geom.Geom_Surface:
        """Returns a surface being analyzed"""

    def Adaptor3d(self) -> nanoocp.GeomAdaptor.GeomAdaptor_Surface:
        """
        Returns the Adaptor.
        Creates it if not yet done.
        """

    def TrueAdaptor3d(self) -> nanoocp.GeomAdaptor.GeomAdaptor_Surface:
        """Returns the Adaptor (may be Null if method Adaptor() was not called)"""

    def Gap(self) -> float:
        """
        Returns 3D distance found by one of the following methods.
        IsDegenerated, DegeneratedValues, ProjectDegenerated
        (distance between 3D point and found or last (if not found)
        singularity),
        IsUClosed, IsVClosed (minimum value of precision to consider
        the surface to be closed),
        ValueOfUV (distance between 3D point and found solution).
        """

    @overload
    def Value(self, u: float, v: float) -> nanoocp.gp.gp_Pnt:
        """
        Returns a 3D point specified by parameters in surface
        parametrical space
        """

    @overload
    def Value(self, p2d: nanoocp.gp.gp_Pnt2d) -> nanoocp.gp.gp_Pnt:
        """
        Returns a 3d point specified by a point in surface
        parametrical space
        """

    def HasSingularities(self, preci: float) -> bool:
        """
        Returns True if the surface has singularities for the given
        precision (i.e. if there are surface singularities with sizes
        not greater than precision).
        """

    def NbSingularities(self, preci: float) -> int:
        """
        Returns the number of singularities for the given precision
        (i.e. number of surface singularities with sizes not greater
        than precision).
        """

    def Singularity(self, num: int, P3d: nanoocp.gp.gp_Pnt, firstP2d: nanoocp.gp.gp_Pnt2d, lastP2d: nanoocp.gp.gp_Pnt2d) -> tuple[bool, float, float, float, bool]:
        """
        Returns the characteristics of the singularity specified by
        its rank number <num>.
        That means, that it is not necessary for <num> to be in the
        range [1, NbSingularities] but must be not greater than
        possible (see ComputeSingularities).
        The returned characteristics are:
        preci: the smallest precision with which the iso-line is
        considered as degenerated,
        P3d: 3D point of singularity (middle point of the surface
        iso-line),
        firstP2d and lastP2d: first and last 2D points of the
        iso-line in parametrical surface,
        firstpar and lastpar: first and last parameters of the
        iso-line in parametrical surface,
        uisodeg: if the degenerated iso-line is U-iso (True) or
        V-iso (False).
        Returns False if <num> is out of range, else returns True.
        """

    @overload
    def IsDegenerated(self, P3d: nanoocp.gp.gp_Pnt, preci: float) -> bool:
        """
        Returns True if there is at least one surface boundary which
        is considered as degenerated with <preci> and distance
        between P3d and corresponding singular point is less than
        <preci>
        """

    @overload
    def IsDegenerated(self, p2d1: nanoocp.gp.gp_Pnt2d, p2d2: nanoocp.gp.gp_Pnt2d, tol: float, ratio: float) -> bool:
        """
        Returns True if straight pcurve going from point p2d1 to p2d2
        is degenerate, i.e. lies in the singularity of the surface.
        NOTE: it uses another method of detecting singularity than
        used by ComputeSingularities() et al.!
        For that, maximums of distances between points p2d1, p2d2
        and 0.5*(p2d1+p2d2) and between corresponding 3d points are
        computed.
        The pcurve (p2d1, p2d2) is considered as degenerate if:
        - max distance in 3d is less than <tol>
        - max distance in 2d is at least <ratio> times greater than
        the Resolution computed from max distance in 3d
        (max3d < tol && max2d > ratio * Resolution(max3d))
        NOTE: <ratio> should be >1 (e.g. 10)
        """

    def DegeneratedValues(self, P3d: nanoocp.gp.gp_Pnt, preci: float, firstP2d: nanoocp.gp.gp_Pnt2d, lastP2d: nanoocp.gp.gp_Pnt2d, forward: bool = True) -> tuple[bool, float, float]:
        """
        Returns True if there is at least one surface iso-line which
        is considered as degenerated with <preci> and distance
        between P3d and corresponding singular point is less than
        <preci> (like IsDegenerated).
        Returns characteristics of the first found boundary matching
        those criteria.
        """

    @overload
    def ProjectDegenerated(self, P3d: nanoocp.gp.gp_Pnt, preci: float, neighbour: nanoocp.gp.gp_Pnt2d, result: nanoocp.gp.gp_Pnt2d) -> bool:
        """
        Projects a point <P3d> on a singularity by computing
        one of the coordinates of preliminary computed <result>.

        Finds the iso-line which is considered as degenerated with
        <preci> and
        a. distance between P3d and corresponding singular point is
        less than <preci> (like IsDegenerated) or
        b. difference between already computed <result>'s coordinate
        and iso-coordinate of the boundary is less than 2D
        resolution (computed from <preci> by Geom_Adaptor).
        Then sets not yet computed <result>'s coordinate taking it
        from <neighbour> and returns True.
        """

    @overload
    def ProjectDegenerated(self, nbrPnt: int, points: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt], pnt2d: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt2d], preci: float, direct: bool) -> bool:
        """
        Checks points at the beginning (direct is True) or end
        (direct is False) of array <points> to lie in singularity of
        surface, and if yes, adjusts the indeterminate 2d coordinate
        of these points by nearest point which is not in singularity.
        Returns True if some points were adjusted.
        """

    def Bounds(self) -> tuple[float, float, float, float]:
        """
        Returns the bounds of the surface
        (from Bounds from Surface, but buffered)
        """

    def ComputeBoundIsos(self) -> None:
        """Computes bound isos (protected against exceptions)"""

    def UIso(self, U: float) -> nanoocp.Geom.Geom_Curve:
        """
        Returns a U-Iso. Null if not possible or failed
        Remark : bound isos are buffered
        """

    def VIso(self, V: float) -> nanoocp.Geom.Geom_Curve:
        """
        Returns a V-Iso. Null if not possible or failed
        Remark : bound isos are buffered
        """

    def IsUClosed(self, preci: float = -1.0) -> bool:
        """
        Tells if the Surface is spatially closed in U with given
        precision. If <preci> < 0 then Precision::Confusion is used.
        If Geom_Surface says that the surface is U-closed, this method
        also says this. Otherwise additional analysis is performed,
        comparing given precision with the following distances:
        - periodic B-Splines are closed,
        - polynomial B-Spline with boundary multiplicities degree+1
        and Bezier - maximum distance between poles,
        - rational B-Spline or one with boundary multiplicities not
        degree+1 - maximum distance computed at knots and their
        middles,
        - surface of extrusion - distance between ends of basis
        curve,
        - other (RectangularTrimmed and Offset) - maximum distance
        computed at 100 equi-distanted points.
        """

    def IsVClosed(self, preci: float = -1.0) -> bool:
        """
        Tells if the Surface is spatially closed in V with given
        precision. If <preci> < 0 then Precision::Confusion is used.
        If Geom_Surface says that the surface is V-closed, this method
        also says this. Otherwise additional analysis is performed,
        comparing given precision with the following distances:
        - periodic B-Splines are closed,
        - polynomial B-Spline with boundary multiplicities degree+1
        and Bezier - maximum distance between poles,
        - rational B-Spline or one with boundary multiplicities not
        degree+1 - maximum distance computed at knots and their
        middles,
        - surface of revolution - distance between ends of basis
        curve,
        - other (RectangularTrimmed and Offset) - maximum distance
        computed at 100 equi-distanted points.
        """

    def ValueOfUV(self, P3D: nanoocp.gp.gp_Pnt, preci: float) -> nanoocp.gp.gp_Pnt2d:
        """
        Computes the parameters in the surface parametrical space of
        3D point.
        The result is parameters of the point projected onto the
        surface.
        This method enhances functionality provided by the standard
        tool GeomAPI_ProjectPointOnSurface by treatment of cases when
        the projected point is near to the surface boundaries and
        when this standard tool fails.
        """

    def NextValueOfUV(self, p2dPrev: nanoocp.gp.gp_Pnt2d, P3D: nanoocp.gp.gp_Pnt, preci: float, maxpreci: float = -1.0) -> nanoocp.gp.gp_Pnt2d:
        """
        Projects a point P3D on the surface.
        Does the same thing as ValueOfUV but tries to optimize
        computations by taking into account previous point <p2dPrev>:
        makes a step by UV and tries Newton algorithm.
        If <maxpreci> >0. and distance between solution and
        P3D is greater than <maxpreci>, that solution is considered
        as bad, and ValueOfUV() is used.
        If not succeeded, calls ValueOfUV()
        """

    def UVFromIso(self, P3D: nanoocp.gp.gp_Pnt, preci: float) -> tuple[float, float, float]:
        """
        Tries a refinement of an already computed couple (U,V) by
        using projecting 3D point on iso-lines:
        1. boundaries of the surface,
        2. iso-lines passing through (U,V)
        3. iteratively received iso-lines passing through new U and
        new V (number of iterations is limited by 5 in each
        direction)
        Returns the best resulting distance between P3D and Value(U,V)
        in the case of success. Else, returns a very great value
        """

    def UCloseVal(self) -> float:
        """Returns minimum value to consider the surface as U-closed"""

    def VCloseVal(self) -> float:
        """Returns minimum value to consider the surface as V-closed"""

    def GetBoxUF(self) -> nanoocp.Bnd.Bnd_Box: ...

    def GetBoxUL(self) -> nanoocp.Bnd.Bnd_Box: ...

    def GetBoxVF(self) -> nanoocp.Bnd.Bnd_Box: ...

    def GetBoxVL(self) -> nanoocp.Bnd.Bnd_Box: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeAnalysis_TransferParameters(nanoocp.Standard.Standard_Transient):
    """
    This tool is used for transferring parameters
    from 3d curve of the edge to pcurve and vice versa.

    Default behaviour is to trsnafer parameters with help
    of linear transformation:

    T2d = myShift + myScale * T3d
    where
    myScale = ( Last2d - First2d ) / ( Last3d - First3d )
    myShift = First2d - First3d * myScale
    [First3d, Last3d] and [First2d, Last2d] are ranges of
    edge on curve and pcurve

    This behaviour can be redefined in derived classes, for example,
    using projection.
    """

    @overload
    def __init__(self) -> None:
        """Creates empty tool with myShift = 0 and myScale = 1"""

    @overload
    def __init__(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Creates a tool and initializes it with edge and face"""

    @overload
    def __init__(self, theOther: ShapeAnalysis_TransferParameters) -> None: ...

    def Init(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Initialize a tool with edge and face"""

    def SetMaxTolerance(self, maxtol: float) -> None:
        """
        Sets maximal tolerance to use linear recomputation of
        parameters.
        """

    @overload
    def Perform(self, Params: nanoocp.NCollection.NCollection_HSequence[float] | None, To2d: bool) -> nanoocp.NCollection.NCollection_HSequence[float]:
        """
        Transfers parameters given by sequence Params from 3d curve
        to pcurve (if To2d is True) or back (if To2d is False)
        """

    @overload
    def Perform(self, Param: float, To2d: bool) -> float:
        """
        Transfers parameter given by sequence Params from 3d curve
        to pcurve (if To2d is True) or back (if To2d is False)
        """

    def TransferRange(self, newEdge: nanoocp.TopoDS.TopoDS_Edge, prevPar: float, currPar: float, To2d: bool) -> None:
        """
        Recomputes range of curves from NewEdge.
        If Is2d equals True parameters are recomputed by curve2d else by curve3d.
        """

    def IsSameRange(self) -> bool:
        """
        Returns True if 3d curve of edge and pcurve are SameRange
        (in default implementation, if myScale == 1 and myShift == 0)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeAnalysis_TransferParametersProj(ShapeAnalysis_TransferParameters):
    """
    This tool is used for transferring parameters
    from 3d curve of the edge to pcurve and vice versa.
    This tool transfers parameters with help of
    projection points from curve 3d on curve 2d and
    vice versa
    """

    @overload
    def __init__(self) -> None:
        """Creates empty constructor."""

    @overload
    def __init__(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def __init__(self, theOther: ShapeAnalysis_TransferParametersProj) -> None: ...

    def Init(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def Perform(self, Papams: nanoocp.NCollection.NCollection_HSequence[float] | None, To2d: bool) -> nanoocp.NCollection.NCollection_HSequence[float]:
        """
        Transfers parameters given by sequence Params from 3d curve
        to pcurve (if To2d is True) or back (if To2d is False)
        """

    @overload
    def Perform(self, Param: float, To2d: bool) -> float:
        """
        Transfers parameter given by Param from 3d curve
        to pcurve (if To2d is True) or back (if To2d is False)
        """

    def ForceProjection(self) -> bool:
        """
        Returns modifiable flag forcing projection
        If it is False (default), projection is done only
        if edge is not SameParameter or if tolerance of edge
        is greater than MaxTolerance()
        """

    def SetForceProjection(self, theValue: bool) -> None:
        """
        Python addition: sets the value ForceProjection() returns by reference in C++.
        """

    def TransferRange(self, newEdge: nanoocp.TopoDS.TopoDS_Edge, prevPar: float, currPar: float, Is2d: bool) -> None:
        """
        Recomputes range of curves from NewEdge.
        If Is2d equals True parameters are recomputed by curve2d else by curve3d.
        """

    def IsSameRange(self) -> bool:
        """Returns False;"""

    @overload
    @staticmethod
    def CopyNMVertex(theVert: nanoocp.TopoDS.TopoDS_Vertex, toedge: nanoocp.TopoDS.TopoDS_Edge, fromedge: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Make a copy of non-manifold vertex theVert
        (i.e. create new TVertex and replace PointRepresentations for this vertex
        from fromedge to toedge. Other representations were copied)
        """

    @overload
    @staticmethod
    def CopyNMVertex(theVert: nanoocp.TopoDS.TopoDS_Vertex, toFace: nanoocp.TopoDS.TopoDS_Face, fromFace: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Make a copy of non-manifold vertex theVert
        (i.e. create new TVertex and replace PointRepresentations for this vertex
        from fromFace to toFace. Other representations were copied)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeAnalysis_Wire(nanoocp.Standard.Standard_Transient):
    """
    This class provides analysis of a wire to be compliant to
    CAS.CADE requirements.

    The functionalities provided are the following:
    1. consistency of 2d and 3d edge curve senses
    2. connection of adjacent edges regarding to:
    a. their vertices
    b. their pcurves
    c. their 3d curves
    3. adjacency of the edge vertices to its pcurve and 3d curve
    4. if a wire is closed or not (considering its 3d and 2d
    contour)
    5. if a wire is outer on its face (considering pcurves)

    This class can be used in conjunction with class
    ShapeFix_Wire, which will fix the problems detected by this class.

    The methods of the given class match to ones of the class
    ShapeFix_Wire, e.g., CheckSmall and FixSmall.
    This class also includes some auxiliary methods
    (e.g., CheckOuterBound, etc.),
    which have no pair in ShapeFix_Wire.

    Like methods of ShapeFix_Wire the ones of this class are
    grouped into two levels:
    - Public which are recommended for use (the most global
    method is Perform),
    - Advanced, for optional use only

    For analyzing result of Public API checking methods use
    corresponding Status... method.
    The 'advanced' functions share the single status field which
    contains the result of the last performed 'advanced' method.
    It is queried by the method LastCheckStatus().

    In order to prepare an analyzer, it is necessary to load a wire,
    set face and precision.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, wire: nanoocp.TopoDS.TopoDS_Wire, face: nanoocp.TopoDS.TopoDS_Face, precision: float) -> None:
        """
        Creates object with standard TopoDS_Wire, face
        and precision
        """

    @overload
    def __init__(self, sbwd: nanoocp.ShapeExtend.ShapeExtend_WireData | None, face: nanoocp.TopoDS.TopoDS_Face, precision: float) -> None:
        """
        Creates the object with WireData object, face
        and precision
        """

    @overload
    def __init__(self, theOther: ShapeAnalysis_Wire) -> None: ...

    @overload
    def Init(self, wire: nanoocp.TopoDS.TopoDS_Wire, face: nanoocp.TopoDS.TopoDS_Face, precision: float) -> None:
        """
        Initializes the object with standard TopoDS_Wire, face
        and precision
        """

    @overload
    def Init(self, sbwd: nanoocp.ShapeExtend.ShapeExtend_WireData | None, face: nanoocp.TopoDS.TopoDS_Face, precision: float) -> None:
        """
        Initializes the object with WireData object, face
        and precision
        """

    @overload
    def Load(self, wire: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Loads the object with standard TopoDS_Wire"""

    @overload
    def Load(self, sbwd: nanoocp.ShapeExtend.ShapeExtend_WireData | None) -> None:
        """Loads the object with WireData object"""

    @overload
    def SetFace(self, face: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Loads the face the wire lies on"""

    @overload
    def SetFace(self, theFace: nanoocp.TopoDS.TopoDS_Face, theSurfaceAnalysis: ShapeAnalysis_Surface | None) -> None:
        """Loads the face the wire lies on and surface analysis object"""

    @overload
    def SetSurface(self, theSurfaceAnalysis: ShapeAnalysis_Surface | None) -> None:
        """Loads the surface analysis object"""

    @overload
    def SetSurface(self, surface: nanoocp.Geom.Geom_Surface | None) -> None: ...

    @overload
    def SetSurface(self, surface: nanoocp.Geom.Geom_Surface | None, location: nanoocp.TopLoc.TopLoc_Location) -> None:
        """Loads the surface the wire lies on"""

    def SetPrecision(self, precision: float) -> None: ...

    def ClearStatuses(self) -> None:
        """
        Unsets all the status and distance fields
        wire, face and precision are not cleared
        """

    def IsLoaded(self) -> bool:
        """Returns True if wire is loaded and has number of edges >0"""

    def IsReady(self) -> bool:
        """Returns True if IsLoaded and underlying face is not null"""

    def Precision(self) -> float:
        """Returns the value of precision"""

    def WireData(self) -> nanoocp.ShapeExtend.ShapeExtend_WireData:
        """Returns wire object being analyzed"""

    def NbEdges(self) -> int:
        """Returns the number of edges in the wire, or 0 if it is not loaded"""

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns the working face"""

    def Surface(self) -> ShapeAnalysis_Surface:
        """Returns the working surface"""

    def Perform(self) -> bool:
        """
        Performs all the checks in the following order :
        CheckOrder, CheckSmall, CheckConnected, CheckEdgeCurves,
        CheckDegenerated, CheckSelfIntersection, CheckLacking,
        CheckClosed
        Returns: True if at least one method returned True;
        For deeper analysis use Status...(status) methods
        """

    @overload
    def CheckOrder(self, isClosed: bool = True, mode3d: bool = True) -> bool:
        """
        Calls CheckOrder and returns False if wire is already
        ordered (tail-to-head), True otherwise
        Flag <isClosed> defines if the wire is closed or not
        Flag <mode3d> defines which mode is used (3d or 2d)
        """

    @overload
    def CheckOrder(self, sawo: ShapeAnalysis_WireOrder, isClosed: bool = True, theMode3D: bool = True, theModeBoth: bool = False) -> bool:
        """
        Analyzes the order of the edges in the wire,
        uses class WireOrder for that purpose.
        Flag <isClosed> defines if the wire is closed or not
        Flag <theMode3D> defines 3D or 2d mode.
        Flag <theModeBoth> defines miscible mode and the flag <theMode3D> is ignored.
        Returns False if wire is already ordered (tail-to-head),
        True otherwise.
        Use returned WireOrder object for deeper analysis.
        Status:
        OK   : the same edges orientation, the same edges sequence
        DONE1: the same edges orientation, not the same edges sequence
        DONE2: as DONE1 and gaps more than myPrecision
        DONE3: not the same edges orientation (some need to be reversed)
        DONE4: as DONE3 and gaps more than myPrecision
        FAIL : algorithm failed (could not detect order)
        """

    @overload
    def CheckConnected(self, prec: float = 0.0) -> bool:
        """
        Calls to CheckConnected for each edge
        Returns: True if at least one pair of disconnected edges (not sharing the
        same vertex) was detected
        """

    @overload
    def CheckConnected(self, num: int, prec: float = 0.0) -> bool:
        """
        Checks connected edges (num-th and preceding).
        Tests with starting preci from <SBWD> or with <prec> if
        it is greater.
        Considers Vertices.
        Returns: False if edges are connected by the common vertex, else True
        Status  :
        OK    : Vertices (end of num-1 th edge and start on num-th one)
        are already the same
        DONE1 : Absolutely confused (gp::Resolution)
        DONE2 : Confused at starting <preci> from <SBWD>
        DONE3 : Confused at <prec> but not <preci>
        FAIL1 : Not confused
        FAIL2 : Not confused but confused with <preci> if reverse num-th edge
        """

    @overload
    def CheckSmall(self, precsmall: float = 0.0) -> bool:
        """
        Calls to CheckSmall for each edge
        Returns: True if at least one small edge was detected
        """

    @overload
    def CheckSmall(self, num: int, precsmall: float = 0.0) -> bool:
        """
        Checks if an edge has a length not greater than myPreci or
        precsmall (if it is smaller)
        Returns: False if its length is greater than precision
        Status:
        OK   : edge is not small or degenerated
        DONE1: edge is small, vertices are the same
        DONE2: edge is small, vertices are not the same
        FAIL : no 3d curve and pcurve
        """

    def CheckEdgeCurves(self) -> bool:
        """
        Checks edges geometry (consistency of 2d and 3d senses, adjasment
        of curves to the vertices, etc.).
        The order of the checks :
        Call ShapeAnalysis_Wire to check:
        ShapeAnalysis_Edge::CheckCurve3dWithPCurve  (1),
        ShapeAnalysis_Edge::CheckVertcesWithPCurve  (2),
        ShapeAnalysis_Edge::CheckVertcesWithCurve3d (3),
        CheckSeam                                   (4)
        Additional:
        CheckGap3d                                  (5),
        CheckGap2d                                  (6),
        ShapeAnalysis_Edge::CheckSameParameter      (7)
        Returns: True if at least one check returned True
        Remark:  The numbers in brackets show with what DONEi or FAILi
        the status can be queried
        """

    @overload
    def CheckDegenerated(self) -> bool:
        """
        Calls to CheckDegenerated for each edge
        Returns: True if at least one incorrect degenerated edge was detected
        """

    @overload
    def CheckDegenerated(self, num: int, dgnr1: nanoocp.gp.gp_Pnt2d, dgnr2: nanoocp.gp.gp_Pnt2d) -> bool:
        """
        Checks for degenerated edge between two adjacent ones.
        Fills parameters dgnr1 and dgnr2 with points in parametric
        space that correspond to the singularity (either gap that
        needs to be filled by degenerated edge or that already filled)
        Returns: False if no singularity or edge is already degenerated,
        otherwise True
        Status:
        OK   : No surface singularity, or edge is already degenerated
        DONE1: Degenerated edge should be inserted (gap in 2D)
        DONE2: Edge <num> should be made degenerated (recompute pcurve
        and set the flag)
        FAIL1: One of edges neighbouring to degenerated one has
        no pcurve
        FAIL2: Edge marked as degenerated and has no pcurve
        but singularity is not detected
        """

    @overload
    def CheckDegenerated(self, num: int) -> bool:
        """
        Checks for degenerated edge between two adjacent ones.
        Remark : Calls previous function
        Status : See the function above for details
        """

    def CheckClosed(self, prec: float = 0.0) -> bool:
        """
        Checks if wire is closed, performs CheckConnected,
        CheckDegenerated and CheckLacking for the first and the last edges
        Returns: True if at least one check returned True
        Status:
        FAIL1 or DONE1: see CheckConnected
        FAIL2 or DONE2: see CheckDegenerated
        """

    def CheckSelfIntersection(self) -> bool:
        """
        Checks self-intersection of the wire (considering pcurves)
        Looks for self-intersecting edges and each pair of intersecting
        edges.
        Warning: It does not check each edge with any other one (only each two
        adjacent edges)
        The order of the checks :
        CheckSelfIntersectingEdge, CheckIntersectingEdges
        Returns: True if at least one check returned True
        Status:  FAIL1 or DONE1 - see CheckSelfIntersectingEdge
        FAIL2 or DONE2 - see CheckIntersectingEdges
        """

    @overload
    def CheckLacking(self) -> bool:
        """
        Calls to CheckLacking for each edge
        Returns: True if at least one lacking edge was detected
        """

    @overload
    def CheckLacking(self, num: int, Tolerance: float, p2d1: nanoocp.gp.gp_Pnt2d, p2d2: nanoocp.gp.gp_Pnt2d) -> bool:
        """
        Checks if there is a gap in 2d between edges, not comprised by
        the tolerance of their common vertex.
        If <Tolerance> is greater than 0. and less than tolerance of
        the vertex, then this value is used for check.
        Returns: True if not closed gap was detected
        p2d1 and p2d2 are the endpoint of <num-1>th edge and start of
        the <num>th edge in 2d.
        Status:
        OK: No edge is lacking (3d and 2d connection)
        FAIL1: edges have no vertices (at least one of them)
        FAIL2: edges are neither connected by common vertex, nor have
        coincided vertices
        FAIL1: edges have no pcurves
        DONE1: the gap is detected which cannot be closed by the tolerance
        of the common vertex (or with value of <Tolerance>)
        DONE2: is set (together with DONE1) if gap is detected and the
        vector (p2d2 - p2d1) goes in direction opposite to the pcurves
        of the edges (if angle is more than 0.9*PI).
        """

    @overload
    def CheckLacking(self, num: int, Tolerance: float = 0.0) -> bool:
        """
        Checks if there is a gap in 2D between edges and not comprised by vertex tolerance
        The value of SBWD.thepreci is used.
        Returns: False if no edge should be inserted
        Status:
        OK    : No edge is lacking (3d and 2d connection)
        DONE1 : The vertex tolerance should be increased only (2d gap is
        small)
        DONE2 : Edge can be inserted (3d and 2d gaps are large enough)
        """

    def CheckGaps3d(self) -> bool: ...

    def CheckGaps2d(self) -> bool: ...

    def CheckCurveGaps(self) -> bool: ...

    def CheckSeam__Geom2d_Curve__Geom2d_Curve__float__float(self, num: int) -> tuple[bool, nanoocp.Geom2d.Geom2d_Curve, nanoocp.Geom2d.Geom2d_Curve, float, float]:
        """
        CheckSeam__Geom2d_Curve__Geom2d_Curve__float__float: the C++ overload CheckSeam(const int, occ::handle<Geom2d_Curve> &, occ::handle<Geom2d_Curve> &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Checks if a seam pcurves are correct oriented
        Returns: False (status OK) if given edge is not a seam or if it is OK
        C1 - current pcurve for FORWARD edge,
        C2 - current pcurve for REVERSED edge (if returns True they
        should be swapped for the seam),
        cf, cl - first and last parameters on curves
        Status:
        OK   : Pcurves are correct or edge is not seam
        DONE : Seam pcurves should be swapped
        """

    def CheckSeam(self, num: int) -> bool:
        """
        Checks if a seam pcurves are correct oriented
        See previous functions for details
        """

    def CheckGap3d(self, num: int = 0) -> bool:
        """
        Checks gap between edges in 3D (3d curves).
        Checks the distance between ends of 3d curves of the num-th
        and preceding edge.
        The distance can be queried by MinDistance3d.

        Returns: True if status is DONE
        Status:
        OK   : Gap is less than myPrecision
        DONE : Gap is greater than myPrecision
        FAIL : No 3d curve(s) on the edge(s)
        """

    def CheckGap2d(self, num: int = 0) -> bool:
        """
        Checks gap between edges in 2D (pcurves).
        Checks the distance between ends of pcurves of the num-th
        and preceding edge.
        The distance can be queried by MinDistance2d.

        Returns: True if status is DONE
        Status:
        OK   : Gap is less than parametric precision out of myPrecision
        DONE : Gap is greater than parametric precision out of myPrecision
        FAIL : No pcurve(s) on the edge(s)
        """

    def CheckCurveGap(self, num: int = 0) -> bool:
        """
        Checks gap between points on 3D curve and points on surface
        generated by pcurve of the num-th edge.
        The distance can be queried by MinDistance3d.

        Returns: True if status is DONE
        Status:
        OK   : Gap is less than myPrecision
        DONE : Gap is greater than myPrecision
        FAIL : No 3d curve(s) on the edge(s)
        """

    @overload
    def CheckSelfIntersectingEdge(self, num: int, points2d: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntRes2d.IntRes2d_IntersectionPoint], points3d: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt]) -> bool:
        """
        Checks if num-th edge is self-intersecting.
        Self-intersection is reported only if intersection point lies outside
        of both end vertices of the edge.
        Returns: True if edge is self-intersecting.
        If returns True it also fills the sequences of intersection points
        and corresponding 3d points (only that are not enclosed by a vertices)
        Status:
        FAIL1 : No pcurve
        FAIL2 : No vertices
        DONE1 : Self-intersection found
        """

    @overload
    def CheckSelfIntersectingEdge(self, num: int) -> bool: ...

    @overload
    def CheckIntersectingEdges(self, num: int, points2d: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntRes2d.IntRes2d_IntersectionPoint], points3d: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt], errors: nanoocp.NCollection.NCollection_Sequence[float]) -> bool:
        """
        Checks two adjacent edges for intersecting.
        Intersection is reported only if intersection point is not enclosed
        by the common end vertex of the edges.
        Returns: True if intersection is found.
        If returns True it also fills the sequences of intersection points,
        corresponding 3d points, and errors for them (half-distances between
        intersection points in 3d calculated from one and from another edge)
        Status:
        FAIL1 : No pcurve
        FAIL2 : No vertices
        DONE1 : Self-intersection found
        """

    @overload
    def CheckIntersectingEdges(self, num: int) -> bool:
        """
        Checks two adjacent edges for intersecting.
        Remark : Calls the previous method
        Status : See the function above for details
        """

    @overload
    def CheckIntersectingEdges(self, num1: int, num2: int, points2d: nanoocp.NCollection.NCollection_Sequence[nanoocp.IntRes2d.IntRes2d_IntersectionPoint], points3d: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt], errors: nanoocp.NCollection.NCollection_Sequence[float]) -> bool:
        """
        Checks i-th and j-th edges for intersecting.
        Remark : See the previous method for details
        """

    @overload
    def CheckIntersectingEdges(self, num1: int, num2: int) -> bool:
        """
        Checks i-th and j-th edges for intersecting.
        Remark : Calls previous method.
        Status : See the function above for details
        """

    def CheckOuterBound(self, APIMake: bool = True) -> bool:
        """
        Checks if wire defines an outer bound on the face
        Uses ShapeAnalysis::IsOuterBound for analysis
        If <APIMake> is True uses BRepAPI_MakeWire to build the
        wire, if False (to be used only when edges share common
        vertices) uses BRep_Builder to build the wire
        """

    def CheckNotchedEdges(self, num: int, Tolerance: float = 0.0) -> tuple[bool, int, float]:
        """Detects a notch"""

    def CheckSmallArea(self, theWire: nanoocp.TopoDS.TopoDS_Wire) -> bool:
        """Checks if wire has parametric area less than precision."""

    def CheckShapeConnect(self, shape: nanoocp.TopoDS.TopoDS_Shape, prec: float = 0.0) -> bool:
        """
        Checks with what orientation <shape> (wire or edge) can be
        connected to the wire.
        Tests distances with starting <preci> from <SBWD> (close confusion),
        but if given <prec> is greater, tests with <prec> (coarse confusion).
        The smallest found distance can be returned by MinDistance3d

        Returns: False if status is FAIL (see below)
        Status:
        DONE1 : If <shape> follows <SBWD>, direct sense (normal)
        DONE2 : If <shape> follows <SBWD>, but if reversed
        DONE3 : If <shape> precedes <SBWD>, direct sense
        DONE4 : If <shape> precedes <SBWD>, but if reversed
        FAIL1 : If <shape> is neither an edge nor a wire
        FAIL2 : If <shape> cannot be connected to <SBWD>

        DONE5 : To the tail of <SBWD> the <shape> is closer with
        direct sense
        DONE6 : To the head of <SBWD> the <shape> is closer with
        direct sense

        Remark:   Statuses DONE1 - DONE4, FAIL1 - FAIL2 are basic and
        describe the nearest connection of the <shape> to <SBWD>.
        Statuses DONE5 and DONE6 are advanced and are to be used when
        analyzing with what sense (direct or reversed) the <shape>
        should be connected to <SBWD>:
        For tail of <SBWD> if DONE4 is True <shape> should be direct,
        otherwise reversed.
        For head of <SBWD> if DONE5 is True <shape> should be direct,
        otherwise reversed.
        """

    def CheckShapeConnect__float__float__float__float(self, shape: nanoocp.TopoDS.TopoDS_Shape, prec: float = 0.0) -> tuple[bool, float, float, float, float]:
        """
        CheckShapeConnect__float__float__float__float: the C++ overload CheckShapeConnect(double &, double &, double &, double &, const TopoDS_Shape &, const double); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        The same as previous CheckShapeConnect but is more advanced.
        It returns the distances between each end of <sbwd> and each
        end of <shape>. For example, <tailhead> stores distance
        between tail of <sbwd> and head of <shape>
        Remark:  First method CheckShapeConnect calls this one
        """

    def CheckLoop(self, aMapLoopVertices: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], aMapVertexEdges: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], aMapSmallEdges: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], aMapSeemEdges: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> bool:
        """
        Checks existence of loop on wire and return vertices which are loop vertices
        (vertices belonging to a few pairs of edges)
        """

    def CheckTail(self, theEdge1: nanoocp.TopoDS.TopoDS_Edge, theEdge2: nanoocp.TopoDS.TopoDS_Edge, theMaxSine: float, theMaxWidth: float, theMaxTolerance: float, theEdge11: nanoocp.TopoDS.TopoDS_Edge, theEdge12: nanoocp.TopoDS.TopoDS_Edge, theEdge21: nanoocp.TopoDS.TopoDS_Edge, theEdge22: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    def StatusOrder(self, Status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusConnected(self, Status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusEdgeCurves(self, Status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusDegenerated(self, Status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusClosed(self, Status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusSmall(self, Status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusSelfIntersection(self, Status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusLacking(self, Status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusGaps3d(self, Status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusGaps2d(self, Status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusCurveGaps(self, Status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def StatusLoop(self, Status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool: ...

    def LastCheckStatus(self, Status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Querying the status of the LAST performed 'Advanced' checking procedure
        """

    def MinDistance3d(self) -> float:
        """
        Returns the last lowest distance in 3D computed by
        CheckOrientation, CheckConnected, CheckContinuity3d,
        CheckVertex, CheckNewVertex
        """

    def MinDistance2d(self) -> float:
        """
        Returns the last lowest distance in 2D-UV computed by
        CheckContinuity2d
        """

    def MaxDistance3d(self) -> float:
        """
        Returns the last maximal distance in 3D computed by
        CheckOrientation, CheckConnected, CheckContinuity3d,
        CheckVertex, CheckNewVertex, CheckSameParameter
        """

    def MaxDistance2d(self) -> float:
        """
        Returns the last maximal distance in 2D-UV computed by
        CheckContinuity2d
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeAnalysis_WireOrder:
    """
    This class is intended to control and, if possible, redefine
    the order of a list of edges which define a wire
    Edges are not given directly, but as their bounds (start,end)

    This allows to use this tool, either on existing wire, or on
    data just taken from a file (coordinates are easy to get)

    It can work, either in 2D, or in 3D, or miscible mode
    The tolerance for each mode is fixed

    Two phases : firstly add the couples (start, end)
    secondly perform then get the result
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theMode3D: bool, theTolerance: float, theModeBoth: bool = False) -> None:
        """
        Creates a WireOrder.
        Flag <theMode3D> defines 3D or 2d mode.
        Flag <theModeBoth> defines miscible mode and the flag <theMode3D> is ignored.
        Warning: Parameter <theTolerance> is not used in algorithm.
        """

    @overload
    def __init__(self, theOther: ShapeAnalysis_WireOrder) -> None: ...

    def SetMode(self, theMode3D: bool, theTolerance: float, theModeBoth: bool = False) -> None:
        """
        Sets new values.
        Clears the edge list if the mode (<theMode3D> or <theModeBoth> ) changes.
        Clears the connexion list.
        Warning: Parameter <theTolerance> is not used in algorithm.
        """

    def Tolerance(self) -> float:
        """Returns the working tolerance"""

    def Clear(self) -> None:
        """Clears the list of edges, but not mode and tol"""

    @overload
    def Add(self, theStart3d: nanoocp.gp.gp_XYZ, theEnd3d: nanoocp.gp.gp_XYZ) -> None:
        """Adds a couple of points 3D (start, end)"""

    @overload
    def Add(self, theStart2d: nanoocp.gp.gp_XY, theEnd2d: nanoocp.gp.gp_XY) -> None:
        """Adds a couple of points 2D (start, end)"""

    @overload
    def Add(self, theStart3d: nanoocp.gp.gp_XYZ, theEnd3d: nanoocp.gp.gp_XYZ, theStart2d: nanoocp.gp.gp_XY, theEnd2d: nanoocp.gp.gp_XY) -> None:
        """Adds a couple of points 3D and 2D (start, end)"""

    def NbEdges(self) -> int:
        """Returns the count of added couples of points (one per edges)"""

    def KeepLoopsMode(self) -> bool:
        """
        If this mode is True method perform does not sort edges of
        different loops. The resulting order is first loop, second
        one etc...
        """

    def SetKeepLoopsMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value KeepLoopsMode() returns by reference in C++.
        """

    def Perform(self, closed: bool = True) -> None:
        """
        Computes the better order
        Optimised if the couples were already in order
        The criterium is : two couples in order if distance between
        end-prec and start-cur is less then starting tolerance <tol>
        Else, the smallest distance is reached
        Warning: Parameter <closed> not used
        """

    def IsDone(self) -> bool:
        """
        Tells if Perform has been done
        Else, the following methods returns original values
        """

    def Status(self) -> int:
        """
        Returns the status of the order (0 if not done) :
        0 : all edges are direct and in sequence
        1 : all edges are direct but some are not in sequence
        -1 : some edges are reversed, but no gap remain
        3 : edges in sequence are just shifted in forward or reverse manner
        """

    def Ordered(self, theIdx: int) -> int:
        """
        Returns the number of original edge which correspond to the
        newly ordered number <n>
        Warning : the returned value is NEGATIVE if edge should be reversed
        """

    def XYZ(self, theIdx: int, theStart3D: nanoocp.gp.gp_XYZ, theEnd3D: nanoocp.gp.gp_XYZ) -> None:
        """Returns the values of the couple <num>, as 3D values"""

    def XY(self, theIdx: int, theStart2D: nanoocp.gp.gp_XY, theEnd2D: nanoocp.gp.gp_XY) -> None:
        """Returns the values of the couple <num>, as 2D values"""

    def Gap(self, num: int = 0) -> float:
        """
        Returns the gap between a couple and its preceding
        <num> is considered ordered
        If <num> = 0 (D), returns the greatest gap found
        """

    def SetChains(self, gap: float) -> None:
        """
        Determines the chains inside which successive edges have a gap
        less than a given value. Queried by NbChains and Chain
        """

    def NbChains(self) -> int:
        """Returns the count of computed chains"""

    def Chain(self, num: int) -> tuple[int, int]:
        """
        Returns, for the chain n0 num, starting and ending numbers of
        edges. In the list of ordered edges (see Ordered for originals)
        """

    def SetCouples(self, gap: float) -> None:
        """
        Determines the couples of edges for which end and start fit
        inside a given gap. Queried by NbCouples and Couple
        Warning: function isn't implemented
        """

    def NbCouples(self) -> int:
        """Returns the count of computed couples"""

    def Couple(self, num: int) -> tuple[int, int]:
        """
        Returns, for the couple n0 num, the two implied edges
        In the list of ordered edges
        """

class ShapeAnalysis_WireVertex:
    """
    Analyzes and records status of vertices in a Wire

    The Wire has formerly been loaded in a ShapeExtend_WireData
    For each Vertex, a status and some data can be attached
    (case found, position and parameters)
    Then, these information can be used to fix problems
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: ShapeAnalysis_WireVertex) -> None: ...

    @overload
    def Init(self, wire: nanoocp.TopoDS.TopoDS_Wire, preci: float) -> None: ...

    @overload
    def Init(self, swbd: nanoocp.ShapeExtend.ShapeExtend_WireData | None, preci: float) -> None: ...

    @overload
    def Load(self, wire: nanoocp.TopoDS.TopoDS_Wire) -> None: ...

    @overload
    def Load(self, sbwd: nanoocp.ShapeExtend.ShapeExtend_WireData | None) -> None: ...

    def SetPrecision(self, preci: float) -> None:
        """
        Sets the precision for work
        Analysing: for each Vertex, comparison between the end of the
        preceding edge and the start of the following edge
        Each Vertex rank corresponds to the End Vertex of the Edge of
        same rank, in the ShapeExtend_WireData. I.E. for Vertex <num>,
        Edge <num> is the preceding one, <num+1> is the following one
        """

    def Analyze(self) -> None: ...

    def SetSameVertex(self, num: int) -> None:
        """Records status "Same Vertex" (logically) on Vertex <num>"""

    def SetSameCoords(self, num: int) -> None:
        """Records status "Same Coords" (at the Vertices Tolerances)"""

    def SetClose(self, num: int) -> None:
        """Records status "Close Coords" (at the Precision of <me>)"""

    def SetEnd(self, num: int, pos: nanoocp.gp.gp_XYZ, ufol: float) -> None:
        """
        <num> is the End of preceding Edge, and its projection on the
        following one lies on it at the Precision of <me>
        <ufol> gives the parameter on the following edge
        """

    def SetStart(self, num: int, pos: nanoocp.gp.gp_XYZ, upre: float) -> None:
        """
        <num> is the Start of following Edge, its projection on the
        preceding one lies on it at the Precision of <me>
        <upre> gives the parameter on the preceding edge
        """

    def SetInters(self, num: int, pos: nanoocp.gp.gp_XYZ, upre: float, ufol: float) -> None:
        """
        <num> is the Intersection of both Edges
        <upre> is the parameter on preceding edge, <ufol> on
        following edge
        """

    def SetDisjoined(self, num: int) -> None:
        """<num> cannot be said as same vertex"""

    def IsDone(self) -> bool:
        """Returns True if analysis was performed, else returns False"""

    def Precision(self) -> float:
        """Returns precision value used in analysis"""

    def NbEdges(self) -> int:
        """
        Returns the number of edges in analyzed wire (i.e. the
        length of all arrays)
        """

    def WireData(self) -> nanoocp.ShapeExtend.ShapeExtend_WireData:
        """Returns analyzed wire"""

    def Status(self, num: int) -> int:
        """
        Returns the recorded status for a vertex
        More detail by method Data
        """

    def Position(self, num: int) -> nanoocp.gp.gp_XYZ: ...

    def UPrevious(self, num: int) -> float: ...

    def UFollowing(self, num: int) -> float: ...

    def Data(self, num: int, pos: nanoocp.gp.gp_XYZ) -> tuple[int, float, float]:
        """
        Returns the recorded status for a vertex
        With its recorded position and parameters on both edges
        These values are relevant regarding the status:
        Status  Meaning    Position  Preceding   Following
        0       Same       no        no          no
        1       SameCoord  no        no          no
        2       Close      no        no          no
        3       End        yes       no          yes
        4       Start      yes       yes         no
        5       Inters     yes       yes         yes
        -1      Disjoined  no        no          no
        """

    def NextStatus(self, stat: int, num: int = 0) -> int:
        """
        For a given status, returns the rank of the vertex which
        follows <num> and has the same status. 0 if no more
        Acts as an iterator, starts on the first one
        """

    def NextCriter(self, crit: int, num: int = 0) -> int:
        """
        For a given criter, returns the rank of the vertex which
        follows <num> and has the same status. 0 if no more
        Acts as an iterator, starts on the first one
        Criters are:
        0: same vertex (status 0)
        1: a solution exists (status >= 0)
        2: same coords (i.e. same params) (status 0 1 2)
        3: same coods but not same vertex (status 1 2)
        4: redefined coords (status 3 4 5)
        -1: no solution (status -1)
        """

class ShapeAnalysis_CanonicalRecognition:
    """
    This class provides operators for analysis surfaces and curves of shapes
    in order to find out more simple geometry entities, which could replace
    existing complex (for example, BSpline) geometry objects with given tolerance.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """constructor with shape initialisation"""

    @overload
    def __init__(self, theOther: ShapeAnalysis_CanonicalRecognition) -> None: ...

    def SetShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Sets shape"""

    def GetShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns input shape"""

    def GetGap(self) -> float:
        """Returns deviation between input geometry entity and analytical entity"""

    def GetStatus(self) -> int:
        """
        Returns status of operation.
        Current meaning of possible values of status:
        -1 - algorithm is not initalazed by shape
        0 - no errors
        1 - error during any operation (usually - because of wrong input data)
        Any operation (calling any methods like IsPlane(...), ...) can be performed
        when current staue is equal 0.
        If after any operation status != 0, it is necessary to set it 0 by method ClearStatus()
        before calling other operation.
        """

    def ClearStatus(self) -> None:
        """Returns status to be equal 0."""

    def IsPlane(self, theTol: float, thePln: nanoocp.gp.gp_Pln) -> bool:
        """
        Returns true if the underlined surface can be represent by plane with tolerance theTol
        and sets in thePln the result plane.
        """

    def IsCylinder(self, theTol: float, theCyl: nanoocp.gp.gp_Cylinder) -> bool:
        """
        Returns true if the underlined surface can be represent by cylindrical one with tolerance
        theTol and sets in theCyl the result cylinrical surface.
        """

    def IsCone(self, theTol: float, theCone: nanoocp.gp.gp_Cone) -> bool:
        """
        Returns true if the underlined surface can be represent by conical one with tolerance theTol
        and sets in theCone the result conical surface.
        """

    def IsSphere(self, theTol: float, theSphere: nanoocp.gp.gp_Sphere) -> bool:
        """
        Returns true if the underlined surface can be represent by spherical one with tolerance theTol
        and sets in theSphere the result spherical surface.
        """

    def IsLine(self, theTol: float, theLin: nanoocp.gp.gp_Lin) -> bool:
        """
        Returns true if the underlined curve can be represent by line with tolerance theTol
        and sets in theLin the result line.
        """

    def IsCircle(self, theTol: float, theCirc: nanoocp.gp.gp_Circ) -> bool:
        """
        Returns true if the underlined curve can be represent by circle with tolerance theTol
        and sets in theCirc the result circle.
        """

    def IsEllipse(self, theTol: float, theElips: nanoocp.gp.gp_Elips) -> bool:
        """
        Returns true if the underlined curve can be represent by ellipse with tolerance theTol
        and sets in theCirc the result ellipse.
        """

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.IntRes2d
import nanoocp.ShapeAnalysis
import nanoocp.TopTools
ShapeAnalysis_DataMapOfShapeListOfReal = nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[float], nanoocp.TopTools.TopTools_ShapeMapHasher]
ShapeAnalysis_HSequenceOfFreeBounds = nanoocp.NCollection.NCollection_HSequence[nanoocp.ShapeAnalysis.ShapeAnalysis_FreeBoundData]
ShapeAnalysis_SequenceOfFreeBounds = nanoocp.NCollection.NCollection_Sequence[nanoocp.ShapeAnalysis.ShapeAnalysis_FreeBoundData]
