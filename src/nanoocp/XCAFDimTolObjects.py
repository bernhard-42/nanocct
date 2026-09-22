"""OCCT package XCAFDimTolObjects (toolkit TKXCAF)."""
import importlib as _importlib

from nanoocp._TKXCAF import XCAFDimTolObjects as _ext
from nanoocp._TKXCAF.XCAFDimTolObjects import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "XCAFDimTolObjects_DatumModifiersSequence": ("nanoocp.NCollection", "NCollection_Sequence__XCAFDimTolObjects_DatumSingleModif"),
    "XCAFDimTolObjects_DimensionModifiersSequence": ("nanoocp.NCollection", "NCollection_Sequence__XCAFDimTolObjects_DimensionModif"),
    "XCAFDimTolObjects_GeomToleranceModifiersSequence": ("nanoocp.NCollection", "NCollection_Sequence__XCAFDimTolObjects_GeomToleranceModif"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
