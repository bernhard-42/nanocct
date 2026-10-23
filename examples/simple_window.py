"""Show a unit box in a real OCCT window, driven from Python -- one script for macOS, Windows and Linux.

The one part that differs between the platforms, creating the window, is `native_window()`:

- macOS: `Cocoa_Window` creates its NSWindow itself, but only once an NSApplication exists ("Cocoa application
  should be instantiated before window"); `tkinter.Tk()` creates one.
- Windows: `WNT_Window` is created from a registered `WNT_WClass`; nanocct leaves out the class's window procedure
  and OCCT then uses the Win32 default, `DefWindowProcW` (Binding-Rules.md R-OPTIONAL-PTR). With no cursor
  given, OCCT's class shows the "unavailable" cursor over the window.
- Linux: `Xw_Window` creates an X11 window on the display connection (the Linux build has USE_XLIB=ON); under WSL
  that is WSLg's X server.

On all three, tkinter's loop keeps the OCCT window alive -- it runs NSApp on macOS and dispatches the thread's messages
on Windows -- and we redraw from its timer.

Run it with:   uv run python examples/simple_window.py
Ctrl-C in the terminal, or closing the Tk control window, ends it.
"""

import sys
import tkinter as tk

from nanocct.AIS import AIS_InteractiveContext, AIS_Shape, AIS_Shaded
from nanocct.Aspect import Aspect_DisplayConnection, Aspect_TOL_SOLID, Aspect_Window
from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
from nanocct.OpenGl import OpenGl_GraphicDriver
from nanocct.Prs3d import Prs3d_LineAspect
from nanocct.Quantity import Quantity_Color, Quantity_NOC_BLACK, Quantity_NOC_STEELBLUE, Quantity_TOC_sRGB
from nanocct.V3d import V3d_Viewer, V3d_XposYnegZpos

WIDTH, HEIGHT = 900, 700
FRAME_MS = 16                      # ~60 Hz
TITLE = "OCCT 8.0.1 - unit box"


def native_window(display: Aspect_DisplayConnection, title: str, x: int, y: int, width: int, height: int) -> Aspect_Window:
    """This platform's window, created by OCCT itself (no native handle needed) and hidden until Map()."""
    if sys.platform == "linux":
        from nanocct.Xw import Xw_Window                    # X11 only in the Linux build
        return Xw_Window(display, title, x, y, width, height)
    if sys.platform == "darwin":
        from nanocct.Cocoa import Cocoa_Window             # macOS only
        return Cocoa_Window(title, x, y, width, height)
    if sys.platform == "win32":
        from nanocct.WNT import WNT_WClass, WNT_Window      # Windows only
        # <winuser.h>: redraw the whole window on resize; a resizable window with a title bar but no close button,
        # so that it is closed together with the Tk window
        CS_VREDRAW, CS_HREDRAW = 0x0001, 0x0002
        WS_CAPTION, WS_THICKFRAME, WS_CLIPCHILDREN, WS_CLIPSIBLINGS = 0x00C00000, 0x00040000, 0x02000000, 0x04000000
        wclass = WNT_WClass("nanocct example", CS_VREDRAW | CS_HREDRAW)
        return WNT_Window(title, wclass, WS_CAPTION | WS_THICKFRAME | WS_CLIPCHILDREN | WS_CLIPSIBLINGS,
                          x, y, width, height)
    sys.exit(f"simple_window.py runs on macOS, Windows and Linux, not on {sys.platform}")


def main() -> None:
    # 1. the control window; its event loop also serves the OCCT window (and on macOS it is the NSApplication)
    root = tk.Tk()
    root.title("nanocct control")
    root.geometry("300x80+1050+100")
    tk.Label(root, text="OCCT window is open.\nClose this window to quit.").pack(padx=10, pady=10)
    root.update()

    # 2. the OCCT viewer, exactly as in C++
    display = Aspect_DisplayConnection()
    driver = OpenGl_GraphicDriver(display)

    viewer = V3d_Viewer(driver)
    viewer.SetDefaultLights()
    viewer.SetLightOn()

    view = viewer.CreateView()
    context = AIS_InteractiveContext(viewer)

    # 3. a real window. Map() unconditionally: WNT_Window::IsMapped() answers True for a window never shown
    window = native_window(display, TITLE, 100, 100, WIDTH, HEIGHT)
    view.SetWindow(window)
    window.Map()

    view.SetBackgroundColor(Quantity_Color(0.12, 0.14, 0.18, Quantity_TOC_sRGB))

    box = AIS_Shape(BRepPrimAPI_MakeBox(1.0, 1.0, 1.0).Shape())
    box.SetColor(Quantity_Color(Quantity_NOC_STEELBLUE))
    drawer = box.Attributes()                  # the edges: OCCT draws the face boundaries on the shaded box
    drawer.SetFaceBoundaryDraw(True)
    drawer.SetFaceBoundaryAspect(Prs3d_LineAspect(Quantity_Color(Quantity_NOC_BLACK), Aspect_TOL_SOLID, 1.5))
    context.SetDisplayMode(box, AIS_Shaded, True)

    context.Display(box, True)

    view.SetProj(V3d_XposYnegZpos)     # the axonometric view; View_Axo() does not exist in OCCT 8
    view.FitAll()
    view.Redraw()

    print(f"OCCT window {WIDTH}x{HEIGHT} open; close the Tk control window (or Ctrl-C) to quit.")

    # 4. the event loop: tkinter keeps the window alive, we follow resizes and redraw from its timer
    alive = True
    size = window.Size()

    def on_close() -> None:
        nonlocal alive
        alive = False
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    def tick() -> None:
        nonlocal size
        if not alive:
            return
        # Size() is the window's current size on both platforms; DoResize() is not a "did it change" test
        # (it answers Aspect_TOR_NO_BORDER when nothing changed, and on Windows misses a maximize)
        if window.Size() != size:
            size = window.Size()
            view.MustBeResized()
        view.Redraw()
        root.after(FRAME_MS, tick)

    root.after(FRAME_MS, tick)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        pass
    finally:
        view.Remove()
        print("closed.")


if __name__ == "__main__":
    main()
