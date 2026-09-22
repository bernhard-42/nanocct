"""OCCT package XmlMNaming (toolkit TKXml)"""

from typing import overload

import nanoocp.LDOM
import nanoocp.Message
import nanoocp.Standard
import nanoocp.TDF
import nanoocp.TDocStd
import nanoocp.TopAbs
import nanoocp.TopTools
import nanoocp.TopoDS
import nanoocp.XmlMDF
import nanoocp.XmlObjMgt


class XmlMNaming:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XmlMNaming) -> None: ...

    @staticmethod
    def AddDrivers(aDriverTable: nanoocp.XmlMDF.XmlMDF_ADriverTable | None, aMessageDriver: nanoocp.Message.Message_Messenger | None) -> None:
        """Adds the attribute drivers to <aDriverTable>."""

class XmlMNaming_NamedShapeDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    @overload
    def __init__(self, aMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMNaming_NamedShapeDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: ...

    def ReadShapeSection(self, anElement: nanoocp.LDOM.LDOM_Element, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Input the shapes from DOM element"""

    def WriteShapeSection(self, anElement: nanoocp.LDOM.LDOM_Element, theStorageFormatVersion: nanoocp.TDocStd.TDocStd_FormatVersion, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Output the shapes into DOM element"""

    def Clear(self) -> None:
        """Clear myShapeSet"""

    def GetShapesLocations(self) -> nanoocp.TopTools.TopTools_LocationSet:
        """get the format of topology"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlMNaming_NamingDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    @overload
    def __init__(self, aMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMNaming_NamingDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, theSource: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theTarget: nanoocp.TDF.TDF_Attribute | None, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, theSource: nanoocp.TDF.TDF_Attribute | None, theTarget: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, theRelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlMNaming_Shape1:
    """
    The XmlMNaming_Shape1 is the Persistent view of a TopoDS_Shape.

    Shape1 contains:
    - a reference to a TShape
    - a reference to Location
    - an Orientation.
    """

    @overload
    def __init__(self, Doc: nanoocp.LDOM.LDOM_Document) -> None: ...

    @overload
    def __init__(self, E: nanoocp.LDOM.LDOM_Element) -> None: ...

    @overload
    def __init__(self, theOther: XmlMNaming_Shape1) -> None: ...

    def Element(self) -> nanoocp.LDOM.LDOM_Element:
        """return myElement"""

    def TShapeId(self) -> int: ...

    def LocId(self) -> int: ...

    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def SetShape(self, ID: int, LocID: int, Orient: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    def SetVertex(self, theVertex: nanoocp.TopoDS.TopoDS_Shape) -> None: ...
