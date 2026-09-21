"""OCCT package LocOpe (toolkit TKFeat)."""
import importlib as _importlib

from nanoocp._TKFeat import LocOpe as _ext
from nanoocp._TKFeat.LocOpe import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "LocOpe_SequenceOfCirc": ("nanoocp.NCollection", "NCollection_Sequence__gp_Circ"),
    "LocOpe_SequenceOfLin": ("nanoocp.NCollection", "NCollection_Sequence__gp_Lin"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
