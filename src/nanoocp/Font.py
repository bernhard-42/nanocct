"""OCCT package Font (toolkit TKService)."""
import importlib as _importlib

from nanoocp._TKService import Font as _ext
from nanoocp._TKService.Font import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "Font_NListOfSystemFont": ("nanoocp.NCollection", "NCollection_List__Handle_Font_SystemFont"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
