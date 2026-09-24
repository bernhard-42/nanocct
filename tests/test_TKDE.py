"""Generated bindings for TKDE (DataExchange: the DE package): the format-agnostic transfer framework OCCT 8 puts in
front of STEP/IGES/STL/glTF -- DE_Wrapper with its configuration nodes and providers, the shape-healing parameter
struct every reader shares, and the content probe that reads a CAD file's first bytes. The providers themselves arrive
with their own toolkits (TKDESTEP & co.), so DE_Wrapper finds none here."""
import importlib
import io
from pathlib import Path

import pytest

from conftest import report

from nanoocp.DE import (DE_ConfigurationContext, DE_ConfigurationNode, DE_Provider, DE_ShapeFixConfigurationNode,
                        DE_ShapeFixParameters, DE_ValidationUtils, DE_Wrapper)
from nanoocp.NCollection import NCollection_Buffer
from nanoocp.TCollection import TCollection_AsciiString
from nanoocp.TopAbs import TopAbs_ShapeEnum
from nanoocp.TopoDS import TopoDS_Shape

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKDE" / "report.txt"


def test_package_imports():
    assert importlib.import_module("nanoocp.DE").__name__ == "nanoocp.DE"


def test_shape_fix_parameters_is_a_plain_struct():
    """DE_ShapeFixParameters: 60 public fields, the FixMode enum class nested as in C++ (R-ENUM, R-FIELD)."""
    p = DE_ShapeFixParameters()
    assert p.Tolerance3d == pytest.approx(1.0e-6) and p.MaxTolerance3d == pytest.approx(1.0)
    assert p.DetalizationLevel == TopAbs_ShapeEnum.TopAbs_VERTEX
    assert p.NonManifold is False
    assert [m.name for m in DE_ShapeFixParameters.FixMode] == ["FixOrNot", "NotFix", "Fix"]
    assert p.FixFreeShellMode == DE_ShapeFixParameters.FixMode.FixOrNot
    assert p.AutoCorrectPrecisionMode == DE_ShapeFixParameters.FixMode.Fix       # OCCT's own default
    p.Tolerance3d = 1.0e-4
    p.FixFreeShellMode = DE_ShapeFixParameters.FixMode.Fix
    assert p.Tolerance3d == pytest.approx(1.0e-4) and p.FixFreeShellMode == DE_ShapeFixParameters.FixMode.Fix


def test_configuration_context_reads_a_resource_string():
    ctx = DE_ConfigurationContext()
    assert ctx.LoadStr("provider.a.real : 2.5\nprovider.a.int : 7\nprovider.a.bool : 1\nprovider.a.str : hello\n")
    assert ctx.GetInternalMap().Extent() == 4
    assert ctx.IsParamSet("real", "provider.a")
    assert ctx.RealVal("real", 0.0, "provider.a") == pytest.approx(2.5)
    assert ctx.IntegerVal("int", 0, "provider.a") == 7
    assert ctx.BooleanVal("bool", False, "provider.a") is True
    assert ctx.StringVal("str", "", "provider.a").ToCString() == "hello"
    assert ctx.GetReal("real", "provider.a") == (True, 2.5)                      # double& -> returned (R-OUT)
    value = TCollection_AsciiString()
    assert ctx.GetString("str", value, "provider.a") and value.ToCString() == "hello"   # class ref filled in place (R-REF-CLASS)
    assert ctx.GetReal("missing", "provider.a") == (False, 0.0)


def test_wrapper_configuration():
    global_wrapper = DE_Wrapper.GlobalWrapper()
    assert isinstance(global_wrapper, DE_Wrapper)
    assert DE_Wrapper.GlobalWrapper() is global_wrapper                          # the same Transient comes back (handle caster)
    own = DE_Wrapper()
    assert own is not global_wrapper and own.Nodes().Extent() == 0
    text = own.Save()
    assert text.ToCString().startswith("!Description of the config file for DE toolkit")
    assert isinstance(own.Copy(), DE_Wrapper)
    assert own.Find("STEP", "OCC") == (False, None)                              # handle<node>& -> returned (R-OUT-HANDLE)
    assert own.FindProvider("box.stp", True) == (False, None)                    # no provider toolkit is generated yet


def test_the_work_session_stays_a_parameter():
    """handle<XSControl_WorkSession>& theWS is documented @param[in] and read by the call (personizeWS:
    theWS->NormAdaptor(), DESTEP_Provider.cxx:692-707), so it is in/out: the parameter stays and is returned
    (overrides.toml [inout]). Without that it would be a pure out-parameter and all eight Read/Write overloads
    of each class would collide into Read__XSControl_WorkSession (16 report lines)."""
    for cls in (DE_Provider, DE_Wrapper):
        assert not hasattr(cls, "Read__XSControl_WorkSession") and not hasattr(cls, "Write__XSControl_WorkSession")
    doc = DE_Wrapper.Read.__doc__
    assert "theWS: nanoocp.XSControl.XSControl_WorkSession | None" in doc      # the type resolves since TKXSBase
    assert "-> tuple[bool, nanoocp.XSControl.XSControl_WorkSession]" in doc
    wrapper = DE_Wrapper()
    # no provider is registered, so DE_Wrapper::Read fails before it touches the session: it comes back unchanged (None)
    assert wrapper.Read("box.stp", TopoDS_Shape(), None) == (False, None)
    assert wrapper.Write("box.stp", TopoDS_Shape(), None) == (False, None)


def test_content_buffer_reads_bytes():
    """DE is a binary-stream package (overrides.toml [stream] binary_packages): CreateContentBuffer reads 2048 raw
    bytes for the format probe (DE_ValidationUtils.cxx:317-339), the path overload opens std::ios::binary."""
    assert "theStream: typing.BinaryIO" in DE_ValidationUtils.CreateContentBuffer.__doc__
    ok, buffer = DE_ValidationUtils.CreateContentBuffer(io.BytesIO(b"ISO-10303-21;\nHEADER;\x00\xff"))
    assert ok and isinstance(buffer, NCollection_Buffer) and buffer.Size() == 2048
    assert DE_Wrapper().FindReadProvider("box.stp", io.BytesIO(b"ISO-10303-21;")) == (False, None)
    with pytest.raises(TypeError):
        DE_ValidationUtils.CreateContentBuffer(io.StringIO("ISO-10303-21;"))     # a text file-like falls through
    assert DE_ValidationUtils.CreateContentBuffer("does-not-exist.stp") == (False, None)
    assert DE_ValidationUtils.ValidateFileForReading("does-not-exist.stp", "ctx") is False


def test_the_abstract_bases_have_no_constructor():
    """DE_Provider, DE_ConfigurationNode and DE_ShapeFixConfigurationNode leave pure virtuals of DE_ConfigurationNode
    unimplemented, so clang emits no complete-object constructor (C1) for them and the nm check reports the declared
    ones as undefined -- the outcome an abstract class gets anyway. Providers are subclasses in the format toolkits."""
    for cls in (DE_Provider, DE_ConfigurationNode, DE_ShapeFixConfigurationNode):
        with pytest.raises(TypeError, match="no constructor defined"):
            cls()
    # DE_PluginHolder<T> is the C++ registration idiom (a static holder per provider) and stays unbound: from Python a
    # node registers itself the way that template's constructor does (DE_ConfigurationNode.cxx: Register -> Bind).
    assert hasattr(DE_ConfigurationNode, "Register") and hasattr(DE_Wrapper, "Bind")


def test_report_is_the_expected_portable_lines():
    _, lines, undefined, _ = report("TKDE")
    assert len(lines) == 7
    # every undefined entry is a constructor OCCT declares but does not define (Unix reports them, Windows exports
    # nothing for them either, and a platform that defines them reports none): checked by content, not by count
    assert all("DE_ConfigurationNode::" in line or "DE_Provider::" in line
               or "DE_ShapeFixConfigurationNode::" in line for line in undefined)
    kinds = sorted(line.split("\t")[0] for line in lines)
    assert kinds == ["std"] + ["stream"] * 4 + ["template"] * 2
    # the stream nodes hold a stream reference beyond the call, so the stream-based Read/Write overloads stay unusable (2d)
    assert sum("StreamNode" in line for line in lines) == 4
    assert sum("DE_PluginHolder" in line or "DE_MultiPluginHolder" in line for line in lines) == 2
    assert any(line.endswith("unsupported std type: std::mutex") for line in lines)
