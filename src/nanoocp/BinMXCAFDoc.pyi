"""OCCT package BinMXCAFDoc (toolkit TKBinXCAF)"""

from typing import overload

import nanoocp.BinMDF
import nanoocp.BinMNaming
import nanoocp.BinObjMgt
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TDF
import nanoocp.TopLoc


class BinMXCAFDoc:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BinMXCAFDoc) -> None: ...

    @staticmethod
    def AddDrivers(theDriverTable: nanoocp.BinMDF.BinMDF_ADriverTable | None, theMsgDrv: nanoocp.Message.Message_Messenger | None) -> None:
        """Adds the attribute drivers to <theDriverTable>."""

class BinMXCAFDoc_AssemblyItemRefDriver(nanoocp.BinMDF.BinMDF_ADriver):
    @overload
    def __init__(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMXCAFDoc_AssemblyItemRefDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMXCAFDoc_CentroidDriver(nanoocp.BinMDF.BinMDF_ADriver):
    @overload
    def __init__(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMXCAFDoc_CentroidDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMXCAFDoc_ColorDriver(nanoocp.BinMDF.BinMDF_ADriver):
    @overload
    def __init__(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMXCAFDoc_ColorDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMXCAFDoc_DatumDriver(nanoocp.BinMDF.BinMDF_ADriver):
    @overload
    def __init__(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMXCAFDoc_DatumDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMXCAFDoc_DimTolDriver(nanoocp.BinMDF.BinMDF_ADriver):
    @overload
    def __init__(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMXCAFDoc_DimTolDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMXCAFDoc_GraphNodeDriver(nanoocp.BinMDF.BinMDF_ADriver):
    @overload
    def __init__(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMXCAFDoc_GraphNodeDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMXCAFDoc_LengthUnitDriver(nanoocp.BinMDF.BinMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMXCAFDoc_LengthUnitDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMXCAFDoc_LocationDriver(nanoocp.BinMDF.BinMDF_ADriver):
    @overload
    def __init__(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMXCAFDoc_LocationDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    @overload
    def Translate(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theLoc: nanoocp.TopLoc.TopLoc_Location, theMap: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Translate(self, theLoc: nanoocp.TopLoc.TopLoc_Location, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theMap: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None:
        """Translate transient location to storable"""

    def SetNSDriver(self, theNSDriver: nanoocp.BinMNaming.BinMNaming_NamedShapeDriver | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMXCAFDoc_MaterialDriver(nanoocp.BinMDF.BinMDF_ADriver):
    @overload
    def __init__(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMXCAFDoc_MaterialDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMXCAFDoc_NoteDriver(nanoocp.BinMDF.BinMDF_ADriver):
    @overload
    def Paste(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMXCAFDoc_NoteCommentDriver(BinMXCAFDoc_NoteDriver):
    @overload
    def __init__(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMXCAFDoc_NoteCommentDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMXCAFDoc_NoteBinDataDriver(BinMXCAFDoc_NoteDriver):
    @overload
    def __init__(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMXCAFDoc_NoteBinDataDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMXCAFDoc_VisMaterialDriver(nanoocp.BinMDF.BinMDF_ADriver):
    """Binary persistence driver for XCAFDoc_VisMaterial attribute."""

    @overload
    def __init__(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: BinMXCAFDoc_VisMaterialDriver) -> None: ...

    MaterialVersionMajor_1: int = 1

    MaterialVersionMinor_0: int = 0

    MaterialVersionMinor_1: int = 1

    MaterialVersionMajor: int = 1

    MaterialVersionMinor: int = 1

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """Create new instance of XCAFDoc_VisMaterial."""

    @overload
    def Paste(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool:
        """Paste attribute from persistence into document."""

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None:
        """Paste attribute from document into persistence."""

class BinMXCAFDoc_VisMaterialToolDriver(nanoocp.BinMDF.BinMDF_ADriver):
    """Binary persistence driver for XCAFDoc_VisMaterialTool attribute."""

    @overload
    def __init__(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: BinMXCAFDoc_VisMaterialToolDriver) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """Create new instance of XCAFDoc_VisMaterialTool."""

    @overload
    def Paste(self, theSource: nanoocp.BinObjMgt.BinObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool:
        """Paste attribute from persistence into document."""

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.BinObjMgt.BinObjMgt_Persistent, theRelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None:
        """Paste attribute from document into persistence."""
