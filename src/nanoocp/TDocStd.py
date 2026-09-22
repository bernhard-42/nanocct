"""OCCT package TDocStd (toolkit TKLCAF)."""
import importlib as _importlib

from nanoocp._TKLCAF import TDocStd as _ext
from nanoocp._TKLCAF.TDocStd import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TDocStd_SequenceOfApplicationDelta": ("nanoocp.NCollection", "NCollection_Sequence__Handle_TDocStd_ApplicationDelta"),
    "TDocStd_SequenceOfDocument": ("nanoocp.NCollection", "NCollection_Sequence__Handle_TDocStd_Document"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
