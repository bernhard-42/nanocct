"""OCCT pre-8.0 typedef names with prefix GeomInt (OCCT src/Deprecated/NCollectionAliases)."""
import importlib as _importlib


# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {
    "GeomInt_VectorOfReal": ("nanoocp.NCollection", "NCollection_DynamicArray__double"),
}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
