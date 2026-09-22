"""OCCT package AIS (toolkit TKV3d)."""
import importlib as _importlib

from nanoocp._TKV3d import AIS as _ext
from nanoocp._TKV3d.AIS import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "AIS_DataMapOfShapeDrawer": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__Handle_AIS_ColoredDrawer__TopTools_ShapeMapHasher"),
    "AIS_ListOfInteractive": ("nanoocp.NCollection", "NCollection_List__Handle_AIS_InteractiveObject"),
    "AIS_NArray1OfEntityOwner": ("nanoocp.NCollection", "NCollection_Array1__Handle_SelectMgr_EntityOwner"),
    "AIS_NListOfEntityOwner": ("nanoocp.NCollection", "NCollection_List__Handle_SelectMgr_EntityOwner"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
