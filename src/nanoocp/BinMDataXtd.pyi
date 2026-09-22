"""OCCT package BinMDataXtd (toolkit TKBin)"""

from typing import overload

import nanoocp.BinMDF
import nanoocp.BinObjMgt
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TDF


class BinMDataXtd:
    """Storage and Retrieval drivers for modelling attributes."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BinMDataXtd) -> None: ...

    @staticmethod
    def AddDrivers(theDriverTable: nanoocp.BinMDF.BinMDF_ADriverTable | None, aMsgDrv: nanoocp.Message.Message_Messenger | None) -> None:
        """Adds the attribute drivers to <theDriverTable>."""

    @staticmethod
    def SetDocumentVersion(DocVersion: int) -> None: ...

    @staticmethod
    def DocumentVersion() -> int: ...

class BinMDataXtd_ConstraintDriver(nanoocp.BinMDF.BinMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMDataXtd_ConstraintDriver) -> None: ...

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

class BinMDataXtd_GeometryDriver(nanoocp.BinMDF.BinMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMDataXtd_GeometryDriver) -> None: ...

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

class BinMDataXtd_PatternStdDriver(nanoocp.BinMDF.BinMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMDataXtd_PatternStdDriver) -> None: ...

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

class BinMDataXtd_PresentationDriver(nanoocp.BinMDF.BinMDF_ADriver):
    """Presentation Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMDataXtd_PresentationDriver) -> None: ...

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

class BinMDataXtd_PositionDriver(nanoocp.BinMDF.BinMDF_ADriver):
    """Position Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMDataXtd_PositionDriver) -> None: ...

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

class BinMDataXtd_TriangulationDriver(nanoocp.BinMDF.BinMDF_ADriver):
    """TDataXtd_Triangulation attribute bin Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMDataXtd_TriangulationDriver) -> None: ...

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
