"""OCCT package BRepFill (toolkit TKBool)."""
import importlib as _importlib

from nanoocp._TKBool import BRepFill as _ext
from nanoocp._TKBool.BRepFill import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "BRepFill_DataMapOfShapeHArray2OfShape": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__opencascade_handle__NCollection_HArray2__TopoDS_Shape__TopTools_ShapeMapHasher"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
