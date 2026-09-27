"""Generated bindings for TKXSBase (DataExchange: Interface, Transfer, IFGraph, IFSelect, TransferBRep, XSControl,
XSAlgo, MoniTool): the exchange kernel every format toolkit builds on -- the static parameters CadQuery sets before a
STEP write, the work session, the transfer processes and binders, the check machinery. The norms themselves
(STEPControl_Controller & co.) arrive with TKDESTEP, so a work session has no controller here."""
import importlib

import pytest

from conftest import report

from OCP3x.BRepGProp import BRepGProp
from OCP3x.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCP3x.DE import DE_ShapeFixParameters, DE_Wrapper
from OCP3x.IFSelect import (IFSelect_RetDone, IFSelect_RetError, IFSelect_ReturnStatus, IFSelect_SessionPilot,
                              IFSelect_WorkSession)
from OCP3x.Interface import (Interface_Check, Interface_CheckIterator, Interface_EntityIterator, Interface_MSG,
                               Interface_Static)
from OCP3x.GProp import GProp_GProps
from OCP3x.Message import Message_ProgressRange
from OCP3x.MoniTool import MoniTool_AttrList
from OCP3x.ShapeProcess import ShapeProcess
from OCP3x.Standard import Standard_DomainError
from OCP3x.Transfer import Transfer_ActorOfTransientProcess, Transfer_FinderProcess, Transfer_TransientProcess
from OCP3x.TransferBRep import TransferBRep_ShapeBinder
from OCP3x.XSAlgo import XSAlgo_ShapeProcessor
from OCP3x.XSControl import XSControl_Reader, XSControl_WorkSession
from pathlib import Path

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKXSBase" / "report.txt"


@pytest.mark.parametrize("pkg", ["Interface", "Transfer", "IFGraph", "IFSelect", "TransferBRep", "XSControl",
                                 "XSAlgo", "MoniTool"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"OCP3x.{pkg}").__name__ == f"OCP3x.{pkg}"


def test_interface_static_is_what_cadquery_sets():
    """CadQuery writes STEP after Interface_Static.SetIVal_s/SetCVal_s (shapes.py:560-563); in OCP3x the names carry
    no _s (R-STATIC-S: no instance method of that name). A parameter must be declared before it can be set -- the STEP
    names come from STEPControl_Controller::Init (TKDESTEP), so this test declares its own."""
    assert Interface_Static.SetIVal_s("OCP3x.undeclared", 1) is False
    assert Interface_Static.Init_s("OCP3x", "OCP3x.test.int", "i", "0")        # char type, 1-character str (R-CHAR)
    assert Interface_Static.Init_s("OCP3x", "OCP3x.test.unit", "t", "MM")
    assert Interface_Static.SetIVal_s("OCP3x.test.int", 42) and Interface_Static.IVal_s("OCP3x.test.int") == 42
    assert Interface_Static.SetCVal_s("OCP3x.test.unit", "INCH") and Interface_Static.CVal_s("OCP3x.test.unit") == "INCH"
    assert Interface_Static.IsPresent_s("OCP3x.test.int") and Interface_Static.IsSet_s("OCP3x.test.int")
    assert Interface_Static.Static_s("OCP3x.test.int").Type() is not None
    assert Interface_Static.Items_s().Length() >= 2


def test_return_status_enum():
    """CadQuery compares against IFSelect_RetDone at module level (importers/assembly.py:159), R-ENUM."""
    assert IFSelect_ReturnStatus.IFSelect_RetDone is IFSelect_RetDone and int(IFSelect_RetDone) == 1
    assert IFSelect_RetError != IFSelect_RetDone


def test_work_session_without_a_norm():
    ws = XSControl_WorkSession()
    assert type(ws).__mro__[1].__name__ == "IFSelect_WorkSession"                # XSControl_WorkSession : IFSelect_WorkSession
    assert ws.NormAdaptor() is None and ws.Model() is None                       # null handle -> None (R-HANDLE)
    assert ws.TransferReader() is not None and ws.TransferWriter() is not None
    reader = XSControl_Reader(ws, False)
    assert reader.WS() is ws                                                     # the same Transient comes back
    # without a model the session has no graph: OCCT throws, and the exception arrives as its C++ type (4.2)
    with pytest.raises(Standard_DomainError, match="Graph not available"):
        reader.NbRootsForTransfer()


def test_transfer_processes_and_the_shape_binder():
    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    binder = TransferBRep_ShapeBinder(box)
    assert binder.HasResult() and binder.ResultTypeName() == "TopoDS_Solid"
    assert not binder.Result().IsNull()
    process = Transfer_TransientProcess(10)
    assert process.NbMapped() == 0
    assert Transfer_FinderProcess(10).NbMapped() == 0


def test_check_machinery_iterates():
    check = Interface_Check()
    check.AddFail("a failure")
    check.AddWarning("a warning")
    assert (check.NbFails(), check.NbWarnings()) == (1, 1)
    assert check.CFail(1) == "a failure" and check.CWarning(1) == "a warning"
    checks = Interface_CheckIterator()
    checks.Add(check, 1)
    assert [type(c).__name__ for c in checks] == ["Interface_Check"]             # R-ITER on More/Next/Value
    assert list(Interface_EntityIterator()) == []


def test_the_shape_processor_takes_the_de_parameters():
    """XSAlgo_ShapeProcessor's DE_ShapeFixParameters constructor has a `= {}` default (R-DEFAULT list-initialises a
    braced default) and nanobind converts it at .def time, so _TKXSBase imports _TKDE although OCCT's EXTERNLIB does
    not link it (R-LINK)."""
    processor = XSAlgo_ShapeProcessor(DE_ShapeFixParameters())
    assert type(processor).__name__ == "XSAlgo_ShapeProcessor"
    assert "OCP3x._TKDE" in Path(__file__).parents[1].joinpath("src/cpp/TKXSBase/_TKXSBase.cpp").read_text()
    assert hasattr(XSControl_Reader, "SetShapeFixParameters")


def test_the_work_session_closes_tkde_signatures():
    """TKDE's Read/Write name XSControl_WorkSession; until this toolkit the stubs spelled it as an unresolved string."""
    assert "OCP3x.XSControl.XSControl_WorkSession" in DE_Wrapper.Read.__doc__
    assert '"XSControl_WorkSession"' not in Path(__file__).parents[1].joinpath("src/OCP3x/DE.pyi").read_text()


def test_the_string_out_parameters_have_named_alternatives():
    """const char*& out-parameters cannot be bound (R-UNSUPPORTED); OCCT has a value-returning twin for the ones a
    user reaches for (2d)."""
    attrs = MoniTool_AttrList()
    attrs.SetStringAttribute("a", "hello")
    assert attrs.StringAttribute("a") == "hello"
    assert not hasattr(attrs, "GetStringAttribute")
    assert Interface_MSG("key", 3).Value() == "key"                              # operator const char* is skipped
    assert not any("operator const char" in name for name in dir(Interface_MSG))


def test_session_pilot():
    pilot = IFSelect_SessionPilot("OCP3x> ")
    assert pilot.Session() is None                                               # no session until SetSession (1:1)
    session = IFSelect_WorkSession()
    pilot.SetSession(session)
    assert pilot.Session() is session and pilot.RecordMode() is False


def test_the_shape_process_flags_are_a_set_of_operations():
    """R-BITSET: ShapeProcess::OperationsFlags is a std::bitset indexed by ShapeProcess::Operation; Python passes and
    receives the set of enumerators (nanobind's arithmetic enums are IntEnums, so the plain ints that come back
    compare equal). The flags live on the transfer actor -- XSControl_Reader forwards to it and has none without a
    norm, so the round trip is tested where OCCT stores it (XSControl_Reader.cxx)."""
    actor = Transfer_ActorOfTransientProcess()
    assert actor.GetProcessingFlags() == (set(), False)
    flags = {ShapeProcess.FixShape, ShapeProcess.SameParameter}
    actor.SetProcessingFlags(flags)
    stored, used = actor.GetProcessingFlags()
    assert stored == flags and stored == {1, 15} and used is True
    actor.SetProcessingFlags([0, 1])                                             # any iterable of indices is accepted
    assert actor.GetProcessingFlags()[0] == {ShapeProcess.DirectFaces, ShapeProcess.SameParameter}
    for bad in ({99}, "FixShape", {-1}, {"FixShape"}):
        with pytest.raises(TypeError):
            actor.SetProcessingFlags(bad)
    processor = XSAlgo_ShapeProcessor(DE_ShapeFixParameters())
    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    processed = processor.ProcessShape(box, {ShapeProcess.FixShape}, Message_ProgressRange())
    properties = GProp_GProps()
    BRepGProp.VolumeProperties_s(processed, properties)
    assert properties.Mass() == pytest.approx(6.0)                               # a clean box survives unchanged


def test_report_categories():
    _, lines, undefined, _ = report("TKXSBase")
    assert all(any(k in line for k in ("IFSelect_", "MoniTool_Element::", "TransferBRep::")) for line in undefined)
    assert len(lines) == 40
    counts: dict[str, int] = {}
    for line in lines:
        counts[line.split("\t")[0]] = counts.get(line.split("\t")[0], 0) + 1
    assert counts == {"raw-pointer": 19, "overload-collision": 9, "iterator": 5,
                      "rvalue": 3, "template": 3, "conversion": 1}
    assert not any("bitset" in line for line in lines)                           # closed by R-BITSET (2026-09-22)
    # the rvalue lines are the && twins of bound const& overloads, so nothing is lost
    assert all("SetShapeFixParameters" in line for line in lines if line.startswith("rvalue"))
