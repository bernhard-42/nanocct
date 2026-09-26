"""Generated bindings for TKOpenGl (Visualization: the OpenGl package): OCCT's OpenGL graphic driver. With it a
V3d_Viewer has a real driver, so AIS_InteractiveContext.Display() works instead of dereferencing a null one -- the
single biggest limitation nanoOCP carried until 2026-09-22. Rendering to an image still needs a drawable, which a
virtual window does not provide on macOS; the test pins that boundary down."""
import importlib
import platform
from pathlib import Path

import pytest

from conftest import report

from nanoocp import Message
from nanoocp.AIS import AIS_InteractiveContext, AIS_Shape
from nanoocp.Aspect import Aspect_DisplayConnection, Aspect_NeutralWindow
from nanoocp.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanoocp.Graphic3d import Graphic3d_BT_RGB
from nanoocp.Image import Image_PixMap
from nanoocp.OpenGl import OpenGl_Caps, OpenGl_Context, OpenGl_GraphicDriver
from nanoocp.V3d import V3d_Viewer

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKOpenGl" / "report.txt"


@pytest.fixture
def quiet_messenger():
    """A context without a drawable prints GL errors; the test asserts the return values instead."""
    printers = list(Message.Message.DefaultMessenger_s().Printers())
    levels = [p.GetTraceLevel() for p in printers]
    for p in printers:
        p.SetTraceLevel(Message.Message_Fail)
    yield
    for p, level in zip(printers, levels):
        p.SetTraceLevel(level)


@pytest.fixture
def display():
    """The display connection, or a skip where no display server can be reached."""
    try:
        return Aspect_DisplayConnection()
    except Exception as exc:
        pytest.skip(f"no display server: {type(exc).__name__}: {exc}")


def offscreen_window(display, width, height):
    """A window the platform's GL backend accepts, without putting anything on screen.

    macOS (CGL) and Windows are happy with a virtual Aspect_NeutralWindow -- it has no drawable, which is the point of
    the test below. X11 is not: OCCT asks XGetWindowAttributes about window id 0 and Xlib's *default error handler
    exits the process*, so the whole pytest run dies with "BadWindow" and no traceback (banach, 2026-09-23). There
    Xw_Window makes a real window instead, which is never mapped, so nothing appears either.
    """
    if platform.system() == "Linux":
        Xw = pytest.importorskip("nanoocp.Xw")
        return Xw.Xw_Window(display, "nanoOCP test", 100, 100, width, height)
    window = Aspect_NeutralWindow()
    window.SetVirtual(True)
    window.SetSize(width, height)
    return window


@pytest.fixture
def driver(display):
    """A graphic driver, or a skip where no display server can be reached.

    OCCT talks to a window system here: X11 on Linux (USE_XLIB=ON, its own default), CGL on macOS, WGL on Windows.
    Over ssh or in a container there is no DISPLAY, and Aspect_DisplayConnection raises rather than returning a
    headless driver -- an environment limitation, not a binding defect, so the tests that need a driver skip
    (banach, 2026-09-23: "Can not connect to the server", DISPLAY empty). A Linux CI runner needs xvfb for these.
    """
    return OpenGl_GraphicDriver(display)


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


def test_displaying_a_shape_no_longer_segfaults(driver, display, quiet_messenger):
    """Until TKOpenGl was generated, V3d_Viewer(None) was the only viewer available and anything that builds a
    Graphic3d_Structure -- AIS_InteractiveContext.Display, TPrsStd_AISPresentation.Display -- dereferenced the null
    driver and crashed the process (a row in Design.md 2d). With a real driver it simply works."""
    viewer = V3d_Viewer(driver)
    viewer.SetDefaultLights()
    viewer.SetLightOn()
    view = viewer.CreateView()
    window = offscreen_window(display, 800, 600)
    view.SetWindow(window)
    assert window.Size() == (800, 600)

    context = AIS_InteractiveContext(viewer)
    shape = AIS_Shape(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape())
    context.Display(shape, True)
    assert context.IsDisplayed(shape)
    view.FitAll()
    view.Redraw()                                                 # no crash, whatever the GL surface can do


@pytest.mark.skipif(platform.system() == "Linux",
                    reason="a virtual Aspect_NeutralWindow has no X window, and OCCT's X11 path then aborts the "
                           "process through Xlib's default error handler (BadWindow) instead of raising")
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
    # macOS: a virtual Aspect_NeutralWindow has no drawable, every framebuffer operation fails and ToPixMap answers
    # False after falling back to the on-screen buffer. Windows renders into it and answers True (gauss, 2026-09-24).
    rendered = view.ToPixMap(pixmap, 200, 200, Graphic3d_BT_RGB)
    assert rendered is (platform.system() == "Windows")
    assert (pixmap.SizeX(), pixmap.SizeY()) == (200, 200)         # the buffer is allocated either way


def test_report_is_the_gl_entry_point_tables():
    """Almost the whole report is the GL loader: OpenGl_GlFunctions' C function pointers (raw-pointer) and the
    OpenGl_Arb*/OpenGl_Ext* structs re-exporting them with `using` (inheritance). Neither has any meaning from
    Python -- OpenGL is called through the driver (2d).

    This is the one report whose *portable* categories are not identical across platforms either: the entry-point
    tables are OCCT's own, and a CGL build lists different extensions from an EGL one (macOS 768 raw-pointer and
    4 override, Linux 773 and 2). Those two are therefore bounded rather than pinned; everything else is exact."""
    lines, portable, undefined, counts = report("TKOpenGl")
    assert counts["raw-pointer"] + counts["inheritance"] > 1500
    assert counts["raw-pointer"] >= 768 and counts["inheritance"] == 767
    assert len(portable) >= 1589
    assert all("OpenGl_" in line for line in undefined)
    assert sum("NCollection_Vec2<unsigned int>::cwiseAbs" in line for line in lines) == 1
    assert "misc" not in counts
    assert sum("of a base, not a method" in line for line in lines) == 755   # the re-exported GL entry points
    # the ten GL function tables that derive protected from OpenGl_GlFunctions: the base's members are not bound,
    # but the classes are constructible again since 2026-09-23 (it declares no operator new), which took their
    # "no constructors" line out of the report -- 1 587 lines before
    assert sum("non-public base OpenGl_GlFunctions dropped" in line for line in lines) == 10
    assert "not-constructible" not in counts
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
        # Cocoa is only generated on macOS (overrides.toml [platform]), so the module itself is absent elsewhere --
        # importing it at the top of the file would fail collection of the whole module on Linux and Windows.
        Cocoa = pytest.importorskip("nanoocp.Cocoa", reason="Cocoa is built on macOS only")
        try:
            window = Cocoa.Cocoa_Window("nanoOCP test", 100, 100, 400, 300)
        except Exception as exc:                                  # no window server
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
