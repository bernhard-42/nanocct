"""OCCT package ShapeExtend (toolkit TKShHealing)."""
import importlib as _importlib

from nanoocp._TKShHealing import ShapeExtend as _ext
from nanoocp._TKShHealing.ShapeExtend import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "ShapeExtend_DataMapOfShapeListOfMsg": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__NCollection_List__Message_Msg__TopTools_ShapeMapHasher"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
