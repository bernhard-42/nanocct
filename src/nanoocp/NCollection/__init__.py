"""OCCT package NCollection (toolkit TKernel)."""
import importlib as _importlib

from nanoocp._TKernel import NCollection as _ext
from nanoocp._TKernel.NCollection import *  # noqa: F401,F403


# NCollection_Xxx[T] -> bound class (Design.md 6a); tables generated from manifest.json
from nanoocp._templates import Template as _Template

NCollection_Array1 = _Template("NCollection_Array1", "nanoocp.NCollection", {
    (('nanoocp.AppDef', 'AppDef_MultiPointConstraint'),): "NCollection_Array1__AppDef_MultiPointConstraint",
    (('nanoocp.AppParCurves', 'AppParCurves_ConstraintCouple'),): "NCollection_Array1__AppParCurves_ConstraintCouple",
    (('nanoocp.AppParCurves', 'AppParCurves_MultiPoint'),): "NCollection_Array1__AppParCurves_MultiPoint",
    (('nanoocp.BRepGraphInc', 'ParityOrientation'),): "NCollection_Array1__BRepGraphInc_ParityOrientation",
    (('nanoocp.BRepGraph', 'BRepGraph_ItemUID'),): "NCollection_Array1__BRepGraph_ItemUID",
    (('nanoocp.BRepGraph', 'BRepGraph_NodeId'),): "NCollection_Array1__BRepGraph_NodeId",
    (('nanoocp.BRepGraph', 'BRepGraph_CoEdgeId'),): "NCollection_Array1__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_CoEdge",
    (('nanoocp.BRepGraph', 'BRepGraph_FaceId'),): "NCollection_Array1__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Face",
    (('nanoocp.BRepGraph', 'BRepGraph_ProductId'),): "NCollection_Array1__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Product",
    (('nanoocp.BRepGraph', 'BRepGraph_ShellId'),): "NCollection_Array1__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Shell",
    (('nanoocp.BRepGraph', 'BRepGraph_SolidId'),): "NCollection_Array1__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Solid",
    (('nanoocp.BRepGraph', 'BRepGraph_WireId'),): "NCollection_Array1__BRepGraph_NodeId_Typed__BRepGraph_NodeId_Kind_Wire",
    (('nanoocp.BRepGraph', 'BRepGraph_RefId'),): "NCollection_Array1__BRepGraph_RefId",
    (('nanoocp.BRepGraph', 'BRepGraph_ChildRefId'),): "NCollection_Array1__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Child",
    (('nanoocp.BRepGraph', 'BRepGraph_FaceRefId'),): "NCollection_Array1__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Face",
    (('nanoocp.BRepGraph', 'BRepGraph_OccurrenceRefId'),): "NCollection_Array1__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Occurrence",
    (('nanoocp.BRepGraph', 'BRepGraph_ShellRefId'),): "NCollection_Array1__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Shell",
    (('nanoocp.BRepGraph', 'BRepGraph_SolidRefId'),): "NCollection_Array1__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Solid",
    (('nanoocp.BRepGraph', 'BRepGraph_WireRefId'),): "NCollection_Array1__BRepGraph_RefId_Typed__BRepGraph_RefId_Kind_Wire",
    (('nanoocp.BRepGraph', 'BRepGraph_UID'),): "NCollection_Array1__BRepGraph_UID",
    (('nanoocp.Bnd', 'Bnd_Box'),): "NCollection_Array1__Bnd_Box",
    (('nanoocp.Geom2dGridEval', 'CurveD1'),): "NCollection_Array1__Geom2dGridEval_CurveD1",
    (('nanoocp.Geom2dGridEval', 'CurveD2'),): "NCollection_Array1__Geom2dGridEval_CurveD2",
    (('nanoocp.Geom2dGridEval', 'CurveD3'),): "NCollection_Array1__Geom2dGridEval_CurveD3",
    (('nanoocp.Geom', 'Geom_Curve.ResD1'),): "NCollection_Array1__Geom_Curve_ResD1",
    (('nanoocp.Geom', 'Geom_Curve.ResD2'),): "NCollection_Array1__Geom_Curve_ResD2",
    (('nanoocp.Geom', 'Geom_Curve.ResD3'),): "NCollection_Array1__Geom_Curve_ResD3",
    (('nanoocp.Geom', 'Geom_Surface.ResD1'),): "NCollection_Array1__Geom_Surface_ResD1",
    (('nanoocp.Geom', 'Geom_Surface.ResD2'),): "NCollection_Array1__Geom_Surface_ResD2",
    (('nanoocp.Geom', 'Geom_Surface.ResD3'),): "NCollection_Array1__Geom_Surface_ResD3",
    (('nanoocp.Geom2d', 'Geom2d_BSplineCurve'),): "NCollection_Array1__Handle_Geom2d_BSplineCurve",
    (('nanoocp.Geom2d', 'Geom2d_BezierCurve'),): "NCollection_Array1__Handle_Geom2d_BezierCurve",
    (('nanoocp.Geom', 'Geom_BSplineCurve'),): "NCollection_Array1__Handle_Geom_BSplineCurve",
    (('nanoocp.Geom', 'Geom_BezierCurve'),): "NCollection_Array1__Handle_Geom_BezierCurve",
    (('nanoocp.Geom', 'Geom_BezierSurface'),): "NCollection_Array1__Handle_Geom_BezierSurface",
    (('nanoocp.Standard', 'Standard_Persistent'),): "NCollection_Array1__Handle_Standard_Persistent",
    (('nanoocp.BVH', 'BVH_Vec3f'),): "NCollection_Array1__NCollection_Vec3__float",
    (('nanoocp.Poly', 'Poly_Triangle'),): "NCollection_Array1__Poly_Triangle",
    (('nanoocp.TopLoc', 'TopLoc_Location'),): "NCollection_Array1__TopLoc_Location",
    (('builtins', 'float'),): "NCollection_Array1__double",
    (('nanoocp.gp', 'gp_Pnt'),): "NCollection_Array1__gp_Pnt",
    (('nanoocp.gp', 'gp_Pnt2d'),): "NCollection_Array1__gp_Pnt2d",
    (('nanoocp.gp', 'gp_Vec'),): "NCollection_Array1__gp_Vec",
    (('nanoocp.gp', 'gp_Vec2d'),): "NCollection_Array1__gp_Vec2d",
    (('nanoocp.gp', 'gp_XYZ'),): "NCollection_Array1__gp_XYZ",
    (('builtins', 'int'),): "NCollection_Array1__int",
    (('nanoocp.NCollection', 'NCollection_HArray1__int'),): "NCollection_Array1__opencascade_handle__NCollection_HArray1__int",
})
NCollection_Array2 = _Template("NCollection_Array2", "nanoocp.NCollection", {
    (('nanoocp.Geom', 'Geom_Surface.ResD1'),): "NCollection_Array2__Geom_Surface_ResD1",
    (('nanoocp.Geom', 'Geom_Surface.ResD2'),): "NCollection_Array2__Geom_Surface_ResD2",
    (('nanoocp.Geom', 'Geom_Surface.ResD3'),): "NCollection_Array2__Geom_Surface_ResD3",
    (('nanoocp.Geom', 'Geom_BezierSurface'),): "NCollection_Array2__Handle_Geom_BezierSurface",
    (('builtins', 'float'),): "NCollection_Array2__double",
    (('nanoocp.gp', 'gp_Pnt'),): "NCollection_Array2__gp_Pnt",
    (('nanoocp.gp', 'gp_Pnt2d'),): "NCollection_Array2__gp_Pnt2d",
    (('nanoocp.gp', 'gp_Vec'),): "NCollection_Array2__gp_Vec",
    (('builtins', 'int'),): "NCollection_Array2__int",
    (('nanoocp.NCollection', 'NCollection_HArray1__int'),): "NCollection_Array2__opencascade_handle__NCollection_HArray1__int",
})
NCollection_DataMap = _Template("NCollection_DataMap", "nanoocp.NCollection", {
    (('nanoocp.TCollection', 'TCollection_AsciiString'), ('nanoocp.TCollection', 'TCollection_AsciiString')): "NCollection_DataMap__TCollection_AsciiString__TCollection_AsciiString",
    (('nanoocp.TCollection', 'TCollection_AsciiString'), ('builtins', 'int')): "NCollection_DataMap__TCollection_AsciiString__int",
    (('nanoocp.TopoDS', 'TopoDS_Shape'), ('nanoocp.BRepGraph', 'BRepGraph_NodeId'), ('nanoocp.TopTools', 'TopTools_ShapeMapHasher')): "NCollection_DataMap__TopoDS_Shape__BRepGraph_NodeId__TopTools_ShapeMapHasher",
    (('builtins', 'int'), ('builtins', 'float')): "NCollection_DataMap__int__double",
})
NCollection_DoubleMap = _Template("NCollection_DoubleMap", "nanoocp.NCollection", {
    (('builtins', 'int'), ('nanoocp.TCollection', 'TCollection_AsciiString')): "NCollection_DoubleMap__int__TCollection_AsciiString",
})
NCollection_DynamicArray = _Template("NCollection_DynamicArray", "nanoocp.NCollection", {
    (('nanoocp.gp', 'gp_Pnt2d'),): "NCollection_DynamicArray__gp_Pnt2d",
    (('builtins', 'int'),): "NCollection_DynamicArray__int",
})
NCollection_HArray1 = _Template("NCollection_HArray1", "nanoocp.NCollection", {
    (('nanoocp.AppParCurves', 'AppParCurves_ConstraintCouple'),): "NCollection_HArray1__AppParCurves_ConstraintCouple",
    (('nanoocp.Bnd', 'Bnd_Box'),): "NCollection_HArray1__Bnd_Box",
    (('nanoocp.Geom2d', 'Geom2d_BSplineCurve'),): "NCollection_HArray1__Handle_Geom2d_BSplineCurve",
    (('nanoocp.Geom', 'Geom_BSplineCurve'),): "NCollection_HArray1__Handle_Geom_BSplineCurve",
    (('nanoocp.Standard', 'Standard_Persistent'),): "NCollection_HArray1__Handle_Standard_Persistent",
    (('nanoocp.Poly', 'Poly_Triangle'),): "NCollection_HArray1__Poly_Triangle",
    (('builtins', 'float'),): "NCollection_HArray1__double",
    (('nanoocp.gp', 'gp_Pnt'),): "NCollection_HArray1__gp_Pnt",
    (('nanoocp.gp', 'gp_Pnt2d'),): "NCollection_HArray1__gp_Pnt2d",
    (('nanoocp.gp', 'gp_XYZ'),): "NCollection_HArray1__gp_XYZ",
    (('builtins', 'int'),): "NCollection_HArray1__int",
})
NCollection_HArray2 = _Template("NCollection_HArray2", "nanoocp.NCollection", {
    (('builtins', 'float'),): "NCollection_HArray2__double",
    (('nanoocp.gp', 'gp_Pnt'),): "NCollection_HArray2__gp_Pnt",
    (('nanoocp.gp', 'gp_Pnt2d'),): "NCollection_HArray2__gp_Pnt2d",
    (('builtins', 'int'),): "NCollection_HArray2__int",
    (('nanoocp.NCollection', 'NCollection_HArray1__int'),): "NCollection_HArray2__opencascade_handle__NCollection_HArray1__int",
})
NCollection_HSequence = _Template("NCollection_HSequence", "nanoocp.NCollection", {
    (('nanoocp.Storage', 'Storage_Root'),): "NCollection_HSequence__Handle_Storage_Root",
    (('nanoocp.TCollection', 'TCollection_HAsciiString'),): "NCollection_HSequence__Handle_TCollection_HAsciiString",
    (('nanoocp.TCollection', 'TCollection_HExtendedString'),): "NCollection_HSequence__Handle_TCollection_HExtendedString",
    (('nanoocp.Units', 'Units_Quantity'),): "NCollection_HSequence__Handle_Units_Quantity",
    (('nanoocp.Units', 'Units_Token'),): "NCollection_HSequence__Handle_Units_Token",
    (('nanoocp.Units', 'Units_Unit'),): "NCollection_HSequence__Handle_Units_Unit",
    (('nanoocp.TCollection', 'TCollection_AsciiString'),): "NCollection_HSequence__TCollection_AsciiString",
    (('nanoocp.gp', 'gp_Pnt'),): "NCollection_HSequence__gp_Pnt",
    (('builtins', 'int'),): "NCollection_HSequence__int",
    (('nanoocp.NCollection', 'NCollection_HSequence__gp_Pnt'),): "NCollection_HSequence__opencascade_handle__NCollection_HSequence__gp_Pnt",
})
NCollection_IndexedDataMap = _Template("NCollection_IndexedDataMap", "nanoocp.NCollection", {
    (('nanoocp.TCollection', 'TCollection_AsciiString'), ('nanoocp.Standard', 'Standard_DumpValue')): "NCollection_IndexedDataMap__TCollection_AsciiString__Standard_DumpValue",
    (('nanoocp.TCollection', 'TCollection_AsciiString'), ('nanoocp.TCollection', 'TCollection_AsciiString')): "NCollection_IndexedDataMap__TCollection_AsciiString__TCollection_AsciiString",
    (('nanoocp.TopoDS', 'TopoDS_Shape'), ('nanoocp.NCollection', 'NCollection_List__TopoDS_Shape'), ('nanoocp.TopTools', 'TopTools_ShapeMapHasher')): "NCollection_IndexedDataMap__TopoDS_Shape__NCollection_List__TopoDS_Shape__TopTools_ShapeMapHasher",
})
NCollection_IndexedMap = _Template("NCollection_IndexedMap", "nanoocp.NCollection", {
    (('nanoocp.Message', 'Message_MetricType'),): "NCollection_IndexedMap__Message_MetricType",
    (('nanoocp.TCollection', 'TCollection_AsciiString'),): "NCollection_IndexedMap__TCollection_AsciiString",
    (('nanoocp.TopoDS', 'TopoDS_Shape'), ('nanoocp.TopTools', 'TopTools_ShapeMapHasher')): "NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher",
})
NCollection_List = _Template("NCollection_List", "nanoocp.NCollection", {
    (('nanoocp.Bnd', 'Bnd_Range'),): "NCollection_List__Bnd_Range",
    (('nanoocp.BRep', 'BRep_CurveRepresentation'),): "NCollection_List__Handle_BRep_CurveRepresentation",
    (('nanoocp.BRep', 'BRep_PointRepresentation'),): "NCollection_List__Handle_BRep_PointRepresentation",
    (('nanoocp.Message', 'Message_Alert'),): "NCollection_List__Handle_Message_Alert",
    (('nanoocp.Poly', 'Poly_Triangulation'),): "NCollection_List__Handle_Poly_Triangulation",
    (('nanoocp.Poly', 'Poly_CoherentTriangulation.TwoIntegers'),): "NCollection_List__Poly_CoherentTriangulation_TwoIntegers",
    (('nanoocp.Poly', 'Poly_MakeLoops.Link'),): "NCollection_List__Poly_MakeLoops_Link",
    (('nanoocp.TopoDS', 'TopoDS_Shape'),): "NCollection_List__TopoDS_Shape",
    (('builtins', 'float'),): "NCollection_List__double",
    (('nanoocp.gp', 'gp_Pnt'),): "NCollection_List__gp_Pnt",
    (('builtins', 'int'),): "NCollection_List__int",
})
NCollection_Map = _Template("NCollection_Map", "nanoocp.NCollection", {
    (('nanoocp.TopoDS', 'TopoDS_Shape'), ('nanoocp.TopTools', 'TopTools_ShapeMapHasher')): "NCollection_Map__TopoDS_Shape__TopTools_ShapeMapHasher",
    (('builtins', 'int'),): "NCollection_Map__int",
})
NCollection_Sequence = _Template("NCollection_Sequence", "nanoocp.NCollection", {
    (('nanoocp.AppParCurves', 'AppParCurves_MultiCurve'),): "NCollection_Sequence__AppParCurves_MultiCurve",
    (('nanoocp.Extrema', 'Extrema_POnCurv'),): "NCollection_Sequence__Extrema_POnCurv",
    (('nanoocp.Extrema', 'Extrema_POnSurf'),): "NCollection_Sequence__Extrema_POnSurf",
    (('nanoocp.AdvApp2Var', 'AdvApp2Var_Iso'),): "NCollection_Sequence__Handle_AdvApp2Var_Iso",
    (('nanoocp.AdvApp2Var', 'AdvApp2Var_Node'),): "NCollection_Sequence__Handle_AdvApp2Var_Node",
    (('nanoocp.AdvApp2Var', 'AdvApp2Var_Patch'),): "NCollection_Sequence__Handle_AdvApp2Var_Patch",
    (('nanoocp.Geom2d', 'Geom2d_Curve'),): "NCollection_Sequence__Handle_Geom2d_Curve",
    (('nanoocp.Message', 'Message_Printer'),): "NCollection_Sequence__Handle_Message_Printer",
    (('nanoocp.Standard', 'Standard_Transient'),): "NCollection_Sequence__Handle_Standard_Transient",
    (('nanoocp.Storage', 'Storage_Root'),): "NCollection_Sequence__Handle_Storage_Root",
    (('nanoocp.TCollection', 'TCollection_HAsciiString'),): "NCollection_Sequence__Handle_TCollection_HAsciiString",
    (('nanoocp.TCollection', 'TCollection_HExtendedString'),): "NCollection_Sequence__Handle_TCollection_HExtendedString",
    (('nanoocp.Units', 'Units_Quantity'),): "NCollection_Sequence__Handle_Units_Quantity",
    (('nanoocp.Units', 'Units_Token'),): "NCollection_Sequence__Handle_Units_Token",
    (('nanoocp.Units', 'Units_Unit'),): "NCollection_Sequence__Handle_Units_Unit",
    (('nanoocp.NCollection', 'NCollection_Sequence__Handle_AdvApp2Var_Iso'),): "NCollection_Sequence__NCollection_Sequence__Handle_AdvApp2Var_Iso",
    (('nanoocp.TCollection', 'TCollection_AsciiString'),): "NCollection_Sequence__TCollection_AsciiString",
    (('nanoocp.TCollection', 'TCollection_ExtendedString'),): "NCollection_Sequence__TCollection_ExtendedString",
    (('builtins', 'float'),): "NCollection_Sequence__double",
    (('nanoocp.gp', 'gp_Pnt'),): "NCollection_Sequence__gp_Pnt",
    (('nanoocp.gp', 'gp_Pnt2d'),): "NCollection_Sequence__gp_Pnt2d",
    (('builtins', 'int'),): "NCollection_Sequence__int",
    (('nanoocp.NCollection', 'NCollection_HSequence__gp_Pnt'),): "NCollection_Sequence__opencascade_handle__NCollection_HSequence__gp_Pnt",
})
NCollection_Shared = _Template("NCollection_Shared", "nanoocp.NCollection", {
    (('nanoocp.NCollection', 'NCollection_Map__int'),): "NCollection_Shared__NCollection_Map__int",
})

# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits

# C++ namespaces of the package (Python modules nanoocp.<package>.<namespace>)
import nanoocp.NCollection.NCollection_Primes  # noqa: E402,F401
