"""OCCT package Bnd (toolkit TKMath)."""
import importlib as _importlib

from nanoocp._TKMath import Bnd as _ext
from nanoocp._TKMath.Bnd import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "Bnd_Array1OfBox": ("nanoocp.NCollection", "NCollection_Array1__Bnd_Box"),
    "Bnd_HArray1OfBox": ("nanoocp.NCollection", "NCollection_HArray1__Bnd_Box"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
