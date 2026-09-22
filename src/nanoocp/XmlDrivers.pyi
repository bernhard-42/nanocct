"""OCCT package XmlDrivers (toolkit TKXml)"""

from typing import overload

import nanoocp.LDOM
import nanoocp.Message
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDocStd
import nanoocp.XmlLDrivers
import nanoocp.XmlMDF


class XmlDrivers:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XmlDrivers) -> None: ...

    @staticmethod
    def Factory(theGUID: nanoocp.Standard.Standard_GUID) -> nanoocp.Standard.Standard_Transient: ...

    @staticmethod
    def DefineFormat(theApp: nanoocp.TDocStd.TDocStd_Application | None) -> None:
        """
        Defines format "XmlOcaf" and registers its read and write drivers
        in the specified application
        """

    @staticmethod
    def AttributeDrivers(theMsgDriver: nanoocp.Message.Message_Messenger | None) -> nanoocp.XmlMDF.XmlMDF_ADriverTable: ...

class XmlDrivers_DocumentRetrievalDriver(nanoocp.XmlLDrivers.XmlLDrivers_DocumentRetrievalDriver):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XmlDrivers_DocumentRetrievalDriver) -> None: ...

    def AttributeDrivers(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> nanoocp.XmlMDF.XmlMDF_ADriverTable: ...

    def ReadShapeSection(self, thePDoc: nanoocp.LDOM.LDOM_Element, theMsgDriver: nanoocp.Message.Message_Messenger | None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.XmlMDF.XmlMDF_ADriver: ...

    def ShapeSetCleaning(self, theDriver: nanoocp.XmlMDF.XmlMDF_ADriver | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlDrivers_DocumentStorageDriver(nanoocp.XmlLDrivers.XmlLDrivers_DocumentStorageDriver):
    @overload
    def __init__(self, theCopyright: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    @overload
    def __init__(self, theOther: XmlDrivers_DocumentStorageDriver) -> None: ...

    def AttributeDrivers(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> nanoocp.XmlMDF.XmlMDF_ADriverTable: ...

    def WriteShapeSection(self, thePDoc: nanoocp.LDOM.LDOM_Element, theStorageFormatVersion: nanoocp.TDocStd.TDocStd_FormatVersion, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
