"""OCCT package PCDM (toolkit TKCDF)"""

import enum
from typing import BinaryIO, overload

import nanoocp.CDM
import nanoocp.LDOM
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.Storage
import nanoocp.TCollection


class PCDM_TypeOfFileDriver(enum.IntEnum):
    PCDM_TOFD_File = 0

    PCDM_TOFD_CmpFile = 1

    PCDM_TOFD_XmlFile = 2

    PCDM_TOFD_Unknown = 3

PCDM_TOFD_File: PCDM_TypeOfFileDriver = PCDM_TypeOfFileDriver.PCDM_TOFD_File

PCDM_TOFD_CmpFile: PCDM_TypeOfFileDriver = PCDM_TypeOfFileDriver.PCDM_TOFD_CmpFile

PCDM_TOFD_XmlFile: PCDM_TypeOfFileDriver = PCDM_TypeOfFileDriver.PCDM_TOFD_XmlFile

PCDM_TOFD_Unknown: PCDM_TypeOfFileDriver = PCDM_TypeOfFileDriver.PCDM_TOFD_Unknown

class PCDM_ReaderStatus(enum.IntEnum):
    """
    Status of reading of a document.
    The following values are accessible:
    - PCDM_RS_OK: the document was successfully read;
    - PCDM_RS_NoDriver: driver is not found for the defined file format;
    - PCDM_RS_UnknownFileDriver: check of the file failed (file doesn't exist, for example);
    - PCDM_RS_OpenError: attempt to open the file failed;
    - PCDM_RS_NoVersion: document version of the file is out of scope;
    - PCDM_RS_NoSchema: NOT USED;
    - PCDM_RS_NoDocument: document is empty (failed to be read correctly);
    - PCDM_RS_ExtensionFailure: NOT USED;
    - PCDM_RS_WrongStreamMode: file is not open for reading (a mistaken mode);
    - PCDM_RS_FormatFailure: mistake in document data structure;
    - PCDM_RS_TypeFailure: data type is unknown;
    - PCDM_RS_TypeNotFoundInSchema: data type is not found in schema (STD file format);
    - PCDM_RS_UnrecognizedFileFormat: document data structure is wrong (binary file format);
    - PCDM_RS_MakeFailure: conversion of data from persistent to transient attributes failed (XML
    file format);
    - PCDM_RS_PermissionDenied: file can't be opened because permission is denied;
    - PCDM_RS_DriverFailure: something went wrong (a general mistake of reading of a document);
    - PCDM_RS_AlreadyRetrievedAndModified: document is already retrieved and modified in current
    session;
    - PCDM_RS_AlreadyRetrieved: document is already in current session (already retrieved);
    - PCDM_RS_UnknownDocument: file doesn't exist on disk;
    - PCDM_RS_WrongResource: wrong resource file (.RetrievalPlugin);
    - PCDM_RS_ReaderException: no shape section in the document file (binary file format);
    - PCDM_RS_NoModel: NOT USED;
    - PCDM_RS_UserBreak: user stopped reading of the document;
    """

    PCDM_RS_OK = 0

    PCDM_RS_NoDriver = 1

    PCDM_RS_UnknownFileDriver = 2

    PCDM_RS_OpenError = 3

    PCDM_RS_NoVersion = 4

    PCDM_RS_NoSchema = 5

    PCDM_RS_NoDocument = 6

    PCDM_RS_ExtensionFailure = 7

    PCDM_RS_WrongStreamMode = 8

    PCDM_RS_FormatFailure = 9

    PCDM_RS_TypeFailure = 10

    PCDM_RS_TypeNotFoundInSchema = 11

    PCDM_RS_UnrecognizedFileFormat = 12

    PCDM_RS_MakeFailure = 13

    PCDM_RS_PermissionDenied = 14

    PCDM_RS_DriverFailure = 15

    PCDM_RS_AlreadyRetrievedAndModified = 16

    PCDM_RS_AlreadyRetrieved = 17

    PCDM_RS_UnknownDocument = 18

    PCDM_RS_WrongResource = 19

    PCDM_RS_ReaderException = 20

    PCDM_RS_NoModel = 21

    PCDM_RS_UserBreak = 22

PCDM_RS_OK: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_OK

PCDM_RS_NoDriver: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_NoDriver

PCDM_RS_UnknownFileDriver: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_UnknownFileDriver

PCDM_RS_OpenError: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_OpenError

PCDM_RS_NoVersion: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_NoVersion

PCDM_RS_NoSchema: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_NoSchema

PCDM_RS_NoDocument: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_NoDocument

PCDM_RS_ExtensionFailure: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_ExtensionFailure

PCDM_RS_WrongStreamMode: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_WrongStreamMode

PCDM_RS_FormatFailure: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_FormatFailure

PCDM_RS_TypeFailure: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_TypeFailure

PCDM_RS_TypeNotFoundInSchema: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_TypeNotFoundInSchema

PCDM_RS_UnrecognizedFileFormat: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_UnrecognizedFileFormat

PCDM_RS_MakeFailure: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_MakeFailure

PCDM_RS_PermissionDenied: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_PermissionDenied

PCDM_RS_DriverFailure: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_DriverFailure

PCDM_RS_AlreadyRetrievedAndModified: PCDM_ReaderStatus = ...

PCDM_RS_AlreadyRetrieved: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_AlreadyRetrieved

PCDM_RS_UnknownDocument: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_UnknownDocument

PCDM_RS_WrongResource: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_WrongResource

PCDM_RS_ReaderException: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_ReaderException

PCDM_RS_NoModel: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_NoModel

PCDM_RS_UserBreak: PCDM_ReaderStatus = PCDM_ReaderStatus.PCDM_RS_UserBreak

class PCDM_StoreStatus(enum.IntEnum):
    """
    Status of storage of a document on disk.
    If it is PCDM_SS_OK, the document is successfully saved on disk.
    Else - there is an error.
    """

    PCDM_SS_OK = 0

    PCDM_SS_DriverFailure = 1

    PCDM_SS_WriteFailure = 2

    PCDM_SS_Failure = 3

    PCDM_SS_Doc_IsNull = 4

    PCDM_SS_No_Obj = 5

    PCDM_SS_Info_Section_Error = 6

    PCDM_SS_UserBreak = 7

    PCDM_SS_UnrecognizedFormat = 8

PCDM_SS_OK: PCDM_StoreStatus = PCDM_StoreStatus.PCDM_SS_OK

PCDM_SS_DriverFailure: PCDM_StoreStatus = PCDM_StoreStatus.PCDM_SS_DriverFailure

PCDM_SS_WriteFailure: PCDM_StoreStatus = PCDM_StoreStatus.PCDM_SS_WriteFailure

PCDM_SS_Failure: PCDM_StoreStatus = PCDM_StoreStatus.PCDM_SS_Failure

PCDM_SS_Doc_IsNull: PCDM_StoreStatus = PCDM_StoreStatus.PCDM_SS_Doc_IsNull

PCDM_SS_No_Obj: PCDM_StoreStatus = PCDM_StoreStatus.PCDM_SS_No_Obj

PCDM_SS_Info_Section_Error: PCDM_StoreStatus = PCDM_StoreStatus.PCDM_SS_Info_Section_Error

PCDM_SS_UserBreak: PCDM_StoreStatus = PCDM_StoreStatus.PCDM_SS_UserBreak

PCDM_SS_UnrecognizedFormat: PCDM_StoreStatus = PCDM_StoreStatus.PCDM_SS_UnrecognizedFormat

class PCDM:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: PCDM) -> None: ...

    @overload
    @staticmethod
    def FileDriverType(aFileName: nanoocp.TCollection.TCollection_AsciiString) -> tuple[PCDM_TypeOfFileDriver, nanoocp.Storage.Storage_BaseDriver]: ...

    @overload
    @staticmethod
    def FileDriverType(theIStream: BinaryIO) -> tuple[PCDM_TypeOfFileDriver, nanoocp.Storage.Storage_BaseDriver]: ...

class PCDM_Document(nanoocp.Standard.Standard_Persistent):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: PCDM_Document) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class PCDM_DOMHeaderParser(nanoocp.LDOM.LDOMParser):
    def __init__(self) -> None: ...

    def SetStartElementName(self, aStartElementName: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def SetEndElementName(self, anEndElementName: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def startElement(self) -> bool: ...

    def endElement(self) -> bool: ...

    def GetElement(self) -> nanoocp.LDOM.LDOM_Element: ...

class PCDM_DriverError(nanoocp.Standard.Standard_Failure):
    pass

class PCDM_Reader(nanoocp.Standard.Standard_Transient):
    @overload
    def Read(self, aFileName: nanoocp.TCollection.TCollection_ExtendedString, aNewDocument: nanoocp.CDM.CDM_Document | None, anApplication: nanoocp.CDM.CDM_Application | None, theFilter: PCDM_ReaderFilter | None = None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """retrieves the content of the file into a new Document."""

    @overload
    def Read(self, theIStream: BinaryIO, theStorageData: nanoocp.Storage.Storage_Data | None, theDoc: nanoocp.CDM.CDM_Document | None, theApplication: nanoocp.CDM.CDM_Application | None, theFilter: PCDM_ReaderFilter | None = None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    def GetStatus(self) -> PCDM_ReaderStatus: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class PCDM_ReaderFilter(nanoocp.Standard.Standard_Transient):
    """
    Class represents a document reading filter.

    It allows to set attributes (by class names) that must be skipped during the document reading
    or attributes that must be retrieved only.
    In addition it is possible to define one or several subtrees (by entry) which must be
    retrieved during the reading. Other labels are created, but no one attribute on them.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an empty filter, so, all will be retrieved if nothing else is defined.
        """

    @overload
    def __init__(self, theSkipped: nanoocp.Standard.Standard_Type | None) -> None:
        """Creates a filter to skip only one type of attributes."""

    @overload
    def __init__(self, theEntryToRead: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Creates a filter to read only sub-labels of a label-path.
        Like, for "0:2" it will read all attributes for labels "0:2", "0:2:1", etc.
        """

    @overload
    def __init__(self, theAppend: PCDM_ReaderFilter.AppendMode) -> None:
        """
        Creates a filter to append the content of file to open to existing document.
        """

    @overload
    def __init__(self, theOther: PCDM_ReaderFilter) -> None: ...

    class AppendMode(enum.IntEnum):
        """Supported modes of appending the file content into existing document"""

        AppendMode_Forbid = 0

        AppendMode_Protect = 1

        AppendMode_Overwrite = 2

    AppendMode_Forbid: PCDM_ReaderFilter.AppendMode = AppendMode.AppendMode_Forbid

    AppendMode_Protect: PCDM_ReaderFilter.AppendMode = AppendMode.AppendMode_Protect

    AppendMode_Overwrite: PCDM_ReaderFilter.AppendMode = AppendMode.AppendMode_Overwrite

    @overload
    def AddSkipped(self, theSkipped: nanoocp.Standard.Standard_Type | None) -> None:
        """Adds skipped attribute by type."""

    @overload
    def AddSkipped(self, theSkipped: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Adds skipped attribute by type name."""

    @overload
    def AddRead(self, theRead: nanoocp.Standard.Standard_Type | None) -> None:
        """Adds attribute to read by type. Disables the skipped attributes added."""

    @overload
    def AddRead(self, theRead: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Adds attribute to read by type name. Disables the skipped attributes added.
        """

    def AddPath(self, theEntryToRead: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Adds sub-tree path (like "0:2")."""

    def Clear(self) -> None:
        """Makes filter pass all data."""

    @overload
    def IsPassed(self, theAttributeID: nanoocp.Standard.Standard_Type | None) -> bool:
        """Returns true if attribute must be read."""

    @overload
    def IsPassed(self, theEntry: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Returns true if content of the label must be read."""

    @overload
    def IsPassed(self) -> bool:
        """Returns true if content of the currently iterated label must be read."""

    def IsPassedAttr(self, theAttributeType: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Returns true if attribute must be read."""

    @overload
    def IsSubPassed(self, theEntry: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Returns true if some sub-label of the given label is passed."""

    @overload
    def IsSubPassed(self) -> bool:
        """
        Returns true if some sub-label of the currently iterated label is passed.
        """

    def IsPartTree(self) -> bool:
        """Returns true if only part of the document tree will be retrieved."""

    def Mode(self) -> PCDM_ReaderFilter.AppendMode:
        """Returns the append mode."""

    def SetMode(self, theValue: PCDM_ReaderFilter.AppendMode) -> None:
        """Python addition: sets the value Mode() returns by reference in C++."""

    def IsAppendMode(self) -> bool:
        """Returns true if appending to the document is performed."""

    def StartIteration(self) -> None:
        """
        Starts the tree iterator. It is used for fast searching of passed labels if the whole tree of
        labels is parsed. So, on each iteration step the methods Up and Down must be called after the
        iteration start.
        """

    def Up(self) -> None:
        """Iteration to the child label."""

    def Down(self, theTag: int) -> None:
        """Iteration to the child with defined tag."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class PCDM_Reference:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aReferenceIdentifier: int, aFileName: nanoocp.TCollection.TCollection_ExtendedString, aDocumentVersion: int) -> None: ...

    @overload
    def __init__(self, theOther: PCDM_Reference) -> None: ...

    def ReferenceIdentifier(self) -> int: ...

    def FileName(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def DocumentVersion(self) -> int: ...

class PCDM_ReadWriter(nanoocp.Standard.Standard_Transient):
    def Version(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """returns PCDM_ReadWriter_1."""

    def WriteReferenceCounter(self, aData: nanoocp.Storage.Storage_Data | None, aDocument: nanoocp.CDM.CDM_Document | None) -> None: ...

    def WriteReferences(self, aData: nanoocp.Storage.Storage_Data | None, aDocument: nanoocp.CDM.CDM_Document | None, theReferencerFileName: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    def WriteExtensions(self, aData: nanoocp.Storage.Storage_Data | None, aDocument: nanoocp.CDM.CDM_Document | None) -> None: ...

    def WriteVersion(self, aData: nanoocp.Storage.Storage_Data | None, aDocument: nanoocp.CDM.CDM_Document | None) -> None: ...

    def ReadReferenceCounter(self, theFileName: nanoocp.TCollection.TCollection_ExtendedString, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> int: ...

    def ReadReferences(self, aFileName: nanoocp.TCollection.TCollection_ExtendedString, theReferences: nanoocp.NCollection.NCollection_Sequence[nanoocp.PCDM.PCDM_Reference], theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    def ReadExtensions(self, aFileName: nanoocp.TCollection.TCollection_ExtendedString, theExtensions: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_ExtendedString], theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    def ReadDocumentVersion(self, aFileName: nanoocp.TCollection.TCollection_ExtendedString, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> int: ...

    @staticmethod
    def Open(aDriver: nanoocp.Storage.Storage_BaseDriver | None, aFileName: nanoocp.TCollection.TCollection_ExtendedString, anOpenMode: nanoocp.Storage.Storage_OpenMode) -> None: ...

    @staticmethod
    def Reader(aFileName: nanoocp.TCollection.TCollection_ExtendedString) -> PCDM_ReadWriter:
        """returns the convenient Reader for a File."""

    @staticmethod
    def Writer() -> PCDM_ReadWriter: ...

    @staticmethod
    def WriteFileFormat(aData: nanoocp.Storage.Storage_Data | None, aDocument: nanoocp.CDM.CDM_Document | None) -> None: ...

    @overload
    @staticmethod
    def FileFormat(aFileName: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        tries to get a format in the file. returns an empty
        string if the file could not be read or does not have
        a FileFormat information.
        """

    @overload
    @staticmethod
    def FileFormat(theIStream: BinaryIO) -> tuple[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.Storage.Storage_Data]:
        """
        tries to get a format from the stream. returns an empty
        string if the file could not be read or does not have
        a FileFormat information.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class PCDM_ReadWriter_1(PCDM_ReadWriter):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: PCDM_ReadWriter_1) -> None: ...

    def Version(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """returns PCDM_ReadWriter_1."""

    def WriteReferenceCounter(self, aData: nanoocp.Storage.Storage_Data | None, aDocument: nanoocp.CDM.CDM_Document | None) -> None: ...

    def WriteReferences(self, aData: nanoocp.Storage.Storage_Data | None, aDocument: nanoocp.CDM.CDM_Document | None, theReferencerFileName: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    def WriteExtensions(self, aData: nanoocp.Storage.Storage_Data | None, aDocument: nanoocp.CDM.CDM_Document | None) -> None: ...

    def WriteVersion(self, aData: nanoocp.Storage.Storage_Data | None, aDocument: nanoocp.CDM.CDM_Document | None) -> None: ...

    def ReadReferenceCounter(self, aFileName: nanoocp.TCollection.TCollection_ExtendedString, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> int: ...

    def ReadReferences(self, aFileName: nanoocp.TCollection.TCollection_ExtendedString, theReferences: nanoocp.NCollection.NCollection_Sequence[nanoocp.PCDM.PCDM_Reference], theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    def ReadExtensions(self, aFileName: nanoocp.TCollection.TCollection_ExtendedString, theExtensions: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_ExtendedString], theMsgDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    def ReadDocumentVersion(self, aFileName: nanoocp.TCollection.TCollection_ExtendedString, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class PCDM_ReferenceIterator(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None:
        """Warning! The constructor does not initialization."""

    @overload
    def __init__(self, theOther: PCDM_ReferenceIterator) -> None: ...

    def LoadReferences(self, aDocument: nanoocp.CDM.CDM_Document | None, aMetaData: nanoocp.CDM.CDM_MetaData | None, anApplication: nanoocp.CDM.CDM_Application | None, UseStorageConfiguration: bool) -> None: ...

    def Init(self, aMetaData: nanoocp.CDM.CDM_MetaData | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class PCDM_RetrievalDriver(PCDM_Reader):
    @staticmethod
    def DocumentVersion(theFileName: nanoocp.TCollection.TCollection_ExtendedString, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> int: ...

    @staticmethod
    def ReferenceCounter(theFileName: nanoocp.TCollection.TCollection_ExtendedString, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> int: ...

    def SetFormat(self, aformat: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    def GetFormat(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class PCDM_Writer(nanoocp.Standard.Standard_Transient):
    @overload
    def Write(self, aDocument: nanoocp.CDM.CDM_Document | None, aFileName: nanoocp.TCollection.TCollection_ExtendedString, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def Write(self, theDocument: nanoocp.CDM.CDM_Document | None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """Write <theDocument> to theOStream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class PCDM_StorageDriver(PCDM_Writer):
    """
    persistent implementation of storage.

    The application must redefine one the two Make()
    methods. The first one, if the application wants to
    put only one document in the storage file.

    The second method should be redefined to put
    additional document that could be used by the
    retrieval instead of the principal document, depending
    on the schema used during the retrieval.
    For example, a second document could be a standard
    CDMShape_Document. This means that a client
    application will already be able to extract a CDMShape_Document
    of the file, if the Shape Schema remains unchanged.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: PCDM_StorageDriver) -> None: ...

    @overload
    def Make(self, aDocument: nanoocp.CDM.CDM_Document | None) -> PCDM_Document:
        """raises NotImplemented."""

    @overload
    def Make(self, aDocument: nanoocp.CDM.CDM_Document | None, Documents: nanoocp.NCollection.NCollection_Sequence[nanoocp.PCDM.PCDM_Document]) -> None:
        """
        By default, puts in the Sequence the document returns
        by the previous Make method.
        """

    @overload
    def Write(self, aDocument: nanoocp.CDM.CDM_Document | None, aFileName: nanoocp.TCollection.TCollection_ExtendedString, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Warning! raises DriverError if an error occurs during inside the
        Make method.
        stores the content of the Document into a new file.

        by default Write will use Make method to build a persistent
        document and the Schema method to write the persistent document.
        """

    @overload
    def Write(self, theDocument: nanoocp.CDM.CDM_Document | None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """Write <theDocument> to theOStream"""

    def SetFormat(self, aformat: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    def GetFormat(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def IsError(self) -> bool: ...

    def SetIsError(self, theIsError: bool) -> None: ...

    def GetStoreStatus(self) -> PCDM_StoreStatus: ...

    def SetStoreStatus(self, theStoreStatus: PCDM_StoreStatus) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.PCDM
PCDM_SequenceOfDocument = nanoocp.NCollection.NCollection_Sequence[nanoocp.PCDM.PCDM_Document]
PCDM_SequenceOfReference = nanoocp.NCollection.NCollection_Sequence[nanoocp.PCDM.PCDM_Reference]
