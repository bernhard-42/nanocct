"""IR -> nanobind C++ source."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

from .model import Class, Enum, Function, Method, PackageIR, Param, TemplateInstance
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
                 known_templates: dict[str, dict], toolkit_order: list[str] | None = None, paths: dict[str, str] | None = None):
        self.ir = ir
        self.paths = paths if paths is not None else {}    # manifest "paths": C++ class -> Python path exceptions
        self.toolkit_order = toolkit_order if toolkit_order is not None else []   # generated toolkits, dependencies first
        self.include_dir = include_dir
        self.known = known_classes            # C++ class name -> package, for everything bound (previous runs + this run)
        self.toolkit_of = toolkit_of          # package -> toolkit
        self.templates = known_templates      # canonical instance key -> {toolkit, package, name}; updated while emitting
        self.local = {c.name for c in ir.classes}
        self.report: list[str] = []
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
            if skip_out and (p.is_out and not p.is_inout or p.stream == "out"):
                continue
            if p.default is None:
                parts.append(f'nb::arg("{p.name}")')
            else:
                # cast to the parameter's value type: a `char` default written as 0 must become a
                # 1-character str, an enum default written as an int must become the enum, etc.
                parts.append(f'nb::arg("{p.name}") = static_cast<std::decay_t<{p.type}>>({p.default})')
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
        return ", ".join(p.type for p in params)

    # ---- members -------------------------------------------------------------------------------
    def _lambda_call(self, cls: str | None, m: Method, self_type: str | None = None) -> str:
        """Lambda that maps out-params to a returned tuple (also handles static methods). self_type: the bound
        type when it differs from cls (non-copyable wrapper)."""
        ins = [p for p in m.params if (not p.is_out or p.is_inout) and p.stream != "out"]
        outs = [p for p in m.params if p.is_out]
        lam_params: list[str] = []
        if cls is not None and not m.is_static:
            lam_params.append(f"{'const ' if m.is_const else ''}{self_type if self_type is not None else cls} &self")
        lam_params += [f"const nanoocp::TextInput &{p.name}" if p.stream == "in" else f"{_strip_ref(p.type) if p.is_inout else p.type} {p.name}" for p in ins]
        body: list[str] = [f"{_strip_ref(p.type)} {p.name}{{}};" for p in outs if not p.is_inout]
        # streams: an ostream& parameter becomes a returned str; an istream&/stringstream parameter takes a text file-like
        # object (nanoocp::TextInput caster in nanoocp_common.h: typing.TextIO, never a str -- that would collide with the
        # file-path overloads such as BRepTools::Read(shape, path, builder))
        body += [f"std::ostringstream {p.name}_stream;" for p in m.params if p.stream == "out"]
        body += [f"std::stringstream {p.name}_stream({p.name}.text);" for p in m.params if p.stream == "in"]
        call_args = ", ".join(f"{p.name}_stream" if p.stream != "" else p.name for p in m.params)
        if cls is None:
            callee = f"{m.name}({call_args})"
        elif m.is_static:
            callee = f"{cls}::{m.name}({call_args})"
        else:
            callee = f"self.{m.name}({call_args})"
        results: list[str] = []
        if m.result_kind == "ptr_transient":
            body.append(f"opencascade::handle<{m.result_class}> result({callee});")
            results.append("result")
        elif m.result_kind == "ref_transient":
            body.append(f"opencascade::handle<{m.result_class}> result(&({callee}));")
            results.append("result")
        elif m.result != "void":
            body.append(f"auto result = {callee};")
            results.append("result")
        else:
            body.append(f"{callee};")
        results += [p.name for p in outs]
        results += [f"nanoocp_stream_text({p.name}_stream)" for p in m.params if p.stream == "out"]
        if len(results) == 1:
            body.append(f"return {results[0]};")
        elif len(results) > 1:
            body.append(f"return std::make_tuple({', '.join(results)});")
        return f"[]({', '.join(lam_params)}) {{ {' '.join(body)} }}"

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
        self._note_types(m.result, *(p.type for p in m.params))
        T = cls.name                       # member pointers name the class itself ...
        B = cls.bound_type                 # ... lambdas take the bound type (a wrapper for non-copyable classes)
        if m.result_kind == "ref_primitive":
            return self._ref_primitive(cls, m, py)
        has_out = any(p.is_out or p.stream != "" for p in m.params)
        wrap = m.result_kind in ("ptr_transient", "ref_transient")   # never let nanobind own a Transient
        policy = {"ptr_class": ", nb::rv_policy::reference", "ref_mutable": ", nb::rv_policy::reference_internal"}.get(m.result_kind, "")
        if m.name in _INPLACE_OPS:
            # OCCT in-place operators return void; Python expects self back
            lam = f"[]({B} &self{''.join(f', {p.type} {p.name}' for p in m.params)}) -> {B} & {{ self.{m.name}({', '.join(p.name for p in m.params)}); return self; }}"
            return f'.def("{py}", {lam}, nb::rv_policy::reference{self._extras(m.doc, m.params, False, True)})'
        if has_out or wrap:
            defn = "def_static" if m.is_static else "def"
            return f'.{defn}("{py}", {self._lambda_call(T, m, B)}{self._extras(m.doc, m.params, True, m.is_operator)})'
        ne = " noexcept" if m.is_noexcept else ""
        if m.is_static:
            fn = f"static_cast<{m.result} (*)({self._sig(m.params)}){ne}>(&{T}::{m.name})"
            return f'.def_static("{py}", {fn}{policy}{self._extras(m.doc, m.params, False, False)})'
        const = " const" if m.is_const else ""
        fn = f"static_cast<{m.result} ({T}::*)({self._sig(m.params)}){const}{ne}>(&{T}::{m.name})"
        return f'.def("{py}", {fn}{policy}{self._extras(m.doc, m.params, False, m.is_operator)})'

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
        if cls.is_transient:
            lam_params = ", ".join(f"{p.type} {p.name}" for p in params)
            call = ", ".join(p.name for p in params)
            fn = f"nb::new_([]({lam_params}) {{ return opencascade::handle<{cls.bound_type}>(new {cls.bound_type}({call})); }})"
        else:
            fn = f"nb::init<{self._sig(params)}>()"
        return f".def({fn}{self._extras(doc, params, False, False)})"

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
                if wrapped not in self.known and wrapped not in self.templates:
                    self.report.append(f"{key}: wrapped type {wrapped} is not bound -> instantiation skipped")
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
        if c.outer in skipped:
            self.report.append(f"{c.name}: outer class {c.outer} is not bound -> nested class skipped")
            skipped.add(c.name)
            return False
        for b in c.bases:
            if c.is_exception and b.startswith("std::"):
                continue
            if b not in self.known:
                self.report.append(f"{c.name}: base class {b} is not bound (package not generated) -> class skipped")
                skipped.add(c.name)
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
        ir = self.ir
        skipped: set[str] = set()
        classes = [c for c in self._ordered_classes() if self._base_ok(c, skipped)]
        instances = self._instances()   # registers this package's NCollection instantiations in self.templates (defaults may use them)
        free_ops: dict[str, list[str]] = {}
        module_fns: list[str] = []
        for fn in ir.functions:
            if fn.skip_reason is not None:
                continue
            if fn.is_operator:
                r = self._free_operator(fn)
                if r is None:
                    self.report.append(f"{fn.name}({self._sig(fn.params)}): free operator not mapped")
                else:
                    free_ops.setdefault(r[0], []).append(r[1])
            else:
                unbound = self._unbound_default(fn.params)
                if unbound is not None:
                    self.report.append(f"{fn.name}({self._sig(fn.params)}): default argument of unbound type {unbound} -> function skipped")
                    continue
                self._note_types(fn.result, *(p.type for p in fn.params))
                ne = " noexcept" if fn.is_noexcept else ""
                if fn.result_kind in ("ptr_transient", "ref_transient"):
                    self.report.append(f"{fn.name}({self._sig(fn.params)}): free function returning Transient pointer/reference not supported yet")
                    continue
                policy = {"ptr_class": ", nb::rv_policy::reference", "ref_mutable": ", nb::rv_policy::reference"}.get(fn.result_kind, "")
                qualified = fn.qualified if fn.qualified != "" else fn.name
                if any(p.is_out or p.stream != "" for p in fn.params):   # out-params/streams -> returned tuple, as for methods
                    as_method = Method(name=qualified, params=fn.params, result=fn.result, result_kind=fn.result_kind,
                                       result_class=fn.result_class, is_static=False, is_const=False, is_noexcept=fn.is_noexcept, doc=fn.doc)
                    module_fns.append(f'    {self._module(fn.scope)}.def("{py_safe(fn.name)}", {self._lambda_call(None, as_method)}{self._extras(fn.doc, fn.params, True, False)});')
                    continue
                module_fns.append(f'    {self._module(fn.scope)}.def("{py_safe(fn.name)}", static_cast<{fn.result} (*)({self._sig(fn.params)}){ne}>(&{qualified}){policy}{self._extras(fn.doc, fn.params, False, False)});')

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
        aliased: set[str] = set()      # instantiations already bound by another package: alias only
        for c in classes:
            self._note_types(*c.bases)
            if c.template_key != "":
                found = self.templates.get(c.template_key)
                if found is not None and found.get("by") != self.ir.name and not found.get("skipped", False):
                    declare.append(f'    m.attr("{c.py_name}") = nb::module_::import_("nanoocp._{found["toolkit"]}.{found["package"]}").attr("{found["name"]}");')
                    aliased.add(c.name)
                    continue
                self.templates[c.template_key] = {"toolkit": self.toolkit_of[self.ir.name], "package": self.ir.name, "name": c.py_name, "by": self.ir.name}
            if c.is_exception:
                declare.append(self._exception(c))
                continue
            # nanobind takes one base and reuses the derived pointer for it, so only the first (offset-0) base
            # can be declared; further bases are reported (their members are not inherited in Python)
            for extra in c.bases[1:]:
                self.report.append(f"{c.name}: additional base {extra} not declared (nanobind: single inheritance, offset-0 base only)")
            bases = "".join(f", {b}" for b in c.bases[:1])
            d = _cpp_doc(c.doc)
            doc_arg = f", {d}" if d is not None else ""
            if c.noncopyable:
                wrappers.append(f"// {c.name}: its copy/move constructors do not compile although declared (overrides.toml [skip] noncopyable):\n"
                                f"// bound through a wrapper with deleted copy and move, under the original name\n"
                                f"struct {c.bound_type} : {c.name} {{\n    using {c.name}::{c.name};\n"
                                f"    {c.bound_type}(const {c.bound_type} &) = delete;\n    {c.bound_type}({c.bound_type} &&) = delete;\n}};")
            declare.append(f'    {{ nb::class_<{c.bound_type}{bases}> cls({self._attr(c.scope)}, "{c.py_name}"{doc_arg});')
            for e in c.enums:
                declare += ["      " + l for l in self._enum(e, "cls")]
            declare.append("    }")

            body: list[str] = []
            implicit_default = False
            if c.is_exception or c.name in aliased:
                continue
            if not c.constructible:
                self.report.append(f"{c.name}: operator new is not public -> no constructors")
            if not c.is_abstract and c.constructible:
                declared = [k for k in c.ctors if k.skip_reason is None]
                # nanobind wants the zero-argument nb::new_ overload first; sort by required-parameter count
                declared.sort(key=lambda k: sum(1 for q in k.params if q.default is None))
                implicit_default = not c.has_declared_ctor    # emitted first (nanobind wants the zero-argument overload first)
                for k in declared:
                    unbound = self._unbound_default(k.params)
                    if unbound is not None:
                        self.report.append(f"{c.name}::{c.name}({self._sig(k.params)}): default argument of unbound type {unbound} -> constructor skipped")
                        continue
                    body.append(self._ctor(c, k.params, k.doc))
            bound = [m for m in c.methods if m.skip_reason is None]
            mixed = {m.name for m in bound if m.is_static} & {m.name for m in bound if not m.is_static}
            # overloads that become indistinguishable once out-params are dropped: nanobind takes the first registered.
            # An overload returning a scalar (double, bool, enum, str) without out-params is the direct C++ API and wins
            # (BRep_Tool::Parameter(V, E) -> double over Parameter(V, E, double&) -> bool; TopAbs::ShapeTypeFromString
            # -> enum); otherwise (void or a class result) the overload with the most out-params wins, as its values come
            # back as a tuple (gp_Pnt::Coord(x&, y&, z&) over Coord() -> gp_XYZ, Bnd_Box::Get(6 x double&) over Get() ->
            # Limits, OSD_Chronometer::Show(double&) over the printing Show()). The other overload is unreachable, reported.
            def preference(m: Method) -> tuple[int, int]:
                n_out = sum(1 for p in m.params if p.is_out and not p.is_inout)
                return (0, n_out) if m.result_scalar and n_out == 0 else (1, -n_out)
            def py_sig(m: Method) -> tuple:
                return (m.name, m.is_static, tuple(_strip_ref(p.type) for p in m.params if (not p.is_out or p.is_inout) and p.stream != "out"))
            groups: dict[tuple, list[Method]] = {}
            for m in bound:
                groups.setdefault(py_sig(m), []).append(m)
            ordered: list[Method] = []           # header order, except that a colliding group is emitted at its first member, winner first
            emitted: set[int] = set()
            for m in c.methods:
                if id(m) in emitted:
                    continue
                members = groups.get(py_sig(m), [m]) if m.skip_reason is None else [m]
                if len(members) > 1 and any(p.is_out for mm in members for p in mm.params):
                    members = sorted(members, key=preference)
                    for loser in members[1:]:
                        self.report.append(f"{c.name}::{loser.name}({self._sig(loser.params)}): same Python signature as "
                                           f"{loser.name}({self._sig(members[0].params)}) after out-param removal -> unreachable")
                else:
                    members = [m]
                for mm in members:
                    emitted.add(id(mm))
                    ordered.append(mm)
            for name in sorted(mixed):
                self.report.append(f"{c.name}::{name}: static overloads renamed to {name}_s (instance method of same name exists)")
            for m in ordered:
                s = self._method(c, m, mixed)
                if s is not None:
                    body.append(s)
            body += free_ops.get(c.name, [])
            for conv in c.conversions:          # operator bool/int/double() -> Python dunder; class targets: see conversions below
                dunder = {"bool": "__bool__", "int": "__int__", "float": "__float__"}.get(conv.kind)
                if dunder is not None:
                    self._note_types(conv.target)
                    body.append(f'.def("{dunder}", [](const {c.bound_type} &self) {{ return static_cast<{conv.target}>(self); }}{", " + _cpp_doc(conv.doc) if conv.doc != "" else ""})')
            if c.name in ir.hashable or c.template_key != "" and c.template_key.split("<", 1)[0] in ir.hashable_templates:
                # std::hash<T> specialised by OCCT (fully, or partially for a class template) -> hashability consistent with __eq__
                body.append(f'.def("__hash__", [](const {c.bound_type} &self) {{ return static_cast<Py_ssize_t>(std::hash<{c.name}>{{}}(self)); }})')
            cls_expr = f'nb::borrow<nb::class_<{c.bound_type}>>({self._attr(c.scope)}.attr("{c.py_name}"))'
            if implicit_default:
                define.append(f'    nanoocp_implicit_default_ctor<{c.bound_type}>({cls_expr});')
            if len(body) > 0:
                define.append(f'    {cls_expr}')
                define += ["        " + b for b in body]
                define[-1] += ";"
            # the implicit copy constructor (no user-declared one, TopoDS_Shape(const TopoDS_Vertex&)): bound when it exists,
            # after the declared constructors (nanobind wants a zero-argument nb::new_ before any other overload)
            if not c.is_abstract and c.constructible and not any(k.is_copy for k in c.ctors):
                define.append(f'    nanoocp_implicit_copy_ctor<{c.bound_type}>({cls_expr});')
            for f in c.fields:                 # read/write when the field type is copy-assignable (decided at compile time), else read-only
                self._note_types(f.type)
                dd = _cpp_doc(f.doc)
                define.append(f'    nanoocp_def_field({cls_expr}, "{py_safe(f.name)}", &{c.name}::{f.name}{", " + dd if dd is not None else ""});')
            if len(body) == 0 and len(c.fields) == 0:
                continue
            # C++ implicit conversions (non-explicit converting constructors) apply in Python too
            if not c.is_abstract and c.constructible:
                seen: set[str] = set()
                for k in c.ctors:
                    if k.skip_reason is None and k.is_implicit:
                        src = k.params[0].type
                        if src not in seen:
                            seen.add(src)
                            define.append(f"    nb::implicitly_convertible<std::decay_t<{src}>, {c.bound_type}>();")

        # operator T() const with a bound class T: T gets a constructor from this class, plus the implicit conversion when
        # the operator is not explicit (TopoDS_Shape s = aMakeShape; BRepGraph_NodeId(anEdgeId)). Emitted in a phase of its
        # own (after every definition of the toolkit: nanobind wants a class's zero-argument __new__ before other overloads)
        conversions: list[str] = []
        for c in classes:
            for conv in c.conversions:
                if conv.kind not in ("class", "handle"):
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
                helper = "nanoocp_conversion_handle" if conv.kind == "handle" else "nanoocp_conversion"
                conversions.append(f'    {helper}<{c.name}, {conv.target}>({target}, {"false" if conv.is_explicit else "true"});')
                self._note_types(conv.target)

        # typedefs of bound classes (using CurveD1 = Geom_Curve::ResD1 in namespace GeomGridEval) -> Python aliases;
        # scalar typedefs (Standard_Real) and the rest are not exposed
        seen_aliases: set[tuple[tuple[str, ...], str]] = set()
        for td in ir.typedefs:
            key = (td.scope, td.py_name)
            if key in seen_aliases or any(c.py_name == td.py_name and c.scope == td.scope for c in classes):
                continue                           # a 6c alias instantiation is a class of its own
            seen_aliases.add(key)
            inst = self.templates.get(td.target)
            if inst is not None and not inst.get("skipped", False) and inst["package"] != "":
                # alias of a bound NCollection instantiation (BVH_Array3d = NCollection_LinearVector<NCollection_Vec3<double>>)
                define.append(f'    {self._attr(td.scope)}.attr("{td.py_name}") = nb::module_::import_("nanoocp._{self.toolkit_of[inst["package"]]}.{inst["package"]}").attr("{inst["name"]}");   // {td.py_name} = {td.written}')
                continue
            pkg = self.known.get(td.target)
            if pkg is None or "<" in td.target:
                if td.scope != ():
                    self.report.append(f"{'::'.join(td.scope)}::{td.py_name} = {td.written}: type alias of an unbound type (not bound)")
                continue
            attrs = "".join(f'.attr("{a}")' for a in py_path(td.target, pkg, self.paths).split("."))
            src = (f'nb::module_::import_("nanoocp._{self.toolkit_of[pkg]}.{pkg}"){attrs}' if pkg != self.ir.name else f"m{attrs}")
            define.append(f'    {self._attr(td.scope)}.attr("{td.py_name}") = {src};   // {td.py_name} = {td.written}')

        includes = [f"#include <{h}>" for h in ir.prelude + ir.headers]
        if len(instances) > 0:
            includes.insert(0, '#include "nanoocp_ncollection.h"')
        for ident in sorted(self._idents):
            hdr = f"{ident}.hxx"
            if hdr not in ir.headers and (self.include_dir / hdr).exists():
                includes.append(f"#include <{hdr}>")

        out = [
            f"// Generated by the nanoOCP generator from OCCT package {ir.name} (toolkit {ir.toolkit}). Do not edit.",
            '#include "nanoocp_common.h"',
            *includes,
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
