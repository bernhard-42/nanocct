"""OCCT package BinMDocStd (toolkit TKBinL)"""

from typing import overload

import nanoocp.BinMDF
import nanoocp.BinObjMgt
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TDF


class BinMDocStd:
    """Storage and Retrieval drivers for TDocStd modelling attributes."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BinMDocStd) -> None: ...

    @staticmethod
    def AddDrivers(theDriverTable: nanoocp.BinMDF.BinMDF_ADriverTable | None, aMsgDrv: nanoocp.Message.Message_Messenger | None) -> None:
        """Adds the attribute drivers to <theDriverTable>."""

class BinMDocStd_XLinkDriver(nanoocp.BinMDF.BinMDF_ADriver):
    """XLink attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMDocStd_XLinkDriver) -> None: ...

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
