"""OCCT package IGESDimen (toolkit TKDEIGES)."""
import importlib as _importlib

from nanoocp._TKDEIGES import IGESDimen as _ext
from nanoocp._TKDEIGES.IGESDimen import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "IGESDimen_Array1OfGeneralNote": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESDimen_GeneralNote"),
    "IGESDimen_Array1OfLeaderArrow": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESDimen_LeaderArrow"),
    "IGESDimen_HArray1OfGeneralNote": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESDimen_GeneralNote"),
    "IGESDimen_HArray1OfLeaderArrow": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESDimen_LeaderArrow"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
