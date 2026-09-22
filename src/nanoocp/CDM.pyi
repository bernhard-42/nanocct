"""OCCT package CDM (toolkit TKCDF)"""

import enum
from typing import overload

import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Resource
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.CDM


class CDM_CanCloseStatus(enum.IntEnum):
    CDM_CCS_OK = 0

    CDM_CCS_NotOpen = 1

    CDM_CCS_UnstoredReferenced = 2

    CDM_CCS_ModifiedReferenced = 3

    CDM_CCS_ReferenceRejection = 4

CDM_CCS_OK: CDM_CanCloseStatus = CDM_CanCloseStatus.CDM_CCS_OK

CDM_CCS_NotOpen: CDM_CanCloseStatus = CDM_CanCloseStatus.CDM_CCS_NotOpen

CDM_CCS_UnstoredReferenced: CDM_CanCloseStatus = CDM_CanCloseStatus.CDM_CCS_UnstoredReferenced

CDM_CCS_ModifiedReferenced: CDM_CanCloseStatus = CDM_CanCloseStatus.CDM_CCS_ModifiedReferenced

CDM_CCS_ReferenceRejection: CDM_CanCloseStatus = CDM_CanCloseStatus.CDM_CCS_ReferenceRejection

class CDM_Application(nanoocp.Standard.Standard_Transient):
    def Resources(self) -> nanoocp.Resource.Resource_Manager:
        """
        The manager returned by this virtual method will be
        used to search for Format.Retrieval resource items.
        """

    def MessageDriver(self) -> nanoocp.Message.Message_Messenger:
        """Returns default messenger;"""

    def BeginOfUpdate(self, aDocument: CDM_Document | None) -> None:
        """
        this method is called before the update of a document.
        By default, writes in MessageDriver().
        """

    def EndOfUpdate(self, aDocument: CDM_Document | None, theStatus: bool, ErrorString: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        this method is called after the update of a document.
        By default, writes in MessageDriver().
        """

    def Write(self, aString: str) -> None:
        """writes the string in the application MessagerDriver."""

    def Name(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """Returns the application name."""

    def Version(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the application version."""

    def MetaDataLookUpTable(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.CDM.CDM_MetaData]:
        """Returns MetaData LookUpTable"""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class CDM_Reference(nanoocp.Standard.Standard_Transient):
    def __init__(self, theOther: CDM_Reference) -> None: ...

    def FromDocument(self) -> CDM_Document: ...

    def ToDocument(self) -> CDM_Document: ...

    def ReferenceIdentifier(self) -> int: ...

    def DocumentVersion(self) -> int: ...

    def IsReadOnly(self) -> bool: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class CDM_Document(nanoocp.Standard.Standard_Transient):
    """
    An applicative document is an instance of a class inheriting CDM_Document.
    These documents have the following properties:
    - they can have references to other documents.
    - the modifications of a document are propagated to the referencing
    documents.
    - a document can be stored in different formats, with or
    without a persistent model.
    - the drivers for storing and retrieving documents are
    plugged in when necessary.
    - a document has a modification counter. This counter is
    incremented when the document is modified. When a document
    is stored, the current counter value is memorized as the
    last storage version of the document. A document is
    considered to be modified when the counter value is
    different from the storage version. Once the document is
    saved the storage version and the counter value are
    identical. The document is now not considered to be
    modified.
    - a reference is a link between two documents. A reference has two
    components: the "From Document" and the "To Document". When
    a reference is created, an identifier of the reference is generated.
    This identifier is unique in the scope of the From Document and
    is conserved during storage and retrieval. This means that the
    referenced document will be always accessible through this
    identifier.
    - a reference memorizes the counter value of the To Document when
    the reference is created. The From Document is considered to
    be up to date relative to the To Document when the
    reference counter value is equal to the To Document counter value.
    -  retrieval of a document having references does not imply
    the retrieving of the referenced documents.
    """

    @overload
    def Update(self, ErrorString: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        This method Update will be called
        to signal the end of the modified references list.
        The document should be recomputed and
        UpdateFromDocuments should be called. Update should
        returns True in case of success, false otherwise. In
        case of Failure, additional information can be given in
        ErrorString.
        """

    @overload
    def Update(self) -> None:
        """
        the following method should be used instead:

        Update(me:mutable; ErrorString: out ExtendedString from TCollection)
        returns Boolean from Standard
        """

    def StorageFormat(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        The Storage Format is the key which is used to determine in the
        application resources the storage driver plugin, the file
        extension and other data used to store the document.
        """

    def Extensions(self, Extensions: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_ExtendedString]) -> None:
        """by default empties the extensions."""

    def GetAlternativeDocument(self, aFormat: nanoocp.TCollection.TCollection_ExtendedString) -> tuple[bool, CDM_Document]:
        """
        This method can be redefined to extract another document in
        a different format. For example, to extract a Shape
        from an applicative document.
        """

    @overload
    def CreateReference(self, anOtherDocument: CDM_Document | None) -> int:
        """
        Creates a reference from this document to {anOtherDocument}.
        Returns a reference identifier. This reference identifier
        is unique in the document and will not be used for the
        next references, even after the storing of the document.
        If there is already a reference between the two documents,
        the reference is not created, but its reference identifier
        is returned.
        """

    @overload
    def CreateReference(self, aMetaData: CDM_MetaData | None, aReferenceIdentifier: int, anApplication: CDM_Application | None, aToDocumentVersion: int, UseStorageConfiguration: bool) -> None: ...

    @overload
    def CreateReference(self, aMetaData: CDM_MetaData | None, anApplication: CDM_Application | None, aDocumentVersion: int, UseStorageConfiguration: bool) -> int: ...

    def RemoveReference(self, aReferenceIdentifier: int) -> None:
        """
        Removes the reference between the From Document and the
        To Document identified by a reference identifier.
        """

    def RemoveAllReferences(self) -> None:
        """Removes all references having this document for From Document."""

    def Document(self, aReferenceIdentifier: int) -> CDM_Document:
        """
        Returns the To Document of the reference identified by
        aReferenceIdentifier. If the ToDocument is stored and
        has not yet been retrieved, this method will retrieve it.
        """

    def IsInSession(self, aReferenceIdentifier: int) -> bool:
        """
        returns True if the To Document of the reference
        identified by aReferenceIdentifier is in session, False
        if it corresponds to a not yet retrieved document.
        """

    @overload
    def IsStored(self, aReferenceIdentifier: int) -> bool:
        """
        returns True if the To Document of the reference
        identified by aReferenceIdentifier has already been stored,
        False otherwise.
        """

    @overload
    def IsStored(self) -> bool: ...

    def Name(self, aReferenceIdentifier: int) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        returns the name of the metadata of the To Document of
        the reference identified by aReferenceIdentifier.
        """

    def ToReferencesNumber(self) -> int:
        """
        returns the number of references having this document as
        From Document.
        """

    def FromReferencesNumber(self) -> int:
        """
        returns the number of references having this document as
        To Document.
        """

    def ShallowReferences(self, aDocument: CDM_Document | None) -> bool:
        """returns True is this document references aDocument;"""

    def DeepReferences(self, aDocument: CDM_Document | None) -> bool:
        """returns True is this document references aDocument;"""

    def CopyReference(self, aFromDocument: CDM_Document | None, aReferenceIdentifier: int) -> int:
        """
        Copies a reference to this document. This method
        avoid retrieval of referenced document. The arguments
        are the original document and a valid reference
        identifier Returns the local identifier.
        """

    @overload
    def IsReadOnly(self) -> bool:
        """indicates that this document cannot be modified."""

    @overload
    def IsReadOnly(self, aReferenceIdentifier: int) -> bool:
        """indicates that the referenced document cannot be modified,"""

    def SetIsReadOnly(self) -> None: ...

    def UnsetIsReadOnly(self) -> None: ...

    def Modify(self) -> None:
        """
        Indicates that this document has been modified.
        This method increments the modification counter.
        """

    def Modifications(self) -> int:
        """returns the current modification counter."""

    def UnModify(self) -> None: ...

    def IsUpToDate(self, aReferenceIdentifier: int) -> bool:
        """
        returns true if the modification counter found in the given
        reference is equal to the actual modification counter of
        the To Document. This method is able to deal with a reference
        to a not retrieved document.
        """

    def SetIsUpToDate(self, aReferenceIdentifier: int) -> None:
        """
        Resets the modification counter in the given reference
        to the actual modification counter of its To Document.
        This method should be called after the application has updated
        this document.
        """

    def SetComment(self, aComment: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """associates a comment with this document."""

    def AddComment(self, aComment: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """appends a comment into comments of this document."""

    def SetComments(self, aComments: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_ExtendedString]) -> None:
        """associates a comments with this document."""

    def Comments(self, aComments: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_ExtendedString]) -> None:
        """
        returns the associated comments through <aComments>.
        Returns empty sequence if no comments are associated.
        """

    def Comment(self) -> str:
        """
        Returns the first of associated comments.
        By default the comment is an empty string.
        """

    def StorageVersion(self) -> int:
        """
        returns the value of the modification counter at the
        time of storage. By default returns 0.
        """

    def SetMetaData(self, aMetaData: CDM_MetaData | None) -> None:
        """
        associates database information to a document which
        has been stored. The name of the document is now the
        name which has beenused to store the data.
        """

    def UnsetIsStored(self) -> None: ...

    def MetaData(self) -> CDM_MetaData: ...

    def Folder(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def SetRequestedFolder(self, aFolder: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """defines the folder in which the object should be stored."""

    def RequestedFolder(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def HasRequestedFolder(self) -> bool: ...

    def SetRequestedName(self, aName: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """defines the name under which the object should be stored."""

    def RequestedName(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        Determines under which the document is going to be store.
        By default the name of the document will be used.
        If the document has no name its presentation will be used.
        """

    def SetRequestedPreviousVersion(self, aPreviousVersion: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    def UnsetRequestedPreviousVersion(self) -> None: ...

    def HasRequestedPreviousVersion(self) -> bool: ...

    def RequestedPreviousVersion(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def SetRequestedComment(self, aComment: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """defines the Comment with which the object should be stored."""

    def RequestedComment(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def LoadResources(self) -> None:
        """read (or rereads) the following resource."""

    def FindFileExtension(self) -> bool: ...

    def FileExtension(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        gets the Desktop.Domain.Application.`FileFormat`.FileExtension resource.
        """

    def FindDescription(self) -> bool: ...

    def Description(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """gets the `FileFormat`.Description resource."""

    def IsModified(self) -> bool:
        """
        returns true if the version is greater than the
        storage version
        """

    def Print(self) -> str: ...

    @overload
    def IsOpened(self) -> bool: ...

    @overload
    def IsOpened(self, aReferenceIdentifier: int) -> bool:
        """
        returns true if the document corresponding to the
        given reference has been retrieved and opened.
        Otherwise returns false. This method does not retrieve
        the referenced document
        """

    def Open(self, anApplication: CDM_Application | None) -> None: ...

    def CanClose(self) -> CDM_CanCloseStatus: ...

    def Close(self) -> None: ...

    def Application(self) -> CDM_Application: ...

    def CanCloseReference(self, aDocument: CDM_Document | None, aReferenceIdentifier: int) -> bool:
        """
        A referenced document may indicate through this
        virtual method that it does not allow the closing of
        aDocument which it references through the reference
        aReferenceIdentifier. By default returns true.
        """

    def CloseReference(self, aDocument: CDM_Document | None, aReferenceIdentifier: int) -> None:
        """
        A referenced document may update its internal
        data structure when {aDocument} which it references
        through the reference {aReferenceIdentifier} is being closed.
        By default this method does nothing.
        """

    def ReferenceCounter(self) -> int: ...

    def Reference(self, aReferenceIdentifier: int) -> CDM_Reference: ...

    def SetModifications(self, Modifications: int) -> None: ...

    def SetReferenceCounter(self, aReferenceCounter: int) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class CDM_MetaData(nanoocp.Standard.Standard_Transient):
    def __init__(self, theOther: CDM_MetaData) -> None: ...

    @overload
    @staticmethod
    def LookUp(theLookUpTable: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.CDM.CDM_MetaData], aFolder: nanoocp.TCollection.TCollection_ExtendedString, aName: nanoocp.TCollection.TCollection_ExtendedString, aPath: nanoocp.TCollection.TCollection_ExtendedString, aFileName: nanoocp.TCollection.TCollection_ExtendedString, ReadOnly: bool) -> CDM_MetaData: ...

    @overload
    @staticmethod
    def LookUp(theLookUpTable: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_ExtendedString, nanoocp.CDM.CDM_MetaData], aFolder: nanoocp.TCollection.TCollection_ExtendedString, aName: nanoocp.TCollection.TCollection_ExtendedString, aPath: nanoocp.TCollection.TCollection_ExtendedString, aVersion: nanoocp.TCollection.TCollection_ExtendedString, aFileName: nanoocp.TCollection.TCollection_ExtendedString, ReadOnly: bool) -> CDM_MetaData: ...

    def IsRetrieved(self) -> bool: ...

    def Document(self) -> CDM_Document: ...

    def Folder(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        returns the folder in which the meta-data has to be created
        or has to be found.
        """

    def Name(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        returns the name under which the meta-data has to be created
        or has to be found.
        """

    def Version(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        returns the version under which the meta-data has to be found.
        Warning: raises NoSuchObject from Standard if no Version has been defined
        """

    def HasVersion(self) -> bool:
        """
        indicates that the version has to be taken into account when
        searching the corresponding meta-data.
        """

    def FileName(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def Print(self) -> str: ...

    def Path(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def UnsetDocument(self) -> None: ...

    def IsReadOnly(self) -> bool: ...

    def SetIsReadOnly(self) -> None: ...

    def UnsetIsReadOnly(self) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class CDM_ReferenceIterator:
    @overload
    def __init__(self, aDocument: CDM_Document | None) -> None: ...

    @overload
    def __init__(self, theOther: CDM_ReferenceIterator) -> None: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

    def Document(self) -> CDM_Document: ...

    def ReferenceIdentifier(self) -> int: ...

    def DocumentVersion(self) -> int:
        """returns the Document Version in the reference."""
