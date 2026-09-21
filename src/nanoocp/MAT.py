"""OCCT package MAT (toolkit TKTopAlgo)."""
import importlib as _importlib

from nanoocp._TKTopAlgo import MAT as _ext
from nanoocp._TKTopAlgo.MAT import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "MAT_SequenceOfArc": ("nanoocp.NCollection", "NCollection_Sequence__Handle_MAT_Arc"),
    "MAT_SequenceOfBasicElt": ("nanoocp.NCollection", "NCollection_Sequence__Handle_MAT_BasicElt"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
