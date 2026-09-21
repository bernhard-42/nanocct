"""OCCT package ShapeFix (toolkit TKShHealing)."""
import importlib as _importlib

from nanoocp._TKShHealing import ShapeFix as _ext
from nanoocp._TKShHealing.ShapeFix import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "ShapeFix_SequenceOfWireSegment": ("nanoocp.NCollection", "NCollection_Sequence__ShapeFix_WireSegment"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
