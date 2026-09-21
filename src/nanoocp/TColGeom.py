"""OCCT pre-8.0 typedef names with prefix TColGeom (OCCT src/Deprecated/NCollectionAliases)."""
import importlib as _importlib


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TColGeom_Array1OfBSplineCurve": ("nanoocp.NCollection", "NCollection_Array1__Handle_Geom_BSplineCurve"),
    "TColGeom_Array1OfBezierCurve": ("nanoocp.NCollection", "NCollection_Array1__Handle_Geom_BezierCurve"),
    "TColGeom_Array1OfCurve": ("nanoocp.NCollection", "NCollection_Array1__Handle_Geom_Curve"),
    "TColGeom_Array1OfSurface": ("nanoocp.NCollection", "NCollection_Array1__Handle_Geom_Surface"),
    "TColGeom_Array2OfBezierSurface": ("nanoocp.NCollection", "NCollection_Array2__Handle_Geom_BezierSurface"),
    "TColGeom_Array2OfSurface": ("nanoocp.NCollection", "NCollection_Array2__Handle_Geom_Surface"),
    "TColGeom_HArray1OfBSplineCurve": ("nanoocp.NCollection", "NCollection_HArray1__Handle_Geom_BSplineCurve"),
    "TColGeom_HArray1OfCurve": ("nanoocp.NCollection", "NCollection_HArray1__Handle_Geom_Curve"),
    "TColGeom_HArray2OfSurface": ("nanoocp.NCollection", "NCollection_HArray2__Handle_Geom_Surface"),
    "TColGeom_HSequenceOfBoundedCurve": ("nanoocp.NCollection", "NCollection_HSequence__Handle_Geom_BoundedCurve"),
    "TColGeom_SequenceOfBoundedCurve": ("nanoocp.NCollection", "NCollection_Sequence__Handle_Geom_BoundedCurve"),
    "TColGeom_SequenceOfCurve": ("nanoocp.NCollection", "NCollection_Sequence__Handle_Geom_Curve"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
