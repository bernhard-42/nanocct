"""OCCT package StepShape (toolkit TKDESTEP)."""
import importlib as _importlib

from nanoocp._TKDESTEP import StepShape as _ext
from nanoocp._TKDESTEP.StepShape import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "StepShape_Array1OfConnectedEdgeSet": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepShape_ConnectedEdgeSet"),
    "StepShape_Array1OfConnectedFaceSet": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepShape_ConnectedFaceSet"),
    "StepShape_Array1OfEdge": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepShape_Edge"),
    "StepShape_Array1OfFace": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepShape_Face"),
    "StepShape_Array1OfFaceBound": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepShape_FaceBound"),
    "StepShape_Array1OfGeometricSetSelect": ("nanoocp.NCollection", "NCollection_Array1__StepShape_GeometricSetSelect"),
    "StepShape_Array1OfOrientedClosedShell": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepShape_OrientedClosedShell"),
    "StepShape_Array1OfOrientedEdge": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepShape_OrientedEdge"),
    "StepShape_Array1OfShapeDimensionRepresentationItem": ("nanoocp.NCollection", "NCollection_Array1__StepShape_ShapeDimensionRepresentationItem"),
    "StepShape_Array1OfShell": ("nanoocp.NCollection", "NCollection_Array1__StepShape_Shell"),
    "StepShape_Array1OfValueQualifier": ("nanoocp.NCollection", "NCollection_Array1__StepShape_ValueQualifier"),
    "StepShape_HArray1OfConnectedEdgeSet": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepShape_ConnectedEdgeSet"),
    "StepShape_HArray1OfConnectedFaceSet": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepShape_ConnectedFaceSet"),
    "StepShape_HArray1OfEdge": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepShape_Edge"),
    "StepShape_HArray1OfFace": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepShape_Face"),
    "StepShape_HArray1OfFaceBound": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepShape_FaceBound"),
    "StepShape_HArray1OfGeometricSetSelect": ("nanoocp.NCollection", "NCollection_HArray1__StepShape_GeometricSetSelect"),
    "StepShape_HArray1OfOrientedClosedShell": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepShape_OrientedClosedShell"),
    "StepShape_HArray1OfOrientedEdge": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepShape_OrientedEdge"),
    "StepShape_HArray1OfShapeDimensionRepresentationItem": ("nanoocp.NCollection", "NCollection_HArray1__StepShape_ShapeDimensionRepresentationItem"),
    "StepShape_HArray1OfShell": ("nanoocp.NCollection", "NCollection_HArray1__StepShape_Shell"),
    "StepShape_HArray1OfValueQualifier": ("nanoocp.NCollection", "NCollection_HArray1__StepShape_ValueQualifier"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
