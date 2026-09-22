"""OCCT package IGESSolid (toolkit TKDEIGES)."""
import importlib as _importlib

from nanoocp._TKDEIGES import IGESSolid as _ext
from nanoocp._TKDEIGES.IGESSolid import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "IGESSolid_Array1OfFace": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESSolid_Face"),
    "IGESSolid_Array1OfLoop": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESSolid_Loop"),
    "IGESSolid_Array1OfShell": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESSolid_Shell"),
    "IGESSolid_Array1OfVertexList": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESSolid_VertexList"),
    "IGESSolid_HArray1OfFace": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESSolid_Face"),
    "IGESSolid_HArray1OfLoop": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESSolid_Loop"),
    "IGESSolid_HArray1OfShell": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESSolid_Shell"),
    "IGESSolid_HArray1OfVertexList": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESSolid_VertexList"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
