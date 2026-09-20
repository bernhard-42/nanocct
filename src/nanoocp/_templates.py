"""Runtime support for the NCollection_Xxx[T] spelling of container instantiations (Design.md 6a).

nanobind registers one concrete class per C++ instantiation (NCollection_Array1__gp_Pnt); the Template
objects below map Python element types to those classes so that NCollection_Array1[gp_Pnt] reads like
the OCCT documentation's NCollection_Array1<gp_Pnt>. The generator writes the tables (nanoocp/NCollection.py)."""
from __future__ import annotations

import importlib
from typing import Any


class Template:
    """One NCollection template kind. ``tmpl[T]`` / ``tmpl[K, V]`` returns the bound class."""

    def __init__(self, name: str, module: str, instances: dict[tuple[tuple[str, str], ...], str]) -> None:
        self._name = name
        self._module = module
        self._specs = instances                                 # ((module, attr), ...) -> bound class name
        self._by_type: dict[tuple[Any, ...], Any] | None = None

    def _resolve(self) -> dict[tuple[Any, ...], Any]:
        if self._by_type is None:
            home = importlib.import_module(self._module)
            table: dict[tuple[Any, ...], Any] = {}
            for specs, cls_name in self._specs.items():
                key = tuple(getattr(importlib.import_module(mod), attr) for mod, attr in specs)
                table[key] = getattr(home, cls_name)
            self._by_type = table
        return self._by_type

    def __getitem__(self, item: Any) -> Any:
        key = item if isinstance(item, tuple) else (item,)
        cls = self._resolve().get(key)
        if cls is None:
            args = ", ".join(getattr(k, "__name__", repr(k)) for k in key)
            raise TypeError(f"{self._name}<{args}> is not bound by nanoocp (no bound OCCT signature uses it). "
                            f"Bound: {', '.join(sorted(self.bound()))}")
        return cls

    def bound(self) -> list[str]:
        """Names of the bound instantiations, e.g. ['NCollection_Array1__double', ...]."""
        return list(self._specs.values())

    def __iter__(self):
        return iter(self._resolve().keys())

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        raise TypeError(f"{self._name} is a template: use {self._name}[ElementType](...) or one of {self.bound()}")

    def __repr__(self) -> str:
        return f"<nanoocp template {self._name}, {len(self._specs)} instantiations>"
