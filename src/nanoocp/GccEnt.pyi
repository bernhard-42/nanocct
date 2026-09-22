"""OCCT package GccEnt (toolkit TKGeomAlgo)"""

import enum
from typing import overload

import nanoocp.Standard
import nanoocp.gp


class GccEnt_Position(enum.IntEnum):
    """
    Qualifies the position of a solution of a construction
    algorithm with respect to one of its arguments. This is one of the following:
    -   GccEnt_unqualified: the position of the solution
    is undefined with respect to the argument,
    -   GccEnt_enclosing: the solution encompasses the argument,
    -   GccEnt_enclosed: the solution is encompassed by the argument,
    -   GccEnt_outside: the solution and the argument
    are external to one another,
    -   GccEnt_noqualifier: the value returned during a
    consultation of the qualifier when the argument is
    defined as GccEnt_unqualified.
    Note: the interior of a line or any open curve is
    defined as the left-hand side of the line or curve in
    relation to its orientation.
    """

    GccEnt_unqualified = 0

    GccEnt_enclosing = 1

    GccEnt_enclosed = 2

    GccEnt_outside = 3

    GccEnt_noqualifier = 4

GccEnt_unqualified: GccEnt_Position = GccEnt_Position.GccEnt_unqualified

GccEnt_enclosing: GccEnt_Position = GccEnt_Position.GccEnt_enclosing

GccEnt_enclosed: GccEnt_Position = GccEnt_Position.GccEnt_enclosed

GccEnt_outside: GccEnt_Position = GccEnt_Position.GccEnt_outside

GccEnt_noqualifier: GccEnt_Position = GccEnt_Position.GccEnt_noqualifier

class GccEnt:
    """
    This package provides an implementation of the qualified
    entities useful to create 2d entities with geometric
    constraints. The qualifier explains which subfamily of
    solutions we want to obtain. It uses the following law: the
    matter/the interior side is at the left of the line, if we go
    from the beginning to the end.
    The qualifiers are:
    Enclosing   : the solution(s) must enclose the argument.
    Enclosed    : the solution(s) must be enclosed in the
    argument.
    Outside     : both the solution(s) and the argument must be
    outside to each other.
    Unqualified : the position is undefined, so give all the
    solutions.
    The use of a qualifier is always required if such
    subfamilies exist. For example, it is not used for a point.
    Note:    the interior of a curve is defined as the left-hand
    side of the curve in relation to its orientation.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GccEnt) -> None: ...

    @staticmethod
    def Print(thePosition: GccEnt_Position) -> str:
        """Prints the name of Position type as a String on the Stream."""

    @staticmethod
    def PositionToString(thePosition: GccEnt_Position) -> str:
        """
        Returns the string name for a given position.
        @param thePosition position type
        @return string identifier from the list UNQUALIFIED ENCLOSING ENCLOSED OUTSIDE NOQUALIFIER
        """

    @staticmethod
    def PositionFromString(thePositionString: str) -> GccEnt_Position:
        """
        Returns the position from the given string identifier (using case-insensitive comparison).
        @param thePositionString string identifier
        @return position or GccEnt_unqualified if string identifier is invalid
        """

    @staticmethod
    def PositionFromString__GccEnt_Position(thePositionString: str) -> tuple[bool, GccEnt_Position]:
        """
        PositionFromString__GccEnt_Position: the C++ overload PositionFromString(const char *, GccEnt_Position &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Determines the position from the given string identifier (using case-insensitive comparison).
        @param thePositionString string identifier
        @param thePosition detected shape type
        @return TRUE if string identifier is known
        """

    @overload
    @staticmethod
    def Unqualified(Obj: nanoocp.gp.gp_Lin2d) -> GccEnt_QualifiedLin:
        """
        Constructs a qualified line,
        so that the relative position to the circle or line of the
        solution computed by a construction algorithm using the
        qualified circle or line is not qualified, i.e. all solutions apply.
        """

    @overload
    @staticmethod
    def Unqualified(Obj: nanoocp.gp.gp_Circ2d) -> GccEnt_QualifiedCirc:
        """
        Constructs a qualified circle
        so that the relative position to the circle or line of the
        solution computed by a construction algorithm using the
        qualified circle or line is not qualified, i.e. all solutions apply.
        """

    @staticmethod
    def Enclosing(Obj: nanoocp.gp.gp_Circ2d) -> GccEnt_QualifiedCirc:
        """
        Constructs such a qualified circle that the solution
        computed by a construction algorithm using the qualified
        circle encloses the circle.
        """

    @overload
    @staticmethod
    def Enclosed(Obj: nanoocp.gp.gp_Lin2d) -> GccEnt_QualifiedLin:
        """
        Constructs a qualified line,
        so that the solution computed by a construction
        algorithm using the qualified circle or line is enclosed by
        the circle or line.
        """

    @overload
    @staticmethod
    def Enclosed(Obj: nanoocp.gp.gp_Circ2d) -> GccEnt_QualifiedCirc:
        """
        Constructs a qualified circle
        so that the solution computed by a construction
        algorithm using the qualified circle or line is enclosed by
        the circle or line.
        """

    @overload
    @staticmethod
    def Outside(Obj: nanoocp.gp.gp_Lin2d) -> GccEnt_QualifiedLin:
        """
        Constructs a qualified line,
        so that the solution computed by a construction
        algorithm using the qualified circle or line and the circle
        or line are external to one another.
        """

    @overload
    @staticmethod
    def Outside(Obj: nanoocp.gp.gp_Circ2d) -> GccEnt_QualifiedCirc:
        """
        Constructs a qualified circle
        so that the solution computed by a construction
        algorithm using the qualified circle or line and the circle
        or line are external to one another.
        """

class GccEnt_BadQualifier(nanoocp.Standard.Standard_DomainError):
    pass

class GccEnt_QualifiedCirc:
    """
    Creates a qualified 2d Circle.
    A qualified 2D circle is a circle (gp_Circ2d circle) with a
    qualifier which specifies whether the solution of a
    construction algorithm using the qualified circle (as an argument):
    -   encloses the circle, or
    -   is enclosed by the circle, or
    -   is built so that both the circle and it are external to one another, or
    -   is undefined (all solutions apply).
    """

    @overload
    def __init__(self, Qualified: nanoocp.gp.gp_Circ2d, Qualifier: GccEnt_Position) -> None:
        """
        Constructs a qualified circle by assigning the qualifier
        Qualifier to the circle Qualified. Qualifier may be:
        -   GccEnt_enclosing if the solution computed by a
        construction algorithm using the qualified circle
        encloses the circle, or
        -   GccEnt_enclosed if the solution is enclosed by the circle, or
        -   GccEnt_outside if both the solution and the circle
        are external to one another, or
        -   GccEnt_unqualified if all solutions apply.
        """

    @overload
    def __init__(self, theOther: GccEnt_QualifiedCirc) -> None: ...

    def Qualified(self) -> nanoocp.gp.gp_Circ2d:
        """Returns a 2D circle to which the qualifier is assigned."""

    def Qualifier(self) -> GccEnt_Position:
        """
        Returns
        -   the qualifier of this qualified circle, if it is enclosing,
        enclosed or outside, or
        -   GccEnt_noqualifier if it is unqualified.
        """

    def IsUnqualified(self) -> bool:
        """
        Returns true if the Circ2d is Unqualified and false in
        the other cases.
        """

    def IsEnclosing(self) -> bool:
        """
        Returns true if the solution computed by a construction
        algorithm using this qualified circle encloses the circle.
        """

    def IsEnclosed(self) -> bool:
        """
        Returns true if the solution computed by a construction
        algorithm using this qualified circle is enclosed by the circle.
        """

    def IsOutside(self) -> bool:
        """
        Returns true if both the solution computed by a
        construction algorithm using this qualified circle and the
        circle are external to one another.
        """

class GccEnt_QualifiedLin:
    """
    Describes a qualified 2D line.
    A qualified 2D line is a line (gp_Lin2d line) with a
    qualifier which specifies whether the solution of a
    construction algorithm using the qualified line (as an argument):
    -   is 'enclosed' by the line, or
    -   is built so that both the line and it are external to one another, or
    -   is undefined (all solutions apply).
    Note: the interior of a line is defined as the left-hand
    side of the line in relation to its orientation (i.e. when
    moving from the start to the end of the curve).
    """

    @overload
    def __init__(self, Qualified: nanoocp.gp.gp_Lin2d, Qualifier: GccEnt_Position) -> None:
        """
        Constructs a qualified line by assigning the qualifier
        Qualifier to the line Qualified.
        Qualifier may be:
        -   GccEnt_enclosed if the solution is enclosed by the line, or
        -   GccEnt_outside if both the solution and the line are external to one another, or
        -   GccEnt_unqualified if all solutions apply.
        Note : the interior of a line is defined as the left-hand
        side of the line in relation to its orientation.
        """

    @overload
    def __init__(self, theOther: GccEnt_QualifiedLin) -> None: ...

    def Qualified(self) -> nanoocp.gp.gp_Lin2d:
        """Returns a 2D line to which the qualifier is assigned."""

    def Qualifier(self) -> GccEnt_Position:
        """
        Returns the qualifier of this qualified line, if it is "enclosed" or
        "outside", or
        -   GccEnt_noqualifier if it is unqualified.
        """

    def IsUnqualified(self) -> bool:
        """
        Returns true if the solution is unqualified and false in
        the other cases.
        """

    def IsEnclosed(self) -> bool:
        """
        Returns true if the solution is Enclosed in the Lin2d and false in
        the other cases.
        """

    def IsOutside(self) -> bool:
        """
        Returns true if the solution is Outside the Lin2d and false in
        the other cases.
        """
