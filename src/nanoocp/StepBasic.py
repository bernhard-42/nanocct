"""OCCT package StepBasic (toolkit TKDESTEP)."""
import importlib as _importlib

from nanoocp._TKDESTEP import StepBasic as _ext
from nanoocp._TKDESTEP.StepBasic import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "StepBasic_Array1OfApproval": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepBasic_Approval"),
    "StepBasic_Array1OfDerivedUnitElement": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepBasic_DerivedUnitElement"),
    "StepBasic_Array1OfDocument": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepBasic_Document"),
    "StepBasic_Array1OfNamedUnit": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepBasic_NamedUnit"),
    "StepBasic_Array1OfOrganization": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepBasic_Organization"),
    "StepBasic_Array1OfPerson": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepBasic_Person"),
    "StepBasic_Array1OfProduct": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepBasic_Product"),
    "StepBasic_Array1OfProductContext": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepBasic_ProductContext"),
    "StepBasic_Array1OfUncertaintyMeasureWithUnit": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepBasic_UncertaintyMeasureWithUnit"),
    "StepBasic_HArray1OfApproval": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepBasic_Approval"),
    "StepBasic_HArray1OfDerivedUnitElement": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepBasic_DerivedUnitElement"),
    "StepBasic_HArray1OfDocument": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepBasic_Document"),
    "StepBasic_HArray1OfNamedUnit": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepBasic_NamedUnit"),
    "StepBasic_HArray1OfOrganization": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepBasic_Organization"),
    "StepBasic_HArray1OfPerson": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepBasic_Person"),
    "StepBasic_HArray1OfProduct": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepBasic_Product"),
    "StepBasic_HArray1OfProductContext": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepBasic_ProductContext"),
    "StepBasic_HArray1OfUncertaintyMeasureWithUnit": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepBasic_UncertaintyMeasureWithUnit"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
