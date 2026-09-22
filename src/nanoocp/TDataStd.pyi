"""OCCT package TDataStd (toolkit TKLCAF)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TColStd
import nanoocp.TCollection
import nanoocp.TDF


class TDataStd_RealEnum(enum.IntEnum):
    """
    The terms of this enumeration define the
    semantics of a real number value.
    """

    TDataStd_SCALAR = 0

    TDataStd_LENGTH = 1

    TDataStd_ANGULAR = 2

TDataStd_SCALAR: TDataStd_RealEnum = TDataStd_RealEnum.TDataStd_SCALAR

TDataStd_LENGTH: TDataStd_RealEnum = TDataStd_RealEnum.TDataStd_LENGTH

TDataStd_ANGULAR: TDataStd_RealEnum = TDataStd_RealEnum.TDataStd_ANGULAR

class TDataStd:
    """
    This package defines standard attributes for
    modelling.
    These allow you to create and modify labels
    and attributes for many basic data types.
    Standard topological and visualization
    attributes have also been created.
    To find an attribute attached to a specific label,
    you use the GUID of the type of attribute you
    are looking for. To do this, first find this
    information using the method GetID as follows: Standard_GUID anID =
    MyAttributeClass::GetID();
    Then, use the method Find for the label as follows:
    bool HasAttribute
    =
    aLabel.Find(anID,anAttribute);
    Note
    For information on the relations between this
    component of OCAF and the others, refer to the OCAF User's Guide.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd) -> None: ...

    @staticmethod
    def IDList(anIDList: nanoocp.NCollection.NCollection_List[nanoocp.Standard.Standard_GUID]) -> None:
        """
        Appends to <anIDList> the list of the attributes
        IDs of this package. CAUTION: <anIDList> is NOT
        cleared before use.
        """

    @staticmethod
    def Print(DIM: TDataStd_RealEnum) -> str:
        """
        Prints the name of the real dimension <DIM> as a String on
        the Stream <S> and returns <S>.
        """

class TDataStd_AsciiString(nanoocp.TDF.TDF_Attribute):
    """
    Used to define an AsciiString attribute containing a TCollection_AsciiString
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_AsciiString) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        Returns the GUID of the attribute.
        """

    @overload
    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, string: nanoocp.TCollection.TCollection_AsciiString) -> TDataStd_AsciiString:
        """
        Finds, or creates an AsciiString attribute and sets the string.
        the AsciiString attribute is returned.
        AsciiString methods
        ===================
        """

    @overload
    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, guid: nanoocp.Standard.Standard_GUID, string: nanoocp.TCollection.TCollection_AsciiString) -> TDataStd_AsciiString:
        """
        Finds, or creates, an AsciiString attribute with explicit user defined <guid> and sets
        <string>. The Name attribute is returned.
        """

    def Set(self, S: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    @overload
    def SetID(self, guid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit user defined GUID to the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    def Get(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def IsEmpty(self) -> bool: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_BooleanArray(nanoocp.TDF.TDF_Attribute):
    """An array of boolean values."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_BooleanArray) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        Static methods
        ==============
        Returns an ID for array.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, lower: int, upper: int) -> TDataStd_BooleanArray:
        """Finds or creates an attribute with internal boolean array."""

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, theGuid: nanoocp.Standard.Standard_GUID, lower: int, upper: int) -> TDataStd_BooleanArray:
        """
        Finds or creates an attribute with the array using explicit user defined <guid>.
        """

    def Init(self, lower: int, upper: int) -> None:
        """Initialize the inner array with bounds from <lower> to <upper>"""

    def SetValue(self, index: int, value: bool) -> None:
        """
        Sets the <Index>th element of the array to <Value>
        OutOfRange exception is raised if <Index> doesn't respect Lower and Upper bounds of the
        internal array.
        """

    @overload
    def SetID(self, theGuid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit GUID (user defined) for the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    def Value(self, Index: int) -> bool:
        """Return the value of the <Index>th element of the array."""

    def __call__(self, Index: int) -> bool: ...

    def Lower(self) -> int:
        """Returns the lower boundary of the array."""

    def Upper(self) -> int:
        """Returns the upper boundary of the array."""

    def Length(self) -> int:
        """Returns the number of elements in the array."""

    def InternalArray(self) -> nanoocp.NCollection.NCollection_HArray1__unsigned_char: ...

    def SetInternalArray(self, values: nanoocp.NCollection.NCollection_HArray1__unsigned_char | None) -> None: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_BooleanList(nanoocp.TDF.TDF_Attribute):
    """Contains a list of bolleans."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_BooleanList) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        Static methods
        ==============
        Returns the ID of the list of booleans attribute.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label) -> TDataStd_BooleanList:
        """Finds or creates a list of boolean values attribute."""

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, theGuid: nanoocp.Standard.Standard_GUID) -> TDataStd_BooleanList:
        """
        Finds or creates a list of boolean values attribute with explicit user defined <guid>.
        """

    def IsEmpty(self) -> bool: ...

    def Extent(self) -> int: ...

    def Prepend(self, value: bool) -> None: ...

    def Append(self, value: bool) -> None: ...

    def Clear(self) -> None: ...

    def First(self) -> bool: ...

    def Last(self) -> bool: ...

    def List(self) -> nanoocp.NCollection.NCollection_List__unsigned_char:
        """
        1 - means TRUE,
        0 - means FALSE.
        """

    def InsertBefore(self, index: int, before_value: bool) -> bool:
        """
        Inserts the <value> before the <index> position.
        The indices start with 1 .. Extent().
        """

    def InsertAfter(self, index: int, after_value: bool) -> bool:
        """
        Inserts the <value> after the <index> position.
        The indices start with 1 .. Extent().
        """

    def Remove(self, index: int) -> bool:
        """Removes a value at <index> position."""

    @overload
    def SetID(self, theGuid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit GUID (user defined) for the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_ByteArray(nanoocp.TDF.TDF_Attribute):
    """An array of Byte (unsigned char) values."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_ByteArray) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        Static methods
        ==============
        Returns an ID for array.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, lower: int, upper: int, isDelta: bool = False) -> TDataStd_ByteArray:
        """
        Finds or creates an attribute with the array on the specified label.
        If <isDelta> == False, DefaultDeltaOnModification is used.
        If <isDelta> == True, DeltaOnModification of the current attribute is used.
        If attribute is already set, all input parameters are refused and the found
        attribute is returned.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, theGuid: nanoocp.Standard.Standard_GUID, lower: int, upper: int, isDelta: bool = False) -> TDataStd_ByteArray:
        """
        Finds or creates an attribute with byte array and explicit user defined <guid> on the
        specified label.
        """

    def Init(self, lower: int, upper: int) -> None:
        """Initialize the inner array with bounds from <lower> to <upper>"""

    def SetValue(self, index: int, value: int) -> None:
        """
        Sets the <Index>th element of the array to <Value>
        OutOfRange exception is raised if <Index> doesn't respect Lower and Upper bounds of the
        internal array.
        """

    @overload
    def SetID(self, theGuid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit GUID (user defined) for the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    def Value(self, Index: int) -> int:
        """Return the value of the <Index>th element of the array."""

    def __call__(self, Index: int) -> int: ...

    def Lower(self) -> int:
        """Returns the lower boundary of the array."""

    def Upper(self) -> int:
        """Returns the upper boundary of the array."""

    def Length(self) -> int:
        """Returns the number of elements in the array."""

    def InternalArray(self) -> nanoocp.NCollection.NCollection_HArray1__unsigned_char: ...

    def ChangeArray(self, newArray: nanoocp.NCollection.NCollection_HArray1__unsigned_char | None, isCheckItems: bool = True) -> None:
        """
        Sets the inner array <myValue> of the attribute to
        <newArray>. If value of <newArray> differs from <myValue>, Backup performed
        and myValue refers to new instance of HArray1OfInteger that holds <newArray>
        values.
        If <isCheckItems> equal True each item of <newArray> will be checked with each
        item of <myValue> for coincidence (to avoid backup).
        """

    def GetDelta(self) -> bool: ...

    def SetDelta(self, isDelta: bool) -> None:
        """for internal use only!"""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DeltaOnModification(self, anOldAttribute: nanoocp.TDF.TDF_Attribute | None) -> nanoocp.TDF.TDF_DeltaOnModification:
        """
        Makes a DeltaOnModification between <me> and
        <anOldAttribute>.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class TDataStd_ChildNodeIterator:
    """
    Iterates on the ChildStepren step of a step, at the
    first level only. It is possible to ask the
    iterator to explore all the sub step levels of the
    given one, with the option "allLevels".
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty iterator."""

    @overload
    def __init__(self, aTreeNode: TDataStd_TreeNode | None, allLevels: bool = False) -> None:
        """
        Iterates on the ChildStepren of the given Step. If
        <allLevels> option is set to true, it explores not
        only the first, but all the sub Step levels.
        """

    @overload
    def __init__(self, theOther: TDataStd_ChildNodeIterator) -> None: ...

    def __iter__(self) -> TDataStd_ChildNodeIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> TDataStd_TreeNode:
        """Python addition: see __iter__."""

    def Initialize(self, aTreeNode: TDataStd_TreeNode | None, allLevels: bool = False) -> None:
        """
        Initializes the iteration on the Children Step of
        the given Step. If <allLevels> option is set to
        true, it explores not only the first, but all the
        sub Step levels.
        """

    def More(self) -> bool:
        """
        Returns True if there is a current Item in the
        iteration.
        """

    def Next(self) -> None:
        """Move to the next Item"""

    def NextBrother(self) -> None:
        """
        Move to the next Brother. If there is none, go up
        etc. This method is interesting only with
        "allLevels" behavior, because it avoids to explore
        the current Step ChildStepren.
        """

    def Value(self) -> TDataStd_TreeNode:
        """
        Returns the current item; a null Step if there is
        no one.
        """

class TDataStd_GenericExtString(nanoocp.TDF.TDF_Attribute):
    """
    An ancestor attribute for all attributes which have TCollection_ExtendedString field.
    If an attribute inherits this one it should not have drivers for persistence.
    Also this attribute provides functionality to have on the same label same attributes with
    different IDs.
    """

    def Set(self, S: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """Sets <S> as name. Raises if <S> is not a valid name."""

    def SetID(self, guid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit user defined GUID to the attribute."""

    def Get(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """Returns the name contained in this name attribute."""

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the attribute."""

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_Comment(TDataStd_GenericExtString):
    """
    Comment attribute. may be associated to any label
    to store user comment.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_Comment) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        Returns the GUID for comments.
        """

    @overload
    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label) -> TDataStd_Comment:
        """
        Find, or create a Comment attribute. the Comment
        attribute is returned.
        """

    @overload
    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, string: nanoocp.TCollection.TCollection_ExtendedString) -> TDataStd_Comment:
        """
        Finds, or creates a Comment attribute and sets the string.
        the Comment attribute is returned.
        Comment methods
        ============
        """

    def Set(self, S: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    @overload
    def SetID(self, guid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit user defined GUID to the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class TDataStd_Current(nanoocp.TDF.TDF_Attribute):
    """
    this attribute, located at root label, manage an
    access to a current label.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_Current) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        """

    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label) -> None:
        """Set <L> as current of <L> Framework."""

    @staticmethod
    def Get(acces: nanoocp.TDF.TDF_Label) -> nanoocp.TDF.TDF_Label:
        """returns current of <acces> Framework. raise if (!Has)"""

    @staticmethod
    def Has(acces: nanoocp.TDF.TDF_Label) -> bool:
        """
        returns True if a current label is managed in <acces>
        Framework.
        class methods
        =============
        """

    def SetLabel(self, current: nanoocp.TDF.TDF_Label) -> None: ...

    def GetLabel(self) -> nanoocp.TDF.TDF_Label: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_GenericEmpty(nanoocp.TDF.TDF_Attribute):
    """
    An ancestor attribute for all attributes which have no fields.
    If an attribute inherits this one it should not have drivers for persistence.
    """

    def Restore(self, arg0: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def Paste(self, arg0: nanoocp.TDF.TDF_Attribute | None, arg1: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_DeltaOnModificationOfByteArray(nanoocp.TDF.TDF_DeltaOnModification):
    """
    This class provides default services for an
    AttributeDelta on a MODIFICATION action.
    """

    @overload
    def __init__(self, Arr: TDataStd_ByteArray | None) -> None:
        """Initializes a TDF_DeltaOnModification."""

    @overload
    def __init__(self, theOther: TDataStd_DeltaOnModificationOfByteArray) -> None: ...

    def Apply(self) -> None:
        """Applies the delta to the attribute."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_DeltaOnModificationOfExtStringArray(nanoocp.TDF.TDF_DeltaOnModification):
    """
    This class provides default services for an
    AttributeDelta on a MODIFICATION action.
    """

    @overload
    def __init__(self, Arr: TDataStd_ExtStringArray | None) -> None:
        """Initializes a TDF_DeltaOnModification."""

    @overload
    def __init__(self, theOther: TDataStd_DeltaOnModificationOfExtStringArray) -> None: ...

    def Apply(self) -> None:
        """Applies the delta to the attribute."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_DeltaOnModificationOfIntArray(nanoocp.TDF.TDF_DeltaOnModification):
    """
    This class provides default services for an
    AttributeDelta on a MODIFICATION action.
    """

    @overload
    def __init__(self, Arr: TDataStd_IntegerArray | None) -> None:
        """Initializes a TDF_DeltaOnModification."""

    @overload
    def __init__(self, theOther: TDataStd_DeltaOnModificationOfIntArray) -> None: ...

    def Apply(self) -> None:
        """Applies the delta to the attribute."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_DeltaOnModificationOfIntPackedMap(nanoocp.TDF.TDF_DeltaOnModification):
    """
    This class provides default services for an
    AttributeDelta on a MODIFICATION action.
    """

    @overload
    def __init__(self, Arr: TDataStd_IntPackedMap | None) -> None:
        """Initializes a TDF_DeltaOnModification."""

    @overload
    def __init__(self, theOther: TDataStd_DeltaOnModificationOfIntPackedMap) -> None: ...

    def Apply(self) -> None:
        """Applies the delta to the attribute."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_DeltaOnModificationOfRealArray(nanoocp.TDF.TDF_DeltaOnModification):
    """
    This class provides default services for an
    AttributeDelta on a MODIFICATION action
    """

    @overload
    def __init__(self, Arr: TDataStd_RealArray | None) -> None:
        """Initializes a TDF_DeltaOnModification."""

    @overload
    def __init__(self, theOther: TDataStd_DeltaOnModificationOfRealArray) -> None: ...

    def Apply(self) -> None:
        """Applies the delta to the attribute."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_Directory(TDataStd_GenericEmpty):
    """
    Associates a directory in the data framework with
    a TDataStd_TagSource attribute.
    You can create a new directory label and add
    sub-directory or object labels to it,
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_Directory) -> None: ...

    @staticmethod
    def Find(current: nanoocp.TDF.TDF_Label) -> tuple[bool, TDataStd_Directory]:
        """
        class methods
        =============
        Searches for a directory attribute on the label
        current, or on one of the father labels of current.
        If a directory attribute is found, true is returned,
        and the attribute found is set as D.
        """

    @staticmethod
    def New(label: nanoocp.TDF.TDF_Label) -> TDataStd_Directory:
        """
        Creates an empty Directory attribute, located at
        <label>. Raises if <label> has attribute
        """

    @staticmethod
    def AddDirectory(dir: TDataStd_Directory | None) -> TDataStd_Directory:
        """
        Creates a new sub-label and sets the
        sub-directory dir on that label.
        """

    @staticmethod
    def MakeObjectLabel(dir: TDataStd_Directory | None) -> nanoocp.TDF.TDF_Label:
        """
        Makes new label and returns it to insert
        other object attributes (sketch,part...etc...)
        """

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        Directory methods
        ===============
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class TDataStd_Expression(nanoocp.TDF.TDF_Attribute):
    """
    Expression attribute.
    ====================

    * Data Structure of the Expression is stored in a
    string and references to variables used by the string

    Warning: To be consistent, each Variable referenced by the
    expression must have its equivalent in the string
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_Expression) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        """

    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label) -> TDataStd_Expression:
        """
        Find, or create, an Expression attribute.
        Expressionmethods
        ============
        """

    def Name(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """build and return the expression name"""

    def SetExpression(self, E: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    def GetExpression(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def GetVariables(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Attribute]: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_ExtStringArray(nanoocp.TDF.TDF_Attribute):
    """
    ExtStringArray Attribute. Handles an array of UNICODE strings (represented by the
    TCollection_ExtendedString class).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_ExtStringArray) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        Returns the GUID for the attribute.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, lower: int, upper: int, isDelta: bool = False) -> TDataStd_ExtStringArray:
        """
        Finds, or creates, an ExtStringArray attribute with <lower>
        and <upper> bounds on the specified label.
        If <isDelta> == False, DefaultDeltaOnModification is used.
        If <isDelta> == True, DeltaOnModification of the current attribute is used.
        If attribute is already set, all input parameters are refused and the found
        attribute is returned.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, theGuid: nanoocp.Standard.Standard_GUID, lower: int, upper: int, isDelta: bool = False) -> TDataStd_ExtStringArray:
        """
        Finds, or creates, an ExtStringArray attribute with explicit user defined <guid>.
        The ExtStringArray attribute is returned.
        """

    def Init(self, lower: int, upper: int) -> None:
        """Initializes the inner array with bounds from <lower> to <upper>"""

    def SetValue(self, Index: int, Value: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Sets the <Index>th element of the array to <Value>
        OutOfRange exception is raised if <Index> doesn't respect Lower and Upper bounds of the
        internal array.
        """

    @overload
    def SetID(self, theGuid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit GUID (user defined) for the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    def Value(self, Index: int) -> nanoocp.TCollection.TCollection_ExtendedString:
        """Returns the value of the <Index>th element of the array"""

    def __call__(self, Index: int) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def Lower(self) -> int:
        """Return the lower bound."""

    def Upper(self) -> int:
        """Return the upper bound"""

    def Length(self) -> int:
        """Return the number of elements of <me>."""

    def ChangeArray(self, newArray: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_ExtendedString] | None, isCheckItems: bool = True) -> None:
        """
        Sets the inner array <myValue> of the ExtStringArray attribute to <newArray>.
        If value of <newArray> differs from <myValue>, Backup performed and myValue
        refers to new instance of HArray1OfExtendedString that holds <newArray> values
        If <isCheckItems> equal True each item of <newArray> will be checked with each
        item of <myValue> for coincidence (to avoid backup).
        """

    def Array(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_ExtendedString]:
        """Return the inner array of the ExtStringArray attribute"""

    def GetDelta(self) -> bool: ...

    def SetDelta(self, isDelta: bool) -> None:
        """for internal use only!"""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DeltaOnModification(self, anOldAttribute: nanoocp.TDF.TDF_Attribute | None) -> nanoocp.TDF.TDF_DeltaOnModification:
        """
        Makes a DeltaOnModification between <me> and
        <anOldAttribute>.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class TDataStd_ExtStringList(nanoocp.TDF.TDF_Attribute):
    """Contains a list of ExtendedString."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_ExtStringList) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        Static methods
        ==============
        Returns the ID of the list of strings attribute.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label) -> TDataStd_ExtStringList:
        """
        Finds or creates a list of string values attribute with explicit user defined <guid>.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, theGuid: nanoocp.Standard.Standard_GUID) -> TDataStd_ExtStringList:
        """Finds or creates a list of string values attribute."""

    def IsEmpty(self) -> bool: ...

    def Extent(self) -> int: ...

    def Prepend(self, value: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    def Append(self, value: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    @overload
    def SetID(self, theGuid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit GUID (user defined) for the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    @overload
    def InsertBefore(self, value: nanoocp.TCollection.TCollection_ExtendedString, before_value: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """Inserts the <value> before the first meet of <before_value>."""

    @overload
    def InsertBefore(self, index: int, before_value: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        Inserts the <value> before the <index> position.
        The indices start with 1 .. Extent().
        """

    @overload
    def InsertAfter(self, value: nanoocp.TCollection.TCollection_ExtendedString, after_value: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """Inserts the <value> after the first meet of <after_value>."""

    @overload
    def InsertAfter(self, index: int, after_value: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        Inserts the <value> after the <index> position.
        The indices start with 1 .. Extent().
        """

    @overload
    def Remove(self, value: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """Removes the first meet of the <value>."""

    @overload
    def Remove(self, index: int) -> bool:
        """Removes a value at <index> position."""

    def Clear(self) -> None: ...

    def First(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def Last(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def List(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_ExtendedString]: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_HDataMapOfStringByte(nanoocp.Standard.Standard_Transient):
    """
    Extension of NCollection_DataMap<TCollection_ExtendedString, uint8_t> class
    to be manipulated by handle.
    """

    @overload
    def __init__(self, NbBuckets: int = 1) -> None: ...

    @overload
    def __init__(self, theOther: nanoocp.NCollection.NCollection_DataMap__TCollection_ExtendedString__unsigned_char) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_HDataMapOfStringByte) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Map(self) -> nanoocp.NCollection.NCollection_DataMap__TCollection_ExtendedString__unsigned_char: ...

    def ChangeMap(self) -> nanoocp.NCollection.NCollection_DataMap__TCollection_ExtendedString__unsigned_char: ...

class TDataStd_HDataMapOfStringHArray1OfInteger(nanoocp.Standard.Standard_Transient):
    """
    Extension of NCollection_DataMap<TCollection_ExtendedString,
    occ::handle<NCollection_HArray1<int>>> class to be manipulated by handle.
    """

    @overload
    def __init__(self, NbBuckets: int = 1) -> None: ...

    @overload
    def __init__(self, theOther: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.NCollection.NCollection_HArray1[int]]) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_HDataMapOfStringHArray1OfInteger) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Map(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.NCollection.NCollection_HArray1[int]]: ...

    def ChangeMap(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.NCollection.NCollection_HArray1[int]]: ...

class TDataStd_HDataMapOfStringHArray1OfReal(nanoocp.Standard.Standard_Transient):
    """
    Extension of NCollection_DataMap<TCollection_ExtendedString,
    occ::handle<NCollection_HArray1<double>>> class to be manipulated by handle.
    """

    @overload
    def __init__(self, NbBuckets: int = 1) -> None: ...

    @overload
    def __init__(self, theOther: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.NCollection.NCollection_HArray1[float]]) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_HDataMapOfStringHArray1OfReal) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Map(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.NCollection.NCollection_HArray1[float]]: ...

    def ChangeMap(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.NCollection.NCollection_HArray1[float]]: ...

class TDataStd_HDataMapOfStringInteger(nanoocp.Standard.Standard_Transient):
    """
    Extension of NCollection_DataMap<TCollection_ExtendedString, int> class
    to be manipulated by handle.
    """

    @overload
    def __init__(self, NbBuckets: int = 1) -> None: ...

    @overload
    def __init__(self, theOther: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, int]) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_HDataMapOfStringInteger) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Map(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, int]: ...

    def ChangeMap(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, int]: ...

class TDataStd_HDataMapOfStringReal(nanoocp.Standard.Standard_Transient):
    """
    Extension of NCollection_DataMap<TCollection_ExtendedString, double> class
    to be manipulated by handle.
    """

    @overload
    def __init__(self, NbBuckets: int = 1) -> None: ...

    @overload
    def __init__(self, theOther: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, float]) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_HDataMapOfStringReal) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Map(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, float]: ...

    def ChangeMap(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, float]: ...

class TDataStd_HDataMapOfStringString(nanoocp.Standard.Standard_Transient):
    """
    Extension of NCollection_DataMap<TCollection_ExtendedString, TCollection_ExtendedString> class
    to be manipulated by handle.
    """

    @overload
    def __init__(self, NbBuckets: int = 1) -> None: ...

    @overload
    def __init__(self, theOther: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.TCollection.TCollection_ExtendedString]) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_HDataMapOfStringString) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Map(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.TCollection.TCollection_ExtendedString]: ...

    def ChangeMap(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.TCollection.TCollection_ExtendedString]: ...

class TDataStd_Integer(nanoocp.TDF.TDF_Attribute):
    """The basis to define an integer attribute."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_Integer) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        Returns the GUID for integers.
        """

    @overload
    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, value: int) -> TDataStd_Integer:
        """
        Finds, or creates, an Integer attribute and sets <value>
        the Integer attribute is returned.
        """

    @overload
    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, guid: nanoocp.Standard.Standard_GUID, value: int) -> TDataStd_Integer:
        """
        Finds, or creates, an Integer attribute with explicit user defined <guid> and sets <value>.
        The Integer attribute is returned.
        """

    def Set(self, V: int) -> None:
        """
        Integer methods
        ===============
        """

    @overload
    def SetID(self, guid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit GUID (user defined) for the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    def Get(self) -> int:
        """Returns the integer value contained in the attribute."""

    def IsCaptured(self) -> bool:
        """Returns True if there is a reference on the same label"""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_IntegerArray(nanoocp.TDF.TDF_Attribute):
    """Contains an array of integers."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_IntegerArray) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        Returns the GUID for arrays of integers.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, lower: int, upper: int, isDelta: bool = False) -> TDataStd_IntegerArray:
        """
        Finds or creates on the <label> an integer array attribute
        with the specified <lower> and <upper> boundaries.
        If <isDelta> == False, DefaultDeltaOnModification is used.
        If <isDelta> == True, DeltaOnModification of the current attribute is used.
        If attribute is already set, all input parameters are refused and the found
        attribute is returned.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, theGuid: nanoocp.Standard.Standard_GUID, lower: int, upper: int, isDelta: bool = False) -> TDataStd_IntegerArray:
        """
        Finds, or creates, an IntegerArray attribute with explicit user defined <guid>.
        The IntegerArray attribute is returned.
        """

    def Init(self, lower: int, upper: int) -> None:
        """Initialize the inner array with bounds from <lower> to <upper>"""

    def SetValue(self, Index: int, Value: int) -> None:
        """
        Sets the <Index>th element of the array to <Value>
        OutOfRange exception is raised if <Index> doesn't respect Lower and Upper bounds
        of the internal array.
        """

    @overload
    def SetID(self, theGuid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit GUID (user defined) for the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    def Value(self, Index: int) -> int:
        """Return the value of the <Index>th element of the array"""

    def __call__(self, Index: int) -> int: ...

    def Lower(self) -> int:
        """Returns the lower boundary of this array of integers."""

    def Upper(self) -> int:
        """Return the upper boundary of this array of integers."""

    def Length(self) -> int:
        """
        Returns the length of this array of integers in
        terms of the number of elements it contains.
        """

    def ChangeArray(self, newArray: nanoocp.NCollection.NCollection_HArray1[int] | None, isCheckItems: bool = True) -> None:
        """
        Sets the inner array <myValue> of the IntegerArray attribute to
        <newArray>. If value of <newArray> differs from <myValue>, Backup performed
        and myValue refers to new instance of HArray1OfInteger that holds <newArray>
        values
        If <isCheckItems> equal True each item of <newArray> will be checked with each
        item of <myValue> for coincidence (to avoid backup).
        """

    def Array(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """Return the inner array of the IntegerArray attribute"""

    def GetDelta(self) -> bool: ...

    def SetDelta(self, isDelta: bool) -> None:
        """for internal use only!"""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None:
        """Note. Uses inside ChangeArray() method"""

    def Dump(self) -> str: ...

    def DeltaOnModification(self, anOldAttribute: nanoocp.TDF.TDF_Attribute | None) -> nanoocp.TDF.TDF_DeltaOnModification:
        """
        Makes a DeltaOnModification between <me> and
        <anOldAttribute>.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class TDataStd_IntegerList(nanoocp.TDF.TDF_Attribute):
    """Contains a list of integers."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_IntegerList) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        Static methods
        ==============
        Returns the ID of the list of integer attribute.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label) -> TDataStd_IntegerList:
        """Finds or creates a list of integer values attribute."""

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, theGuid: nanoocp.Standard.Standard_GUID) -> TDataStd_IntegerList:
        """
        Finds or creates a list of integer values attribute with explicit user defined <guid>.
        """

    def IsEmpty(self) -> bool: ...

    def Extent(self) -> int: ...

    def Prepend(self, value: int) -> None: ...

    def Append(self, value: int) -> None: ...

    @overload
    def SetID(self, theGuid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit GUID (user defined) for the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    def InsertBefore(self, value: int, before_value: int) -> bool:
        """Inserts the <value> before the first meet of <before_value>."""

    def InsertBeforeByIndex(self, index: int, before_value: int) -> bool:
        """
        Inserts the <value> before the <index> position.
        The indices start with 1 .. Extent().
        """

    def InsertAfter(self, value: int, after_value: int) -> bool:
        """Inserts the <value> after the first meet of <after_value>."""

    def InsertAfterByIndex(self, index: int, after_value: int) -> bool:
        """
        Inserts the <value> after the <index> position.
        The indices start with 1 .. Extent().
        """

    def Remove(self, value: int) -> bool:
        """Removes the first meet of the <value>."""

    def RemoveByIndex(self, index: int) -> bool:
        """Removes a value at <index> position."""

    def Clear(self) -> None: ...

    def First(self) -> int: ...

    def Last(self) -> int: ...

    def List(self) -> nanoocp.NCollection.NCollection_List[int]: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_IntPackedMap(nanoocp.TDF.TDF_Attribute):
    """Attribute for storing TColStd_PackedMapOfInteger"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_IntPackedMap) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        Returns the GUID of the attribute.
        """

    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, isDelta: bool = False) -> TDataStd_IntPackedMap:
        """
        Finds or creates an integer map attribute on the given label.
        If <isDelta> == False, DefaultDeltaOnModification is used.
        If <isDelta> == True, DeltaOnModification of the current attribute is used.
        If attribute is already set, input parameter <isDelta> is refused and the found
        attribute returned.
        Attribute methods
        ===================
        """

    @overload
    def ChangeMap(self, theMap: nanoocp.TColStd.TColStd_HPackedMapOfInteger | None) -> bool: ...

    @overload
    def ChangeMap(self, theMap: nanoocp.TColStd.TColStd_PackedMapOfInteger) -> bool: ...

    def GetMap(self) -> nanoocp.TColStd.TColStd_PackedMapOfInteger: ...

    def GetHMap(self) -> nanoocp.TColStd.TColStd_HPackedMapOfInteger: ...

    def Clear(self) -> bool: ...

    def Add(self, theKey: int) -> bool: ...

    def Remove(self, theKey: int) -> bool: ...

    def Contains(self, theKey: int) -> bool: ...

    def Extent(self) -> int: ...

    def IsEmpty(self) -> bool: ...

    def GetDelta(self) -> bool: ...

    def SetDelta(self, isDelta: bool) -> None:
        """for internal use only!"""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DeltaOnModification(self, anOldAttribute: nanoocp.TDF.TDF_Attribute | None) -> nanoocp.TDF.TDF_DeltaOnModification:
        """
        Makes a DeltaOnModification between <me> and
        <anOldAttribute>.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class TDataStd_Name(TDataStd_GenericExtString):
    """
    Used to define a name attribute containing a string which specifies the name.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_Name) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods working on the name itself
        ========================================
        Returns the GUID for name attributes.
        """

    @overload
    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, string: nanoocp.TCollection.TCollection_ExtendedString) -> TDataStd_Name:
        """
        Creates (if does not exist) and sets the name in the name attribute.
        from any label <L> search in father labels (L is not
        concerned) the first name attribute. if found set it in
        <father>.
        class methods working on the name tree
        ======================================
        Search in the whole TDF_Data the Name attribute which
        fit with <fullPath>. Returns True if found.
        Search under <currentLabel> a label which fit with
        <name>. Returns True if found. Shortcut which avoids
        building a ListOfExtendedStrin.
        Search in the whole TDF_Data the label which fit with name
        Returns True if found.
        tools methods to translate path <-> pathlist
        ===========================================
        move to draw For Draw test we may provide this tool method which convert a path in a
        sequence of string to call after the FindLabel methods.
        Example: if it's given "Assembly:Part_1:Sketch_5" it will return in <pathlist>
        the list of 3 strings: "Assembly","Part_1","Sketch_5".
        move to draw from <pathlist> build the string path
        Name methods
        ============
        """

    @overload
    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, guid: nanoocp.Standard.Standard_GUID, string: nanoocp.TCollection.TCollection_ExtendedString) -> TDataStd_Name:
        """
        Finds, or creates, a Name attribute with explicit user defined <guid> and sets <string>.
        The Name attribute is returned.
        """

    def Set(self, S: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """Sets <S> as name. Raises if <S> is not a valid name."""

    @overload
    def SetID(self, guid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit user defined GUID to the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class TDataStd_NamedData(nanoocp.TDF.TDF_Attribute):
    """Contains a named data."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: TDataStd_NamedData) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the named data attribute."""

    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label) -> TDataStd_NamedData:
        """Finds or creates a named data attribute."""

    def HasIntegers(self) -> bool:
        """
        Returns true if at least one named integer value is kept in the attribute.
        """

    def HasInteger(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        Returns true if the attribute contains specified by Name
        integer value.
        """

    def GetInteger(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> int:
        """
        Returns the integer value specified by the Name.
        It returns 0 if internal map doesn't contain the specified
        integer (use HasInteger() to check before).
        """

    def SetInteger(self, theName: nanoocp.TCollection.TCollection_ExtendedString, theInteger: int) -> None:
        """
        Defines a named integer.
        If the integer already exists, it changes its value to <theInteger>.
        """

    def GetIntegersContainer(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, int]:
        """Returns the internal container of named integers."""

    def ChangeIntegers(self, theIntegers: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, int]) -> None:
        """Replace the container content by new content of the <theIntegers>."""

    def HasReals(self) -> bool:
        """
        Returns true if at least one named real value is kept in the attribute.
        """

    def HasReal(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """Returns true if the attribute contains a real specified by Name."""

    def GetReal(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> float:
        """
        Returns the named real.
        It returns 0.0 if there is no such a named real
        (use HasReal()).
        """

    def SetReal(self, theName: nanoocp.TCollection.TCollection_ExtendedString, theReal: float) -> None:
        """
        Defines a named real.
        If the real already exists, it changes its value to <theReal>.
        """

    def GetRealsContainer(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, float]:
        """Returns the internal container of named reals."""

    def ChangeReals(self, theReals: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, float]) -> None:
        """Replace the container content by new content of the <theReals>."""

    def HasStrings(self) -> bool:
        """Returns true if there are some named strings in the attribute."""

    def HasString(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """Returns true if the attribute contains this named string."""

    def GetString(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        Returns the named string.
        It returns an empty string if there is no such a named string
        (use HasString()).
        """

    def SetString(self, theName: nanoocp.TCollection.TCollection_ExtendedString, theString: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Defines a named string.
        If the string already exists, it changes its value to <theString>.
        """

    def GetStringsContainer(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.TCollection.TCollection_ExtendedString]:
        """Returns the internal container of named strings."""

    def ChangeStrings(self, theStrings: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.TCollection.TCollection_ExtendedString]) -> None:
        """Replace the container content by new content of the <theStrings>."""

    def HasBytes(self) -> bool:
        """Returns true if there are some named bytes in the attribute."""

    def HasByte(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """Returns true if the attribute contains this named byte."""

    def GetByte(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> int:
        """
        Returns the named byte.
        It returns 0 if there is no such a named byte
        (use HasByte()).
        """

    def SetByte(self, theName: nanoocp.TCollection.TCollection_ExtendedString, theByte: int) -> None:
        """
        Defines a named byte.
        If the byte already exists, it changes its value to <theByte>.
        """

    def GetBytesContainer(self) -> nanoocp.NCollection.NCollection_DataMap__TCollection_ExtendedString__unsigned_char:
        """Returns the internal container of named bytes."""

    def ChangeBytes(self, theBytes: nanoocp.NCollection.NCollection_DataMap__TCollection_ExtendedString__unsigned_char) -> None:
        """Replace the container content by new content of the <theBytes>."""

    def HasArraysOfIntegers(self) -> bool:
        """
        Returns true if there are some named arrays of integer values in the attribute.
        """

    def HasArrayOfIntegers(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        Returns true if the attribute contains this named array of integer values.
        """

    def GetArrayOfIntegers(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """
        Returns the named array of integer values.
        It returns a NULL Handle if there is no such a named array of integers
        (use HasArrayOfIntegers()).
        """

    def SetArrayOfIntegers(self, theName: nanoocp.TCollection.TCollection_ExtendedString, theArrayOfIntegers: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """
        Defines a named array of integer values.
        @param[in] theName  key
        @param[in] theArrayOfIntegers  new value, overrides existing (passed array will be copied by
        value!)
        """

    def GetArraysOfIntegersContainer(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.NCollection.NCollection_HArray1[int]]:
        """Returns the internal container of named arrays of integer values."""

    def ChangeArraysOfIntegers(self, theArraysOfIntegers: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.NCollection.NCollection_HArray1[int]]) -> None:
        """
        Replace the container content by new content of the <theArraysOfIntegers>.
        """

    def HasArraysOfReals(self) -> bool:
        """
        Returns true if there are some named arrays of real values in the attribute.
        """

    def HasArrayOfReals(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        Returns true if the attribute contains this named array of real values.
        """

    def GetArrayOfReals(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns the named array of real values.
        It returns a NULL Handle if there is no such a named array of reals
        (use HasArrayOfReals()).
        """

    def SetArrayOfReals(self, theName: nanoocp.TCollection.TCollection_ExtendedString, theArrayOfReals: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """
        Defines a named array of real values.
        @param[in] theName key
        @param[in] theArrayOfReals new value, overrides existing (passed array will be copied by
        value!)
        """

    def GetArraysOfRealsContainer(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.NCollection.NCollection_HArray1[float]]:
        """Returns the internal container of named arrays of real values."""

    def ChangeArraysOfReals(self, theArraysOfReals: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.NCollection.NCollection_HArray1[float]]) -> None:
        """
        Replace the container content by new content of the <theArraysOfReals>.
        """

    def Clear(self) -> None:
        """Clear data."""

    def HasDeferredData(self) -> bool:
        """
        @name late-load deferred data interface
        Returns TRUE if some data is not loaded from deferred storage and can be loaded using
        LoadDeferredData().

        Late-load interface allows to avoid loading auxiliary data into memory until it is needed by
        application and also speed up reader by skipping data chunks in file. This feature requires
        file format having special structure, and usually implies read-only access, therefore default
        implementation will return FALSE here.

        Late-load elements require special attention to ensure data consistency,
        as such elements are created in undefined state (no data) and Undo/Redo mechanism will not
        work until deferred data being loaded.

        Usage scenarios:
        - Application displays model in read-only way.
        Late-load elements are loaded temporarily on demand and immediately unloaded.
        theNamedData->LoadDeferredData (true);
        TCollection_AsciiString aValue = theNamedData->GetString (theKey);
        theNamedData->UnloadDeferredData();
        - Application saves the model into another format.
        All late-load elements should be loaded (at least temporary during operation).
        - Application modifies the model.
        Late-load element should be loaded with removed link to deferred storage,
        so that Undo()/Redo() will work as expected since loading.
        theNamedData->LoadDeferredData (false);
        theNamedData->SetString (theKey, theNewValue);
        """

    def LoadDeferredData(self, theToKeepDeferred: bool = False) -> bool:
        """
        Load data from deferred storage, without calling Backup().
        As result, the content of the object will be overridden by data from deferred storage (which
        is normally read-only).
        @param[in] theToKeepDeferred  when TRUE, the link to deferred storage will be preserved
        so that it will be possible calling UnloadDeferredData()
        afterwards for releasing memory
        @return FALSE if deferred storage is unavailable or deferred data has been already loaded
        """

    def UnloadDeferredData(self) -> bool:
        """
        Releases data if object has connected deferred storage, without calling Backup().
        WARNING! This operation does not unload modifications to deferred storage (normally it is
        read-only), so that modifications will be discarded (if any).
        @return FALSE if object has no deferred data
        """

    def clear(self) -> None:
        """Clear data without calling Backup()."""

    def setInteger(self, theName: nanoocp.TCollection.TCollection_ExtendedString, theInteger: int) -> None:
        """Defines a named integer (without calling Backup)."""

    def setReal(self, theName: nanoocp.TCollection.TCollection_ExtendedString, theReal: float) -> None:
        """Defines a named real (without calling Backup)."""

    def setString(self, theName: nanoocp.TCollection.TCollection_ExtendedString, theString: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """Defines a named string (without calling Backup)."""

    def setByte(self, theName: nanoocp.TCollection.TCollection_ExtendedString, theByte: int) -> None:
        """Defines a named byte (without calling Backup)."""

    def setArrayOfIntegers(self, theName: nanoocp.TCollection.TCollection_ExtendedString, theArrayOfIntegers: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """Defines a named array of integer values (without calling Backup)."""

    def setArrayOfReals(self, theName: nanoocp.TCollection.TCollection_ExtendedString, theArrayOfReals: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """Defines a named array of real values (without calling Backup)."""

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """@name TDF_Attribute interface"""

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_NoteBook(TDataStd_GenericEmpty):
    """NoteBook Object attribute"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_NoteBook) -> None: ...

    @staticmethod
    def Find(current: nanoocp.TDF.TDF_Label) -> tuple[bool, TDataStd_NoteBook]:
        """
        class methods
        =============
        try to retrieve a NoteBook attribute at <current> label
        or in fathers label of <current>. Returns True if
        found and set <N>.
        """

    @staticmethod
    def New(label: nanoocp.TDF.TDF_Label) -> TDataStd_NoteBook:
        """
        Create an enpty NoteBook attribute, located at
        <label>. Raises if <label> has attribute
        """

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        NoteBook methods
        ===============
        """

    @overload
    def Append(self, value: float, isExported: bool = False) -> TDataStd_Real:
        """
        Tool to Create an Integer attribute from <value>,
        Insert it in a new son label of <me>. The Real
        attribute is returned.
        """

    @overload
    def Append(self, value: int, isExported: bool = False) -> TDataStd_Integer:
        """
        Tool to Create an Real attribute from <value>, Insert
        it in a new son label of <me>. The Integer attribute
        is returned.
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class TDataStd_Real(nanoocp.TDF.TDF_Attribute):
    """The basis to define a real number attribute."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_Real) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        Returns the default GUID for real numbers.
        """

    @overload
    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, value: float) -> TDataStd_Real:
        """
        Finds, or creates, a Real attribute with default GUID and sets <value>.
        The Real attribute is returned. The Real dimension is Scalar by default.
        Use SetDimension to overwrite.
        Real methods
        ============
        """

    @overload
    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, guid: nanoocp.Standard.Standard_GUID, value: float) -> TDataStd_Real:
        """
        Finds, or creates, a Real attribute with explicit GUID and sets <value>.
        The Real attribute is returned.
        Real methods
        ============
        """

    def SetDimension(self, DIM: TDataStd_RealEnum) -> None:
        """
        Deprecated in OCCT: TDataStd_Real::SetDimension() is deprecated. Please avoid usage of this method.

        Obsolete method that will be removed in next versions.
        This field is not supported in the persistence mechanism.
        """

    def GetDimension(self) -> TDataStd_RealEnum:
        """
        Deprecated in OCCT: TDataStd_Real::GetDimension() is deprecated. Please avoid usage of this method.

        Obsolete method that will be removed in next versions.
        This field is not supported in the persistence mechanism.
        """

    def Set(self, V: float) -> None:
        """Sets the real number V."""

    @overload
    def SetID(self, guid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit GUID for the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    def Get(self) -> float:
        """Returns the real number value contained in the attribute."""

    def IsCaptured(self) -> bool:
        """Returns True if there is a reference on the same label"""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_RealArray(nanoocp.TDF.TDF_Attribute):
    """A framework for an attribute composed of a real number array."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_RealArray) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        Returns the GUID for arrays of reals.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, lower: int, upper: int, isDelta: bool = False) -> TDataStd_RealArray:
        """
        Finds or creates on the <label> a real array attribute with
        the specified <lower> and <upper> boundaries.
        If <isDelta> == False, DefaultDeltaOnModification is used.
        If <isDelta> == True, DeltaOnModification of the current attribute is used.
        If attribute is already set, input parameter <isDelta> is refused and the found
        attribute returned.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, theGuid: nanoocp.Standard.Standard_GUID, lower: int, upper: int, isDelta: bool = False) -> TDataStd_RealArray:
        """
        Finds, or creates, an RealArray attribute with explicit user defined <guid>.
        The RealArray attribute is returned.
        """

    def Init(self, lower: int, upper: int) -> None:
        """Initialize the inner array with bounds from <lower> to <upper>"""

    @overload
    def SetID(self, theGuid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit GUID (user defined) for the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    def SetValue(self, Index: int, Value: float) -> None:
        """
        Sets the <Index>th element of the array to <Value>
        OutOfRange exception is raised if <Index> doesn't respect Lower and Upper bounds of the
        internal array.
        """

    def Value(self, Index: int) -> float:
        """Return the value of the <Index>th element of the array"""

    def __call__(self, Index: int) -> float: ...

    def Lower(self) -> int:
        """Returns the lower boundary of the array."""

    def Upper(self) -> int:
        """Returns the upper boundary of the array."""

    def Length(self) -> int:
        """
        Returns the number of elements of the array of reals
        in terms of the number of elements it contains.
        """

    def ChangeArray(self, newArray: nanoocp.NCollection.NCollection_HArray1[float] | None, isCheckItems: bool = True) -> None:
        """
        Sets the inner array <myValue> of the RealArray attribute
        to <newArray>. If value of <newArray> differs from <myValue>,
        Backup performed and myValue refers to new instance of HArray1OfReal
        that holds <newArray> values
        If <isCheckItems> equal True each item of <newArray> will be checked with each
        item of <myValue> for coincidence (to avoid backup).
        """

    def Array(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """Returns the handle of this array of reals."""

    def GetDelta(self) -> bool: ...

    def SetDelta(self, isDelta: bool) -> None:
        """for internal use only!"""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None:
        """Note. Uses inside ChangeArray() method"""

    def Dump(self) -> str: ...

    def DeltaOnModification(self, anOldAttribute: nanoocp.TDF.TDF_Attribute | None) -> nanoocp.TDF.TDF_DeltaOnModification:
        """
        Makes a DeltaOnModification between <me> and
        <anOldAttribute>.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class TDataStd_RealList(nanoocp.TDF.TDF_Attribute):
    """Contains a list of doubles."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_RealList) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        Static methods
        ==============
        Returns the ID of the list of doubles attribute.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label) -> TDataStd_RealList:
        """Finds or creates a list of double values attribute."""

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, theGuid: nanoocp.Standard.Standard_GUID) -> TDataStd_RealList:
        """
        Finds or creates a list of double values attribute with explicit user defined <guid>.
        """

    def IsEmpty(self) -> bool: ...

    def Extent(self) -> int: ...

    def Prepend(self, value: float) -> None: ...

    def Append(self, value: float) -> None: ...

    @overload
    def SetID(self, theGuid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit GUID (user defined) for the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    def InsertBefore(self, value: float, before_value: float) -> bool:
        """Inserts the <value> before the first meet of <before_value>."""

    def InsertBeforeByIndex(self, index: int, before_value: float) -> bool:
        """
        Inserts the <value> before the <index> position.
        The indices start with 1 .. Extent().
        """

    def InsertAfter(self, value: float, after_value: float) -> bool:
        """Inserts the <value> after the first meet of <after_value>."""

    def InsertAfterByIndex(self, index: int, after_value: float) -> bool:
        """
        Inserts the <value> after the <index> position.
        The indices start with 1 .. Extent().
        """

    def Remove(self, value: float) -> bool:
        """Removes the first meet of the <value>."""

    def RemoveByIndex(self, index: int) -> bool:
        """Removes a value at <index> position."""

    def Clear(self) -> None: ...

    def First(self) -> float: ...

    def Last(self) -> float: ...

    def List(self) -> nanoocp.NCollection.NCollection_List[float]: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_ReferenceArray(nanoocp.TDF.TDF_Attribute):
    """Contains an array of references to the labels."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_ReferenceArray) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        Static methods
        ==============
        Returns the ID of the array of references (labels) attribute.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, lower: int, upper: int) -> TDataStd_ReferenceArray:
        """Finds or creates an array of reference values (labels) attribute."""

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, theGuid: nanoocp.Standard.Standard_GUID, lower: int, upper: int) -> TDataStd_ReferenceArray:
        """
        Finds or creates an array of reference values (labels) attribute with explicit user defined
        <guid>.
        """

    def Init(self, lower: int, upper: int) -> None:
        """Initialize the inner array with bounds from <lower> to <upper>"""

    def SetValue(self, index: int, value: nanoocp.TDF.TDF_Label) -> None:
        """
        Sets the <Index>th element of the array to <Value>
        OutOfRange exception is raised if <Index> doesn't respect Lower and Upper bounds of the
        internal array.
        """

    @overload
    def SetID(self, theGuid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit GUID (user defined) for the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    def Value(self, Index: int) -> nanoocp.TDF.TDF_Label:
        """Returns the value of the <Index>th element of the array."""

    def __call__(self, Index: int) -> nanoocp.TDF.TDF_Label: ...

    def Lower(self) -> int:
        """Returns the lower boundary of the array."""

    def Upper(self) -> int:
        """Returns the upper boundary of the array."""

    def Length(self) -> int:
        """Returns the number of elements in the array."""

    def InternalArray(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.TDF.TDF_Label]: ...

    def SetInternalArray(self, values: nanoocp.NCollection.NCollection_HArray1[nanoocp.TDF.TDF_Label] | None, isCheckItems: bool = True) -> None: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def References(self, DS: nanoocp.TDF.TDF_DataSet | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_ReferenceList(nanoocp.TDF.TDF_Attribute):
    """Contains a list of references."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_ReferenceList) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        Static methods
        ==============
        Returns the ID of the list of references (labels) attribute.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label) -> TDataStd_ReferenceList:
        """Finds or creates a list of reference values (labels) attribute."""

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, theGuid: nanoocp.Standard.Standard_GUID) -> TDataStd_ReferenceList:
        """
        Finds or creates a list of reference values (labels) attribute with explicit user defined
        <guid>.
        """

    def IsEmpty(self) -> bool: ...

    def Extent(self) -> int: ...

    def Prepend(self, value: nanoocp.TDF.TDF_Label) -> None: ...

    def Append(self, value: nanoocp.TDF.TDF_Label) -> None: ...

    @overload
    def SetID(self, theGuid: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the explicit GUID (user defined) for the attribute."""

    @overload
    def SetID(self) -> None:
        """Sets default GUID for the attribute."""

    @overload
    def InsertBefore(self, value: nanoocp.TDF.TDF_Label, before_value: nanoocp.TDF.TDF_Label) -> bool:
        """Inserts the <value> before the first meet of <before_value>."""

    @overload
    def InsertBefore(self, index: int, before_value: nanoocp.TDF.TDF_Label) -> bool:
        """
        Inserts the label before the <index> position.
        The indices start with 1 .. Extent().
        """

    @overload
    def InsertAfter(self, value: nanoocp.TDF.TDF_Label, after_value: nanoocp.TDF.TDF_Label) -> bool:
        """Inserts the <value> after the first meet of <after_value>."""

    @overload
    def InsertAfter(self, index: int, after_value: nanoocp.TDF.TDF_Label) -> bool:
        """
        Inserts the label after the <index> position.
        The indices start with 1 .. Extent().
        """

    @overload
    def Remove(self, value: nanoocp.TDF.TDF_Label) -> bool:
        """Removes the first meet of the <value>."""

    @overload
    def Remove(self, index: int) -> bool:
        """Removes a label at "index" position."""

    def Clear(self) -> None: ...

    def First(self) -> nanoocp.TDF.TDF_Label: ...

    def Last(self) -> nanoocp.TDF.TDF_Label: ...

    def List(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label]: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def References(self, DS: nanoocp.TDF.TDF_DataSet | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_Relation(TDataStd_Expression):
    """
    Relation attribute.
    ==================

    * Data Structure of the Expression is stored in a
    string and references to variables used by the string

    Warning: To be consistent, each Variable referenced by the
    relation must have its equivalent in the string
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_Relation) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        """

    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label) -> TDataStd_Relation:
        """
        Find, or create, an Relation attribute.
        Real methods
        ============
        """

    def SetRelation(self, E: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    def GetRelation(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class TDataStd_Tick(TDataStd_GenericEmpty):
    """
    Defines a boolean attribute.
    If it exists at a label - true,
    Otherwise - false.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_Tick) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        Static methods
        ==============
        """

    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label) -> TDataStd_Tick:
        """
        Find, or create, a Tick attribute.
        Tick methods
        ============
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class TDataStd_TreeNode(nanoocp.TDF.TDF_Attribute):
    """
    Allows you to define an explicit tree of labels
    which you can also edit.
    Without this class, the data structure cannot be fully edited.
    This service is required if for presentation
    purposes, you want to create an application with
    a tree which allows you to organize and link data
    as a function of application features.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_TreeNode) -> None: ...

    @staticmethod
    def Find(L: nanoocp.TDF.TDF_Label) -> tuple[bool, TDataStd_TreeNode]:
        """
        class methods working on the node
        =================================
        Returns true if the tree node T is found on the label L.
        Otherwise, false is returned.
        """

    @overload
    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label) -> TDataStd_TreeNode:
        """
        Finds or Creates a TreeNode attribute on the label <L>
        with the default tree ID, returned by the method
        <GetDefaultTreeID>. Returns the created/found TreeNode
        attribute.
        """

    @overload
    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label, ExplicitTreeID: nanoocp.Standard.Standard_GUID) -> TDataStd_TreeNode:
        """
        Finds or Creates a TreeNode attribute on the label
        <L>, with an explicit tree ID. <ExplicitTreeID> is
        the ID returned by <TDF_Attribute::ID> method.
        Returns the found/created TreeNode attribute.
        """

    @staticmethod
    def GetDefaultTreeID() -> nanoocp.Standard.Standard_GUID:
        """
        returns a default tree ID. this ID is used by the
        <Set> method without explicit tree ID.
        Instance methods:
        ================
        """

    def Append(self, Child: TDataStd_TreeNode | None) -> bool:
        """
        Insert the TreeNode <Child> as last child of <me>. If
        the insertion is successful <me> becomes the Father of <Child>.
        """

    def Prepend(self, Child: TDataStd_TreeNode | None) -> bool:
        """
        Insert the the TreeNode <Child> as first child of
        <me>. If the insertion is successful <me> becomes the Father of <Child>
        """

    def InsertBefore(self, Node: TDataStd_TreeNode | None) -> bool:
        """
        Inserts the TreeNode <Node> before <me>. If insertion is successful <me>
        and <Node> belongs to the same Father.
        """

    def InsertAfter(self, Node: TDataStd_TreeNode | None) -> bool:
        """
        Inserts the TreeNode <Node> after <me>. If insertion is successful <me>
        and <Node> belongs to the same Father.
        """

    def Remove(self) -> bool:
        """
        Removes this tree node attribute from its father
        node. The result is that this attribute becomes a root node.
        """

    def Depth(self) -> int:
        """
        Returns the depth of this tree node in the overall tree node structure.
        In other words, the number of father tree nodes of this one is returned.
        """

    def NbChildren(self, allLevels: bool = False) -> int:
        """
        Returns the number of child nodes.
        If <allLevels> is true, the method counts children of all levels
        (children of children ...)
        """

    def IsAscendant(self, of: TDataStd_TreeNode | None) -> bool:
        """
        Returns true if this tree node attribute is an
        ascendant of of. In other words, if it is a father or
        the father of a father of of.
        """

    def IsDescendant(self, of: TDataStd_TreeNode | None) -> bool:
        """
        Returns true if this tree node attribute is a
        descendant of of. In other words, if it is a child or
        the child of a child of of.
        """

    def IsRoot(self) -> bool:
        """
        Returns true if this tree node attribute is the
        ultimate father in the tree.
        """

    def Root(self) -> TDataStd_TreeNode:
        """Returns the ultimate father of this tree node attribute."""

    def IsFather(self, of: TDataStd_TreeNode | None) -> bool:
        """Returns true if this tree node attribute is a father of of."""

    def IsChild(self, of: TDataStd_TreeNode | None) -> bool:
        """Returns true if this tree node attribute is a child of of."""

    def HasFather(self) -> bool:
        """Returns true if this tree node attribute has a father tree node."""

    def Father(self) -> TDataStd_TreeNode:
        """Returns the father TreeNode of <me>. Null if root."""

    def HasNext(self) -> bool:
        """Returns true if this tree node attribute has a next tree node."""

    def Next(self) -> TDataStd_TreeNode:
        """
        Returns the next tree node in this tree node attribute.
        Warning
        This tree node is null if it is the last one in this
        tree node attribute.Returns the next TreeNode of <me>. Null if last.
        """

    def HasPrevious(self) -> bool:
        """Returns true if this tree node attribute has a previous tree node."""

    def Previous(self) -> TDataStd_TreeNode:
        """
        Returns the previous tree node of this tree node attribute.
        Warning
        This tree node is null if it is the first one in this tree node attribute.
        """

    def HasFirst(self) -> bool:
        """Returns true if this tree node attribute has a first child tree node."""

    def First(self) -> TDataStd_TreeNode:
        """Returns the first child tree node in this tree node object."""

    def HasLast(self) -> bool:
        """Returns true if this tree node attribute has a last child tree node."""

    def Last(self) -> TDataStd_TreeNode:
        """Returns the last child tree node in this tree node object."""

    def FindLast(self) -> TDataStd_TreeNode:
        """
        Returns the last child tree node in this tree node object.
        to set fields
        =============
        """

    def SetTreeID(self, explicitID: nanoocp.Standard.Standard_GUID) -> None: ...

    def SetFather(self, F: TDataStd_TreeNode | None) -> None: ...

    def SetNext(self, F: TDataStd_TreeNode | None) -> None: ...

    def SetPrevious(self, F: TDataStd_TreeNode | None) -> None: ...

    def SetFirst(self, F: TDataStd_TreeNode | None) -> None: ...

    def SetLast(self, F: TDataStd_TreeNode | None) -> None:
        """
        TreeNode callback:
        ==================
        """

    def AfterAddition(self) -> None:
        """Connect the TreeNode to its father child list"""

    def BeforeForget(self) -> None:
        """Disconnect the TreeNode from its Father child list"""

    def AfterResume(self) -> None:
        """Reconnect the TreeNode to its father child list."""

    def BeforeUndo(self, anAttDelta: nanoocp.TDF.TDF_AttributeDelta | None, forceIt: bool = False) -> bool:
        """Disconnect the TreeNode, if necessary."""

    def AfterUndo(self, anAttDelta: nanoocp.TDF.TDF_AttributeDelta | None, forceIt: bool = False) -> bool:
        """
        Reconnect the TreeNode, if necessary.
        Implementation of Attribute methods:
        ===================================
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """
        Returns the tree ID (default or explicit one depending on the Set method used).
        """

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def References(self, aDataSet: nanoocp.TDF.TDF_DataSet | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_UAttribute(nanoocp.TDF.TDF_Attribute):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_UAttribute) -> None: ...

    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, LocalID: nanoocp.Standard.Standard_GUID) -> TDataStd_UAttribute:
        """
        api class methods
        =============
        Find, or create, a UAttribute attribute with <LocalID> as Local GUID.
        The UAttribute attribute is returned.
        UAttribute methods
        ============
        """

    def SetID(self, LocalID: nanoocp.Standard.Standard_GUID) -> None: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def References(self, DS: nanoocp.TDF.TDF_DataSet | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataStd_Variable(nanoocp.TDF.TDF_Attribute):
    """
    Variable attribute.
    ==================

    * A variable is associated to a TDataStd_Real (which
    contains its current value) and a TDataStd_Name
    attribute (which contains its name). It contains a
    constant flag, and a Unit

    * An expression may be assigned to a variable. In
    thatcase the expression is handled by the associated
    Expression Attribute and the Variable returns True to
    the method <IsAssigned>.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataStd_Variable) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        """

    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label) -> TDataStd_Variable:
        """
        Find, or create, a Variable attribute.
        Real methods
        ============
        """

    @overload
    def Name(self, string: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        set or change the name of the variable, in myUnknown
        and my associated Name attribute.
        """

    @overload
    def Name(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        returns string stored in the associated Name
        attribute.
        """

    @overload
    def Set(self, value: float) -> None:
        """
        retrieve or create the associated real attribute and
        set the value <value>.
        """

    @overload
    def Set(self, value: float, dimension: TDataStd_RealEnum) -> None:
        """
        Deprecated in OCCT: TDataStd_Variable::Set(value, dimension) is deprecated. Please use TDataStd_Variable::Set(value) instead.

        Obsolete method that will be removed in next versions.
        The dimension argument is not supported in the persistence mechanism.
        """

    def IsValued(self) -> bool:
        """returns True if a Real attribute is associated."""

    def Get(self) -> float:
        """returns value stored in associated Real attribute."""

    def Real(self) -> TDataStd_Real:
        """returns associated Real attribute."""

    def IsAssigned(self) -> bool:
        """
        returns True if an Expression attribute is associated.
        create(if doesn't exist), set and returns the assigned
        expression attribute.
        """

    def Assign(self) -> TDataStd_Expression:
        """
        create(if doesn't exist) and returns the assigned
        expression attribute. fill it after.
        """

    def Desassign(self) -> None:
        """
        if <me> is assigned delete the associated expression
        attribute.
        """

    def Expression(self) -> TDataStd_Expression:
        """
        if <me> is assigned, returns associated Expression
        attribute.
        """

    def IsCaptured(self) -> bool:
        """shortcut for <Real()->IsCaptured()>"""

    def IsConstant(self) -> bool:
        """A constant value is not modified by regeneration."""

    @overload
    def Unit(self, unit: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    @overload
    def Unit(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        to read/write fields
        ====================
        """

    def Constant(self, status: bool) -> None:
        """
        if <status> is True, this variable will not be
        modified by the solver.
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def References(self, DS: nanoocp.TDF.TDF_DataSet | None) -> None:
        """to export reference to the associated Name attribute."""

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
TDataStd_HLabelArray1 = nanoocp.NCollection.NCollection_HArray1[nanoocp.TDF.TDF_Label]
TDataStd_LabelArray1 = nanoocp.NCollection.NCollection_Array1[nanoocp.TDF.TDF_Label]
TDataStd_ListOfByte = nanoocp.NCollection.NCollection_List__unsigned_char
TDataStd_ListOfExtendedString = nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_ExtendedString]
