"""OCCT package StepFEA (toolkit TKDESTEP)."""
import importlib as _importlib

from nanoocp._TKDESTEP import StepFEA as _ext
from nanoocp._TKDESTEP.StepFEA import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "StepFEA_Array1OfCurveElementEndOffset": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepFEA_CurveElementEndOffset"),
    "StepFEA_Array1OfCurveElementEndRelease": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepFEA_CurveElementEndRelease"),
    "StepFEA_Array1OfCurveElementInterval": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepFEA_CurveElementInterval"),
    "StepFEA_Array1OfDegreeOfFreedom": ("nanoocp.NCollection", "NCollection_Array1__StepFEA_DegreeOfFreedom"),
    "StepFEA_Array1OfElementRepresentation": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepFEA_ElementRepresentation"),
    "StepFEA_Array1OfNodeRepresentation": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepFEA_NodeRepresentation"),
    "StepFEA_HArray1OfCurveElementEndOffset": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepFEA_CurveElementEndOffset"),
    "StepFEA_HArray1OfCurveElementEndRelease": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepFEA_CurveElementEndRelease"),
    "StepFEA_HArray1OfCurveElementInterval": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepFEA_CurveElementInterval"),
    "StepFEA_HArray1OfDegreeOfFreedom": ("nanoocp.NCollection", "NCollection_HArray1__StepFEA_DegreeOfFreedom"),
    "StepFEA_HArray1OfElementRepresentation": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepFEA_ElementRepresentation"),
    "StepFEA_HArray1OfNodeRepresentation": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepFEA_NodeRepresentation"),
    "StepFEA_HSequenceOfElementGeometricRelationship": ("nanoocp.NCollection", "NCollection_HSequence__Handle_StepFEA_ElementGeometricRelationship"),
    "StepFEA_HSequenceOfElementRepresentation": ("nanoocp.NCollection", "NCollection_HSequence__Handle_StepFEA_ElementRepresentation"),
    "StepFEA_SequenceOfElementGeometricRelationship": ("nanoocp.NCollection", "NCollection_Sequence__Handle_StepFEA_ElementGeometricRelationship"),
    "StepFEA_SequenceOfElementRepresentation": ("nanoocp.NCollection", "NCollection_Sequence__Handle_StepFEA_ElementRepresentation"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
