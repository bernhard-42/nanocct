"""OCCT package Font (toolkit TKService)"""

import enum
from typing import overload

import nanoocp.BVH
import nanoocp.Graphic3d
import nanoocp.Image
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection


class Font_FontAspect(enum.IntEnum):
    """Specifies aspect of system font."""

    Font_FontAspect_UNDEFINED = -1

    Font_FontAspect_Regular = 0

    Font_FontAspect_Bold = 1

    Font_FontAspect_Italic = 2

    Font_FontAspect_BoldItalic = 3

    Font_FA_Undefined = -1

    Font_FA_Regular = 0

    Font_FA_Bold = 1

    Font_FA_Italic = 2

    Font_FA_BoldItalic = 3

Font_FontAspect_UNDEFINED: Font_FontAspect = Font_FontAspect.Font_FontAspect_UNDEFINED

Font_FontAspect_Regular: Font_FontAspect = Font_FontAspect.Font_FontAspect_Regular

Font_FontAspect_Bold: Font_FontAspect = Font_FontAspect.Font_FontAspect_Bold

Font_FontAspect_Italic: Font_FontAspect = Font_FontAspect.Font_FontAspect_Italic

Font_FontAspect_BoldItalic: Font_FontAspect = Font_FontAspect.Font_FontAspect_BoldItalic

Font_FA_Undefined: Font_FontAspect = Font_FontAspect.Font_FA_Undefined

Font_FA_Regular: Font_FontAspect = Font_FontAspect.Font_FA_Regular

Font_FA_Bold: Font_FontAspect = Font_FontAspect.Font_FA_Bold

Font_FA_Italic: Font_FontAspect = Font_FontAspect.Font_FA_Italic

Font_FA_BoldItalic: Font_FontAspect = Font_FontAspect.Font_FA_BoldItalic

Font_FontAspect_NB: int = 4

class Font_Hinting(enum.IntEnum):
    """Enumeration defining font hinting options."""

    Font_Hinting_Off = 0

    Font_Hinting_Normal = 1

    Font_Hinting_Light = 2

    Font_Hinting_ForceAutohint = 16

    Font_Hinting_NoAutohint = 32

Font_Hinting_Off: Font_Hinting = Font_Hinting.Font_Hinting_Off

Font_Hinting_Normal: Font_Hinting = Font_Hinting.Font_Hinting_Normal

Font_Hinting_Light: Font_Hinting = Font_Hinting.Font_Hinting_Light

Font_Hinting_ForceAutohint: Font_Hinting = Font_Hinting.Font_Hinting_ForceAutohint

Font_Hinting_NoAutohint: Font_Hinting = Font_Hinting.Font_Hinting_NoAutohint

class Font_StrictLevel(enum.IntEnum):
    """Enumeration defining font search restrictions."""

    Font_StrictLevel_Strict = 0

    Font_StrictLevel_Aliases = 1

    Font_StrictLevel_Any = 2

Font_StrictLevel_Strict: Font_StrictLevel = Font_StrictLevel.Font_StrictLevel_Strict

Font_StrictLevel_Aliases: Font_StrictLevel = Font_StrictLevel.Font_StrictLevel_Aliases

Font_StrictLevel_Any: Font_StrictLevel = Font_StrictLevel.Font_StrictLevel_Any

class Font_UnicodeSubset(enum.IntEnum):
    """Enumeration defining Unicode subsets."""

    Font_UnicodeSubset_Western = 0

    Font_UnicodeSubset_Korean = 1

    Font_UnicodeSubset_CJK = 2

    Font_UnicodeSubset_Arabic = 3

Font_UnicodeSubset_Western: Font_UnicodeSubset = Font_UnicodeSubset.Font_UnicodeSubset_Western

Font_UnicodeSubset_Korean: Font_UnicodeSubset = Font_UnicodeSubset.Font_UnicodeSubset_Korean

Font_UnicodeSubset_CJK: Font_UnicodeSubset = Font_UnicodeSubset.Font_UnicodeSubset_CJK

Font_UnicodeSubset_Arabic: Font_UnicodeSubset = Font_UnicodeSubset.Font_UnicodeSubset_Arabic

Font_UnicodeSubset_NB: int = 3

class Font_Rect:
    """Auxiliary POD structure - 2D rectangle definition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Font_Rect) -> None: ...

    @overload
    def TopLeft(self) -> nanoocp.BVH.BVH_Vec2f: ...

    @overload
    def TopLeft(self, theVec: nanoocp.BVH.BVH_Vec2f) -> nanoocp.BVH.BVH_Vec2f:
        """Top-left corner as vec2."""

    def TopRight(self, theVec: nanoocp.BVH.BVH_Vec2f) -> nanoocp.BVH.BVH_Vec2f:
        """Top-right corner as vec2."""

    def BottomLeft(self, theVec: nanoocp.BVH.BVH_Vec2f) -> nanoocp.BVH.BVH_Vec2f:
        """Bottom-left corner as vec2."""

    def BottomRight(self, theVec: nanoocp.BVH.BVH_Vec2f) -> nanoocp.BVH.BVH_Vec2f:
        """Bottom-right corner as vec2."""

    def Width(self) -> float:
        """Rectangle width."""

    def Height(self) -> float:
        """Rectangle height."""

    def DumpJson(self, arg1: int) -> object:
        """Dumps the content of me into the stream"""

    @property
    def Left(self) -> float:
        """left   position"""

    @Left.setter
    def Left(self, arg: float, /) -> None: ...

    @property
    def Right(self) -> float:
        """right  position"""

    @Right.setter
    def Right(self, arg: float, /) -> None: ...

    @property
    def Top(self) -> float:
        """top    position"""

    @Top.setter
    def Top(self, arg: float, /) -> None: ...

    @property
    def Bottom(self) -> float:
        """bottom position"""

    @Bottom.setter
    def Bottom(self, arg: float, /) -> None: ...

class Font_FTFontParams:
    """Font initialization parameters."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, thePointSize: int, theResolution: int) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: Font_FTFontParams) -> None: ...

    @property
    def PointSize(self) -> int:
        """face size in points (1/72 inch)"""

    @PointSize.setter
    def PointSize(self, arg: int, /) -> None: ...

    @property
    def Resolution(self) -> int:
        """resolution of the target device in dpi for FT_Set_Char_Size()"""

    @Resolution.setter
    def Resolution(self, arg: int, /) -> None: ...

    @property
    def FontHinting(self) -> Font_Hinting:
        """
        request hinting (exclude FT_LOAD_NO_HINTING flag), Font_Hinting_Off by default;
        """

    @FontHinting.setter
    def FontHinting(self, arg: Font_Hinting, /) -> None: ...

    @property
    def ToSynthesizeItalic(self) -> bool:
        """
        generate italic style (e.g. for font family having no italic style); FALSE by default
        """

    @ToSynthesizeItalic.setter
    def ToSynthesizeItalic(self, arg: bool, /) -> None: ...

    @property
    def IsSingleStrokeFont(self) -> bool:
        """single-stroke (one-line) font, FALSE by default"""

    @IsSingleStrokeFont.setter
    def IsSingleStrokeFont(self, arg: bool, /) -> None: ...

class Font_FTFont(nanoocp.Standard.Standard_Transient):
    """
    Wrapper over FreeType font.
    Notice that this class uses internal buffers for loaded glyphs
    and it is absolutely UNSAFE to load/read glyph from concurrent threads!
    """

    def __init__(self, theFTLib: Font_FTLibrary | None = None) -> None:
        """Create uninitialized instance."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def FindAndCreate(theFontName: nanoocp.TCollection.TCollection_AsciiString, theFontAspect: Font_FontAspect, theParams: Font_FTFontParams, theStrictLevel: Font_StrictLevel = Font_StrictLevel.Font_StrictLevel_Any) -> Font_FTFont:
        """
        Find the font Initialize the font.
        @param theFontName    the font name
        @param theFontAspect  the font style
        @param theParams      initialization parameters
        @param theStrictLevel search strict level for using aliases and fallback
        @return true on success
        """

    @staticmethod
    def IsCharFromCJK(theUChar: str) -> bool:
        """
        Return TRUE if specified character is within subset of modern CJK characters.
        """

    @staticmethod
    def IsCharFromHiragana(theUChar: str) -> bool:
        """
        Return TRUE if specified character is within subset of Hiragana (Japanese).
        """

    @staticmethod
    def IsCharFromKatakana(theUChar: str) -> bool:
        """
        Return TRUE if specified character is within subset of Katakana (Japanese).
        """

    @staticmethod
    def IsCharFromKorean(theUChar: str) -> bool:
        """
        Return TRUE if specified character is within subset of modern Korean characters (Hangul).
        """

    @staticmethod
    def IsCharFromArabic(theUChar: str) -> bool:
        """
        Return TRUE if specified character is within subset of Arabic characters.
        """

    @staticmethod
    def IsCharRightToLeft(theUChar: str) -> bool:
        """
        Return TRUE if specified character should be displayed in Right-to-Left order.
        """

    @staticmethod
    def CharSubset(theUChar: str) -> Font_UnicodeSubset:
        """Determine Unicode subset for specified character"""

    def IsValid(self) -> bool:
        """@return true if font is loaded"""

    def GlyphImage(self) -> nanoocp.Image.Image_PixMap:
        """@return image plane for currently rendered glyph"""

    @overload
    def Init(self, theFontPath: nanoocp.TCollection.TCollection_AsciiString, theParams: Font_FTFontParams, theFaceId: int = 0) -> bool:
        """
        Initialize the font from the given file path.
        @param theFontPath path to the font
        @param theParams   initialization parameters
        @param theFaceId   face id within the file (0 by default)
        @return true on success
        """

    @overload
    def Init(self, theData: nanoocp.NCollection.NCollection_Buffer | None, theFileName: nanoocp.TCollection.TCollection_AsciiString, theParams: Font_FTFontParams, theFaceId: int = 0) -> bool:
        """
        Initialize the font from the given file path or memory buffer.
        @param theData     memory to read from, should NOT be freed after initialization!
        when NULL, function will attempt to open theFileName file
        @param theFileName optional path to the font
        @param theParams   initialization parameters
        @param theFaceId   face id within the file (0 by default)
        @return true on success
        """

    @overload
    def Init(self, theFontPath: nanoocp.NCollection.NCollection_String, thePointSize: int, theResolution: int) -> bool:
        """
        Deprecated in OCCT: Deprecated method, Font_FTFontParams should be used for passing parameters

        Initialize the font.
        @param theFontPath   path to the font
        @param thePointSize  the face size in points (1/72 inch)
        @param theResolution the resolution of the target device in dpi
        @return true on success
        """

    @overload
    def Init(self, theFontName: nanoocp.NCollection.NCollection_String, theFontAspect: Font_FontAspect, thePointSize: int, theResolution: int) -> bool:
        """
        Deprecated in OCCT: Deprecated method, Font_FTFontParams should be used for passing parameters

        Initialize the font.
        @param theFontName   the font name
        @param theFontAspect the font style
        @param thePointSize  the face size in points (1/72 inch)
        @param theResolution the resolution of the target device in dpi
        @return true on success
        """

    def FindAndInit(self, theFontName: nanoocp.TCollection.TCollection_AsciiString, theFontAspect: Font_FontAspect, theParams: Font_FTFontParams, theStrictLevel: Font_StrictLevel = Font_StrictLevel.Font_StrictLevel_Any) -> bool:
        """
        Find (using Font_FontMgr) and initialize the font from the given name.
        @param theFontName    the font name
        @param theFontAspect  the font style
        @param theParams      initialization parameters
        @param theStrictLevel search strict level for using aliases and fallback
        @return true on success
        """

    def ToUseUnicodeSubsetFallback(self) -> bool:
        """
        Return flag to use fallback fonts in case if used font does not include symbols from specific
        Unicode subset; TRUE by default.
        @sa Font_FontMgr::ToUseUnicodeSubsetFallback()
        """

    def SetUseUnicodeSubsetFallback(self, theToFallback: bool) -> None:
        """
        Set if fallback fonts should be used in case if used font does not include symbols from
        specific Unicode subset.
        """

    def IsSingleStrokeFont(self) -> bool:
        """
        Return TRUE if this is single-stroke (one-line) font, FALSE by default.
        Such fonts define single-line glyphs instead of closed contours, so that they are rendered
        incorrectly by normal software.
        """

    def SetSingleStrokeFont(self, theIsSingleLine: bool) -> None:
        """Set if this font should be rendered as single-stroke (one-line)."""

    def ToSynthesizeItalic(self) -> bool:
        """Return TRUE if italic style should be synthesized; FALSE by default."""

    def Release(self) -> None:
        """Release currently loaded font."""

    def RenderGlyph(self, theChar: str) -> bool:
        """Render specified glyph into internal buffer (bitmap)."""

    def GlyphMaxSizeX(self, theToIncludeFallback: bool = False) -> int:
        """@return maximal glyph width in pixels (rendered to bitmap)."""

    def GlyphMaxSizeY(self, theToIncludeFallback: bool = False) -> int:
        """@return maximal glyph height in pixels (rendered to bitmap)."""

    def Ascender(self) -> float:
        """
        @return vertical distance from the horizontal baseline to the highest character coordinate.
        """

    def Descender(self) -> float:
        """
        @return vertical distance from the horizontal baseline to the lowest character coordinate.
        """

    def LineSpacing(self) -> float:
        """@return default line spacing (the baseline-to-baseline distance)."""

    def PointSize(self) -> int:
        """Configured point size"""

    def WidthScaling(self) -> float:
        """Return glyph scaling along X-axis."""

    def SetWidthScaling(self, theScaleFactor: float) -> None:
        """
        Setup glyph scaling along X-axis.
        By default glyphs are not scaled (scaling factor = 1.0)
        """

    def HasSymbol(self, theUChar: str) -> bool:
        """
        Return TRUE if font contains specified symbol (excluding fallback list).
        """

    @overload
    def AdvanceX(self, theUCharNext: str) -> float:
        """
        Compute horizontal advance to the next character with kerning applied when applicable.
        Assuming text rendered horizontally.
        @param theUCharNext the next character to compute advance from current one
        """

    @overload
    def AdvanceX(self, theUChar: str, theUCharNext: str) -> float:
        """
        Compute horizontal advance to the next character with kerning applied when applicable.
        Assuming text rendered horizontally.
        @param theUChar     the character to be loaded as current one
        @param theUCharNext the next character to compute advance from current one
        """

    @overload
    def AdvanceY(self, theUCharNext: str) -> float:
        """
        Compute vertical advance to the next character with kerning applied when applicable.
        Assuming text rendered vertically.
        @param theUCharNext the next character to compute advance from current one
        """

    @overload
    def AdvanceY(self, theUChar: str, theUCharNext: str) -> float:
        """
        Compute vertical advance to the next character with kerning applied when applicable.
        Assuming text rendered vertically.
        @param theUChar     the character to be loaded as current one
        @param theUCharNext the next character to compute advance from current one
        """

    def GlyphsNumber(self, theToIncludeFallback: bool = False) -> int:
        """
        Return glyphs number in this font.
        @param theToIncludeFallback if TRUE then the number will include fallback list
        """

    def GlyphRect(self, theRect: Font_Rect) -> None:
        """Retrieve glyph bitmap rectangle"""

    def BoundingBox(self, theString: nanoocp.NCollection.NCollection_String, theAlignX: nanoocp.Graphic3d.Graphic3d_HorizontalTextAlignment, theAlignY: nanoocp.Graphic3d.Graphic3d_VerticalTextAlignment) -> Font_Rect:
        """
        Computes bounding box of the given text using plain-text formatter (Font_TextFormatter).
        Note that bounding box takes into account the text alignment options.
        Its corners are relative to the text alignment anchor point, their coordinates can be
        negative.
        """

class Font_TextFormatter(nanoocp.Standard.Standard_Transient):
    """
    This class is intended to prepare formatted text by using:
    - font to string combination,
    - alignment,
    - wrapping.

    After text formatting, each symbol of formatted text is placed in some position.
    Further work with the formatter is using an iterator.
    The iterator gives an access to each symbol inside the initial row.
    Also it's possible to get only significant/writable symbols of the text.
    Formatter gives an access to geometrical position of a symbol by the symbol index in the
    text. Example of correspondence of some text symbol to an index in "row_1\\n\\nrow_2\\n":
    "row_1\\n"  - 0-5 indices;
    "\\n"       - 6 index;
    "\\n"       - 7 index;
    "row_2\\n"  - 8-13 indices.
    Pay attention that fonts should have the same LineSpacing value for correct formatting.
    Example of the formatter using:
    @code
    occ::handle<Font_TextFormatter> aFormatter = new Font_TextFormatter();
    aFormatter->Append(text_1, aFont1);
    aFormatter->Append(text_2, aFont2);
    // setting of additional properties such as wrapping or alignment
    aFormatter->Format();
    @endcode
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theOther: Font_TextFormatter) -> None: ...

    class IterationFilter(enum.IntEnum):
        """Iteration filter flags. Command symbols are skipped with any filter."""

        IterationFilter_None = 0

        IterationFilter_ExcludeInvisible = 2

    IterationFilter_None: Font_TextFormatter.IterationFilter = IterationFilter.IterationFilter_None

    IterationFilter_ExcludeInvisible: Font_TextFormatter.IterationFilter = IterationFilter.IterationFilter_ExcludeInvisible

    class Iterator:
        """
        Iterator through formatted symbols.
        It's possible to filter returned symbols to have only significant ones.
        """

        @overload
        def __init__(self, theFormatter: Font_TextFormatter, theFilter: Font_TextFormatter.IterationFilter = IterationFilter.IterationFilter_None) -> None:
            """Constructor with initialization."""

        @overload
        def __init__(self, theOther: Font_TextFormatter.Iterator) -> None: ...

        def More(self) -> bool:
            """Returns TRUE if iterator points to a valid item."""

        def HasNext(self) -> bool:
            """Returns TRUE if next item exists"""

        def Symbol(self) -> str:
            """Returns current symbol."""

        def SymbolNext(self) -> str:
            """Returns the next symbol if exists."""

        def SymbolPosition(self) -> int:
            """Returns current symbol position."""

        def SymbolPositionNext(self) -> int:
            """Returns the next symbol position."""

        def Next(self) -> None:
            """Moves to the next item."""

    def SetupAlignment(self, theAlignX: nanoocp.Graphic3d.Graphic3d_HorizontalTextAlignment, theAlignY: nanoocp.Graphic3d.Graphic3d_VerticalTextAlignment) -> None:
        """Setup alignment style."""

    def Reset(self) -> None:
        """Reset current progress."""

    def Append(self, theString: nanoocp.NCollection.NCollection_String, theFont: Font_FTFont) -> None:
        """Render specified text to inner buffer."""

    def Format(self) -> None:
        """
        Perform formatting on the buffered text.
        Should not be called more than once after initialization!
        """

    def TopLeft(self, theIndex: int) -> nanoocp.BVH.BVH_Vec2f:
        """Deprecated in OCCT: BottomLeft should be used instead"""

    def BottomLeft(self, theIndex: int) -> nanoocp.BVH.BVH_Vec2f:
        """Returns specific glyph rectangle."""

    def String(self) -> nanoocp.NCollection.NCollection_String:
        """Returns current rendering string."""

    def GlyphBoundingBox(self, theIndex: int, theBndBox: Font_Rect) -> bool:
        """
        Returns symbol bounding box
        @param bounding box.
        """

    def LineHeight(self, theIndex: int) -> float:
        """
        Returns the line height
        @param theIndex a line index, obtained by LineIndex()
        """

    def LineWidth(self, theIndex: int) -> float:
        """Returns width of a line"""

    def IsLFSymbol(self, theIndex: int) -> bool:
        """
        Returns true if the symbol by the index is '\\n'. The width of the symbol is zero.
        """

    def FirstPosition(self) -> float:
        """Returns position of the first symbol in a line using alignment"""

    def LinePositionIndex(self, theIndex: int) -> int:
        """Returns column index of the corner index in the current line"""

    def LineIndex(self, theIndex: int) -> int:
        """Returns row index of the corner index among text lines"""

    def TabSize(self) -> int:
        """Returns tab size."""

    def HorizontalTextAlignment(self) -> nanoocp.Graphic3d.Graphic3d_HorizontalTextAlignment:
        """Returns horizontal alignment style"""

    def VerticalTextAlignment(self) -> nanoocp.Graphic3d.Graphic3d_VerticalTextAlignment:
        """Returns vertical alignment style"""

    def SetWrapping(self, theWidth: float) -> None:
        """
        Sets text wrapping width, zero means that the text is not bounded by width
        """

    def HasWrapping(self) -> bool:
        """
        Returns text maximum width, zero means that the text is not bounded by width
        """

    def Wrapping(self) -> float:
        """
        Returns text maximum width, zero means that the text is not bounded by width
        """

    def WordWrapping(self) -> bool:
        """returns TRUE when trying not to break words when wrapping text"""

    def SetWordWrapping(self, theIsWordWrapping: bool) -> None:
        """returns TRUE when trying not to break words when wrapping text"""

    def ResultWidth(self) -> float:
        """@return width of formatted text."""

    def ResultHeight(self) -> float:
        """@return height of formatted text."""

    def MaximumSymbolWidth(self) -> float:
        """@return maximum width of the text symbol"""

    def BndBox(self, theBndBox: Font_Rect) -> None:
        """@param bounding box."""

    def Corners(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.BVH.BVH_Vec2f]:
        """
        Returns internal container of the top left corners of a formatted rectangles.
        """

    def NewLines(self) -> nanoocp.NCollection.NCollection_DynamicArray__float:
        """Returns container of each line position at LF in formatted text"""

    @staticmethod
    def IsCommandSymbol(theSymbol: str) -> bool:
        """Returns true if the symbol is CR, BEL, FF, NP, BS or VT"""

    @staticmethod
    def IsSeparatorSymbol(theSymbol: str) -> bool:
        """Returns true if the symbol separates words when wrapping is enabled"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Font_SystemFont(nanoocp.Standard.Standard_Transient):
    """
    This class stores information about the font, which is merely a file path and cached metadata
    about the font.
    """

    @overload
    def __init__(self, theFontName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Creates a new font object."""

    @overload
    def __init__(self, theOther: Font_SystemFont) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def FontKey(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns font family name (lower-cased)."""

    def FontName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns font family name."""

    def FontPath(self, theAspect: Font_FontAspect) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns font file path."""

    def FontFaceId(self, theAspect: Font_FontAspect) -> int:
        """Returns font file path."""

    def SetFontPath(self, theAspect: Font_FontAspect, thePath: nanoocp.TCollection.TCollection_AsciiString, theFaceId: int = 0) -> None:
        """Sets font file path for specific aspect."""

    def HasFontAspect(self, theAspect: Font_FontAspect) -> bool:
        """
        Returns TRUE if dedicated file for specified font aspect has been defined.
        """

    def FontPathAny(self, theAspect: Font_FontAspect) -> tuple[nanoocp.TCollection.TCollection_AsciiString, bool, int]:
        """Returns any defined font file path."""

    def IsEqual(self, theOtherFont: Font_SystemFont | None) -> bool:
        """Return true if the FontName, FontAspect and FontSize are the same."""

    def IsSingleStrokeFont(self) -> bool:
        """
        Return TRUE if this is single-stroke (one-line) font, FALSE by default.
        Such fonts define single-line glyphs instead of closed contours, so that they are rendered
        incorrectly by normal software.
        """

    def SetSingleStrokeFont(self, theIsSingleLine: bool) -> None:
        """Set if this font should be rendered as single-stroke (one-line)."""

    def ToString(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Format font description."""

    def __eq__(self, theFont: Font_SystemFont) -> bool: ...

class Font_FontMgr(nanoocp.Standard.Standard_Transient):
    """Collects and provides information about available fonts in system."""

    def __init__(self, theOther: Font_FontMgr) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def GetInstance() -> Font_FontMgr:
        """Return global instance of font manager."""

    @staticmethod
    def FontAspectToString(theAspect: Font_FontAspect) -> str:
        """Return font aspect as string."""

    def ToUseUnicodeSubsetFallback(self) -> bool:
        """
        Return flag to use fallback fonts in case if used font does not include symbols from specific
        Unicode subset; TRUE by default.
        """

    def SetToUseUnicodeSubsetFallback(self, theValue: bool) -> None:
        """
        Python addition: sets the value ToUseUnicodeSubsetFallback() returns by reference in C++.
        """

    def AvailableFonts(self, theList: nanoocp.NCollection.NCollection_List[nanoocp.Font.Font_SystemFont]) -> None:
        """Return the list of available fonts."""

    def GetAvailableFonts(self) -> nanoocp.NCollection.NCollection_List[nanoocp.Font.Font_SystemFont]:
        """Return the list of available fonts."""

    def GetAvailableFontsNames(self, theFontsNames: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_HAsciiString]) -> None:
        """Returns sequence of available fonts names"""

    @overload
    def GetFont(self, theFontName: nanoocp.TCollection.TCollection_HAsciiString | None, theFontAspect: Font_FontAspect, theFontSize: int) -> Font_SystemFont:
        """
        Returns font that match given parameters.
        If theFontName is empty string returned font can have any FontName.
        If theFontAspect is Font_FA_Undefined returned font can have any FontAspect.
        If theFontSize is "-1" returned font can have any FontSize.
        """

    @overload
    def GetFont(self, theFontName: nanoocp.TCollection.TCollection_AsciiString) -> Font_SystemFont:
        """
        Returns font that match given name or NULL if such font family is NOT registered.
        Note that unlike FindFont(), this method ignores font aliases and does not look for fall-back.
        """

    @overload
    def FindFont(self, theFontName: nanoocp.TCollection.TCollection_AsciiString, theStrictLevel: Font_StrictLevel, theFontAspect: Font_FontAspect, theDoFailMsg: bool = True) -> tuple[Font_SystemFont, Font_FontAspect]:
        """
        Tries to find font by given parameters.
        If the specified font is not found tries to use font names mapping.
        If the requested family name not found -> search for any font family with given aspect and
        height. If the font is still not found, returns any font available in the system. Returns NULL
        in case when the fonts are not found in the system.
        @param[in] theFontName           font family to find or alias name
        @param[in] theStrictLevel        search strict level for using aliases and fallback
        @param[in][out] theFontAspect    font aspect to find (considered only if family name is not
        found);
        can be modified if specified font alias refers to another
        style (compatibility with obsolete aliases)
        @param[in] theDoFailMsg          put error message on failure into default messenger
        """

    @overload
    def FindFont(self, theFontName: nanoocp.TCollection.TCollection_AsciiString, theFontAspect: Font_FontAspect) -> tuple[Font_SystemFont, Font_FontAspect]:
        """Tries to find font by given parameters."""

    def FindFallbackFont(self, theSubset: Font_UnicodeSubset, theFontAspect: Font_FontAspect) -> Font_SystemFont:
        """
        Tries to find fallback font for specified Unicode subset.
        Returns NULL in case when fallback font is not found in the system.
        @param[in] theSubset      Unicode subset
        @param[in] theFontAspect  font aspect to find
        """

    @overload
    def CheckFont(self, theFonts: nanoocp.NCollection.NCollection_Sequence[nanoocp.Font.Font_SystemFont], theFontPath: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Read font file and retrieve information from it (the list of font faces).
        """

    @overload
    def CheckFont(self, theFontPath: str) -> Font_SystemFont:
        """Read font file and retrieve information from it."""

    def RegisterFont(self, theFont: Font_SystemFont | None, theToOverride: bool) -> bool:
        """
        Register new font.
        If there is existing entity with the same name and properties but different path
        then font will be overridden or ignored depending on theToOverride flag.
        """

    def RegisterFonts(self, theFonts: nanoocp.NCollection.NCollection_Sequence[nanoocp.Font.Font_SystemFont], theToOverride: bool) -> bool:
        """Register new fonts."""

    def ToTraceAliases(self) -> bool:
        """
        Return flag for tracing font aliases usage via Message_Trace messages; TRUE by default.
        """

    def SetTraceAliases(self, theToTrace: bool) -> None:
        """
        Set flag for tracing font alias usage; useful to trace which fonts are actually used.
        Can be disabled to avoid redundant messages with Message_Trace level.
        """

    def ToPrintErrors(self) -> bool:
        """
        Return flag for printing error messages via Message_Fail messages; TRUE by default.
        """

    def SetPrintErrors(self, theToPrintErrors: bool) -> None:
        """
        Set flag for printing error messages.
        Can be disabled to avoid error messages with Message_Fail level.
        """

    def GetAllAliases(self, theAliases: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_HAsciiString]) -> None:
        """
        Return font names with defined aliases.
        @param[out] theAliases  alias names
        """

    def GetFontAliases(self, theFontNames: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_HAsciiString], theAliasName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Return aliases to specified font name.
        @param[out] theFontNames  font names associated with alias name
        @param[in] theAliasName   alias name
        """

    def AddFontAlias(self, theAliasName: nanoocp.TCollection.TCollection_AsciiString, theFontName: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Register font alias.

        Font alias allows using predefined short-cuts like Font_NOF_MONOSPACE or Font_NOF_SANS_SERIF,
        and defining several fallback fonts like Font_NOF_CJK ("cjk") or "courier" for fonts,
        which availability depends on system.

        By default, Font_FontMgr registers standard aliases, which could be extended or replaced by
        application basing on better knowledge of the system or basing on additional fonts packaged
        with application itself. Aliases are defined "in advance", so that they could point to
        non-existing fonts, and they are resolved dynamically on request - first existing font is
        returned in case of multiple aliases to the same name.

        @param[in] theAliasName  alias name or name of another font to be used as alias
        @param[in] theFontName   font to be used as substitution for alias
        @return FALSE if alias has been already registered
        """

    def RemoveFontAlias(self, theAliasName: nanoocp.TCollection.TCollection_AsciiString, theFontName: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Unregister font alias.
        @param[in] theAliasName  alias name or name of another font to be used as alias;
        all aliases will be removed in case of empty name
        @param[in] theFontName   font to be used as substitution for alias;
        all fonts will be removed in case of empty name
        @return TRUE if alias has been removed
        """

    def InitFontDataBase(self) -> None:
        """Collects available fonts paths."""

    def ClearFontDataBase(self) -> None:
        """Clear registry. Can be used for testing purposes."""

    @staticmethod
    def EmbedFallbackFont() -> nanoocp.NCollection.NCollection_Buffer:
        """
        Return DejaVu font as embed a single fallback font.
        It can be used in cases when there is no own font file.
        Note: result buffer is readonly and should not be changed,
        any data modification can lead to unpredictable consequences.
        """

class Font_FTLibrary(nanoocp.Standard.Standard_Transient):
    """Wrapper over FT_Library. Provides access to FreeType library."""

    def __init__(self) -> None:
        """Initialize new FT_Library instance."""

    def IsValid(self) -> bool:
        """
        This method should always return true.
        @return true if FT_Library instance is valid.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.Font
Font_NListOfSystemFont = nanoocp.NCollection.NCollection_List[nanoocp.Font.Font_SystemFont]
