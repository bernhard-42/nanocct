"""OCCT package IGESGeom (toolkit TKDEIGES)."""
import importlib as _importlib

from nanoocp._TKDEIGES import IGESGeom as _ext
from nanoocp._TKDEIGES.IGESGeom import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "IGESGeom_Array1OfBoundary": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESGeom_Boundary"),
    "IGESGeom_Array1OfCurveOnSurface": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESGeom_CurveOnSurface"),
    "IGESGeom_Array1OfTransformationMatrix": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESGeom_TransformationMatrix"),
    "IGESGeom_HArray1OfBoundary": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESGeom_Boundary"),
    "IGESGeom_HArray1OfCurveOnSurface": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESGeom_CurveOnSurface"),
    "IGESGeom_HArray1OfTransformationMatrix": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESGeom_TransformationMatrix"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
