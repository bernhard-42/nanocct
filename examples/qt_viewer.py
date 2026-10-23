"""A small OCCT viewer in a Qt window -- one script for macOS, Windows and Linux.

OCCT draws straight into a Qt widget. Qt gives the widget a native window -- an HWND on Windows, an X window on Linux,
an NSView on macOS -- and QWidget.winId() returns its handle as an integer. Aspect_NeutralWindow.SetNativeHandle takes
that integer on all three platforms (Binding-Rules.md R-NATIVE-HANDLE), and V3d_View.SetWindow renders into it. Qt runs
the event loop and hands the mouse to AIS_ViewController, OCCT's own navigation, which also highlights what is under the
mouse and selects on a click -- the behaviour of OCCT's own viewers.

    left drag     rotate               wheel        zoom at the mouse
    middle drag   pan                  click        select a face (the status bar describes it)
    right drag    zoom                 view cube    click a face, edge or corner to turn the view there

The part: a box with rounded edges and a hole through it (BRepFilletAPI_MakeFillet, BRepAlgoAPI_Cut), shaded with
its edges drawn.

Needs PySide6:   uv pip install PySide6-Essentials
Run it with:     python examples/qt_viewer.py

On Linux Qt has to use X11 (xcb), because OCCT's Linux build draws through X11 (Xw); the script sets
QT_QPA_PLATFORM=xcb unless it is set already, and XWayland covers a Wayland desktop and WSLg. Qt's xcb plugin needs a
few system libraries a minimal system lacks ("xcb-cursor0 or libxcb-cursor0 is needed"); on Ubuntu:
    sudo apt install libxcb-cursor0 libxkbcommon-x11-0 libxcb-icccm4 libxcb-keysyms1 libxcb-shape0 libxcb-xinerama0
"""

import os
import sys

if sys.platform == "linux":
    os.environ.setdefault("QT_QPA_PLATFORM", "xcb")  # before Qt starts

from PySide6.QtCore import QEvent, Qt, QTimer, Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from nanocct import TopoDS
from nanocct.AIS import (
    AIS_InteractiveContext,
    AIS_Shaded,
    AIS_Shape,
    AIS_ViewController,
    AIS_ViewCube,
    AIS_WireFrame,
)
from nanocct.Aspect import (
    Aspect_DisplayConnection,
    Aspect_GFM_VER,
    Aspect_NeutralWindow,
    Aspect_ScrollDelta,
    Aspect_TOL_SOLID,
    Aspect_VKeyFlags_ALT,
    Aspect_VKeyFlags_CTRL,
    Aspect_VKeyFlags_NONE,
    Aspect_VKeyFlags_SHIFT,
    Aspect_VKeyMouse_LeftButton,
    Aspect_VKeyMouse_MiddleButton,
    Aspect_VKeyMouse_NONE,
    Aspect_VKeyMouse_RightButton,
)
from nanocct.BRepAdaptor import BRepAdaptor_Surface
from nanocct.BRepAlgoAPI import BRepAlgoAPI_Cut
from nanocct.BRepFilletAPI import BRepFilletAPI_MakeFillet
from nanocct.BRepGProp import BRepGProp
from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from nanocct.BVH import BVH_Vec2i
from nanocct.gp import gp_Ax2, gp_Dir, gp_Pnt
from nanocct.GProp import GProp_GProps
from nanocct.OpenGl import OpenGl_GraphicDriver
from nanocct.Prs3d import Prs3d_LineAspect
from nanocct.Quantity import (
    Quantity_Color,
    Quantity_NOC_BLACK,
    Quantity_NOC_STEELBLUE,
    Quantity_TOC_sRGB,
)
from nanocct.TopAbs import TopAbs_ShapeEnum
from nanocct.TopExp import TopExp_Explorer
from nanocct.TopoDS import TopoDS_Shape
from nanocct.V3d import V3d_Viewer, V3d_Xpos, V3d_XposYnegZpos, V3d_Yneg, V3d_Zpos


def make_part() -> TopoDS_Shape:
    """A 40 mm box with 4 mm fillets on every edge and a 16 mm hole through it."""
    box = BRepPrimAPI_MakeBox(gp_Pnt(-20.0, -20.0, -20.0), 40.0, 40.0, 40.0).Shape()
    fillet = BRepFilletAPI_MakeFillet(box)
    edges = []
    explorer = TopExp_Explorer(box, TopAbs_ShapeEnum.TopAbs_EDGE)
    while explorer.More():  # an edge is met once per face it bounds
        edge = TopoDS.Edge(explorer.Current())
        if not any(edge.IsSame(seen) for seen in edges):
            edges.append(edge)
            fillet.Add(4.0, edge)
        explorer.Next()
    hole = BRepPrimAPI_MakeCylinder(
        gp_Ax2(gp_Pnt(0.0, 0.0, -30.0), gp_Dir(0.0, 0.0, 1.0)), 8.0, 60.0
    ).Shape()
    return BRepAlgoAPI_Cut(fillet.Shape(), hole).Shape()


def describe_selection(context: AIS_InteractiveContext) -> str:
    """The status bar's text for what is selected: a face's surface type and area."""
    context.InitSelected()
    if not context.MoreSelected():
        return "nothing selected -- click a face"
    shape = context.SelectedShape()
    if shape.ShapeType() != TopAbs_ShapeEnum.TopAbs_FACE:
        return shape.ShapeType().name.removeprefix("TopAbs_").lower()
    face = TopoDS.Face(shape)
    kind = BRepAdaptor_Surface(face).GetType().name.removeprefix("GeomAbs_")
    props = GProp_GProps()
    BRepGProp.SurfaceProperties_s(face, props)
    return f"face: {kind}, area {props.Mass():.1f} mm²"


class OcctWidget(QWidget):
    """A QWidget OCCT renders into through its native window handle."""

    selection_changed = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        # OCCT paints the native window itself: Qt must give the widget one and not paint over it
        self.setAttribute(Qt.WidgetAttribute.WA_NativeWindow)
        self.setAttribute(Qt.WidgetAttribute.WA_PaintOnScreen)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)
        self.setMouseTracking(True)  # hover highlighting without a pressed button
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setMinimumSize(400, 300)

        self.viewer = V3d_Viewer(OpenGl_GraphicDriver(Aspect_DisplayConnection()))
        self.viewer.SetDefaultLights()
        self.viewer.SetLightOn()
        self.view = self.viewer.CreateView()
        self.context = AIS_InteractiveContext(self.viewer)
        self.controller = AIS_ViewController()
        self.window: Aspect_NeutralWindow | None = None
        self.selection = ""
        self.clicked = False  # a button was released: the selection may have changed

        self.part = AIS_Shape(make_part())
        self.part.SetColor(Quantity_Color(Quantity_NOC_STEELBLUE))
        drawer = self.part.Attributes()  # the edges, drawn on the shaded faces
        drawer.SetFaceBoundaryDraw(True)
        drawer.SetFaceBoundaryAspect(
            Prs3d_LineAspect(Quantity_Color(Quantity_NOC_BLACK), Aspect_TOL_SOLID, 1.5)
        )

        # the view cube turns the view when one of its faces, edges or corners is clicked, animated by the controller
        self.cube = AIS_ViewCube()
        self.cube.SetViewAnimation(self.controller.ViewAnimation())
        self.cube.SetFixedAnimationLoop(False)
        self.cube.SetAutoStartAnimation(True)
        # the cube's sizes are pixels; these are the values for a device pixel ratio of 1, see _apply_device_ratio
        self.cube_size = 55.0
        self.cube_axes = (
            self.cube.AxesRadius(),
            self.cube.AxesConeRadius(),
            self.cube.AxesSphereRadius(),
        )
        offset = self.cube.TransformPersistence().Offset2d()
        self.cube_offset = (offset.x(), offset.y())

    # ---- the native window ------------------------------------------------------------------------------------------
    def paintEngine(self):
        return None  # WA_PaintOnScreen: OCCT, not Qt, paints

    def _pixels(self) -> tuple[int, int]:
        """The widget's size in device pixels -- OCCT's window is physical, Qt's sizes are logical on a HiDPI screen."""
        ratio = self.devicePixelRatioF()
        return round(self.width() * ratio), round(self.height() * ratio)

    def _apply_device_ratio(self) -> None:
        """Scale what OCCT draws in pixels to the screen's device pixel ratio (2 on a Retina display), so the view
        looks the same on every screen. Line widths and text follow RenderingParams.Resolution (72 is a ratio of 1).
        The view cube lives in pixel coordinates, which ignore the resolution (Graphic3d_TransformPers.hxx), so its
        size, axes and corner offset are scaled here -- but not its font: the resolution scales text already, and
        SetSize's own font scaling would make the labels twice too large."""
        ratio = self.devicePixelRatioF()
        self.view.ChangeRenderingParams().Resolution = round(72 * ratio)
        self.cube.SetSize(
            self.cube_size * ratio
        )  # scales the facet extension and padding too ...
        self.cube.SetFontHeight(
            0.16 * self.cube_size
        )  # ... and the font, back to what SetSize gives at 1
        radius, cone, sphere = self.cube_axes
        self.cube.SetAxesRadius(radius * ratio)
        self.cube.SetAxesConeRadius(cone * ratio)
        self.cube.SetAxesSphereRadius(sphere * ratio)
        persistence = self.cube.TransformPersistence()
        persistence.SetOffset2d(
            BVH_Vec2i(
                round(self.cube_offset[0] * ratio), round(self.cube_offset[1] * ratio)
            )
        )
        self.cube.SetTransformPersistence(persistence)

    def _attach(self) -> None:
        """Hand the widget's native window to OCCT, at the first paint. Not when the widget is shown: on macOS the
        NSView then still has the widget's minimum size (400x300 while Qt reported 1000x699), OCCT
        sizes its GL surface from the NSView, and nothing resizes it afterwards -- macOS stretched the small image to
        the window, with fat edges and a huge view cube until the first resize."""
        if self.window is not None:
            return
        self.window = Aspect_NeutralWindow()
        self.window.SetNativeHandle(
            int(self.winId())
        )  # HWND, X window or NSView*: an int everywhere
        self.window.SetSize(*self._pixels())
        self.view.SetWindow(self.window)
        self.view.SetBgGradientColors(
            Quantity_Color(0.30, 0.35, 0.42, Quantity_TOC_sRGB),
            Quantity_Color(0.08, 0.09, 0.11, Quantity_TOC_sRGB),
            Aspect_GFM_VER,
            False,
        )
        self.context.Display(self.part, False)
        self.context.SetDisplayMode(self.part, AIS_Shaded, False)
        self.context.Deactivate(self.part)  # select faces rather than the whole shape
        self.context.Activate(
            self.part, AIS_Shape.SelectionMode_s(TopAbs_ShapeEnum.TopAbs_FACE)
        )
        self._apply_device_ratio()
        self.context.Display(self.cube, False)
        self.set_projection(V3d_XposYnegZpos)

    def event(self, event) -> bool:
        # moved to a screen with another device pixel ratio: the size in points stays, so no resizeEvent follows,
        # and OCCT reads the new backing scale only when told that the window changed
        if (
            event.type() == QEvent.Type.DevicePixelRatioChange
            and self.window is not None
        ):
            self._apply_device_ratio()
            self.context.Redisplay(self.cube, False)
            self.window.SetSize(*self._pixels())
            self.view.MustBeResized()
            self.update()
            # a native child window (WA_NativeWindow, which OCCT needs) leaves Qt's toolbar at the old screen's scale
            # until the mouse enters the view or the window loses focus; a repaint right away was not enough, one
            # 100 ms later was (seen on macOS, also without OCCT). QWidget.window: self.window is OCCT's
            QTimer.singleShot(100, QWidget.window(self).repaint)
        return super().event(event)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        if self.window is not None:
            self.window.SetSize(*self._pixels())
            self.view.MustBeResized()
            self.update()

    def paintEvent(self, event) -> None:
        self._attach()
        self.view.InvalidateImmediate()
        self.controller.FlushViewEvents(
            self.context, self.view, True
        )  # navigation, highlighting, picking, redraw
        if not self.controller.ViewAnimation().IsStopped():
            QTimer.singleShot(
                16, self.update
            )  # the view cube's camera animation: next frame
        if self.clicked:  # the controller picks during the flush above
            self.clicked = False
            text = describe_selection(self.context)
            if text != self.selection:
                self.selection = text
                self.selection_changed.emit(text)

    # ---- the mouse, handed to AIS_ViewController ----------------------------------------------------------------------
    def _point(self, event) -> BVH_Vec2i:
        ratio = self.devicePixelRatioF()
        position = event.position()
        return BVH_Vec2i(round(position.x() * ratio), round(position.y() * ratio))

    @staticmethod
    def _buttons(buttons) -> int:
        mask = int(Aspect_VKeyMouse_NONE)
        for qt_button, occt_button in (
            (Qt.MouseButton.LeftButton, Aspect_VKeyMouse_LeftButton),
            (Qt.MouseButton.MiddleButton, Aspect_VKeyMouse_MiddleButton),
            (Qt.MouseButton.RightButton, Aspect_VKeyMouse_RightButton),
        ):
            if buttons & qt_button:
                mask |= int(occt_button)
        return mask

    @staticmethod
    def _modifiers(modifiers) -> int:
        mask = int(Aspect_VKeyFlags_NONE)
        for qt_key, occt_flag in (
            (Qt.KeyboardModifier.ShiftModifier, Aspect_VKeyFlags_SHIFT),
            (Qt.KeyboardModifier.ControlModifier, Aspect_VKeyFlags_CTRL),
            (Qt.KeyboardModifier.AltModifier, Aspect_VKeyFlags_ALT),
        ):
            if modifiers & qt_key:
                mask |= int(occt_flag)
        return mask

    def mousePressEvent(self, event) -> None:
        self.controller.UpdateMouseButtons(
            self._point(event),
            self._buttons(event.buttons()),
            self._modifiers(event.modifiers()),
            False,
        )
        self.update()

    def mouseReleaseEvent(self, event) -> None:
        self.controller.UpdateMouseButtons(
            self._point(event),
            self._buttons(event.buttons()),
            self._modifiers(event.modifiers()),
            False,
        )
        self.clicked = True
        self.update()

    def mouseMoveEvent(self, event) -> None:
        self.controller.UpdateMousePosition(
            self._point(event),
            self._buttons(event.buttons()),
            self._modifiers(event.modifiers()),
            False,
        )
        self.update()

    def wheelEvent(self, event) -> None:
        self.controller.UpdateZoom(
            Aspect_ScrollDelta(
                self._point(event),
                event.angleDelta().y() / 8.0,
                self._modifiers(event.modifiers()),
            )
        )
        self.update()

    # ---- what the toolbar does ----------------------------------------------------------------------------------------
    def set_projection(self, projection) -> None:
        self.view.SetProj(projection)
        self.view.FitAll()
        self.update()

    def fit_all(self) -> None:
        self.view.FitAll()
        self.update()

    def set_wireframe(self, wireframe: bool) -> None:
        self.context.SetDisplayMode(
            self.part, AIS_WireFrame if wireframe else AIS_Shaded, False
        )
        # the controller redraws the whole view only when it is invalidated -- a camera change does that, a new
        # display mode does not -- and otherwise just the highlighting layer
        self.view.Invalidate()
        self.update()


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("nanocct -- OCCT in a Qt window")
        self.viewer = OcctWidget(self)
        self.setCentralWidget(self.viewer)

        toolbar = self.addToolBar("View")
        for label, slot in (
            ("Fit", self.viewer.fit_all),
            ("Iso", lambda: self.viewer.set_projection(V3d_XposYnegZpos)),
            ("Front", lambda: self.viewer.set_projection(V3d_Yneg)),
            ("Right", lambda: self.viewer.set_projection(V3d_Xpos)),
            ("Top", lambda: self.viewer.set_projection(V3d_Zpos)),
        ):
            action = QAction(label, self)
            action.triggered.connect(slot)
            toolbar.addAction(action)
        toolbar.addSeparator()
        wireframe = QAction("Wireframe", self)
        wireframe.setCheckable(True)
        wireframe.toggled.connect(self.viewer.set_wireframe)
        toolbar.addAction(wireframe)

        self.viewer.selection_changed.connect(self.statusBar().showMessage)
        self.statusBar().showMessage(
            "drag to rotate, wheel to zoom, click a face to select it"
        )

    def closeEvent(self, event) -> None:
        self.viewer.view.Remove()
        super().closeEvent(event)


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(1000, 750)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
