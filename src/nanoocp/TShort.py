"""OCCT package TShort (toolkit TKernel)."""
import importlib as _importlib

from nanoocp._TKernel import TShort as _ext
from nanoocp._TKernel.TShort import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TShort_Array1OfShortReal": ("nanoocp.NCollection", "NCollection_Array1__float"),
    "TShort_HArray1OfShortReal": ("nanoocp.NCollection", "NCollection_HArray1__float"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
