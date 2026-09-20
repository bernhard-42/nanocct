"""OCCT package Units (toolkit TKernel)."""
import importlib as _importlib

from nanoocp._TKernel import Units as _ext
from nanoocp._TKernel.Units import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "Units_QtsSequence": ("nanoocp.NCollection", "NCollection_Sequence__Handle_Units_Quantity"),
    "Units_QuantitiesSequence": ("nanoocp.NCollection", "NCollection_HSequence__Handle_Units_Quantity"),
    "Units_TksSequence": ("nanoocp.NCollection", "NCollection_Sequence__Handle_Units_Token"),
    "Units_TokensSequence": ("nanoocp.NCollection", "NCollection_HSequence__Handle_Units_Token"),
    "Units_UnitsSequence": ("nanoocp.NCollection", "NCollection_HSequence__Handle_Units_Unit"),
    "Units_UtsSequence": ("nanoocp.NCollection", "NCollection_Sequence__Handle_Units_Unit"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
