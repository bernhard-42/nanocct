"""OCCT package Message (toolkit TKernel)."""
import importlib as _importlib

from nanoocp._TKernel import Message as _ext
from nanoocp._TKernel.Message import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
