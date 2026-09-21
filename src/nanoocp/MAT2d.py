"""OCCT package MAT2d (toolkit TKTopAlgo)."""
import importlib as _importlib

from nanoocp._TKTopAlgo import MAT2d as _ext
from nanoocp._TKTopAlgo.MAT2d import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "MAT2d_SequenceOfConnexion": ("nanoocp.NCollection", "NCollection_Sequence__Handle_MAT2d_Connexion"),
    "MAT2d_SequenceOfSequenceOfGeometry": ("nanoocp.NCollection", "NCollection_Sequence__NCollection_Sequence__Handle_Geom2d_Geometry"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
