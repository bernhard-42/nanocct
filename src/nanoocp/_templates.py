"""Runtime support for the NCollection_Xxx[T] spelling of container instantiations (Design.md 6a).

nanobind registers one concrete class per C++ instantiation (NCollection_Array1__gp_Pnt); the Template
objects below map Python element types to those classes so that NCollection_Array1[gp_Pnt] reads like
the OCCT documentation's NCollection_Array1<gp_Pnt>. The generator writes the tables (nanoocp/NCollection.py)."""
from __future__ import annotations

import functools
import importlib
from typing import Any


class Template:
    """One NCollection template kind. ``tmpl[T]`` / ``tmpl[K, V]`` returns the bound class."""

    def __init__(self, name: str, module: str, instances: dict[tuple[tuple[str, str], ...], str]) -> None:
        self._name = name
        self._module = module
        self._specs = instances                                 # ((module, attr), ...) -> bound class name
        self._by_type: dict[tuple[Any, ...], Any] | None = None

    @staticmethod
    def _spec_of(cls: Any) -> tuple[str, str]:
        """(module, attribute path) of a bound class, as the generated tables spell it."""
        return (getattr(cls, "__module__", ""), getattr(cls, "__qualname__", getattr(cls, "__name__", "")))

    def __getitem__(self, item: Any) -> Any:
        """NCollection_Array1[gp_Pnt] -> the bound class, importing only the toolkit that holds it.

        Resolved per key on purpose: building the whole table would import every module the table mentions --
        45 toolkits for the container kinds -- which is exactly the eager import this design removes."""
        key = item if isinstance(item, tuple) else (item,)
        cls_name = self._specs.get(tuple(self._spec_of(k) for k in key))
        if cls_name is None:
            # a class in a C++ namespace has __module__ nanoocp.<pkg>.<ns> while the table spells it
            # ("nanoocp.<pkg>", "<ns>.<cls>"), so fall back to matching the resolved classes
            for specs, name in self._specs.items():
                if len(specs) == len(key) and all(self._lookup(m, a) is k for (m, a), k in zip(specs, key)):
                    cls_name = name
                    break
        if cls_name is None:
            args = ", ".join(getattr(k, "__name__", repr(k)) for k in key)
            raise TypeError(f"{self._name}<{args}> is not bound by nanoocp (no bound OCCT signature uses it). "
                            f"Bound: {', '.join(sorted(self.bound()))}")
        return getattr(importlib.import_module(self._module), cls_name)

    @staticmethod
    def _lookup(module: str, attr: str) -> Any:
        try:
            return functools.reduce(getattr, attr.split("."), importlib.import_module(module))
        except (ImportError, AttributeError):
            return None

    def _resolve(self) -> dict[tuple[Any, ...], Any]:
        """The whole table, for __iter__ only -- it imports every module the table mentions."""
        if self._by_type is None:
            self._by_type = {tuple(self._lookup(m, a) for m, a in specs): getattr(importlib.import_module(self._module), name)
                             for specs, name in self._specs.items()}
        return self._by_type

    def bound(self) -> list[str]:
        """Names of the bound instantiations, e.g. ['NCollection_Array1__double', ...]."""
        return list(self._specs.values())

    def __iter__(self):
        return iter(self._resolve().keys())

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        raise TypeError(f"{self._name} is a template: use {self._name}[ElementType](...) or one of {self.bound()}")

    def __repr__(self) -> str:
        return f"<nanoocp template {self._name}, {len(self._specs)} instantiations>"
