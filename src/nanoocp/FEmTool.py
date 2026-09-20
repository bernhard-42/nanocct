"""OCCT package FEmTool (toolkit TKGeomBase)."""
import importlib as _importlib

from nanoocp._TKGeomBase import FEmTool as _ext
from nanoocp._TKGeomBase.FEmTool import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "FEmTool_AssemblyTable": ("nanoocp.NCollection", "NCollection_Array2__opencascade_handle__NCollection_HArray1__int"),
    "FEmTool_HAssemblyTable": ("nanoocp.NCollection", "NCollection_HArray2__opencascade_handle__NCollection_HArray1__int"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
