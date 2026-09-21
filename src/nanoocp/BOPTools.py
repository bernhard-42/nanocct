"""OCCT package BOPTools (toolkit TKBO)."""
import importlib as _importlib

from nanoocp._TKBO import BOPTools as _ext
from nanoocp._TKBO.BOPTools import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "BOPTools_ListOfConnexityBlock": ("nanoocp.NCollection", "NCollection_List__BOPTools_ConnexityBlock"),
    "BOPTools_ListOfCoupleOfShape": ("nanoocp.NCollection", "NCollection_List__BOPTools_CoupleOfShape"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
