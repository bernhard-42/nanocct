"""OCCT package AdvApp2Var (toolkit TKGeomBase)."""
import importlib as _importlib

from nanoocp._TKGeomBase import AdvApp2Var as _ext
from nanoocp._TKGeomBase.AdvApp2Var import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "AdvApp2Var_SequenceOfNode": ("nanoocp.NCollection", "NCollection_Sequence__Handle_AdvApp2Var_Node"),
    "AdvApp2Var_SequenceOfPatch": ("nanoocp.NCollection", "NCollection_Sequence__Handle_AdvApp2Var_Patch"),
    "AdvApp2Var_SequenceOfStrip": ("nanoocp.NCollection", "NCollection_Sequence__NCollection_Sequence__Handle_AdvApp2Var_Iso"),
    "AdvApp2Var_Strip": ("nanoocp.NCollection", "NCollection_Sequence__Handle_AdvApp2Var_Iso"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
