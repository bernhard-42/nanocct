"""OCCT package StepRepr (toolkit TKDESTEP)."""
import importlib as _importlib

from nanoocp._TKDESTEP import StepRepr as _ext
from nanoocp._TKDESTEP.StepRepr import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "StepRepr_Array1OfMaterialPropertyRepresentation": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepRepr_MaterialPropertyRepresentation"),
    "StepRepr_Array1OfPropertyDefinitionRepresentation": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepRepr_PropertyDefinitionRepresentation"),
    "StepRepr_Array1OfRepresentationItem": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepRepr_RepresentationItem"),
    "StepRepr_Array1OfShapeAspect": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepRepr_ShapeAspect"),
    "StepRepr_HArray1OfMaterialPropertyRepresentation": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepRepr_MaterialPropertyRepresentation"),
    "StepRepr_HArray1OfPropertyDefinitionRepresentation": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepRepr_PropertyDefinitionRepresentation"),
    "StepRepr_HArray1OfRepresentationItem": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepRepr_RepresentationItem"),
    "StepRepr_HArray1OfShapeAspect": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepRepr_ShapeAspect"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
