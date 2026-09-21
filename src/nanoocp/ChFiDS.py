"""OCCT package ChFiDS (toolkit TKFillet)."""
import importlib as _importlib

from nanoocp._TKFillet import ChFiDS as _ext
from nanoocp._TKFillet.ChFiDS import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "ChFiDS_HData": ("nanoocp.NCollection", "NCollection_HSequence__Handle_ChFiDS_SurfData"),
    "ChFiDS_ListOfHElSpine": ("nanoocp.NCollection", "NCollection_List__Handle_ChFiDS_ElSpine"),
    "ChFiDS_ListOfStripe": ("nanoocp.NCollection", "NCollection_List__Handle_ChFiDS_Stripe"),
    "ChFiDS_Regularities": ("nanoocp.NCollection", "NCollection_List__ChFiDS_Regul"),
    "ChFiDS_SecArray1": ("nanoocp.NCollection", "NCollection_Array1__ChFiDS_CircSection"),
    "ChFiDS_SecHArray1": ("nanoocp.NCollection", "NCollection_HArray1__ChFiDS_CircSection"),
    "ChFiDS_SequenceOfSurfData": ("nanoocp.NCollection", "NCollection_Sequence__Handle_ChFiDS_SurfData"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
