"""OCCT package TopAbs (toolkit TKG3d)"""

import enum
from typing import overload


class TopAbs_Orientation(enum.IntEnum):
    """
    Identifies the orientation of a topological shape.
    Orientation can represent a relation between two
    entities, or it can apply to a shape in its own right.
    When used to describe a relation between two
    shapes, orientation allows you to use the underlying
    entity in either direction. For example on a curve
    which is oriented FORWARD (say from left to right)
    you can have both a FORWARD and a REVERSED
    edge. The FORWARD edge will be oriented from
    left to right, and the REVERSED edge from right to
    left. In this way, you share the underlying entity. In
    other words, two faces of a cube can share an
    edge, and can also be used to build compound shapes.
    For each case in which an element is used as the
    boundary of a geometric domain of a higher
    dimension, this element defines two local regions of
    which one is arbitrarily considered as the default
    region. A change in orientation implies a switch of
    default region. This allows you to apply changes of
    orientation to the shape as a whole.
    """

    TopAbs_FORWARD = 0

    TopAbs_REVERSED = 1

    TopAbs_INTERNAL = 2

    TopAbs_EXTERNAL = 3

TopAbs_FORWARD: TopAbs_Orientation = TopAbs_Orientation.TopAbs_FORWARD

TopAbs_REVERSED: TopAbs_Orientation = TopAbs_Orientation.TopAbs_REVERSED

TopAbs_INTERNAL: TopAbs_Orientation = TopAbs_Orientation.TopAbs_INTERNAL

TopAbs_EXTERNAL: TopAbs_Orientation = TopAbs_Orientation.TopAbs_EXTERNAL

class TopAbs_ShapeEnum(enum.IntEnum):
    """
    Identifies various topological shapes. This
    enumeration allows you to use dynamic typing of shapes.
    The values are listed in order of complexity, from the
    most complex to the most simple i.e.
    COMPOUND > COMPSOLID > SOLID > .... > VERTEX > SHAPE.
    Any shape can contain simpler shapes in its definition.
    Abstract topological data structure describes a basic
    entity, the shape (present in this enumeration as the
    SHAPE value), which can be divided into the following
    component topologies:
    - COMPOUND: A group of any of the shapes below.
    - COMPSOLID: A set of solids connected by their
    faces. This expands the notions of WIRE and SHELL to solids.
    - SOLID: A part of 3D space bounded by shells.
    - SHELL: A set of faces connected by some of the
    edges of their wire boundaries. A shell can be open or closed.
    - FACE: Part of a plane (in 2D geometry) or a surface
    (in 3D geometry) bounded by a closed wire. Its
    geometry is constrained (trimmed) by contours.
    - WIRE: A sequence of edges connected by their
    vertices. It can be open or closed depending on
    whether the edges are linked or not.
    - EDGE: A single dimensional shape corresponding
    to a curve, and bound by a vertex at each extremity.
    - VERTEX: A zero-dimensional shape corresponding to a point in geometry.
    """

    TopAbs_COMPOUND = 0

    TopAbs_COMPSOLID = 1

    TopAbs_SOLID = 2

    TopAbs_SHELL = 3

    TopAbs_FACE = 4

    TopAbs_WIRE = 5

    TopAbs_EDGE = 6

    TopAbs_VERTEX = 7

    TopAbs_SHAPE = 8

TopAbs_COMPOUND: TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_COMPOUND

TopAbs_COMPSOLID: TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_COMPSOLID

TopAbs_SOLID: TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SOLID

TopAbs_SHELL: TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHELL

TopAbs_FACE: TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_FACE

TopAbs_WIRE: TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_WIRE

TopAbs_EDGE: TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_EDGE

TopAbs_VERTEX: TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_VERTEX

TopAbs_SHAPE: TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE

class TopAbs_State(enum.IntEnum):
    """
    Identifies the position of a vertex or a set of
    vertices relative to a region of a shape.
    The figure shown above illustrates the states of
    vertices found in various parts of the edge relative
    to the face which it intersects.
    """

    TopAbs_IN = 0

    TopAbs_OUT = 1

    TopAbs_ON = 2

    TopAbs_UNKNOWN = 3

TopAbs_IN: TopAbs_State = TopAbs_State.TopAbs_IN

TopAbs_OUT: TopAbs_State = TopAbs_State.TopAbs_OUT

TopAbs_ON: TopAbs_State = TopAbs_State.TopAbs_ON

TopAbs_UNKNOWN: TopAbs_State = TopAbs_State.TopAbs_UNKNOWN

class TopAbs:
    """
    This package gives resources for Topology oriented
    applications such as: Topological Data Structure,
    Topological Algorithms.

    It contains the:

    * ShapeEnum enumeration to describe the
    different topological shapes.

    * Orientation enumeration to describe the
    orientation of a topological shape.

    * State enumeration to describes the
    position of a point relative to a Shape.

    * Methods to manage the enumerations.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopAbs) -> None: ...

    @staticmethod
    def Compose(Or1: TopAbs_Orientation, Or2: TopAbs_Orientation) -> TopAbs_Orientation:
        """
        Compose the Orientation <Or1> and <Or2>. This
        composition is not symmetric (if you switch <Or1> and
        <Or2> the result is different). It assumes that <Or1>
        is the Orientation of a Shape S1 containing a Shape S2
        of Orientation Or2. The result is the cumulated
        orientation of S2 in S1. The composition law is:

        \\ Or2     FORWARD  REVERSED INTERNAL EXTERNAL
        Or1       -------------------------------------
        FORWARD   | FORWARD  REVERSED INTERNAL EXTERNAL
        |
        REVERSED  | REVERSED FORWARD  INTERNAL EXTERNAL
        |
        INTERNAL  | INTERNAL INTERNAL INTERNAL INTERNAL
        |
        EXTERNAL  | EXTERNAL EXTERNAL EXTERNAL EXTERNAL
        Note: The top corner in the table is the most important
        for the purposes of Open CASCADE topology and shape sharing.
        """

    @staticmethod
    def Reverse(Or: TopAbs_Orientation) -> TopAbs_Orientation:
        """
        Exchanges the interior/exterior status of the two
        sides. This is what happens when the sense of
        direction is reversed. The following rules apply:

        FORWARD          REVERSED
        REVERSED         FORWARD
        INTERNAL         INTERNAL
        EXTERNAL         EXTERNAL

        Reverse exchange the material sides.
        """

    @staticmethod
    def Complement(Or: TopAbs_Orientation) -> TopAbs_Orientation:
        """
        Reverses the interior/exterior status of each side of
        the object. So, to take the complement of an object
        means to reverse the interior/exterior status of its
        boundary, i.e. inside becomes outside.
        The method returns the complementary orientation,
        following the rules in the table below:
        FORWARD          REVERSED
        REVERSED         FORWARD
        INTERNAL         EXTERNAL
        EXTERNAL         INTERNAL

        Complement complements the material side.
        Inside becomes outside.
        """

    @overload
    @staticmethod
    def Print(theShapeType: TopAbs_ShapeEnum) -> object:
        """Prints the name of Shape type as a String on the Stream."""

    @overload
    @staticmethod
    def Print(theOrientation: TopAbs_Orientation) -> object:
        """Prints the name of the Orientation as a String on the Stream."""

    @overload
    @staticmethod
    def Print(St: TopAbs_State) -> object:
        """
        Prints the name of the State <St> as a String on
        the Stream <S> and returns <S>.
        """

    @staticmethod
    def ShapeTypeToString(theType: TopAbs_ShapeEnum) -> str:
        """
        Returns the string name for a given shape type.
        @param theType shape type
        @return string identifier from the list COMPOUND, COMPSOLID, SOLID, SHELL, FACE, WIRE, EDGE,
        VERTEX, SHAPE
        """

    @overload
    @staticmethod
    def ShapeTypeFromString(theTypeString: str) -> TopAbs_ShapeEnum:
        """
        Returns the shape type from the given string identifier (using case-insensitive comparison).
        @param theTypeString string identifier
        @return shape type or TopAbs_SHAPE if string identifier is invalid
        """

    @overload
    @staticmethod
    def ShapeTypeFromString(theTypeString: str) -> tuple[bool, TopAbs_ShapeEnum]:
        """
        Determines the shape type from the given string identifier (using case-insensitive
        comparison).
        @param theTypeString string identifier
        @param theType detected shape type
        @return TRUE if string identifier is known
        """

    @staticmethod
    def ShapeOrientationToString(theOrientation: TopAbs_Orientation) -> str:
        """
        Returns the string name for a given shape orientation.
        @param theOrientation shape orientation
        @return string identifier from the list FORWARD, REVERSED, INTERNAL, EXTERNAL
        """

    @overload
    @staticmethod
    def ShapeOrientationFromString(theOrientationString: str) -> TopAbs_Orientation:
        """
        Returns the shape orientation from the given string identifier (using case-insensitive
        comparison).
        @param theOrientationString string identifier
        @return shape orientation or TopAbs_FORWARD if string identifier is invalid
        """

    @overload
    @staticmethod
    def ShapeOrientationFromString(theOrientationString: str) -> tuple[bool, TopAbs_Orientation]:
        """
        Determines the shape orientation from the given string identifier (using case-insensitive
        comparison).
        @param theOrientationString string identifier
        @param theOrientation detected shape orientation
        @return TRUE if string identifier is known
        """
