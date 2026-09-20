"""Intermediate representation of what gets bound."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Param:
    name: str
    type: str            # C++ spelling as written (typedefs resolved to canonical where safe)
    default: str | None  # C++ expression or None
    is_out: bool         # non-const lvalue ref to a primitive -> returned in a tuple
    is_inout: bool = False  # ... and also taken as input (overrides.toml [inout])


@dataclass
class Method:
    name: str
    params: list[Param]
    result: str                 # C++ return type spelling, "void" if none
    result_kind: str            # value | ptr_transient | ref_transient | ptr_class | ref_mutable | other (see parse._result_kind)
    result_class: str           # for ptr_/ref_ kinds: the pointee class name
    is_static: bool
    is_const: bool
    is_noexcept: bool
    doc: str
    is_operator: bool = False
    skip_reason: str | None = None
    defined_in_header: bool = False   # inline definition seen in the TU (no library symbol needed)


@dataclass
class Constructor:
    params: list[Param]
    doc: str
    skip_reason: str | None = None
    is_implicit: bool = False     # non-explicit converting constructor -> nb::implicitly_convertible


@dataclass
class Field:
    name: str
    type: str
    is_const: bool
    doc: str


@dataclass
class Enum:
    name: str            # fully qualified C++ name (e.g. gp_Dir::D)
    py_name: str         # name in Python (D for nested, gp_TrsfForm at module level)
    values: list[tuple[str, str]]   # (py name, fully qualified C++ name)
    is_scoped: bool
    doc: str
    header: str
    is_anonymous: bool = False   # enum { A = 1, B = 2 }; -> integer constants, no Python enum type


@dataclass
class Class:
    name: str            # C++ spelling, e.g. gp_Pnt or NCollection_Lerp<gp_Trsf>
    py_name: str         # Python name, e.g. gp_Pnt or NCollection_Lerp_gp_Trsf
    bases: list[str]
    header: str
    doc: str
    is_transient: bool          # derives (transitively) from Standard_Transient
    is_exception: bool          # derives (transitively) from Standard_Failure -> bound as Python exception
    is_abstract: bool
    has_declared_ctor: bool = False   # any constructor at any access level (suppresses the implicit default ctor)
    template_key: str = ""            # for an instantiation bound under an alias: canonical key (dedupe across packages)
    constructible: bool = True        # False when operator new is not public (placement new impossible)
    ctors: list[Constructor] = field(default_factory=list)
    methods: list[Method] = field(default_factory=list)
    fields: list[Field] = field(default_factory=list)
    enums: list[Enum] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)   # human readable report lines


@dataclass
class Function:
    name: str
    params: list[Param]
    result: str
    result_kind: str
    result_class: str
    is_noexcept: bool
    doc: str
    header: str
    is_operator: bool = False
    skip_reason: str | None = None


@dataclass
class TemplateInstance:
    template: str         # NCollection_Array1
    args: list[str]       # canonical template arguments, e.g. ["gp_Pnt"]
    key: str              # canonical type spelling, e.g. NCollection_Array1<gp_Pnt>
    element: str          # canonical spelling of the element type (first argument), for the home package


@dataclass
class PackageIR:
    name: str
    toolkit: str
    headers: list[str]
    classes: list[Class] = field(default_factory=list)
    enums: list[Enum] = field(default_factory=list)
    functions: list[Function] = field(default_factory=list)
    typedefs: list[tuple[str, str]] = field(default_factory=list)   # (alias, target)
    constants: list[tuple[str, str, str]] = field(default_factory=list)  # (py name, C++ expression, doc): namespace-level constexpr
    instances: dict[str, TemplateInstance] = field(default_factory=dict)  # NCollection instances used in bound signatures
    report: list[str] = field(default_factory=list)
