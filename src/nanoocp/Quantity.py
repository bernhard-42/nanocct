"""OCCT package Quantity (toolkit TKernel)."""
import importlib as _importlib

from nanoocp._TKernel import Quantity as _ext
from nanoocp._TKernel.Quantity import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "Quantity_Array1OfColor": ("nanoocp.NCollection", "NCollection_Array1__Quantity_Color"),
    "Quantity_HArray1OfColor": ("nanoocp.NCollection", "NCollection_HArray1__Quantity_Color"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
