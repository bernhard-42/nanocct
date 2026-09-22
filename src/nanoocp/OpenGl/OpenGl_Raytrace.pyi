"""C++ namespace OpenGl_Raytrace (OCCT package OpenGl)"""

from typing import overload

import nanoocp.OpenGl


def IsRaytracedGroup(theGroup: nanoocp.OpenGl.OpenGl_Group) -> bool:
    """Checks to see if the group contains ray-trace geometry."""

@overload
def IsRaytracedElement(theNode: nanoocp.OpenGl.OpenGl_ElementNode) -> bool: ...

@overload
def IsRaytracedElement(theElement: nanoocp.OpenGl.OpenGl_Element) -> bool:
    """Checks to see if the element contains ray-trace geometry."""
