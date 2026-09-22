"""OCCT package XmlObjMgt (toolkit TKXmlL)"""

from typing import overload

import nanoocp.LDOM
import nanoocp.NCollection
import nanoocp.Storage
import nanoocp.TCollection
import nanoocp.gp
import nanoocp.Standard


class XmlObjMgt:
    """
    This package defines services to manage the storage
    grain of data produced by applications and those classes
    to manage persistent extern reference.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XmlObjMgt) -> None: ...

    @staticmethod
    def IdString() -> nanoocp.LDOM.LDOMString:
        """Define the name of XMLattribute 'ID' (to be used everywhere)"""

    @staticmethod
    def SetExtendedString(theElement: nanoocp.LDOM.LDOM_Element, theString: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """Add attribute <theElement extstring="theString" ...>"""

    @staticmethod
    def GetExtendedString(theElement: nanoocp.LDOM.LDOM_Element, theString: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """Get attribute <theElement extstring="theString" ...>"""

    @staticmethod
    def GetStringValue(theElement: nanoocp.LDOM.LDOM_Element) -> nanoocp.LDOM.LDOMString:
        """Returns the first child text node"""

    @staticmethod
    def SetStringValue(theElement: nanoocp.LDOM.LDOM_Element, theData: nanoocp.LDOM.LDOMString, isClearText: bool = False) -> None:
        """
        Add theData as the last child text node to theElement
        isClearText(True) avoids analysis of the string and replacement
        of characters like '<' and '&' during XML file storage.
        Do NEVER set isClearText unless you have a hell of a reason
        """

    @staticmethod
    def GetTagEntryString(theTarget: nanoocp.LDOM.LDOMString, theTagEntry: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Convert XPath expression (DOMString) into TagEntry string
        returns False on Error
        """

    @staticmethod
    def SetTagEntryString(theSource: nanoocp.LDOM.LDOMString, theTagEntry: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Convert XPath expression (DOMString) into TagEntry string
        returns False on Error
        """

    @staticmethod
    def FindChildElement(theSource: nanoocp.LDOM.LDOM_Element, theObjId: int) -> nanoocp.LDOM.LDOM_Element: ...

    @staticmethod
    def FindChildByRef(theSource: nanoocp.LDOM.LDOM_Element, theRefName: nanoocp.LDOM.LDOMString) -> nanoocp.LDOM.LDOM_Element: ...

    @staticmethod
    def FindChildByName(theSource: nanoocp.LDOM.LDOM_Element, theName: nanoocp.LDOM.LDOMString) -> nanoocp.LDOM.LDOM_Element: ...

    @staticmethod
    def GetReal(theString: nanoocp.LDOM.LDOMString) -> tuple[bool, float]: ...

class XmlObjMgt_Array1:
    """
    The class Array1 represents unidimensional
    array of fixed size known at run time.
    The range of the index is user defined.
    Warning: Programs clients of such class must be independent
    of the range of the first element. Then, a C++ for
    loop must be written like this
    for (i = A->Lower(); i <= A->Upper(); i++)
    """

    @overload
    def __init__(self, Low: int, Up: int) -> None:
        """
        Create an array of lower bound <Low> and
        upper bound <Up>. Range error is raised
        when <Up> is less than <Low>.
        """

    @overload
    def __init__(self, theParent: nanoocp.LDOM.LDOM_Element, theName: nanoocp.LDOM.LDOMString) -> None:
        """
        for restoration from DOM_Element which is child of
        theParent:
        <theParent ...>
        <theName ...>
        """

    @overload
    def __init__(self, theOther: XmlObjMgt_Array1) -> None: ...

    def CreateArrayElement(self, theParent: nanoocp.LDOM.LDOM_Element, theName: nanoocp.LDOM.LDOMString) -> None:
        """Create DOM_Element representing the array, under 'theParent'"""

    def Element(self) -> nanoocp.LDOM.LDOM_Element:
        """Returns the DOM element of <me>."""

    def Length(self) -> int:
        """Returns the number of elements of <me>."""

    def Lower(self) -> int:
        """Returns the lower bound."""

    def Upper(self) -> int:
        """Returns the upper bound."""

    def SetValue(self, Index: int, Value: nanoocp.LDOM.LDOM_Element) -> None:
        """Set the <Index>th element of the array to <Value>."""

    def Value(self, Index: int) -> nanoocp.LDOM.LDOM_Element:
        """Returns the value of <Index>th element of the array."""

class XmlObjMgt_GP:
    """Translation of gp (simple geometry) objects"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XmlObjMgt_GP) -> None: ...

    @overload
    @staticmethod
    def Translate(aTrsf: nanoocp.gp.gp_Trsf) -> nanoocp.LDOM.LDOMString: ...

    @overload
    @staticmethod
    def Translate(aMat: nanoocp.gp.gp_Mat) -> nanoocp.LDOM.LDOMString: ...

    @overload
    @staticmethod
    def Translate(anXYZ: nanoocp.gp.gp_XYZ) -> nanoocp.LDOM.LDOMString: ...

    @overload
    @staticmethod
    def Translate(aStr: nanoocp.LDOM.LDOMString, T: nanoocp.gp.gp_Trsf) -> bool: ...

    @overload
    @staticmethod
    def Translate(aStr: nanoocp.LDOM.LDOMString, T: nanoocp.gp.gp_Mat) -> bool: ...

    @overload
    @staticmethod
    def Translate(aStr: nanoocp.LDOM.LDOMString, T: nanoocp.gp.gp_XYZ) -> bool: ...

class XmlObjMgt_Persistent:
    """root for XML-persistence"""

    @overload
    def __init__(self) -> None:
        """empty constructor"""

    @overload
    def __init__(self, theElement: nanoocp.LDOM.LDOM_Element) -> None:
        """constructor"""

    @overload
    def __init__(self, theElement: nanoocp.LDOM.LDOM_Element, theRef: nanoocp.LDOM.LDOMString) -> None:
        """constructor from sub-element of Element referenced by theRef"""

    @overload
    def __init__(self, theOther: XmlObjMgt_Persistent) -> None: ...

    def CreateElement(self, theParent: nanoocp.LDOM.LDOM_Element, theType: nanoocp.LDOM.LDOMString, theID: int) -> None:
        """myElement := <theType id="theID"/>"""

    def SetId(self, theId: int) -> None: ...

    def Element(self) -> nanoocp.LDOM.LDOM_Element:
        """return myElement"""

    def Id(self) -> int: ...

class XmlObjMgt_RRelocationTable(nanoocp.NCollection.NCollection_DataMap[int, nanoocp.Standard.Standard_Transient]):
    """
    Retrieval relocation table is modeled as a child class of
    NCollection_DataMap<int, occ::handle<Standard_Transient>> that stores a handle to the file
    header section. With that attribute drivers have access to the file header
    section.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XmlObjMgt_RRelocationTable) -> None: ...

    def GetHeaderData(self) -> nanoocp.Storage.Storage_HeaderData:
        """Returns a handle to the header data of the file that is begin read"""

    def SetHeaderData(self, theHeaderData: nanoocp.Storage.Storage_HeaderData | None) -> None:
        """
        Sets the storage header data.

        @param theHeaderData header data of the file that is begin read
        """

    def Clear(self, doReleaseMemory: bool = True) -> None: ...

class XmlObjMgt_SRelocationTable(nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]):
    """
    Stored relocation table is modeled as a child class of
    NCollection_DataMap<int, occ::handle<Standard_Transient>> that stores a handle to the file
    header section. With that attribute drivers have access to the file header
    section.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XmlObjMgt_SRelocationTable) -> None: ...

    def GetHeaderData(self) -> nanoocp.Storage.Storage_HeaderData:
        """Returns a handle to the header data of the file that is begin read"""

    def SetHeaderData(self, theHeaderData: nanoocp.Storage.Storage_HeaderData | None) -> None:
        """
        Sets the storage header data.

        @param theHeaderData header data of the file that is begin read
        """

    def Clear(self, doReleaseMemory: bool = True) -> None: ...

# C++ typedef aliases
XmlObjMgt_DOMString = nanoocp.LDOM.LDOMString
XmlObjMgt_Element = nanoocp.LDOM.LDOM_Element
XmlObjMgt_Document = nanoocp.LDOM.LDOM_Document
