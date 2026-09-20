"""OCCT package Poly (toolkit TKMath)."""
import importlib as _importlib

from nanoocp._TKMath import Poly as _ext
from nanoocp._TKMath.Poly import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "Poly_Array1OfTriangle": ("nanoocp.NCollection", "NCollection_Array1__Poly_Triangle"),
    "Poly_HArray1OfTriangle": ("nanoocp.NCollection", "NCollection_HArray1__Poly_Triangle"),
    "Poly_ListOfTriangulation": ("nanoocp.NCollection", "NCollection_List__Handle_Poly_Triangulation"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
