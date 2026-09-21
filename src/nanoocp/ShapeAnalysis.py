"""OCCT package ShapeAnalysis (toolkit TKShHealing)."""
import importlib as _importlib

from nanoocp._TKShHealing import ShapeAnalysis as _ext
from nanoocp._TKShHealing.ShapeAnalysis import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "ShapeAnalysis_DataMapOfShapeListOfReal": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__NCollection_List__double__TopTools_ShapeMapHasher"),
    "ShapeAnalysis_HSequenceOfFreeBounds": ("nanoocp.NCollection", "NCollection_HSequence__Handle_ShapeAnalysis_FreeBoundData"),
    "ShapeAnalysis_SequenceOfFreeBounds": ("nanoocp.NCollection", "NCollection_Sequence__Handle_ShapeAnalysis_FreeBoundData"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
