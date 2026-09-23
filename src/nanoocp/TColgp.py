"""OCCT pre-8.0 typedef names with prefix TColgp (OCCT src/Deprecated/NCollectionAliases)."""
import importlib as _importlib


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TColgp_Array1OfDir": ("nanoocp.NCollection", "NCollection_Array1__gp_Dir"),
    "TColgp_Array1OfPnt": ("nanoocp.NCollection", "NCollection_Array1__gp_Pnt"),
    "TColgp_Array1OfPnt2d": ("nanoocp.NCollection", "NCollection_Array1__gp_Pnt2d"),
    "TColgp_Array1OfVec": ("nanoocp.NCollection", "NCollection_Array1__gp_Vec"),
    "TColgp_Array1OfVec2d": ("nanoocp.NCollection", "NCollection_Array1__gp_Vec2d"),
    "TColgp_Array1OfXY": ("nanoocp.NCollection", "NCollection_Array1__gp_XY"),
    "TColgp_Array1OfXYZ": ("nanoocp.NCollection", "NCollection_Array1__gp_XYZ"),
    "TColgp_Array2OfPnt": ("nanoocp.NCollection", "NCollection_Array2__gp_Pnt"),
    "TColgp_Array2OfPnt2d": ("nanoocp.NCollection", "NCollection_Array2__gp_Pnt2d"),
    "TColgp_Array2OfVec": ("nanoocp.NCollection", "NCollection_Array2__gp_Vec"),
    "TColgp_Array2OfXYZ": ("nanoocp.NCollection", "NCollection_Array2__gp_XYZ"),
    "TColgp_HArray1OfDir": ("nanoocp.NCollection", "NCollection_HArray1__gp_Dir"),
    "TColgp_HArray1OfPnt": ("nanoocp.NCollection", "NCollection_HArray1__gp_Pnt"),
    "TColgp_HArray1OfPnt2d": ("nanoocp.NCollection", "NCollection_HArray1__gp_Pnt2d"),
    "TColgp_HArray1OfVec": ("nanoocp.NCollection", "NCollection_HArray1__gp_Vec"),
    "TColgp_HArray1OfVec2d": ("nanoocp.NCollection", "NCollection_HArray1__gp_Vec2d"),
    "TColgp_HArray1OfXY": ("nanoocp.NCollection", "NCollection_HArray1__gp_XY"),
    "TColgp_HArray1OfXYZ": ("nanoocp.NCollection", "NCollection_HArray1__gp_XYZ"),
    "TColgp_HArray2OfPnt": ("nanoocp.NCollection", "NCollection_HArray2__gp_Pnt"),
    "TColgp_HArray2OfPnt2d": ("nanoocp.NCollection", "NCollection_HArray2__gp_Pnt2d"),
    "TColgp_HArray2OfXYZ": ("nanoocp.NCollection", "NCollection_HArray2__gp_XYZ"),
    "TColgp_HSequenceOfPnt": ("nanoocp.NCollection", "NCollection_HSequence__gp_Pnt"),
    "TColgp_SequenceOfPnt": ("nanoocp.NCollection", "NCollection_Sequence__gp_Pnt"),
    "TColgp_SequenceOfPnt2d": ("nanoocp.NCollection", "NCollection_Sequence__gp_Pnt2d"),
    "TColgp_SequenceOfVec": ("nanoocp.NCollection", "NCollection_Sequence__gp_Vec"),
    "TColgp_SequenceOfXY": ("nanoocp.NCollection", "NCollection_Sequence__gp_XY"),
    "TColgp_SequenceOfXYZ": ("nanoocp.NCollection", "NCollection_Sequence__gp_XYZ"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
