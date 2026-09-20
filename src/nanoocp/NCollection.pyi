from typing import Generic, Self, TypeVar, overload
from collections.abc import Iterator
import nanoocp.Standard

_T = TypeVar('_T')
_K = TypeVar('_K')
_V = TypeVar('_V')

class NCollection_Array1(Generic[_T]):
    """NCollection_Array1<T>: unidimensional array of fixed size with user-defined index range (OCCT).
    Instantiations are the concrete classes NCollection_Array1__<T>; NCollection_Array1[T] returns them."""
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    @overload
    def __init__(self, theSize: int) -> None: ...
    @overload
    def __init__(self, theOther: NCollection_Array1[_T]) -> None: ...
    def Init(self, theValue: _T) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDeletable(self) -> bool: ...
    def Assign(self, theOther: NCollection_Array1[_T]) -> Self: ...
    def CopyValues(self, theOther: NCollection_Array1[_T]) -> Self: ...
    def First(self) -> _T: ...
    def Last(self) -> _T: ...
    def Value(self, theIndex: int) -> _T: ...
    def At(self, theIndex: int) -> _T: ...
    def SetValue(self, theIndex: int, theItem: _T) -> None: ...
    def UpdateLowerBound(self, theLower: int) -> None: ...
    def UpdateUpperBound(self, theUpper: int) -> None: ...
    @overload
    def Resize(self, theLower: int, theUpper: int, theToCopyData: bool) -> None: ...
    @overload
    def Resize(self, theSize: int, theToCopyData: bool) -> None: ...
    def ChangeFirst(self) -> _T: ...
    def ChangeLast(self) -> _T: ...
    def ChangeValue(self, theIndex: int) -> _T: ...
    def ChangeAt(self, theIndex: int) -> _T: ...
    def __call__(self, theIndex: int) -> _T: ...
    def __getitem__(self, theIndex: int) -> _T: ...
    def __setitem__(self, theIndex: int, theItem: _T) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
class NCollection_HArray1(nanoocp.Standard.Standard_Transient, Generic[_T]):
    """NCollection_HArray1<T>: handle-managed (Standard_Transient) NCollection_Array1<T>."""
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int, theValue: _T) -> None: ...
    @overload
    def __init__(self, theOther: NCollection_Array1[_T]) -> None: ...
    def Array1(self) -> NCollection_Array1[_T]: ...
    def ChangeArray1(self) -> Self: ...
    def Init(self, theValue: _T) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDeletable(self) -> bool: ...
    def Assign(self, theOther: NCollection_Array1[_T]) -> Self: ...
    def CopyValues(self, theOther: NCollection_Array1[_T]) -> Self: ...
    def First(self) -> _T: ...
    def Last(self) -> _T: ...
    def Value(self, theIndex: int) -> _T: ...
    def At(self, theIndex: int) -> _T: ...
    def SetValue(self, theIndex: int, theItem: _T) -> None: ...
    def UpdateLowerBound(self, theLower: int) -> None: ...
    def UpdateUpperBound(self, theUpper: int) -> None: ...
    @overload
    def Resize(self, theLower: int, theUpper: int, theToCopyData: bool) -> None: ...
    @overload
    def Resize(self, theSize: int, theToCopyData: bool) -> None: ...
    def ChangeFirst(self) -> _T: ...
    def ChangeLast(self) -> _T: ...
    def ChangeValue(self, theIndex: int) -> _T: ...
    def ChangeAt(self, theIndex: int) -> _T: ...
    def __call__(self, theIndex: int) -> _T: ...
    def __getitem__(self, theIndex: int) -> _T: ...
    def __setitem__(self, theIndex: int, theItem: _T) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...

"""OCCT package NCollection (toolkit TKernel)"""

from collections.abc import Iterator
import enum
from typing import overload

import nanoocp.Standard


class NCollection_CellFilter_Action(enum.IntEnum):
    """Auxiliary enumeration serving as response from method Inspect"""

    CellFilter_Keep = 0

    CellFilter_Purge = 1

class NCollection_BaseAllocator(nanoocp.Standard.Standard_Transient):
    """
    Purpose:     Basic class for memory allocation wizards.
    Defines  the  interface  for devising  different  allocators
    firstly to be used  by collections of NCollection, though it
    it is not  deferred. It allocates/frees  the memory  through
    Standard procedures, thus it is  unnecessary (and  sometimes
    injurious) to have  more than one such  allocator.  To avoid
    creation  of multiple  objects the  constructors  were  maid
    inaccessible.  To  create the  BaseAllocator use  the method
    CommonBaseAllocator.
    Note that this object is managed by Handle.
    """

    @staticmethod
    def CommonBaseAllocator() -> NCollection_BaseAllocator:
        """
        CommonBaseAllocator
        This method is designed to have the only one BaseAllocator (to avoid
        useless copying of collections). However one can use operator new to
        create more BaseAllocators, but it is injurious.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class NCollection_ListNode:
    """
    Purpose:     This class is used to  represent a node  in the BaseList and
    BaseMap.
    """

    def Next(self) -> NCollection_ListNode:
        """Next pointer const access"""

class NCollection_BaseMap:
    """
    Purpose:     This is a base class for all Maps:
    Map
    DataMap
    DoubleMap
    IndexedMap
    IndexedDataMap
    Provides utilitites for managing the buckets.
    """

    def NbBuckets(self) -> int:
        """NbBuckets"""

    def Extent(self) -> int:
        """Extent (number of elements, legacy int-returning API)."""

    def Length(self) -> int:
        """
        Length - number of elements (legacy int-returning API, synonym of Extent()).
        """

    def Size(self) -> int:
        """Size - number of elements."""

    def IsEmpty(self) -> bool:
        """IsEmpty"""

    def Allocator(self) -> NCollection_BaseAllocator:
        """Returns attached allocator"""

class NCollection_DefaultHasher__bool:
    """Explicit specialization for bool."""

    def __init__(self) -> None: ...

    @overload
    def __call__(self, theKey: bool) -> int: ...

    @overload
    def __call__(self, theK1: bool, theK2: bool) -> bool: ...

class NCollection_DefaultHasher__char:
    """Explicit specialization for char."""

    def __init__(self) -> None: ...

    @overload
    def __call__(self, theKey: str) -> int: ...

    @overload
    def __call__(self, theK1: str, theK2: str) -> bool: ...

class NCollection_DefaultHasher__signed_char:
    """Explicit specialization for signed char."""

    def __init__(self) -> None: ...

    @overload
    def __call__(self, theKey: int) -> int: ...

    @overload
    def __call__(self, theK1: int, theK2: int) -> bool: ...

class NCollection_DefaultHasher__unsigned_char:
    """Explicit specialization for unsigned char."""

    def __init__(self) -> None: ...

    @overload
    def __call__(self, theKey: int) -> int: ...

    @overload
    def __call__(self, theK1: int, theK2: int) -> bool: ...

class NCollection_DefaultHasher__wchar_t:
    """Explicit specialization for wchar_t."""

    def __init__(self) -> None: ...

    @overload
    def __call__(self, theKey: "wchar_t") -> int: ...

    @overload
    def __call__(self, theK1: "wchar_t", theK2: "wchar_t") -> bool: ...

class NCollection_DefaultHasher__char16_t:
    """Explicit specialization for char16_t."""

    def __init__(self) -> None: ...

    @overload
    def __call__(self, theKey: "char16_t") -> int: ...

    @overload
    def __call__(self, theK1: "char16_t", theK2: "char16_t") -> bool: ...

class NCollection_DefaultHasher__char32_t:
    """Explicit specialization for char32_t."""

    def __init__(self) -> None: ...

    @overload
    def __call__(self, theKey: "char32_t") -> int: ...

    @overload
    def __call__(self, theK1: "char32_t", theK2: "char32_t") -> bool: ...

class NCollection_DefaultHasher__short:
    """Explicit specialization for short."""

    def __init__(self) -> None: ...

    @overload
    def __call__(self, theKey: int) -> int: ...

    @overload
    def __call__(self, theK1: int, theK2: int) -> bool: ...

class NCollection_DefaultHasher__int:
    """Explicit specialization for int."""

    def __init__(self) -> None: ...

    @overload
    def __call__(self, theKey: int) -> int: ...

    @overload
    def __call__(self, theK1: int, theK2: int) -> bool: ...

class NCollection_DefaultHasher__long:
    """Explicit specialization for long."""

    def __init__(self) -> None: ...

    @overload
    def __call__(self, theKey: int) -> int: ...

    @overload
    def __call__(self, theK1: int, theK2: int) -> bool: ...

class NCollection_DefaultHasher__long_long:
    """Explicit specialization for long long."""

    def __init__(self) -> None: ...

    @overload
    def __call__(self, theKey: int) -> int: ...

    @overload
    def __call__(self, theK1: int, theK2: int) -> bool: ...

class NCollection_DefaultHasher__unsigned_short:
    """Explicit specialization for unsigned short."""

    def __init__(self) -> None: ...

    @overload
    def __call__(self, theKey: int) -> int: ...

    @overload
    def __call__(self, theK1: int, theK2: int) -> bool: ...

class NCollection_DefaultHasher__unsigned_int:
    """Explicit specialization for unsigned int."""

    def __init__(self) -> None: ...

    @overload
    def __call__(self, theKey: int) -> int: ...

    @overload
    def __call__(self, theK1: int, theK2: int) -> bool: ...

class NCollection_DefaultHasher__unsigned_long:
    """Explicit specialization for unsigned long."""

    def __init__(self) -> None: ...

    @overload
    def __call__(self, theKey: int) -> int: ...

    @overload
    def __call__(self, theK1: int, theK2: int) -> bool: ...

class NCollection_DefaultHasher__unsigned_long_long:
    """Explicit specialization for unsigned long long."""

    def __init__(self) -> None: ...

    @overload
    def __call__(self, theKey: int) -> int: ...

    @overload
    def __call__(self, theK1: int, theK2: int) -> bool: ...

class NCollection_SeqNode:
    def Next(self) -> NCollection_SeqNode: ...

    def Previous(self) -> NCollection_SeqNode: ...

    def SetNext(self, theNext: NCollection_SeqNode) -> None: ...

    def SetPrevious(self, thePrev: NCollection_SeqNode) -> None: ...

class NCollection_BaseSequence:
    """
    Purpose:     This  is  a base  class  for  the  Sequence.  It  deals with
    an indexed bidirectional list of NCollection_SeqNode's.
    """

    def IsEmpty(self) -> bool: ...

    def Length(self) -> int:
        """Number of items (legacy int-returning API)."""

    def Size(self) -> int:
        """Size - number of items."""

    def Allocator(self) -> NCollection_BaseAllocator:
        """Returns attached allocator"""

class NCollection_AccAllocator(NCollection_BaseAllocator):
    """
    Class NCollection_AccAllocator - accumulating memory allocator. This
    class allocates memory on request returning the pointer to the allocated
    space. The allocation units are grouped in blocks requested from the
    system as required. This memory is returned to the system when all
    allocations in a block are freed.

    By comparison with the standard new() and malloc() calls, this method is
    faster and consumes very small additional memory to maintain the heap.

    By comparison with NCollection_IncAllocator, this class requires some more
    additional memory and a little more time for allocation and deallocation.
    Memory overhead for NCollection_IncAllocator is 12 bytes per block;
    average memory overhead for NCollection_AccAllocator is 28 bytes per block.

    All pointers returned by Allocate() are aligned to 4 byte boundaries.
    To define the sizeof memory blocks requested from the OS, use the
    parameter of the constructor (measured in bytes).
    """

    def __init__(self, theBlockSize: int = 24600) -> None:
        """Constructor"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class NCollection_AlignedAllocator(NCollection_BaseAllocator):
    """NCollection allocator with managed memory alignment capabilities."""

    def __init__(self, theAlignment: int) -> None:
        """
        Constructor. The alignment should be specified explicitly:
        16 bytes for SSE instructions
        32 bytes for AVX instructions
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class NCollection_BaseList:
    def Extent(self) -> int: ...

    def Length(self) -> int:
        """
        Length - number of nodes (legacy int-returning API, synonym of Extent()).
        """

    def Size(self) -> int:
        """Size - number of nodes."""

    def IsEmpty(self) -> bool: ...

    def Allocator(self) -> NCollection_BaseAllocator:
        """Returns attached allocator"""

class NCollection_Buffer(nanoocp.Standard.Standard_Transient):
    """Low-level buffer object."""

    def IsEmpty(self) -> bool:
        """@return true if buffer is not allocated"""

    def Size(self) -> int:
        """Return buffer length in bytes."""

    def Allocator(self) -> NCollection_BaseAllocator:
        """@return buffer allocator"""

    def SetAllocator(self, theAlloc: NCollection_BaseAllocator) -> None:
        """Assign new buffer allocator with de-allocation of buffer."""

    def Allocate(self, theSize: int) -> bool:
        """
        Allocate the buffer.
        @param theSize buffer length in bytes
        """

    def Free(self) -> None:
        """De-allocate buffer."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class NCollection_IncAllocator(NCollection_BaseAllocator):
    """
    Class NCollection_IncAllocator - incremental memory  allocator. This class
    allocates  memory  on  request  returning  the  pointer  to  an  allocated
    block. This memory is never returned  to the system until the allocator is
    destroyed.

    By comparison with  the standard new() and malloc()  calls, this method is
    faster and consumes very small additional memory to maintain the heap.

    All pointers  returned by Allocate() are  aligned to the size  of the data
    type "aligned_t". To  modify the size of memory  blocks requested from the
    OS,  use the parameter  of the  constructor (measured  in bytes);  if this
    parameter is  smaller than  25 bytes on  32bit or  49 bytes on  64bit, the
    block size will be the default 12 kbytes.

    It is not recommended  to use memory blocks  larger than 16KB  on  Windows
    platform  for the repeated operations  because  Low Fragmentation Heap  is
    not going to be  used  for  these  allocations  which  may lead  to memory
    fragmentation and the general performance slow down.

    Note that this allocator is most suitable for single-threaded algorithms
    (consider creating dedicated allocators per working thread),
    and thread-safety of allocations is DISABLED by default (see SetThreadSafe()).
    """

    def __init__(self, theBlockSize: int = 12288) -> None:
        """
        Constructor.
        Note that this constructor does NOT setup mutex for using allocator concurrently from
        different threads, see SetThreadSafe() method.

        The default size of the memory blocks is 12KB.
        It is not recommended to use memory blocks larger than 16KB on Windows
        platform for the repeated operations (and thus multiple allocations)
        because Low Fragmentation Heap is not going to be used for these allocations,
        leading to memory fragmentation and eventual performance slow down.
        """

    class IBlockSizeLevel(enum.Enum):
        """Description ability to next growing size each 5-th new block"""

        Min = 0

        Small = 1

        Medium = 2

        Large = 3

        Max = 4

    def SetThreadSafe(self, theIsThreadSafe: bool = True) -> None:
        """
        Setup mutex for thread-safe allocations.
        @warning Must not be called concurrently with Allocate/AllocateOptimal/Reset/clean
        on the same allocator instance; toggling the mutex while another thread
        holds a shared_lock on the fast path is undefined behaviour.
        """

    def Reset(self, theReleaseMemory: bool = False) -> None:
        """
        Re-initialize the allocator so that the next Allocate call should
        start allocating in the very beginning as though the allocator is just
        constructed. Warning: make sure that all previously allocated data are
        no more used in your code!
        @param theReleaseMemory
        True - release all previously allocated memory, False - preserve it
        for future allocations.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class NCollection_ForwardRangeSentinel:
    """Empty sentinel type used as the end marker for range-for loops."""

    def __init__(self) -> None: ...

class NCollection_HeapAllocator(NCollection_BaseAllocator):
    """Allocator that uses the global dynamic heap (malloc / free)."""

    @staticmethod
    def GlobalHeapAllocator() -> NCollection_HeapAllocator: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class NCollection_SparseArrayBase:
    """
    Base class for NCollection_SparseArray;
    provides non-template implementation of general mechanics
    of block allocation, items creation / deletion etc.

    Type-specific item operations (construction, destruction, copy)
    are provided by the derived template class via function pointers
    passed as arguments to the protected methods.
    """

    def Size(self) -> int:
        """Returns number of currently contained items"""

    def HasValue(self, theIndex: int) -> bool:
        """Check whether the value at given index is set"""

class NCollection_WinHeapAllocator(NCollection_BaseAllocator):
    """
    This memory allocator creates dedicated heap for allocations.
    This technics available only on Windows platform
    (no alternative on Unix systems).
    It may be used to take control over memory fragmentation
    because on destruction ALL allocated memory will be released
    to the system.

    This allocator can also be created per each working thread
    however its real multi-threading performance is dubious.

    Notice that this also means that existing pointers will be broken
    and you should control that allocator is alive along all objects
    allocated with him.
    """

    def __init__(self, theInitSizeBytes: int = 524288) -> None:
        """Main constructor"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class NCollection_Array1__Handle_Standard_Persistent(NCollection_Array1[nanoocp.Standard.Standard_Persistent]): ...
class NCollection_HArray1__Handle_Standard_Persistent(NCollection_HArray1[nanoocp.Standard.Standard_Persistent]): ...
class NCollection_Array1__double(NCollection_Array1[float]): ...
