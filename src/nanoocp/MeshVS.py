"""OCCT package MeshVS (toolkit TKMeshVS)."""
import importlib as _importlib

from nanoocp._TKMeshVS import MeshVS as _ext
from nanoocp._TKMeshVS.MeshVS import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "MeshVS_Array1OfSequenceOfInteger": ("nanoocp.NCollection", "NCollection_Array1__NCollection_Sequence__int"),
    "MeshVS_HArray1OfSequenceOfInteger": ("nanoocp.NCollection", "NCollection_HArray1__NCollection_Sequence__int"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
