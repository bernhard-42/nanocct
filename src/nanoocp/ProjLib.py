"""OCCT package ProjLib (toolkit TKGeomBase)."""
import importlib as _importlib

from nanoocp._TKGeomBase import ProjLib as _ext
from nanoocp._TKGeomBase.ProjLib import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "ProjLib_HSequenceOfHSequenceOfPnt": ("nanoocp.NCollection", "NCollection_HSequence__opencascade_handle__NCollection_HSequence__gp_Pnt"),
    "ProjLib_SequenceOfHSequenceOfPnt": ("nanoocp.NCollection", "NCollection_Sequence__opencascade_handle__NCollection_HSequence__gp_Pnt"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
