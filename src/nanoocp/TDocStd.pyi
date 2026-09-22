"""OCCT package TDocStd (toolkit TKLCAF)"""

import enum
from typing import BinaryIO, overload

import nanoocp.CDF
import nanoocp.CDM
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.PCDM
import nanoocp.Resource
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDF


class TDocStd_FormatVersion(enum.IntEnum):
    """
    Storage format versions of OCAF documents in XML and binary file formats.

    OCAF document file format evolves and a new version number indicates each improvement of the
    format. This enumeration lists all versions of an OCAF document. TDocStd_FormatVersion_CURRENT
    value refers to the last file format version. By default, Open CASCADE Technology writes new
    documents using the last file format version. The last version of Open CASCADE Technology is
    able to read old documents of any version. However, a previous version of Open CASCADE
    Technology may not be able to read a new document. In this case use the method
    ChangeStorageFormatVersion() from TDocStd_Document to change the file format version. Then, save
    the document by means of SaveAs() from TDocStd_Application.

    If it is necessary to improve an XML or binary file format of OCAF document, follow please the
    next steps:
    - increment the file format version in this enumeration. Put a reference to the last file format
    version by means of TDocStd_FormatVersion_CURRENT.
    - introduce the improvement in OCAF attribute storage and retrieval drivers, if necessary.
    As an example, please consider the file XmlMDataStd_TreeNodeDriver.cxx.
    - test the improvement on current file format version and on the previous one.
    """

    TDocStd_FormatVersion_VERSION_2 = 2

    TDocStd_FormatVersion_VERSION_3 = 3

    TDocStd_FormatVersion_VERSION_4 = 4

    TDocStd_FormatVersion_VERSION_5 = 5

    TDocStd_FormatVersion_VERSION_6 = 6

    TDocStd_FormatVersion_VERSION_7 = 7

    TDocStd_FormatVersion_VERSION_8 = 8

    TDocStd_FormatVersion_VERSION_9 = 9

    TDocStd_FormatVersion_VERSION_10 = 10

    TDocStd_FormatVersion_VERSION_11 = 11

    TDocStd_FormatVersion_VERSION_12 = 12

    TDocStd_FormatVersion_CURRENT = 12

TDocStd_FormatVersion_VERSION_2: TDocStd_FormatVersion = ...

TDocStd_FormatVersion_VERSION_3: TDocStd_FormatVersion = ...

TDocStd_FormatVersion_VERSION_4: TDocStd_FormatVersion = ...

TDocStd_FormatVersion_VERSION_5: TDocStd_FormatVersion = ...

TDocStd_FormatVersion_VERSION_6: TDocStd_FormatVersion = ...

TDocStd_FormatVersion_VERSION_7: TDocStd_FormatVersion = ...

TDocStd_FormatVersion_VERSION_8: TDocStd_FormatVersion = ...

TDocStd_FormatVersion_VERSION_9: TDocStd_FormatVersion = ...

TDocStd_FormatVersion_VERSION_10: TDocStd_FormatVersion = ...

TDocStd_FormatVersion_VERSION_11: TDocStd_FormatVersion = ...

TDocStd_FormatVersion_VERSION_12: TDocStd_FormatVersion = ...

TDocStd_FormatVersion_CURRENT: TDocStd_FormatVersion = ...

TDocStd_FormatVersion_LOWER: int = 2

TDocStd_FormatVersion_UPPER: int = 12

class TDocStd:
    """
    This package define CAF main classes.

    * The standard application root class

    * The standard document which contains data

    * The external reference mechanism between documents

    * Attributes for Document management
    Standard documents offer you a ready-to-use
    document containing a TDF-based data
    structure. The documents themselves are
    contained in a class inheriting from
    TDocStd_Application which manages creation,
    storage and retrieval of documents.
    You can implement undo and redo in your
    document, and refer from the data framework of
    one document to that of another one. This is
    done by means of external link attributes, which
    store the path and the entry of external links. To
    sum up, standard documents alone provide
    access to the data framework. They also allow
    you to:
    - Update external links
    - Manage the saving and opening of data
    - Manage undo/redo functionality.
    Note
    For information on the relations between this
    component of OCAF and the others, refer to the
    OCAF User's Guide.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDocStd) -> None: ...

    @staticmethod
    def IDList(anIDList: nanoocp.NCollection.NCollection_List[nanoocp.Standard.Standard_GUID]) -> None:
        """
        specific GUID of this package
        =============================
        Appends to <anIDList> the list of the attributes
        IDs of this package. CAUTION: <anIDList> is NOT
        cleared before use.
        """

class TDocStd_Document(nanoocp.CDM.CDM_Document):
    """
    The contents of a TDocStd_Application, a
    document is a container for a data framework
    composed of labels and attributes. As such,
    TDocStd_Document is the entry point into the data framework.
    To gain access to the data, you create a document as follows:
    occ::handle<TDocStd_Document> MyDF = new TDocStd_Document
    The document also allows you to manage:
    -   modifications, providing Undo and Redo functions.
    -   command transactions.
    Warning: The only data saved is the framework (TDF_Data)
    """

    def __init__(self, astorageformat: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Constructs a document object defined by the
        string astorageformat.
        If a document is created outside of an application using this constructor, it must be
        managed by a Handle. Otherwise memory problems could appear: call of
        TDocStd_Owner::GetDocument creates a occ::handle<TDocStd_Document>, so, releasing it will
        produce a crash.
        """

    @staticmethod
    def Get(L: nanoocp.TDF.TDF_Label) -> TDocStd_Document:
        """
        Will Abort any execution, clear fields
        returns the document which contains <L>. raises an
        exception if the document is not found.
        """

    def IsSaved(self) -> bool:
        """the document is saved in a file."""

    def IsChanged(self) -> bool:
        """
        returns True if document differs from the state of last saving.
        this method have to be called only working in the transaction mode
        """

    def SetSaved(self) -> None:
        """This method have to be called to show document that it has been saved"""

    def SetSavedTime(self, theTime: int) -> None:
        """
        Say to document what it is not saved.
        Use value, returned earlier by GetSavedTime().
        """

    def GetSavedTime(self) -> int:
        """Returns value of <mySavedTime> to be used later in SetSavedTime()"""

    def GetName(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """raise if <me> is not saved."""

    def GetPath(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        returns the OS path of the file, in which one <me> is
        saved. Raise an exception if <me> is not saved.
        """

    def SetData(self, data: nanoocp.TDF.TDF_Data | None) -> None: ...

    def GetData(self) -> nanoocp.TDF.TDF_Data: ...

    def Main(self) -> nanoocp.TDF.TDF_Label:
        """
        Returns the main label in this data framework.
        By definition, this is the label with the entry 0:1.
        """

    def IsEmpty(self) -> bool:
        """Returns True if the main label has no attributes"""

    def IsValid(self) -> bool:
        """
        Returns False if the document has been modified
        but not recomputed.
        """

    def SetModified(self, L: nanoocp.TDF.TDF_Label) -> None:
        """
        Notify the label as modified, the Document becomes UnValid.
        returns True if <L> has been notified as modified.
        """

    def PurgeModified(self) -> None:
        """
        Remove all modifications. After this call The document
        becomesagain Valid.
        """

    def GetModified(self) -> nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]:
        """
        Returns the labels which have been modified in
        this document.
        """

    def NewCommand(self) -> None:
        """Launches a new command. This command may be undone."""

    def HasOpenCommand(self) -> bool:
        """returns True if a Command transaction is open in the current ."""

    def OpenCommand(self) -> None:
        """
        Opens a new command transaction in this document.
        You can use HasOpenCommand to see whether a command is already open.
        Exceptions
        Standard_DomainError if a command is already open in this document.
        """

    def CommitCommand(self) -> bool:
        """
        Commits documents transactions and fills the
        transaction manager with documents that have
        been changed during the transaction.
        If no command transaction is open, nothing is done.
        Returns True if a new delta has been added to myUndos.
        """

    def AbortCommand(self) -> None:
        """
        Abort the Command transaction. Does nothing If there is
        no Command transaction open.
        """

    def GetUndoLimit(self) -> int:
        """The current limit on the number of undos"""

    def SetUndoLimit(self, L: int) -> None:
        """
        Set the limit on the number of Undo Delta stored 0
        will disable Undo on the document A negative value
        means no limit. Note that by default Undo is disabled.
        Enabling it will take effect with the next call to
        NewCommand. Of course this limit is the same for Redo
        """

    def ClearUndos(self) -> None:
        """Remove all stored Undos and Redos"""

    def ClearRedos(self) -> None:
        """Remove all stored Redos"""

    def GetAvailableUndos(self) -> int:
        """
        Returns the number of undos stored in this
        document. If this figure is greater than 0, the method Undo
        can be used.
        """

    def Undo(self) -> bool:
        """
        Will UNDO one step, returns False if no undo was
        done (Undos == 0).
        Otherwise, true is returned and one step in the
        list of undoes is undone.
        """

    def GetAvailableRedos(self) -> int:
        """
        Returns the number of redos stored in this
        document. If this figure is greater than 0, the method Redo
        can be used.
        """

    def Redo(self) -> bool:
        """
        Will REDO one step, returns False if no redo was
        done (Redos == 0).
        Otherwise, true is returned, and one step in the list of redoes is done again.
        """

    def GetUndos(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Delta]: ...

    def GetRedos(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Delta]: ...

    def RemoveFirstUndo(self) -> None:
        """
        Removes the first undo in the list of document undos.
        It is used in the application when the undo limit is exceed.
        """

    def InitDeltaCompaction(self) -> bool:
        """
        Initializes the procedure of delta compaction
        Returns false if there is no delta to compact
        Marks the last delta as a "from" delta
        """

    def PerformDeltaCompaction(self) -> bool:
        """
        Performs the procedure of delta compaction
        Makes all deltas starting from "from" delta
        till the last one to be one delta.
        """

    def UpdateReferences(self, aDocEntry: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Set modifications on labels impacted by external
        references to the entry. The document becomes invalid
        and must be recomputed.
        """

    def Recompute(self) -> None:
        """
        Recompute if the document was not valid and propagate
        the recorded modification.
        """

    def StorageFormat(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def SetEmptyLabelsSavingMode(self, isAllowed: bool) -> None:
        """
        Sets saving mode for empty labels. If true, empty labels will be saved.
        """

    def EmptyLabelsSavingMode(self) -> bool:
        """Returns saving mode for empty labels."""

    def ChangeStorageFormat(self, newStorageFormat: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """methods for the nested transaction mode"""

    def SetNestedTransactionMode(self, isAllowed: bool = True) -> None:
        """Sets nested transaction mode if isAllowed == true"""

    def IsNestedTransactionMode(self) -> bool:
        """Returns true if mode is set"""

    def SetModificationMode(self, theTransactionOnly: bool) -> None:
        """if theTransactionOnly is True changes is denied outside transactions"""

    def ModificationMode(self) -> bool:
        """returns True if changes allowed only inside transactions"""

    def BeforeClose(self) -> None:
        """Prepares document for closing"""

    def StorageFormatVersion(self) -> TDocStd_FormatVersion:
        """Returns version of the format to be used to store the document"""

    def ChangeStorageFormatVersion(self, theVersion: TDocStd_FormatVersion) -> None:
        """Sets version of the format to be used to store the document"""

    @staticmethod
    def CurrentStorageFormatVersion() -> TDocStd_FormatVersion:
        """Returns current storage format version of the document."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDocStd_Application(nanoocp.CDF.CDF_Application):
    """
    The abstract root class for all application classes.
    They are in charge of:
    -   Creating documents
    -   Storing documents and retrieving them
    -   Initializing document views.
    To create a useful OCAF-based application, you
    derive a class from Application and implement
    the methods below. You will have to redefine the
    deferred (virtual) methods Formats,
    InitDocument, and Resources, and override others.
    The application is a container for a document,
    which in its turn is the container of the data
    framework made up of labels and attributes.
    Besides furnishing a container for documents,
    TDocStd_Application provides the following
    services for them:
    -   Creation of new documents
    -   Activation of documents in sessions of an application
    -   Storage and retrieval of documents
    -   Initialization of document views.
    Note:
    If a client needs detailed information concerning
    the events during the Open/Store operation, a MessageDriver
    based on Message_PrinterOStream may be used. In case of need client
    can implement his own version inheriting from Message_Printer class
    and add it to the Messenger.
    Also the trace level of messages can be tuned by setting trace level (SetTraceLevel (Gravity ))
    for the used Printer. By default, trace level is Message_Info, so that all messages are output.
    """

    @overload
    def __init__(self) -> None:
        """Constructs the new instance and registers it in CDM_Session"""

    @overload
    def __init__(self, theOther: TDocStd_Application) -> None: ...

    def IsDriverLoaded(self) -> bool:
        """
        Check if meta data driver was successfully loaded
        by the application constructor
        """

    def Resources(self) -> nanoocp.Resource.Resource_Manager:
        """
        Returns resource manager defining supported persistent formats.

        Default implementation loads resource file with name ResourcesName(),
        unless field myResources is already initialized (either by
        previous call or in any other way).

        The resource manager should define:

        * Format name for each file extension supported:
        - [Extension].FileFormat: [Format]

        * For each format supported (as returned by Formats()),
        its extension, description string, and (when applicable)
        GUIDs of storage and retrieval plugins:
        - [Format].Description: [Description]
        - [Format].FileExtension: [Extension]
        - [Format].RetrievalPlugin: [GUID] (optional)
        - [Format].StoragePlugin: [GUID] (optional)
        """

    def ResourcesName(self) -> str:
        """
        Returns the name of the file containing the
        resources of this application, for support of legacy
        method of loading formats data from resource files.

        Method DefineFormat() can be used to define all necessary
        parameters explicitly without actually using resource files.

        In a resource file, the application associates the
        schema name of the document with the storage and
        retrieval plug-ins that are to be loaded for each
        document. On retrieval, the application reads the
        schema name in the heading of the CSF file and
        loads the plug-in indicated in the resource file.
        This plug-in instantiates the actual driver for
        transient-persistent conversion.
        Your application can bring this process into play
        by defining a class which inherits
        CDF_Application and redefines the function
        which returns the appropriate resources file. At
        this point, the function Retrieve and the class
        CDF_Store can be called. This allows you to
        deal with storage and retrieval of - as well as
        copying and pasting - documents.
        To implement a class like this, several virtual
        functions should be redefined. In particular, you
        must redefine the abstract function Resources
        inherited from the superclass CDM_Application.

        Default implementation returns empty string.
        """

    def DefineFormat(self, theFormat: nanoocp.TCollection.TCollection_AsciiString, theDescription: nanoocp.TCollection.TCollection_AsciiString, theExtension: nanoocp.TCollection.TCollection_AsciiString, theReader: nanoocp.PCDM.PCDM_RetrievalDriver | None, theWriter: nanoocp.PCDM.PCDM_StorageDriver | None) -> None:
        """
        Sets up resources and registers read and storage drivers for
        the specified format.

        @param theFormat - unique name for the format, used to identify it.
        @param theDescription - textual description of the format.
        @param theExtension - extension of the files in that format.
        The same extension can be used by several formats.
        @param theReader - instance of the read driver for the format.
        Null value is allowed (no possibility to read).
        @param theWriter - instance of the write driver for the format.
        Null value is allowed (no possibility to write).
        """

    def ReadingFormats(self, theFormats: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Returns the sequence of reading formats supported by the application.

        @param theFormats - sequence of reading formats. Output parameter.
        """

    def WritingFormats(self, theFormats: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Returns the sequence of writing formats supported by the application.

        @param theFormats - sequence of writing formats. Output parameter.
        """

    def NbDocuments(self) -> int:
        """
        returns the number of documents handled by the current applicative session.
        """

    def GetDocument(self, index: int) -> TDocStd_Document:
        """
        Returns the document at the given 1-based index.
        The index is any integer between 1 and NbDocuments().
        @param[in] index 1-based document index
        @return handle to the document
        """

    def GetDocument__TDocStd_Document(self, index: int) -> TDocStd_Document:
        """
        GetDocument__TDocStd_Document: the C++ overload GetDocument(const int, occ::handle<TDocStd_Document> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use GetDocument() returning handle by value instead

        @deprecated Use GetDocument() returning handle by value instead.
        """

    def NewDocument__CDM_Document(self, format: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.CDM.CDM_Document:
        """
        NewDocument__CDM_Document: the C++ overload NewDocument(const TCollection_ExtendedString &, occ::handle<CDM_Document> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Constructs the empty new document aDoc.
        This document will have the format format.
        If InitDocument is redefined for a specific
        application, the new document is handled by the
        applicative session.
        """

    def NewDocument__TDocStd_Document(self, format: nanoocp.TCollection.TCollection_ExtendedString) -> TDocStd_Document:
        """
        NewDocument__TDocStd_Document: the C++ overload NewDocument(const TCollection_ExtendedString &, occ::handle<TDocStd_Document> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        A non-virtual method taking a TDocStd_Documment object as an input.
        Internally it calls a virtual method NewDocument() with CDM_Document object.
        """

    def InitDocument(self, aDoc: nanoocp.CDM.CDM_Document | None) -> None:
        """
        Initialize the document aDoc for the applicative session.
        This virtual function is called by NewDocument
        and is to be redefined for each specific application.
        Modified flag (different of disk version)
        =============
        to open/save a document
        =======================
        """

    def Close(self, aDoc: TDocStd_Document | None) -> None:
        """
        Close the given document. the document is not any more
        handled by the applicative session.
        """

    def IsInSession(self, path: nanoocp.TCollection.TCollection_ExtendedString) -> int:
        """
        Returns an index for the document found in the
        path path in this applicative session.
        If the returned value is 0, the document is not
        present in the applicative session.
        This method can be used for the interactive part
        of an application. For instance, on a call to
        Open, the document to be opened may already
        be in memory. IsInSession checks to see if this
        is the case. Open can be made to depend on
        the value of the index returned: if IsInSession
        returns 0, the document is opened; if it returns
        another value, a message is displayed asking the
        user if he wants to override the version of the
        document in memory.
        Example:
        int insession = A->IsInSession(aDoc);
        if (insession > 0) {
        std::cout << "document " << insession << " is already in session" << std::endl;
        return 0;
        }
        """

    @overload
    def Open(self, thePath: nanoocp.TCollection.TCollection_ExtendedString, theFilter: nanoocp.PCDM.PCDM_ReaderFilter | None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> tuple[nanoocp.PCDM.PCDM_ReaderStatus, TDocStd_Document]:
        """
        Retrieves the document from specified file.
        In order not to override a version of the document which is already in memory,
        this method can be made to depend on the value returned by IsInSession.
        @param[in]  thePath   file path to open
        @param[out] theDoc    result document
        @param[in]  theFilter optional filter to skip attributes or parts of the retrieved tree
        @param[in]  theRange  optional progress indicator
        @return reading status
        """

    @overload
    def Open(self, thePath: nanoocp.TCollection.TCollection_ExtendedString, theRange: nanoocp.Message.Message_ProgressRange = ...) -> tuple[nanoocp.PCDM.PCDM_ReaderStatus, TDocStd_Document]:
        """
        Retrieves the document from specified file.
        In order not to override a version of the document which is already in memory,
        this method can be made to depend on the value returned by IsInSession.
        @param[in]  thePath  file path to open
        @param[out] theDoc   result document
        @param[in]  theRange optional progress indicator
        @return reading status
        """

    @overload
    def Open(self, theIStream: BinaryIO, theFilter: nanoocp.PCDM.PCDM_ReaderFilter | None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> tuple[nanoocp.PCDM.PCDM_ReaderStatus, TDocStd_Document]:
        """
        Retrieves document from standard stream.
        @param[in,out] theIStream input seekable stream
        @param[out]    theDoc     result document
        @param[in]     theFilter  optional filter to skip attributes or parts of the retrieved tree
        @param[in]     theRange   optional progress indicator
        @return reading status
        """

    @overload
    def Open(self, theIStream: BinaryIO, theRange: nanoocp.Message.Message_ProgressRange = ...) -> tuple[nanoocp.PCDM.PCDM_ReaderStatus, TDocStd_Document]:
        """
        Retrieves document from standard stream.
        @param[in,out] theIStream input seekable stream
        @param[out]    theDoc     result document
        @param[in]     theRange   optional progress indicator
        @return reading status
        """

    @overload
    def SaveAs(self, theDoc: TDocStd_Document | None, path: nanoocp.TCollection.TCollection_ExtendedString, theRange: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.PCDM.PCDM_StoreStatus:
        """
        Save the active document in the file <name> in the
        path <path>. overwrites the file if it already exists.
        """

    @overload
    def SaveAs(self, theDoc: TDocStd_Document | None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> tuple[nanoocp.PCDM.PCDM_StoreStatus, bytes]:
        """
        Save theDoc to standard SEEKABLE stream theOStream.
        the stream should support SEEK functionality
        """

    @overload
    def SaveAs(self, theDoc: TDocStd_Document | None, path: nanoocp.TCollection.TCollection_ExtendedString, theStatusMessage: nanoocp.TCollection.TCollection_ExtendedString, theRange: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.PCDM.PCDM_StoreStatus:
        """
        Save the active document in the file <name> in the
        path <path>. overwrite the file if it already exists.
        """

    @overload
    def Save(self, theDoc: TDocStd_Document | None, theRange: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.PCDM.PCDM_StoreStatus:
        """
        Save aDoc active document.
        Exceptions:
        Standard_NotImplemented if the document
        was not retrieved in the applicative session by using Open.
        """

    @overload
    def Save(self, theDoc: TDocStd_Document | None, theStatusMessage: nanoocp.TCollection.TCollection_ExtendedString, theRange: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.PCDM.PCDM_StoreStatus:
        """Save the document overwriting the previous file"""

    def SaveAs__bytes(self, theDoc: TDocStd_Document | None, theStatusMessage: nanoocp.TCollection.TCollection_ExtendedString, theRange: nanoocp.Message.Message_ProgressRange = ...) -> tuple[nanoocp.PCDM.PCDM_StoreStatus, bytes]:
        """
        SaveAs__bytes: the C++ overload SaveAs(const occ::handle<TDocStd_Document> &, Standard_OStream &, TCollection_ExtendedString &, const Message_ProgressRange &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Save theDoc TO standard SEEKABLE stream theOStream.
        the stream should support SEEK functionality
        """

    def OnOpenTransaction(self, theDoc: TDocStd_Document | None) -> None:
        """Notification that is fired at each OpenTransaction event."""

    def OnCommitTransaction(self, theDoc: TDocStd_Document | None) -> None:
        """Notification that is fired at each CommitTransaction event."""

    def OnAbortTransaction(self, theDoc: TDocStd_Document | None) -> None:
        """Notification that is fired at each AbortTransaction event."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDocStd_ApplicationDelta(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDocStd_ApplicationDelta) -> None: ...

    def GetDocuments(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.TDocStd.TDocStd_Document]: ...

    def GetName(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def SetName(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDocStd_CompoundDelta(nanoocp.TDF.TDF_Delta):
    """
    A delta set is available at <aSourceTime>. If
    applied, it restores the TDF_Data in the state it
    was at <aTargetTime>.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a compound delta.
        Validates <me> at <aBeginTime>. If applied, it
        restores the TDF_Data in the state it was at
        <anEndTime>. Reserved to TDF_Data.
        """

    @overload
    def __init__(self, theOther: TDocStd_CompoundDelta) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDocStd_Context:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDocStd_Context) -> None: ...

    def SetModifiedReferences(self, Mod: bool) -> None: ...

    def ModifiedReferences(self) -> bool: ...

class TDocStd_Modified(nanoocp.TDF.TDF_Attribute):
    """
    Transient attribute which register modified labels.
    This attribute is attached to root label.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDocStd_Modified) -> None: ...

    @staticmethod
    def IsEmpty_s(access: nanoocp.TDF.TDF_Label) -> bool:
        """
        API class methods
        =================
        """

    @staticmethod
    def Add(alabel: nanoocp.TDF.TDF_Label) -> bool: ...

    @staticmethod
    def Remove(alabel: nanoocp.TDF.TDF_Label) -> bool: ...

    @staticmethod
    def Contains(alabel: nanoocp.TDF.TDF_Label) -> bool: ...

    @staticmethod
    def Get_s(access: nanoocp.TDF.TDF_Label) -> nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]:
        """if <IsEmpty> raise an exception."""

    @staticmethod
    def Clear_s(access: nanoocp.TDF.TDF_Label) -> None:
        """remove all modified labels. becomes empty"""

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        Modified methods
        ================
        """

    def IsEmpty(self) -> bool: ...

    def Clear(self) -> None: ...

    def AddLabel(self, L: nanoocp.TDF.TDF_Label) -> bool:
        """add <L> as modified"""

    def RemoveLabel(self, L: nanoocp.TDF.TDF_Label) -> bool:
        """remove <L> as modified"""

    def Get(self) -> nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]:
        """returns modified label map"""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDocStd_MultiTransactionManager(nanoocp.Standard.Standard_Transient):
    """
    Class for synchronization of transactions within multiple documents.
    Each transaction of this class involvess one transaction in each modified document.

    The documents to be synchronized should be added explicitly to
    the manager; then its interface is used to ensure that all transactions
    (Open/Commit, Undo/Redo) are performed synchronously in all managed documents.

    The current implementation does not support nested transactions
    on multitransaction manager level. It only sets the flag enabling
    or disabling nested transactions in all its documents, so that
    a nested transaction can be opened for each particular document
    with TDocStd_Document class interface.

    NOTE: When you invoke CommitTransaction of multi transaction
    manager, all nested transaction of its documents will be closed (committed).
    """

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: TDocStd_MultiTransactionManager) -> None: ...

    def SetUndoLimit(self, theLimit: int) -> None:
        """Sets undo limit for the manager and all documents."""

    def GetUndoLimit(self) -> int:
        """Returns undo limit for the manager."""

    def Undo(self) -> None:
        """
        Undoes the current transaction of the manager.
        It calls the Undo () method of the document being
        on top of the manager list of undos (list.First())
        and moves the list item to the top of the list of manager
        redos (list.Prepend(item)).
        """

    def Redo(self) -> None:
        """
        Redoes the current transaction of the application. It calls
        the Redo () method of the document being on top of the
        manager list of redos (list.First()) and moves the list
        item to the top of the list of manager undos (list.Prepend(item)).
        """

    def GetAvailableUndos(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.TDocStd.TDocStd_ApplicationDelta]:
        """Returns available manager undos."""

    def GetAvailableRedos(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.TDocStd.TDocStd_ApplicationDelta]:
        """Returns available manager redos."""

    def OpenCommand(self) -> None:
        """
        Opens transaction in each document and sets the flag that
        transaction is opened. If there are already opened transactions in the documents,
        these transactions will be aborted before opening new ones.
        """

    def AbortCommand(self) -> None:
        """
        Unsets the flag of started manager transaction and aborts
        transaction in each document.
        """

    @overload
    def CommitCommand(self) -> bool:
        """
        Commits transaction in all documents and fills the transaction manager
        with the documents that have been changed during the transaction.
        Returns True if new data has been added to myUndos.
        NOTE: All nested transactions in the documents will be committed.
        """

    @overload
    def CommitCommand(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        Makes the same steps as the previous function but defines the name for transaction.
        Returns True if new data has been added to myUndos.
        """

    def HasOpenCommand(self) -> bool:
        """Returns true if a transaction is opened."""

    def RemoveLastUndo(self) -> None:
        """
        Removes undo information from the list of undos of the manager and
        all documents which have been modified during the transaction.
        """

    def DumpTransaction(self) -> str:
        """Dumps transactions in undos and redos"""

    def AddDocument(self, theDoc: TDocStd_Document | None) -> None:
        """
        Adds the document to the transaction manager and
        checks if it has been already added
        """

    def RemoveDocument(self, theDoc: TDocStd_Document | None) -> None:
        """Removes the document from the transaction manager."""

    def Documents(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.TDocStd.TDocStd_Document]:
        """Returns the added documents to the transaction manager."""

    def SetNestedTransactionMode(self, isAllowed: bool = True) -> None:
        """
        Sets nested transaction mode if isAllowed == true
        NOTE: field myIsNestedTransactionMode exists only for synchronization
        between several documents and has no effect on transactions
        of multitransaction manager.
        """

    def IsNestedTransactionMode(self) -> bool:
        """
        Returns true if NestedTransaction mode is set.
        Methods for protection of changes outside transactions
        """

    def SetModificationMode(self, theTransactionOnly: bool) -> None:
        """
        If theTransactionOnly is True, denies all changes outside transactions.
        """

    def ModificationMode(self) -> bool:
        """Returns True if changes are allowed only inside transactions."""

    def ClearUndos(self) -> None:
        """Clears undos in the manager and in documents."""

    def ClearRedos(self) -> None:
        """Clears redos in the manager and in documents."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDocStd_Owner(nanoocp.TDF.TDF_Attribute):
    """
    This attribute located at the root label of the
    framework contains a back reference to the owner
    TDocStd_Document, providing access to the document
    from any label. private class Owner;
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDocStd_Owner) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        """

    @overload
    @staticmethod
    def SetDocument_s(indata: nanoocp.TDF.TDF_Data | None, doc: TDocStd_Document | None) -> None: ...

    @overload
    @staticmethod
    def SetDocument_s(indata: nanoocp.TDF.TDF_Data | None, doc: TDocStd_Document) -> None: ...

    @staticmethod
    def GetDocument_s(ofdata: nanoocp.TDF.TDF_Data | None) -> TDocStd_Document:
        """
        Owner methods
        ===============
        """

    @overload
    def SetDocument(self, document: TDocStd_Document | None) -> None: ...

    @overload
    def SetDocument(self, document: TDocStd_Document) -> None: ...

    def GetDocument(self) -> TDocStd_Document: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDocStd_PathParser:
    """parse an OS path"""

    @overload
    def __init__(self, path: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    @overload
    def __init__(self, theOther: TDocStd_PathParser) -> None: ...

    def Parse(self) -> None: ...

    def Trek(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def Name(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def Extension(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def Path(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def Length(self) -> int: ...

class TDocStd_XLink(nanoocp.TDF.TDF_Attribute):
    """
    An attribute to store the path and the entry of
    external links.
    These refer from one data structure to a data
    structure in another document.
    """

    @overload
    def __init__(self) -> None:
        """Initializes fields."""

    @overload
    def __init__(self, theOther: TDocStd_XLink) -> None: ...

    @staticmethod
    def Set(atLabel: nanoocp.TDF.TDF_Label) -> TDocStd_XLink:
        """Sets an empty external reference, at the label aLabel."""

    def Update(self) -> nanoocp.TDF.TDF_Reference:
        """Updates the data referenced in this external link attribute."""

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the attribute."""

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns the GUID for external links."""

    @overload
    def DocumentEntry(self, aDocEntry: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Sets the name aDocEntry for the external
        document in this external link attribute.
        """

    @overload
    def DocumentEntry(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the contents of the document identified by aDocEntry.
        aDocEntry provides external data to this external link attribute.
        """

    @overload
    def LabelEntry(self, aLabel: nanoocp.TDF.TDF_Label) -> None:
        """
        Sets the label entry for this external link attribute with the label aLabel.
        aLabel pilots the importation of data from the document entry.
        """

    @overload
    def LabelEntry(self, aLabEntry: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Sets the label entry for this external link attribute
        as a document identified by aLabEntry.
        """

    @overload
    def LabelEntry(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the contents of the field <myLabelEntry>."""

    def AfterAddition(self) -> None:
        """
        Updates the XLinkRoot attribute by adding <me>
        to its list.
        """

    def BeforeRemoval(self) -> None:
        """
        Updates the XLinkRoot attribute by removing <me>
        from its list.
        """

    def BeforeUndo(self, anAttDelta: nanoocp.TDF.TDF_AttributeDelta | None, forceIt: bool = False) -> bool:
        """Something to do before applying <anAttDelta>."""

    def AfterUndo(self, anAttDelta: nanoocp.TDF.TDF_AttributeDelta | None, forceIt: bool = False) -> bool:
        """Something to do after applying <anAttDelta>."""

    def BackupCopy(self) -> nanoocp.TDF.TDF_Attribute:
        """
        Returns a null handle. Raise always for it is
        nonsense to use this method.
        """

    def Restore(self, anAttribute: nanoocp.TDF.TDF_Attribute | None) -> None:
        """Does nothing."""

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """Returns a null handle."""

    def Paste(self, intoAttribute: nanoocp.TDF.TDF_Attribute | None, aRelocationTable: nanoocp.TDF.TDF_RelocationTable | None) -> None:
        """Does nothing."""

    def Dump(self) -> str:
        """Dumps the attribute on <aStream>."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDocStd_XLinkIterator:
    """
    Iterates on Reference attributes.
    This is an iterator giving all the external references
    of a Document.
    """

    @overload
    def __init__(self) -> None:
        """Returns an empty iterator;"""

    @overload
    def __init__(self, D: TDocStd_Document | None) -> None:
        """Creates an iterator on Reference of <D>."""

    @overload
    def __init__(self, theOther: TDocStd_XLinkIterator) -> None: ...

    def Initialize(self, D: TDocStd_Document | None) -> None:
        """Restarts an iteration with <D>."""

    def More(self) -> bool:
        """
        Returns True if there is a current Item in the
        iteration.
        """

    def Next(self) -> None:
        """Move to the next item; raises if there is no more item."""

    def Value(self) -> TDocStd_XLink:
        """Returns the current item; a null handle if there is none."""

class TDocStd_XLinkRoot(nanoocp.TDF.TDF_Attribute):
    """
    This attribute is the root of all external
    references contained in a Data from TDF. Only one
    instance of this class is added to the TDF_Data
    root label. Starting from this attribute all the
    Reference are linked together, to be found easily.
    """

    def __init__(self, theOther: TDocStd_XLinkRoot) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns the ID: 2a96b61d-ec8b-11d0-bee7-080009dc3333"""

    @staticmethod
    def Set(aDF: nanoocp.TDF.TDF_Data | None) -> TDocStd_XLinkRoot:
        """
        Sets an empty XLinkRoot to Root or gets the
        existing one. Only one attribute per TDF_Data.
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the attribute."""

    def BackupCopy(self) -> nanoocp.TDF.TDF_Attribute:
        """Returns a null handle."""

    def Restore(self, anAttribute: nanoocp.TDF.TDF_Attribute | None) -> None:
        """Does nothing."""

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """Returns a null handle."""

    def Paste(self, intoAttribute: nanoocp.TDF.TDF_Attribute | None, aRelocationTable: nanoocp.TDF.TDF_RelocationTable | None) -> None:
        """Does nothing."""

    def Dump(self) -> str:
        """Dumps the attribute on <aStream>."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDocStd_XLinkTool:
    """
    This tool class is used to copy the content of
    source label under target label. Only child
    labels and attributes of source are copied.
    attributes located out of source scope are not
    copied by this algorithm.
    Depending of the called method an external
    reference is set in the target document to
    registered the externallink.
    Provide services to set, update and perform
    external references.
    Warning1: Nothing is provided in this class about the
    opportunity to copy, set a link or update it.
    Such decisions must be under application control.
    Warning2: If the document manages shapes, use after copy
    TNaming::ChangeShapes(target,M) to make copy of
    shapes.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDocStd_XLinkTool) -> None: ...

    def CopyWithLink(self, intarget: nanoocp.TDF.TDF_Label, fromsource: nanoocp.TDF.TDF_Label) -> None:
        """
        Copies the content of the label <fromsource> to the label <intarget>.
        The link is registered with an XLink attribute by <intarget>
        label. if the content of <fromsource> is not
        self-contained, and/or <intarget> has already an XLink
        attribute, an exception is raised.
        """

    def UpdateLink(self, L: nanoocp.TDF.TDF_Label) -> None:
        """
        Update the external reference set at <L>.
        Example
        occ::handle<TDocStd_Document> aDoc;
        if
        (!OCAFTest::GetDocument(1,aDoc)) return 1;
        occ::handle<TDataStd_Reference> aRef;
        TDocStd_XLinkTool xlinktool;
        if
        (!OCAFTest::Find(aDoc,2),TDataStd_Reference::GetID(),aRef) return 1;
        xlinktool.UpdateLink(aRef->Label());
        Exceptions
        Standard_DomainError if <L> has no XLink attribute.
        """

    def Copy(self, intarget: nanoocp.TDF.TDF_Label, fromsource: nanoocp.TDF.TDF_Label) -> None:
        """
        Copy the content of <fromsource> under
        <intarget>. No link is registered. No check is done.
        Example
        occ::handle<TDocStd_Document> DOC, XDOC;
        TDF_Label L, XL;
        TDocStd_XLinkTool xlinktool;
        xlinktool.Copy(L,XL);
        Exceptions:
        Standard_DomainError if the contents of
        fromsource are not entirely in the scope of this
        label, in other words, are not self-contained.
        !!! ==> Warning:
        If the document manages shapes use the next way:
        TDocStd_XLinkTool xlinktool;
        xlinktool.Copy(L,XL);
        NCollection_DataMap<TopoDS_Shape, TopoDS_Shape, TopTools_ShapeMapHasher> M;
        TNaming::ChangeShapes(target,M);
        """

    def IsDone(self) -> bool: ...

    def DataSet(self) -> nanoocp.TDF.TDF_DataSet: ...

    def RelocationTable(self) -> nanoocp.TDF.TDF_RelocationTable: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.TDocStd
TDocStd_SequenceOfApplicationDelta = nanoocp.NCollection.NCollection_Sequence[nanoocp.TDocStd.TDocStd_ApplicationDelta]
TDocStd_SequenceOfDocument = nanoocp.NCollection.NCollection_Sequence[nanoocp.TDocStd.TDocStd_Document]
