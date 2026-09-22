"""OCCT package MoniTool (toolkit TKXSBase)."""
import importlib as _importlib

from nanoocp._TKXSBase import MoniTool as _ext
from nanoocp._TKXSBase.MoniTool import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "MoniTool_DataMapOfShapeTransient": ("nanoocp.NCollection", "NCollection_DataMap__TopoDS_Shape__Handle_Standard_Transient__TopTools_ShapeMapHasher"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
