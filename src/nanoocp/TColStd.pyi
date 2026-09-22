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
        """Resize the map (legacy int-taking)."""

    @overload
    def ReSize(self, theNbBuckets: int) -> None:
        """Resize the map"""

    def Clear(self) -> None:
        """Clear the map"""

    def Add(self, theKey: int) -> bool:
        """
        Add a key to the map
        @param[in] theKey the key to add
        @return true if the key was added, false if it already existed
        """

    @overload
    def Contains(self, theKey: int) -> bool:
        """
        Check if the map contains a key
        @param[in] theKey the key to check
        @return true if the key is in the map
        """

    @overload
    def Contains(self, theOther: TColStd_PackedMapOfInteger) -> bool:
        """
        Deprecated in OCCT: This method will be removed after OCCT 7.9 release. Use methods from NCollection_PackedMapAlgo.hxx instead.

        @deprecated Use NCollection_PackedMapAlgo::Contains() instead
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

    def Union(self, theLeft: TColStd_PackedMapOfInteger, theRight: TColStd_PackedMapOfInteger) -> None:
        """
        Deprecated in OCCT: This method will be removed after OCCT 7.9 release. Use methods from NCollection_PackedMapAlgo.hxx instead.

        @deprecated Use NCollection_PackedMapAlgo::Union() instead
        """

    def Unite(self, theOther: TColStd_PackedMapOfInteger) -> bool:
        """
        Deprecated in OCCT: This method will be removed after OCCT 7.9 release. Use methods from NCollection_PackedMapAlgo.hxx instead.

        @deprecated Use NCollection_PackedMapAlgo::Unite() instead
        """

    def Intersection(self, theLeft: TColStd_PackedMapOfInteger, theRight: TColStd_PackedMapOfInteger) -> None:
        """
        Deprecated in OCCT: This method will be removed after OCCT 7.9 release. Use methods from NCollection_PackedMapAlgo.hxx instead.

        @deprecated Use NCollection_PackedMapAlgo::Intersection() instead
        """

    def Intersect(self, theOther: TColStd_PackedMapOfInteger) -> bool:
        """
        Deprecated in OCCT: This method will be removed after OCCT 7.9 release. Use methods from NCollection_PackedMapAlgo.hxx instead.

        @deprecated Use NCollection_PackedMapAlgo::Intersect() instead
        """

    def Subtraction(self, theLeft: TColStd_PackedMapOfInteger, theRight: TColStd_PackedMapOfInteger) -> None:
        """
        Deprecated in OCCT: This method will be removed after OCCT 7.9 release. Use methods from NCollection_PackedMapAlgo.hxx instead.

        @deprecated Use NCollection_PackedMapAlgo::Subtraction() instead
        """

    def Subtract(self, theOther: TColStd_PackedMapOfInteger) -> bool:
        """
        Deprecated in OCCT: This method will be removed after OCCT 7.9 release. Use methods from NCollection_PackedMapAlgo.hxx instead.

        @deprecated Use NCollection_PackedMapAlgo::Subtract() instead
        """

    def Difference(self, theLeft: TColStd_PackedMapOfInteger, theRight: TColStd_PackedMapOfInteger) -> None:
        """
        Deprecated in OCCT: This method will be removed after OCCT 7.9 release. Use methods from NCollection_PackedMapAlgo.hxx instead.

        @deprecated Use NCollection_PackedMapAlgo::Difference() instead
        """

    def Differ(self, theOther: TColStd_PackedMapOfInteger) -> bool:
        """
        Deprecated in OCCT: This method will be removed after OCCT 7.9 release. Use methods from NCollection_PackedMapAlgo.hxx instead.

        @deprecated Use NCollection_PackedMapAlgo::Differ() instead
        """

    def IsEqual(self, theOther: TColStd_PackedMapOfInteger) -> bool:
        """
        Deprecated in OCCT: This method will be removed after OCCT 7.9 release. Use methods from NCollection_PackedMapAlgo.hxx instead.

        @deprecated Use NCollection_PackedMapAlgo::IsEqual() instead
        """

    def IsSubset(self, theOther: TColStd_PackedMapOfInteger) -> bool:
        """
        Deprecated in OCCT: This method will be removed after OCCT 7.9 release. Use methods from NCollection_PackedMapAlgo.hxx instead.

        @deprecated Use NCollection_PackedMapAlgo::IsSubset() instead
        """

    def HasIntersection(self, theOther: TColStd_PackedMapOfInteger) -> bool:
        """
        Deprecated in OCCT: This method will be removed after OCCT 7.9 release. Use methods from NCollection_PackedMapAlgo.hxx instead.

        @deprecated Use NCollection_PackedMapAlgo::HasIntersection() instead
        """

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

    @overload
    def __init__(self, theOther: TColStd_HPackedMapOfInteger) -> None: ...

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
import nanoocp.TCollection
TColStd_Array1OfAsciiString = nanoocp.NCollection.NCollection_Array1[nanoocp.TCollection.TCollection_AsciiString]
TColStd_Array1OfBoolean = nanoocp.NCollection.NCollection_Array1[bool]
TColStd_Array1OfByte = nanoocp.NCollection.NCollection_Array1__unsigned_char
TColStd_Array1OfInteger = nanoocp.NCollection.NCollection_Array1[int]
TColStd_Array1OfReal = nanoocp.NCollection.NCollection_Array1[float]
TColStd_Array2OfInteger = nanoocp.NCollection.NCollection_Array2[int]
TColStd_Array2OfReal = nanoocp.NCollection.NCollection_Array2[float]
TColStd_HArray1OfBoolean = nanoocp.NCollection.NCollection_HArray1[bool]
TColStd_HArray1OfByte = nanoocp.NCollection.NCollection_HArray1__unsigned_char
TColStd_HArray1OfInteger = nanoocp.NCollection.NCollection_HArray1[int]
TColStd_HArray1OfReal = nanoocp.NCollection.NCollection_HArray1[float]
TColStd_HArray2OfInteger = nanoocp.NCollection.NCollection_HArray2[int]
TColStd_HArray2OfReal = nanoocp.NCollection.NCollection_HArray2[float]
TColStd_HSequenceOfAsciiString = nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_AsciiString]
TColStd_HSequenceOfHAsciiString = nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]
TColStd_HSequenceOfHExtendedString = nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HExtendedString]
TColStd_HSequenceOfInteger = nanoocp.NCollection.NCollection_HSequence[int]
TColStd_HSequenceOfReal = nanoocp.NCollection.NCollection_HSequence[float]
TColStd_ListOfInteger = nanoocp.NCollection.NCollection_List[int]
TColStd_ListOfReal = nanoocp.NCollection.NCollection_List[float]
TColStd_SequenceOfAsciiString = nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_AsciiString]
TColStd_SequenceOfBoolean = nanoocp.NCollection.NCollection_Sequence[bool]
TColStd_SequenceOfExtendedString = nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_ExtendedString]
TColStd_SequenceOfHAsciiString = nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_HAsciiString]
TColStd_SequenceOfHExtendedString = nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_HExtendedString]
TColStd_SequenceOfInteger = nanoocp.NCollection.NCollection_Sequence[int]
TColStd_SequenceOfReal = nanoocp.NCollection.NCollection_Sequence[float]
TColStd_SequenceOfTransient = nanoocp.NCollection.NCollection_Sequence[nanoocp.Standard.Standard_Transient]
