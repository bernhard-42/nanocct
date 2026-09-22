"""OCCT package Image (toolkit TKService)"""

from collections.abc import Sequence
import enum
from typing import TextIO, overload

import nanoocp.NCollection
import nanoocp.Quantity
import nanoocp.Standard
import nanoocp.TCollection


class Image_Format(enum.IntEnum):
    """This enumeration defines packed image plane formats"""

    Image_Format_UNKNOWN = 0

    Image_Format_Gray = 1

    Image_Format_Alpha = 2

    Image_Format_RGB = 3

    Image_Format_BGR = 4

    Image_Format_RGB32 = 5

    Image_Format_BGR32 = 6

    Image_Format_RGBA = 7

    Image_Format_BGRA = 8

    Image_Format_GrayF = 9

    Image_Format_AlphaF = 10

    Image_Format_RGF = 11

    Image_Format_RGBF = 12

    Image_Format_BGRF = 13

    Image_Format_RGBAF = 14

    Image_Format_BGRAF = 15

    Image_Format_GrayF_half = 16

    Image_Format_RGF_half = 17

    Image_Format_RGBAF_half = 18

    Image_Format_Gray16 = 19

Image_Format_UNKNOWN: Image_Format = Image_Format.Image_Format_UNKNOWN

Image_Format_Gray: Image_Format = Image_Format.Image_Format_Gray

Image_Format_Alpha: Image_Format = Image_Format.Image_Format_Alpha

Image_Format_RGB: Image_Format = Image_Format.Image_Format_RGB

Image_Format_BGR: Image_Format = Image_Format.Image_Format_BGR

Image_Format_RGB32: Image_Format = Image_Format.Image_Format_RGB32

Image_Format_BGR32: Image_Format = Image_Format.Image_Format_BGR32

Image_Format_RGBA: Image_Format = Image_Format.Image_Format_RGBA

Image_Format_BGRA: Image_Format = Image_Format.Image_Format_BGRA

Image_Format_GrayF: Image_Format = Image_Format.Image_Format_GrayF

Image_Format_AlphaF: Image_Format = Image_Format.Image_Format_AlphaF

Image_Format_RGF: Image_Format = Image_Format.Image_Format_RGF

Image_Format_RGBF: Image_Format = Image_Format.Image_Format_RGBF

Image_Format_BGRF: Image_Format = Image_Format.Image_Format_BGRF

Image_Format_RGBAF: Image_Format = Image_Format.Image_Format_RGBAF

Image_Format_BGRAF: Image_Format = Image_Format.Image_Format_BGRAF

Image_Format_GrayF_half: Image_Format = Image_Format.Image_Format_GrayF_half

Image_Format_RGF_half: Image_Format = Image_Format.Image_Format_RGF_half

Image_Format_RGBAF_half: Image_Format = Image_Format.Image_Format_RGBAF_half

Image_Format_Gray16: Image_Format = Image_Format.Image_Format_Gray16

Image_Format_NB: int = 20

class Image_CompressedFormat(enum.IntEnum):
    """
    List of compressed pixel formats natively supported by various graphics hardware (e.g. for
    efficient decoding on-the-fly). It is defined as extension of Image_Format.
    """

    Image_CompressedFormat_UNKNOWN = 0

    Image_CompressedFormat_RGB_S3TC_DXT1 = 20

    Image_CompressedFormat_RGBA_S3TC_DXT1 = 21

    Image_CompressedFormat_RGBA_S3TC_DXT3 = 22

    Image_CompressedFormat_RGBA_S3TC_DXT5 = 23

Image_CompressedFormat_UNKNOWN: Image_CompressedFormat = ...

Image_CompressedFormat_RGB_S3TC_DXT1: Image_CompressedFormat = ...

Image_CompressedFormat_RGBA_S3TC_DXT1: Image_CompressedFormat = ...

Image_CompressedFormat_RGBA_S3TC_DXT3: Image_CompressedFormat = ...

Image_CompressedFormat_RGBA_S3TC_DXT5: Image_CompressedFormat = ...

Image_CompressedFormat_NB: int = 24

class Image_ColorRGB:
    """POD structure for packed RGB color value (3 bytes)"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Image_ColorRGB) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    def r(self) -> int:
        """Alias to 1st component (red intensity)."""

    def Setr(self, theValue: int) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def g(self) -> int:
        """Alias to 2nd component (green intensity)."""

    def Setg(self, theValue: int) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def b(self) -> int:
        """Alias to 3rd component (blue intensity)."""

    def Setb(self, theValue: int) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    @property
    def v(self) -> list[int]: ...

    @v.setter
    def v(self, arg: Sequence[int], /) -> None: ...

class Image_ColorRGB32:
    """
    POD structure for packed RGB color value (4 bytes with extra byte for alignment)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Image_ColorRGB32) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    def r(self) -> int:
        """Alias to 1st component (red intensity)."""

    def Setr(self, theValue: int) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def g(self) -> int:
        """Alias to 2nd component (green intensity)."""

    def Setg(self, theValue: int) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def b(self) -> int:
        """Alias to 3rd component (blue intensity)."""

    def Setb(self, theValue: int) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    @property
    def v(self) -> list[int]: ...

    @v.setter
    def v(self, arg: Sequence[int], /) -> None: ...

class Image_ColorRGBA:
    """POD structure for packed RGBA color value (4 bytes)"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Image_ColorRGBA) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    def r(self) -> int:
        """Alias to 1st component (red intensity)."""

    def Setr(self, theValue: int) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def g(self) -> int:
        """Alias to 2nd component (green intensity)."""

    def Setg(self, theValue: int) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def b(self) -> int:
        """Alias to 3rd component (blue intensity)."""

    def Setb(self, theValue: int) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    def a(self) -> int:
        """Alias to 4th component (alpha value)."""

    def Seta(self, theValue: int) -> None:
        """Python addition: sets the value a() returns by reference in C++."""

    @property
    def v(self) -> list[int]: ...

    @v.setter
    def v(self, arg: Sequence[int], /) -> None: ...

class Image_ColorBGR:
    """POD structure for packed BGR color value (3 bytes)"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Image_ColorBGR) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    def r(self) -> int:
        """Alias to 3rd component (red intensity)."""

    def Setr(self, theValue: int) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def g(self) -> int:
        """Alias to 2nd component (green intensity)."""

    def Setg(self, theValue: int) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def b(self) -> int:
        """Alias to 1st component (blue intensity)."""

    def Setb(self, theValue: int) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    @property
    def v(self) -> list[int]: ...

    @v.setter
    def v(self, arg: Sequence[int], /) -> None: ...

class Image_ColorBGR32:
    """
    POD structure for packed BGR color value (4 bytes with extra byte for alignment)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Image_ColorBGR32) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    def r(self) -> int:
        """Alias to 3rd component (red intensity)."""

    def Setr(self, theValue: int) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def g(self) -> int:
        """Alias to 2nd component (green intensity)."""

    def Setg(self, theValue: int) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def b(self) -> int:
        """Alias to 1st component (blue intensity)."""

    def Setb(self, theValue: int) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    @property
    def v(self) -> list[int]: ...

    @v.setter
    def v(self, arg: Sequence[int], /) -> None: ...

class Image_ColorBGRA:
    """POD structure for packed BGRA color value (4 bytes)"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Image_ColorBGRA) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    def r(self) -> int:
        """Alias to 3rd component (red intensity)."""

    def Setr(self, theValue: int) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def g(self) -> int:
        """Alias to 2nd component (green intensity)."""

    def Setg(self, theValue: int) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def b(self) -> int:
        """Alias to 1st component (blue intensity)."""

    def Setb(self, theValue: int) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    def a(self) -> int:
        """Alias to 4th component (alpha value)."""

    def Seta(self, theValue: int) -> None:
        """Python addition: sets the value a() returns by reference in C++."""

    @property
    def v(self) -> list[int]: ...

    @v.setter
    def v(self, arg: Sequence[int], /) -> None: ...

class Image_ColorRGF:
    """POD structure for packed float RG color value (2 floats)"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Image_ColorRGF) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    def r(self) -> float:
        """Alias to 1st component (red intensity)."""

    def Setr(self, theValue: float) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def g(self) -> float:
        """Alias to 2nd component (green intensity)."""

    def Setg(self, theValue: float) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    @property
    def v(self) -> list[float]: ...

    @v.setter
    def v(self, arg: Sequence[float], /) -> None: ...

class Image_ColorRGBF:
    """POD structure for packed float RGB color value (3 floats)"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Image_ColorRGBF) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    def r(self) -> float:
        """Alias to 1st component (red intensity)."""

    def Setr(self, theValue: float) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def g(self) -> float:
        """Alias to 2nd component (green intensity)."""

    def Setg(self, theValue: float) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def b(self) -> float:
        """Alias to 3rd component (blue intensity)."""

    def Setb(self, theValue: float) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    @property
    def v(self) -> list[float]: ...

    @v.setter
    def v(self, arg: Sequence[float], /) -> None: ...

class Image_ColorBGRF:
    """POD structure for packed BGR float color value (3 floats)"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Image_ColorBGRF) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    def r(self) -> float:
        """Alias to 3rd component (red intensity)."""

    def Setr(self, theValue: float) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def g(self) -> float:
        """Alias to 2nd component (green intensity)."""

    def Setg(self, theValue: float) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def b(self) -> float:
        """Alias to 1st component (blue intensity)."""

    def Setb(self, theValue: float) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    @property
    def v(self) -> list[float]: ...

    @v.setter
    def v(self, arg: Sequence[float], /) -> None: ...

class Image_ColorRGBAF:
    """POD structure for packed RGBA color value (4 floats)"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Image_ColorRGBAF) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    def r(self) -> float:
        """Alias to 1st component (red intensity)."""

    def Setr(self, theValue: float) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def g(self) -> float:
        """Alias to 2nd component (green intensity)."""

    def Setg(self, theValue: float) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def b(self) -> float:
        """Alias to 3rd component (blue intensity)."""

    def Setb(self, theValue: float) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    def a(self) -> float:
        """Alias to 4th component (alpha value)."""

    def Seta(self, theValue: float) -> None:
        """Python addition: sets the value a() returns by reference in C++."""

    @property
    def v(self) -> list[float]: ...

    @v.setter
    def v(self, arg: Sequence[float], /) -> None: ...

class Image_ColorBGRAF:
    """POD structure for packed float BGRA color value (4 floats)"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Image_ColorBGRAF) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    def r(self) -> float:
        """Alias to 3rd component (red intensity)."""

    def Setr(self, theValue: float) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def g(self) -> float:
        """Alias to 2nd component (green intensity)."""

    def Setg(self, theValue: float) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def b(self) -> float:
        """Alias to 1st component (blue intensity)."""

    def Setb(self, theValue: float) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    def a(self) -> float:
        """Alias to 4th component (alpha value)."""

    def Seta(self, theValue: float) -> None:
        """Python addition: sets the value a() returns by reference in C++."""

    @property
    def v(self) -> list[float]: ...

    @v.setter
    def v(self, arg: Sequence[float], /) -> None: ...

class Image_PixMapData(nanoocp.NCollection.NCollection_Buffer):
    """Structure to manage image buffer."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Image_PixMapData) -> None: ...

    def ZeroData(self) -> None:
        """Reset all values to zeros."""

    def MaxRowAligmentBytes(self) -> int:
        """
        Compute the maximal row alignment for current row size.
        @return maximal row alignment in bytes (up to 16 bytes).
        """

    def SetTopDown(self, theIsTopDown: bool) -> None:
        """
        Setup scanlines order in memory - top-down or bottom-up.
        Drawers should explicitly specify this value if current state IsTopDown() was ignored!
        @param theIsTopDown top-down flag
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @property
    def SizeBPP(self) -> int:
        """bytes per pixel"""

    @SizeBPP.setter
    def SizeBPP(self, arg: int, /) -> None: ...

    @property
    def SizeX(self) -> int:
        """width  in pixels"""

    @SizeX.setter
    def SizeX(self, arg: int, /) -> None: ...

    @property
    def SizeY(self) -> int:
        """height in pixels"""

    @SizeY.setter
    def SizeY(self, arg: int, /) -> None: ...

    @property
    def SizeZ(self) -> int:
        """depth  in pixels"""

    @SizeZ.setter
    def SizeZ(self, arg: int, /) -> None: ...

    @property
    def SizeRowBytes(self) -> int:
        """number of bytes per line (in most cases equal to 3 * sizeX)"""

    @SizeRowBytes.setter
    def SizeRowBytes(self, arg: int, /) -> None: ...

    @property
    def SizeSliceBytes(self) -> int:
        """number of bytes per 2D slice"""

    @SizeSliceBytes.setter
    def SizeSliceBytes(self, arg: int, /) -> None: ...

    @property
    def TopToDown(self) -> int:
        """image scanlines direction in memory from Top to the Down"""

    @TopToDown.setter
    def TopToDown(self, arg: int, /) -> None: ...

class Image_PixMap(nanoocp.Standard.Standard_Transient):
    """Class represents packed image plane."""

    def __init__(self) -> None:
        """Empty constructor. Initialize the NULL image plane."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def IsBigEndianHost() -> bool:
        """Determine Big-Endian at runtime"""

    @staticmethod
    def SizePixelBytes_s(thePixelFormat: Image_Format) -> int:
        """
        Return bytes reserved for one pixel (may include extra bytes for alignment).
        """

    @staticmethod
    def SwapRgbaBgra(theImage: Image_PixMap) -> bool:
        """
        Auxiliary method for swapping bytes between RGB and BGR formats.
        This method modifies the image data but does not change pixel format!
        Method will fail if pixel format is not one of the following:
        - Image_Format_RGB32 / Image_Format_BGR32
        - Image_Format_RGBA  / Image_Format_BGRA
        - Image_Format_RGB   / Image_Format_BGR
        - Image_Format_RGBF  / Image_Format_BGRF
        - Image_Format_RGBAF / Image_Format_BGRAF
        """

    @staticmethod
    def ToBlackWhite(theImage: Image_PixMap) -> None:
        """Convert image to Black/White."""

    @staticmethod
    def FlipY(theImage: Image_PixMap) -> bool:
        """Reverse line order as it draws it from bottom to top."""

    @staticmethod
    def DefaultAllocator() -> nanoocp.NCollection.NCollection_BaseAllocator:
        """Return default image data allocator."""

    @overload
    @staticmethod
    def ImageFormatToString(theFormat: Image_Format) -> str:
        """Return string representation of pixel format."""

    @overload
    @staticmethod
    def ImageFormatToString(theFormat: Image_CompressedFormat) -> str:
        """Return string representation of compressed pixel format."""

    def Format(self) -> Image_Format:
        """Return pixel format."""

    def SetFormat(self, thePixelFormat: Image_Format) -> None:
        """
        Override pixel format specified by InitXXX() methods.
        Will throw exception if pixel size of new format is not equal to currently initialized format.
        Intended to switch formats indicating different interpretation of the same data
        (e.g. ImgGray and ImgAlpha).
        """

    def Width(self) -> int:
        """Return image width in pixels."""

    def Height(self) -> int:
        """Return image height in pixels."""

    def Depth(self) -> int:
        """Return image depth in pixels."""

    def SizeX(self) -> int:
        """Return image width in pixels."""

    def SizeY(self) -> int:
        """Return image height in pixels."""

    def SizeZ(self) -> int:
        """Return image depth in pixels."""

    def SizeXYZ(self) -> NCollection_Vec3__unsigned_long:
        """Return image width x height x depth in pixels."""

    def Ratio(self) -> float:
        """Return width / height."""

    def IsEmpty(self) -> bool:
        """Return true if data is NULL."""

    def PixelColor(self, theX: int, theY: int, theToLinearize: bool = False) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """
        Returns the pixel color. This function is relatively slow.
        Beware that this method takes coordinates in opposite order in contrast to ::Value() and
        ::ChangeValue().
        @param[in] theX column index from left, starting from 0
        @param[in] theY row    index from top,  starting from 0
        @param[in] theToLinearize when TRUE, the color stored in non-linear color space (e.g.
        Image_Format_RGB) will be linearized
        @return the pixel color
        """

    @overload
    def SetPixelColor(self, theX: int, theY: int, theColor: nanoocp.Quantity.Quantity_Color, theToDeLinearize: bool = False) -> None: ...

    @overload
    def SetPixelColor(self, theX: int, theY: int, theColor: nanoocp.Quantity.Quantity_ColorRGBA, theToDeLinearize: bool = False) -> None:
        """
        Sets the pixel color. This function is relatively slow.
        Beware that this method takes coordinates in opposite order in contrast to ::Value() and
        ::ChangeValue().
        @param[in] theX column index from left
        @param[in] theY row    index from top
        @param[in] theColor color to store
        @param[in] theToDeLinearize when TRUE, the gamma correction will be applied for storing in
        non-linear color space (e.g. Image_Format_RGB)
        """

    def InitTrash(self, thePixelFormat: Image_Format, theSizeX: int, theSizeY: int, theSizeRowBytes: int = 0) -> bool:
        """
        Initialize image plane with required dimensions.
        Memory will be left uninitialized (performance trick).
        """

    def InitCopy(self, theCopy: Image_PixMap) -> bool:
        """
        Initialize by copying data.
        If you want to copy alien data you should create wrapper using InitWrapper() before.
        """

    def InitZero(self, thePixelFormat: Image_Format, theSizeX: int, theSizeY: int, theSizeRowBytes: int = 0, theValue: int = 0) -> bool:
        """
        Initialize image plane with required dimensions.
        Buffer will be zeroed (black color for most formats).
        """

    def Clear(self) -> None:
        """Method correctly deallocate internal buffer."""

    def InitTrash3D(self, thePixelFormat: Image_Format, theSizeXYZ: NCollection_Vec3__unsigned_long, theSizeRowBytes: int = 0) -> bool:
        """
        Initialize 2D/3D image with required dimensions.
        Memory will be left uninitialized (performance trick).
        """

    def InitZero3D(self, thePixelFormat: Image_Format, theSizeXYZ: NCollection_Vec3__unsigned_long, theSizeRowBytes: int = 0, theValue: int = 0) -> bool:
        """
        Initialize 2D/3D image with required dimensions.
        Buffer will be zeroed (black color for most formats).
        """

    def IsTopDown(self) -> bool:
        """
        @name low-level API for batch-processing (pixels reading / comparison / modification)
        Returns TRUE if image data is stored from Top to the Down.
        By default Bottom Up order is used instead
        (topmost scanlines starts from the bottom in memory).
        which is most image frameworks naturally support.

        Notice that access methods within this class automatically
        convert input row-index to apply this flag!
        You should use this flag only if interconnect with alien APIs and buffers.
        @return true if image data is top-down
        """

    def SetTopDown(self, theIsTopDown: bool) -> None:
        """
        Setup scanlines order in memory - top-down or bottom-up.
        Drawers should explicitly specify this value if current state IsTopDown() was ignored!
        @param theIsTopDown top-down flag
        """

    def TopDownInc(self) -> int:
        """
        Returns +1 if scanlines ordered in Top->Down order in memory and -1 otherwise.
        @return scanline increment for Top->Down iteration
        """

    def SizePixelBytes(self) -> int:
        """
        Return bytes reserved for one pixel (may include extra bytes for alignment).
        """

    def SizeRowBytes(self) -> int:
        """
        Return bytes reserved per row.
        Could be larger than needed to store packed row (extra bytes for alignment etc.).
        """

    def RowExtraBytes(self) -> int:
        """Return the extra bytes in the row."""

    def MaxRowAligmentBytes(self) -> int:
        """
        Compute the maximal row alignment for current row size.
        @return maximal row alignment in bytes (up to 16 bytes).
        """

    def SizeSliceBytes(self) -> int:
        """Return number of bytes per 2D slice."""

    def SizeBytes(self) -> int:
        """Return buffer size"""

    @staticmethod
    def ConvertFromHalfFloat(theHalf: int) -> float:
        """Convert 16-bit half-float value into 32-bit float (simple conversion)."""

    @staticmethod
    def ConvertToHalfFloat(theFloat: float) -> int:
        """
        Convert 32-bit float value into IEEE-754 16-bit floating-point format without infinity:
        1-5-10, exp-15, +-131008.0, +-6.1035156E-5, +-5.9604645E-8, 3.311 digits.
        """

class Image_AlienPixMap(Image_PixMap):
    """
    Image class that support file reading/writing operations using auxiliary image library.
    Supported image formats:
    - *.bmp - bitmap image, lossless format without compression.
    - *.ppm - PPM (Portable Pixmap Format), lossless format without compression.
    - *.png - PNG (Portable Network Graphics) lossless format with compression.
    - *.jpg, *.jpe, *.jpeg - JPEG/JIFF (Joint Photographic Experts Group) lossy format (compressed
    with quality losses). YUV color space used (automatically converted from/to RGB).
    - *.tif, *.tiff - TIFF (Tagged Image File Format).
    - *.tga - TGA (Truevision Targa Graphic), lossless format.
    - *.gif - GIF (Graphical Interchange Format), lossy format. Color stored using palette (up to
    256 distinct colors).
    - *.exr - OpenEXR high dynamic-range format (supports float pixel formats).
    """

    def __init__(self) -> None:
        """Empty constructor."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def IsTopDownDefault() -> bool:
        """Return default rows order used by underlying image library."""

    @overload
    def Load(self, theFileName: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Read image data from file."""

    @overload
    def Load(self, theStream: TextIO, theFileName: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Read image data from stream."""

    def Save(self, theFileName: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Write image data to file.
        @param[in] theFileName file name to save
        """

    def Save__str(self, theExtension: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, str]:
        """
        Save__str: the C++ overload Save(std::ostream &, const TCollection_AsciiString &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Write image data to stream.
        @param[out] theStream   stream where to write
        @param[in] theExtension image format
        """

    def InitTrash(self, thePixelFormat: Image_Format, theSizeX: int, theSizeY: int, theSizeRowBytes: int = 0) -> bool:
        """
        Initialize image plane with required dimensions.
        @param[in] thePixelFormat  if specified pixel format doesn't supported by image library
        than nearest supported will be used instead!
        @param[in] theSizeRowBytes may be ignored by this class and required alignment will be used
        instead!
        """

    def InitCopy(self, theCopy: Image_PixMap) -> bool:
        """Initialize by copying data."""

    def Clear(self) -> None:
        """Method correctly deallocate internal buffer."""

    def AdjustGamma(self, theGammaCorr: float) -> bool:
        """
        Performs gamma correction on image.
        @param[in] theGamma - gamma value to use; a value of 1.0 leaves the image alone
        """

class Image_CompressedPixMap(nanoocp.Standard.Standard_Transient):
    """
    Compressed pixmap data definition.
    It is defined independently from Image_PixMap, which defines only uncompressed formats.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Image_CompressedPixMap) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def BaseFormat(self) -> Image_Format:
        """Return base (uncompressed) pixel format."""

    def SetBaseFormat(self, theFormat: Image_Format) -> None:
        """Set base (uncompressed) pixel format."""

    def CompressedFormat(self) -> Image_CompressedFormat:
        """Return compressed format."""

    def SetCompressedFormat(self, theFormat: Image_CompressedFormat) -> None:
        """Set compressed format."""

    def FaceData(self) -> nanoocp.NCollection.NCollection_Buffer:
        """Return raw (compressed) data."""

    def SetFaceData(self, theBuffer: nanoocp.NCollection.NCollection_Buffer | None) -> None:
        """Set raw (compressed) data."""

    def MipMaps(self) -> nanoocp.NCollection.NCollection_Array1[int]:
        """Return Array of mipmap sizes, including base level."""

    def ChangeMipMaps(self) -> nanoocp.NCollection.NCollection_Array1[int]:
        """Return Array of mipmap sizes, including base level."""

    def IsCompleteMipMapSet(self) -> bool:
        """Return TRUE if complete mip map level set (up to 1x1 resolution)."""

    def SetCompleteMipMapSet(self, theIsComplete: bool) -> None:
        """Set if complete mip map level set (up to 1x1 resolution)."""

    def FaceBytes(self) -> int:
        """Return surface length in bytes."""

    def SetFaceBytes(self, theSize: int) -> None:
        """Set surface length in bytes."""

    def SizeX(self) -> int:
        """Return surface width."""

    def SizeY(self) -> int:
        """Return surface height."""

    def SetSize(self, theSizeX: int, theSizeY: int) -> None:
        """Set surface width x height."""

    def IsTopDown(self) -> bool:
        """Return TRUE if image layout is top-down (always true)."""

    def NbFaces(self) -> int:
        """Return number of faces in the file; should be 6 for cubemap."""

    def SetNbFaces(self, theSize: int) -> None:
        """Set number of faces in the file."""

class Image_DDSParser:
    """Auxiliary tool for parsing DDS file structure (without decoding)."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Image_DDSParser) -> None: ...

    @overload
    @staticmethod
    def Load(theSupported: Image_SupportedFormats | None, theFile: nanoocp.TCollection.TCollection_AsciiString, theFaceIndex: int, theFileOffset: int = 0) -> Image_CompressedPixMap:
        """
        Load the face from DDS file.
        @param[in] theSupported  list of supported image formats
        @param[in] theFile       file path
        @param[in] theFaceIndex  face index, within [0, Image_CompressedPixMap::NbFaces()) range;
        use -1 to skip reading the face data
        @param[in] theFileOffset  offset to the DDS data
        @return loaded face or NULL if file cannot be read or not valid DDS file
        """

    @overload
    @staticmethod
    def Load(theSupported: Image_SupportedFormats | None, theBuffer: nanoocp.NCollection.NCollection_Buffer | None, theFaceIndex: int) -> Image_CompressedPixMap:
        """
        Load the face from DDS file.
        @param[in] theSupported  list of supported image formats
        @param[in] theBuffer     pre-loaded file data, should be at least of 128 bytes long defining
        DDS header.
        @param[in] theFaceIndex  face index, within [0, Image_CompressedPixMap::NbFaces()) range;
        use -1 to skip reading the face data
        @return loaded face or NULL if file cannot be read or not valid DDS file
        """

class Image_Diff(nanoocp.Standard.Standard_Transient):
    """
    This class compares two images pixel-by-pixel.
    It uses the following methods to ignore the difference between images:
    - Black/White comparison. It makes the images 2-colored before the comparison.
    - Equality with tolerance. Colors of two pixels are considered the same if the
    difference of their color is less than a tolerance.
    - Border filter. The algorithm ignores alone independent pixels,
    which are different on both images, ignores the "border effect" -
    the difference caused by triangles located at angle about 0 or 90 degrees to the user.

    Border filter ignores a difference in implementation of
    anti-aliasing and other effects on boundary of a shape.
    The triangles of a boundary zone are usually located so that their normals point aside the user
    (about 90 degree between the normal and the direction to the user's eye).
    Deflection of the light for such a triangle depends on implementation of the video driver.
    In order to skip this difference the following algorithm is used:
    a) "Different" pixels are grouped and checked on "one-pixel width line".
    indeed, the pixels may represent not a line, but any curve.
    But the width of this curve should be not more than a pixel.
    This group of pixels become a candidate to be ignored because of boundary effect.
    b) The group of pixels is checked on belonging to a "shape".
    Neighbour pixels are checked from the reference image.
    This test confirms a fact that the group of pixels belongs to a shape and
    represent a boundary of the shape.
    In this case the whole group of pixels is ignored (considered as same).
    Otherwise, the group of pixels may represent a geometrical curve in the viewer 3D
    and should be considered as "different".

    References:
    1. http://pdiff.sourceforge.net/ypg01.pdf
    2. http://pdiff.sourceforge.net/metric.html
    3. http://www.cs.ucf.edu/~sumant/publications/sig99.pdf
    4. http://www.worldscientific.com/worldscibooks/10.1142/2641#t=toc (there is a list of
    articles and books in PDF format)
    """

    @overload
    def __init__(self) -> None:
        """An empty constructor. Init() should be called for initialization."""

    @overload
    def __init__(self, theOther: Image_Diff) -> None: ...

    @overload
    def Init(self, theImageRef: Image_PixMap | None, theImageNew: Image_PixMap | None, theToBlackWhite: bool = False) -> bool:
        """
        Initialize algorithm by two images.
        @return false if images has different or unsupported pixel format.
        """

    @overload
    def Init(self, theImgPathRef: nanoocp.TCollection.TCollection_AsciiString, theImgPathNew: nanoocp.TCollection.TCollection_AsciiString, theToBlackWhite: bool = False) -> bool:
        """
        Initialize algorithm by two images (will be loaded from files).
        @return false if images couldn't be opened or their format is unsupported.
        """

    def SetColorTolerance(self, theTolerance: float) -> None:
        """
        Color tolerance for equality check. Should be within range 0..1:
        Corresponds to a difference between white and black colors (maximum difference).
        By default, the tolerance is equal to 0 thus equality check will return false for any
        different colors.
        """

    def ColorTolerance(self) -> float:
        """Color tolerance for equality check."""

    def SetBorderFilterOn(self, theToIgnore: bool) -> None:
        """
        Sets taking into account (ignoring) a "border effect" on comparison of images.
        The border effect is caused by a border of shaded shapes in the viewer 3d.
        Triangles of this area are located at about 0 or 90 degrees to the user.
        Therefore, they deflect light differently according to implementation of a video card driver.
        This flag allows to detect such a "border" area and skip it from comparison of images.
        Filter turned OFF by default.
        """

    def IsBorderFilterOn(self) -> bool:
        """
        Returns a flag of taking into account (ignoring) a border effect in comparison of images.
        """

    def Compare(self) -> int:
        """
        Compares two images. It returns a number of different pixels (or groups of pixels).
        It returns -1 if algorithm not initialized before.
        """

    @overload
    def SaveDiffImage(self, theDiffImage: Image_PixMap) -> bool: ...

    @overload
    def SaveDiffImage(self, theDiffPath: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Saves a difference between two images as white pixels on black background.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Image_SupportedFormats(nanoocp.Standard.Standard_Transient):
    """Structure holding information about supported texture formats."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Image_SupportedFormats) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def IsSupported(self, theFormat: Image_Format) -> bool:
        """Return TRUE if image format is supported."""

    @overload
    def IsSupported(self, theFormat: Image_CompressedFormat) -> bool:
        """Return TRUE if compressed image format is supported."""

    @overload
    def Add(self, theFormat: Image_Format) -> None:
        """Set if image format is supported or not."""

    @overload
    def Add(self, theFormat: Image_CompressedFormat) -> None:
        """Set if compressed image format is supported or not."""

    def HasCompressed(self) -> bool:
        """Return TRUE if there are compressed image formats supported."""

    def Clear(self) -> None:
        """Reset flags."""

class Image_Texture(nanoocp.Standard.Standard_Transient):
    """
    Texture image definition.
    The image can be stored as path to image file, as file path with the given offset and as a data
    buffer of encoded image.
    """

    @overload
    def __init__(self, theFileName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Constructor pointing to file location."""

    @overload
    def __init__(self, theBuffer: nanoocp.NCollection.NCollection_Buffer | None, theId: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Constructor pointing to buffer."""

    @overload
    def __init__(self, theFileName: nanoocp.TCollection.TCollection_AsciiString, theOffset: int, theLength: int) -> None:
        """Constructor pointing to file part."""

    @overload
    def __init__(self, theOther: Image_Texture) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def TextureId(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return generated texture id."""

    def FilePath(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return image file path."""

    def FileOffset(self) -> int:
        """Return offset within file."""

    def FileLength(self) -> int:
        """Return length of image data within the file after offset."""

    def DataBuffer(self) -> nanoocp.NCollection.NCollection_Buffer:
        """Return buffer holding encoded image content."""

    def MimeType(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return mime-type of image file based on ProbeImageFileFormat()."""

    def ProbeImageFileFormat(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return image file format."""

    def ReadCompressedImage(self, theSupported: Image_SupportedFormats | None) -> Image_CompressedPixMap:
        """
        Image reader without decoding data for formats supported natively by GPUs.
        """

    def ReadImage(self, theSupported: Image_SupportedFormats | None) -> Image_PixMap:
        """Image reader."""

    def WriteImage(self, theFile: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Write image to specified file without decoding data."""

    def WriteImage__str(self, theFile: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, str]:
        """
        WriteImage__str: the C++ overload WriteImage(std::ostream &, const TCollection_AsciiString &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Write image to specified stream without decoding data.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """
        @name hasher interface
        Dumps the content of me into the stream
        """

class Image_VideoParams:
    """
    Auxiliary structure defining video parameters.
    Please refer to FFmpeg documentation for defining text values.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Image_VideoParams) -> None: ...

    @overload
    def SetFramerate(self, theNumerator: int, theDenominator: int) -> None:
        """Setup playback FPS."""

    @overload
    def SetFramerate(self, theValue: int) -> None:
        """
        Setup playback FPS.
        For fixed-fps content, timebase should be 1/framerate and timestamp increments should be
        identical to 1.
        """

    @property
    def Format(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        [optional]  video format (container), if empty - will be determined from the file name
        """

    @Format.setter
    def Format(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def VideoCodec(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        [optional]  codec identifier, if empty - default codec from file format will be used
        """

    @VideoCodec.setter
    def VideoCodec(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def PixelFormat(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        [optional]  pixel format, if empty - default codec pixel format will be used
        """

    @PixelFormat.setter
    def PixelFormat(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def Width(self) -> int:
        """[mandatory] video frame width"""

    @Width.setter
    def Width(self, arg: int, /) -> None: ...

    @property
    def Height(self) -> int:
        """[mandatory] video frame height"""

    @Height.setter
    def Height(self, arg: int, /) -> None: ...

    @property
    def FpsNum(self) -> int:
        """[mandatory] framerate numerator"""

    @FpsNum.setter
    def FpsNum(self, arg: int, /) -> None: ...

    @property
    def FpsDen(self) -> int:
        """[mandatory] framerate denumerator"""

    @FpsDen.setter
    def FpsDen(self, arg: int, /) -> None: ...

    @property
    def VideoCodecParams(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]:
        """map of advanced video codec parameters"""

    @VideoCodecParams.setter
    def VideoCodecParams(self, arg: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString], /) -> None: ...

class Image_VideoRecorder(nanoocp.Standard.Standard_Transient):
    """Video recording tool based on FFmpeg framework."""

    def __init__(self) -> None:
        """Empty constructor."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Close(self) -> None:
        """Close the stream - stop recorder."""

    def Open(self, theFileName: str, theParams: Image_VideoParams) -> bool:
        """
        Open output stream - initialize recorder.
        @param[in] theFileName  video filename
        @param[in] theParams    video parameters
        """

    def ChangeFrame(self) -> Image_PixMap:
        """
        Access RGBA frame, should NOT be re-initialized outside.
        Note that image is expected to have upper-left origin.
        """

    def FrameCount(self) -> int:
        """Return current frame index."""

    def PushFrame(self) -> bool:
        """Push new frame, should be called after Open()."""

class NCollection_Vec3__unsigned_long:
    """
    Generic 3-components vector.
    To be used as RGB color pixel or XYZ 3D-point.
    The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor. Construct the zero vector."""

    @overload
    def __init__(self, theValue: int) -> None:
        """Initialize ALL components of vector within specified value."""

    @overload
    def __init__(self, theVec2: "NCollection_Vec2<unsigned long>", theZ: int = 0) -> None:
        """Constructor from 2-components vector + optional 3rd value."""

    @overload
    def __init__(self, theX: int, theY: int, theZ: int) -> None:
        """Per-component constructor."""

    @overload
    def __init__(self, theOther: NCollection_Vec3__unsigned_long) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    @overload
    def SetValues(self, theX: int, theY: int, theZ: int) -> None: ...

    @overload
    def SetValues(self, theVec2: "NCollection_Vec2<unsigned long>", theZ: int) -> None:
        """Assign new values to the vector."""

    def xy(self) -> "NCollection_Vec2<unsigned long>":
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def yx(self) -> "NCollection_Vec2<unsigned long>":
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def xz(self) -> "NCollection_Vec2<unsigned long>":
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def zx(self) -> "NCollection_Vec2<unsigned long>":
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def yz(self) -> "NCollection_Vec2<unsigned long>":
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def zy(self) -> "NCollection_Vec2<unsigned long>":
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def xyz(self) -> NCollection_Vec3__unsigned_long:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def xzy(self) -> NCollection_Vec3__unsigned_long:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def yxz(self) -> NCollection_Vec3__unsigned_long:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def yzx(self) -> NCollection_Vec3__unsigned_long:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def zyx(self) -> NCollection_Vec3__unsigned_long:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def zxy(self) -> NCollection_Vec3__unsigned_long:
        """@return 3 components by their names in specified order (in GLSL-style)"""

    def x(self) -> int:
        """Alias to 1st component as X coordinate in XYZ."""

    def Setx(self, theValue: int) -> None:
        """Python addition: sets the value x() returns by reference in C++."""

    def r(self) -> int:
        """Alias to 1st component as RED channel in RGB."""

    def Setr(self, theValue: int) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def y(self) -> int:
        """Alias to 2nd component as Y coordinate in XYZ."""

    def Sety(self, theValue: int) -> None:
        """Python addition: sets the value y() returns by reference in C++."""

    def g(self) -> int:
        """Alias to 2nd component as GREEN channel in RGB."""

    def Setg(self, theValue: int) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def z(self) -> int:
        """Alias to 3rd component as Z coordinate in XYZ."""

    def Setz(self, theValue: int) -> None:
        """Python addition: sets the value z() returns by reference in C++."""

    def b(self) -> int:
        """Alias to 3rd component as BLUE channel in RGB."""

    def Setb(self, theValue: int) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    def IsEqual(self, theOther: NCollection_Vec3__unsigned_long) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __eq__(self, theOther: NCollection_Vec3__unsigned_long) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __ne__(self, theOther: NCollection_Vec3__unsigned_long) -> bool:
        """
        Check this vector with another vector for non-equality (without tolerance!).
        """

    def __iadd__(self, theAdd: NCollection_Vec3__unsigned_long) -> NCollection_Vec3__unsigned_long:
        """Compute per-component summary."""

    def __neg__(self) -> NCollection_Vec3__unsigned_long:
        """Unary -."""

    def __isub__(self, theDec: NCollection_Vec3__unsigned_long) -> NCollection_Vec3__unsigned_long:
        """Compute per-component subtraction."""

    def Multiply(self, theFactor: int) -> None:
        """Compute per-component multiplication by scale factor."""

    @overload
    def __imul__(self, theRight: NCollection_Vec3__unsigned_long) -> NCollection_Vec3__unsigned_long:
        """Compute per-component multiplication."""

    @overload
    def __imul__(self, theFactor: int) -> NCollection_Vec3__unsigned_long:
        """Compute per-component multiplication by scale factor."""

    @overload
    def __mul__(self, theFactor: int) -> NCollection_Vec3__unsigned_long:
        """Compute per-component multiplication by scale factor."""

    @overload
    def __mul__(self, arg: NCollection_Vec3__unsigned_long, /) -> NCollection_Vec3__unsigned_long: ...

    def Multiplied(self, theFactor: int) -> NCollection_Vec3__unsigned_long:
        """Compute per-component multiplication by scale factor."""

    def cwiseMin(self, theVec: NCollection_Vec3__unsigned_long) -> NCollection_Vec3__unsigned_long:
        """Compute component-wise minimum of two vectors."""

    def cwiseMax(self, theVec: NCollection_Vec3__unsigned_long) -> NCollection_Vec3__unsigned_long:
        """Compute component-wise maximum of two vectors."""

    def maxComp(self) -> int:
        """Compute maximum component of the vector."""

    def minComp(self) -> int:
        """Compute minimum component of the vector."""

    @overload
    def __itruediv__(self, theInvFactor: int) -> NCollection_Vec3__unsigned_long:
        """Compute per-component division by scale factor."""

    @overload
    def __itruediv__(self, theRight: NCollection_Vec3__unsigned_long) -> NCollection_Vec3__unsigned_long:
        """Compute per-component division."""

    @overload
    def __truediv__(self, theInvFactor: int) -> NCollection_Vec3__unsigned_long:
        """Compute per-component division by scale factor."""

    @overload
    def __truediv__(self, arg: NCollection_Vec3__unsigned_long, /) -> NCollection_Vec3__unsigned_long: ...

    def Dot(self, theOther: NCollection_Vec3__unsigned_long) -> int:
        """Computes the dot product."""

    def Modulus(self) -> int:
        """Computes the vector modulus (magnitude, length)."""

    def SquareModulus(self) -> int:
        """
        Computes the square of vector modulus (magnitude, length).
        This method may be used for performance tricks.
        """

    def Normalize(self) -> None:
        """Normalize the vector."""

    def Normalized(self) -> NCollection_Vec3__unsigned_long:
        """Normalize the vector."""

    @staticmethod
    def Cross(theVec1: NCollection_Vec3__unsigned_long, theVec2: NCollection_Vec3__unsigned_long) -> NCollection_Vec3__unsigned_long:
        """Computes the cross product."""

    @staticmethod
    def GetLERP(theFrom: NCollection_Vec3__unsigned_long, theTo: NCollection_Vec3__unsigned_long, theT: int) -> NCollection_Vec3__unsigned_long:
        """
        Compute linear interpolation between to vectors.
        @param theT - interpolation coefficient 0..1;
        @return interpolation result.
        """

    @staticmethod
    def DX() -> NCollection_Vec3__unsigned_long:
        """Construct DX unit vector."""

    @staticmethod
    def DY() -> NCollection_Vec3__unsigned_long:
        """Construct DY unit vector."""

    @staticmethod
    def DZ() -> NCollection_Vec3__unsigned_long:
        """Construct DZ unit vector."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def __add__(self, arg: NCollection_Vec3__unsigned_long, /) -> NCollection_Vec3__unsigned_long: ...

    def __sub__(self, arg: NCollection_Vec3__unsigned_long, /) -> NCollection_Vec3__unsigned_long: ...
