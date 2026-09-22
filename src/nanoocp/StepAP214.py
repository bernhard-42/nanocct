"""OCCT package StepAP214 (toolkit TKDESTEP)."""
import importlib as _importlib

from nanoocp._TKDESTEP import StepAP214 as _ext
from nanoocp._TKDESTEP.StepAP214 import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "StepAP214_Array1OfApprovalItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_ApprovalItem"),
    "StepAP214_Array1OfAutoDesignDateAndPersonItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_AutoDesignDateAndPersonItem"),
    "StepAP214_Array1OfAutoDesignDateAndTimeItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_AutoDesignDateAndTimeItem"),
    "StepAP214_Array1OfAutoDesignDatedItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_AutoDesignDatedItem"),
    "StepAP214_Array1OfAutoDesignGeneralOrgItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_AutoDesignGeneralOrgItem"),
    "StepAP214_Array1OfAutoDesignGroupedItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_AutoDesignGroupedItem"),
    "StepAP214_Array1OfAutoDesignPresentedItemSelect": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_AutoDesignPresentedItemSelect"),
    "StepAP214_Array1OfAutoDesignReferencingItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_AutoDesignReferencingItem"),
    "StepAP214_Array1OfDateAndTimeItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_DateAndTimeItem"),
    "StepAP214_Array1OfDateItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_DateItem"),
    "StepAP214_Array1OfDocumentReferenceItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_DocumentReferenceItem"),
    "StepAP214_Array1OfExternalIdentificationItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_ExternalIdentificationItem"),
    "StepAP214_Array1OfGroupItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_GroupItem"),
    "StepAP214_Array1OfOrganizationItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_OrganizationItem"),
    "StepAP214_Array1OfPersonAndOrganizationItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_PersonAndOrganizationItem"),
    "StepAP214_Array1OfPresentedItemSelect": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_PresentedItemSelect"),
    "StepAP214_Array1OfSecurityClassificationItem": ("nanoocp.NCollection", "NCollection_Array1__StepAP214_SecurityClassificationItem"),
    "StepAP214_HArray1OfApprovalItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_ApprovalItem"),
    "StepAP214_HArray1OfAutoDesignDateAndPersonItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_AutoDesignDateAndPersonItem"),
    "StepAP214_HArray1OfAutoDesignDateAndTimeItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_AutoDesignDateAndTimeItem"),
    "StepAP214_HArray1OfAutoDesignDatedItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_AutoDesignDatedItem"),
    "StepAP214_HArray1OfAutoDesignGeneralOrgItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_AutoDesignGeneralOrgItem"),
    "StepAP214_HArray1OfAutoDesignGroupedItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_AutoDesignGroupedItem"),
    "StepAP214_HArray1OfAutoDesignPresentedItemSelect": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_AutoDesignPresentedItemSelect"),
    "StepAP214_HArray1OfAutoDesignReferencingItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_AutoDesignReferencingItem"),
    "StepAP214_HArray1OfDateAndTimeItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_DateAndTimeItem"),
    "StepAP214_HArray1OfDateItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_DateItem"),
    "StepAP214_HArray1OfDocumentReferenceItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_DocumentReferenceItem"),
    "StepAP214_HArray1OfExternalIdentificationItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_ExternalIdentificationItem"),
    "StepAP214_HArray1OfGroupItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_GroupItem"),
    "StepAP214_HArray1OfOrganizationItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_OrganizationItem"),
    "StepAP214_HArray1OfPersonAndOrganizationItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_PersonAndOrganizationItem"),
    "StepAP214_HArray1OfPresentedItemSelect": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_PresentedItemSelect"),
    "StepAP214_HArray1OfSecurityClassificationItem": ("nanoocp.NCollection", "NCollection_HArray1__StepAP214_SecurityClassificationItem"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
