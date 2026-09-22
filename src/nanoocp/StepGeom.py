"""OCCT package StepGeom (toolkit TKDESTEP)."""
import importlib as _importlib

from nanoocp._TKDESTEP import StepGeom as _ext
from nanoocp._TKDESTEP.StepGeom import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "StepGeom_Array1OfCartesianPoint": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepGeom_CartesianPoint"),
    "StepGeom_Array1OfCompositeCurveSegment": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepGeom_CompositeCurveSegment"),
    "StepGeom_Array1OfPcurveOrSurface": ("nanoocp.NCollection", "NCollection_Array1__StepGeom_PcurveOrSurface"),
    "StepGeom_Array1OfSurfaceBoundary": ("nanoocp.NCollection", "NCollection_Array1__StepGeom_SurfaceBoundary"),
    "StepGeom_Array1OfTrimmingSelect": ("nanoocp.NCollection", "NCollection_Array1__StepGeom_TrimmingSelect"),
    "StepGeom_Array2OfCartesianPoint": ("nanoocp.NCollection", "NCollection_Array2__Handle_StepGeom_CartesianPoint"),
    "StepGeom_Array2OfSurfacePatch": ("nanoocp.NCollection", "NCollection_Array2__Handle_StepGeom_SurfacePatch"),
    "StepGeom_HArray1OfCartesianPoint": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepGeom_CartesianPoint"),
    "StepGeom_HArray1OfCompositeCurveSegment": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepGeom_CompositeCurveSegment"),
    "StepGeom_HArray1OfPcurveOrSurface": ("nanoocp.NCollection", "NCollection_HArray1__StepGeom_PcurveOrSurface"),
    "StepGeom_HArray1OfSurfaceBoundary": ("nanoocp.NCollection", "NCollection_HArray1__StepGeom_SurfaceBoundary"),
    "StepGeom_HArray1OfTrimmingSelect": ("nanoocp.NCollection", "NCollection_HArray1__StepGeom_TrimmingSelect"),
    "StepGeom_HArray2OfCartesianPoint": ("nanoocp.NCollection", "NCollection_HArray2__Handle_StepGeom_CartesianPoint"),
    "StepGeom_HArray2OfSurfacePatch": ("nanoocp.NCollection", "NCollection_HArray2__Handle_StepGeom_SurfacePatch"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
