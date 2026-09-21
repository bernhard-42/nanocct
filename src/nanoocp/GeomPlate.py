"""OCCT package GeomPlate (toolkit TKGeomAlgo)."""
import importlib as _importlib

from nanoocp._TKGeomAlgo import GeomPlate as _ext
from nanoocp._TKGeomAlgo.GeomPlate import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "GeomPlate_Array1OfHCurve": ("nanoocp.NCollection", "NCollection_Array1__Handle_Adaptor3d_Curve"),
    "GeomPlate_HArray1OfHCurve": ("nanoocp.NCollection", "NCollection_HArray1__Handle_Adaptor3d_Curve"),
    "GeomPlate_SequenceOfAij": ("nanoocp.NCollection", "NCollection_Sequence__GeomPlate_Aij"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
