"""Runtime support for the NCollection_Xxx[T] spelling of container instantiations (Design.md 6a).

nanobind registers one concrete class per C++ instantiation (NCollection_Array1__gp_Pnt). The generated
nanoocp/NCollection/__init__.py declares one small class per template, a subclass of `Generic` below, whose
`_instances` table maps the Python element types to those classes, so that NCollection_Array1[gp_Pnt] reads like
the OCCT documentation's NCollection_Array1<gp_Pnt> and *is* NCollection_Array1__gp_Pnt.

The table keys are the element types themselves, as Python passes them to `__class_getitem__`: the type for one
argument (NCollection_Array1[gp_Pnt]), a tuple for several (NCollection_DataMap[int, float]). A key the generator
spells wrong fails when the module is imported, not later as a silent "not bound".

`isinstance(x, NCollection_Array1)` holds for every instantiation and for everything that derives from one in C++
(an HArray1<T> is an Array1<T>, an NCollection_Shared<T> is a T): one rule for every template, decided on the
class's MRO. nanobind's single inheritance cannot express it -- HArray1<T> already uses its one base for Array1<T>
-- so the relation is virtual (abc), not a base class: `__mro__` does not list the generic class."""
from __future__ import annotations

import abc
from typing import Any


class Generic(metaclass=abc.ABCMeta):
    """An OCCT class template. `NCollection_Array1[gp_Pnt]` is the bound class NCollection_Array1__gp_Pnt."""

    _instances: dict[Any, type] = {}         # element type(s) -> bound instantiation; set by each generated subclass
    _classes: frozenset[type] = frozenset()  # the bound instantiations, for __subclasshook__

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        cls._classes = frozenset(cls._instances.values())

    def __class_getitem__(cls, params: Any) -> type:
        try:
            return cls._instances[params]
        except KeyError:
            args = ", ".join(getattr(p, "__name__", repr(p)) for p in (params if isinstance(params, tuple) else (params,)))
            raise TypeError(f"{cls.__name__}[{args}] is not bound by nanoocp (no bound OCCT signature uses it)") from None

    @classmethod
    def __subclasshook__(cls, sub: type) -> Any:
        if any(c in cls._classes for c in getattr(sub, "__mro__", ())):
            return True
        return NotImplemented

    def __new__(cls, *args: Any, **kwargs: Any) -> Any:
        raise TypeError(f"{cls.__name__} is a class template: give its arguments, {cls.__name__}[T](...)")

    @classmethod
    def bound(cls) -> list[str]:
        """Names of the bound instantiations, e.g. ['NCollection_Array1__double', ...]."""
        return sorted(c.__name__ for c in cls._classes)
