"""OCCT package Extrema (toolkit TKGeomBase)."""
import importlib as _importlib

from nanoocp._TKGeomBase import Extrema as _ext
from nanoocp._TKGeomBase.Extrema import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "Extrema_SequenceOfPOnCurv": ("nanoocp.NCollection", "NCollection_Sequence__Extrema_POnCurv"),
    "Extrema_SequenceOfPOnCurv2d": ("nanoocp.NCollection", "NCollection_Sequence__Extrema_POnCurv2d"),
    "Extrema_SequenceOfPOnSurf": ("nanoocp.NCollection", "NCollection_Sequence__Extrema_POnSurf"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
