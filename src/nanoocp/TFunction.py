"""OCCT pre-8.0 typedef names with prefix TFunction (OCCT src/Deprecated/NCollectionAliases)."""
import importlib as _importlib


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TFunction_Array1OfDataMapOfGUIDDriver": ("nanoocp.NCollection", "NCollection_Array1__int"),
    "TFunction_HArray1OfDataMapOfGUIDDriver": ("nanoocp.NCollection", "NCollection_HArray1__int"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
