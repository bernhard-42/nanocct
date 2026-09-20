// Shared by every generated nanoOCP translation unit.
#pragma once
#include <nanobind/nanobind.h>
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
#include <tuple>
#include <type_traits>

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
            value = opencascade::handle<T>(ptr);
            return true;
        }
        // a multiple-inheritance type whose Transient base is not the bound base (HArray1 -> Standard_Transient)
        for (const mi_entry &e : nanoocp_mi_list()) {
            if (PyType_IsSubtype(Py_TYPE(src.ptr()), (PyTypeObject *) e.py_type)) {
                Standard_Transient *t = e.to_transient(inst_ptr<void>(src));
                Td *ptr = dynamic_cast<Td *>(t);
                if (ptr == nullptr) return false;
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
