// Part of nanocct_common.h -- the objects shared by every extension module (nanocct_shared) and the multiple-inheritance / Kept<T> type registry (Runtime.md 5.2, R-KEPT).
// Include nanocct_common.h, not this file: the parts rely on each other in the order it includes them.
#pragma once

// ---------------------------------------------------------------------------------------------
// Multiple inheritance (Runtime.md 5.2). nanobind reuses the derived-class pointer as the base
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
    const std::type_info *bound = nullptr;               // R-KEPT: the entry of a nanocct::Kept<T> -- the type Python sees, T
    PyObject *(*find)(void *stored) = nullptr;           // the existing Python object of `stored` (nb::find), new reference or null
};

// ONE object of type T for all extension modules. Every toolkit is its own shared library, and an inline function's
// static is one per library there (hidden visibility): a type registered by _TKMath (NCollection_HArray1<int>) was
// unknown to the caster of every other toolkit, so it was refused where a handle<Standard_Transient> is expected
// (2026-09-30). The first module to need it creates the object and leaves it on the `nanocct` package as a capsule
// (attribute `attr`); every module finds the same one there. All modules are built by the same compiler with the same
// flags, so the layout agrees; the object is never freed (the modules are never unloaded). The first call of each
// module needs the GIL (it imports `nanocct`); later calls only read the cached pointer.
template <typename T> T &nanocct_shared(const char *attr, const char *capsule) {
    static T *obj = nullptr;
    if (obj == nullptr) {
        nb::object pkg = nb::module_::import_("nanocct");
        if (nb::hasattr(pkg, attr))
            obj = static_cast<T *>(PyCapsule_GetPointer(pkg.attr(attr).ptr(), capsule));
        else {
            obj = new T();
            pkg.attr(attr) = nb::steal(PyCapsule_New(obj, capsule, nullptr));
        }
    }
    return *obj;
}
// ONE MI registry for all extension modules (nanocct_shared). Called with the GIL held (module init, the casters).
struct mi_registry {
    std::unordered_map<std::string, mi_entry> by_name;   // key: typeid(S).name()
    std::vector<mi_entry> list;
};
inline mi_registry &nanocct_mi_registry() { return nanocct_shared<mi_registry>("_mi_registry", "nanocct._mi_registry"); }
inline std::unordered_map<std::string, mi_entry> &nanocct_mi_by_name() { return nanocct_mi_registry().by_name; }
inline std::vector<mi_entry> &nanocct_mi_list() { return nanocct_mi_registry().list; }

template <typename S> void nanocct_register_mi(nb::handle py_type) {
    using B = typename mi_traits<S>::base;
    mi_entry e{py_type.ptr(),
               [](void *stored) -> Standard_Transient * { return static_cast<S *>(static_cast<B *>(stored)); },
               [](Standard_Transient *t) -> void * { return static_cast<B *>(static_cast<S *>(dynamic_cast<void *>(t))); }};
    // looked up as B at the stored address, where nanobind registered the object (B need not be at offset 0 of S:
    // NCollection_Shared<T>); its dynamic type S matches the existing wrapper
    e.find = [](void *stored) -> PyObject * { return nb::find(*static_cast<B *>(stored)).release().ptr(); };
    nanocct_mi_by_name()[typeid(S).name()] = e;
    nanocct_mi_list().push_back(e);
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
// TKernel translator finally falls back to nanocct.Standard.Standard_Failure.
inline std::unordered_map<std::string, PyObject *> &nanocct_exception_map() {
    static std::unordered_map<std::string, PyObject *> map;
    return map;
}

template <typename T> void nanocct_register_exception(nb::handle py_type) {
    nanocct_exception_map()[typeid(T).name()] = py_type.ptr();
}

// scope: the package module or a namespace submodule
inline nb::object nanocct_new_exception(nb::handle m, const char *name, const char *doc, PyObject *base) {
    std::string qualified = nb::borrow<nb::str>(m.attr("__name__")).c_str();
    qualified += ".";
    qualified += name;
    nb::object type = nb::steal(PyErr_NewExceptionWithDoc(qualified.c_str(), doc, base, nullptr));
    m.attr(name) = type;
    return type;
}
