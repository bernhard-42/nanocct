"""OCCT package XmlLDrivers (toolkit TKXmlL)"""

from typing import BinaryIO, overload

import nanoocp.CDM
import nanoocp.Message
import nanoocp.PCDM
import nanoocp.Standard
import nanoocp.Storage
import nanoocp.TCollection
import nanoocp.TDocStd
import nanoocp.XmlMDF


class XmlLDrivers:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XmlLDrivers) -> None: ...

    @staticmethod
    def Factory(theGUID: nanoocp.Standard.Standard_GUID) -> nanoocp.Standard.Standard_Transient: ...

    @staticmethod
    def CreationDate() -> nanoocp.TCollection.TCollection_AsciiString: ...

    @staticmethod
    def DefineFormat(theApp: nanoocp.TDocStd.TDocStd_Application | None) -> None:
        """
        Defines format "XmlLOcaf" and registers its read and write drivers
        in the specified application
        """

    @staticmethod
    def AttributeDrivers(theMsgDriver: nanoocp.Message.Message_Messenger | None) -> nanoocp.XmlMDF.XmlMDF_ADriverTable: ...

class XmlLDrivers_DocumentRetrievalDriver(nanoocp.PCDM.PCDM_RetrievalDriver):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XmlLDrivers_DocumentRetrievalDriver) -> None: ...

    @overload
    def Read(self, theFileName: nanoocp.TCollection.TCollection_ExtendedString, theNewDocument: nanoocp.CDM.CDM_Document | None, theApplication: nanoocp.CDM.CDM_Application | None, theFilter: nanoocp.PCDM.PCDM_ReaderFilter | None = None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def Read(self, theIStream: BinaryIO, theStorageData: nanoocp.Storage.Storage_Data | None, theDoc: nanoocp.CDM.CDM_Document | None, theApplication: nanoocp.CDM.CDM_Application | None, theFilter: nanoocp.PCDM.PCDM_ReaderFilter | None = None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    def AttributeDrivers(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> nanoocp.XmlMDF.XmlMDF_ADriverTable: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlLDrivers_NamespaceDef:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, thePrefix: nanoocp.TCollection.TCollection_AsciiString, theURI: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    @overload
    def __init__(self, theOther: XmlLDrivers_NamespaceDef) -> None: ...

    def Prefix(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def URI(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

class XmlLDrivers_DocumentStorageDriver(nanoocp.PCDM.PCDM_StorageDriver):
    @overload
    def __init__(self, theCopyright: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    @overload
    def __init__(self, theOther: XmlLDrivers_DocumentStorageDriver) -> None: ...

    @overload
    def Write(self, theDocument: nanoocp.CDM.CDM_Document | None, theFileName: nanoocp.TCollection.TCollection_ExtendedString, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def Write(self, theDocument: nanoocp.CDM.CDM_Document | None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bytes: ...

    def AttributeDrivers(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> nanoocp.XmlMDF.XmlMDF_ADriverTable: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
