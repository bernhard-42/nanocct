// Part of nanocct_common.h -- what the generated define phase calls per class: R-ITER, the implicit constructors, conversions (R-CONV), fields (R-FIELD) and the exception translator.
// Include nanocct_common.h, not this file: the parts rely on each other in the order it includes them.
#pragma once

// Constructors of a class-template instantiation whose abstractness only the compiler can see (BVH_PrimitiveSet<double, 3>
// through the pure virtuals of BVH_Set): the generic lambda's body is instantiated only when the class is concrete (R-TEMPLATE-BASE).
template <typename T, typename F> void nanocct_if_concrete(nb::class_<T> cls, F f) {
    if constexpr (!std::is_abstract_v<T>)
        f(cls);
}

// R-ITER: a class with More()/Next() and a parameterless Value() or Current() gets __iter__, a Python iterator over it
// through nb::make_iterator, like the containers: a hand-written __next__ ended every loop with a thrown
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
// R-KEPT: a class whose bindings keep arguments is constructed as nanocct::Kept<T>.
template <typename T, bool K, typename... A> T *nanocct_new_transient(A &&...args) {
    if constexpr (K)
        return new nanocct::Kept<T>(std::forward<A>(args)...);
    else
        return new T(std::forward<A>(args)...);
}

// R-IMPLICIT-DEFAULT: the implicit default constructor, bound only when std::is_default_constructible_v<T>
template <typename T, bool K = false> void nanocct_implicit_default_ctor(nb::class_<T> cls) {
    if constexpr (std::is_default_constructible_v<T>) {
        if constexpr (std::is_base_of_v<Standard_Transient, T>)
            cls.def(nb::new_([]() { return opencascade::handle<T>(nanocct_new_transient<T, K>()); }));
        else
            cls.def(nb::init<>());
    }
}

// R-IMPLICIT-COPY: the implicit copy constructor (none declared by the class): bound when it exists (deleted for classes
// with a reference or non-copyable member) and the generator found it safe (R-COPY: never for a class whose destructor
// may free a pointer the copy would share). Sub-class arguments convert implicitly, as in C++ (TopoDS_Shape(aVertex)).
// View (R-COPY): the class holds pointers, which the copy shares, so the copy keeps the original alive and what the
// original's slots hold now (keep_view_arg<0, 2> through nb::new_, as for R-CTOR-KEEP). R-KEPT: K, a Kept<T> class -- the
// original then lives in a slot of the copy's C++ object when Cpp (it cannot own the copy), named by Tag and Slot.
template <typename T, bool View = false, bool K = false, bool Cpp = false, typename Tag = void, size_t Slot = 0>
void nanocct_implicit_copy_ctor(nb::class_<T> cls) {
    if constexpr (std::is_copy_constructible_v<T>) {
        if constexpr (std::is_base_of_v<Standard_Transient, T> && View && K)
            cls.def(nb::new_([](const T &other) { return opencascade::handle<T>(nanocct_new_transient<T, K>(other)); }),
                    nb::arg("theOther"), nb::call_policy<nanocct::keep_arg<Tag, T, 2, Slot, true, Cpp>>());
        else if constexpr (std::is_base_of_v<Standard_Transient, T> && View)
            cls.def(nb::new_([](const T &other) { return opencascade::handle<T>(new T(other)); }), nb::arg("theOther"),
                    nb::call_policy<nanocct::keep_view_arg<0, 2>>());
        else if constexpr (std::is_base_of_v<Standard_Transient, T>)
            cls.def(nb::new_([](const T &other) { return opencascade::handle<T>(nanocct_new_transient<T, K>(other)); }),
                    nb::arg("theOther"));
        else if constexpr (View)
            cls.def(nb::init<const T &>(), nb::arg("theOther"), nb::call_policy<nanocct::keep_view_arg<1, 2>>());
        else
            cls.def(nb::init<const T &>(), nb::arg("theOther"));
    }
}

// R-CONV: operator To() const of From: To gets a constructor from From (To(aFrom) in Python) and, unless the operator
// is explicit, the implicit conversion C++ has (a From passes where a To is expected). From is taken by non-const
// reference: some operators are not const (Message_Msg).
template <typename From, typename To, bool K = false> void nanocct_conversion(nb::handle to_type, bool implicit) {
    auto cls = nb::borrow<nb::class_<To>>(to_type);
    if constexpr (std::is_base_of_v<Standard_Transient, To>)
        cls.def(nb::new_([](From &from) { return opencascade::handle<To>(nanocct_new_transient<To, K>(static_cast<To>(from))); }),
                nb::arg("theFrom"));
    else
        cls.def("__init__", [](To *self, From &from) { new (self) To(static_cast<To>(from)); }, nb::arg("theFrom"));
    if (implicit)
        nb::implicitly_convertible<From, To>();
}

// R-CONV: operator opencascade::handle<To>() const of From: the handle's object becomes the result of To(aFrom)
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
