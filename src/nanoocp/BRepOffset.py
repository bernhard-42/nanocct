"""OCCT package BRepOffset (toolkit TKOffset)."""
import importlib as _importlib

from nanoocp._TKOffset import BRepOffset as _ext
from nanoocp._TKOffset.BRepOffset import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "BRepOffset_DataMapOfShapeOffset": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__BRepOffset_Offset__TopTools_ShapeMapHasher"),
    "BRepOffset_ListOfInterval": ("nanoocp.NCollection", "NCollection_List__BRepOffset_Interval"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
