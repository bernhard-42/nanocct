"""OCCT pre-8.0 typedef names with prefix TopOpeBRepDS (OCCT src/Deprecated/NCollectionAliases)."""
import importlib as _importlib


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference": ("nanoocp.NCollection", "NCollection_Array1__int"),
    "TopOpeBRepDS_HArray1OfDataMapOfIntegerListOfInterference": ("nanoocp.NCollection", "NCollection_HArray1__int"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
