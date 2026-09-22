"""OCCT package IFSelect (toolkit TKXSBase)."""
import importlib as _importlib

from nanoocp._TKXSBase import IFSelect as _ext
from nanoocp._TKXSBase.IFSelect import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "IFSelect_TSeqOfSelection": ("nanoocp.NCollection", "NCollection_Sequence__Handle_IFSelect_Selection"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
