"""OCCT package BRepExtrema (toolkit TKTopAlgo)."""
import importlib as _importlib

from nanoocp._TKTopAlgo import BRepExtrema as _ext
from nanoocp._TKTopAlgo.BRepExtrema import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "BRepExtrema_SeqOfSolution": ("nanoocp.NCollection", "NCollection_Sequence__BRepExtrema_SolutionElem"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
