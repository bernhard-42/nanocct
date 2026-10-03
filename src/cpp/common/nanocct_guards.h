// Part of nanocct_common.h -- the view registry and the container guards (R-VIEW-GUARD).
// Include nanocct_common.h, not this file: the parts rely on each other in the order it includes them.
#pragma once

// R-VIEW-GUARD (Binding-Rules.md): a view is anything that points into an NCollection container's storage: an element
// reference (ChangeValue, a List's Append result, a map's ChangeFind or ChangeSeek, ...), a numpy array over it, an
// iterator (OCCT's Iterator classes and the Python ones of __iter__). A call that would invalidate a view is treated as
// Python treats its own types:
// - element references and numpy arrays: the container refuses the call with BufferError -- Python's rule for bytearray,
//   which refuses to resize while a buffer is exported;
// - iterators: the call goes ahead and the container's live iterators go stale; a stale iterator raises RuntimeError on
//   its next use -- Python's rule for dict, set and deque ("dictionary changed size during iteration").
// Which call invalidates which kind of view is OCCT's container code, read once (Binding-Rules.md, the R-VIEW-GUARD
// table): the binder (nanocct_ncollection.h) checks its own members, nanocct::guarded checks every generated function that
// takes a container by non-const reference or pointer -- OCCT may change it -- and a container data member checks before
// it is assigned. Views are counted per C++ container address, so two Python wrappers of one container agree, in ONE
// table for all extension modules (nanocct_shared): a generated function of any toolkit sees the views another toolkit's
// binder handed out. A view's count goes when the view dies (nb::keep_alive_cb; a numpy array: its owner capsule).
// Staleness is a generation per container, an atomic the container's iterators share: an invalidating call bumps it, an
// iterator remembers the value it was registered at (constructor, Init/Initialize). An iterator's check is one table
// lookup by its C++ address and an atomic load (a Python iterator of __iter__ holds the generation itself: one atomic
// load), so a loop pays a few ns per step. `live` counts all views of all containers: a call made while nothing is viewed
// anywhere costs one atomic load.
// The table is touched only from binding glue, which holds the GIL (calls, call policies, keep_alive_cb, capsule
// destructors): a GIL build needs no lock, a free-threaded build (Py_GIL_DISABLED) takes a mutex.
#if defined(Py_GIL_DISABLED)
using view_mutex = std::mutex;
#else
struct view_mutex { void lock() noexcept {} void unlock() noexcept {} };
#endif
enum class view_kind : size_t { element = 0, iterator = 1 };
using view_generation = std::atomic<uint64_t>;
struct view_registry {
    struct counts {                                       // a container with live views
        size_t n[2] = {0, 0};                             // by view_kind
        std::shared_ptr<view_generation> generation = std::make_shared<view_generation>(0);
    };
    struct view {                                         // a live view object
        const void *container = nullptr;
        view_kind kind = view_kind::element;
        const void *object = nullptr;                     // an iterator's C++ object: its key in `iterators`
        std::shared_ptr<view_generation> generation;      // an iterator's container's generation ...
        uint64_t stamp = 0;                               // ... and the value it started at
    };
    view_mutex mutex;
    std::atomic<size_t> live{0};
    std::unordered_map<const void *, counts> containers;            // container -> its live views
    std::unordered_map<PyObject *, std::unique_ptr<view>> views;    // view object -> what it views (an iterator can be re-initialised)
    std::unordered_map<const void *, view *> iterators;             // C++ object of an iterator view -> its record
};
inline view_registry &view_table() { return nanocct_shared<view_registry>("_view_registry", "nanocct._view_registry"); }
// both under the lock
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
    std::lock_guard<view_mutex> lock(reg.mutex);
    auto it = reg.views.find(static_cast<PyObject *>(view));
    if (it == reg.views.end())
        return;
    view_unlink(reg, it->second->container, it->second->kind);
    auto i = reg.iterators.find(it->second->object);
    if (i != reg.iterators.end() && i->second == it->second.get())
        reg.iterators.erase(i);
    reg.views.erase(it);
}
// `view` (a nanobind instance) points into the container at `container` until it dies. The same object again (nanobind
// returns the wrapper it already has for an address) counts once; an iterator initialised on another container moves.
// Every registration (re)starts an iterator at the container's current generation: a re-initialised iterator is fresh.
inline void add_view(nb::handle view, const void *container, view_kind kind) {
    if (!view.is_valid() || view.is_none())
        return;
    view_registry &reg = view_table();
    bool fresh;
    {
        std::lock_guard<view_mutex> lock(reg.mutex);
        std::unique_ptr<view_registry::view> &v = reg.views[view.ptr()];
        fresh = v == nullptr;
        if (fresh) {
            v = std::make_unique<view_registry::view>();
        } else if (v->container != container || v->kind != kind) {
            view_unlink(reg, v->container, v->kind);
        }
        if (fresh || v->container != container || v->kind != kind) {
            v->container = container;
            v->kind = kind;
            view_link(reg, container, kind);
        }
        if (kind == view_kind::iterator) {
            v->object = nb::inst_ptr<void>(view);
            v->generation = reg.containers[container].generation;
            v->stamp = v->generation->load();
            reg.iterators[v->object] = v.get();
        }
    }
    if (fresh)
        nb::keep_alive_cb(view, view.ptr(), &release_view);
}
// the container an iterator object was registered for, nullptr if none (a default-constructed Iterator)
inline const void *viewed_container(PyObject *iterator) {
    view_registry &reg = view_table();
    std::lock_guard<view_mutex> lock(reg.mutex);
    auto it = reg.views.find(iterator);
    return it == reg.views.end() ? nullptr : it->second->container;
}
// numpy: the owner of an array over the container's storage -- counts one element view and keeps the container's Python
// object alive until the array (and every array derived from it) is gone. nanobind refuses reference_internal for an
// ndarray that has an owner (nb_ndarray.cpp, ndarray_export), so the owner does both.
struct exported_view { const void *container; PyObject *owner; };
inline nb::capsule export_view(const void *container, nb::handle owner) {
    view_registry &reg = view_table();
    {
        std::lock_guard<view_mutex> lock(reg.mutex);
        view_link(reg, container, view_kind::element);
    }
    auto *payload = new exported_view{container, owner.inc_ref().ptr()};
    return nb::capsule(payload, [](void *p) noexcept {
        auto *e = static_cast<exported_view *>(p);
        {
            view_registry &r = view_table();
            std::lock_guard<view_mutex> lock(r.mutex);
            view_unlink(r, e->container, view_kind::element);
        }
        Py_DECREF(e->owner);                             // outside the lock: the release can run Python code
        delete e;
    });
}
// the live element views (element references, numpy arrays) of a container
inline size_t live_elements(const void *container) {
    view_registry &reg = view_table();
    if (reg.live.load() == 0)
        return 0;
    std::lock_guard<view_mutex> lock(reg.mutex);
    auto it = reg.containers.find(container);
    return it == reg.containers.end() ? 0 : it->second.n[(size_t) view_kind::element];
}
[[noreturn]] inline void raise_viewed(size_t n, const std::string &what) {
    const std::string msg = what + ": " + std::to_string(n) + " live view(s) of this container (element references or "
        "numpy arrays) would be invalidated by this call; release them first (BufferError, as bytearray raises while a "
        "buffer is exported)";
    throw nb::buffer_error(msg.c_str());
}
// the call goes ahead: the container's live iterators go stale, except `except` (an iterator the call itself goes through
// and leaves valid, as List.Remove(it)), which moves to the new generation
inline void invalidate_iterators(const void *container, PyObject *except = nullptr) {
    view_registry &reg = view_table();
    if (reg.live.load() == 0)
        return;
    std::lock_guard<view_mutex> lock(reg.mutex);
    auto it = reg.containers.find(container);
    if (it == reg.containers.end() || it->second.n[(size_t) view_kind::iterator] == 0)
        return;
    const uint64_t now = it->second.generation->fetch_add(1) + 1;
    if (except != nullptr) {
        auto v = reg.views.find(except);
        if (v != reg.views.end() && v->second->container == container && v->second->kind == view_kind::iterator)
            v->second->stamp = now;
    }
}
// BufferError when the container has live element views the call would invalidate; otherwise its iterators go stale.
// what: the member, for the message.
inline void refuse_if_viewed(const void *container, const char *what, PyObject *except = nullptr) {
    const size_t n = live_elements(container);
    if (n != 0)
        raise_viewed(n, what);
    invalidate_iterators(container, except);
}
[[noreturn]] inline void raise_stale(const char *what) {
    const std::string msg = std::string(what) + ": the container changed during iteration; initialise the iterator "
        "again (RuntimeError, as dict raises after a change of size during iteration)";
    throw std::runtime_error(msg);
}
// RuntimeError when the C++ object `object` is a registered iterator whose container changed since it was (re)initialised.
// what: the member, for the message.
inline void refuse_if_stale(const void *object, const char *what) {
    view_registry &reg = view_table();
    if (reg.live.load() == 0)
        return;
    bool stale;
    {
        std::lock_guard<view_mutex> lock(reg.mutex);
        auto it = reg.iterators.find(object);
        stale = it != reg.iterators.end() && it->second->generation->load(std::memory_order_relaxed) != it->second->stamp;
    }
    if (stale)
        raise_stale(what);
}
// A container's Python iterator (__iter__): nb::make_iterator drives a C++ iterator, which raises RuntimeError before it
// moves or compares once the container changed. The generation and its start value are shared by the begin and end
// copies and set right after the Python iterator is registered (iterate below), from its record.
struct iterate_start {
    std::shared_ptr<view_generation> generation;
    uint64_t stamp = 0;
};
template <typename I> struct checked_iterator {
    I it;
    std::shared_ptr<iterate_start> start;
    mutable bool stepped = false;             // ++ checked, the == right after it need not (nanocct_iter_cursor)
    void check() const {
        if (start->generation != nullptr && start->generation->load(std::memory_order_relaxed) != start->stamp)
            raise_stale("iterator");
    }
    bool operator==(const checked_iterator &o) const {
        if (!stepped)
            check();
        stepped = false;
        return it == o.it;
    }
    bool operator!=(const checked_iterator &o) const { return !(*this == o); }
    checked_iterator &operator++() { check(); ++it; stepped = true; return *this; }
    decltype(auto) operator*() const { return *it; }
};
// __iter__: a Python iterator over [first, last), registered as an iterator view of `self` (R-VIEW-GUARD)
template <nb::rv_policy::value Policy = nb::rv_policy::automatic_reference_v, typename C, typename I>
auto iterate(nb::handle scope, const char *name, const C &self, I first, I last) {
    auto start = std::make_shared<iterate_start>();
    auto it = nb::make_iterator<Policy>(scope, name, checked_iterator<I>{first, start}, checked_iterator<I>{last, start});
    add_view(it, &self, view_kind::iterator);
    view_registry &reg = view_table();
    std::lock_guard<view_mutex> lock(reg.mutex);
    auto v = reg.views.find(it.ptr());
    if (v != reg.views.end()) {
        start->generation = v->second->generation;
        start->stamp = v->second->stamp;
    }
    return it;
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

// R-VIEW-GUARD for generated code: the call refuses when a container argument it may change has live element views, and
// makes its iterators stale otherwise (every argument is checked before any iterator goes stale). The check runs
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
template <typename A> void refuse_element_viewed_argument(A &argument, size_t position) {
    const void *container = container_address(argument);
    if (container == nullptr)
        return;
    const size_t n = live_elements(container);
    if (n != 0)
        raise_viewed(n, "argument " + std::to_string(position));
}
template <typename A> void invalidate_argument_iterators(A &argument) {
    const void *container = container_address(argument);
    if (container != nullptr)
        invalidate_iterators(container);
}
// one argument (a generated lambda or constructor body)
template <typename A> void refuse_viewed_argument(A &argument, size_t position) {
    refuse_element_viewed_argument(argument, position);
    invalidate_argument_iterators(argument);
}
template <size_t... K, typename... A> void refuse_viewed_arguments(A &...arguments) {
    if (view_table().live.load() == 0)
        return;
    auto all = std::forward_as_tuple(arguments...);
    (refuse_element_viewed_argument(std::get<K>(all), K + 1), ...);
    (invalidate_argument_iterators(std::get<K>(all)), ...);
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

// R-VIEW-GUARD for generated iterator classes constructed or initialised on a container (emit.py _stale_check): every
// member but Init/Initialize raises RuntimeError once that container changed. One atomic load while nothing is viewed.
template <typename T> void refuse_if_stale_self(const T &self, const char *what) {
    refuse_if_stale(static_cast<const void *>(&self), what);
}
// the directly bound member with the same signature, self first (as guarded): fresh_call<F>::call, F a member function
// or a function taking self first (guarded<...>::call)
template <typename T, T F> struct fresh_impl;
template <typename R, typename C, typename... A, R (C::*F)(A...)> struct fresh_impl<R (C::*)(A...), F> {
    static R call(C &self, A... a) { refuse_if_stale_self(self, "iterator"); return (self.*F)(std::forward<A>(a)...); }
};
template <typename R, typename C, typename... A, R (C::*F)(A...) const> struct fresh_impl<R (C::*)(A...) const, F> {
    static R call(const C &self, A... a) { refuse_if_stale_self(self, "iterator"); return (self.*F)(std::forward<A>(a)...); }
};
template <typename R, typename C, typename... A, R (C::*F)(A...) noexcept> struct fresh_impl<R (C::*)(A...) noexcept, F> {
    static R call(C &self, A... a) { refuse_if_stale_self(self, "iterator"); return (self.*F)(std::forward<A>(a)...); }
};
template <typename R, typename C, typename... A, R (C::*F)(A...) const noexcept>
struct fresh_impl<R (C::*)(A...) const noexcept, F> {
    static R call(const C &self, A... a) { refuse_if_stale_self(self, "iterator"); return (self.*F)(std::forward<A>(a)...); }
};
template <typename R, typename C, typename... A, R (*F)(C &, A...)> struct fresh_impl<R (*)(C &, A...), F> {
    static R call(C &self, A... a) { refuse_if_stale_self(self, "iterator"); return F(self, std::forward<A>(a)...); }
};
template <auto F> using fresh_call = fresh_impl<decltype(F), F>;
}

// R-VIEW-GUARD: a container member (an NCollection_List, Array1, ... held by value) as nanocct_def_field binds it, whose
// setter refuses while the container has live element views and makes its iterators stale -- the assignment would free or
// reallocate what they point into.
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
