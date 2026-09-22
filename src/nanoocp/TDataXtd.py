"""OCCT package TDataXtd (toolkit TKCAF)."""
import importlib as _importlib

from nanoocp._TKCAF import TDataXtd as _ext
from nanoocp._TKCAF.TDataXtd import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TDataXtd_Array1OfTrsf": ("nanoocp.NCollection", "NCollection_Array1__gp_Trsf"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
