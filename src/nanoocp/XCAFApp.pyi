"""OCCT package XCAFApp (toolkit TKXCAF)"""

import nanoocp.CDM
import nanoocp.Standard
import nanoocp.TDocStd


class XCAFApp_Application(nanoocp.TDocStd.TDocStd_Application):
    """Implements an Application for the DECAF documents"""

    def __init__(self, theOther: XCAFApp_Application) -> None: ...

    def ResourcesName(self) -> str:
        """
        methods from TDocStd_Application
        ================================
        """

    def InitDocument(self, aDoc: nanoocp.CDM.CDM_Document | None) -> None:
        """Set XCAFDoc_DocumentTool attribute"""

    @staticmethod
    def GetApplication() -> XCAFApp_Application:
        """
        Initializes (for the first time) and returns the
        static object (XCAFApp_Application)
        This is the only valid method to get XCAFApp_Application
        object, and it should be called at least once before
        any actions with documents in order to init application
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
