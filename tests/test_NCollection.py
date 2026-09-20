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


def test_harray1_is_transient_with_full_array_api():
    h = H(1, 2)
    assert isinstance(h, Standard.Standard_Transient)
    assert h.GetRefCount() == 1
    assert h.DynamicType().Name() == "NCollection_HArray1"
    assert h.Length() == 2 and len(h) == 2 and h.Value(1) is None
    assert not isinstance(h, AH)                               # single-inheritance limitation, documented
    assert type(h.Array1()) is AH                              # sliced copy of the array part
    assert h.ChangeArray1() is h                               # mutable view = the object itself


def test_harray1_converts_implicitly_to_array1():
    h = H(1, 2)
    assert type(AH(h)) is AH
    b = AH()
    b.Assign(h)                                                # C++: const NCollection_Array1<T>& parameter
    assert b.Length() == 2


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
        NCollection.NCollection_Array1[int]
    with pytest.raises(TypeError, match="template"):
        NCollection.NCollection_Array1(1, 2)
    assert "NCollection_Array1__double" in NCollection.NCollection_Array1.bound()
