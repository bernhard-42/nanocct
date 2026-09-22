"""OCCT package StepDimTol (toolkit TKDESTEP)."""
import importlib as _importlib

from nanoocp._TKDESTEP import StepDimTol as _ext
from nanoocp._TKDESTEP.StepDimTol import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "StepDimTol_Array1OfDatumReference": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepDimTol_DatumReference"),
    "StepDimTol_Array1OfDatumReferenceCompartment": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepDimTol_DatumReferenceCompartment"),
    "StepDimTol_Array1OfDatumReferenceElement": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepDimTol_DatumReferenceElement"),
    "StepDimTol_Array1OfDatumReferenceModifier": ("nanoocp.NCollection", "NCollection_Array1__StepDimTol_DatumReferenceModifier"),
    "StepDimTol_Array1OfDatumSystemOrReference": ("nanoocp.NCollection", "NCollection_Array1__StepDimTol_DatumSystemOrReference"),
    "StepDimTol_Array1OfGeometricToleranceModifier": ("nanoocp.NCollection", "NCollection_Array1__StepDimTol_GeometricToleranceModifier"),
    "StepDimTol_Array1OfToleranceZoneTarget": ("nanoocp.NCollection", "NCollection_Array1__StepDimTol_ToleranceZoneTarget"),
    "StepDimTol_HArray1OfDatumReference": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepDimTol_DatumReference"),
    "StepDimTol_HArray1OfDatumReferenceCompartment": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepDimTol_DatumReferenceCompartment"),
    "StepDimTol_HArray1OfDatumReferenceElement": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepDimTol_DatumReferenceElement"),
    "StepDimTol_HArray1OfDatumReferenceModifier": ("nanoocp.NCollection", "NCollection_HArray1__StepDimTol_DatumReferenceModifier"),
    "StepDimTol_HArray1OfDatumSystemOrReference": ("nanoocp.NCollection", "NCollection_HArray1__StepDimTol_DatumSystemOrReference"),
    "StepDimTol_HArray1OfGeometricToleranceModifier": ("nanoocp.NCollection", "NCollection_HArray1__StepDimTol_GeometricToleranceModifier"),
    "StepDimTol_HArray1OfToleranceZoneTarget": ("nanoocp.NCollection", "NCollection_HArray1__StepDimTol_ToleranceZoneTarget"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
