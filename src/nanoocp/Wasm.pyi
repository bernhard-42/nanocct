"""OCCT package Wasm (toolkit TKService)"""

from typing import overload

import nanoocp.Aspect
import nanoocp.BVH
import nanoocp.Standard
import nanoocp.TCollection


class Wasm_Window(nanoocp.Aspect.Aspect_Window):
    """
    This class defines WebAssembly window (HTML5 canvas) intended for creation of OpenGL (WebGL)
    context.

    Note that canvas may define an independent dimensions for backing store (WebGL buffer to render)
    and for CSS (logical units to present buffer onto screen).
    These dimensions differ when browser is dragged into a high pixel density screen (HiDPI),
    or when user scales page in the browser (in both cases window.devicePixelRatio JavaScript
    property becomes not equal to 1.0).

    By default, Wasm_Window::DoResize() will scale backing store of a canvas basing on
    DevicePixelRatio() scale factor to ensure canvas content being rendered with the native
    resolution and not stretched by browser. This, however, might have side effects:
    - a slow GPU might experience performance issues on drawing into larger buffer (e.g. HiDPI);
    - user interface displayed in 3D Viewer (e.g. AIS presentations) should be scaled proportionally
    to be accessible,
    which might require extra processing at application level.
    Consider changing ToScaleBacking flag passed to Wasm_Window constructor in case of issues.
    """

    @overload
    def __init__(self, theCanvasId: nanoocp.TCollection.TCollection_AsciiString, theToScaleBacking: bool = True) -> None:
        """
        Wraps existing HTML5 canvas into window.
        @param[in] theCanvasId target HTML element id defined in a querySelector() syntax
        @param[in] theToScaleBacking when TRUE, window will automatically scale backing store of
        canvas
        basing on DevicePixelRatio() scale factor within DoResize()
        """

    @overload
    def __init__(self, theOther: Wasm_Window) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def MouseButtonsFromNative(theButtons: int) -> int:
        """Convert Emscripten mouse buttons into Aspect_VKeyMouse."""

    @staticmethod
    def VirtualKeyFromNative(theKey: int) -> int:
        """Convert DOM virtual key into Aspect_VKey."""

    def IsMapped(self) -> bool:
        """Return true if window is not hidden."""

    def Map(self) -> None:
        """Change window mapped flag to TRUE."""

    def Unmap(self) -> None:
        """Change window mapped flag to FALSE."""

    def DoResize(self) -> nanoocp.Aspect.Aspect_TypeOfResize:
        """
        Resize window.
        In case of ToScaleBacking flag, this method will resize the backing store of canvas
        basing on DevicePixelRatio() scale factor and CSS canvas size.
        """

    def DoMapping(self) -> bool:
        """Apply the mapping change to the window."""

    def Ratio(self) -> float:
        """Returns window ratio equal to the physical width/height dimensions."""

    def Position(self) -> tuple[int, int, int, int]:
        """Returns The Window POSITION in PIXEL"""

    def Size(self) -> tuple[int, int]:
        """Return the window size in pixels."""

    def SetSizeLogical(self, theSize: nanoocp.BVH.BVH_Vec2d) -> None:
        """
        Set new window size in logical (density-independent units).
        Backing store will be resized basing on DevicePixelRatio().
        """

    def SetSizeBacking(self, theSize: nanoocp.BVH.BVH_Vec2i) -> None:
        """
        Set new window size in pixels.
        Logical size of the element will be resized basing on DevicePixelRatio().
        """

    def CanvasId(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns canvas id."""

    def NativeHandle(self) -> int:
        """
        Current EGL implementation in Emscripten accepts only 0 for native window id.
        """

    def NativeParentHandle(self) -> int:
        """Always returns 0 for this class."""

    def DevicePixelRatio(self) -> float:
        """Return device pixel ratio (logical to backing store scale factor)."""

    def SetDevicePixelRatio(self, theDevicePixelRatio: float) -> None:
        """Sets device pixel ratio for a window with IsVirtual() flag."""

    def InvalidateContent(self, theDisp: nanoocp.Aspect.Aspect_DisplayConnection | None) -> None:
        """Invalidate entire window content through generation of Expose event."""
