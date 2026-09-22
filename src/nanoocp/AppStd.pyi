"""OCCT package AppStd (toolkit TKCAF)"""

from typing import overload

import nanoocp.Standard
import nanoocp.TDocStd


class AppStd_Application(nanoocp.TDocStd.TDocStd_Application):
    """Legacy class defining resources name for standard OCAF documents"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: AppStd_Application) -> None: ...

    def ResourcesName(self) -> str:
        """returns the file name which contains application resources"""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
