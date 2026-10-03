// Part of nanocct_common.h -- the lifetime machinery: OCAF owners (R-OWNER), method slots (R-METHOD-KEEP), Kept<T> (R-KEPT), the keep policies (R-COPY, R-CTOR-KEEP, R-RESULT-KEEP) and R-ARRAY-PTR's copy.
// Include nanocct_common.h, not this file: the parts rely on each other in the order it includes them.
#pragma once

// ---------------------------------------------------------------------------------------------
// R-OWNER (Binding-Rules.md): the owner of an OCAF object, known by its type. A TDF_Label and a TDF_Attribute point into the
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

// R-KEPT (Binding-Rules.md): a Transient keeps what it was given as long as its C++ object lives, not only as long as its
// Python object. An OCCT container or document can hold the object after Python dropped it (IntPatch_PolyhedronBVH(poly)
// appended to an NCollection_HSequence, `del bvh, poly`): kept by the Python object, the argument went with it and the
// object read freed memory. So the bindings construct such a class -- one whose constructors or methods keep arguments
// (the generator decides) -- as nanocct::Kept<T>: T itself, plus the slots of the object (the table above, moved onto the
// C++ object). An argument that can own the object itself stays kept by the Python object (Param.kept_cpp): from the C++
// side it would be a reference cycle no garbage collector sees (a VrmlData scene holds its nodes, a node points to its
// scene). Python never sees the subclass: the handle caster reports T (kept registry entry in the MI registry).
using held_slots = std::vector<std::pair<slot_key, PyObject *>>;

// Releasing Python references from a C++ destructor, which runs wherever OCCT drops the last handle: a Python thread
// (holds the GIL, or may wait for it), an OCCT worker thread without a Python thread state (std::thread, the thread pool)
// -- where waiting for the GIL deadlocks while the Python thread that started the algorithm holds it and waits for the
// worker -- or after the interpreter is gone (a C++ static). A worker never blocks: its references go into a queue that one
// Py_AddPendingCall drains on the main thread. After finalisation nothing is released (the leak report at exit is the
// safe side: the object still points to them). The queue is per module (it needs no GIL to be found) and never freed.
struct deferred_releases {
    std::mutex mutex;
    std::vector<PyObject *> pending;
    bool scheduled = false;
};
inline deferred_releases &deferred() {
    static deferred_releases *queue = new deferred_releases();   // never freed: may be used during static destruction
    return *queue;
}
inline int drain_deferred(void *) noexcept {
    std::vector<PyObject *> items;
    {
        deferred_releases &q = deferred();
        std::lock_guard<std::mutex> lock(q.mutex);
        items.swap(q.pending);
        q.scheduled = false;
    }
    for (PyObject *o : items)
        Py_DECREF(o);
    return 0;
}
inline void release_held(held_slots &held) noexcept {
    if (held.empty() || !nb::is_alive())
        return;
    if (PyGILState_GetThisThreadState() == nullptr) {     // not a Python thread: never wait for the GIL
        deferred_releases &q = deferred();
        bool schedule = false;
        {
            std::lock_guard<std::mutex> lock(q.mutex);
            for (auto &entry : held)
                q.pending.push_back(entry.second);
            if (!q.scheduled)
                schedule = q.scheduled = true;
        }
        if (schedule && Py_AddPendingCall(drain_deferred, nullptr) != 0) {
            std::lock_guard<std::mutex> lock(q.mutex);   // the pending-call queue is full: the next release schedules again
            q.scheduled = false;
        }
        return;
    }
    nb::gil_scoped_acquire gil;                           // nested use on a thread that holds it is fine
    for (auto &entry : held)
        Py_DECREF(entry.second);
}

struct kept_base {
    // The slot table's mutex, looked up here: a binding constructs every Kept<T>, with the GIL held. Delete() runs wherever
    // OCCT drops the last handle (a worker thread, after finalisation), where slots() may not be called -- its first call
    // in a toolkit imports nanocct (nanocct_shared).
    std::mutex *guard = &slots().mutex;
    held_slots held;                                      // this object's slots, guarded by *guard (slots().mutex)
    virtual ~kept_base() { release_held(held); }          // empty after Delete(), which releases after T's destructor
};
// T first, at offset 0: nanobind's stored pointer is the T* of the object. Not for a multiple-inheritance H-collection,
// whose bound base sits at offset 0 instead (the generator never asks for one).
template <typename T> struct Kept final : T, kept_base {
    static_assert(!has_mi_traits<T>::value, "R-KEPT: not for a multiple-inheritance type");
    // forwarding, not `using T::T`: an inherited constructor is never a copy constructor ([over.match.funcs]), and a copy of
    // a kept class (Graphic3d_ClipPlane(theOther)) is constructed here too
    template <typename... A> explicit Kept(A &&...args) : T(std::forward<A>(args)...) {}
    // Standard_Transient::Delete() (the only definition in OCCT, Standard_Transient.hxx) is what the last handle calls.
    // Bases are destroyed in reverse order, so ~kept_base runs before ~T, whose destructor may still read the arguments:
    // the slots are taken out first and released after T's own Delete() has destroyed the whole object.
    void Delete() const override {
        held_slots held;
        {
            std::lock_guard<std::mutex> lock(*this->guard);   // store_slot and slot_arguments use held under it
            held.swap(const_cast<Kept *>(this)->held);
        }
        T::Delete();
        release_held(held);
    }
};
// the Kept part of an object whose binding is on class Self, or nullptr (a T that OCCT constructed itself)
template <typename Self> kept_base *kept_of(PyObject *o) noexcept {
    if constexpr (std::is_base_of_v<Standard_Transient, Self> && !has_mi_traits<Self>::value) {
        Self *ptr = nb::inst_ptr<Self>(o);
        if (ptr == nullptr)
            return nullptr;
        if constexpr (!std::is_final_v<Self>)
            if (typeid(*ptr) == typeid(Kept<Self>))           // the usual case, without the cross-cast through the hierarchy
                return static_cast<Kept<Self> *>(ptr);
        return dynamic_cast<kept_base *>(static_cast<Standard_Transient *>(ptr));
    } else {
        return nullptr;
    }
}
// the same for any object (an argument whose class the policy does not know): every bound Transient except the
// multiple-inheritance H-collections derives from Standard_Transient in Python too, with it at offset 0
inline kept_base *kept_of_any(PyObject *o) noexcept {
    nb::handle transient = nb::type<Standard_Transient>();
    if (!transient.is_valid() || !PyType_IsSubtype(Py_TYPE(o), (PyTypeObject *) transient.ptr()))
        return nullptr;
    return dynamic_cast<kept_base *>(nb::inst_ptr<Standard_Transient>(o));
}
// the handle caster asks the MI registry for the dynamic type's name: a Kept<T> is shown as T (its own typeid is unknown to
// nanobind, which would fall back to the static type -- a Standard_Transient for an object taken out of an HSequence)
template <typename T> void register_kept(nb::handle py_type) {
    mi_entry e{py_type.ptr(),
               [](void *stored) -> Standard_Transient * { return static_cast<T *>(stored); },
               [](Standard_Transient *t) -> void * { return static_cast<T *>(static_cast<Kept<T> *>(dynamic_cast<void *>(t))); },
               &typeid(T)};
    // nb::find(T&): nanobind does not know Kept<T>'s own typeid and looks the object up as T, the type Python sees
    e.find = [](void *stored) -> PyObject * { return nb::find(*static_cast<T *>(stored)).release().ptr(); };
    nanocct_mi_by_name()[typeid(Kept<T>).name()] = e;
}

// A slot store: its owner's C++ object for a Kept<T> (k), the table otherwise. The previous argument goes outside the
// lock: its release can run Python code.
inline void store_slot(PyObject *owner, kept_base *k, slot_key key, PyObject *argument) {
    PyObject *previous = nullptr;
    Py_INCREF(argument);
    {
        slot_registry &reg = slots();
        std::lock_guard<std::mutex> lock(reg.mutex);
        held_slots *held = nullptr;
        if (k != nullptr) {
            held = &k->held;
        } else {
            auto [it, created] = reg.slots.try_emplace(owner);
            if (created)
                nb::keep_alive_cb(owner, owner, &release_slots);
            held = &it->second;
        }
        auto entry = std::find_if(held->begin(), held->end(), [&](const auto &e) { return e.first == key; });
        if (entry != held->end())
            previous = std::exchange(entry->second, argument);
        else
            held->emplace_back(key, argument);
    }
    Py_XDECREF(previous);
}
// What an object's slots hold now, in the table and on its C++ object (a Kept<T> can have both: an argument that passed
// the cycle check and one that did not); new references.
inline std::vector<PyObject *> slot_arguments(PyObject *o) {
    kept_base *k = kept_of_any(o);
    std::vector<PyObject *> out;
    slot_registry &reg = slots();
    std::lock_guard<std::mutex> lock(reg.mutex);
    auto it = reg.slots.find(o);
    if (it != reg.slots.end())
        for (auto &entry : it->second)
            out.push_back(entry.second);
    if (k != nullptr)
        for (auto &entry : k->held)
            out.push_back(entry.second);
    for (PyObject *argument : out)
        Py_INCREF(argument);
    return out;
}

// R-COPY / R-RESULT-KEEP: the nurse may hold pointers copied out of the patient -- a copy of it, a view it produced --
// and those may point into what the patient's slots hold now. A slot drops its argument when the patient stores the next
// one (ext.Initialize(c2) after cp = Extrema_ExtCC2d(ext)), so keeping the patient is not enough: the nurse keeps the
// arguments themselves (accumulating, nb::keep_alive_obj; never itself).
inline void keep_slots_of(PyObject *nurse, PyObject *patient) {
    for (PyObject *argument : slot_arguments(patient)) {
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
// R-COPY, R-CTOR-KEEP: keep_view_of as a call policy, numbered like nb::keep_alive (0 is the result, 1 self, nb::new_'s
// arguments count from 2): a copy keeps its original, a constructor an argument it copies pointers out of
// (TDF_ChildIterator(label), the argument-layout keep). A None nurse (nb::new_'s no-op __init__) keeps nothing.
template <size_t Nurse, size_t Patient> struct keep_view_arg {
    static void precall(PyObject **, size_t, nb::detail::cleanup_list *) {}
    static void postcall(PyObject **args, size_t, nb::handle ret) {
        PyObject *nurse = Nurse == 0 ? ret.ptr() : args[Nurse - 1];
        if (nurse != nullptr && nurse != Py_None)
            keep_view_of(nurse, args[Patient - 1]);
    }
};
// R-KEPT: a kept argument of a constructor of a Kept<T> class (nb::new_: the result is the nurse, the arguments count from
// 2). Cpp: it passed the cycle check -- it lives in a slot of the C++ object (Tag, Slot: the file and its slot number, as
// for keep_slot), and so does what its own slots hold now when the object may copy pointers out of it (View, R-COPY).
// Otherwise it is kept by the Python object, as by keep_alive<0, Patient> / keep_view_arg<0, Patient>.
template <typename Tag, typename Self, size_t Patient, size_t Slot, bool View, bool Cpp> struct keep_arg {
    static void precall(PyObject **, size_t, nb::detail::cleanup_list *) {}
    static void postcall(PyObject **args, size_t, nb::handle ret) {
        PyObject *nurse = ret.ptr();
        PyObject *patient = args[Patient - 1];
        if (nurse == nullptr || nurse == Py_None || patient == nurse)   // None: nb::new_'s no-op __init__
            return;
        kept_base *k = nullptr;
        if constexpr (Cpp)
            k = kept_of<Self>(nurse);
        if (k == nullptr) {
            if constexpr (View)
                keep_view_of(nurse, patient);
            else
                nb::keep_alive_obj(nurse, patient);
            return;
        }
        store_slot(nurse, k, slot_key{&slot_tag<Tag>::id, Slot}, patient);
        if constexpr (View) {
            std::vector<PyObject *> more = slot_arguments(patient);
            {
                std::lock_guard<std::mutex> lock(slots().mutex);
                for (PyObject *argument : more)
                    if (argument != nurse)
                        k->held.emplace_back(slot_key{nullptr, 0}, argument);   // accumulating: never a slot's key
                    else
                        Py_DECREF(argument);                                    // under the lock: not the last reference
            }
        }
    }
};

// R-ARRAY-PTR (Binding-Rules.md): an array a listed member takes by its first element (VrmlData_Coordinate(scene, name,
// nPoints, arrPoints)) is a Python sequence. The object keeps the pointer, so the elements are copied into memory of the
// owner's allocator -- where OCCT's own reader puts them (VrmlData_ArrayVec3d::AllocateValues: Scene().Allocator(),
// VrmlData_Geometry.cxx) -- and live as long as it. An empty sequence passes nullptr, as the C++ default does.
template <typename Owner, typename T> const T *allocator_copy(const Owner &owner, const std::vector<T> &items) {
    static_assert(std::is_trivially_destructible_v<T>, "R-ARRAY-PTR: an incremental allocator never runs destructors");
    if (items.empty())
        return nullptr;
    T *out = static_cast<T *>(owner.Allocator()->Allocate(items.size() * sizeof(T)));
    std::uninitialized_copy(items.begin(), items.end(), out);
    return out;
}
} // namespace nanocct
