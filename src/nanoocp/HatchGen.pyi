"""OCCT package HatchGen (toolkit TKGeomAlgo)"""

import enum
from typing import overload

import nanoocp.IntRes2d
import nanoocp.TopAbs


class HatchGen_IntersectionType(enum.IntEnum):
    """
    Intersection type between the hatching and the
    element.
    """

    HatchGen_TRUE = 0

    HatchGen_TOUCH = 1

    HatchGen_TANGENT = 2

    HatchGen_UNDETERMINED = 3

HatchGen_TRUE: HatchGen_IntersectionType = HatchGen_IntersectionType.HatchGen_TRUE

HatchGen_TOUCH: HatchGen_IntersectionType = HatchGen_IntersectionType.HatchGen_TOUCH

HatchGen_TANGENT: HatchGen_IntersectionType = HatchGen_IntersectionType.HatchGen_TANGENT

HatchGen_UNDETERMINED: HatchGen_IntersectionType = HatchGen_IntersectionType.HatchGen_UNDETERMINED

class HatchGen_ErrorStatus(enum.IntEnum):
    """Error status."""

    HatchGen_NoProblem = 0

    HatchGen_TrimFailure = 1

    HatchGen_TransitionFailure = 2

    HatchGen_IncoherentParity = 3

    HatchGen_IncompatibleStates = 4

HatchGen_NoProblem: HatchGen_ErrorStatus = HatchGen_ErrorStatus.HatchGen_NoProblem

HatchGen_TrimFailure: HatchGen_ErrorStatus = HatchGen_ErrorStatus.HatchGen_TrimFailure

HatchGen_TransitionFailure: HatchGen_ErrorStatus = HatchGen_ErrorStatus.HatchGen_TransitionFailure

HatchGen_IncoherentParity: HatchGen_ErrorStatus = HatchGen_ErrorStatus.HatchGen_IncoherentParity

HatchGen_IncompatibleStates: HatchGen_ErrorStatus = HatchGen_ErrorStatus.HatchGen_IncompatibleStates

class HatchGen_IntersectionPoint:
    def SetIndex(self, Index: int) -> None:
        """Sets the index of the supporting curve."""

    def Index(self) -> int:
        """Returns the index of the supporting curve."""

    def SetParameter(self, Parameter: float) -> None:
        """Sets the parameter on the curve."""

    def Parameter(self) -> float:
        """Returns the parameter on the curve."""

    def SetPosition(self, Position: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """Sets the position of the point on the curve."""

    def Position(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Returns the position of the point on the curve."""

    def SetStateBefore(self, State: nanoocp.TopAbs.TopAbs_State) -> None:
        """Sets the transition state before the intersection."""

    def StateBefore(self) -> nanoocp.TopAbs.TopAbs_State:
        """Returns the transition state before the intersection."""

    def SetStateAfter(self, State: nanoocp.TopAbs.TopAbs_State) -> None:
        """Sets the transition state after the intersection."""

    def StateAfter(self) -> nanoocp.TopAbs.TopAbs_State:
        """Returns the transition state after of the intersection."""

    def SetSegmentBeginning(self, State: bool = True) -> None:
        """Sets the flag that the point is the beginning of a segment."""

    def SegmentBeginning(self) -> bool:
        """Returns the flag that the point is the beginning of a segment."""

    def SetSegmentEnd(self, State: bool = True) -> None:
        """Sets the flag that the point is the end of a segment."""

    def SegmentEnd(self) -> bool:
        """Returns the flag that the point is the end of a segment."""

    def Dump(self, Index: int = 0) -> None:
        """Dump of the point on element."""

class HatchGen_PointOnElement(HatchGen_IntersectionPoint):
    @overload
    def __init__(self) -> None:
        """---Purpose; Creates an empty point on element"""

    @overload
    def __init__(self, Point: nanoocp.IntRes2d.IntRes2d_IntersectionPoint) -> None:
        """Creates a point from an intersection point."""

    @overload
    def __init__(self, theOther: HatchGen_PointOnElement) -> None: ...

    def SetIntersectionType(self, Type: HatchGen_IntersectionType) -> None:
        """Sets the intersection type at this point."""

    def IntersectionType(self) -> HatchGen_IntersectionType:
        """Returns the intersection type at this point."""

    def IsIdentical(self, Point: HatchGen_PointOnElement, Confusion: float) -> bool:
        """
        Tests if the point is identical to an other.
        That is to say :
        P1.myIndex  = P2.myIndex
        Abs (P1.myParam - P2.myParam) <= Confusion
        P1.myPosit  = P2.myPosit
        P1.myBefore = P2.myBefore
        P1.myAfter  = P2.myAfter
        P1.mySegBeg = P2.mySegBeg
        P1.mySegEnd = P2.mySegEnd
        P1.myType   = P2.myType
        """

    def IsDifferent(self, Point: HatchGen_PointOnElement, Confusion: float) -> bool:
        """Tests if the point is different from an other."""

    def Dump(self, Index: int = 0) -> None:
        """Dump of the point on element."""

class HatchGen_PointOnHatching(HatchGen_IntersectionPoint):
    @overload
    def __init__(self) -> None:
        """Creates an empty point."""

    @overload
    def __init__(self, Point: nanoocp.IntRes2d.IntRes2d_IntersectionPoint) -> None:
        """Creates a point from an intersection point."""

    @overload
    def __init__(self, theOther: HatchGen_PointOnHatching) -> None: ...

    def AddPoint(self, Point: HatchGen_PointOnElement, Confusion: float) -> None:
        """Adds a point on element to the point."""

    def NbPoints(self) -> int:
        """
        Returns the number of elements intersecting the
        hatching at this point.
        """

    def Point(self, Index: int) -> HatchGen_PointOnElement:
        """
        Returns the Index-th point on element of the point.
        The exception OutOfRange is raised if
        Index > NbPoints.
        """

    def RemPoint(self, Index: int) -> None:
        """
        Removes the Index-th point on element of the point.
        The exception OutOfRange is raised if
        Index > NbPoints.
        """

    def ClrPoints(self) -> None:
        """Removes all the points on element of the point."""

    def IsLower(self, Point: HatchGen_PointOnHatching, Confusion: float) -> bool:
        """
        Tests if the point is lower than an other.
        A point on hatching P1 is said to be lower than an
        other P2 if :
        P2.myParam - P1.myParam > Confusion
        """

    def IsEqual(self, Point: HatchGen_PointOnHatching, Confusion: float) -> bool:
        """
        Tests if the point is equal to an other.
        A point on hatching P1 is said to be equal to an
        other P2 if :
        | P2.myParam - P1.myParam | <= Confusion
        """

    def IsGreater(self, Point: HatchGen_PointOnHatching, Confusion: float) -> bool:
        """
        Tests if the point is greater than an other.
        A point on hatching P1 is said to be greater than an
        other P2 if :
        P1.myParam - P2.myParam > Confusion
        """

    def Dump(self, Index: int = 0) -> None:
        """Dump of the point."""

class HatchGen_Domain:
    @overload
    def __init__(self) -> None:
        """Creates an infinite domain."""

    @overload
    def __init__(self, P1: HatchGen_PointOnHatching, P2: HatchGen_PointOnHatching) -> None:
        """Creates a domain for the curve associated to a hatching."""

    @overload
    def __init__(self, P: HatchGen_PointOnHatching, First: bool) -> None:
        """
        Creates a semi-infinite domain for the curve associated
        to a hatching. The `First' flag means that the given
        point is the first one.
        """

    @overload
    def __init__(self, theOther: HatchGen_Domain) -> None: ...

    @overload
    def SetPoints(self, P1: HatchGen_PointOnHatching, P2: HatchGen_PointOnHatching) -> None:
        """Sets the first and the second points of the domain."""

    @overload
    def SetPoints(self) -> None:
        """
        Sets the first and the second points of the domain
        as the infinite.
        """

    @overload
    def SetFirstPoint(self, P: HatchGen_PointOnHatching) -> None:
        """Sets the first point of the domain."""

    @overload
    def SetFirstPoint(self) -> None:
        """
        Sets the first point of the domain at the
        infinite.
        """

    @overload
    def SetSecondPoint(self, P: HatchGen_PointOnHatching) -> None:
        """Sets the second point of the domain."""

    @overload
    def SetSecondPoint(self) -> None:
        """
        Sets the second point of the domain at the
        infinite.
        """

    def HasFirstPoint(self) -> bool:
        """Returns True if the domain has a first point."""

    def FirstPoint(self) -> HatchGen_PointOnHatching:
        """
        Returns the first point of the domain.
        The exception DomainError is raised if
        HasFirstPoint returns False.
        """

    def HasSecondPoint(self) -> bool:
        """Returns True if the domain has a second point."""

    def SecondPoint(self) -> HatchGen_PointOnHatching:
        """
        Returns the second point of the domain.
        The exception DomainError is raised if
        HasSecondPoint returns False.
        """

    def Dump(self, Index: int = 0) -> None:
        """Dump of the domain."""
