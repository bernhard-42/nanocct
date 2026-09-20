"""OCCT package Storage (toolkit TKernel)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection


class Storage_OpenMode(enum.IntEnum):
    """
    Specifies opening modes for a file:
    -   Storage_VSNone : no mode is specified
    -   Storage_VSRead : the file is open for  reading operations
    -   Storage_VSWrite : the file is open for writing operations
    -   Storage_VSReadWrite : the file is open
    for both reading and writing operations.
    """

    Storage_VSNone = 0

    Storage_VSRead = 1

    Storage_VSWrite = 2

    Storage_VSReadWrite = 3

class Storage_Error(enum.IntEnum):
    """
    Error codes returned by the ErrorStatus
    function on a Storage_Data set of data during a
    storage or retrieval operation :
    -   Storage_VSOk : no problem has been detected
    -   Storage_VSOpenError : an error has
    occurred when opening the driver
    -   Storage_VSModeError : the driver has not
    been opened in the correct mode
    -   Storage_VSCloseError : an error has
    occurred when closing the driver
    -   Storage_VSAlreadyOpen : the driver is already open
    -   Storage_VSNotOpen : the driver is not open
    -   Storage_VSSectionNotFound : a section
    has not been found in the driver
    -   Storage_VSWriteError : an error occurred when writing the driver
    -   Storage_VSFormatError : the file format is wrong
    -   Storage_VSUnknownType : a type is not known from the schema
    -   Storage_VSTypeMismatch : trying to read a wrong type
    -   Storage_VSInternalError : an internal error has been detected
    -   Storage_VSExtCharParityError : an error
    has occurred while reading 16 bit character
    """

    Storage_VSOk = 0

    Storage_VSOpenError = 1

    Storage_VSModeError = 2

    Storage_VSCloseError = 3

    Storage_VSAlreadyOpen = 4

    Storage_VSNotOpen = 5

    Storage_VSSectionNotFound = 6

    Storage_VSWriteError = 7

    Storage_VSFormatError = 8

    Storage_VSUnknownType = 9

    Storage_VSTypeMismatch = 10

    Storage_VSInternalError = 11

    Storage_VSExtCharParityError = 12

    Storage_VSWrongFileDriver = 13

class Storage_SolveMode(enum.IntEnum):
    Storage_AddSolve = 0

    Storage_WriteSolve = 1

    Storage_ReadSolve = 2

class Storage:
    """
    Storage package is used to write and read persistent objects.
    These objects are read and written by a retrieval or storage
    algorithm (Storage_Schema object) in a container (disk, memory,
    network ...). Drivers (FSD_File objects) assign a physical
    container for data to be stored or retrieved.
    The standard procedure for an application in
    reading a container is the following:
    -   open the driver in reading mode,
    -   call the Read function from the schema,
    setting the driver as a parameter. This function returns
    an instance of the Storage_Data class which contains the data being read,
    -   close the driver.
    The standard procedure for an application in writing a container is the following:
    -   open the driver in writing mode,
    -   create an instance of the Storage_Data class, then
    add the persistent data to write with the function AddRoot,
    -   call the function Write from the schema,
    setting the driver and the Storage_Data instance as parameters,
    -   close the driver.
    """

    def __init__(self) -> None: ...

    @staticmethod
    def Version() -> nanoocp.TCollection.TCollection_AsciiString:
        """returns the version of Storage's read/write routines"""

class Storage_Root(nanoocp.Standard.Standard_Transient):
    """
    A root object extracted from a Storage_Data object.
    A Storage_Root encapsulates a persistent
    object which is a root of a Storage_Data object.
    It contains additional information: the name and
    the data type of the persistent object.
    When retrieving a Storage_Data object from a
    container (for example, a file) you access its
    roots with the function Roots which returns a
    sequence of root objects. The provided functions
    allow you to request information about each root of the sequence.
    You do not create explicit roots: when inserting
    data in a Storage_Data object, you just provide
    the persistent object and optionally its name to the function AddRoot.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theName: nanoocp.TCollection.TCollection_AsciiString, theObject: nanoocp.Standard.Standard_Persistent) -> None: ...

    @overload
    def __init__(self, theName: nanoocp.TCollection.TCollection_AsciiString, theRef: int, theType: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def SetName(self, theName: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the name of this root object.
        The name may have been given explicitly when
        the root was inserted into the Storage_Data
        object. If not, the name is a reference number
        which was assigned automatically by the driver
        when writing the set of data into the container.
        When naming the roots, it is easier to retrieve
        objects by significant references rather than by
        references without any semantic values.
        Warning
        The returned string will be empty if you call this
        function before having named this root object,
        either explicitly, or when writing the set of data
        into the container.
        """

    def SetObject(self, anObject: nanoocp.Standard.Standard_Persistent) -> None: ...

    def Object(self) -> nanoocp.Standard.Standard_Persistent:
        """Returns the persistent object encapsulated by this root."""

    def Type(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the name of this root type."""

    def SetReference(self, aRef: int) -> None: ...

    def Reference(self) -> int: ...

    def SetType(self, aType: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Storage_Data(nanoocp.Standard.Standard_Transient):
    """
    A picture memorizing the data stored in a
    container (for example, in a file).
    A Storage_Data object represents either:
    -   persistent data to be written into a container,
    or
    -   persistent data which are read from a container.
    A Storage_Data object is used in both the
    storage and retrieval operations:
    -   Storage mechanism: create an empty
    Storage_Data object, then add successively
    persistent objects (roots) to be stored using
    the function AddRoot. When the set of data is
    complete, write it to a container using the
    function Write in your Storage_Schema
    storage/retrieval algorithm.
    -   Retrieval mechanism: a Storage_Data
    object is returned by the Read function from
    your Storage_Schema storage/retrieval
    algorithm. Use the functions NumberOfRoots
    and Roots to find the roots which were stored
    in the read container.
    The roots of a Storage_Data object may share
    references on objects. The shared internal
    references of a Storage_Data object are
    maintained by the storage/retrieval mechanism.
    Note: References shared by objects which are
    contained in two distinct Storage_Data objects
    are not maintained by the storage/retrieval
    mechanism: external references are not
    supported by Storage_Schema algorithm
    """

    def __init__(self) -> None:
        """
        Creates an empty set of data.
        You explicitly create a Storage_Data object
        when preparing the set of objects to be stored
        together in a container (for example, in a file).
        Then use the function AddRoot to add
        persistent objects to the set of data.
        A Storage_Data object is also returned by the
        Read function of a Storage_Schema
        storage/retrieval algorithm. Use the functions
        NumberOfRoots and Roots to find the roots
        which were stored in the read container.
        """

    def ErrorStatus(self) -> Storage_Error:
        """
        Returns Storage_VSOk if
        -   the last storage operation performed with the
        function Read, or
        -   the last retrieval operation performed with the function Write
        by a Storage_Schema algorithm, on this set of data was successful.
        If the storage or retrieval operation was not
        performed, the returned error status indicates the
        reason why the operation failed. The algorithm
        stops its analysis at the first detected error
        """

    def ClearErrorStatus(self) -> None:
        """
        Clears the error status positioned either by:
        -   the last storage operation performed with the
        Read function, or
        -   the last retrieval operation performed with the Write function
        by a Storage_Schema algorithm, on this set of data.
        This error status may be read by the function ErrorStatus.
        """

    def ErrorStatusExtension(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def CreationDate(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """return the creation date"""

    def StorageVersion(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """return the Storage package version"""

    def SchemaVersion(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """get the version of the schema"""

    def SchemaName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """get the schema's name"""

    def SetApplicationVersion(self, aVersion: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """set the version of the application"""

    def ApplicationVersion(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """get the version of the application"""

    def SetApplicationName(self, aName: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """set the name of the application"""

    def ApplicationName(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """get the name of the application"""

    def SetDataType(self, aType: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """set the data type"""

    def DataType(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """returns data type"""

    def AddToUserInfo(self, anInfo: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """add <theUserInfo> to the user information"""

    def UserInfo(self) -> nanoocp.NCollection.NCollection_Sequence__TCollection_AsciiString:
        """return the user information"""

    def AddToComments(self, aComment: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """add <theUserInfo> to the user information"""

    def Comments(self) -> nanoocp.NCollection.NCollection_Sequence__TCollection_ExtendedString:
        """return the user information"""

    def NumberOfObjects(self) -> int:
        """
        the number of persistent objects
        Return:
        the number of persistent objects readed
        """

    def NumberOfRoots(self) -> int:
        """
        Returns the number of root objects in this set of data.
        -   When preparing a storage operation, the
        result is the number of roots inserted into this
        set of data with the function AddRoot.
        -   When retrieving an object, the result is the
        number of roots stored in the read container.
        Use the Roots function to get these roots in a sequence.
        """

    @overload
    def AddRoot(self, anObject: nanoocp.Standard.Standard_Persistent) -> None:
        """
        add a persistent root to write. the name of the root
        is a driver reference number.
        """

    @overload
    def AddRoot(self, aName: nanoocp.TCollection.TCollection_AsciiString, anObject: nanoocp.Standard.Standard_Persistent) -> None:
        """
        Adds the root anObject to this set of data.
        The name of the root is aName if given; if not, it
        will be a reference number assigned by the driver
        when writing the set of data into the container.
        When naming the roots, it is easier to retrieve
        objects by significant references rather than by
        references without any semantic values.
        """

    def RemoveRoot(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Removes from this set of data the root object named aName.
        Warning
        Nothing is done if there is no root object whose
        name is aName in this set of data.
        """

    def Roots(self) -> nanoocp.NCollection.NCollection_HSequence__Handle_Storage_Root:
        """
        Returns the roots of this set of data in a sequence.
        -   When preparing a storage operation, the
        sequence contains the roots inserted into this
        set of data with the function AddRoot.
        -   When retrieving an object, the sequence
        contains the roots stored in the container read.
        -   An empty sequence is returned if there is no root in this set of data.
        """

    def Find(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> Storage_Root:
        """
        Gives the root object whose name is aName in
        this set of data. The returned object is a
        Storage_Root object, from which the object it
        encapsulates may be extracted.
        Warning
        A null handle is returned if there is no root object
        whose name is aName in this set of data.
        """

    def IsRoot(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """returns true if <me> contains a root named <aName>"""

    def NumberOfTypes(self) -> int:
        """Returns the number of types of objects used in this set of data."""

    def IsType(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Returns true if this set of data contains an object of type aName.
        Persistent objects from this set of data must
        have types which are recognized by the
        Storage_Schema algorithm used to store or retrieve them.
        """

    def Types(self) -> nanoocp.NCollection.NCollection_HSequence__TCollection_AsciiString:
        """
        Gives the list of types of objects used in this set of data in a sequence.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def HeaderData(self) -> Storage_HeaderData: ...

    def RootData(self) -> Storage_RootData: ...

    def TypeData(self) -> Storage_TypeData: ...

    def InternalData(self) -> Storage_InternalData: ...

    def Clear(self) -> None: ...

class Storage_BaseDriver(nanoocp.Standard.Standard_Transient):
    """
    Root class for drivers. A driver assigns a physical container
    to data to be stored or retrieved, for instance a file.
    The FSD package provides two derived concrete classes :
    -   FSD_File is a general driver which defines a
    file as the container of data.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def OpenMode(self) -> Storage_OpenMode: ...

    def Open(self, aName: nanoocp.TCollection.TCollection_AsciiString, aMode: Storage_OpenMode) -> Storage_Error:
        """@name Virtual methods, to be provided by descendants"""

    def IsEnd(self) -> bool:
        """returns True if we are at end of the stream"""

    def Tell(self) -> int:
        """return position in the file. Return -1 upon error."""

    def BeginWriteInfoSection(self) -> Storage_Error: ...

    def WriteInfo(self, nbObj: int, dbVersion: nanoocp.TCollection.TCollection_AsciiString, date: nanoocp.TCollection.TCollection_AsciiString, schemaName: nanoocp.TCollection.TCollection_AsciiString, schemaVersion: nanoocp.TCollection.TCollection_AsciiString, appName: nanoocp.TCollection.TCollection_ExtendedString, appVersion: nanoocp.TCollection.TCollection_AsciiString, objectType: nanoocp.TCollection.TCollection_ExtendedString, userInfo: nanoocp.NCollection.NCollection_Sequence__TCollection_AsciiString) -> None: ...

    def EndWriteInfoSection(self) -> Storage_Error: ...

    def BeginReadInfoSection(self) -> Storage_Error: ...

    def ReadInfo(self, dbVersion: nanoocp.TCollection.TCollection_AsciiString, date: nanoocp.TCollection.TCollection_AsciiString, schemaName: nanoocp.TCollection.TCollection_AsciiString, schemaVersion: nanoocp.TCollection.TCollection_AsciiString, appName: nanoocp.TCollection.TCollection_ExtendedString, appVersion: nanoocp.TCollection.TCollection_AsciiString, objectType: nanoocp.TCollection.TCollection_ExtendedString, userInfo: nanoocp.NCollection.NCollection_Sequence__TCollection_AsciiString) -> int: ...

    def EndReadInfoSection(self) -> Storage_Error: ...

    def BeginWriteCommentSection(self) -> Storage_Error: ...

    def WriteComment(self, userComments: nanoocp.NCollection.NCollection_Sequence__TCollection_ExtendedString) -> None: ...

    def EndWriteCommentSection(self) -> Storage_Error: ...

    def BeginReadCommentSection(self) -> Storage_Error: ...

    def ReadComment(self, userComments: nanoocp.NCollection.NCollection_Sequence__TCollection_ExtendedString) -> None: ...

    def EndReadCommentSection(self) -> Storage_Error: ...

    def BeginWriteTypeSection(self) -> Storage_Error: ...

    def SetTypeSectionSize(self, aSize: int) -> None: ...

    def WriteTypeInformations(self, typeNum: int, typeName: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def EndWriteTypeSection(self) -> Storage_Error: ...

    def BeginReadTypeSection(self) -> Storage_Error: ...

    def TypeSectionSize(self) -> int: ...

    def ReadTypeInformations(self, typeName: nanoocp.TCollection.TCollection_AsciiString) -> int: ...

    def EndReadTypeSection(self) -> Storage_Error: ...

    def BeginWriteRootSection(self) -> Storage_Error: ...

    def SetRootSectionSize(self, aSize: int) -> None: ...

    def WriteRoot(self, rootName: nanoocp.TCollection.TCollection_AsciiString, aRef: int, aType: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def EndWriteRootSection(self) -> Storage_Error: ...

    def BeginReadRootSection(self) -> Storage_Error: ...

    def RootSectionSize(self) -> int: ...

    def ReadRoot(self, rootName: nanoocp.TCollection.TCollection_AsciiString, aType: nanoocp.TCollection.TCollection_AsciiString) -> int: ...

    def EndReadRootSection(self) -> Storage_Error: ...

    def BeginWriteRefSection(self) -> Storage_Error: ...

    def SetRefSectionSize(self, aSize: int) -> None: ...

    def WriteReferenceType(self, reference: int, typeNum: int) -> None: ...

    def EndWriteRefSection(self) -> Storage_Error: ...

    def BeginReadRefSection(self) -> Storage_Error: ...

    def RefSectionSize(self) -> int: ...

    def ReadReferenceType(self) -> tuple[int, int]: ...

    def EndReadRefSection(self) -> Storage_Error: ...

    def BeginWriteDataSection(self) -> Storage_Error: ...

    def WritePersistentObjectHeader(self, aRef: int, aType: int) -> None: ...

    def BeginWritePersistentObjectData(self) -> None: ...

    def BeginWriteObjectData(self) -> None: ...

    def EndWriteObjectData(self) -> None: ...

    def EndWritePersistentObjectData(self) -> None: ...

    def EndWriteDataSection(self) -> Storage_Error: ...

    def BeginReadDataSection(self) -> Storage_Error: ...

    def ReadPersistentObjectHeader(self) -> tuple[int, int]: ...

    def BeginReadPersistentObjectData(self) -> None: ...

    def BeginReadObjectData(self) -> None: ...

    def EndReadObjectData(self) -> None: ...

    def EndReadPersistentObjectData(self) -> None: ...

    def EndReadDataSection(self) -> Storage_Error: ...

    def SkipObject(self) -> None: ...

    def Close(self) -> Storage_Error: ...

    def PutReference(self, aValue: int) -> Storage_BaseDriver:
        """@name Output methods"""

    def PutCharacter(self, aValue: str) -> Storage_BaseDriver: ...

    def PutExtCharacter(self, aValue: "char16_t") -> Storage_BaseDriver: ...

    def PutInteger(self, aValue: int) -> Storage_BaseDriver: ...

    def PutBoolean(self, aValue: bool) -> Storage_BaseDriver: ...

    def PutReal(self, aValue: float) -> Storage_BaseDriver: ...

    def PutShortReal(self, aValue: float) -> Storage_BaseDriver: ...

    def GetReference(self) -> tuple[Storage_BaseDriver, int]:
        """@name Input methods"""

    def GetCharacter(self) -> tuple[Storage_BaseDriver, str]: ...

    def GetExtCharacter(self) -> tuple[Storage_BaseDriver, "char16_t"]: ...

    def GetInteger(self) -> tuple[Storage_BaseDriver, int]: ...

    def GetBoolean(self) -> tuple[Storage_BaseDriver, bool]: ...

    def GetReal(self) -> tuple[Storage_BaseDriver, float]: ...

    def GetShortReal(self) -> tuple[Storage_BaseDriver, float]: ...

class Storage_Bucket:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theSpaceSize: int) -> None: ...

    def Clear(self) -> None: ...

class Storage_BucketOfPersistent:
    def __init__(self, theBucketSize: int = 300000, theBucketNumber: int = 100) -> None: ...

    def Length(self) -> int: ...

    def Append(self, sp: nanoocp.Standard.Standard_Persistent) -> None: ...

    def Value(self, theIndex: int) -> nanoocp.Standard.Standard_Persistent: ...

    def Clear(self) -> None: ...

class Storage_BucketIterator:
    def __init__(self, arg0: Storage_BucketOfPersistent) -> None: ...

    def Init(self, arg0: Storage_BucketOfPersistent) -> None: ...

    def Reset(self) -> None: ...

    def Value(self) -> nanoocp.Standard.Standard_Persistent: ...

    def More(self) -> bool: ...

    def Next(self) -> None: ...

class Storage_CallBack(nanoocp.Standard.Standard_Transient):
    def New(self) -> nanoocp.Standard.Standard_Persistent: ...

    def Add(self, aPers: nanoocp.Standard.Standard_Persistent, aSchema: Storage_Schema) -> None: ...

    def Write(self, aPers: nanoocp.Standard.Standard_Persistent, aDriver: Storage_BaseDriver, aSchema: Storage_Schema) -> None: ...

    def Read(self, aPers: nanoocp.Standard.Standard_Persistent, aDriver: Storage_BaseDriver, aSchema: Storage_Schema) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Storage_DefaultCallBack(Storage_CallBack):
    def __init__(self) -> None: ...

    def New(self) -> nanoocp.Standard.Standard_Persistent: ...

    def Add(self, thePers: nanoocp.Standard.Standard_Persistent, theSchema: Storage_Schema) -> None: ...

    def Write(self, thePers: nanoocp.Standard.Standard_Persistent, theDriver: Storage_BaseDriver, theSchema: Storage_Schema) -> None: ...

    def Read(self, thePers: nanoocp.Standard.Standard_Persistent, theDriver: Storage_BaseDriver, theSchema: Storage_Schema) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Storage_HeaderData(nanoocp.Standard.Standard_Transient):
    def __init__(self) -> None: ...

    def Read(self, theDriver: Storage_BaseDriver) -> bool: ...

    def CreationDate(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """return the creation date"""

    def StorageVersion(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """return the Storage package version"""

    def SchemaVersion(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """get the version of the schema"""

    def SchemaName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """get the schema's name"""

    def SetApplicationVersion(self, aVersion: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """set the version of the application"""

    def ApplicationVersion(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """get the version of the application"""

    def SetApplicationName(self, aName: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """set the name of the application"""

    def ApplicationName(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """get the name of the application"""

    def SetDataType(self, aType: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """set the data type"""

    def DataType(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """returns data type"""

    def AddToUserInfo(self, theUserInfo: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """add <theUserInfo> to the user information"""

    def UserInfo(self) -> nanoocp.NCollection.NCollection_Sequence__TCollection_AsciiString:
        """return the user information"""

    def AddToComments(self, aComment: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """add <theUserInfo> to the user information"""

    def Comments(self) -> nanoocp.NCollection.NCollection_Sequence__TCollection_ExtendedString:
        """return the user information"""

    def NumberOfObjects(self) -> int:
        """
        the number of persistent objects
        Return:
        the number of persistent objects readed
        """

    def ErrorStatus(self) -> Storage_Error: ...

    def ErrorStatusExtension(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def ClearErrorStatus(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetNumberOfObjects(self, anObjectNumber: int) -> None: ...

    @overload
    def SetStorageVersion(self, aVersion: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    @overload
    def SetStorageVersion(self, theVersion: int) -> None: ...

    def SetCreationDate(self, aDate: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def SetSchemaVersion(self, aVersion: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def SetSchemaName(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

class Storage_TypedCallBack(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aTypeName: nanoocp.TCollection.TCollection_AsciiString, aCallBack: Storage_CallBack) -> None: ...

    def SetType(self, aType: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def Type(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def SetCallBack(self, aCallBack: Storage_CallBack) -> None: ...

    def CallBack(self) -> Storage_CallBack: ...

    def SetIndex(self, anIndex: int) -> None: ...

    def Index(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Storage_InternalData(nanoocp.Standard.Standard_Transient):
    def __init__(self) -> None: ...

    def ReadArray(self) -> nanoocp.NCollection.NCollection_HArray1__Handle_Standard_Persistent: ...

    def Clear(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Storage_RootData(nanoocp.Standard.Standard_Transient):
    def __init__(self) -> None: ...

    def Read(self, theDriver: Storage_BaseDriver) -> bool: ...

    def NumberOfRoots(self) -> int:
        """returns the number of roots."""

    def AddRoot(self, aRoot: Storage_Root) -> None:
        """
        add a root to <me>. If a root with same name is present, it
        will be replaced by <aRoot>.
        """

    def Roots(self) -> nanoocp.NCollection.NCollection_HSequence__Handle_Storage_Root: ...

    def Find(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> Storage_Root:
        """find a root with name <aName>."""

    def IsRoot(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """returns true if <me> contains a root named <aName>"""

    def RemoveRoot(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """remove the root named <aName>."""

    def ErrorStatus(self) -> Storage_Error: ...

    def ErrorStatusExtension(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def ClearErrorStatus(self) -> None: ...

    def UpdateRoot(self, aName: nanoocp.TCollection.TCollection_AsciiString, aPers: nanoocp.Standard.Standard_Persistent) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Storage_Schema(nanoocp.Standard.Standard_Transient):
    """
    Root class for basic storage/retrieval algorithms.
    A Storage_Schema object processes:
    -   writing of a set of persistent data into a
    container (store mechanism),
    -   reading of a container to extract all the
    contained persistent data (retrieve mechanism).
    A Storage_Schema object is based on the data
    schema for the persistent data of the application, i.e.:
    -   the list of all persistent objects which may be
    known by the application,
    -   the organization of their data; a data schema
    knows how to browse each persistent object it contains.
    During the store or retrieve operation, only
    persistent objects known from the data schema
    can be processed; they are then stored or
    retrieved according to their description in the schema.
    A data schema is specific to the object classes to
    be read or written. Tools dedicated to the
    environment in use allow a description of the
    application persistent data structure.
    Storage_Schema algorithms are called basic
    because they do not support external references
    between containers.
    """

    def __init__(self) -> None:
        """
        Builds a storage/retrieval algorithm based on a
        given data schema.
        Example
        For example, if ShapeSchema is the class
        inheriting from Storage_Schema and containing
        the description of your application data schema,
        you create a storage/retrieval algorithm as follows:
        occ::handle<ShapeSchema> s = new
        ShapeSchema;
        -------- --
        USER API -- --------------------------------------------------------------
        -------- --
        """

    def SetVersion(self, aVersion: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """returns version of the schema"""

    def Version(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """returns the version of the schema"""

    def SetName(self, aSchemaName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """set the schema's name"""

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """returns the schema's name"""

    def Write(self, s: Storage_BaseDriver, aData: Storage_Data) -> None:
        """
        Writes the data aggregated in aData into the
        container defined by the driver <s>. The storage
        operation is performed according to the data
        schema with which this algorithm is working.
        Note: aData may aggregate several root objects
        to be stored together.
        """

    @staticmethod
    def ICreationDate() -> nanoocp.TCollection.TCollection_AsciiString:
        """return a current date string"""

    @staticmethod
    def CheckTypeMigration(theTypeName: nanoocp.TCollection.TCollection_AsciiString, theNewName: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        returns True if theType migration is identified
        the callback support provides a way to read a file
        with a incomplete schema.
        ex. A file contains 3 types a, b, and c.
        The application's schema contains only 2
        type a and b. If you try to read the file in
        the application, you will have an error. To
        bypass this problem you can give to your
        application's schema a callback used when
        the schema doesn't know how to handle this
        type.
        """

    def AddReadUnknownTypeCallBack(self, aTypeName: nanoocp.TCollection.TCollection_AsciiString, aCallBack: Storage_CallBack) -> None:
        """add two functions to the callback list"""

    def RemoveReadUnknownTypeCallBack(self, aTypeName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """remove a callback for a type"""

    def InstalledCallBackList(self) -> nanoocp.NCollection.NCollection_HSequence__TCollection_AsciiString:
        """
        returns a list of type name with installed
        callback.
        """

    def ClearCallBackList(self) -> None:
        """clear all callback from schema instance."""

    def UseDefaultCallBack(self) -> None:
        """
        install a callback for all unknown type. the
        objects with unknown types will be skipped. (look
        SkipObject method in BaseDriver)
        """

    def DontUseDefaultCallBack(self) -> None:
        """tells schema to uninstall the default callback."""

    def IsUsingDefaultCallBack(self) -> bool:
        """ask if the schema is using the default callback."""

    def SetDefaultCallBack(self, f: Storage_CallBack) -> None:
        """
        overload the default function for build. (use to
        set an error message or skip an object while
        reading an unknown type).
        """

    def ResetDefaultCallBack(self) -> None:
        """
        reset the default function defined by Storage
        package.
        """

    def DefaultCallBack(self) -> Storage_CallBack:
        """
        returns the read function used when the
        UseDefaultCallBack() is set.
        """

    def WritePersistentObjectHeader(self, sp: nanoocp.Standard.Standard_Persistent, theDriver: Storage_BaseDriver) -> None: ...

    def WritePersistentReference(self, sp: nanoocp.Standard.Standard_Persistent, theDriver: Storage_BaseDriver) -> None: ...

    def AddPersistent(self, sp: nanoocp.Standard.Standard_Persistent, tName: str) -> bool: ...

    def PersistentToAdd(self, sp: nanoocp.Standard.Standard_Persistent) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Storage_StreamReadError(nanoocp.Standard.Standard_Failure):
    pass

class Storage_StreamExtCharParityError(Storage_StreamReadError):
    pass

class Storage_StreamFormatError(nanoocp.Standard.Standard_Failure):
    pass

class Storage_StreamModeError(nanoocp.Standard.Standard_Failure):
    pass

class Storage_StreamTypeMismatchError(Storage_StreamReadError):
    pass

class Storage_StreamUnknownTypeError(Storage_StreamReadError):
    pass

class Storage_StreamWriteError(nanoocp.Standard.Standard_Failure):
    pass

class Storage_TypeData(nanoocp.Standard.Standard_Transient):
    def __init__(self) -> None: ...

    def Read(self, theDriver: Storage_BaseDriver) -> bool: ...

    def NumberOfTypes(self) -> int: ...

    def AddType(self, aName: nanoocp.TCollection.TCollection_AsciiString, aTypeNum: int) -> None:
        """add a type to the list"""

    @overload
    def Type(self, aTypeNum: int) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def Type(self, aTypeName: nanoocp.TCollection.TCollection_AsciiString) -> int:
        """returns the name of the type with number <aTypeNum>"""

    def IsType(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> bool: ...

    def Types(self) -> nanoocp.NCollection.NCollection_HSequence__TCollection_AsciiString: ...

    def ErrorStatus(self) -> Storage_Error: ...

    def ErrorStatusExtension(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def ClearErrorStatus(self) -> None: ...

    def Clear(self) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
Storage_HPArray = nanoocp.NCollection.NCollection_HArray1__Handle_Standard_Persistent
Storage_HSeqOfRoot = nanoocp.NCollection.NCollection_HSequence__Handle_Storage_Root
Storage_PArray = nanoocp.NCollection.NCollection_Array1__Handle_Standard_Persistent
Storage_SeqOfRoot = nanoocp.NCollection.NCollection_Sequence__Handle_Storage_Root
