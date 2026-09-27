"""Show a unit box in a real OCCT window, driven from Python.

Two things this had to solve on macOS:

1. `Cocoa_Window` refuses to create its NSWindow unless an NSApplication already exists
   ("Aspect_WindowDefinitionError: Cocoa application should be instantiated before window").
   OCCT 8.0.1 has no Cocoa_Application class of its own -- that name lives in OCCT's samples,
   the library's Cocoa package is only Cocoa_Window and Cocoa_LocalPool. `tkinter.Tk()` creates
   the NSApplication for us, with no extra dependency.

2. Something has to pump the Cocoa event loop, or the window never paints and the OS marks it
   unresponsive. tkinter's own loop does that: `root.after(...)` + `root.mainloop()` keeps NSApp
   running, and we redraw from the timer callback.

Run it with:   uv run python window.py
Ctrl-C in the terminal, or closing the Tk control window, ends it.
"""

import tkinter as tk

from OCP3x.AIS import AIS_InteractiveContext, AIS_Shape, AIS_Shaded
from OCP3x.Aspect import Aspect_DisplayConnection
from OCP3x.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCP3x.Cocoa import Cocoa_Window
from OCP3x.Quantity import Quantity_Color, Quantity_NOC_STEELBLUE, Quantity_TOC_sRGB
from OCP3x.V3d import V3d_Viewer, V3d_XposYnegZpos
from OCP3x.OpenGl import OpenGl_GraphicDriver

WIDTH, HEIGHT = 900, 700
FRAME_MS = 16                      # ~60 Hz


def main() -> None:
    # 1. the NSApplication, courtesy of tkinter. Keep the Tk window: closing it stops the loop.
    root = tk.Tk()
    root.title("OCP3x control")
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

    # 3. a real window -- OCCT creates the NSWindow itself, no native handle needed
    window = Cocoa_Window("OCCT 8.0.1 - unit box", 100, 100, WIDTH, HEIGHT)
    view.SetWindow(window)
    if not window.IsMapped():
        window.Map()

    view.SetBackgroundColor(Quantity_Color(0.12, 0.14, 0.18, Quantity_TOC_sRGB))

    box = AIS_Shape(BRepPrimAPI_MakeBox(1.0, 1.0, 1.0).Shape())
    box.SetColor(Quantity_Color(Quantity_NOC_STEELBLUE))
    context.SetDisplayMode(box, AIS_Shaded, True)
    
    context.Display(box, True)

    view.SetProj(V3d_XposYnegZpos)     # the axonometric view; View_Axo() does not exist in OCCT 8
    view.FitAll()
    view.Redraw()

    print(f"OCCT window {WIDTH}x{HEIGHT} open; close the Tk control window (or Ctrl-C) to quit.")

    # 4. the event loop: tkinter pumps NSApp, we redraw from its timer
    alive = True

    def on_close() -> None:
        nonlocal alive
        alive = False
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    def tick() -> None:
        if not alive:
            return
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
