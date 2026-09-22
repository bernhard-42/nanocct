"""OCCT package PCDM (toolkit TKCDF)."""
import importlib as _importlib

from nanoocp._TKCDF import PCDM as _ext
from nanoocp._TKCDF.PCDM import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "PCDM_SequenceOfDocument": ("nanoocp.NCollection", "NCollection_Sequence__Handle_PCDM_Document"),
    "PCDM_SequenceOfReference": ("nanoocp.NCollection", "NCollection_Sequence__PCDM_Reference"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
