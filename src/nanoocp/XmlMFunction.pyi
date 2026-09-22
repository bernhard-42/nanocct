"""OCCT package XmlMFunction (toolkit TKXmlL)"""

from typing import overload

import nanoocp.Message
import nanoocp.Standard
import nanoocp.TDF
import nanoocp.XmlMDF
import nanoocp.XmlObjMgt


class XmlMFunction:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XmlMFunction) -> None: ...

    @staticmethod
    def AddDrivers(aDriverTable: nanoocp.XmlMDF.XmlMDF_ADriverTable | None, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None:
        """Adds the attribute storage drivers to <aDriverTable>."""

class XmlMFunction_FunctionDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    """Attribute Driver."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMFunction_FunctionDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, Source: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, Target: nanoocp.TDF.TDF_Attribute | None, RelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, Source: nanoocp.TDF.TDF_Attribute | None, Target: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, RelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlMFunction_GraphNodeDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    """XML persistence driver for dependencies of a function."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMFunction_GraphNodeDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, Source: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, Target: nanoocp.TDF.TDF_Attribute | None, RelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, Source: nanoocp.TDF.TDF_Attribute | None, Target: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, RelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XmlMFunction_ScopeDriver(nanoocp.XmlMDF.XmlMDF_ADriver):
    """XML persistence driver for a scope of functions."""

    @overload
    def __init__(self, theMessageDriver: nanoocp.Message.Message_Messenger | None) -> None: ...

    @overload
    def __init__(self, theOther: XmlMFunction_ScopeDriver) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @overload
    def Paste(self, Source: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, Target: nanoocp.TDF.TDF_Attribute | None, RelocTable: nanoocp.XmlObjMgt.XmlObjMgt_RRelocationTable) -> bool: ...

    @overload
    def Paste(self, Source: nanoocp.TDF.TDF_Attribute | None, Target: nanoocp.XmlObjMgt.XmlObjMgt_Persistent, RelocTable: nanoocp.XmlObjMgt.XmlObjMgt_SRelocationTable) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
