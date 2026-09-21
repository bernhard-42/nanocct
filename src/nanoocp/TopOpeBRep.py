"""OCCT package TopOpeBRep (toolkit TKBool)."""
import importlib as _importlib

from nanoocp._TKBool import TopOpeBRep as _ext
from nanoocp._TKBool.TopOpeBRep import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TopOpeBRep_Array1OfLineInter": ("nanoocp.NCollection", "NCollection_Array1__TopOpeBRep_LineInter"),
    "TopOpeBRep_HArray1OfLineInter": ("nanoocp.NCollection", "NCollection_HArray1__TopOpeBRep_LineInter"),
    "TopOpeBRep_SequenceOfPoint2d": ("nanoocp.NCollection", "NCollection_Sequence__TopOpeBRep_Point2d"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
