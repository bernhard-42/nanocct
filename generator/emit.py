"""IR -> nanobind C++ source."""
from __future__ import annotations

from collections.abc import Callable

import re
import shutil
from pathlib import Path

from .model import Class, Constructor, ConversionKind, Enum, Function, Method, PackageIR, Param, ResultKind, StreamKind, TemplateInstance
from .ncollection import BINDERS
from .parse import _py_identifier, py_path, py_safe

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
    "operator!": (None, "__not__", None),
}
_INPLACE_OPS = {
    "operator+=": "__iadd__", "operator-=": "__isub__", "operator*=": "__imul__",
    "operator/=": "__itruediv__", "operator%=": "__imod__", "operator^=": "__ixor__",
    "operator&=": "__iand__", "operator|=": "__ior__",
}
_IDENT_RE = re.compile(r"[A-Za-z_]\w*")


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


# Design.md 6 R-OPERATOR, R-IOP
def _py_name(m: Method) -> str | None:
    """Python attribute name for a method; None when the operator has no Python counterpart."""
    if not m.is_operator:
        return py_safe(m.name)
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


class Emitter:
    def __init__(self, ir: PackageIR, include_dir: Path, known_classes: dict[str, str], toolkit_of: dict[str, str],
                 known_templates: dict[str, dict], toolkit_order: list[str] | None = None, paths: dict[str, str] | None = None,
                 prelude_check: Callable[[list[str]], list[str]] | None = None):
        self.ir = ir
        self.prelude_check = prelude_check    # R-PRELUDE for the emitted include list (parse.include_prelude); None in unit tests
        self.paths = paths if paths is not None else {}    # manifest "paths": C++ class -> Python path exceptions
        self.toolkit_order = toolkit_order if toolkit_order is not None else []   # generated toolkits, dependencies first
        self.include_dir = include_dir
        self.known = known_classes            # C++ class name -> package, for everything bound (previous runs + this run)
        self.toolkit_of = toolkit_of          # package -> toolkit
        self.templates = known_templates      # canonical instance key -> {toolkit, package, name}; updated while emitting
        self.local = {c.name for c in ir.classes}
        self.report: list[str] = []
        self.skipped: set[str] = set()        # classes of this package not bound after all (base/outer not bound); the caller drops them from the manifest
        self._idents: set[str] = set()

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

    # Design.md 6 R-DEFAULT-UNBOUND
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

    def _args(self, params: list[Param], skip_out: bool) -> str:
        parts: list[str] = []
        for p in params:
            if p.omitted or skip_out and (p.is_out and not p.is_inout or p.stream == StreamKind.OUT):
                continue
            # a handle<T> parameter accepts None (a null handle); without .none() nanobind rejects None before
            # the caster runs (Design.md 4.2)
            arg = f'nb::arg("{p.name}").none()' if p.is_handle else f'nb::arg("{p.name}")'
            if p.default is None:
                parts.append(arg)
            else:
                # cast to the parameter's value type: a `char` default written as 0 must become a
                # 1-character str, an enum default written as an int must become the enum, etc.
                parts.append(f'{arg} = static_cast<std::decay_t<{p.type}>>({p.default})')
                self._note_types(p.default)
        return "".join(", " + s for s in parts)

    def _extras(self, doc: str, params: list[Param], skip_out: bool, operator: bool) -> str:
        s = self._args(params, skip_out)
        d = _cpp_doc(doc)
        if d is not None:
            s += ", " + d
        if operator:
            s += ", nb::is_operator()"
        return s

    def _sig(self, params: list[Param]) -> str:
        return ", ".join(f"{p.type}[{p.array_len}]" if p.array_len > 0 else p.type for p in params)

    # ---- members -------------------------------------------------------------------------------
    # Design.md 6 R-OUT, R-OUT-HANDLE, R-INOUT, R-STREAM-OUT, R-STREAM-IN, R-RESULT
    def _lambda_call(self, cls: str | None, m: Method, self_type: str | None = None) -> str:
        """Lambda that maps out-params to a returned tuple (also handles static methods). self_type: the bound
        type when it differs from cls (non-copyable wrapper)."""
        ins = [p for p in m.params if (not p.is_out or p.is_inout) and p.stream != StreamKind.OUT and not p.omitted]
        outs = [p for p in m.params if p.is_out]
        lam_params: list[str] = []
        if cls is not None and not m.is_static:
            lam_params.append(f"{'const ' if m.is_const else ''}{self_type if self_type is not None else cls} &self")
        lam_params += [f"const nanoocp::{'BinaryInput' if p.binary else 'TextInput'} &{p.name}" if p.stream == StreamKind.IN
                       else f"const std::array<{p.type}, {p.array_len}> &{p.name}" if p.array_len > 0     # R-FIXED-ARRAY in: a sequence of N
                       else f"{_strip_ref(p.type) if p.is_inout else p.type} {p.name}" for p in ins]
        body: list[str] = [f"{p.type} {p.name}[{p.array_len}]{{}};" if p.array_len > 0 else f"{_strip_ref(p.type)} {p.name}{{}};"
                           for p in outs if not p.is_inout]
        # R-FIXED-ARRAY: a const T[N] parameter is copied from the std::array into a C array for the call
        body += [f"{p.type} {p.name}_arr[{p.array_len}]; std::copy({p.name}.begin(), {p.name}.end(), {p.name}_arr);" for p in ins if p.array_len > 0]
        # streams: an ostream& parameter becomes a returned str; an istream&/stringstream parameter takes a text file-like
        # object (nanoocp::TextInput caster in nanoocp_common.h: typing.TextIO, never a str -- that would collide with the
        # file-path overloads such as BRepTools::Read(shape, path, builder))
        body += [f"std::ostringstream {p.name}_stream;" for p in m.params if p.stream == StreamKind.OUT]
        body += [f"std::stringstream {p.name}_stream({p.name}.{'data' if p.binary else 'text'});" for p in m.params if p.stream == StreamKind.IN]
        call_args = ", ".join("nullptr" if p.omitted                                   # R-OPTIONAL-PTR
                              else f"{p.name}_stream" if p.stream != StreamKind.NONE
                              else f"{p.name}_arr" if p.array_len > 0 and not p.is_out else p.name for p in m.params)
        if cls is None:
            callee = f"{m.name}({call_args})"
        elif m.is_static:
            callee = f"{cls}::{m.name}({call_args})"
        else:
            callee = f"self.{m.name}({call_args})"
        results: list[str] = []
        if m.result_kind == ResultKind.PTR_TRANSIENT:
            body.append(f"opencascade::handle<{m.result_class}> result({callee});")
            results.append("result")
        elif m.result_kind == ResultKind.REF_TRANSIENT:
            body.append(f"opencascade::handle<{m.result_class}> result(&({callee}));")
            results.append("result")
        elif m.result != "void":
            body.append(f"auto result = {callee};")
            results.append("result")
        else:
            body.append(f"{callee};")
        for p in outs:
            if p.array_len > 0:                # R-FIXED-ARRAY out: N values back as a list
                body.append(f"std::array<{p.type}, {p.array_len}> {p.name}_out; std::copy(std::begin({p.name}), std::end({p.name}), {p.name}_out.begin());")
        results += [f"{p.name}_out" if p.array_len > 0 else p.name for p in outs]
        results += [f"nanoocp_stream_{'bytes' if p.binary else 'text'}({p.name}_stream)" for p in m.params if p.stream == StreamKind.OUT]
        if len(results) == 1:
            body.append(f"return {results[0]};")
        elif len(results) > 1:
            body.append(f"return std::make_tuple({', '.join(results)});")
        return f"[]({', '.join(lam_params)}) {{ {' '.join(body)} }}"

    # Design.md 6 R-STATIC-S, R-RESULT, R-REF-PRIMITIVE
    def _method(self, cls: Class, m: Method, mixed: set[str]) -> str | None:
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
        if m.is_static and m.name in mixed:
            py += "_s"          # Python cannot overload a static with an instance method of the same name
        doc = m.doc
        if m.suffix != "":      # R-COLLISION: the suffix names the returned out-parameters that distinguish the overload
            py += m.suffix
            doc = f"{py}: the C++ overload {m.name}({self._sig(m.params)}); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).\n{m.doc}"
        self._note_types(m.result, *(p.type for p in m.params))
        self._note_types(m.result_class_name, *(p.class_name for p in m.params))   # the class behind a typedef (IMeshData::IFaceHandle = handle<IMeshData_Face>): its header must be included
        T = cls.name                       # member pointers name the class itself ...
        B = cls.bound_type                 # ... lambdas take the bound type (a wrapper for non-copyable classes)
        if m.result_kind == ResultKind.REF_PRIMITIVE:
            return self._ref_primitive(cls, m, py)
        has_out = any(p.is_out or p.stream != StreamKind.NONE for p in m.params)
        wrap = m.result_kind in (ResultKind.PTR_TRANSIENT, ResultKind.REF_TRANSIENT)   # never let nanobind own a Transient
        policy = {ResultKind.PTR_CLASS: ", nb::rv_policy::reference", ResultKind.REF_MUTABLE: ", nb::rv_policy::reference_internal"}.get(m.result_kind, "")
        if m.name in _INPLACE_OPS:
            # OCCT in-place operators return void; Python expects self back
            lam = f"[]({B} &self{''.join(f', {p.type} {p.name}' for p in m.params)}) -> {B} & {{ self.{m.name}({', '.join(p.name for p in m.params)}); return self; }}"
            return f'.def("{py}", {lam}, nb::rv_policy::reference{self._extras(doc, m.params, False, True)})'
        if has_out or wrap or m.via_using != "" or m.force_lambda or any(p.omitted or p.array_len > 0 for p in m.params):
            # R-USING: a member re-exported by `using Base::name;` is called on the derived object (the base may be non-public);
            # R-PTR-REF, R-OPTIONAL-PTR, R-FIXED-ARRAY need a lambda too
            defn = "def_static" if m.is_static else "def"
            ptr_policy = policy if m.result_kind == ResultKind.PTR_CLASS else ""     # a lambda copies class results (auto)
            return f'.{defn}("{py}", {self._lambda_call(T, m, B)}{ptr_policy}{self._extras(doc, m.params, True, m.is_operator)})'
        ne = " noexcept" if m.is_noexcept else ""
        if m.is_static:
            fn = f"static_cast<{m.result} (*)({self._sig(m.params)}){ne}>(&{T}::{m.name})"
            return f'.def_static("{py}", {fn}{policy}{self._extras(doc, m.params, False, False)})'
        const = " const" if m.is_const else ""
        fn = f"static_cast<{m.result} ({T}::*)({self._sig(m.params)}){const}{ne}>(&{T}::{m.name})"
        return f'.def("{py}", {fn}{policy}{self._extras(doc, m.params, False, m.is_operator)})'

    # Design.md 6 R-REF-PRIMITIVE
    def _ref_primitive(self, cls: Class, m: Method, py: str) -> str:
        """double& Value(i, j): a getter under the C++ name (returns the value) and, as a Python addition, a setter:
        Set<Name> with the Change prefix dropped (ChangeValue -> SetValue, Value -> SetValue, IsCopyMesh -> SetIsCopyMesh)
        unless the class already has a method of that name, and __setitem__ (plus __getitem__) for operator()/operator[]."""
        B = cls.bound_type
        params = ", ".join(f"{p.type} {p.name}" for p in m.params)
        sep = ", " if len(m.params) > 0 else ""
        args = ", ".join(p.name for p in m.params)
        getter = f'.def("{py}", []({B} &self{sep}{params}) -> {m.result} {{ return self.{m.name}({args}); }}{self._extras(m.doc, m.params, False, m.is_operator)})'
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
                lines = [getter, f'.def("{setter}", []({B} &self{sep}{params}, {m.result} theValue) {{ self.{m.name}({args}) = theValue; }}{self._args(m.params, False)}, nb::arg("theValue"), "{note}")']
        self._note_types(m.result)
        return "\n        ".join(lines)

    def _ctor(self, cls: Class, params: list[Param], doc: str) -> str:
        self._note_types(*(p.type for p in params))
        self._note_types(*(p.class_name for p in params))
        special = any(p.omitted or p.array_len > 0 for p in params)     # R-OPTIONAL-PTR / R-FIXED-ARRAY: nb::init cannot drop or convert
        ins = [p for p in params if not p.omitted]
        lam_params = ", ".join(f"const std::array<{p.type}, {p.array_len}> &{p.name}" if p.array_len > 0 else f"{p.type} {p.name}" for p in ins)
        pre = " ".join(f"{p.type} {p.name}_arr[{p.array_len}]; std::copy({p.name}.begin(), {p.name}.end(), {p.name}_arr);" for p in ins if p.array_len > 0)
        call = ", ".join("nullptr" if p.omitted else f"{p.name}_arr" if p.array_len > 0 else p.name for p in params)
        if cls.is_transient:
            fn = f"nb::new_([]({lam_params}) {{ {pre}return opencascade::handle<{cls.bound_type}>(new {cls.bound_type}({call})); }})"
        elif special:
            self_param = f"{cls.bound_type} *self" + (", " if len(ins) > 0 else "")
            fn = f'"__init__", []({self_param}{lam_params}) {{ {pre}new (self) {cls.bound_type}({call}); }}'
        else:
            fn = f"nb::init<{self._sig(params)}>()"
        return f".def({fn}{self._extras(doc, params, False, False)})"

    # Design.md 6 R-FREE-OP
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
            lam = f"[]({a.type} {a.name}, {b.type} {b.name}) {{ return {a.name} {sym} {b.name}; }}"
            return ta, f'.def("{binary}", {lam}, nb::is_operator()) /* free {fn.name} */'
        if tb in self.local and reflected is not None:
            lam = f"[]({b.type} {b.name}, {a.type} {a.name}) {{ return {a.name} {sym} {b.name}; }}"
            return tb, f'.def("{reflected}", {lam}, nb::is_operator()) /* free {fn.name} */'
        return None

    # Design.md 6 R-ENUM, R-ANON-ENUM
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
        return lines

    # ---- NCollection template instances ---------------------------------------------------------
    def _instances(self) -> list[str]:
        """Second registration phase: bind every NCollection instantiation this package's signatures use and
        that no earlier package/run has bound, into nanoocp.NCollection (its module object exists as soon as
        TKernel is imported, which every toolkit does first)."""
        lines: list[str] = []
        generated = set(self.known.values())

        def bind(template: str, args: list[str]) -> None:
            key = f"{template}<{', '.join(args)}>"
            if key in self.templates:
                return
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
            home = "NCollection"                            # every instantiation lives in nanoocp.NCollection
            if home not in generated:
                home = self.ir.name
            name = _py_identifier(key)
            scope = "m" if home == self.ir.name else f'nb::module_::import_("nanoocp._{self.toolkit_of[home]}.{home}")'
            lines.append(f'    {{ nb::module_ home = {scope}; {BINDERS[template]["binder"]}<{", ".join(args)}>(home, "{name}"); }}')
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
            # before any package is declared), never through the nanoocp.<pkg> shim: importing the shim
            # while the toolkit module is still initialising would freeze a half-filled namespace
            attrs = "".join(f'.attr("{a}")' for a in py_path(b, pkg, self.paths).split("."))
            base = (f'nb::module_::import_("nanoocp._{self.toolkit_of[pkg]}.{pkg}"){attrs}.ptr()'
                    if pkg != self.ir.name else f'm{attrs}.ptr()')
        d = _cpp_doc(c.doc)
        return f'    nanoocp_register_exception<{c.name}>(nanoocp_new_exception({self._attr(c.scope)}, "{c.py_name}", {d if d is not None else "nullptr"}, {base}));'

    def emit(self) -> str:
        """The package's .cpp: declare (classes, enums, constants, submodules), templates (NCollection instantiations),
        define (members, free functions, aliases), conversions (operator T() targets) -- one function per phase."""
        ir = self.ir
        skipped = self.skipped
        classes = [c for c in self._ordered_classes() if self._base_ok(c, skipped)]
        for c in ir.classes:          # a skipped instantiation stays in the manifest as skipped: later runs know it is not new
            if c.name in skipped and c.template_key != "":
                self.templates[c.template_key] = {"toolkit": "", "package": "", "name": "", "by": ir.name, "skipped": True}
        instances = self._instances()   # registers this package's NCollection instantiations in self.templates (defaults may use them)
        free_ops, module_fns = self._functions()
        declare: list[str] = []
        define: list[str] = []
        wrappers: list[str] = []      # file-scope wrapper structs for non-copyable classes
        for ns in ir.namespaces:      # C++ namespaces other than the package's own -> submodules
            declare.append(f'    {self._module(ns[:-1])}.def_submodule("{ns[-1]}", "C++ namespace {"::".join(ns)} (OCCT package {ir.name})");')
        for k in ir.constants:
            declare.append(f'    {self._attr(k.scope)}.attr("{k.py_name}") = nb::cast({k.cpp});')
            self._note_types(k.cpp)
        for e in ir.enums:
            declare += ["    " + l for l in self._enum(e, self._attr(e.scope))]
        for c in classes:
            if self._declare_class(c, declare, wrappers):
                self._define_class(c, free_ops, define)
        conversions = self._conversions(classes)
        define += self._aliases(classes)
        out = [
            f"// Generated by the nanoOCP generator from OCCT package {ir.name} (toolkit {ir.toolkit}). Do not edit.",
            '#include "nanoocp_common.h"',
            *self._includes(len(instances) > 0),
            "",
            *(wrappers + [""] if len(wrappers) > 0 else []),

            f"void nanoocp_declare_{ir.name}(nb::module_ &m) {{",
            *declare,
            "}",
            "",
            f"void nanoocp_templates_{ir.name}(nb::module_ &m) {{",
            *instances,
            "}",
            "",
            f"void nanoocp_define_{ir.name}(nb::module_ &m) {{",
            *define,
            *module_fns,
            "}",
            "",
            f"void nanoocp_conversions_{ir.name}(nb::module_ &m) {{",
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
        for fn in skip_const_twins(plain):                            # R-CONST-TWIN: TopoDS::Vertex(const TopoDS_Shape&) vs (TopoDS_Shape&)
            q = fn.qualified if fn.qualified != "" else fn.name
            self.report.append(f"{q}({self._sig(fn.params)}): const twin of a less const overload -> not bound")
        plain, demoted = order_by_width(plain)                       # R-WIDTH: Abs(double) before Abs(float)
        for narrow, wide in demoted:
            q = wide.qualified if wide.qualified != "" else wide.name
            self.report.append(f"{q}({self._sig(narrow.params)}): same Python signature as {q}({self._sig(wide.params)}) -> registered after it (width preference)")
        for fn, suffix in resolve_overload_collisions(plain):
            fn.suffix = suffix           # R-COLLISION applies to namespace functions too
        for fn in plain + [f for f in self.ir.functions if f.is_operator]:
            if fn.skip_reason is not None:
                continue
            if fn.is_operator:
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
            # it to (no self), so it is copied rather than returned as a dangling reference; the const& overloads of
            # those functions are the reachable ones anyway (registered first)
            policy = {ResultKind.PTR_CLASS: ", nb::rv_policy::reference", ResultKind.REF_MUTABLE: ", nb::rv_policy::copy"}.get(fn.result_kind, "")
            qualified = fn.qualified if fn.qualified != "" else fn.name
            py, doc = py_safe(fn.name), fn.doc
            if fn.suffix != "":
                py += fn.suffix
                doc = f"{py}: the C++ overload {qualified}({self._sig(fn.params)}); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).\n{fn.doc}"
                self.report.append(f"{qualified}({self._sig(fn.params)}): same Python signature as another overload after out-param removal -> bound as {py}")
            if any(p.is_out or p.stream != StreamKind.NONE or p.omitted or p.array_len > 0 for p in fn.params):
                # out-params/streams -> returned tuple, as for methods; R-OPTIONAL-PTR / R-FIXED-ARRAY need the lambda too
                as_method = Method(name=qualified, params=fn.params, result=fn.result, result_kind=fn.result_kind,
                                   result_class=fn.result_class, is_static=False, is_const=False, is_noexcept=fn.is_noexcept, doc=doc)
                ptr_policy = policy if fn.result_kind == ResultKind.PTR_CLASS else ""
                module_fns.append(f'    {self._module(fn.scope)}.def("{py}", {self._lambda_call(None, as_method)}{ptr_policy}{self._extras(doc, fn.params, True, False)});')
                continue
            module_fns.append(f'    {self._module(fn.scope)}.def("{py}", static_cast<{fn.result} (*)({self._sig(fn.params)}){ne}>(&{qualified}){policy}{self._extras(doc, fn.params, False, False)});')
        return free_ops, module_fns

    def _declare_class(self, c: Class, declare: list[str], wrappers: list[str]) -> bool:
        """Declare phase of one class: nb::class_ with its offset-0 base and nested enums, or an alias when another
        package already bound the instantiation, or the exception type. Returns whether the define phase applies."""
        self._note_types(*c.bases)
        if c.template_key != "":
            found = self.templates.get(c.template_key)
            if found is not None and found.get("by") != self.ir.name and not found.get("skipped", False):
                declare.append(f'    m.attr("{c.py_name}") = nb::module_::import_("nanoocp._{found["toolkit"]}.{found["package"]}").attr("{found["name"]}");')
                return False
            self.templates[c.template_key] = {"toolkit": self.toolkit_of[self.ir.name], "package": self.ir.name, "name": c.py_name, "by": self.ir.name}
        if c.is_exception:
            declare.append(self._exception(c))
            return False
        # nanobind takes one base and reuses the derived pointer for it, so only the first (offset-0) base
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
            if get is not None and get.result_kind == ResultKind.VALUE and get.result != "void":
                return name
        return None

    def _define_class(self, c: Class, free_ops: dict[str, list[str]], define: list[str]) -> None:
        """Define phase of one class: constructors, methods (collisions resolved), free operators, scalar conversion
        dunders, __hash__, fields, implicit conversions, __iter__."""
        body: list[str] = []
        def cls_expr_of(cc: Class) -> str:
            return f'nb::borrow<nb::class_<{cc.bound_type}>>({self._attr(cc.scope)}.attr("{cc.py_name}"))'
        implicit_default = False
        if not c.constructible:
            self.report.append(f"{c.name}: operator new is not public -> no constructors")
        if not c.is_abstract and c.constructible:
            declared, demoted = order_by_width([k for k in c.ctors if k.skip_reason is None])   # R-WIDTH
            for narrow, wide in demoted:
                self.report.append(f"{c.name}::{c.name}({self._sig(narrow.params)}): same Python signature as {c.name}({self._sig(wide.params)}) -> registered after it (width preference)")
            # nanobind wants the zero-argument nb::new_ overload first; sort by required-parameter count (stable: width order kept)
            declared.sort(key=lambda k: sum(1 for q in k.params if q.default is None))
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
                body.append(self._ctor(c, k.params[:n], k.doc))
        bound = [m for m in c.methods if m.skip_reason is None]
        mixed = {m.name for m in bound if m.is_static} & {m.name for m in bound if not m.is_static}
        for m in skip_const_twins(c.methods):       # R-CONST-TWIN
            self.report.append(f"{c.name}::{m.name}({self._sig(m.params)}){' const' if m.is_const else ''}: const twin of a less const overload -> not bound")
        methods, demoted = order_by_width(c.methods)   # R-WIDTH: wider scalar overloads registered first
        for narrow, wide in demoted:
            self.report.append(f"{c.name}::{narrow.name}({self._sig(narrow.params)}): same Python signature as {wide.name}({self._sig(wide.params)}) -> registered after it (width preference)")
        resolved = resolve_overload_collisions(methods)
        for m, suffix in resolved:
            m.suffix = suffix
            if suffix != "" and _py_name(m) is not None:      # operators without a Python spelling are reported as such
                self.report.append(f"{c.name}::{m.name}({self._sig(m.params)}): same Python signature as another overload "
                                   f"after out-param removal -> bound as {_py_name(m)}{'_s' if m.is_static and m.name in mixed else ''}{suffix}")
        for name in sorted(mixed):
            self.report.append(f"{c.name}::{name}: static overloads renamed to {name}_s (instance method of same name exists)")
        for m, _ in resolved:
            s = self._method(c, m, mixed)
            if s is not None:
                body.append(s)
        body += free_ops.get(c.name, [])
        getter = self._iter_getter(c)
        if getter is not None:       # R-ITER (Design.md 2c): More()/Next()/Value() classes are their own Python iterator
            self.report.append(f"{c.name}: __iter__ added (More/Next/{getter})")
            define.append(f'    nanoocp_def_iter<{c.bound_type}>({cls_expr_of(c)}, []({c.bound_type} &self) {{ return self.{getter}(); }});')
        for conv in c.conversions:          # operator bool/int/double() -> Python dunder; class targets: see _conversions
            dunder = {ConversionKind.BOOL: "__bool__", ConversionKind.INT: "__int__", ConversionKind.FLOAT: "__float__"}.get(conv.kind)
            if dunder is not None:
                self._note_types(conv.target)
                body.append(f'.def("{dunder}", [](const {c.bound_type} &self) {{ return static_cast<{conv.target}>(self); }}{", " + _cpp_doc(conv.doc) if conv.doc != "" else ""})')
        ir = self.ir
        if c.name in ir.hashable or c.template_key != "" and c.template_key.split("<", 1)[0] in ir.hashable_templates:
            # R-HASH: std::hash<T> specialised by OCCT (fully, or partially for a class template) -> hashability consistent with __eq__
            body.append(f'.def("__hash__", [](const {c.bound_type} &self) {{ return static_cast<Py_ssize_t>(std::hash<{c.name}>{{}}(self)); }})')
        cls_expr = cls_expr_of(c)
        if implicit_default:
            define.append(f'    nanoocp_implicit_default_ctor<{c.bound_type}>({cls_expr});')
        if len(body) > 0:
            define.append(f'    {cls_expr}')
            define += ["        " + b for b in body]
            define[-1] += ";"
        # R-IMPLICIT-COPY: the implicit copy constructor (no user-declared one, TopoDS_Shape(const TopoDS_Vertex&)): bound when it exists,
        # after the declared constructors (nanobind wants a zero-argument nb::new_ before any other overload)
        if not c.is_abstract and c.constructible and not any(k.is_copy for k in c.ctors):
            define.append(f'    nanoocp_implicit_copy_ctor<{c.bound_type}>({cls_expr});')
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
            define.append(f'    nanoocp_def_field({cls_expr}, "{py_safe(f.name)}", &{c.name}::{f.name}{", " + dd if dd is not None else ""});')
        if len(body) == 0 and len(c.fields) == 0:
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

    # Design.md 6 R-CONV
    def _conversions(self, classes: list[Class]) -> list[str]:
        """operator T() const with a bound class T: T gets a constructor from this class, plus the implicit conversion when
        the operator is not explicit (TopoDS_Shape s = aMakeShape; BRepGraph_NodeId(anEdgeId)). Emitted in a phase of its
        own (after every definition of the toolkit: nanobind wants a class's zero-argument __new__ before other overloads)."""
        conversions: list[str] = []
        for c in classes:
            for conv in c.conversions:
                if conv.kind not in (ConversionKind.CLASS, ConversionKind.HANDLE):
                    continue
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
                target = (f'nb::module_::import_("nanoocp._{self.toolkit_of[pkg]}.{pkg}"){attrs}' if pkg != self.ir.name else f"m{attrs}")
                helper = "nanoocp_conversion_handle" if conv.kind == ConversionKind.HANDLE else "nanoocp_conversion"
                conversions.append(f'    {helper}<{c.name}, {conv.target}>({target}, {"false" if conv.is_explicit else "true"});')
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
                out.append(f'    {self._attr(td.scope)}.attr("{td.py_name}") = nb::module_::import_("nanoocp._{self.toolkit_of[inst["package"]]}.{inst["package"]}").attr("{inst["name"]}");   // {td.py_name} = {td.written}')
                continue
            pkg = self.known.get(td.target)
            if pkg is None or "<" in td.target or td.target in self.skipped:
                if td.target in self.skipped:
                    self.report.append(f"{td.py_name} = {td.written}: type alias of a type that is not bound (skipped)")
                elif td.scope != ():
                    self.report.append(f"{'::'.join(td.scope)}::{td.py_name} = {td.written}: type alias of an unbound type (not bound)")
                continue
            attrs = "".join(f'.attr("{a}")' for a in py_path(td.target, pkg, self.paths).split("."))
            src = (f'nb::module_::import_("nanoocp._{self.toolkit_of[pkg]}.{pkg}"){attrs}' if pkg != self.ir.name else f"m{attrs}")
            out.append(f'    {self._attr(td.scope)}.attr("{td.py_name}") = {src};   // {td.py_name} = {td.written}')
        return out

    def _includes(self, with_ncollection: bool) -> list[str]:
        """The package headers (prelude first), plus every OCCT header named by an identifier the emitted code mentions."""
        ir = self.ir
        includes = [f"#include <{h}>" for h in ir.prelude + ir.headers]
        if with_ncollection:
            includes.insert(0, '#include "nanoocp_ncollection.h"')
        extra = [f"{ident}.hxx" for ident in sorted(self._idents)
                 if f"{ident}.hxx" not in ir.headers and (self.include_dir / f"{ident}.hxx").exists()]
        if self.prelude_check is not None and len(extra) > 0:
            # an extra header may not be self-contained (Contap_Line.hxx); the headers it needs go first (R-PRELUDE)
            needed = [h for h in self.prelude_check(ir.prelude + ir.headers + extra) if h not in ir.prelude + ir.headers + extra]
            if len(needed) > 0:
                self.report.append(f"{ir.name}: extra headers not self-contained, {', '.join(needed)} included first")
                extra = needed + extra
        includes += [f"#include <{h}>" for h in extra]
        return includes


# Design.md 6 R-COLLISION
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
    next to Parameters__float__float__float__float; an overload without out-parameters keeps the plain name (gp_Pnt::Coord()
    -> gp_XYZ, as in C++). The suffix is unique within a group because C++ overloads cannot share a parameter list.
    Takes Methods or Functions (name, params, skip_reason, optionally is_static). Returns (overload, suffix) for every
    overload that is not skipped, in header order; the suffix is '' outside collision groups."""
    def py_sig(m) -> tuple:
        return (getattr(m, "qualified", "") or m.name, getattr(m, "is_static", False),
                tuple(_strip_ref(p.type) for p in m.params if (not p.is_out or p.is_inout) and p.stream != StreamKind.OUT))

    groups: dict[tuple, list] = {}
    for m in overloads:
        if m.skip_reason is None:
            groups.setdefault(py_sig(m), []).append(m)
    result: list[tuple[object, str]] = []
    for m in overloads:
        if m.skip_reason is not None:
            continue
        members = groups[py_sig(m)]
        colliding = len(members) > 1 and any(p.is_out or p.stream == StreamKind.OUT for mm in members for p in mm.params)
        result.append((m, out_suffix(m.params) if colliding else ""))
    return result


# Design.md 6 R-CONST-TWIN
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


# Design.md 6 R-WIDTH
_WIDTH_RANK = {"double": ("float", 0), "Standard_Real": ("float", 0), "float": ("float", 1), "Standard_ShortReal": ("float", 1),
               "int": ("int", 0), "Standard_Integer": ("int", 0)}
_WIDE_INTS = {"size_t", "Standard_Size", "unsigned", "unsigned int", "long", "unsigned long", "long long", "unsigned long long",
              "short", "unsigned short", "int8_t", "uint8_t", "int16_t", "uint16_t", "int32_t", "uint32_t", "int64_t", "uint64_t"}


def _width(t: str) -> tuple[str, int]:
    """(Python type, rank) of a scalar parameter type: double/int rank 0, float and the other integer widths rank 1;
    anything else is its own spelling with rank 0."""
    base = _strip_ref(t)
    if base in _WIDTH_RANK:
        return _WIDTH_RANK[base]
    if base in _WIDE_INTS:
        return ("int", 1)
    return (base, 0)


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


# Design.md 6 R-CTOR-AMBIGUOUS
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
    decls = "\n".join(f"void nanoocp_declare_{p}(nb::module_ &);\nvoid nanoocp_templates_{p}(nb::module_ &);\nvoid nanoocp_define_{p}(nb::module_ &);\n"
                      f"void nanoocp_conversions_{p}(nb::module_ &);" for p in packages)
    imports = "\n".join(f'    nb::module_::import_("nanoocp._{d}");' for d in depends)
    subs = "\n".join(
        f'    nb::module_ m_{p} = m.def_submodule("{p}", "OCCT package {p} (toolkit {toolkit})");\n'
        f'    m_{p}.attr("__name__") = "nanoocp.{p}";\n'
        f'    sys_modules["nanoocp._{toolkit}.{p}"] = m_{p};'
        for p in packages)
    # C++ namespaces (submodules created by the declare phase) are importable by their dotted name, like packages.
    # nanobind registers a submodule under <parent __name__>.<name>, i.e. nanoocp.<pkg>.<ns>: that key belongs to
    # the Python shim module (nanoocp/<pkg>/<ns>.py) and is removed again, or `import nanoocp.<pkg>.<ns>` would
    # find the extension submodule without ever importing the package shim.
    declares = "\n".join(f"    nanoocp_declare_{p}(m_{p});" + "".join(
        f'\n    sys_modules["nanoocp._{toolkit}.{p}.{".".join(ns)}"] = m_{p}{"".join(f".attr(\"{a}\")" for a in ns)};'
        f'\n    sys_modules.attr("pop")("nanoocp.{p}.{".".join(ns)}", nb::none());'
        for ns in namespaces.get(p, [])) for p in packages)
    templates = "\n".join(f"    nanoocp_templates_{p}(m_{p});" for p in packages)
    defines = "\n".join(f"    nanoocp_define_{p}(m_{p});" for p in packages)
    conversions = "\n".join(f"    nanoocp_conversions_{p}(m_{p});" for p in packages)
    if toolkit == "TKernel":
        translator = '    nanoocp_install_exception_translator(m_Standard.attr("Standard_Failure").ptr());'
    else:
        translator = "    nanoocp_install_exception_translator(nullptr);"
    return f"""// Generated by the nanoOCP generator: extension module for OCCT toolkit {toolkit}. Do not edit.
#include "nanoocp_common.h"

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


def write_package_shims(py_root: Path, package: str, toolkit: str | None, aliases: dict[str, tuple[str, str]],
                        namespaces: list[tuple[str, ...]],
                        accessors: dict[str, dict[tuple[tuple[str, str], ...], str]] | None = None) -> None:
    """nanoocp/<package>.py, or for a package whose C++ code declares namespaces of its own (Geom2dEval_RepCurveDesc
    in package Geom2dEval) the Python package nanoocp/<package>/__init__.py with one module per namespace, so that
    `from nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc import Base` and the .pyi layout follow the C++ nesting."""
    shim = emit_package_shim(package, toolkit, aliases, accessors)
    pkg_dir = py_root / package
    module_file = py_root / f"{package}.py"
    if len(namespaces) == 0:
        if pkg_dir.is_dir():
            shutil.rmtree(pkg_dir)                  # the package lost its namespaces (regeneration)
        module_file.write_text(shim)
        return
    assert toolkit is not None
    module_file.unlink(missing_ok=True)
    (py_root / f"{package}.pyi").unlink(missing_ok=True)
    pkg_dir.mkdir(exist_ok=True)
    top = sorted({ns[0] for ns in namespaces})
    files: dict[Path, str] = {}
    # absolute imports: `from . import X` would keep the extension submodule that the star import above already bound
    files[pkg_dir / "__init__.py"] = (shim + "\n# C++ namespaces of the package (Python modules nanoocp.<package>.<namespace>)\n"
                                      + "".join(f"import nanoocp.{package}.{n}  # noqa: E402,F401\n" for n in top))
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
            f'from nanoocp._{toolkit}.{package}.{".".join(ns)} import *  # noqa: F401,F403\n'
            + "".join(f'import nanoocp.{package}.{".".join(ns)}.{n}  # noqa: E402,F401\n' for n in children))
    for target, text in files.items():
        target.write_text(text)
    for stale in pkg_dir.rglob("*.py"):             # namespace modules of an earlier run; stubs (.pyi) are left alone
        if stale not in files:
            stale.unlink()


def emit_package_shim(package: str, toolkit: str | None, aliases: dict[str, tuple[str, str]],
                      accessors: dict[str, dict[tuple[tuple[str, str], ...], str]] | None = None) -> str:
    """Python module nanoocp.<package>. toolkit=None: a pure alias module (prefix of deprecated typedefs
    that is not a package in OCCT 8, e.g. TColgp). accessors (NCollection only): template -> {element type
    specs -> bound class name} for the NCollection_Xxx[T] spelling."""
    alias_lines = "".join(f'    "{a}": ("nanoocp.{pkg}", "{name}"),\n' for a, (pkg, name) in sorted(aliases.items()))
    accessor_block = ""
    if accessors is not None:
        parts = ["", "# NCollection_Xxx[T] -> bound class (Design.md 6a); tables generated from manifest.json",
                 "from nanoocp._templates import Template as _Template", ""]
        for tmpl in sorted(accessors):
            entries = "".join(f"    {specs!r}: \"{name}\",\n" for specs, name in sorted(accessors[tmpl].items(), key=lambda kv: kv[1]))
            parts.append(f'{tmpl} = _Template("{tmpl}", "nanoocp.NCollection", {{\n{entries}}})')
        accessor_block = "\n".join(parts) + "\n"
    if toolkit is None:
        head = f'''"""OCCT pre-8.0 typedef names with prefix {package} (OCCT src/Deprecated/NCollectionAliases)."""
import importlib as _importlib
'''
        fallback = '    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")'
    else:
        head = f'''"""OCCT package {package} (toolkit {toolkit})."""
import importlib as _importlib

from nanoocp._{toolkit} import {package} as _ext
from nanoocp._{toolkit}.{package} import *  # noqa: F401,F403
'''
        fallback = "    return getattr(_ext, name)   # NCollection instantiations bound into this package by other toolkits"
    return f'''{head}
{accessor_block}
# deprecated NCollection typedef names -> (home module, bound name)
_ALIASES = {{
{alias_lines}}}


def __getattr__(name):
    target = _ALIASES.get(name)
    if target is not None:
        return getattr(_importlib.import_module(target[0]), target[1])
{fallback}
'''
