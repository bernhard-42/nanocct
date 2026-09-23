"""OCCT package BinXCAFDrivers (toolkit TKBinXCAF)"""

from typing import overload

import nanoocp.BinDrivers
import nanoocp.BinMDF
import nanoocp.Message
import nanoocp.Standard
import nanoocp.TDocStd


class BinXCAFDrivers:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BinXCAFDrivers) -> None: ...

    @staticmethod
    def Factory(theGUID: nanoocp.Standard.Standard_GUID) -> nanoocp.Standard.Standard_Transient: ...

    @staticmethod
    def DefineFormat(theApp: nanoocp.TDocStd.TDocStd_Application | None) -> None:
        """
        Defines format "BinXCAF" and registers its read and write drivers
        in the specified application
        """

    @staticmethod
    def AttributeDrivers(MsgDrv: nanoocp.Message.Message_Messenger | None) -> nanoocp.BinMDF.BinMDF_ADriverTable:
        """Creates the table of drivers of types supported"""

class BinXCAFDrivers_DocumentRetrievalDriver(nanoocp.BinDrivers.BinDrivers_DocumentRetrievalDriver):
    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BinXCAFDrivers_DocumentRetrievalDriver) -> None: ...

    def AttributeDrivers(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> nanoocp.BinMDF.BinMDF_ADriverTable: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinXCAFDrivers_DocumentStorageDriver(nanoocp.BinDrivers.BinDrivers_DocumentStorageDriver):
    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BinXCAFDrivers_DocumentStorageDriver) -> None: ...

    def AttributeDrivers(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> nanoocp.BinMDF.BinMDF_ADriverTable: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
