"""libclang front end: parse one OCCT package as a single translation unit and build the IR."""
from __future__ import annotations

import platform
import re
import shutil
import subprocess
import tempfile
import tomllib
from pathlib import Path

from clang import cindex
from clang.cindex import AccessSpecifier as Access
from clang.cindex import CursorKind as K
from clang.cindex import TypeKind as TK

from .model import Class, Constant, Constructor, Enum, Field, Function, Method, PackageIR, Param, TemplateInstance
from .occt import OcctTree, Package

_PRIMITIVE_KINDS = {
    TK.BOOL, TK.CHAR_U, TK.UCHAR, TK.CHAR16, TK.CHAR32, TK.USHORT, TK.UINT, TK.ULONG,
    TK.ULONGLONG, TK.CHAR_S, TK.SCHAR, TK.WCHAR, TK.SHORT, TK.INT, TK.LONG, TK.LONGLONG,
    TK.FLOAT, TK.DOUBLE, TK.LONGDOUBLE, TK.ENUM,
}
_OVERRIDES = tomllib.loads((Path(__file__).parent / "overrides.toml").read_text())
_INOUT = set(_OVERRIDES.get("inout", []))
_SKIP_CLASSES = set(_OVERRIDES.get("skip", {}).get("classes", []))
_SKIP_HEADERS = set(_OVERRIDES.get("skip", {}).get("headers", []))
_SKIP_NAMESPACES = set(_OVERRIDES.get("skip", {}).get("namespaces", []))
_SKIP_METHODS = set(_OVERRIDES.get("skip", {}).get("methods", []))
_EXTRA_INSTANCES = list(_OVERRIDES.get("instantiate", {}).get("extra", []))

_UNSUPPORTED_RE = re.compile(
    r"std::(__\w+::)?((basic_)?(ostream|istream|iostream|stringstream|ostringstream|istringstream)|ios_base|ios|streambuf|"
    r"locale|thread|mutex|atomic|type_info|exception_ptr)\b"
)
# std templates nanobind casts (nanobind/stl/*.h, all included from nanoocp_common.h)
_STD_TEMPLATES_OK = {"shared_ptr", "unique_ptr", "vector", "map", "unordered_map", "set", "unordered_set", "pair",
                     "optional", "function", "tuple", "array", "variant", "list", "basic_string", "basic_string_view"}


def _resource_dir() -> str | None:
    clang = shutil.which("clang")
    if clang is None:
        return None
    rd = subprocess.run([clang, "-print-resource-dir"], capture_output=True, text=True, check=True).stdout.strip()
    if rd == "":
        return None
    return rd


def configure_libclang() -> str:
    """Prefer the libclang shipped with the clang on PATH (same version as the SDK/stdlib it was
    tested with); fall back to the pip 'libclang' wheel. Returns a description for logging."""
    rd = _resource_dir()
    if rd is not None:
        # <prefix>/lib/clang/<ver> -> <prefix>/lib/libclang.*
        lib_dir = Path(rd).parent.parent
        names = {"Darwin": ["libclang.dylib"], "Linux": ["libclang.so", "libclang-*.so*", "libclang.so.*"],
                 "Windows": ["libclang.dll"]}[platform.system()]
        for pattern in names:
            hits = sorted(lib_dir.glob(pattern)) + sorted((lib_dir.parent / "bin").glob(pattern))
            if len(hits) > 0:
                cindex.Config.set_library_file(str(hits[0]))
                return f"system libclang {hits[0]}"
    return "pip libclang"


def clang_args(tree: OcctTree) -> list[str]:
    args = ["-x", "c++", "-std=c++17", f"-I{tree.include_dir}", "-DHAVE_FREETYPE", "-DHAVE_RAPIDJSON"]
    rd = _resource_dir()
    if rd is not None:
        args += ["-resource-dir", rd]
    if platform.system() == "Darwin":
        sdk = subprocess.run(["xcrun", "--show-sdk-path"], capture_output=True, text=True, check=True).stdout.strip()
        if sdk != "":
            args += ["-isysroot", sdk]
    return args


def _doc(cursor: cindex.Cursor) -> str:
    raw = cursor.raw_comment
    if raw is None:
        return ""
    lines: list[str] = []
    for line in raw.splitlines():
        s = line.strip()
        for prefix in ("//!<", "//!", "///", "/**", "/*!", "/*", "*/", "*"):
            if s.startswith(prefix):
                s = s[len(prefix):]
                break
        if s.endswith("*/"):
            s = s[:-2]
        lines.append(s.strip())
    while len(lines) > 0 and lines[0] == "":
        lines.pop(0)
    while len(lines) > 0 and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def _default_expr(param: cindex.Cursor, scope: str, members: set[str]) -> str | None:
    """Default value as written, with unqualified references to static members / enumerators of the
    enclosing class qualified (the expression is emitted outside the class scope)."""
    toks = [t.spelling for t in param.get_tokens()]
    if "=" not in toks:
        return None
    expr = toks[toks.index("=") + 1:]
    if len(expr) == 0:
        return None
    if scope != "":
        for i, tok in enumerate(expr):
            if tok in members and (i == 0 or expr[i - 1] != "::") and not (i + 1 < len(expr) and expr[i + 1] == "("):
                expr[i] = f"{scope}::{tok}"
    # names from a namespace, written unqualified thanks to the enclosing namespace or a using-directive
    # (MathRoot: `double theSupBound = THE_2PI` with `using namespace MathUtils`): qualify via the AST reference
    for ref in param.walk_preorder():
        if ref.kind not in (K.DECL_REF_EXPR, K.TYPE_REF) or ref.referenced is None:
            continue
        target = ref.referenced
        qualified = _namespace_qualified(target)
        if qualified is None:
            continue
        for i, tok in enumerate(expr):
            if tok == target.spelling and (i == 0 or expr[i - 1] != "::"):
                expr[i] = qualified
    return _apply_subst(" ".join(expr))          # template parameters in defaults (Element_t(0)) while instantiating.replace(" (", "(").replace("( ", "(").replace(" )", ")").replace(" ::", "::").replace(":: ", "::")


def _namespace_qualified(decl: cindex.Cursor) -> str | None:
    """Fully qualified name of a declaration whose enclosing scopes include a (named) namespace; None otherwise."""
    parts = [decl.spelling]
    parent = decl.semantic_parent
    has_namespace = False
    while parent is not None and parent.kind != K.TRANSLATION_UNIT:
        if parent.kind == K.NAMESPACE:
            if parent.spelling == "":
                return None
            has_namespace = True
            parts.append(parent.spelling)
        elif parent.kind in (K.CLASS_DECL, K.STRUCT_DECL, K.CLASS_TEMPLATE):
            parts.append(parent.spelling)
        elif parent.kind == K.ENUM_DECL:
            if parent.is_scoped_enum():
                parts.append(parent.spelling)
        else:
            return None
        parent = parent.semantic_parent
    if not has_namespace:
        return None
    return "::".join(reversed(parts))


def _is_out_param(t: cindex.Type) -> bool:
    if t.kind != TK.LVALUEREFERENCE:
        return False
    pointee = t.get_pointee()
    if pointee.is_const_qualified():
        return False
    return pointee.get_canonical().kind in _PRIMITIVE_KINDS


_subst: dict[str, str] = {}          # template parameter -> argument while walking a class template (alias instantiation)
_subst_self: tuple[str, str] | None = None   # (template name, full instantiation) for the injected class name


def _apply_subst(spelling: str) -> str:
    if len(_subst) == 0:
        return spelling
    out = spelling
    for param, arg in _subst.items():
        out = re.sub(rf"\b{re.escape(param)}\b", arg, out)
    if _subst_self is not None:
        tmpl, full = _subst_self
        out = re.sub(rf"\b{re.escape(tmpl)}\b(?!\s*<)", full, out)      # injected class name: math_VectorBase -> math_VectorBase<double>
    return out


def _type_spelling(t: cindex.Type) -> str:
    """Type as written in the header (keeps portable typedef names such as Standard_Size), except that
    types nested in a class are spelled fully qualified (the header may say 'D' inside gp_Dir). While a
    class template is walked for an alias instantiation, template parameters are substituted."""
    return _apply_subst(_type_spelling_raw(t))


def _in_user_namespace(decl: cindex.Cursor) -> bool:
    """True for a declaration inside an OCCT namespace (TopoDS::Vertex, Geom2dGridEval::CurveD1), false for std."""
    parent = decl.semantic_parent
    return (parent is not None and parent.kind == K.NAMESPACE and parent.spelling != ""
            and parent.spelling != "std" and not parent.spelling.startswith("__"))


def _type_spelling_raw(t: cindex.Type) -> str:
    base = t
    suffix = ""                      # qualifiers/declarators outside the base type, rebuilt below
    while base.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE, TK.POINTER):
        suffix = {TK.LVALUEREFERENCE: " &", TK.RVALUEREFERENCE: " &&", TK.POINTER: " *"}[base.kind] + (" const" if base.is_const_qualified() else "") + suffix
        base = base.get_pointee()
    decl = base.get_declaration()
    if decl.kind != K.NO_DECL_FOUND:
        parent = decl.semantic_parent
        if parent is not None and parent.kind in (K.CLASS_DECL, K.STRUCT_DECL, K.CLASS_TEMPLATE):
            return t.get_canonical().spelling
        # a plain class in an OCCT namespace may be written unqualified inside that namespace (class Full : public Base)
        if decl.kind in (K.CLASS_DECL, K.STRUCT_DECL, K.ENUM_DECL) and _in_user_namespace(decl) \
                and base.get_canonical().get_num_template_arguments() <= 0:
            return t.get_canonical().spelling
    canon_base = base.get_canonical()
    if canon_base.kind == TK.RECORD and canon_base.get_num_template_arguments() > 0 and "<" in base.spelling:
        # template arguments may themselves be nested types (NCollection_List<TwoIntegers>): respell each one.
        # Non-type arguments (BVH_Box<double, 3>, Standard_Static_Assert<true>) have no type: keep the spelling as written.
        arg_types = [canon_base.get_template_argument_type(i) for i in range(canon_base.get_num_template_arguments())]
        if all(a.kind != TK.INVALID for a in arg_types):
            head = base.spelling[: base.spelling.index("<")].replace("const ", "").strip()
            args = [_type_spelling(a) for a in arg_types]
            return ("const " if base.is_const_qualified() else "") + f"{head}<{', '.join(args)}>" + suffix
    s = t.spelling
    for kw in ("class ", "struct ", "enum "):
        s = s.replace(kw, "")
    return s


def _py_identifier(cpp_name: str) -> str:
    """Python name for a C++ type: identity for plain classes; template instantiations (which OCCT 8 does not
    typedef) become template__arg1__arg2 with OCCT's Handle_X convention for handle<X>, nested left to right:
    NCollection_DataMap<TopoDS_Shape, handle<Geom_Surface>> -> NCollection_DataMap__TopoDS_Shape__Handle_Geom_Surface."""
    s = cpp_name
    while True:
        t = re.sub(r"(?:opencascade::|occ::)?handle<([^<>]+)>", r"Handle_\1", s)
        if t == s:
            break
        s = t
    s = s.replace("::", "_")
    s = re.sub(r"\s*<\s*", "__", s)
    s = re.sub(r"\s*,\s*", "__", s)
    s = re.sub(r"\s*>\s*", "", s)
    s = re.sub(r"[^A-Za-z0-9_]", "_", s)
    return s


def py_path(cpp_name: str, package: str) -> str:
    """Python attribute path of a bound C++ type relative to nanoocp.<package>: nested classes and namespaces keep
    their C++ nesting (gp_Dir::D -> gp_Dir.D, Geom2dEval_RepCurveDesc::Base -> Geom2dEval_RepCurveDesc.Base);
    a namespace named like the package is the package module itself (Geom2dGridEval::CurveD1 -> CurveD1)."""
    if "<" in cpp_name:
        return _py_identifier(cpp_name)
    parts = cpp_name.split("::")
    if len(parts) > 1 and parts[0] == package:
        parts = parts[1:]
    return ".".join(parts)


def _unsupported(t: cindex.Type, allow_out: bool) -> str | None:
    canon = t.get_canonical()
    cs = canon.spelling
    if _UNSUPPORTED_RE.search(cs) is not None:
        return "iostream type"
    if canon.kind == TK.RVALUEREFERENCE:
        return "rvalue reference"
    if canon.kind in (TK.CONSTANTARRAY, TK.INCOMPLETEARRAY, TK.VARIABLEARRAY):
        return "array"
    if canon.kind == TK.POINTER:
        pointee = canon.get_pointee()
        pk = pointee.get_canonical().kind
        if pk == TK.RECORD:
            d = pointee.get_declaration()
            # template instantiations (NCollection_Array1<double>*) have no definition cursor in the TU but are complete
            if d.kind == K.NO_DECL_FOUND or (d.get_definition() is None and pointee.get_canonical().get_num_template_arguments() <= 0):
                return "pointer to incomplete type"
        if pk == TK.FUNCTIONPROTO or pk == TK.FUNCTIONNOPROTO:
            return "function pointer"
        if pk == TK.VOID:
            return "void pointer"
        if pk in (TK.CHAR_S, TK.CHAR_U) and pointee.is_const_qualified():
            return None            # const char* is fine
        if pk in _PRIMITIVE_KINDS or pk == TK.POINTER:
            return "raw pointer to primitive"
    if canon.kind == TK.MEMBERPOINTER:
        return "member pointer"
    base = canon
    while base.kind in (TK.LVALUEREFERENCE, TK.POINTER):
        base = base.get_pointee().get_canonical()
    if base.kind == TK.RECORD:
        decl = base.get_declaration()
        parent = decl.semantic_parent
        if parent is not None and parent.kind == K.NAMESPACE and parent.spelling in ("std", "__1"):
            if base.get_num_template_arguments() > 0:
                if decl.spelling not in _STD_TEMPLATES_OK:
                    return f"std::{decl.spelling}"
                if decl.spelling in ("basic_string", "basic_string_view"):
                    if base.get_template_argument_type(0).get_canonical().kind in (TK.CHAR_S, TK.CHAR_U):
                        return None
                    return f"std::{decl.spelling} of non-char"
                for i in range(base.get_num_template_arguments()):
                    arg = base.get_template_argument_type(i)
                    if arg.kind == TK.INVALID:
                        continue
                    r = _unsupported(arg, allow_out=False)
                    if r is not None:
                        return f"std::{decl.spelling} of {r}"
                    ad = arg.get_canonical().get_declaration()
                    if ad.kind in (K.CLASS_DECL, K.STRUCT_DECL) and ad.semantic_parent is not None \
                            and ad.semantic_parent.kind in (K.CLASS_DECL, K.STRUCT_DECL) and ad.access_specifier != Access.PUBLIC:
                        return f"std::{decl.spelling} of non-public nested class {ad.spelling}"
        elif parent is not None and parent.kind in (K.CLASS_DECL, K.STRUCT_DECL) and base.get_num_template_arguments() == 0:
            pass
    if canon.kind == TK.LVALUEREFERENCE and canon.get_pointee().get_canonical().kind == TK.POINTER:
        return "reference to pointer"
    if canon.kind == TK.LVALUEREFERENCE and not allow_out:
        pointee = canon.get_pointee()
        if not pointee.is_const_qualified() and pointee.get_canonical().kind in _PRIMITIVE_KINDS:
            return "reference to primitive"
    return None


def _result_kind(t: cindex.Type) -> tuple[str, str]:
    """How a returned pointer/reference must be treated (see Design.md section 6)."""
    canon = t.get_canonical()
    if canon.kind not in (TK.POINTER, TK.LVALUEREFERENCE):
        return "value", ""
    pointee = canon.get_pointee()
    decl = pointee.get_declaration()
    if decl.kind not in (K.CLASS_DECL, K.STRUCT_DECL):
        return "other", ""
    name = _type_spelling(pointee).replace("const ", "").strip()
    if _derives_from(decl, "Standard_Transient"):
        return ("ptr_transient" if canon.kind == TK.POINTER else "ref_transient"), name
    if canon.kind == TK.POINTER:
        return "ptr_class", name
    if not pointee.is_const_qualified():
        return "ref_mutable", name
    return "value", name


def _params(cursor: cindex.Cursor, qualified: str = "", scope: str = "", members: set[str] | None = None) -> tuple[list[Param], str | None]:
    params: list[Param] = []
    inout = qualified in _INOUT
    if members is None:
        members = set()
    for i, p in enumerate(cursor.get_arguments()):
        reason = _unsupported(p.type, allow_out=True)
        if reason is None and "type-parameter-" in _type_spelling(p.type):
            reason = "dependent type (unresolved template parameter)"
        if reason is not None:
            return params, f"param '{p.spelling}': {reason}"
        name = p.spelling
        if name == "":
            name = f"arg{i}"
        is_out = _is_out_param(p.type)
        _note_instance(p.type)
        params.append(Param(name=name, type=_type_spelling(p.type), default=_default_expr(p, scope, members), is_out=is_out, is_inout=is_out and inout))
    if cursor.type.kind == TK.FUNCTIONPROTO and cursor.type.is_function_variadic():
        return params, "variadic"
    return params, None


def _is_noexcept(cursor: cindex.Cursor) -> bool:
    k = cursor.exception_specification_kind
    return k in (cindex.ExceptionSpecificationKind.BASIC_NOEXCEPT, cindex.ExceptionSpecificationKind.DYNAMIC_NONE)


_derives_cache: dict[tuple[str, str], bool] = {}


def _derives_from(cls: cindex.Cursor, root: str) -> bool:
    """True if cls is root or (transitively) derives from it, following the AST base specifiers."""
    name = cls.spelling
    if name == root:
        return True
    key = (name, root)
    if key in _derives_cache:
        return _derives_cache[key]
    result = False
    for b in cls.get_children():
        if b.kind == K.CXX_BASE_SPECIFIER:
            d = b.type.get_declaration()
            if d.kind != K.NO_DECL_FOUND and _derives_from(d, root):
                result = True
                break
    _derives_cache[key] = result
    return result


def _enum(cursor: cindex.Cursor, header: str, scope: str | None) -> Enum:
    qual = f"{scope}::{cursor.spelling}" if scope is not None else cursor.spelling
    values: list[tuple[str, str]] = []
    for v in cursor.get_children():
        if v.kind == K.ENUM_CONSTANT_DECL:
            cpp = f"{qual}::{v.spelling}" if cursor.is_scoped_enum() else (f"{scope}::{v.spelling}" if scope is not None else v.spelling)
            values.append((v.spelling, cpp))
    return Enum(name=qual, py_name=cursor.spelling, values=values, is_scoped=cursor.is_scoped_enum(), doc=_doc(cursor), header=header,
                is_anonymous=cursor.is_anonymous() or cursor.spelling == "" or cursor.spelling.startswith("("))


def _method(cursor: cindex.Cursor, cls_name: str, members: set[str]) -> Method | None:
    name = cursor.spelling
    if name.startswith("operator") and name in ("operator=", "operator new", "operator delete", "operator new[]", "operator delete[]"):
        return None
    params, reason = _params(cursor, f"{cls_name}::{name}", cls_name, members)
    _note_instance(cursor.result_type)
    rk, rc = _result_kind(cursor.result_type)
    m = Method(name=name, params=params, result=_type_spelling(cursor.result_type), result_kind=rk, result_class=rc,
               is_static=cursor.is_static_method(),
               is_const=cursor.is_const_method(), is_noexcept=_is_noexcept(cursor), doc=_doc(cursor),
               is_operator=name.startswith("operator"), skip_reason=reason)
    if m.skip_reason is None:
        m.skip_reason = _unsupported(cursor.result_type, allow_out=False)
        if m.skip_reason is None and "type-parameter-" in m.result:
            m.skip_reason = "dependent type (unresolved template parameter)"
        if m.skip_reason is not None:
            m.skip_reason = "return: " + m.skip_reason
    # inline (in-class or out-of-class in the header) vs. defined in the library; needs bodies parsed
    m.defined_in_header = (cursor.is_definition() or cursor.get_definition() is not None
                           or cursor.is_pure_virtual_method())      # pure virtual: dispatched via vtable, no symbol
    if m.skip_reason is None and cursor.is_deleted_method():
        m.skip_reason = "deleted"
    if m.skip_reason is None:
        sig = f"{cls_name}::{name}({', '.join(p.type for p in params)})"
        if f"{cls_name}::{name}" in _SKIP_METHODS or sig in _SKIP_METHODS:
            m.skip_reason = "overrides.toml [skip] methods"
    if m.skip_reason is None and cursor.availability == cindex.AvailabilityKind.DEPRECATED:
        m.skip_reason = "deprecated"
    return m


def _class(cursor: cindex.Cursor, header: str, package: str, outer: str = "") -> Class:
    cpp_name = _type_spelling(cursor.type)          # 'NCollection_Lerp<gp_Trsf>' for a specialization
    path = py_path(cpp_name, package).split(".")
    c = Class(name=cpp_name, py_name=path[-1], bases=[], header=header, doc=_doc(cursor),
              is_transient=_derives_from(cursor, "Standard_Transient"),
              is_exception=_derives_from(cursor, "Standard_Failure"), is_abstract=cursor.is_abstract_record(),
              scope=tuple(path[:-1]), outer=outer)
    members: set[str] = set()      # names usable unqualified inside the class (for default arguments)
    for ch in cursor.get_children():
        if ch.kind in (K.VAR_DECL, K.FIELD_DECL, K.ENUM_DECL, K.TYPEDEF_DECL, K.TYPE_ALIAS_DECL, K.CLASS_DECL, K.STRUCT_DECL):
            members.add(ch.spelling)
        if ch.kind == K.ENUM_DECL:
            members.update(v.spelling for v in ch.get_children() if v.kind == K.ENUM_CONSTANT_DECL)
    # nanobind constructs value types with placement new: possible only if the class declares no
    # operator new at all, or a public operator new(size_t, void*) (DEFINE_STANDARD_ALLOC does).
    news = [ch for ch in cursor.get_children() if ch.kind == K.CXX_METHOD and ch.spelling == "operator new"]
    if len(news) > 0 and not any(ch.access_specifier == Access.PUBLIC and len(list(ch.get_arguments())) == 2
                                 and list(ch.get_arguments())[1].type.get_canonical().spelling == "void *" for ch in news):
        c.constructible = False
    for ch in cursor.get_children():
        if ch.kind == K.CXX_BASE_SPECIFIER:
            if ch.access_specifier != Access.PUBLIC:
                c.skipped.append(f"{c.name}: non-public base {_type_spelling(ch.type)} dropped; class not constructible")
                c.constructible = False
                continue
            c.bases.append(_type_spelling(ch.type))
            continue
        if ch.kind == K.CONSTRUCTOR:
            c.has_declared_ctor = True
        if ch.access_specifier != Access.PUBLIC:
            continue
        if ch.kind == K.CONSTRUCTOR:
            if ch.is_move_constructor() or ch.is_deleted_method():
                continue
            params, reason = _params(ch, "", c.name, members)
            required = [q for q in params if q.default is None]
            implicit = (len(params) >= 1 and len(required) <= 1 and not ch.is_explicit_method()
                        and not ch.is_copy_constructor() and not ch.is_move_constructor())
            ctor = Constructor(params=params, doc=_doc(ch), skip_reason=reason, is_implicit=implicit)
            if ctor.skip_reason is None and ch.availability == cindex.AvailabilityKind.DEPRECATED:
                ctor.skip_reason = "deprecated"
            if ctor.skip_reason is not None:
                c.skipped.append(f"{c.name}::{c.name}({', '.join(p.type for p in params)}): {ctor.skip_reason}")
            c.ctors.append(ctor)
        elif ch.kind == K.CXX_METHOD:
            m = _method(ch, c.name, members)
            if m is None:
                continue
            if m.skip_reason is not None:
                c.skipped.append(f"{c.name}::{m.name}({', '.join(p.type for p in m.params)}): {m.skip_reason}")
            c.methods.append(m)
        elif ch.kind == K.FIELD_DECL:
            reason = _unsupported(ch.type, allow_out=False)
            if reason is None and ch.type.get_canonical().kind in (TK.CONSTANTARRAY, TK.INCOMPLETEARRAY, TK.VARIABLEARRAY):
                reason = "array"
            if reason is None and ch.type.get_canonical().kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE):
                reason = "reference member (no pointer-to-member)"
            if reason is not None:
                c.skipped.append(f"{c.name}::{ch.spelling}: field {reason}")
                continue
            c.fields.append(Field(name=ch.spelling, type=_type_spelling(ch.type), is_const=ch.type.is_const_qualified(), doc=_doc(ch)))
        elif ch.kind == K.ENUM_DECL and ch.is_definition():
            c.enums.append(_enum(ch, header, c.name))
        elif ch.kind in (K.FUNCTION_TEMPLATE,):
            c.skipped.append(f"{c.name}::{ch.spelling}: template member")
        elif ch.kind in (K.CLASS_DECL, K.STRUCT_DECL) and ch.is_definition():
            if ch.spelling == "":
                c.skipped.append(f"{c.name}: anonymous nested struct")
            elif len(_subst) > 0:
                c.skipped.append(f"{cursor.spelling}::{ch.spelling}: nested class of a class template (alias instantiation)")
            else:
                c.nested.append(_class(ch, header, package, outer=c.name))
        elif ch.kind == K.CLASS_TEMPLATE:
            c.skipped.append(f"{c.name}::{ch.spelling}: nested class template")
    return c


_instances_seen: dict[str, TemplateInstance] = {}    # filled while parsing a package (reset per package)


def _canonical_args(t: cindex.Type) -> str:
    """Portable canonical spelling of a type used as a template argument (typedefs resolved, std::__1 stripped)."""
    return re.sub(r"std::__\w+::", "std::", t.get_canonical().spelling)


def _note_instance(t: cindex.Type) -> None:
    """If t (or its pointee) is an instantiation of an NCollection template we have a binder for, record it,
    including nested instantiations in its arguments."""
    from .ncollection import BINDERS
    canon = t.get_canonical()
    while canon.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE, TK.POINTER):
        canon = canon.get_pointee().get_canonical()
    if canon.kind != TK.RECORD or canon.get_num_template_arguments() <= 0:
        return
    decl = canon.get_declaration()
    if decl.spelling == "handle":       # opencascade::handle<NCollection_HArray1<T>> -> look inside
        _note_instance(canon.get_template_argument_type(0))
        return
    if decl.spelling not in BINDERS:
        return
    from .ncollection import instance_args
    all_args = [_canonical_args(canon.get_template_argument_type(i)) for i in range(canon.get_num_template_arguments())]
    args = instance_args(decl.spelling, all_args)     # default hashers are not part of the key/name
    for i in range(len(args)):
        _note_instance(canon.get_template_argument_type(i))
    key = f"{decl.spelling}<{', '.join(args)}>"
    _instances_seen.setdefault(key, TemplateInstance(template=decl.spelling, args=args, key=key, element=args[0]))


def _split_top(text: str) -> list[str]:
    out, depth, cur = [], 0, ""
    for ch in text:
        depth += ch == "<"
        depth -= ch == ">"
        if ch == "," and depth == 0:
            out.append(cur.strip()); cur = ""
        else:
            cur += ch
    out.append(cur.strip())
    return out


def _find_class_template(tu: cindex.TranslationUnit, name: str) -> tuple[cindex.Cursor | None, list[list[str]]]:
    """The template's definition plus the parameter names of every declaration (a forward declaration may
    name the parameters differently, and libclang spells some dependent types with those names)."""
    definition = None
    param_lists: list[list[str]] = []
    for cur in tu.cursor.get_children():
        if cur.kind == K.CLASS_TEMPLATE and cur.spelling == name:
            param_lists.append([p.spelling for p in cur.get_children() if p.kind in (K.TEMPLATE_TYPE_PARAMETER, K.TEMPLATE_NON_TYPE_PARAMETER)])
            if cur.is_definition():
                definition = cur
    return definition, param_lists


def _alias_instance(tu: cindex.TranslationUnit, cur: cindex.Cursor, header: str, package: str, report: list[str]) -> Class | None:
    """using math_Vector = math_VectorBase<double>; -> the template's members instantiated for these arguments
    (Design.md 6c). NCollection containers (hand-written binders) and std types are not handled here."""
    from .ncollection import BINDERS
    t = cur.underlying_typedef_type
    canon = t.get_canonical()
    if canon.kind != TK.RECORD or canon.get_num_template_arguments() <= 0 or "<" not in t.spelling:
        return None
    tmpl_name = canon.get_declaration().spelling
    if tmpl_name in BINDERS or tmpl_name == "handle" or t.spelling.startswith("std::"):
        return None
    tmpl, param_lists = _find_class_template(tu, tmpl_name)
    if tmpl is None:
        report.append(f"{cur.spelling} = {t.spelling}: class template {tmpl_name} not found in the translation unit")
        return None
    params = [p for p in tmpl.get_children() if p.kind in (K.TEMPLATE_TYPE_PARAMETER, K.TEMPLATE_NON_TYPE_PARAMETER)]
    # arguments as written, from the canonical type when the alias goes through a metafunction
    # (BVH_Vec3d = BVH::VectorType<double, 3>::Type resolves to NCollection_Vec3<double>)
    spelled = t.spelling if t.spelling.split("<", 1)[0].split("::")[-1] == tmpl_name else canon.spelling
    if "<" not in spelled:
        report.append(f"{cur.spelling} = {t.spelling}: cannot read template arguments")
        return None
    written = _split_top(spelled[spelled.index("<") + 1 : spelled.rindex(">")])
    n = canon.get_num_template_arguments()
    if len(params) < n or len(written) > n:
        report.append(f"{cur.spelling} = {t.spelling}: cannot match template arguments")
        return None
    args: list[str] = []
    keys: list[str] = []
    for i in range(n):
        at = canon.get_template_argument_type(i)
        if at.kind != TK.INVALID:
            args.append(_type_spelling_raw(at)); keys.append(_canonical_args(at))
        elif i < len(written):
            args.append(written[i]); keys.append(written[i])          # non-type argument, as written
        else:
            report.append(f"{cur.spelling} = {t.spelling}: defaulted non-type argument not supported")
            return None
    global _subst, _subst_self
    full = f"{tmpl_name}<{', '.join(args)}>"
    _subst = {}
    for names in param_lists:                      # every declaration's parameter names, position-wise
        for name, a in zip(names, args):
            _subst.setdefault(name, a)
    _subst_self = (tmpl_name, full)
    try:
        c = _class(tmpl, header, package)
    finally:
        _subst = {}
        _subst_self = None
    c.name = full
    c.py_name = cur.spelling
    c.template_key = f"{tmpl_name}<{', '.join(keys)}>"
    c.doc = c.doc if c.doc != "" else _doc(cur)
    for m in c.methods:
        m.defined_in_header = True            # instantiated from the header, no library symbol involved
    return c


def _prefixes(scope: tuple[str, ...]) -> list[tuple[str, ...]]:
    """('A', 'B') -> [('A',), ('A', 'B')]"""
    return [scope[:i] for i in range(1, len(scope) + 1)]


def parse_package(tree: OcctTree, pkg: Package, args: list[str] | None = None) -> PackageIR:
    if args is None:
        args = clang_args(tree)
    ir = PackageIR(name=pkg.name, toolkit=pkg.toolkit, headers=[h for h in pkg.headers if h not in _SKIP_HEADERS])
    for h in pkg.headers:
        if h in _SKIP_HEADERS:
            ir.report.append(f"{h}: skipped (overrides.toml [skip] headers)")
    headers = set(ir.headers)
    _instances_seen.clear()
    with tempfile.TemporaryDirectory() as td:
        umbrella = Path(td) / f"{pkg.name}__all.hxx"
        # prelude: some OCCT headers are not self-contained (MathUtils_Config.hxx uses size_t with only <limits>)
        umbrella.write_text("#include <cstddef>\n#include <cstdint>\n#include <cstring>\n#include <string>\n"
                            + "".join(f"#include <{h}>\n" for h in ir.headers))
        index = cindex.Index.create()
        # bodies are parsed (no PARSE_SKIP_FUNCTION_BODIES): only then does get_definition() find the
        # out-of-class inline definitions that decide whether a method needs a library symbol
        tu = index.parse(str(umbrella), args=args)
        errors = [d for d in tu.diagnostics if d.severity >= cindex.Diagnostic.Error]
        if len(errors) > 0:
            raise RuntimeError(f"{pkg.name}: {len(errors)} parse errors, first: {errors[0]}")
        def top_level(cursor: cindex.Cursor, ns: str):
            """File-scope declarations, descending into namespaces (OCCT 8 math packages use them)."""
            for cur in cursor.get_children():
                f = cur.location.file
                if f is None:
                    continue
                if Path(f.name).name not in headers:
                    continue
                if cur.kind == K.NAMESPACE:
                    yield from top_level(cur, f"{ns}{cur.spelling}::")
                else:
                    yield cur, ns

        def add_class(c: Class) -> None:
            ir.classes.append(c)
            for n in c.nested:               # nested classes are bound after (and into) their outer class
                add_class(n)

        for cur, ns in top_level(tu.cursor, ""):
            header = Path(cur.location.file.name).name
            # a namespace named like the package is the package module itself (TopoDS::Vertex -> nanoocp.TopoDS.Vertex);
            # every other namespace becomes a submodule (Geom2dEval_RepCurveDesc::Base -> nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base)
            ns_parts = ns.rstrip(":").split("::") if ns != "" else []
            if "" in ns_parts:
                ir.report.append(f"{header}: {cur.spelling}: anonymous namespace (not bound)")
                continue
            if any(part in _SKIP_NAMESPACES for part in ns_parts):
                if cur.is_definition() or cur.kind == K.FUNCTION_DECL:
                    ir.report.append(f"{ns}{cur.spelling}: namespace skipped (overrides.toml [skip] namespaces)")
                continue
            if len(ns_parts) > 0 and ns_parts[0] == pkg.name:
                ns_parts = ns_parts[1:]
            scope = tuple(ns_parts)
            if ns != "" and cur.kind == K.VAR_DECL and cur.type.is_const_qualified():
                # namespace-level constants (constexpr double MathUtils::THE_NEWTON_FTOL_SQ = ...) -> module attributes
                ir.constants.append(Constant(py_name=cur.spelling, cpp=f"{ns}{cur.spelling}", doc=_doc(cur), scope=scope))
                continue
            if ns != "" and cur.kind in (K.FUNCTION_TEMPLATE, K.CLASS_TEMPLATE):
                ir.report.append(f"{ns}{cur.spelling}: template in namespace (not bound)")
                continue
            if ns != "" and cur.kind in (K.TYPEDEF_DECL, K.TYPE_ALIAS_DECL):
                ir.report.append(f"{ns}{cur.spelling}: type alias in namespace (not bound)")
                continue
            if cur.kind in (K.CLASS_DECL, K.STRUCT_DECL) and cur.is_definition():
                c = _class(cur, header, pkg.name)
                if c.name in _SKIP_CLASSES:
                    ir.report.append(f"{c.name}: skipped (overrides.toml [skip])")
                    continue
                add_class(c)
            elif cur.kind == K.ENUM_DECL and cur.is_definition():
                e = _enum(cur, header, ns.rstrip(":") if ns != "" else None)
                e.scope = scope
                ir.enums.append(e)
            elif cur.kind == K.FUNCTION_DECL:
                params, reason = _params(cur, f"{ns}{cur.spelling}")
                rk, rc = _result_kind(cur.result_type)
                fn = Function(name=cur.spelling, params=params, result=_type_spelling(cur.result_type),
                              result_kind=rk, result_class=rc,
                              is_noexcept=_is_noexcept(cur), doc=_doc(cur), header=header,
                              is_operator=cur.spelling.startswith("operator"), skip_reason=reason,
                              qualified=f"{ns}{cur.spelling}", scope=scope)
                if fn.skip_reason is None:
                    fn.skip_reason = _unsupported(cur.result_type, allow_out=False)
                if fn.skip_reason is not None:
                    ir.report.append(f"{fn.name}(...): {fn.skip_reason}")
                ir.functions.append(fn)
            elif cur.kind in (K.TYPEDEF_DECL, K.TYPE_ALIAS_DECL):
                ir.typedefs.append((cur.spelling, _type_spelling(cur.underlying_typedef_type)))
                if not any(c.py_name == cur.spelling for c in ir.classes):     # the same alias appears in several headers
                    inst = _alias_instance(tu, cur, header, pkg.name, ir.report)
                    if inst is not None:
                        ir.classes.append(inst)
            elif cur.kind in (K.CLASS_TEMPLATE, K.FUNCTION_TEMPLATE):
                ir.report.append(f"{cur.spelling}: template (not bound)")
    for c in ir.classes:
        ir.report.extend(c.skipped)
    # every namespace with a bound member, outer ones first (the emitter creates the submodules in this order);
    # nested classes are excluded: their scope ends in class names
    namespaces = {sc for c in ir.classes if c.outer == "" for sc in _prefixes(c.scope)}
    namespaces |= {sc for e in ir.enums for sc in _prefixes(e.scope)}
    namespaces |= {sc for f in ir.functions if f.skip_reason is None for sc in _prefixes(f.scope)}
    namespaces |= {sc for k in ir.constants for sc in _prefixes(k.scope)}
    ir.namespaces = sorted(namespaces)
    # only instances referenced by members that are actually bound matter, but the over-approximation
    # (every signature seen) is harmless: an unused instantiation just costs compile time
    ir.instances = dict(_instances_seen)
    if pkg.name == "NCollection":
        from .ncollection import BINDERS
        for spelled in _EXTRA_INSTANCES:
            m = re.match(r"(\w+)<(.+)>$", spelled)
            if m is None or m.group(1) not in BINDERS:
                ir.report.append(f"overrides [instantiate]: cannot parse or no binder for {spelled}")
                continue
            args = [a.strip() for a in m.group(2).split(",")]
            ir.instances.setdefault(spelled, TemplateInstance(template=m.group(1), args=args, key=spelled, element=args[0]))
    return ir
