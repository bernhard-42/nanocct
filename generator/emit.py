"""IR -> nanobind C++ source."""
from __future__ import annotations

from collections.abc import Callable

import re
import shutil
from pathlib import Path

from .model import Class, Constructor, ConversionKind, Enum, Function, Method, PackageIR, Param, ResultKind, StreamKind, TemplateInstance
from .ncollection import BINDERS
from .parse import NOT_VALUE_COPY, VIEW_CLASSES, _py_identifier, py_path, py_safe

# C++ operator -> (binary python name, unary python name, reflected python name)
_BINARY_OPS = {
    "operator+": ("__add__", "__pos__", "__radd__"),
    "operator-": ("__sub__", "__neg__", "__rsub__"),
    "operator*": ("__mul__", None, "__rmul__"),
    "operator/": ("__truediv__", None, "__rtruediv__"),
    "operator%": ("__mod__", None, "__rmod__"),
    "operator^": ("__xor__", None, "__rxor__"),
    "operator&": ("__and__", None, "__rand__"),
    "operator|": ("__or__", None, "__ror__"),
    "operator==": ("__eq__", None, None),
    "operator!=": ("__ne__", None, None),
    "operator<": ("__lt__", None, None),
    "operator<=": ("__le__", None, None),
    "operator>": ("__gt__", None, None),
    "operator>=": ("__ge__", None, None),
    "operator()": ("__call__", "__call__", None),
    "operator[]": ("__getitem__", None, None),
    # no operator!: Python has no protocol `not` would call -- `not x` asks __bool__ (R-OPERATOR)
}
_INPLACE_OPS = {
    "operator+=": "__iadd__", "operator-=": "__isub__", "operator*=": "__imul__",
    "operator/=": "__itruediv__", "operator%=": "__imod__", "operator^=": "__ixor__",
    "operator&=": "__iand__", "operator|=": "__ior__",
}
_IDENT_RE = re.compile(r"[A-Za-z_]\w*")


# Binding-Rules.md R-DOCSTRING: the docstring as a raw string literal (R"nbdoc(...)nbdoc")
def _cpp_doc(doc: str) -> str | None:
    if doc == "":
        return None
    assert ")nbdoc\"" not in doc
    return f'R"nbdoc({doc})nbdoc"'


def _strip_ref(t: str) -> str:
    """'double &' -> 'double'; 'const int &' -> 'int' (for out-param locals)."""
    s = t.replace("&", "").strip()
    if s.startswith("const "):
        s = s[len("const "):]
    return s


# Binding-Rules.md R-OPERATOR, R-IOP, R-STR
def _py_name(m: Method) -> str | None:
    """Python attribute name for a method; None when the operator has no Python counterpart."""
    if not m.is_operator:
        # R-BASELINE: a method keeps its C++ name (the deviations: R-KEYWORD, R-STATIC-S, R-COLLISION, the operators)
        return py_safe(m.name)
    if m.name == "operator<<" and len(m.params) == 1 and not m.params[0].binary:
        # R-STR, member forms: `Standard_OStream& operator<<(Standard_OStream&)`, const or not, prints *this (TDF_Label,
        # TDF_Attribute: `{ return Dump(anOS); }`; CDM_MetaData, not const: `return Print(anOStream);` in the .cxx)
        # -> __str__; `VrmlData_Scene& operator<<(Standard_IStream&)` reads a scene -> Read(TextIO), a named method,
        # because __lshift__ would read as a bit shift
        if m.params[0].stream == StreamKind.OUT:
            return "__str__"
        if m.params[0].stream == StreamKind.IN:
            return "Read"
    if m.name in _INPLACE_OPS:
        return _INPLACE_OPS[m.name]
    entry = _BINARY_OPS.get(m.name)
    if entry is None:
        return None
    binary, unary, _ = entry
    if len(m.params) == 0:
        return unary
    if len(m.params) == 1 or m.name == "operator()":
        return binary
    return None



def _names_not_value_copy(result: str) -> bool:
    """R-RESULT: does a result type name a class of overrides.toml [not_value_copy], itself or as a container's element
    (`const NCollection_Sequence<IntTools_CommonPrt> &`)? Such a copy is a different object, so it is not copied."""
    return any(re.search(rf"\b{re.escape(c)}\b", result) is not None for c in NOT_VALUE_COPY)

class Emitter:
    def __init__(self, ir: PackageIR, include_dir: Path, known_classes: dict[str, str], toolkit_of: dict[str, str],
                 known_templates: dict[str, dict], toolkit_order: list[str] | None = None, paths: dict[str, str] | None = None,
                 prelude_check: Callable[[list[str]], list[str]] | None = None, bases_of: dict[str, list[str]] | None = None,
                 kept: set[str] | None = None):
        self.ir = ir
        self.kept = kept if kept is not None else set()   # R-KEPT: every class the bindings construct as nanocct::Kept<T> (manifest "kept")
        self._self = ""                                   # R-KEPT: the bound type of the class being defined (keep_slot's Self)
        self.bases_of = bases_of if bases_of is not None else {}   # R-OVERLOAD-ORDER: every bound class -> its direct bases (manifest "bases")
        self._ancestor_cache: dict[tuple[str, tuple[str, ...]], set[str]] = {}
        self.prelude_check = prelude_check    # R-PRELUDE for the emitted include list (parse.include_prelude); None in unit tests
        self.paths = paths if paths is not None else {}    # manifest "paths": C++ class -> Python path exceptions
        self.toolkit_order = toolkit_order if toolkit_order is not None else []   # generated toolkits, dependencies first
        self.include_dir = include_dir
        self.known = known_classes            # C++ class name -> package, for everything bound (previous runs + this run)
        self.toolkit_of = toolkit_of          # package -> toolkit
        self.templates = known_templates      # canonical instance key -> {toolkit, package, name}; updated while emitting
        self.local = {c.name for c in ir.classes}
        self._class_named = {c.name: c for c in ir.classes}   # R-STR: the class a free print operator belongs to
        self.report: list[str] = []
        self.includes: list[str] = []         # OCCT headers the emitted file includes; the caller derives the link libraries (R-LINK)
        self.needs_views = False              # R-VIEW: this package binds a class from overrides.toml [views]
        self.skipped: set[str] = set()        # classes of this package not bound after all (base/outer not bound); the caller drops them from the manifest
        self.slots = 0                         # R-METHOD-KEEP: the slots of this file (one per kept method parameter)
        self._iterating = False                # R-VIEW-GUARD: the class being defined is an iterator class (R-ITER)
        self.needs_ocaf = False               # R-OWNER: this file applies nanocct::owners to an OCAF type (nanocct_ocaf.h)
        # R-UNHASHABLE: classes whose bound __eq__ compares against their own type, filled while free operators are
        # mapped (the member ones are found in _define_class). A free operator== against something else -- the
        # NCollection_ForwardRangeIterator/Sentinel pair -- is not value equality and must not land here.
        self.value_eq: set[str] = set()
        # PARALLEL EMIT (2026-09-24): ownership of a 6c instantiation is normally decided *by* emitting -- the first
        # package to need it claims it ("if key in self.templates: return"). That makes the emit loop order-dependent
        # and unparallelisable. plan() runs exactly the part of emit() that decides ownership, so the driver can run it
        # over every package in emit order first; with preassigned=True the registry then already carries the owner in
        # its "by" field and each package decides alone: emit the ones assigned to it, skip the rest.
        # _emitted_instances keeps a package from emitting the same key twice, which the old first-come guard did implicitly.
        self.preassigned = False
        self._emitted_instances: set[str] = set()
        self._idents: set[str] = set()
        self._wrapped = {c.name for c in ir.classes if c.noncopyable}   # R-UNBOUND-TYPE: registered under the wrapper's typeid
        self._local_types = self.local | {e.name for e in ir.enums} | {e.name for c in ir.classes for e in c.enums}   # bound here
        self._template_names = {k.split("<")[0] for k in known_templates} | set(BINDERS) | {  # R-UNBOUND-TYPE: not judged
            src for info in BINDERS.values() for src in info.get("nested_from", {}).values()} | {
            c.name.split("<")[0] for c in ir.classes if c.template_key != ""}

    def _owns(self, key: str) -> bool:
        """Should this package emit the instantiation `key`? (with a preassigned registry: only if it is the owner)"""
        if key in self._emitted_instances:
            return False
        entry = self.templates.get(key)
        if entry is None:
            return True
        if self.preassigned:
            return entry.get("by") == self.ir.name
        return False

    def _claim_template(self, c: Class) -> dict | None:
        """6c: an un-aliased instantiation is bound by the first package that declares it; every later package aliases
        the owner's class instead. Returns the owner's registry entry when this package has to alias, None when it owns
        the class itself. The declare phase calls it to emit the alias; plan() calls it for the decision alone."""
        found = self.templates.get(c.template_key)
        if found is not None and found.get("by") != self.ir.name and not found.get("skipped", False):
            return found
        self.templates[c.template_key] = {"toolkit": self.toolkit_of[self.ir.name], "package": self.ir.name,
                                          "name": c.py_name, "by": self.ir.name}
        return None

    # ---- helpers -------------------------------------------------------------------------------
    @staticmethod
    def _attr(scope: tuple[str, ...]) -> str:
        """Expression for the Python object at a scope path below the package module m (a namespace submodule
        or an enclosing class): nb::class_/nb::enum_ take it as the scope handle."""
        return "m" + "".join(f'.attr("{s}")' for s in scope)

    @staticmethod
    def _module(scope: tuple[str, ...]) -> str:
        """Same as _attr for a namespace scope, typed as nb::module_ (for .def / def_submodule)."""
        if len(scope) == 0:
            return "m"
        return f'nb::borrow<nb::module_>({Emitter._attr(scope)})'

    def _note_types(self, *texts: str) -> None:
        for t in texts:
            for ident in _IDENT_RE.findall(t):
                self._idents.add(ident)

    # Binding-Rules.md R-DEFAULT-UNBOUND
    def _unbound_default(self, params: list[Param]) -> str | None:
        """The type of a defaulted parameter that no binding knows: nanobind converts defaults to Python objects at
        .def time, so such a member would abort the module import (nb::cast -> std::bad_cast)."""
        for p in params:
            if p.default is None or p.class_name == "" or p.default in ("nullptr", "NULL", "0") and "*" in p.type:
                continue                           # a null pointer casts to None without looking the type up
            if p.class_name in self.known or p.class_name in self.templates:
                continue
            return p.class_name
        return None

    # Binding-Rules.md R-UNBOUND-TYPE
    def _unbound_reason(self, name: str) -> str | None:
        """Why the class/enum `name` has no nanobind registration a signature could use, or None when it has one.
        Besides "bound nowhere": a Standard_Failure descendant is a Python exception type, not a value type, and a
        class bound through its R-NONCOPYABLE wrapper is registered under the wrapper's typeid only."""
        if name == "" or "<" in name or name.split("::")[0] in self._template_names:
            # a template instantiation (or a class nested in one) is spelled here without its default arguments
            # (math_VectorBase<>, NCollection_FlatDataMap<K, V>) or bound under another name (NCollection_TListIterator<T> is
            # the List binder's Iterator), so `known`/`templates` cannot answer for it: not judged, the binding stays
            return None
        if name in self.skipped:
            return "is not bound (its class is skipped)"
        if name in self._wrapped:
            return "is not bound (only its non-copyable wrapper is)"
        if name == "Standard_Failure" or "Standard_Failure" in self._ancestors_of(name):
            return "is not bound as a value (a Python exception type)"
        if name in self.templates:
            return None if not self.templates[name].get("skipped", False) else "is not bound (instantiation skipped)"
        return None if name in self.known or name in self._local_types else "is not bound"

    def _skip_unbound(self, members: list) -> list[tuple[object, str]]:
        """R-UNBOUND-TYPE: a member whose parameter or result is a class no binding registers cannot be called (no Python
        object of the type exists) or fails on every non-null result (nanobind: "Unable to convert function return value");
        OSD_OpenFile even opened the file first. Such a member is not bound. Sets skip_reason; returns (member, message)."""
        skipped: list[tuple[object, str]] = []
        for m in members:
            if m.skip_reason is not None:
                continue
            names = [p.class_name for p in m.params if not p.omitted and p.bytes_of == ""] + [getattr(m, "result_class_name", "")]
            keys = [p.instance_key for p in m.params if not p.omitted and p.bytes_of == ""] + [getattr(m, "result_instance_key", "")]
            found = next(((n, w) for n in names if (w := self._unbound_reason(n)) is not None), None) \
                or next(((k, w) for k in keys if (w := self._unbound_instance_reason(k)) is not None), None)
            if found is not None:
                m.skip_reason = f"type {found[0]} {found[1]}"
                skipped.append((m, m.skip_reason))
        return skipped

    # the binder kinds with a nested Iterator class (6a); every other class nested in a binder instantiation is never bound
    _KINDS_WITH_ITERATOR = {"NCollection_List", "NCollection_Sequence", "NCollection_Map", "NCollection_DataMap",
                            "NCollection_IndexedMap", "NCollection_IndexedDataMap", "NCollection_DoubleMap"}

    def _unbound_instance_reason(self, key: str) -> str | None:
        """R-UNBOUND-TYPE for an NCollection binder instantiation, by its registry key (parse._binder_key: the key
        _note_instance records, so no spelling comparison is involved): unbound when the registry has no such
        instantiation (its element type is unsupported: a raw pointer, NCollection_IndexedMap<Graphic3d_CStructure *>)
        or skipped it, and for a nested class other than a kind's Iterator (DynamicArray<T>::DynamicIterator)."""
        if key == "":
            return None
        base, _, nested = key.rpartition(">::") if ">::" in key else (key, "", "")
        base = base + ">" if nested != "" else base
        entry = self.templates.get(base)
        if entry is None:
            return "is not bound (no binder instantiation)"
        if entry.get("skipped", False):
            return "is not bound (instantiation skipped)"
        if nested != "" and (nested != "Iterator" or base.split("<")[0] not in self._KINDS_WITH_ITERATOR):
            return f"is not bound (the binders bind no {nested} class)"
        return None

    def _ancestors_of(self, name: str) -> set[str]:
        found: set[str] = set()
        todo = [name]
        while len(todo) > 0:
            for b in self.bases_of.get(todo.pop(), []):
                if b not in found:
                    found.add(b)
                    todo.append(b)
        return found

    def _ancestors(self, p: Param) -> set[str]:
        """R-OVERLOAD-ORDER: every base of the class behind a parameter -- what the package's parse saw
        (parse._class_ancestors: template bases, NCollection_Array2<T> : NCollection_Array1<T>) closed over the bases of
        every bound class (a package that only forward-declares Geom_BSplineCurve cannot see its bases itself)."""
        key = (p.class_name, p.class_ancestors)
        if key not in self._ancestor_cache:
            found: set[str] = set()
            todo = [p.class_name, *p.class_ancestors]
            while len(todo) > 0:
                for b in self.bases_of.get(todo.pop(), []):
                    if b not in found:
                        found.add(b)
                        todo.append(b)
            self._ancestor_cache[key] = found | set(p.class_ancestors)
        return self._ancestor_cache[key]

    def _args(self, params: list[Param], skip_out: bool) -> str:
        parts: list[str] = []
        for p in params:
            if p.omitted or p.bytes_of != "" or skip_out and (p.is_out and not p.is_inout or p.stream == StreamKind.OUT):
                continue
            # R-HANDLE: a handle<T> parameter accepts None (a null handle); without .none() nanobind rejects None before
            # the caster runs (Design.md 4.2); so does a class pointer, with or without a null default (R-PTR-NULL: without
            # .none() a null default is refused)
            arg = f'nb::arg("{p.name}").none()' if p.is_handle or p.ptr_none else f'nb::arg("{p.name}")'
            # R-ENUM-ARG: an enum parameter takes its enumerators only, as in C++. nanobind's enum caster takes any int
            # that is an enumerator's value in its convert pass, True and False included (nb_enum.cpp), so
            # BRepGraph_ChildExplorer(g, root, Kind.Edge, True, False) reached (AvoidKind, EmitAvoidKind, TraversalMode)
            # registered before C++'s choice (TargetKind, CumLoc, CumOri)
            if p.is_enum:
                arg += ".noconvert()"
            if p.cstr_none:                    # R-CSTR-NULL: None reaches the OptionalCString caster only with .none()
                parts.append(f'nb::arg("{p.name}").none() = nb::none()')
            elif p.default is None:
                parts.append(arg)
            else:
                # cast to the parameter's value type: a `char` default written as 0 must become a
                # 1-character str, an enum default written as an int must become the enum, etc. A braced default
                # (`= {}`: XSAlgo_ShapeProcessor's DE_ShapeFixParameters, the ParameterMap of SetShapeFixParameters)
                # is list-initialised instead -- static_cast from a braced-init-list is not C++ (R-DEFAULT, 2026-09-22).
                if p.default.startswith("{"):
                    parts.append(f'{arg} = std::decay_t<{p.type}>{p.default}')
                else:
                    parts.append(f'{arg} = static_cast<std::decay_t<{p.type}>>({p.default})')
                self._note_types(p.default)
        return "".join(", " + s for s in parts)

    def _extras(self, doc: str, params: list[Param], skip_out: bool, operator: bool) -> str:
        s = self._args(params, skip_out)
        d = _cpp_doc(doc)
        if d is not None:
            s += ", " + d
        if operator:
            s += ", nb::is_operator()"           # R-OPERATOR
        return s

    # Binding-Rules.md R-KEPT
    def _new_type(self, cls_name: str) -> str:
        """What `new` constructs for a Transient the bindings create: nanocct::Kept<T> for a class whose bindings keep arguments."""
        return f"nanocct::Kept<{cls_name}>" if cls_name in self.kept else cls_name

    # Binding-Rules.md R-METHOD-KEEP
    def _keep_slots(self, m: Method) -> str:
        """One nanocct::keep_slot call policy per method parameter the object can keep the address of: the argument's
        Python position (1 is self) counts the parameters the signature shows, as _args does with skip_out."""
        if m.is_static:
            return ""
        out, position = "", 1
        for p in m.params:
            if p.omitted or p.bytes_of != "" or (p.is_out and not p.is_inout) or p.stream == StreamKind.OUT:
                continue
            position += 1
            if p.kept and p.kept_cpp:      # R-KEPT: on the C++ object of a Kept<T>
                out += f", nb::call_policy<nanocct::keep_slot<nanocct_slots, {position}, {self.slots}, {self._self}, true>>()"
                self.slots += 1
            elif p.kept:
                out += f", nb::call_policy<nanocct::keep_slot<nanocct_slots, {position}, {self.slots}>>()"
                self.slots += 1
        return out

    # Binding-Rules.md R-VIEW-GUARD
    def _report_owned_container(self, cls: Class, m: Method) -> None:
        """The residual: a container the object owns, handed out by reference. Its views are checked against the
        container's own members and every bound call taking it, not against what its owner does to it in C++."""
        if m.result_container:
            self.report.append(f"{cls.name}::{m.name}({self._sig(m.params)}): returns {m.result}, a container the object owns -- "
                               f"its own changes to it are not checked against the container's views (R-VIEW-GUARD)")

    def _iterator_views(self, params: list[Param], positions: dict[int, int], self_pos: int) -> str:
        """An iterator class (R-ITER: More/Next/Value) constructed or initialised from a container iterates it -- an iterator
        view of each container argument (nanocct::view_of; over-counting one it only copies is the safe side). self_pos: the
        object's position as in nb::keep_alive (1 = self, 0 = the result of nb::new_)."""
        if not self._iterating:
            return ""
        return "".join(f", nb::call_policy<nanocct::view_of<nanocct::view_kind::iterator, {self_pos}, {positions[i]}>>()"
                       for i, p in enumerate(params) if p.container and i in positions)

    def _iterator_init(self, m: Method) -> str:
        """R-VIEW-GUARD: Init/Initialize of an iterator class re-targets it (OCCT's iterator protocol, as More/Next/Value)."""
        if m.is_static or m.name not in ("Init", "Initialize"):
            return ""
        return self._iterator_views(m.params, self._positions(m, True), 1)

    @staticmethod
    def _guarded(fn: str, params: list[Param]) -> str:
        """A directly bound function taking a container it may change goes through nanocct::guarded: same signature, the
        check runs after nanobind converted the arguments (a call policy's precall runs before, and raised for the wrong
        overload). The positions are the C++ parameters', which a direct binding shows all of."""
        positions = [str(i) for i, p in enumerate(params) if p.guarded]
        if len(positions) == 0:
            return fn
        return f"&nanocct::guarded<{fn}, {', '.join(positions)}>::call"

    @staticmethod
    def _guard_checks(params: list[Param]) -> list[str]:
        """The same check as the first statements of a lambda: each container parameter it may change, by name, with its
        position among the parameters Python passes (self not counted) for the message."""
        out, position = [], 0
        for p in params:
            if p.omitted or p.bytes_of != "" or (p.is_out and not p.is_inout) or p.stream == StreamKind.OUT:
                continue
            position += 1
            if p.guarded:
                out.append(f"nanocct::refuse_viewed_argument({p.name}, {position});")
        return out

    @staticmethod
    def _positions(m: Method | Function, method: bool) -> dict[int, int]:
        """Python position of each parameter the signature shows (1 is self for a method), as _keep_slots counts them."""
        out, position = {}, 1 if method else 0
        for i, p in enumerate(m.params):
            if p.omitted or p.bytes_of != "" or (p.is_out and not p.is_inout) or p.stream == StreamKind.OUT:
                continue
            position += 1
            out[i] = position
        return out

    # Binding-Rules.md R-RESULT-KEEP, R-OWNER
    def _keep_views(self, m: Method | Function, method: bool) -> str:
        """nanocct::keep_view call policies: a result, an argument the call writes into, or a returned out-handle of a class
        that holds pointers keeps the objects it may point into (self for a method, and the parameters the parser found);
        one whose OCAF owners are known keeps those instead. method: a non-static member function (self is argument 1)."""
        positions = self._positions(m, method)
        outs = [p for p in m.params if p.is_out]
        n_results = (0 if m.result == "void" else 1) + len(outs) + sum(1 for p in m.params if p.stream == StreamKind.OUT)
        out = ""

        def policy(cpp_type: str, owned: bool, nurse: int, elem: int, patients: list[int]) -> str:
            if owned:
                self.needs_ocaf = True
            return (f", nb::call_policy<nanocct::keep_view<{cpp_type}, {'true' if owned else 'false'}, {nurse}, {elem}"
                    f"{''.join(f', {k}' for k in patients)}>>()")

        # a `const T&` of a class whose copy drops state comes back by reference (R-RESULT, [not_value_copy]): it may be an object
        # Python already has, which must not collect producers -- it could be one of them (keep_view decides the same at
        # compile time for a class that cannot be copied at all)
        by_reference = m.result.rstrip().endswith("&") and (_names_not_value_copy(m.result) or m.result_by_reference)
        if m.result != "void" and (m.result_owned or m.result_view and not by_reference):
            patients = [] if m.result_owned else ([1] if method else []) + [positions[i] for i in m.result_keeps if i in positions]
            if m.result_owned or len(patients) > 0:
                out += policy(m.result, m.result_owned, 0, 0 if n_results > 1 else -1, patients)
        for i, p in enumerate(m.params):
            if i in positions and (p.out_view or (p.owned and not p.is_out)):
                patients = [] if p.owned else [k for k in ([1] if method else []) + [positions[j] for j in p.out_keeps if j in positions]
                                                if k != positions[i]]
                if p.owned or len(patients) > 0:
                    out += policy(p.type, p.owned, positions[i], -1, patients)
            elif p.is_out and p.owned:
                elem = (0 if m.result == "void" else 1) + outs.index(p)
                out += policy(p.type, True, 0, elem if n_results > 1 else -1, [])
        return out

    def _sig(self, params: list[Param]) -> str:
        return ", ".join(f"{p.type}[{p.array_len}]" if p.array_len > 0 else p.type for p in params)

    # ---- members -------------------------------------------------------------------------------
    # Binding-Rules.md R-OUT, R-OUT-HANDLE, R-INOUT, R-STREAM-OUT, R-STREAM-IN, R-RESULT
    def _lambda_call(self, cls: str | None, m: Method, self_type: str | None = None) -> str:
        """Lambda that maps out-params to a returned tuple (also handles static methods). self_type: the bound
        type when it differs from cls (non-copyable wrapper)."""
        ins = [p for p in m.params if (not p.is_out or p.is_inout) and p.stream != StreamKind.OUT
               and not p.omitted and p.bytes_of == ""]
        outs = [p for p in m.params if p.is_out]
        lam_params: list[str] = []
        if cls is not None and not m.is_static:
            lam_params.append(f"{'const ' if m.is_const else ''}{self_type if self_type is not None else cls} &self")
        lam_params += [f"const nb::bytes &{p.name}" if p.is_bytes                                    # R-BYTES
                       else f"const nanocct::{'BinaryInput' if p.binary else 'TextInput'} &{p.name}" if p.stream == StreamKind.IN
                       else f"nanocct::OptionalCString {p.name}" if p.cstr_none                              # R-CSTR-NULL: str or None
                       else f"const std::array<{p.type}, {p.array_len}> &{p.name}" if p.array_len > 0     # R-FIXED-ARRAY in: a sequence of N
                       else f"{_strip_ref(p.type) if p.is_inout else p.type} {p.name}" for p in ins]
        body: list[str] = self._guard_checks(m.params)          # R-VIEW-GUARD
        body += [f"{p.type} {p.name}[{p.array_len}]{{}};" if p.array_len > 0 else f"{_strip_ref(p.type)} {p.name}{{}};"
                 for p in outs if not p.is_inout]
        # R-FIXED-ARRAY: a const T[N] parameter is copied from the std::array into a C array for the call
        body += [f"{p.type} {p.name}_arr[{p.array_len}]; std::copy({p.name}.begin(), {p.name}.end(), {p.name}_arr);" for p in ins if p.array_len > 0]
        # streams: an ostream& parameter becomes a returned str; an istream&/stringstream parameter takes a text file-like
        # object (nanocct::TextInput caster in nanocct_common.h: typing.TextIO, never a str -- that would collide with the
        # file-path overloads such as BRepTools::Read(shape, path, builder))
        body += [f"std::ostringstream {p.name}_stream;" for p in m.params if p.stream == StreamKind.OUT]
        body += [f"std::stringstream {p.name}_stream({p.name}.{'data' if p.binary else 'text'});" for p in m.params if p.stream == StreamKind.IN]
        call_args = ", ".join(f"(const uint8_t *) {p.name}.c_str()" if p.is_bytes        # R-BYTES: the buffer ...
                              else f"{p.bytes_of}.size()" if p.bytes_of != ""             # ... and its length, from the same object
                              else "nullptr" if p.omitted                                   # R-OPTIONAL-PTR
                              else f"{p.name}.ptr" if p.cstr_none                        # R-CSTR-NULL
                              else f"{p.name}_stream" if p.stream != StreamKind.NONE
                              else f"{p.name}_arr" if p.array_len > 0 and not p.is_out else p.name for p in m.params)
        # R-NULL: the call goes to OCCT as is, here and through a member pointer (_method) -- no null-input guard; OCCT's
        # behaviour on a null argument stays OCCT's
        if cls is None:
            callee = f"{m.name}({call_args})"
        elif m.is_static:
            callee = f"{cls}::{m.name}({call_args})"
        else:
            callee = f"self.{m.name}({call_args})"
        # R-OUT: the C++ return value's temporary is prefixed nanocct_ like every other generated name: 99 OCCT parameters
        # are called `result` (IGESConvGeom::SplineCurveFromIGES(…, handle<Geom_BSplineCurve>& result)), and a bare `result`
        # here would be a redefinition when such a parameter is an out-parameter of a non-void method
        results: list[str] = []
        if m.result_kind == ResultKind.PTR_TRANSIENT:
            body.append(f"opencascade::handle<{m.result_class}> nanocct_result({callee});")
            results.append("nanocct_result")
        elif m.result_kind == ResultKind.REF_TRANSIENT:
            # R-RESULT for `T&` to a Transient: a reference count of 0 means no handle owns the object -- it is a member held by
            # value (BRepAdaptor_Curve::Curve() -> its GeomAdaptor_Curve) or static storage. Wrapping it in a handle as is lets
            # the last Python reference delete memory that was never allocated on its own ("pointer being freed was not
            # allocated", found by build123d's SVG exporter, 2026-09-25). Such an object gets one permanent reference, so no
            # handle can ever delete it; the owner is kept alive by keep_alive<0, 1> (_method). Handle-owned objects are unchanged.
            body.append(f"auto &nanocct_ref = {callee}; "
                        f"if (nanocct_ref.GetRefCount() == 0) const_cast<std::remove_const_t<std::remove_reference_t<decltype(nanocct_ref)>> &>(nanocct_ref).IncrementRefCounter(); "
                        f"opencascade::handle<{m.result_class}> nanocct_result(&nanocct_ref);")
            results.append("nanocct_result")
        elif m.result_kind == ResultKind.VALUE_TRANSIENT:
            # R-RESULT for `T` by value, T Transient: never a nanobind-owned copy (reference count 0, deleted by the first
            # handle it meets); the prvalue initialises a heap object held by a handle, as in every Transient constructor
            body.append(f"opencascade::handle<{m.result_class}> nanocct_result(new {self._new_type(m.result_class)}({callee}));")
            results.append("nanocct_result")
        elif m.result_by_reference and len(outs) == 0 and not any(p.stream == StreamKind.OUT for p in m.params):
            # R-COPY: `auto` would copy the result; the reference goes out as it is (reference_internal, _method)
            body.append(f"return {callee};")
            return f"[]({', '.join(lam_params)}) -> {m.result} {{ {' '.join(body)} }}"
        elif m.result_on_heap:
            # R-COPY: nanobind would move the value into its own object -- for a class without its own move or copy
            # constructor a copy sharing the pointers the temporary's destructor frees; the prvalue initialises the heap
            # object instead (guaranteed copy elision), which Python owns (take_ownership)
            body.append(f"auto *nanocct_result = new std::remove_cv_t<{m.result}>({callee});")
            results.append("nanocct_result")
        elif m.result != "void":
            body.append(f"auto nanocct_result = {callee};")
            results.append("nanocct_result")
        else:
            body.append(f"{callee};")
        for p in outs:
            if p.array_len > 0:                # R-FIXED-ARRAY out: N values back as a list
                body.append(f"std::array<{p.type}, {p.array_len}> {p.name}_out; std::copy(std::begin({p.name}), std::end({p.name}), {p.name}_out.begin());")
        results += [f"{p.name}_out" if p.array_len > 0 else p.name for p in outs]
        results += [f"nanocct_stream_{'bytes' if p.binary else 'text'}({p.name}_stream)" for p in m.params if p.stream == StreamKind.OUT]
        if len(results) == 1:
            body.append(f"return {results[0]};")
        elif len(results) > 1:
            body.append(f"return std::make_tuple({', '.join(results)});")
        return f"[]({', '.join(lam_params)}) {{ {' '.join(body)} }}"

    # Binding-Rules.md R-STATIC-S, R-RESULT, R-REF-PRIMITIVE
    def _method(self, cls: Class, m: Method) -> str | None:
        if m.skip_reason is not None:
            return None
        unbound = self._unbound_default(m.params)
        if unbound is not None:
            self.report.append(f"{cls.name}::{m.name}({self._sig(m.params)}): default argument of unbound type {unbound} -> method skipped")
            return None
        py = _py_name(m)
        if py is None:
            self.report.append(f"{cls.name}::{m.name}({self._sig(m.params)}): operator has no Python equivalent")
            return None
        if m.is_static:
            py += "_s"          # R-STATIC-S: every static method, OCP's rule -- a static and an instance method never share a name
        doc = m.doc
        if m.suffix != "":      # R-COLLISION: the suffix names the returned out-parameters that distinguish the overload
            py += m.suffix
            doc = f"{py}: the C++ overload {m.name}({self._sig(m.params)}); the suffix lists its returned out-parameters (nanocct R-COLLISION).\n{m.doc}"
        self._note_types(m.result, *(p.type for p in m.params))
        self._note_types(m.result_class_name, *(p.class_name for p in m.params))   # the class behind a typedef (IMeshData::IFaceHandle = handle<IMeshData_Face>): its header must be included
        T = cls.name                       # member pointers name the class itself ...
        B = cls.bound_type                 # ... lambdas take the bound type (a wrapper for non-copyable classes)
        if m.result_kind == ResultKind.REF_PRIMITIVE:
            return self._ref_primitive(cls, m, py)
        has_out = any(p.is_out or p.stream != StreamKind.NONE for p in m.params)
        wrap = m.result_kind in (ResultKind.PTR_TRANSIENT, ResultKind.REF_TRANSIENT, ResultKind.VALUE_TRANSIENT)   # never let nanobind own a Transient
        # R-RESULT: a T* or T& to another class keeps its owner alive (reference_internal: keep_alive<0, 1> on a new wrapper
        # -- nanobind returns an existing wrapper, self included, as is, so `return this` cannot keep itself alive)
        policy = {ResultKind.PTR_CLASS: ", nb::rv_policy::reference_internal", ResultKind.REF_MUTABLE: ", nb::rv_policy::reference_internal"}.get(m.result_kind, "")
        if m.result_kind in (ResultKind.PTR_CLASS, ResultKind.REF_MUTABLE) and m.is_static:
            # R-RESULT: a static method has no self to tie the result to (BRepMesh_DiscretFactory::Get(), the singleton):
            # reference_internal made every call fail ("Unable to convert function return value")
            policy = ", nb::rv_policy::reference"
        if m.result_kind == ResultKind.VALUE and m.result.rstrip().endswith("&"):
            # R-RESULT: a const T& is copied, or returned by reference when T cannot be copied (nanocct_common.h), when its
            # copy constructor does not copy the state (overrides.toml [not_value_copy]) or when the copy would share what
            # the destructor frees (R-COPY)
            if _names_not_value_copy(m.result) or m.result_by_reference:
                policy = ", nb::rv_policy::reference" if m.is_static else ", nb::rv_policy::reference_internal"
            else:
                policy = f", nanocct::cref_policy<{m.result}, {'false' if m.is_static else 'true'}>{{}}"
        if m.name in _INPLACE_OPS:
            # R-IOP: OCCT in-place operators return void (or *this); the lambda calls the operator and returns self, the same
            # Python object
            checks = "".join(c + " " for c in self._guard_checks(m.params))    # R-VIEW-GUARD
            lam = f"[]({B} &self{''.join(f', {p.type} {p.name}' for p in m.params)}) -> {B} & {{ {checks}self.{m.name}({', '.join(p.name for p in m.params)}); return self; }}"
            return f'.def("{py}", {lam}, nb::rv_policy::reference{self._keep_slots(m)}{self._extras(doc, m.params, False, True)})'
        if (m.result_on_heap or m.result_by_reference) and has_out:
            # R-COPY: the result would sit in a tuple, whose caster takes one return policy for every element (and the
            # lambda's `auto` copies it)
            self.report.append(f"{cls.name}::{m.name}({self._sig(m.params)}): returns {m.result} with out-parameters, and its "
                               f"copy would share the pointers its destructor frees (R-COPY) -> method skipped")
            return None
        if has_out or wrap or m.via_using != "" or m.force_lambda or m.result_on_heap or any(p.omitted or p.array_len > 0 or p.cstr_none or p.is_bytes for p in m.params):
            # R-USING: a member re-exported by `using Base::name;` is called on the derived object (the base may be non-public);
            # R-PTR-REF, R-OPTIONAL-PTR, R-FIXED-ARRAY, R-CSTR-NULL need a lambda too
            defn = "def_static" if m.is_static else "def"
            ptr_policy = policy if m.result_kind == ResultKind.PTR_CLASS else ""     # a lambda copies class results (auto)
            if m.result_on_heap:
                ptr_policy = ", nb::rv_policy::take_ownership"
            elif m.result_by_reference:
                ptr_policy = policy
            if m.result_kind == ResultKind.REF_TRANSIENT and not m.is_static:
                # R-RESULT: the member lives as long as its owner -- keep_alive<0, 1>, except when the result is self (8.18)
                ptr_policy += ", nb::call_policy<nanocct::KeepOwnerUnlessSelf>()"
            if m.result_kind == ResultKind.PTR_CLASS:      # a reference result is copied here (auto), a pointer is not
                self._report_owned_container(cls, m)
            return f'.{defn}("{py}", {self._lambda_call(T, m, B)}{ptr_policy}{self._keep_slots(m)}{self._iterator_init(m)}{self._keep_views(m, not m.is_static)}{self._extras(doc, m.params, True, m.is_operator)})'
        ne = " noexcept" if m.is_noexcept else ""
        if m.result_kind in (ResultKind.PTR_CLASS, ResultKind.REF_MUTABLE):
            self._report_owned_container(cls, m)
        if m.is_static:
            fn = self._guarded(f"static_cast<{m.result} (*)({self._sig(m.params)}){ne}>(&{T}::{m.name})", m.params)
            return f'.def_static("{py}", {fn}{policy}{self._keep_views(m, False)}{self._extras(doc, m.params, False, False)})'
        const = " const" if m.is_const else ""
        fn = self._guarded(f"static_cast<{m.result} ({T}::*)({self._sig(m.params)}){const}{ne}>(&{T}::{m.name})", m.params)
        return f'.def("{py}", {fn}{policy}{self._keep_slots(m)}{self._iterator_init(m)}{self._keep_views(m, True)}{self._extras(doc, m.params, False, m.is_operator)})'

    # Binding-Rules.md R-REF-PRIMITIVE
    def _ref_primitive(self, cls: Class, m: Method, py: str) -> str:
        """double& Value(i, j): a getter under the C++ name (returns the value) and, as a Python addition, a setter:
        Set<Name> with the Change prefix dropped (ChangeValue -> SetValue, Value -> SetValue, IsCopyMesh -> SetIsCopyMesh)
        unless the class already has a method of that name, and __setitem__ (plus __getitem__) for operator()/operator[]."""
        B = cls.bound_type
        params = ", ".join(f"{p.type} {p.name}" for p in m.params)
        sep = ", " if len(m.params) > 0 else ""
        args = ", ".join(p.name for p in m.params)
        keep = self._keep_slots(m)
        checks = "".join(c + " " for c in self._guard_checks(m.params))    # R-VIEW-GUARD
        getter = f'.def("{py}", []({B} &self{sep}{params}) -> {m.result} {{ {checks}return self.{m.name}({args}); }}{keep}{self._extras(m.doc, m.params, False, m.is_operator)})'
        note = f"Python addition: sets the value {m.name}({args}) returns by reference in C++."
        if m.is_operator:
            if len(m.params) == 1:
                index, unpack = f"{m.params[0].type} {m.params[0].name}", args
            else:
                index, unpack = f"std::tuple<{', '.join(_strip_ref(p.type) for p in m.params)}> theIndex", ", ".join(f"std::get<{i}>(theIndex)" for i in range(len(m.params)))
            lines = [getter,
                     f'.def("__getitem__", []({B} &self, {index}) -> {m.result} {{ return self.{m.name}({unpack}); }}, "Python addition: alias to {m.name}.")',
                     f'.def("__setitem__", []({B} &self, {index}, {m.result} theValue) {{ self.{m.name}({unpack}) = theValue; }}, "{note}")']
        else:
            setter = "Set" + (m.name[len("Change"):] if m.name.startswith("Change") else m.name)
            if any(o.name == setter and o.skip_reason is None for o in cls.methods):
                lines = [getter]                # gp_XYZ::ChangeCoord(i): SetCoord(i, v) exists in OCCT
            else:
                lines = [getter, f'.def("{setter}", []({B} &self{sep}{params}, {m.result} theValue) {{ {checks}self.{m.name}({args}) = theValue; }}{keep}{self._args(m.params, False)}, nb::arg("theValue"), "{note}")']
        self._note_types(m.result)
        return "\n        ".join(lines)

    def _ctor(self, cls: Class, params: list[Param], doc: str, type_name: str | None = None) -> str:
        """type_name: a dependent alias of the bound type (inside nanocct_if_concrete's generic lambda), so that `new T(...)` is
        only instantiated when the class is concrete."""
        self._note_types(*(p.type for p in params))
        self._note_types(*(p.class_name for p in params))
        T = type_name if type_name is not None else cls.bound_type
        # R-OPTIONAL-PTR / R-FIXED-ARRAY / R-CSTR-NULL / R-BYTES: nb::init cannot drop or convert
        # R-VIEW-GUARD: a container argument the constructor may change is checked in the body, after nanobind's conversion
        special = any(p.omitted or p.array_len > 0 or p.cstr_none or p.is_bytes or p.guarded for p in params)
        ins = [p for p in params if not p.omitted and p.bytes_of == ""]
        lam_params = ", ".join(f"const std::array<{p.type}, {p.array_len}> &{p.name}" if p.array_len > 0
                               else f"nanocct::OptionalCString {p.name}" if p.cstr_none
                               else f"const nb::bytes &{p.name}" if p.is_bytes else f"{p.type} {p.name}" for p in ins)
        pre = "".join(c + " " for c in self._guard_checks(params))
        pre += " ".join(f"{p.type} {p.name}_arr[{p.array_len}]; std::copy({p.name}.begin(), {p.name}.end(), {p.name}_arr);" for p in ins if p.array_len > 0)
        call = ", ".join("nullptr" if p.omitted else f"{p.name}_arr" if p.array_len > 0 else f"{p.name}.ptr" if p.cstr_none
                         else f"(const uint8_t *) {p.name}.c_str()" if p.is_bytes         # R-BYTES: the buffer ...
                         else f"{p.bytes_of}.size()" if p.bytes_of != ""                 # ... and its length, from the same object
                         else p.name for p in params)
        # R-BYTES in a constructor: the object may keep the pointer (WNT_HIDSpaceMouse stores myData(theData) and reads it
        # later, WNT_HIDSpaceMouse.cxx:154), so the bytes object lives as long as the new object: keep_alive<1, k>, where 1 is
        # `self` of __init__ and its parameters are numbered from 2. The nb::new_ path of a Transient has no such case and
        # its numbering is not verified, so it is refused rather than guessed.
        if cls.is_transient and any(p.is_bytes for p in ins):
            raise ValueError(f"R-BYTES in the constructor of the Transient {cls.name}: keep_alive for nb::new_ is not verified")
        keep = "".join(f", nb::keep_alive<1, {2 + i}>()" for i, p in enumerate(ins) if p.is_bytes)
        # R-CTOR-KEEP: an argument the object keeps a pointer or reference to lives as long as the object. nb::new_ hands
        # its extras to __new__(cls, args...), which returns the object, and to a no-op __init__(self, args...)
        # (nb_class.h, new_::execute): the nurse is the result, 0 -- in __init__ that is None, which keep_alive ignores
        # (nb_type.cpp, keep_alive_py) -- and the arguments count from 2 in both
        nurse = 0 if cls.is_transient else 1
        # R-COPY, R-CTOR-KEEP: an argument the object may copy pointers out of (a copy constructor, TDF_ChildIterator(label))
        # is kept with what its slots hold now (nanocct::keep_view_arg, the argument-layout keep): its next Initialize must not
        # free what the new object points to
        if cls.kept:
            # R-KEPT: the object is a nanocct::Kept<T>; an argument that cannot own it lives in a slot of its C++ object
            for i, p in enumerate(ins):
                if p.kept:
                    keep += (f", nb::call_policy<nanocct::keep_arg<nanocct_slots, {T}, {2 + i}, {self.slots}, "
                             f"{'true' if p.kept_view else 'false'}, {'true' if p.kept_cpp else 'false'}>>()")
                    self.slots += 1
        else:
            keep += "".join(f", nb::call_policy<nanocct::keep_view_arg<{nurse}, {2 + i}>>()" if p.kept_view
                            else f", nb::keep_alive<{nurse}, {2 + i}>()" for i, p in enumerate(ins) if p.kept)
        keep += self._iterator_views(ins, {i: 2 + i for i in range(len(ins))}, nurse)     # R-VIEW-GUARD
        if cls.is_transient:
            new_t = f"nanocct::Kept<{T}>" if cls.kept else T
            fn = f"nb::new_([]({lam_params}) {{ {pre}return opencascade::handle<{T}>(new {new_t}({call})); }})"
        elif special or type_name is not None:
            self_param = f"{T} *self" + (", " if len(ins) > 0 else "")
            fn = f'"__init__", []({self_param}{lam_params}) {{ {pre}new (self) {T}({call}); }}'
        else:
            fn = f"nb::init<{self._sig(params)}>()"
        return f".def({fn}{keep}{self._extras(doc, params, False, False)})"

    # Binding-Rules.md R-STR
    def _print_operator(self, fn: Function) -> tuple[str, str] | str:
        """`operator<<(Standard_OStream&, const T&)` as T.__str__, or the reason it is not one. It is OCCT's print-me idiom
        only when it is declared in T's own header (X.hxx or its X.lxx) and the stream is text: BinTools declares
        operator<<(ostream&, const gp_Pnt&) in BinTools_ShapeSetBase.hxx and writes binary doubles with it, and
        BinObjMgt_Persistent's operator<< is its binary Write. An exception class has str() already (its message)."""
        stream, obj = fn.params
        target = obj.class_name if obj.class_name != "" else _strip_ref(obj.type)
        cls = self._class_named.get(target)
        if cls is None:
            return f"operand {target} is not a class of this package"
        if stream.binary:
            return "binary stream ([stream] binary_packages), not a text rendering"
        if fn.header != cls.header:
            return f"declared in {fn.header}, not in {cls.header}"
        if cls.is_exception:
            return "exception class: str() is its message already"
        if any(m.skip_reason is None and _py_name(m) == "__str__" for m in cls.methods):
            return "the member operator<<(Standard_OStream&) is bound as __str__ already"
        self._note_types(obj.type)
        lam = (f"[]({obj.type} {obj.name}) {{ std::ostringstream nanocct_stream; nanocct_stream << {obj.name}; "
               f"return nanocct_stream_text(nanocct_stream); }}")
        return cls.name, f'.def("__str__", {lam}) /* free {fn.name} (R-STR) */'

    # Binding-Rules.md R-FREE-OP
    def _free_operator(self, fn: Function) -> tuple[str, str] | None:
        """Bind a free binary operator as a (reflected) method on the class of its class-typed operand."""
        entry = _BINARY_OPS.get(fn.name)
        if entry is None or len(fn.params) != 2:
            return None
        binary, _, reflected = entry
        a, b = fn.params
        ta, tb = _strip_ref(a.type), _strip_ref(b.type)
        sym = fn.name[len("operator"):]
        self._note_types(fn.result, a.type, b.type)
        if ta in self.local:
            if fn.name == "operator==" and tb == ta:
                self.value_eq.add(ta)
            lam = f"[]({a.type} {a.name}, {b.type} {b.name}) {{ return {a.name} {sym} {b.name}; }}"
            return ta, f'.def("{binary}", {lam}, nb::is_operator()) /* free {fn.name} */'
        if tb in self.local and reflected is not None:
            lam = f"[]({b.type} {b.name}, {a.type} {a.name}) {{ return {a.name} {sym} {b.name}; }}"
            return tb, f'.def("{reflected}", {lam}, nb::is_operator()) /* free {fn.name} */'
        return None

    # Binding-Rules.md R-ENUM, R-ANON-ENUM
    def _enum(self, e: Enum, scope: str) -> list[str]:
        if e.is_anonymous:      # C++ integer constants: enum { X = 1 };  -> scope.X = 1
            return [f'{scope}.attr("{py}") = nb::int_(static_cast<long long>({cpp}));' for py, cpp in e.values]
        d = _cpp_doc(e.doc)
        head = f'nb::enum_<{e.name}>({scope}, "{e.py_name}"'
        if d is not None:
            head += f", {d}"
        if not e.is_scoped:
            head += ", nb::is_arithmetic()"
        head += ")"
        lines = [head]
        for py, cpp in e.values:
            lines.append(f'    .value("{py}", {cpp})')
        if not e.is_scoped:
            # C++ puts the enumerators of an unscoped enum into the enclosing scope (TopAbs_FACE next to
            # TopAbs_ShapeEnum); export_values() does the same on the module or class. Scoped enums stay nested.
            lines.append("    .export_values()")
        lines[-1] += ";"
        if not e.is_scoped:
            # export_values() skips alias enumerators (Python's Enum iteration hides them): export those by name
            lines += [f'{scope}.attr("{py}") = {scope}.attr("{e.py_name}").attr("{py}");' for py in e.aliases]
        return lines

    # ---- NCollection template instances ---------------------------------------------------------
    def _instances(self) -> list[str]:
        """Second registration phase: bind every NCollection instantiation this package's signatures use and
        that no earlier package/run has bound, into nanocct.NCollection (its module object exists as soon as
        TKernel is imported, which every toolkit does first)."""
        lines: list[str] = []
        generated = set(self.known.values())

        def bind(template: str, args: list[str]) -> None:
            key = f"{template}<{', '.join(args)}>"
            if not self._owns(key):
                return
            self._emitted_instances.add(key)
            for a in args:                                 # nested containers first
                m = re.match(r"(NCollection_\w+)<(.+)>$", a)
                if m is not None and m.group(1) in BINDERS:
                    bind(m.group(1), [x.strip() for x in m.group(2).split(",")])
            for req in BINDERS[template]["requires"]:      # e.g. Array1<T> before HArray1<T>
                bind(req, args)
            if BINDERS[template].get("wraps", False):
                wrapped = args[0]
                if wrapped not in self.known and (wrapped not in self.templates or self.templates[wrapped].get("skipped", False)):
                    self.report.append(f"{key}: wrapped type {wrapped} is not bound -> instantiation skipped")
                    self.templates[key] = {"toolkit": "", "package": "", "name": "", "by": self.ir.name, "skipped": True}
                    return
            unbound = [a for a in args if a in self.skipped]     # a nested enum/class of a class skipped just before (_base_ok, Design.md 5.2)
            if len(unbound) > 0:
                self.report.append(f"{key}: element type {unbound[0]} is not bound (its class is skipped) -> instantiation skipped")
                self.templates[key] = {"toolkit": "", "package": "", "name": "", "by": self.ir.name, "skipped": True}
                return
            pointers = [a for a in args if a.endswith("*")]      # NCollection_DataMap<IMeshData_Face*, ...> (IMeshData): a raw pointer has no Python spelling
            if len(pointers) > 0:
                self.report.append(f"{key}: template argument {pointers[0]} is a raw pointer -> instantiation skipped")
                self.templates[key] = {"toolkit": "", "package": "", "name": "", "by": self.ir.name, "skipped": True}
                return
            owner = self.ir.copy_owner_instances.get(key, "")
            if owner != "" and not BINDERS[template].get("wraps", False):
                # R-COPY: a container copies its elements (Value(), Append, its own copy) -- each copy would share what the
                # element's destructor frees
                self.report.append(f"{key}: its elements' copy would share the pointers the destructor of {owner} may free (R-COPY) "
                                   f"-> instantiation skipped")
                self.templates[key] = {"toolkit": "", "package": "", "name": "", "by": self.ir.name, "skipped": True}
                return
            flags = ""
            if owner != "":
                self.report.append(f"{key}: no constructor from {args[0]} -- the copy would share the pointers the destructor of "
                                   f"{owner} may free (R-COPY)")
                flags = ", false"                           # bind_NCollection_Shared<T, CopyT = false>
            if any(a in self.ir.owned_args for a in args):
                self.needs_ocaf = True                      # R-OWNER: the binder keeps the OCAF owners of these elements
            home = "NCollection"                            # every instantiation lives in nanocct.NCollection
            if home not in generated:
                home = self.ir.name
            name = _py_identifier(key)
            scope = "m" if home == self.ir.name else f'nb::module_::import_("nanocct._{self.toolkit_of[home]}.{home}")'
            lines.append(f'    {{ nb::module_ home = {scope}; {BINDERS[template]["binder"]}<{", ".join(args)}{flags}>(home, "{name}"); }}')
            self.templates[key] = {"toolkit": self.toolkit_of[self.ir.name], "package": home, "name": name, "by": self.ir.name}
            self._note_types(*args)

        for key in sorted(self.ir.instances):
            inst = self.ir.instances[key]
            bind(inst.template, inst.args)
        return lines

    # ---- whole package -------------------------------------------------------------------------
    def _ordered_classes(self) -> list[Class]:
        """Bases before derived (only intra-package edges matter for ordering)."""
        done: list[Class] = []
        seen: set[str] = set()
        by_name = {c.name: c for c in self.ir.classes}

        def visit(c: Class) -> None:
            if c.name in seen:
                return
            seen.add(c.name)
            for b in c.bases:
                if b in by_name:
                    visit(by_name[b])
            if c.outer in by_name:            # a nested class is declared into its outer class
                visit(by_name[c.outer])
            done.append(c)

        for c in self.ir.classes:
            visit(c)
        return done

    def _base_ok(self, c: Class, skipped: set[str]) -> bool:
        def skip(c: Class) -> None:
            skipped.add(c.name)
            skipped.update(e.name for e in c.enums)     # its nested enums (BRepExtrema_ProximityDistTool::ProxPnt_Status) go with it:
                                                        # no alias, instantiation or manifest entry may name them (Design.md 5.2)
        if c.outer in skipped:
            self.report.append(f"{c.name}: outer class {c.outer} is not bound -> nested class skipped")
            skip(c)
            return False
        for b in c.bases:
            if c.is_exception and b.startswith("std::"):
                continue
            owner = b[:-len("::Iterator")] if b.endswith("::Iterator") else b
            if c.after_templates and (owner in self.ir.instances or (owner in self.templates and not self.templates[owner].get("skipped", False))):
                continue                                # 6a: a binder instantiation or its nested Iterator, registered in the templates phase
            if b not in self.known or b in skipped:     # skipped: a base of this package that was skipped just before (bases come first)
                self.report.append(f"{c.name}: base class {b} is not bound ({'skipped' if b in skipped else 'package not generated'}) -> class skipped")
                skip(c)
                return False
        return True

    def _exception(self, c: Class) -> str:
        """Standard_Failure descendants become Python exception types, keeping the C++ hierarchy."""
        occt_bases = [b for b in c.bases if b in self.known]
        if len(occt_bases) == 0:
            base = "PyExc_RuntimeError"
        else:
            b = occt_bases[0]
            pkg = self.known[b]
            # sibling packages are looked up through the extension submodule (registered in sys.modules
            # before any package is declared), never through the nanocct.<pkg> shim: importing the shim
            # while the toolkit module is still initialising would freeze a half-filled namespace
            attrs = "".join(f'.attr("{a}")' for a in py_path(b, pkg, self.paths).split("."))
            base = (f'nb::module_::import_("nanocct._{self.toolkit_of[pkg]}.{pkg}"){attrs}.ptr()'
                    if pkg != self.ir.name else f'm{attrs}.ptr()')
        d = _cpp_doc(c.doc)
        return f'    nanocct_register_exception<{c.name}>(nanocct_new_exception({self._attr(c.scope)}, "{c.py_name}", {d if d is not None else "nullptr"}, {base}));'

    def plan(self) -> tuple[list[Class], list[str]]:
        """The first phase of emit(): which classes survive their bases (5.2) and which 6a instantiations this
        package binds. Returns the surviving classes and the templates-phase lines.

        Split out because it is also everything the *registry* needs before the declare phase, so assign_templates()
        can run it without emitting anything."""
        ir = self.ir
        skipped = self.skipped
        classes = [c for c in self._ordered_classes() if self._base_ok(c, skipped)]
        for c in ir.classes:          # a skipped instantiation stays in the manifest as skipped: later runs know it is not new
            if c.name in skipped and c.template_key != "":
                self.templates[c.template_key] = {"toolkit": "", "package": "", "name": "", "by": ir.name, "skipped": True}
        instances = self._instances()   # registers this package's NCollection instantiations in self.templates (defaults may use them)
        for c in [c for c in classes if c.after_templates]:    # the binder base (or the Iterator's owner) may have been skipped just now
            owners = [b[:-len("::Iterator")] if b.endswith("::Iterator") else b for b in c.bases]
            if any(self.templates.get(o, {}).get("skipped", False) for o in owners):
                self.report.append(f"{c.name}: base class {c.bases[0]} is not bound (instantiation skipped) -> class skipped")
                skipped.add(c.name)
                classes.remove(c)
        return classes, instances

    def assign_templates(self) -> None:
        """Write every entry this package would put into the shared instantiation registry, without emitting anything.

        A parallel emit needs the owner of every instantiation decided up front, and in the sequential loop that
        decision *is* the emitting: `_instances()` binds what no earlier package has bound, and the declare phase
        claims a 6c instantiation or aliases the package that got there first. So the driver runs this over every
        package in emit order, sharing one registry, and the packages can then be emitted independently
        (`preassigned=True`). It runs the real decisions rather than a copy of them.

        The writes come out in the same order as in emit(): the declare phase interleaves them with the define phase,
        which never writes to the registry. It must stay that way round -- claiming inside plan() would let
        R-DEFAULT-UNBOUND see a class of the same package that emit() has not declared yet."""
        classes, _ = self.plan()
        for c in classes:
            if c.template_key != "":
                self._claim_template(c)

    def emit(self) -> str:
        """The package's .cpp: declare (classes, enums, constants, submodules), templates (NCollection instantiations),
        define (members, free functions, aliases), conversions (operator T() targets) -- one function per phase."""
        ir = self.ir
        skipped = self.skipped
        classes, instances = self.plan()
        free_ops, module_fns = self._functions()
        declare: list[str] = []
        define: list[str] = []
        wrappers: list[str] = []      # file-scope wrapper structs for non-copyable classes
        for ns in ir.namespaces:      # R-NAMESPACE: C++ namespaces other than the package's own -> submodules
            declare.append(f'    {self._module(ns[:-1])}.def_submodule("{ns[-1]}", "C++ namespace {"::".join(ns)} (OCCT package {ir.name})");')
        for k in ir.constants:
            declare.append(f'    {self._attr(k.scope)}.attr("{k.py_name}") = nb::cast({k.cpp});')
            self._note_types(k.cpp)
        for e in ir.enums:
            declare += ["    " + l for l in self._enum(e, self._attr(e.scope))]
        deferred: list[str] = []      # classes deriving from a binder instantiation's nested Iterator: declared after the instantiations
        for c in classes:
            target = deferred if c.after_templates else declare
            if self._declare_class(c, target, wrappers):
                self._define_class(c, free_ops, define)
        conversions = self._conversions(classes)
        define += self._aliases(classes)
        out = [
            f"// Generated by the nanocct generator from OCCT package {ir.name} (toolkit {ir.toolkit}). Do not edit.",
            '#include "nanocct_common.h"',
            *self._includes(len(instances) > 0),
            "",
            *(["namespace { struct nanocct_slots {}; }   // R-METHOD-KEEP: this file's slot table", ""] if self.slots > 0 else []),
            *(wrappers + [""] if len(wrappers) > 0 else []),

            f"void nanocct_declare_{ir.name}(nb::module_ &m) {{",
            *declare,
            "}",
            "",
            f"void nanocct_templates_{ir.name}(nb::module_ &m) {{",
            *instances,
            *deferred,
            "}",
            "",
            f"void nanocct_define_{ir.name}(nb::module_ &m) {{",
            *define,
            *module_fns,
            "}",
            "",
            f"void nanocct_conversions_{ir.name}(nb::module_ &m) {{",
            *conversions,
            "}",
            "",
        ]
        return "\n".join(out)

    def _functions(self) -> tuple[dict[str, list[str]], list[str]]:
        """Free functions: operators become members of their class operand (free_ops, by class name); the rest are
        module attributes (with the out-param tuple rule of methods)."""
        free_ops: dict[str, list[str]] = {}
        module_fns: list[str] = []
        plain = [f for f in self.ir.functions if not f.is_operator]
        for fn, why in self._skip_unbound(plain):                     # R-UNBOUND-TYPE: OSD_OpenFile -> FILE*
            q = fn.qualified if fn.qualified != "" else fn.name
            self.report.append(f"{q}({self._sig(fn.params)}): {why} -> not bound")
        for fn in skip_const_twins(plain):                            # R-CONST-TWIN: TopoDS::Vertex(const TopoDS_Shape&) vs (TopoDS_Shape&)
            q = fn.qualified if fn.qualified != "" else fn.name
            self.report.append(f"{q}({self._sig(fn.params)}): const twin of a less const overload -> not bound")
        plain, demoted = order_by_width(plain)                       # R-WIDTH: Abs(double) before Abs(float)
        plain, moved = order_by_derivation(plain, self._ancestors)   # R-OVERLOAD-ORDER: (TopoDS_Face) before (TopoDS_Shape)
        for derived, base in moved:
            q = derived.qualified if derived.qualified != "" else derived.name
            self.report.append(f"{q}({self._sig(derived.params)}): takes a derived class of {q}({self._sig(base.params)}) -> registered before it")
        for gone, taker in drop_unreachable(plain):                  # R-UNREACHABLE: Abs(float) after Abs(double)
            q = gone.qualified if gone.qualified != "" else gone.name
            self.report.append(f"{q}({self._sig(gone.params)}): same Python signature as {q}({self._sig(taker.params)}), registered before it -> not bound (unreachable)")
        for narrow, wide in demoted:
            if narrow.skip_reason is None:
                q = wide.qualified if wide.qualified != "" else wide.name
                self.report.append(f"{q}({self._sig(narrow.params)}): same Python signature as {q}({self._sig(wide.params)}) -> registered after it (width preference)")
        for fn, suffix in resolve_overload_collisions(plain):
            fn.suffix = suffix           # R-COLLISION applies to namespace functions too
        # R-FREE-OP: hidden friends, collected per class; an instantiation may be listed twice in ir.classes (the class
        # ordering pass dedups by name), so take each class once
        friend_ops = [f for c in {c.name: c for c in self.ir.classes}.values() for f in c.friend_ops]
        seen_ops: set[tuple[str, str]] = set()   # a friend declared in the class and defined at file scope in the .lxx (math_Matrix's operator*)
        for fn in plain + [f for f in self.ir.functions if f.is_operator] + friend_ops:
            if fn.skip_reason is not None:
                continue
            if fn.is_operator:
                key = (fn.name, self._sig(fn.params))
                if key in seen_ops:
                    continue
                seen_ops.add(key)
                if fn.name == "operator<<" and len(fn.params) == 2 and fn.params[0].stream == StreamKind.OUT:
                    printed = self._print_operator(fn)          # R-STR
                    if isinstance(printed, str):
                        self.report.append(f"{fn.name}({self._sig(fn.params)}): not bound as __str__: {printed}")
                    else:
                        free_ops.setdefault(printed[0], []).append(printed[1])
                    continue
                r = self._free_operator(fn)
                if r is None:
                    self.report.append(f"{fn.name}({self._sig(fn.params)}): free operator not mapped")
                else:
                    free_ops.setdefault(r[0], []).append(r[1])
                continue
            unbound = self._unbound_default(fn.params)
            if unbound is not None:
                self.report.append(f"{fn.name}({self._sig(fn.params)}): default argument of unbound type {unbound} -> function skipped")
                continue
            self._note_types(fn.result, *(p.type for p in fn.params))
            ne = " noexcept" if fn.is_noexcept else ""
            if fn.result_kind in (ResultKind.PTR_TRANSIENT, ResultKind.REF_TRANSIENT):
                self.report.append(f"{fn.name}({self._sig(fn.params)}): free function returning Transient pointer/reference not supported yet")
                continue
            # R-RESULT for free functions: a mutable reference result (TopoDS::Vertex(TopoDS_Shape&)) has no owner to tie
            # it to (no self), so it is copied rather than returned as a dangling reference; for TopoDS::Vertex & co. this
            # mutable overload is the bound one (R-CONST-TWIN drops the const& twin)
            policy = {ResultKind.PTR_CLASS: ", nb::rv_policy::reference", ResultKind.REF_MUTABLE: ", nb::rv_policy::copy"}.get(fn.result_kind, "")
            if fn.result_kind == ResultKind.VALUE and fn.result.rstrip().endswith("&"):
                # R-RESULT: no owner to tie a reference to
                policy = (", nb::rv_policy::reference" if _names_not_value_copy(fn.result) or fn.result_by_reference
                          else f", nanocct::cref_policy<{fn.result}, false>{{}}")
            qualified = fn.qualified if fn.qualified != "" else fn.name
            py, doc = py_safe(fn.name), fn.doc
            if fn.suffix != "":
                py += fn.suffix
                doc = f"{py}: the C++ overload {qualified}({self._sig(fn.params)}); the suffix lists its returned out-parameters (nanocct R-COLLISION).\n{fn.doc}"
                self.report.append(f"{qualified}({self._sig(fn.params)}): same Python signature as another overload after out-param removal -> bound as {py}")
            if (fn.result_on_heap or fn.result_by_reference) and any(p.is_out or p.stream == StreamKind.OUT for p in fn.params):
                self.report.append(f"{qualified}({self._sig(fn.params)}): returns {fn.result} with out-parameters, and its "
                                   f"copy would share the pointers its destructor frees (R-COPY) -> function skipped")
                continue
            if fn.result_kind == ResultKind.VALUE_TRANSIENT or fn.result_on_heap or any(
                    p.is_out or p.stream != StreamKind.NONE or p.omitted or p.array_len > 0 or p.cstr_none or p.is_bytes for p in fn.params):
                # R-OUT: out-params/streams -> returned tuple, as for methods; R-OPTIONAL-PTR / R-FIXED-ARRAY / R-CSTR-NULL
                # need the lambda too, and so does a Transient returned by value (R-RESULT: into a handle, never a
                # nanobind-owned copy)
                as_method = Method(name=qualified, params=fn.params, result=fn.result, result_kind=fn.result_kind,
                                   result_class=fn.result_class, is_static=False, is_const=False, is_noexcept=fn.is_noexcept, doc=doc,
                                   result_on_heap=fn.result_on_heap, result_by_reference=fn.result_by_reference)
                ptr_policy = (", nb::rv_policy::take_ownership" if fn.result_on_heap
                              else policy if fn.result_kind == ResultKind.PTR_CLASS or fn.result_by_reference else "")
                module_fns.append(f'    {self._module(fn.scope)}.def("{py}", {self._lambda_call(None, as_method)}{ptr_policy}{self._keep_views(fn, False)}{self._extras(doc, fn.params, True, False)});')
                continue
            direct = self._guarded(f"static_cast<{fn.result} (*)({self._sig(fn.params)}){ne}>(&{qualified})", fn.params)
            module_fns.append(f'    {self._module(fn.scope)}.def("{py}", {direct}{policy}{self._keep_views(fn, False)}{self._extras(doc, fn.params, False, False)});')
        return free_ops, module_fns

    def _declare_class(self, c: Class, declare: list[str], wrappers: list[str]) -> bool:
        """Declare phase of one class: nb::class_ with its offset-0 base and nested enums, or an alias when another
        package already bound the instantiation, or the exception type. Returns whether the define phase applies."""
        self._note_types(*c.bases)
        if c.template_key != "":
            found = self._claim_template(c)
            if found is not None:
                declare.append(f'    m.attr("{c.py_name}") = nb::module_::import_("nanocct._{found["toolkit"]}.{found["package"]}").attr("{found["name"]}");')
                return False
        if c.is_exception:
            declare.append(self._exception(c))
            return False
        # R-MI: nanobind takes one base and reuses the derived pointer for it, so only the first (offset-0) base
        # can be declared; further bases are reported (their members are not inherited in Python)
        for extra in c.bases[1:]:
            self.report.append(f"{c.name}: additional base {extra} not declared (nanobind: single inheritance, offset-0 base only)")
        bases = "".join(f", {b}" for b in c.bases[:1])
        d = _cpp_doc(c.doc)
        doc_arg = f", {d}" if d is not None else ""
        if c.noncopyable:
            ctor_name = c.name.split("<")[0]      # inheriting constructors name the template, not the instantiation
            wrappers.append(f"// {c.name}: its copy/move constructors do not compile although declared (R-NONCOPYABLE):\n"
                            f"// bound through a wrapper with deleted copy and move, under the original name\n"
                            f"struct {c.bound_type} : {c.name} {{\n    using {c.name}::{ctor_name};\n"
                            f"    {c.bound_type}(const {c.bound_type} &) = delete;\n    {c.bound_type}({c.bound_type} &&) = delete;\n}};")
        declare.append(f'    {{ nb::class_<{c.bound_type}{bases}> cls({self._attr(c.scope)}, "{c.py_name}"{doc_arg});')
        for e in c.enums:
            declare += ["      " + l for l in self._enum(e, "cls")]
        declare.append("    }")
        return True

    def _iter_getter(self, c: Class) -> str | None:
        """R-ITER: the name of the parameterless Value()/Current() when the class also has More() -> bool and
        Next() (all bound, non-static); None otherwise. The element must be copied out (a value or const-reference
        result, ResultKind.VALUE), because Next() is called right after reading it."""
        live = {(m.name, len(m.params)): m for m in c.methods if m.skip_reason is None and not m.is_static}
        more, nxt = live.get(("More", 0)), live.get(("Next", 0))
        if more is None or nxt is None or _strip_ref(more.result) != "bool":
            return None
        for name in ("Value", "Current"):
            get = live.get((name, 0))
            if get is not None and (get.result_by_reference or get.result_on_heap):
                return None          # R-COPY: an element whose copy would share what its destructor frees is not copied out
            if get is not None and get.result_kind in (ResultKind.VALUE, ResultKind.VALUE_TRANSIENT) and get.result != "void":
                return name
            if get is not None and get.result_kind == ResultKind.OTHER and self._copyable_const_ref(get.result):
                return name          # a dependent `const TheKeyType&` of a 6c instantiation (NCollection_FlatMap<K, H>::Iterator)
        return None

    # R-ITER: a dependent const X& Value()/Current() of a 6c instantiation is copied out unless X is a Transient
    def _copyable_const_ref(self, result: str) -> bool:
        """`const X &` inside a 6c instantiation: libclang gives the dependent pointee no declaration, so parse._result_kind
        says OTHER although nanobind copies it like any const-reference result. Safe to copy unless X is a Transient
        (R-RESULT: a nanobind-owned Transient copy is deleted by the first handle it meets) -- decided from the manifest's
        bases of every bound class."""
        m = re.fullmatch(r"const (.+?)\s*&", result.strip())
        if m is None:
            return False
        seen: set[str] = set()
        todo = [m.group(1).strip()]
        while len(todo) > 0:
            name = todo.pop()
            if name == "Standard_Transient":
                return False
            for b in self.bases_of.get(name, []):
                if b not in seen:
                    seen.add(b)
                    todo.append(b)
        return True

    def _define_class(self, c: Class, free_ops: dict[str, list[str]], define: list[str]) -> None:
        """Define phase of one class: constructors, methods (collisions resolved), free operators, scalar conversion
        dunders, __hash__, fields, implicit conversions, __iter__."""
        body: list[str] = []
        ctor_body: list[str] = []     # constructors of a 6c instantiation: guarded at compile time (abstractness is not visible in the template)
        self._iterating = self._iter_getter(c) is not None    # R-VIEW-GUARD: constructors and Init/Initialize make iterator views
        self._self = c.bound_type                              # R-KEPT: keep_slot's Self
        unhashable = False            # R-UNHASHABLE: emitted after the body, as a statement of its own
        def cls_expr_of(cc: Class) -> str:
            return f'nb::borrow<nb::class_<{cc.bound_type}>>({self._attr(cc.scope)}.attr("{cc.py_name}"))'
        implicit_default = False
        if not c.constructible:
            why = c.not_constructible_reason if c.not_constructible_reason != "" else "operator new is not public"
            self.report.append(f"{c.name}: {why} -> no constructors")
        if not c.is_abstract and c.constructible:
            for k, why in self._skip_unbound(c.ctors):                  # R-UNBOUND-TYPE: GCPnts_DistFunctionMV(GCPnts_DistFunction&)
                self.report.append(f"{c.name}::{c.name}({self._sig(k.params)}): {why} -> constructor not bound")
            declared, demoted = order_by_width([k for k in c.ctors if k.skip_reason is None])   # R-WIDTH
            # nanobind wants the zero-argument nb::new_ overload first; sort by required-parameter count (stable: width order kept)
            declared.sort(key=lambda k: sum(1 for q in k.params if q.default is None))
            declared, moved = order_by_derivation(declared, self._ancestors)   # R-OVERLOAD-ORDER: the copy constructor before a base-class one
            for derived, base in moved:
                self.report.append(f"{c.name}::{c.name}({self._sig(derived.params)}): takes a derived class of {c.name}({self._sig(base.params)}) -> registered before it")
            for gone, taker in drop_unreachable(declared):             # R-UNREACHABLE: (const char16_t*) after (const char*, bool = false)
                self.report.append(f"{c.name}::{c.name}({self._sig(gone.params)}): same Python signature as {c.name}({self._sig(taker.params)}), registered before it -> not bound (unreachable)")
            declared = [k for k in declared if k.skip_reason is None]
            for narrow, wide in demoted:
                if narrow.skip_reason is None:
                    self.report.append(f"{c.name}::{c.name}({self._sig(narrow.params)}): same Python signature as {c.name}({self._sig(wide.params)}) -> registered after it (width preference)")
            # R-IMPLICIT-DEFAULT: a class declaring no constructor gets the implicit default one, bound only if
            # std::is_default_constructible_v<T> (nanocct_implicit_default_ctor)
            implicit_default = not c.has_declared_ctor    # emitted first (nanobind wants the zero-argument overload first)
            arities = {id(k): n for k, n in resolve_ctor_arities(declared)}
            for k in declared:
                unbound = self._unbound_default(k.params)
                if unbound is not None:
                    self.report.append(f"{c.name}::{c.name}({self._sig(k.params)}): default argument of unbound type {unbound} -> constructor skipped")
                    continue
                n = arities.get(id(k))     # R-CTOR-AMBIGUOUS: the arity nanobind may call without a C++ ambiguity
                if n is None:
                    self.report.append(f"{c.name}::{c.name}({self._sig(k.params)}): every call form is ambiguous with another constructor in C++ -> constructor skipped")
                    continue
                if n < len(k.params):
                    self.report.append(f"{c.name}::{c.name}({self._sig(k.params)}): a call with all arguments is ambiguous with another constructor in C++ -> bound with the first {n}")
                if c.template_key != "":
                    ctor_body.append(self._ctor(c, k.params[:n], k.doc, type_name="nanocct_T"))
                else:
                    body.append(self._ctor(c, k.params[:n], k.doc))
        for m, why in self._skip_unbound(c.methods):   # R-UNBOUND-TYPE: MoniTool_Timer::Dictionary() -> a map over const char*
            self.report.append(f"{c.name}::{m.name}({self._sig(m.params)}): {why} -> not bound")
        bound = [m for m in c.methods if m.skip_reason is None]
        for m in skip_const_twins(c.methods):       # R-CONST-TWIN
            self.report.append(f"{c.name}::{m.name}({self._sig(m.params)}){' const' if m.is_const else ''}: const twin of a less const overload -> not bound")
        methods, demoted = order_by_width(c.methods)   # R-WIDTH: wider scalar overloads registered first
        methods, moved = order_by_derivation(methods, self._ancestors)   # R-OVERLOAD-ORDER: (NCollection_Array2<T>) before (NCollection_Array1<T>)
        for derived, base in moved:
            self.report.append(f"{c.name}::{derived.name}({self._sig(derived.params)}): takes a derived class of {base.name}({self._sig(base.params)}) -> registered before it")
        for gone, taker in drop_unreachable([m for m in methods if _py_name(m) is not None]):   # R-UNREACHABLE: AssignCat(char) after AssignCat(const char*)
            self.report.append(f"{c.name}::{gone.name}({self._sig(gone.params)}): same Python signature as {taker.name}({self._sig(taker.params)}), registered before it -> not bound (unreachable)")
        for narrow, wide in demoted:
            if narrow.skip_reason is None:
                self.report.append(f"{c.name}::{narrow.name}({self._sig(narrow.params)}): same Python signature as {wide.name}({self._sig(wide.params)}) -> registered after it (width preference)")
        resolved = resolve_overload_collisions(methods)
        for m, suffix in resolved:
            m.suffix = suffix
            if suffix != "" and _py_name(m) is not None:      # operators without a Python spelling are reported as such
                self.report.append(f"{c.name}::{m.name}({self._sig(m.params)}): same Python signature as another overload "
                                   f"after out-param removal -> bound as {_py_name(m)}{'_s' if m.is_static else ''}{suffix}")
        for m, _ in resolved:
            s = self._method(c, m)
            if s is not None:
                body.append(s)
        body += free_ops.get(c.name, [])
        if c.name in VIEW_CLASSES:
            # R-VIEW (Design.md 2c): a zero-copy numpy view (__array__), defined per class in
            # src/cpp/common/nanocct_views.h. Listed in overrides.toml [views] because which class gets which
            # view is data, not a shape the generator could detect.
            self.report.append(f"{c.name}: zero-copy numpy views added (nanocct_def_views)")
            self.needs_views = True
            define.append(f"    nanocct_def_views<{c.bound_type}>({cls_expr_of(c)});")
        getter = self._iter_getter(c)
        if getter is not None:       # R-ITER (Design.md 2c): More()/Next()/Value() classes are their own Python iterator
            self.report.append(f"{c.name}: __iter__ added (More/Next/{getter})")
            get = next(m for m in c.methods if m.name == getter and len(m.params) == 0 and not m.is_static and m.skip_reason is None)
            value = (f"opencascade::handle<{get.result_class}>(new {self._new_type(get.result_class)}(self.{getter}()))"   # R-RESULT: never a nanobind-owned Transient
                     if get.result_kind == ResultKind.VALUE_TRANSIENT else f"self.{getter}()")
            # R-RESULT-KEEP: an element of a class holding pointers keeps the iterated object; R-OWNER: an OCAF one its owners
            view = ", true" if get.result_view else ""
            if get.result_owned:
                self.needs_ocaf = True
            define.append(f'    nanocct_def_iter<{c.bound_type}{view}>({cls_expr_of(c)}, []({c.bound_type} &self) {{ return {value}; }});')
        for conv in c.conversions:          # operator bool/int/double() -> Python dunder; class targets: see _conversions
            dunder = {ConversionKind.BOOL: "__bool__", ConversionKind.INT: "__int__", ConversionKind.FLOAT: "__float__"}.get(conv.kind)
            if dunder is not None:
                self._note_types(conv.target)
                # R-CONV-SCALAR: a non-const conversion operator needs a non-const self (MeshVS_Buffer::operator int&())
                qual = "const " if conv.is_const else ""
                body.append(f'.def("{dunder}", [{qual and ""}]({qual}{c.bound_type} &self) {{ return static_cast<{conv.target}>(self); }}{", " + _cpp_doc(conv.doc) if conv.doc != "" else ""})')
        is_null = next((m for m in bound if m.name == "IsNull" and len(m.params) == 0 and not m.is_static
                        and m.result in ("bool", "Standard_Boolean")), None)
        if is_null is not None and not any(conv.kind == ConversionKind.BOOL for conv in c.conversions):
            # R-NULL-BOOL: OCCT gives the class IsNull() and no operator bool -> a null object is falsy, as a null
            # handle is (None, R-HANDLE) and an empty container is (__len__). Without it every object would be true
            # and `if shape:` would silently hold for a null shape. The self follows IsNull's constness
            # (PeriodicInterval::IsNull() is not const).
            self.report.append(f"{c.name}: __bool__ = not IsNull() added (IsNull() without operator bool)")
            qual = "const " if is_null.is_const else ""
            body.append(f'.def("__bool__", []({qual}{c.bound_type} &self) {{ return !self.IsNull(); }}, "Python addition: not IsNull().")')
        ir = self.ir
        if c.name in ir.hashable or c.template_key != "" and c.template_key.split("<", 1)[0] in ir.hashable_templates:
            # R-HASH: std::hash<T> specialised by OCCT (fully, or partially for a class template) -> hashability consistent with __eq__.
            # Some OCCT specialisations forward to the class's own HashCode() (TCollection_AsciiString.lxx:32), so when
            # HashCode is not in the library the lambda below does not link even though it needs no symbol itself --
            # the same trap as the inline members in overrides.toml [skip] methods, but this one is emitted by us, so
            # there is nothing to list there (BRepGraph_UsagePath on Windows, LNK2019, 2026-09-23).
            hash_code = next((m for m in c.methods if m.name == "HashCode"), None)
            if hash_code is not None and hash_code.skip_reason == "declared but not defined in the library":
                # worded so report.py's "undefined" pattern ("no definition in lib") matches it: the cause is a
                # missing library symbol like any other R-UNDEFINED skip, and an uncategorised message lands in "misc",
                # which the report tests reject on purpose
                self.report.append(f"{c.name}::__hash__: std::hash forwards to HashCode, which has "
                                   f"no definition in lib{ir.toolkit} -> not bound")
            else:
                body.append(f'.def("__hash__", [](const {c.bound_type} &self) {{ return static_cast<Py_ssize_t>(std::hash<{c.name}>{{}}(self)); }})')
        elif c.name in self.value_eq or any(m.name == "operator==" and len(m.params) == 1
                                            and _strip_ref(m.params[0].type) == c.name for m in bound):
            # R-UNHASHABLE (Binding-Rules.md): the class has a value __eq__ and OCCT gives no hash for it. nanobind never
            # touches tp_hash, and Python's "define __eq__ -> __hash__ becomes None" rule fires only at type creation,
            # so the class would keep object.__hash__ and `a == b` with `hash(a) != hash(b)` would make a dict or set
            # lookup by an equal value fail silently. Python's own answer for such a class is to be unhashable.
            self.report.append(f"{c.name}: __hash__ = None added (value __eq__ without a hash)")
            unhashable = True
        cls_expr = cls_expr_of(c)
        if c.kept:
            # R-KEPT: the handle caster shows a nanocct::Kept<T> as T (before any constructor can hand one to Python)
            define.append(f'    nanocct::register_kept<{c.bound_type}>({cls_expr});')
        if implicit_default:
            define.append(f'    nanocct_implicit_default_ctor<{c.bound_type}{", true" if c.kept else ""}>({cls_expr});')
        if len(ctor_body) > 0:
            # a template instantiation may be abstract through pure virtuals of its bases (BVH_PrimitiveSet<double, 3> via BVH_Set):
            # libclang cannot tell inside the template, the compiler can (R-TEMPLATE-BASE)
            define.append(f"    nanocct_if_concrete<{c.bound_type}>({cls_expr}, [](auto &cls) {{ using nanocct_T = typename std::decay_t<decltype(cls)>::Type; cls")
            define += ["        " + b for b in ctor_body]
            define[-1] += "; });"
        # R-BASELINE: the class's members as one chain of .def calls under their C++ names; nanobind resolves the overloads
        if len(body) > 0:
            define.append(f'    {cls_expr}')
            define += ["        " + b for b in body]
            define[-1] += ";"
        if unhashable:
            # after the body: nb::none() is an attribute assignment, not a .def, and setting it last keeps it
            # independent of whatever the chain above did
            define.append(f'    {cls_expr}.attr("__hash__") = nb::none();')
        # R-IMPLICIT-COPY: the implicit copy constructor (no user-declared one, TopoDS_Shape(const TopoDS_Vertex&)): bound when it exists,
        # after the declared constructors (nanobind wants a zero-argument nb::new_ before any other overload)
        if not c.is_abstract and c.constructible and not any(k.is_copy for k in c.ctors):
            if c.copy_owner != "":
                # R-COPY: the copy would share the pointers a destructor frees -- the second destructor frees them again
                self.report.append(f"{c.name}: no copy constructor -- an implicit copy would share the pointers the destructor of "
                                   f"{c.copy_owner} may free (R-COPY)")
            else:
                # R-COPY: the copy of a class holding pointers shares them, so it keeps the original alive (and what its slots hold)
                if c.kept:
                    # R-KEPT: the copy is a Kept<T> too; the original it shares pointers with stays kept by the copy's Python object
                    # (an argument of the class's own type can own the copy, which the cycle check of a constructor parameter
                    # would have to show first)
                    define.append(f'    nanocct_implicit_copy_ctor<{c.bound_type}, {"true" if c.view else "false"}, true, false, nanocct_slots, {self.slots}>({cls_expr});')
                    self.slots += 1
                else:
                    define.append(f'    nanocct_implicit_copy_ctor<{c.bound_type}{", true" if c.view else ""}>({cls_expr});')
        for f in c.fields:                 # R-FIELD: read/write when the field type is copy-assignable (decided at compile time), else read-only
            self._note_types(f.type)
            dd = _cpp_doc(f.doc)
            if f.array_len > 0:            # R-FIXED-ARRAY member: a list property (read/write unless const)
                A, B = f"std::array<{f.type}, {f.array_len}>", c.bound_type
                getter = f"[](const {B} &self) {{ {A} a; std::copy(std::begin(self.{f.name}), std::end(self.{f.name}), a.begin()); return a; }}"
                if f.is_const:
                    define.append(f'    {cls_expr}.def_prop_ro("{py_safe(f.name)}", {getter}{", " + dd if dd is not None else ""});')
                else:
                    setter = f"[]({B} &self, const {A} &a) {{ std::copy(a.begin(), a.end(), std::begin(self.{f.name})); }}"
                    define.append(f'    {cls_expr}.def_prop_rw("{py_safe(f.name)}", {getter}, {setter}{", " + dd if dd is not None else ""});')
                continue
            if f.is_bitfield:              # R-FIELD bit-field: no pointer-to-member exists, read and write through lambdas
                B = c.bound_type
                getter = f"[](const {B} &self) {{ return static_cast<{f.type}>(self.{f.name}); }}"
                setter = f"[]({B} &self, {f.type} v) {{ self.{f.name} = v; }}"
                define.append(f'    {cls_expr}.def_prop_rw("{py_safe(f.name)}", {getter}, {setter}{", " + dd if dd is not None else ""});')
                continue
            if f.is_pointer:               # R-FIELD: a raw pointer member is read-only, a copy of what it points to
                define.append(f'    nanocct_def_pointer_field({cls_expr}, "{py_safe(f.name)}", &{c.name}::{f.name}{", " + dd if dd is not None else ""});')
                continue
            # R-VIEW-GUARD: assigning a container member frees or reallocates what its views point into
            helper = "nanocct_def_container_field" if f.is_container else "nanocct_def_field"
            define.append(f'    {helper}({cls_expr}, "{py_safe(f.name)}", &{c.name}::{f.name}{", " + dd if dd is not None else ""});')
        for k in c.statics:                # R-STATIC-DATA: a read-only static property returning the value
            why = self._unbound_reason(k.type_class)
            if why is not None:            # an enum no binding registers: the cast would abort the module import
                self.report.append(f"{k.cpp}: type {k.type_class} {why} -> static data member not bound")
                continue
            # a prvalue copy of the value, not a reference: an in-class-initialised `static const int X = 5;` has no
            # definition to take the address of, and binding a reference (nb::cast(C::X)) would odr-use it
            # (and a read-only static property rather than a plain class attribute, which any assignment would replace)
            define.append(f'    {cls_expr}.def_prop_ro_static("{k.py_name}", [](nb::handle) {{ return static_cast<std::remove_cv_t<decltype({k.cpp})>>({k.cpp}); }});')
            self._note_types(k.type_class)
        if len(body) == 0 and len(c.fields) == 0 and len(c.statics) == 0:
            return
        # R-IMPLICIT-CONV: C++ implicit conversions (non-explicit converting constructors) apply in Python too
        if not c.is_abstract and c.constructible:
            seen: set[str] = set()
            for k in c.ctors:
                # R-CTOR-AMBIGUOUS: no conversion when the one-argument call is ambiguous (`IntPolyh_Array<T> a = 5;` is ambiguous in C++ too)
                if k.skip_reason is None and k.is_implicit and not ctor_call_ambiguous(c.ctors, k, 1):
                    src = k.params[0].type
                    if src not in seen:
                        seen.add(src)
                        define.append(f"    nb::implicitly_convertible<std::decay_t<{src}>, {c.bound_type}>();")

    # Binding-Rules.md R-CONV
    def _conversions(self, classes: list[Class]) -> list[str]:
        """operator T() const with a bound class T: T gets a constructor from this class, plus the implicit conversion when
        the operator is not explicit (TopoDS_Shape s = aMakeShape; BRepGraph_NodeId(anEdgeId)). Emitted in a phase of its
        own (after every definition of the toolkit: nanobind wants a class's zero-argument __new__ before other overloads)."""
        conversions: list[str] = []
        seen: set[tuple[str, str]] = set()      # const and non-const twins (XmlObjMgt_Persistent::operator XmlObjMgt_Element&/const&) once
        for c in classes:
            for conv in c.conversions:
                if conv.kind not in (ConversionKind.CLASS, ConversionKind.HANDLE):
                    continue
                if (c.name, conv.target_class) in seen:
                    continue
                seen.add((c.name, conv.target_class))
                inst = self.templates.get(conv.target_class)
                if inst is not None and not inst.get("skipped", False):
                    pkg, path = inst["package"], inst["name"]         # an instantiation bound under an alias (BVH_Vec3f)
                else:
                    pkg = self.known.get(conv.target_class)
                    path = py_path(conv.target_class, pkg, self.paths) if pkg is not None else ""
                if pkg is None or pkg == "":
                    self.report.append(f"{c.name}::operator {conv.target}(): target type is not bound -> conversion skipped")
                    continue
                order = self.toolkit_order
                if self.toolkit_of[pkg] in order and self.toolkit_of[self.ir.name] in order \
                        and order.index(self.toolkit_of[pkg]) > order.index(self.toolkit_of[self.ir.name]):
                    self.report.append(f"{c.name}::operator {conv.target}(): target lives in a later toolkit ({self.toolkit_of[pkg]}) -> conversion skipped")
                    continue
                attrs = "".join(f'.attr("{a}")' for a in path.split("."))
                target = (f'nb::module_::import_("nanocct._{self.toolkit_of[pkg]}.{pkg}"){attrs}' if pkg != self.ir.name else f"m{attrs}")
                helper = "nanocct_conversion_handle" if conv.kind == ConversionKind.HANDLE else "nanocct_conversion"
                kept_target = ", true" if helper == "nanocct_conversion" and conv.target_class in self.kept else ""   # R-KEPT
                conversions.append(f'    {helper}<{c.name}, {conv.target}{kept_target}>({target}, {"false" if conv.is_explicit else "true"});')
                self._note_types(conv.target)
        return conversions

    def _aliases(self, classes: list[Class]) -> list[str]:
        """R-ALIAS: typedefs of bound classes (using CurveD1 = Geom_Curve::ResD1 in namespace GeomGridEval) -> Python aliases;
        scalar typedefs (Standard_Real) and the rest are not exposed."""
        out: list[str] = []
        seen_aliases: set[tuple[tuple[str, ...], str]] = set()
        for td in self.ir.typedefs:
            key = (td.scope, td.py_name)
            if key in seen_aliases or any(c.py_name == td.py_name and c.scope == td.scope for c in classes):
                continue                           # a 6c alias instantiation is a class of its own
            seen_aliases.add(key)
            inst = self.templates.get(td.target)
            if inst is not None and not inst.get("skipped", False) and inst["package"] != "":
                # alias of a bound NCollection instantiation (BVH_Array3d = NCollection_LinearVector<NCollection_Vec3<double>>)
                out.append(f'    {self._attr(td.scope)}.attr("{td.py_name}") = nb::module_::import_("nanocct._{self.toolkit_of[inst["package"]]}.{inst["package"]}").attr("{inst["name"]}");   // {td.py_name} = {td.written}')
                continue
            pkg = self.known.get(td.target)
            if pkg is not None and "<" in td.target and td.target not in self.skipped:
                # alias of a 6c instantiation bound by an earlier package under its mangled name (BVH_Box3d = BVH_Box<double, 3>,
                # bound on demand by Bnd before BVH's typedef): an attribute alias like any other (R-ALIAS)
                attrs = "".join(f'.attr("{a}")' for a in py_path(td.target, pkg, self.paths).split("."))
                src = (f'nb::module_::import_("nanocct._{self.toolkit_of[pkg]}.{pkg}"){attrs}' if pkg != self.ir.name else f"m{attrs}")
                out.append(f'    {self._attr(td.scope)}.attr("{td.py_name}") = {src};   // {td.py_name} = {td.written}')
                continue
            if pkg is None or "<" in td.target or td.target in self.skipped:
                if td.target in self.skipped:
                    self.report.append(f"{td.py_name} = {td.written}: type alias of a type that is not bound (skipped)")
                elif td.scope != ():
                    self.report.append(f"{'::'.join(td.scope)}::{td.py_name} = {td.written}: type alias of an unbound type (not bound)")
                continue
            # A target in a *later* toolkit cannot be imported here: this module is half-initialised when that
            # toolkit imports it back, so `import_("nanocct._TKV3d.StdPrs")` raises "not a package" and the whole
            # import fails. R-CONV already skips a forward conversion target for the same reason (_conversions
            # above); do the same and report it. It cost `import nanocct._TKV3d` on its own until 2026-09-24,
            # which the eager import hid by always loading TKService first. Both names stay reachable as
            # StdPrs_BRepFont / StdPrs_BRepTextBuilder.
            order = self.toolkit_order
            if pkg != self.ir.name and self.toolkit_of[pkg] in order and self.toolkit_of[self.ir.name] in order \
                    and order.index(self.toolkit_of[pkg]) > order.index(self.toolkit_of[self.ir.name]):
                self.report.append(f"{td.py_name} = {td.written}: target lives in a later toolkit "
                                   f"({self.toolkit_of[pkg]}) -> the alias is not bound, use {td.target}")
                continue
            attrs = "".join(f'.attr("{a}")' for a in py_path(td.target, pkg, self.paths).split("."))
            src = (f'nb::module_::import_("nanocct._{self.toolkit_of[pkg]}.{pkg}"){attrs}' if pkg != self.ir.name else f"m{attrs}")
            out.append(f'    {self._attr(td.scope)}.attr("{td.py_name}") = {src};   // {td.py_name} = {td.written}')
        return out

    def _includes(self, with_ncollection: bool) -> list[str]:
        """The package headers (prelude first), plus every OCCT header named by an identifier the emitted code mentions."""
        ir = self.ir
        includes = [f"#include <{h}>" for h in ir.prelude + ir.headers]
        if with_ncollection:
            includes.insert(0, '#include "nanocct_ncollection.h"')
        if self.needs_views:
            includes.insert(0, '#include "nanocct_views.h"')
        if self.needs_ocaf:
            # R-OWNER: the OCAF owners of TDF_Label/TDF_Data/TDF_Attribute (and what they are named in, for R-LINK)
            includes.insert(0, '#include "nanocct_ocaf.h"')
            self._note_types("TDF_Attribute TDF_Data TDF_Label TDocStd_Document TDocStd_Owner")
        # R-PTR-INCOMPLETE: a class only forward-declared in the package's headers gets its own header here when OCCT
        # installs one
        extra = [f"{ident}.hxx" for ident in sorted(self._idents)
                 if f"{ident}.hxx" not in ir.headers and (self.include_dir / f"{ident}.hxx").exists()]
        if self.prelude_check is not None and len(extra) > 0:
            # an extra header may not be self-contained (Contap_Line.hxx); the headers it needs go first (R-PRELUDE)
            needed = [h for h in self.prelude_check(ir.prelude + ir.headers + extra) if h not in ir.prelude + ir.headers + extra]
            if len(needed) > 0:
                self.report.append(f"{ir.name}: extra headers not self-contained, {', '.join(needed)} included first")
                extra = needed + extra
        includes += [f"#include <{h}>" for h in extra]
        self.includes = ir.prelude + ir.headers + extra
        return includes


# the C++ scalars without a Python type of their own (nanocct/_templates.py; the stub header in stubs.py declares the same five)
_SCALAR_MARKERS = ("float32", "uchar", "uint", "ulong", "ulonglong")


# Binding-Rules.md R-COLLISION
def out_suffix(params: list[Param]) -> str:
    """'__float__float' for the removed out-parameters of an overload (streams: str, or bytes in a binary package); '' when
    the overload has none. Double underscores separate the parts because OCCT names contain single ones (Design.md 2a)."""
    parts = [("bytes" if p.binary else "str") if p.stream == StreamKind.OUT else p.out_py
             for p in params if p.stream == StreamKind.OUT or p.is_out and not p.is_inout]
    return "" if len(parts) == 0 else "__" + "__".join(parts)


def resolve_overload_collisions(overloads: list) -> list[tuple[object, str]]:
    """Overloads that become indistinguishable once out-params are dropped (Python has no dispatch on results) are told
    apart by a suffix naming the removed out-parameters' Python types: gp_Pnt::Coord(double&, double&, double&) is bound
    as Coord__float__float__float, GeomAPI_IntCS::Parameters(int, double&, double&, double&) as Parameters__float__float__float
    next to Parameters__float__float__float__float; an overload without out-parameters keeps the plain name
    (BOPDS_PaveBlock::HasEdge() -> bool next to HasEdge__int -> (bool, int); gp_Pnt::Coord() -> gp_XYZ next to
    Coord__float__float__float), without exception -- the name is derivable from the header alone. The suffix is unique
    within a group because C++ overloads cannot share a parameter list.
    Takes Methods or Functions (name, params, skip_reason, optionally is_static). Returns (overload, suffix) for every
    overload that is not skipped, in header order; the suffix is '' outside collision groups."""
    def py_sig(m) -> tuple:
        return (getattr(m, "qualified", "") or m.name, getattr(m, "is_static", False),
                tuple(_strip_ref(p.type) for p in m.params if (not p.is_out or p.is_inout) and p.stream != StreamKind.OUT))

    def full_sig(m) -> tuple:     # every parameter, out-params included, scalar widths folded (R-WIDTH twins are one overload here)
        return tuple((_width(p.type)[0], p.is_out and not p.is_inout, p.stream) for p in m.params)

    groups: dict[tuple, list] = {}
    for m in overloads:
        if m.skip_reason is None:
            groups.setdefault(py_sig(m), []).append(m)
    result: list[tuple[object, str]] = []
    for m in overloads:
        if m.skip_reason is not None:
            continue
        members = groups[py_sig(m)]
        # width twins (Graphic3d_Vertex::Coord(double&, double&, double&) / Coord(float&, float&, float&)) are the same
        # overload from Python and do not make a collision by themselves; the wider one is registered first (R-WIDTH)
        distinct = {full_sig(mm) for mm in members}
        colliding = len(distinct) > 1 and any(p.is_out or p.stream == StreamKind.OUT for mm in members for p in mm.params)
        result.append((m, out_suffix(m.params) if colliding else ""))
    return result


# Binding-Rules.md R-CONST-TWIN
def skip_const_twins(overloads: list) -> list:
    """Overloads that differ only in constness -- of the method (const T& Value(i) const / T& Value(i)) or of a
    parameter (TopoDS::Vertex(const TopoDS_Shape&) / (TopoDS_Shape&)) -- look identical from Python, whose objects are
    never const: C++ would pick the non-const one on such an object, so only the least-const twin is bound. Takes Methods
    or Functions; returns the skipped twins (their skip_reason is set)."""
    def key(m) -> tuple:
        return (getattr(m, "qualified", "") or m.name, getattr(m, "is_static", False), tuple(_strip_ref(p.type) for p in m.params))

    def constness(m) -> int:
        return (1 if getattr(m, "is_const", False) else 0) + sum(1 for p in m.params if p.type != _strip_ref(p.type) and p.type.startswith("const "))

    live = [m for m in overloads if m.skip_reason is None]
    groups: dict[tuple, list] = {}
    for m in live:
        groups.setdefault(key(m), []).append(m)
    skipped: list = []
    for members in groups.values():
        if len(members) < 2 or len({constness(m) for m in members}) < 2:
            continue
        least = min(constness(m) for m in members)
        for m in members:
            if constness(m) > least:
                m.skip_reason = "const twin of a less const overload"
                skipped.append(m)
    return skipped


# Binding-Rules.md R-WIDTH
_WIDTH_RANK = {"double": ("float", 0), "Standard_Real": ("float", 0), "float": ("float", 1), "Standard_ShortReal": ("float", 1),
               "int": ("int", 0), "Standard_Integer": ("int", 0)}
_WIDE_INTS = {"size_t", "Standard_Size", "unsigned", "unsigned int", "long", "unsigned long", "long long", "unsigned long long",
              "short", "unsigned short", "int8_t", "uint8_t", "int16_t", "uint16_t", "int32_t", "uint32_t", "int64_t", "uint64_t"}


# R-WIDTH for text (T1, 2026-09-30): every C++ text type is a Python str. The rank is C++'s own preference for a narrow
# string literal: const char* (exact match) before std::string_view/std::string (a conversion), then the UTF-16 string,
# then the single characters. Not "the widest" -- Resource_Manager::SetResource(name, const char16_t*) stores the value
# through Resource_Unicode's format, which with the default NoConversion turns "Größe" into Latin-1 bytes for Value()
# (measured in C++); TCollection_ExtendedString(const char*) reads UTF-8 as one byte per character, as it does in C++
# (TCollection_ExtendedString(s, True) decodes it).
_TEXT_RANK = {"char*": 0, "Standard_CString": 0, "std::string_view": 1, "std::basic_string_view<char>": 1, "std::string": 1,
              "std::basic_string<char>": 1, "char16_t*": 2, "Standard_ExtString": 2, "char": 3, "Standard_Character": 3,
              "char16_t": 4, "Standard_ExtCharacter": 4, "char32_t": 5, "Standard_Utf32Char": 5}
_TEXT_STRINGS = 2     # ranks up to here take any str; the single characters above take one character each


def _width(t: str) -> tuple[str, int]:
    """(Python type, rank) of a scalar parameter type: double/int rank 0, float and the other integer widths rank 1;
    a text type is ("str", its _TEXT_RANK); anything else is its own spelling with rank 0."""
    base = _strip_ref(t)
    if base in _WIDTH_RANK:
        return _WIDTH_RANK[base]
    if base in _WIDE_INTS:
        return ("int", 1)
    text = _TEXT_RANK.get(re.sub(r"\bconst\b|\s", "", base))
    if text is not None:
        return ("str", text)
    return (base, 0)


def _covers(x: Param, y: Param) -> bool:
    """Whether every Python argument parameter y accepts is also accepted by x (R-UNREACHABLE): a double takes every
    float, a string type every text; an int never covers another int width (nanobind's range check fails over, so
    Poly_ArrayOfNodes::Value(2**31) reaches the size_t twin), and a class covers only itself."""
    (kx, rx), (ky, ry) = _width(x.type), _width(y.type)
    if kx != ky:
        return False
    if kx == "float":
        return rx <= ry
    if kx == "str":
        return rx <= _TEXT_STRINGS or rx == ry
    return rx == ry


# Binding-Rules.md R-UNREACHABLE
def drop_unreachable(overloads: list) -> list[tuple[object, object]]:
    """An overload that an earlier-registered one of the same name takes over for every call it accepts is never reached
    from Python: nanobind calls the first overload that accepts the arguments. Such an overload is not bound
    (TCollection_ExtendedString(const char16_t*) after TCollection_ExtendedString(const char*, bool = false), Abs(float)
    after Abs(double)). Compared per number of passed arguments, so a defaulted parameter counts; overloads with out-
    parameters are left alone (R-COLLISION may give them a name of their own). Sets skip_reason; returns (dropped, taker)."""
    def key(m) -> tuple:
        return (getattr(m, "qualified", "") or getattr(m, "name", ""), getattr(m, "is_static", False))

    def has_out(m) -> bool:
        return any(p.is_out and not p.is_inout or p.stream == StreamKind.OUT for p in m.params)

    def arities(m) -> range:
        ps = _py_params(m)
        return range(sum(1 for p in ps if p.default is None and not p.cstr_none), len(ps) + 1)

    dropped: list[tuple[object, object]] = []
    earlier: list = []
    for y in overloads:
        if y.skip_reason is not None:
            continue
        if not has_out(y):
            yp = _py_params(y)
            takers = []
            for a in arities(y):
                taker = next((x for x in earlier if key(x) == key(y) and not has_out(x) and a in arities(x)
                              and all(_covers(xp, q) for xp, q in zip(_py_params(x)[:a], yp[:a]))), None)
                takers.append(taker)
            if len(takers) > 0 and all(t is not None for t in takers):
                y.skip_reason = "unreachable: an earlier overload takes every call"
                dropped.append((y, takers[0]))
                continue
        earlier.append(y)
    return dropped


# Binding-Rules.md R-WIDTH
def order_by_width(overloads: list) -> tuple[list, list[tuple[object, object]]]:
    """Overloads that differ only in the width of scalar parameters (Abs(double)/Abs(float), Value(int)/Value(size_t))
    are the same call from Python; nanobind takes the first registered, so the wider twin (double over float, int over
    size_t/unsigned/long) is emitted first. Returns the overloads in emission order and every (narrow, wide) pair."""
    def key(m) -> tuple:     # constructors have no name
        return (getattr(m, "qualified", "") or getattr(m, "name", ""), getattr(m, "is_static", False), tuple(_width(p.type)[0] for p in m.params))

    def rank(m) -> int:
        return sum(_width(p.type)[1] for p in m.params)

    live = [m for m in overloads if m.skip_reason is None]
    groups: dict[tuple, list] = {}
    for m in live:
        groups.setdefault(key(m), []).append(m)
    ordered: list = []
    demoted: list[tuple[object, object]] = []
    seen: set[int] = set()
    for m in overloads:
        if m.skip_reason is not None or id(m) in seen:
            continue
        members = groups[key(m)]
        by_rank = sorted(members, key=rank)      # stable: header order within equal rank
        demoted += [(x, by_rank[0]) for x in members if rank(x) > rank(by_rank[0])]   # reported whether or not the order changed
        for x in by_rank:
            seen.add(id(x))
            ordered.append(x)
    return ordered, demoted


# Binding-Rules.md R-OVERLOAD-ORDER
def _py_params(m) -> list[Param]:
    """The parameters a Python call passes (out-params, dropped optional pointers and R-BYTES lengths are not)."""
    return [p for p in m.params if not p.omitted and p.bytes_of == "" and not (p.is_out and not p.is_inout)
            and p.stream != StreamKind.OUT]


def _narrower(a: Param, b: Param, ancestors_of: Callable[[Param], set[str]]) -> bool | None:
    """True if every argument a accepts is also accepted by b and a is the narrower one (a's class derives from b's),
    False if the two take the same type, None if they are unrelated."""
    if a.class_name == "" or b.class_name == "":
        return False if _width(a.type)[0] == _width(b.type)[0] else None
    if a.class_name == b.class_name:
        return False
    return True if b.class_name in ancestors_of(a) else None


def order_by_derivation(overloads: list, ancestors_of: Callable[[Param], set[str]]) -> tuple[list, list[tuple[object, object]]]:
    """nanobind registers overloads in order and calls the first that accepts the arguments; a derived-class object is
    accepted by a base-class parameter in its first pass already. So an overload taking the base registered before one
    taking the derived class shadows it -- PLib::CoefficientsPoles(const NCollection_Array1<gp_Pnt>&, ...) caught
    NCollection_Array2<gp_Pnt> arguments and ran the curve algorithm, where C++ overload resolution picks the surface
    overload. An overload is therefore moved in front of every overload of the same name and number of
    Python parameters that takes, position by position, the same types or bases of its types (at least one a base).
    The order is otherwise kept. Returns the overloads in emission order and every (moved, shadowing) pair."""
    def key(m) -> tuple:
        return (getattr(m, "qualified", "") or getattr(m, "name", ""), getattr(m, "is_static", False), len(_py_params(m)))

    def dominates(x, y) -> bool:           # x must be registered before y
        if key(x) != key(y):
            return False
        rel = [_narrower(a, b, ancestors_of) for a, b in zip(_py_params(x), _py_params(y))]
        return all(r is not None for r in rel) and any(r is True for r in rel)

    ordered: list = []
    moved: list[tuple[object, object]] = []
    for m in overloads:
        at = next((i for i, o in enumerate(ordered) if o.skip_reason is None and dominates(m, o)), None)
        if m.skip_reason is not None or at is None:
            ordered.append(m)
        else:
            moved.append((m, ordered[at]))
            ordered.insert(at, m)
    return ordered, moved


# Binding-Rules.md R-CTOR-AMBIGUOUS
def ctor_call_ambiguous(ctors: list[Constructor], k: Constructor, n: int) -> bool:
    """Whether a C++ call of constructor k with its first n parameters is ambiguous with another (not skipped)
    constructor: one that is viable with n arguments of the same types (required(o) <= n <= len(o.params))."""
    def types(c: Constructor) -> tuple[str, ...]:
        return tuple(_strip_ref(p.type) for p in c.params[:n])

    return any(o is not k and o.skip_reason is None and sum(1 for p in o.params if p.default is None) <= n <= len(o.params)
               and types(o) == types(k) for o in ctors)


def resolve_ctor_arities(ctors: list[Constructor]) -> list[tuple[Constructor, int]]:
    """nanobind's nb::init<Args...> (and the nb::new_ lambda) always calls the C++ constructor with every parameter of
    the bound overload (Python fills the defaults), so a constructor whose full-arity call is ambiguous in C++ does not
    compile: IntPolyh_Array(const int aIncrement = 256) next to IntPolyh_Array(const int aN, const int aIncrement = 256)
    -- `IntPolyh_Array<T>(5)` is ambiguous in C++ too. Such a constructor is bound with the largest number of leading
    parameters that is unambiguous (here none: the zero-argument form), dropping trailing defaulted ones; the dropped
    calls are reachable through the other overload. Returns (constructor, arity) for the bindable constructors in the
    given order; a constructor with no unambiguous arity is left out (the caller reports it)."""
    result: list[tuple[Constructor, int]] = []
    for k in ctors:
        if k.skip_reason is not None:
            continue
        required = sum(1 for p in k.params if p.default is None)
        for n in range(len(k.params), required - 1, -1):
            if not ctor_call_ambiguous(ctors, k, n):
                result.append((k, n))
                break
    return result


def emit_toolkit_module(toolkit: str, packages: list[str], depends: list[str], namespaces: dict[str, list[tuple[str, ...]]]) -> str:
    decls = "\n".join(f"void nanocct_declare_{p}(nb::module_ &);\nvoid nanocct_templates_{p}(nb::module_ &);\nvoid nanocct_define_{p}(nb::module_ &);\n"
                      f"void nanocct_conversions_{p}(nb::module_ &);" for p in packages)
    imports = "\n".join(f'    nb::module_::import_("nanocct._{d}");' for d in depends)
    subs = "\n".join(
        f'    nb::module_ m_{p} = m.def_submodule("{p}", "OCCT package {p} (toolkit {toolkit})");\n'
        f'    m_{p}.attr("__name__") = "nanocct.{p}";\n'
        f'    sys_modules["nanocct._{toolkit}.{p}"] = m_{p};'
        for p in packages)
    # C++ namespaces (submodules created by the declare phase) are importable by their dotted name, like packages.
    # nanobind registers a submodule under <parent __name__>.<name>, i.e. nanocct.<pkg>.<ns>: that key belongs to
    # the Python shim module (nanocct/<pkg>/<ns>.py) and is removed again, or `import nanocct.<pkg>.<ns>` would
    # find the extension submodule without ever importing the package shim.
    declares = "\n".join(f"    nanocct_declare_{p}(m_{p});" + "".join(
        f'\n    sys_modules["nanocct._{toolkit}.{p}.{".".join(ns)}"] = m_{p}{"".join(f".attr(\"{a}\")" for a in ns)};'
        f'\n    sys_modules.attr("pop")("nanocct.{p}.{".".join(ns)}", nb::none());'
        for ns in namespaces.get(p, [])) for p in packages)
    templates = "\n".join(f"    nanocct_templates_{p}(m_{p});" for p in packages)
    defines = "\n".join(f"    nanocct_define_{p}(m_{p});" for p in packages)
    conversions = "\n".join(f"    nanocct_conversions_{p}(m_{p});" for p in packages)
    if toolkit == "TKernel":
        translator = '    nanocct_install_exception_translator(m_Standard.attr("Standard_Failure").ptr());'
    else:
        translator = "    nanocct_install_exception_translator(nullptr);"
    return f"""// Generated by the nanocct generator: extension module for OCCT toolkit {toolkit}. Do not edit.
#include "nanocct_common.h"

{decls}

NB_MODULE(_{toolkit}, m) {{
    m.doc() = "OCCT toolkit {toolkit}";
    nb::object sys_modules = nb::module_::import_("sys").attr("modules");
    // toolkits this one links against must have registered their types first
{imports}
{subs}
    // phase 1: all types (classes, enums) so that signatures/defaults can refer to them
{declares}
{translator}
    // phase 2: NCollection template instances (need their element types)
{templates}
    // phase 3: members
{defines}
    // phase 4: constructors from conversion operators (every class has its own constructors by now)
{conversions}
}}
"""


def write_package_shims(py_root: Path, package: str, toolkit: str,
                        namespaces: list[tuple[str, ...]],
                        accessors: dict[str, dict[tuple[tuple[str, str], ...], str]] | None = None,
                        homed_elsewhere: dict[str, str] | None = None,
                        late_links: list[str] | None = None) -> None:
    """nanocct/<package>.py, or for a package whose C++ code declares namespaces of its own (Geom2dEval_RepCurveDesc
    in package Geom2dEval) the Python package nanocct/<package>/__init__.py with one module per namespace, so that
    `from nanocct.Geom2dEval.Geom2dEval_RepCurveDesc import Base` and the .pyi layout follow the C++ nesting."""
    shim = emit_package_shim(package, toolkit, accessors, homed_elsewhere, late_links)
    pkg_dir = py_root / package
    module_file = py_root / f"{package}.py"
    if len(namespaces) == 0:
        if pkg_dir.is_dir():
            shutil.rmtree(pkg_dir)                  # the package lost its namespaces (regeneration)
        module_file.write_text(shim)
        return
    module_file.unlink(missing_ok=True)
    (py_root / f"{package}.pyi").unlink(missing_ok=True)
    pkg_dir.mkdir(exist_ok=True)
    top = sorted({ns[0] for ns in namespaces})
    files: dict[Path, str] = {}
    # absolute imports: `from . import X` would keep the extension submodule that the star import above already bound
    files[pkg_dir / "__init__.py"] = (shim + "\n# C++ namespaces of the package (Python modules nanocct.<package>.<namespace>)\n"
                                      + "".join(f"import nanocct.{package}.{n}  # noqa: E402,F401\n" for n in top))
    for ns in namespaces:
        has_children = any(len(other) == len(ns) + 1 and other[:len(ns)] == ns for other in namespaces)
        target = pkg_dir.joinpath(*ns)
        if has_children:
            target.mkdir(exist_ok=True)
            target = target / "__init__.py"
        else:
            target = target.with_suffix(".py")
        children = sorted(other[-1] for other in namespaces if len(other) == len(ns) + 1 and other[:len(ns)] == ns)
        files[target] = (
            f'"""C++ namespace {"::".join(ns)} (OCCT package {package}, toolkit {toolkit})."""\n'
            f'from nanocct._{toolkit}.{package}.{".".join(ns)} import *  # noqa: F401,F403\n'
            + "".join(f'import nanocct.{package}.{".".join(ns)}.{n}  # noqa: E402,F401\n' for n in children))
    for target, text in files.items():
        target.write_text(text)
    for stale in pkg_dir.rglob("*.py"):             # namespace modules of an earlier run; stubs (.pyi) are left alone
        if stale not in files:
            stale.unlink()


def emit_package_shim(package: str, toolkit: str,
                      accessors: dict[str, dict[tuple[tuple[str, str], ...], str]] | None = None,
                      homed_elsewhere: dict[str, str] | None = None, late_links: list[str] | None = None) -> str:
    """Python module nanocct.<package>: it re-exports the package's extension submodule under the name a user
    writes. homed_elsewhere: instantiations other toolkits bind into this package (6a) -> those toolkits are
    imported eagerly. accessors (NCollection only): template -> {element type specs -> bound class name} for the
    NCollection_Xxx[T] spelling."""
    head = f'''"""OCCT package {package} (toolkit {toolkit})."""
from nanocct._{toolkit}.{package} import *  # noqa: F401,F403
'''
    # R-LINK forward case: this toolkit links one that comes *later* in the order, so its module cannot import it at
    # registration time. Import it here, after the extension has initialised, or every member naming one of those
    # types is uncallable -- which the eager import used to hide (Binding-Rules.md 6a).
    for late in late_links or []:
        head += f"import nanocct._{late}  # noqa: F401,E402  (R-LINK: linked but later in the order)\n"
    # Eager (6a): other toolkits bind their instantiations into this package -- `nanocct.NCollection` is the one --
    # and loading their element types does not load them (215 of 799 instantiations, 2026-09-27), so importing the
    # package imports every toolkit that binds into it. Afterwards each instantiation is an ordinary attribute.
    eager_block = ""
    if homed_elsewhere:
        eager_block = ("\n# Instantiations bound into this package by other toolkits (Binding-Rules.md 6a): importing the package loads\n"
                       "# every toolkit that binds one, so each of them is an ordinary attribute afterwards.\n"
                       + "".join(f"import nanocct._{tk}  # noqa: E402,F401\n" for tk in sorted(set(homed_elsewhere.values())))
                       + f"from nanocct._{toolkit}.{package} import *  # noqa: E402,F401,F403  (again: now with every instantiation)\n")
    accessor_block = ""
    if accessors is not None:
        own = f"nanocct.{package}"
        marker_mod = "nanocct._templates"     # float32, uchar, ...: imported by name, so they are this package's too (8.20)
        modules = sorted({mod for table in accessors.values() for specs in table for mod, _ in specs} - {"builtins", own, marker_mod})
        markers = sorted({qual for table in accessors.values() for specs in table for mod, qual in specs if mod == marker_mod})
        if package == "NCollection":
            # all five, whatever this platform instantiates: `from nanocct.NCollection import ulonglong` is documented API, and
            # which marker a platform uses at all is its C library's business -- size_t and uint64_t are `unsigned long` on
            # glibc, `unsigned long long` on Windows, one of each on macOS (measured on the three trees, 2026-09-30)
            markers = sorted(set(markers) | set(_SCALAR_MARKERS))
        alias = {m: "_m_" + m.split(".", 1)[1].replace(".", "_") for m in modules}

        def spell(mod: str, qual: str) -> str:
            return qual if mod in ("builtins", own, marker_mod) else f"{alias[mod]}.{qual}"

        parts = ["", "# NCollection_Xxx[T] -> the bound class (Binding-Rules.md 6a): one generic class per template, keyed by the",
                 "# element types as Python passes them to __class_getitem__ (the type, or a tuple for several)",
                 "from nanocct._templates import Generic as _Generic  # noqa: E402"]
        if len(markers) > 0:
            parts.append(f"from nanocct._templates import {', '.join(markers)}  # noqa: E402,F401  (C++ scalars without a Python type, Binding-Rules.md 6a)")
        parts += [f"import {m} as {alias[m]}  # noqa: E402" for m in modules]
        for tmpl in sorted(accessors):
            parts += ["", "", f"class {tmpl}(_Generic):", "    _instances = {"]
            for specs, name in sorted(accessors[tmpl].items(), key=lambda kv: kv[1]):
                key = spell(*specs[0]) if len(specs) == 1 else "(" + ", ".join(spell(*sp) for sp in specs) + ")"
                parts.append(f"        {key}: {name},")
            parts.append("    }")
        accessor_block = "\n".join(parts) + "\n"
    return f"{head}{eager_block}{accessor_block}"
