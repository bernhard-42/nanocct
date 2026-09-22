"""OCCT package gp (toolkit TKMath)."""
import importlib as _importlib

from nanoocp._TKMath import gp as _ext
from nanoocp._TKMath.gp import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "gp_Vec2f": ("nanoocp.BVH", "BVH_Vec2f"),
    "gp_Vec3f": ("nanoocp.Quantity", "NCollection_Vec3__float"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
