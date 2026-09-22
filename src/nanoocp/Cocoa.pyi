"""OCCT package Cocoa (toolkit TKService)"""

from typing import overload

import nanoocp.Aspect
import nanoocp.Standard
import nanoocp.TCollection


class Cocoa_LocalPool:
    """Auxiliary class to create local pool."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Cocoa_LocalPool) -> None: ...

class Cocoa_Window(nanoocp.Aspect.Aspect_Window):
    """This class defines Cocoa window"""

    @overload
    def __init__(self, theTitle: str, thePxLeft: int, thePxTop: int, thePxWidth: int, thePxHeight: int) -> None:
        """
        Creates a NSWindow and NSView defined by his position and size in pixels
        """

    @overload
    def __init__(self, theOther: Cocoa_Window) -> None: ...

    @staticmethod
    def VirtualKeyFromNative(theKey: int) -> int:
        """Convert Carbon virtual key into Aspect_VKey."""

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

    def NativeHandle(self) -> int:
        """@return native Window handle"""

    def NativeParentHandle(self) -> int:
        """@return parent of native Window handle"""

    def SetTitle(self, theTitle: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets window title."""

    def InvalidateContent(self, theDisp: nanoocp.Aspect.Aspect_DisplayConnection | None = None) -> None:
        """
        Invalidate entire window content by setting NSView::setNeedsDisplay property.
        Call will be implicitly redirected to the main thread when called from non-GUI thread.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
