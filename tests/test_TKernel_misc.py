"""Generated bindings for the remaining TKernel packages."""
import importlib

import pytest

from nanoocp import Message, NCollection, OSD, Precision, Quantity, TCollection

PACKAGES = ["FSD", "OSD", "Plugin", "Quantity", "Resource", "Standard", "StdFail", "Storage", "TColStd", "TCollection",
            "TShort", "Units", "UnitsAPI", "UnitsMethods", "NCollection", "Message", "FlexLexer", "Precision"]


@pytest.mark.parametrize("pkg", PACKAGES)
def test_every_package_imports(pkg):
    m = importlib.import_module(f"nanoocp.{pkg}")
    assert m.__name__ == f"nanoocp.{pkg}"


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
    assert Precision.Precision.Confusion() == 1e-7
    c = Quantity.Quantity_Color(1.0, 0.0, 0.0, Quantity.Quantity_TypeOfColor.Quantity_TOC_RGB)
    assert (c.Red(), c.Green(), c.Blue()) == (1.0, 0.0, 0.0)
    assert Quantity.Quantity_Color.StringName(c.Name()) == "RED"


def test_singletons_are_transient_handles():
    assert type(Message.Message.DefaultMessenger()).__name__ == "Message_Messenger"
    a = NCollection.NCollection_BaseAllocator.CommonBaseAllocator()
    assert a.GetRefCount() >= 1


def test_static_suffix_rule_in_tcollection():
    assert TCollection.TCollection_AsciiString.IsEqual_s(TCollection.TCollection_AsciiString("a"), TCollection.TCollection_AsciiString("a")) is True


def test_extended_string_round_trip():
    from nanoocp import TCollection
    e = TCollection.TCollection_ExtendedString("héllo €", True)               # from UTF-8
    assert e.Length() == 7
    assert e.ToExtString() == "héllo €"                                       # const char16_t* -> str (UTF-16 caster)
    assert e.Value(2) == "é"                                                  # char16_t -> 1-character str
    e2 = TCollection.TCollection_ExtendedString()
    e2.AssignCat("x€")                                                        # str -> const char16_t*
    assert e2.ToExtString() == "x€" and e2.Search("€") == 2
