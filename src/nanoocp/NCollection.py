"""OCCT package NCollection (toolkit TKernel)."""
import importlib as _importlib

from nanoocp._TKernel import NCollection as _ext
from nanoocp._TKernel.NCollection import *  # noqa: F401,F403


# NCollection_Xxx[T] -> bound class (Design.md 6a); tables generated from manifest.json
from nanoocp._templates import Template as _Template

NCollection_Array1 = _Template("NCollection_Array1", "nanoocp.NCollection", {
    (('nanoocp.Standard', 'Standard_Persistent'),): "NCollection_Array1__Handle_Standard_Persistent",
    (('builtins', 'float'),): "NCollection_Array1__double",
})
NCollection_HArray1 = _Template("NCollection_HArray1", "nanoocp.NCollection", {
    (('nanoocp.Standard', 'Standard_Persistent'),): "NCollection_HArray1__Handle_Standard_Persistent",
})

# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
