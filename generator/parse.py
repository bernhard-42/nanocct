"""libclang front end: parse one OCCT package as a single translation unit and build the IR."""
from __future__ import annotations

import ctypes
import keyword
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

from .binders import BINDERS, instance_args
from .model import (Class, Constant, Constructor, Conversion, ConversionKind, Enum, Field, Function, Method, PackageIR, Param,
                    ResultKind, StreamKind, TemplateInstance, TypeAlias)
from .occt import OcctTree, Package

_PRIMITIVE_KINDS = {
    TK.BOOL, TK.CHAR_U, TK.UCHAR, TK.CHAR16, TK.CHAR32, TK.USHORT, TK.UINT, TK.ULONG,
    TK.ULONGLONG, TK.CHAR_S, TK.SCHAR, TK.WCHAR, TK.SHORT, TK.INT, TK.LONG, TK.LONGLONG,
    TK.FLOAT, TK.DOUBLE, TK.LONGDOUBLE, TK.ENUM,
}
_STL_ITERATORS = {"NCollection_ForwardRangeIterator", "NCollection_IndexedIterator", "NCollection_StlIterator", "NCollection_UtfIterator"}
_PRIMITIVE_SPELLINGS = {"double", "float", "int", "bool", "char", "long", "short", "size_t", "unsigned", "unsigned int", "unsigned long",
                        "long long", "unsigned long long", "int8_t", "uint8_t", "int16_t", "uint16_t", "int32_t", "uint32_t", "int64_t", "uint64_t",
                        "char16_t", "char32_t", "wchar_t", "Standard_Real", "Standard_Integer", "Standard_Boolean", "Standard_ShortReal",
                        "Standard_Character", "Standard_Byte", "Standard_Size", "Standard_ExtCharacter", "Standard_Utf8Char"}
_OVERRIDES = tomllib.loads((Path(__file__).parent / "overrides.toml").read_text())
_INOUT = set(_OVERRIDES.get("inout", []))
_SKIP_CLASSES = set(_OVERRIDES.get("skip", {}).get("classes", []))
_SKIP_HEADERS = set(_OVERRIDES.get("skip", {}).get("headers", []))
_INCLUDE_DIR: Path | None = None       # the OCCT include directory of the current parse (R-PTR-INCOMPLETE: is there a header for a forward-declared class?)
_NONCOPYABLE = set(_OVERRIDES.get("skip", {}).get("noncopyable", []))
_SKIP_NAMESPACES = set(_OVERRIDES.get("skip", {}).get("namespaces", []))
_SKIP_METHODS = set(_OVERRIDES.get("skip", {}).get("methods", []))
_EXTRA_INSTANCES = list(_OVERRIDES.get("instantiate", {}).get("extra", []))
_INCLUDE_HEADERS: dict[str, list[str]] = _OVERRIDES.get("include", {}).get("headers", {})   # package -> the only headers to bind
INCLUDE_PACKAGES: dict[str, list[str]] = _OVERRIDES.get("include", {}).get("packages", {})   # toolkit -> the only packages to generate
_BINARY_PACKAGES = set(_OVERRIDES.get("stream", {}).get("binary_packages", []))   # packages whose streams carry binary formats (BinTools)

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
    tested with); fall back to the pip 'libclang' wheel. Returns a description for logging. Idempotent: cindex
    accepts the library file only before first use."""
    if cindex.Config.loaded:
        return "libclang already loaded"
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


# Design.md 6 R-DEPRECATED
def _deprecation_message(cursor: cindex.Cursor) -> str | None:
    """The message of Standard_DEPRECATED("...") / [[deprecated("...")]] on a declaration, "" when deprecated without a
    message, None when not deprecated. cindex exposes only Cursor.availability, so clang_getCursorPlatformAvailability
    is called through ctypes for the text."""
    if cursor.availability != cindex.AvailabilityKind.DEPRECATED:
        return None
    lib = cindex.conf.lib
    fn = lib.clang_getCursorPlatformAvailability
    if fn.argtypes is None:
        fn.argtypes = [cindex.Cursor, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(cindex._CXString), ctypes.POINTER(ctypes.c_int),
                       ctypes.POINTER(cindex._CXString), ctypes.c_void_p, ctypes.c_int]
        fn.restype = ctypes.c_int
    always_deprecated = ctypes.c_int()
    always_unavailable = ctypes.c_int()
    deprecated_message = cindex._CXString()
    unavailable_message = cindex._CXString()
    fn(cursor, ctypes.byref(always_deprecated), ctypes.byref(deprecated_message), ctypes.byref(always_unavailable),
       ctypes.byref(unavailable_message), None, 0)
    message = lib.clang_getCString(deprecated_message)
    if isinstance(message, bytes):
        message = message.decode("utf-8", "replace")
    return "" if message is None else message


def _doc_with_deprecation(cursor: cindex.Cursor) -> str:
    """The docstring of a member; a deprecated member (Standard_DEPRECATED) keeps its binding and gets OCCT's deprecation
    message as the first line, so the OCCT documentation's advice reaches the Python user (Design.md 6)."""
    doc = _doc(cursor)
    message = _deprecation_message(cursor)
    if message is None:
        return doc
    note = "Deprecated in OCCT" + (f": {message}" if message != "" else ".")
    return note if doc == "" else f"{note}\n\n{doc}"


# Design.md 6 R-DEFAULT, R-DEFAULT-QUAL
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
        if ref.kind == K.TYPE_REF and target.kind not in (K.CLASS_DECL, K.STRUCT_DECL, K.ENUM_DECL, K.TYPEDEF_DECL, K.TYPE_ALIAS_DECL):
            continue                             # template parameters (Element_t(0) in NCollection_Vec3) are substituted, not qualified
        # a type nested in a class is qualified too (`= Options()` inside BRepGraphInc_Populate); a value reference
        # only when a namespace is involved (class members are handled above, other classes' members are written qualified)
        qualified = _scope_qualified(target, need_namespace=ref.kind == K.DECL_REF_EXPR)
        if qualified is None:
            continue
        for i, tok in enumerate(expr):
            if tok == target.spelling and (i == 0 or expr[i - 1] != "::"):
                expr[i] = qualified
    joined = _SUBST.apply(" ".join(expr))        # template parameters in defaults (Element_t(0)) while instantiating
    # the tokens are joined with spaces; tidy the spelling (`Message_ProgressRange ( )` -> `Message_ProgressRange()`)
    return joined.replace(" (", "(").replace("( ", "(").replace(" )", ")").replace(" ::", "::").replace(":: ", "::")


def _scope_qualified(decl: cindex.Cursor, need_namespace: bool) -> str | None:
    """Fully qualified name of a declaration nested in classes/namespaces; None when it is not nested at all (or, with
    need_namespace, when no named namespace is among the enclosing scopes) or sits in an anonymous namespace."""
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
    if len(parts) == 1 or (need_namespace and not has_namespace):
        return None
    return "::".join(reversed(parts))


def _out_py_type(t: cindex.Type) -> str:
    """Python type name of an out-parameter (double& -> float, int& -> int, bool& -> bool, char& -> str, an enum or the
    class behind a handle<T>& -> its 6a/6c Python spelling): the R-COLLISION suffix component."""
    canon = t.get_canonical()
    while canon.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE, TK.POINTER):
        canon = canon.get_pointee().get_canonical()
    if canon.kind in (TK.FLOAT, TK.DOUBLE, TK.LONGDOUBLE):
        return "float"
    if canon.kind == TK.BOOL:
        return "bool"
    if canon.kind in (TK.CHAR_S, TK.CHAR_U, TK.SCHAR, TK.UCHAR, TK.CHAR16, TK.CHAR32, TK.WCHAR):
        return "str"
    if canon.kind in (TK.INT, TK.UINT, TK.SHORT, TK.USHORT, TK.LONG, TK.ULONG, TK.LONGLONG, TK.ULONGLONG):
        return "int"
    std_name = _std_caster_name(canon)
    if std_name is not None:
        return _STD_PY_NAMES[std_name]              # std::pair<int, int>& -> tuple
    return _py_identifier(_class_behind(t))        # enum/class name; a container instantiation by its 6a concrete name


def _class_behind(t: cindex.Type) -> str:
    """Canonical name of the OCCT class or enum a parameter type refers to (through const/&/*), "" for anything
    else (scalars, std types, opencascade::handle -> the handle's pointee is what must be bound)."""
    canon = t.get_canonical()
    while canon.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE, TK.POINTER):
        canon = canon.get_pointee().get_canonical()
    if canon.kind not in (TK.RECORD, TK.ENUM):
        return ""
    decl = canon.get_declaration()
    if decl.kind == K.NO_DECL_FOUND:
        return ""
    if decl.spelling == "handle" and canon.get_num_template_arguments() == 1:
        return _class_behind(canon.get_template_argument_type(0))
    parent = decl.semantic_parent
    if parent is not None and parent.kind == K.NAMESPACE and (parent.spelling == "std" or parent.spelling.startswith("__")):
        return ""
    return _canonical_args(canon).replace("const ", "")


# Design.md 6 R-HANDLE (nb::arg(...).none() emitted in emit._args)
def _is_handle(t: cindex.Type) -> bool:
    """opencascade::handle<T>, possibly behind const/&."""
    canon = t.get_canonical()
    while canon.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE):
        canon = canon.get_pointee().get_canonical()
    if canon.kind != TK.RECORD:
        # inside a class template (6c walk) handle<BVH_Builder<NumType, Dimension>> is a dependent type without a declaration
        return _SUBST.active and re.match(r"^(const )?(opencascade::|occ::)?handle<", _type_spelling(t)) is not None
    decl = canon.get_declaration()
    return decl.kind != K.NO_DECL_FOUND and decl.spelling == "handle" and canon.get_num_template_arguments() == 1


# Design.md 6 R-OUT, R-OUT-HANDLE; R-INOUT is decided in _params from overrides.toml
def _is_out_param(t: cindex.Type) -> bool:
    """Non-const lvalue reference to a primitive or to a handle<T>: the callee writes it, Python gets it back in the
    result tuple. A handle<T>& is an out-parameter because the caster hands the callee a temporary handle, so a
    handle assigned by the callee (GeomTools::Read(handle<Geom_Curve>&, ...)) would otherwise be lost silently;
    in/out cases are listed in overrides.toml [inout] exactly as for double&."""
    if t.kind != TK.LVALUEREFERENCE:
        return False
    pointee = t.get_pointee()
    if pointee.is_const_qualified():
        return False
    return pointee.get_canonical().kind in _PRIMITIVE_KINDS or _is_handle(pointee) or _std_caster_name(pointee) is not None


_STD_PY_NAMES = {"pair": "tuple", "tuple": "tuple", "vector": "list", "map": "dict", "unordered_map": "dict", "set": "set",
                 "unordered_set": "set", "optional": "Optional", "basic_string": "str", "basic_string_view": "str"}


def _std_caster_name(t: cindex.Type) -> str | None:
    """'pair', 'vector', ... when t is a std type nanobind converts by value (R-STL); None otherwise. A non-const reference to
    one is an out-parameter (BRepMesh_ConeRangeSplitter::GetSplitSteps(..., std::pair<int, int>&)): the caster hands the callee
    a temporary, so it cannot be filled in place like a class reference."""
    canon = t.get_canonical()
    if canon.kind != TK.RECORD:
        return None
    decl = canon.get_declaration()
    parent = decl.semantic_parent
    if parent is not None and parent.kind == K.NAMESPACE and parent.spelling in ("std", "__1") and decl.spelling in _STD_PY_NAMES:
        return decl.spelling
    return None


class Substitution:
    """The 6c walk (Design.md): while the definition of a class template is walked to bind one instantiation, every type
    spelling and default expression is rewritten through this object. Inactive (no template parameters) outside the walk.
    One module-level instance, set up and cleared by _instantiate_template, read by _type_spelling/_default_expr/_class."""

    def __init__(self) -> None:
        self.params: dict[str, str] = {}             # template parameter -> argument
        self.self_: tuple[str, str, str] | None = None   # (template leaf name, full instantiation, qualified template name): the injected class name
        self.members: dict[str, str] = {}            # member types of the template (using IdType = ...) written unqualified inside it -> spelling
        self.scope: dict[str, str] = {}              # types/templates of the enclosing namespaces and classes -> qualified name (DefTraits<...>)

    @property
    def active(self) -> bool:
        return len(self.params) > 0

    @property
    def leaf(self) -> str | None:
        """The template's own (unqualified) name while walking, else None."""
        return None if self.self_ is None else self.self_[0]

    def clear(self) -> None:
        self.params = {}
        self.self_ = None
        self.members = {}
        self.scope = {}

    def apply(self, spelling: str) -> str:
        if not self.active:
            return spelling
        out = spelling
        for param, arg in self.params.items():
            out = re.sub(rf"(?<![:\w]){re.escape(param)}\b", arg, out)
        if self.self_ is not None:
            leaf, full, qualified = self.self_
            for name, spelling in self.members.items():   # IdType -> Typed::IdType (the leaf becomes the full instantiation below)
                out = re.sub(rf"(?<![:\w]){re.escape(name)}\b", spelling, out)
            for name, qual in self.scope.items():    # DefTraits -> BRepGraph_ReverseIterator::DefTraits
                out = re.sub(rf"(?<![:\w]){re.escape(name)}\b", qual, out)
            # injected class name: math_VectorBase -> math_VectorBase<double>; written with its own arguments
            # (Typed<TheKind> inside BRepGraph_NodeId::Typed) -> qualified template name, the arguments were substituted above.
            # A qualified spelling of another template with the same leaf name (BRepGraph_RefId::Typed) is left alone.
            out = re.sub(rf"(?<![:\w]){re.escape(leaf)}\b(?!\s*<)", full, out)
            out = re.sub(rf"(?<![:\w]){re.escape(leaf)}\b(?=\s*<)", qualified, out)
        return out


_SUBST = Substitution()


def _type_spelling(t: cindex.Type) -> str:
    """Type as written in the header (keeps portable typedef names such as Standard_Size), except that
    types nested in a class are spelled fully qualified (the header may say 'D' inside gp_Dir). While a
    class template is walked for an alias instantiation, template parameters are substituted."""
    return _SUBST.apply(_type_spelling_raw(t))


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
        if _SUBST.leaf is not None and parent is not None and parent.kind == K.CLASS_TEMPLATE and parent.spelling == _SUBST.leaf \
                and decl.kind in (K.TYPEDEF_DECL, K.TYPE_ALIAS_DECL, K.CLASS_DECL, K.STRUCT_DECL, K.ENUM_DECL):
            # member type of the class template being instantiated (using TypedId = typename NodeTraits<DefT>::TypedId;
            # CurrentId() returns TypedId): qualify with the injected class name, which becomes the full instantiation;
            # a non-public typedef (BRepGraph_MutGuard::TypeId) cannot be named from outside: spell its underlying type
            if decl.kind in (K.TYPEDEF_DECL, K.TYPE_ALIAS_DECL) and decl.access_specifier != Access.PUBLIC:
                return ("const " if base.is_const_qualified() else "") + _type_spelling_raw(decl.underlying_typedef_type) + suffix
            return ("const " if base.is_const_qualified() else "") + f"{_SUBST.leaf}::{decl.spelling}" + suffix
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
        # non-type arguments (INVALID): their canonical spelling (NCollection_AliasedArray<> written -> <16> canonical)
        canon_args = _split_top(canon_base.spelling[canon_base.spelling.index("<") + 1 : canon_base.spelling.rindex(">")]) \
            if "<" in canon_base.spelling else []
        if all(a.kind != TK.INVALID for a in arg_types) or len(canon_args) == len(arg_types):
            head = base.spelling[: base.spelling.index("<")].replace("const ", "").strip()
            tdecl = canon_base.get_declaration()
            if tdecl.kind != K.NO_DECL_FOUND and "::" not in head and tdecl.semantic_parent is not None \
                    and tdecl.semantic_parent.kind in (K.CLASS_DECL, K.STRUCT_DECL, K.CLASS_TEMPLATE, K.NAMESPACE) \
                    and tdecl.semantic_parent.spelling not in ("", "std") and not tdecl.semantic_parent.spelling.startswith("__"):
                head = _qualified_template(tdecl)     # a nested template written unqualified inside its scope (BaseTraits<...>)
            args = [_type_spelling(a) if a.kind != TK.INVALID else canon_args[i] for i, a in enumerate(arg_types)]
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


def py_path(cpp_name: str, package: str, paths: dict[str, str] | None = None) -> str:
    """Python attribute path of a bound C++ type relative to nanoocp.<package>: nested classes and namespaces keep
    their C++ nesting (gp_Dir::D -> gp_Dir.D, Geom2dEval_RepCurveDesc::Base -> Geom2dEval_RepCurveDesc.Base);
    a namespace named like the package is the package module itself (Geom2dGridEval::CurveD1 -> CurveD1). paths
    (manifest) records the exceptions the name alone cannot tell: a *class* named like its package keeps its name
    (BRepGraph::ShapesView -> BRepGraph.ShapesView)."""
    if paths is not None and cpp_name in paths:
        return paths[cpp_name]
    if "<" in cpp_name:
        return _py_identifier(cpp_name)
    parts = cpp_name.split("::")
    if len(parts) > 1 and parts[0] == package:
        parts = parts[1:]
    return ".".join(parts)


def _ast_py_path(cursor: cindex.Cursor, package: str) -> str:
    """py_path from the declaration itself: enclosing classes and namespaces, minus an outermost namespace named
    like the package."""
    parts = [cursor.spelling]
    parent = cursor.semantic_parent
    while parent is not None and parent.kind in (K.NAMESPACE, K.CLASS_DECL, K.STRUCT_DECL, K.CLASS_TEMPLATE) and parent.spelling != "":
        outermost_ns = parent.kind == K.NAMESPACE and (parent.semantic_parent is None or parent.semantic_parent.kind == K.TRANSLATION_UNIT)
        if not (outermost_ns and parent.spelling == package):
            parts.append(parent.spelling)
        parent = parent.semantic_parent
    return ".".join(reversed(parts))


# Design.md 6 R-UNSUPPORTED, R-ARRAY, R-ITERATOR, R-STL, R-CSTRING
def _unsupported(t: cindex.Type, allow_out: bool) -> str | None:
    canon = t.get_canonical()
    cs = canon.spelling
    if _UNSUPPORTED_RE.search(cs) is not None:
        return "iostream type"
    if canon.kind == TK.RVALUEREFERENCE:
        return "rvalue reference"
    if canon.kind in (TK.CONSTANTARRAY, TK.INCOMPLETEARRAY, TK.VARIABLEARRAY):
        return "array"
    if canon.kind == TK.LVALUEREFERENCE and canon.get_pointee().get_canonical().kind in (TK.CONSTANTARRAY, TK.INCOMPLETEARRAY, TK.VARIABLEARRAY):
        return "array"                          # int (&)[3] (BRepMesh_Triangle::Initialize)
    if canon.kind == TK.POINTER:
        pointee = canon.get_pointee()
        pk = pointee.get_canonical().kind
        if pk == TK.RECORD:
            d = pointee.get_declaration()
            # template instantiations (NCollection_Array1<double>*) have no definition cursor in the TU but are complete
            if d.kind == K.NO_DECL_FOUND or (d.get_definition() is None and pointee.get_canonical().get_num_template_arguments() <= 0):
                # R-PTR-INCOMPLETE: a class only forward-declared in this TU (BOPDS_DS* BOPAlgo_Builder::PDS()) is fine when OCCT
                # installs its header -- the emitter includes <Class>.hxx (class_name -> _note_types) and binds the pointer
                if d.kind == K.NO_DECL_FOUND or _INCLUDE_DIR is None or not (_INCLUDE_DIR / f"{d.spelling}.hxx").exists():
                    return "pointer to incomplete type"
        if pk == TK.FUNCTIONPROTO or pk == TK.FUNCTIONNOPROTO:
            return "function pointer"
        if pk == TK.VOID:
            return "void pointer"
        if pk in (TK.CHAR_S, TK.CHAR_U, TK.CHAR16) and pointee.is_const_qualified():
            return None            # const char* / const char16_t* (Standard_ExtString) -> str, casters in nanoocp_common.h
        if pk in _PRIMITIVE_KINDS or pk == TK.POINTER:
            return "raw pointer to primitive"
    if canon.kind == TK.MEMBERPOINTER:
        return "member pointer"
    it_base = canon
    while it_base.kind in (TK.LVALUEREFERENCE, TK.POINTER):
        it_base = it_base.get_pointee().get_canonical()
    if it_base.kind == TK.RECORD:
        it_decl = it_base.get_declaration()
        if it_decl.kind != K.NO_DECL_FOUND and (it_decl.spelling in _STL_ITERATORS or (
                it_decl.spelling == "DynamicIterator" and it_decl.semantic_parent is not None
                and it_decl.semantic_parent.spelling == "NCollection_DynamicArray")):
            return "STL-style iterator"        # begin()/end() adapters; Python iterates through __iter__ / More-Next-Value
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
    if canon.kind == TK.LVALUEREFERENCE and canon.get_pointee().get_canonical().kind == TK.POINTER:
        return "reference to pointer"
    if canon.kind == TK.LVALUEREFERENCE and not allow_out:
        pointee = canon.get_pointee()
        if not pointee.is_const_qualified() and pointee.get_canonical().kind in _PRIMITIVE_KINDS:
            return "reference to primitive"
    return None


# Design.md 6 R-RESULT
def _result_kind(t: cindex.Type) -> tuple[str, str]:
    """How a returned pointer/reference must be treated (see Design.md section 6)."""
    canon = t.get_canonical()
    if canon.kind not in (TK.POINTER, TK.LVALUEREFERENCE):
        return ResultKind.VALUE, ""
    pointee = canon.get_pointee()
    decl = pointee.get_declaration()
    if decl.kind not in (K.CLASS_DECL, K.STRUCT_DECL):
        return ResultKind.OTHER, ""
    name = _type_spelling(pointee).replace("const ", "").strip()
    if _derives_from(decl, "Standard_Transient"):
        return (ResultKind.PTR_TRANSIENT if canon.kind == TK.POINTER else ResultKind.REF_TRANSIENT), name
    if canon.kind == TK.POINTER:
        return ResultKind.PTR_CLASS, name
    if not pointee.is_const_qualified():
        return ResultKind.REF_MUTABLE, name
    return ResultKind.VALUE, name


# Design.md 6 R-STREAM-OUT, R-STREAM-IN
def _stream_kind(t: cindex.Type) -> str:
    """'out' for a mutable std::ostream& (Dump, DumpJson, Print, Write: the text is returned as a str), 'in' for a
    std::istream& or a std::stringstream (const or not: InitFromJson, Read: a text file-like object is read into a stringstream, nanoocp::TextInput), else ''."""
    canon = t.get_canonical()
    if canon.kind != TK.LVALUEREFERENCE:
        return ""
    pointee = canon.get_pointee()
    decl = pointee.get_canonical().get_declaration()
    if decl.kind == K.NO_DECL_FOUND:
        return ""
    parent = decl.semantic_parent
    if parent is None or parent.kind != K.NAMESPACE or not (parent.spelling == "std" or parent.spelling.startswith("__")):
        return ""
    if decl.spelling == "basic_ostream" and not pointee.is_const_qualified():
        return StreamKind.OUT
    if decl.spelling in ("basic_istream", "basic_stringstream", "basic_istringstream"):
        return StreamKind.IN
    return ""


_OPTIONAL_PTR_REASONS = ("raw pointer to primitive", "void pointer", "pointer to incomplete type", "function pointer", "reference to pointer", "iostream type")


# Design.md 6 R-FIXED-ARRAY
def _fixed_array(t: cindex.Type) -> tuple[str, int, bool] | None:
    """(element type spelling, N, is_const) for a C array parameter or member of a primitive or class type -- gp_Pnt theP[8]
    (Bnd_OBB::GetVertex), int (&theNodes)[3] (BRepMesh_Triangle), double myPeriod[3] -- else None (unknown size, arrays of
    pointers/std types)."""
    canon = t.get_canonical()
    if canon.kind == TK.LVALUEREFERENCE:
        canon = canon.get_pointee().get_canonical()
    if canon.kind != TK.CONSTANTARRAY:
        return None
    elem = canon.element_type
    ek = elem.get_canonical().kind
    if ek not in _PRIMITIVE_KINDS and ek != TK.RECORD:
        return None
    if _unsupported(elem, allow_out=False) is not None or _class_behind(elem) == "" and ek == TK.RECORD:
        return None
    const = elem.is_const_qualified() or canon.is_const_qualified() or "const" in _type_spelling(elem)   # libclang puts the const on either
    return _type_spelling(elem).replace("const ", "").strip(), canon.element_count, const


def _params(cursor: cindex.Cursor, qualified: str = "", scope: str = "", members: set[str] | None = None,
            allow_streams: bool = True) -> tuple[list[Param], str | None]:
    """allow_streams: False for constructors (an object may keep the stream reference beyond the call)."""
    params: list[Param] = []
    inout = qualified in _INOUT or "*::" + qualified.rsplit("::", 1)[-1] in _INOUT   # "*::InitFromJson": every class
    if members is None:
        members = set()
    for i, p in enumerate(cursor.get_arguments()):
        stream = _stream_kind(p.type) if allow_streams else StreamKind.NONE
        reason = _unsupported(p.type, allow_out=True) if stream == StreamKind.NONE else None
        if reason is None and "type-parameter-" in _type_spelling(p.type):
            reason = "dependent type (unresolved template parameter)"
        if reason is None and _SUBST.active and p.type.get_canonical().kind == TK.POINTER:
            # 6c: Element_t* becomes float* only after substitution; the libclang type is a pointer to a template parameter,
            # so the raw-pointer check above did not see it (NCollection_Mat4<T>::Map(T*), R-UNSUPPORTED)
            spelled = _type_spelling(p.type)
            base = spelled.rstrip("* ").removeprefix("const ").strip()
            is_str = spelled.startswith("const ") and base in ("char", "char16_t", "Standard_Character", "Standard_ExtCharacter", "Standard_Utf8Char")
            if base in _PRIMITIVE_SPELLINGS and not is_str:
                reason = "raw pointer to primitive (template argument)"
        name = p.spelling
        if name == "":
            name = f"arg{i}"
        if reason in _OPTIONAL_PTR_REASONS and p.type.get_canonical().kind == TK.POINTER and _default_expr(p, scope, members) in ("NULL", "nullptr", "0"):
            # R-OPTIONAL-PTR: an optional output/context pointer (BRepFill_AdvancedEvolved::IsDone(unsigned* theErrorCode = 0),
            # BRep_Tool::CurveOnSurface(..., bool* theIsStored = NULL)) is dropped; the callee gets nullptr
            params.append(Param(name=name, type=_type_spelling(p.type), default=None, is_out=False, omitted=True))
            continue
        if reason == "array" and not _SUBST.active:
            arr = _fixed_array(p.type)
            if arr is not None:
                elem, n, const = arr           # R-FIXED-ARRAY: const -> a sequence of N in; non-const -> N values returned
                elem_t = p.type.get_canonical().get_pointee().get_canonical().element_type if p.type.get_canonical().kind == TK.LVALUEREFERENCE else p.type.get_canonical().element_type
                _note_instance(elem_t)
                params.append(Param(name=name, type=elem, default=None, is_out=not const, array_len=n, class_name=_class_behind(elem_t),
                                    out_py="list" if not const else ""))
                continue
        if reason is not None:
            return params, f"param '{p.spelling}': {reason}"
        is_out = _is_out_param(p.type)
        _note_instance(p.type)
        params.append(Param(name=name, type=_type_spelling(p.type), default=_default_expr(p, scope, members), is_out=is_out, is_inout=is_out and inout,
                            class_name=_class_behind(p.type), stream=stream, is_handle=_is_handle(p.type),
                            out_py=_out_py_type(p.type) if is_out else ""))
    if cursor.type.kind == TK.FUNCTIONPROTO and cursor.type.is_function_variadic():
        return params, "variadic"
    return params, None


def _is_noexcept(cursor: cindex.Cursor) -> bool:
    k = cursor.exception_specification_kind
    return k in (cindex.ExceptionSpecificationKind.BASIC_NOEXCEPT, cindex.ExceptionSpecificationKind.DYNAMIC_NONE)


_derives_cache: dict[tuple[str, str], bool] = {}
_template_bases: list[tuple[str, cindex.Type, str]] = []   # (derived class, base type, header): bases that are template instantiations
_template_uses: list[cindex.Type] = []                      # template instantiations seen in bound signatures (on-demand 6c)
_dependent_bases: list[tuple[str, str, str]] = []           # (derived instantiation, substituted base spelling, header): template bases seen
                                                            # inside a 6c walk (BVH_Box<double, 3> : BVH_BaseBox<double, 3, BVH_Box>), resolved
                                                            # through a probe re-parse (R-TEMPLATE-BASE)


def _instance_spelling(t: cindex.Type) -> str:
    """The name _instantiate_template gives an instantiation of t's template: qualified template name + canonical arguments."""
    canon = t.get_canonical()
    decl = canon.get_declaration()
    args = []
    for i in range(canon.get_num_template_arguments()):
        at = canon.get_template_argument_type(i)
        args.append(_type_spelling_raw(at) if at.kind != TK.INVALID else None)
    if any(a is None for a in args):            # non-type arguments: libclang cannot spell them here, keep the written form
        written = _type_spelling(t.get_canonical()) if "<" in canon.spelling else _type_spelling(t)
        return written
    return f"{_qualified_template(decl)}<{', '.join(args)}>"


def _is_plain_template_instance(t: cindex.Type) -> bool:
    """An instantiation of an OCCT class template that is not an NCollection binder kind, a handle or a std type."""
    canon = t.get_canonical()
    if canon.kind != TK.RECORD or canon.get_num_template_arguments() <= 0:
        return False
    decl = canon.get_declaration()
    if decl.kind == K.NO_DECL_FOUND or decl.spelling in BINDERS or decl.spelling == "handle":
        return False
    parent = decl.semantic_parent
    return not (parent is not None and parent.kind == K.NAMESPACE and (parent.spelling == "std" or parent.spelling.startswith("__")))


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


# Design.md 6 R-KEYWORD
def py_safe(name: str) -> str:
    """Python name for a C++ identifier: keywords get a trailing underscore (GProp_PEquation::Type::None -> None_)."""
    if keyword.iskeyword(name):
        return name + "_"
    return name


# Design.md 6 R-ENUM, R-ANON-ENUM
def _enum(cursor: cindex.Cursor, header: str, scope: str | None) -> Enum:
    qual = f"{scope}::{cursor.spelling}" if scope is not None else cursor.spelling
    values: list[tuple[str, str]] = []
    for v in cursor.get_children():
        if v.kind == K.ENUM_CONSTANT_DECL:
            cpp = f"{qual}::{v.spelling}" if cursor.is_scoped_enum() else (f"{scope}::{v.spelling}" if scope is not None else v.spelling)
            values.append((py_safe(v.spelling), cpp))
    return Enum(name=qual, py_name=cursor.spelling, values=values, is_scoped=cursor.is_scoped_enum(), doc=_doc(cursor), header=header,
                is_anonymous=cursor.is_anonymous() or cursor.spelling == "" or cursor.spelling.startswith("("))


# Design.md 6 R-UNDEFINED (skip_reason from the nm check in __main__), R-REF-PRIMITIVE (result_kind)
def _method(cursor: cindex.Cursor, cls_name: str, members: set[str]) -> Method | None:
    name = cursor.spelling
    if name.startswith("operator") and name in ("operator=", "operator new", "operator delete", "operator new[]", "operator delete[]"):
        return None
    params, reason = _params(cursor, f"{cls_name}::{name}", cls_name, members)
    _note_instance(cursor.result_type)
    rk, rc = _result_kind(cursor.result_type)
    m = Method(name=name, params=params, result=_type_spelling(cursor.result_type), result_kind=rk, result_class=rc,
               is_static=cursor.is_static_method(),
               is_const=cursor.is_const_method(), is_noexcept=_is_noexcept(cursor), doc=_doc_with_deprecation(cursor),
               is_deprecated=cursor.availability == cindex.AvailabilityKind.DEPRECATED,
               is_operator=name.startswith("operator"), skip_reason=reason, result_class_name=_class_behind(cursor.result_type))
    returns_stream = _stream_kind(cursor.result_type) == StreamKind.OUT and any(p.stream == StreamKind.OUT for p in params)
    if m.skip_reason is None and returns_stream:
        m.result, m.result_kind, m.result_class = "void", ResultKind.VALUE, ""    # Standard_OStream& Print(x, Standard_OStream&): the stream itself, for chaining
    if m.skip_reason is None:
        m.skip_reason = _unsupported(cursor.result_type, allow_out=False) if not returns_stream else None
        rc0 = cursor.result_type.get_canonical()
        if m.skip_reason == "reference to pointer" and rc0.get_pointee().get_canonical().get_pointee().get_canonical().kind == TK.RECORD:
            # R-PTR-REF: BOPAlgo_Builder*& BRepAlgoAPI_BuilderAlgo::Builder() -> bound as the pointer (a lambda copies it out;
            # rv_policy::reference for a class, a handle for a Transient)
            ptr_t = rc0.get_pointee()
            if _unsupported(ptr_t, allow_out=False) is None:
                m.skip_reason = None
                m.result = _type_spelling(ptr_t)
                m.result_kind, m.result_class = _result_kind(ptr_t)
                m.result_class_name = _class_behind(ptr_t)
                m.force_lambda = True
        if m.skip_reason == "reference to primitive" and rc0.kind == TK.LVALUEREFERENCE and not cursor.is_const_method():
            # double& Value(i, j) (math_Matrix), double& ChangeCoord(i) (gp_XYZ): Python cannot hold the reference,
            # so the emitter binds a getter plus a Set<Name>/__setitem__ counterpart (Design.md 6, Python addition)
            m.skip_reason = None
            m.result_kind, m.result = ResultKind.REF_PRIMITIVE, _type_spelling(rc0.get_pointee()).replace("const ", "")
        if m.skip_reason is None and re.match(r"(const )?(\w+)<", m.result) is not None \
                and re.match(r"(const )?(\w+)<", m.result).group(2) in _STL_ITERATORS:
            m.skip_reason = "return: STL-style iterator"     # dependent spelling inside an instantiated template (begin()/end())
        if m.skip_reason is None and "type-parameter-" in m.result:
            m.skip_reason = "dependent type (unresolved template parameter)"
        rcanon = cursor.result_type.get_canonical()
        if m.skip_reason is None and "type-parameter-" in rcanon.spelling:
            # dependent result of an instantiated template: the canonical type does not say what the pointee is.
            # `T &` written as such -> the substituted spelling names the class: mutable reference (reference_internal);
            # a pointer or a typedef hiding one (LinearVector<T>::iterator = T*) -> nanobind would take ownership of
            # an element -> skipped
            if rcanon.kind == TK.LVALUEREFERENCE and not rcanon.get_pointee().is_const_qualified() and m.result.endswith("&") \
                    and not m.result.startswith("const ") and m.result[:-1].strip() not in _PRIMITIVE_SPELLINGS:
                m.result_kind, m.result_class = ResultKind.REF_MUTABLE, m.result[:-1].strip()
            elif rcanon.kind == TK.LVALUEREFERENCE and not rcanon.get_pointee().is_const_qualified() and m.result.endswith("&") \
                    and not m.result.startswith("const ") and not cursor.is_const_method():
                m.result_kind, m.result = ResultKind.REF_PRIMITIVE, m.result[:-1].strip()   # math_VectorBase<double>::Value(i) -> double&
            elif rcanon.kind == TK.POINTER and re.fullmatch(r"const (char|Standard_Utf8Char|Standard_Character) \*", m.result) is not None:
                pass                               # NCollection_UtfString<char>::ToCString(): const char* -> str
            elif rcanon.kind == TK.POINTER or rcanon.kind == TK.LVALUEREFERENCE and not rcanon.get_pointee().is_const_qualified():
                m.skip_reason = "dependent pointer/mutable reference result"
        if m.skip_reason is not None:
            m.skip_reason = "return: " + m.skip_reason
    # inline (in-class or out-of-class in the header) vs. defined in the library; needs bodies parsed
    m.defined_in_header = (cursor.is_definition() or cursor.get_definition() is not None
                           or cursor.is_pure_virtual_method())      # pure virtual: dispatched via vtable, no symbol
    m.mangled = cursor.mangled_name
    if m.skip_reason is None and cursor.is_deleted_method():
        m.skip_reason = "deleted"
    if m.skip_reason is None:
        sig = f"{cls_name}::{name}({', '.join(p.type for p in params)})"
        if f"{cls_name}::{name}" in _SKIP_METHODS or sig in _SKIP_METHODS:
            m.skip_reason = "overrides.toml [skip] methods"
    return m


def _incomplete_in(t: cindex.Type) -> str | None:
    """Name of a record type with no definition in the translation unit that t holds by value: t itself or a
    template argument of it (NCollection_LinearVector<Slot>); pointers/references/handles are fine."""
    canon = t.get_canonical()
    if canon.kind in (TK.POINTER, TK.LVALUEREFERENCE, TK.RVALUEREFERENCE):
        return None
    if canon.kind != TK.RECORD:
        return None
    decl = canon.get_declaration()
    if decl.kind != K.NO_DECL_FOUND and decl.spelling in ("handle", "NCollection_Handle", "unique_ptr", "shared_ptr", "weak_ptr"):
        return None                              # pointer-like: the pointee may stay incomplete in the header (BRepOffsetAPI_ThruSections)
    if decl.kind != K.NO_DECL_FOUND and decl.get_definition() is None and canon.get_num_template_arguments() <= 0:
        return canon.spelling
    for i in range(canon.get_num_template_arguments()):
        arg = canon.get_template_argument_type(i)
        if arg.kind == TK.INVALID:
            continue
        r = _incomplete_in(arg)
        if r is not None:
            return r
    return None


_INT_KINDS = {TK.INT, TK.UINT, TK.LONG, TK.ULONG, TK.LONGLONG, TK.ULONGLONG, TK.SHORT, TK.USHORT}


# Design.md 6 R-CONV, R-CONV-SCALAR
def _conversion(cursor: cindex.Cursor) -> Conversion | None:
    """operator bool/int/double() -> __bool__/__int__/__float__; operator T()/operator handle<T>() for a class or
    enum T -> a constructor T(self) (plus an implicit conversion when not explicit)."""
    t = cursor.result_type
    if t.get_canonical().kind == TK.LVALUEREFERENCE:   # operator const handle<T>&() const: the referenced value
        t = t.get_canonical().get_pointee()
    canon = t.get_canonical()
    doc = _doc(cursor)
    explicit = cursor.is_explicit_method()
    if canon.kind == TK.BOOL:
        return Conversion(ConversionKind.BOOL, "bool", "", explicit, doc)
    if canon.kind in _INT_KINDS:
        return Conversion(ConversionKind.INT, _type_spelling(t), "", explicit, doc)
    if canon.kind in (TK.DOUBLE, TK.FLOAT, TK.LONGDOUBLE):
        return Conversion(ConversionKind.FLOAT, _type_spelling(t), "", explicit, doc)
    if canon.kind == TK.ENUM:
        return None                              # no Python spelling for a conversion to an enum (BRepGraphInc_ParityOrientation)
    if canon.kind == TK.RECORD:
        decl = canon.get_declaration()
        if decl.kind == K.NO_DECL_FOUND or _unsupported(t, allow_out=False) is not None:
            return None
        if decl.spelling == "handle" and canon.get_num_template_arguments() == 1:
            pointee = canon.get_template_argument_type(0)
            if pointee.get_declaration().kind == K.NO_DECL_FOUND:
                return None
            return Conversion(ConversionKind.HANDLE, _type_spelling(pointee), _class_behind(pointee), explicit, doc)
        parent = decl.semantic_parent
        if parent is not None and parent.kind == K.NAMESPACE and (parent.spelling == "std" or parent.spelling.startswith("__")):
            return None
        return Conversion(ConversionKind.CLASS, _type_spelling(t).replace("const ", "").strip(), _class_behind(t), explicit, doc)
    return None


# Design.md 6 R-NESTED, R-FIELD, R-INCOMPLETE, R-IMPLICIT-CONV, R-IMPLICIT-DEFAULT, R-MI, R-NONCOPYABLE
_DETECTED_NONCOPYABLE: set[str] = set()     # classes found non-copyable while parsing this run (CellFilter members), by canonical name


def _holds_uncopyable_element(t: cindex.Type) -> bool:
    """A container member whose element type declares its copy constructor deleted (NCollection_Sequence<CSLib_Class2d> in
    BRepTopAdaptor_FClass2d): the container's implicit copy does not compile although the traits say it does."""
    canon = t.get_canonical()
    if canon.kind != TK.RECORD or canon.get_num_template_arguments() <= 0 or canon.get_declaration().spelling not in BINDERS:
        return False                                # only the NCollection value containers store their elements by value
    for i in range(canon.get_num_template_arguments()):
        arg = canon.get_template_argument_type(i)
        if arg.kind == TK.INVALID:
            continue
        decl = arg.get_canonical().get_declaration()
        if decl.kind in (K.CLASS_DECL, K.STRUCT_DECL) and decl.get_definition() is not None and any(
                ch.kind == K.CONSTRUCTOR and ch.is_copy_constructor() and ch.is_deleted_method() for ch in decl.get_definition().get_children()):
            return True
    return False


def _strip_cv(spelling: str) -> str:
    return re.sub(r"^const ", "", spelling).strip()


def _members(cursor: cindex.Cursor) -> set[str]:
    """Names usable unqualified inside a class body (for qualifying default arguments, R-DEFAULT)."""
    members: set[str] = set()
    for ch in cursor.get_children():
        if ch.kind in (K.VAR_DECL, K.FIELD_DECL, K.ENUM_DECL, K.TYPEDEF_DECL, K.TYPE_ALIAS_DECL, K.CLASS_DECL, K.STRUCT_DECL):
            members.add(ch.spelling)
        if ch.kind == K.ENUM_DECL:
            members.update(v.spelling for v in ch.get_children() if v.kind == K.ENUM_CONSTANT_DECL)
    return members


def _ctor(ch: cindex.Cursor, c: Class, members: set[str]) -> Constructor:
    params, reason = _params(ch, "", c.name, members, allow_streams=False)
    required = [q for q in params if q.default is None]
    implicit = (len(params) >= 1 and len(required) <= 1 and not ch.is_explicit_method()
                and not ch.is_copy_constructor() and not ch.is_move_constructor())
    ctor = Constructor(params=params, doc=_doc_with_deprecation(ch), skip_reason=reason, is_implicit=implicit, is_copy=ch.is_copy_constructor(),
                       defined_in_header=ch.is_definition() or ch.get_definition() is not None or ch.is_default_method() or _SUBST.active,
                       mangled=ch.mangled_name)
    if ctor.skip_reason is not None:
        c.skipped.append(f"{c.name}::{c.name}({', '.join(p.type for p in params)}): {ctor.skip_reason}")
    return ctor


# Design.md 6 R-USING
def _using_methods(using: cindex.Cursor, c: Class) -> None:
    """`using Base::name;` in a public section: the base's overloads of `name` become members of this class -- needed when
    the base is non-public (BRepAlgoAPI_Algo : protected BOPAlgo_Options re-exports SetFuzzyValue, HasErrors, ...) and when the
    class's own overloads would otherwise hide the base's in nanobind (Blend_FuncInv::Set). The emitter binds them through
    lambdas on this class (a member pointer of the base would need the inaccessible upcast)."""
    odr = next((k for k in using.get_children() if k.kind == K.OVERLOADED_DECL_REF), None)
    if odr is None:
        return                                     # `using Base::SomeType;`: nothing to bind
    lib = cindex.conf.lib
    for i in range(lib.clang_getNumOverloadedDecls(odr)):
        d = lib.clang_getOverloadedDecl(odr, i)
        if d.kind == K.CONSTRUCTOR:
            # `using Base::Base;`: Derived(args) is valid for every base constructor except copy/move (BRepGraph_FacesOfEdge)
            if d.is_copy_constructor() or d.is_move_constructor() or d.is_deleted_method() or d.access_specifier == Access.PRIVATE:
                continue
            ctor = _ctor(d, c, _members(d.semantic_parent))
            ctor.defined_in_header = True          # the base's symbol; the base's own binding runs the nm check
            c.ctors.append(ctor)                   # has_declared_ctor stays: inherited constructors do not suppress the implicit default one
            continue
        if d.kind != K.CXX_METHOD or d.access_specifier == Access.PRIVATE:
            c.skipped.append(f"{c.name}: using {using.spelling}: {d.kind.name.lower()} (not bound)")
            continue
        base_cursor = d.semantic_parent
        base = _type_spelling(base_cursor.type)
        m = _method(d, base, _members(base_cursor))
        if m is None:
            continue
        m.via_using = base
        m.defined_in_header = True                 # its symbol lives in the base's library; the base's own binding runs the nm check
        if m.skip_reason is not None:
            c.skipped.append(f"{c.name}::{m.name}({', '.join(p.type for p in m.params)}) (using {base}::{m.name}): {m.skip_reason}")
        c.methods.append(m)


def _class(cursor: cindex.Cursor, header: str, package: str, outer: str = "") -> Class:
    cpp_name = _type_spelling(cursor.type)          # 'NCollection_Lerp<gp_Trsf>' for a specialization
    if cpp_name == "":                              # a class template walked for an alias instantiation (6c)
        cpp_name = _SUBST.apply(cursor.spelling)
    path = (py_path(cpp_name, package) if "<" in cpp_name else _ast_py_path(cursor, package)).split(".")
    parent = cursor.semantic_parent
    if outer == "" and "<" not in cpp_name and parent is not None and parent.kind in (K.CLASS_DECL, K.STRUCT_DECL):
        outer = _qualified_template(parent)        # defined out of class (class BRepGraph::ShapesView { ... }): still nested
    c = Class(name=cpp_name, py_name=path[-1], bases=[], header=header, doc=_doc(cursor),
              is_transient=_derives_from(cursor, "Standard_Transient"),
              is_exception=_derives_from(cursor, "Standard_Failure"), is_abstract=cursor.is_abstract_record(),
              scope=tuple(path[:-1]), outer=outer, noncopyable=cpp_name in _NONCOPYABLE)
    members = _members(cursor)     # names usable unqualified inside the class (for default arguments)
    # a data member (any access) of a type that is only declared in the headers (BRepGraph_CacheMesh::Slot, defined in
    # the .cxx) makes the destructor uninstantiable -> nb::class_ cannot be formed
    for ch in cursor.get_children():
        if ch.kind == K.FIELD_DECL:
            inc = _incomplete_in(ch.type)
            if inc is not None:
                c.skipped.append(f"{c.name}: member {ch.spelling} of incomplete type {inc} -> class skipped")
                c.unbindable = True
                break
            # R-NONCOPYABLE, detected: NCollection_CellFilter<...>::Cell has a user-declared move constructor, so the
            # NCollection_Map<Cell> inside every CellFilter cannot be copied while the traits say it can (math_GlobOptMin,
            # BRepExtrema_ProximityValueTool, BRepMesh_CircleTool, BRepMesh_VertexTool); a class holding such a member by value
            # goes through the wrapper like the hand-listed ones
            fcanon = ch.type.get_canonical().spelling
            if "NCollection_CellFilter<" in fcanon or _strip_cv(fcanon) in _DETECTED_NONCOPYABLE or _holds_uncopyable_element(ch.type):
                if c.is_transient:
                    # no wrapper for a Transient class (the wrapper would be the registered type while OCCT hands out the OCCT
                    # class) and nanobind's copy wrapper would not compile: BRepMesh_VertexTool stays out
                    c.skipped.append(f"{c.name}: member {ch.spelling} of type {_strip_cv(fcanon)} is not copyable and the class is Transient "
                                     f"(no non-copyable wrapper possible) -> class skipped")
                    c.unbindable = True
                    break
                if not c.noncopyable:
                    c.skipped.append(f"{c.name}: member {ch.spelling} of type {_strip_cv(fcanon)} is not copyable -> bound through the non-copyable wrapper (R-NONCOPYABLE)")
                c.noncopyable = True
    # nanobind constructs value types with placement new: possible only if the class declares no
    # operator new at all, or a public operator new(size_t, void*) (DEFINE_STANDARD_ALLOC does).
    news = [ch for ch in cursor.get_children() if ch.kind == K.CXX_METHOD and ch.spelling == "operator new"]
    if len(news) > 0 and not any(ch.access_specifier == Access.PUBLIC and len(list(ch.get_arguments())) == 2
                                 and list(ch.get_arguments())[1].type.get_canonical().spelling == "void *" for ch in news):
        c.constructible = False
        # nanobind instantiates wrap_copy/wrap_move (placement new) for every non-trivially copy/move-constructible class;
        # with the placement form hidden that does not compile (BRepMeshData_Curve: DEFINE_INC_ALLOC + a base class).
        # Poly_CoherentTriPtr (pointer fields only) is trivially copyable and binds fine
        children = list(cursor.get_children())
        deleted_copy = any(ch.kind == K.CONSTRUCTOR and ch.is_copy_constructor() and (ch.is_deleted_method() or ch.access_specifier != Access.PUBLIC)
                           for ch in children)
        non_trivial = (any(ch.kind == K.CXX_BASE_SPECIFIER for ch in children)
                       or any(ch.kind == K.CXX_METHOD and ch.is_virtual_method() for ch in children)
                       or any(ch.kind == K.FIELD_DECL and ch.type.get_canonical().kind == TK.RECORD for ch in children))
        if non_trivial and not deleted_copy:
            c.skipped.append(f"{c.name}: operator new is not public (no placement form) and the class is not trivially copyable: "
                             f"nanobind cannot instantiate its copy/move wrappers -> class skipped")
            c.unbindable = True
    if cpp_name.startswith("NCollection_CellFilter<") and not c.noncopyable:      # the CellFilter instantiation itself (its CellMap member)
        c.skipped.append(f"{c.name}: its NCollection_Map<Cell> member is not copyable -> bound through the non-copyable wrapper (R-NONCOPYABLE)")
        c.noncopyable = True
    if c.noncopyable:
        _DETECTED_NONCOPYABLE.add(c.name)
    for ch in cursor.get_children():
        if ch.kind == K.CXX_BASE_SPECIFIER:
            if ch.access_specifier != Access.PUBLIC:
                c.skipped.append(f"{c.name}: non-public base {_type_spelling(ch.type)} dropped; class not constructible")
                c.constructible = False
                continue
            if not _SUBST.active and _is_plain_template_instance(ch.type):
                # a template base is named as its instantiation is (canonical arguments, defaults spelled out), also when the
                # header writes a typedef (BRepExtrema_TriangleSet : BVH_PrimitiveSet3d = BVH_PrimitiveSet<double, 3>)
                c.bases.append(_instance_spelling(ch.type))
                _template_bases.append((c.name, ch.type, header))
                continue
            c.bases.append(_type_spelling(ch.type))
            if _SUBST.active and "<" in c.bases[-1] and not c.bases[-1].startswith(("std::", "opencascade::handle<")) \
                    and c.bases[-1].split("<")[0] not in BINDERS:
                _dependent_bases.append((c.name, c.bases[-1], header))     # only spellable after substitution: needs its own Type
            continue
        if ch.kind == K.CONSTRUCTOR:
            c.has_declared_ctor = True
        if ch.access_specifier != Access.PUBLIC:
            continue
        if ch.kind == K.CONSTRUCTOR:
            if ch.is_move_constructor() or ch.is_deleted_method():
                continue
            c.ctors.append(_ctor(ch, c, members))
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
            if reason == "array" and not _SUBST.active:
                arr = _fixed_array(ch.type)
                if arr is not None:            # R-FIXED-ARRAY: double myPeriod[3] (BOPAlgo_MakePeriodic::PeriodicityParams) -> a list property
                    elem, n, const = arr
                    _note_instance(ch.type.get_canonical().element_type)
                    c.fields.append(Field(name=ch.spelling, type=elem, is_const=const, doc=_doc(ch), array_len=n))
                    continue
            if reason is None and ch.type.get_canonical().kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE):
                reason = "reference member (no pointer-to-member)"
            if reason is not None:
                c.skipped.append(f"{c.name}::{ch.spelling}: field {reason}")
                continue
            _note_instance(ch.type)                # a container-typed field needs its instantiation like a parameter does
            c.fields.append(Field(name=ch.spelling, type=_type_spelling(ch.type), is_const=ch.type.is_const_qualified(), doc=_doc(ch)))
        elif ch.kind == K.CONVERSION_FUNCTION:
            conv = _conversion(ch)
            if conv is None:
                c.skipped.append(f"{c.name}::{ch.spelling}: conversion operator to an unsupported type")
            else:
                c.conversions.append(conv)
        elif ch.kind == K.ENUM_DECL and ch.is_definition():
            c.enums.append(_enum(ch, header, c.name))
        elif ch.kind == K.USING_DECLARATION:
            _using_methods(ch, c)
        elif ch.kind in (K.FUNCTION_TEMPLATE,):
            c.skipped.append(f"{c.name}::{ch.spelling}: template member")
        elif ch.kind in (K.CLASS_DECL, K.STRUCT_DECL) and ch.is_definition():
            if ch.spelling == "":
                c.skipped.append(f"{c.name}: anonymous nested struct")
            elif _SUBST.active:
                c.skipped.append(f"{cursor.spelling}::{ch.spelling}: nested class of a class template (alias instantiation)")
            else:
                n = _class(ch, header, package, outer=c.name)
                if n.unbindable:
                    c.skipped.extend(n.skipped)
                else:
                    c.nested.append(n)
        elif ch.kind == K.CLASS_TEMPLATE:
            c.skipped.append(f"{c.name}::{ch.spelling}: nested class template")
    return c


_instances_seen: dict[str, TemplateInstance] = {}    # filled while parsing a package (reset per package)


def _canonical_args(t: cindex.Type) -> str:
    """Portable canonical spelling of a type used as a template argument (typedefs resolved, std::__1 stripped)."""
    return re.sub(r"std::__\w+::", "std::", t.get_canonical().spelling)


_NESTED_OWNER = {src: kind for kind, info in BINDERS.items() for src in info.get("nested_from", {}).values()}   # TListIterator -> List


def _note_instance(t: cindex.Type) -> None:
    """If t (or its pointee) is an instantiation of an NCollection template we have a binder for, record it,
    including nested instantiations in its arguments. Any other OCCT class template instantiation in a signature
    (BRepGraph_MutGuard<...>, BVH_Box<double, 3>) is recorded for on-demand instantiation (6c)."""
    canon = t.get_canonical()
    while canon.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE, TK.POINTER):
        canon = canon.get_pointee().get_canonical()
    if canon.kind != TK.RECORD or canon.get_num_template_arguments() <= 0:
        return
    decl = canon.get_declaration()
    if decl.spelling == "handle":       # opencascade::handle<NCollection_HArray1<T>> -> look inside
        _note_instance(canon.get_template_argument_type(0))
        return
    owner = _NESTED_OWNER.get(decl.spelling)
    if owner is not None:
        # NCollection_TListIterator<T> is NCollection_List<T>::Iterator, bound by the List binder (6a) as
        # NCollection_List__T.Iterator: record the owner instantiation instead of a 6c class of its own (TopOpeBRepDS)
        args = [_canonical_args(canon.get_template_argument_type(i)) for i in range(canon.get_num_template_arguments())]
        for i in range(len(args)):
            _note_instance(canon.get_template_argument_type(i))
        key = f"{owner}<{', '.join(instance_args(owner, args))}>"
        _instances_seen.setdefault(key, TemplateInstance(template=owner, args=instance_args(owner, args), key=key))
        return
    if decl.spelling not in BINDERS:
        if not _SUBST.active and _is_plain_template_instance(t) and "type-parameter-" not in canon.spelling:
            _template_uses.append(t)
        for i in range(canon.get_num_template_arguments()):   # NCollection_Iterator<NCollection_DynamicArray<T>>: the argument
            arg = canon.get_template_argument_type(i)
            if arg.kind != TK.INVALID:
                _note_instance(arg)
        return
    all_args = [_canonical_args(canon.get_template_argument_type(i)) for i in range(canon.get_num_template_arguments())]
    args = instance_args(decl.spelling, all_args)     # default hashers are not part of the key/name
    for i in range(len(args)):
        _note_instance(canon.get_template_argument_type(i))
    key = f"{decl.spelling}<{', '.join(args)}>"
    _instances_seen.setdefault(key, TemplateInstance(template=decl.spelling, args=args, key=key))


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


def _qualified_template(decl: cindex.Cursor) -> str:
    """BRepGraph_NodeId::Typed for a template nested in a class, BRepGraph_RefsIterator::RefIterator in a namespace."""
    parts = [decl.spelling]
    parent = decl.semantic_parent
    while parent is not None and parent.kind in (K.NAMESPACE, K.CLASS_DECL, K.STRUCT_DECL, K.CLASS_TEMPLATE) and parent.spelling != "":
        parts.append(parent.spelling)
        parent = parent.semantic_parent
    return "::".join(reversed(parts))


def _scope_reopenings(tu: cindex.TranslationUnit, qualified: str) -> list[cindex.Cursor]:
    """Every cursor declaring the scope A::B (a namespace may be reopened in several headers)."""
    scopes = [tu.cursor]
    for name in qualified.split("::"):
        scopes = [ch for sc in scopes for ch in sc.get_children()
                  if ch.kind in (K.NAMESPACE, K.CLASS_DECL, K.STRUCT_DECL, K.CLASS_TEMPLATE) and ch.spelling == name]
    return scopes


def _find_class_template(tu: cindex.TranslationUnit, qualified: str) -> tuple[cindex.Cursor | None, list[list[str]]]:
    """The template's definition plus the parameter names of every declaration (a forward declaration may
    name the parameters differently, and libclang spells some dependent types with those names). Nested
    templates are found by descending the enclosing classes/namespaces (every reopening of a namespace)."""
    definition = None
    param_lists: list[list[str]] = []
    parts = qualified.split("::")
    scopes = _scope_reopenings(tu, "::".join(parts[:-1])) if len(parts) > 1 else [tu.cursor]
    for sc in scopes:
        for cur in sc.get_children():
            if cur.kind == K.CLASS_TEMPLATE and cur.spelling == parts[-1]:
                param_lists.append([p.spelling for p in cur.get_children() if p.kind in (K.TEMPLATE_TYPE_PARAMETER, K.TEMPLATE_NON_TYPE_PARAMETER)])
                if cur.is_definition():
                    definition = cur
    return definition, param_lists


def _template_default(param: cindex.Cursor) -> str | None:
    """Default of a template parameter as written (`bool IsFull = false` -> 'false')."""
    toks = [t.spelling for t in param.get_tokens()]
    if "=" not in toks:
        return None
    return " ".join(toks[toks.index("=") + 1:])


# Design.md 6c (template aliases and on-demand instantiations), R-TEMPLATE-NAME
def _instantiate_template(tu: cindex.TranslationUnit, t: cindex.Type, header: str, package: str, report: list[str],
                          what: str, py_name: str | None) -> Class | None:
    """The members of a class template instantiated for the arguments of t, walked from the template's definition
    with argument substitution (Design.md 6c). py_name: the alias name, or None for an instantiation that is only a
    base class (BRepGraph_WiresOfEdge : EdgeParentsOf<...>) -> the mangled name. NCollection containers (hand-written
    binders) and std types are not handled here. Returns None (with a report line) when it cannot be done."""
    canon = t.get_canonical()
    if canon.kind != TK.RECORD or canon.get_num_template_arguments() <= 0 or "<" not in t.spelling:
        return None
    tmpl_name = canon.get_declaration().spelling
    if tmpl_name in BINDERS or tmpl_name == "handle" or t.spelling.startswith("std::"):
        return None
    qualified = _qualified_template(canon.get_declaration())        # BRepGraph_NodeId::Typed for nested templates
    tmpl, param_lists = _find_class_template(tu, qualified)
    if tmpl is None:
        report.append(f"{what}: class template {qualified} not found in the translation unit")
        return None
    params = [p for p in tmpl.get_children() if p.kind in (K.TEMPLATE_TYPE_PARAMETER, K.TEMPLATE_NON_TYPE_PARAMETER)]
    # arguments as written, from the canonical type when the alias goes through a metafunction
    # (BVH_Vec3d = BVH::VectorType<double, 3>::Type resolves to NCollection_Vec3<double>)
    spelled = t.spelling if t.spelling.split("<", 1)[0].split("::")[-1] == tmpl_name else canon.spelling
    if "<" not in spelled:
        report.append(f"{what}: cannot read template arguments")
        return None
    inner = spelled[spelled.index("<") + 1 : spelled.rindex(">")].strip()
    written = _split_top(inner) if inner != "" else []
    n = canon.get_num_template_arguments()
    if len(written) < n and "<" in canon.spelling:           # defaulted arguments: the canonical spelling may have them all
        canon_inner = canon.spelling[canon.spelling.index("<") + 1 : canon.spelling.rindex(">")].strip()
        canon_written = _split_top(canon_inner) if canon_inner != "" else []
        if len(canon_written) == n:
            written = canon_written
    if len(params) < n or len(written) > n:
        report.append(f"{what}: cannot match template arguments")
        return None
    args: list[str] = []          # what the members are substituted with
    spelled_args: list[str] = []  # how the instantiation is spelled (== args, except for a defaulted argument libclang
    keys: list[str] = []          # cannot spell: NCollection_AliasedArray<> stays <> in the name, 16 in the substitution)
    for i in range(n):
        at = canon.get_template_argument_type(i)
        if at.kind != TK.INVALID:
            args.append(_type_spelling_raw(at)); spelled_args.append(args[-1]); keys.append(_canonical_args(at))
            _note_instance(at)                    # NCollection_Iterator<NCollection_DynamicArray<T>>: the container must be bound
        elif i < len(written):
            args.append(written[i]); spelled_args.append(written[i]); keys.append(written[i])   # non-type argument, as written
        else:
            default = _template_default(params[i])                    # BRepGraph_Iterator<DefT, bool IsFull = false>
            if default is None:
                report.append(f"{what}: non-type argument {i + 1} neither written nor defaulted")
                return None
            args.append(default); spelled_args.append(""); keys.append("")
    full = f"{qualified}<{', '.join(a for a in spelled_args if a != '')}>"
    if full in _SKIP_CLASSES:
        report.append(f"{what}: {full}: skipped (overrides.toml [skip] classes)")
        return None
    pointer_args = [a for a in args if a.endswith("*")]
    if len(pointer_args) > 0:
        # HLRBRep instantiates Extrema_GenLocateExtPC<void*, ...>, GeomLProp_CLPropsBase<..., const HLRBRep_Curve*, ...>: every
        # member takes or returns the pointer (R-UNSUPPORTED), and `const T&` with T a pointer is `T* const&`, not what the
        # substitution spells; the whole instantiation stays out
        report.append(f"{what}: template argument {pointer_args[0]} is a raw pointer -> not bound")
        return None
    assert not _SUBST.active, "nested template walks are not supported"
    for names in param_lists:                      # every declaration's parameter names, position-wise
        for name, a in zip(names, args):
            _SUBST.params.setdefault(name, a)
    _SUBST.self_ = (tmpl_name, full, qualified)
    type_kinds = (K.TYPEDEF_DECL, K.TYPE_ALIAS_DECL, K.CLASS_DECL, K.STRUCT_DECL, K.ENUM_DECL, K.CLASS_TEMPLATE)
    for ch in tmpl.get_children():
        if ch.kind not in type_kinds or ch.spelling == "" or ch.spelling in _SUBST.params:
            continue
        if ch.access_specifier == Access.PUBLIC or ch.kind not in (K.TYPEDEF_DECL, K.TYPE_ALIAS_DECL):
            _SUBST.members[ch.spelling] = f"{tmpl_name}::{ch.spelling}"
        else:
            # a private member typedef used in a public signature (BRepGraph_MutGuard::TypeId) cannot be named from
            # outside: spell its underlying type, with the template parameters substituted
            underlying = _type_spelling_raw(ch.underlying_typedef_type)
            for param, a in _SUBST.params.items():
                underlying = re.sub(rf"(?<![:\w]){re.escape(param)}\b", a, underlying)
            _SUBST.members[ch.spelling] = underlying
    ancestor = tmpl.semantic_parent
    while ancestor is not None and ancestor.kind in (K.NAMESPACE, K.CLASS_DECL, K.STRUCT_DECL) and ancestor.spelling != "":
        prefix = _qualified_template(ancestor)
        for sc in _scope_reopenings(tu, prefix):
            for ch in sc.get_children():
                if ch.kind in type_kinds and ch.spelling != "" and ch.spelling != tmpl_name and ch.spelling not in _SUBST.params \
                        and ch.spelling not in _SUBST.members:
                    _SUBST.scope.setdefault(ch.spelling, f"{prefix}::{ch.spelling}")
        ancestor = ancestor.semantic_parent
    try:
        c = _class(tmpl, header, package)
    finally:
        _SUBST.clear()
    c.name = full
    c.py_name = py_name if py_name is not None else _py_identifier(full)
    c.template_key = f"{qualified}<{', '.join(k for k in keys if k != '')}>"
    for m in c.methods:
        m.defined_in_header = True            # instantiated from the header, no library symbol involved
    return c


def _alias_instance(tu: cindex.TranslationUnit, cur: cindex.Cursor, header: str, package: str, report: list[str]) -> Class | None:
    """using math_Vector = math_VectorBase<double>; -> the template instantiated under the alias name (Design.md 6c)."""
    t = cur.underlying_typedef_type
    c = _instantiate_template(tu, t, header, package, report, f"{cur.spelling} = {t.spelling}", cur.spelling)
    if c is not None:
        c.doc = c.doc if c.doc != "" else _doc(cur)
    return c


def _prefixes(scope: tuple[str, ...]) -> list[tuple[str, ...]]:
    """('A', 'B') -> [('A',), ('A', 'B')]"""
    return [scope[:i] for i in range(1, len(scope) + 1)]


def _missing_headers(errors: list, include_dir: Path, have: list[str]) -> list[str]:
    """R-PRELUDE: the OCCT headers (as '<X.hxx>') that the parse diagnostics say are missing before the parsed ones."""
    missing = {m.group(1) for d in errors
               for m in [re.search(r"(?:incomplete (?:return )?type|use of undeclared identifier|unknown type name) '(?:const )?(\w+)'", d.spelling)]
               if m is not None}
    return sorted(f"<{name}.hxx>" for name in missing if (include_dir / f"{name}.hxx").exists() and f"<{name}.hxx>" not in have)


_STD_PRELUDE = ["<cstddef>", "<cstdint>", "<cstring>", "<string>"]   # some OCCT headers use size_t with only <limits> included


# Design.md 6 R-PRELUDE
def include_prelude(headers: list[str], include_dir: Path, args: list[str]) -> list[str]:
    """Headers ('X.hxx') that must precede the given OCCT headers so that the list compiles: the R-PRELUDE loop applied to an
    emitted include list, whose identifier-based extra headers may not be self-contained (Contap_Line.hxx names
    handle<Adaptor2d_Curve2d> without declaring it; HLRTopoBRep includes Contap_Contour.hxx). Bodies are skipped: one cheap TU."""
    index = cindex.Index.create()
    found: list[str] = []
    with tempfile.TemporaryDirectory() as td:
        tu_file = Path(td) / "includes.cpp"
        for _ in range(6):
            tu_file.write_text("".join(f"#include {h}\n" for h in _STD_PRELUDE + found) + "".join(f"#include <{h}>\n" for h in headers))
            tu = index.parse(str(tu_file), args=args, options=cindex.TranslationUnit.PARSE_SKIP_FUNCTION_BODIES)
            errors = [d for d in tu.diagnostics if d.severity >= cindex.Diagnostic.Error]
            extra = _missing_headers(errors, include_dir, found) if len(errors) > 0 else []
            if len(extra) == 0:
                break
            found += extra
    return [h.strip("<>") for h in found]


def parse_package(tree: OcctTree, pkg: Package, args: list[str] | None = None, known_elsewhere: set[str] | None = None) -> PackageIR:
    """known_elsewhere: C++ names of classes bound by earlier packages/runs (instantiations used in signatures are
    only instantiated when nobody has bound them yet)."""
    if args is None:
        args = clang_args(tree)
    if known_elsewhere is None:
        known_elsewhere = set()
    global _INCLUDE_DIR
    _INCLUDE_DIR = tree.include_dir
    allowed = _INCLUDE_HEADERS.get(pkg.name)          # a partial package (the font slice of Visualization): allowlist
    if allowed is not None:
        for h in allowed:
            if h not in pkg.headers:
                raise ValueError(f"overrides.toml [include] headers: {h} is not a header of package {pkg.name}")
    ir = PackageIR(name=pkg.name, toolkit=pkg.toolkit,
                   headers=[h for h in pkg.headers if h not in _SKIP_HEADERS and (allowed is None or h in allowed)])
    for h in pkg.headers:
        if h in _SKIP_HEADERS:
            ir.report.append(f"{h}: skipped (overrides.toml [skip] headers)")
        elif allowed is not None and h not in allowed:
            ir.report.append(f"{h}: not in the allowlist (overrides.toml [include] headers)")
    headers = set(ir.headers)
    _instances_seen.clear()
    _template_bases.clear()
    _template_uses.clear()
    _dependent_bases.clear()
    with tempfile.TemporaryDirectory() as td:
        umbrella = Path(td) / f"{pkg.name}__all.hxx"
        # prelude: some OCCT headers are not self-contained (MathUtils_Config.hxx uses size_t with only <limits>)
        prelude = list(_STD_PRELUDE)
        index = cindex.Index.create()
        for _ in range(6):
            umbrella.write_text("".join(f"#include {h}\n" for h in prelude) + "".join(f"#include <{h}>\n" for h in ir.headers))
            # bodies are parsed (no PARSE_SKIP_FUNCTION_BODIES): only then does get_definition() find the
            # out-of-class inline definitions that decide whether a method needs a library symbol
            tu = index.parse(str(umbrella), args=args)
            errors = [d for d in tu.diagnostics if d.severity >= cindex.Diagnostic.Error]
            if len(errors) == 0:
                break
            # R-PRELUDE: a header that uses a forward-declared class in inline code (GeomGridEval_Line.hxx calls
            # Geom_Line::Lin() with gp_Lin only forward-declared) or names a class it neither includes nor declares
            # (IntWalk_PWalking.hxx: handle<IntSurf_LineOn2S>; ChFiKPart_ComputeData_ChPlnCon.hxx: ChFiDS_ChamfMode);
            # OCCT's .cxx includes that header first. Include that class's header before the package headers and parse again.
            extra = _missing_headers(errors, tree.include_dir, prelude)
            if len(extra) == 0:
                break
            prelude += extra
            ir.prelude += [h.strip("<>") for h in extra]
            ir.report.append(f"{pkg.name}: headers not self-contained, parsed with {', '.join(extra)} included first")
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
            if ns == "" and cur.semantic_parent is not None and cur.semantic_parent.kind == K.NAMESPACE:
                ns = _qualified_template(cur.semantic_parent) + "::"     # `template <> struct std::hash<X>` written at file scope
            # a namespace named like the package is the package module itself (TopoDS::Vertex -> nanoocp.TopoDS.Vertex);
            # every other namespace becomes a submodule (Geom2dEval_RepCurveDesc::Base -> nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base)
            ns_parts = [part for part in (ns.rstrip(":").split("::") if ns != "" else []) if not part.startswith("__")]   # std::__1 -> std
            if "" in ns_parts:
                ir.report.append(f"{header}: {cur.spelling}: anonymous namespace (not bound)")
                continue
            if any(part in _SKIP_NAMESPACES for part in ns_parts):
                if ns_parts == ["std"] and cur.kind == K.STRUCT_DECL and cur.spelling == "hash" and cur.is_definition() \
                        and cur.type.get_num_template_arguments() == 1:
                    ir.hashable.add(_canonical_args(cur.type.get_template_argument_type(0)))   # std::hash<TopoDS_Shape> -> __hash__
                    continue
                if ns_parts == ["std"] and cur.kind == K.CLASS_TEMPLATE_PARTIAL_SPECIALIZATION and cur.spelling == "hash" \
                        and cur.type.get_num_template_arguments() == 1:
                    tdecl = cur.type.get_template_argument_type(0).get_declaration()           # std::hash<BRepGraph_RefId::Typed<K>>
                    if tdecl.kind == K.CLASS_TEMPLATE:
                        ir.hashable_templates.add(_qualified_template(tdecl))
                    continue
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
            if cur.kind in (K.CLASS_DECL, K.STRUCT_DECL) and cur.is_definition():
                c = _class(cur, header, pkg.name)
                if c.name in _SKIP_CLASSES:
                    ir.report.append(f"{c.name}: skipped (overrides.toml [skip])")
                    continue
                if c.unbindable:
                    ir.report.extend(c.skipped)
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
                              is_noexcept=_is_noexcept(cur), doc=_doc_with_deprecation(cur), header=header,
                              is_operator=cur.spelling.startswith("operator"), skip_reason=reason,
                              qualified=f"{ns}{cur.spelling}", scope=scope,
                              defined_in_header=cur.is_definition() or cur.get_definition() is not None, mangled=cur.mangled_name)
                if fn.skip_reason is None:
                    fn.skip_reason = _unsupported(cur.result_type, allow_out=False)
                if fn.skip_reason is not None:
                    ir.report.append(f"{fn.name}(...): {fn.skip_reason}")
                ir.functions.append(fn)
            elif cur.kind in (K.TYPEDEF_DECL, K.TYPE_ALIAS_DECL):
                ir.typedefs.append(TypeAlias(py_name=cur.spelling, target=_canonical_args(cur.underlying_typedef_type),
                                             written=_type_spelling(cur.underlying_typedef_type), scope=scope))
                _note_instance(cur.underlying_typedef_type)      # BVH_Array3d = NCollection_LinearVector<...>: bind the instantiation
                if ns != "":
                    continue                       # alias instantiation (6c) only at package level
                if not any(c.py_name == cur.spelling for c in ir.classes):     # the same alias appears in several headers
                    inst = _alias_instance(tu, cur, header, pkg.name, ir.report)
                    if inst is not None:
                        ir.classes.append(inst)
            elif cur.kind in (K.CLASS_TEMPLATE, K.FUNCTION_TEMPLATE):
                ir.report.append(f"{cur.spelling}: template (not bound)")
        # bases that are un-aliased template instantiations (BRepGraph_WiresOfEdge : EdgeParentsOf<...>): instantiated
        # on demand under the mangled name, so that the derived class can be bound (Design.md 6c)
        seen_uses: set[str] = set()
        while len(_template_bases) > 0 or len(_template_uses) > 0:
            if len(_template_bases) > 0:
                derived, base_type, base_header = _template_bases.pop(0)
                what = f"{derived}: base class"
            else:
                base_type, base_header, derived = _template_uses.pop(0), ir.headers[0], ""
                what = "used in a signature:"
            base_name = _instance_spelling(base_type) if derived != "" else _type_spelling(base_type)
            if base_name in seen_uses or any(c.name == base_name for c in ir.classes):
                continue
            seen_uses.add(base_name)
            if base_name in known_elsewhere or base_name in _SKIP_CLASSES:
                continue                              # bound by an earlier package/run (manifest) or skipped on purpose
            inst = _instantiate_template(tu, base_type, base_header, pkg.name, ir.report, f"{what} {base_name}", None)
            if inst is not None and inst.name != base_name:
                # defaulted arguments spelled out by the instantiation (BVH_PairTraverse<double, 3> -> <double, 3, void, double>):
                # the derived classes name the base as instantiated
                for c in ir.classes:
                    c.bases = [inst.name if x == base_name else x for x in c.bases]
                seen_uses.add(inst.name)
            if inst is not None:
                add_class(inst)
        # R-TEMPLATE-BASE: template bases of instantiations are spelled only after substitution (BVH_BaseBox<double, 3, BVH_Box>,
        # BVH_BaseTraverse<double>): a probe typedef per spelling in a second parse gives them a libclang Type to instantiate from;
        # what still cannot be instantiated is dropped from the derived class's bases (reported) instead of skipping the class
        for _ in range(4):
            todo = [(d, b, h) for d, b, h in _dependent_bases if b not in seen_uses and not any(c.name == b for c in ir.classes)
                    and b not in (known_elsewhere or set())]
            if len(todo) == 0:
                break
            spellings = sorted({b for _, b, _ in todo})
            probe = Path(td) / f"{pkg.name}__probe.hxx"
            probe.write_text(umbrella.read_text() + "".join(f"using nanoocp_probe_{i} = {b};\n" for i, b in enumerate(spellings)))
            tu2 = index.parse(str(probe), args=args)
            probes = {cur.spelling: cur for cur in tu2.cursor.get_children() if cur.kind == K.TYPE_ALIAS_DECL and cur.spelling.startswith("nanoocp_probe_")}
            _dependent_bases.clear()
            for i, b in enumerate(spellings):
                seen_uses.add(b)
                cur = probes.get(f"nanoocp_probe_{i}")
                derived_names = [d for d, bb, _ in todo if bb == b]
                inst = None
                if cur is not None:
                    inst = _instantiate_template(tu2, cur.underlying_typedef_type, ir.headers[0], pkg.name, ir.report, f"{derived_names[0]}: base class {b}", None)
                else:
                    ir.report.append(f"{derived_names[0]}: base class {b}: the probe typedef did not compile")
                if inst is not None:
                    if inst.name != b:            # defaulted arguments spelled out by the instantiation: the derived classes follow
                        for c in ir.classes:
                            c.bases = [inst.name if x == b else x for x in c.bases]
                    add_class(inst)
        # a template base that could not be instantiated is dropped from its derived classes (R-TEMPLATE-BASE): the class binds
        # without the base's members. A Transient class whose only path to Standard_Transient is that base cannot be bound at all.
        names = {c.name for c in ir.classes}
        for c in ir.classes:
            for b in list(c.bases):
                if "<" in b and b not in names and not b.startswith(("std::", "opencascade::handle<")) and b not in (known_elsewhere or set()) \
                        and b.split("<")[0] not in BINDERS:
                    c.bases.remove(b)
                    c.skipped.append(f"{c.name}: template base {b} cannot be instantiated -> dropped, its members are not inherited (R-TEMPLATE-BASE)")
            if c.is_transient and len(c.bases) == 0 and c.name != "Standard_Transient":
                c.skipped.append(f"{c.name}: its path to Standard_Transient was a dropped template base -> class skipped")
                c.unbindable = True
        ir.classes = [c for c in ir.classes if not c.unbindable]
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
    if pkg.name in _BINARY_PACKAGES:            # R-STREAM-OUT/IN: binary formats -> bytes / typing.BinaryIO
        for params in [m.params for c in ir.classes for m in c.methods] + [f.params for f in ir.functions]:
            for prm in params:
                if prm.stream != StreamKind.NONE:
                    prm.binary = True
    if pkg.name == "NCollection":
        for spelled in _EXTRA_INSTANCES:
            m = re.match(r"(\w+)<(.+)>$", spelled)
            if m is None or m.group(1) not in BINDERS:
                ir.report.append(f"overrides [instantiate]: cannot parse or no binder for {spelled}")
                continue
            args = [a.strip() for a in m.group(2).split(",")]
            ir.instances.setdefault(spelled, TemplateInstance(template=m.group(1), args=args, key=spelled))
    return ir
