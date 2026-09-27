// Shared by every generated nanoOCP translation unit.
#pragma once
// MSVC only: nanobind defines NB_INLINE as __forceinline, and MSVC's optimizer is superlinear in the size of a
// function that expands it that often. A binding registration function is exactly that. Measured on gauss
// (i7-8700, MSVC 14.44, 2026-09-23) for src/cpp/TKMath/math.cpp -- 531 .def calls in one function -- at the build's
// own /O2 /Ob2 /Os:
//     __forceinline (stock)   ~1677 s (in the parallel build; /O1 alone ran >8 min and was killed)
//     inline                      16 s, and the object is SMALLER (6958 KB vs 9045 KB at /Od)
// Upstream reports the same and names __forceinline as the trigger: 2 h 28 m -> 3 m 04 s
// (https://github.com/wjakob/nanobind/discussions/791). nb_defs.h is #pragma once guarded, so pulling it in first and
// redefining the macro here needs no patched or vendored nanobind. clang and gcc keep always_inline: neither has the
// problem, and nanobind wants the hint for the binding layer's hot paths.
#if defined(_MSC_VER)
#  include <nanobind/nb_defs.h>
#  undef NB_INLINE
#  define NB_INLINE inline
#endif
#include <nanobind/nanobind.h>
#include <nanobind/make_iterator.h>
#include <nanobind/stl/array.h>
#include <nanobind/stl/function.h>
#include <nanobind/stl/list.h>
#include <nanobind/stl/map.h>
#include <nanobind/stl/optional.h>
#include <nanobind/stl/pair.h>
#include <nanobind/stl/set.h>
#include <nanobind/stl/shared_ptr.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/string_view.h>
#include <nanobind/stl/tuple.h>
#include <nanobind/stl/unique_ptr.h>
#include <nanobind/stl/unordered_map.h>
#include <nanobind/stl/unordered_set.h>
#include <nanobind/stl/variant.h>
#include <nanobind/stl/vector.h>
#include <algorithm>
#include <array>
#include <bitset>
#include <tuple>
#include <type_traits>

#include <sstream>
#include <string>
#include <typeinfo>
#include <unordered_map>
#include <vector>

#include <Standard_Failure.hxx>
#include <Standard_Handle.hxx>
#include <Standard_Transient.hxx>

namespace nb = nanobind;

// ---------------------------------------------------------------------------------------------
// Multiple inheritance (Design.md 4.2). nanobind reuses the derived-class pointer as the base
// pointer, so a bound base must live at offset 0 of the derived object (verified: HArray1 bound with
// base Standard_Transient read myLowerBound as the reference count). For a class S with several
// bases, nanobind's base is the offset-0 one (mi_traits<S>::base); members of the other base are
// bound through lambdas that static_cast from base& to S& (an adjusting downcast), and the handle
// caster converts between the stored base pointer and Standard_Transient* via this registry.
template <typename S> struct mi_traits;      // specialised by binders: { using base = B; }

struct mi_entry {
    PyObject *py_type;                                   // nanobind type of S
    Standard_Transient *(*to_transient)(void *stored);   // stored (base subobject) -> Transient subobject
    void *(*from_transient)(Standard_Transient *);       // Transient subobject of an S -> stored pointer
};

inline std::unordered_map<std::string, mi_entry> &nanoocp_mi_by_name() {   // key: typeid(S).name()
    static std::unordered_map<std::string, mi_entry> m;
    return m;
}
inline std::vector<mi_entry> &nanoocp_mi_list() {
    static std::vector<mi_entry> v;
    return v;
}

template <typename S> void nanoocp_register_mi(nb::handle py_type) {
    using B = typename mi_traits<S>::base;
    mi_entry e{py_type.ptr(),
               [](void *stored) -> Standard_Transient * { return static_cast<S *>(static_cast<B *>(stored)); },
               [](Standard_Transient *t) -> void * { return static_cast<B *>(static_cast<S *>(dynamic_cast<void *>(t))); }};
    nanoocp_mi_by_name()[typeid(S).name()] = e;
    nanoocp_mi_list().push_back(e);
}

template <typename S, typename = void> struct has_mi_traits : std::false_type {};
template <typename S> struct has_mi_traits<S, std::void_t<typename mi_traits<S>::base>> : std::true_type {};

// The multiple-inheritance types of NCollection. Declared here (forward declarations) so that every
// translation unit that instantiates the handle caster for them agrees on the layout rule.
template <class T> class NCollection_Array1;
template <class T> class NCollection_Array2;
template <class T> class NCollection_Sequence;
template <class T> class NCollection_HArray1;
template <class T> class NCollection_HArray2;
template <class T> class NCollection_HSequence;
template <class T, typename> class NCollection_Shared;
template <typename T> struct mi_traits<NCollection_HArray1<T>> { using base = NCollection_Array1<T>; };     // : Array1<T>, Standard_Transient
template <typename T> struct mi_traits<NCollection_HArray2<T>> { using base = NCollection_Array2<T>; };     // : Array2<T>, Standard_Transient
template <typename T> struct mi_traits<NCollection_HSequence<T>> { using base = NCollection_Sequence<T>; }; // : Sequence<T>, Standard_Transient
template <typename T, typename E> struct mi_traits<NCollection_Shared<T, E>> { using base = T; };           // : Standard_Transient, T

// ---------------------------------------------------------------------------------------------
// OCCT exceptions. Standard_Failure descendants declared with DEFINE_STANDARD_EXCEPTION are
// header-only, so their typeinfo is duplicated per shared object and catch-by-derived-type does
// not work across the OCCT library / extension module boundary. Each toolkit module therefore
// registers one translator that catches Standard_Failure and dispatches on the mangled name of
// the dynamic type; names it does not know are rethrown to the next module's translator, and the
// TKernel translator finally falls back to nanoocp.Standard.Standard_Failure.
inline std::unordered_map<std::string, PyObject *> &nanoocp_exception_map() {
    static std::unordered_map<std::string, PyObject *> map;
    return map;
}

template <typename T> void nanoocp_register_exception(nb::handle py_type) {
    nanoocp_exception_map()[typeid(T).name()] = py_type.ptr();
}

// scope: the package module or a namespace submodule
inline nb::object nanoocp_new_exception(nb::handle m, const char *name, const char *doc, PyObject *base) {
    std::string qualified = nb::borrow<nb::str>(m.attr("__name__")).c_str();
    qualified += ".";
    qualified += name;
    nb::object type = nb::steal(PyErr_NewExceptionWithDoc(qualified.c_str(), doc, base, nullptr));
    m.attr(name) = type;
    return type;
}

// R-ITER (Design.md 2c): a class with More()/Next() and a parameterless Value() or Current() is its own Python
// iterator, like a file object: __iter__ returns self, __next__ yields the current element and advances. The element
// is copied out before Next() (a const reference from Value() would dangle afterwards).
// Constructors of a class-template instantiation whose abstractness only the compiler can see (BVH_PrimitiveSet<double, 3>
// through the pure virtuals of BVH_Set): the generic lambda's body is instantiated only when the class is concrete (R-TEMPLATE-BASE).
template <typename T, typename F> void nanoocp_if_concrete(nb::class_<T> cls, F f) {
    if constexpr (!std::is_abstract_v<T>)
        f(cls);
}

// R-ITER through nb::make_iterator, like the containers: a hand-written __next__ ended every loop with a thrown
// nb::stop_iteration, a C++ exception that cost ~8 us per loop however short (2026-09-27: a TopExp_Explorer over
// 6 faces took 8.5 us against 0.47 us for a More()/Next() loop). make_iterator ends without one. The cursor
// advances the object itself, so it is exhausted afterwards, like a file; the element is copied out before Next().
template <typename T, typename Get> struct nanoocp_iter_cursor {
    T *obj;                                   // nullptr: the end sentinel
    Get get;
    bool done() const { return obj == nullptr || !obj->More(); }
    bool operator==(const nanoocp_iter_cursor &o) const { return done() == o.done(); }
    bool operator!=(const nanoocp_iter_cursor &o) const { return !(*this == o); }
    nanoocp_iter_cursor &operator++() { obj->Next(); return *this; }
    auto operator*() const { return get(*obj); }    // by value: Current() may be a reference that Next() changes
};

template <typename T, typename Get> void nanoocp_def_iter(nb::class_<T> cls, Get get) {
    cls.def("__iter__", [get](T &self) {
        using Cursor = nanoocp_iter_cursor<T, Get>;
        return nb::make_iterator<nb::rv_policy::move>(nb::type<T>(), "iterator", Cursor{&self, get}, Cursor{nullptr, get});
    }, nb::keep_alive<0, 1>(),
    "Python addition: iterate with More()/Next(), yielding Value() (or Current()); the iterator advances the object "
    "itself, so it is exhausted afterwards.");
}

// The implicit default constructor of a class that declares none: bound only when it exists (a reference
// member or a non-default-constructible member deletes it; the header does not say so).
template <typename T> void nanoocp_implicit_default_ctor(nb::class_<T> cls) {
    if constexpr (std::is_default_constructible_v<T>) {
        if constexpr (std::is_base_of_v<Standard_Transient, T>)
            cls.def(nb::new_([]() { return opencascade::handle<T>(new T()); }));
        else
            cls.def(nb::init<>());
    }
}

// The implicit copy constructor (none declared by the class): bound when it exists (deleted for classes with a
// reference or non-copyable member). Sub-class arguments convert implicitly, as in C++ (TopoDS_Shape(aVertex)).
template <typename T> void nanoocp_implicit_copy_ctor(nb::class_<T> cls) {
    if constexpr (std::is_copy_constructible_v<T>) {
        if constexpr (std::is_base_of_v<Standard_Transient, T>)
            cls.def(nb::new_([](const T &other) { return opencascade::handle<T>(new T(other)); }), nb::arg("theOther"));
        else
            cls.def(nb::init<const T &>(), nb::arg("theOther"));
    }
}

// operator To() const of From: To gets a constructor from From (To(aFrom) in Python) and, unless the operator is
// explicit, the implicit conversion C++ has (a From passes where a To is expected). From is taken by non-const
// reference: some operators are not const (Message_Msg).
template <typename From, typename To> void nanoocp_conversion(nb::handle to_type, bool implicit) {
    auto cls = nb::borrow<nb::class_<To>>(to_type);
    if constexpr (std::is_base_of_v<Standard_Transient, To>)
        cls.def(nb::new_([](From &from) { return opencascade::handle<To>(new To(static_cast<To>(from))); }), nb::arg("theFrom"));
    else
        cls.def("__init__", [](To *self, From &from) { new (self) To(static_cast<To>(from)); }, nb::arg("theFrom"));
    if (implicit)
        nb::implicitly_convertible<From, To>();
}

// operator opencascade::handle<To>() const of From: the handle's object becomes the result of To(aFrom)
template <typename From, typename To> void nanoocp_conversion_handle(nb::handle to_type, bool implicit) {
    auto cls = nb::borrow<nb::class_<To>>(to_type);
    cls.def(nb::new_([](From &from) { return static_cast<opencascade::handle<To>>(from); }), nb::arg("theFrom"));
    if (implicit)
        nb::implicitly_convertible<From, To>();
}

// Public data member: read/write when its type can be assigned to (a member with a deleted copy assignment, e.g. of
// type BRepGraphInc_Storage, or a const member is read-only). Decided at compile time, the header does not say.
template <typename C, typename T, typename D, typename... Extra>
void nanoocp_def_field(nb::class_<C> cls, const char *name, D T::*p, const Extra &...extra) {
    if constexpr (std::is_copy_assignable_v<D> && !std::is_const_v<D>)
        cls.def_rw(name, p, extra...);
    else
        cls.def_ro(name, p, extra...);
}

// fallback: the Python type for Standard_Failure, or nullptr to pass unknown exceptions on
inline void nanoocp_install_exception_translator(PyObject *fallback) {
    nb::register_exception_translator(
        [](const std::exception_ptr &p, void *payload) {
            try {
                std::rethrow_exception(p);
            } catch (const Standard_Failure &e) {
                auto &map = nanoocp_exception_map();
                auto it = map.find(typeid(e).name());
                if (it != map.end()) {
                    PyErr_SetString(it->second, e.what());
                    return;
                }
                if (payload != nullptr) {
                    PyErr_SetString((PyObject *) payload, e.what());
                    return;
                }
                throw;
            }
        },
        fallback);
}

// The text an OCCT method wrote to a std::ostream& parameter, as a str. OCCT streams are text (Dump, DumpJson, Print,
// BRepTools::Write); decoded with surrogateescape so that a stray non-UTF-8 byte is lossless.
inline nb::str nanoocp_stream_text(const std::ostringstream &stream) {
    const std::string text = stream.str();
    return nb::steal<nb::str>(PyUnicode_DecodeUTF8(text.data(), static_cast<Py_ssize_t>(text.size()), "surrogateescape"));
}

// The same for the binary formats (the BinTools package, overrides.toml [stream] binary_packages): bytes.
inline nb::bytes nanoocp_stream_bytes(const std::ostringstream &stream) {
    const std::string data = stream.str();
    return nb::bytes(data.data(), data.size());
}

// A std::istream& / std::stringstream parameter (BRepTools::Read, InitFromJson): the text of a Python file-like object
// (anything with read(): io.StringIO, an open text file). A str is deliberately not accepted -- it would collide with
// the file-path overloads -- so a non-file-like argument falls through to the next overload. Typed typing.TextIO.
namespace nanoocp {
struct TextInput {
    std::string text;
};
// The binary counterpart (BinTools::Read): a binary file-like object (io.BytesIO, a file opened "rb"), whose read()
// returns bytes. Typed typing.BinaryIO. A text file-like object falls through (read() returns str).
struct BinaryInput {
    std::string data;
};
// R-CSTR-NULL: a const char* parameter with a null default (LDOM_XmlWriter(const char* theEncoding = nullptr),
// STEPCAFControl_Writer::Write(..., const char* theIsMulti = nullptr)). nanobind's const char* caster rejects None, which
// would make the default unreachable; this one takes a str or None (-> nullptr). The UTF-8 buffer belongs to the str
// object, which is alive for the duration of the call (as for nanobind's own caster). Typed `str | None` (with .none()).
struct OptionalCString {
    const char *ptr = nullptr;
};
// R-RESULT: nb::keep_alive<0, 1> for a `T&` Transient member result, except when the result is self. A method returning
// *this (LDOM_MemManager::Self(), FSD_File::PutInteger()) hands back the same Python object, and nanobind's keep_alive_py
// has no nurse == patient check (nb_type.cpp, nanobind 3.1.0): the object would hold a reference to itself that the
// garbage collector cannot see, and would never be freed ("nanobind: leaked instances", State.md 8.18).
struct KeepOwnerUnlessSelf {
    static void precall(PyObject **, size_t, nb::detail::cleanup_list *) {}
    static void postcall(PyObject **args, size_t, PyObject *&ret) {
        if (ret != nullptr && ret != args[0])
            nb::keep_alive_obj(ret, args[0]);   // the result (nurse) keeps self (patient) alive
    }
};
}

NAMESPACE_BEGIN(NB_NAMESPACE)
NAMESPACE_BEGIN(detail)

// Design.md 6 R-BITSET: an std::bitset<N> is a set of flags indexed by an enumerator
// (ShapeProcess::OperationsFlags = std::bitset<ShapeProcess::Operation::Last + 1>), so Python sees the set of the
// indices whose bit is set: proc.ProcessShape(shape, {ShapeProcess.FixShape, ShapeProcess.SameParameter}).
// nanobind's arithmetic enums are Python IntEnums, so the enumerators go in as ints and the plain ints that come
// back compare and hash equal to them ({0, 1} == {ShapeProcess.DirectFaces, ShapeProcess.SameParameter}).
// Any iterable of indices is accepted (set, frozenset, list, tuple); str, bytes and dict are rejected so that a
// name-taking overload stays reachable (ShapeProcess::Perform(context, const char* seq, range)).
template <size_t N> struct type_caster<std::bitset<N>> {
    NB_TYPE_CASTER(std::bitset<N>, const_name("set[int]"))

    bool from_python(handle src, uint32_t, cleanup_list *) noexcept {
        if (src.ptr() == nullptr || str_check(src.ptr()) || bytes_check(src.ptr()) || dict_check(src.ptr()))
            return false;
        PyObject *iterator = PyObject_GetIter(src.ptr());
        if (iterator == nullptr) {
            PyErr_Clear();
            return false;
        }
        value.reset();
        bool ok = true;
        PyObject *item = nullptr;
        while (ok && (item = PyIter_Next(iterator)) != nullptr) {
            if (!int_check(item)) {
                ok = false;
            } else {
                Py_ssize_t index = PyLong_AsSsize_t(item);
                if (index < 0 || (size_t) index >= N)
                    ok = false;
                else
                    value.set((size_t) index);
            }
            Py_DECREF(item);
        }
        Py_DECREF(iterator);
        if (PyErr_Occurred() != nullptr) {
            PyErr_Clear();
            ok = false;
        }
        return ok;
    }

    static handle from_cpp(const std::bitset<N> &v, rv_policy, cleanup_list *) noexcept {
        PyObject *out = PySet_New(nullptr);
        if (out == nullptr) {
            PyErr_Clear();
            return handle();
        }
        for (size_t i = 0; i < N; ++i) {
            if (!v.test(i))
                continue;
            PyObject *index = PyLong_FromSize_t(i);
            if (index == nullptr || PySet_Add(out, index) != 0) {
                Py_XDECREF(index);
                Py_DECREF(out);
                PyErr_Clear();
                return handle();
            }
            Py_DECREF(index);
        }
        return out;
    }
};

template <> struct type_caster<nanoocp::TextInput> {
    NB_TYPE_CASTER(nanoocp::TextInput, const_name("typing.TextIO"))

    bool from_python(handle src, uint32_t, cleanup_list *) noexcept {
        if (!hasattr(src, "read"))
            return false;
        try {
            object text = src.attr("read")();
            if (!str_check(text.ptr()))
                return false;
            bytes data = borrow<bytes>(text.attr("encode")("utf-8", "surrogateescape"));   // the inverse of nanoocp_stream_text
            value.text.assign(data.c_str(), data.size());
        } catch (...) {
            return false;
        }
        return true;
    }

    static handle from_cpp(const nanoocp::TextInput &, rv_policy, cleanup_list *) noexcept { return none_ref(); }
};

template <> struct type_caster<nanoocp::OptionalCString> {
    NB_TYPE_CASTER(nanoocp::OptionalCString, const_name("str"))   // nb::arg(...).none() appends "| None"

    bool from_python(handle src, uint32_t, cleanup_list *) noexcept {
        if (src.is_none()) {
            value.ptr = nullptr;
            return true;
        }
        if (!str_check(src.ptr()))
            return false;
        Py_ssize_t size = 0;
        value.ptr = PyUnicode_AsUTF8AndSize(src.ptr(), &size);
        if (value.ptr == nullptr) {
            PyErr_Clear();
            return false;
        }
        return true;
    }

    static handle from_cpp(const nanoocp::OptionalCString &v, rv_policy, cleanup_list *) noexcept {
        if (v.ptr == nullptr)
            return none_ref();
        return PyUnicode_FromString(v.ptr);
    }
};

template <> struct type_caster<nanoocp::BinaryInput> {
    NB_TYPE_CASTER(nanoocp::BinaryInput, const_name("typing.BinaryIO"))

    bool from_python(handle src, uint32_t, cleanup_list *) noexcept {
        if (!hasattr(src, "read"))
            return false;
        try {
            object data = src.attr("read")();
            if (!PyBytes_Check(data.ptr()))
                return false;
            bytes b = borrow<bytes>(data);
            value.data.assign(b.c_str(), b.size());
        } catch (...) {
            return false;
        }
        return true;
    }

    static handle from_cpp(const nanoocp::BinaryInput &, rv_policy, cleanup_list *) noexcept { return none_ref(); }
};

NAMESPACE_END(detail)
NAMESPACE_END(NB_NAMESPACE)

// Type caster for char16_t and const char16_t* (Standard_ExtString: OCCT's UTF-16 strings, TCollection_ExtendedString),
// modeled on nanobind's char caster: a Python str converts to a NUL-terminated UTF-16 buffer owned by the caster for the
// duration of the call, a const char16_t* result decodes to str, a single char16_t is a 1-character str.
NAMESPACE_BEGIN(NB_NAMESPACE)
NAMESPACE_BEGIN(detail)

template <> struct type_caster<char16_t> {
    using Value = const char16_t *;
    Value value = nullptr;
    std::u16string storage;
    static constexpr auto Name = const_name("str");
    template <typename T_>
    using Cast = std::conditional_t<is_pointer_v<T_>, const char16_t *, char16_t>;

    bool from_python(handle src, uint32_t, cleanup_list *) noexcept {
        if (!str_check(src.ptr()))
            return false;
        PyObject *bytes = PyUnicode_AsUTF16String(src.ptr());     // BOM + native byte order
        if (bytes == nullptr) {
            PyErr_Clear();
            return false;
        }
        char *buf = nullptr;
        Py_ssize_t n = 0;
        if (PyBytes_AsStringAndSize(bytes, &buf, &n) != 0) {
            PyErr_Clear();
            Py_DECREF(bytes);
            return false;
        }
        const char16_t *units = reinterpret_cast<const char16_t *>(buf);
        size_t count = static_cast<size_t>(n) / sizeof(char16_t);
        if (count > 0 && units[0] == u'\uFEFF') {
            ++units;
            --count;
        }
        storage.assign(units, count);
        Py_DECREF(bytes);
        value = storage.c_str();
        return true;
    }

    static handle from_cpp(const char16_t *v, rv_policy, cleanup_list *) noexcept {
        if (v == nullptr)
            return none_ref();
        int byteorder = 0;                                          // native
        return PyUnicode_DecodeUTF16(reinterpret_cast<const char *>(v),
                                     static_cast<Py_ssize_t>(std::char_traits<char16_t>::length(v) * sizeof(char16_t)),
                                     nullptr, &byteorder);
    }

    static handle from_cpp(char16_t v, rv_policy, cleanup_list *) noexcept {
        int byteorder = 0;
        return PyUnicode_DecodeUTF16(reinterpret_cast<const char *>(&v), sizeof(char16_t), nullptr, &byteorder);
    }

    template <typename T_>
    NB_INLINE bool can_cast() const noexcept {
        return std::is_pointer_v<T_> || storage.size() == 1;
    }

    explicit operator const char16_t *() { return value; }

    explicit operator char16_t() {
        if (storage.size() == 1)
            return storage[0];
        throw next_overload();
    }
};

NAMESPACE_END(detail)
NAMESPACE_END(NB_NAMESPACE)

// Type caster for char32_t (Standard_Utf32Char: the code-point API of Font_FTFont, Font_TextFormatter, NCollection_UtfString):
// a 1-character Python str, like char and char16_t (Design.md R-CHAR16).
NAMESPACE_BEGIN(NB_NAMESPACE)
NAMESPACE_BEGIN(detail)

template <> struct type_caster<char32_t> {
    NB_TYPE_CASTER(char32_t, const_name("str"))

    bool from_python(handle src, uint32_t, cleanup_list *) noexcept {
        if (!str_check(src.ptr()) || PyUnicode_GetLength(src.ptr()) != 1)
            return false;
        Py_UCS4 c = PyUnicode_ReadChar(src.ptr(), 0);
        if (c == (Py_UCS4) -1 && PyErr_Occurred()) {
            PyErr_Clear();
            return false;
        }
        value = static_cast<char32_t>(c);
        return true;
    }

    static handle from_cpp(char32_t v, rv_policy, cleanup_list *) noexcept {
        int byteorder = 0;                                          // native; PyUnicode_FromKindAndData is not in the stable ABI
        return PyUnicode_DecodeUTF32(reinterpret_cast<const char *>(&v), sizeof(char32_t), nullptr, &byteorder);
    }
};

NAMESPACE_END(detail)
NAMESPACE_END(NB_NAMESPACE)

// Type caster for opencascade::handle<T> (also occ::handle<T>), modeled on nanobind's shared_ptr
// caster. The Python instance never owns the C++ object directly; a heap-allocated handle is attached
// via keep_alive, so OCCT's intrusive reference count governs the lifetime on both sides.
NAMESPACE_BEGIN(NB_NAMESPACE)
NAMESPACE_BEGIN(detail)

template <typename T> struct type_caster<opencascade::handle<T>> {
    static constexpr bool IsClass = true;
    using Caster = make_caster<T>;
    using Td = std::decay_t<T>;
    NB_TYPE_CASTER(opencascade::handle<T>, Caster::Name)

    bool from_python(handle src, uint32_t flags, cleanup_list *cleanup) noexcept {
        if (src.is_none()) { value = opencascade::handle<T>(); return true; }
        flags &= ~cast_flags::convert;
        Caster caster;
        if (caster.from_python(src, flags, cleanup)) {
            Td *ptr = caster.operator Td *();
            if constexpr (has_mi_traits<Td>::value)      // stored pointer is the offset-0 base subobject
                ptr = static_cast<Td *>(reinterpret_cast<typename mi_traits<Td>::base *>(static_cast<void *>(ptr)));
            // A reference count of 0 means no handle owns the object: nanobind does (a by-value copy, a member reached
            // through a field). A handle made from it would delete that memory when it goes, whatever C++ does with it
            // (8.18). Every Transient nanoocp creates is handle-held (constructors, R-RESULT), so this is a gap in the
            // bindings; refusing the argument turns a crash into a TypeError.
            if (ptr != nullptr && ptr->GetRefCount() == 0)
                return false;
            value = opencascade::handle<T>(ptr);
            return true;
        }
        // a multiple-inheritance type whose Transient base is not the bound base (HArray1 -> Standard_Transient)
        for (const mi_entry &e : nanoocp_mi_list()) {
            if (PyType_IsSubtype(Py_TYPE(src.ptr()), (PyTypeObject *) e.py_type)) {
                Standard_Transient *t = e.to_transient(inst_ptr<void>(src));
                Td *ptr = dynamic_cast<Td *>(t);
                if (ptr == nullptr || ptr->GetRefCount() == 0) return false;   // count 0: see above
                value = opencascade::handle<T>(ptr);
                return true;
            }
        }
        return false;
    }

    static handle from_cpp(const Value &value, rv_policy, cleanup_list *cleanup) noexcept {
        Td *ptr = value.get();
        if (!ptr) return none().release();
        const std::type_info *type = &typeid(Td);
        const std::type_info *type_p = &typeid(*ptr);
        void *stored = ptr;
        if constexpr (has_mi_traits<Td>::value) {
            stored = static_cast<typename mi_traits<Td>::base *>(ptr);
        } else {
            auto &mi = nanoocp_mi_by_name();
            auto it = mi.find(type_p->name());          // dynamic type is a registered MI type
            if (it != mi.end()) stored = it->second.from_transient(ptr);
        }
        bool is_new = false;
        handle result = NB_CALL(nb_type_put)(NB_CTX_C(cleanup), type, type_p, stored,
                                             rv_policy::reference, cleanup, &is_new);
        if (is_new) {
            auto *holder = new opencascade::handle<Standard_Transient>(ptr);
            keep_alive_cb(result, holder,
                          [](void *p) noexcept { delete (opencascade::handle<Standard_Transient> *) p; });
        }
        return result;
    }
};

NAMESPACE_END(detail)
NAMESPACE_END(NB_NAMESPACE)
