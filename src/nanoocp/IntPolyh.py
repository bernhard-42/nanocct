"""OCCT package IntPolyh (toolkit TKGeomAlgo)."""
import importlib as _importlib

from nanoocp._TKGeomAlgo import IntPolyh as _ext
from nanoocp._TKGeomAlgo.IntPolyh import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "IntPolyh_ListOfCouples": ("nanoocp.NCollection", "NCollection_List__IntPolyh_Couple"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
