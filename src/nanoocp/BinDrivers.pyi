"""OCCT package BinDrivers (toolkit TKBin)"""

import enum
from typing import BinaryIO, overload

import nanoocp.BinLDrivers
import nanoocp.BinMDF
import nanoocp.Message
import nanoocp.Standard
import nanoocp.TDocStd


class BinDrivers_Marker(enum.IntEnum):
    BinDrivers_ENDATTRLIST = -1

    BinDrivers_ENDLABEL = -2

BinDrivers_ENDATTRLIST: BinDrivers_Marker = BinDrivers_Marker.BinDrivers_ENDATTRLIST

BinDrivers_ENDLABEL: BinDrivers_Marker = BinDrivers_Marker.BinDrivers_ENDLABEL

class BinDrivers:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BinDrivers) -> None: ...

    @staticmethod
    def Factory(theGUID: nanoocp.Standard.Standard_GUID) -> nanoocp.Standard.Standard_Transient: ...

    @staticmethod
    def DefineFormat(theApp: nanoocp.TDocStd.TDocStd_Application | None) -> None:
        """
        Defines format "BinOcaf" and registers its read and write drivers
        in the specified application
        """

    @staticmethod
    def AttributeDrivers(MsgDrv: nanoocp.Message.Message_Messenger | None) -> nanoocp.BinMDF.BinMDF_ADriverTable:
        """Creates the table of drivers of types supported"""

class BinDrivers_DocumentRetrievalDriver(nanoocp.BinLDrivers.BinLDrivers_DocumentRetrievalDriver):
    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BinDrivers_DocumentRetrievalDriver) -> None: ...

    def AttributeDrivers(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> nanoocp.BinMDF.BinMDF_ADriverTable: ...

    def ReadShapeSection(self, theSection: nanoocp.BinLDrivers.BinLDrivers_DocumentSection, theIS: BinaryIO, isMess: bool = False, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    def CheckShapeSection(self, thePos: int, theIS: BinaryIO) -> None: ...

    def Clear(self) -> None:
        """Clears the NamedShape driver"""

    def EnableQuickPartReading(self, theMessageDriver: nanoocp.Message.Message_Messenger | None, theValue: bool) -> None:
        """Enables reading in the quick part access mode."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinDrivers_DocumentStorageDriver(nanoocp.BinLDrivers.BinLDrivers_DocumentStorageDriver):
    """persistent implementation of storage a document in a binary file"""

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BinDrivers_DocumentStorageDriver) -> None: ...

    def AttributeDrivers(self, theMsgDriver: nanoocp.Message.Message_Messenger | None) -> nanoocp.BinMDF.BinMDF_ADriverTable: ...

    def WriteShapeSection(self, theDocSection: nanoocp.BinLDrivers.BinLDrivers_DocumentSection, theDocVer: nanoocp.TDocStd.TDocStd_FormatVersion, theRange: nanoocp.Message.Message_ProgressRange = ...) -> bytes:
        """implements the procedure of writing a shape section to file"""

    def IsWithTriangles(self) -> bool:
        """Return true if shape should be stored with triangles."""

    def IsWithNormals(self) -> bool:
        """Return true if shape should be stored with triangulation normals."""

    def SetWithTriangles(self, theMessageDriver: nanoocp.Message.Message_Messenger | None, theWithTriangulation: bool) -> None:
        """Set if triangulation should be stored or not."""

    def SetWithNormals(self, theMessageDriver: nanoocp.Message.Message_Messenger | None, theWithTriangulation: bool) -> None:
        """Set if triangulation should be stored with normals or not."""

    def EnableQuickPartWriting(self, theMessageDriver: nanoocp.Message.Message_Messenger | None, theValue: bool) -> None:
        """Enables writing in the quick part access mode."""

    def Clear(self) -> None:
        """Clears the NamedShape driver"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
