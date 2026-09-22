"""OCCT package Graphic3d (toolkit TKService)."""
import importlib as _importlib

from nanoocp._TKService import Graphic3d as _ext
from nanoocp._TKService.Graphic3d import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "Graphic3d_Mat4": ("nanoocp.BVH", "BVH_Mat4f"),
    "Graphic3d_Mat4d": ("nanoocp.BVH", "BVH_Mat4d"),
    "Graphic3d_SequenceOfGroup": ("nanoocp.NCollection", "NCollection_Sequence__Handle_Graphic3d_Group"),
    "Graphic3d_Vec2": ("nanoocp.BVH", "BVH_Vec2f"),
    "Graphic3d_Vec2d": ("nanoocp.BVH", "BVH_Vec2d"),
    "Graphic3d_Vec2i": ("nanoocp.BVH", "BVH_Vec2i"),
    "Graphic3d_Vec3": ("nanoocp.Quantity", "NCollection_Vec3__float"),
    "Graphic3d_Vec3d": ("nanoocp.BVH", "BVH_Vec3d"),
    "Graphic3d_Vec3i": ("nanoocp.BVH", "BVH_Vec3i"),
    "Graphic3d_Vec4": ("nanoocp.Quantity", "NCollection_Vec4__float"),
    "Graphic3d_Vec4d": ("nanoocp.BVH", "BVH_Vec4d"),
    "Graphic3d_Vec4i": ("nanoocp.BVH", "BVH_Vec4i"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
