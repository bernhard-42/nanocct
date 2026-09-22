"""OCCT package StepAP203 (toolkit TKDESTEP)."""
import importlib as _importlib

from nanoocp._TKDESTEP import StepAP203 as _ext
from nanoocp._TKDESTEP.StepAP203 import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "StepAP203_Array1OfApprovedItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP203_ApprovedItem"),
    "StepAP203_Array1OfCertifiedItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP203_CertifiedItem"),
    "StepAP203_Array1OfChangeRequestItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP203_ChangeRequestItem"),
    "StepAP203_Array1OfClassifiedItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP203_ClassifiedItem"),
    "StepAP203_Array1OfContractedItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP203_ContractedItem"),
    "StepAP203_Array1OfDateTimeItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP203_DateTimeItem"),
    "StepAP203_Array1OfPersonOrganizationItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP203_PersonOrganizationItem"),
    "StepAP203_Array1OfSpecifiedItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP203_SpecifiedItem"),
    "StepAP203_Array1OfStartRequestItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP203_StartRequestItem"),
    "StepAP203_Array1OfWorkItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP203_WorkItem"),
    "StepAP203_HArray1OfApprovedItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP203_ApprovedItem"),
    "StepAP203_HArray1OfCertifiedItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP203_CertifiedItem"),
    "StepAP203_HArray1OfChangeRequestItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP203_ChangeRequestItem"),
    "StepAP203_HArray1OfClassifiedItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP203_ClassifiedItem"),
    "StepAP203_HArray1OfContractedItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP203_ContractedItem"),
    "StepAP203_HArray1OfDateTimeItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP203_DateTimeItem"),
    "StepAP203_HArray1OfPersonOrganizationItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP203_PersonOrganizationItem"),
    "StepAP203_HArray1OfSpecifiedItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP203_SpecifiedItem"),
    "StepAP203_HArray1OfStartRequestItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP203_StartRequestItem"),
    "StepAP203_HArray1OfWorkItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP203_WorkItem"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
