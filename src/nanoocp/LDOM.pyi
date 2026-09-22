"""OCCT package LDOM (toolkit TKCDF)"""

import enum
from typing import TextIO, overload

import nanoocp.Standard
import nanoocp.TCollection


class LDOMBasicString:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, anOther: LDOMBasicString) -> None: ...

    @overload
    def __init__(self, aValue: int) -> None: ...

    @overload
    def __init__(self, aValue: str) -> None: ...

    @overload
    def __init__(self, aValue: str, aDoc: LDOM_MemManager | None) -> None: ...

    @overload
    def __init__(self, aValue: str, aLen: int, aDoc: LDOM_MemManager | None) -> None: ...

    class StringType(enum.IntEnum):
        LDOM_NULL = 0

        LDOM_Integer = 1

        LDOM_AsciiFree = 2

        LDOM_AsciiDoc = 3

        LDOM_AsciiDocClear = 4

        LDOM_AsciiHashed = 5

    LDOM_NULL: LDOMBasicString.StringType = StringType.LDOM_NULL

    LDOM_Integer: LDOMBasicString.StringType = StringType.LDOM_Integer

    LDOM_AsciiFree: LDOMBasicString.StringType = StringType.LDOM_AsciiFree

    LDOM_AsciiDoc: LDOMBasicString.StringType = StringType.LDOM_AsciiDoc

    LDOM_AsciiDocClear: LDOMBasicString.StringType = StringType.LDOM_AsciiDocClear

    LDOM_AsciiHashed: LDOMBasicString.StringType = StringType.LDOM_AsciiHashed

    def Type(self) -> LDOMBasicString.StringType: ...

    def GetInteger(self) -> tuple[bool, int]: ...

    def GetString(self) -> str: ...

    def equals(self, anOther: LDOMBasicString) -> bool: ...

    def __eq__(self, anOther: LDOMBasicString) -> bool: ...

    def __ne__(self, anOther: LDOMBasicString) -> bool: ...

class LDOMString(LDOMBasicString):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, anOther: LDOMString) -> None: ...

    @overload
    def __init__(self, aValue: int) -> None: ...

    @overload
    def __init__(self, aValue: str) -> None: ...

    def getOwnerDocument(self) -> LDOM_MemManager: ...

class LDOM_MemManager(nanoocp.Standard.Standard_Transient):
    def __init__(self, aBlockSize: int) -> None: ...

    @overload
    def HashedAllocate(self, aString: str, theLen: int) -> tuple[str, int]: ...

    @overload
    def HashedAllocate(self, aString: str, theLen: int, theResult: LDOMBasicString) -> None: ...

    @staticmethod
    def Hash(theString: str, theLen: int) -> int: ...

    @staticmethod
    def CompareStrings(theString: str, theHashValue: int, theHashedStr: str) -> bool: ...

    def Self(self) -> LDOM_MemManager: ...

    def RootElement(self) -> LDOM_BasicElement: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class LDOM_Node:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, anOther: LDOM_Node) -> None: ...

    class NodeType(enum.IntEnum):
        UNKNOWN = 0

        ELEMENT_NODE = 1

        ATTRIBUTE_NODE = 2

        TEXT_NODE = 3

        CDATA_SECTION_NODE = 4

        COMMENT_NODE = 8

    UNKNOWN: LDOM_Node.NodeType = NodeType.UNKNOWN

    ELEMENT_NODE: LDOM_Node.NodeType = NodeType.ELEMENT_NODE

    ATTRIBUTE_NODE: LDOM_Node.NodeType = NodeType.ATTRIBUTE_NODE

    TEXT_NODE: LDOM_Node.NodeType = NodeType.TEXT_NODE

    CDATA_SECTION_NODE: LDOM_Node.NodeType = NodeType.CDATA_SECTION_NODE

    COMMENT_NODE: LDOM_Node.NodeType = NodeType.COMMENT_NODE

    def getOwnerDocument(self) -> LDOM_MemManager: ...

    def __eq__(self, anOther: LDOM_Node) -> bool: ...

    def __ne__(self, anOther: LDOM_Node) -> bool: ...

    def isNull(self) -> bool: ...

    def getNodeType(self) -> LDOM_Node.NodeType: ...

    def getNodeName(self) -> LDOMString: ...

    def getNodeValue(self) -> LDOMString: ...

    def getFirstChild(self) -> LDOM_Node: ...

    def getLastChild(self) -> LDOM_Node: ...

    def getNextSibling(self) -> LDOM_Node: ...

    def removeChild(self, aChild: LDOM_Node) -> None: ...

    def appendChild(self, aChild: LDOM_Node) -> None: ...

    def hasChildNodes(self) -> bool: ...

    def SetValueClear(self) -> None: ...

class LDOM_Attr(LDOM_Node):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, anOther: LDOM_Attr) -> None: ...

    def getName(self) -> LDOMString: ...

    def getValue(self) -> LDOMString: ...

    def setValue(self, aValue: LDOMString) -> None: ...

class LDOM_BasicNode:
    def isNull(self) -> bool: ...

    def getNodeType(self) -> LDOM_Node.NodeType: ...

    def GetSibling(self) -> LDOM_BasicNode: ...

class LDOM_BasicAttribute(LDOM_BasicNode):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LDOM_BasicAttribute) -> None: ...

    def GetName(self) -> str: ...

    def GetValue(self) -> LDOMBasicString: ...

    def SetValue(self, aValue: LDOMBasicString, aDoc: LDOM_MemManager | None) -> None: ...

class LDOM_BasicElement(LDOM_BasicNode):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LDOM_BasicElement) -> None: ...

    @staticmethod
    def Create(aName: str, aLength: int, aDoc: LDOM_MemManager | None) -> LDOM_BasicElement: ...

    def GetTagName(self) -> str: ...

    def GetFirstChild(self) -> LDOM_BasicNode: ...

    def GetLastChild(self) -> LDOM_BasicNode: ...

    def GetAttribute(self, aName: LDOMBasicString, aLastCh: LDOM_BasicNode) -> LDOM_BasicAttribute: ...

class LDOM_BasicText(LDOM_BasicNode):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LDOM_BasicText) -> None: ...

    def GetData(self) -> LDOMBasicString: ...

    def SetData(self, aValue: LDOMBasicString, aDoc: LDOM_MemManager | None) -> None: ...

class LDOM_CharacterData(LDOM_Node):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LDOM_CharacterData) -> None: ...

    def getData(self) -> LDOMString: ...

    def setData(self, aValue: LDOMString) -> None: ...

    def getLength(self) -> int: ...

class LDOM_Text(LDOM_CharacterData):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, anOther: LDOM_Text) -> None: ...

class LDOM_CDATASection(LDOM_Text):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LDOM_CDATASection) -> None: ...

class LDOM_CharReference:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LDOM_CharReference) -> None: ...

class LDOM_Comment(LDOM_CharacterData):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LDOM_Comment) -> None: ...

class LDOM_NodeList:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LDOM_NodeList) -> None: ...

    def item(self, arg0: int) -> LDOM_Node: ...

    def getLength(self) -> int: ...

class LDOM_Element(LDOM_Node):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, anOther: LDOM_Element) -> None: ...

    def getTagName(self) -> LDOMString: ...

    def getAttribute(self, aName: LDOMString) -> LDOMString: ...

    def getAttributeNode(self, aName: LDOMString) -> LDOM_Attr: ...

    def getElementsByTagName(self, aName: LDOMString) -> LDOM_NodeList: ...

    def setAttribute(self, aName: LDOMString, aValue: LDOMString) -> None: ...

    def setAttributeNode(self, aNewAttr: LDOM_Attr) -> None: ...

    def removeAttribute(self, aName: LDOMString) -> None: ...

    def GetChildByTagName(self, aTagName: LDOMString) -> LDOM_Element: ...

    def GetSiblingByTagName(self) -> LDOM_Element: ...

    def ReplaceElement(self, anOther: LDOM_Element) -> None: ...

    def GetAttributesList(self) -> LDOM_NodeList: ...

class LDOM_Document:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aMemManager: LDOM_MemManager) -> None: ...

    @overload
    def __init__(self, theOther: LDOM_Document) -> None: ...

    @staticmethod
    def createDocument(theQualifiedName: LDOMString) -> LDOM_Document: ...

    def createElement(self, theTagName: LDOMString) -> LDOM_Element: ...

    def createCDATASection(self, theData: LDOMString) -> LDOM_CDATASection: ...

    def createComment(self, theData: LDOMString) -> LDOM_Comment: ...

    def createTextNode(self, theData: LDOMString) -> LDOM_Text: ...

    def getDocumentElement(self) -> LDOM_Element: ...

    def getElementsByTagName(self, theTagName: LDOMString) -> LDOM_NodeList: ...

    def __eq__(self, anOther: LDOM_Document) -> bool: ...

    def __ne__(self, anOther: LDOM_Document) -> bool: ...

    def isNull(self) -> bool: ...

class LDOM_DocumentType:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LDOM_DocumentType) -> None: ...

class LDOM_LDOMImplementation:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: LDOM_LDOMImplementation) -> None: ...

    @staticmethod
    def createDocument(aNamespaceURI: LDOMString, aQualifiedName: LDOMString, aDocType: LDOM_DocumentType) -> LDOM_Document: ...

class LDOM_XmlReader:
    def __init__(self, aDocument: LDOM_MemManager | None, anErrorString: nanoocp.TCollection.TCollection_AsciiString, theTagPerStep: bool = False) -> None: ...

    class RecordType(enum.IntEnum):
        XML_UNKNOWN = 0

        XML_HEADER = 1

        XML_DOCTYPE = 2

        XML_COMMENT = 3

        XML_START_ELEMENT = 4

        XML_END_ELEMENT = 5

        XML_FULL_ELEMENT = 6

        XML_TEXT = 7

        XML_CDATA = 8

        XML_EOF = 9

    XML_UNKNOWN: LDOM_XmlReader.RecordType = RecordType.XML_UNKNOWN

    XML_HEADER: LDOM_XmlReader.RecordType = RecordType.XML_HEADER

    XML_DOCTYPE: LDOM_XmlReader.RecordType = RecordType.XML_DOCTYPE

    XML_COMMENT: LDOM_XmlReader.RecordType = RecordType.XML_COMMENT

    XML_START_ELEMENT: LDOM_XmlReader.RecordType = RecordType.XML_START_ELEMENT

    XML_END_ELEMENT: LDOM_XmlReader.RecordType = RecordType.XML_END_ELEMENT

    XML_FULL_ELEMENT: LDOM_XmlReader.RecordType = RecordType.XML_FULL_ELEMENT

    XML_TEXT: LDOM_XmlReader.RecordType = RecordType.XML_TEXT

    XML_CDATA: LDOM_XmlReader.RecordType = RecordType.XML_CDATA

    XML_EOF: LDOM_XmlReader.RecordType = RecordType.XML_EOF

    def ReadRecord(self, theIStream: TextIO, theData: "LDOM_OSStream") -> tuple[LDOM_XmlReader.RecordType, bool]: ...

    def GetElement(self) -> LDOM_BasicElement: ...

    def CreateElement(self, theName: str, theLen: int) -> None: ...

    @staticmethod
    def getInteger(theValue: LDOMBasicString, theStart: str, theEnd: str) -> bool: ...

    def GetBOM(self) -> "LDOM_OSStream::BOMType": ...

class LDOM_XmlWriter:
    def __init__(self, theEncoding: str | None = None) -> None: ...

    def SetIndentation(self, theIndent: int) -> None: ...

    @overload
    def Write(self, theDoc: LDOM_Document) -> str: ...

    @overload
    def Write(self, theNode: LDOM_Node) -> str: ...

class LDOMParser:
    def __init__(self) -> None: ...

    def getDocument(self) -> LDOM_Document: ...

    @overload
    def parse(self, aFileName: str) -> bool: ...

    @overload
    def parse(self, anInput: TextIO, theTagPerStep: bool = False, theWithoutRoot: bool = False) -> bool: ...

    def GetError(self, aData: nanoocp.TCollection.TCollection_AsciiString) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def GetBOM(self) -> "LDOM_OSStream::BOMType": ...
