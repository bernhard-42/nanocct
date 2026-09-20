"""OCCT package TColStd (toolkit TKernel)"""

from typing import overload

import nanoocp.Standard


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
    def __init__(self, theOther: "NCollection_PackedMap<int>") -> None:
        """
        Constructor from already existing map; performs copying.
        @param theOther the map to copy
        """

    def Map(self) -> "NCollection_PackedMap<int>":
        """Returns const reference to the underlying map."""

    def ChangeMap(self) -> "NCollection_PackedMap<int>":
        """Returns mutable reference to the underlying map."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
TColStd_Array1OfReal = nanoocp.NCollection.NCollection_Array1__double
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
