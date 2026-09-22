"""OCCT package StepVisual (toolkit TKDESTEP)."""
import importlib as _importlib

from nanoocp._TKDESTEP import StepVisual as _ext
from nanoocp._TKDESTEP.StepVisual import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "StepVisual_Array1OfAnnotationPlaneElement": ("nanoocp.NCollection", "NCollection_Array1__StepVisual_AnnotationPlaneElement"),
    "StepVisual_Array1OfBoxCharacteristicSelect": ("nanoocp.NCollection", "NCollection_Array1__StepVisual_BoxCharacteristicSelect"),
    "StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect": ("nanoocp.NCollection", "NCollection_Array1__StepVisual_CameraModelD3MultiClippingInterectionSelect"),
    "StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect": ("nanoocp.NCollection", "NCollection_Array1__StepVisual_CameraModelD3MultiClippingUnionSelect"),
    "StepVisual_Array1OfCurveStyleFontPattern": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepVisual_CurveStyleFontPattern"),
    "StepVisual_Array1OfDirectionCountSelect": ("nanoocp.NCollection", "NCollection_Array1__StepVisual_DirectionCountSelect"),
    "StepVisual_Array1OfDraughtingCalloutElement": ("nanoocp.NCollection", "NCollection_Array1__StepVisual_DraughtingCalloutElement"),
    "StepVisual_Array1OfFillStyleSelect": ("nanoocp.NCollection", "NCollection_Array1__StepVisual_FillStyleSelect"),
    "StepVisual_Array1OfInvisibleItem": ("nanoocp.NCollection", "NCollection_Array1__StepVisual_InvisibleItem"),
    "StepVisual_Array1OfLayeredItem": ("nanoocp.NCollection", "NCollection_Array1__StepVisual_LayeredItem"),
    "StepVisual_Array1OfPresentationStyleAssignment": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepVisual_PresentationStyleAssignment"),
    "StepVisual_Array1OfPresentationStyleSelect": ("nanoocp.NCollection", "NCollection_Array1__StepVisual_PresentationStyleSelect"),
    "StepVisual_Array1OfRenderingPropertiesSelect": ("nanoocp.NCollection", "NCollection_Array1__StepVisual_RenderingPropertiesSelect"),
    "StepVisual_Array1OfStyleContextSelect": ("nanoocp.NCollection", "NCollection_Array1__StepVisual_StyleContextSelect"),
    "StepVisual_Array1OfSurfaceStyleElementSelect": ("nanoocp.NCollection", "NCollection_Array1__StepVisual_SurfaceStyleElementSelect"),
    "StepVisual_Array1OfTessellatedEdgeOrVertex": ("nanoocp.NCollection", "NCollection_Array1__StepVisual_TessellatedEdgeOrVertex"),
    "StepVisual_Array1OfTessellatedStructuredItem": ("nanoocp.NCollection", "NCollection_Array1__Handle_StepVisual_TessellatedStructuredItem"),
    "StepVisual_Array1OfTextOrCharacter": ("nanoocp.NCollection", "NCollection_Array1__StepVisual_TextOrCharacter"),
    "StepVisual_HArray1OfAnnotationPlaneElement": ("nanoocp.NCollection", "NCollection_HArray1__StepVisual_AnnotationPlaneElement"),
    "StepVisual_HArray1OfBoxCharacteristicSelect": ("nanoocp.NCollection", "NCollection_HArray1__StepVisual_BoxCharacteristicSelect"),
    "StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect": ("nanoocp.NCollection", "NCollection_HArray1__StepVisual_CameraModelD3MultiClippingInterectionSelect"),
    "StepVisual_HArray1OfCameraModelD3MultiClippingUnionSelect": ("nanoocp.NCollection", "NCollection_HArray1__StepVisual_CameraModelD3MultiClippingUnionSelect"),
    "StepVisual_HArray1OfCurveStyleFontPattern": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepVisual_CurveStyleFontPattern"),
    "StepVisual_HArray1OfDirectionCountSelect": ("nanoocp.NCollection", "NCollection_HArray1__StepVisual_DirectionCountSelect"),
    "StepVisual_HArray1OfDraughtingCalloutElement": ("nanoocp.NCollection", "NCollection_HArray1__StepVisual_DraughtingCalloutElement"),
    "StepVisual_HArray1OfFillStyleSelect": ("nanoocp.NCollection", "NCollection_HArray1__StepVisual_FillStyleSelect"),
    "StepVisual_HArray1OfInvisibleItem": ("nanoocp.NCollection", "NCollection_HArray1__StepVisual_InvisibleItem"),
    "StepVisual_HArray1OfLayeredItem": ("nanoocp.NCollection", "NCollection_HArray1__StepVisual_LayeredItem"),
    "StepVisual_HArray1OfPresentationStyleAssignment": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepVisual_PresentationStyleAssignment"),
    "StepVisual_HArray1OfPresentationStyleSelect": ("nanoocp.NCollection", "NCollection_HArray1__StepVisual_PresentationStyleSelect"),
    "StepVisual_HArray1OfRenderingPropertiesSelect": ("nanoocp.NCollection", "NCollection_HArray1__StepVisual_RenderingPropertiesSelect"),
    "StepVisual_HArray1OfStyleContextSelect": ("nanoocp.NCollection", "NCollection_HArray1__StepVisual_StyleContextSelect"),
    "StepVisual_HArray1OfSurfaceStyleElementSelect": ("nanoocp.NCollection", "NCollection_HArray1__StepVisual_SurfaceStyleElementSelect"),
    "StepVisual_HArray1OfTessellatedEdgeOrVertex": ("nanoocp.NCollection", "NCollection_HArray1__StepVisual_TessellatedEdgeOrVertex"),
    "StepVisual_HArray1OfTessellatedStructuredItem": ("nanoocp.NCollection", "NCollection_HArray1__Handle_StepVisual_TessellatedStructuredItem"),
    "StepVisual_HArray1OfTextOrCharacter": ("nanoocp.NCollection", "NCollection_HArray1__StepVisual_TextOrCharacter"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
