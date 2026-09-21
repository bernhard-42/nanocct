"""OCCT package BOPDS (toolkit TKBO)."""
import importlib as _importlib

from nanoocp._TKBO import BOPDS as _ext
from nanoocp._TKBO.BOPDS import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "BOPDS_ListOfPave": ("nanoocp.NCollection", "NCollection_List__BOPDS_Pave"),
    "BOPDS_VectorOfCurve": ("nanoocp.NCollection", "NCollection_DynamicArray__BOPDS_Curve"),
    "BOPDS_VectorOfFaceInfo": ("nanoocp.NCollection", "NCollection_DynamicArray__BOPDS_FaceInfo"),
    "BOPDS_VectorOfInterfEE": ("nanoocp.NCollection", "NCollection_DynamicArray__BOPDS_InterfEE"),
    "BOPDS_VectorOfInterfEF": ("nanoocp.NCollection", "NCollection_DynamicArray__BOPDS_InterfEF"),
    "BOPDS_VectorOfInterfEZ": ("nanoocp.NCollection", "NCollection_DynamicArray__BOPDS_InterfEZ"),
    "BOPDS_VectorOfInterfFF": ("nanoocp.NCollection", "NCollection_DynamicArray__BOPDS_InterfFF"),
    "BOPDS_VectorOfInterfFZ": ("nanoocp.NCollection", "NCollection_DynamicArray__BOPDS_InterfFZ"),
    "BOPDS_VectorOfInterfVE": ("nanoocp.NCollection", "NCollection_DynamicArray__BOPDS_InterfVE"),
    "BOPDS_VectorOfInterfVF": ("nanoocp.NCollection", "NCollection_DynamicArray__BOPDS_InterfVF"),
    "BOPDS_VectorOfInterfVV": ("nanoocp.NCollection", "NCollection_DynamicArray__BOPDS_InterfVV"),
    "BOPDS_VectorOfInterfVZ": ("nanoocp.NCollection", "NCollection_DynamicArray__BOPDS_InterfVZ"),
    "BOPDS_VectorOfInterfZZ": ("nanoocp.NCollection", "NCollection_DynamicArray__BOPDS_InterfZZ"),
    "BOPDS_VectorOfPoint": ("nanoocp.NCollection", "NCollection_DynamicArray__BOPDS_Point"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
