"""Generated bindings for TKOpenGl (Visualization: the OpenGl package): OCCT's OpenGL graphic driver. With it a
V3d_Viewer has a real driver, so AIS_InteractiveContext.Display() works instead of dereferencing a null one -- the
single biggest limitation nanocct carried until 2026-09-22. Rendering to an image needs a drawable, which only a
real native window provides -- shown or not, and marked virtual for offscreen work, as OCCT's own `vinit -virtual`
does; a virtual Aspect_NeutralWindow without a handle has none (Excluded.md)."""
import contextlib
import importlib
import os
import platform
from pathlib import Path

import pytest

from conftest import report

from nanocct import Message
from nanocct.AIS import AIS_InteractiveContext, AIS_Shape
from nanocct.Aspect import Aspect_DisplayConnection, Aspect_NeutralWindow
from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanocct.Graphic3d import Graphic3d_BT_RGB
from nanocct.Image import Image_PixMap
from nanocct.OpenGl import OpenGl_Caps, OpenGl_GraphicDriver
from nanocct.V3d import V3d_Viewer
from nanocct.Xw import Xw_Window                                  # generated everywhere; it opens windows on Linux only

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


# GitHub's macOS runners are virtual machines without a GPU, and OCCT asks for an accelerated context by default
# (NSOpenGLPFAAccelerated, OpenGl_Window_1.mm), so every GL context failed there with "OpenGl_Window::CreateWindow:
# NSOpenGLContext creation failed" (the first CI run, 2026-09-28). OCCT's own switch for that is
# OpenGl_Caps.contextNoAccel: Apple's software renderer (kCGLRendererGenericFloatID) on macOS, WGL_NO_ACCELERATION_ARB
# on Windows. So the tests run on that runner too, with the software renderer, and everywhere else on the GPU.
SOFTWARE_GL = os.environ.get("GITHUB_ACTIONS") == "true" and platform.system() == "Darwin"


def gl_driver(display):
    """The graphic driver every test here renders with. OCCT talks to a window system: X11 on Linux (USE_XLIB=ON, its
    own default; `make test` runs the suite under xvfb-run), CGL on macOS, WGL on Windows. The options are read when a
    window's GL context is created, so they can be set after construction."""
    driver = OpenGl_GraphicDriver(display)
    driver.ChangeOptions().contextNoAccel = SOFTWARE_GL
    return driver


@pytest.fixture
def display():
    """The display connection. Without a display server (an empty DISPLAY: over ssh, or a container without xvfb) it
    raises -- a broken test environment, which fails rather than being skipped."""
    return Aspect_DisplayConnection()


_WNT_CLASS = []      # the one window class of the test process: RegisterClassW refuses a second class of the same name


def wnt_window(title, width, height):
    """A real Win32 window that is never shown: WNT_Window creates it without WS_VISIBLE and only Map() would show it.
    Its class is OCCT's with the default window procedure -- WNT_WClass's theWndProc is dropped and OCCT turns the NULL
    into DefWindowProcW (R-OPTIONAL-PTR, overrides.toml [null_ok]); the style constants are <winuser.h>'s."""
    WNT = importlib.import_module("nanocct.WNT")                  # WNT_WClass/WNT_Window exist on Windows only
    if len(_WNT_CLASS) == 0:
        CS_VREDRAW, CS_HREDRAW = 0x0001, 0x0002
        _WNT_CLASS.append(WNT.WNT_WClass("nanocct tests", CS_VREDRAW | CS_HREDRAW))
    WS_POPUP, WS_CLIPCHILDREN, WS_CLIPSIBLINGS = 0x80000000, 0x02000000, 0x04000000
    return WNT.WNT_Window(title, _WNT_CLASS[0], WS_POPUP | WS_CLIPCHILDREN | WS_CLIPSIBLINGS, 0, 0, width, height)


def offscreen_window(display, width, height):
    """A window the platform's GL backend accepts, without putting anything on screen.

    macOS (CGL) is happy with a virtual Aspect_NeutralWindow -- it has no drawable, which is enough for Display but
    not for an image (Excluded.md). X11 is not: OCCT asks XGetWindowAttributes about window id 0 and Xlib's *default error handler exits the
    process*, so the whole pytest run dies with "BadWindow" and no traceback (banach, 2026-09-23). There Xw_Window makes
    a real window instead, which is never mapped, so nothing appears either. Windows takes a virtual window only as far
    as the driver allows: without a window handle OCCT sets the pixel format on the *screen's* device context
    (GetDC(NULL), OpenGl_Window.cxx), which one driver accepted on 2026-09-24 and refuses since its update of
    2026-10-07 ("SetPixelFormat failed. Error code: -1073283066", 0xC0070006; reproduced with plain ctypes, while the
    same pixel format on a hidden window is accepted). So Windows gets a real, hidden WNT_Window too.
    """
    if platform.system() == "Linux":
        return Xw_Window(display, "nanocct test", 100, 100, width, height)
    if platform.system() == "Windows":
        return wnt_window("nanocct test", width, height)
    window = Aspect_NeutralWindow()
    window.SetVirtual(True)
    window.SetSize(width, height)
    return window


@pytest.fixture
def driver(display):
    return gl_driver(display)


@pytest.mark.parametrize("pkg", ["OpenGl", "Textures"])
def test_every_package_imports(pkg):
    assert importlib.import_module(f"nanocct.{pkg}").__name__ == f"nanocct.{pkg}"


def test_the_driver_constructs_and_initialises(driver):
    assert type(driver).__name__ == "OpenGl_GraphicDriver"
    assert driver.InitContext()
    assert driver.GetSharedContext() is None                      # no context until a window is attached
    caps = driver.Options()
    assert isinstance(caps, OpenGl_Caps)
    assert isinstance(caps.contextDebug, bool)                    # a plain bool field, nanocct_def_field (R-FIELD)


def test_displaying_a_shape_no_longer_segfaults(driver, display, quiet_messenger):
    """Until TKOpenGl was generated, V3d_Viewer(None) was the only viewer available and anything that builds a
    Graphic3d_Structure -- AIS_InteractiveContext.Display, TPrsStd_AISPresentation.Display -- dereferenced the null
    driver and crashed the process (a row in Excluded.md). With a real driver it simply works."""
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


def test_report_is_the_gl_entry_point_tables():
    """Almost the whole report is the GL loader: OpenGl_GlFunctions' C function pointers (raw-pointer) and the
    OpenGl_Arb*/OpenGl_Ext* structs re-exporting them with `using` (inheritance). Neither has any meaning from
    Python -- OpenGL is called through the driver (Excluded.md).

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


@contextlib.contextmanager
def real_window(width, height):
    """A native window of this platform, never shown.

    Windows: a WNT_Window (wnt_window). Linux: an Xw_Window on the X display (xvfb-run in `make test`). macOS: a
    Cocoa_Window, which needs an NSApplication before it can create its NSWindow (OCCT raises
    Aspect_WindowDefinitionError otherwise), and tkinter's Tk() creates one -- no PyObjC needed."""
    if platform.system() == "Windows":
        yield wnt_window("nanocct test", width, height)
        return
    if platform.system() == "Linux":
        yield Xw_Window(Aspect_DisplayConnection(), "nanocct test", 100, 100, width, height)
        return
    import tkinter
    root = tkinter.Tk()
    try:
        root.withdraw()
        root.update()
        # Cocoa is only generated on macOS (overrides.toml [platform]), so the module itself is absent elsewhere --
        # importing it at the top of the file would fail collection of the whole module on Linux and Windows.
        Cocoa = importlib.import_module("nanocct.Cocoa")
        yield Cocoa.Cocoa_Window("nanocct test", 100, 100, width, height)
    finally:
        root.destroy()


def _box_colours(window, width, height):
    """Render a unit box in a view on `window` and dump it at width x height: the set of colours sampled from the image.
    The box comes back in OCCT's default yellow, which is how a caller knows the image is not an empty buffer."""
    driver = gl_driver(Aspect_DisplayConnection())
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
    assert view.ToPixMap(pixmap, width, height, Graphic3d_BT_RGB)
    assert (pixmap.SizeX(), pixmap.SizeY()) == (width, height)
    return {(round(c.Red(), 3), round(c.Green(), 3), round(c.Blue(), 3))
            for c in (pixmap.PixelColor(x, y).GetRGB() for x in range(0, width, 13) for y in range(0, height, 13))}


def test_a_real_window_renders_the_box(quiet_messenger):
    """The whole point of the driver: a rendered image, in a native window (real_window). The window is never mapped,
    so nothing appears on screen; ToPixMap still renders."""
    with real_window(400, 300) as window:
        colours = _box_colours(window, 400, 300)
        assert (1.0, 1.0, 0.0) in colours                         # AIS_Shape's default yellow: the box is there
        assert len(colours) >= 2                                  # ... and a background


def test_a_real_window_marked_virtual_renders_offscreen(quiet_messenger):
    """OCCT's own offscreen route -- the Draw harness's `vinit -virtual` (ViewerTest_ViewerCommands.cxx), described in
    "Offscreen OCCT viewer" (unlimited3d.wordpress.com, 2022-01-30): a real native window that is never mapped, marked
    virtual before the view takes it, and the image dumped from a framebuffer object. The real window provides the
    drawable, so the GL context is complete on every platform -- unlike a virtual Aspect_NeutralWindow without a handle,
    which has no drawable on macOS, lands on the screen's device context on Windows and aborts in Xlib on Linux
    (Excluded.md). The dump is larger than the 64 x 64 window: ToPixMap renders into its own framebuffer, not into the
    window's surface."""
    with real_window(64, 64) as window:
        window.SetVirtual(True)
        assert window.IsVirtual() is True
        assert window.IsMapped() is True                          # a virtual window counts as mapped; Map() does nothing
        colours = _box_colours(window, 320, 240)
        assert (1.0, 1.0, 0.0) in colours                         # AIS_Shape's default yellow: the box is there
        assert len(colours) >= 2                                  # ... and a background
