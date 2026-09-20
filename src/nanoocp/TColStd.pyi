"""OCCT package TColStd (toolkit TKernel)"""

from typing import overload

import nanoocp.Standard


class TColStd_PackedMapOfInteger:
    """
    @brief Optimized Map for integer values of various integral types.

    This template class provides a memory-efficient storage for sets of integers.
    Each block of BitsPerBlock (32 or 64) consecutive integers is stored compactly
    using bit manipulation. The block size is automatically selected based on
    the integer type: 32 bits for int/unsigned, 64 bits for int64_t/size_t.

    @tparam IntType The integral type to store (int, unsigned int, int64_t, size_t, etc.)
    """

    @overload
    def __init__(self, theNbBuckets: int = 1) -> None:
        """Constructor"""

    @overload
    def __init__(self, theNbBuckets: int) -> None:
        """Constructor (legacy int-taking)."""

    @overload
    def __init__(self, theOther: TColStd_PackedMapOfInteger) -> None:
        """Copy constructor"""

    def Assign(self, theOther: TColStd_PackedMapOfInteger) -> TColStd_PackedMapOfInteger:
        """Assignment operator"""

    @overload
    def ReSize(self, theNbBuckets: int) -> None:
        """Resize the map"""

    @overload
    def ReSize(self, theNbBuckets: int) -> None:
        """Resize the map (legacy int-taking)."""

    def Clear(self) -> None:
        """Clear the map"""

    def Add(self, theKey: int) -> bool:
        """
        Add a key to the map
        @param[in] theKey the key to add
        @return true if the key was added, false if it already existed
        """

    def Contains(self, theKey: int) -> bool:
        """
        Check if the map contains a key
        @param[in] theKey the key to check
        @return true if the key is in the map
        """

    def Remove(self, theKey: int) -> bool:
        """
        Remove a key from the map
        @param[in] theKey the key to remove
        @return true if the key was removed, false if it was not present
        """

    def NbBuckets(self) -> int:
        """Returns the number of map buckets."""

    def Extent(self) -> int:
        """Returns map extent (legacy int-returning API)."""

    def Length(self) -> int:
        """Returns map extent (legacy int-returning API, synonym of Extent())."""

    def Size(self) -> int:
        """Returns map extent."""

    def IsEmpty(self) -> bool:
        """Returns TRUE if map is empty."""

    def GetMinimalMapped(self) -> int:
        """Query the minimal contained key value."""

    def GetMaximalMapped(self) -> int:
        """Query the maximal contained key value."""

class TColStd_HPackedMapOfInteger(nanoocp.Standard.Standard_Transient):
    """
    @deprecated This Handle wrapper class is deprecated.
    Use TColStd_PackedMapOfInteger directly instead.
    """

    @overload
    def __init__(self, theNbBuckets: int = 1) -> None:
        """
        Constructor of empty map.
        @param theNbBuckets initial number of buckets
        """

    @overload
    def __init__(self, theOther: TColStd_PackedMapOfInteger) -> None:
        """
        Constructor from already existing map; performs copying.
        @param theOther the map to copy
        """

    def Map(self) -> TColStd_PackedMapOfInteger:
        """Returns const reference to the underlying map."""

    def ChangeMap(self) -> TColStd_PackedMapOfInteger:
        """Returns mutable reference to the underlying map."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
TColStd_Array1OfInteger = nanoocp.NCollection.NCollection_Array1__int
TColStd_Array1OfReal = nanoocp.NCollection.NCollection_Array1__double
TColStd_Array2OfInteger = nanoocp.NCollection.NCollection_Array2__int
TColStd_Array2OfReal = nanoocp.NCollection.NCollection_Array2__double
TColStd_HArray1OfInteger = nanoocp.NCollection.NCollection_HArray1__int
TColStd_HArray1OfReal = nanoocp.NCollection.NCollection_HArray1__double
TColStd_HArray2OfInteger = nanoocp.NCollection.NCollection_HArray2__int
TColStd_HArray2OfReal = nanoocp.NCollection.NCollection_HArray2__double
TColStd_HSequenceOfAsciiString = nanoocp.NCollection.NCollection_HSequence__TCollection_AsciiString
TColStd_HSequenceOfHAsciiString = nanoocp.NCollection.NCollection_HSequence__Handle_TCollection_HAsciiString
TColStd_HSequenceOfHExtendedString = nanoocp.NCollection.NCollection_HSequence__Handle_TCollection_HExtendedString
TColStd_HSequenceOfInteger = nanoocp.NCollection.NCollection_HSequence__int
TColStd_ListOfInteger = nanoocp.NCollection.NCollection_List__int
TColStd_SequenceOfAsciiString = nanoocp.NCollection.NCollection_Sequence__TCollection_AsciiString
TColStd_SequenceOfExtendedString = nanoocp.NCollection.NCollection_Sequence__TCollection_ExtendedString
TColStd_SequenceOfHAsciiString = nanoocp.NCollection.NCollection_Sequence__Handle_TCollection_HAsciiString
TColStd_SequenceOfHExtendedString = nanoocp.NCollection.NCollection_Sequence__Handle_TCollection_HExtendedString
TColStd_SequenceOfInteger = nanoocp.NCollection.NCollection_Sequence__int
TColStd_SequenceOfTransient = nanoocp.NCollection.NCollection_Sequence__Handle_Standard_Transient
