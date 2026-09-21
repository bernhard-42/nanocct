"""OCCT package HLRBRep (toolkit TKHLR)."""
import importlib as _importlib

from nanoocp._TKHLR import HLRBRep as _ext
from nanoocp._TKHLR.HLRBRep import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "HLRBRep_Array1OfEData": ("nanoocp.NCollection", "NCollection_Array1__HLRBRep_EdgeData"),
    "HLRBRep_Array1OfFData": ("nanoocp.NCollection", "NCollection_Array1__HLRBRep_FaceData"),
    "HLRBRep_SeqOfShapeBounds": ("nanoocp.NCollection", "NCollection_Sequence__HLRBRep_ShapeBounds"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
