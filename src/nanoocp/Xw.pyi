"""OCCT package Xw (toolkit TKService)"""

from typing import overload

import nanoocp.Aspect
import nanoocp.Standard
import nanoocp.TCollection


class Xw_Window(nanoocp.Aspect.Aspect_Window):
    """
    This class defines XLib window intended for creation of OpenGL context.
    """

    @overload
    def __init__(self, theXDisplay: nanoocp.Aspect.Aspect_DisplayConnection | None, theXWin: int) -> None:
        """Creates a wrapper over existing Window handle"""

    @overload
    def __init__(self, theXDisplay: nanoocp.Aspect.Aspect_DisplayConnection | None, theTitle: str, thePxLeft: int, thePxTop: int, thePxWidth: int, thePxHeight: int) -> None:
        """
        Creates a XLib window defined by his position and size in pixels.
        Throws exception if window can not be created or Display do not support GLX extension.
        """

    @overload
    def __init__(self, theOther: Xw_Window) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def VirtualKeyFromNative(theKey: int) -> int:
        """Convert X11 virtual key (KeySym) into Aspect_VKey."""

    def Map(self) -> None:
        """Opens the window <me>"""

    def Unmap(self) -> None:
        """Closes the window <me>"""

    def DoResize(self) -> nanoocp.Aspect.Aspect_TypeOfResize:
        """Applies the resizing to the window <me>"""

    def DoMapping(self) -> bool:
        """Apply the mapping change to the window <me>"""

    def IsMapped(self) -> bool:
        """Returns True if the window <me> is opened"""

    def Ratio(self) -> float:
        """Returns The Window RATIO equal to the physical WIDTH/HEIGHT dimensions"""

    def Position(self) -> tuple[int, int, int, int]:
        """Returns The Window POSITION in PIXEL"""

    def Size(self) -> tuple[int, int]:
        """Returns The Window SIZE in PIXEL"""

    def XWindow(self) -> int:
        """@return native Window handle"""

    def NativeHandle(self) -> int:
        """@return native Window handle"""

    def NativeParentHandle(self) -> int:
        """@return parent of native Window handle"""

    def SetTitle(self, theTitle: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets window title."""

    def InvalidateContent(self, theDisp: nanoocp.Aspect.Aspect_DisplayConnection | None) -> None:
        """
        Invalidate entire window content through generation of Expose event.
        This method does not aggregate multiple calls into single event - dedicated event will be sent
        on each call. When NULL display connection is specified, the connection specified on window
        creation will be used. Sending exposure messages from non-window thread would require
        dedicated display connection opened specifically for this working thread to avoid race
        conditions, since Xlib display connection is not thread-safe by default.
        """
