"""OCCT package StdPrs (toolkit TKV3d)"""

from collections.abc import Sequence
import enum
from typing import overload

import nanoocp.Adaptor2d
import nanoocp.Adaptor3d
import nanoocp.BRep
import nanoocp.BRepAdaptor
import nanoocp.BRepLib
import nanoocp.Bnd
import nanoocp.Font
import nanoocp.Geom
import nanoocp.GeomAbs
import nanoocp.Graphic3d
import nanoocp.HLRAlgo
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.Prs3d
from nanoocp.Prs3d import Prs3d_BndBox as StdPrs_BndBox
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.gp


class StdPrs_Volume(enum.IntEnum):
    """
    defines the way how to interpret input shapes
    Volume_Autodetection to perform Autodetection (would split input shape into two groups)
    Volume_Closed as Closed volumes (to activate back-face culling and capping plane algorithms)
    Volume_Opened as Open volumes (shells or solids with holes)
    """

    StdPrs_Volume_Autodetection = 0

    StdPrs_Volume_Closed = 1

    StdPrs_Volume_Opened = 2

StdPrs_Volume_Autodetection: StdPrs_Volume = StdPrs_Volume.StdPrs_Volume_Autodetection

StdPrs_Volume_Closed: StdPrs_Volume = StdPrs_Volume.StdPrs_Volume_Closed

StdPrs_Volume_Opened: StdPrs_Volume = StdPrs_Volume.StdPrs_Volume_Opened

class StdPrs_BRepFont(nanoocp.Standard.Standard_Transient):
    """
    This tool provides basic services for rendering of vectorized text glyphs as BRep shapes.
    Single instance initialize single font for sequential glyphs rendering with implicit caching of
    already rendered glyphs. Thus position of each glyph in the text is specified by shape location.

    Please notice that this implementation uses mutex for thread-safety access,
    thus may lead to performance penalties in case of concurrent access.
    Although caching should eliminate this issue after rendering of sufficient number of glyphs.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theFontPath: nanoocp.NCollection.NCollection_String, theSize: float, theFaceId: int = 0) -> None:
        """
        Constructor with initialization.
        @param theFontPath FULL path to the font
        @param theSize     the face size in model units
        @param theFaceId   face id within the file (0 by default)
        """

    @overload
    def __init__(self, theFontName: nanoocp.NCollection.NCollection_String, theFontAspect: nanoocp.Font.Font_FontAspect, theSize: float, theStrictLevel: nanoocp.Font.Font_StrictLevel = Font_StrictLevel.Font_StrictLevel_Any) -> None:
        """
        Constructor with initialization.
        @param theFontName    the font name
        @param theFontAspect  the font style
        @param theSize        the face size in model units
        @param theStrictLevel search strict level for using aliases and fallback
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def FindAndCreate(theFontName: nanoocp.TCollection.TCollection_AsciiString, theFontAspect: nanoocp.Font.Font_FontAspect, theSize: float, theStrictLevel: nanoocp.Font.Font_StrictLevel = Font_StrictLevel.Font_StrictLevel_Any) -> StdPrs_BRepFont:
        """
        Find the font Initialize the font.
        @param theFontName    the font name
        @param theFontAspect  the font style
        @param theSize        the face size in model units
        @param theStrictLevel search strict level for using aliases and fallback
        @return true on success
        """

    def Release(self) -> None:
        """Release currently loaded font."""

    @overload
    def Init(self, theFontPath: nanoocp.NCollection.NCollection_String, theSize: float, theFaceId: int) -> bool:
        """
        Initialize the font.
        @param theFontPath FULL path to the font
        @param theSize     the face size in model units
        @param theFaceId   face id within the file (0 by default)
        @return true on success
        """

    @overload
    def Init(self, theFontName: nanoocp.NCollection.NCollection_String, theFontAspect: nanoocp.Font.Font_FontAspect, theSize: float) -> bool:
        """
        Find (using Font_FontMgr) and initialize the font from the given name.
        Alias for FindAndInit() for backward compatibility.
        """

    def FindAndInit(self, theFontName: nanoocp.TCollection.TCollection_AsciiString, theFontAspect: nanoocp.Font.Font_FontAspect, theSize: float, theStrictLevel: nanoocp.Font.Font_StrictLevel = Font_StrictLevel.Font_StrictLevel_Any) -> bool:
        """
        Find (using Font_FontMgr) and initialize the font from the given name.
        Please take into account that size is specified NOT in typography points (pt.).
        If you need to specify size in points, value should be converted.
        Formula for pt. -> m conversion:
        aSizeMeters = 0.0254 * theSizePt / 72.0
        @param theFontName   the font name
        @param theFontAspect the font style
        @param theSize       the face size in model units
        @param theStrictLevel search strict level for using aliases and fallback
        @return true on success
        """

    def FTFont(self) -> nanoocp.Font.Font_FTFont:
        """Return wrapper over FreeType font."""

    def RenderGlyph(self, theChar: str) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Render single glyph as TopoDS_Shape.
        @param theChar glyph identifier
        @return rendered glyph within cache, might be NULL shape
        """

    def SetCompositeCurveMode(self, theToConcatenate: bool) -> None:
        """
        Setup glyph geometry construction mode.
        By default algorithm creates independent TopoDS_Edge
        for each original curve in the glyph (line segment or Bezie curve).
        Algorithm might optionally create composite BSpline curve for each contour
        which reduces memory footprint but limits curve class to C0.
        Notice that altering this flag clears currently accumulated cache!
        """

    def SetWidthScaling(self, theScaleFactor: float) -> None:
        """
        Setup glyph scaling along X-axis.
        By default glyphs are not scaled (scaling factor = 1.0)
        """

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

    def PointSize(self) -> float:
        """Configured point size"""

    @overload
    def AdvanceX(self, theUCharNext: str) -> float: ...

    @overload
    def AdvanceX(self, theUChar: str, theUCharNext: str) -> float:
        """
        Compute advance to the next character with kerning applied when applicable.
        Assuming text rendered horizontally.
        """

    @overload
    def AdvanceY(self, theUCharNext: str) -> float: ...

    @overload
    def AdvanceY(self, theUChar: str, theUCharNext: str) -> float:
        """
        Compute advance to the next character with kerning applied when applicable.
        Assuming text rendered vertically.
        """

    def Scale(self) -> float:
        """Returns scaling factor for current font size."""

class StdPrs_BRepTextBuilder:
    """Represents class for applying text formatting."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_BRepTextBuilder) -> None: ...

    @overload
    def Perform(self, theFont: StdPrs_BRepFont, theFormatter: nanoocp.Font.Font_TextFormatter | None, thePenLoc: nanoocp.gp.gp_Ax3 = ...) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Render text as BRep shape.
        @param theFormatter formatter which defines aligned text
        @param thePenLoc start position and orientation on the baseline
        @return result shape with pen transformation applied as shape location
        """

    @overload
    def Perform(self, theFont: StdPrs_BRepFont, theString: nanoocp.NCollection.NCollection_String, thePenLoc: nanoocp.gp.gp_Ax3 = ..., theHAlign: nanoocp.Graphic3d.Graphic3d_HorizontalTextAlignment = ..., theVAlign: nanoocp.Graphic3d.Graphic3d_VerticalTextAlignment = ...) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Render text as BRep shape.
        @param theString text in UTF-8 encoding
        @param thePenLoc start position and orientation on the baseline
        @param theHAlign horizontal alignment of the text
        @param theVAlign vertical alignment of the text
        @return result shape with pen transformation applied as shape location
        """

class StdPrs_Curve(nanoocp.Prs3d.Prs3d_Root):
    """
    A framework to define display of lines, arcs of circles
    and conic sections.
    This is done with a fixed number of points, which can be modified.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_Curve) -> None: ...

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, drawCurve: bool = True) -> None:
        """
        Adds to the presentation aPresentation the drawing of the curve aCurve.
        The aspect is defined by LineAspect in aDrawer.
        If drawCurve equals false the curve will not be displayed,
        it is used if the curve is a part of some shape and PrimitiveArray
        visualization approach is activated (it is activated by default).
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, drawCurve: bool = True) -> None:
        """
        Adds to the presentation aPresentation the drawing of the curve aCurve.
        The aspect is defined by LineAspect in aDrawer.
        The drawing will be limited between the points of parameter U1 and U2.
        If drawCurve equals false the curve will not be displayed,
        it is used if the curve is a part of some shape and PrimitiveArray
        visualization approach is activated (it is activated by default).
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, Points: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt], drawCurve: bool = True) -> None:
        """
        adds to the presentation aPresentation the drawing of the curve aCurve.
        The aspect is the current aspect.
        aDeflection is used in the circle case.
        Points give a sequence of curve points.
        If drawCurve equals false the curve will not be displayed,
        it is used if the curve is a part of some shape and PrimitiveArray
        visualization approach is activated (it is activated by default).
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, Points: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt], aNbPoints: int = 30, drawCurve: bool = True) -> None:
        """
        adds to the presentation aPresentation the drawing of the curve
        aCurve.
        The aspect is the current aspect.
        The drawing will be limited between the points of parameter
        U1 and U2.
        aDeflection is used in the circle case.
        Points give a sequence of curve points.
        If drawCurve equals false the curve will not be displayed,
        it is used if the curve is a part of some shape and PrimitiveArray
        visualization approach is activated (it is activated by default).
        """

    @overload
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> bool: ...

    @overload
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aDeflection: float, aLimit: float, aNbPoints: int) -> bool:
        """
        returns true if the distance between the point (X,Y,Z) and the
        drawing of the curve is less than aDistance.
        """

    @overload
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> bool: ...

    @overload
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, aDeflection: float, aNbPoints: int) -> bool:
        """
        returns true if the distance between the point (X,Y,Z) and the
        drawing of the curve aCurve is less than aDistance.
        The drawing is considered between the points
        of parameter U1 and U2;
        """

class StdPrs_DeflectionCurve(nanoocp.Prs3d.Prs3d_Root):
    """
    A framework to provide display of any curve with
    respect to the maximal chordal deviation defined in
    the Prs3d_Drawer attributes manager.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_DeflectionCurve) -> None: ...

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, drawCurve: bool = True) -> None:
        """
        adds to the presentation aPresentation the drawing of the curve
        aCurve with respect to the maximal chordial deviation defined
        by the drawer aDrawer.
        The aspect is defined by LineAspect in aDrawer.
        If drawCurve equals false the curve will not be displayed,
        it is used if the curve is a part of some shape and PrimitiveArray
        visualization approach is activated (it is activated by default).
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, drawCurve: bool = True) -> None:
        """
        adds to the presentation aPresentation the drawing of the curve
        aCurve with respect to the maximal chordial deviation defined
        by the drawer aDrawer.
        The aspect is defined by LineAspect in aDrawer.
        The drawing will be limited between the points of parameter U1 and U2.
        If drawCurve equals false the curve will not be displayed,
        it is used if the curve is a part of some shape and PrimitiveArray
        visualization approach is activated (it is activated by default).
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aDeflection: float, aLimit: float, anAngle: float = 0.2, drawCurve: bool = True) -> None:
        """
        adds to the presentation aPresentation the drawing of the curve
        aCurve with respect to the maximal chordial deviation aDeflection.
        The aspect is the current aspect
        If drawCurve equals false the curve will not be displayed,
        it is used if the curve is a part of some shape and PrimitiveArray
        visualization approach is activated (it is activated by default).
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aDeflection: float, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, Points: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt], drawCurve: bool = True) -> None:
        """
        adds to the presentation aPresentation the drawing of the curve
        aCurve with respect to the maximal chordial deviation aDeflection.
        The aspect is the current aspect
        Points give a sequence of curve points.
        If drawCurve equals false the curve will not be displayed,
        it is used if the curve is a part of some shape and PrimitiveArray
        visualization approach is activated (it is activated by default).
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, aDeflection: float, Points: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt], anAngle: float = 0.2, drawCurve: bool = True) -> None:
        """
        adds to the presentation aPresentation the drawing of the curve
        aCurve with respect to the maximal chordial deviation aDeflection.
        The aspect is the current aspect
        The drawing will be limited between the points of parameter U1 and U2.
        Points give a sequence of curve points.
        If drawCurve equals false the curve will not be displayed,
        it is used if the curve is a part of some shape and PrimitiveArray
        visualization approach is activated (it is activated by default).
        """

    @overload
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> bool:
        """
        returns true if the distance between the point (X,Y,Z) and the
        drawing of the curve aCurve with respect of the maximal
        chordial deviation defined by the drawer aDrawer is less then aDistance.
        """

    @overload
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> bool:
        """
        returns true if the distance between the point (X,Y,Z) and the
        drawing of the curve aCurve with respect of the maximal
        chordial deviation defined by the drawer aDrawer is less
        then aDistance. The drawing is considered between the points
        of parameter U1 and U2;
        """

    @overload
    @staticmethod
    def Match(theX: float, theY: float, theZ: float, theDistance: float, theCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, theDeflection: float, theLimit: float, theAngle: float) -> bool:
        """
        Returns true if the distance between the point (theX, theY, theZ)
        and the drawing with respect of the maximal chordial deviation theDeflection is less then
        theDistance.
        """

    @overload
    @staticmethod
    def Match(theX: float, theY: float, theZ: float, theDistance: float, theCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, theU1: float, theU2: float, theDeflection: float, theAngle: float) -> bool:
        """
        Returns true if the distance between the point (theX, theY, theZ)
        and the drawing with respect of the maximal chordial deviation theDeflection is less then
        theDistance. The drawing is considered between the points of parameter theU1 and theU2.
        """

class StdPrs_HLRShapeI(nanoocp.Standard.Standard_Transient):
    """
    Computes the presentation of objects with removal of their hidden lines for a specific
    projector.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ComputeHLR(self, thePrs: nanoocp.Graphic3d.Graphic3d_Structure | None, theShape: nanoocp.TopoDS.TopoDS_Shape, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theProjector: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """Compute presentation for specified shape."""

class StdPrs_HLRPolyShape(StdPrs_HLRShapeI):
    """
    Instantiates Prs3d_PolyHLRShape to define a display of a shape where hidden
    and visible lines are identified with respect to a given projection.
    StdPrs_HLRPolyShape works with a polyhedral simplification of the shape whereas
    StdPrs_HLRShape takes the shape itself into account.
    When you use StdPrs_HLRShape, you obtain an exact result, whereas, when you use
    StdPrs_HLRPolyShape, you reduce computation time but obtain polygonal segments. The polygonal
    algorithm is used.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_HLRPolyShape) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ComputeHLR(self, thePrs: nanoocp.Graphic3d.Graphic3d_Structure | None, theShape: nanoocp.TopoDS.TopoDS_Shape, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theProjector: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """Compute presentation for specified shape."""

class StdPrs_HLRShape(StdPrs_HLRShapeI):
    """
    Computes the presentation of objects with removal of their hidden lines for a specific
    projector. The exact algorithm is used.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_HLRShape) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ComputeHLR(self, thePrs: nanoocp.Graphic3d.Graphic3d_Structure | None, theShape: nanoocp.TopoDS.TopoDS_Shape, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theProjector: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """Compute presentation for specified shape."""

class StdPrs_HLRToolShape:
    @overload
    def __init__(self, TheShape: nanoocp.TopoDS.TopoDS_Shape, TheProjector: nanoocp.HLRAlgo.HLRAlgo_Projector) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_HLRToolShape) -> None: ...

    def NbEdges(self) -> int: ...

    def InitVisible(self, EdgeNumber: int) -> None: ...

    def MoreVisible(self) -> bool: ...

    def NextVisible(self) -> None: ...

    def Visible(self, TheEdge: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> tuple[float, float]: ...

    def InitHidden(self, EdgeNumber: int) -> None: ...

    def MoreHidden(self) -> bool: ...

    def NextHidden(self) -> None: ...

    def Hidden(self, TheEdge: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> tuple[float, float]: ...

class StdPrs_ToolTriangulatedShape(nanoocp.BRepLib.BRepLib_ToolTriangulatedShape):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_ToolTriangulatedShape) -> None: ...

    @staticmethod
    def IsTriangulated(theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Similar to BRepTools::Triangulation() but without extra checks.
        @return true if all faces within shape are triangulated.
        """

    @staticmethod
    def IsClosed(theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Checks back faces visibility for specified shape (to activate back-face culling).
        @return true if shape is closed manifold Solid or compound of such Solids.
        """

    @staticmethod
    def GetDeflection(theShape: nanoocp.TopoDS.TopoDS_Shape, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> float:
        """
        Computes the absolute deflection value depending on the type of deflection in theDrawer:
        <ul>
        <li><b>Aspect_TOD_RELATIVE</b>: the absolute deflection is computed using the relative
        deviation coefficient from theDrawer and the shape's bounding box;</li>
        <li><b>Aspect_TOD_ABSOLUTE</b>: the maximal chordial deviation from theDrawer is
        returned.</li>
        </ul>
        In case of the type of deflection in theDrawer computed relative deflection for shape is
        stored as absolute deflection. It is necessary to use it later on for sub-shapes. This
        function should always be used to compute the deflection value for building discrete
        representations of the shape (triangulation, wireframe) to avoid inconsistencies between
        different representations of the shape and undesirable visual artifacts.
        """

    @staticmethod
    def IsTessellated(theShape: nanoocp.TopoDS.TopoDS_Shape, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> bool:
        """
        Checks whether the shape is properly triangulated for a given display settings.
        @param[in] theShape  the shape.
        @param[in] theDrawer  the display settings.
        """

    @staticmethod
    def Tessellate(theShape: nanoocp.TopoDS.TopoDS_Shape, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> bool:
        """
        Validates triangulation within the shape and performs tessellation if necessary.
        @param[in] theShape  the shape.
        @param[in] theDrawer  the display settings.
        @return true if tessellation was recomputed and false otherwise.
        """

    @staticmethod
    def ClearOnOwnDeflectionChange(theShape: nanoocp.TopoDS.TopoDS_Shape, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theToResetCoeff: bool) -> None:
        """
        If presentation has own deviation coefficient and IsAutoTriangulation() is true,
        function will compare actual coefficients with previous values and will clear triangulation on
        their change (regardless actual tessellation quality). Function is placed here for
        compatibility reasons - new code should avoid using IsAutoTriangulation().
        @param[in] theShape   the shape
        @param[in] theDrawer  the display settings
        @param[in] theToResetCoeff  updates coefficients in theDrawer to actual state to avoid
        redundant recomputations
        """

class StdPrs_Isolines(nanoocp.Prs3d.Prs3d_Root):
    """
    Tool for computing isoline representation for a face or surface.
    Depending on a flags set to the given Prs3d_Drawer instance, on-surface (is used
    by default) or on-triangulation isoline builder algorithm will be used.
    If the given shape is not triangulated, on-surface isoline builder will be applied
    regardless of Prs3d_Drawer flags.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_Isolines) -> None: ...

    class PntOnIso:
        """Auxiliary structure defining 3D point on isoline."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: StdPrs_Isolines.PntOnIso) -> None: ...

        @property
        def Pnt(self) -> nanoocp.gp.gp_Pnt:
            """3D point"""

        @Pnt.setter
        def Pnt(self, arg: nanoocp.gp.gp_Pnt, /) -> None: ...

        @property
        def Param(self) -> float:
            """parameter along the line (for sorting)"""

        @Param.setter
        def Param(self, arg: float, /) -> None: ...

    class SegOnIso:
        """Auxiliary structure defining segment of isoline."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: StdPrs_Isolines.SegOnIso) -> None: ...

        def __lt__(self, theOther: StdPrs_Isolines.SegOnIso) -> bool: ...

        @property
        def Pnts(self) -> list[StdPrs_Isolines.PntOnIso]: ...

        @Pnts.setter
        def Pnts(self, arg: Sequence[StdPrs_Isolines.PntOnIso], /) -> None: ...

    @overload
    @staticmethod
    def Add(thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theFace: nanoocp.TopoDS.TopoDS_Face, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theDeflection: float) -> None:
        """
        Computes isolines presentation for a TopoDS face.
        This method chooses proper version of isoline builder algorithm : on triangulation
        or surface depending on the flag passed from Prs3d_Drawer attributes.
        This method is a default way to display isolines for a given TopoDS face.
        @param[in] thePresentation  the presentation.
        @param[in] theFace  the face.
        @param[in] theDrawer  the display settings.
        @param[in] theDeflection  the deflection for isolines-on-surface version.
        """

    @overload
    @staticmethod
    def Add(theFace: nanoocp.TopoDS.TopoDS_Face, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theDeflection: float, theUPolylines: nanoocp.NCollection.NCollection_List[nanoocp.NCollection.NCollection_HSequence[nanoocp.gp.gp_Pnt]], theVPolylines: nanoocp.NCollection.NCollection_List[nanoocp.NCollection.NCollection_HSequence[nanoocp.gp.gp_Pnt]]) -> None:
        """
        Computes isolines presentation for a TopoDS face.
        This method chooses proper version of isoline builder algorithm : on triangulation
        or surface depending on the flag passed from Prs3d_Drawer attributes.
        This method is a default way to display isolines for a given TopoDS face.
        @param[in] theFace  the face.
        @param[in] theDrawer  the display settings.
        @param[in] theDeflection  the deflection for isolines-on-surface version.
        """

    @overload
    @staticmethod
    def AddOnTriangulation(thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theFace: nanoocp.TopoDS.TopoDS_Face, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Computes isolines on triangulation and adds them to a presentation.
        @param[in] thePresentation  the presentation.
        @param[in] theFace  the face.
        @param[in] theDrawer  the display settings.
        """

    @overload
    @staticmethod
    def AddOnTriangulation(theFace: nanoocp.TopoDS.TopoDS_Face, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theUPolylines: nanoocp.NCollection.NCollection_List[nanoocp.NCollection.NCollection_HSequence[nanoocp.gp.gp_Pnt]], theVPolylines: nanoocp.NCollection.NCollection_List[nanoocp.NCollection.NCollection_HSequence[nanoocp.gp.gp_Pnt]]) -> None:
        """
        Computes isolines on triangulation.
        @param[in] theFace  the face.
        @param[in] theDrawer  the display settings.
        @param[out] theUPolylines  the sequence of result polylines
        @param[out] theVPolylines  the sequence of result polylines
        """

    @overload
    @staticmethod
    def AddOnTriangulation(thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theTriangulation: nanoocp.Poly.Poly_Triangulation | None, theSurface: nanoocp.Geom.Geom_Surface | None, theLocation: nanoocp.TopLoc.TopLoc_Location, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theUIsoParams: nanoocp.NCollection.NCollection_Sequence[float], theVIsoParams: nanoocp.NCollection.NCollection_Sequence[float]) -> None:
        """
        Computes isolines on triangulation and adds them to a presentation.
        @param[in] thePresentation  the presentation.
        @param[in] theTriangulation  the triangulation.
        @param[in] theSurface  the definition of triangulated surface. The surface
        adapter is used to precisely evaluate isoline points using surface
        law and fit them on triangulation. If NULL is passed, the method will
        use linear interpolation of triangle node's UV coordinates to evaluate
        isoline points.
        @param[in] theLocation  the location transformation defined for triangulation (surface).
        @param[in] theDrawer  the display settings.
        @param[in] theUIsoParams  the parameters of u isolines to compute.
        @param[in] theVIsoParams  the parameters of v isolines to compute.
        """

    @overload
    @staticmethod
    def AddOnSurface(thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theFace: nanoocp.TopoDS.TopoDS_Face, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theDeflection: float) -> None:
        """
        Computes isolines on surface and adds them to presentation.
        @param[in] thePresentation  the presentation.
        @param[in] theFace  the face.
        @param[in] theDrawer  the display settings.
        @param[in] theDeflection  the deflection value.
        """

    @overload
    @staticmethod
    def AddOnSurface(theFace: nanoocp.TopoDS.TopoDS_Face, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theDeflection: float, theUPolylines: nanoocp.NCollection.NCollection_List[nanoocp.NCollection.NCollection_HSequence[nanoocp.gp.gp_Pnt]], theVPolylines: nanoocp.NCollection.NCollection_List[nanoocp.NCollection.NCollection_HSequence[nanoocp.gp.gp_Pnt]]) -> None:
        """
        Computes isolines on surface and adds them to presentation.
        @param[in] theFace  the face
        @param[in] theDrawer  the display settings
        @param[in] theDeflection  the deflection value
        @param[out] theUPolylines  the sequence of result polylines
        @param[out] theVPolylines  the sequence of result polylines
        """

    @overload
    @staticmethod
    def AddOnSurface(thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theSurface: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theDeflection: float, theUIsoParams: nanoocp.NCollection.NCollection_Sequence[float], theVIsoParams: nanoocp.NCollection.NCollection_Sequence[float]) -> None:
        """
        Computes isolines on surface and adds them to presentation.
        @param[in] thePresentation  the presentation.
        @param[in] theSurface  the surface.
        @param[in] theDrawer  the display settings.
        @param[in] theDeflection  the deflection value.
        @param[in] theUIsoParams  the parameters of u isolines to compute.
        @param[in] theVIsoParams  the parameters of v isolines to compute.
        """

    @staticmethod
    def UVIsoParameters(theFace: nanoocp.TopoDS.TopoDS_Face, theNbIsoU: int, theNbIsoV: int, theUVLimit: float, theUIsoParams: nanoocp.NCollection.NCollection_Sequence[float], theVIsoParams: nanoocp.NCollection.NCollection_Sequence[float]) -> tuple[float, float, float, float]:
        """
        Evaluate sequence of parameters for drawing uv isolines for a given face.
        @param[in] theFace  the face.
        @param[in] theNbIsoU  the number of u isolines.
        @param[in] theNbIsoV  the number of v isolines.
        @param[in] theUVLimit  the u, v parameter value limit.
        @param[out] theUIsoParams  the sequence of u isoline parameters.
        @param[out] theVIsoParams  the sequence of v isoline parameters.
        @param[out] theUmin  the lower U boundary of  theFace.
        @param[out] theUmax  the upper U boundary of  theFace.
        @param[out] theVmin  the lower V boundary of  theFace.
        @param[out] theVmax  the upper V boundary of  theFace.
        """

class StdPrs_Plane(nanoocp.Prs3d.Prs3d_Root):
    """A framework to display infinite planes."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_Plane) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aPlane: nanoocp.Adaptor3d.Adaptor3d_Surface, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Defines display of infinite planes.
        The infinite plane aPlane is added to the display
        aPresentation, and the attributes of the display are
        defined by the attribute manager aDrawer.
        """

    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aPlane: nanoocp.Adaptor3d.Adaptor3d_Surface, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> bool:
        """
        returns true if the distance between the point (X,Y,Z) and the
        plane is less than aDistance.
        """

class StdPrs_ToolPoint:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_ToolPoint) -> None: ...

    @staticmethod
    def Coord(aPoint: nanoocp.Geom.Geom_Point | None) -> tuple[float, float, float]: ...

class StdPrs_Point:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_Point) -> None: ...

    @staticmethod
    def Add(thePrs: nanoocp.Graphic3d.Graphic3d_Structure | None, thePoint: nanoocp.Geom.Geom_Point | None, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None: ...

    @staticmethod
    def Match(thePoint: nanoocp.Geom.Geom_Point | None, theX: float, theY: float, theZ: float, theDistance: float) -> bool: ...

class StdPrs_PoleCurve(nanoocp.Prs3d.Prs3d_Root):
    """
    A framework to provide display of Bezier or BSpline curves
    (by drawing a broken line linking the poles of the curve).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_PoleCurve) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Defines display of BSpline and Bezier curves.
        Adds the 3D curve aCurve to the
        StdPrs_PoleCurve algorithm. This shape is found in
        the presentation object aPresentation, and its display
        attributes are set in the attribute manager aDrawer.
        The curve object from Adaptor3d provides data from
        a Geom curve. This makes it possible to use the
        surface in a geometric algorithm.
        """

    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> bool:
        """
        returns true if the distance between the point (X,Y,Z) and the
        broken line made of the poles is less then aDistance.
        """

    @staticmethod
    def Pick(X: float, Y: float, Z: float, aDistance: float, aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> int:
        """
        returns the pole the most near of the point (X,Y,Z) and
        returns its range. The distance between the pole and
        (X,Y,Z) must be less then aDistance. If no pole corresponds, 0 is returned.
        """

class StdPrs_ShadedShape(nanoocp.Prs3d.Prs3d_Root):
    """
    Auxiliary procedures to prepare Shaded presentation of specified shape.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_ShadedShape) -> None: ...

    @overload
    @staticmethod
    def Add(thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theShape: nanoocp.TopoDS.TopoDS_Shape, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theVolume: StdPrs_Volume = StdPrs_Volume.StdPrs_Volume_Autodetection, theGroup: nanoocp.Graphic3d.Graphic3d_Group | None = None) -> None:
        """
        Shades <theShape>.
        @param theVolumeType defines the way how to interpret input shapes - as Closed volumes (to
        activate back-face culling and capping plane algorithms), as Open volumes (shells or solids
        with holes) or to perform Autodetection (would split input shape into two groups)
        """

    @overload
    @staticmethod
    def Add(thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theShape: nanoocp.TopoDS.TopoDS_Shape, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theHasTexels: bool, theUVOrigin: nanoocp.gp.gp_Pnt2d, theUVRepeat: nanoocp.gp.gp_Pnt2d, theUVScale: nanoocp.gp.gp_Pnt2d, theVolume: StdPrs_Volume = StdPrs_Volume.StdPrs_Volume_Autodetection, theGroup: nanoocp.Graphic3d.Graphic3d_Group | None = None) -> None:
        """
        Shades <theShape> with texture coordinates.
        @param theVolumeType defines the way how to interpret input shapes - as Closed volumes (to
        activate back-face culling and capping plane algorithms), as Open volumes (shells or solids
        with holes) or to perform Autodetection (would split input shape into two groups)
        """

    @staticmethod
    def ExploreSolids(theShape: nanoocp.TopoDS.TopoDS_Shape, theBuilder: nanoocp.BRep.BRep_Builder, theClosed: nanoocp.TopoDS.TopoDS_Compound, theOpened: nanoocp.TopoDS.TopoDS_Compound, theIgnore1DSubShape: bool) -> None:
        """
        Searches closed and unclosed subshapes in shape structure and puts them
        into two compounds for separate processing of closed and unclosed sub-shapes
        """

    @staticmethod
    def AddWireframeForFreeElements(thePrs: nanoocp.Graphic3d.Graphic3d_Structure | None, theShape: nanoocp.TopoDS.TopoDS_Shape, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """Computes wireframe presentation for free wires and vertices"""

    @staticmethod
    def AddWireframeForFacesWithoutTriangles(thePrs: nanoocp.Graphic3d.Graphic3d_Structure | None, theShape: nanoocp.TopoDS.TopoDS_Shape, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Computes special wireframe presentation for faces without triangulation.
        """

    @overload
    @staticmethod
    def FillTriangles(theShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles:
        """
        Create primitive array with triangles for specified shape.
        @param[in] theShape  the shape with precomputed triangulation
        """

    @overload
    @staticmethod
    def FillTriangles(theShape: nanoocp.TopoDS.TopoDS_Shape, theHasTexels: bool, theUVOrigin: nanoocp.gp.gp_Pnt2d, theUVRepeat: nanoocp.gp.gp_Pnt2d, theUVScale: nanoocp.gp.gp_Pnt2d) -> nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles:
        """
        Create primitive array of triangles for specified shape.
        @param theShape     the shape with precomputed triangulation
        @param theHasTexels define UV coordinates in primitive array
        @param theUVOrigin  origin for UV coordinates
        @param theUVRepeat  repeat parameters  for UV coordinates
        @param theUVScale   scale coefficients for UV coordinates
        @return triangles array or NULL if specified face does not have computed triangulation
        """

    @staticmethod
    def FillFaceBoundaries(theShape: nanoocp.TopoDS.TopoDS_Shape, theUpperContinuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_CN) -> nanoocp.Graphic3d.Graphic3d_ArrayOfSegments:
        """
        Define primitive array of boundary segments for specified shape.
        @param theShape segments array or NULL if specified face does not have computed triangulation
        @param theUpperContinuity the most edge continuity class to be included to result (edges with
        more continuity will be ignored)
        """

class StdPrs_ShadedSurface(nanoocp.Prs3d.Prs3d_Root):
    """
    Computes the shading presentation of surfaces.
    Draws a surface by drawing the isoparametric curves with respect to
    a maximal chordial deviation.
    The number of isoparametric curves to be drawn and their color are
    controlled by the furnished Drawer.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_ShadedSurface) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aSurface: nanoocp.Adaptor3d.Adaptor3d_Surface, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Adds the surface aSurface to the presentation object aPresentation.
        The surface's display attributes are set in the attribute manager aDrawer.
        The surface object from Adaptor3d provides data
        from a Geom surface in order to use the surface in an algorithm.
        """

class StdPrs_ShapeTool:
    """Describes the behaviour requested for a wireframe shape presentation."""

    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theAllVertices: bool = False) -> None:
        """
        Constructs the tool and initializes it using theShape and theAllVertices
        (optional) arguments. By default, only isolated and internal vertices are considered,
        however if theAllVertices argument is equal to True, all shape's vertices are taken into
        account.
        """

    def InitFace(self) -> None: ...

    def MoreFace(self) -> bool: ...

    def NextFace(self) -> None: ...

    def GetFace(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def FaceBound(self) -> nanoocp.Bnd.Bnd_Box: ...

    def IsPlanarFace(self) -> bool: ...

    def InitCurve(self) -> None: ...

    def MoreCurve(self) -> bool: ...

    def NextCurve(self) -> None: ...

    def GetCurve(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def CurveBound(self) -> nanoocp.Bnd.Bnd_Box: ...

    def Neighbours(self) -> int: ...

    def FacesOfEdge(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]: ...

    def InitVertex(self) -> None: ...

    def MoreVertex(self) -> bool: ...

    def NextVertex(self) -> None: ...

    def GetVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def HasSurface(self) -> bool: ...

    def CurrentTriangulation(self, l: nanoocp.TopLoc.TopLoc_Location) -> nanoocp.Poly.Poly_Triangulation: ...

    def HasCurve(self) -> bool: ...

    def PolygonOnTriangulation(self, l: nanoocp.TopLoc.TopLoc_Location) -> tuple[nanoocp.Poly.Poly_PolygonOnTriangulation, nanoocp.Poly.Poly_Triangulation]: ...

    def Polygon3D(self, l: nanoocp.TopLoc.TopLoc_Location) -> nanoocp.Poly.Poly_Polygon3D: ...

    @staticmethod
    def IsPlanarFace_s(theFace: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

class StdPrs_ToolRFace:
    """
    Iterator over 2D curves restricting a face (skipping internal/external edges).
    In addition, the algorithm skips NULL curves - IsInvalidGeometry() can be checked if this should
    be handled within algorithm.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, aSurface: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None) -> None:
        """Constructor with initialization."""

    def IsOriented(self) -> bool:
        """Return TRUE indicating that iterator looks only for oriented edges."""

    def Init(self) -> None:
        """Move iterator to the first element."""

    def More(self) -> bool:
        """Return TRUE if iterator points to the curve."""

    def Next(self) -> None:
        """Go to the next curve in the face."""

    def Value(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """Return current curve."""

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Return current edge."""

    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Return current edge orientation."""

    def IsInvalidGeometry(self) -> bool:
        """Return TRUE if NULL curves have been skipped."""

class StdPrs_ToolVertex:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_ToolVertex) -> None: ...

    @staticmethod
    def Coord(aPoint: nanoocp.TopoDS.TopoDS_Vertex) -> tuple[float, float, float]: ...

class StdPrs_Vertex:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_Vertex) -> None: ...

    @staticmethod
    def Add(thePrs: nanoocp.Graphic3d.Graphic3d_Structure | None, thePoint: nanoocp.TopoDS.TopoDS_Vertex, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None: ...

    @staticmethod
    def Match(thePoint: nanoocp.TopoDS.TopoDS_Vertex, theX: float, theY: float, theZ: float, theDistance: float) -> bool: ...

class StdPrs_WFDeflectionRestrictedFace(nanoocp.Prs3d.Prs3d_Root):
    """
    A framework to provide display of U and V
    isoparameters of faces, while allowing you to impose
    a deflection on them.
    Computes the wireframe presentation of faces with
    restrictions by displaying a given number of U and/or
    V isoparametric curves. The isoparametric curves are
    drawn with respect to a maximal chordial deviation.
    The presentation includes the restriction curves.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_WFDeflectionRestrictedFace) -> None: ...

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Defines a display featuring U and V isoparameters.
        Adds the surface aFace to the
        StdPrs_WFRestrictedFace algorithm. This face is
        found in a shape in the presentation object
        aPresentation, and its display attributes - in
        particular, the number of U and V isoparameters - are
        set in the attribute manager aDrawer.
        aFace is BRepAdaptor_Surface surface created
        from a face in a topological shape. which is passed
        as an argument through the
        BRepAdaptor_Surface surface created from it.
        This is what allows the topological face to be treated
        as a geometric surface.
        """

    @overload
    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, DrawUIso: bool, DrawVIso: bool, Deflection: float, NBUiso: int, NBViso: int, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, Curves: nanoocp.NCollection.NCollection_List[nanoocp.NCollection.NCollection_HSequence[nanoocp.gp.gp_Pnt]]) -> None:
        """
        Defines a display of a delection-specified face. The
        display will feature U and V isoparameters.
        Adds the topology aShape to the
        StdPrs_WFRestrictedFace algorithm. This shape is
        found in the presentation object aPresentation, and
        its display attributes - except the number of U and V
        isoparameters - are set in the attribute manager aDrawer.
        The function sets the number of U and V
        isoparameters, NBUiso and NBViso, in the shape. To
        do this, the arguments DrawUIso and DrawVIso must be true.
        aFace is BRepAdaptor_Surface surface created
        from a face in a topological shape. which is passed
        as an argument through the
        BRepAdaptor_Surface surface created from it.
        This is what allows the topological face to be treated
        as a geometric surface.
        Curves give a sequence of face curves, it is used if the PrimitiveArray
        visualization approach is activated (it is activated by default).
        """

    @staticmethod
    def AddUIso(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Defines a display featuring U isoparameters
        respectively. Add the surface aFace to the
        StdPrs_WFRestrictedFace algorithm. This face
        is found in a shape in the presentation object
        aPresentation, and its display attributes - in
        particular, the number of U isoparameters -
        are set in the attribute manager aDrawer.
        aFace is BRepAdaptor_Surface surface
        created from a face in a topological shape. which
        is passed to the function as an argument through
        the BRepAdaptor_Surface surface created from
        it. This is what allows the topological face to be
        treated as a geometric surface.
        """

    @staticmethod
    def AddVIso(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Defines a display featuring V isoparameters
        respectively. Add the surface aFace to the
        StdPrs_WFRestrictedFace algorithm. This face
        is found in a shape in the presentation object
        aPresentation, and its display attributes - in
        particular, the number of V isoparameters -
        are set in the attribute manager aDrawer.
        aFace is BRepAdaptor_Surface surface
        created from a face in a topological shape. which
        is passed to the function as an argument through
        the BRepAdaptor_Surface surface created from
        it. This is what allows the topological face to be
        treated as a geometric surface.
        """

    @overload
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> bool: ...

    @overload
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, DrawUIso: bool, DrawVIso: bool, aDeflection: float, NBUiso: int, NBViso: int) -> bool: ...

    @staticmethod
    def MatchUIso(X: float, Y: float, Z: float, aDistance: float, aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> bool: ...

    @staticmethod
    def MatchVIso(X: float, Y: float, Z: float, aDistance: float, aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> bool: ...

class StdPrs_WFDeflectionSurface(nanoocp.Prs3d.Prs3d_Root):
    """
    Draws a surface by drawing the isoparametric curves with respect to
    a maximal chordial deviation.
    The number of isoparametric curves to be drawn and their color are
    controlled by the furnished Drawer.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_WFDeflectionSurface) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aSurface: nanoocp.Adaptor3d.Adaptor3d_Surface | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Adds the surface aSurface to the presentation object
        aPresentation, and defines its boundaries and isoparameters.
        The shape's display attributes are set in the attribute
        manager aDrawer. These include whether deflection
        is absolute or relative to the size of the shape.
        The surface aSurface is a surface object from
        Adaptor, and provides data from a Geom surface.
        This makes it possible to use the surface in a geometric algorithm.
        Note that this surface object is manipulated by handles.
        """

class StdPrs_WFPoleSurface(nanoocp.Prs3d.Prs3d_Root):
    """
    Computes the presentation of surfaces by drawing a
    double network of lines linking the poles of the surface
    in the two parametric direction.
    The number of lines to be drawn is controlled
    by the NetworkNumber of the given Drawer.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_WFPoleSurface) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aSurface: nanoocp.Adaptor3d.Adaptor3d_Surface, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Adds the surface aSurface to the presentation object aPresentation.
        The shape's display attributes are set in the attribute manager aDrawer.
        The surface aSurface is a surface object from
        Adaptor3d, and provides data from a Geom surface.
        This makes it possible to use the surface in a geometric algorithm.
        """

class StdPrs_WFRestrictedFace(nanoocp.Prs3d.Prs3d_Root):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_WFRestrictedFace) -> None: ...

    @overload
    @staticmethod
    def Add(thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, theDrawUIso: bool, theDrawVIso: bool, theNbUIso: int, theNbVIso: int, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theCurves: nanoocp.NCollection.NCollection_List[nanoocp.NCollection.NCollection_HSequence[nanoocp.gp.gp_Pnt]]) -> None: ...

    @overload
    @staticmethod
    def Add(thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None: ...

    @overload
    @staticmethod
    def Match(theX: float, theY: float, theZ: float, theDistance: float, theFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, theDrawUIso: bool, theDrawVIso: bool, theDeflection: float, theNbUIso: int, theNbVIso: int, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> bool: ...

    @overload
    @staticmethod
    def Match(theX: float, theY: float, theZ: float, theDistance: float, theFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> bool: ...

    @staticmethod
    def MatchUIso(theX: float, theY: float, theZ: float, theDistance: float, theFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> bool: ...

    @staticmethod
    def MatchVIso(theX: float, theY: float, theZ: float, theDistance: float, theFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> bool: ...

    @staticmethod
    def AddUIso(thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None: ...

    @staticmethod
    def AddVIso(thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None: ...

class StdPrs_WFShape(nanoocp.Prs3d.Prs3d_Root):
    """Tool for computing wireframe presentation of a TopoDS_Shape."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_WFShape) -> None: ...

    @staticmethod
    def Add(thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theShape: nanoocp.TopoDS.TopoDS_Shape, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theIsParallel: bool = False) -> None:
        """
        Computes wireframe presentation of a shape.
        @param[in] thePresentation  the presentation.
        @param[in] theShape  the shape.
        @param[in] theDrawer  the draw settings.
        @param[in] theIsParallel  perform algorithm using multiple threads
        """

    @overload
    @staticmethod
    def AddEdgesOnTriangulation(theShape: nanoocp.TopoDS.TopoDS_Shape, theToExcludeGeometric: bool = True) -> nanoocp.Graphic3d.Graphic3d_ArrayOfPrimitives:
        """
        Compute free and boundary edges on a triangulation of each face in the given shape.
        @param[in] theShape               the list of triangulated faces
        @param[in] theToExcludeGeometric  flag indicating that Faces with defined Surface should be
        skipped
        """

    @overload
    @staticmethod
    def AddEdgesOnTriangulation(theSegments: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt], theShape: nanoocp.TopoDS.TopoDS_Shape, theToExcludeGeometric: bool = True) -> None:
        """
        Compute free and boundary edges on a triangulation of each face in the given shape.
        @param[in] theSegments            the sequence of points defining segments
        @param[in] theShape               the list of triangulated faces
        @param[in] theToExcludeGeometric  flag indicating that Faces with defined Surface should be
        skipped
        """

    @staticmethod
    def AddAllEdges(theShape: nanoocp.TopoDS.TopoDS_Shape, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> nanoocp.Graphic3d.Graphic3d_ArrayOfPrimitives:
        """
        Compute all edges (wire, free, unfree) and put them into single primitive array.
        @param[in] theShape  the shape
        @param[in] theDrawer  the drawer settings (deviation angle and maximal parameter value)
        """

    @staticmethod
    def AddVertexes(theShape: nanoocp.TopoDS.TopoDS_Shape, theVertexMode: nanoocp.Prs3d.Prs3d_VertexDrawMode) -> nanoocp.Graphic3d.Graphic3d_ArrayOfPoints:
        """
        Compute vertex presentation for a shape.
        @param[in] theShape  the shape
        @param[in] theVertexMode  vertex filter
        """

class StdPrs_WFSurface(nanoocp.Prs3d.Prs3d_Root):
    """
    Computes the wireframe presentation of surfaces
    by displaying a given number of U and/or V isoparametric
    curves. The isoparametric curves are drawn with respect
    to a given number of points.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdPrs_WFSurface) -> None: ...

    @staticmethod
    def Add(aPresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, aSurface: nanoocp.Adaptor3d.Adaptor3d_Surface | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Draws a surface by drawing the isoparametric curves with respect to
        a fixed number of points given by the Drawer.
        The number of isoparametric curves to be drawn and their color are
        controlled by the furnished Drawer.
        """
