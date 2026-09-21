"""OCCT package TopOpeBRepDS (toolkit TKBool)."""
import importlib as _importlib

from nanoocp._TKBool import TopOpeBRepDS as _ext
from nanoocp._TKBool.TopOpeBRepDS import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference": ("nanoocp.NCollection", "NCollection_Array1__int"),
    "TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__TopOpeBRepDS_ListOfShapeOn1State__TopTools_ShapeMapHasher"),
    "TopOpeBRepDS_DataMapOfShapeState": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__TopAbs_State__TopTools_ShapeMapHasher"),
    "TopOpeBRepDS_HArray1OfDataMapOfIntegerListOfInterference": ("nanoocp.NCollection", "NCollection_HArray1__int"),
    "TopOpeBRepDS_IndexedDataMapOfShapeWithState": ("nanoocp.NCollection", "NCollection_IndexedDataMap__TopoDS_Shape__TopOpeBRepDS_ShapeWithState__TopTools_ShapeMapHasher"),
    "TopOpeBRepDS_ListOfInterference": ("nanoocp.NCollection", "NCollection_List__Handle_TopOpeBRepDS_Interference"),
    "TopOpeBRepDS_MapOfShapeData": ("nanoocp.NCollection", "NCollection_IndexedDataMap__TopoDS_Shape__TopOpeBRepDS_ShapeData__TopTools_ShapeMapHasher"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
