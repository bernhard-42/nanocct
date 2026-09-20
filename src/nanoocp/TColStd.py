"""OCCT package TColStd (toolkit TKernel)."""
import importlib as _importlib

from nanoocp._TKernel import TColStd as _ext
from nanoocp._TKernel.TColStd import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TColStd_Array1OfReal": ("nanoocp.NCollection", "NCollection_Array1__double"),
    "TColStd_Array2OfReal": ("nanoocp.NCollection", "NCollection_Array2__double"),
    "TColStd_HArray2OfReal": ("nanoocp.NCollection", "NCollection_HArray2__double"),
    "TColStd_HSequenceOfAsciiString": ("nanoocp.NCollection", "NCollection_HSequence__TCollection_AsciiString"),
    "TColStd_HSequenceOfHAsciiString": ("nanoocp.NCollection", "NCollection_HSequence__Handle_TCollection_HAsciiString"),
    "TColStd_HSequenceOfHExtendedString": ("nanoocp.NCollection", "NCollection_HSequence__Handle_TCollection_HExtendedString"),
    "TColStd_HSequenceOfInteger": ("nanoocp.NCollection", "NCollection_HSequence__int"),
    "TColStd_ListOfInteger": ("nanoocp.NCollection", "NCollection_List__int"),
    "TColStd_SequenceOfAsciiString": ("nanoocp.NCollection", "NCollection_Sequence__TCollection_AsciiString"),
    "TColStd_SequenceOfExtendedString": ("nanoocp.NCollection", "NCollection_Sequence__TCollection_ExtendedString"),
    "TColStd_SequenceOfHAsciiString": ("nanoocp.NCollection", "NCollection_Sequence__Handle_TCollection_HAsciiString"),
    "TColStd_SequenceOfHExtendedString": ("nanoocp.NCollection", "NCollection_Sequence__Handle_TCollection_HExtendedString"),
    "TColStd_SequenceOfInteger": ("nanoocp.NCollection", "NCollection_Sequence__int"),
    "TColStd_SequenceOfTransient": ("nanoocp.NCollection", "NCollection_Sequence__Handle_Standard_Transient"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
