"""OCCT package Aspect (toolkit TKService)."""
import importlib as _importlib

from nanoocp._TKService import Aspect as _ext
from nanoocp._TKService.Aspect import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "Aspect_TouchMap": ("nanoocp.NCollection", "NCollection_IndexedDataMap__unsigned_long__Aspect_Touch"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
