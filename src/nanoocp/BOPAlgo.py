"""OCCT package BOPAlgo (toolkit TKBO)."""
import importlib as _importlib

from nanoocp._TKBO import BOPAlgo as _ext
from nanoocp._TKBO.BOPAlgo import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "BOPAlgo_ListOfCheckResult": ("nanoocp.NCollection", "NCollection_List__BOPAlgo_CheckResult"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
