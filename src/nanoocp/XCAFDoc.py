"""OCCT package XCAFDoc (toolkit TKXCAF)."""
import importlib as _importlib

from nanoocp._TKXCAF import XCAFDoc as _ext
from nanoocp._TKXCAF.XCAFDoc import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "XCAFDoc_DataMapOfShapeLabel": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__TDF_Label__TopTools_ShapeMapHasher"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
