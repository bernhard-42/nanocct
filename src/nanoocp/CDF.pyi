"""OCCT package CDF (toolkit TKCDF)"""

import enum
from typing import BinaryIO, overload

import nanoocp.CDM
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.PCDM
import nanoocp.Standard
import nanoocp.TCollection


class CDF_TypeOfActivation(enum.IntEnum):
    CDF_TOA_New = 0

    CDF_TOA_Modified = 1

    CDF_TOA_Unchanged = 2

CDF_TOA_New: CDF_TypeOfActivation = CDF_TypeOfActivation.CDF_TOA_New

CDF_TOA_Modified: CDF_TypeOfActivation = CDF_TypeOfActivation.CDF_TOA_Modified

CDF_TOA_Unchanged: CDF_TypeOfActivation = CDF_TypeOfActivation.CDF_TOA_Unchanged

class CDF_StoreSetNameStatus(enum.IntEnum):
    CDF_SSNS_OK = 0

    CDF_SSNS_ReplacingAnExistentDocument = 1

    CDF_SSNS_OpenDocument = 2

CDF_SSNS_OK: CDF_StoreSetNameStatus = CDF_StoreSetNameStatus.CDF_SSNS_OK

CDF_SSNS_ReplacingAnExistentDocument: CDF_StoreSetNameStatus = ...

CDF_SSNS_OpenDocument: CDF_StoreSetNameStatus = CDF_StoreSetNameStatus.CDF_SSNS_OpenDocument

class CDF_SubComponentStatus(enum.IntEnum):
    CDF_SCS_Consistent = 0

    CDF_SCS_Unconsistent = 1

    CDF_SCS_Stored = 2

    CDF_SCS_Modified = 3

CDF_SCS_Consistent: CDF_SubComponentStatus = CDF_SubComponentStatus.CDF_SCS_Consistent

CDF_SCS_Unconsistent: CDF_SubComponentStatus = CDF_SubComponentStatus.CDF_SCS_Unconsistent

CDF_SCS_Stored: CDF_SubComponentStatus = CDF_SubComponentStatus.CDF_SCS_Stored

CDF_SCS_Modified: CDF_SubComponentStatus = CDF_SubComponentStatus.CDF_SCS_Modified

class CDF_TryStoreStatus(enum.IntEnum):
    CDF_TS_OK = 0

    CDF_TS_NoCurrentDocument = 1

    CDF_TS_NoDriver = 2

    CDF_TS_NoSubComponentDriver = 3

CDF_TS_OK: CDF_TryStoreStatus = CDF_TryStoreStatus.CDF_TS_OK

CDF_TS_NoCurrentDocument: CDF_TryStoreStatus = CDF_TryStoreStatus.CDF_TS_NoCurrentDocument

CDF_TS_NoDriver: CDF_TryStoreStatus = CDF_TryStoreStatus.CDF_TS_NoDriver

CDF_TS_NoSubComponentDriver: CDF_TryStoreStatus = CDF_TryStoreStatus.CDF_TS_NoSubComponentDriver

class CDF_MetaDataDriver(nanoocp.Standard.Standard_Transient):
    """
    this class list the method that must be available for
    a specific DBMS
    """

    def HasVersionCapability(self) -> bool:
        """
        returns true if the MetaDataDriver can manage different
        versions of a Data.
        By default, returns false.
        """

    def CreateDependsOn(self, aFirstData: nanoocp.CDM.CDM_MetaData | None, aSecondData: nanoocp.CDM.CDM_MetaData | None) -> None:
        """
        Creates a "Depends On" relation between two Datas.
        By default does nothing
        """

    def CreateReference(self, aFrom: nanoocp.CDM.CDM_MetaData | None, aTo: nanoocp.CDM.CDM_MetaData | None, aReferenceIdentifier: int, aToDocumentVersion: int) -> None: ...

    def HasVersion(self, aFolder: nanoocp.TCollection.TCollection_ExtendedString, aName: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """by default return true."""

    def BuildFileName(self, aDocument: nanoocp.CDM.CDM_Document | None) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def SetName(self, aDocument: nanoocp.CDM.CDM_Document | None, aName: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        this method is useful if the name of an object
        depends on the metadatadriver. For example a Driver
        based on the operating system can choose to add
        the extension of file to create to the object.
        """

    @overload
    def Find(self, aFolder: nanoocp.TCollection.TCollection_ExtendedString, aName: nanoocp.TCollection.TCollection_ExtendedString, aVersion: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        should indicate whether meta-data exist in the DBMS corresponding
        to the Data.
        aVersion may be NULL;
        """

    @overload
    def Find(self, aFolder: nanoocp.TCollection.TCollection_ExtendedString, aName: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """calls Find with an empty version"""

    def HasReadPermission(self, aFolder: nanoocp.TCollection.TCollection_ExtendedString, aName: nanoocp.TCollection.TCollection_ExtendedString, aVersion: nanoocp.TCollection.TCollection_ExtendedString) -> bool: ...

    @overload
    def MetaData(self, aFolder: nanoocp.TCollection.TCollection_ExtendedString, aName: nanoocp.TCollection.TCollection_ExtendedString, aVersion: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.CDM.CDM_MetaData:
        """
        should return the MetaData stored in the DBMS with the meta-data
        corresponding to the Data. If the MetaDataDriver has version management capabilities
        the version has to be set in the returned MetaData.
        aVersion may be NULL
        MetaData is called by GetMetaData
        If the version is set to NULL, MetaData should return
        the last version of the metadata
        """

    @overload
    def MetaData(self, aFolder: nanoocp.TCollection.TCollection_ExtendedString, aName: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.CDM.CDM_MetaData:
        """calls MetaData with an empty version"""

    def LastVersion(self, aMetaData: nanoocp.CDM.CDM_MetaData | None) -> nanoocp.CDM.CDM_MetaData:
        """
        by default returns aMetaDATA
        should return the MetaData stored in the DBMS with the meta-data
        corresponding to the path. If the MetaDataDriver has version management capabilities
        the version has to be set in the returned MetaData.
        MetaData is called by GetMetaData
        If the version is not included in the path, MetaData should return
        the last version of the metadata
        is deferred;
        """

    def CreateMetaData(self, aDocument: nanoocp.CDM.CDM_Document | None, aFileName: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.CDM.CDM_MetaData:
        """
        should create meta-data corresponding to aData and maintaining a meta-link
        between these meta-data and aFileName
        CreateMetaData is called by CreateData
        If the metadata-driver
        has version capabilities, version must be set in the returned Data.
        """

    def FindFolder(self, aFolder: nanoocp.TCollection.TCollection_ExtendedString) -> bool: ...

    def DefaultFolder(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def ReferenceIterator(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> nanoocp.PCDM.PCDM_ReferenceIterator: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class CDF_Application(nanoocp.CDM.CDM_Application):
    @staticmethod
    def Load(aGUID: nanoocp.Standard.Standard_GUID) -> CDF_Application:
        """
        plugs an application.

        Open is used
        - for opening a Document that has been created in an application
        - for opening a Document from the database
        - for opening a Document from a file.
        The Open methods always add the document in the session directory and
        calls the virtual Activate method. The document is considered to be
        opened until Close is used. To be storable, a document must be
        opened by an application since the application resources are
        needed to store it.
        """

    def NewDocument(self, theFormat: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.CDM.CDM_Document:
        """
        Constructs an new empty document.
        This document will have the specified format.
        If InitDocument() is redefined for a specific
        application, the new document is handled by the
        applicative session.
        """

    def InitDocument(self, theDoc: nanoocp.CDM.CDM_Document | None) -> None:
        """
        Initialize a document for the applicative session.
        This virtual function is called by NewDocument
        and should be redefined for each specific application.
        """

    def Open(self, aDocument: nanoocp.CDM.CDM_Document | None) -> None:
        """
        puts the document in the current session directory
        and calls the virtual method Activate on it.
        """

    def CanClose(self, aDocument: nanoocp.CDM.CDM_Document | None) -> nanoocp.CDM.CDM_CanCloseStatus: ...

    def Close(self, aDocument: nanoocp.CDM.CDM_Document | None) -> None:
        """
        removes the document of the current session directory
        and closes the document;
        """

    @overload
    def Retrieve(self, aFolder: nanoocp.TCollection.TCollection_ExtendedString, aName: nanoocp.TCollection.TCollection_ExtendedString, UseStorageConfiguration: bool = True, theFilter: nanoocp.PCDM.PCDM_ReaderFilter | None = None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.CDM.CDM_Document:
        """
        This method retrieves a document from the database.
        If the Document references other documents which have
        been updated, the latest version of these documents will
        be used if {UseStorageConfiguration} is true.
        The content of {aFolder}, {aName} and {aVersion} depends on
        the Database Manager system. If the DBMS is only based on
        the OS, {aFolder} is a directory and {aName} is the name of a
        file. In this case the use of the syntax with {aVersion}
        has no sense. For example:

        occ::handle<CDM_Document> theDocument=myApplication->Retrieve("/home/cascade","box.dsg");
        If the DBMS is EUCLID/Design Manager, {aFolder}, {aName}
        have the form they have in EUCLID/Design Manager. For example:

        occ::handle<CDM_Document> theDocument=myApplication->Retrieve("|user|cascade","box");

        Since the version is not specified in this syntax, the latest will be used.
        A link is kept with the database through an instance of CDM_MetaData
        """

    @overload
    def Retrieve(self, aFolder: nanoocp.TCollection.TCollection_ExtendedString, aName: nanoocp.TCollection.TCollection_ExtendedString, aVersion: nanoocp.TCollection.TCollection_ExtendedString, UseStorageConfiguration: bool = True, theFilter: nanoocp.PCDM.PCDM_ReaderFilter | None = None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.CDM.CDM_Document:
        """
        This method retrieves a document from the database.
        If the Document references other documents which have
        been updated, the latest version of these documents
        will be used if {UseStorageConfiguration} is
        true. If the DBMS is only based on the OS,
        this syntax should not be used.

        If the DBMS is EUCLID/Design Manager, {aFolder}, {aName}
        and {aVersion} have the form they have in
        EUCLID/Design Manager. For example:

        occ::handle<CDM_Document> theDocument=myApplication->Retrieve("|user|cascade","box","2");
        A link is kept with the database through an instance
        of CDM_MetaData
        """

    @overload
    def CanRetrieve(self, theFolder: nanoocp.TCollection.TCollection_ExtendedString, theName: nanoocp.TCollection.TCollection_ExtendedString, theAppendMode: bool) -> nanoocp.PCDM.PCDM_ReaderStatus: ...

    @overload
    def CanRetrieve(self, theFolder: nanoocp.TCollection.TCollection_ExtendedString, theName: nanoocp.TCollection.TCollection_ExtendedString, theVersion: nanoocp.TCollection.TCollection_ExtendedString, theAppendMode: bool) -> nanoocp.PCDM.PCDM_ReaderStatus: ...

    def GetRetrieveStatus(self) -> nanoocp.PCDM.PCDM_ReaderStatus:
        """Checks status after Retrieve"""

    def Read(self, theIStream: BinaryIO, theFilter: nanoocp.PCDM.PCDM_ReaderFilter | None = None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.CDM.CDM_Document:
        """
        Reads theDocument from standard SEEKABLE stream theIStream,
        the stream should support SEEK functionality
        """

    def ReaderFromFormat(self, aFormat: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.PCDM.PCDM_Reader:
        """
        Returns instance of read driver for specified format.

        Default implementation uses plugin mechanism to load reader dynamically.
        For this to work, application resources should define GUID of
        the plugin as value of [Format].RetrievalPlugin, and "Plugin"
        resource should define name of plugin library to be loaded as
        value of [GUID].Location. Plugin library should provide
        method PLUGINFACTORY returning instance of the reader for the
        same GUID (see Plugin_Macro.hxx).

        In case if reader is not available, will raise Standard_NoSuchObject
        or other exception if raised by plugin loader.
        """

    def WriterFromFormat(self, aFormat: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.PCDM.PCDM_StorageDriver:
        """
        Returns instance of storage driver for specified format.

        Default implementation uses plugin mechanism to load driver dynamically.
        For this to work, application resources should define GUID of
        the plugin as value of [Format].StoragePlugin, and "Plugin"
        resource should define name of plugin library to be loaded as
        value of [GUID].Location. Plugin library should provide
        method PLUGINFACTORY returning instance of the reader for the
        same GUID (see Plugin_Macro.hxx).

        In case if driver is not available, will raise Standard_NoSuchObject
        or other exception if raised by plugin loader.
        """

    def Format(self, aFileName: nanoocp.TCollection.TCollection_ExtendedString, theFormat: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        try to retrieve a Format directly in the file or in
        application resource by using extension.
        returns True if found
        """

    def DefaultFolder(self) -> str: ...

    def SetDefaultFolder(self, aFolder: str) -> bool: ...

    def MetaDataDriver(self) -> CDF_MetaDataDriver:
        """returns MetaDatdDriver of this application"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @property
    def myMetaDataDriver(self) -> CDF_MetaDataDriver: ...

    @myMetaDataDriver.setter
    def myMetaDataDriver(self, arg: CDF_MetaDataDriver, /) -> None: ...

    @property
    def myDirectory(self) -> CDF_Directory: ...

    @myDirectory.setter
    def myDirectory(self, arg: CDF_Directory, /) -> None: ...

class CDF_Directory(nanoocp.Standard.Standard_Transient):
    """
    A directory is a collection of documents. There is only one instance
    of a given document in a directory.
    put.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty directory."""

    @overload
    def __init__(self, theOther: CDF_Directory) -> None: ...

    def Add(self, aDocument: nanoocp.CDM.CDM_Document | None) -> None:
        """adds a document into the directory."""

    def Remove(self, aDocument: nanoocp.CDM.CDM_Document | None) -> None:
        """removes the document."""

    def Contains(self, aDocument: nanoocp.CDM.CDM_Document | None) -> bool:
        """Returns true if the document aDocument is in the directory"""

    def Last(self) -> nanoocp.CDM.CDM_Document:
        """
        returns the last document (if any) which has been added
        in the directory.
        """

    def Length(self) -> int:
        """returns the number of documents of the directory."""

    def IsEmpty(self) -> bool:
        """returns true if the directory is empty."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class CDF_DirectoryIterator:
    @overload
    def __init__(self, aDirectory: CDF_Directory | None) -> None: ...

    @overload
    def __init__(self, theOther: CDF_DirectoryIterator) -> None: ...

    def MoreDocument(self) -> bool:
        """Returns True if there are more entries to return"""

    def NextDocument(self) -> None:
        """
        Go to the next entry
        (if there is not, Value will raise an exception)
        """

    def Document(self) -> nanoocp.CDM.CDM_Document:
        """Returns item value of current entry"""

class CDF_FWOSDriver(CDF_MetaDataDriver):
    @overload
    def __init__(self, theLookUpTable: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.CDM.CDM_MetaData]) -> None:
        """
        Initializes the MetaDatadriver connected to specified look-up table.
        Note that the created driver will keep reference to the table,
        thus it must have life time longer than this object.
        """

    @overload
    def __init__(self, theOther: CDF_FWOSDriver) -> None: ...

    def Find(self, aFolder: nanoocp.TCollection.TCollection_ExtendedString, aName: nanoocp.TCollection.TCollection_ExtendedString, aVersion: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        indicate whether a file exists corresponding to the folder and the name
        """

    def HasReadPermission(self, aFolder: nanoocp.TCollection.TCollection_ExtendedString, aName: nanoocp.TCollection.TCollection_ExtendedString, aVersion: nanoocp.TCollection.TCollection_ExtendedString) -> bool: ...

    def FindFolder(self, aFolder: nanoocp.TCollection.TCollection_ExtendedString) -> bool: ...

    def DefaultFolder(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def BuildFileName(self, aDocument: nanoocp.CDM.CDM_Document | None) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def SetName(self, aDocument: nanoocp.CDM.CDM_Document | None, aName: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class CDF_MetaDataDriverFactory(nanoocp.Standard.Standard_Transient):
    def Build(self) -> CDF_MetaDataDriver: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class CDF_Store:
    @overload
    def __init__(self, aDocument: nanoocp.CDM.CDM_Document | None) -> None:
        """creates a store list from the document of the current selection."""

    @overload
    def __init__(self, theOther: CDF_Store) -> None: ...

    def Folder(self) -> nanoocp.TCollection.TCollection_HExtendedString:
        """returns the folder in which the current document will be stored."""

    def Name(self) -> nanoocp.TCollection.TCollection_HExtendedString:
        """returns the name under which the current document will be stored"""

    def IsStored(self) -> bool:
        """returns true if the current document is already stored"""

    def IsModified(self) -> bool: ...

    def CurrentIsConsistent(self) -> bool: ...

    def IsConsistent(self) -> bool: ...

    def HasAPreviousVersion(self) -> bool: ...

    def PreviousVersion(self) -> nanoocp.TCollection.TCollection_HExtendedString: ...

    def IsMainDocument(self) -> bool:
        """
        returns true if the currentdocument is the main one, ie the document
        of the current selection.
        """

    @overload
    def SetFolder(self, aFolder: nanoocp.TCollection.TCollection_ExtendedString) -> bool: ...

    @overload
    def SetFolder(self, aFolder: str) -> bool:
        """
        defines the folder in which the document should be
        stored. returns true if the Folder exists,
        false otherwise.
        """

    @overload
    def SetName(self, aName: str) -> CDF_StoreSetNameStatus: ...

    @overload
    def SetName(self, aName: nanoocp.TCollection.TCollection_ExtendedString) -> CDF_StoreSetNameStatus:
        """defines the name under which the document should be stored."""

    def SetComment(self, aComment: str) -> None: ...

    def Comment(self) -> nanoocp.TCollection.TCollection_HExtendedString: ...

    def RecheckName(self) -> CDF_StoreSetNameStatus:
        """
        defines the name under which the document should be stored.
        uses for example after modification of the folder.
        """

    def SetPreviousVersion(self, aPreviousVersion: str) -> bool: ...

    def Realize(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    def Path(self) -> str:
        """returns the complete path of the created meta-data."""

    def MetaDataPath(self) -> nanoocp.TCollection.TCollection_HExtendedString:
        """
        returns the path of the previous store is the object
        is already stored, otherwise an empty string;
        """

    def Description(self) -> nanoocp.TCollection.TCollection_HExtendedString:
        """returns the description of the format of the main object."""

    def SetCurrent(self, aPresentation: str) -> None: ...

    def SetMain(self) -> None:
        """
        the two following methods can be used just after
        Realize or Import -- method to know if
        these methods worked correctly, and if not why.
        """

    def StoreStatus(self) -> nanoocp.PCDM.PCDM_StoreStatus: ...

    def AssociatedStatusText(self) -> str: ...

class CDF_StoreList(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, aDocument: nanoocp.CDM.CDM_Document | None) -> None: ...

    @overload
    def __init__(self, theOther: CDF_StoreList) -> None: ...

    def __iter__(self) -> CDF_StoreList:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.CDM.CDM_Document:
        """Python addition: see __iter__."""

    def IsConsistent(self) -> bool: ...

    def Store(self, aStatusAssociatedText: nanoocp.TCollection.TCollection_ExtendedString, theRange: nanoocp.Message.Message_ProgressRange = ...) -> tuple[nanoocp.PCDM.PCDM_StoreStatus, nanoocp.CDM.CDM_MetaData]:
        """
        stores each object of the storelist in the reverse
        order of which they had been added.
        """

    def Init(self) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Value(self) -> nanoocp.CDM.CDM_Document: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
