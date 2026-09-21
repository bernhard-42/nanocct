"""OCCT package HLRAlgo (toolkit TKHLR)."""
import importlib as _importlib

from nanoocp._TKHLR import HLRAlgo as _ext
from nanoocp._TKHLR.HLRAlgo import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "HLRAlgo_Array1OfPHDat": ("nanoocp.NCollection", "NCollection_Array1__HLRAlgo_PolyHidingData"),
    "HLRAlgo_Array1OfPINod": ("nanoocp.NCollection", "NCollection_Array1__Handle_HLRAlgo_PolyInternalNode"),
    "HLRAlgo_Array1OfPISeg": ("nanoocp.NCollection", "NCollection_Array1__HLRAlgo_PolyInternalSegment"),
    "HLRAlgo_Array1OfTData": ("nanoocp.NCollection", "NCollection_Array1__HLRAlgo_TriangleData"),
    "HLRAlgo_HArray1OfPHDat": ("nanoocp.NCollection", "NCollection_HArray1__HLRAlgo_PolyHidingData"),
    "HLRAlgo_HArray1OfTData": ("nanoocp.NCollection", "NCollection_HArray1__HLRAlgo_TriangleData"),
    "HLRAlgo_InterferenceList": ("nanoocp.NCollection", "NCollection_List__HLRAlgo_Interference"),
    "HLRAlgo_ListOfBPoint": ("nanoocp.NCollection", "NCollection_List__HLRAlgo_BiPoint"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
