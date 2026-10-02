// Shared by every generated nanocct translation unit.
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
#include <functional>
#include <bitset>
#include <tuple>
#include <type_traits>

#include <atomic>
#include <mutex>
#include <sstream>
#include <string>
#include <typeinfo>
#include <unordered_map>
#include <utility>
#include <vector>

#include <Standard_Failure.hxx>
#include <Standard_Handle.hxx>
#include <Standard_Transient.hxx>
#include <NCollection_Handle.hxx>

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

// ---------------------------------------------------------------------------------------------
// R-OWNER (Design.md 6): the owner of an OCAF object, known by its type. A TDF_Label and a TDF_Attribute point into the
// TDF_LabelNode tree a TDF_Data owns; the root of a document's data carries a TDocStd_Owner whose raw pointer is the
// TDocStd_Document. owners<T>::keep(nurse, value) keeps the TDF_Data and the TDocStd_Document of `value` alive as long as
// the Python object `nurse` -- for a handle, of its object; for a container, of every element. The definitions need the
// OCAF headers: ocaf_owners is complete only in nanocct_ocaf.h, which the generator includes where the rule applies, so a
// file that applies it without that header does not compile. Every other type: active = false, no code.
class TDF_Label;
class TDF_Data;
class TDF_Attribute;
template <class T> class NCollection_Array1;
template <class T> class NCollection_HArray1;
template <class T> class NCollection_Sequence;
template <class T> class NCollection_HSequence;
template <class T> class NCollection_List;
template <class K, class H> class NCollection_Map;
template <class K, class H> class NCollection_IndexedMap;
template <class K, class V, class H> class NCollection_DataMap;
template <class K, class V, class H> class NCollection_IndexedDataMap;
template <class K1, class K2, class H1, class H2> class NCollection_DoubleMap;

namespace nanocct {
struct ocaf_owners;

template <typename T, typename = void> struct owners {
    static constexpr bool active = false;
    static void keep(PyObject *, const T &) {}
};
template <> struct owners<TDF_Label> {
    static constexpr bool active = true;
    template <typename O = ocaf_owners> static void keep(PyObject *nurse, const TDF_Label &v) { O::label(nurse, v); }
};
template <typename T>
struct owners<T, std::enable_if_t<std::disjunction_v<std::is_same<T, TDF_Data>, std::is_base_of<TDF_Attribute, T>>>> {
    static constexpr bool active = true;
    template <typename O = ocaf_owners> static void keep(PyObject *nurse, const T &v) { O::transient(nurse, v); }
};
template <typename T> struct owners<opencascade::handle<T>> {
    static constexpr bool active = owners<T>::active;
    static void keep(PyObject *nurse, const opencascade::handle<T> &h) {
        if constexpr (active)
            if (!h.IsNull())
                owners<T>::keep(nurse, *h);
    }
};
template <typename E> struct owners<NCollection_Array1<E>> {
    static constexpr bool active = owners<E>::active;
    static void keep(PyObject *nurse, const NCollection_Array1<E> &c) {
        if constexpr (active)
            for (int i = c.Lower(); i <= c.Upper(); ++i)
                owners<E>::keep(nurse, c.Value(i));
    }
};
template <typename E> struct owners<NCollection_HArray1<E>> : owners<NCollection_Array1<E>> {};
template <typename E> struct owners<NCollection_Sequence<E>> {
    static constexpr bool active = owners<E>::active;
    static void keep(PyObject *nurse, const NCollection_Sequence<E> &c) {
        if constexpr (active)
            for (int i = c.Lower(); i <= c.Upper(); ++i)
                owners<E>::keep(nurse, c.Value(i));
    }
};
template <typename E> struct owners<NCollection_HSequence<E>> : owners<NCollection_Sequence<E>> {};
template <typename E> struct owners<NCollection_List<E>> {
    static constexpr bool active = owners<E>::active;
    static void keep(PyObject *nurse, const NCollection_List<E> &c) {
        if constexpr (active)
            for (typename NCollection_List<E>::Iterator it(c); it.More(); it.Next())
                owners<E>::keep(nurse, it.Value());
    }
};
template <typename K, typename H> struct owners<NCollection_Map<K, H>> {
    static constexpr bool active = owners<K>::active;
    static void keep(PyObject *nurse, const NCollection_Map<K, H> &c) {
        if constexpr (active)
            for (typename NCollection_Map<K, H>::Iterator it(c); it.More(); it.Next())
                owners<K>::keep(nurse, it.Key());
    }
};
template <typename K, typename H> struct owners<NCollection_IndexedMap<K, H>> {
    static constexpr bool active = owners<K>::active;
    static void keep(PyObject *nurse, const NCollection_IndexedMap<K, H> &c) {
        if constexpr (active)
            for (int i = 1; i <= c.Extent(); ++i)
                owners<K>::keep(nurse, c.FindKey(i));
    }
};
template <typename K, typename V, typename H> struct owners<NCollection_DataMap<K, V, H>> {
    static constexpr bool active = owners<K>::active || owners<V>::active;
    static void keep(PyObject *nurse, const NCollection_DataMap<K, V, H> &c) {
        if constexpr (active)
            for (typename NCollection_DataMap<K, V, H>::Iterator it(c); it.More(); it.Next()) {
                owners<K>::keep(nurse, it.Key());
                owners<V>::keep(nurse, it.Value());
            }
    }
};
template <typename K, typename V, typename H> struct owners<NCollection_IndexedDataMap<K, V, H>> {
    static constexpr bool active = owners<K>::active || owners<V>::active;
    static void keep(PyObject *nurse, const NCollection_IndexedDataMap<K, V, H> &c) {
        if constexpr (active)
            for (int i = 1; i <= c.Extent(); ++i) {
                owners<K>::keep(nurse, c.FindKey(i));
                owners<V>::keep(nurse, c.FindFromIndex(i));
            }
    }
};
template <typename K1, typename K2, typename H1, typename H2> struct owners<NCollection_DoubleMap<K1, K2, H1, H2>> {
    static constexpr bool active = owners<K1>::active || owners<K2>::active;
    static void keep(PyObject *nurse, const NCollection_DoubleMap<K1, K2, H1, H2> &c) {
        if constexpr (active)
            for (typename NCollection_DoubleMap<K1, K2, H1, H2>::Iterator it(c); it.More(); it.Next()) {
                owners<K1>::keep(nurse, it.Key1());
                owners<K2>::keep(nurse, it.Key2());
            }
    }
};

// the type whose owners a result or argument of C++ type R has: references, pointers and handles looked through
template <typename T> struct owner_target { using type = T; };
template <typename T> struct owner_target<opencascade::handle<T>> { using type = T; };
template <typename R>
using owner_target_t = typename owner_target<std::remove_cv_t<std::remove_pointer_t<std::remove_cv_t<std::remove_reference_t<R>>>>>::type;

// R-METHOD-KEEP: a method argument the object can keep the address of (Extrema_ExtPS::Initialize(S, ...) stores &S) lives
// in a slot of the object -- one slot per (declaration, parameter). A call stores its argument there and releases what the
// slot held, so `for s in surfaces: ext.Initialize(s, ...)` keeps one surface, not all of them (nb::keep_alive would keep
// every one, and its duplicate check walks the whole list on each call). The slots of all objects are in ONE table for all
// extension modules (nanocct_shared: a copy made by one toolkit must see the slots a method of another toolkit filled,
// R-COPY), found by the object's PyObject*, created on first use; the entry, and with it the arguments, goes through
// nb::keep_alive_cb, which nanobind runs after the object's C++ destructor (that destructor still sees its arguments). A
// slot is named by the address of a variable of the generated file (slot_tag<Tag>, Tag: the file's own type) and the
// slot's number in that file. A mutex protects the table, not the GIL (free-threading).
using slot_key = std::pair<const void *, size_t>;
struct slot_registry {
    std::mutex mutex;
    std::unordered_map<PyObject *, std::vector<std::pair<slot_key, PyObject *>>> slots;   // owner -> (slot, argument)
};
inline slot_registry &slots() { return nanocct_shared<slot_registry>("_slot_registry", "nanocct._slot_registry"); }
template <typename Tag> struct slot_tag {
    static inline char id = 0;                            // not const: never merged with another file's
};
inline void release_slots(void *owner) noexcept {
    std::vector<std::pair<slot_key, PyObject *>> held;
    {
        slot_registry &reg = slots();
        std::lock_guard<std::mutex> lock(reg.mutex);
        auto it = reg.slots.find(static_cast<PyObject *>(owner));
        if (it != reg.slots.end()) {
            held.swap(it->second);
            reg.slots.erase(it);
        }
    }
    for (auto &entry : held)                              // outside the lock: an argument's release can run Python code
        Py_DECREF(entry.second);
}
// R-COPY / R-RESULT-KEEP: the nurse may hold pointers copied out of the patient -- a copy of it, a view it produced --
// and those may point into what the patient's slots hold now. A slot drops its argument when the patient stores the next
// one (ext.Initialize(c2) after cp = Extrema_ExtCC2d(ext)), so keeping the patient is not enough: the nurse keeps the
// arguments themselves (accumulating, nb::keep_alive_obj; never itself).
inline void keep_slots_of(PyObject *nurse, PyObject *patient) {
    std::vector<PyObject *> held;
    {
        slot_registry &reg = slots();
        std::lock_guard<std::mutex> lock(reg.mutex);
        auto it = reg.slots.find(patient);
        if (it == reg.slots.end())
            return;
        for (auto &entry : it->second) {
            Py_INCREF(entry.second);
            held.push_back(entry.second);
        }
    }
    for (PyObject *argument : held) {
        if (argument != nurse)
            nb::keep_alive_obj(nurse, argument);
        Py_DECREF(argument);
    }
}
// keep_alive_obj and keep_slots_of together: the nurse may point into the patient and into what the patient points to
inline void keep_view_of(PyObject *nurse, PyObject *patient) {
    if (patient == nurse)
        return;
    nb::keep_alive_obj(nurse, patient);
    keep_slots_of(nurse, patient);
}
// R-COPY: keep_view_of as a call policy, numbered like nb::keep_alive (0 is the result, 1 self, nb::new_'s arguments count
// from 2): a copy keeps its original, a constructor an argument it copies pointers out of (TDF_ChildIterator(label)). A
// None nurse (nb::new_'s no-op __init__) keeps nothing.
template <size_t Nurse, size_t Patient> struct keep_view_arg {
    static void precall(PyObject **, size_t, nb::detail::cleanup_list *) {}
    static void postcall(PyObject **args, size_t, nb::handle ret) {
        PyObject *nurse = Nurse == 0 ? ret.ptr() : args[Nurse - 1];
        if (nurse != nullptr && nurse != Py_None)
            keep_view_of(nurse, args[Patient - 1]);
    }
};
} // namespace nanocct

// R-ITER (Design.md 2c): a class with More()/Next() and a parameterless Value() or Current() is its own Python
// iterator, like a file object: __iter__ returns self, __next__ yields the current element and advances. The element
// is copied out before Next() (a const reference from Value() would dangle afterwards).
// Constructors of a class-template instantiation whose abstractness only the compiler can see (BVH_PrimitiveSet<double, 3>
// through the pure virtuals of BVH_Set): the generic lambda's body is instantiated only when the class is concrete (R-TEMPLATE-BASE).
template <typename T, typename F> void nanocct_if_concrete(nb::class_<T> cls, F f) {
    if constexpr (!std::is_abstract_v<T>)
        f(cls);
}

// R-ITER through nb::make_iterator, like the containers: a hand-written __next__ ended every loop with a thrown
// nb::stop_iteration, a C++ exception that cost ~8 us per loop however short (2026-09-27: a TopExp_Explorer over
// 6 faces took 8.5 us against 0.47 us for a More()/Next() loop). make_iterator ends without one. The cursor
// advances the object itself, so it is exhausted afterwards, like a file; the element is copied out before Next().
// View (R-RESULT-KEEP): the element is a class that holds pointers, so each one keeps the iterated object alive (a
// TDF_Label from TDF_ChildIterator); an element with OCAF owners keeps those too (R-OWNER).
template <typename T, bool View, typename Get> struct nanocct_iter_cursor {
    T *obj;                                   // nullptr: the end sentinel
    Get get;
    PyObject *owner;                          // View: the iterated object (borrowed; the iterator keeps it alive)
    bool done() const { return obj == nullptr || !obj->More(); }
    bool operator==(const nanocct_iter_cursor &o) const { return done() == o.done(); }
    bool operator!=(const nanocct_iter_cursor &o) const { return !(*this == o); }
    nanocct_iter_cursor &operator++() { obj->Next(); return *this; }
    auto operator*() const {                  // by value: Current() may be a reference that Next() changes
        using E = std::remove_cv_t<std::remove_reference_t<decltype(get(*obj))>>;
        if constexpr (View || nanocct::owners<E>::active) {
            E value = get(*obj);
            nb::object element = nb::cast(value, nb::rv_policy::copy);
            if constexpr (View)
                nanocct::keep_view_of(element.ptr(), owner);
            if constexpr (nanocct::owners<E>::active)
                nanocct::owners<E>::keep(element.ptr(), value);
            return nb::typed<nb::object, E>(std::move(element));
        } else {
            return get(*obj);
        }
    }
};

template <typename T, bool View = false, typename Get> void nanocct_def_iter(nb::class_<T> cls, Get get) {
    cls.def("__iter__", [get](T &self) {
        using Cursor = nanocct_iter_cursor<T, View, Get>;
        nb::object owner;
        if constexpr (View)
            owner = nb::find(self);
        return nb::make_iterator<nb::rv_policy::move>(nb::type<T>(), "iterator", Cursor{&self, get, owner.ptr()},
                                                      Cursor{nullptr, get, nullptr});
    }, nb::keep_alive<0, 1>(),
    "Python addition: iterate with More()/Next(), yielding Value() (or Current()); the iterator advances the object "
    "itself, so it is exhausted afterwards.");
}

// The implicit default constructor of a class that declares none: bound only when it exists (a reference
// member or a non-default-constructible member deletes it; the header does not say so).
template <typename T> void nanocct_implicit_default_ctor(nb::class_<T> cls) {
    if constexpr (std::is_default_constructible_v<T>) {
        if constexpr (std::is_base_of_v<Standard_Transient, T>)
            cls.def(nb::new_([]() { return opencascade::handle<T>(new T()); }));
        else
            cls.def(nb::init<>());
    }
}

// The implicit copy constructor (none declared by the class): bound when it exists (deleted for classes with a
// reference or non-copyable member) and the generator found it safe (R-COPY: never for a class whose destructor may free
// a pointer the copy would share). Sub-class arguments convert implicitly, as in C++ (TopoDS_Shape(aVertex)).
// View (R-COPY): the class holds pointers, which the copy shares, so the copy keeps the original alive and what the
// original's slots hold now (keep_view_arg<0, 2> through nb::new_, as for R-CTOR-KEEP).
template <typename T, bool View = false> void nanocct_implicit_copy_ctor(nb::class_<T> cls) {
    if constexpr (std::is_copy_constructible_v<T>) {
        if constexpr (std::is_base_of_v<Standard_Transient, T> && View)
            cls.def(nb::new_([](const T &other) { return opencascade::handle<T>(new T(other)); }), nb::arg("theOther"),
                    nb::call_policy<nanocct::keep_view_arg<0, 2>>());
        else if constexpr (std::is_base_of_v<Standard_Transient, T>)
            cls.def(nb::new_([](const T &other) { return opencascade::handle<T>(new T(other)); }), nb::arg("theOther"));
        else if constexpr (View)
            cls.def(nb::init<const T &>(), nb::arg("theOther"), nb::call_policy<nanocct::keep_view_arg<1, 2>>());
        else
            cls.def(nb::init<const T &>(), nb::arg("theOther"));
    }
}

// operator To() const of From: To gets a constructor from From (To(aFrom) in Python) and, unless the operator is
// explicit, the implicit conversion C++ has (a From passes where a To is expected). From is taken by non-const
// reference: some operators are not const (Message_Msg).
template <typename From, typename To> void nanocct_conversion(nb::handle to_type, bool implicit) {
    auto cls = nb::borrow<nb::class_<To>>(to_type);
    if constexpr (std::is_base_of_v<Standard_Transient, To>)
        cls.def(nb::new_([](From &from) { return opencascade::handle<To>(new To(static_cast<To>(from))); }), nb::arg("theFrom"));
    else
        cls.def("__init__", [](To *self, From &from) { new (self) To(static_cast<To>(from)); }, nb::arg("theFrom"));
    if (implicit)
        nb::implicitly_convertible<From, To>();
}

// operator opencascade::handle<To>() const of From: the handle's object becomes the result of To(aFrom)
template <typename From, typename To> void nanocct_conversion_handle(nb::handle to_type, bool implicit) {
    auto cls = nb::borrow<nb::class_<To>>(to_type);
    cls.def(nb::new_([](From &from) { return static_cast<opencascade::handle<To>>(from); }), nb::arg("theFrom"));
    if (implicit)
        nb::implicitly_convertible<From, To>();
}

// opencascade::handle<T> or not (a field of handle type takes None through its setter, R-HANDLE).
template <typename> struct nanocct_is_handle : std::false_type {};
template <typename T> struct nanocct_is_handle<opencascade::handle<T>> : std::true_type {};

// Public data member: read/write when its type can be assigned to (a member with a deleted copy assignment, e.g. of
// type BRepGraphInc_Storage, or a const member is read-only). Decided at compile time, the header does not say.
template <typename C, typename T, typename D, typename... Extra>
void nanocct_def_field(nb::class_<C> cls, const char *name, D T::*p, const Extra &...extra) {
    if constexpr (nanocct_is_handle<D>::value && !std::is_const_v<D>)
        // R-HANDLE: a null handle reads as None, so None must be assignable too (a plain def_rw setter refused it)
        cls.def_rw(name, p, nb::for_setter(nb::arg("value").none()), extra...);
    else if constexpr (std::is_copy_assignable_v<D> && !std::is_const_v<D>)
        cls.def_rw(name, p, extra...);
    else
        cls.def_ro(name, p, extra...);
}

// R-FIELD: a raw pointer member (a class, or a `const char*` / `const char16_t*` string) is read-only -- a setter would
// store the address of a Python object nothing keeps alive -- and reads as a copy of what it points to: a str for a
// string, an independent object for a class (the generator binds none whose copy would share what its destructor frees),
// None for a null pointer.
template <typename C, typename T, typename D, typename... Extra>
void nanocct_def_pointer_field(nb::class_<C> cls, const char *name, D T::*p, const Extra &...extra) {
    static_assert(std::is_pointer_v<D>, "R-FIELD: nanocct_def_pointer_field takes a raw pointer member");
    using P = std::remove_cv_t<std::remove_pointer_t<D>>;
    if constexpr (std::is_same_v<P, char> || std::is_same_v<P, char16_t>) {
        cls.def_prop_ro(name, [p](const C &self) -> const P * { return self.*p; }, extra...);
    } else {
        static_assert(std::is_copy_constructible_v<P>, "R-FIELD: the pointee of a bound pointer member must be copyable");
        cls.def_prop_ro(name, [p](const C &self) -> std::optional<P> {
            if (self.*p == nullptr)
                return std::nullopt;
            return *(self.*p);
        }, extra...);
    }
}

// fallback: the Python type for Standard_Failure, or nullptr to pass unknown exceptions on
inline void nanocct_install_exception_translator(PyObject *fallback) {
    nb::register_exception_translator(
        [](const std::exception_ptr &p, void *payload) {
            try {
                std::rethrow_exception(p);
            } catch (const Standard_Failure &e) {
                auto &map = nanocct_exception_map();
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
inline nb::str nanocct_stream_text(const std::ostringstream &stream) {
    const std::string text = stream.str();
    return nb::steal<nb::str>(PyUnicode_DecodeUTF8(text.data(), static_cast<Py_ssize_t>(text.size()), "surrogateescape"));
}

// The same for the binary formats (the BinTools package, overrides.toml [stream] binary_packages): bytes.
inline nb::bytes nanocct_stream_bytes(const std::ostringstream &stream) {
    const std::string data = stream.str();
    return nb::bytes(data.data(), data.size());
}

// A std::istream& / std::stringstream parameter (BRepTools::Read, InitFromJson): the text of a Python file-like object
// (anything with read(): io.StringIO, an open text file). A str is deliberately not accepted -- it would collide with
// the file-path overloads -- so a non-file-like argument falls through to the next overload. Typed typing.TextIO.
namespace nanocct {
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
// garbage collector cannot see, and would never be freed ("nanobind: leaked instances").
struct KeepOwnerUnlessSelf {
    static void precall(PyObject **, size_t, nb::detail::cleanup_list *) {}
    static void postcall(PyObject **args, size_t, PyObject *&ret) {
        if (ret != nullptr && ret != args[0])
            nb::keep_alive_obj(ret, args[0]);   // the result (nurse) keeps self (patient) alive
    }
};
// R-METHOD-KEEP: a method argument the object can keep the address of (Extrema_ExtPS::Initialize(S, ...) stores &S) lives
// in a slot of the object -- one slot per (declaration, parameter). A call stores its argument there and releases what the
// slot held, so `for s in surfaces: ext.Initialize(s, ...)` keeps one surface, not all of them (nb::keep_alive would keep
// every one, and its duplicate check walks the whole list on each call). The slots of an object are a list in a table per
// generated translation unit (Tag, the file's own type), found by the object's PyObject*, created on first use; the entry,
// and with it the arguments, goes through nb::keep_alive_cb, which nanobind runs after the object's C++ destructor (that
// destructor still sees its arguments). A mutex protects the table, not the GIL (free-threading).
// R-METHOD-KEEP (the table: nanocct::slots above). Patient: the argument's position as in nb::keep_alive (1 is self);
// Slot: the declaration and parameter, numbered per file. An object passed to itself is not kept by itself (a reference
// the garbage collector cannot see).
template <typename Tag, size_t Patient, size_t Slot> struct keep_slot {
    static void precall(PyObject **, size_t, nb::detail::cleanup_list *) {}
    static void postcall(PyObject **args, size_t, nb::handle) {
        PyObject *owner = args[0];
        PyObject *argument = args[Patient - 1];          // the converted object when an implicit conversion took place
        if (argument == owner)
            return;
        PyObject *previous = nullptr;
        Py_INCREF(argument);
        {
            slot_registry &reg = slots();
            std::lock_guard<std::mutex> lock(reg.mutex);
            auto [it, created] = reg.slots.try_emplace(owner);
            if (created)
                nb::keep_alive_cb(owner, owner, &release_slots);
            const slot_key key{&slot_tag<Tag>::id, Slot};
            auto &held = it->second;
            auto entry = std::find_if(held.begin(), held.end(), [&](const auto &e) { return e.first == key; });
            if (entry != held.end())
                previous = std::exchange(entry->second, argument);
            else
                held.emplace_back(key, argument);
        }
        Py_XDECREF(previous);                             // outside the lock: an argument's release can run Python code
    }
};
// R-RESULT-KEEP / R-OWNER (Design.md 6): a result, or an argument the call writes into, of a class that holds pointers
// keeps alive what it may point into. R: its C++ type; Owned: the generator found that R's OCAF owners are known -- checked
// against nanocct::owners, so the two cannot disagree silently; Nurse: 0 = the result, k = argument k (1 is self); Elem:
// the result's position in a returned tuple (out-parameters), -1 if none; Patients: the arguments it may point into.
// keep_alive_obj on a fresh result keeps one call's arguments; an argument written into keeps them for good, nanobind
// skipping duplicates. The nurse also keeps what the patients' slots hold now (keep_slots_of: it may point there too).
// A nurse that is also a patient (a method returning *this) keeps nothing of itself. A `const T&` of
// a class that cannot be copied comes back by reference (cref_policy) and may be an object Python already has -- one of the
// patients, even (VrmlData_Node::Scene() of the scene the node keeps): it keeps no producers, which could make a cycle.
template <typename R, bool Owned, size_t Nurse, int Elem, size_t... Patients> struct keep_view {
    using T = owner_target_t<R>;
    static_assert(owners<T>::active == Owned, "R-OWNER: the generator and nanocct::owners disagree about this type");
    static constexpr bool keeps_producers = Nurse != 0 || !std::is_lvalue_reference_v<R>
                                            || std::is_copy_constructible_v<std::remove_cv_t<std::remove_reference_t<R>>>;
    static void precall(PyObject **, size_t, nb::detail::cleanup_list *) {}
    static void postcall(PyObject **args, size_t, nb::handle ret) {
        PyObject *nurse = Nurse == 0 ? ret.ptr() : args[Nurse - 1];
        if constexpr (Elem >= 0)
            nurse = PyTuple_GetItem(nurse, Elem);       // borrowed
        if (nurse == nullptr || nurse == Py_None)
            return;
        if constexpr (keeps_producers)
            (keep_view_of(nurse, args[Patients - 1]), ...);
        if constexpr (Owned)
            owners<T>::keep(nurse, nb::cast<const T &>(nb::handle(nurse)));
    }
};
// R-RESULT: a `const T&` result is copied (nanobind's default) -- unless T cannot be copied (a deleted copy constructor
// in either form, `T(const T&)` or `T(T&)`, or a member that cannot be copied: Extrema_ExtCC, Extrema_ExtPS), where
// nanobind's copy aborts the process ("Critical nanobind error"). Such a result is handed out by reference instead:
// tied to its owner for a method (reference_internal), plain for a static method or free function (no owner).
// Decided by the compiler, so a class's copyability never has to be guessed from its header. nanobind 3.1 takes the
// policy as a compile-time tag type (nb_attr.h: a runtime rv_policy value is rejected), hence a type: cref_policy<R, O>{}.
template <typename R, bool HasOwner>
using cref_policy = nb::rv_policy::policy_tag<
    std::is_copy_constructible_v<std::remove_cv_t<std::remove_reference_t<R>>> ? nb::rv_policy::copy_v
    : HasOwner ? nb::rv_policy::reference_internal_v : nb::rv_policy::reference_v>;

// R-VIEW-GUARD (Design.md 6): an NCollection container refuses a call that would invalidate one of its live views, with
// BufferError -- Python's own rule for bytearray, which refuses to resize while a buffer is exported. A view is anything
// that points into a container's storage: an element reference (ChangeValue, a List's Append result, a map's ChangeFind or
// ChangeSeek, ...), a numpy array over it, an iterator (OCCT's Iterator classes and the Python ones of __iter__). Which call
// invalidates which kind of view is OCCT's container code, read once (Design.md 6, the R-VIEW-GUARD table): the binder
// (nanocct_ncollection.h) checks its own members, nanocct::guarded checks every generated function that takes a container
// by non-const reference or pointer -- OCCT may change it -- and a container data member checks before it is assigned.
// Views are counted per C++ container address, so two Python wrappers of one container agree, in ONE table for all
// extension modules (nanocct_shared): a generated function of any toolkit sees the views another toolkit's binder handed
// out. A view's count goes when the view dies (nb::keep_alive_cb; a numpy array: its owner capsule). A mutex protects the
// table, not the GIL (free-threading); `live` counts all views of all containers, so a call made while nothing is viewed
// anywhere costs one atomic load.
enum class view_kind : size_t { element = 0, iterator = 1 };
struct view_registry {
    struct counts { size_t n[2] = {0, 0}; };              // by view_kind
    struct view { const void *container; view_kind kind; };
    std::mutex mutex;
    std::atomic<size_t> live{0};
    std::unordered_map<const void *, counts> containers;  // container -> its live views
    std::unordered_map<PyObject *, view> views;          // view object -> what it views (an iterator can be re-initialised)
};
inline view_registry &view_table() { return nanocct_shared<view_registry>("_view_registry", "nanocct._view_registry"); }
// both under the mutex
inline void view_link(view_registry &reg, const void *container, view_kind kind) {
    reg.containers[container].n[(size_t) kind] += 1;
    reg.live.fetch_add(1);
}
inline void view_unlink(view_registry &reg, const void *container, view_kind kind) {
    auto it = reg.containers.find(container);
    if (it == reg.containers.end())
        return;
    it->second.n[(size_t) kind] -= 1;
    if (it->second.n[0] == 0 && it->second.n[1] == 0)
        reg.containers.erase(it);
    reg.live.fetch_sub(1);
}
inline void release_view(void *view) noexcept {
    view_registry &reg = view_table();
    std::lock_guard<std::mutex> lock(reg.mutex);
    auto it = reg.views.find(static_cast<PyObject *>(view));
    if (it == reg.views.end())
        return;
    view_unlink(reg, it->second.container, it->second.kind);
    reg.views.erase(it);
}
// `view` (a nanobind instance) points into the container at `container` until it dies. The same object again (nanobind
// returns the wrapper it already has for an address) counts once; an iterator initialised on another container moves.
inline void add_view(nb::handle view, const void *container, view_kind kind) {
    if (!view.is_valid() || view.is_none())
        return;
    view_registry &reg = view_table();
    {
        std::lock_guard<std::mutex> lock(reg.mutex);
        auto [it, fresh] = reg.views.try_emplace(view.ptr(), view_registry::view{container, kind});
        if (!fresh) {
            if (it->second.container != container || it->second.kind != kind) {
                view_unlink(reg, it->second.container, it->second.kind);
                it->second = view_registry::view{container, kind};
                view_link(reg, container, kind);
            }
            return;
        }
        view_link(reg, container, kind);
    }
    nb::keep_alive_cb(view, view.ptr(), &release_view);
}
// the container an iterator object was registered for, nullptr if none (a default-constructed Iterator)
inline const void *viewed_container(PyObject *iterator) {
    view_registry &reg = view_table();
    std::lock_guard<std::mutex> lock(reg.mutex);
    auto it = reg.views.find(iterator);
    return it == reg.views.end() ? nullptr : it->second.container;
}
// numpy: the owner of an array over the container's storage -- counts one element view and keeps the container's Python
// object alive until the array (and every array derived from it) is gone. nanobind refuses reference_internal for an
// ndarray that has an owner (nb_ndarray.cpp, ndarray_export), so the owner does both.
struct exported_view { const void *container; PyObject *owner; };
inline nb::capsule export_view(const void *container, nb::handle owner) {
    view_registry &reg = view_table();
    {
        std::lock_guard<std::mutex> lock(reg.mutex);
        view_link(reg, container, view_kind::element);
    }
    auto *payload = new exported_view{container, owner.inc_ref().ptr()};
    return nb::capsule(payload, [](void *p) noexcept {
        auto *e = static_cast<exported_view *>(p);
        {
            view_registry &r = view_table();
            std::lock_guard<std::mutex> lock(r.mutex);
            view_unlink(r, e->container, view_kind::element);
        }
        Py_DECREF(e->owner);                             // outside the lock: the release can run Python code
        delete e;
    });
}
// the live views of a container: all kinds, or iterators only; `except` (an iterator the call itself goes through, as in
// List.Remove(it)) is not counted
inline size_t live_views(const void *container, bool iterators_only, PyObject *except = nullptr) {
    view_registry &reg = view_table();
    if (reg.live.load() == 0)
        return 0;
    std::lock_guard<std::mutex> lock(reg.mutex);
    auto it = reg.containers.find(container);
    if (it == reg.containers.end())
        return 0;
    size_t n = it->second.n[(size_t) view_kind::iterator] + (iterators_only ? 0 : it->second.n[(size_t) view_kind::element]);
    if (except != nullptr) {
        auto v = reg.views.find(except);
        if (v != reg.views.end() && v->second.container == container && (!iterators_only || v->second.kind == view_kind::iterator))
            n -= 1;
    }
    return n;
}
[[noreturn]] inline void raise_viewed(size_t n, const std::string &what) {
    const std::string msg = what + ": " + std::to_string(n) + " live view(s) of this container (element references, "
        "iterators or numpy arrays) would be invalidated by this call; release them first (BufferError, as bytearray "
        "raises while a buffer is exported)";
    throw nb::buffer_error(msg.c_str());
}
// BufferError when the container has live views the call would invalidate. what: the member, for the message.
inline void refuse_if_viewed(const void *container, const char *what, PyObject *except = nullptr) {
    const size_t n = live_views(container, false, except);
    if (n != 0)
        raise_viewed(n, what);
}
// a hashed map's table can grow on insert: its iterators (not its element references) would be invalidated
inline void refuse_if_iterated(const void *container, const char *what) {
    const size_t n = live_views(container, true);
    if (n != 0) {
        const std::string msg = std::string(what) + ": " + std::to_string(n) + " live iterator(s) of this map would be "
            "invalidated by this call (the table may grow); finish or release them first (BufferError)";
        throw nb::buffer_error(msg.c_str());
    }
}
// call policies: the result (0) or argument Self (1-based) becomes a view of the container that is argument Container
// (1-based; 1 is self, as in nb::keep_alive). In a constructor's postcall args[0] is the new object; nb::new_'s arguments
// count from 2, its result is the object. A None argument (a null pointer) is no container.
template <view_kind Kind, size_t Self = 0, size_t Container = 1> struct view_of {
    static void precall(PyObject **, size_t, nb::detail::cleanup_list *) {}
    static void postcall(PyObject **args, size_t, nb::handle ret) {
        nb::handle view = Self == 0 ? ret : nb::handle(args[Self - 1]);
        PyObject *container = args[Container - 1];
        if (view.is_valid() && container != nullptr && container != Py_None)
            add_view(view, nb::inst_ptr<void>(container), Kind);
    }
};
// an element reference handed out by an iterator (Iterator.ChangeValue) is a view of the iterator's container
struct view_through_iterator {
    static void precall(PyObject **, size_t, nb::detail::cleanup_list *) {}
    static void postcall(PyObject **args, size_t, nb::handle ret) {
        const void *container = viewed_container(args[0]);
        if (ret.is_valid() && container != nullptr)
            add_view(ret, container, view_kind::element);
    }
};

// R-VIEW-GUARD for generated code: the call refuses when a container argument it may change has live views. The check runs
// inside the call, after nanobind converted the arguments: a call policy's precall runs before the conversion, and raising
// there pre-empted another overload taking the same container const (PLib::SetPoles: (const Array1<gp_Pnt>&,
// Array1<double>&) and (..., const Array1<double>&, Array1<double>&)). K: the 0-based C++ parameter positions (self not
// counted). A null pointer argument has nothing to check.
template <typename A> const void *container_address(A &argument) {
    if constexpr (std::is_pointer_v<A>)
        return static_cast<const void *>(argument);
    else
        return static_cast<const void *>(&argument);
}
// position: the argument's 1-based position in the Python call, self not counted (for the message)
template <typename A> void refuse_viewed_argument(A &argument, size_t position) {
    const void *container = container_address(argument);
    if (container == nullptr)
        return;
    const size_t n = live_views(container, false);
    if (n != 0)
        raise_viewed(n, "argument " + std::to_string(position));
}
template <size_t... K, typename... A> void refuse_viewed_arguments(A &...arguments) {
    if (view_table().live.load() == 0)
        return;
    auto all = std::forward_as_tuple(arguments...);
    (refuse_viewed_argument(std::get<K>(all), K + 1), ...);
}
// the bound function with the same signature (a member function takes self first, as nanobind's own wrapper does):
// guarded<static_cast<Sig>(&C::Method), K...>::call. Dispatch on the exact function type: deducing from the value made a
// noexcept function match both the plain and the noexcept specialisation (clang: ambiguous partial specialisations).
template <typename T, T F, size_t... K> struct guarded_impl;
template <typename R, typename... A, R (*F)(A...), size_t... K> struct guarded_impl<R (*)(A...), F, K...> {
    static R call(A... a) { refuse_viewed_arguments<K...>(a...); return F(std::forward<A>(a)...); }
};
template <typename R, typename... A, R (*F)(A...) noexcept, size_t... K> struct guarded_impl<R (*)(A...) noexcept, F, K...> {
    static R call(A... a) { refuse_viewed_arguments<K...>(a...); return F(std::forward<A>(a)...); }
};
template <typename R, typename C, typename... A, R (C::*F)(A...), size_t... K> struct guarded_impl<R (C::*)(A...), F, K...> {
    static R call(C &self, A... a) { refuse_viewed_arguments<K...>(a...); return (self.*F)(std::forward<A>(a)...); }
};
template <typename R, typename C, typename... A, R (C::*F)(A...) const, size_t... K> struct guarded_impl<R (C::*)(A...) const, F, K...> {
    static R call(const C &self, A... a) { refuse_viewed_arguments<K...>(a...); return (self.*F)(std::forward<A>(a)...); }
};
template <typename R, typename C, typename... A, R (C::*F)(A...) noexcept, size_t... K>
struct guarded_impl<R (C::*)(A...) noexcept, F, K...> {
    static R call(C &self, A... a) { refuse_viewed_arguments<K...>(a...); return (self.*F)(std::forward<A>(a)...); }
};
template <typename R, typename C, typename... A, R (C::*F)(A...) const noexcept, size_t... K>
struct guarded_impl<R (C::*)(A...) const noexcept, F, K...> {
    static R call(const C &self, A... a) { refuse_viewed_arguments<K...>(a...); return (self.*F)(std::forward<A>(a)...); }
};
template <auto F, size_t... K> using guarded = guarded_impl<decltype(F), F, K...>;
}

// R-VIEW-GUARD: a container member (an NCollection_List, Array1, ... held by value) as nanocct_def_field binds it, whose
// setter refuses while the container has live views -- the assignment would free or reallocate what they point into.
// The property is nanobind's def_rw (nb_class.h) with that check in the setter.
template <typename C, typename T, typename D, typename... Extra>
void nanocct_def_container_field(nb::class_<C> cls, const char *name, D T::*p, const Extra &...extra) {
    if constexpr (std::is_copy_assignable_v<D> && !std::is_const_v<D>)
        cls.def_prop_rw(name,
            [p](const C &c) -> const D & { return c.*p; },
            [p, name](C &c, const D &value) { nanocct::refuse_if_viewed(&(c.*p), name); c.*p = value; },
            extra...);
    else
        cls.def_ro(name, p, extra...);
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

template <> struct type_caster<nanocct::TextInput> {
    NB_TYPE_CASTER(nanocct::TextInput, const_name("typing.TextIO"))

    bool from_python(handle src, uint32_t, cleanup_list *) noexcept {
        if (!hasattr(src, "read"))
            return false;
        try {
            object text = src.attr("read")();
            if (!str_check(text.ptr()))
                return false;
            bytes data = borrow<bytes>(text.attr("encode")("utf-8", "surrogateescape"));   // the inverse of nanocct_stream_text
            value.text.assign(data.c_str(), data.size());
        } catch (...) {
            return false;
        }
        return true;
    }

    static handle from_cpp(const nanocct::TextInput &, rv_policy, cleanup_list *) noexcept { return none_ref(); }
};

template <> struct type_caster<nanocct::OptionalCString> {
    NB_TYPE_CASTER(nanocct::OptionalCString, const_name("str"))   // nb::arg(...).none() appends "| None"

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

    static handle from_cpp(const nanocct::OptionalCString &v, rv_policy, cleanup_list *) noexcept {
        if (v.ptr == nullptr)
            return none_ref();
        return PyUnicode_FromString(v.ptr);
    }
};

template <> struct type_caster<nanocct::BinaryInput> {
    NB_TYPE_CASTER(nanocct::BinaryInput, const_name("typing.BinaryIO"))

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

    static handle from_cpp(const nanocct::BinaryInput &, rv_policy, cleanup_list *) noexcept { return none_ref(); }
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
            // (8.18). Every Transient nanocct creates is handle-held (constructors, R-RESULT), so this is a gap in the
            // bindings; refusing the argument turns a crash into a TypeError.
            if (ptr != nullptr && ptr->GetRefCount() == 0)
                return false;
            value = opencascade::handle<T>(ptr);
            return true;
        }
        // a multiple-inheritance type whose Transient base is not the bound base (HArray1 -> Standard_Transient)
        for (const mi_entry &e : nanocct_mi_list()) {
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
            auto &mi = nanocct_mi_by_name();
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

// Type caster for NCollection_Handle<T> (R-NCHANDLE): OCCT's reference-counted owner of a *non*-Transient
// object, transparent like opencascade::handle. A result is the object itself, shared with its owner as in C++, kept
// alive by a heap copy of the handle attached with keep_alive (the handle's hidden Ptr is a Standard_Transient, so OCCT's
// reference count governs the lifetime). A null handle is None -- IsNull() is asked first, because
// NCollection_Handle::get() dereferences the null Ptr (NCollection_Handle.hxx). A parameter takes the object or None, and
// the object is COPIED into a new handle: the handle deletes what it holds, and the Python object owns its C++ object.
NAMESPACE_BEGIN(NB_NAMESPACE)
NAMESPACE_BEGIN(detail)

template <typename T> struct type_caster<NCollection_Handle<T>> {
    static constexpr bool IsClass = true;
    using Caster = make_caster<T>;
    NB_TYPE_CASTER(NCollection_Handle<T>, Caster::Name)

    bool from_python(handle src, uint32_t flags, cleanup_list *cleanup) noexcept {
        if (src.is_none()) { value = NCollection_Handle<T>(); return true; }
        flags &= ~cast_flags::convert;
        Caster caster;
        if (!caster.from_python(src, flags, cleanup))
            return false;
        T *ptr = caster.operator T *();
        if (ptr == nullptr)
            return false;
        try {
            value = NCollection_Handle<T>(new T(*ptr));
        } catch (...) {
            return false;
        }
        return true;
    }

    static handle from_cpp(const Value &value, rv_policy, cleanup_list *cleanup) noexcept {
        if (value.IsNull()) return none().release();
        T *ptr = const_cast<T *>(value.get());
        bool is_new = false;
        handle result = NB_CALL(nb_type_put)(NB_CTX_C(cleanup), &typeid(T), &typeid(T), ptr,
                                             rv_policy::reference, cleanup, &is_new);
        if (is_new && result.is_valid()) {
            auto *holder = new NCollection_Handle<T>(value);
            keep_alive_cb(result, holder, [](void *p) noexcept { delete (NCollection_Handle<T> *) p; });
        }
        return result;
    }
};

NAMESPACE_END(detail)
NAMESPACE_END(NB_NAMESPACE)

// Type caster for std::reference_wrapper<T> results: NCollection_FlatMap::Contained() returns
// std::optional<std::reference_wrapper<const K>>, NCollection_FlatDataMap::Contained() an optional pair of them. nanobind has
// no caster for it, so those members raised TypeError. A const T is returned as a copy (a read-only key or value); a
// mutable T as a reference into its owner that keeps the owner alive (reference_internal), so edits reach the map as
// in C++. Results only: no OCCT parameter takes a reference_wrapper.
NAMESPACE_BEGIN(NB_NAMESPACE)
NAMESPACE_BEGIN(detail)

template <typename T> struct type_caster<std::reference_wrapper<T>> {
    using Td = std::remove_cv_t<T>;
    using Caster = make_caster<Td>;
    static constexpr auto Name = Caster::Name;

    static handle from_cpp(std::reference_wrapper<T> value, rv_policy policy, cleanup_list *cleanup) noexcept {
        if constexpr (std::is_const_v<T>)
            policy = rv_policy::copy;
        else if (policy == rv_policy::automatic || policy == rv_policy::automatic_reference)
            policy = rv_policy::reference_internal;
        return Caster::from_cpp(value.get(), policy, cleanup);
    }
};

NAMESPACE_END(detail)
NAMESPACE_END(NB_NAMESPACE)
