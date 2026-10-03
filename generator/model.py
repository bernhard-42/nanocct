"""Intermediate representation of what gets bound."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class ResultKind(StrEnum):
    """How a method's result is handed to Python (parse._result_kind, emit._method); Runtime.md 5.2 and Binding-Rules.md."""
    VALUE = "value"                    # copied (nanobind default), also void
    VALUE_TRANSIENT = "value_transient"  # T by value with T Transient: moved into handle<T>(new T(...)), like a constructor
    PTR_TRANSIENT = "ptr_transient"    # T* with T Transient: wrapped in a handle<T>, never owned by nanobind
    REF_TRANSIENT = "ref_transient"    # T& with T Transient: same
    PTR_CLASS = "ptr_class"            # T* other class: rv_policy::reference_internal (reference for a static method or free function)
    REF_MUTABLE = "ref_mutable"        # T& (mutable) other class: rv_policy::reference_internal (ChangeXxx accessors)
    REF_PRIMITIVE = "ref_primitive"    # double& Value(i): getter + Set<Name>/__setitem__ Python additions
    OTHER = "other"


class StreamKind(StrEnum):
    """A std::ostream& / std::istream& parameter (Binding-Rules.md)."""
    NONE = ""
    OUT = "out"      # std::ostream&: dropped from the signature, the written text is returned as a str
    IN = "in"        # std::istream& / Standard_SStream&: a text file-like object (typing.TextIO, nanocct::TextInput), never a str


class ConversionKind(StrEnum):
    """operator T() const (Binding-Rules.md): a Python dunder for a scalar target, a constructor of T from this class otherwise."""
    BOOL = "bool"
    INT = "int"
    FLOAT = "float"
    CLASS = "class"
    HANDLE = "handle"


@dataclass
class Param:
    name: str
    type: str            # C++ spelling as written (typedefs resolved to canonical where safe)
    default: str | None  # C++ expression or None
    is_out: bool         # non-const lvalue ref to a primitive or to a handle<T> -> returned in a tuple
    is_inout: bool = False  # ... and also taken as input (overrides.toml [inout])
    class_name: str = ""    # canonical name of the class/enum type behind the parameter ("" for scalars, strings, std types)
    is_handle: bool = False # opencascade::handle<T> (by value or reference): nb::arg(...).none(), a null handle is None
    stream: StreamKind = StreamKind.NONE
    binary: bool = False    # the stream carries a binary format (overrides.toml [stream] binary_packages): bytes / typing.BinaryIO instead of str / typing.TextIO
    out_py: str = ""        # Python type name of a removed out-parameter (float, int, bool, str, an enum or class name): the R-COLLISION suffix
    omitted: bool = False   # R-OPTIONAL-PTR: a pointer parameter with a null default, dropped from the signature; the callee gets nullptr
    cstr_none: bool = False # R-CSTR-NULL: a const char* parameter with a null default: `str | None = None` (nanocct::OptionalCString caster)
    ptr_none: bool = False  # R-PTR-NULL: a class pointer parameter takes None (nb::arg(...).none()), `= None` with a null default
    instance_key: str = ""     # R-UNBOUND-TYPE: the NCollection binder instantiation behind the type (parse._binder_key), "" if none
    class_ancestors: tuple[str, ...] = ()   # R-OVERLOAD-ORDER: every base of class_name, spelled like class_name (parse._class_ancestors)
    kept: bool = False      # R-CTOR-KEEP / R-METHOD-KEEP: a parameter the object can keep the address of: keep_alive / keep_slot
    kept_view: bool = False # R-COPY: kept because the object may hold pointers copied out of it (a copy, TDF_ChildIterator(label)):
                            # it keeps what the argument's slots hold now too (nanocct::keep_view_arg)
    is_enum: bool = False   # R-ENUM-ARG: an enum or std::optional<enum> by value or reference: nb::arg(...).noconvert(), no int in its place
    array_len: int = 0      # R-FIXED-ARRAY: a C array T[N] / T (&)[N] of this length; `type` is the element type; is_out when non-const
    is_bytes: bool = False  # R-BYTES: a `const uint8_t*` input buffer, taken as `bytes`; the length parameter that follows it is dropped
    bytes_of: str = ""      # R-BYTES: this parameter is that buffer's length and is dropped; the value is the bytes parameter's name
    seq_owner: str = ""     # R-ARRAY-PTR: a `const T*` array of a listed member, taken as a sequence of T: the elements are copied
                            # into memory of this C++ object's Allocator() (overrides.toml [array]) and the copy is passed
    seq_of: str = ""        # R-ARRAY-PTR: this parameter is that array's count and is dropped; the value is the sequence parameter's name
    out_view: bool = False  # R-RESULT-KEEP: a non-const reference/pointer to a class holding pointers, which the call writes into:
    out_keeps: tuple[int, ...] = ()  # ... it keeps self (a method) and these parameters (indices) alive
    owned: bool = False     # R-OWNER: an argument written into, or a returned out-handle, of a type whose OCAF owners are known
    guarded: bool = False   # R-VIEW-GUARD: a non-const reference/pointer to an NCollection container: the call may change it, so it
                            # refuses (BufferError) while the container has live views (nanocct::guarded, nanocct_common.h)
    container: bool = False # R-VIEW-GUARD: a reference/pointer to an NCollection container, any constness: an iterator class (R-ITER)
                            # constructed or initialised from it is an iterator view of it
    kept_cpp: bool = False  # R-KEPT: a kept argument of a Transient that cannot own the object (parse._cycle_path): the C++ object
                            # of a nanocct::Kept<T> keeps it; one that can stays kept by the Python object (a cycle no GC sees)


@dataclass
class Method:
    name: str
    params: list[Param]
    result: str                 # C++ return type spelling, "void" if none
    result_kind: ResultKind
    result_class: str           # for ptr_/ref_ kinds: the pointee class name
    is_static: bool
    is_const: bool
    is_noexcept: bool
    doc: str
    is_operator: bool = False
    skip_reason: str | None = None
    defined_in_header: bool = False   # inline definition seen in the TU (no library symbol needed)
    mangled: str = ""                # linker symbol (libclang mangling); R-UNDEFINED compares it with nm's list
    result_class_name: str = ""       # canonical class/enum behind the result ("" for void, scalars, strings), see parse._class_behind
    result_instance_key: str = ""     # R-UNBOUND-TYPE: the NCollection binder instantiation behind the result (parse._binder_key)
    is_deprecated: bool = False       # Standard_DEPRECATED: bound, the message leads the docstring
    suffix: str = ""                  # R-COLLISION: "__float__float" appended to the Python name when overloads collide after out-param removal
    via_using: str = ""               # R-USING: the base class whose member a `using Base::name;` re-exports on this class
    force_lambda: bool = False        # bound through a lambda even without out-parameters (R-PTR-REF: a T*& result returned as T*)
    result_view: bool = False         # R-RESULT-KEEP: a class by value/const& whose layout holds pointers: keeps self and result_keeps
    result_keeps: tuple[int, ...] = ()  # ... the parameters (indices) whose objects it may point into
    result_keeps_producer: bool = False   # R-ALLOCATOR: a Transient/handle result of a class holding an allocator keeps self
    result_owned: bool = False        # R-OWNER: the result's type has known OCAF owners (TDF_Label, TDF_Attribute, ...): kept instead
    result_by_reference: bool = False # R-COPY: a `const T&` of an owner class (its copy would free what the original points to): by reference
    result_on_heap: bool = False      # R-COPY: a `T` by value of an owner class without its own move/copy constructor: new T(call)
    result_container: bool = False    # R-VIEW-GUARD: a non-const reference/pointer to an NCollection container the object owns:
                                      # its own changes to it are not checked against the container's views (reported)


@dataclass
class Constructor:
    params: list[Param]
    doc: str
    skip_reason: str | None = None
    is_implicit: bool = False     # non-explicit converting constructor -> nb::implicitly_convertible
    is_copy: bool = False
    defined_in_header: bool = False
    mangled: str = ""


@dataclass
class Conversion:
    """operator T() const: a Python dunder for bool/int/float, a constructor of T from this class for class/handle."""
    kind: ConversionKind
    target: str                 # C++ spelling of T (the pointee for handle)
    target_class: str           # canonical class/enum name of T, "" for scalars
    is_explicit: bool
    doc: str
    # operator T() is usually const, but not always (MeshVS_Buffer::operator double&()/int&()): a scalar dunder's
    # lambda must then take a non-const self, or the static_cast does not compile (R-CONV-SCALAR)
    is_const: bool = True


@dataclass
class Field:
    name: str
    type: str
    is_const: bool
    doc: str
    array_len: int = 0          # R-FIXED-ARRAY: a C array member T[N]; `type` is the element type; a list property
    is_bitfield: bool = False   # R-FIELD: a bit-field (`unsigned stick : 1`) has no pointer-to-member; a property through lambdas
    is_pointer: bool = False    # R-FIELD: a raw pointer (a class or `const char*`): read-only, the getter returns a copy of the pointee
    is_container: bool = False  # R-VIEW-GUARD: an NCollection container held by value: assigning it refuses while it has live views


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
    aliases: list[str] = field(default_factory=list)   # R-ENUM: py names of enumerators repeating an earlier value (Font_FA_Bold = Font_FontAspect_Bold)


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
    after_templates: bool = False     # 7a: a base is a binder instantiation's nested Iterator -> declared in the templates phase, after it
    has_declared_ctor: bool = False   # any constructor at any access level (suppresses the implicit default ctor)
    template_key: str = ""            # for an instantiation bound under an alias: canonical key (dedupe across packages)
    constructible: bool = True        # False when operator new is not public (placement new impossible),
                                      # or when overrides.toml [skip] constructors lists the class
    not_constructible_reason: str = ""   # what to report; "" means the operator new case
    unbindable: bool = False          # nb::class_ cannot be instantiated (member of incomplete type); reported, not bound
    noncopyable: bool = False         # bound through a wrapper struct with deleted copy/move (overrides.toml [skip] noncopyable)
    view: bool = False                # R-COPY, R-CTOR-KEEP: its layout holds pointers, so a copy (sharing them) keeps the original alive
    copy_owner: str = ""              # R-COPY: where a destructor may free a pointer an implicit copy duplicates: no implicit copy
    dtor_mangled: str = ""            # a user-declared, not-inline destructor's linker symbol; "" when there is none to link
                                      # (implicit or defined in the header). R-UNDEFINED checks it: nanobind instantiates
                                      # wrap_destruct<T> for every bound class, so an unexported ~T() is a link error
    kept: bool = False                # R-KEPT: the bindings construct it as nanocct::Kept<T> (decided by the driver over all packages:
                                      # its bound constructors or methods, or a bound base's, keep an argument with kept_cpp)
    kept_blocker: str = ""            # R-KEPT: why nanocct::Kept<T> cannot be derived from it ("" if it can): final, a private
                                      # destructor, a final Delete(), a multiple-inheritance H-collection
    virtual_symbols: list[str] = field(default_factory=list)   # R-KEPT: the linker symbols of its virtual functions that the
                                      # headers do not define (the final overriders); Kept<T>'s own vtable names each of them

    @property
    def bound_type(self) -> str:
        """The C++ type nb::class_ is instantiated with: the class itself, or its non-copyable wrapper."""
        return f"nanocct_wrap_{self.py_name}" if self.noncopyable else self.name
    ctors: list[Constructor] = field(default_factory=list)
    methods: list[Method] = field(default_factory=list)
    fields: list[Field] = field(default_factory=list)
    statics: list[Constant] = field(default_factory=list)      # R-STATIC-DATA: public static const data members -> read-only static properties
    conversions: list[Conversion] = field(default_factory=list)
    enums: list[Enum] = field(default_factory=list)
    nested: list[Class] = field(default_factory=list)  # public nested classes (flattened into PackageIR.classes by the parser)
    skipped: list[str] = field(default_factory=list)   # human readable report lines
    friend_ops: list["Function"] = field(default_factory=list)   # R-FREE-OP: hidden-friend operators declared in the class body


@dataclass
class Function:
    name: str
    params: list[Param]
    result: str
    result_kind: ResultKind
    result_class: str
    is_noexcept: bool
    doc: str
    header: str
    is_operator: bool = False
    skip_reason: str | None = None
    qualified: str = ""         # C++ name to call (Ns::Name for a function in a namespace); "" -> name
    scope: tuple[str, ...] = () # Python attribute path of the enclosing C++ namespace, relative to the package module
    suffix: str = ""            # R-COLLISION, as for methods
    defined_in_header: bool = False   # inline definition seen in the TU (no library symbol needed)
    mangled: str = ""                 # linker symbol; R-UNDEFINED compares it with nm's list (FUN_scanloi in TopOpeBRepDS)
    result_class_name: str = ""       # canonical class/enum behind the result, as for methods (R-UNBOUND-TYPE)
    result_instance_key: str = ""     # as for methods
    result_view: bool = False         # R-RESULT-KEEP, R-OWNER: as for methods
    result_keeps: tuple[int, ...] = ()
    result_owned: bool = False
    result_by_reference: bool = False # R-COPY: as for methods
    result_on_heap: bool = False


@dataclass
class Constant:
    py_name: str
    cpp: str                    # fully qualified C++ expression
    doc: str
    scope: tuple[str, ...] = ()
    type_class: str = ""        # the class/enum behind the value's type, for R-UNBOUND-TYPE ("" for a scalar); class statics only
    mangled: str = ""           # class statics: the linker symbol, for R-UNDEFINED when the value is not in the header
    value_in_header: bool = True  # class statics: an in-class initialiser or constexpr -- read as a constant, no symbol needed


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
    owned_args: set[str] = field(default_factory=set)   # R-OWNER: instance arguments with known OCAF owners (TDF_Label, handle<TDF_Attribute>)
    copy_owner_instances: dict[str, str] = field(default_factory=dict)   # R-COPY: binder instantiations whose elements are owners -> where
    report: list[str] = field(default_factory=list)
