"""OCCT package SelectMgr (toolkit TKV3d)."""
import importlib as _importlib

from nanoocp._TKV3d import SelectMgr as _ext
from nanoocp._TKV3d.SelectMgr import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "SelectMgr_ListOfFilter": ("nanoocp.NCollection", "NCollection_List__Handle_SelectMgr_Filter"),
    "SelectMgr_Mat4": ("nanoocp.BVH", "BVH_Mat4d"),
    "SelectMgr_SequenceOfSelection": ("nanoocp.NCollection", "NCollection_Sequence__Handle_SelectMgr_Selection"),
    "SelectMgr_Vec3": ("nanoocp.BVH", "BVH_Vec3d"),
    "SelectMgr_Vec4": ("nanoocp.BVH", "BVH_Vec4d"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
