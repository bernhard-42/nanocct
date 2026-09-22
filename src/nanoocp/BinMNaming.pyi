"""OCCT package BinMNaming (toolkit TKBin)"""

from typing import BinaryIO, overload

import nanoocp.BinMDF
import nanoocp.BinObjMgt
import nanoocp.BinTools
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TDF


class BinMNaming:
    """Storage/Retrieval drivers for TNaming attributes"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BinMNaming) -> None: ...

    @staticmethod
    def AddDrivers(theDriverTable: nanoocp.BinMDF.BinMDF_ADriverTable | None, aMsgDrv: nanoocp.Message.Message_Messenger | None) -> None:
        """Adds the attribute drivers to <theDriverTable>."""

class BinMNaming_NamedShapeDriver(nanoocp.BinMDF.BinMDF_ADriver):
    """NamedShape Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMNaming_NamedShapeDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, Source: nanoocp.BinObjMgt.BinObjMgt_Persistent, Target: nanoocp.TDF.TDF_Attribute | None, RelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, Source: nanoocp.TDF.TDF_Attribute | None, Target: nanoocp.BinObjMgt.BinObjMgt_Persistent, RelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    def ReadShapeSection(self, theIS: BinaryIO, therange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Input the shapes from Bin Document file"""

    def WriteShapeSection(self, theDocVer: int, therange: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """Output the shapes into Bin Document file"""

    def Clear(self) -> None:
        """Clear myShapeSet"""

    def IsWithTriangles(self) -> bool:
        """Return true if shape should be stored with triangles."""

    def IsWithNormals(self) -> bool:
        """Return true if shape should be stored with triangulation normals."""

    def SetWithTriangles(self, isWithTriangles: bool) -> None:
        """set whether to store triangulation"""

    def SetWithNormals(self, isWithNormals: bool) -> None:
        """set whether to store triangulation with normals"""

    def GetShapesLocations(self) -> nanoocp.BinTools.BinTools_LocationSet:
        """get the shapes locations"""

    def EnableQuickPart(self, theValue: bool) -> None:
        """
        Sets the flag for quick part of the document access: shapes are stored in the attribute.
        """

    def IsQuickPart(self) -> bool:
        """
        Returns true if quick part of the document access is enabled: shapes are stored in the
        attribute.
        """

    def ShapeSet(self, theReading: bool) -> nanoocp.BinTools.BinTools_ShapeSetBase:
        """Returns shape-set of the needed type"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinMNaming_NamingDriver(nanoocp.BinMDF.BinMDF_ADriver):
    """Naming Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: BinMNaming_NamingDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, Source: nanoocp.BinObjMgt.BinObjMgt_Persistent, Target: nanoocp.TDF.TDF_Attribute | None, RelocTable: nanoocp.BinObjMgt.BinObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, Source: nanoocp.TDF.TDF_Attribute | None, Target: nanoocp.BinObjMgt.BinObjMgt_Persistent, RelocTable: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Standard.Standard_Transient]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
