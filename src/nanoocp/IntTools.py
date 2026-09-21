"""OCCT package IntTools (toolkit TKBO)."""
import importlib as _importlib

from nanoocp._TKBO import IntTools as _ext
from nanoocp._TKBO.IntTools import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "IntTools_ListOfCurveRangeSample": ("nanoocp.NCollection", "NCollection_List__IntTools_CurveRangeSample"),
    "IntTools_ListOfSurfaceRangeSample": ("nanoocp.NCollection", "NCollection_List__IntTools_SurfaceRangeSample"),
    "IntTools_SequenceOfCommonPrts": ("nanoocp.NCollection", "NCollection_Sequence__IntTools_CommonPrt"),
    "IntTools_SequenceOfCurves": ("nanoocp.NCollection", "NCollection_Sequence__IntTools_Curve"),
    "IntTools_SequenceOfPntOn2Faces": ("nanoocp.NCollection", "NCollection_Sequence__IntTools_PntOn2Faces"),
    "IntTools_SequenceOfRanges": ("nanoocp.NCollection", "NCollection_Sequence__IntTools_Range"),
    "IntTools_SequenceOfRoots": ("nanoocp.NCollection", "NCollection_Sequence__IntTools_Root"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
