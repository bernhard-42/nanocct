"""OCCT package TopTools (toolkit TKBRep)."""
import importlib as _importlib

from nanoocp._TKBRep import TopTools as _ext
from nanoocp._TKBRep.TopTools import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TopTools_DataMapOfShapeListOfShape": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__NCollection_List__TopoDS_Shape__TopTools_ShapeMapHasher"),
    "TopTools_DataMapOfShapeShape": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__TopoDS_Shape__TopTools_ShapeMapHasher"),
    "TopTools_IndexedDataMapOfShapeListOfShape": ("nanoocp.NCollection", "NCollection_IndexedDataMap__TopoDS_Shape__NCollection_List__TopoDS_Shape__TopTools_ShapeMapHasher"),
    "TopTools_IndexedMapOfShape": ("nanoocp.NCollection", "NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher"),
    "TopTools_ListOfShape": ("nanoocp.NCollection", "NCollection_List__TopoDS_Shape"),
    "TopTools_MapOfShape": ("nanoocp.NCollection", "NCollection_Map__TopoDS_Shape__TopTools_ShapeMapHasher"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
