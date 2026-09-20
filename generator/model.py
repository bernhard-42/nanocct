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
    class_name: str = ""    # canonical name of the class/enum type behind the parameter ("" for scalars, strings, std types)


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
    is_copy: bool = False
    defined_in_header: bool = False


@dataclass
class Conversion:
    """operator T() const: kind is bool | int | float (Python dunder) or class | handle (a constructor of T from this class)."""
    kind: str
    target: str                 # C++ spelling of T (the pointee for handle)
    target_class: str           # canonical class/enum name of T, "" for scalars
    is_explicit: bool
    doc: str


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
    scope: tuple[str, ...] = ()  # Python attribute path of the enclosing C++ namespace, relative to the package module


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
    scope: tuple[str, ...] = ()       # Python attribute path of the enclosing namespace(s)/class(es), relative to the package module
                                      # (scope + py_name = the full path; recorded in the manifest when parse.py_path cannot derive it)
    outer: str = ""                   # C++ name of the enclosing class for a nested class (declared after it)
    has_declared_ctor: bool = False   # any constructor at any access level (suppresses the implicit default ctor)
    template_key: str = ""            # for an instantiation bound under an alias: canonical key (dedupe across packages)
    constructible: bool = True        # False when operator new is not public (placement new impossible)
    unbindable: bool = False          # nb::class_ cannot be instantiated (member of incomplete type); reported, not bound
    ctors: list[Constructor] = field(default_factory=list)
    methods: list[Method] = field(default_factory=list)
    fields: list[Field] = field(default_factory=list)
    conversions: list[Conversion] = field(default_factory=list)
    enums: list[Enum] = field(default_factory=list)
    nested: list[Class] = field(default_factory=list)  # public nested classes (flattened into PackageIR.classes by the parser)
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
    qualified: str = ""         # C++ name to call (Ns::Name for a function in a namespace); "" -> name
    scope: tuple[str, ...] = () # Python attribute path of the enclosing C++ namespace, relative to the package module


@dataclass
class Constant:
    py_name: str
    cpp: str                    # fully qualified C++ expression
    doc: str
    scope: tuple[str, ...] = ()


@dataclass
class TypeAlias:
    py_name: str
    target: str                 # canonical C++ spelling of the aliased type (a bound class -> Python alias)
    written: str                # as written in the header, for the report
    scope: tuple[str, ...] = ()


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
    prelude: list[str] = field(default_factory=list)     # headers included before the package's own (non-self-contained headers)
    classes: list[Class] = field(default_factory=list)
    enums: list[Enum] = field(default_factory=list)
    functions: list[Function] = field(default_factory=list)
    typedefs: list[TypeAlias] = field(default_factory=list)
    constants: list[Constant] = field(default_factory=list)    # namespace-level constexpr values
    namespaces: list[tuple[str, ...]] = field(default_factory=list)   # C++ namespaces bound as submodules (Python paths, outer first)
    hashable: set[str] = field(default_factory=set)   # classes with a std::hash<T> specialisation in this package's headers -> __hash__
    hashable_templates: set[str] = field(default_factory=set)   # class templates with a partial std::hash<Tmpl<...>> specialisation
    instances: dict[str, TemplateInstance] = field(default_factory=dict)  # NCollection instances used in bound signatures
    report: list[str] = field(default_factory=list)
