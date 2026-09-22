"""OCCT package IGESDefs (toolkit TKDEIGES)."""
import importlib as _importlib

from nanoocp._TKDEIGES import IGESDefs as _ext
from nanoocp._TKDEIGES.IGESDefs import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "IGESDefs_Array1OfTabularData": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESDefs_TabularData"),
    "IGESDefs_HArray1OfTabularData": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESDefs_TabularData"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
