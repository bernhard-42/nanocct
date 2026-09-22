"""OCCT package TNaming (toolkit TKCAF)."""
import importlib as _importlib

from nanoocp._TKCAF import TNaming as _ext
from nanoocp._TKCAF.TNaming import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TNaming_ListOfNamedShape": ("nanoocp.NCollection", "NCollection_List__Handle_TNaming_NamedShape"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
