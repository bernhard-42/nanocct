"""OCCT package IGESBasic (toolkit TKDEIGES)."""
import importlib as _importlib

from nanoocp._TKDEIGES import IGESBasic as _ext
from nanoocp._TKDEIGES.IGESBasic import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "IGESBasic_Array1OfLineFontEntity": ("nanoocp.NCollection", "NCollection_Array1__Handle_IGESData_LineFontEntity"),
    "IGESBasic_Array2OfHArray1OfReal": ("nanoocp.NCollection", "NCollection_Array2__opencascade_handle__NCollection_HArray1__double"),
    "IGESBasic_HArray1OfLineFontEntity": ("nanoocp.NCollection", "NCollection_HArray1__Handle_IGESData_LineFontEntity"),
    "IGESBasic_HArray2OfHArray1OfReal": ("nanoocp.NCollection", "NCollection_HArray2__opencascade_handle__NCollection_HArray1__double"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
