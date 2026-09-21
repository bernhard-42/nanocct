"""OCCT package IntRes2d (toolkit TKGeomAlgo)"""

import enum
from typing import overload

import nanoocp.gp


class IntRes2d_Position(enum.IntEnum):
    IntRes2d_Head = 0

    IntRes2d_Middle = 1

    IntRes2d_End = 2

IntRes2d_Head: IntRes2d_Position = IntRes2d_Position.IntRes2d_Head

IntRes2d_Middle: IntRes2d_Position = IntRes2d_Position.IntRes2d_Middle

IntRes2d_End: IntRes2d_Position = IntRes2d_Position.IntRes2d_End

class IntRes2d_TypeTrans(enum.IntEnum):
    IntRes2d_In = 0

    IntRes2d_Out = 1

    IntRes2d_Touch = 2

    IntRes2d_Undecided = 3

IntRes2d_In: IntRes2d_TypeTrans = IntRes2d_TypeTrans.IntRes2d_In

IntRes2d_Out: IntRes2d_TypeTrans = IntRes2d_TypeTrans.IntRes2d_Out

IntRes2d_Touch: IntRes2d_TypeTrans = IntRes2d_TypeTrans.IntRes2d_Touch

IntRes2d_Undecided: IntRes2d_TypeTrans = IntRes2d_TypeTrans.IntRes2d_Undecided

class IntRes2d_Situation(enum.IntEnum):
    IntRes2d_Inside = 0

    IntRes2d_Outside = 1

    IntRes2d_Unknown = 2

IntRes2d_Inside: IntRes2d_Situation = IntRes2d_Situation.IntRes2d_Inside

IntRes2d_Outside: IntRes2d_Situation = IntRes2d_Situation.IntRes2d_Outside

IntRes2d_Unknown: IntRes2d_Situation = IntRes2d_Situation.IntRes2d_Unknown

class IntRes2d_Domain:
    """
    Definition of the domain of parameter on a 2d-curve.
    Most of the time, a domain is defined by two extremities.
    An extremity is made of :
    - a point in 2d-space (Pnt2d from gp),
    - a parameter on the curve,
    - a tolerance in the 2d-space.
    Sometimes, it can be made of 0 or 1 point ( for an infinite
    or semi-infinite line for example).

    For Intersection algorithms, Ellipses and Circles
    Domains must be closed.
    So, SetEquivalentParameters(.,.) method must be called
    after initializing the first and the last bounds.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an infinite Domain (HasFirstPoint = False
        and HasLastPoint = False).
        """

    @overload
    def __init__(self, Pnt: nanoocp.gp.gp_Pnt2d, Par: float, Tol: float, First: bool) -> None:
        """
        Creates a semi-infinite Domain. If First is set to
        True, the given point is the first point of the domain,
        otherwise it is the last point.
        """

    @overload
    def __init__(self, Pnt1: nanoocp.gp.gp_Pnt2d, Par1: float, Tol1: float, Pnt2: nanoocp.gp.gp_Pnt2d, Par2: float, Tol2: float) -> None:
        """Creates a bounded Domain."""

    @overload
    def __init__(self, theOther: IntRes2d_Domain) -> None: ...

    @overload
    def SetValues(self, Pnt1: nanoocp.gp.gp_Pnt2d, Par1: float, Tol1: float, Pnt2: nanoocp.gp.gp_Pnt2d, Par2: float, Tol2: float) -> None:
        """Sets the values for a bounded domain."""

    @overload
    def SetValues(self) -> None:
        """Sets the values for an infinite domain."""

    @overload
    def SetValues(self, Pnt: nanoocp.gp.gp_Pnt2d, Par: float, Tol: float, First: bool) -> None:
        """Sets the values for a semi-infinite domain."""

    def SetEquivalentParameters(self, zero: float, period: float) -> None:
        """Defines a closed domain."""

    def HasFirstPoint(self) -> bool:
        """
        Returns True if the domain has a first point, i-e
        a point defining the lowest admitted parameter on the
        curve.
        """

    def FirstParameter(self) -> float:
        """
        Returns the parameter of the first point of the domain
        The exception DomainError is raised if HasFirstPoint
        returns False.
        """

    def FirstPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the first point of the domain.
        The exception DomainError is raised if HasFirstPoint
        returns False.
        """

    def FirstTolerance(self) -> float:
        """
        Returns the tolerance of the first (left) bound.
        The exception DomainError is raised if HasFirstPoint
        returns False.
        """

    def HasLastPoint(self) -> bool:
        """
        Returns True if the domain has a last point, i-e
        a point defining the highest admitted parameter on the
        curve.
        """

    def LastParameter(self) -> float:
        """
        Returns the parameter of the last point of the domain.
        The exception DomainError is raised if HasLastPoint
        returns False.
        """

    def LastPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the last point of the domain.
        The exception DomainError is raised if HasLastPoint
        returns False.
        """

    def LastTolerance(self) -> float:
        """
        Returns the tolerance of the last (right) bound.
        The exception DomainError is raised if HasLastPoint
        returns False.
        """

    def IsClosed(self) -> bool:
        """Returns True if the domain is closed."""

    def EquivalentParameters(self) -> tuple[float, float]:
        """
        Returns Equivalent parameters if the domain is closed.
        Otherwise, the exception DomainError is raised.
        """

class IntRes2d_Transition:
    """
    Definition of the type of transition near an
    intersection point between two curves. The transition
    is either a "true transition", which means that one of
    the curves goes inside or outside the area defined by
    the other curve near the intersection, or a "touch
    transition" which means that the first curve does not
    cross the other one, or an "undecided" transition,
    which means that the curves are superposed.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, Pos: IntRes2d_Position) -> None:
        """Creates an UNDECIDED transition."""

    @overload
    def __init__(self, Tangent: bool, Pos: IntRes2d_Position, Type: IntRes2d_TypeTrans) -> None:
        """Creates an IN or OUT transition."""

    @overload
    def __init__(self, Tangent: bool, Pos: IntRes2d_Position, Situ: IntRes2d_Situation, Oppos: bool) -> None:
        """Creates a TOUCH transition."""

    @overload
    def __init__(self, theOther: IntRes2d_Transition) -> None: ...

    @overload
    def SetValue(self, Tangent: bool, Pos: IntRes2d_Position, Type: IntRes2d_TypeTrans) -> None:
        """Sets the values of an IN or OUT transition."""

    @overload
    def SetValue(self, Tangent: bool, Pos: IntRes2d_Position, Situ: IntRes2d_Situation, Oppos: bool) -> None:
        """Sets the values of a TOUCH transition."""

    @overload
    def SetValue(self, Pos: IntRes2d_Position) -> None:
        """Sets the values of an UNDECIDED transition."""

    def SetPosition(self, Pos: IntRes2d_Position) -> None:
        """Sets the value of the position."""

    def PositionOnCurve(self) -> IntRes2d_Position:
        """
        Indicates if the intersection is at the beginning
        (IntRes2d_Head), at the end (IntRes2d_End), or in
        the middle (IntRes2d_Middle) of the curve.
        """

    def TransitionType(self) -> IntRes2d_TypeTrans:
        """
        Returns the type of transition at the intersection.
        It may be IN or OUT or TOUCH, or UNDECIDED if the
        two first derivatives are not enough to give
        the tangent to one of the two curves.
        """

    def IsTangent(self) -> bool:
        """
        Returns TRUE when the 2 curves are tangent at the
        intersection point.
        Theexception DomainError is raised if the type of
        transition is UNDECIDED.
        """

    def Situation(self) -> IntRes2d_Situation:
        """
        returns a significant value if TransitionType returns
        TOUCH. In this case, the function returns :
        INSIDE when the curve remains inside the other one,
        OUTSIDE when it remains outside the other one,
        UNKNOWN when the calculus, based on the second derivatives
        cannot give the result.
        If TransitionType returns IN or OUT or UNDECIDED, the
        exception DomainError is raised.
        """

    def IsOpposite(self) -> bool:
        """
        returns a significant value if TransitionType
        returns TOUCH. In this case, the function returns
        true when the 2 curves locally define two
        different parts of the space. If TransitionType
        returns IN or OUT or UNDECIDED, the exception
        DomainError is raised.
        """

class IntRes2d_IntersectionPoint:
    """
    Definition of an intersection point between two
    2D curves.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt2d, Uc1: float, Uc2: float, Trans1: IntRes2d_Transition, Trans2: IntRes2d_Transition, ReversedFlag: bool) -> None:
        """
        Creates an IntersectionPoint.
        if ReversedFlag is False, the parameter Uc1(resp. Uc2)
        and the Transition Trans1 (resp. Trans2) refer to
        the first curve (resp. second curve) otherwise Uc1
        and Trans1 (resp. Uc2 and Trans2) refer to the
        second curve (resp. the first curve).
        """

    @overload
    def __init__(self, theOther: IntRes2d_IntersectionPoint) -> None: ...

    def SetValues(self, P: nanoocp.gp.gp_Pnt2d, Uc1: float, Uc2: float, Trans1: IntRes2d_Transition, Trans2: IntRes2d_Transition, ReversedFlag: bool) -> None:
        """
        Sets the values for an existing intersection
        point. The meaning of the parameters are the same
        as for the Create.
        """

    def Value(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the value of the coordinates of the
        intersection point in the 2D space.
        """

    def ParamOnFirst(self) -> float:
        """Returns the parameter on the first curve."""

    def ParamOnSecond(self) -> float:
        """Returns the parameter on the second curve."""

    def TransitionOfFirst(self) -> IntRes2d_Transition:
        """
        Returns the transition of the 1st curve compared to
        the 2nd one.
        """

    def TransitionOfSecond(self) -> IntRes2d_Transition:
        """
        returns the transition of the 2nd curve compared to
        the 1st one.
        """

class IntRes2d_IntersectionSegment:
    """
    Definition of an intersection curve between
    two 2D curves.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, Oppos: bool) -> None:
        """Creates an infinite segment of intersection."""

    @overload
    def __init__(self, P1: IntRes2d_IntersectionPoint, P2: IntRes2d_IntersectionPoint, Oppos: bool, ReverseFlag: bool) -> None: ...

    @overload
    def __init__(self, P: IntRes2d_IntersectionPoint, First: bool, Oppos: bool, ReverseFlag: bool) -> None: ...

    @overload
    def __init__(self, theOther: IntRes2d_IntersectionSegment) -> None: ...

    def IsOpposite(self) -> bool:
        """
        Returns FALSE if the intersection segment has got
        the same orientation on both curves.
        """

    def HasFirstPoint(self) -> bool:
        """
        Returns True if the segment is limited by a first
        point. This point defines the lowest parameter
        admitted on the first curve for the segment. If
        IsOpposite returns False, it defines the lowest
        parameter on the second curve, otherwise, it is
        the highest parameter on the second curve.
        """

    def FirstPoint(self) -> IntRes2d_IntersectionPoint:
        """
        Returns the first point of the segment as an
        IntersectionPoint (with a transition). The
        exception DomainError is raised if HasFirstPoint
        returns False.
        """

    def HasLastPoint(self) -> bool:
        """
        Returns True if the segment is limited by a last
        point. This point defines the highest parameter
        admitted on the first curve for the segment. If
        IsOpposite returns False, it defines the highest
        parameter on the second curve, otherwise, it is
        the lowest parameter on the second curve.
        """

    def LastPoint(self) -> IntRes2d_IntersectionPoint:
        """
        Returns the last point of the segment as an
        IntersectionPoint (with a transition). The
        exception DomainError is raised if
        HasLastExtremity returns False.
        """

class IntRes2d_Intersection:
    """
    Defines the root class of all the Intersections
    between two 2D-Curves, and provides all the methods
    about the results of the Intersections Algorithms.
    """

    def IsDone(self) -> bool:
        """returns TRUE when the computation was successful."""

    def IsEmpty(self) -> bool:
        """
        Returns TRUE if there is no intersection between the
        given arguments.
        The exception NotDone is raised if IsDone returns FALSE.
        """

    def NbPoints(self) -> int:
        """
        This function returns the number of intersection
        points between the 2 curves.
        The exception NotDone is raised if IsDone returns FALSE.
        """

    def Point(self, N: int) -> IntRes2d_IntersectionPoint:
        """
        This function returns the intersection point
        of range N;
        The exception NotDone is raised if IsDone returns FALSE.
        The exception OutOfRange is raised if (N <= 0)
        or (N > NbPoints).
        """

    def NbSegments(self) -> int:
        """
        This function returns the number of intersection
        segments between the two curves.
        The exception NotDone is raised if IsDone returns FALSE.
        """

    def Segment(self, N: int) -> IntRes2d_IntersectionSegment:
        """
        This function returns the intersection segment
        of range N;
        The exception NotDone is raised if IsDone returns FALSE.
        The exception OutOfRange is raised if (N <= 0)
        or (N > NbPoints).
        """

    def SetReversedParameters(self, Reverseflag: bool) -> None: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.IntRes2d
IntRes2d_SequenceOfIntersectionPoint = nanoocp.NCollection.NCollection_Sequence[nanoocp.IntRes2d.IntRes2d_IntersectionPoint]
