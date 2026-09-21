"""OCCT package Geom2dHatch (toolkit TKGeomAlgo)"""

from typing import overload

import nanoocp.Geom2d
import nanoocp.Geom2dAdaptor
import nanoocp.Geom2dInt
import nanoocp.HatchGen
import nanoocp.IntRes2d
import nanoocp.TopAbs
import nanoocp.gp


class Geom2dHatch_Intersector(nanoocp.Geom2dInt.Geom2dInt_GInter):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Confusion: float, Tangency: float) -> None:
        """Creates an intersector."""

    @overload
    def __init__(self, theOther: Geom2dHatch_Intersector) -> None: ...

    def ConfusionTolerance(self) -> float:
        """
        Returns the confusion tolerance of the
        intersector.
        """

    def SetConfusionTolerance(self, Confusion: float) -> None:
        """Sets the confusion tolerance of the intersector."""

    def TangencyTolerance(self) -> float:
        """
        Returns the tangency tolerance of the
        intersector.
        """

    def SetTangencyTolerance(self, Tangency: float) -> None:
        """Sets the tangency tolerance of the intersector."""

    def Intersect(self, C1: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, C2: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None:
        """
        Intersects the curves C1 and C2.
        The results are retrieved by the usual methods
        described in IntRes2d_Intersection.
        Creates an intersector.
        """

    def Perform(self, L: nanoocp.gp.gp_Lin2d, P: float, Tol: float, E: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None:
        """
        Performs the intersection between the 2d line
        segment (<L>, <P>) and the Curve <E>. The line
        segment is the part of the 2d line <L> of
        parameter range [0, <P>] (P is positive and can be
        RealLast()). Tol is the Tolerance on the segment.
        The order is relevant, the first argument is the
        segment, the second the Edge.
        """

    def LocalGeometry(self, E: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, U: float, T: nanoocp.gp.gp_Dir2d, N: nanoocp.gp.gp_Dir2d) -> float:
        """
        Returns in <T>, <N> and <C> the tangent, normal
        and curvature of the edge <E> at parameter value
        <U>.
        """

class Geom2dHatch_FClass2dOfClassifier:
    @overload
    def __init__(self) -> None:
        """Creates an undefined classifier."""

    @overload
    def __init__(self, theOther: Geom2dHatch_FClass2dOfClassifier) -> None: ...

    def Reset(self, L: nanoocp.gp.gp_Lin2d, P: float, Tol: float) -> None:
        """
        Starts a classification process. The point to
        classify is the origin of the line <L>. <P> is
        the original length of the segment on <L> used to
        compute intersections. <Tol> is the tolerance
        attached to the line segment in intersections.
        """

    def Compare(self, E: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Or: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Updates the classification process with the edge
        <E> from the boundary.
        """

    def Parameter(self) -> float:
        """Returns the current value of the parameter."""

    def Intersector(self) -> Geom2dHatch_Intersector:
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

class Geom2dHatch_Classifier:
    @overload
    def __init__(self) -> None:
        """Empty constructor, undefined algorithm."""

    @overload
    def __init__(self, F: Geom2dHatch_Elements, P: nanoocp.gp.gp_Pnt2d, Tol: float) -> None:
        """
        Creates an algorithm to classify the Point P with
        Tolerance <T> on the face described by <F>.
        """

    @overload
    def __init__(self, theOther: Geom2dHatch_Classifier) -> None: ...

    def Perform(self, F: Geom2dHatch_Elements, P: nanoocp.gp.gp_Pnt2d, Tol: float) -> None:
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
        Returns True if the face contains no wire.
        The state is IN.
        """

    def Edge(self) -> nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve:
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

class Geom2dHatch_Element:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Curve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Orientation: nanoocp.TopAbs.TopAbs_Orientation = TopAbs_Orientation.TopAbs_FORWARD) -> None:
        """Creates an element."""

    @overload
    def __init__(self, theOther: Geom2dHatch_Element) -> None: ...

    def Curve(self) -> nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve:
        """Returns the curve associated to the element."""

    def ChangeCurve(self) -> nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve:
        """Returns the curve associated to the element."""

    @overload
    def Orientation(self, Orientation: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """Sets the orientation of the element."""

    @overload
    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Returns the orientation of the element."""

class Geom2dHatch_Elements:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Other: Geom2dHatch_Elements) -> None: ...

    def Clear(self) -> None: ...

    def Bind(self, K: int, I: Geom2dHatch_Element) -> bool: ...

    def IsBound(self, K: int) -> bool: ...

    def UnBind(self, K: int) -> bool: ...

    def Find(self, K: int) -> Geom2dHatch_Element: ...

    @overload
    def __call__(self, K: int) -> Geom2dHatch_Element: ...

    @overload
    def __call__(self, K: int) -> Geom2dHatch_Element: ...

    def ChangeFind(self, K: int) -> Geom2dHatch_Element: ...

    def CheckPoint(self, P: nanoocp.gp.gp_Pnt2d) -> bool: ...

    def Reject(self, P: nanoocp.gp.gp_Pnt2d) -> bool: ...

    def Segment(self, P: nanoocp.gp.gp_Pnt2d, L: nanoocp.gp.gp_Lin2d) -> tuple[bool, float]: ...

    def OtherSegment(self, P: nanoocp.gp.gp_Pnt2d, L: nanoocp.gp.gp_Lin2d) -> tuple[bool, float]: ...

    def InitWires(self) -> None: ...

    def MoreWires(self) -> bool: ...

    def NextWire(self) -> None: ...

    def RejectWire(self, L: nanoocp.gp.gp_Lin2d, Par: float) -> bool: ...

    def InitEdges(self) -> None: ...

    def MoreEdges(self) -> bool: ...

    def NextEdge(self) -> None: ...

    def RejectEdge(self, L: nanoocp.gp.gp_Lin2d, Par: float) -> bool: ...

    def CurrentEdge(self, E: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> nanoocp.TopAbs.TopAbs_Orientation: ...

class Geom2dHatch_Hatching:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Curve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None:
        """Creates a hatching."""

    @overload
    def __init__(self, theOther: Geom2dHatch_Hatching) -> None: ...

    def Curve(self) -> nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve:
        """Returns the curve associated to the hatching."""

    def ChangeCurve(self) -> nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve:
        """Returns the curve associated to the hatching."""

    @overload
    def TrimDone(self, Flag: bool) -> None:
        """
        Sets the flag about the trimming computations to the
        given value.
        """

    @overload
    def TrimDone(self) -> bool:
        """Returns the flag about the trimming computations."""

    @overload
    def TrimFailed(self, Flag: bool) -> None:
        """
        Sets the flag about the trimming failure to the
        given value.
        """

    @overload
    def TrimFailed(self) -> bool:
        """Returns the flag about the trimming failure."""

    @overload
    def IsDone(self, Flag: bool) -> None:
        """
        Sets the flag about the domains computation to the
        given value.
        """

    @overload
    def IsDone(self) -> bool:
        """Returns the flag about the domains computation."""

    @overload
    def Status(self, theStatus: nanoocp.HatchGen.HatchGen_ErrorStatus) -> None:
        """Sets the error status."""

    @overload
    def Status(self) -> nanoocp.HatchGen.HatchGen_ErrorStatus:
        """Returns the error status."""

    def AddPoint(self, Point: nanoocp.HatchGen.HatchGen_PointOnHatching, Confusion: float) -> None:
        """Adds an intersection point to the hatching."""

    def NbPoints(self) -> int:
        """
        Returns the number of intersection points
        of the hatching.
        """

    def Point(self, Index: int) -> nanoocp.HatchGen.HatchGen_PointOnHatching:
        """
        Returns the Index-th intersection point of the
        hatching.
        The exception OutOfRange is raised if
        Index < 1 or Index > NbPoints.
        """

    def ChangePoint(self, Index: int) -> nanoocp.HatchGen.HatchGen_PointOnHatching:
        """
        Returns the Index-th intersection point of the
        hatching.
        The exception OutOfRange is raised if
        Index < 1 or Index > NbPoints.
        """

    def RemPoint(self, Index: int) -> None:
        """
        Removes the Index-th intersection point of the
        hatching.
        The exception OutOfRange is raised if
        Index < 1 or Index > NbPoints.
        """

    def ClrPoints(self) -> None:
        """Removes all the intersection points of the hatching."""

    def AddDomain(self, Domain: nanoocp.HatchGen.HatchGen_Domain) -> None:
        """Adds a domain to the hatching."""

    def NbDomains(self) -> int:
        """Returns the number of domains of the hatching."""

    def Domain(self, Index: int) -> nanoocp.HatchGen.HatchGen_Domain:
        """
        Returns the Index-th domain of the hatching.
        The exception OutOfRange is raised if
        Index < 1 or Index > NbDomains.
        """

    def RemDomain(self, Index: int) -> None:
        """
        Removes the Index-th domain of the hatching.
        The exception OutOfRange is raised if
        Index < 1 or Index > NbDomains.
        """

    def ClrDomains(self) -> None:
        """Removes all the domains of the hatching."""

    def ClassificationPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns a point on the curve.
        This point will be used for the classification.
        """

class Geom2dHatch_Hatcher:
    @overload
    def __init__(self, Intersector: Geom2dHatch_Intersector, Confusion2d: float, Confusion3d: float, KeepPnt: bool = False, KeepSeg: bool = False) -> None:
        """Returns an empty hatcher."""

    @overload
    def __init__(self, theOther: Geom2dHatch_Hatcher) -> None: ...

    @overload
    def Intersector(self, Intersector: Geom2dHatch_Intersector) -> None:
        """Sets the associated intersector."""

    @overload
    def Intersector(self) -> Geom2dHatch_Intersector:
        """Returns the associated intersector."""

    def ChangeIntersector(self) -> Geom2dHatch_Intersector:
        """Returns the associated intersector."""

    @overload
    def Confusion2d(self, Confusion: float) -> None:
        """Sets the confusion tolerance."""

    @overload
    def Confusion2d(self) -> float:
        """
        Returns the 2d confusion tolerance, i.e. the value under
        which two points are considered identical in the
        parametric space of the hatching.
        """

    @overload
    def Confusion3d(self, Confusion: float) -> None:
        """Sets the confusion tolerance."""

    @overload
    def Confusion3d(self) -> float:
        """
        Returns the 3d confusion tolerance, i.e. the value under
        which two points are considered identical in the
        3d space of the hatching.
        """

    @overload
    def KeepPoints(self, Keep: bool) -> None:
        """Sets the above flag."""

    @overload
    def KeepPoints(self) -> bool:
        """Returns the flag about the points consideration."""

    @overload
    def KeepSegments(self, Keep: bool) -> None:
        """Sets the above flag."""

    @overload
    def KeepSegments(self) -> bool:
        """Returns the flag about the segments consideration."""

    def Clear(self) -> None:
        """Removes all the hatchings and all the elements."""

    def ElementCurve(self, IndE: int) -> nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve:
        """Returns the curve associated to the IndE-th element."""

    @overload
    def AddElement(self, Curve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve, Orientation: nanoocp.TopAbs.TopAbs_Orientation = TopAbs_Orientation.TopAbs_FORWARD) -> int: ...

    @overload
    def AddElement(self, Curve: nanoocp.Geom2d.Geom2d_Curve | None, Orientation: nanoocp.TopAbs.TopAbs_Orientation = TopAbs_Orientation.TopAbs_FORWARD) -> int:
        """Adds an element to the hatcher and returns its index."""

    def RemElement(self, IndE: int) -> None:
        """Removes the IndE-th element from the hatcher."""

    def ClrElements(self) -> None:
        """Removes all the elements from the hatcher."""

    def HatchingCurve(self, IndH: int) -> nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve:
        """Returns the curve associated to the IndH-th hatching."""

    def AddHatching(self, Curve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> int:
        """Adds a hatching to the hatcher and returns its index."""

    def RemHatching(self, IndH: int) -> None:
        """Removes the IndH-th hatching from the hatcher."""

    def ClrHatchings(self) -> None:
        """Removes all the hatchings from the hatcher."""

    def NbPoints(self, IndH: int) -> int:
        """
        Returns the number of intersection points of
        the IndH-th hatching.
        """

    def Point(self, IndH: int, IndP: int) -> nanoocp.HatchGen.HatchGen_PointOnHatching:
        """
        Returns the IndP-th intersection point of the
        IndH-th hatching.
        """

    @overload
    def Trim(self) -> None:
        """
        Trims all the hatchings of the hatcher by all the
        elements of the hatcher.
        """

    @overload
    def Trim(self, Curve: nanoocp.Geom2dAdaptor.Geom2dAdaptor_Curve) -> int:
        """
        Adds a hatching to the hatcher and trims it by
        the elements already given and returns its index.
        """

    @overload
    def Trim(self, IndH: int) -> None:
        """
        Trims the IndH-th hatching by the elements
        already given.
        """

    @overload
    def ComputeDomains(self) -> None:
        """Computes the domains of all the hatchings."""

    @overload
    def ComputeDomains(self, IndH: int) -> None:
        """Computes the domains of the IndH-th hatching."""

    def TrimDone(self, IndH: int) -> bool:
        """
        Returns the fact that the intersections were computed
        for the IndH-th hatching.
        """

    def TrimFailed(self, IndH: int) -> bool:
        """
        Returns the fact that the intersections failed
        for the IndH-th hatching.
        """

    def IsDone(self, IndH: int) -> bool:
        """
        Returns the fact that the domains were computed
        for the IndH-th hatching.
        """

    def Status(self, IndH: int) -> nanoocp.HatchGen.HatchGen_ErrorStatus:
        """Returns the status about the IndH-th hatching."""

    def NbDomains(self, IndH: int) -> int:
        """
        Returns the number of domains of the IndH-th hatching.
        Only ONE "INFINITE" domain means that the hatching is
        fully included in the contour defined by the elements.
        """

    def Domain(self, IndH: int, IDom: int) -> nanoocp.HatchGen.HatchGen_Domain:
        """Returns the IDom-th domain of the IndH-th hatching."""

    def Dump(self) -> None:
        """Dump the hatcher."""
