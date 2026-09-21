"""OCCT package Standard (toolkit TKernel)"""

import enum
from typing import TextIO, TypeAlias, overload

import nanoocp.NCollection
import nanoocp.TCollection
import nanoocp.Standard


class Standard_JsonKey(enum.IntEnum):
    """Kind of key in Json string"""

    Standard_JsonKey_None = 0

    Standard_JsonKey_OpenChild = 1

    Standard_JsonKey_CloseChild = 2

    Standard_JsonKey_OpenContainer = 3

    Standard_JsonKey_CloseContainer = 4

    Standard_JsonKey_Quote = 5

    Standard_JsonKey_SeparatorKeyToValue = 6

    Standard_JsonKey_SeparatorValueToValue = 7

Standard_JsonKey_None: Standard_JsonKey = Standard_JsonKey.Standard_JsonKey_None

Standard_JsonKey_OpenChild: Standard_JsonKey = Standard_JsonKey.Standard_JsonKey_OpenChild

Standard_JsonKey_CloseChild: Standard_JsonKey = Standard_JsonKey.Standard_JsonKey_CloseChild

Standard_JsonKey_OpenContainer: Standard_JsonKey = Standard_JsonKey.Standard_JsonKey_OpenContainer

Standard_JsonKey_CloseContainer: Standard_JsonKey = Standard_JsonKey.Standard_JsonKey_CloseContainer

Standard_JsonKey_Quote: Standard_JsonKey = Standard_JsonKey.Standard_JsonKey_Quote

Standard_JsonKey_SeparatorKeyToValue: Standard_JsonKey = ...

Standard_JsonKey_SeparatorValueToValue: Standard_JsonKey = ...

class Standard:
    """
    The package Standard provides global memory allocator and other basic
    services used by other OCCT components.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Standard) -> None: ...

    class AllocatorType(enum.Enum):
        """Enumiration of possible allocator types"""

        NATIVE = 0

        OPT = 1

        TBB = 2

        JEMALLOC = 3

    @staticmethod
    def GetAllocatorType() -> Standard.AllocatorType:
        """Returns default allocator type"""

    @staticmethod
    def Purge() -> int:
        """
        Deallocates the storage retained on the free list
        and clears the list.
        Returns non-zero if some memory has been actually freed.
        """

class Standard_Failure(RuntimeError):
    """
    Forms the root of the entire exception hierarchy.
    Inherits from std::exception and implements what() interface.
    """

class Standard_AbortiveTransaction(Standard_Failure):
    pass

class Standard_Transient:
    """
    Abstract class which forms the root of the entire
    Transient class hierarchy.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, arg0: Standard_Transient) -> None:
        """Copy constructor -- does nothing"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> Standard_Type:
        """Returns type descriptor of Standard_Transient class"""

    def DynamicType(self) -> Standard_Type:
        """Returns a type descriptor about this object."""

    @overload
    def IsInstance(self, theType: Standard_Type | None) -> bool:
        """Returns a true value if this is an instance of Type."""

    @overload
    def IsInstance(self, theTypeName: str) -> bool:
        """Returns a true value if this is an instance of TypeName."""

    @overload
    def IsKind(self, theType: Standard_Type | None) -> bool:
        """
        Returns true if this is an instance of Type or an
        instance of any class that inherits from Type.
        Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """

    @overload
    def IsKind(self, theTypeName: str) -> bool:
        """
        Returns true if this is an instance of TypeName or an
        instance of any class that inherits from TypeName.
        Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """

    def This(self) -> Standard_Transient:
        """
        Returns non-const pointer to this object (like const_cast).
        For protection against creating handle to objects allocated in stack
        or call from constructor, it will raise exception Standard_ProgramError
        if reference counter is zero.
        """

    def GetRefCount(self) -> int:
        """Get the reference counter of this object"""

    def IncrementRefCounter(self) -> None:
        """
        Increments the reference counter of this object.
        Uses relaxed memory ordering since incrementing only requires atomicity,
        not synchronization with other memory operations.
        """

    def DecrementRefCounter(self) -> int:
        """
        Decrements the reference counter of this object;
        returns the decremented value.
        Uses release ordering for the decrement to ensure all writes to the object
        are visible before the count reaches zero. An acquire fence is added only
        when the count reaches zero, ensuring proper synchronization before deletion.
        This is more efficient than using acq_rel for every decrement.
        """

    def Delete(self) -> None:
        """Memory deallocator for transient classes"""

class Standard_Type(Standard_Transient):
    """
    This class provides legacy interface (type descriptor) to run-time type
    information (RTTI) for OCCT classes inheriting from Standard_Transient.

    In addition to features provided by standard C++ RTTI (type_info),
    Standard_Type allows passing descriptor as an object and using it for
    analysis of the type:
    - get descriptor of a parent class
    - get user-defined name of the class
    - get size of the object

    Use static template method Instance() to get descriptor for a given type.
    Objects supporting OCCT RTTI return their type descriptor by method DynamicType().

    To be usable with OCCT type system, the class should provide:
    - typedef base_type to its base class in the hierarchy
    - method get_type_name() returning programmer-defined name of the class
    (as a statically allocated constant C string or string literal)

    Note that user-defined name is used since typeid.name() is usually mangled in
    compiler-dependent way.

    Only single chain of inheritance is supported, with a root base class Standard_Transient.
    """

    def __init__(self, theOther: Standard_Type) -> None: ...

    def SystemName(self) -> str:
        """Returns the system type name of the class (typeinfo.name)"""

    def Name(self) -> str:
        """Returns the given name of the class type (get_type_name)"""

    def Size(self) -> int:
        """Returns the size of the class instance in bytes"""

    def Parent(self) -> Standard_Type:
        """Returns descriptor of the base class in the hierarchy"""

    @overload
    def SubType(self, theOther: Standard_Type | None) -> bool: ...

    @overload
    def SubType(self, theOther: str) -> bool:
        """
        Returns True if this type is the same as theOther, or inherits from theOther.
        Note that multiple inheritance is not supported.
        """

    def Print(self) -> object:
        """Prints type (address of descriptor + name) to a stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> Standard_Type: ...

    def DynamicType(self) -> Standard_Type: ...

class Standard_ProgramError(Standard_Failure):
    pass

class Standard_CLocaleSentry:
    """
    This class intended to temporary switch C locale and logically equivalent to setlocale(LC_ALL,
    "C"). It is intended to format text regardless of user locale settings (for import/export
    functionality). Thus following calls to Sprintf, atoi and other functions will use "C" locale.
    Destructor of this class will return original locale.

    Notice that this functionality is platform dependent and intended only to workaround alien code
    that doesn't setup locale correctly.

    Internally you should prefer more portable C++ locale interfaces
    or OCCT wrappers to some C functions like Sprintf, Atof, Strtod.
    """

    def __init__(self) -> None:
        """Setup current C locale to "C"."""

class Standard_Condition:
    """
    This is boolean flag intended for communication between threads.
    One thread sets this flag to TRUE to indicate some event happened
    and another thread either waits this event or checks periodically its state to perform job.

    This class provides interface similar to WinAPI Event objects.
    """

    def __init__(self, theIsSet: bool = False) -> None:
        """
        Default constructor.
        @param theIsSet Initial flag state
        """

    def Set(self) -> None:
        """Set event into signaling state."""

    def Reset(self) -> None:
        """Reset event (unset signaling state)"""

    @overload
    def Wait(self) -> None:
        """Wait for Event (infinity)."""

    @overload
    def Wait(self, theTimeMilliseconds: int) -> bool:
        """
        Wait for signal requested time.
        @param theTimeMilliseconds wait limit in milliseconds
        @return true if get event
        """

    def Check(self) -> bool:
        """
        Do not wait for signal - just test it state.
        @return true if get event
        """

    def CheckReset(self) -> bool:
        """
        Method perform two steps at-once - reset the event object
        and returns true if it was in signaling state.
        @return true if event object was in signaling state.
        """

class Standard_DomainError(Standard_Failure):
    pass

class Standard_ConstructionError(Standard_DomainError):
    pass

class Standard_CStringHasher:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Standard_CStringHasher) -> None: ...

    @overload
    def __call__(self, theString: str) -> int: ...

    @overload
    def __call__(self, theString1: str, theString2: str) -> bool: ...

class Standard_DimensionError(Standard_DomainError):
    pass

class Standard_DimensionMismatch(Standard_DimensionError):
    pass

class Standard_NumericError(Standard_Failure):
    pass

class Standard_DivideByZero(Standard_NumericError):
    pass

class Standard_RangeError(Standard_DomainError):
    pass

class Standard_OutOfRange(Standard_RangeError):
    pass

class Standard_TypeMismatch(Standard_DomainError):
    pass

class Standard_NoSuchObject(Standard_DomainError):
    pass

class Standard_DumpValue:
    """Type for storing a dump value with the stream position"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theValue: nanoocp.TCollection.TCollection_AsciiString, theStartPos: int) -> None: ...

    @overload
    def __init__(self, theOther: Standard_DumpValue) -> None: ...

    @property
    def myValue(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """current string value"""

    @myValue.setter
    def myValue(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def myStartPosition(self) -> int:
        """position of the value first char in the whole stream"""

    @myStartPosition.setter
    def myStartPosition(self, arg: int, /) -> None: ...

class Standard_Dump:
    """
    This interface has some tool methods for stream (in JSON format) processing.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Standard_Dump) -> None: ...

    @staticmethod
    def Text(theStream: TextIO) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Converts stream value to string value. The result is original stream value.
        @param theStream source value
        @return text presentation
        """

    @staticmethod
    def FormatJson(theStream: TextIO, theIndent: int = 3) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Converts stream value to string value. Improves the text presentation with the following
        cases:
        - for '{' append after '\\n' and indent to the next value, increment current indent value
        - for '}' append '\\n' and current indent before it, decrement indent value
        - for ',' append after '\\n' and indent to the next value. If the current symbol is in massive
        container [], do nothing Covers result with opened and closed brackets on the top level, if it
        has no symbols there.
        @param theStream source value
        @param theIndent count of ' ' symbols to apply hierarchical indent of the text values
        @return text presentation
        """

    @staticmethod
    def SplitJson(theStreamStr: nanoocp.TCollection.TCollection_AsciiString, theKeyToValues: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.Standard.Standard_DumpValue]) -> bool:
        """
        Converts stream into map of values.

        The one level stream example: 'key_1: value_1, key_2: value_2'
        In output: values contain 'key_1: value_1' and 'key_2: value_2'.

        The two level stream example: 'key_1: value_1, key_2: value_2, key_3: {sublevel_key_1:
        sublevel_value_1}, key_4: value_4' In output values contain 'key_1: value_1', 'key_2:
        value_2', 'key_3: {sublevel_key_1: sublevel_value_1}' and 'key_4: value_4'. The sublevel value
        might be processed later using the same method.

        @param theStreamStr stream value
        @param[out] theKeyToValues  container of split values. It contains key to value and position
        of the value in the stream text
        """

    @staticmethod
    def HierarchicalValueIndices(theValues: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> nanoocp.NCollection.NCollection_List[int]:
        """Returns container of indices in values, that has hierarchical value"""

    @staticmethod
    def HasChildKey(theSourceValue: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Returns true if the value has bracket key"""

    @staticmethod
    def JsonKeyToString(theKey: Standard_JsonKey) -> str:
        """Returns key value for enum type"""

    @staticmethod
    def JsonKeyLength(theKey: Standard_JsonKey) -> int:
        """Returns length value for enum type"""

    @staticmethod
    def AddValuesSeparator() -> object:
        """@param theOStream source value"""

    @staticmethod
    def GetPointerPrefix() -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns default prefix added for each pointer info string if short presentation of pointer
        used
        """

    @staticmethod
    def GetPointerInfo(thePointer: Standard_Transient | None, isShortInfo: bool = True) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Convert handle pointer to address of the pointer. If the handle is NULL, the result is an
        empty string.
        @param thePointer a pointer
        @param isShortInfo if true, all '0' symbols in the beginning of the pointer are skipped
        @return the string value
        """

    @staticmethod
    def DumpKeyToClass(theKey: nanoocp.TCollection.TCollection_AsciiString, theField: nanoocp.TCollection.TCollection_AsciiString) -> object:
        """
        Append into output value: "Name": { Field }
        @param[out] theOStream  stream to be fill with values
        @param theKey a source value
        @param theField stream value
        """

    @staticmethod
    def ProcessStreamName(theStreamStr: nanoocp.TCollection.TCollection_AsciiString, theName: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, int]:
        """
        Check whether the parameter name is equal to the name in the stream at position
        @param[in]  theStreamStr stream with values
        @param[in]  theName      stream key value
        @param[out] theStreamPos current position in the stream
        """

    @staticmethod
    def ProcessFieldName(theStreamStr: nanoocp.TCollection.TCollection_AsciiString, theName: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, int]:
        """
        Check whether the field name is equal to the name in the stream at position
        @param[in]  theStreamStr stream with values
        @param[in]  theName      stream key field value
        @param[out] theStreamPos current position in the stream
        """

    @staticmethod
    def InitValue(theStreamStr: nanoocp.TCollection.TCollection_AsciiString, theValue: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, int]:
        """
        Returns real value
        @param[in]  theStreamStr stream with values
        @param[out] theStreamPos current position in the stream
        @param[out] theValue     stream value
        """

    @staticmethod
    def DumpFieldToName(theField: nanoocp.TCollection.TCollection_AsciiString) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Convert field name into dump text value, removes "&" and "my" prefixes
        An example, for field myValue, theName is Value, for &myCLass, the name is Class
        @param theField a source value
        """

class Standard_Overflow(Standard_NumericError):
    pass

class Standard_Underflow(Standard_NumericError):
    pass

class Standard_ErrorHandler:
    """
    Class implementing mechanics of conversion of signals to exceptions.

    Each instance of it stores data for jump placement,
    and callbacks to be called during jump (for proper resource release).

    The active handlers are stored in the global stack, which is used
    to find appropriate handler when signal is raised.
    """

    @overload
    def __init__(self) -> None:
        """
        Create a ErrorHandler (to be used with try{}catch(){}).
        It uses the "setjmp" and "longjmp" routines.
        """

    @overload
    def __init__(self, theOther: Standard_ErrorHandler) -> None: ...

    class Callback:
        """
        Defines a base class for callback objects that can be registered
        in the OCC error handler (the class simulating C++ exceptions)
        so as to be correctly destroyed when error handler is activated.

        Note that this is needed only when Open CASCADE is compiled with
        OCC_CONVERT_SIGNALS options (i.e. on UNIX/Linux).
        In that case, raising OCC exception and/or signal will not cause
        C++ stack unwinding and destruction of objects created in the stack.

        This class is intended to protect critical objects and operations in
        the try {} catch {} block from being bypassed by OCC signal or exception.

        Inherit your object from that class, implement DestroyCallback() function,
        and call Register/Unregister in critical points.

        Note that you must ensure that your object has life span longer than
        that of the try {} block in which it calls Register().
        """

        def RegisterCallback(self) -> None: ...

        def UnregisterCallback(self) -> None: ...

        def DestroyCallback(self) -> None:
            """
            The callback function to perform necessary callback action.
            Called by the exception handler when it is being destroyed but
            still has this callback registered.
            """

    def Destroy(self) -> None:
        """Unlinks and checks if there is a raised exception."""

    def Raise(self) -> None:
        """
        Throws C++ exception if exception object set,
        otherwise prints error and terminates program.
        """

    def Label(self) -> int:
        """Returns label for jump"""

    def Error(self) -> None | "OSD_SIGBUS" | "OSD_SIGHUP" | "OSD_SIGILL" | "OSD_SIGINT" | "OSD_SIGKILL" | "OSD_SIGQUIT" | "OSD_SIGSEGV" | "OSD_SIGSYS" | "OSD_Exception_ACCESS_VIOLATION" | "OSD_Exception_ARRAY_BOUNDS_EXCEEDED" | "OSD_Exception_ILLEGAL_INSTRUCTION" | "OSD_Exception_IN_PAGE_ERROR" | "OSD_Exception_INT_OVERFLOW" | "OSD_Exception_INVALID_DISPOSITION" | "OSD_Exception_NONCONTINUABLE_EXCEPTION" | "OSD_Exception_PRIV_INSTRUCTION" | "OSD_Exception_STACK_OVERFLOW" | "OSD_Exception_STATUS_NO_MEMORY" | "Standard_DivideByZero" | "Standard_NumericError" | "Standard_Overflow" | "Standard_ProgramError" | "Standard_Underflow":
        """Returns the current Error variant."""

    @staticmethod
    def IsInTryBlock() -> bool:
        """Test if the code is currently running in a try block"""

class Standard_UUID:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Standard_UUID) -> None: ...

    @property
    def Data1(self) -> int: ...

    @Data1.setter
    def Data1(self, arg: int, /) -> None: ...

    @property
    def Data2(self) -> int: ...

    @Data2.setter
    def Data2(self, arg: int, /) -> None: ...

    @property
    def Data3(self) -> int: ...

    @Data3.setter
    def Data3(self, arg: int, /) -> None: ...

class Standard_GUID:
    @overload
    def __init__(self) -> None:
        """Creates a GUID with all zeros."""

    @overload
    def __init__(self, aGuid: str) -> None:
        """
        build a GUID from an ascii string with the
        following format:
        Length : 36 char
        "00000000-0000-0000-0000-000000000000\"
        """

    @overload
    def __init__(self, aGuid: str) -> None:
        """
        build a GUID from an unicode string with the
        following format:

        "00000000-0000-0000-0000-000000000000\"
        """

    @overload
    def __init__(self, theUUID: Standard_UUID) -> None:
        """Creates a GUID from a Standard_UUID."""

    @overload
    def __init__(self, theGuid: Standard_GUID) -> None:
        """Copy constructor."""

    @overload
    def __init__(self, a32b: int, a16b1: str, a16b2: str, a16b3: str, a8b1: int, a8b2: int, a8b3: int, a8b4: int, a8b5: int, a8b6: int) -> None:
        """Creates a GUID from the given components."""

    def ToUUID(self) -> Standard_UUID:
        """Converts to Standard_UUID."""

    def IsSame(self, uid: Standard_GUID) -> bool:
        """Returns true if this GUID is equal to uid."""

    def __eq__(self, uid: Standard_GUID) -> bool: ...

    def IsNotSame(self, uid: Standard_GUID) -> bool:
        """Returns true if this GUID is not equal to uid."""

    def __ne__(self, uid: Standard_GUID) -> bool: ...

    @overload
    def Assign(self, uid: Standard_GUID) -> None: ...

    @overload
    def Assign(self, uid: Standard_UUID) -> None:
        """Assigns uid to this GUID."""

    def ShallowDump(self) -> object:
        """
        Display the GUID with the following format:

        "00000000-0000-0000-0000-000000000000\"
        """

    @staticmethod
    def CheckGUIDFormat(aGuid: str) -> bool:
        """
        Check the format of a GUID string.
        It checks the size, the position of the '-' and the correct size of fields.
        """

    def __hash__(self) -> int: ...

class Standard_ImmutableObject(Standard_DomainError):
    pass

class Standard_LicenseError(Standard_Failure):
    pass

class Standard_LicenseNotFound(Standard_LicenseError):
    pass

class Standard_MMgrRoot:
    """
    Root class for Open CASCADE mmemory managers.
    Defines only abstract interface functions.
    """

    def Purge(self, isDestroyed: bool = False) -> int:
        """
        Purge internally cached unused memory blocks (if any)
        by releasing them to the operating system.
        Must return non-zero if some memory has been actually released,
        or zero otherwise.

        If option isDestroyed is True, this means that memory
        manager is not expected to be used any more; note however
        that in general case it is still possible to have calls to that
        instance of memory manager after this (e.g. to free memory
        of static objects in OCC). Thus this option should
        command the memory manager to release any cached memory
        to the system and not cache any more, but still remain operable...

        Default implementation does nothing and returns 0.
        """

class Standard_MMgrOpt(Standard_MMgrRoot):
    """
    @brief Open CASCADE memory manager optimized for speed.

    The behaviour is different for memory blocks of different sizes,
    according to specified options provided to constructor:

    - Small blocks with size less than or equal to aCellSize are allocated
    in big pools of memory. The parameter aNbPages specifies size of
    these pools in pages (operating system-dependent).
    When freed, small block is not returned to the system but added
    into free blocks list and reused when block of the same size is
    requested.

    - Medium size blocks with size less than aThreshold are allocated
    using malloc() or calloc() function but not returned to the system
    when method Free() is called; instead they are put into free list
    and reused when block of the same size is requested.
    Blocks of medium size stored in free lists can be released to the
    system (by free()) by calling method Purge().

    - Large blocks with size greater than or equal to aThreshold are allocated
    and freed directly: either using malloc()/calloc() and free(), or using
    memory mapped files (if option aMMap is True)

    Thus the optimization of memory allocation/deallocation is reached
    for small and medium size blocks using free lists method;
    note that space allocated for small blocks cannot be (currently) released
    to the system while space for medium size blocks can be released by method Purge().

    Note that destructor of that class frees all free lists and memory pools
    allocated for small blocks.

    Note that size of memory blocks allocated by this memory manager is always
    rounded up to 16 bytes. In addition, 8 bytes are added at the beginning
    of the memory block to hold auxiliary information (size of the block when
    in use, or pointer to the next free block when in free list).
    This the expense of speed optimization. At the same time, allocating small
    blocks is usually less costly than directly by malloc since allocation is made
    once (when allocating a pool) and overheads induced by malloc are minimized.
    """

    def __init__(self, aClear: bool = True, aMMap: bool = True, aCellSize: int = 200, aNbPages: int = 10000, aThreshold: int = 40000) -> None:
        """
        Constructor. If aClear is True, the allocated emmory will be
        nullified. For description of other parameters, see description
        of the class above.
        """

    def Purge(self, isDestroyed: bool) -> int:
        """
        Release medium-sized blocks of memory in free lists to the system.
        Returns number of actually freed blocks
        """

class Standard_MultiplyDefined(Standard_DomainError):
    pass

class Standard_Mutex(Standard_ErrorHandler.Callback):
    def __init__(self) -> None:
        """
        Constructor: creates a mutex object and initializes it.
        It is strongly recommended that mutexes were created as
        static objects whenever possible.
        """

    class Sentry:
        """
        @brief Simple sentry class providing convenient interface to mutex.

        Provides automatic locking and unlocking a mutex in its constructor
        and destructor, thus ensuring correct unlock of the mutex even in case of
        raising an exception or signal from the protected code.

        Create instance of that class when entering critical section.
        """

        @overload
        def __init__(self, theMutex: Standard_Mutex) -> None:
            """
            Constructor - initializes the sentry object by reference to a
            mutex (which must be initialized) and locks the mutex immediately
            """

        @overload
        def __init__(self, theMutex: Standard_Mutex) -> None:
            """
            Constructor - initializes the sentry object by pointer to a
            mutex and locks the mutex if its pointer is not NULL
            """

    def Lock(self) -> None:
        """
        Method to lock the mutex; waits until the mutex is released
        by other threads, locks it and then returns
        """

    def TryLock(self) -> bool:
        """
        Method to test the mutex; if the mutex is not hold by other thread,
        locks it and returns True; otherwise returns False without waiting
        mutex to be released.
        """

    def Unlock(self) -> None:
        """Method to unlock the mutex; releases it to other users"""

class Standard_NegativeValue(Standard_RangeError):
    pass

class Standard_NoMoreObject(Standard_DomainError):
    pass

class Standard_NotImplemented(Standard_ProgramError):
    pass

class Standard_NullObject(Standard_DomainError):
    pass

class Standard_NullValue(Standard_RangeError):
    pass

class Standard_OutOfMemory(Standard_ProgramError):
    """
    Standard_OutOfMemory exception is defined explicitly and not by
    macro DEFINE_STANDARD_EXCEPTION, to avoid necessity of dynamic
    memory allocations during throwing and stack unwinding:

    - message string is stored as field, not allocated dynamically
    (storable message length is limited by buffer size)

    The reason is that in out-of-memory condition any memory allocation can
    fail, thus use of operator new for allocation of new exception instance
    is dangerous (can cause recursion until stack overflow, see #24836).
    """

class Standard_Persistent(Standard_Transient):
    """
    Root of "persistent" classes, a legacy support of
    object oriented databases, now outdated.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Standard_Persistent) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> Standard_Type: ...

    def DynamicType(self) -> Standard_Type: ...

    def TypeNum(self) -> int: ...

    def SetTypeNum(self, theValue: int) -> None:
        """Python addition: sets the value TypeNum() returns by reference in C++."""

class Standard_ReadBuffer:
    """
    Auxiliary tool for buffered reading from input stream within chunks of constant size.
    """

    @overload
    def __init__(self, theDataLen: int, theChunkLen: int, theIsPartialPayload: bool = False) -> None:
        """Constructor with initialization."""

    @overload
    def __init__(self, theOther: Standard_ReadBuffer) -> None: ...

    def Init(self, theDataLen: int, theChunkLen: int, theIsPartialPayload: bool = False) -> None:
        """
        Initialize the buffer.
        @param[in] theDataLen   the full length of input data to read from stream.
        @param[in] theChunkLen  the length of single chunk to read
        @param[in] theIsPartialPayload  when FALSE, theDataLen will be automatically aligned to the
        multiple of theChunkLen;
        when TRUE, last chunk will be read from stream exactly till
        theDataLen allowing portion of chunk to be uninitialized
        (useful for interleaved data)
        """

    def IsDone(self) -> bool:
        """
        Return TRUE if amount of read bytes is equal to requested length of entire data.
        """

class Standard_ReadLineBuffer:
    """Auxiliary tool for buffered reading of lines from input stream."""

    @overload
    def __init__(self, theMaxBufferSizeBytes: int) -> None:
        """
        Constructor with initialization.
        @param theMaxBufferSizeBytes the length of buffer to read (in bytes)
        """

    @overload
    def __init__(self, theOther: Standard_ReadLineBuffer) -> None: ...

    def Clear(self) -> None:
        """Clear buffer and cached values."""

    def IsMultilineMode(self) -> bool:
        """
        Returns TRUE when the Multiline Mode is on; FALSE by default.
        Multiline modes joins several lines in file having \\ at the end of line:
        @code
        Line starts here, \\ // line continuation character without this comment
        continues \\         // line continuation character without this comment
        and ends.
        @endcode
        """

    def ToPutGapInMultiline(self) -> bool:
        """
        Put gap space while merging lines within multiline syntax, so that the following sample:
        @code
        1/2/3\\      // line continuation character without this comment
        4/5/6
        @endcode
        Will become "1/2/3 4/5/6" when flag is TRUE, and "1/2/35/5/6" otherwise.
        """

    def SetMultilineMode(self, theMultilineMode: bool, theToPutGap: bool = True) -> None:
        """
        Sets or unsets the multi-line mode.
        @param[in] theMultilineMode  multiline mode flag
        @param[in] theToPutGap       put gap space while connecting lines (no gap otherwise)
        """

Standard_ErrorHandlerCallback: TypeAlias = Standard_ErrorHandler.Callback

@overload
def Abs(theValue: int) -> int:
    """
    Returns the absolute value of a int @p Value.
    Equivalent to std::abs.
    """

@overload
def Abs(theValue: float) -> float:
    """
    Returns the absolute value of a double @p Value.
    Equivalent to std::abs.
    """

@overload
def Abs(theValue: float) -> float:
    """
    Returns the absolute value of a float @p Value.
    Equivalent to std::abs.
    """

def IsEven(theValue: int) -> bool:
    """Returns true if @p theValue is even."""

def IsOdd(theValue: int) -> bool:
    """Returns true if @p theValue is odd."""

@overload
def Max(theValue1: int, theValue2: int) -> int:
    """
    Returns the maximum value of two integers.
    Equivalent to std::max.
    """

@overload
def Max(theValue1: float, theValue2: float) -> float:
    """
    Returns the maximum value of two doubles.
    Equivalent to std::max.
    """

@overload
def Max(theValue1: float, theValue2: float) -> float:
    """
    Returns the maximum value of two floats.
    Equivalent to std::max.
    """

@overload
def Min(theValue1: int, theValue2: int) -> int:
    """
    Returns the minimum value of two integers.
    Equivalent to std::min.
    """

@overload
def Min(theValue1: float, theValue2: float) -> float:
    """
    Returns the minimum value of two doubles.
    Equivalent to std::min.
    """

@overload
def Min(theValue1: float, theValue2: float) -> float:
    """
    Returns the minimum value of two floats.
    Equivalent to std::min.
    """

def Modulus(theValue: int, theDivisor: int) -> int:
    """Returns the modulus of @p theValue by @p theDivisor."""

@overload
def Square(theValue: int) -> int:
    """
    Returns the square of a int @p theValue.
    Note that behavior is undefined in case of overflow.
    """

@overload
def Square(theValue: float) -> float:
    """Returns the square of a double @p theValue."""

def IntegerFirst() -> int:
    """Returns the minimum value of an integer."""

def IntegerLast() -> int:
    """Returns the maximum value of an integer."""

def IntegerSize() -> int:
    """Returns the size in bits of an integer."""

def ACos(theValue: float) -> float:
    """Returns the value of the arc cosine of a @p theValue."""

def ACosApprox(theValue: float) -> float:
    """
    Returns the approximate value of the arc cosine @p theValue.
    The max error is about 1 degree near Value=0.
    NOTE: Avoid using this function in new code, it presumably slower then std::acos.
    """

def ASin(theValue: float) -> float:
    """Returns the value of the arc sine of a @p theValue."""

def ATan2(theX: float, theY: float) -> float:
    """
    Computes the arc tangent of @p theX divided by @p theY using the signs of both
    arguments to determine the quadrant of the return value.
    """

def ATanh(theValue: float) -> float:
    """Returns the value of the hyperbolic arc tangent of @p theValue."""

def ACosh(theValue: float) -> float:
    """Returns the value of the hyperbolic arc cosine of @p theValue."""

def Cosh(theValue: float) -> float:
    """Returns the hyperbolic cosine of a double @p theValue."""

def Sinh(theValue: float) -> float:
    """Returns the hyperbolic sine of a double @p theValue."""

def Log(theValue: float) -> float:
    """Computes the natural (base-e) logarithm of number @p theValue."""

def Sqrt(theValue: float) -> float:
    """Returns the square root of a double @p theValue."""

def NextAfter(theValue: float, theDirection: float) -> float:
    """
    Returns the next representable value of a double @p theValue
    in the direction of @p theDirection. Equivalent to std::nextafter.
    """

def Sign(theMagnitude: float, theSign: float) -> float:
    """
    Composes a floating point value with the magnitude of @p theMagnitude
    and the sign of @p theSign. Equivalent to std::copysign.
    """

def RealSmall() -> float:
    """Returns the minimum positive double value greater than zero."""

@overload
def IsEqual(theValue1: float, theValue2: float) -> bool:
    """
    Returns Standard_True if two doubles are equal within the precision
    defined by RealSmall().
    """

@overload
def IsEqual(One: str, Two: str) -> bool: ...

@overload
def IsEqual(One: str, Two: str) -> bool: ...

@overload
def IsEqual(theOne: str, theTwo: str) -> bool:
    """Returns Standard_True if two strings are equal"""

def RealDigits() -> int:
    """Returns the number of digits of precision in a double."""

def RealEpsilon() -> float:
    """
    Returns the minimum positive double such that
    1.0 + RealEpsilon() != 1.0.
    """

def RealFirst() -> float:
    """Returns the minimum value of a double."""

def RealFirst10Exp() -> int:
    """Returns the minimum value of exponent(base 10) of a double."""

def RealLast() -> float:
    """Returns the maximum value of a double."""

def RealLast10Exp() -> int:
    """Returns the maximum value of exponent(base 10) of a double."""

def RealMantissa() -> int:
    """Returns the size in bits of the mantissa part of a double."""

def RealRadix() -> int:
    """Returns the radix of a double."""

def RealSize() -> int:
    """Returns the size in bits of a double."""

def IntToReal(theValue: int) -> float:
    """Converts a int @p theValue to a double."""

def ATan(theValue: float) -> float:
    """Returns the value of the arc tangent of a double @p theValue."""

def Ceiling(theValue: float) -> float:
    """
    Returns the next integer greater than or equal to a double @p theValue.
    """

def Cos(theValue: float) -> float:
    """
    Returns the cosine of a double @p theValue.
    Equivalent to std::cos.
    """

def Epsilon(theValue: float) -> float:
    """
    The function returns absolute value of difference between @p theValue and other nearest value of
    double type. Nearest value is chosen in direction of infinity the same sign as @p theValue.
    If @p theValue is 0 then returns minimal positive value of double type.
    """

def Exp(theValue: float) -> float:
    """
    Returns the exponential of a double @p theValue.
    Equivalent to std::exp.
    """

def Floor(theValue: float) -> float:
    """
    Returns the nearest integer less than or equal to a double @p theValue.
    Equivalent to std::floor.
    """

def IntegerPart(theValue: float) -> float:
    """
    Returns the integer part of a double @p theValue.
    Equivalent to std::trunc.
    """

def Log10(theValue: float) -> float:
    """
    Returns the logarithm to base 10 of a double @p theValue.
    Equivalent to std::log10.
    """

def Pow(theValue: float, thePower: float) -> float:
    """Returns a double @p theValue raised to the power of @p thePower."""

def RealPart(theValue: float) -> float:
    """
    Returns the fractional part of a double @p theValue.
    Always non-negative.
    """

def RealToInt(theValue: float) -> int:
    """
    Converts a double @p theValue to the nearest valid int.
    If input value is out of valid range for int, minimal or maximal possible int is returned.
    """

def RealToShortReal(theValue: float) -> float:
    """
    Converts a double @p theValue to the nearest valid float.
    If input value is out of valid range for float, minimal or maximal
    possible float is returned.
    """

def Round(theValue: float) -> float:
    """
    Returns the nearest integer of a double @p theValue.
    Equivalent to std::round.
    """

def Sin(theValue: float) -> float:
    """
    Returns the sine of a double @p theValue.
    Equivalent to std::sin.
    """

def ASinh(theValue: float) -> float:
    """
    Returns the hyperbolic arc sine of a double @p theValue.
    Equivalent to std::asinh.
    """

def Tan(theValue: float) -> float:
    """
    Returns the tangent of a double @p theValue.
    Equivalent to std::tan.
    """

def Tanh(theValue: float) -> float:
    """
    Returns the hyperbolic tangent of a double @p theValue.
    Equivalent to std::tanh.
    """

def IsAlphabetic(me: str) -> bool: ...

def IsDigit(me: str) -> bool: ...

def IsXDigit(me: str) -> bool: ...

def IsAlphanumeric(me: str) -> bool: ...

def IsControl(me: str) -> bool: ...

def IsGraphic(me: str) -> bool: ...

def IsLowerCase(me: str) -> bool: ...

def IsPrintable(me: str) -> bool: ...

def IsPunctuation(me: str) -> bool: ...

def IsSpace(me: str) -> bool: ...

def IsUpperCase(me: str) -> bool: ...

def LowerCase(me: str) -> str: ...

def UpperCase(me: str) -> str: ...

def ToExtCharacter(achar: str) -> str: ...

def ToCharacter(achar: str) -> str: ...

def IsAnAscii(achar: str) -> bool: ...

def Standard_ASSERT_DO_NOTHING() -> None:
    """
    @file
    This header file defines a set of ASSERT macros intended for use
    in algorithms for debugging purposes and as a tool to organise
    checks for abnormal situations in the uniform way.

    In contrast to C assert() function that terminates the process, these
    macros provide choice of the action to be performed if assert failed,
    thus allowing execution to continue when possible.
    Except for the message for developer that appears only in Debug mode,
    the macros behave in the same way in both Release and Debug modes.


    The ASSERT macros differ in the way they react on a wrong situation:
    - Standard_ASSERT_RAISE:  raises exception Standard_ProgramError
    - Standard_ASSERT_RETURN: returns specified value (last argument may
    be left empty to return void)
    - Standard_ASSERT_SKIP:   does nothing
    - Standard_ASSERT_VOID:   does nothing; even does not evaluate first arg
    when in Release mode
    - Standard_ASSERT_INVOKE: causes unconditional assert
    - Standard_ASSERT:        base macro (used by other macros);
    does operation indicated in argument "todo"

    The assertion is assumed to fail if the first argument is
    evaluated to zero (false).
    The first argument is evaluated by all macros except Standard_ASSERT_VOID
    which does not evaluate first argument when in Release mode.
    The mode is triggered by preprocessor macro _DEBUG: if it is defined,
    Debug mode is assumed, Release otherwise.

    In debug mode, if condition is not satisfied the macros call
    Standard_ASSERT_INVOKE_ which:
    - on Windows (under VC++), stops code execution and prompts to attach
    debugger to the process immediately.
    - on POSIX systems, prints message to cerr and raises signal SIGTRAP to stop
    execution when under debugger (may terminate the process if not under debugger).

    The second argument (message) should be string constant ("...").

    The Standard_STATIC_ASSERT macro is to be used for compile time checks.
    To use this macro, write:

    Standard_STATIC_ASSERT(const_expression);

    If const_expression is false, a compiler error occurs.

    The macros are formed as functions and require semicolon at the end.
    """

def ShortRealSmall() -> float:
    """Returns the minimum positive float value."""

def ShortRealDigits() -> int:
    """Returns the number of digits of precision in a float."""

def ShortRealEpsilon() -> float:
    """
    Returns the minimum positive float such that 1.0f + ShortRealEpsilon() != 1.0f.
    """

def ShortRealFirst() -> float:
    """Returns the minimum negative value of a float."""

def ShortRealFirst10Exp() -> int:
    """Returns the minimum value of exponent(base 10) of a float."""

def ShortRealLast() -> float:
    """Returns the maximum value of a float."""

def ShortRealLast10Exp() -> int:
    """Returns the maximum value of exponent(base 10) of a float."""

def ShortRealMantissa() -> int:
    """Returns the mantissa (number of bits in the significand) of a float."""

def ShortRealRadix() -> int:
    """Returns the radix (base) of a float."""

def ShortRealSize() -> int:
    """Returns the size in bits of a float."""

# C++ typedef aliases
Standard_HMutex = nanoocp.NCollection.NCollection_Shared[nanoocp.Standard.Standard_Mutex]
