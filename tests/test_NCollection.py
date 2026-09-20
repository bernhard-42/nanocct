"""Hand-written NCollection binders (Design.md 6a): Array1 / HArray1, instantiated by the generator."""
import pytest

from nanoocp import NCollection, Standard, TColStd

A = NCollection.NCollection_Array1__double                         # home = element type's package (double -> Standard)
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


def test_deprecated_typedef_alias():
    assert TColStd.TColStd_Array1OfReal is A
    a = TColStd.TColStd_Array1OfReal(1, 3)
    a.Init(2.5)
    assert list(a) == [2.5, 2.5, 2.5]


def test_docstrings_come_from_the_template_header():
    assert "Constant value access" in A.Value.__doc__
    assert "unidimensional arrays" in A.__doc__
    assert "Python addition" in A.__len__.__doc__


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


# ------------------------------------------------------------------------------------------ Sequence
from nanoocp import TCollection  # noqa: E402

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


def test_sequence_and_list_aliases():
    from nanoocp import TColStd
    assert TColStd.TColStd_SequenceOfAsciiString is S
    assert TColStd.TColStd_ListOfInteger is L
    assert TColStd.TColStd_HSequenceOfAsciiString is HS


def test_occt_method_returning_a_container():
    from nanoocp import Message
    printers = Message.Message.DefaultMessenger().Printers()
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
    from nanoocp import BVH, MathRoot, NCollection
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
