"""OCCT package Plate (toolkit TKGeomAlgo)."""
import importlib as _importlib

from nanoocp._TKGeomAlgo import Plate as _ext
from nanoocp._TKGeomAlgo.Plate import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "Plate_Array1OfPinpointConstraint": ("nanoocp.NCollection", "NCollection_Array1__Plate_PinpointConstraint"),
    "Plate_SequenceOfPinpointConstraint": ("nanoocp.NCollection", "NCollection_Sequence__Plate_PinpointConstraint"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
