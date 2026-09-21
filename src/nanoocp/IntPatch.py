"""OCCT package IntPatch (toolkit TKGeomAlgo)."""
import importlib as _importlib

from nanoocp._TKGeomAlgo import IntPatch as _ext
from nanoocp._TKGeomAlgo.IntPatch import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "IntPatch_SequenceOfLine": ("nanoocp.NCollection", "NCollection_Sequence__Handle_IntPatch_Line"),
    "IntPatch_SequenceOfPoint": ("nanoocp.NCollection", "NCollection_Sequence__IntPatch_Point"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
