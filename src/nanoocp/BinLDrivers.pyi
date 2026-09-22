"""OCCT package BinLDrivers (toolkit TKBinL)"""

import enum
from typing import BinaryIO, overload

import nanoocp.BinMDF
import nanoocp.CDM
import nanoocp.Message
import nanoocp.PCDM
import nanoocp.Standard
import nanoocp.Storage
import nanoocp.TCollection
import nanoocp.TDocStd


class BinLDrivers_Marker(enum.IntEnum):
    BinLDrivers_ENDATTRLIST = -1

    BinLDrivers_ENDLABEL = -2

BinLDrivers_ENDATTRLIST: BinLDrivers_Marker = BinLDrivers_Marker.BinLDrivers_ENDATTRLIST

BinLDrivers_ENDLABEL: BinLDrivers_Marker = BinLDrivers_Marker.BinLDrivers_ENDLABEL

class BinLDrivers:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BinLDrivers) -> None: ...

    @staticmethod
    def Factory(theGUID: nanoocp.Standard.Standard_GUID) -> nanoocp.Standard.Standard_Transient: ...

    @staticmethod
    def DefineFormat(theApp: nanoocp.TDocStd.TDocStd_Application | None) -> None:
        """
        Defines format "BinLOcaf" and registers its read and write drivers
        in the specified application
        """

    @staticmethod
    def AttributeDrivers(MsgDrv: nanoocp.Message.Message_Messenger | None) -> nanoocp.BinMDF.BinMDF_ADriverTable:
        """Creates a table of the supported drivers' types"""

class BinLDrivers_DocumentSection:
    """
    More or less independent part of the saved/restored document
    that is distinct from OCAF data themselves but may be referred
    by them.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theName: nanoocp.TCollection.TCollection_AsciiString, isPostRead: bool) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BinLDrivers_DocumentSection) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Query the name of the section."""

    def IsPostRead(self) -> bool:
        """
        Query the status: if the Section should be read after OCAF;
        False means that the Section is read before starting to
        read OCAF data.
        """

    def Offset(self) -> int:
        """Query the offset of the section in the persistent file"""

    def SetOffset(self, theOffset: int) -> None:
        """Set the offset of the section in the persistent file"""

    def Length(self) -> int:
        """Query the length of the section in the persistent file"""

    def SetLength(self, theLength: int) -> None:
        """Set the length of the section in the persistent file"""

    def WriteTOC(self, theDocFormatVersion: nanoocp.TDocStd.TDocStd_FormatVersion) -> bytes:
        """Create a Section entry in the Document TOC (list of sections)"""

    def Write(self, theOffset: int, theDocFormatVersion: nanoocp.TDocStd.TDocStd_FormatVersion) -> bytes:
        """
        Save Offset and Length data into the Section entry
        in the Document TOC (list of sections)
        """

    @staticmethod
    def ReadTOC(theSection: BinLDrivers_DocumentSection, theIS: BinaryIO, theDocFormatVersion: nanoocp.TDocStd.TDocStd_FormatVersion) -> bool:
        """
        Fill a DocumentSection instance from the data that are read
        from TOC. Returns false in case of the stream reading problem.
        """

class BinLDrivers_DocumentRetrievalDriver(nanoocp.PCDM.PCDM_RetrievalDriver):
    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BinLDrivers_DocumentRetrievalDriver) -> None: ...

    @overload
    def Read(self, theFileName: nanoocp.TCollection.TCollection_ExtendedString, theNewDocument: nanoocp.CDM.CDM_Document | None, theApplication: nanoocp.CDM.CDM_Application | None, theFilter: nanoocp.PCDM.PCDM_ReaderFilter | None = None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """retrieves the content of the file into a new Document."""

    @overload
    def Read(self, theIStream: BinaryIO, theStorageData: nanoocp.Storage.Storage_Data | None, theDoc: nanoocp.CDM.CDM_Document | None, theApplication: nanoocp.CDM.CDM_Application | None, theFilter: nanoocp.PCDM.PCDM_ReaderFilter | None = None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    def AttributeDrivers(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> nanoocp.BinMDF.BinMDF_ADriverTable: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinLDrivers_DocumentStorageDriver(nanoocp.PCDM.PCDM_StorageDriver):
    """persistent implementation of storage a document in a binary file"""

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BinLDrivers_DocumentStorageDriver) -> None: ...

    @overload
    def Write(self, theDocument: nanoocp.CDM.CDM_Document | None, theFileName: nanoocp.TCollection.TCollection_ExtendedString, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Write <theDocument> to the binary file <theFileName>"""

    @overload
    def Write(self, theDocument: nanoocp.CDM.CDM_Document | None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """Write <theDocument> to theOStream"""

    def AttributeDrivers(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> nanoocp.BinMDF.BinMDF_ADriverTable: ...

    def AddSection(self, theName: nanoocp.TCollection.TCollection_AsciiString, isPostRead: bool = True) -> None:
        """Create a section that should be written after the OCAF data"""

    def IsQuickPart(self, theVersion: int) -> bool:
        """
        Return true if document should be stored in quick mode for partial reading
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
