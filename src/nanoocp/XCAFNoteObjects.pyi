"""OCCT package XCAFNoteObjects (toolkit TKXCAF)"""

from typing import overload

import nanoocp.Standard
import nanoocp.TopoDS
import nanoocp.gp


class XCAFNoteObjects_NoteObject(nanoocp.Standard.Standard_Transient):
    """object to store note auxiliary data"""

    @overload
    def __init__(self) -> None:
        """Empty object"""

    @overload
    def __init__(self, theObj: XCAFNoteObjects_NoteObject | None) -> None:
        """Copy constructor."""

    @overload
    def __init__(self, theOther: XCAFNoteObjects_NoteObject) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def HasPlane(self) -> bool:
        """Returns True if plane is specified"""

    def GetPlane(self) -> nanoocp.gp.gp_Ax2:
        """Returns a right-handed coordinate system of the plane"""

    def SetPlane(self, thePlane: nanoocp.gp.gp_Ax2) -> None:
        """Sets a right-handed coordinate system of the plane"""

    def HasPoint(self) -> bool:
        """
        Returns True if the attachment point on the annotated object is specified
        """

    def GetPoint(self) -> nanoocp.gp.gp_Pnt:
        """Returns the attachment point on the annotated object"""

    def SetPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """Sets the anchor point on the annotated object"""

    def HasPointText(self) -> bool:
        """Returns True if the text position is specified"""

    def GetPointText(self) -> nanoocp.gp.gp_Pnt:
        """Returns the text position"""

    def SetPointText(self, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """Sets the text position"""

    def GetPresentation(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns a tessellated annotation if specified"""

    def SetPresentation(self, thePresentation: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Sets a tessellated annotation"""

    def Reset(self) -> None:
        """Resets data to the state after calling the default constructor"""
