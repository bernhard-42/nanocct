"""OCCT package Resource (toolkit TKernel)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection


class Resource_FormatType(enum.IntEnum):
    """
    List of non ASCII format types which may be converted into the Unicode 16 bits format type.
    Use the functions provided by the Resource_Unicode class to convert a string
    from one of these non ASCII format to Unicode, and vice versa.
    """

    Resource_FormatType_SJIS = 0

    Resource_FormatType_EUC = 1

    Resource_FormatType_NoConversion = 2

    Resource_FormatType_GB = 3

    Resource_FormatType_UTF8 = 4

    Resource_FormatType_SystemLocale = 5

    Resource_FormatType_CP1250 = 6

    Resource_FormatType_CP1251 = 7

    Resource_FormatType_CP1252 = 8

    Resource_FormatType_CP1253 = 9

    Resource_FormatType_CP1254 = 10

    Resource_FormatType_CP1255 = 11

    Resource_FormatType_CP1256 = 12

    Resource_FormatType_CP1257 = 13

    Resource_FormatType_CP1258 = 14

    Resource_FormatType_iso8859_1 = 15

    Resource_FormatType_iso8859_2 = 16

    Resource_FormatType_iso8859_3 = 17

    Resource_FormatType_iso8859_4 = 18

    Resource_FormatType_iso8859_5 = 19

    Resource_FormatType_iso8859_6 = 20

    Resource_FormatType_iso8859_7 = 21

    Resource_FormatType_iso8859_8 = 22

    Resource_FormatType_iso8859_9 = 23

    Resource_FormatType_CP850 = 24

    Resource_FormatType_GBK = 25

    Resource_FormatType_Big5 = 26

    Resource_FormatType_ANSI = 2

    Resource_SJIS = 0

    Resource_EUC = 1

    Resource_ANSI = 2

    Resource_GB = 3

class Resource_LexicalCompare:
    def __init__(self) -> None: ...

    def IsLower(self, Left: nanoocp.TCollection.TCollection_AsciiString, Right: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Returns True if <Left> is lower than <Right>."""

class Resource_Manager(nanoocp.Standard.Standard_Transient):
    """Defines a resource structure and its management methods."""

    @overload
    def __init__(self) -> None:
        """Create an empty Resource manager"""

    @overload
    def __init__(self, aName: str, Verbose: bool = False) -> None:
        """
        Create a Resource manager.
        Attempts to find the two following files:
        $CSF_`aName`Defaults/aName
        $CSF_`aName`UserDefaults/aName
        and load them respectively into a reference and a user resource structure.

        If CSF_ResourceVerbose defined, seeked files will be printed.

        FILE SYNTAX
        The syntax of a resource file is a sequence of resource
        lines terminated by newline characters or end of file. The
        syntax of an individual resource line is:
        """

    @overload
    def __init__(self, theName: nanoocp.TCollection.TCollection_AsciiString, theDefaultsDirectory: nanoocp.TCollection.TCollection_AsciiString, theUserDefaultsDirectory: nanoocp.TCollection.TCollection_AsciiString, theIsVerbose: bool = False) -> None:
        """
        Create a Resource manager.
        @param[in] theName  description file name
        @param[in] theDefaultsDirectory   default folder for looking description file
        @param[in] theUserDefaultsDirectory  user folder for looking description file
        @param[in] theIsVerbose  print verbose messages
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Save(self) -> bool:
        """
        Save the user resource structure in the specified file.
        Creates the file if it does not exist.
        """

    @overload
    def Find(self, aResource: str) -> bool: ...

    @overload
    def Find(self, theResource: nanoocp.TCollection.TCollection_AsciiString, theValue: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """returns True if the Resource does exist."""

    def Integer(self, aResourceName: str) -> int:
        """
        Gets the value of an integer resource according to its
        instance and its type.
        """

    def Real(self, aResourceName: str) -> float:
        """
        Gets the value of a real resource according to its instance
        and its type.
        """

    def Value(self, aResourceName: str) -> str:
        """
        Gets the value of a CString resource according to its instance
        and its type.
        """

    @overload
    def SetResource(self, aResourceName: str, aValue: int) -> None:
        """
        Sets the new value of an integer resource.
        If the resource does not exist, it is created.
        """

    @overload
    def SetResource(self, aResourceName: str, aValue: float) -> None:
        """
        Sets the new value of a real resource.
        If the resource does not exist, it is created.
        """

    @overload
    def SetResource(self, aResourceName: str, aValue: str) -> None:
        """
        Sets the new value of an CString resource.
        If the resource does not exist, it is created.
        """

    @staticmethod
    def GetResourcePath(aPath: nanoocp.TCollection.TCollection_AsciiString, aName: str, isUserDefaults: bool) -> None:
        """
        Gets the resource file full path by its name.
        If corresponding environment variable is not set
        or file doesn't exist returns empty string.
        """

    def GetMap(self, theRefMap: bool = True) -> nanoocp.NCollection.NCollection_DataMap__TCollection_AsciiString__TCollection_AsciiString:
        """Returns internal Ref or User map with parameters"""

    def IsInitialized(self) -> bool:
        """Returns true if Resource have been found"""

class Resource_NoSuchResource(nanoocp.Standard.Standard_NoSuchObject):
    pass

class Resource_Unicode:
    """
    This class provides functions used to convert a non-ASCII C string
    given in ANSI, EUC, GB or SJIS format, to a
    Unicode string of extended characters, and vice versa.
    """

    def __init__(self) -> None: ...

    @staticmethod
    def ConvertSJISToUnicode(fromstr: str, tostr: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Converts non-ASCII CString <fromstr> in SJIS format
        to Unicode ExtendedString <tostr>.
        """

    @staticmethod
    def ConvertEUCToUnicode(fromstr: str, tostr: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Converts non-ASCII CString <fromstr> in EUC format
        to Unicode ExtendedString <tostr>.
        """

    @staticmethod
    def ConvertGBToUnicode(fromstr: str, tostr: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Converts non-ASCII CString <fromstr> in GB format
        to Unicode ExtendedString <tostr>.
        """

    @staticmethod
    def ConvertGBKToUnicode(fromstr: str, tostr: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        Converts non-ASCII CString <fromstr> in GBK format
        to Unicode ExtendedString <tostr>.
        """

    @staticmethod
    def ConvertBig5ToUnicode(fromstr: str, tostr: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        Converts non-ASCII CString <fromstr> in Big5 format
        to Unicode ExtendedString <tostr>.
        """

    @staticmethod
    def SetFormat(typecode: Resource_FormatType) -> None:
        """
        Defines the current conversion format as typecode.
        This conversion format will then be used by the
        functions ConvertFormatToUnicode and
        ConvertUnicodeToFormat to convert the strings.
        """

    @staticmethod
    def GetFormat() -> Resource_FormatType:
        """
        Returns the current conversion format (either
        ANSI, EUC, GB or SJIS).
        The current converting format must be defined in
        advance with the SetFormat function.
        """

    @staticmethod
    def ReadFormat() -> None:
        """
        Reads converting format from resource "FormatType"
        in Resource Manager "CharSet\"
        """

    @overload
    @staticmethod
    def ConvertFormatToUnicode(theFromStr: str, theToStr: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Converts the non-ASCII C string (as specified by GetFormat()) to the Unicode string of
        extended characters.
        """

    @overload
    @staticmethod
    def ConvertFormatToUnicode(theFormat: Resource_FormatType, theFromStr: str, theToStr: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Converts the non-ASCII C string in specified format to the Unicode string of extended
        characters.
        @param[in] theFormat   source encoding
        @param[in] theFromStr  text to convert
        @param[out] theToStr   destination string
        """
