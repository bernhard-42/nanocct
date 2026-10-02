"""Generated bindings for the remaining TKernel packages."""
import importlib

import pytest

from nanocct import Message, NCollection, OSD, Precision, Quantity, TCollection, TColStd

PACKAGES = ["FSD", "OSD", "Plugin", "Quantity", "Resource", "Standard", "StdFail", "Storage", "TColStd", "TCollection",
            "TShort", "Units", "UnitsAPI", "UnitsMethods", "NCollection", "Message", "FlexLexer", "Precision"]


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    m = importlib.import_module(f"nanocct.{pkg}")
    assert m.__name__ == f"nanocct.{pkg}"


def test_ascii_string():
    s = TCollection.TCollection_AsciiString("Hello")
    s.AssignCat(" World")
    assert s.ToCString() == "Hello World"
    assert s.Length() == 11
    assert s.IsEqual("Hello World") is True
    assert s.Token(" ", 2).ToCString() == "World"


def test_extended_string_and_replacement():
    e = TCollection.TCollection_ExtendedString("a€b", True)
    assert e.Length() == 3
    assert TCollection.TCollection_AsciiString(e, "?").ToCString() == "a?b"   # char parameter takes a 1-char str


def test_implicit_conversion_str_to_ascii_string():
    p = OSD.OSD_Path("/tmp/x/y.txt")                     # OSD_Path(const TCollection_AsciiString&)
    assert p.Name().ToCString() == "y"
    assert p.Extension().ToCString() == ".txt"


def test_transient_string_is_handle_managed():
    h = TCollection.TCollection_HAsciiString("shared")
    assert h.ToCString() == "shared"
    assert h.IsKind("Standard_Transient") is True
    assert h.GetRefCount() == 1


def test_precision_and_color():
    assert Precision.Precision.Confusion_s() == 1e-7
    c = Quantity.Quantity_Color(1.0, 0.0, 0.0, Quantity.Quantity_TypeOfColor.Quantity_TOC_RGB)
    assert (c.Red(), c.Green(), c.Blue()) == (1.0, 0.0, 0.0)
    assert Quantity.Quantity_Color.StringName_s(c.Name()) == "RED"


def test_singletons_are_transient_handles():
    assert type(Message.Message.DefaultMessenger_s()).__name__ == "Message_Messenger"
    a = NCollection.NCollection_BaseAllocator.CommonBaseAllocator_s()
    assert a.GetRefCount() >= 1


def test_static_suffix_rule_in_tcollection():
    assert TCollection.TCollection_AsciiString.IsEqual_s(TCollection.TCollection_AsciiString("a"), TCollection.TCollection_AsciiString("a")) is True


def test_extended_string_round_trip():
    from nanocct import TCollection
    e = TCollection.TCollection_ExtendedString("héllo €", True)               # from UTF-8
    assert e.Length() == 7
    assert e.ToExtString() == "héllo €"                                       # const char16_t* -> str (UTF-16 caster)
    assert e.Value(2) == "é"                                                  # char16_t -> 1-character str
    e2 = TCollection.TCollection_ExtendedString()
    e2.AssignCat("x€")                                                        # str -> const char16_t*
    assert e2.ToExtString() == "x€" and e2.Search("€") == 2


def test_value_eq_without_a_hash_is_unhashable():
    """R-UNHASHABLE (2026-09-25): a class with a value __eq__ and no hash must be unhashable.

    nanobind never touches tp_hash, and Python's "define __eq__ and __hash__ becomes None" rule fires only at type
    creation -- a .def() after it does not trigger it. So without the explicit nb::none() these classes kept
    object.__hash__ and `a == b` held while `hash(a) != hash(b)`, which makes a dict or set lookup by an equal value
    miss without raising. Python's own answer for such a class is to be unhashable, which at least fails loudly.
    """
    from nanocct import Bnd, Quantity, TopExp, TopLoc
    a, b = Bnd.Bnd_Range(0.0, 1.0), Bnd.Bnd_Range(0.0, 1.0)
    assert a == b and Bnd.Bnd_Range.__hash__ is None
    with pytest.raises(TypeError, match="unhashable type"):
        hash(a)
    with pytest.raises(TypeError, match="unhashable type"):
        {a: 1}                                                                  # noqa: B018 -- the point is the raise
    assert Quantity.Quantity_Date.__hash__ is None                              # a plain value class
    assert Quantity.NCollection_Vec3__float.__hash__ is None                    # and a 7c instantiation (owned by Quantity)
    # a class OCCT *does* give a hash keeps it, value equality and all (the .lxx specialisation above)
    assert TopLoc.TopLoc_Location.__hash__ is not None
    # R-ITERATOR: the ForwardRangeIterator/Sentinel pair -- the one OCCT case of an __eq__ against another type only -- is
    # not bound at all (tests/test_generator.py covers that rule with a synthetic pair)
    assert not hasattr(TopExp, "NCollection_ForwardRangeIterator__TopExp_Explorer")


def test_lxx_hash_and_free_functions_are_bound():
    """OCCT keeps std::hash<TCollection_AsciiString> and TopLoc_Location's ShallowDump in the .lxx part of the header;
    those file-scope declarations belong to the package since 2026-09-22 (they were missed before: equal strings hashed
    by identity)."""
    from nanocct import TopLoc, math
    a, b = TCollection.TCollection_AsciiString("abc"), TCollection.TCollection_AsciiString("abc")
    assert a == b and hash(a) == hash(b) and {a: 1}[b] == 1
    assert hash(a) != hash(TCollection.TCollection_AsciiString("abd"))
    assert TCollection.IsEqual(a, b) is True                                    # inline free function of the .lxx
    # std::hash<handle<TCollection_HAsciiString>> / equal_to<handle<...>> in the same .lxx are specialisations on the handle,
    # not on the class: HAsciiString objects have no value __eq__ and keep the identity hash (consistent, not by value)
    h = TCollection.TCollection_HAsciiString("abc")
    assert (h == TCollection.TCollection_HAsciiString("abc")) is False and hash(h) == hash(h)
    loc = TopLoc.TopLoc_Location()
    assert hash(loc) == hash(TopLoc.TopLoc_Location()) and TopLoc.ShallowDump(loc).startswith("TopLoc_Location")
    m = math.math_Matrix(1, 2, 1, 2, 1.0)
    assert (2.0 * m)(1, 1) == 2.0                                               # friend operator*(double, math_Matrix) defined in the .lxx


def test_messages_are_collected_not_subclassed():
    """Excluded.md: Python cannot subclass Message_Printer/Message_ProgressIndicator (no trampolines, 8.5 not
    planned), but OCCT's own Message_PrinterToReport collects messages for reading back."""
    from nanocct.Message import (Message, Message_Fail, Message_Printer, Message_PrinterOStream, Message_PrinterToReport,
                                 Message_ProgressIndicator, Message_Warning)
    from nanocct.TCollection import TCollection_AsciiString

    for base in (Message_Printer, Message_ProgressIndicator):
        class Sub(base):
            pass
        with pytest.raises(TypeError, match="no constructor defined"):
            Sub()

    messenger = Message.DefaultMessenger_s()
    saved = list(messenger.Printers())              # restored afterwards: the default messenger is process-wide
    try:
        messenger.RemovePrinters(Message_PrinterOStream.get_type_descriptor_s())
        printer = Message_PrinterToReport()
        messenger.AddPrinter(printer)
        messenger.Send(TCollection_AsciiString("first warning"), Message_Warning)
        messenger.Send(TCollection_AsciiString("a failure"), Message_Fail)
        report = printer.Report()
        assert [a.GetMessageKey() for a in report.GetAlerts(Message_Warning)] == ["first warning"]
        assert report.GetAlerts(Message_Fail).Size() == 1
        assert report.Dump(Message_Warning) == "first warning\n"
    finally:
        messenger.RemovePrinters(Message_PrinterToReport.get_type_descriptor_s())
        messenger.RemovePrinters(Message_PrinterOStream.get_type_descriptor_s())
        for saved_printer in saved:
            messenger.AddPrinter(saved_printer)


def test_packed_map_iterator_is_bound_under_the_alias():
    """nested classes of an instantiation bound under an alias were not added to the IR at all
    (TColStd_PackedMapOfInteger = NCollection_PackedMap<int>). Its Iterator has Key(), not Value(), so R-ITER gives it no
    __iter__: More/Next/Key as in C++."""
    packed = TColStd.TColStd_PackedMapOfInteger()
    for k in (9, 4, 16):
        packed.Add(k)
    it, keys = TColStd.TColStd_PackedMapOfInteger.Iterator(packed), []
    while it.More():
        keys.append(it.Key())
        it.Next()
    assert sorted(keys) == [4, 9, 16]
