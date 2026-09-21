"""OCCT pre-8.0 typedef names with prefix TColGeom2d (OCCT src/Deprecated/NCollectionAliases)."""
import importlib as _importlib


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TColGeom2d_Array1OfBSplineCurve": ("nanoocp.NCollection", "NCollection_Array1__Handle_Geom2d_BSplineCurve"),
    "TColGeom2d_Array1OfBezierCurve": ("nanoocp.NCollection", "NCollection_Array1__Handle_Geom2d_BezierCurve"),
    "TColGeom2d_Array1OfCurve": ("nanoocp.NCollection", "NCollection_Array1__Handle_Geom2d_Curve"),
    "TColGeom2d_HArray1OfBSplineCurve": ("nanoocp.NCollection", "NCollection_HArray1__Handle_Geom2d_BSplineCurve"),
    "TColGeom2d_HArray1OfCurve": ("nanoocp.NCollection", "NCollection_HArray1__Handle_Geom2d_Curve"),
    "TColGeom2d_SequenceOfCurve": ("nanoocp.NCollection", "NCollection_Sequence__Handle_Geom2d_Curve"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
