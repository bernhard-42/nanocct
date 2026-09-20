"""OCCT package NCollection (toolkit TKernel)."""
import importlib as _importlib

from nanoocp._TKernel import NCollection as _ext
from nanoocp._TKernel.NCollection import *  # noqa: F401,F403


# NCollection_Xxx[T] -> bound class (Design.md 6a); tables generated from manifest.json
from nanoocp._templates import Template as _Template

NCollection_Array1 = _Template("NCollection_Array1", "nanoocp.NCollection", {
    (('nanoocp.Bnd', 'Bnd_Box'),): "NCollection_Array1__Bnd_Box",
    (('nanoocp.Standard', 'Standard_Persistent'),): "NCollection_Array1__Handle_Standard_Persistent",
    (('nanoocp.Poly', 'Poly_Triangle'),): "NCollection_Array1__Poly_Triangle",
    (('builtins', 'float'),): "NCollection_Array1__double",
    (('nanoocp.gp', 'gp_Pnt'),): "NCollection_Array1__gp_Pnt",
    (('nanoocp.gp', 'gp_Pnt2d'),): "NCollection_Array1__gp_Pnt2d",
    (('nanoocp.gp', 'gp_Vec'),): "NCollection_Array1__gp_Vec",
    (('builtins', 'int'),): "NCollection_Array1__int",
})
NCollection_Array2 = _Template("NCollection_Array2", "nanoocp.NCollection", {
    (('builtins', 'float'),): "NCollection_Array2__double",
    (('nanoocp.gp', 'gp_Pnt'),): "NCollection_Array2__gp_Pnt",
    (('nanoocp.gp', 'gp_Vec'),): "NCollection_Array2__gp_Vec",
    (('builtins', 'int'),): "NCollection_Array2__int",
})
NCollection_DataMap = _Template("NCollection_DataMap", "nanoocp.NCollection", {
    (('nanoocp.TCollection', 'TCollection_AsciiString'), ('nanoocp.TCollection', 'TCollection_AsciiString')): "NCollection_DataMap__TCollection_AsciiString__TCollection_AsciiString",
    (('nanoocp.TCollection', 'TCollection_AsciiString'), ('builtins', 'int')): "NCollection_DataMap__TCollection_AsciiString__int",
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
    (('nanoocp.Bnd', 'Bnd_Box'),): "NCollection_HArray1__Bnd_Box",
    (('nanoocp.Standard', 'Standard_Persistent'),): "NCollection_HArray1__Handle_Standard_Persistent",
    (('nanoocp.Poly', 'Poly_Triangle'),): "NCollection_HArray1__Poly_Triangle",
    (('builtins', 'float'),): "NCollection_HArray1__double",
    (('nanoocp.gp', 'gp_Pnt'),): "NCollection_HArray1__gp_Pnt",
    (('nanoocp.gp', 'gp_Pnt2d'),): "NCollection_HArray1__gp_Pnt2d",
    (('builtins', 'int'),): "NCollection_HArray1__int",
})
NCollection_HArray2 = _Template("NCollection_HArray2", "nanoocp.NCollection", {
    (('builtins', 'float'),): "NCollection_HArray2__double",
    (('builtins', 'int'),): "NCollection_HArray2__int",
})
NCollection_HSequence = _Template("NCollection_HSequence", "nanoocp.NCollection", {
    (('nanoocp.Storage', 'Storage_Root'),): "NCollection_HSequence__Handle_Storage_Root",
    (('nanoocp.TCollection', 'TCollection_HAsciiString'),): "NCollection_HSequence__Handle_TCollection_HAsciiString",
    (('nanoocp.TCollection', 'TCollection_HExtendedString'),): "NCollection_HSequence__Handle_TCollection_HExtendedString",
    (('nanoocp.Units', 'Units_Quantity'),): "NCollection_HSequence__Handle_Units_Quantity",
    (('nanoocp.Units', 'Units_Token'),): "NCollection_HSequence__Handle_Units_Token",
    (('nanoocp.Units', 'Units_Unit'),): "NCollection_HSequence__Handle_Units_Unit",
    (('nanoocp.TCollection', 'TCollection_AsciiString'),): "NCollection_HSequence__TCollection_AsciiString",
    (('builtins', 'int'),): "NCollection_HSequence__int",
})
NCollection_IndexedDataMap = _Template("NCollection_IndexedDataMap", "nanoocp.NCollection", {
    (('nanoocp.TCollection', 'TCollection_AsciiString'), ('nanoocp.Standard', 'Standard_DumpValue')): "NCollection_IndexedDataMap__TCollection_AsciiString__Standard_DumpValue",
    (('nanoocp.TCollection', 'TCollection_AsciiString'), ('nanoocp.TCollection', 'TCollection_AsciiString')): "NCollection_IndexedDataMap__TCollection_AsciiString__TCollection_AsciiString",
})
NCollection_IndexedMap = _Template("NCollection_IndexedMap", "nanoocp.NCollection", {
    (('nanoocp.Message', 'Message_MetricType'),): "NCollection_IndexedMap__Message_MetricType",
    (('nanoocp.TCollection', 'TCollection_AsciiString'),): "NCollection_IndexedMap__TCollection_AsciiString",
})
NCollection_List = _Template("NCollection_List", "nanoocp.NCollection", {
    (('nanoocp.Bnd', 'Bnd_Range'),): "NCollection_List__Bnd_Range",
    (('nanoocp.Message', 'Message_Alert'),): "NCollection_List__Handle_Message_Alert",
    (('nanoocp.Poly', 'Poly_Triangulation'),): "NCollection_List__Handle_Poly_Triangulation",
    (('builtins', 'int'),): "NCollection_List__int",
})
NCollection_Map = _Template("NCollection_Map", "nanoocp.NCollection", {
    (('builtins', 'int'),): "NCollection_Map__int",
})
NCollection_Sequence = _Template("NCollection_Sequence", "nanoocp.NCollection", {
    (('nanoocp.Message', 'Message_Printer'),): "NCollection_Sequence__Handle_Message_Printer",
    (('nanoocp.Standard', 'Standard_Transient'),): "NCollection_Sequence__Handle_Standard_Transient",
    (('nanoocp.Storage', 'Storage_Root'),): "NCollection_Sequence__Handle_Storage_Root",
    (('nanoocp.TCollection', 'TCollection_HAsciiString'),): "NCollection_Sequence__Handle_TCollection_HAsciiString",
    (('nanoocp.TCollection', 'TCollection_HExtendedString'),): "NCollection_Sequence__Handle_TCollection_HExtendedString",
    (('nanoocp.Units', 'Units_Quantity'),): "NCollection_Sequence__Handle_Units_Quantity",
    (('nanoocp.Units', 'Units_Token'),): "NCollection_Sequence__Handle_Units_Token",
    (('nanoocp.Units', 'Units_Unit'),): "NCollection_Sequence__Handle_Units_Unit",
    (('nanoocp.TCollection', 'TCollection_AsciiString'),): "NCollection_Sequence__TCollection_AsciiString",
    (('nanoocp.TCollection', 'TCollection_ExtendedString'),): "NCollection_Sequence__TCollection_ExtendedString",
    (('nanoocp.gp', 'gp_Pnt2d'),): "NCollection_Sequence__gp_Pnt2d",
    (('builtins', 'int'),): "NCollection_Sequence__int",
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
