"""OCCT package V3d (toolkit TKV3d)."""
import importlib as _importlib

from nanoocp._TKV3d import V3d as _ext
from nanoocp._TKV3d.V3d import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "V3d_ListOfLight": ("nanoocp.NCollection", "NCollection_List__Handle_Graphic3d_CLight"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
