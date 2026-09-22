"""OCCT package TransferBRep (toolkit TKXSBase)."""
import importlib as _importlib

from nanoocp._TKXSBase import TransferBRep as _ext
from nanoocp._TKXSBase.TransferBRep import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TransferBRep_HSequenceOfTransferResultInfo": ("nanoocp.NCollection", "NCollection_HSequence__Handle_TransferBRep_TransferResultInfo"),
    "TransferBRep_SequenceOfTransferResultInfo": ("nanoocp.NCollection", "NCollection_Sequence__Handle_TransferBRep_TransferResultInfo"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
