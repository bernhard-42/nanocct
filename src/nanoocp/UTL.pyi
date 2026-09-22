"""OCCT package UTL (toolkit TKCDF)"""

from typing import overload

import nanoocp.OSD
import nanoocp.Resource
import nanoocp.Standard
import nanoocp.Storage
import nanoocp.TCollection


class UTL:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: UTL) -> None: ...

    @staticmethod
    def xgetenv(aCString: str) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    @staticmethod
    def OpenFile(aFile: nanoocp.Storage.Storage_BaseDriver | None, aName: nanoocp.TCollection.TCollection_ExtendedString, aMode: nanoocp.Storage.Storage_OpenMode) -> nanoocp.Storage.Storage_Error: ...

    @staticmethod
    def AddToUserInfo(aData: nanoocp.Storage.Storage_Data | None, anInfo: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

    @staticmethod
    def Path(aFileName: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.OSD.OSD_Path: ...

    @staticmethod
    def Disk(aPath: nanoocp.OSD.OSD_Path) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    @staticmethod
    def Trek(aPath: nanoocp.OSD.OSD_Path) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    @staticmethod
    def Name(aPath: nanoocp.OSD.OSD_Path) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    @overload
    @staticmethod
    def Extension(aPath: nanoocp.OSD.OSD_Path) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    @overload
    @staticmethod
    def Extension(aFileName: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    @staticmethod
    def FileIterator(aPath: nanoocp.OSD.OSD_Path, aMask: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.OSD.OSD_FileIterator: ...

    @staticmethod
    def LocalHost() -> nanoocp.TCollection.TCollection_ExtendedString: ...

    @staticmethod
    def ExtendedString(anAsciiString: nanoocp.TCollection.TCollection_AsciiString) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    @staticmethod
    def GUID(anXString: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def Find(aResourceManager: nanoocp.Resource.Resource_Manager | None, aResourceName: nanoocp.TCollection.TCollection_ExtendedString) -> bool: ...

    @staticmethod
    def Value(aResourceManager: nanoocp.Resource.Resource_Manager | None, aResourceName: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    @staticmethod
    def IntegerValue(anExtendedString: nanoocp.TCollection.TCollection_ExtendedString) -> int: ...

    @staticmethod
    def CString(anExtendedString: nanoocp.TCollection.TCollection_ExtendedString) -> str: ...

    @staticmethod
    def IsReadOnly(aFileName: nanoocp.TCollection.TCollection_ExtendedString) -> bool: ...
