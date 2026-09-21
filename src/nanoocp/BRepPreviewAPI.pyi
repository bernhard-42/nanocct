"""OCCT package BRepPreviewAPI (toolkit TKPrim)"""

from typing import overload

import nanoocp.BRepPrimAPI
import nanoocp.Message


class BRepPreviewAPI_MakeBox(nanoocp.BRepPrimAPI.BRepPrimAPI_MakeBox):
    """
    Builds a valid box, if points fulfill the conditions of a valid box.
    And allows to build a preview, otherwise.
    There are 4 cases:
    1 - preview can be a vertex if thin box in all directions is a point;
    2 - preview can be an edge if thin box in two directions is a point;
    3 - preview can be a rectangular face if thin box in only one direction is a point;
    4 - preview can be a valid box if point values fulfill the conditions of a valid box.
    """

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BRepPreviewAPI_MakeBox) -> None: ...

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Creates a preview depending on point values."""
