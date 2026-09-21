"""OCCT package IntSurf (toolkit TKGeomAlgo)."""
import importlib as _importlib

from nanoocp._TKGeomAlgo import IntSurf as _ext
from nanoocp._TKGeomAlgo.IntSurf import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "IntSurf_ListOfPntOn2S": ("nanoocp.NCollection", "NCollection_List__IntSurf_PntOn2S"),
    "IntSurf_SequenceOfInteriorPoint": ("nanoocp.NCollection", "NCollection_Sequence__IntSurf_InteriorPoint"),
    "IntSurf_SequenceOfPathPoint": ("nanoocp.NCollection", "NCollection_Sequence__IntSurf_PathPoint"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
