"""Hand-written NCollection binders (Design.md 6a), all 15 kinds, instantiated by the generator."""
import pytest

from OCP3x import NCollection, Standard, TColStd
from OCP3x._templates import Generic

A = NCollection.NCollection_Array1__double                         # every instantiation lives in OCP3x.NCollection (Design.md 6a)
AH = NCollection.NCollection_Array1__Handle_Standard_Persistent
H = NCollection.NCollection_HArray1__Handle_Standard_Persistent


def test_array1_occt_api():
    a = A(1, 5)
    a.Init(0.5)
    a.SetValue(3, 7.0)
    assert (a.Lower(), a.Upper(), a.Length(), a.Size()) == (1, 5, 5, 5)
    assert a.Value(3) == 7.0
    assert a(3) == 7.0                                         # OCCT operator() alias of Value
    assert a[3] == 7.0                                         # OCCT operator[] alias of Value (OCCT index!)
    assert (a.First(), a.Last()) == (0.5, 0.5)
    assert a.At(2) == 7.0                                      # 0-based checked access
    assert A(3).Lower() == 0 and A(3).Upper() == 2             # zero-based constructor


def test_array1_python_additions():
    a = A(1, 3)
    a.Init(1.0)
    a[2] = 9.0                                                 # __setitem__ -> SetValue
    assert len(a) == 3                                         # __len__ -> Length
    assert list(a) == [1.0, 9.0, 1.0]                          # __iter__ Lower..Upper


def test_array1_out_of_range_is_occt_exception():
    with pytest.raises(Standard.Standard_OutOfRange):
        A(1, 3)[4]


def test_array1_copy_and_assign():
    a = A(1, 2)
    a.Init(1.0)
    b = A(a)
    b.SetValue(1, -1.0)
    assert a[1] == 1.0 and b[1] == -1.0
    assert A().Assign(b)[1] == -1.0


def test_array1_of_handles_null_is_none():
    a = AH(1, 2)
    assert a.Value(1) is None
    p = Standard.Standard_Persistent()
    a.SetValue(1, p)
    assert a.Value(1) is p                                     # same object through the handle caster
    assert p.GetRefCount() == 2                                # array + Python holder


def test_harray1_is_an_array1_with_transient_members():
    h = H(5, 9)                                                # Lower() = 5: catches an unadjusted Transient pointer
    assert h.GetRefCount() == 1
    assert h.DynamicType().Name() == "NCollection_HArray1"
    assert h.IsKind("Standard_Transient") is True
    assert h.Length() == 5 and len(h) == 5 and h.Value(5) is None
    assert isinstance(h, AH)                                   # nanobind base = the offset-0 base NCollection_Array1
    assert not isinstance(h, Standard.Standard_Transient)      # the Transient base is at a non-zero offset (Design.md 4.2)
    assert type(h.Array1()) is AH                              # sliced copy of the array part
    assert h.ChangeArray1() is h                               # mutable view = the object itself


def test_harray1_passes_as_array1_and_as_transient_handle():
    h = H(1, 2)
    b = AH()
    b.Assign(h)                                                # C++: const NCollection_Array1<T>& (inherited base)
    assert b.Length() == 2
    seq = NCollection.NCollection_Sequence[Standard.Standard_Transient]()
    seq.Append(h)                                              # handle<Standard_Transient> parameter: MI registry up-cast
    assert h.GetRefCount() == 2
    back = seq.Value(1)                                        # handle<Standard_Transient> holding an HArray1: down-cast
    assert back is h and back.Lower() == 1
    with pytest.raises(TypeError):
        AH(1, 1).SetValue(1, h)                                # not a Standard_Persistent: rejected, no corruption


def test_the_pre_8_0_typedef_names_are_not_exposed():
    """OCP3x is an OCCT 8 binding: the pre-8.0 aliases of src/Deprecated/NCollectionAliases
    (TColStd_Array1OfReal & co) are not bound -- the 8.0 spelling is the container itself
    (decision 2026-09-24, Design.md 6a). 6c aliases that OCCT still declares as real classes stay."""
    assert not hasattr(TColStd, "TColStd_Array1OfReal")
    a = A(1, 3)
    a.Init(2.5)
    assert list(a) == [2.5, 2.5, 2.5]
    assert TColStd.TColStd_PackedMapOfInteger is not None      # 6c: bound as a class, not an alias


def test_docstrings_come_from_the_template_header():
    assert "Constant value access" in A.Value.__doc__
    assert "unidimensional arrays" in A.__doc__
    assert "Python addition" in A.__len__.__doc__


# R-DEPRECATED (Design.md 6) in the hand-written binders: NCollection_Map is the only one of the 15 templates whose
# header carries Standard_DEPRECATED, on all 11 set operations. The note came only from the generated path until
# 2026-09-25, so these two assertions are what keeps ncollection.py reading the availability attribute.
DEPRECATED_MAP_MEMBERS = ("Union", "Unite", "HasIntersection", "Intersection", "Intersect",
                          "Subtraction", "Subtract", "Difference", "Differ", "IsEqual", "Contains")


@pytest.mark.parametrize("name", DEPRECATED_MAP_MEMBERS)
def test_deprecated_map_member_says_so_in_its_docstring(name):
    doc = getattr(NCollection.NCollection_Map__int, name).__doc__
    assert "Deprecated in OCCT: This method will be removed right after 7.9. release." in doc


def test_the_undeprecated_contains_overload_keeps_its_own_docstring():
    # Contains(theKey) is not deprecated and Contains(theOther) is; they share a Python name, so the binder gives the
    # deprecated one its own docstring constant and nanobind renders the two overloads separately
    blocks = NCollection.NCollection_Map__int.Contains.__doc__.split("``Contains(self, ")
    assert len(blocks) == 3                                                    # the signature header plus one per overload
    assert "Deprecated in OCCT" not in blocks[1]                               # theKey: int
    assert "Deprecated in OCCT" in blocks[2]                                   # theOther: NCollection_Map__int


def test_template_accessor_spelling():
    assert NCollection.NCollection_Array1[float] is A                                  # double -> float
    assert NCollection.NCollection_Array1[Standard.Standard_Persistent] is AH          # handle<X> -> X
    assert NCollection.NCollection_HArray1[Standard.Standard_Persistent] is H
    a = NCollection.NCollection_Array1[float](1, 2)
    a.Init(3.0)
    assert list(a) == [3.0, 3.0]
    with pytest.raises(TypeError, match="not bound"):
        NCollection.NCollection_Array1[bytes]                             # no OCCT signature uses Array1<bytes>
    with pytest.raises(TypeError, match="template"):
        NCollection.NCollection_Array1(1, 2)
    assert "NCollection_Array1__double" in NCollection.NCollection_Array1.bound()


# ---------------------------------------------------------------------------------------------- List
L = NCollection.NCollection_List[int]


def test_list_occt_api_and_python_additions():
    l = L()
    l.Append(1)
    l.Append(2)
    l.Prepend(0)
    assert (l.Extent(), l.Length(), l.Size(), len(l)) == (3, 3, 3, 3)
    assert (l.First(), l.Last()) == (0, 2)
    assert list(l) == [0, 1, 2]
    assert l.Contains(2) is True and (5 in l) is False           # Contains bound because int has operator==
    assert l.Remove(1) is True and list(l) == [0, 2]
    l.Reverse()
    assert list(l) == [2, 0]
    l.RemoveFirst()
    assert list(l) == [0]


def test_list_iterator_is_nested_class():
    l = L()
    for v in (0, 1, 2):
        l.Append(v)
    it = L.Iterator(l)                                           # NCollection_List<T>::Iterator
    seen = []
    while it.More():
        seen.append(it.Value())
        it.Next()
    assert seen == [0, 1, 2]
    it = L.Iterator(l)
    it.Next()
    l.InsertBefore(99, it)
    assert list(l) == [0, 99, 1, 2]
    assert L.Iterator.__qualname__ == "NCollection_List__int.Iterator"


def test_binder_iterators_are_python_iterators():
    """R-ITER applies to the hand-written binder Iterator classes too (2026-09-22): iterating yields Value() -- the
    element for List/Sequence, the key for Map, the value for DataMap -- and advances the Iterator itself, so it is
    exhausted afterwards, like a file (nb::make_iterator since 2026-09-27, not a __next__ on the object)."""
    l = L()
    for v in (3, 4):
        l.Append(v)
    it = L.Iterator(l)
    assert list(it) == [3, 4] and list(it) == [] and it.More() is False         # exhausted, like a file
    m = NCollection.NCollection_DataMap[int, float]()
    m.Bind(1, 1.5)
    m.Bind(2, 2.5)
    assert sorted(NCollection.NCollection_DataMap[int, float].Iterator(m)) == [1.5, 2.5]
    im = NCollection.NCollection_IndexedMap[float]()
    im.Add(7.0)
    im.Add(8.0)
    assert list(NCollection.NCollection_IndexedMap[float].Iterator(im)) == [7.0, 8.0]


# ------------------------------------------------------------------------------------------ Sequence
from OCP3x import TCollection  # noqa: E402

S = NCollection.NCollection_Sequence[TCollection.TCollection_AsciiString]
HS = NCollection.NCollection_HSequence[TCollection.TCollection_AsciiString]


def _strs(seq):
    return [x.ToCString() for x in seq]


def test_sequence_occt_api():
    s = S()
    s.Append(TCollection.TCollection_AsciiString("a"))
    s.Append("b")                                                # implicit str -> TCollection_AsciiString
    s.Prepend("z")
    assert (s.Lower(), s.Upper(), s.Length(), len(s)) == (1, 3, 3, 3)
    assert s.Value(2).ToCString() == "a" and s(2).ToCString() == "a"
    assert s[3].ToCString() == "b"                               # Python addition (1-based, like Value)
    s.ChangeValue(1).AssignCat("!")                              # mutable view for class element types
    assert s.Value(1).ToCString() == "z!"
    s[2] = "B"
    s.Remove(3)
    assert _strs(s) == ["z!", "B"]
    with pytest.raises(Standard.Standard_OutOfRange):
        s.Value(9)


def test_hsequence_is_a_sequence_with_transient_members():
    s = S()
    s.Append("a")
    h = HS()
    h.Append("x")
    h.Append(s)                                                  # Append(SequenceType&)
    assert isinstance(h, S) and h.GetRefCount() == 1
    assert _strs(h) == ["x", "a"]
    assert type(h.Sequence()) is S and h.ChangeSequence() is h
    assert S(h).Length() == 2                                    # HSequence -> Sequence (copy constructor)


def test_sequence_and_list_have_no_pre_8_0_aliases():
    from OCP3x import TColStd
    for gone in ("TColStd_SequenceOfAsciiString", "TColStd_ListOfInteger", "TColStd_HSequenceOfAsciiString"):
        assert not hasattr(TColStd, gone)


def test_occt_method_returning_a_container():
    from OCP3x import Message
    printers = Message.Message.DefaultMessenger_s().Printers()
    assert type(printers).__name__ == "NCollection_Sequence__Handle_Message_Printer"
    assert len(printers) >= 1


# ------------------------------------------------------------------------------------ hashed kinds
Str = TCollection.TCollection_AsciiString


def test_map_set_operations():
    M = NCollection.NCollection_Map[int]
    m = M()
    assert m.Add(1) is True and m.Add(2) is True and m.Add(1) is False
    assert (m.Extent(), len(m)) == (2, 2)
    assert m.Contains(2) is True and (3 in m) is False
    assert sorted(m) == [1, 2]
    other = M()
    other.Add(2)
    other.Add(3)
    u = M()
    u.Union(m, other)
    assert sorted(u) == [1, 2, 3]
    assert m.HasIntersection(other) is True
    assert m.Remove(1) is True and sorted(m) == [2]
    it = M.Iterator(u)
    keys = []
    while it.More():
        keys.append(it.Key())
        it.Next()
    assert sorted(keys) == [1, 2, 3]


def test_datamap_scalar_values():
    D = NCollection.NCollection_DataMap[int, float]
    d = D()
    assert d.Bind(1, 1.5) is True
    d[2] = 2.5
    assert d.Find(1) == 1.5 and d(2) == 2.5 and d[2] == 2.5
    assert d.IsBound(3) is False and (2 in d) is True
    assert d.Seek(3) is None and d.Seek(1) == 1.5                # nullptr -> None, scalar -> value
    assert sorted(d.items()) == [(1, 1.5), (2, 2.5)]
    assert d.TryBound(1, 9.0) == 1.5                             # existing value wins
    assert d.Bound(3, 3.5) == 3.5 and d.UnBind(3) is True
    with pytest.raises(Standard.Standard_NoSuchObject):
        d[7]
    with pytest.raises(KeyError):
        del d[7]


def test_datamap_class_values_are_views():
    D = NCollection.NCollection_DataMap[Str, Str]
    d = D()
    d.Bind("k", "v")                                             # str -> TCollection_AsciiString implicitly
    d.ChangeFind("k").AssignCat("!")
    assert d.Find("k").ToCString() == "v!"
    assert d.Seek("missing") is None
    assert type(d.Seek("k")) is Str


def test_indexed_map():
    IM = NCollection.NCollection_IndexedMap[Str]
    im = IM()
    assert (im.Add("a"), im.Add("b"), im.Add("a")) == (1, 2, 1)
    assert im.FindKey(2).ToCString() == "b" and im(2).ToCString() == "b" and im[2].ToCString() == "b"
    assert im.FindIndex("b") == 2
    assert [k.ToCString() for k in im] == ["a", "b"]
    it = IM.Iterator(im)
    assert (it.Index(), it.Value().ToCString()) == (1, "a")


def test_indexed_data_map():
    IDM = NCollection.NCollection_IndexedDataMap[Str, Str]
    idm = IDM()
    idm.Add("x", "1")
    idm.Add("y", "2")
    assert idm.FindFromKey("y").ToCString() == "2"
    assert idm.FindFromIndex(1).ToCString() == "1" and idm(2).ToCString() == "2" and idm[1].ToCString() == "1"
    assert idm.FindIndex("y") == 2
    assert [(k.ToCString(), v.ToCString()) for k, v in idm.items()] == [("x", "1"), ("y", "2")]
    idm.ChangeFromKey("x").AssignCat("!")
    assert idm.FindFromKey("x").ToCString() == "1!"
    assert idm.Seek("q") is None


def test_map_accessors_and_extra_instantiations():
    assert NCollection.NCollection_Map[int].__name__ == "NCollection_Map__int"
    assert NCollection.NCollection_DataMap[int, float].__name__ == "NCollection_DataMap__int__double"
    assert "NCollection_IndexedMap__TCollection_AsciiString" in NCollection.NCollection_IndexedMap.bound()


# ---------------------------------------------------------------------------- Array2, DynamicArray, DoubleMap, Shared
def test_array2():
    A2 = NCollection.NCollection_Array2[float]
    a = A2(1, 2, 1, 3)
    a.Init(0.0)
    a.SetValue(2, 3, 5.0)
    a[(1, 1)] = 1.0
    assert (a.NbRows(), a.NbColumns(), a.Length(), len(a)) == (2, 3, 6, 6)
    assert a.Value(2, 3) == 5.0 and a(2, 3) == 5.0 and a[(2, 3)] == 5.0
    assert list(a) == [1.0, 0.0, 0.0, 0.0, 0.0, 5.0]             # row-major, inherited from Array1
    assert isinstance(a, NCollection.NCollection_Array1[float])
    assert (a.LowerRow(), a.UpperRow(), a.LowerCol(), a.UpperCol()) == (1, 2, 1, 3)
    h = NCollection.NCollection_HArray2[float](3, 4, 1, 2, 7.0)
    assert h.GetRefCount() == 1 and h.NbRows() == 2 and list(h) == [7.0] * 4
    assert isinstance(h, A2) and type(h.Array2()) is A2 and A2(h).Length() == 4


def test_dynamic_array():
    V = NCollection.NCollection_DynamicArray[int]
    v = V()
    v.Append(10)
    v.Append(20)
    v.Append(30)
    assert list(v) == [10, 20, 30] and (v.Lower(), v.Upper(), len(v)) == (0, 2, 3)
    assert v[1] == 20 and v(1) == 20 and v.Value(1) == 20
    assert v.SetValue(0, 5) == 5
    v.EraseLast()
    assert list(v) == [5, 20]


def test_double_map():
    DM = NCollection.NCollection_DoubleMap[int, TCollection.TCollection_AsciiString]
    dm = DM()
    dm.Bind(1, "one")
    dm.Bind(2, "two")
    assert dm.Find1(1).ToCString() == "one" and dm.Find2("two") == 2
    assert dm.IsBound1(3) is False and dm.IsBound2("two") is True
    assert dm.Seek1(9) is None and dm.Seek2("one") == 1
    assert [(k, s.ToCString()) for k, s in dm.items()] == [(1, "one"), (2, "two")]
    assert [(k, s.ToCString()) for k, s in dm] == [(1, "one"), (2, "two")]


def test_shared_is_the_wrapped_type_plus_transient():
    SM = NCollection.NCollection_Shared[NCollection.NCollection_Map[int]]
    sm = SM()
    sm.Add(3)
    sm.Add(4)
    assert isinstance(sm, NCollection.NCollection_Map[int]) and sorted(sm) == [3, 4] and len(sm) == 2
    assert sm.GetRefCount() == 1 and sm.IsKind("Standard_Transient") is True
    seq = NCollection.NCollection_Sequence[Standard.Standard_Transient]()
    seq.Append(sm)                                                # T is not the offset-0 base here: registry paths
    assert seq.Value(1) is sm and sm.GetRefCount() == 2


def test_linear_vector():
    from OCP3x import BVH, MathRoot, NCollection
    v = NCollection.NCollection_LinearVector[float]()                          # OCCT 8 contiguous vector, 0-based, size_t indices
    v.Append(1.5)
    v.Append(2.5)
    v[0] = 0.5
    assert (len(v), v[1], list(v), v.First(), v.Last()) == (2, 2.5, [0.5, 2.5], 0.5, 2.5)
    assert v.ToArray1().Length() == 2 and v.Capacity() >= 2
    v.Erase(0)
    v.Resize(3, 9.0)
    assert list(v) == [2.5, 9.0, 9.0]
    v.Clear()
    assert v.IsEmpty()
    assert BVH.BVH_Array3d is NCollection.NCollection_LinearVector[BVH.BVH_Vec3d]   # typedef alias of a binder instantiation
    a = BVH.BVH_Array3d()
    a.Append(BVH.BVH_Vec3d(1.0, 2.0, 3.0))
    a.ChangeValue(0).SetValues(4.0, 5.0, 6.0)                                 # reference_internal for class elements
    assert a.Value(0).x() == 4.0
    assert type(MathRoot.MultipleResult().Roots) is NCollection.NCollection_DynamicArray[float]   # container-typed field


def _generics() -> dict[str, type]:
    return {g.__name__: g for g in Generic.__subclasses__()}


def test_every_table_entry_is_a_bound_class_keyed_by_its_element_types():
    """The tables map the element types themselves -- as Python passes them to __class_getitem__: the type for one
    argument, a tuple for several -- to the bound class. A key the generator spelled wrong fails at import, so what
    is left to check is the shape: every key is a type (or a tuple of types), every value is the instantiation
    named after the rule, reachable under its concrete name, and the subscription returns exactly it."""
    generics = _generics()
    assert len(generics) == 15, sorted(generics)
    total = 0
    for name, G in generics.items():
        for key, cls in G._instances.items():
            total += 1
            types = key if isinstance(key, tuple) else (key,)
            assert all(isinstance(t, type) for t in types), (name, key)
            assert cls.__name__.startswith(name + "__"), (name, cls)
            assert getattr(NCollection, cls.__name__) is cls
            assert G[key] is cls
    assert total > 700, f"only {total} instantiations in the tables; did they stop being generated?"


def test_every_instantiation_is_an_instance_of_its_generic():
    """isinstance(x, NCollection_Array1) holds for every instantiation of every template (S1 + ABC, 2026-09-27):
    one rule, decided on the MRO, no exceptions for the kinds whose one nanobind base is already taken by C++."""
    for name, G in _generics().items():
        for cls in G._instances.values():
            assert issubclass(cls, G), (name, cls.__name__)


def test_generic_relations_are_exactly_the_cpp_bases():
    """An instantiation is also an instance of another generic exactly when C++ derives it from one: Array2<T> and
    HArray1<T> from Array1<T>, HArray2<T> from Array2<T>, HSequence<T> from Sequence<T>, and NCollection_Shared<T>
    from T. Anything else would be a false positive of the MRO rule."""
    generics = _generics()
    cpp_bases = {"NCollection_Array2": {"NCollection_Array1"}, "NCollection_HArray1": {"NCollection_Array1"},
                 "NCollection_HArray2": {"NCollection_Array2", "NCollection_Array1"},
                 "NCollection_HSequence": {"NCollection_Sequence"}}
    for name, G in generics.items():
        for cls in G._instances.values():
            also = {o for o, O in generics.items() if O is not G and issubclass(cls, O)}
            if name == "NCollection_Shared":                    # Shared<T> : Standard_Transient, T
                t = cls.__mro__[1] if cls.__mro__[1] is not object else None
                assert also == {o for o, O in generics.items() if O is not G and t is not None and issubclass(t, O)}, cls
            else:
                assert also == cpp_bases.get(name, set()), (cls.__name__, also)


def test_isinstance_against_the_generic_classes():
    from OCP3x.gp import gp_Pnt
    a = NCollection.NCollection_Array1[gp_Pnt](1, 3)
    h = NCollection.NCollection_HArray1[float](1, 3)
    a2 = NCollection.NCollection_Array2[float](1, 2, 1, 2)
    h2 = NCollection.NCollection_HArray2[float](1, 2, 1, 2)
    hs = NCollection.NCollection_HSequence[float]()
    lst = NCollection.NCollection_List[gp_Pnt]()
    assert isinstance(a, NCollection.NCollection_Array1) and not isinstance(a, NCollection.NCollection_HArray1)
    assert isinstance(h, NCollection.NCollection_HArray1) and isinstance(h, NCollection.NCollection_Array1)
    assert not isinstance(h, NCollection.NCollection_Array2)
    assert isinstance(a2, NCollection.NCollection_Array2) and isinstance(a2, NCollection.NCollection_Array1)
    assert not isinstance(a2, NCollection.NCollection_HArray2)
    assert all(isinstance(h2, G) for G in (NCollection.NCollection_HArray2, NCollection.NCollection_Array2, NCollection.NCollection_Array1))
    assert isinstance(hs, NCollection.NCollection_HSequence) and isinstance(hs, NCollection.NCollection_Sequence)
    assert isinstance(lst, NCollection.NCollection_List) and not isinstance(lst, NCollection.NCollection_Array1)
    assert not isinstance(1.0, NCollection.NCollection_Array1)
    assert isinstance(a, NCollection.NCollection_Array1[gp_Pnt])           # the subscription *is* the class


def test_generic_subscription_errors():
    from OCP3x.gp import gp_Pnt
    from OCP3x.TopoDS import TopoDS_Shape
    from OCP3x.TopTools import TopTools_ShapeMapHasher
    with pytest.raises(TypeError, match=r"NCollection_Array1\[gp_Pnt, gp_Pnt\] is not bound"):
        NCollection.NCollection_Array1[gp_Pnt, gp_Pnt]
    with pytest.raises(TypeError, match=r"NCollection_DataMap\[int\] is not bound"):
        NCollection.NCollection_DataMap[int]
    with pytest.raises(TypeError, match="unhashable"):
        NCollection.NCollection_Array1[[gp_Pnt]]
    with pytest.raises(TypeError, match="class template"):
        NCollection.NCollection_Map()
    three = NCollection.NCollection_IndexedDataMap[TopoDS_Shape, NCollection.NCollection_List[TopoDS_Shape], TopTools_ShapeMapHasher]
    assert three is NCollection.NCollection_IndexedDataMap__TopoDS_Shape__NCollection_List__TopoDS_Shape__TopTools_ShapeMapHasher
