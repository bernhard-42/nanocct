"""OCCT package XmlMDF (toolkit TKXmlL)"""

from typing import overload

import nanoocp.LDOM
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDF
import nanoocp.XmlObjMgt
import nanoocp.XmlMDF


class XmlMDF_ADriver(nanoocp.Standard.Standard_Transient):
    """Attribute Storage/Retrieval Driver."""

    def VersionNumber(self) -> int:
        """
        Returns the version number from which the driver
        is available.
        """

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """Creates a new attribute from TDF."""

    def SourceType(self) -> nanoocp.Standard.Standard_Type:
        """
        Returns the type of source object,
        inheriting from Attribute from TDF.
        """

    def TypeName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the full XML tag name (including NS prefix)"""

    def Namespace(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the namespace string"""

    @overload
    def Paste(self, aSource: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, aTarget: nanoocp.TDF.TDF_Attribute | None, aRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, aSource: nanoocp.TDF.TDF_Attribute | None, aTarget: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, aRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None:
        """
        Translate the contents of <aSource> and put it
        into <aTarget>, using the relocation table
        <aRelocTable> to keep the sharings.
        """

    def MessageDriver(self) -> nanoocp.Message.Message_Messenger:
        """Returns the current message driver of this driver"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlMDF:
    """
    This package provides classes and methods to
    translate a transient DF into a persistent one and
    vice versa.

    Driver

    A driver is a tool used to translate a transient
    attribute into a persistent one and vice versa.

    Driver Table

    A driver table is an object building links between
    object types and object drivers. In the
    translation process, a driver table is asked to
    give a translation driver for each current object
    to be translated.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XmlMDF) -> None: ...

    @overload
    @staticmethod
    def FromTo(aSource: nanoocp.TDF.TDF_Data | None, aTarget: nanoocp.LDOM.LDOM_Element, aReloc: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable, aDrivers: XmlMDF_ADriverTable | None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Translates a transient <aSource> into a persistent
        <aTarget>.
        """

    @overload
    @staticmethod
    def FromTo(aSource: nanoocp.LDOM.LDOM_Element, aReloc: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable, aDrivers: XmlMDF_ADriverTable | None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, nanoocp.TDF.TDF_Data]:
        """
        Translates a persistent <aSource> into a transient
        <aTarget>.
        Returns True if completed successfully (False on error)
        """

    @staticmethod
    def AddDrivers(aDriverTable: XmlMDF_ADriverTable | None, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None:
        """Adds the attribute storage drivers to <aDriverSeq>."""

class XmlMDF_ADriverTable(nanoocp.Standard.Standard_Transient):
    """
    A driver table is an object building links between
    object types and object drivers. In the
    translation process, a driver table is asked to
    give a translation driver for each current object
    to be translated.
    """

    @overload
    def __init__(self) -> None:
        """Creates a mutable ADriverTable from XmlMDF."""

    @overload
    def __init__(self, theOther: XmlMDF_ADriverTable) -> None: ...

    def AddDriver(self, anHDriver: XmlMDF_ADriver | None) -> None:
        """Sets a translation driver: <aDriver>."""

    @overload
    def AddDerivedDriver(self, theInstance: nanoocp.TDF.TDF_Attribute | None) -> None:
        """
        Adds a translation driver for the derived attribute. The base driver must be already added.
        @param theInstance is newly created attribute, detached from any label
        """

    @overload
    def AddDerivedDriver(self, theDerivedType: str) -> nanoocp.Standard.Standard_Type:
        """
        Adds a translation driver for the derived attribute. The base driver must be already added.
        @param theDerivedType is registered attribute type using IMPLEMENT_DERIVED_ATTRIBUTE macro
        """

    def CreateDrvMap(self, theDriverMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.XmlMDF.XmlMDF_ADriver]) -> None:
        """Fills the map by all registered drivers."""

    def GetDriver(self, theType: nanoocp.Standard.Standard_Type | None) -> tuple[bool, XmlMDF_ADriver]:
        """
        Gets a driver <aDriver> according to <aType>

        Returns True if a driver is found; false otherwise.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlMDF_ReferenceDriver(XmlMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMDF_ReferenceDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, Source: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, Target: nanoocp.TDF.TDF_Attribute | None, RelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, Source: nanoocp.TDF.TDF_Attribute | None, Target: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, RelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlMDF_TagSourceDriver(XmlMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMDF_TagSourceDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, Source: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, Target: nanoocp.TDF.TDF_Attribute | None, RelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, Source: nanoocp.TDF.TDF_Attribute | None, Target: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, RelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlMDF_DerivedDriver(XmlMDF_ADriver):
    """
    A universal driver for the attribute that inherits another attribute with
    ready to used persistence mechanism implemented (already has a driver to store/retrieve).
    """

    @overload
    def __init__(self, theDerivative: nanoocp.TDF.TDF_Attribute | None, theBaseDriver: XmlMDF_ADriver | None) -> None:
        """
        Creates a derivative persistence driver for theDerivative attribute by reusage of
        theBaseDriver
        @param theDerivative an instance of the attribute, just created, detached from any label
        @param theBaseDriver a driver of the base attribute, called by Paste methods
        """

    @overload
    def __init__(self, theOther: XmlMDF_DerivedDriver) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """Creates a new instance of the derivative attribute"""

    def TypeName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the full XML tag name (including NS prefix)"""

    @overload
    def Paste(self, theSource: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool:
        """Reuses the base driver to read the base fields"""

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None:
        """Reuses the base driver to store the base fields"""
