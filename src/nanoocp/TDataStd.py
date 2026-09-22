"""OCCT package TDataStd (toolkit TKLCAF)."""
import importlib as _importlib

from nanoocp._TKLCAF import TDataStd as _ext
from nanoocp._TKLCAF.TDataStd import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TDataStd_HLabelArray1": ("nanoocp.NCollection", "NCollection_HArray1__TDF_Label"),
    "TDataStd_LabelArray1": ("nanoocp.NCollection", "NCollection_Array1__TDF_Label"),
    "TDataStd_ListOfByte": ("nanoocp.NCollection", "NCollection_List__unsigned_char"),
    "TDataStd_ListOfExtendedString": ("nanoocp.NCollection", "NCollection_List__TCollection_ExtendedString"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
