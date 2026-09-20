"""OCCT package TopLoc (toolkit TKMath)"""

from typing import overload

import nanoocp.Standard
import nanoocp.gp


class TopLoc_Datum3D(nanoocp.Standard.Standard_Transient):
    """
    Describes a coordinate transformation, i.e. a change
    to an elementary 3D coordinate system, or position in 3D space.
    A Datum3D is always described relative to the default datum.
    The default datum is described relative to itself: its
    origin is (0,0,0), and its axes are (1,0,0) (0,1,0) (0,0,1).
    """

    @overload
    def __init__(self) -> None:
        """Constructs a default Datum3D."""

    @overload
    def __init__(self, T: nanoocp.gp.gp_Trsf) -> None:
        """
        Constructs a Datum3D form a Trsf from gp. An error is
        raised if the Trsf is not a rigid transformation.
        """

    def Transformation(self) -> nanoocp.gp.gp_Trsf:
        """
        Returns a gp_Trsf which, when applied to this datum, produces the default datum.
        """

    def Trsf(self) -> nanoocp.gp.gp_Trsf:
        """
        Returns a gp_Trsf which, when applied to this datum, produces the default datum.
        """

    def Form(self) -> nanoocp.gp.gp_TrsfForm:
        """Return transformation form."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TopLoc_ItemLocation:
    """
    An ItemLocation is an elementary coordinate system
    in a Location.

    The ItemLocation contains:
    * The elementary Datum.
    * The exponent of the elementary Datum.
    * The transformation associated to the composition.
    """

    def __init__(self, D: TopLoc_Datum3D, P: int) -> None:
        """
        Sets the elementary Datum to <D>
        Sets the exponent to <P>
        """

class TopLoc_SListOfItemLocation:
    """
    An SListOfItemLocation is a LISP like list of Items.
    An SListOfItemLocation is:
    . Empty.
    . Or it has a Value and a Tail which is an other SListOfItemLocation.

    The Tail of an empty list is an empty list.
    SListOfItemLocation are shared. It means that they can be
    modified through other lists.
    SListOfItemLocation may be used as Iterators. They have Next,
    More, and value methods. To iterate on the content
    of the list S just do.

    SListOfItemLocation Iterator;
    for (Iterator = S; Iterator.More(); Iterator.Next())
    X = Iterator.Value();
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty List."""

    @overload
    def __init__(self, Other: TopLoc_SListOfItemLocation) -> None:
        """Creates a list from an other one. The lists are shared."""

    @overload
    def __init__(self, anItem: TopLoc_ItemLocation, aTail: TopLoc_SListOfItemLocation) -> None:
        """Creates a List with <anItem> as value and <aTail> as tail."""

    def Assign(self, Other: TopLoc_SListOfItemLocation) -> TopLoc_SListOfItemLocation:
        """
        Sets a list from an other one. The lists are
        shared. The list itself is returned.
        """

    def IsEmpty(self) -> bool:
        """Return true if this list is empty"""

    def Clear(self) -> None:
        """Sets the list to be empty."""

    def Value(self) -> TopLoc_ItemLocation:
        """
        Returns the current value of the list. An error is
        raised if the list is empty.
        """

    def Tail(self) -> TopLoc_SListOfItemLocation:
        """
        Returns the current tail of the list. On an empty
        list the tail is the list itself.
        """

    def Construct(self, anItem: TopLoc_ItemLocation) -> None:
        """
        Replaces the list by a list with <anItem> as Value
        and the list <me> as tail.
        """

    def ToTail(self) -> None:
        """Replaces the list <me> by its tail."""

    def More(self) -> bool:
        """
        Returns True if the iterator has a current value.
        This is !IsEmpty()
        """

    def Next(self) -> None:
        """
        Moves the iterator to the next object in the list.
        If the iterator is empty it will stay empty. This is ToTail()
        """

class TopLoc_Location:
    """
    A Location is a composite transition. It comprises a
    series of elementary reference coordinates, i.e.
    objects of type TopLoc_Datum3D, and the powers to
    which these objects are raised.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty local coordinate system object.
        Note: A Location constructed from a default datum is said to be "empty".
        """

    @overload
    def __init__(self, theOther: TopLoc_Location) -> None:
        """Copy constructor."""

    @overload
    def __init__(self, T: nanoocp.gp.gp_Trsf) -> None:
        """
        Constructs the local coordinate system object defined
        by the transformation T. T invokes in turn, a TopLoc_Datum3D object.
        """

    @overload
    def __init__(self, D: TopLoc_Datum3D) -> None:
        """
        Constructs the local coordinate system object defined by the 3D datum D.
        Exceptions
        Standard_ConstructionError if the transformation
        T does not represent a 3D coordinate system.
        """

    def IsIdentity(self) -> bool:
        """Returns true if this location is equal to the Identity transformation."""

    def Identity(self) -> None:
        """Resets this location to the Identity transformation."""

    def FirstDatum(self) -> TopLoc_Datum3D:
        """
        Returns the first elementary datum of the
        Location. Use the NextLocation function recursively to access
        the other data comprising this location.
        Exceptions
        Standard_NoSuchObject if this location is empty.
        """

    def FirstPower(self) -> int:
        """
        Returns the power elevation of the first
        elementary datum.
        Exceptions
        Standard_NoSuchObject if this location is empty.
        """

    def NextLocation(self) -> TopLoc_Location:
        """
        Returns a Location representing <me> without the
        first datum. We have the relation:

        <me> = NextLocation() * FirstDatum() ^ FirstPower()
        Exceptions
        Standard_NoSuchObject if this location is empty.
        """

    def Transformation(self) -> nanoocp.gp.gp_Trsf:
        """
        Returns the transformation associated to the
        coordinate system.
        """

    def Inverted(self) -> TopLoc_Location:
        """
        Returns the inverse of <me>.

        <me> * Inverted() is an Identity.
        """

    def Multiplied(self, Other: TopLoc_Location) -> TopLoc_Location:
        """
        Returns <me> * <Other>, the elementary datums are
        concatenated.
        """

    def __mul__(self, Other: TopLoc_Location) -> TopLoc_Location: ...

    def Divided(self, Other: TopLoc_Location) -> TopLoc_Location:
        """Returns <me> / <Other>."""

    def __truediv__(self, Other: TopLoc_Location) -> TopLoc_Location: ...

    def Predivided(self, Other: TopLoc_Location) -> TopLoc_Location:
        """Returns <Other>.Inverted() * <me>."""

    def Powered(self, pwr: int) -> TopLoc_Location:
        """
        Returns me at the power <pwr>. If <pwr> is zero
        returns Identity. <pwr> can be lower than zero
        (usual meaning for powers).
        """

    def HashCode(self) -> int:
        """
        Returns a hashed value for this local coordinate system. This value is used, with map tables,
        to store and retrieve the object easily
        @return a computed hash code
        """

    def IsEqual(self, theOther: TopLoc_Location) -> bool:
        """
        Returns true if this location and the location Other
        have the same elementary data, i.e. contain the same
        series of TopLoc_Datum3D and respective powers.
        This method is an alias for operator ==.
        """

    def __eq__(self, theOther: TopLoc_Location) -> bool: ...

    def IsDifferent(self, theOther: TopLoc_Location) -> bool:
        """
        Returns true if this location and the location Other do
        not have the same elementary data, i.e. do not
        contain the same series of TopLoc_Datum3D and respective powers.
        This method is an alias for operator !=.
        """

    def __ne__(self, theOther: TopLoc_Location) -> bool: ...

    def Clear(self) -> None:
        """Clear myItems"""

    @staticmethod
    def ScalePrec() -> float: ...

class TopLoc_SListNodeOfItemLocation(nanoocp.Standard.Standard_Transient):
    def __init__(self, I: TopLoc_ItemLocation, aTail: TopLoc_SListOfItemLocation) -> None: ...

    def Tail(self) -> TopLoc_SListOfItemLocation: ...

    def Value(self) -> TopLoc_ItemLocation: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
