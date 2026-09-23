"""OCCT package XmlMXCAFDoc (toolkit TKXmlXCAF)"""

from typing import overload

import nanoocp.LDOM
import nanoocp.Message
import nanoocp.Standard
import nanoocp.TDF
import nanoocp.TopLoc
import nanoocp.XmlMDF
import nanoocp.XmlObjMgt


class XmlMXCAFDoc:
    """
    Storage and Retrieval drivers for modelling attributes.
    Transient attributes are defined in package XCAFDoc
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XmlMXCAFDoc) -> None: ...

    @staticmethod
    def AddDrivers(aDriverTable: nanoocp.XmlMDF.XmlMDF_ADriverTable | None, anMsgDrv: nanoocp.Message.Message_Messenger | None) -> None:
        """Adds the attribute drivers to <aDriverTable>."""

class XmlMXCAFDoc_AssemblyItemRefDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMXCAFDoc_AssemblyItemRefDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlMXCAFDoc_CentroidDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMXCAFDoc_CentroidDriver) -> None: ...

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

class XmlMXCAFDoc_ColorDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMXCAFDoc_ColorDriver) -> None: ...

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

class XmlMXCAFDoc_DatumDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMXCAFDoc_DatumDriver) -> None: ...

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

class XmlMXCAFDoc_DimTolDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMXCAFDoc_DimTolDriver) -> None: ...

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

class XmlMXCAFDoc_GraphNodeDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMXCAFDoc_GraphNodeDriver) -> None: ...

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

class XmlMXCAFDoc_LengthUnitDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMXCAFDoc_LengthUnitDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlMXCAFDoc_LocationDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMXCAFDoc_LocationDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, Source: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, Target: nanoocp.TDF.TDF_Attribute | None, RelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, Source: nanoocp.TDF.TDF_Attribute | None, Target: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, RelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: ...

    @overload
    def Translate(self, theLoc: nanoocp.TopLoc.TopLoc_Location, theParent: nanoocp.LDOM.LDOM_Element, theMap: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None:
        """Translate a non storable Location to a storable Location."""

    @overload
    def Translate(self, theParent: nanoocp.LDOM.LDOM_Element, theLoc: nanoocp.TopLoc.TopLoc_Location, theMap: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool:
        """Translate a storable Location to a non storable Location."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlMXCAFDoc_MaterialDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMXCAFDoc_MaterialDriver) -> None: ...

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

class XmlMXCAFDoc_NoteDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    """Attribute Driver."""

    @overload
    def Paste(self, theSource: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlMXCAFDoc_NoteCommentDriver(XmlMXCAFDoc_NoteDriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMXCAFDoc_NoteCommentDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlMXCAFDoc_NoteBinDataDriver(XmlMXCAFDoc_NoteDriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMXCAFDoc_NoteBinDataDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlMXCAFDoc_VisMaterialDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: XmlMXCAFDoc_VisMaterialDriver) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """Create new instance of XCAFDoc_VisMaterial."""

    @overload
    def Paste(self, theSource: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool:
        """Paste attribute from persistence into document."""

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None:
        """Paste attribute from document into persistence."""

class XmlMXCAFDoc_VisMaterialToolDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    """XML persistence driver for XCAFDoc_VisMaterialTool."""

    @overload
    def __init__(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: XmlMXCAFDoc_VisMaterialToolDriver) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """Create new instance of XCAFDoc_VisMaterialTool."""

    @overload
    def Paste(self, theSource: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool:
        """Paste attribute from persistence into document."""

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None:
        """Paste attribute from document into persistence."""
