"""OCCT pre-8.0 typedef names with prefix SelectMgr (OCCT src/Deprecated/NCollectionAliases)."""
import importlib as _importlib


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "SelectMgr_Mat4": ("nanoocp.BVH", "BVH_Mat4d"),
    "SelectMgr_Vec3": ("nanoocp.BVH", "BVH_Vec3d"),
    "SelectMgr_Vec4": ("nanoocp.BVH", "BVH_Vec4d"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
