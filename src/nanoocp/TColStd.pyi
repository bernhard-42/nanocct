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
