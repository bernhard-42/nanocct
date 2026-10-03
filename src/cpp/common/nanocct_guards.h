// Part of nanocct_common.h -- the view registry and the container guards (R-VIEW-GUARD).
// Include nanocct_common.h, not this file: the parts rely on each other in the order it includes them.
#pragma once

// R-VIEW-GUARD (Binding-Rules.md): an NCollection container refuses a call that would invalidate one of its live views, with
// BufferError -- Python's own rule for bytearray, which refuses to resize while a buffer is exported. A view is anything
// that points into a container's storage: an element reference (ChangeValue, a List's Append result, a map's ChangeFind or
// ChangeSeek, ...), a numpy array over it, an iterator (OCCT's Iterator classes and the Python ones of __iter__). Which call
// invalidates which kind of view is OCCT's container code, read once (Binding-Rules.md, the R-VIEW-GUARD table): the binder
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
