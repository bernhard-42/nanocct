"""OCCT package TDF (toolkit TKLCAF)."""
import importlib as _importlib

from nanoocp._TKLCAF import TDF as _ext
from nanoocp._TKLCAF.TDF import *  # noqa: F401,F403


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TDF_AttributeDeltaList": ("nanoocp.NCollection", "NCollection_List__Handle_TDF_AttributeDelta"),
    "TDF_AttributeList": ("nanoocp.NCollection", "NCollection_List__Handle_TDF_Attribute"),
    "TDF_AttributeSequence": ("nanoocp.NCollection", "NCollection_Sequence__Handle_TDF_Attribute"),
    "TDF_DeltaList": ("nanoocp.NCollection", "NCollection_List__Handle_TDF_Delta"),
    "TDF_IDList": ("nanoocp.NCollection", "NCollection_List__Standard_GUID"),
    "TDF_LabelList": ("nanoocp.NCollection", "NCollection_List__TDF_Label"),
    "TDF_LabelSequence": ("nanoocp.NCollection", "NCollection_Sequence__TDF_Label"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits
