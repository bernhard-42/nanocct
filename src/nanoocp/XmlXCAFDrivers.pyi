"""OCCT package XmlXCAFDrivers (toolkit TKXmlXCAF)"""

from typing import overload

import nanoocp.Message
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDocStd
import nanoocp.XmlDrivers
import nanoocp.XmlMDF


class XmlXCAFDrivers:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XmlXCAFDrivers) -> None: ...

    @staticmethod
    def Factory(aGUID: nanoocp.Standard.Standard_GUID) -> nanoocp.Standard.Standard_Transient:
        """
        Depending from the ID, returns a list of storage
        or retrieval attribute drivers. Used for plugin.

        Standard data model drivers
        ===========================
        47b0b826-d931-11d1-b5da-00a0c9064368 Transient-Persistent
        47b0b827-d931-11d1-b5da-00a0c9064368 Persistent-Transient

        XCAF data model drivers
        =================================
        ed8793f8-3142-11d4-b9b5-0060b0ee281b Transient-Persistent
        ed8793f9-3142-11d4-b9b5-0060b0ee281b Persistent-Transient
        ed8793fa-3142-11d4-b9b5-0060b0ee281b XCAFSchema
        """

    @staticmethod
    def DefineFormat(theApp: nanoocp.TDocStd.TDocStd_Application | None) -> None:
        """
        Defines format "XmlXCAF" and registers its read and write drivers
        in the specified application
        """

class XmlXCAFDrivers_DocumentRetrievalDriver(nanoocp.XmlDrivers.XmlDrivers_DocumentRetrievalDriver):
    """retrieval driver of a XS document"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XmlXCAFDrivers_DocumentRetrievalDriver) -> None: ...

    def AttributeDrivers(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> nanoocp.XmlMDF.XmlMDF_ADriverTable: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlXCAFDrivers_DocumentStorageDriver(nanoocp.XmlDrivers.XmlDrivers_DocumentStorageDriver):
    """storage driver of a XS document"""

    @overload
    def __init__(self, theCopyright: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    @overload
    def __init__(self, theOther: XmlXCAFDrivers_DocumentStorageDriver) -> None: ...

    def AttributeDrivers(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> nanoocp.XmlMDF.XmlMDF_ADriverTable: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
