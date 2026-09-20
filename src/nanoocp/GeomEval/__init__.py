"""OCCT package GeomEval (toolkit TKG3d)."""
import importlib as _importlib

from nanoocp._TKG3d import GeomEval as _ext
from nanoocp._TKG3d.GeomEval import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits

# C++ namespaces of the package (Python modules nanoocp.<package>.<namespace>)
import nanoocp.GeomEval.GeomEval_RepCurveDesc  # noqa: E402,F401
import nanoocp.GeomEval.GeomEval_RepSurfaceDesc  # noqa: E402,F401
