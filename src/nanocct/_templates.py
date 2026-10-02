"""Runtime support for the NCollection_Xxx[T] spelling of container instantiations (Binding-Rules.md 7a).

nanobind registers one concrete class per C++ instantiation (NCollection_Array1__gp_Pnt). The generated
nanocct/NCollection/__init__.py declares one small class per template, a subclass of `Generic` below, whose
`_instances` table maps the Python element types to those classes, so that NCollection_Array1[gp_Pnt] reads like
the OCCT documentation's NCollection_Array1<gp_Pnt> and *is* NCollection_Array1__gp_Pnt.

The table keys are the element types themselves, as Python passes them to `__class_getitem__`: the type for one
argument (NCollection_Array1[gp_Pnt]), a tuple for several (NCollection_DataMap[int, float]). A key the generator
spells wrong fails when the module is imported, not later as a silent "not bound".

`isinstance(x, NCollection_Array1)` holds for every instantiation and for everything that derives from one in C++
(an HArray1<T> is an Array1<T>, an NCollection_Shared<T> is a T): one rule for every template, decided on the
class's MRO. nanobind's single inheritance cannot express it -- HArray1<T> already uses its one base for Array1<T>
-- so the relation is virtual (abc), not a base class: `__mro__` does not list the generic class.

Four C++ scalars are spelled by their Python type (C++ `double` is `float`, `int`, `bool`, `std::string` is `str`). The
five without a Python type of their own are spelled by the markers below (Binding-Rules.md 7a): NCollection_HArray1[float32] is
NCollection_HArray1__float, a C++ 32-bit float array. They are keys only -- the values are plain Python floats and ints,
converted and range-checked by the bound class -- so each marker subclasses the Python type, and the stubs make them
aliases of it: precision is not a Python type."""
from __future__ import annotations

import abc
from typing import Any


class float32(float):
    """C++ `float` (32-bit) as a template argument: NCollection_Array1[float32] is NCollection_Array1__float."""


class uchar(int):
    """C++ `unsigned char` as a template argument: NCollection_HArray1[uchar] is NCollection_HArray1__unsigned_char."""


class uint(int):
    """C++ `unsigned int` as a template argument: NCollection_DynamicArray[uint] is NCollection_DynamicArray__unsigned_int."""


class ulong(int):
    """C++ `unsigned long` as a template argument (64-bit on macOS and Linux, 32-bit on Windows)."""


class ulonglong(int):
    """C++ `unsigned long long` as a template argument: NCollection_LinearVector[ulonglong] is
    NCollection_LinearVector__unsigned_long_long."""


# C++ spelling -> the Python spelling of a template argument, for the error message of a C++ name in the brackets
_CXX_NAMES = {"double": "float", "float": "float32", "unsigned char": "uchar", "unsigned int": "uint",
              "unsigned long": "ulong", "unsigned long long": "ulonglong", "std::string": "str"}


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
            given = params if isinstance(params, tuple) else (params,)
            args = ", ".join(getattr(p, "__name__", repr(p)) for p in given)
            names = [p for p in given if isinstance(p, str)]
            if len(names) > 0:                      # NCollection_Array1['double']: a C++ name, not a Python type
                hints = ", ".join(f"{_CXX_NAMES[n]} for C++ {n}" for n in names if n in _CXX_NAMES)
                if hints != "":
                    hints = f" -- {hints} (from nanocct.NCollection)"
                raise TypeError(f"{cls.__name__}[{args}]: template arguments are Python types, not C++ names{hints}") from None
            raise TypeError(f"{cls.__name__}[{args}] is not bound by nanocct (no bound OCCT signature uses it)") from None

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
