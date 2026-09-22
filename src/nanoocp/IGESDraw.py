"""OCCT package IGESDraw (toolkit TKDEIGES)."""
import importlib as _importlib

from nanoocp._TKDEIGES import IGESDraw as _ext
from nanoocp._TKDEIGES.IGESDraw import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "IGESDraw_Array1OfConnectPoint": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESDraw_ConnectPoint"),
    "IGESDraw_Array1OfViewKindEntity": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESData_ViewKindEntity"),
    "IGESDraw_HArray1OfConnectPoint": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESDraw_ConnectPoint"),
    "IGESDraw_HArray1OfViewKindEntity": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESData_ViewKindEntity"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
