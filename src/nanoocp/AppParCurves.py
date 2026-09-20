"""OCCT package AppParCurves (toolkit TKGeomBase)."""
import importlib as _importlib

from nanoocp._TKGeomBase import AppParCurves as _ext
from nanoocp._TKGeomBase.AppParCurves import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "AppParCurves_Array1OfConstraintCouple": ("nanoocp.NCollection", "NCollection_Array1__AppParCurves_ConstraintCouple"),
    "AppParCurves_Array1OfMultiPoint": ("nanoocp.NCollection", "NCollection_Array1__AppParCurves_MultiPoint"),
    "AppParCurves_HArray1OfConstraintCouple": ("nanoocp.NCollection", "NCollection_HArray1__AppParCurves_ConstraintCouple"),
    "AppParCurves_SequenceOfMultiCurve": ("nanoocp.NCollection", "NCollection_Sequence__AppParCurves_MultiCurve"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
