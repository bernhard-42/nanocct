"""OCCT package XCAFPrs (toolkit TKXCAF)."""
import importlib as _importlib

from nanoocp._TKXCAF import XCAFPrs as _ext
from nanoocp._TKXCAF.XCAFPrs import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "XCAFPrs_IndexedDataMapOfShapeStyle": ("nanoocp.NCollection", "NCollection_IndexedDataMap__TopoDS_Shape__XCAFPrs_Style__TopTools_ShapeMapHasher"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
