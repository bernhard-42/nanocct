"""OCCT package BRep (toolkit TKBRep)."""
import importlib as _importlib

from nanoocp._TKBRep import BRep as _ext
from nanoocp._TKBRep.BRep import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "BRep_ListOfCurveRepresentation": ("nanoocp.NCollection", "NCollection_List__Handle_BRep_CurveRepresentation"),
    "BRep_ListOfPointRepresentation": ("nanoocp.NCollection", "NCollection_List__Handle_BRep_PointRepresentation"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
