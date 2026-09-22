"""OCCT package IGESAppli (toolkit TKDEIGES)."""
import importlib as _importlib

from nanoocp._TKDEIGES import IGESAppli as _ext
from nanoocp._TKDEIGES.IGESAppli import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "IGESAppli_Array1OfFiniteElement": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESAppli_FiniteElement"),
    "IGESAppli_Array1OfNode": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESAppli_Node"),
    "IGESAppli_HArray1OfFiniteElement": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESAppli_FiniteElement"),
    "IGESAppli_HArray1OfNode": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESAppli_Node"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
