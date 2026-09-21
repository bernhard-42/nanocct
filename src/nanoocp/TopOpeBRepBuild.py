"""OCCT package TopOpeBRepBuild (toolkit TKBool)."""
import importlib as _importlib

from nanoocp._TKBool import TopOpeBRepBuild as _ext
from nanoocp._TKBool.TopOpeBRepBuild import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TopOpeBRepBuild_IndexedDataMapOfShapeVertexInfo": ("nanoocp.NCollection", "NCollection_IndexedDataMap__TopoDS_Shape__TopOpeBRepBuild_VertexInfo__TopTools_ShapeMapHasher"),
    "TopOpeBRepBuild_ListOfLoop": ("nanoocp.NCollection", "NCollection_List__Handle_TopOpeBRepBuild_Loop"),
    "TopOpeBRepBuild_ListOfPave": ("nanoocp.NCollection", "NCollection_List__Handle_TopOpeBRepBuild_Pave"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
