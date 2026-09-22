"""OCCT package Intrv (toolkit TKHLR)"""

import enum
from typing import overload


class Intrv_Position(enum.IntEnum):
    Intrv_Before = 0

    Intrv_JustBefore = 1

    Intrv_OverlappingAtStart = 2

    Intrv_JustEnclosingAtEnd = 3

    Intrv_Enclosing = 4

    Intrv_JustOverlappingAtStart = 5

    Intrv_Similar = 6

    Intrv_JustEnclosingAtStart = 7

    Intrv_Inside = 8

    Intrv_JustOverlappingAtEnd = 9

    Intrv_OverlappingAtEnd = 10

    Intrv_JustAfter = 11

    Intrv_After = 12

Intrv_Before: Intrv_Position = Intrv_Position.Intrv_Before

Intrv_JustBefore: Intrv_Position = Intrv_Position.Intrv_JustBefore

Intrv_OverlappingAtStart: Intrv_Position = Intrv_Position.Intrv_OverlappingAtStart

Intrv_JustEnclosingAtEnd: Intrv_Position = Intrv_Position.Intrv_JustEnclosingAtEnd

Intrv_Enclosing: Intrv_Position = Intrv_Position.Intrv_Enclosing

Intrv_JustOverlappingAtStart: Intrv_Position = Intrv_Position.Intrv_JustOverlappingAtStart

Intrv_Similar: Intrv_Position = Intrv_Position.Intrv_Similar

Intrv_JustEnclosingAtStart: Intrv_Position = Intrv_Position.Intrv_JustEnclosingAtStart

Intrv_Inside: Intrv_Position = Intrv_Position.Intrv_Inside

Intrv_JustOverlappingAtEnd: Intrv_Position = Intrv_Position.Intrv_JustOverlappingAtEnd

Intrv_OverlappingAtEnd: Intrv_Position = Intrv_Position.Intrv_OverlappingAtEnd

Intrv_JustAfter: Intrv_Position = Intrv_Position.Intrv_JustAfter

Intrv_After: Intrv_Position = Intrv_Position.Intrv_After

class Intrv_Interval:
    """
    **-----------****             Other
    ***---*                                   IsBefore
    ***----------*                            IsJustBefore
    ***---------------*                       IsOverlappingAtStart
    ***------------------------*              IsJustEnclosingAtEnd
    ***-----------------------------------*   IsEnclosing
    ***----*                       IsJustOverlappingAtStart
    ***-------------*              IsSimilar
    ***------------------------*   IsJustEnclosingAtStart
    ***-*                   IsInside
    ***------*              IsJustOverlappingAtEnd
    ***-----------------*   IsOverlappingAtEnd
    ***--------*   IsJustAfter
    ***---*   IsAfter
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Start: float, End: float) -> None: ...

    @overload
    def __init__(self, Start: float, TolStart: float, End: float, TolEnd: float) -> None: ...

    @overload
    def __init__(self, theOther: Intrv_Interval) -> None: ...

    def Start(self) -> float: ...

    def End(self) -> float: ...

    def TolStart(self) -> float: ...

    def TolEnd(self) -> float: ...

    def Bounds(self) -> tuple[float, float, float, float]: ...

    def SetStart(self, Start: float, TolStart: float) -> None: ...

    def FuseAtStart(self, Start: float, TolStart: float) -> None:
        """
        ****+****-------------------->      Old one
        ****+****------------------------>      New one to fuse
        <<<     <<<
        ****+****------------------------>      result
        """

    def CutAtStart(self, Start: float, TolStart: float) -> None:
        """
        ****+****----------->      Old one
        <----------**+**                        Tool for cutting
        >>>     >>>
        ****+****----------->      result
        """

    def SetEnd(self, End: float, TolEnd: float) -> None: ...

    def FuseAtEnd(self, End: float, TolEnd: float) -> None:
        """
        <---------------------****+****      Old one
        <-----------------**+**              New one to fuse
        >>>     >>>
        <---------------------****+****      result
        """

    def CutAtEnd(self, End: float, TolEnd: float) -> None:
        """
        <-----****+****                      Old one
        **+**------>             Tool for cutting
        <<<     <<<
        <-----****+****                      result
        """

    def IsProbablyEmpty(self) -> bool:
        """
        True if myStart+myTolStart > myEnd-myTolEnd
        or if myEnd+myTolEnd > myStart-myTolStart
        """

    def Position(self, Other: Intrv_Interval) -> Intrv_Position:
        """
        True if me is Before Other
        **-----------****             Other
        ***-----*                                   Before
        ***------------*                            JustBefore
        ***-----------------*                       OverlappingAtStart
        ***--------------------------*              JustEnclosingAtEnd
        ***-------------------------------------*   Enclosing
        ***----*                       JustOverlappingAtStart
        ***-------------*              Similar
        ***------------------------*   JustEnclosingAtStart
        ***-*                   Inside
        ***------*              JustOverlappingAtEnd
        ***-----------------*   OverlappingAtEnd
        ***--------*   JustAfter
        ***---*   After
        """

    def IsBefore(self, Other: Intrv_Interval) -> bool:
        """
        True if me is Before Other
        ***----------------**                              me
        **-----------****          Other
        """

    def IsAfter(self, Other: Intrv_Interval) -> bool:
        """
        True if me is After Other
        **-----------****          me
        ***----------------**                              Other
        """

    def IsInside(self, Other: Intrv_Interval) -> bool:
        """
        True if me is Inside Other
        **-----------****                          me
        ***--------------------------**                    Other
        """

    def IsEnclosing(self, Other: Intrv_Interval) -> bool:
        """
        True if me is Enclosing Other
        ***----------------------------****                  me
        ***------------------**                        Other
        """

    def IsJustEnclosingAtStart(self, Other: Intrv_Interval) -> bool:
        """
        True if me is just Enclosing Other at start
        ***---------------------------****            me
        ***------------------**                        Other
        """

    def IsJustEnclosingAtEnd(self, Other: Intrv_Interval) -> bool:
        """
        True if me is just Enclosing Other at End
        ***----------------------------****                  me
        ***-----------------****                   Other
        """

    def IsJustBefore(self, Other: Intrv_Interval) -> bool:
        """
        True if me is just before Other
        ***--------****                                      me
        ***-----------**                        Other
        """

    def IsJustAfter(self, Other: Intrv_Interval) -> bool:
        """
        True if me is just after Other
        ****-------****                         me
        ***-----------**                                     Other
        """

    def IsOverlappingAtStart(self, Other: Intrv_Interval) -> bool:
        """
        True if me is overlapping Other at start
        ***---------------***                                me
        ***-----------**                        Other
        """

    def IsOverlappingAtEnd(self, Other: Intrv_Interval) -> bool:
        """
        True if me is overlapping Other at end
        ***-----------**                        me
        ***---------------***                                Other
        """

    def IsJustOverlappingAtStart(self, Other: Intrv_Interval) -> bool:
        """
        True if me is just overlapping Other at start
        ***-----------***                                    me
        ***------------------------**                        Other
        """

    def IsJustOverlappingAtEnd(self, Other: Intrv_Interval) -> bool:
        """
        True if me is just overlapping Other at end
        ***-----------*                         me
        ***------------------------**                        Other
        """

    def IsSimilar(self, Other: Intrv_Interval) -> bool:
        """
        True if me and Other have the same bounds
        *----------------***                                me
        ***-----------------**                               Other
        """

class Intrv_Intervals:
    """
    The class Intervals is a sorted sequence of non
    overlapping Real Intervals.
    """

    @overload
    def __init__(self) -> None:
        """Creates a void sequence of intervals."""

    @overload
    def __init__(self, Int: Intrv_Interval) -> None:
        """Creates a sequence of one interval."""

    @overload
    def __init__(self, theOther: Intrv_Intervals) -> None: ...

    @overload
    def Intersect(self, Tool: Intrv_Interval) -> None:
        """Intersects the intervals with the interval <Tool>."""

    @overload
    def Intersect(self, Tool: Intrv_Intervals) -> None:
        """
        Intersects the intervals with the intervals in the
        sequence <Tool>.
        """

    @overload
    def Subtract(self, Tool: Intrv_Interval) -> None: ...

    @overload
    def Subtract(self, Tool: Intrv_Intervals) -> None: ...

    @overload
    def Unite(self, Tool: Intrv_Interval) -> None: ...

    @overload
    def Unite(self, Tool: Intrv_Intervals) -> None: ...

    @overload
    def XUnite(self, Tool: Intrv_Interval) -> None: ...

    @overload
    def XUnite(self, Tool: Intrv_Intervals) -> None: ...

    def NbIntervals(self) -> int: ...

    def Value(self, Index: int) -> Intrv_Interval: ...

def AreFused(c1: float, t1: float, c2: float, t2: float) -> bool: ...
