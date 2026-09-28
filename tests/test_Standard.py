"""Generated bindings for OCCT package Standard (toolkit TKernel): exceptions, Transient, free functions."""
import pytest

from nanocct import Standard, StdFail, gp


def test_exception_hierarchy_mirrors_occt():
    mro = [c.__name__ for c in Standard.Standard_OutOfRange.__mro__]
    assert mro[:5] == ["Standard_OutOfRange", "Standard_RangeError", "Standard_DomainError", "Standard_Failure", "RuntimeError"]
    assert issubclass(StdFail.StdFail_NotDone, Standard.Standard_Failure)          # other package, same toolkit
    assert issubclass(gp.gp_VectorWithNullMagnitude, Standard.Standard_DomainError)  # other toolkit


def test_cpp_exception_arrives_as_its_dynamic_type():
    with pytest.raises(Standard.Standard_OutOfRange):
        gp.gp_Pnt().Coord(9)
    with pytest.raises(Standard.Standard_ConstructionError, match="zero norm"):
        gp.gp_Dir(0.0, 0.0, 0.0)
    with pytest.raises(gp.gp_VectorWithNullMagnitude):                            # header-only exception class
        gp.gp_Vec(1.0, 0.0, 0.0).Angle(gp.gp_Vec(0.0, 0.0, 0.0))
    with pytest.raises(Standard.Standard_Failure):                                # base catches derived
        gp.gp_Pnt().Coord(9)


def test_exception_raised_from_python():
    with pytest.raises(Standard.Standard_Failure) as info:
        raise Standard.Standard_NoSuchObject("nope")
    assert type(info.value) is Standard.Standard_NoSuchObject
    assert str(info.value) == "nope"


def test_transient_identity_and_refcount():
    t = Standard.Standard_Transient()
    assert t.GetRefCount() == 1                 # the Python holder
    assert t.This() is t                        # raw pointer return wrapped in a handle -> same Python object
    assert t.GetRefCount() == 1
    assert t.DynamicType().Name() == "Standard_Transient"
    assert t.IsKind("Standard_Transient") is True
    assert Standard.Standard_Transient.get_type_descriptor_s().Name() == "Standard_Transient"


def test_free_functions():
    assert Standard.Sqrt(16.0) == 4.0
    assert Standard.Max(1, 2) == 2
    assert Standard.IsDigit("7") is True
    assert Standard.RealLast() > 1e300


def test_guid():
    assert Standard.Standard_GUID("00000000-0000-0000-0000-000000000000").IsSame(Standard.Standard_GUID()) is True
