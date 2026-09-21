"""OCCT package Hatch (toolkit TKGeomAlgo)"""

import enum
from typing import overload

import nanoocp.gp


class Hatch_LineForm(enum.IntEnum):
    """Form of a trimmed line"""

    Hatch_XLINE = 0

    Hatch_YLINE = 1

    Hatch_ANYLINE = 2

Hatch_XLINE: Hatch_LineForm = Hatch_LineForm.Hatch_XLINE

Hatch_YLINE: Hatch_LineForm = Hatch_LineForm.Hatch_YLINE

Hatch_ANYLINE: Hatch_LineForm = Hatch_LineForm.Hatch_ANYLINE

class Hatch_Parameter:
    """
    Stores an intersection on a line represented by :

    * A Real parameter.

    * A flag True when the parameter starts an interval.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Par1: float, Start: bool, Index: int = 0, Par2: float = 0.0) -> None: ...

    @overload
    def __init__(self, theOther: Hatch_Parameter) -> None: ...

class Hatch_Line:
    """
    Stores a Line in the Hatcher. Represented by:

    * A Lin2d from gp, the geometry of the line.

    * Bounding parameters for the line.

    * A sorted List of Parameters, the intersections
    on the line.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, L: nanoocp.gp.gp_Lin2d, T: Hatch_LineForm) -> None: ...

    @overload
    def __init__(self, theOther: Hatch_Line) -> None: ...

    def AddIntersection(self, Par1: float, Start: bool, Index: int, Par2: float, theToler: float) -> None:
        """Insert a new intersection in the sorted list."""

class Hatch_Hatcher:
    """
    The Hatcher is an algorithm to compute cross
    hatchings in a 2d plane. It is mainly dedicated to
    display purpose.

    Computing cross hatchings is a 3 steps process :

    1. The users stores in the Hatcher a set of 2d
    lines to be trimmed. Methods in the "Lines"
    category.

    2. The user trims the lines with a boundary. The
    inside of a boundary is on the left side. Methods
    in the "Trimming" category.

    3. The user reads back the trimmed lines. Methods
    in the "Results" category.

    The result is a set of parameter intervals on the
    line. The first parameter of an Interval may be
    RealFirst() and the last may be RealLast().

    A line can be a line parallel to the axis (X or Y
    line or a 2D line.

    The Hatcher has two modes :

    * The "Oriented" mode, where the orientation of
    the trimming curves is considered. The hatch are
    kept on the left of the trimming curve. In this
    mode infinite hatch can be computed.

    * The "UnOriented" mode, where the hatch are
    always finite.
    """

    @overload
    def __init__(self, Tol: float, Oriented: bool = True) -> None:
        """
        Returns an empty hatcher. <Tol> is the tolerance
        for intersections.
        """

    @overload
    def __init__(self, theOther: Hatch_Hatcher) -> None: ...

    @overload
    def Tolerance(self, Tol: float) -> None: ...

    @overload
    def Tolerance(self) -> float: ...

    @overload
    def AddLine(self, L: nanoocp.gp.gp_Lin2d, T: Hatch_LineForm = Hatch_LineForm.Hatch_ANYLINE) -> None:
        """
        Add a line <L> to be trimmed. <T> the type is
        only kept from information. It is not used in the
        computation.
        """

    @overload
    def AddLine(self, D: nanoocp.gp.gp_Dir2d, Dist: float) -> None:
        """
        Add an infinite line on direction <D> at distance
        <Dist> from the origin to be trimmed. <Dist> may
        be negative.

        If O is the origin of the 2D plane, and V the
        vector perpendicular to D (in the direct direction).

        A point P is on the line if :
        OP dot V = Dist
        The parameter of P on the line is
        OP dot D
        """

    def AddXLine(self, X: float) -> None:
        """
        Add an infinite line parallel to the Y-axis at
        abciss <X>.
        """

    def AddYLine(self, Y: float) -> None:
        """
        Add an infinite line parallel to the X-axis at
        ordinate <Y>.
        """

    @overload
    def Trim(self, L: nanoocp.gp.gp_Lin2d, Index: int = 0) -> None:
        """Trims the lines at intersections with <L>."""

    @overload
    def Trim(self, L: nanoocp.gp.gp_Lin2d, Start: float, End: float, Index: int = 0) -> None:
        """
        Trims the lines at intersections with <L> in the
        parameter range <Start>, <End>
        """

    @overload
    def Trim(self, P1: nanoocp.gp.gp_Pnt2d, P2: nanoocp.gp.gp_Pnt2d, Index: int = 0) -> None:
        """
        Trims the line at intersection with the oriented
        segment P1,P2.
        """

    @overload
    def NbIntervals(self) -> int:
        """
        Returns the total number of intervals on all the
        lines.
        """

    @overload
    def NbIntervals(self, I: int) -> int:
        """Returns the number of intervals on line of index <I>."""

    def NbLines(self) -> int:
        """Returns the number of lines."""

    def Line(self, I: int) -> nanoocp.gp.gp_Lin2d:
        """Returns the line of index <I>."""

    def LineForm(self, I: int) -> Hatch_LineForm:
        """Returns the type of the line of index <I>."""

    def IsXLine(self, I: int) -> bool:
        """
        Returns True if the line of index <I> has a
        constant X value.
        """

    def IsYLine(self, I: int) -> bool:
        """
        Returns True if the line of index <I> has a
        constant Y value.
        """

    def Coordinate(self, I: int) -> float:
        """
        Returns the X or Y coordinate of the line of index
        <I> if it is a X or a Y line.
        """

    def Start(self, I: int, J: int) -> float:
        """
        Returns the first parameter of interval <J> on
        line <I>.
        """

    def StartIndex(self, I: int, J: int) -> tuple[int, float]:
        """
        Returns the first Index and Par2 of interval <J> on
        line <I>.
        """

    def End(self, I: int, J: int) -> float:
        """
        Returns the last parameter of interval <J> on
        line <I>.
        """

    def EndIndex(self, I: int, J: int) -> tuple[int, float]:
        """
        Returns the last Index and Par2 of interval <J> on
        line <I>.
        """
