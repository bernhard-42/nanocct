"""OCCT package TColStd (toolkit TKernel)."""
import importlib as _importlib

from nanoocp._TKernel import TColStd as _ext
from nanoocp._TKernel.TColStd import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TColStd_Array1OfAsciiString": ("nanoocp.NCollection", "NCollection_Array1__TCollection_AsciiString"),
    "TColStd_Array1OfBoolean": ("nanoocp.NCollection", "NCollection_Array1__bool"),
    "TColStd_Array1OfByte": ("nanoocp.NCollection", "NCollection_Array1__unsigned_char"),
    "TColStd_Array1OfExtendedString": ("nanoocp.NCollection", "NCollection_Array1__TCollection_ExtendedString"),
    "TColStd_Array1OfInteger": ("nanoocp.NCollection", "NCollection_Array1__int"),
    "TColStd_Array1OfListOfInteger": ("nanoocp.NCollection", "NCollection_Array1__NCollection_List__int"),
    "TColStd_Array1OfReal": ("nanoocp.NCollection", "NCollection_Array1__double"),
    "TColStd_Array1OfTransient": ("nanoocp.NCollection", "NCollection_Array1__Handle_Standard_Transient"),
    "TColStd_Array2OfInteger": ("nanoocp.NCollection", "NCollection_Array2__int"),
    "TColStd_Array2OfReal": ("nanoocp.NCollection", "NCollection_Array2__double"),
    "TColStd_Array2OfTransient": ("nanoocp.NCollection", "NCollection_Array2__Handle_Standard_Transient"),
    "TColStd_HArray1OfAsciiString": ("nanoocp.NCollection", "NCollection_HArray1__TCollection_AsciiString"),
    "TColStd_HArray1OfBoolean": ("nanoocp.NCollection", "NCollection_HArray1__bool"),
    "TColStd_HArray1OfByte": ("nanoocp.NCollection", "NCollection_HArray1__unsigned_char"),
    "TColStd_HArray1OfExtendedString": ("nanoocp.NCollection", "NCollection_HArray1__TCollection_ExtendedString"),
    "TColStd_HArray1OfInteger": ("nanoocp.NCollection", "NCollection_HArray1__int"),
    "TColStd_HArray1OfListOfInteger": ("nanoocp.NCollection", "NCollection_HArray1__NCollection_List__int"),
    "TColStd_HArray1OfReal": ("nanoocp.NCollection", "NCollection_HArray1__double"),
    "TColStd_HArray1OfTransient": ("nanoocp.NCollection", "NCollection_HArray1__Handle_Standard_Transient"),
    "TColStd_HArray2OfInteger": ("nanoocp.NCollection", "NCollection_HArray2__int"),
    "TColStd_HArray2OfReal": ("nanoocp.NCollection", "NCollection_HArray2__double"),
    "TColStd_HArray2OfTransient": ("nanoocp.NCollection", "NCollection_HArray2__Handle_Standard_Transient"),
    "TColStd_HSequenceOfAsciiString": ("nanoocp.NCollection", "NCollection_HSequence__TCollection_AsciiString"),
    "TColStd_HSequenceOfExtendedString": ("nanoocp.NCollection", "NCollection_HSequence__TCollection_ExtendedString"),
    "TColStd_HSequenceOfHAsciiString": ("nanoocp.NCollection", "NCollection_HSequence__Handle_TCollection_HAsciiString"),
    "TColStd_HSequenceOfHExtendedString": ("nanoocp.NCollection", "NCollection_HSequence__Handle_TCollection_HExtendedString"),
    "TColStd_HSequenceOfInteger": ("nanoocp.NCollection", "NCollection_HSequence__int"),
    "TColStd_HSequenceOfReal": ("nanoocp.NCollection", "NCollection_HSequence__double"),
    "TColStd_HSequenceOfTransient": ("nanoocp.NCollection", "NCollection_HSequence__Handle_Standard_Transient"),
    "TColStd_ListOfAsciiString": ("nanoocp.NCollection", "NCollection_List__TCollection_AsciiString"),
    "TColStd_ListOfInteger": ("nanoocp.NCollection", "NCollection_List__int"),
    "TColStd_ListOfReal": ("nanoocp.NCollection", "NCollection_List__double"),
    "TColStd_ListOfTransient": ("nanoocp.NCollection", "NCollection_List__Handle_Standard_Transient"),
    "TColStd_SequenceOfAsciiString": ("nanoocp.NCollection", "NCollection_Sequence__TCollection_AsciiString"),
    "TColStd_SequenceOfBoolean": ("nanoocp.NCollection", "NCollection_Sequence__bool"),
    "TColStd_SequenceOfExtendedString": ("nanoocp.NCollection", "NCollection_Sequence__TCollection_ExtendedString"),
    "TColStd_SequenceOfHAsciiString": ("nanoocp.NCollection", "NCollection_Sequence__Handle_TCollection_HAsciiString"),
    "TColStd_SequenceOfHExtendedString": ("nanoocp.NCollection", "NCollection_Sequence__Handle_TCollection_HExtendedString"),
    "TColStd_SequenceOfInteger": ("nanoocp.NCollection", "NCollection_Sequence__int"),
    "TColStd_SequenceOfReal": ("nanoocp.NCollection", "NCollection_Sequence__double"),
    "TColStd_SequenceOfTransient": ("nanoocp.NCollection", "NCollection_Sequence__Handle_Standard_Transient"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
