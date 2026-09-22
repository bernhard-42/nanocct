"""OCCT package IGESGraph (toolkit TKDEIGES)."""
import importlib as _importlib

from nanoocp._TKDEIGES import IGESGraph as _ext
from nanoocp._TKDEIGES.IGESGraph import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "IGESGraph_Array1OfColor": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESGraph_Color"),
    "IGESGraph_Array1OfTextDisplayTemplate": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESGraph_TextDisplayTemplate"),
    "IGESGraph_Array1OfTextFontDef": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESGraph_TextFontDef"),
    "IGESGraph_HArray1OfColor": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESGraph_Color"),
    "IGESGraph_HArray1OfTextDisplayTemplate": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESGraph_TextDisplayTemplate"),
    "IGESGraph_HArray1OfTextFontDef": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESGraph_TextFontDef"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
