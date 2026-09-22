"""OCCT package BinObjMgt (toolkit TKBinL)"""

from typing import BinaryIO, overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.Storage
import nanoocp.TCollection
import nanoocp.TDF


class BinObjMgt_Position(nanoocp.Standard.Standard_Transient):
    """Stores and manipulates position in the stream."""

    def __init__(self, theOther: BinObjMgt_Position) -> None: ...

    def StoreSize(self) -> bytes:
        """Stores the difference between the current position and the stored one."""

    def WriteSize(self, theDummy: bool = False) -> bytes:
        """
        Writes stored size at the stored position. Changes the current stream position.
        If theDummy is true, is writes to the current position zero size.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BinObjMgt_Persistent:
    """
    Binary persistent representation of an object.
    Really it is used as a buffer for read/write an object.

    It takes care of Little/Big endian by inversing bytes
    in objects of standard types (see FSD_FileHeader.hxx
    for the default value of DO_INVERSE).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: BinObjMgt_Persistent) -> None: ...

    def PutCharacter(self, theValue: str) -> BinObjMgt_Persistent: ...

    def PutByte(self, theValue: int) -> BinObjMgt_Persistent: ...

    def PutExtCharacter(self, theValue: str) -> BinObjMgt_Persistent: ...

    def PutInteger(self, theValue: int) -> BinObjMgt_Persistent: ...

    def PutBoolean(self, theValue: bool) -> BinObjMgt_Persistent: ...

    def PutReal(self, theValue: float) -> BinObjMgt_Persistent: ...

    def PutShortReal(self, theValue: float) -> BinObjMgt_Persistent: ...

    def PutCString(self, theValue: str) -> BinObjMgt_Persistent:
        """Offset in output buffer is not aligned"""

    def PutAsciiString(self, theValue: nanoocp.TCollection.TCollection_AsciiString) -> BinObjMgt_Persistent:
        """Offset in output buffer is word-aligned"""

    def PutExtendedString(self, theValue: nanoocp.TCollection.TCollection_ExtendedString) -> BinObjMgt_Persistent:
        """Offset in output buffer is word-aligned"""

    def PutLabel(self, theValue: nanoocp.TDF.TDF_Label) -> BinObjMgt_Persistent: ...

    def PutGUID(self, theValue: nanoocp.Standard.Standard_GUID) -> BinObjMgt_Persistent: ...

    def GetCharacter(self) -> str: ...

    def GetByte(self) -> int: ...

    def GetExtCharacter(self) -> str: ...

    def GetInteger(self) -> int: ...

    def GetBoolean(self) -> bool: ...

    def GetReal(self) -> float: ...

    def GetShortReal(self) -> float: ...

    def GetAsciiString(self, theValue: nanoocp.TCollection.TCollection_AsciiString) -> BinObjMgt_Persistent: ...

    def GetExtendedString(self, theValue: nanoocp.TCollection.TCollection_ExtendedString) -> BinObjMgt_Persistent: ...

    def GetLabel(self, theDS: nanoocp.TDF.TDF_Data | None, theValue: nanoocp.TDF.TDF_Label) -> BinObjMgt_Persistent: ...

    def GetGUID(self, theValue: nanoocp.Standard.Standard_GUID) -> BinObjMgt_Persistent: ...

    def Position(self) -> int:
        """Tells the current position for get/put"""

    def SetPosition(self, thePos: int) -> bool:
        """
        Sets the current position for get/put.
        Resets an error state depending on the validity of thePos.
        Returns the new state (value of IsOK())
        """

    def Truncate(self) -> None:
        """
        Truncates the buffer by current position,
        i.e. updates mySize
        """

    def IsError(self) -> bool:
        """Indicates an error after Get methods or SetPosition"""

    def __not__(self) -> bool: ...

    def IsOK(self) -> bool:
        """Indicates a good state after Get methods or SetPosition"""

    def Init(self) -> None:
        """Initializes me to reuse again"""

    def SetId(self, theId: int) -> None:
        """Sets the Id of the object"""

    def SetTypeId(self, theId: int) -> None:
        """Sets the Id of the type of the object"""

    def Id(self) -> int:
        """Returns the Id of the object"""

    def TypeId(self) -> int:
        """Returns the Id of the type of the object"""

    def Length(self) -> int:
        """Returns the length of data"""

    def Write(self, theDirectStream: bool = False) -> bytes:
        """
        Stores <me> to the stream.
        inline Standard_OStream& operator<< (Standard_OStream&,
        BinObjMgt_Persistent&) is also available.
        If theDirectStream is true, after this data the direct stream data is stored.
        """

    def Read(self, theIS: BinaryIO) -> None:
        """
        Retrieves <me> from the stream.
        inline Standard_IStream& operator>> (Standard_IStream&,
        BinObjMgt_Persistent&) is also available
        """

    def Destroy(self) -> None:
        """
        Frees the allocated memory;
        This object can be reused after call to Init
        """

    def IsDirect(self) -> bool:
        """
        Returns true if after this record a direct writing to the stream is performed.
        """

    def StreamStart(self) -> BinObjMgt_Position:
        """Returns the start position of the direct writing in the stream"""

    def __bool__(self) -> bool: ...

class BinObjMgt_RRelocationTable(nanoocp.NCollection.NCollection_DataMap[int, nanoocp.Standard.Standard_Transient]):
    """
    Retrieval relocation table is modeled as a child class of
    NCollection_DataMap<int, occ::handle<Standard_Transient>> that stores a handle to the file
    header section. With that attribute drivers have access to the file header
    section.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BinObjMgt_RRelocationTable) -> None: ...

    def GetHeaderData(self) -> nanoocp.Storage.Storage_HeaderData:
        """Returns a handle to the header data of the file that is begin read"""

    def SetHeaderData(self, theHeaderData: nanoocp.Storage.Storage_HeaderData | None) -> None:
        """
        Sets the storage header data.

        @param theHeaderData header data of the file that is begin read
        """

    def Clear(self, doReleaseMemory: bool = True) -> None: ...
