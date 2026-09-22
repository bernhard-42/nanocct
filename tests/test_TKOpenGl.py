"""Generated bindings for TKOpenGl (Visualization: the OpenGl package): OCCT's OpenGL graphic driver. With it a
V3d_Viewer has a real driver, so AIS_InteractiveContext.Display() works instead of dereferencing a null one -- the
single biggest limitation nanoOCP carried until 2026-09-22. Rendering to an image still needs a drawable, which a
virtual window does not provide on macOS; the test pins that boundary down."""
import importlib
from pathlib import Path

import pytest

from nanoocp import Message
from nanoocp.AIS import AIS_InteractiveContext, AIS_Shape
from nanoocp.Aspect import Aspect_DisplayConnection, Aspect_NeutralWindow
from nanoocp.Cocoa import Cocoa_Window
from nanoocp.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanoocp.Graphic3d import Graphic3d_BT_RGB
from nanoocp.Image import Image_PixMap
from nanoocp.OpenGl import OpenGl_Caps, OpenGl_Context, OpenGl_GraphicDriver
from nanoocp.V3d import V3d_Viewer

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKOpenGl" / "report.txt"


@pytest.fixture
def quiet_messenger():
    """A context without a drawable prints GL errors; the test asserts the return values instead."""
    printers = list(Message.Message.DefaultMessenger().Printers())
    levels = [p.GetTraceLevel() for p in printers]
    for p in printers:
        p.SetTraceLevel(Message.Message_Fail)
    yield
    for p, level in zip(printers, levels):
        p.SetTraceLevel(level)


@pytest.fixture
def driver():
    return OpenGl_GraphicDriver(Aspect_DisplayConnection())


@pytest.mark.parametrize("pkg", ["OpenGl", "Textures"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanoocp.{pkg}").__name__ == f"nanoocp.{pkg}"


def test_the_driver_constructs_and_initialises(driver):
    assert type(driver).__name__ == "OpenGl_GraphicDriver"
    assert driver.InitContext()
    assert driver.GetSharedContext() is None                      # no context until a window is attached
    caps = driver.Options()
    assert isinstance(caps, OpenGl_Caps)
    assert isinstance(caps.contextDebug, bool)                    # a bit-field, bound through def_prop_rw (R-FIELD)


def test_displaying_a_shape_no_longer_segfaults(driver, quiet_messenger):
    """Until TKOpenGl was generated, V3d_Viewer(None) was the only viewer available and anything that builds a
    Graphic3d_Structure -- AIS_InteractiveContext.Display, TPrsStd_AISPresentation.Display -- dereferenced the null
    driver and crashed the process (a row in Design.md 2d). With a real driver it simply works."""
    viewer = V3d_Viewer(driver)
    viewer.SetDefaultLights()
    viewer.SetLightOn()
    view = viewer.CreateView()
    window = Aspect_NeutralWindow()
    window.SetVirtual(True)
    window.SetSize(800, 600)
    view.SetWindow(window)
    assert window.IsVirtual() and window.Size() == (800, 600)

    context = AIS_InteractiveContext(viewer)
    shape = AIS_Shape(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape())
    context.Display(shape, True)
    assert context.IsDisplayed(shape)
    view.FitAll()
    view.Redraw()                                                 # no crash, whatever the GL surface can do


def test_a_virtual_window_gives_a_context_without_a_drawable(driver, quiet_messenger):
    """The GL context is created and valid, but a virtual Aspect_NeutralWindow has no drawable on macOS, so every
    framebuffer operation fails (GL_INVALID_FRAMEBUFFER_OPERATION) and ToPixMap answers False after falling back to
    the on-screen buffer. Offscreen rendering needs a native window handle -- the Aspect_Drawable row in 2d."""
    viewer = V3d_Viewer(driver)
    view = viewer.CreateView()
    window = Aspect_NeutralWindow()
    window.SetVirtual(True)
    window.SetSize(200, 200)
    view.SetWindow(window)

    context = driver.GetSharedContext()
    assert isinstance(context, OpenGl_Context) and context.IsValid()

    pixmap = Image_PixMap()
    assert view.ToPixMap(pixmap, 200, 200, Graphic3d_BT_RGB) is False
    assert (pixmap.SizeX(), pixmap.SizeY()) == (200, 200)         # the buffer is allocated, the render is not done


def test_report_is_the_gl_entry_point_tables():
    """1 587 lines, and 1 533 of them are the GL loader: OpenGl_GlFunctions' C function pointers (raw-pointer) and
    the OpenGl_Arb*/OpenGl_Ext* structs re-exporting them with `using` (inheritance). Neither has any meaning from
    Python -- OpenGL is called through the driver (2d)."""
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    counts: dict[str, int] = {}
    for line in lines:
        counts[line.split("\t")[0]] = counts.get(line.split("\t")[0], 0) + 1
    assert counts["raw-pointer"] + counts["inheritance"] > 1500
    assert counts["raw-pointer"] == 766 and counts["inheritance"] == 767
    assert len(lines) == 1587
    assert "misc" not in counts
    assert sum("of a base, not a method" in line for line in lines) == 755   # the re-exported GL entry points
    assert sum("non-public base OpenGl_GlFunctions dropped" in line for line in lines) == 10
    # the GLES-only header is skipped explicitly (USE_GLES2=OFF)
    assert any("OpenGl_GLESExtensions.hxx: skipped" in line for line in lines)


def test_a_real_window_renders_the_box(quiet_messenger):
    """The whole point of the driver: a rendered image. macOS needs an NSApplication before Cocoa_Window can create
    its NSWindow (OCCT raises Aspect_WindowDefinitionError otherwise), and tkinter's Tk() creates one -- no PyObjC
    needed. The window is never mapped, so nothing appears on screen; ToPixMap still renders. The box comes back in
    OCCT's default yellow, which is how the test knows it is not an empty buffer."""
    tkinter = pytest.importorskip("tkinter")
    try:
        root = tkinter.Tk()
    except tkinter.TclError as exc:                               # headless CI: no display
        pytest.skip(f"no display for tkinter: {exc}")
    try:
        root.withdraw()
        root.update()
        try:
            window = Cocoa_Window("nanoOCP test", 100, 100, 400, 300)
        except Exception as exc:                                  # not macOS, or no window server
            pytest.skip(f"Cocoa_Window unavailable: {type(exc).__name__}: {exc}")
        driver = OpenGl_GraphicDriver(Aspect_DisplayConnection())
        viewer = V3d_Viewer(driver)
        viewer.SetDefaultLights()
        viewer.SetLightOn()
        view = viewer.CreateView()
        view.SetWindow(window)
        context = AIS_InteractiveContext(viewer)
        context.Display(AIS_Shape(BRepPrimAPI_MakeBox(1.0, 1.0, 1.0).Shape()), True)
        view.FitAll()
        view.Redraw()

        pixmap = Image_PixMap()
        assert view.ToPixMap(pixmap, 400, 300, Graphic3d_BT_RGB)
        assert (pixmap.SizeX(), pixmap.SizeY()) == (400, 300)
        colours = {(round(c.Red(), 3), round(c.Green(), 3), round(c.Blue(), 3))
                   for c in (pixmap.PixelColor(x, y).GetRGB() for x in range(0, 400, 13) for y in range(0, 300, 13))}
        assert (1.0, 1.0, 0.0) in colours                         # AIS_Shape's default yellow: the box is there
        assert len(colours) >= 2                                  # ... and a background
    finally:
        root.destroy()
