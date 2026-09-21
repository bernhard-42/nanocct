"""OCCT package TopTools (toolkit TKBRep)."""
import importlib as _importlib

from nanoocp._TKBRep import TopTools as _ext
from nanoocp._TKBRep.TopTools import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TopTools_Array1OfShape": ("nanoocp.NCollection", "NCollection_Array1__TopoDS_Shape"),
    "TopTools_Array2OfShape": ("nanoocp.NCollection", "NCollection_Array2__TopoDS_Shape"),
    "TopTools_DataMapOfShapeBox": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__Bnd_Box__TopTools_ShapeMapHasher"),
    "TopTools_DataMapOfShapeInteger": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__int__TopTools_ShapeMapHasher"),
    "TopTools_DataMapOfShapeListOfShape": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__NCollection_List__TopoDS_Shape__TopTools_ShapeMapHasher"),
    "TopTools_DataMapOfShapeReal": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__double__TopTools_ShapeMapHasher"),
    "TopTools_DataMapOfShapeShape": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__TopoDS_Shape__TopTools_ShapeMapHasher"),
    "TopTools_HArray1OfShape": ("nanoocp.NCollection", "NCollection_HArray1__TopoDS_Shape"),
    "TopTools_HArray2OfShape": ("nanoocp.NCollection", "NCollection_HArray2__TopoDS_Shape"),
    "TopTools_HSequenceOfShape": ("nanoocp.NCollection", "NCollection_HSequence__TopoDS_Shape"),
    "TopTools_IndexedDataMapOfShapeListOfShape": ("nanoocp.NCollection", "NCollection_IndexedDataMap__TopoDS_Shape__NCollection_List__TopoDS_Shape__TopTools_ShapeMapHasher"),
    "TopTools_IndexedDataMapOfShapeReal": ("nanoocp.NCollection", "NCollection_IndexedDataMap__TopoDS_Shape__double__TopTools_ShapeMapHasher"),
    "TopTools_IndexedDataMapOfShapeShape": ("nanoocp.NCollection", "NCollection_IndexedDataMap__TopoDS_Shape__TopoDS_Shape__TopTools_ShapeMapHasher"),
    "TopTools_IndexedMapOfShape": ("nanoocp.NCollection", "NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher"),
    "TopTools_ListOfListOfShape": ("nanoocp.NCollection", "NCollection_List__NCollection_List__TopoDS_Shape"),
    "TopTools_ListOfShape": ("nanoocp.NCollection", "NCollection_List__TopoDS_Shape"),
    "TopTools_MapOfShape": ("nanoocp.NCollection", "NCollection_Map__TopoDS_Shape__TopTools_ShapeMapHasher"),
    "TopTools_SequenceOfShape": ("nanoocp.NCollection", "NCollection_Sequence__TopoDS_Shape"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
