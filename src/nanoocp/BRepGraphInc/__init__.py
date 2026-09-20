"""OCCT package BRepGraphInc (toolkit TKBRep)."""
import importlib as _importlib

from nanoocp._TKBRep import BRepGraphInc as _ext
from nanoocp._TKBRep.BRepGraphInc import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits

# C++ namespaces of the package (Python modules nanoocp.<package>.<namespace>)
import nanoocp.BRepGraphInc.BRepGraphInc_Load  # noqa: E402,F401
