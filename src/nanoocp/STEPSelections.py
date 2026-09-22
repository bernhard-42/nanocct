"""OCCT package STEPSelections (toolkit TKDESTEP)."""
import importlib as _importlib

from nanoocp._TKDESTEP import STEPSelections as _ext
from nanoocp._TKDESTEP.STEPSelections import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "STEPSelections_HSequenceOfAssemblyLink": ("nanoocp.NCollection", "NCollection_HSequence__Handle_STEPSelections_AssemblyLink"),
    "STEPSelections_SequenceOfAssemblyLink": ("nanoocp.NCollection", "NCollection_Sequence__Handle_STEPSelections_AssemblyLink"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
