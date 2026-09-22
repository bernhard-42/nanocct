"""OCCT package BinMDF (toolkit TKBinL)"""

from typing import overload

import nanoocp.BinObjMgt
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDF


class BinMDF:
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
    def __init__(self, theOther: BinMDF) -> None: ...

    @staticmethod
    def AddDrivers(aDriverTable: BinMDF_ADriverTable | None, aMsgDrv: nanoocp.Message.Message_Messenger | None) -> None:
        """Adds the attribute storage drivers to <aDriverTable>."""

class BinMDF_ADriver(nanoocp.Standard.Standard_Transient):
    """Attribute Storage/Retrieval Driver."""

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """Creates a new attribute from TDF."""

    def SourceType(self) -> nanoocp.Standard.Standard_Type:
        """
        Returns the type of source object,
        inheriting from Attribute from TDF.
        """

    def TypeName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the type name of the attribute object"""

    @overload
    def Paste(self, aSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, aTarget: nanoocp.TDF.TDF_Attribute | None, aRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, aSource: nanoocp.TDF.TDF_Attribute | None, aTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, aRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None:
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

class BinMDF_ADriverTable(nanoocp.Standard.Standard_Transient):
    """
    A driver table is an object building links between
    object types and object drivers. In the
    translation process, a driver table is asked to
    give a translation driver for each current object
    to be translated.
    """

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BinMDF_ADriverTable) -> None: ...

    def AddDriver(self, theDriver: BinMDF_ADriver | None) -> None:
        """Adds a translation driver <theDriver>."""

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

    @overload
    def AssignIds(self, theTypes: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None:
        """
        Assigns the IDs to the drivers of the given Types.
        It uses indices in the map as IDs.
        Useful in storage procedure.
        """

    @overload
    def AssignIds(self, theTypeNames: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Assigns the IDs to the drivers of the given Type Names;
        It uses indices in the sequence as IDs.
        Useful in retrieval procedure.
        """

    @overload
    def GetDriver(self, theType: nanoocp.Standard.Standard_Type | None) -> tuple[int, BinMDF_ADriver]:
        """
        Gets a driver <theDriver> according to <theType>.
        Returns Type ID if the driver was assigned an ID; 0 otherwise.
        """

    @overload
    def GetDriver(self, theTypeId: int) -> BinMDF_ADriver:
        """
        Returns a driver according to <theTypeId>.
        Returns null handle if a driver is not found
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMDF_ReferenceDriver(BinMDF_ADriver):
    """Reference attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMDF_ReferenceDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, Source: nanoocp.BinObjMgt.BinObjMgt_Persistent, Target: nanoocp.TDF.TDF_Attribute | None, RelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, Source: nanoocp.TDF.TDF_Attribute | None, Target: nanoocp.BinObjMgt.BinObjMgt_Persistent, RelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMDF_TagSourceDriver(BinMDF_ADriver):
    """TDF_TagSource Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMDF_TagSourceDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, Source: nanoocp.BinObjMgt.BinObjMgt_Persistent, Target: nanoocp.TDF.TDF_Attribute | None, RelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, Source: nanoocp.TDF.TDF_Attribute | None, Target: nanoocp.BinObjMgt.BinObjMgt_Persistent, RelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMDF_DerivedDriver(BinMDF_ADriver):
    """
    A universal driver for the attribute that inherits another attribute with
    ready to used persistence mechanism implemented (already has a driver to store/retrieve).
    """

    @overload
    def __init__(self, theDerivative: nanoocp.TDF.TDF_Attribute | None, theBaseDriver: BinMDF_ADriver | None) -> None:
        """
        Creates a derivative persistence driver for theDerivative attribute by reusage of
        theBaseDriver
        @param theDerivative an instance of the attribute, just created, detached from any label
        @param theBaseDriver a driver of the base attribute, called by Paste methods
        """

    @overload
    def __init__(self, theOther: BinMDF_DerivedDriver) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """Creates a new instance of the derivative attribute"""

    @overload
    def Paste(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool:
        """Reuses the base driver to read the base fields"""

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None:
        """Reuses the base driver to store the base fields"""
