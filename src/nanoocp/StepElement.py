"""OCCT package StepElement (toolkit TKDESTEP)."""
import importlib as _importlib

from nanoocp._TKDESTEP import StepElement as _ext
from nanoocp._TKDESTEP.StepElement import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "StepElement_Array1OfCurveElementEndReleasePacket": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepElement_CurveElementEndReleasePacket"),
    "StepElement_Array1OfCurveElementSectionDefinition": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepElement_CurveElementSectionDefinition"),
    "StepElement_Array1OfHSequenceOfCurveElementPurposeMember": ("nanoocp.NCollection", "NCollection_Array1__opencascade_handle__NCollection_HSequence__Handle_StepElement_CurveElementPurposeMember"),
    "StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember": ("nanoocp.NCollection", "NCollection_Array1__opencascade_handle__NCollection_HSequence__Handle_StepElement_SurfaceElementPurposeMember"),
    "StepElement_Array1OfMeasureOrUnspecifiedValue": ("nanoocp.NCollection", "NCollection_Array1__StepElement_MeasureOrUnspecifiedValue"),
    "StepElement_Array1OfSurfaceSection": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepElement_SurfaceSection"),
    "StepElement_Array1OfVolumeElementPurposeMember": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepElement_VolumeElementPurposeMember"),
    "StepElement_HArray1OfCurveElementEndReleasePacket": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepElement_CurveElementEndReleasePacket"),
    "StepElement_HArray1OfCurveElementSectionDefinition": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepElement_CurveElementSectionDefinition"),
    "StepElement_HArray1OfHSequenceOfCurveElementPurposeMember": ("nanoocp.NCollection", "NCollection_HArray1__opencascade_handle__NCollection_HSequence__Handle_StepElement_CurveElementPurposeMember"),
    "StepElement_HArray1OfHSequenceOfSurfaceElementPurposeMember": ("nanoocp.NCollection", "NCollection_HArray1__opencascade_handle__NCollection_HSequence__Handle_StepElement_SurfaceElementPurposeMember"),
    "StepElement_HArray1OfMeasureOrUnspecifiedValue": ("nanoocp.NCollection", "NCollection_HArray1__StepElement_MeasureOrUnspecifiedValue"),
    "StepElement_HArray1OfSurfaceSection": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepElement_SurfaceSection"),
    "StepElement_HArray1OfVolumeElementPurposeMember": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepElement_VolumeElementPurposeMember"),
    "StepElement_HSequenceOfCurveElementPurposeMember": ("nanoocp.NCollection", "NCollection_HSequence__Handle_StepElement_CurveElementPurposeMember"),
    "StepElement_HSequenceOfCurveElementSectionDefinition": ("nanoocp.NCollection", "NCollection_HSequence__Handle_StepElement_CurveElementSectionDefinition"),
    "StepElement_HSequenceOfElementMaterial": ("nanoocp.NCollection", "NCollection_HSequence__Handle_StepElement_ElementMaterial"),
    "StepElement_HSequenceOfSurfaceElementPurposeMember": ("nanoocp.NCollection", "NCollection_HSequence__Handle_StepElement_SurfaceElementPurposeMember"),
    "StepElement_SequenceOfCurveElementPurposeMember": ("nanoocp.NCollection", "NCollection_Sequence__Handle_StepElement_CurveElementPurposeMember"),
    "StepElement_SequenceOfCurveElementSectionDefinition": ("nanoocp.NCollection", "NCollection_Sequence__Handle_StepElement_CurveElementSectionDefinition"),
    "StepElement_SequenceOfElementMaterial": ("nanoocp.NCollection", "NCollection_Sequence__Handle_StepElement_ElementMaterial"),
    "StepElement_SequenceOfSurfaceElementPurposeMember": ("nanoocp.NCollection", "NCollection_Sequence__Handle_StepElement_SurfaceElementPurposeMember"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
