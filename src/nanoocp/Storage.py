"""OCCT package Storage (toolkit TKernel)."""
import importlib as _importlib

from nanoocp._TKernel import Storage as _ext
from nanoocp._TKernel.Storage import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "Storage_HPArray": ("nanoocp.NCollection", "NCollection_HArray1__Handle_Standard_Persistent"),
    "Storage_PArray": ("nanoocp.NCollection", "NCollection_Array1__Handle_Standard_Persistent"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
