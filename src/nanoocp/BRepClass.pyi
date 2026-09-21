"""OCCT package BRepClass (toolkit TKTopAlgo)"""

from typing import overload

import nanoocp.Geom2dInt
import nanoocp.IntRes2d
import nanoocp.NCollection
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp
import nanoocp.TopTools


class BRepClass_Edge:
    """
    This class is used to send the description of an
    Edge to the classifier. It contains an Edge and a
    Face. So the PCurve of the Edge can be found.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def __init__(self, theOther: BRepClass_Edge) -> None: ...

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns the current Edge"""

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns the Face for the current Edge"""

    def NextEdge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns the next Edge"""

    def SetNextEdge(self, theMapVE: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """Finds and sets the next Edge for the current"""

    def MaxTolerance(self) -> float:
        """Returns the maximum tolerance"""

    def SetMaxTolerance(self, theValue: float) -> None:
        """
        Sets the maximum tolerance at
        which to start checking in the intersector
        """

    def UseBndBox(self) -> bool:
        """
        Returns true if we are using boxes
        in the intersector
        """

    def SetUseBndBox(self, theValue: bool) -> None:
        """
        Sets the status of whether we are
        using boxes or not
        """

class BRepClass_Intersector(nanoocp.Geom2dInt.Geom2dInt_IntConicCurveOfGInter):
    """
    Intersect an Edge with a segment.
    Implement the Intersector2d required by the classifier.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepClass_Intersector) -> None: ...

    def Perform(self, L: nanoocp.gp.gp_Lin2d, P: float, Tol: float, E: BRepClass_Edge) -> None:
        """Intersect the line segment and the edge."""

    def LocalGeometry(self, E: BRepClass_Edge, U: float, T: nanoocp.gp.gp_Dir2d, N: nanoocp.gp.gp_Dir2d) -> float:
        """
        Returns in <T>, <N> and <C> the tangent, normal
        and curvature of the edge <E> at parameter value
        <U>.
        """

class BRepClass_FClass2dOfFClassifier:
    @overload
    def __init__(self) -> None:
        """Creates an undefined classifier."""

    @overload
    def __init__(self, theOther: BRepClass_FClass2dOfFClassifier) -> None: ...

    def Reset(self, L: nanoocp.gp.gp_Lin2d, P: float, Tol: float) -> None:
        """
        Starts a classification process. The point to
        classify is the origin of the line <L>. <P> is
        the original length of the segment on <L> used to
        compute intersections. <Tol> is the tolerance
        attached to the line segment in intersections.
        """

    def Compare(self, E: BRepClass_Edge, Or: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Updates the classification process with the edge
        <E> from the boundary.
        """

    def Parameter(self) -> float:
        """Returns the current value of the parameter."""

    def Intersector(self) -> BRepClass_Intersector:
        """Returns the intersecting algorithm."""

    def ClosestIntersection(self) -> int:
        """
        Returns 0 if the last compared edge had no
        relevant intersection. Else returns the index of
        this intersection in the last intersection
        algorithm.
        """

    def State(self) -> nanoocp.TopAbs.TopAbs_State:
        """Returns the current state of the point."""

    def IsHeadOrEnd(self) -> bool:
        """
        Returns the true if the closest intersection point
        represents head or end of the edge. Returns false
        otherwise.
        """

class BRepClass_FClassifier:
    @overload
    def __init__(self) -> None:
        """Empty constructor, undefined algorithm."""

    @overload
    def __init__(self, F: BRepClass_FaceExplorer, P: nanoocp.gp.gp_Pnt2d, Tol: float) -> None:
        """
        Creates an algorithm to classify the Point P with
        Tolerance <T> on the face described by <F>.
        """

    @overload
    def __init__(self, theOther: BRepClass_FClassifier) -> None: ...

    def Perform(self, F: BRepClass_FaceExplorer, P: nanoocp.gp.gp_Pnt2d, Tol: float) -> None:
        """
        Classify the Point P with Tolerance <T> on the
        face described by <F>.
        """

    def State(self) -> nanoocp.TopAbs.TopAbs_State:
        """Returns the result of the classification."""

    def Rejected(self) -> bool:
        """
        Returns True when the state was computed by a
        rejection. The state is OUT.
        """

    def NoWires(self) -> bool:
        """
        Returns True if the face contains no wire. The
        state is IN.
        """

    def Edge(self) -> BRepClass_Edge:
        """
        Returns the Edge used to determine the
        classification. When the State is ON this is the
        Edge containing the point.
        """

    def EdgeParameter(self) -> float:
        """
        Returns the parameter on Edge() used to determine the
        classification.
        """

    def Position(self) -> nanoocp.IntRes2d.IntRes2d_Position:
        """
        Returns the position of the point on the edge
        returned by Edge.
        """

class BRepClass_FaceClassifier(BRepClass_FClassifier):
    """Provides Constructors with a Face."""

    @overload
    def __init__(self) -> None:
        """Empty constructor, undefined algorithm."""

    @overload
    def __init__(self, F: BRepClass_FaceExplorer, P: nanoocp.gp.gp_Pnt2d, Tol: float) -> None:
        """
        Creates an algorithm to classify the Point P with
        Tolerance <T> on the face described by <F>.
        """

    @overload
    def __init__(self, theF: nanoocp.TopoDS.TopoDS_Face, theP: nanoocp.gp.gp_Pnt2d, theTol: float, theUseBndBox: bool = False, theGapCheckTol: float = 0.1) -> None: ...

    @overload
    def __init__(self, theF: nanoocp.TopoDS.TopoDS_Face, theP: nanoocp.gp.gp_Pnt, theTol: float, theUseBndBox: bool = False, theGapCheckTol: float = 0.1) -> None:
        """
        Creates an algorithm to classify the Point P with
        Tolerance <T> on the face <F>.
        Recommended to use Bnd_Box if the number of edges > 10
        and the geometry is mostly spline
        """

    @overload
    def __init__(self, theOther: BRepClass_FaceClassifier) -> None: ...

    @overload
    def Perform(self, theF: nanoocp.TopoDS.TopoDS_Face, theP: nanoocp.gp.gp_Pnt2d, theTol: float, theUseBndBox: bool = False, theGapCheckTol: float = 0.1) -> None: ...

    @overload
    def Perform(self, theF: nanoocp.TopoDS.TopoDS_Face, theP: nanoocp.gp.gp_Pnt, theTol: float, theUseBndBox: bool = False, theGapCheckTol: float = 0.1) -> None:
        """
        Classify the Point P with Tolerance <T> on the
        face described by <F>.
        Recommended to use Bnd_Box if the number of edges > 10
        and the geometry is mostly spline
        """

class BRepClass_FaceExplorer:
    """
    Provide an exploration of a BRep Face for the
    classification. Return UV edges.
    """

    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def CheckPoint(self, thePoint: nanoocp.gp.gp_Pnt2d) -> bool:
        """
        Checks the point and change its coords if it is located too far
        from the bounding box of the face. New Coordinates of the point
        will be on the line between the point and the center of the
        bounding box. Returns True if point was not changed.
        """

    def Reject(self, P: nanoocp.gp.gp_Pnt2d) -> bool:
        """
        Should return True if the point is outside a
        bounding volume of the face.
        """

    def Segment(self, P: nanoocp.gp.gp_Pnt2d, L: nanoocp.gp.gp_Lin2d) -> tuple[bool, float]:
        """
        Returns in <L>, <Par> a segment having at least
        one intersection with the face boundary to
        compute intersections.
        """

    def OtherSegment(self, P: nanoocp.gp.gp_Pnt2d, L: nanoocp.gp.gp_Lin2d) -> tuple[bool, float]:
        """
        Returns in <L>, <Par> a segment having at least
        one intersection with the face boundary to
        compute intersections. Each call gives another segment.
        """

    def InitWires(self) -> None:
        """Starts an exploration of the wires."""

    def MoreWires(self) -> bool:
        """Returns True if there is a current wire."""

    def NextWire(self) -> None:
        """Sets the explorer to the next wire."""

    def RejectWire(self, L: nanoocp.gp.gp_Lin2d, Par: float) -> bool:
        """
        Returns True if the wire bounding volume does not
        intersect the segment.
        """

    def InitEdges(self) -> None:
        """
        Starts an exploration of the edges of the current
        wire.
        """

    def MoreEdges(self) -> bool:
        """Returns True if there is a current edge."""

    def NextEdge(self) -> None:
        """Sets the explorer to the next edge."""

    def RejectEdge(self, L: nanoocp.gp.gp_Lin2d, Par: float) -> bool:
        """
        Returns True if the edge bounding volume does not
        intersect the segment.
        """

    def CurrentEdge(self, E: BRepClass_Edge) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Current edge in current wire and its orientation."""

    def MaxTolerance(self) -> float:
        """Returns the maximum tolerance"""

    def SetMaxTolerance(self, theValue: float) -> None:
        """
        Sets the maximum tolerance at
        which to start checking in the intersector
        """

    def UseBndBox(self) -> bool:
        """
        Returns true if we are using boxes
        in the intersector
        """

    def SetUseBndBox(self, theValue: bool) -> None:
        """
        Sets the status of whether we are
        using boxes or not
        """

class BRepClass_FacePassiveClassifier:
    @overload
    def __init__(self) -> None:
        """Creates an undefined classifier."""

    @overload
    def __init__(self, theOther: BRepClass_FacePassiveClassifier) -> None: ...

    def Reset(self, L: nanoocp.gp.gp_Lin2d, P: float, Tol: float) -> None:
        """
        Starts a classification process. The point to
        classify is the origin of the line <L>. <P> is
        the original length of the segment on <L> used to
        compute intersections. <Tol> is the tolerance
        attached to the line segment in intersections.
        """

    def Compare(self, E: BRepClass_Edge, Or: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Updates the classification process with the edge
        <E> from the boundary.
        """

    def Parameter(self) -> float:
        """Returns the current value of the parameter."""

    def Intersector(self) -> BRepClass_Intersector:
        """Returns the intersecting algorithm."""

    def ClosestIntersection(self) -> int:
        """
        Returns 0 if the last compared edge had no
        relevant intersection. Else returns the index of
        this intersection in the last intersection
        algorithm.
        """

    def State(self) -> nanoocp.TopAbs.TopAbs_State:
        """Returns the current state of the point."""

    def IsHeadOrEnd(self) -> bool:
        """
        Returns the true if the closest intersection point
        represents head or end of the edge. Returns false
        otherwise.
        """
