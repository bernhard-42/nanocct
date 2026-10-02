"""libclang front end: parse one OCCT package as a single translation unit and build the IR."""
from __future__ import annotations

import ctypes
import keyword
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from fnmatch import fnmatch
from pathlib import Path

from clang import cindex
from clang.cindex import AccessSpecifier as Access
from clang.cindex import CursorKind as K
from clang.cindex import TypeKind as TK

from .binders import BINDERS, instance_args
from .model import (Class, Constant, Constructor, Conversion, ConversionKind, Enum, Field, Function, Method, PackageIR, Param,
                    ResultKind, StreamKind, TemplateInstance, TypeAlias)
from .occt import OcctTree, Package

# R-CHAR: a plain char is a primitive and passes through; nanobind's type_caster<char> makes it a 1-character str
_PRIMITIVE_KINDS = {
    TK.BOOL, TK.CHAR_U, TK.UCHAR, TK.CHAR16, TK.CHAR32, TK.USHORT, TK.UINT, TK.ULONG,
    TK.ULONGLONG, TK.CHAR_S, TK.SCHAR, TK.WCHAR, TK.SHORT, TK.INT, TK.LONG, TK.LONGLONG,
    TK.FLOAT, TK.DOUBLE, TK.LONGDOUBLE, TK.ENUM,
}
# R-HANDLE, R-NCHANDLE: the smart pointers that are transparent in Python (a caster each in nanocct_common.h): the
# object behind them is what gets bound, a null one is None -- opencascade::handle<T> for Transients and
# NCollection_Handle<T>, OCCT's reference-counted owner of a non-Transient object
_SMART_HANDLES = ("handle", "NCollection_Handle")
# R-ITERATOR: the STL-style iterator templates, and the end marker of a forward range (the result of every end() next to
# a NCollection_ForwardRangeIterator begin()); members taking or returning them are skipped
_STL_ITERATORS = {"NCollection_ForwardRangeIterator", "NCollection_ForwardRangeSentinel", "NCollection_IndexedIterator",
                  "NCollection_StlIterator", "NCollection_UtfIterator"}
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
# Classes bound without any constructor. On MSVC it is the *constructor* that stores the vptr, so it is the one
# thing that needs the class's vtable -- and a vtable slot for a virtual OCCT declares without Standard_EXPORT
# cannot be filled (measured on gauss 2026-09-24: placement new -> LNK2019, while binding the class, calling its
# methods and nanobind's wrap_destruct<T> all link). Dropping the constructors therefore keeps the whole class.
_SKIP_CONSTRUCTORS = set(_OVERRIDES.get("skip", {}).get("constructors", []))
# nanobind builds a signature by recursing once per parameter, and MSVC gives up past ~38 with C1202, which no
# flag raises (/constexpr:depth and /constexpr:steps both tested). 37 parameters compile, 40 do not.
_MAX_PARAMS = int(_OVERRIDES.get("skip", {}).get("max_params", 0))
_EXTRA_INSTANCES = list(_OVERRIDES.get("instantiate", {}).get("extra", []))
_INCLUDE_HEADERS: dict[str, list[str]] = _OVERRIDES.get("include", {}).get("headers", {})   # package -> the only headers to bind
INCLUDE_PACKAGES: dict[str, list[str]] = _OVERRIDES.get("include", {}).get("packages", {})   # toolkit -> the only packages to generate
# package -> the platform.system() values that build it; every other platform skips the package before parsing it
PLATFORM_PACKAGES: dict[str, list[str]] = _OVERRIDES.get("platform", {})
# toolkit -> toolkits it must link although nothing in its signatures names them (R-LINK, overrides.toml [link] extra)
EXTRA_LINKS: dict[str, list[str]] = _OVERRIDES.get("link", {}).get("extra", {})
# classes with a zero-copy numpy view (__array__); the "how" is a nanocct_def_views<T> specialisation (R-VIEW, 8.10, 8.21)
VIEW_CLASSES: set[str] = set(_OVERRIDES.get("views", {}).get("classes", []))
NOT_VALUE_COPY: set[str] = set(_OVERRIDES.get("not_value_copy", {}).get("classes", []))   # R-RESULT: const& results by reference
_BINARY_PACKAGES = set(_OVERRIDES.get("stream", {}).get("binary_packages", []))   # packages whose streams carry binary formats (BinTools)
_BINARY_MEMBERS = set(_OVERRIDES.get("stream", {}).get("binary_members", []))     # single members ("TDocStd_Application::Open") in a text package
_BYTES_MEMBERS = set(_OVERRIDES.get("bytes", {}).get("members", []))              # R-BYTES: `const uint8_t*` + length -> one `bytes` parameter

_UNSUPPORTED_RE = re.compile(
    # basic_streambuf and basic_ios too: OSD_FileSystem::OpenStreamBuffer (shared_ptr<std::streambuf>) was reported as
    # "iostream type" on macOS and Linux but bound on Windows, where it is spelled basic_streambuf<char,std::char_traits<char>>
    # (2026-09-30); its result type has no Python type, so it was uncallable there
    r"std::(__\w+::)?((basic_)?(ostream|istream|iostream|stringstream|ostringstream|istringstream|streambuf|ios)|ios_base)\b"
)
# Other std types nanobind has no caster for. Reported by name: "iostream type" was the message for these too until
# 2026-09-22, which read as a stream in the report (DE_Wrapper::GlobalLoadMutex returns a std::mutex&).
_UNSUPPORTED_STD_RE = re.compile(r"std::(__\w+::)?(locale|thread|mutex|atomic|type_info|exception_ptr)\b")
# R-STL: std templates nanobind casts (nanobind/stl/*.h, all included from nanocct_common.h)
_STD_TEMPLATES_OK = {"shared_ptr", "unique_ptr", "vector", "map", "unordered_map", "set", "unordered_set", "pair",
                     "optional", "function", "tuple", "array", "variant", "list", "basic_string", "basic_string_view",
                     "bitset"}   # R-BITSET: set[int] of the set bits' indices (its size is a non-type argument, kind INVALID)


def _resource_dir() -> str | None:
    clang = shutil.which("clang")
    if clang is None:
        return None
    rd = subprocess.run([clang, "-print-resource-dir"], capture_output=True, text=True, check=True).stdout.strip()
    if rd == "":
        return None
    return rd


# Symbols the pip `clang` bindings register that an older libclang does not export. cindex registers *every* binding
# on first use and raises LibclangError on the first miss, so the system library has to be probed before it is chosen:
# Ubuntu 22.04 ships libclang 14, the wheel's bindings are 18.1.1, and `clang_CXXMethod_isDeleted` is missing there
# ("undefined symbol", banach 2026-09-23). The last two are the generator's own extras (6c, R-USING), which have no
# cindex wrapper -- if a library lacks them the run would fail later anyway.
_LIBCLANG_REQUIRED_SYMBOLS = ("clang_CXXMethod_isDeleted", "clang_getSpecializedCursorTemplate",
                              "clang_getNumOverloadedDecls", "clang_getOverloadedDecl")


def _libclang_is_compatible(path: Path) -> bool:
    """Whether this libclang exports what the installed cindex bindings and this generator need. Probed with ctypes
    because cindex accepts a library file only once: a wrong choice cannot be taken back."""
    try:
        lib = ctypes.cdll.LoadLibrary(str(path))
    except OSError:
        return False
    return all(hasattr(lib, name) for name in _LIBCLANG_REQUIRED_SYMBOLS)


def configure_libclang() -> str:
    """Prefer the libclang shipped with the clang on PATH (same version as the SDK/stdlib it was
    tested with) *when it is new enough for the installed bindings*; fall back to the pip 'libclang' wheel. Returns a
    description for logging. Idempotent: cindex accepts the library file only before first use."""
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
            for hit in hits:
                if _libclang_is_compatible(hit):
                    cindex.Config.set_library_file(str(hit))
                    return f"system libclang {hit}"
            if len(hits) > 0:
                return f"pip libclang (system {hits[0]} is too old for the installed bindings)"
    return "pip libclang"


# Third-party headers that an *installed* OCCT header includes, so the parse needs them on the include path just as
# the build did: RWGltf_GltfJsonParser.hxx has `#include <rapidjson/document.h>` under HAVE_RAPIDJSON. deps/build-occt-macos.sh
# puts them next to the OCCT install (deps/rapidjson from deps/fetch-rapidjson.sh); the list grows if
# another one turns up. FreeType is not here: OCCT's headers only forward-declare its types.
_THIRD_PARTY_INCLUDES = (("rapidjson", "include"),)


def clang_args(tree: OcctTree) -> list[str]:
    args = ["-x", "c++", "-std=c++17", f"-I{tree.include_dir}", "-DHAVE_FREETYPE", "-DHAVE_RAPIDJSON"]
    for parts in _THIRD_PARTY_INCLUDES:
        candidate = tree.install.parent.joinpath(*parts)
        if candidate.is_dir():
            args.append(f"-I{candidate}")
    rd = _resource_dir()
    if rd is not None:
        args += ["-resource-dir", rd]
    if platform.system() == "Darwin":
        sdk = subprocess.run(["xcrun", "--show-sdk-path"], capture_output=True, text=True, check=True).stdout.strip()
        if sdk != "":
            args += ["-isysroot", sdk]
    elif platform.system() == "Windows":
        # libclang finds the MSVC toolchain and the Windows SDK by itself, but MSVC's STL refuses a clang older than
        # its own vintage (yvals_core.h:899-917: "STL1000: Unexpected compiler version, expected Clang 19.0.0 or
        # newer" against MSVC 14.44), and the pip libclang wheel is 18.1.1 -- the newest there is. This parse is not
        # a compile: nothing is codegen'd and the STL headers are only read for declarations, so the documented
        # opt-out applies (8.2, 2026-09-23).
        args += ["-D_ALLOW_COMPILER_AND_STL_VERSION_MISMATCH"]
    # An escape hatch for an environment libclang cannot work out by itself. It exists for the manylinux container,
    # where the compiler is gcc-toolset-14 under /opt/rh but libclang's GCC detection only searches /usr/lib/gcc and
    # would read the image's gcc 8 standard library instead (deps/manylinux.Dockerfile sets --gcc-install-dir).
    extra = os.environ.get("NANOCCT_CLANG_ARGS", "").split()
    if len(extra) > 0:
        args += extra
        print(f"clang args from NANOCCT_CLANG_ARGS: {' '.join(extra)}", file=sys.stderr)
    return args


# Binding-Rules.md R-DOCSTRING: a class's or member's docstring is its raw_comment without the comment markers
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


# Binding-Rules.md R-DEPRECATED
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
    message as the first line, so the OCCT documentation's advice reaches the Python user (Binding-Rules.md)."""
    doc = _doc(cursor)
    message = _deprecation_message(cursor)
    if message is None:
        return doc
    note = "Deprecated in OCCT" + (f": {message}" if message != "" else ".")
    return note if doc == "" else f"{note}\n\n{doc}"


# Binding-Rules.md R-DEFAULT, R-DEFAULT-QUAL
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
        # a type nested in a class is qualified too (`= Options()` inside BRepGraphInc_Populate); so is a value reference into
        # a class or namespace: the class's own members are handled above, a nested class sees the enclosing class's
        # enumerators unqualified (`= IterationFilter_None` inside Font_TextFormatter::Iterator), a derived class its base's
        qualified = _scope_qualified(target, need_namespace=False)
        if qualified is None:
            continue
        for i, tok in enumerate(expr):
            if tok == target.spelling and (i == 0 or expr[i - 1] != "::"):
                expr[i] = qualified
    joined = _SUBST.apply(" ".join(expr))        # template parameters in defaults (Element_t(0)) while instantiating
    # a functional cast whose type became a multi-word builtin (`T(0)` -> `unsigned long(0)` in NCollection_Vec3<unsigned long>)
    # is not valid C++: spell it as a C-style cast, `(unsigned long)(0)`
    joined = re.sub(r"\b((?:unsigned|signed|long|short|char|int|double|float)(?:\s+(?:unsigned|signed|long|short|char|int|double|float))+)\s*\(",
                    r"(\1)(", joined)
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
    if decl.spelling in _SMART_HANDLES and canon.get_num_template_arguments() == 1:
        return _class_behind(canon.get_template_argument_type(0))
    parent = decl.semantic_parent
    if parent is not None and parent.kind == K.NAMESPACE and (parent.spelling == "std" or parent.spelling.startswith("__")):
        return ""
    return _canonical_args(canon).replace("const ", "")


# Binding-Rules.md R-ENUM-ARG (nb::arg(...).noconvert() emitted in emit._args)
def _is_enum(t: cindex.Type) -> bool:
    """An enum or a std::optional of one, possibly behind const/& (not behind a pointer). The optional too: nanobind's
    optional caster hands the convert flag to the enum caster, and BRepGraph_ChildExplorer(g, typed root, Kind.Edge,
    True, False) then reached (TargetKind, std::optional<Kind> AvoidKind, EmitAvoidKind) with AvoidKind = Kind(1)."""
    canon = t.get_canonical()
    while canon.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE):
        canon = canon.get_pointee().get_canonical()
    if canon.kind == TK.RECORD and canon.get_num_template_arguments() == 1:
        decl = canon.get_declaration()
        parent = decl.semantic_parent
        while parent is not None and parent.kind == K.NAMESPACE and parent.spelling.startswith("__"):   # libc++'s std::__1
            parent = parent.semantic_parent
        if decl.spelling == "optional" and parent is not None and parent.kind == K.NAMESPACE and parent.spelling == "std":
            return _is_enum(canon.get_template_argument_type(0))
    return canon.kind == TK.ENUM


# Binding-Rules.md R-HANDLE (nb::arg(...).none() emitted in emit._args)
def _is_handle(t: cindex.Type) -> bool:
    """opencascade::handle<T>, possibly behind const/&."""
    canon = t.get_canonical()
    while canon.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE):
        canon = canon.get_pointee().get_canonical()
    if canon.kind != TK.RECORD:
        # inside a class template (6c walk) handle<BVH_Builder<NumType, Dimension>> is a dependent type without a declaration
        return _SUBST.active and re.match(r"^(const )?(opencascade::|occ::)?handle<", _type_spelling(t)) is not None
    decl = canon.get_declaration()
    return decl.kind != K.NO_DECL_FOUND and decl.spelling in _SMART_HANDLES and canon.get_num_template_arguments() == 1


# Binding-Rules.md R-OUT, R-OUT-HANDLE; R-INOUT is decided in _params from overrides.toml
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
    # R-REF-CLASS: a non-const reference to a bound class is no out-parameter: it keeps its T& type, nanobind passes the
    # instance by reference and the callee mutates it in place
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
    """The 6c walk (Binding-Rules.md): while the definition of a class template is walked to bind one instantiation, every type
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
    return _drop_ignored_const(_SUBST.apply(_type_spelling_raw(t)))


# A dependent member type that names a reference: OCCT writes `const typename Container::const_reference Value() const`
# (NCollection_Iterator.hxx:86, and :88 for reference). [dcl.ref]/1 ignores that const and gcc accepts the declaration
# inside the template -- but our static_cast spells the type with the template argument substituted, and there gcc
# refuses it while clang does not: "const qualifiers cannot be applied to C<X>::const_reference {aka const X&}"
# (g++ 11.5, minimal case verified both ways on banach, 2026-09-23). The spelling is the only handle: while the
# template is walked libclang reports the type as UNEXPOSED with no canonical type and no declaration, so nothing can
# be asked about it. Hence the two conventional container typedef names, which are references by definition and are
# the ones NCollection uses.
_IGNORED_CONST_SUFFIXES = ("::reference", "::const_reference")


def _drop_ignored_const(spelled: str) -> str:
    if spelled.startswith("const typename ") and spelled.endswith(_IGNORED_CONST_SUFFIXES):
        return spelled[len("const "):]
    return spelled



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


# Binding-Rules.md R-TEMPLATE-NAME: an instantiation or explicit specialisation with no typedef -> template__arg1__arg2
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
    """Python attribute path of a bound C++ type relative to nanocct.<package>: nested classes and namespaces keep
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


# Binding-Rules.md R-CSTR-NULL: the const char* test for a parameter with a null default
def _is_cstring(t: cindex.Type) -> bool:
    """const char* (Standard_CString): the pointer the char caster maps to str."""
    canon = t.get_canonical()
    if canon.kind != TK.POINTER:
        return False
    pointee = canon.get_pointee().get_canonical()
    return pointee.kind in (TK.CHAR_S, TK.CHAR_U) and pointee.is_const_qualified()


_INTEGRAL_KINDS = (TK.INT, TK.UINT, TK.LONG, TK.ULONG, TK.LONGLONG, TK.ULONGLONG, TK.SHORT, TK.USHORT)


def _is_const_byte_ptr(t: cindex.Type) -> bool:
    """`const uint8_t*` / `const Standard_Byte*` -- the input half of OCCT's buffer pairs (R-BYTES).

    Only the const form: a non-const `uint8_t*` is an output buffer the caller is expected to size and own
    (FSD_Base64::Encode's first overload, FSD_Base64::Decode's), which `bytes` cannot express.
    """
    canon = t.get_canonical()
    if canon.kind != TK.POINTER:
        return False
    pointee = canon.get_pointee()
    return pointee.is_const_qualified() and pointee.get_canonical().kind == TK.UCHAR


# Binding-Rules.md R-UNSUPPORTED, R-ARRAY, R-ITERATOR, R-STL, R-CSTRING
def _unsupported(t: cindex.Type, allow_out: bool) -> str | None:
    canon = t.get_canonical()
    cs = canon.spelling
    if _UNSUPPORTED_RE.search(cs) is not None:
        return "iostream type"
    std_type = _UNSUPPORTED_STD_RE.search(cs)
    if std_type is not None:
        return f"unsupported std type: std::{std_type.group(2)}"
    if canon.kind == TK.RVALUEREFERENCE:
        return "rvalue reference"
    # R-ARRAY: _params binds a fixed-size array parameter (R-FIXED-ARRAY); any other array is skipped and reported
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
        # R-CSTRING, R-CHAR16: const char* / const char16_t* (Standard_ExtString) are strings, casters in nanocct_common.h
        if pk in (TK.CHAR_S, TK.CHAR_U, TK.CHAR16) and pointee.is_const_qualified():
            return None
        if pk in _PRIMITIVE_KINDS or pk == TK.POINTER:
            return "raw pointer to primitive"
    if canon.kind == TK.LVALUEREFERENCE and canon.get_pointee().get_canonical().kind == TK.RECORD:
        pointee = canon.get_pointee()
        d = pointee.get_declaration()
        # R-PTR-INCOMPLETE for references: `const AVStream&` (FFmpeg) and `XEvent&` (X11) in Media/Xw are forward-declared
        # with no header anywhere; nanobind needs the complete type (typeid). Same test as for pointers above.
        if d.kind != K.NO_DECL_FOUND and d.get_definition() is None and pointee.get_canonical().get_num_template_arguments() <= 0 \
                and (_INCLUDE_DIR is None or not (_INCLUDE_DIR / f"{d.spelling}.hxx").exists()):
            return "reference to incomplete type"
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
    if base.kind == TK.ENUM:
        # R-UNBOUND-TYPE for the standard library: an enum of it has no Python type, so a member taking or returning one is
        # uncallable. libstdc++ spells std::ios_base::openmode as the enum std::_Ios_Openmode, where libc++ and MSVC have an
        # integer typedef: OSD_OpenFileDescriptor(name, openmode) raised TypeError on Linux only (measured 2026-09-30)
        ns = base.get_declaration().semantic_parent
        while ns is not None and ns.kind != K.NAMESPACE and ns.kind != K.TRANSLATION_UNIT:
            ns = ns.semantic_parent
        if ns is not None and ns.kind == K.NAMESPACE and ns.spelling in ("std", "__1"):
            return f"std::{base.get_declaration().spelling} (a standard-library enum, no Python type)"
    if canon.kind == TK.LVALUEREFERENCE and canon.get_pointee().get_canonical().kind == TK.POINTER:
        return "reference to pointer"
    if canon.kind == TK.LVALUEREFERENCE and not allow_out:
        pointee = canon.get_pointee()
        if not pointee.is_const_qualified() and pointee.get_canonical().kind in _PRIMITIVE_KINDS:
            return "reference to primitive"
    return None


# Binding-Rules.md R-RESULT
def _result_kind(t: cindex.Type) -> tuple[str, str]:
    """How a returned pointer/reference must be treated (see Binding-Rules.md)."""
    canon = t.get_canonical()
    if canon.kind == TK.RECORD:
        # R-RESULT for `T` by value, T Transient (Geom2dGcc_QualifiedCurve::Qualified() -> Geom2dAdaptor_Curve): a nanobind-
        # owned copy has a reference count of 0, and the first handle<T> parameter it is passed to deletes it when that
        # handle goes (8.18). It is moved to the heap into a handle instead, as every Transient constructor does.
        decl = canon.get_declaration()
        if decl.kind in (K.CLASS_DECL, K.STRUCT_DECL) and _derives_from(decl, "Standard_Transient"):
            return ResultKind.VALUE_TRANSIENT, _type_spelling(t).replace("const ", "").strip()
        return ResultKind.VALUE, ""
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


# Binding-Rules.md R-STREAM-OUT, R-STREAM-IN
def _stream_kind(t: cindex.Type) -> str:
    """'out' for a mutable std::ostream& (Dump, DumpJson, Print, Write: the text is returned as a str), 'in' for a
    std::istream& or a std::stringstream (const or not: InitFromJson, Read: a text file-like object is read into a stringstream, nanocct::TextInput), else ''."""
    canon = t.get_canonical()
    if canon.kind != TK.LVALUEREFERENCE:
        return ""
    pointee = canon.get_pointee()
    decl = pointee.get_canonical().get_declaration()
    if decl.kind == K.NO_DECL_FOUND:
        return ""
    # The MSVC STL declares its types inside `extern "C++" { }`, so the parent is a LINKAGE_SPEC with an empty
    # spelling and the namespace sits above it; libc++ instead nests them in the inline namespace __1. Walk up
    # through both, or every Dump/Write(ostream&) on Windows falls out as "iostream type" (TKCAF alone reported 24,
    # 2026-09-23).
    parent = decl.semantic_parent
    while parent is not None and parent.kind == K.LINKAGE_SPEC:
        parent = parent.semantic_parent
    if parent is None or parent.kind != K.NAMESPACE:
        return ""
    if not (parent.spelling == "std" or parent.spelling.startswith("__")):
        return ""
    if decl.spelling == "basic_ostream" and not pointee.is_const_qualified():
        return StreamKind.OUT
    if decl.spelling in ("basic_istream", "basic_stringstream", "basic_istringstream"):
        return StreamKind.IN
    return ""


# Binding-Rules.md R-STR
def _is_print_operator(name: str, params: list[Param], result_type: cindex.Type) -> bool:
    """`Standard_OStream& operator<<(Standard_OStream&, const T&)`, free or hidden friend: OCCT's "print me" idiom. The
    stream is the first operand, so it is no member of T in Python terms; it becomes T.__str__ (emit._free_operator),
    with the chained stream result dropped like R-STREAM-OUT does for methods. Whether it really prints T -- and not,
    as BinTools' operator<<(ostream&, const gp_Pnt&) does, write binary doubles for another package's class -- is
    decided by the emitter, which knows the class, its header and the package's stream kind."""
    return (name == "operator<<" and len(params) == 2 and params[0].stream == StreamKind.OUT
            and _stream_kind(result_type) == StreamKind.OUT)


# R-OPTIONAL-PTR applies to these reasons; "unsupported std type" is not among them (no OCCT API has an optional
# std::mutex*/std::locale* parameter -- such a parameter would be reported instead of silently dropped).
_OPTIONAL_PTR_REASONS = ("raw pointer to primitive", "void pointer", "pointer to incomplete type", "function pointer", "reference to pointer", "iostream type")


# Binding-Rules.md R-FIXED-ARRAY
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


def _is_empty_shared_ptr_default(param: cindex.Cursor, default: str | None) -> bool:
    """A std::shared_ptr<T> parameter whose default is its own empty form -- `const std::shared_ptr<std::ostream>&
    theStream = std::shared_ptr<std::ostream>()` (RWPly_PlyWriterContext::Open, "open the file yourself").

    The type has no caster, but the default does not need one: R-OPTIONAL-PTR passes `nullptr`, which is that same
    empty shared_ptr. Without this the whole method is skipped, and RWPly_PlyWriterContext -- whose every other member
    needs an open stream -- is bound but unusable."""
    if default is None:
        return False
    spelling = _type_spelling(param.type).removeprefix("const ").rstrip("& ").strip()
    if not spelling.startswith("std::shared_ptr<"):
        return False
    # The two sides cannot be compared as strings: the *type* is canonicalised through the standard library's typedefs
    # while the default expression stays as written, and the libraries differ. libstdc++ (banach, 2026-09-23):
    #     type    'const std::shared_ptr<std::basic_ostream<char, std::char_traits<char>>> &'
    #     default 'std::shared_ptr < std::ostream >()'
    # libc++ keeps `std::ostream` on both sides, which is why an equality test passed on macOS and silently skipped
    # RWPly_PlyWriterContext::Open on Linux -- the exact "bound but unusable" outcome this rule exists to prevent.
    # What matters is only that the default value-initialises an empty shared_ptr, so that is what is checked.
    compact = default.replace(" ", "")
    return compact.startswith("std::shared_ptr<") and compact.endswith(">()")


def _stl_iterator_in_6c(t: cindex.Type) -> str | None:
    """R-ITERATOR inside a 6c walk: a dependent type has no declaration, so _unsupported's STL-iterator test does not see
    NCollection_Iterator<Container>::ValueIter() -> NCollection_IndexedIterator<...> or a binder's nested DynamicIterator;
    after substitution the spelling names it (25 members bound uncallable until 2026-09-30, final review)."""
    if not _SUBST.active:
        return None
    spelled = re.sub(r"^(const\s+)?(typename\s+)?|\s*[&*]+\s*$", "", _type_spelling(t)).strip()
    # also the container's STL member typedef: NCollection_Iterator<Container>::ValueIter() returns
    # `typename Container::iterator` (NCollection_Iterator.hxx:76)
    if spelled.split("<")[0] in _STL_ITERATORS or re.search(r"::DynamicIterator<|::(const_)?iterator$", spelled) is not None:
        return "STL-style iterator"
    return None


def _binder_key(t: cindex.Type) -> str:
    """The registry key of the NCollection binder instantiation behind a parameter or result type (through const, &, *
    and handle<>), computed exactly as _note_instance records it -- or, for a class nested in one (`X<...>::Iterator`,
    `X<...>::DynamicIterator`), that key plus `::<Nested>`. "" for anything else. R-UNBOUND-TYPE asks the registry with it:
    comparing spellings instead had failed on default arguments (math_VectorBase<> vs <double>, dropped hashers)."""
    canon = t.get_canonical()
    while canon.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE, TK.POINTER):
        canon = canon.get_pointee().get_canonical()
    if canon.kind != TK.RECORD:
        return ""
    decl = canon.get_declaration()
    if decl.kind == K.NO_DECL_FOUND:
        return ""
    if decl.spelling in _SMART_HANDLES and canon.get_num_template_arguments() == 1:
        return _binder_key(canon.get_template_argument_type(0))
    owner = _NESTED_OWNER.get(decl.spelling, decl.spelling if decl.spelling in BINDERS else None)
    if owner is not None and canon.get_num_template_arguments() > 0:
        args = [_canonical_args(canon.get_template_argument_type(i)) for i in range(canon.get_num_template_arguments())]
        key = f"{owner}<{', '.join(instance_args(owner, args))}>"
        return key if owner == decl.spelling else key + "::Iterator"      # NCollection_TListIterator<T> is List<T>::Iterator
    m = re.match(r"^(NCollection_\w+)<(.*)>::(\w+)$", _canonical_args(canon))
    if m is not None and m.group(1) in BINDERS:                  # a class nested in a binder instantiation
        return f"{m.group(1)}<{', '.join(instance_args(m.group(1), _split_top(m.group(2))))}>::{m.group(3)}"
    return ""


# R-VIEW-GUARD (Binding-Rules.md): containers the binder guards -- every binder kind except NCollection_Shared, whose bound
# object is the wrapped container at a non-zero offset (a guard on the Shared's own address would never see its views)
_GUARDED_KINDS = frozenset(k for k in BINDERS if k != "NCollection_Shared")


def _container_kind(t: cindex.Type) -> str:
    """The NCollection binder kind (NCollection_List, ...) of the container a type names itself -- by value, reference or
    pointer, never through a handle -- or "". A class nested in an instantiation (an Iterator) is not a container. Inside a
    6c walk a type written with the template's parameters (`TheArray&` in Convert_CompBezierCurvesToBSplineCurveBase) has
    no declaration; the substituted spelling names the instantiation then (as for _stl_iterator_in_6c)."""
    canon = t.get_canonical()
    while canon.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE, TK.POINTER):
        canon = canon.get_pointee().get_canonical()
    if canon.kind == TK.RECORD:
        decl = canon.get_declaration()
        return decl.spelling if decl.spelling in _GUARDED_KINDS else ""
    if _SUBST.active:
        spelled = re.sub(r"^(const\s+)?(typename\s+)?|\s*[&*]+\s*$", "", _type_spelling(t)).strip()
        m = re.match(r"^(NCollection_\w+)\s*<.*>$", spelled)
        if m is not None and m.group(1) in _GUARDED_KINDS:
            return m.group(1)
    return ""


def _mutable_container(t: cindex.Type) -> bool:
    """R-VIEW-GUARD: a parameter OCCT may change a container through -- a non-const reference or pointer to one."""
    canon = t.get_canonical()
    if canon.kind not in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE, TK.POINTER):
        return False
    return not canon.get_pointee().is_const_qualified() and _container_kind(t) != ""


def _params(cursor: cindex.Cursor, qualified: str = "", scope: str = "", members: set[str] | None = None,
            allow_streams: bool = True) -> tuple[list[Param], str | None]:
    """allow_streams: False for constructors (an object may keep the stream reference beyond the call)."""
    params: list[Param] = []
    # R-INOUT: an out-parameter of a member listed in overrides.toml [inout] stays an input and is still returned.
    # The [inout] entries are glob patterns on the qualified name: "gp_Trsf::Transforms" exactly,
    # "*::InitFromJson" for every class, "DE*_Provider::Read" for every DataExchange provider (each one repeats the
    # same personizeWS(theWS) body, and forgetting one only shows up as four overload collisions in its report)
    inout = any(fnmatch(qualified, pattern) for pattern in _INOUT)
    binary = qualified in _BINARY_MEMBERS                         # R-STREAM-OUT, R-STREAM-IN: a document stream in a text package
    # R-BYTES: a `const uint8_t*` parameter immediately followed by its length is one `bytes` parameter.
    # Listed rather than inferred, because "the next integer is the length" is a convention and not a type:
    # every entry has been read. Without it the whole method is unbindable (raw pointer to primitive), which
    # is what kept FSD_Base64::Encode out while its Decode counterpart was bound and, for want of a buffer
    # view, useless.
    args = list(cursor.get_arguments())
    bytes_role: dict[int, str] = {}
    if qualified in _BYTES_MEMBERS:
        for j in range(len(args) - 1):
            if _is_const_byte_ptr(args[j].type) and args[j + 1].type.get_canonical().kind in _INTEGRAL_KINDS:
                bytes_role[j] = ""                                        # the buffer itself
                bytes_role[j + 1] = py_safe(args[j].spelling) or f"arg{j}"   # its length, dropped
    if members is None:
        members = set()
    for i, p in enumerate(args):
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
        if reason is None:
            reason = _stl_iterator_in_6c(p.type)
        name = py_safe(p.spelling)                 # R-KEYWORD: TDF_TagSource::Restore(const handle<TDF_Attribute>& with) -> with_
        if name == "":
            name = f"arg{i}"
        if reason in _OPTIONAL_PTR_REASONS and (
                p.type.get_canonical().kind == TK.POINTER and _default_expr(p, scope, members) in ("NULL", "nullptr", "0")
                or _is_empty_shared_ptr_default(p, _default_expr(p, scope, members))):
            # R-OPTIONAL-PTR: an optional output/context pointer (BRepFill_AdvancedEvolved::IsDone(unsigned int* theErrorCode
            # = nullptr), BRep_Tool::CurveOnSurface(..., bool* theIsStored = nullptr)) is dropped; the callee gets nullptr -- and
            # so is a std::shared_ptr<std::ostream> defaulted to its own empty form (RWPly_PlyWriterContext::Open), for which
            # nullptr is exactly that default (shared_ptr's nullptr_t constructor)
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
        if i in bytes_role:                    # R-BYTES
            params.append(Param(name=name, type=_type_spelling(p.type), default=None, is_out=False,
                                is_bytes=bytes_role[i] == "", bytes_of=bytes_role[i]))
            continue
        if reason is not None:
            # an unnamed parameter (`operator==(const X&, NCollection_ForwardRangeSentinel)`) by its position and type
            who = f"'{p.spelling}'" if p.spelling != "" else f"{i + 1} ({_type_spelling(p.type)})"
            return params, f"param {who}: {reason}"
        is_out = _is_out_param(p.type)
        _note_instance(p.type)
        default = _default_expr(p, scope, members)
        # R-CSTR-NULL: nanobind's const char* caster rejects None, so a null default (LDOM_XmlWriter(const char*
        # theEncoding = nullptr), STEPCAFControl_Writer::Transfer(..., const char* const theIsMulti = nullptr)) would be
        # unreachable -> nanocct::OptionalCString, `str | None = None`
        cstr_none = _is_cstring(p.type) and default in ("NULL", "nullptr", "0")
        # R-PTR-NULL: a class pointer takes None (nullptr), as a handle does (R-HANDLE): nanobind's pointer caster rejects None
        # without .none(). With a null default (BSplCLib_Cache(..., const NCollection_Array1<double>* theWeights = nullptr)) the
        # default itself would be refused; without one, OCCT's documented "NULL = no weights, non-rational" (BSplCLib.hxx:
        # BSplCLib::D0(..., const NCollection_Array1<double>* Weights, ...), BSplCLib::NoWeights() returns that nullptr) would
        # be unreachable. Without a default only a pointer to a class: const char* and const char16_t* are strings (R-CSTR-NULL,
        # R-CHAR16)
        canon = p.type.get_canonical()
        ptr_none = not cstr_none and canon.kind == TK.POINTER and (
            default in ("NULL", "nullptr", "0") or (default is None and canon.get_pointee().get_canonical().kind == TK.RECORD))
        params.append(Param(name=name, type=_type_spelling(p.type), default="nullptr" if cstr_none else default, is_out=is_out, is_inout=is_out and inout,
                            class_name=_class_behind(p.type), stream=stream, is_handle=_is_handle(p.type),
                            out_py=_out_py_type(p.type) if is_out else "", cstr_none=cstr_none, ptr_none=ptr_none,
                            instance_key=_binder_key(p.type),
                            binary=binary and stream != StreamKind.NONE, class_ancestors=_class_ancestors(p.type),
                            is_enum=_is_enum(p.type), guarded=_mutable_container(p.type),
                            container=canon.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE, TK.POINTER) and _container_kind(p.type) != ""))
    if cursor.type.kind == TK.FUNCTIONPROTO and cursor.type.is_function_variadic():
        return params, "variadic"
    return params, None


def _is_noexcept(cursor: cindex.Cursor) -> bool:
    k = cursor.exception_specification_kind
    return k in (cindex.ExceptionSpecificationKind.BASIC_NOEXCEPT, cindex.ExceptionSpecificationKind.DYNAMIC_NONE)


# PARALLELISATION (2026-09-24): these two accumulate *across* packages, so a sequential run lets a late package profit
# from what earlier ones discovered while a worker process only sees its own share -- which made one binding of 65000
# differ (BRepClass3d_SolidExplorer::Intersector). carry_state()/collect_state() make them an explicit input/output so
# a parallel driver can merge them at a barrier and re-parse to a fixpoint. _ancestors_cache (R-OVERLOAD-ORDER) travels the
# same way. Both hold only what a definition showed: a translation unit that merely forward-declares a class reads them
# and never writes, or the pool's order would decide which answer a later one is handed.
_derives_cache: dict[tuple[str, str], bool] = {}
_derives_stack: set[tuple[str, str]] = set()   # keys being resolved (recursion guard for CRTP bases)
_template_bases: list[tuple[str, cindex.Type, str]] = []   # (derived class, base type, header): bases that are template instantiations
_template_uses: list[cindex.Type] = []                      # template instantiations seen in bound signatures (on-demand 6c)
_dependent_bases: list[tuple[str, str, str]] = []           # (derived instantiation, substituted base spelling, header): template bases seen
                                                            # inside a 6c walk (BVH_Box<double, 3> : BVH_BaseBox<double, 3, BVH_Box>), resolved
                                                            # through a probe re-parse (R-TEMPLATE-BASE)
_dependent_uses: list[str] = []                             # substituted spellings of class template instantiations in the member
                                                            # signatures of a 6c walk (NCollection_Vec4<unsigned char>::xyz() ->
                                                            # NCollection_Vec3<unsigned char>): instantiated through the same probe (8.22)


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
    if decl.kind == K.NO_DECL_FOUND or decl.spelling in BINDERS or decl.spelling in _SMART_HANDLES:
        return False
    parent = decl.semantic_parent
    return not (parent is not None and parent.kind == K.NAMESPACE and (parent.spelling == "std" or parent.spelling.startswith("__")))


# Binding-Rules.md R-OVERLOAD-ORDER
_ancestors_cache: dict[str, tuple[str, ...]] = {}


def _class_ancestors(t: cindex.Type) -> tuple[str, ...]:
    """Every (transitive) base of the class behind a parameter type (through const/&/*/handle), spelled like
    _class_behind spells a parameter's class, so emit.order_by_derivation can tell that an overload taking the derived
    class must be registered before one taking the base. A base inside a class template counts only when it repeats the
    template's own parameters (NCollection_Array2<TheItemType> : NCollection_Array1<TheItemType>, so NCollection_Array2<gp_Pnt>
    has the ancestor NCollection_Array1<gp_Pnt>); one with other arguments is left out -- never a wrong ancestor, at worst
    a missing one."""
    canon = t.get_canonical()
    while canon.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE, TK.POINTER):
        canon = canon.get_pointee().get_canonical()
    if canon.kind != TK.RECORD:
        return ()
    decl = canon.get_declaration()
    if decl.kind == K.NO_DECL_FOUND:
        return ()
    if decl.spelling in _SMART_HANDLES and canon.get_num_template_arguments() == 1:
        return _class_ancestors(canon.get_template_argument_type(0))
    defn = decl.get_definition()     # the declaration may be a forward one (`class TopoDS_Face;`), which has no bases
    key = _canonical_args(canon)
    if defn is None:
        # only a forward declaration in this translation unit: what a translation unit with the definition found holds (this
        # process's, or carried in by carry_state); without that the bases are unknown here, and the answer is not cached --
        # the cache outlives the package, and a later translation unit that sees the definition must not be handed it
        # (which package a worker parses first is the pool's choice: R-CTOR-KEEP kept an argument in some runs only)
        if key in _ancestors_cache:
            return _ancestors_cache[key]
        found: list[str] = []
        _collect_ancestors(decl, canon, found, set())
        return tuple(found)
    decl = defn
    if key not in _ancestors_cache:
        found: list[str] = []
        _collect_ancestors(decl, canon, found, set())
        _ancestors_cache[key] = tuple(found)
    return _ancestors_cache[key]


def _collect_ancestors(cls: cindex.Cursor, canon: cindex.Type, found: list[str], seen: set[str]) -> None:
    """cls: the class declaration, canon: its canonical type (for an instantiation the one carrying the arguments)."""
    spelled = _canonical_args(canon).replace("const ", "")
    if spelled in seen:
        return
    seen.add(spelled)
    bases = [b for b in cls.get_children() if b.kind == K.CXX_BASE_SPECIFIER]
    if len(bases) == 0 and canon.get_num_template_arguments() > 0:
        # an implicit instantiation's cursor has no children: its bases are in the template's definition (as in _derives_from)
        tmpl = cindex.conf.lib.clang_getSpecializedCursorTemplate(cls)
        m = re.search(r"<(.*)>$", spelled)
        if tmpl is not None and tmpl.kind != K.NO_DECL_FOUND and m is not None:
            defn = tmpl.get_definition()
            _collect_template_ancestors(defn if defn is not None else tmpl, m.group(1), found, seen)
        return
    for b in bases:
        bt = b.type.get_canonical()
        d = bt.get_declaration()
        if bt.kind == TK.RECORD and d.kind != K.NO_DECL_FOUND and "type-parameter-" not in bt.spelling:
            found.append(_canonical_args(bt).replace("const ", ""))
            dd = d.get_definition()
            _collect_ancestors(dd if dd is not None else d, bt, found, seen)


def _collect_template_ancestors(tmpl: cindex.Cursor, args: str, found: list[str], seen: set[str]) -> None:
    """Bases of a class template's definition that repeat its own parameter list, instantiated with `args` (the
    derived instantiation's argument text), transitively."""
    own = ",".join(ch.spelling for ch in tmpl.get_children() if ch.kind in (K.TEMPLATE_TYPE_PARAMETER, K.TEMPLATE_NON_TYPE_PARAMETER))
    for b in tmpl.get_children():
        if b.kind != K.CXX_BASE_SPECIFIER:
            continue
        m = re.search(r"<(.*)>$", b.type.spelling)
        base = b.type.get_declaration()
        if m is None or m.group(1).replace(" ", "") != own or base.kind != K.CLASS_TEMPLATE:
            continue
        spelled = f"{_qualified_template(base)}<{args}>"
        if spelled in seen:
            continue
        seen.add(spelled)
        found.append(spelled)
        defn = base.get_definition()
        _collect_template_ancestors(defn if defn is not None else base, args, found, seen)


def _derives_from(cls: cindex.Cursor, root: str) -> bool:
    """True if cls is root or (transitively) derives from it, following the AST base specifiers. A base that is a template
    instantiation (SelectMgr_RectangularFrustum : SelectMgr_Frustum<4>, BRepExtrema_TriangleSet : BVH_PrimitiveSet<double, 3>)
    is followed into the template's definition through the base specifier's TEMPLATE_REF: libclang's cursor for the
    instantiation has no children, so it alone would say "no bases". The cache is keyed by USR, not spelling -- the
    instantiation and its template share the spelling (until 2026-09-22 the instantiation's False poisoned the template's
    answer, and such classes got placement-new constructors on a handle-based base)."""
    name = cls.spelling
    if name == root:
        return True
    if not cls.is_definition():
        defn = cls.get_definition()
        if defn is None:
            # only a forward declaration in this translation unit: what a translation unit with the definition found holds
            # (cached under the same USR, or carried in by carry_state); without that False, never cached -- a later
            # translation unit that sees the definition must not be handed it
            return _derives_cache.get((cls.get_usr() or name, root), False)
        cls = defn
    key = (cls.get_usr() or name, root)
    if key in _derives_cache:
        return _derives_cache[key]
    if key in _derives_stack:            # CRTP: Rules_Crtp<T> : Rules_CrtpBase<T, Rules_Crtp> names itself in its base
        return False
    _derives_stack.add(key)
    result = False
    for b in cls.get_children():
        if b.kind == K.CXX_BASE_SPECIFIER:
            targets = []
            d = b.type.get_declaration()
            if d.kind != K.NO_DECL_FOUND:
                targets.append(d)
            # an instantiation's cursor has no children: follow it to its template's definition (clang_getSpecializedCursorTemplate;
            # cindex has no wrapper) -- also when the base is written through a typedef (BRepExtrema_TriangleSet : BVH_PrimitiveSet3d)
            canon_decl = b.type.get_canonical().get_declaration()
            if canon_decl.kind != K.NO_DECL_FOUND and canon_decl.get_num_template_arguments() > 0:
                tmpl = cindex.conf.lib.clang_getSpecializedCursorTemplate(canon_decl)
                if tmpl is not None and tmpl.kind != K.NO_DECL_FOUND:
                    defn = tmpl.get_definition()
                    targets.append(defn if defn is not None else tmpl)
            if any(_derives_from(t, root) for t in targets):
                result = True
                break
    _derives_stack.discard(key)
    _derives_cache[key] = result
    return result


# Binding-Rules.md R-KEYWORD
def py_safe(name: str) -> str:
    """Python name for a C++ identifier: keywords get a trailing underscore (GProp_PEquation::Type::None -> None_)."""
    if keyword.iskeyword(name):
        return name + "_"
    return name


# Binding-Rules.md R-ENUM, R-ANON-ENUM
def _enum(cursor: cindex.Cursor, header: str, scope: str | None) -> Enum:
    qual = f"{scope}::{cursor.spelling}" if scope is not None else cursor.spelling
    values: list[tuple[str, str]] = []
    aliases: list[str] = []
    seen: set[int] = set()
    for v in cursor.get_children():
        if v.kind == K.ENUM_CONSTANT_DECL:
            cpp = f"{qual}::{v.spelling}" if cursor.is_scoped_enum() else (f"{scope}::{v.spelling}" if scope is not None else v.spelling)
            values.append((py_safe(v.spelling), cpp))
            # an enumerator repeating an earlier value is an alias in Python's enum.Enum: nanobind's export_values() iterates
            # the enum class, which skips aliases, so the emitter exports them by name (OCCT's "old aliases": Font_FA_Bold)
            if v.enum_value in seen:
                aliases.append(py_safe(v.spelling))
            seen.add(v.enum_value)
    return Enum(name=qual, py_name=cursor.spelling, values=values, is_scoped=cursor.is_scoped_enum(), doc=_doc(cursor), header=header,
                is_anonymous=cursor.is_anonymous() or cursor.spelling == "" or cursor.spelling.startswith("("), aliases=aliases)


# Binding-Rules.md R-UNDEFINED (skip_reason from the nm check in __main__), R-REF-PRIMITIVE (result_kind)
def _method(cursor: cindex.Cursor, cls_name: str, members: set[str]) -> Method | None:
    name = cursor.spelling
    # R-DELETED: operator= is not bound, without a report line (nor are the allocation operators)
    if name.startswith("operator") and name in ("operator=", "operator new", "operator delete", "operator new[]", "operator delete[]"):
        return None
    params, reason = _params(cursor, f"{cls_name}::{name}", cls_name, members)
    _note_instance(cursor.result_type)
    rk, rc = _result_kind(cursor.result_type)
    m = Method(name=name, params=params, result=_type_spelling(cursor.result_type), result_kind=rk, result_class=rc,
               is_static=cursor.is_static_method(),
               is_const=cursor.is_const_method(), is_noexcept=_is_noexcept(cursor), doc=_doc_with_deprecation(cursor),
               is_deprecated=cursor.availability == cindex.AvailabilityKind.DEPRECATED,
               is_operator=name.startswith("operator"), skip_reason=reason, result_class_name=_class_behind(cursor.result_type),
               result_instance_key=_binder_key(cursor.result_type), result_container=_mutable_container(cursor.result_type))
    result_stream = _stream_kind(cursor.result_type)
    returns_stream = result_stream != StreamKind.NONE and any(p.stream == result_stream for p in params)
    if m.skip_reason is None and returns_stream:
        # Standard_OStream& Print(x, Standard_OStream&), Standard_IStream& BinObjMgt_Persistent::Read(Standard_IStream&): the stream
        # itself, for chaining (R-STREAM-OUT, R-STREAM-IN)
        m.result, m.result_kind, m.result_class = "void", ResultKind.VALUE, ""
    rc0 = cursor.result_type.get_canonical()
    self_type = _type_spelling(rc0.get_pointee()).replace("const ", "") if rc0.kind == TK.LVALUEREFERENCE else ""
    if m.skip_reason is None and (any(p.is_out for p in params) or m.is_operator and any(p.stream != StreamKind.NONE for p in params)) \
            and self_type != "" and (self_type == cls_name or _derives_from(cursor.semantic_parent, self_type)):
        # ... also when the reference is to a base class: `Storage_BaseDriver& FSD_File::GetReference(int&) override` returns
        # *this through the virtual's declared type, and dropping it only in the base made Storage_BaseDriver.GetReference()
        # -> int but FSD_File.GetReference() -> (Storage_BaseDriver, int) for the same virtual (final review 2026-09-30)
        # `const BinObjMgt_Persistent& GetInteger(int&)`: *this, for chaining. The out-param lambda would copy it (`auto result`),
        # and copying a Persistent shares its raw buffers (abort at destruction). Dropped like the chained stream (R-OUT)
        # -- and so is `VrmlData_Scene& operator<<(Standard_IStream&)`, the scene's reader, whose *this would be copied the same way (R-STR)
        m.result, m.result_kind, m.result_class = "void", ResultKind.VALUE, ""
    if m.skip_reason is None:
        m.skip_reason = _unsupported(cursor.result_type, allow_out=False) if not returns_stream else None
        if m.skip_reason is None:
            m.skip_reason = _stl_iterator_in_6c(cursor.result_type)
        rc0 = cursor.result_type.get_canonical()
        if m.skip_reason == "reference to pointer" and rc0.get_pointee().get_canonical().get_pointee().get_canonical().kind == TK.RECORD:
            # R-PTR-REF: a reference to a class pointer (BOPAlgo_Builder* const& BRepAlgoAPI_BuilderAlgo::Builder(),
            # NCollection_ListNode*& NCollection_ListNode::Next()) -> bound as the pointer (a lambda copies it out;
            # rv_policy::reference_internal for a method, reference for a static one, a handle for a Transient)
            ptr_t = rc0.get_pointee()
            if _unsupported(ptr_t, allow_out=False) is None:
                m.skip_reason = None
                m.result = _type_spelling(ptr_t)
                m.result_kind, m.result_class = _result_kind(ptr_t)
                m.result_class_name = _class_behind(ptr_t)
                m.force_lambda = True
        if m.skip_reason == "reference to primitive" and rc0.kind == TK.LVALUEREFERENCE and not cursor.is_const_method():
            # double& Value(i, j) (math_Matrix), double& ChangeCoord(i) (gp_XYZ): Python cannot hold the reference,
            # so the emitter binds a getter plus a Set<Name>/__setitem__ counterpart (R-REF-PRIMITIVE)
            m.skip_reason = None
            m.result_kind, m.result = ResultKind.REF_PRIMITIVE, _type_spelling(rc0.get_pointee()).replace("const ", "")
        # R-ITERATOR: a result spelled as an STL-style iterator, the dependent spelling inside an instantiated template
        # (begin()/end())
        if m.skip_reason is None and re.match(r"(const )?(\w+)<", m.result) is not None \
                and re.match(r"(const )?(\w+)<", m.result).group(2) in _STL_ITERATORS:
            m.skip_reason = "return: STL-style iterator"
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
        m.skip_reason = "deleted"                  # R-DELETED: a deleted method is skipped and reported
    if m.skip_reason is None:
        sig = f"{cls_name}::{name}({', '.join(p.type for p in params)})"
        if f"{cls_name}::{name}" in _SKIP_METHODS or sig in _SKIP_METHODS:
            m.skip_reason = "overrides.toml [skip] methods"
    if m.skip_reason is None and 0 < _MAX_PARAMS < len(params):
        m.skip_reason = f"{len(params)} parameters, more than overrides.toml [skip] max_params ({_MAX_PARAMS})"
    return m


# Binding-Rules.md R-INCOMPLETE
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


# Binding-Rules.md R-CONV, R-CONV-SCALAR
def _conversion(cursor: cindex.Cursor) -> Conversion | None:
    """operator bool/int/double() -> __bool__/__int__/__float__; operator T()/operator handle<T>() for a class or
    enum T -> a constructor T(self) (plus an implicit conversion when not explicit)."""
    t = cursor.result_type
    if t.get_canonical().kind == TK.LVALUEREFERENCE:   # operator const handle<T>&() const: the referenced value
        t = t.get_canonical().get_pointee()
    canon = t.get_canonical()
    doc = _doc(cursor)
    explicit = cursor.is_explicit_method()
    is_const = cursor.is_const_method()
    if canon.kind == TK.BOOL:
        return Conversion(ConversionKind.BOOL, "bool", "", explicit, doc, is_const)
    if canon.kind in _INT_KINDS:
        return Conversion(ConversionKind.INT, _type_spelling(t), "", explicit, doc, is_const)
    if canon.kind in (TK.DOUBLE, TK.FLOAT, TK.LONGDOUBLE):
        return Conversion(ConversionKind.FLOAT, _type_spelling(t), "", explicit, doc, is_const)
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


# Binding-Rules.md R-NONCOPYABLE: the parser's own detection of a non-copyable class (field types, used in _class)
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


# Binding-Rules.md R-CTOR-KEEP
def _core_type(spelling: str) -> str:
    """'const NCollection_LinearVector<int> &' -> 'NCollection_LinearVector<int>': the type behind the outer const and
    pointer/reference declarators, spelled as _type_spelling spells it."""
    s = re.sub(r"(\s*(\*|&&|&)(\s*const)?)+\s*$", "", spelling.strip())
    return re.sub(r"^const\s+", "", s).strip()


def _record_key(t: cindex.Type) -> str:
    """The identity of a class type for R-CTOR-KEEP: canonical (typedefs resolved), without cv-qualifiers."""
    return re.sub(r"\b(const|volatile)\s+", "", _canonical_args(t)).strip()


def _pointee(t: cindex.Type) -> cindex.Type | None:
    """The canonical type behind every pointer/reference level of t, or None when t is neither (`BOPAlgo_PPaveFiller` is
    `BOPAlgo_PaveFiller *` -- a typedef'd pointer is a pointer)."""
    canon = t.get_canonical()
    if canon.kind not in (TK.POINTER, TK.LVALUEREFERENCE, TK.RVALUEREFERENCE):
        return None
    while canon.kind in (TK.POINTER, TK.LVALUEREFERENCE, TK.RVALUEREFERENCE):
        canon = canon.get_pointee().get_canonical()
    return canon


def _is_dependent(t: cindex.Type) -> bool:
    canon = t.get_canonical()
    return canon.kind in (TK.UNEXPOSED, TK.INVALID) or "type-parameter-" in canon.spelling


# owning smart pointers: what they point to is not borrowed from an argument
_OWNING_TEMPLATES = ("opencascade::handle<", "NCollection_Handle<", "std::shared_ptr<", "std::unique_ptr<", "std::weak_ptr<")


def _path(where: str) -> str:
    """A layout path for the report: a probe's or a result's walk starts with the class twice (`X -> X -> Base`)."""
    parts: list[str] = []
    for part in where.split(" -> "):
        if len(parts) == 0 or parts[-1] != part:
            parts.append(part)
    return " -> ".join(parts)


def _declares_move(t: cindex.Type) -> bool:
    """R-COPY: the class of t declares its own move or copy constructor, not defaulted -- returning it by value moves it with
    that one (BRepGraph_MutGuard). Unknown (a dependent type) is no."""
    decl = t.get_canonical().get_declaration()
    defn = decl.get_definition() if decl.kind != K.NO_DECL_FOUND else None
    return defn is not None and (_declares_copy(defn) or any(
        ch.kind == K.CONSTRUCTOR and ch.is_move_constructor() and not ch.is_default_method() and not ch.is_deleted_method()
        for ch in defn.get_children()))


def _declares_copy(defn: cindex.Cursor) -> bool:
    """R-COPY: the class declares its own copy constructor, not defaulted -- trusted to copy what it owns (NCollection's
    containers, TCollection_AsciiString, Message_ProgressRange)."""
    return any(ch.kind == K.CONSTRUCTOR and ch.is_copy_constructor() and not ch.is_default_method() and not ch.is_deleted_method()
               for ch in defn.get_children())


def _destructor_frees(dtor: cindex.Cursor) -> bool:
    """R-COPY: a user-provided destructor that may free (or use) what the object points to: any body that is not empty, and one
    the headers do not show (defined in a .cxx) -- `~T() = default` and `~T() {}` free nothing."""
    if dtor.is_default_method() or dtor.is_deleted_method():
        return False
    defn = dtor.get_definition()
    body = next((ch for ch in (dtor if defn is None else defn).get_children() if ch.kind == K.COMPOUND_STMT), None)
    return body is None or len(list(body.get_children())) > 0


class _Held:
    """What an object keeps pointers or references to, read from its layout (R-CTOR-KEEP): the class types behind every
    pointer or reference data member of any access -- its own, every base's, and those inside members it holds by value,
    recursively; a template instance's type arguments count as members (a container of pointers keeps what they point
    to), and for a container (BINDERS) or a std:: type only they do. `anything`: a `void *` member may hold any object
    (CPnts_UniformDeflection keeps its curve, TopOpeBRepDS_CurveExplorer its data structure as `void*`). `pending`: a base
    or by-value member spelled only after template substitution -- completed by a layout probe at the end of the package
    (_resolve_held_layout). `gaps`: what neither could follow (reported, never guessed). The `mutable_` sets are what a
    const method can store into (R-METHOD-KEEP): mutable members, and members inside a member that is mutable. The `copy_`
    sets are what an implicit copy of the object duplicates (R-COPY): `copy_pointers` the raw pointer and reference members
    of every kind (a `char *` and an `int *` too, not a function pointer), `copy_owners` the classes whose destructor may free
    such a pointer -- a destructor the headers do not show empty (_destructor_frees) in a class whose own part (members,
    bases, by-value members) holds one, or may (a part only a probe completes). Both cover the class and what an implicit
    copy copies member by member -- bases and by-value members, but nothing inside a class that declares its own copy
    constructor (trusted: it copies what it owns)."""

    def __init__(self) -> None:
        self.types: set[str] = set()
        self.anything = False
        self.mutable_types: set[str] = set()         # a subset of types
        self.mutable_anything = False
        self.pending: list[tuple[str, str, bool, bool]] = []     # (spelling, where, in a mutable member, inside a trusted copy)
        self.gaps: list[str] = []
        self.probed: set[str] = set()                # spellings a probe already completed: incomplete there means incomplete
        self.constants: set[str] = set()             # constants of the walked class (a non-type template argument: THE_BUFFER_SIZE)
        self.copy_pointers: set[str] = set()         # where an implicit copy duplicates a raw pointer or reference
        self.copy_owners: set[str] = set()           # where a destructor may free what such a pointer points to
        self._trusted = 0                            # > 0: walking inside a class with its own copy constructor
        self._frames: list[list[bool]] = []          # per class being walked: [its destructor may free, its part copies a pointer]
        self._copies_pointer: dict[str, bool] = {}   # per walked class: its part copies a pointer (a class seen again still counts)
        self._seen: set[tuple[str, bool, bool]] = set()

    def hold(self, key: str, mut: bool) -> None:
        self.types.add(key)
        if mut:
            self.mutable_types.add(key)

    def hold_anything(self, mut: bool) -> None:
        self.anything = True
        if mut:
            self.mutable_anything = True

    def copied(self, where: str) -> None:
        """An implicit copy duplicates a pointer here (not inside a trusted copy constructor)."""
        if self._trusted == 0:
            self.copy_pointers.add(where)
            self._part_copies_pointer()

    def _part_copies_pointer(self) -> None:
        for frame in self._frames:
            frame[1] = True

    def _enter(self, frees: bool) -> None:
        self._frames.append([frees and self._trusted == 0, False])

    def _leave(self, where: str) -> bool:
        """Close the class walked at `where`: an owner when its destructor may free and its part copies a pointer."""
        frees, copies = self._frames.pop()
        if frees and copies:
            self.copy_owners.add(where)
        return copies

    def add_pointee(self, p: cindex.Type, mut: bool) -> None:
        if p.kind == TK.RECORD:
            self.hold(_record_key(p), mut)
        elif p.kind == TK.VOID:
            self.hold_anything(mut)

    def spelled(self, spelled: str, where: str, mut: bool) -> None:
        """A type known only by its spelling (substituted): a pointer or reference to it is held, a class by value is probed."""
        if "type-parameter-" in spelled:
            self.gaps.append(f"{where}: {spelled}")
            return
        core = _core_type(spelled)
        if spelled.rstrip().endswith(("&", "*")) or core == "Standard_Address":
            self.copied(where)
        if spelled.rstrip().endswith(("&", "*")):
            if core in ("void", "Standard_Address"):
                self.hold_anything(mut)
            elif core not in _PRIMITIVE_SPELLINGS:
                self.hold(core, mut)
        elif core == "Standard_Address":
            self.hold_anything(mut)
        elif "<" in core and (core.startswith("std::") or core.split("<")[0] in BINDERS):
            # a container counts by its arguments only (record): read them from the spelling, no probe -- one may be a
            # class constant the probe could not name (math_VectorBase's private THE_BUFFER_SIZE in std::array<T, THE_BUFFER_SIZE>)
            for arg in _split_top(core[core.index("<") + 1 : core.rindex(">")]):
                if re.fullmatch(r"-?\d+[uUlL]*|true|false", arg) is None and arg not in self.constants:
                    self.spelled(arg, f"{where} -> {core}", mut)
        elif core not in _PRIMITIVE_SPELLINGS and not core.startswith(_OWNING_TEMPLATES):
            self.pending.append((core, where, mut, self._trusted > 0))
            if self._trusted == 0:
                self._part_copies_pointer()          # not known before the probe: may (R-COPY, the safe side)

    def member(self, ft: cindex.Type, where: str, mut: bool) -> None:
        p = _pointee(ft)
        if p is not None and not _is_dependent(p):
            if p.kind not in (TK.FUNCTIONPROTO, TK.FUNCTIONNOPROTO):
                self.copied(where)
            self.add_pointee(p, mut)
            return
        canon = ft.get_canonical()
        for t in (ft, canon):
            if t.kind in (TK.CONSTANTARRAY, TK.INCOMPLETEARRAY, TK.VARIABLEARRAY, TK.DEPENDENTSIZEDARRAY):
                self.member(t.element_type, where, mut)
                return
        if canon.kind == TK.RECORD and not _is_dependent(canon):
            self.record(canon, where, mut)
        elif _is_dependent(ft):
            decl = ft.get_declaration()
            if decl.kind in (K.TYPEDEF_DECL, K.TYPE_ALIAS_DECL) and not _is_dependent(decl.underlying_typedef_type):
                self.member(decl.underlying_typedef_type, where, mut)
            else:
                self.spelled(_type_spelling(ft), where, mut)    # inside a class template walked for an alias instantiation (6c)

    def record(self, t: cindex.Type, where: str, mut: bool) -> None:
        """A class held by value or as a base: t is its canonical type; mut: inside a mutable member."""
        key = _record_key(t)
        if key.startswith(_OWNING_TEMPLATES):
            return
        if (key, mut, self._trusted > 0) in self._seen:
            if self._trusted == 0 and self._copies_pointer.get(key, False):
                self._part_copies_pointer()
            return
        self._seen.add((key, mut, self._trusted > 0))
        for i in range(t.get_num_template_arguments()):
            at = t.get_template_argument_type(i)
            if at.kind != TK.INVALID:
                self.member(at, f"{where} -> {key}", mut)
        if key.startswith("std::") or key.split("<")[0] in BINDERS:
            # a container owns its storage (NCollection_Array1<gp_Circ2d>'s `gp_Circ2d* myData` points into its own buffer,
            # not at an argument), and the standard library's layout differs per implementation: the arguments only
            return
        decl = t.get_declaration()
        defn = decl.get_definition() if decl.kind != K.NO_DECL_FOUND else None
        if defn is None:
            if key in self.probed:
                self.gaps.append(f"{where}: {key} (incomplete)")
            else:
                self.pending.append((key, where, mut, self._trusted > 0))  # NCollection_CellFilter<...>::Cell: complete only once named in a probe
                if self._trusted == 0:
                    self._part_copies_pointer()
            return
        if len(list(defn.get_children())) > 0:
            trusted = _declares_copy(defn)
            self._trusted += trusted
            copies = self.cursor(defn, f"{where} -> {key}", mut)
            self._trusted -= trusted
        else:
            tmpl = cindex.conf.lib.clang_getSpecializedCursorTemplate(defn)
            tdef = None if tmpl is None or tmpl.kind == K.NO_DECL_FOUND else tmpl.get_definition()
            tdef = tmpl if tdef is None else tdef
            trusted = tdef is not None and tdef.kind != K.NO_DECL_FOUND and _declares_copy(tdef)
            self._trusted += trusted
            copies = self._instance(t, key, tdef, where, mut)
            self._trusted -= trusted
        if self._trusted == 0:
            self._copies_pointer[key] = copies

    def _instance(self, t: cindex.Type, key: str, tdef: "cindex.Cursor | None", where: str, mut: bool) -> bool:
        """An implicit instantiation's cursor has no children: its members come from the instantiated type, its bases (and its
        destructor) from the template's definition with the template's parameters replaced by this instantiation's arguments.
        Returns whether its part copies a pointer (R-COPY)."""
        known = tdef is not None and tdef.kind != K.NO_DECL_FOUND
        self._enter(known and any(ch.kind == K.DESTRUCTOR and _destructor_frees(ch) for ch in tdef.get_children()))
        self._instance_parts(t, key, tdef if known else None, where, mut)
        return self._leave(f"{where} -> {key}")

    def _instance_parts(self, t: cindex.Type, key: str, tdef: "cindex.Cursor | None", where: str, mut: bool) -> None:
        for f in t.get_fields():
            self.member(f.type, f"{where} -> {key}", mut or f.is_mutable_field())
        if tdef is None:
            return
        tparams = [ch for ch in tdef.get_children()
                   if ch.kind in (K.TEMPLATE_TYPE_PARAMETER, K.TEMPLATE_NON_TYPE_PARAMETER, K.TEMPLATE_TEMPLATE_PARAMETER)]
        names = [ch.spelling for ch in tparams]
        values = _split_top(key[key.index("<") + 1 : key.rindex(">")]) if "<" in key else []
        for tp in tparams[len(values):]:
            # the canonical spelling can leave defaulted arguments out (BVH_Traverse<double, 3, Set> for <..., MetricType = NumType>)
            default = _template_default(tp)
            if default is None:
                break
            for name, value in zip(names, values):
                default = re.sub(rf"(?<![:\w]){re.escape(name)}\b", value, default)
            values.append(default)
        for b in tdef.get_children():
            if b.kind != K.CXX_BASE_SPECIFIER:
                continue
            if not _is_dependent(b.type):
                self.base(b.type, f"{where} -> {key}", mut)
            elif len(names) == len(values):
                spelled = b.type.spelling
                for name, value in zip(names, values):
                    spelled = re.sub(rf"(?<![:\w]){re.escape(name)}\b", value, spelled)
                self.spelled(spelled, f"{where} -> {key}: base", mut)
            else:
                self.gaps.append(f"{where} -> {key}: base {b.type.spelling}")

    def base(self, bt: cindex.Type, where: str, mut: bool) -> None:
        if _is_dependent(bt):
            # the template's parameters only: Substitution.apply would also expand the injected class name, which here can be a
            # template template argument (BVH_Box<T, N> : BVH_BaseBox<T, N, BVH_Box>)
            spelled = bt.spelling
            for name, value in _SUBST.params.items():
                spelled = re.sub(rf"(?<![:\w]){re.escape(name)}\b", value, spelled)
            self.spelled(spelled, f"{where}: base", mut)
        elif bt.get_canonical().kind == TK.RECORD:
            self.record(bt.get_canonical(), where, mut)

    def cursor(self, cls: cindex.Cursor, where: str, mut: bool) -> bool:
        """A class definition walked through its cursor: a plain class, or the class template of a 6c walk. Returns whether its
        part copies a pointer (R-COPY)."""
        children = list(cls.get_children())
        self._enter(any(ch.kind == K.DESTRUCTOR and _destructor_frees(ch) for ch in children))
        for ch in children:
            if ch.kind == K.FIELD_DECL:
                self.member(ch.type, f"{where}::{ch.spelling}", mut or ch.is_mutable_field())
            elif ch.kind == K.CXX_BASE_SPECIFIER:
                self.base(ch.type, where, mut)
        return self._leave(where)

    def absorb(self, r: "_Held", mut: bool, trusted: bool = False) -> None:
        """r: the layout of a member or base held in this object (inside a mutable member when mut, inside a class with its
        own copy constructor when trusted)."""
        if not trusted:
            self.copy_pointers |= r.copy_pointers
            self.copy_owners |= r.copy_owners
        self.types |= r.types
        self.anything = self.anything or r.anything
        self.mutable_types |= r.types if mut else r.mutable_types
        self.mutable_anything = self.mutable_anything or (r.anything if mut else r.mutable_anything)

    def holds(self, key: str, ancestors: tuple[str, ...], const_method: bool) -> bool:
        """Can a constructor or method store an argument of this class (and these bases) here? A const method only into
        mutable members."""
        types, anything = (self.mutable_types, self.mutable_anything) if const_method else (self.types, self.anything)
        return anything or key in types or any(a in types for a in ancestors)

    def shares_pointees(self, other: "_Held", const_method: bool) -> bool:
        """Can this object hold a pointer it copied out of an argument of layout `other` -- TDF_ChildIterator(label) stores
        the label's TDF_LabelNode*? Both hold pointers to a common class, or one side holds a `void *` and the other any
        pointer. A const method only into mutable members."""
        types, anything = (self.mutable_types, self.mutable_anything) if const_method else (self.types, self.anything)
        if anything:
            return len(other.types) > 0 or other.anything
        if other.anything:
            return len(types) > 0
        return len(types & other.types) > 0

    def holds_pointers(self) -> bool:
        return len(self.types) > 0 or self.anything


# R-CTOR-KEEP / R-METHOD-KEEP / R-RESULT-KEEP state of the package being parsed (reset per package): the held state of each
# class, shared by its constructors and methods; the parameters still undecided because part of a layout waits for the probe;
# the layout of every class named in a signature; the results and in-place outputs to decide once the layouts are complete
_held_by_class: dict[tuple[str, int], _Held] = {}    # (class name, hash of the walked definition): a template is walked per instantiation
_held_open: list[tuple[Class, _Held, list[tuple[Param, str, tuple[str, ...], bool, "_Held | None"]]]] = []   # (class, held, (param, key, ancestors, const method, the argument's own layout))
_layout_of_type: dict[str, _Held] = {}               # canonical class spelling (or a substituted spelling) -> its layout
_views_open: list[tuple[str, "Method | Function", Param | None, str, _Held, list[tuple[int, str, tuple[str, ...], "_Held | None"]], "Class | None", str]] = []
#   (qualified name, method or function, the in-place parameter or None for the result, the class it is, its layout,
#    candidates: (parameter index, class, its bases, its layout), the method's class (None: static, free),
#    how a result is copied (R-COPY): "cref" a `const T&`, "value" a `T`, "moves" a `T` whose class declares its own move or
#    copy constructor; "" for an in-place parameter)
_class_layouts: list[tuple[Class, _Held]] = []      # Class.view: a copy of a class holding pointers keeps the original
_kept_view_open: list[tuple[Param, _Held, _Held]] = []   # R-COPY: constructor parameters whose layout may share pointees with the object
_fields_open: list[tuple[Class, Field, _Held | None]] = []   # R-FIELD: raw pointer members, decided once the pointee's layout is complete
_instance_layouts: dict[str, _Held] = {}             # R-COPY: each binder instantiation's layout -- its elements, which the binder copies
_instance_owners: dict[str, str] = {}                # R-COPY: the instantiations among them whose elements are owners -> where


# Binding-Rules.md R-OWNER: the OCAF types whose owner the bindings know -- mirrored by nanocct::owners (nanocct_common.h, defined in
# nanocct_ocaf.h); nanocct::keep_view checks this verdict against the C++ trait at compile time
_OWNED_ROOTS = ("TDF_Label", "TDF_Data")
_OWNED_BASE = "TDF_Attribute"
_LABEL_DOCUMENT = "TDocStd_Document"      # R-OWNER, by layout: a document hands out its data's labels (Main())
_OWNED_CONTAINERS = ("NCollection_Array1", "NCollection_HArray1", "NCollection_Sequence", "NCollection_HSequence", "NCollection_List",
                     "NCollection_Map", "NCollection_IndexedMap", "NCollection_DataMap", "NCollection_IndexedDataMap", "NCollection_DoubleMap")


def _owned(t: cindex.Type) -> bool:
    """R-OWNER: is t -- through references, pointers and handles -- a TDF_Label, a TDF_Data, a TDF_Attribute (or derived), or
    one of the NCollection containers nanocct::owners walks, holding such elements?"""
    canon = t.get_canonical()
    while canon.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE, TK.POINTER):
        canon = canon.get_pointee().get_canonical()
    if canon.kind != TK.RECORD or _is_dependent(canon):
        return False
    key = _record_key(canon)
    decl = canon.get_declaration()
    if key.startswith("opencascade::handle<") and canon.get_num_template_arguments() == 1:
        return _owned(canon.get_template_argument_type(0))
    if key in _OWNED_ROOTS:
        return True
    if decl.spelling in _OWNED_CONTAINERS and canon.get_num_template_arguments() > 0:
        args = [canon.get_template_argument_type(i) for i in range(canon.get_num_template_arguments())]
        return any(_owned(a) for a in args if a.kind != TK.INVALID)
    defn = decl.get_definition() if decl.kind != K.NO_DECL_FOUND else None
    return defn is not None and defn.kind in (K.CLASS_DECL, K.STRUCT_DECL) and _derives_from(defn, _OWNED_BASE)


def _label_source(t: cindex.Type) -> bool:
    """R-OWNER, by layout: is t a handle a TDF_Label can be taken from -- of an OCAF type whose owners are known (_owned: a
    TDF_Data, a TDF_Attribute, a container of them), or of a TDocStd_Document (its data's labels)?"""
    canon = t.get_canonical()
    while canon.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE, TK.POINTER):
        canon = canon.get_pointee().get_canonical()
    if canon.kind != TK.RECORD or not _record_key(canon).startswith("opencascade::handle<") \
            or canon.get_num_template_arguments() != 1:
        return False
    if _owned(canon):
        return True
    # _derives_from, not the definition: the header holding the label usually only forward-declares the document
    # (XCAFPrs_DocumentExplorer.hxx: `class TDocStd_Document;`)
    decl = canon.get_template_argument_type(0).get_canonical().get_declaration()
    return decl.kind != K.NO_DECL_FOUND and _derives_from(decl, _LABEL_DOCUMENT)


def _type_layout(t: cindex.Type, spelled: str = "") -> tuple[str, _Held] | None:
    """R-RESULT-KEEP: the class behind a type -- through references, pointers and handles -- and its layout (_Held), one per
    class and package; None for a scalar or an enum. A dependent type of a 6c walk is read from its substituted spelling
    (`spelled`), completed by the layout probe."""
    canon = t.get_canonical()
    while canon.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE, TK.POINTER):
        canon = canon.get_pointee().get_canonical()
    if _is_dependent(canon):
        core = _core_type(spelled)
        if spelled == "" or core in _PRIMITIVE_SPELLINGS or "type-parameter-" in core:
            return None
        if core not in _layout_of_type:
            # the probe names the class behind the spelling: a typedef can hide a reference or a pointer
            # (NCollection_Array1<T>::const_reference), which as a member spelling would count as a held pointer
            held = _Held()
            held.pending.append((f"std::remove_cv_t<std::remove_pointer_t<std::remove_reference_t<{core}>>>", core, False, False))
            _layout_of_type[core] = held
        return core, _layout_of_type[core]
    if canon.kind == TK.RECORD and _record_key(canon).startswith("opencascade::handle<") and canon.get_num_template_arguments() == 1:
        canon = canon.get_template_argument_type(0).get_canonical()
    if canon.kind != TK.RECORD:
        return None
    key = _record_key(canon)
    if key not in _layout_of_type:
        held = _Held()
        held.record(canon, key, False)
        _layout_of_type[key] = held
    return key, _layout_of_type[key]


# Binding-Rules.md R-RESULT-KEEP, R-OWNER
def _note_views(fn: cindex.Cursor, m: "Method | Function", owner: str, cls: Class | None) -> None:
    """A result, or an argument the call writes into, of a class whose layout holds pointers (a TDF_Label, an LDOMString, a
    Message_Messenger::StreamBuffer) may point into the object that produced it: the result keeps that object -- self for
    a method, and every argument whose class, or a pointer in whose layout, the result can hold. An OCAF type keeps its
    owners instead (R-OWNER), which is all it needs. Decided at the end of the package (_decide_views), once the layout probe
    has completed every layout. owner: the class, "" for a free function (for the report); cls: a method's class, None for a
    static method or a free function."""
    args = list(fn.get_arguments())
    name = f"{owner}::{m.name}" if owner != "" else m.name
    if m.result != "void":
        m.result_owned = _owned(fn.result_type)
    for p, a in zip(m.params, args):
        if p.is_out and p.is_handle:
            p.owned = _owned(a.type)
    cands: list[tuple[int, str, tuple[str, ...], _Held | None]] = []
    for i, (p, a) in enumerate(zip(m.params, args)):
        if p.omitted or p.bytes_of != "" or p.is_bytes or (p.is_out and not p.is_inout) or p.stream != StreamKind.NONE:
            continue
        lay = _type_layout(a.type, p.type)
        if lay is not None:
            cands.append((i, lay[0], p.class_ancestors, lay[1]))
    if m.result != "void" and m.result_kind == ResultKind.VALUE and not m.result_owned:
        rt = fn.result_type.get_canonical()
        if rt.kind == TK.LVALUEREFERENCE and rt.get_pointee().is_const_qualified():
            rt = rt.get_pointee().get_canonical()
        # a class, not a handle -- a Transient's Python object may already exist and would collect the keep-alives of every
        # call -- and not a std:: type (a type caster's copy: no Python object of the class to keep anything)
        spelled = _core_type(m.result)
        if (rt.kind == TK.RECORD and not _record_key(rt).startswith(("std::",) + _OWNING_TEMPLATES)
                or _is_dependent(rt) and not spelled.startswith(("std::", "occ::handle<") + _OWNING_TEMPLATES)):
            lay = _type_layout(rt, m.result)
            if lay is not None:
                how = "cref" if fn.result_type.get_canonical().kind == TK.LVALUEREFERENCE else "moves" if _declares_move(rt) else "value"
                _views_open.append((name, m, None, lay[0], lay[1], cands, cls, how))
    for p, a in zip(m.params, args):
        if p.is_out or p.is_handle or p.omitted or p.stream != StreamKind.NONE or p.array_len > 0 or p.cstr_none or p.is_bytes:
            continue
        canon = a.type.get_canonical()
        if canon.kind not in (TK.LVALUEREFERENCE, TK.POINTER):
            continue
        pointee = canon.get_pointee()
        if pointee.is_const_qualified() or _is_dependent(pointee) or pointee.get_canonical().kind != TK.RECORD:
            continue
        if _owned(a.type):
            p.owned = True
            continue
        if _record_key(pointee.get_canonical()).startswith(("std::",) + _OWNING_TEMPLATES):
            continue
        lay = _type_layout(a.type)
        if lay is not None:
            _views_open.append((name, m, p, lay[0], lay[1], cands, cls, ""))


def _decide_views(report: list[str]) -> None:
    """R-RESULT-KEEP, end of package: the results and in-place outputs whose layout holds pointers keep their producers."""
    kept_by: dict[int, set[str]] = {}            # per class: the classes of the arguments its constructors and methods keep
    for name, m, param, cls, held, cands, owner, how in _views_open:
        if param is None and len(held.copy_owners) > 0 and how != "moves":
            # R-COPY: the copy (a `const T&`) or the move falling back to a copy (a `T` without its own move or copy
            # constructor) would share the pointers a destructor frees: the original by reference, the value built in place
            if how == "cref":
                m.result_by_reference = True
            else:
                m.result_on_heap = True
        if not held.holds_pointers():
            continue
        keeps = tuple(i for i, key, ancestors, lay in cands
                      if held.holds(key, ancestors, False) or (lay is not None and held.shares_pointees(lay, False)))
        if param is None:
            m.result_view, m.result_keeps = True, keeps
            continue
        if owner is not None and id(owner) not in kept_by:
            kept_by[id(owner)] = {q.class_name for k in owner.ctors + owner.methods for q in k.params if q.kept}
        if owner is not None and len(({param.class_name} | set(param.class_ancestors)) & kept_by[id(owner)]) > 0:
            # the object keeps arguments of this class (R-CTOR-KEEP, R-METHOD-KEEP), maybe this one: the argument keeping the
            # object back would be a cycle nanobind's keep-alive records hide from the garbage collector -- both would live for ever
            report.append(f"{name}: in-place argument {param.name} ({cls}) is of a class the object keeps, so it does not keep "
                          f"the object back (a keep-alive cycle) (R-RESULT-KEEP)")
        else:
            param.out_view = True
            param.out_keeps = tuple(i for i in keeps if m.params[i] is not param)


def _held_types(cls: cindex.Cursor, c: Class) -> _Held:
    """The types a class keeps a pointer or reference to (R-CTOR-KEEP), from its whole layout: BRepGraph's reverse
    iterators keep `const ContainerType* myRefs`, GeomBndLib_Surface `const Adaptor3d_Surface* myAdaptorRef`,
    BRepAlgoAPI_Cut its base's `BOPAlgo_PPaveFiller myDSFiller` (a typedef'd pointer), Extrema_ExtPC `TheCurve* myC`."""
    key = (c.name, cls.hash)
    if key not in _held_by_class:
        held = _Held()
        held.constants = {ch.spelling for ch in cls.get_children() if ch.kind in (K.VAR_DECL, K.ENUM_CONSTANT_DECL)} | {
            v.spelling for e in cls.get_children() if e.kind == K.ENUM_DECL for v in e.get_children()}
        held.cursor(cls, c.name, False)
        _held_by_class[key] = held
    return _held_by_class[key]


def _copyable_probe(index: cindex.Index, umbrella: Path, args: list[str], td: str, pointers: list[str]) -> dict[str, bool | None]:
    """R-FIELD: can the class a pointer type points to be copied? Whether a copy constructor is implicitly deleted (a
    `std::atomic` member: NCollection_IncAllocator::IBlock) only the compiler knows, so a probe asks it -- an alias that
    is `int` when std::is_copy_constructible holds and `char` when not, read back as a type. None: did not compile."""
    if len(pointers) == 0:
        return {}
    probe = Path(td) / "nanocct__copyable.hxx"
    have = umbrella.read_text()
    headers = sorted({f"{name}.hxx" for s in pointers for name in re.findall(r"\w+", s)
                      if f"<{name}.hxx>" not in have and (_INCLUDE_DIR / f"{name}.hxx").exists()})
    probe.write_text(have + "#include <type_traits>\n" + "".join(f"#include <{h}>\n" for h in headers) + "".join(
        f"using nanocct_copyable_{i} = std::conditional_t<std::is_copy_constructible_v<std::remove_cv_t<std::remove_pointer_t<{s}>>>, "
        f"int, char>;\n" for i, s in enumerate(pointers)))
    tu = index.parse(str(probe), args=args + ["-ferror-limit=0"])
    aliases = {cur.spelling: cur for cur in tu.cursor.get_children()
               if cur.kind == K.TYPE_ALIAS_DECL and cur.spelling.startswith("nanocct_copyable_")}
    out: dict[str, bool | None] = {}
    for i, s in enumerate(pointers):
        cur = aliases.get(f"nanocct_copyable_{i}")
        kind = None if cur is None else cur.underlying_typedef_type.get_canonical().kind
        out[s] = True if kind == TK.INT else False if kind in (TK.CHAR_S, TK.CHAR_U) else None
    return out


def _resolve_held_layout(index: cindex.Index, umbrella: Path, args: list[str], td: str) -> None:
    """R-CTOR-KEEP, end of package: what the layout walk could only spell (a by-value member or base of a class template
    after substitution: Extrema_GGExtPC's `TheEPC myExtPC`, BVH_Box's base BVH_BaseBox<double, 3, BVH_Box>) gets a probe
    alias completed by sizeof, whose layout the same walk reads -- a few rounds, since a probed layout can pend in turn. A
    class the package's headers only declare (`class gp_Pnt;` before a method returning one) is completed by including its
    header in the probe. Then the open constructor and method parameters are decided; what stays unresolved is reported for
    the classes it leaves undecided."""
    resolved: dict[str, _Held | None] = {}
    open_layouts: list[_Held] = list({id(h): h for h in list(_held_by_class.values()) + list(_layout_of_type.values())
                                      + [h for _, h in _class_layouts]
                                      + [lay for _, _, cands in _held_open for *_, lay in cands if lay is not None]}.values())

    def absorb() -> None:
        """Fold every resolved spelling into the classes that pend on it; a probed layout's own pending entries follow."""
        for held in open_layouts:
            for _ in range(len(resolved) + 1):          # a resolved layout can pend on spellings resolved earlier
                still: list[tuple[str, str, bool, bool]] = []
                changed = False
                for s, where, mut, trusted in held.pending:
                    if s not in resolved:
                        still.append((s, where, mut, trusted))
                        continue
                    changed = True
                    r = resolved[s]
                    if r is None:
                        held.gaps.append(f"{where}: {s} (the layout probe did not compile)")
                    else:
                        held.absorb(r, mut, trusted)
                        held.gaps += [f"{where} -> {g}" for g in r.gaps]
                        still += [(s2, f"{where} -> {w2}", mut or m2, trusted or t2) for s2, w2, m2, t2 in r.pending]
                held.pending = still
                if not changed:
                    break

    for _ in range(10):                            # a probed layout can pend in turn (BVH_Distance -> BVH_Traverse -> ... -> BVH_Object)
        absorb()
        todo = sorted({s for h in open_layouts for s, *_ in h.pending if s not in resolved})
        if len(todo) == 0:
            break
        probe = Path(td) / "nanocct__layout.hxx"
        # the header named like every class in a spelling (a template's arguments too: NCollection_CellFilter<X>::Cell needs X
        # complete), when the umbrella does not include it already
        have = umbrella.read_text()
        headers = sorted({f"{name}.hxx" for s in todo for name in re.findall(r"\w+", s)
                          if f"<{name}.hxx>" not in have and (_INCLUDE_DIR / f"{name}.hxx").exists()})
        probe.write_text(have + "#include <type_traits>\n" + "".join(f"#include <{h}>\n" for h in headers) + "".join(
            f"using nanocct_layout_{i} = {s};\nstatic_assert(sizeof(nanocct_layout_{i}) != 0, \"\");\n" for i, s in enumerate(todo)))
        tu = index.parse(str(probe), args=args + ["-ferror-limit=0"])   # a private member type's access error each: no limit
        aliases = {cur.spelling: cur for cur in tu.cursor.get_children()
                   if cur.kind == K.TYPE_ALIAS_DECL and cur.spelling.startswith("nanocct_layout_")}
        for i, s in enumerate(todo):
            cur = aliases.get(f"nanocct_layout_{i}")
            t = None if cur is None else cur.underlying_typedef_type.get_canonical()
            if t is None or t.kind == TK.INVALID:
                resolved[s] = None                 # did not compile (a private member type does: libclang builds it anyway)
                continue
            h = _Held()
            h.probed.add(s)
            if t.kind == TK.RECORD:
                h.record(t, s, False)
            else:
                h.member(t, s, False)              # a builtin or enum holds nothing; a pointer typedef holds its pointee
            resolved[s] = h
    absorb()
    for c, held, cands in _held_open:
        missed = []
        for p, key, ancestors, const_method, lay in cands:
            if held.holds(key, ancestors, const_method) or (lay is not None and held.shares_pointees(lay, const_method)):
                p.kept = True
            else:
                missed.append(p.name)
        open_layout = held.gaps + [f"{w}: {s} (not resolved within the probe rounds)" for s, w, *_ in held.pending]
        if len(missed) > 0 and len(open_layout) > 0:
            c.skipped.append(f"{c.name}: R-CTOR-KEEP could not follow its whole layout ({'; '.join(sorted(set(open_layout)))}): "
                             f"no keep-alive for {', '.join(sorted(set(missed)))}")
    for c, held in _class_layouts:
        c.view = held.holds_pointers()
        # R-COPY: a class with its own copy constructor is trusted (bound as declared; only the implicit copy is decided here)
        c.copy_owner = "" if any(k.is_copy for k in c.ctors) else _path(min(held.copy_owners, default=""))
    for p, held, own in _kept_view_open:
        p.kept_view = p.kept and held.shares_pointees(own, False)
    for key, lay in sorted(_instance_layouts.items()):
        if len(lay.copy_owners) > 0:
            # R-COPY: a binder copies its elements (Value(), Append, the container's copy; NCollection_Shared<T> a T) -- the
            # emitter skips such an instantiation, or binds NCollection_Shared<T> without its constructor from T
            _instance_owners[key] = _path(min(lay.copy_owners))
    copyable = _copyable_probe(index, umbrella, args, td, sorted({f.type for _, f, _ in _fields_open}))
    for c, f, lay in _fields_open:
        if lay is not None and len(lay.copy_owners) > 0:
            # R-FIELD, R-COPY: a copy of the pointee would share what its destructor frees
            c.skipped.append(f"{c.name}::{f.name}: field is a raw pointer to {_core_type(f.type)}, whose copy would share the "
                             f"pointers its destructor frees (R-COPY) -> not bound")
            c.fields.remove(f)
        elif copyable.get(f.type) is not True:
            why = "cannot be copied" if copyable.get(f.type) is False else "the copy probe could not name"
            c.skipped.append(f"{c.name}::{f.name}: field is a raw pointer to {_core_type(f.type)}, which {why} (R-FIELD) -> not bound")
            c.fields.remove(f)
        else:
            f.is_pointer = True



# Binding-Rules.md R-KEPT: per package, the kept parameters of Transient classes waiting for the cycle check (end of package),
# and what each class reached by the check can own
_cycle_open: list[tuple[Class, cindex.Cursor, str, Param, cindex.Type]] = []   # (class, declaring class, function, param, its type)
_strong_edges_of: dict[str, list[tuple[cindex.Type, str, bool]]] = {}         # class -> (owned class, how, it is a handle's target)
_MI_COLLECTIONS = ("NCollection_HArray1<", "NCollection_HArray2<", "NCollection_HSequence<", "NCollection_Shared<")


def _owned_class(ft: cindex.Type, how: str, edges: list[tuple[cindex.Type, str, bool]]) -> None:
    """The class behind a member or template argument type -- by value, through arrays, pointers and references."""
    canon = ft.get_canonical()
    while canon.kind in (TK.CONSTANTARRAY, TK.INCOMPLETEARRAY, TK.VARIABLEARRAY, TK.POINTER, TK.LVALUEREFERENCE, TK.RVALUEREFERENCE):
        canon = (canon.element_type if canon.kind in (TK.CONSTANTARRAY, TK.INCOMPLETEARRAY, TK.VARIABLEARRAY)
                 else canon.get_pointee()).get_canonical()
    if canon.kind == TK.RECORD and not _is_dependent(canon):
        edges.append((canon, how, False))


def _strong_edges(t: cindex.Type) -> list[tuple[cindex.Type, str, bool]]:
    """R-KEPT: the classes an object of class t can own, one step: its bases, its members (by value, and behind typed
    pointers -- TDF_Data owns its label nodes through one; a back-pointer only adds a path), the arguments of a class
    template (a container's elements), and the target of a handle (marked) or of another owning smart pointer. Not
    followed: `void *`, a function pointer, a class the headers only declare, a dependent type (Binding-Rules.md R-KEPT)."""
    key = _record_key(t)
    if key in _strong_edges_of:
        return _strong_edges_of[key]
    edges: list[tuple[cindex.Type, str, bool]] = []
    _strong_edges_of[key] = edges                  # a class reached again through itself adds nothing new
    n = t.get_num_template_arguments()
    if key.startswith(_OWNING_TEMPLATES):
        if not key.startswith("std::weak_ptr<") and n >= 1 and t.get_template_argument_type(0).kind != TK.INVALID:
            edges.append((t.get_template_argument_type(0).get_canonical(), "", key.startswith("opencascade::handle<")))
        return edges
    for i in range(n):
        if t.get_template_argument_type(i).kind != TK.INVALID:
            _owned_class(t.get_template_argument_type(i), "", edges)
    if key.startswith("std::") or key.split("<")[0] in BINDERS:
        return edges                               # a container or std:: type: its arguments (its storage is its own)
    decl = t.get_declaration()
    defn = decl.get_definition() if decl.kind != K.NO_DECL_FOUND else None
    if defn is None:
        return edges
    children = list(defn.get_children())
    if len(children) == 0:                         # an implicit instantiation: members from the type, bases from the template
        for f in t.get_fields():
            _owned_class(f.type, f"::{f.spelling}", edges)
        tmpl = cindex.conf.lib.clang_getSpecializedCursorTemplate(defn)
        tdef = None if tmpl is None or tmpl.kind == K.NO_DECL_FOUND else tmpl.get_definition()
        children = [] if tdef is None else [b for b in tdef.get_children() if b.kind == K.CXX_BASE_SPECIFIER]
    for ch in children:
        if ch.kind == K.FIELD_DECL:
            _owned_class(ch.type, f"::{ch.spelling}", edges)
        elif ch.kind == K.CXX_BASE_SPECIFIER and not _is_dependent(ch.type) and ch.type.get_canonical().kind == TK.RECORD:
            edges.append((ch.type.get_canonical(), " (base)", False))
    return edges


def _cycle_path(t: cindex.Type, owner: cindex.Cursor) -> str | None:
    """R-KEPT: can an argument of type t own an object of class `owner` -- reach, through what it owns (_strong_edges), a
    handle whose target class is related to owner (a base of it, or derived from it)? Then an argument the C++ object keeps
    would be a reference cycle no garbage collector sees: the path, else None. A dependent type is answered with a path
    too (nothing is known about it: it stays kept by the Python object, as before)."""
    start = _pointee(t)
    start = t.get_canonical() if start is None else start
    if _is_dependent(start) or _is_dependent(owner.type):
        return f"{_type_spelling(t)} (a dependent type, not followed)"
    if start.kind != TK.RECORD:
        return None
    owner_key = _record_key(owner.type)
    related = {owner_key, *_class_ancestors(owner.type)}
    first = _record_key(start)
    todo, seen = [(start, first)], {first}
    while len(todo) > 0:
        cur, path = todo.pop(0)
        for child, how, target in _strong_edges(cur):
            ck = _record_key(child)
            step = f"{path}{how} -> {ck}"
            if target and (ck in related or owner_key in _class_ancestors(child)):
                return step
            if ck not in seen:
                seen.add(ck)
                todo.append((child, step))
    return None


def _decide_cycles() -> None:
    """R-KEPT, end of package: a kept parameter of a Transient class follows the C++ object (kept_cpp) unless its argument
    can own the object (_cycle_path) -- reported, it stays kept by the Python object."""
    for c, owner, fn, p, t in _cycle_open:
        if not p.kept:
            continue
        path = _cycle_path(t, owner)
        p.kept_cpp = path is None
        if path is not None:
            c.skipped.append(f"{c.name}::{fn}: argument {p.name} can own the object ({path}), a cycle no garbage collector sees "
                             f"-> kept by the Python object, not by nanocct::Kept<T> (R-KEPT)")


def _kept_facts(cursor: cindex.Cursor, c: Class) -> tuple[str, list[str]]:
    """R-KEPT: why nanocct::Kept<T> cannot derive from the class ("" if it can), and the linker symbols its own vtable
    needs: the final overrider of every virtual function of the class and its bases that the headers do not define (a
    plain `new T` uses T's vtable from the library instead; on Windows only Standard_EXPORT members are exported). Class
    templates define their members in the headers; their non-template bases are still walked."""
    children = list(cursor.get_children())
    if any(ch.kind == K.CXX_FINAL_ATTR for ch in children):
        return "the class is final", []
    if any(ch.kind == K.DESTRUCTOR and ch.access_specifier == Access.PRIVATE for ch in children):
        return "its destructor is private", []
    if any(a.startswith(_MI_COLLECTIONS) for a in (c.name, *_class_ancestors(cursor.type))):
        return "a multiple-inheritance H-collection (its Transient base is not at offset 0)", []
    finals: dict[tuple[str, tuple[str, ...], bool], cindex.Cursor | None] = {}
    seen: set[str] = set()

    def visit(cls: cindex.Cursor, template: bool) -> None:
        kids = list(cls.get_children())
        if len(kids) == 0 and cls.kind != K.NO_DECL_FOUND:          # an implicit instantiation: the template's definition
            tmpl = cindex.conf.lib.clang_getSpecializedCursorTemplate(cls)
            tdef = None if tmpl is None or tmpl.kind == K.NO_DECL_FOUND else tmpl.get_definition()
            if tdef is not None:
                visit(tdef, True)
            return
        for ch in kids:
            if ch.kind == K.CXX_METHOD and ch.is_virtual_method():
                sig = (ch.spelling, tuple(_canonical_args(a.type) for a in ch.get_arguments()), ch.is_const_method())
                finals.setdefault(sig, None if template else ch)   # a template's member is defined in the header
        for ch in kids:
            if ch.kind == K.CXX_BASE_SPECIFIER and not _is_dependent(ch.type):
                d = ch.type.get_canonical().get_declaration()
                dd = None if d.kind == K.NO_DECL_FOUND else d.get_definition()
                if dd is not None and (dd.get_usr() or dd.spelling) not in seen:
                    seen.add(dd.get_usr() or dd.spelling)
                    visit(dd, template)

    visit(cursor, "<" in c.name or _SUBST.active)
    delete = finals.get(("Delete", (), True))
    if delete is not None and any(ch.kind == K.CXX_FINAL_ATTR for ch in delete.get_children()):
        return "Delete() is final", []
    symbols = sorted({m.mangled_name for m in finals.values() if m is not None and not m.is_pure_virtual_method()
                      and not (m.is_definition() or m.get_definition() is not None or m.is_default_method())})
    return "", symbols


def _decide_kept(fn: cindex.Cursor, c: Class, params: list[Param], is_method: bool, const_method: bool) -> None:
    """R-CTOR-KEEP / R-METHOD-KEEP: mark the parameters of a constructor or method that the object can keep the address of --
    taken by reference or pointer (not a handle, a primitive, a stream, bytes or a returned out-parameter), of a class that
    the object, by its layout (_Held), holds a pointer or reference to -- or, for a constructor, whose own layout holds a
    pointer the object can hold too, copied out of the argument (TDF_ChildIterator(label) keeps the label's TDF_LabelNode*). What waits for the
    layout probe is decided at the end of the package (_resolve_held_layout). A method's out-parameters are returned, not
    passed; an in-out parameter is copied into the binding's lambda, so an address the object keeps would dangle whatever
    the binding does -- reported."""
    held = _held_types(fn.semantic_parent, c)
    undecided: list[tuple[Param, str, tuple[str, ...], bool, _Held | None]] = []
    ocaf_class = _owned(fn.semantic_parent.type)
    for p, arg in zip(params, fn.get_arguments()):
        if p.omitted or p.is_bytes or p.stream != StreamKind.NONE or (is_method and p.is_out and not p.is_inout):
            continue
        if p.is_handle:
            # R-OWNER, by layout: an object whose layout holds a TDF_Label (XCAFPrs_DocumentExplorer's node stack) points into
            # the document a handle argument gave it -- a document, its data or an attribute -- and nothing else keeps that
            # document: the object keeps the argument. Decided at the end of the package, once the layout probe completed
            # every layout (the key is the label's TDF_LabelNode*). An OCAF object itself knows its owners already (R-OWNER).
            if not ocaf_class and not p.is_out and _label_source(arg.type):
                if c.is_transient:
                    _cycle_open.append((c, fn.semantic_parent, fn.spelling, p, arg.type))   # R-KEPT, decided once p.kept is
                undecided.append((p, "TDF_LabelNode", (), const_method, None))
            continue
        pointee = _pointee(arg.type)
        if pointee is None:
            continue
        if _is_dependent(pointee):        # a 6c walk: the parameter is spelled only after substitution
            if not p.type.rstrip().endswith(("&", "*")):
                continue
            key, is_class = _core_type(p.type), _core_type(p.type) not in _PRIMITIVE_SPELLINGS
        else:
            key, is_class = _record_key(pointee), pointee.kind == TK.RECORD
        if not is_class or key.startswith(_OWNING_TEMPLATES):
            continue
        if c.is_transient:
            _cycle_open.append((c, fn.semantic_parent, fn.spelling, p, arg.type))   # R-KEPT, decided once p.kept is
        lay = _type_layout(arg.type, p.type)
        # a pointer copied out of the argument (shares_pointees): constructors only. A new object has no pointers of its own
        # yet, so one it copies points where the argument's does; a method's object already points into what produced it,
        # and the test then mostly matched BRepGraph's editor and the RAII MutGuard it is handed (both hold BRepGraph*): the
        # editor kept the guard in a slot while the guard kept the editor (R-RESULT-KEEP), a keep-alive cycle -- 16 instances
        # leaked, the guard's markModified() never ran
        own = None if lay is None or is_method else lay[1]
        if is_method and p.is_inout:
            if held.holds(key, p.class_ancestors, const_method) or (own is not None and held.shares_pointees(own, const_method)):
                c.skipped.append(f"{c.name}::{fn.spelling}: in-out argument {p.name} is copied into the binding, an address "
                                 f"the object keeps would dangle (R-METHOD-KEEP)")
            continue
        if own is not None:
            _kept_view_open.append((p, held, own))         # R-COPY: kept_view, decided once the layouts are complete
        if held.holds(key, p.class_ancestors, const_method) or (own is not None and held.shares_pointees(own, const_method)):
            p.kept = True
        else:
            undecided.append((p, key, p.class_ancestors, const_method, own))
    if len(undecided) > 0:
        entry = next((e for e in _held_open if e[0] is c and e[1] is held), None)
        if entry is None:
            _held_open.append((c, held, undecided))
        else:
            entry[2].extend(undecided)


def _ctor(ch: cindex.Cursor, c: Class, members: set[str]) -> Constructor:
    # the qualified name lets overrides.toml [bytes] name a constructor (R-BYTES: WNT_HIDSpaceMouse::WNT_HIDSpaceMouse);
    # streams stay out of constructors whatever the name says (allow_streams=False; R-STREAM-OUT, R-STREAM-IN: an object
    # may keep the stream reference beyond the call)
    params, reason = _params(ch, f"{c.name}::{ch.spelling}", c.name, members, allow_streams=False)
    required = [q for q in params if q.default is None]
    # R-IMPLICIT-CONV: a non-explicit constructor callable with one argument converts implicitly (nb::implicitly_convertible
    # in the emitter); copy and move constructors do not
    implicit = (len(params) >= 1 and len(required) <= 1 and not ch.is_explicit_method()
                and not ch.is_copy_constructor() and not ch.is_move_constructor())
    # defined_in_header feeds the nm checks in __main__ (R-UNDEFINED, R-UNDEFINED-COPY): `= default` counts as defined
    ctor = Constructor(params=params, doc=_doc_with_deprecation(ch), skip_reason=reason, is_implicit=implicit, is_copy=ch.is_copy_constructor(),
                       defined_in_header=ch.is_definition() or ch.get_definition() is not None or ch.is_default_method() or _SUBST.active,
                       mangled=ch.mangled_name)
    if not ch.is_move_constructor() and reason is None:
        _decide_kept(ch, c, params, False, False)       # a copy constructor too: the copy shares the original's pointers
    if ctor.skip_reason is None and 0 < _MAX_PARAMS < len(params):
        ctor.skip_reason = f"{len(params)} parameters, more than overrides.toml [skip] max_params ({_MAX_PARAMS})"
    if ctor.skip_reason is not None:
        c.skipped.append(f"{c.name}::{c.name}({', '.join(p.type for p in params)}): {ctor.skip_reason}")
    return ctor


# Binding-Rules.md R-USING
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
            # `using Base::Base;`: Derived(args) is valid for every base constructor except copy/move (BRepGraph_FacesOfEdge);
            # the base's deleted constructors are not bound either (R-DELETED)
            if d.is_copy_constructor() or d.is_move_constructor() or d.is_deleted_method() or d.access_specifier == Access.PRIVATE:
                continue
            ctor = _ctor(d, c, _members(d.semantic_parent))
            ctor.defined_in_header = True          # the base's symbol; the base's own binding runs the nm check
            c.ctors.append(ctor)                   # has_declared_ctor stays: inherited constructors do not suppress the implicit default one
            continue
        if d.kind != K.CXX_METHOD or d.access_specifier == Access.PRIVATE:
            # R-USING re-exports the *methods* behind a using-declaration. A re-exported data member is a different
            # thing and stays out: OpenGl_ArbDbg & co. re-export the GL entry points of the protected OpenGl_GlFunctions
            # base, which are C function pointers (755 of them in TKOpenGl, 2026-09-22).
            what = "data member" if d.kind == K.FIELD_DECL else d.kind.name.lower()
            c.skipped.append(f"{c.name}: using {using.spelling}: {what} of a base, not a method (not bound)")
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
        elif not m.is_static:
            _decide_kept(d, c, m.params, True, m.is_const)       # R-METHOD-KEEP: the base's layout, inside this object
        if m.skip_reason is None:
            _note_views(d, m, c.name, None if m.is_static else c)       # R-RESULT-KEEP
        c.methods.append(m)


def _base_provides_operator_new(base_type, _depth: int = 0) -> bool:
    """True when this base class declares a member operator new, or inherits one from its own bases.

    Inheriting it through a non-public base makes the allocation function inaccessible in the derived class, so
    `new Derived(...)` does not compile (Standard_DefineAlloc.hxx's DEFINE_STANDARD_ALLOC is the source in OCCT)."""
    decl = base_type.get_canonical().get_declaration()
    if decl is None or decl.kind == K.NO_DECL_FOUND or _depth > 8:
        return False
    for ch in decl.get_children():
        if ch.kind == K.CXX_METHOD and ch.spelling == "operator new":
            return True
        if ch.kind == K.CXX_BASE_SPECIFIER and _base_provides_operator_new(ch.type, _depth + 1):
            return True
    return False


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
    if cpp_name in _SKIP_CONSTRUCTORS:
        c.constructible = False
        c.not_constructible_reason = "overrides.toml [skip] constructors"
    members = _members(cursor)     # names usable unqualified inside the class (for default arguments)
    # R-UNDEFINED for the destructor: nanobind instantiates wrap_destruct<T> for every bound class, so a ~T() that the
    # header only declares must be in the library. On Unix it always is (default visibility); on Windows only when the
    # class or the destructor carries Standard_EXPORT -- Storage_Bucket and Storage_BucketOfPersistent carry neither and
    # were the two LNK2019 in the first Windows link of _TKernel (2026-09-23).
    for ch in cursor.get_children():
        # `~X() override = default;` is a definition but libclang reports neither is_definition() nor get_definition()
        # for it (Message_PrinterToReport, Standard_Condition), so is_default_method() has to be asked separately
        if ch.kind == K.DESTRUCTOR and not (ch.is_definition() or ch.get_definition() is not None
                                            or ch.is_default_method() or ch.is_deleted_method()):
            c.dtor_mangled = ch.mangled_name
            break
    if c.is_transient:
        c.kept_blocker, c.virtual_symbols = _kept_facts(cursor, c)     # R-KEPT
    # R-INCOMPLETE: a data member (any access) of a type that is only declared in the headers (BRepGraph_CacheMesh::Slot,
    # defined in the .cxx) makes the destructor uninstantiable -> nb::class_ cannot be formed, the class is skipped
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
                # R-MI: a non-public base is dropped and reported; it costs the constructors only when it provides
                # operator new.
                # The base's members are not inherited publicly, so they are not bound. Construction is only lost when
                # the base *provides* operator new (DEFINE_STANDARD_ALLOC): the inherited allocation function is then
                # inaccessible and `new Derived(...)` is ill-formed even in C++ (Message_LazyProgressScope, verified
                # with a compile test 2026-09-23). A base without one (RWObj_IShapeReceiver, OpenGl_GlFunctions) leaves
                # the class constructible.
                if _base_provides_operator_new(ch.type):
                    c.skipped.append(f"{c.name}: non-public base {_type_spelling(ch.type)} provides operator new "
                                     f"-> inaccessible, class not constructible")
                    c.constructible = False
                else:
                    c.skipped.append(f"{c.name}: non-public base {_type_spelling(ch.type)} dropped; its members are not bound")
                continue
            base_decl = ch.type.get_canonical().get_declaration()
            if not _SUBST.active and base_decl.kind != K.NO_DECL_FOUND and base_decl.spelling == "Iterator" \
                    and base_decl.semantic_parent is not None and base_decl.semantic_parent.spelling in BINDERS \
                    and "Iterator" in BINDERS[base_decl.semantic_parent.spelling].get("nested", {}):
                # 6a: the base is a binder instantiation's nested Iterator (Graphic3d_SequenceOfHClipPlane::Iterator derives from
                # NCollection_Sequence<handle<Graphic3d_ClipPlane>>::Iterator): register the owner instantiation, spell the base
                # with its manifest key and declare the class after the templates phase, where the base exists
                owner_t = base_decl.semantic_parent.type
                _note_instance(owner_t)
                canon = owner_t.get_canonical()
                all_args = [_canonical_args(canon.get_template_argument_type(i)) for i in range(canon.get_num_template_arguments())]
                key = f"{base_decl.semantic_parent.spelling}<{', '.join(instance_args(base_decl.semantic_parent.spelling, all_args))}>"
                c.bases.append(f"{key}::Iterator")
                c.after_templates = True
                continue
            if not _SUBST.active and base_decl.kind != K.NO_DECL_FOUND and base_decl.spelling in BINDERS:
                # 6a: the base is a binder instantiation itself (BinObjMgt_RRelocationTable : NCollection_DataMap<int,
                # handle<Standard_Transient>>, XmlObjMgt_SRelocationTable : NCollection_IndexedMap<handle<Standard_Transient>>):
                # same treatment, the manifest key is the C++ spelling nanobind needs (defaults such as the hasher left out)
                _note_instance(ch.type)
                canon = ch.type.get_canonical()
                all_args = [_canonical_args(canon.get_template_argument_type(i)) for i in range(canon.get_num_template_arguments())]
                c.bases.append(f"{base_decl.spelling}<{', '.join(instance_args(base_decl.spelling, all_args))}>")
                c.after_templates = True
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
            c.has_declared_ctor = True             # R-IMPLICIT-DEFAULT: any declared constructor (any access) counts
        if ch.access_specifier != Access.PUBLIC:
            continue
        if ch.kind == K.CONSTRUCTOR:
            # R-DELETED: deleted and move constructors are not bound, without a report line
            if ch.is_move_constructor() or ch.is_deleted_method():
                continue
            # R-IMPLICIT-COPY, R-COPY: `T(const T&) = default` is the implicit copy, bound as that one
            if ch.is_copy_constructor() and ch.is_default_method():
                continue
            c.ctors.append(_ctor(ch, c, members))
        elif ch.kind == K.CXX_METHOD:
            mark = len(_dependent_uses)
            m = _method(ch, c.name, members)
            if m is None or m.skip_reason is not None:
                del _dependent_uses[mark:]         # a skipped member needs no instantiation (begin()/end() range iterators, 8.22)
            if m is None:
                continue
            if m.skip_reason is not None:
                c.skipped.append(f"{c.name}::{m.name}({', '.join(p.type for p in m.params)}): {m.skip_reason}")
            elif not m.is_static:
                _decide_kept(ch, c, m.params, True, m.is_const)      # R-METHOD-KEEP
            if m.skip_reason is None:
                _note_views(ch, m, c.name, None if m.is_static else c)      # R-RESULT-KEEP
            c.methods.append(m)
        elif ch.kind == K.VAR_DECL:
            # R-STATIC-DATA: a static data member (a VAR_DECL inside a class; FIELD_DECL is the instance kind). Until
            # 2026-09-30 they were dropped without a report line -- 46 public ones, all const: sentinels and defaults such
            # as RWGltf_GltfAccessor::INVALID_ID, NCollection_IncAllocator::THE_DEFAULT_BLOCK_SIZE (final review)
            canon = ch.type.get_canonical()
            if canon.kind in (TK.CONSTANTARRAY, TK.INCOMPLETEARRAY, TK.VARIABLEARRAY):
                c.skipped.append(f"{c.name}::{ch.spelling}: static data member: array (not bound)")
            elif not ch.type.is_const_qualified():
                c.skipped.append(f"{c.name}::{ch.spelling}: static field that is not const -> not bound (a class attribute would be a stale copy)")
            else:
                reason = _unsupported(ch.type, allow_out=False)
                if reason is not None:
                    c.skipped.append(f"{c.name}::{ch.spelling}: static data member: {reason}")
                else:
                    # the value is in the header when the declaration carries an initialiser (`static const int X = 5;`,
                    # constexpr); `static const double X;` is defined in the .cxx and needs the symbol (R-UNDEFINED)
                    c.statics.append(Constant(py_name=py_safe(ch.spelling), cpp=f"{c.name}::{ch.spelling}", doc=_doc(ch),
                                              type_class=_class_behind(ch.type), mangled=ch.mangled_name,
                                              value_in_header=any(x.kind.is_expression() for x in ch.get_children())))
        elif ch.kind == K.FIELD_DECL:
            reason = _unsupported(ch.type, allow_out=False)
            # R-ARRAY: an array field R-FIXED-ARRAY cannot express is skipped and reported below
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
                reason = "reference member (no pointer-to-member)"     # R-UNSUPPORTED: a reference-typed field
            if reason is not None:
                c.skipped.append(f"{c.name}::{ch.spelling}: field {reason}")
                continue
            _note_instance(ch.type)                # a container-typed field needs its instantiation like a parameter does
            c.fields.append(Field(name=ch.spelling, type=_type_spelling(ch.type), is_const=ch.type.is_const_qualified(), doc=_doc(ch),
                                  is_bitfield=ch.is_bitfield(),    # R-FIELD: `unsigned stick : 1` (Graphic3d_CStructure) has no pointer-to-member
                                  is_container=ch.type.get_canonical().kind not in (TK.POINTER, TK.LVALUEREFERENCE, TK.RVALUEREFERENCE)
                                  and _container_kind(ch.type) != ""))
            if ch.type.get_canonical().kind == TK.POINTER or c.fields[-1].type.rstrip().endswith("*"):
                # R-FIELD: a raw pointer member is never written from Python (the object would keep the address of a Python
                # object it does not keep alive); what it points to is read as a copy, decided with the pointee's layout
                pointee = ch.type.get_canonical().get_pointee()
                if pointee.get_canonical().kind in (TK.CHAR_S, TK.CHAR_U):
                    c.fields[-1].is_pointer = True     # const char* (R-CSTRING): a str copy
                else:
                    decl = pointee.get_canonical().get_declaration()
                    defn = decl.get_definition() if decl.kind != K.NO_DECL_FOUND else None
                    if defn is not None and _derives_from(defn, "Standard_Transient"):
                        c.skipped.append(f"{c.name}::{ch.spelling}: field is a raw pointer to a Transient, which a handle may not own "
                                         f"(R-FIELD) -> not bound")
                        c.fields.pop()
                    else:
                        lay = _type_layout(ch.type, c.fields[-1].type)
                        _fields_open.append((c, c.fields[-1], None if lay is None else lay[1]))
        elif ch.kind == K.FRIEND_DECL:
            # R-FREE-OP: a hidden friend operator (`friend NCollection_Vec3 operator+(const NCollection_Vec3&, const NCollection_Vec3&)`
            # in NCollection_Vec2/3/4, math_Matrix, BRepGraph_ItemId) is a free function found by ADL only; it is handed to the
            # free-operator pass, which binds it as a (reflected) dunder on the class operand. Friend classes and non-operator
            # friends are C++ access grants, not API.
            for fr in ch.get_children():
                if fr.kind != K.FUNCTION_DECL or not fr.spelling.startswith("operator") or fr.access_specifier != Access.PUBLIC:
                    continue
                params, reason = _params(fr, fr.spelling)
                rk, rc = _result_kind(fr.result_type)
                fn = Function(name=fr.spelling, params=params, result=_type_spelling(fr.result_type), result_kind=rk, result_class=rc,
                              is_noexcept=_is_noexcept(fr), doc=_doc_with_deprecation(fr), header=c.header, is_operator=True,
                              skip_reason=reason, qualified=fr.spelling,
                              defined_in_header=fr.is_definition() or fr.get_definition() is not None or _SUBST.active, mangled=fr.mangled_name,
                              result_class_name=_class_behind(fr.result_type), result_instance_key=_binder_key(fr.result_type))
                if fn.skip_reason is None and _is_print_operator(fn.name, params, fr.result_type):
                    fn.result, fn.result_kind, fn.result_class = "void", ResultKind.VALUE, ""     # R-STR
                elif fn.skip_reason is None:
                    fn.skip_reason = _unsupported(fr.result_type, allow_out=False)
                if fn.skip_reason is not None:
                    c.skipped.append(f"{c.name}: friend {fn.name}({', '.join(p.type for p in params)}): {fn.skip_reason}")
                c.friend_ops.append(fn)
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
            c.skipped.append(f"{c.name}::{ch.spelling}: template member")      # R-UNSUPPORTED: skipped, reported
        elif ch.kind in (K.CLASS_DECL, K.STRUCT_DECL) and ch.is_definition():
            # R-NESTED: a public nested class/struct becomes a class of its own, declared into its outer class (non-public
            # ones were skipped above)
            if ch.spelling == "":
                c.skipped.append(f"{c.name}: anonymous nested struct")
            elif _SUBST.active and cursor.spelling in _STL_ITERATORS:
                # NCollection_ForwardRangeIterator::PostfixProxy: plumbing of an STL-style iterator, which Python does not
                # use (R-ITERATOR)
                c.skipped.append(f"{cursor.spelling}::{ch.spelling}: nested class of a class template (alias instantiation)")
            else:
                # a nested class of a 6c instantiation is walked with the instantiation's substitution still active
                # (NCollection_FlatMap<K, H>::Iterator: without it the BRepGraph flat maps could not be iterated)
                n = _class(ch, header, package, outer=c.name)
                if _SUBST.active:
                    # _class spells an instantiation's path flat (py_path of a name with '<'); a nested class belongs to its
                    # outer class like any other nested class: NCollection_FlatMap__BRepGraph_UID__...Iterator -> <outer>.Iterator
                    n.scope, n.py_name = c.scope + (c.py_name,), ch.spelling
                if n.unbindable:
                    c.skipped.extend(n.skipped)
                else:
                    c.nested.append(n)
        elif ch.kind == K.CLASS_TEMPLATE:
            c.skipped.append(f"{c.name}::{ch.spelling}: nested class template")      # R-UNSUPPORTED: skipped, reported
    _class_layouts.append((c, _held_types(cursor, c)))     # Class.view, decided with the layout probe
    return c


_instances_seen: dict[str, TemplateInstance] = {}    # filled while parsing a package (reset per package)
_owned_instance_args: set[str] = set()                # R-OWNER: their arguments with known OCAF owners (reset per package)


def collect_state() -> dict:
    """The cross-package state this process accumulated while parsing (see the note at _derives_cache)."""
    return {"noncopyable": set(_DETECTED_NONCOPYABLE), "derives": dict(_derives_cache), "ancestors": dict(_ancestors_cache)}


def carry_state(state: dict) -> None:
    """Seed the cross-package state, so a parse sees what other packages (or processes) already found."""
    _DETECTED_NONCOPYABLE.update(state.get("noncopyable", ()))
    for k, v in state.get("derives", {}).items():
        # a True was computed in a translation unit where the base was visible; never let a False overwrite it
        if v or k not in _derives_cache:
            _derives_cache[k] = v
    # every cached ancestor list was read from a definition (_class_ancestors), so all processes agree on each of them
    _ancestors_cache.update(state.get("ancestors", {}))


def _canonical_args(t: cindex.Type) -> str:
    """Portable canonical spelling of a type used as a template argument (typedefs resolved, std::__1 stripped)."""
    return re.sub(r"std::__\w+::", "std::", t.get_canonical().spelling)


_NESTED_OWNER = {src: kind for kind, info in BINDERS.items() for src in info.get("nested_from", {}).values()}   # TListIterator -> List


def _note_dependent_use(t: cindex.Type) -> None:
    """6c inside a 6c walk: a member of an instantiation names another instantiation of a class template
    through the template's parameters -- NCollection_Vec4<Element_t>::xyz() returns NCollection_Vec3<Element_t> -- which
    libclang reports as a dependent type with no declaration, so _note_instance cannot queue it and the member was bound
    with an unregistered type (`Vec4__unsigned_char().xyz()` raised TypeError: 74 stub lines over four Vec instantiations).
    Its spelling after substitution is recorded instead and instantiated through the R-TEMPLATE-BASE probe typedef."""
    spelled = re.sub(r"\s*(const\s*)?[&*]+\s*(const)?\s*$", "", _type_spelling(t)).removeprefix("const ").strip()
    m = re.match(r"^([\w:]+)<(.*)>$", spelled)
    while m is not None and m.group(1).split("::")[-1] in _SMART_HANDLES:
        # handle<BVH_Tree<T, N>> (BVH_PrimitiveSet<T, N>::BVH()): the instantiation inside the handle is what must be bound --
        # skipping the handle left BVH_Tree<double, 2> and BVH_Builder<double, 2> unbound
        spelled = m.group(2).strip()
        m = re.match(r"^([\w:]+)<(.*)>$", spelled)
    if m is None or "type-parameter-" in spelled:
        return
    name = m.group(1).split("::")[-1]
    if name in BINDERS or m.group(1).startswith("std::"):
        return
    if _SUBST.self_ is not None and (spelled == _SUBST.self_[1] or m.group(1) in (_SUBST.self_[0], _SUBST.self_[2])
                                     and m.group(2).replace(" ", "") == ",".join(_SUBST.params.values()).replace(" ", "")):
        return            # the walked instantiation itself, spelled with its arguments: NCollection_AliasedArray<MyAlignSize> inside
                          # NCollection_AliasedArray<> (key "<>", substituted "<16>") would be bound a second time
    if spelled not in _dependent_uses:
        _dependent_uses.append(spelled)


def _note_instance(t: cindex.Type) -> None:
    """If t (or its pointee) is an instantiation of an NCollection template we have a binder for, record it,
    including nested instantiations in its arguments. Any other OCCT class template instantiation in a signature
    (BRepGraph_MutGuard<...>, BVH_Box<double, 3>) is recorded for on-demand instantiation (6c)."""
    if _SUBST.active:
        _note_dependent_use(t)
    canon = t.get_canonical()
    while canon.kind in (TK.LVALUEREFERENCE, TK.RVALUEREFERENCE, TK.POINTER):
        canon = canon.get_pointee().get_canonical()
    if canon.kind != TK.RECORD or canon.get_num_template_arguments() <= 0:
        return
    decl = canon.get_declaration()
    if decl.spelling in _SMART_HANDLES:  # opencascade::handle<NCollection_HArray1<T>> -> look inside (NCollection_Handle<T> too)
        _note_instance(canon.get_template_argument_type(0))
        return
    for i in range(canon.get_num_template_arguments()):     # R-OWNER: the binder keeps the OCAF owners of such elements
        arg = canon.get_template_argument_type(i)
        if arg.kind != TK.INVALID and _owned(arg):
            _owned_instance_args.add(_canonical_args(arg))
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
        # 6c: queue the *stripped, unqualified* declaration type. `t` may be `const NCollection_Vec4<uint8_t>&`, whose
        # canonical kind is LVALUEREFERENCE, and _is_plain_template_instance would answer False for it -- an
        # instantiation reachable only through a reference parameter was never instantiated, and the method bound with
        # an unregistered type (RWPly_PlyWriterContext::WriteVertex, uncallable; found 2026-09-23). Most were masked by
        # the same instantiation appearing as a field, a by-value parameter or a typedef somewhere else.
        if not _SUBST.active and _is_plain_template_instance(decl.type) and "type-parameter-" not in canon.spelling:
            _template_uses.append(decl.type)
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
    if key not in _instance_layouts and not _is_dependent(canon):
        layout = _type_layout(canon)
        if layout is not None:
            _instance_layouts[key] = layout[1]


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


def _matching_specialisation(tu: cindex.TranslationUnit, qualified: str, args: list[str]) -> tuple[str, cindex.Cursor | None, dict[str, str]] | None:
    """The partial or explicit specialisation an instantiation with these arguments really comes from, or None for the
    primary template. libclang reports the primary template even for an implicit instantiation of a partial
    specialisation (clang_getSpecializedCursorTemplate, measured 2026-09-30), so the specialisations declared in the
    translation unit are matched against the arguments here. Deliberately conservative: a pattern argument must be a
    bare parameter of the specialisation (bound to the argument, consistently) or equal the argument literally; a pattern
    like `T*` or `X<T>` does not match. Returns ("partial", cursor, {parameter: argument}), ("explicit", cursor, {}),
    ("ambiguous", None, {}) when more than one matches (C++ would pick the most specialised one), or None."""
    parts = qualified.split("::")
    scopes = _scope_reopenings(tu, "::".join(parts[:-1])) if len(parts) > 1 else [tu.cursor]
    norm = [a.replace(" ", "") for a in args]
    found: list[tuple[str, cindex.Cursor, dict[str, str]]] = []
    for sc in scopes:
        for cur in sc.get_children():
            if cur.spelling != parts[-1] or not cur.is_definition():
                continue
            if cur.kind == K.CLASS_TEMPLATE_PARTIAL_SPECIALIZATION:
                own = [p.spelling for p in cur.get_children()
                       if p.kind in (K.TEMPLATE_TYPE_PARAMETER, K.TEMPLATE_NON_TYPE_PARAMETER, K.TEMPLATE_TEMPLATE_PARAMETER)]
                # displayname, not type.spelling: the pip libclang 18 (Linux, Windows) spells the specialisation's type
                # with canonical parameters (`Tree<type-parameter-0-0, N, Bin>`), Xcode's with their names (`Tree<T, N,
                # Bin>`); the displayname is `Tree<T, N, Bin>` with both (measured 2026-09-30)
                m = re.search(r"<(.*)>$", cur.displayname or cur.type.spelling)
                pattern = _split_top(m.group(1)) if m is not None else []
                if len(pattern) != len(args):
                    continue
                bound: dict[str, str] = {}
                ok = True
                for pat, arg, na in zip(pattern, args, norm):
                    if pat in own:
                        if bound.setdefault(pat, arg).replace(" ", "") != na:
                            ok = False
                    elif pat.replace(" ", "") != na:
                        ok = False
                    if not ok:
                        break
                if ok and set(bound) == set(own):
                    found.append(("partial", cur, bound))
            elif cur.kind in (K.CLASS_DECL, K.STRUCT_DECL) and "<" in cur.displayname:
                m = re.search(r"<(.*)>$", cur.displayname)
                if m is not None and [a.replace(" ", "") for a in _split_top(m.group(1))] == norm:
                    found.append(("explicit", cur, {}))
    if len(found) == 0:
        return None
    explicit = [f for f in found if f[0] == "explicit"]
    if len(explicit) > 0:
        return explicit[0]                        # a full specialisation beats every partial one in C++
    if len(found) > 1:
        return ("ambiguous", None, {})
    return found[0]


def _template_default(param: cindex.Cursor) -> str | None:
    """Default of a template parameter as written (`bool IsFull = false` -> 'false')."""
    toks = [t.spelling for t in param.get_tokens()]
    if "=" not in toks:
        return None
    return " ".join(toks[toks.index("=") + 1:])


# Binding-Rules.md 6c (template aliases and on-demand instantiations), R-TEMPLATE-NAME
def _instantiate_template(tu: cindex.TranslationUnit, t: cindex.Type, header: str, package: str, report: list[str],
                          what: str, py_name: str | None) -> Class | None:
    """The members of a class template instantiated for the arguments of t, walked from the template's definition
    with argument substitution (Binding-Rules.md 6c). py_name: the alias name, or None for an instantiation that is only a
    base class (BRepGraph_WiresOfEdge : EdgeParentsOf<...>) -> the mangled name. NCollection containers (hand-written
    binders) and std types are not handled here. Returns None (with a report line) when it cannot be done."""
    canon = t.get_canonical()
    if canon.kind != TK.RECORD or canon.get_num_template_arguments() <= 0 or "<" not in t.spelling:
        return None
    tmpl_name = canon.get_declaration().spelling
    if tmpl_name in BINDERS or tmpl_name in _SMART_HANDLES or t.spelling.startswith("std::"):
        return None
    qualified = _qualified_template(canon.get_declaration())        # BRepGraph_NodeId::Typed for nested templates
    # a template of a skipped namespace is third-party plumbing, not API: RWGltf_GltfJsonParser derives from
    # rapidjson::GenericDocument, which dragged in the library's Writer, MemoryPoolAllocator, BasicOStreamWrapper and
    # UTF8<char> -- and their defaults name protected constants, so the package did not compile (2026-09-22)
    if any(part in _SKIP_NAMESPACES for part in qualified.split("::")[:-1]):
        line = f"{qualified}: namespace skipped (overrides.toml [skip] namespaces)"
        if line not in report:
            report.append(line)
        return None
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
    # 6c, partial specialisations: BVH_Tree<T, N, BVH_BinaryTree> is the real class, the primary template
    # BVH_Tree<T, N, Arity> is empty -- walking the primary bound BVH_Tree<double, 3, BVH_BinaryTree> without a member or a base
    spec = _matching_specialisation(tu, qualified, args)
    walked = tmpl
    if spec is not None and spec[0] != "partial":
        # an explicit specialisation is a class of its own, bound from its declaration like any class (not from the template)
        report.append(f"{what}: {full} is an explicit specialisation -> not instantiated from the template" if spec[0] == "explicit"
                      else f"{what}: {full} matches more than one partial specialisation -> not bound")
        return None
    assert not _SUBST.active, "nested template walks are not supported"
    if spec is not None:
        walked = spec[1]
        _SUBST.params.update(spec[2])              # the specialisation's own parameters, deduced from its pattern
    else:
        for names in param_lists:                  # every declaration's parameter names, position-wise
            for name, a in zip(names, args):
                _SUBST.params.setdefault(name, a)
    _SUBST.self_ = (tmpl_name, full, qualified)
    type_kinds = (K.TYPEDEF_DECL, K.TYPE_ALIAS_DECL, K.CLASS_DECL, K.STRUCT_DECL, K.ENUM_DECL, K.CLASS_TEMPLATE)
    for ch in walked.get_children():
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
    ancestor = walked.semantic_parent
    while ancestor is not None and ancestor.kind in (K.NAMESPACE, K.CLASS_DECL, K.STRUCT_DECL) and ancestor.spelling != "":
        prefix = _qualified_template(ancestor)
        for sc in _scope_reopenings(tu, prefix):
            for ch in sc.get_children():
                if ch.kind in type_kinds and ch.spelling != "" and ch.spelling != tmpl_name and ch.spelling not in _SUBST.params \
                        and ch.spelling not in _SUBST.members:
                    _SUBST.scope.setdefault(ch.spelling, f"{prefix}::{ch.spelling}")
        ancestor = ancestor.semantic_parent
    try:
        c = _class(walked, header, package)
    finally:
        _SUBST.clear()
    c.name = full
    c.py_name = py_name if py_name is not None else _py_identifier(full)
    c.template_key = f"{qualified}<{', '.join(k for k in keys if k != '')}>"
    for m in c.methods:
        m.defined_in_header = True            # instantiated from the header, no library symbol involved
    _reparent_nested(c)
    return c


def _reparent_nested(c: Class) -> None:
    """The nested classes of an instantiation were walked while it still had its provisional name; point them at its
    final C++ name and Python path (the alias for TColStd_PackedMapOfInteger = NCollection_PackedMap<int>), recursively."""
    for n in c.nested:
        n.outer, n.scope = c.name, c.scope + (c.py_name,)
        for m in n.methods:
            m.defined_in_header = True
        _reparent_nested(n)


def _alias_instance(tu: cindex.TranslationUnit, cur: cindex.Cursor, header: str, package: str, report: list[str]) -> Class | None:
    """using math_Vector = math_VectorBase<double>; -> the template instantiated under the alias name (Binding-Rules.md 6c)."""
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


# Binding-Rules.md R-PRELUDE
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
    # R-SKIP-HEADER: a header listed in overrides.toml [skip] headers is left out of the parse and reported
    ir = PackageIR(name=pkg.name, toolkit=pkg.toolkit,
                   headers=[h for h in pkg.headers if h not in _SKIP_HEADERS and (allowed is None or h in allowed)])
    for h in pkg.headers:
        if h in _SKIP_HEADERS:
            ir.report.append(f"{h}: skipped (overrides.toml [skip] headers)")
        elif allowed is not None and h not in allowed:
            ir.report.append(f"{h}: not in the allowlist (overrides.toml [include] headers)")
    headers = set(ir.headers)
    _instances_seen.clear()
    _owned_instance_args.clear()
    _template_bases.clear()
    _template_uses.clear()
    _dependent_bases.clear()
    _dependent_uses.clear()
    _held_by_class.clear()
    _held_open.clear()
    _layout_of_type.clear()
    _views_open.clear()
    _class_layouts.clear()
    _kept_view_open.clear()
    _fields_open.clear()
    _instance_layouts.clear()
    _instance_owners.clear()
    _cycle_open.clear()
    _strong_edges_of.clear()
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
        def header_of(f: cindex.File) -> str | None:
            """The package header a cursor belongs to: X.hxx, or X.hxx for a cursor in X.lxx (the inline part that X.hxx includes
            at its end: std::hash<TDF_Label>, std::hash<TCollection_AsciiString>, TopLoc_Location's ShallowDump live there)."""
            name = Path(f.name).name
            if name in headers:
                return name
            if name.endswith(".lxx") and name[:-4] + ".hxx" in headers:
                return name[:-4] + ".hxx"
            return None

        def top_level(cursor: cindex.Cursor, ns: str):
            """File-scope declarations, descending into namespaces (OCCT 8 math packages use them)."""
            for cur in cursor.get_children():
                f = cur.location.file
                if f is None:
                    continue
                if header_of(f) is None:
                    continue
                if cur.kind == K.NAMESPACE:
                    yield from top_level(cur, f"{ns}{cur.spelling}::")
                else:
                    yield cur, ns

        def add_class(c: Class) -> None:
            ir.classes.append(c)
            for n in c.nested:               # nested classes are bound after (and into) their outer class (R-NESTED)
                add_class(n)

        for cur, ns in top_level(tu.cursor, ""):
            header = header_of(cur.location.file)
            assert header is not None
            if cur.kind in (K.CLASS_DECL, K.STRUCT_DECL) and cur.type.get_num_template_arguments() > 0 and cur.semantic_parent is not None \
                    and cur.semantic_parent.kind in (K.CLASS_DECL, K.STRUCT_DECL, K.CLASS_TEMPLATE):
                # an explicit specialisation of a member class template written at file scope (`template <> struct
                # BRepGraphInc_Storage::TypedStorePlanes<BRepGraph_VertexId>` in BRepGraphInc_Storage.lxx): the member template is
                # private to its class; an out-of-line definition of a plain nested class (`class BRepGraph::EditorView`) stays
                continue
            if ns == "" and cur.semantic_parent is not None and cur.semantic_parent.kind == K.NAMESPACE:
                ns = _qualified_template(cur.semantic_parent) + "::"     # `template <> struct std::hash<X>` written at file scope
            # R-NAMESPACE: a namespace named like the package is the package module itself (TopoDS::Vertex ->
            # nanocct.TopoDS.Vertex); every other namespace becomes a submodule (Geom2dEval_RepCurveDesc::Base ->
            # nanocct.Geom2dEval.Geom2dEval_RepCurveDesc.Base)
            ns_parts = [part for part in (ns.rstrip(":").split("::") if ns != "" else []) if not part.startswith("__")]   # std::__1 -> std
            if "" in ns_parts:
                ir.report.append(f"{header}: {cur.spelling}: anonymous namespace (not bound)")
                continue
            if any(part in _SKIP_NAMESPACES for part in ns_parts):
                # R-HASH: a std::hash<T> specialisation (full, or partial for a class template) makes T hashable
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
                # R-TEMPLATE-SKIP: a function or class template in a namespace has no concrete type -> not bound, reported
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
                              defined_in_header=cur.is_definition() or cur.get_definition() is not None, mangled=cur.mangled_name,
                              result_class_name=_class_behind(cur.result_type), result_instance_key=_binder_key(cur.result_type))
                if fn.skip_reason is None and _is_print_operator(fn.name, params, cur.result_type):
                    fn.result, fn.result_kind, fn.result_class = "void", ResultKind.VALUE, ""     # R-STR
                elif fn.skip_reason is None:
                    fn.skip_reason = _unsupported(cur.result_type, allow_out=False)
                if fn.skip_reason is not None:
                    ir.report.append(f"{fn.name}(...): {fn.skip_reason}")
                else:
                    _note_views(cur, fn, "", None)               # R-RESULT-KEEP
                ir.functions.append(fn)
            elif cur.kind in (K.TYPEDEF_DECL, K.TYPE_ALIAS_DECL):
                # R-ALIAS: every typedef is recorded for Emitter._aliases, which binds it as a second name of its target
                ir.typedefs.append(TypeAlias(py_name=cur.spelling, target=_canonical_args(cur.underlying_typedef_type),
                                             written=_type_spelling(cur.underlying_typedef_type), scope=scope))
                _note_instance(cur.underlying_typedef_type)      # BVH_Array3d = NCollection_LinearVector<...>: bind the instantiation
                if ns != "":
                    continue                       # alias instantiation (6c) only at package level
                if not any(c.py_name == cur.spelling for c in ir.classes):     # the same alias appears in several headers
                    inst = _alias_instance(tu, cur, header, pkg.name, ir.report)
                    if inst is not None:
                        add_class(inst)            # with its nested classes (TColStd_PackedMapOfInteger.Iterator)
            elif cur.kind in (K.CLASS_TEMPLATE, K.FUNCTION_TEMPLATE):
                if cur.semantic_parent is not None and cur.semantic_parent.kind in (K.CLASS_DECL, K.STRUCT_DECL, K.CLASS_TEMPLATE):
                    continue                       # an out-of-line member template definition (TCollection_AsciiString::Cat<T> in the .lxx): reported with its class
                # R-TEMPLATE-SKIP: a package-level template no typedef instantiates (6c) -- not bound, reported
                ir.report.append(f"{cur.spelling}: template (not bound)")
        # bases that are un-aliased template instantiations (BRepGraph_WiresOfEdge : EdgeParentsOf<...>): instantiated
        # on demand under the mangled name, so that the derived class can be bound (Binding-Rules.md 6c)
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
            queued = _dependent_bases + [("", u, ir.headers[0]) for u in _dependent_uses]    # "": a use, not a base (8.22)
            todo = [(d, b, h) for d, b, h in queued if b not in seen_uses and not any(c.name == b for c in ir.classes)
                    and b not in (known_elsewhere or set())]
            if len(todo) == 0:
                break
            spellings = sorted({b for _, b, _ in todo})
            probe = Path(td) / f"{pkg.name}__probe.hxx"
            probe.write_text(umbrella.read_text() + "".join(f"using nanocct_probe_{i} = {b};\n" for i, b in enumerate(spellings)))
            tu2 = index.parse(str(probe), args=args)
            probes = {cur.spelling: cur for cur in tu2.cursor.get_children() if cur.kind == K.TYPE_ALIAS_DECL and cur.spelling.startswith("nanocct_probe_")}
            _dependent_bases.clear()
            _dependent_uses.clear()
            for i, b in enumerate(spellings):
                seen_uses.add(b)
                cur = probes.get(f"nanocct_probe_{i}")
                derived_names = [d for d, bb, _ in todo if bb == b and d != ""]
                what = f"{derived_names[0]}: base class {b}" if len(derived_names) > 0 else f"used in a signature: {b}"
                inst = None
                if cur is not None:
                    inst = _instantiate_template(tu2, cur.underlying_typedef_type, ir.headers[0], pkg.name, ir.report, what, None)
                else:
                    ir.report.append(f"{what}: the probe typedef did not compile")
                if inst is not None:
                    if inst.name != b:            # defaulted arguments spelled out by the instantiation: the derived classes follow
                        for c in ir.classes:
                            c.bases = [inst.name if x == b else x for x in c.bases]
                    add_class(inst)
        _resolve_held_layout(index, umbrella, args, td)       # R-CTOR-KEEP: layout spelled only after substitution
        _decide_views(ir.report)                                # R-RESULT-KEEP: once every layout is complete
        _decide_cycles()                                        # R-KEPT: once every parameter's kept is
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
    ir.owned_args = set(_owned_instance_args)
    ir.copy_owner_instances = dict(_instance_owners)
    if pkg.name in _BINARY_PACKAGES:            # R-STREAM-OUT, R-STREAM-IN: binary formats -> bytes / typing.BinaryIO
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
