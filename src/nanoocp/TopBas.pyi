"""OCCT package TopBas (toolkit TKHLR)"""

from typing import overload

import nanoocp.TopAbs


class TopBas_TestInterference:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Inters: float, Bound: int, Orient: nanoocp.TopAbs.TopAbs_Orientation, Trans: nanoocp.TopAbs.TopAbs_Orientation, BTrans: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def __init__(self, theOther: TopBas_TestInterference) -> None: ...

    @overload
    def Intersection(self, I: float) -> None: ...

    @overload
    def Intersection(self) -> float: ...

    @overload
    def Boundary(self, B: int) -> None: ...

    @overload
    def Boundary(self) -> int: ...

    @overload
    def Orientation(self, O: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @overload
    def Transition(self, Tr: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def Transition(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @overload
    def BoundaryTransition(self, BTr: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    @overload
    def BoundaryTransition(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def ChangeIntersection(self) -> float: ...

    def SetIntersection(self, theValue: float) -> None:
        """
        Python addition: sets the value ChangeIntersection() returns by reference in C++.
        """

    def ChangeBoundary(self) -> int: ...

    def SetBoundary(self, theValue: int) -> None:
        """
        Python addition: sets the value ChangeBoundary() returns by reference in C++.
        """
