"""OCCT package IGESGraph (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.IGESBasic
import nanoocp.IGESData
import nanoocp.Interface
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.gp


class IGESGraph:
    """
    This package contains the group of classes necessary
    to define Graphic data among Structure Entities.
    (e.g., Fonts, Colors, Screen management ...)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph) -> None: ...

    @staticmethod
    def Init() -> None:
        """Prepares dynamic data (Protocol, Modules) for this package"""

    @staticmethod
    def Protocol() -> IGESGraph_Protocol:
        """Returns the Protocol for this Package"""

class IGESGraph_Color(nanoocp.IGESData.IGESData_ColorEntity):
    """
    defines IGESColor, Type <314> Form <0>
    in package IGESGraph

    The Color Definition Entity is used to communicate the
    relationship of primary colors to the intensity level of
    the respective graphics devices as a percent of full
    intensity range.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph_Color) -> None: ...

    def Init(self, red: float, green: float, blue: float, aColorName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the fields of the class Color
        - red        : Red   color intensity (range 0.0 to 100.0)
        - green      : Green color intensity (range 0.0 to 100.0)
        - blue       : Blue  color intensity (range 0.0 to 100.0)
        - aColorName : Name of the color (optional)
        """

    def RGBIntensity(self) -> tuple[float, float, float]: ...

    def CMYIntensity(self) -> tuple[float, float, float]: ...

    def HLSPercentage(self) -> tuple[float, float, float]: ...

    def HasColorName(self) -> bool:
        """
        returns True if optional character string is assigned,
        False otherwise.
        """

    def ColorName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        if HasColorName() is True returns the Verbal description of
        the Color.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_DefinitionLevel(nanoocp.IGESData.IGESData_LevelListEntity):
    """
    defines IGESDefinitionLevel, Type <406> Form <1>
    in package IGESGraph

    Indicates the no. of levels on which an entity is
    defined
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph_DefinitionLevel) -> None: ...

    def Init(self, allLevelNumbers: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """
        This method is used to set the fields of the class
        DefinitionLevel
        - allLevelNumbers : Values of Level Numbers
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values in <me>"""

    def NbLevelNumbers(self) -> int:
        """Must return the count of levels (== NbPropertyValues)"""

    def LevelNumber(self, LevelIndex: int) -> int:
        """
        returns the Level Number of <me> indicated by <LevelIndex>
        raises an exception if LevelIndex is <= 0 or
        LevelIndex > NbPropertyValues
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_DrawingSize(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESDrawingSize, Type <406> Form <16>
    in package IGESGraph

    Specifies the drawing size in drawing units. The
    origin of the drawing is defined to be (0,0) in
    drawing space
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph_DrawingSize) -> None: ...

    def Init(self, nbProps: int, aXSize: float, aYSize: float) -> None:
        """
        This method is used to set the fields of the class
        DrawingSize
        - nbProps : Number of property values (NP = 2)
        - aXSize  : Extent of Drawing along positive XD axis
        - aYSize  : Extent of Drawing along positive YD axis
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values in <me> (NP = 2)"""

    def XSize(self) -> float:
        """returns the extent of Drawing along positive XD axis"""

    def YSize(self) -> float:
        """returns the extent of Drawing along positive YD axis"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_DrawingUnits(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESDrawingUnits, Type <406> Form <17>
    in package IGESGraph

    Specifies the drawing space units as outlined
    in the Drawing entity
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph_DrawingUnits) -> None: ...

    def Init(self, nbProps: int, aFlag: int, aUnit: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the fields of the class
        DrawingUnits
        - nbProps : Number of property values (NP = 2)
        - aFlag   : DrawingUnits Flag
        - aUnit   : DrawingUnits Name
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values in <me>"""

    def Flag(self) -> int:
        """returns the drawing space units of <me>"""

    def Unit(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns the name of the drawing space units of <me>"""

    def UnitValue(self) -> float:
        """
        Computes the value of the unit, in meters, according Flag
        (same values as for GlobalSection from IGESData)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_GeneralModule(nanoocp.IGESData.IGESData_GeneralModule):
    """
    Definition of General Services for IGESGraph (specific part)
    This Services comprise : Shared & Implied Lists, Copy, Check
    """

    @overload
    def __init__(self) -> None:
        """Creates a GeneralModule from IGESGraph and puts it into GeneralLib"""

    @overload
    def __init__(self, theOther: IGESGraph_GeneralModule) -> None: ...

    def OwnSharedCase(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a given IGESEntity <ent>, from
        its specific parameters : specific for each type
        """

    def DirChecker(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """
        Returns a DirChecker, specific for each type of Entity
        (identified by its Case Number) : this DirChecker defines
        constraints which must be respected by the DirectoryPart
        """

    def OwnCheckCase(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check for each type of Entity"""

    def NewVoid(self, CN: int) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """Specific creation of a new void entity"""

    def OwnCopyCase(self, CN: int, entfrom: nanoocp.IGESData.IGESData_IGESEntity | None, entto: nanoocp.IGESData.IGESData_IGESEntity | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies parameters which are specific of each Type of Entity"""

    def CategoryNumber(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, shares: nanoocp.Interface.Interface_ShareTool) -> int:
        """
        Returns a category number which characterizes an entity
        Drawing for all
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_HighLight(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESHighLight, Type <406> Form <20>
    in package IGESGraph

    Attaches information that an entity is to be
    displayed in some system dependent manner
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph_HighLight) -> None: ...

    def Init(self, nbProps: int, aHighLightStatus: int) -> None:
        """
        This method is used to set the fields of the class
        HighLight
        - nbProps          : Number of property values (NP = 1)
        - aHighLightStatus : HighLight Flag
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values in <me>"""

    def HighLightStatus(self) -> int:
        """
        returns 0 if <me> is not highlighted(default),
        1 if <me> is highlighted
        """

    def IsHighLighted(self) -> bool:
        """returns True if entity is highlighted"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_IntercharacterSpacing(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESIntercharacterSpacing, Type <406> Form <18>
    in package IGESGraph

    Specifies the gap between letters when fixed-pitch
    spacing is used
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph_IntercharacterSpacing) -> None: ...

    def Init(self, nbProps: int, anISpace: float) -> None:
        """
        This method is used to set the fields of the class
        IntercharacterSpacing
        - nbProps  : Number of property values (NP = 1)
        - anISpace : Intercharacter spacing percentage
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values in <me>"""

    def ISpace(self) -> float:
        """
        returns the Intercharacter Space of <me> in percentage
        of the text height (Range = 0..100)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_LineFontDefPattern(nanoocp.IGESData.IGESData_LineFontEntity):
    """
    defines IGESLineFontDefPattern, Type <304> Form <2>
    in package IGESGraph

    Line Font may be defined by repetition of a basic pattern
    of visible-blank(or, on-off) segments superimposed on
    a line or a curve. The line or curve is then displayed
    according to the basic pattern.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph_LineFontDefPattern) -> None: ...

    def Init(self, allSegLength: nanoocp.NCollection.NCollection_HArray1[float] | None, aPattern: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the fields of the class
        LineFontDefPattern
        - allSegLength : Containing lengths of respective segments
        - aPattern     : HAsciiString indicating visible-blank segments
        """

    def NbSegments(self) -> int:
        """returns the number of segments in the visible-blank pattern"""

    def Length(self, Index: int) -> float:
        """
        returns the Length of Index'th segment of the basic pattern
        raises exception if Index <= 0 or Index > NbSegments
        """

    def DisplayPattern(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns the string indicating which segments of the basic
        pattern are visible and which are blanked.
        e.g:
        theNbSegments = 5 and if Bit Pattern = 10110, which means that
        segments 2, 3 and 5 are visible, whereas segments 1 and 4 are
        blank. The method returns "2H16" as the HAsciiString.
        Note: The bits are right justified. (16h = 10110)
        """

    def IsVisible(self, Index: int) -> bool:
        """
        The Display Pattern is decrypted to
        return True if the Index'th basic pattern is Visible,
        False otherwise.
        If Index > NbSegments or Index <= 0 then return value is
        False.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_LineFontDefTemplate(nanoocp.IGESData.IGESData_LineFontEntity):
    """
    defines IGESLineFontDefTemplate, Type <304> Form <1>
    in package IGESGraph

    Line Font can be defined as a repetition of Template figure
    that is displayed at regularly spaced locations along a
    planer anchoring curve. The anchoring curve itself has
    no visual purpose.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph_LineFontDefTemplate) -> None: ...

    def Init(self, anOrientation: int, aTemplate: nanoocp.IGESBasic.IGESBasic_SubfigureDef | None, aDistance: float, aScale: float) -> None:
        """
        This method is used to set the fields of the class
        LineFontDefTemplate
        - anOrientation : Orientation of Template figure on
        anchoring curve
        - aTemplate     : SubfigureDef entity used as Template figure
        - aDistance     : Distance between the neighbouring Template
        figures
        - aScale        : Scale factor applied to the Template figure
        """

    def Orientation(self) -> int:
        """
        if return value = 0, Each Template display is oriented by aligning
        the axis of the SubfigureDef with the axis of
        the definition space of the anchoring curve.
        = 1, Each Template display is oriented by aligning
        X-axis of the SubfigureDef with the tangent
        vector of the anchoring curve at the point of
        incidence of the curve and the origin of
        subfigure.
        Similarly Z-axis is aligned.
        """

    def TemplateEntity(self) -> nanoocp.IGESBasic.IGESBasic_SubfigureDef:
        """returns SubfigureDef as the Entity used as Template figure."""

    def Distance(self) -> float:
        """
        returns the Distance between any two Template figures on the
        anchoring curve.
        """

    def Scale(self) -> float:
        """
        returns the Scaling factor applied to SubfigureDef to form
        Template figure.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_LineFontPredefined(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESLineFontPredefined, Type <406> Form <19>
    in package IGESGraph

    Provides the ability to specify a line font pattern
    from a predefined list rather than from
    Directory Entry Field 4
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph_LineFontPredefined) -> None: ...

    def Init(self, nbProps: int, aLineFontPatternCode: int) -> None:
        """
        This method is used to set the fields of the class
        LineFontPredefined
        - nbProps              : Number of property values (NP = 1)
        - aLineFontPatternCode : Line Font Pattern Code
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values in <me>"""

    def LineFontPatternCode(self) -> int:
        """returns the Line Font Pattern Code of <me>"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_NominalSize(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESNominalSize, Type <406> Form <13>
    in package IGESGraph

    Specifies a value, a name, and optionally a
    reference to an engineering standard
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph_NominalSize) -> None: ...

    def Init(self, nbProps: int, aNominalSizeValue: float, aNominalSizeName: nanoocp.TCollection.TCollection_HAsciiString | None, aStandardName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        This method is used to set the fields of the class
        NominalSize
        - nbProps           : Number of property values (2 or 3)
        - aNominalSizeValue : NominalSize Value
        - aNominalSizeName  : NominalSize Name
        - aStandardName     : Name of relevant engineering standard
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values in <me>"""

    def NominalSizeValue(self) -> float:
        """returns the value of <me>"""

    def NominalSizeName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns the name of <me>"""

    def HasStandardName(self) -> bool:
        """
        returns True if an engineering Standard is defined for <me>
        else, returns False
        """

    def StandardName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns the name of the relevant engineering standard of <me>"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_Pick(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESPick, Type <406> Form <21>
    in package IGESGraph

    Attaches information that an entity may be picked
    by whatever pick device is used in the receiving
    system
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph_Pick) -> None: ...

    def Init(self, nbProps: int, aPickStatus: int) -> None:
        """
        This method is used to set the fields of the class Pick
        - nbProps     : Number of property values (NP = 1)
        - aPickStatus : Pick Flag
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values in <me>."""

    def PickFlag(self) -> int:
        """
        returns 0 if <me> is pickable(default),
        1 if <me> is not pickable.
        """

    def IsPickable(self) -> bool:
        """returns True if thePick is 0."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_Protocol(nanoocp.IGESData.IGESData_Protocol):
    """Description of Protocol for IGESGraph"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph_Protocol) -> None: ...

    def NbResources(self) -> int:
        """
        Gives the count of Resource Protocol. Here, one
        (Protocol from IGESBasic)
        """

    def Resource(self, num: int) -> nanoocp.Interface.Interface_Protocol:
        """Returns a Resource, given a rank."""

    def TypeNumber(self, atype: nanoocp.Standard.Standard_Type | None) -> int:
        """
        Returns a Case Number, specific of each recognized Type
        This Case Number is then used in Libraries : the various
        Modules attached to this class of Protocol must use them
        in accordance (for a given value of TypeNumber, they must
        consider the same Type as the Protocol defines)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_ReadWriteModule(nanoocp.IGESData.IGESData_ReadWriteModule):
    """
    Defines Graph File Access Module for IGESGraph (specific parts)
    Specific actions concern : Read and Write Own Parameters of
    an IGESEntity.
    """

    @overload
    def __init__(self) -> None:
        """Creates a ReadWriteModule & puts it into ReaderLib & WriterLib"""

    @overload
    def __init__(self, theOther: IGESGraph_ReadWriteModule) -> None: ...

    def CaseIGES(self, typenum: int, formnum: int) -> int:
        """Defines Case Numbers for Entities of IGESGraph"""

    def ReadOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """Reads own parameters from file for an Entity of IGESGraph"""

    def WriteOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_SpecificModule(nanoocp.IGESData.IGESData_SpecificModule):
    """
    Defines Services attached to IGES Entities :
    Dump & OwnCorrect, for IGESGraph
    """

    @overload
    def __init__(self) -> None:
        """Creates a SpecificModule from IGESGraph & puts it into SpecificLib"""

    @overload
    def __init__(self, theOther: IGESGraph_SpecificModule) -> None: ...

    def OwnDump(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Specific Dump (own parameters) for IGESGraph"""

    def OwnCorrect(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None) -> bool:
        """
        Performs non-ambiguous Corrections on Entities which support
        them (DrawingSize,DrawingUnits,HighLight,IntercharacterSpacing,
        LineFontPredefined,NominalSize,Pick,UniformRectGrid)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_TextDisplayTemplate(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGES TextDisplayTemplate Entity,
    Type <312>, form <0, 1> in package IGESGraph

    Used to set parameters for display of information
    which has been logically included in another entity
    as a parameter value
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph_TextDisplayTemplate) -> None: ...

    def Init(self, aWidth: float, aHeight: float, aFontCode: int, aFontEntity: IGESGraph_TextFontDef | None, aSlantAngle: float, aRotationAngle: float, aMirrorFlag: int, aRotationFlag: int, aCorner: nanoocp.gp.gp_XYZ) -> None:
        """
        This method is used to set the fields of the class
        TextDisplayTemplate
        - aWidth         : Character box width
        - aHeight        : Character box height
        - afontCode      : Font code
        - aFontEntity    : Text Font Definition Entity
        - aSlantAngle    : Slant angle
        - aRotationAngle : Rotation angle
        - aMirrorFlag    : Mirror Flag
        - aRotationFlag  : Rotate internal text flag
        - aCorner        : Lower left corner coordinates(Form No. 0),
        Increments from coordinates (Form No. 1)
        """

    def SetIncremental(self, mode: bool) -> None:
        """
        Sets <me> to be Incremental (Form 1) if <mode> is True,
        or Basolute (Form 0) else
        """

    def IsIncremental(self) -> bool:
        """
        returns True if entity is Incremental (Form 1).
        False if entity is Absolute (Form 0).
        """

    def BoxWidth(self) -> float:
        """returns Character Box Width."""

    def BoxHeight(self) -> float:
        """returns Character Box Height."""

    def IsFontEntity(self) -> bool:
        """returns False if theFontEntity is Null, True otherwise."""

    def FontCode(self) -> int:
        """returns the font code."""

    def FontEntity(self) -> IGESGraph_TextFontDef:
        """returns Text Font Definition Entity used to define the font."""

    def SlantAngle(self) -> float:
        """returns slant angle of character in radians."""

    def RotationAngle(self) -> float:
        """returns Rotation angle of text block in radians."""

    def MirrorFlag(self) -> int:
        """
        returns Mirror flag
        Mirror flag : 0 = no mirroring.
        1 = mirror axis perpendicular to text base line.
        2 = mirror axis is text base line.
        """

    def RotateFlag(self) -> int:
        """
        returns Rotate internal text flag.
        Rotate internal text flag : 0 = text horizontal.
        1 = text vertical.
        """

    def StartingCorner(self) -> nanoocp.gp.gp_Pnt:
        """
        If IsIncremental() returns False,
        gets coordinates of lower left corner
        of first character box.
        If IsIncremental() returns True,
        gets increments from X, Y, Z coordinates
        found in parent entity.
        """

    def TransformedStartingCorner(self) -> nanoocp.gp.gp_Pnt:
        """
        If IsIncremental() returns False,
        gets coordinates of lower left corner
        of first character box.
        If IsIncremental() returns True,
        gets increments from X, Y, Z coordinates
        found in parent entity.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_TextFontDef(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGES Text Font Definition Entity, Type <310>
    in package IGESGraph

    Used to define the appearance of characters in a text font.
    It may be used to describe a complete font or a
    modification to a subset of characters in another font.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph_TextFontDef) -> None: ...

    def Init(self, aFontCode: int, aFontName: nanoocp.TCollection.TCollection_HAsciiString | None, aSupersededFont: int, aSupersededEntity: IGESGraph_TextFontDef | None, aScale: int, allASCIICodes: nanoocp.NCollection.NCollection_HArray1[int] | None, allNextCharX: nanoocp.NCollection.NCollection_HArray1[int] | None, allNextCharY: nanoocp.NCollection.NCollection_HArray1[int] | None, allPenMotions: nanoocp.NCollection.NCollection_HArray1[int] | None, allPenFlags: nanoocp.IGESBasic.IGESBasic_HArray1OfHArray1OfInteger | None, allMovePenToX: nanoocp.IGESBasic.IGESBasic_HArray1OfHArray1OfInteger | None, allMovePenToY: nanoocp.IGESBasic.IGESBasic_HArray1OfHArray1OfInteger | None) -> None:
        """
        This method is used to set the fields of the class
        TextFontDef
        - aFontCode         : Font Code
        - aFontName         : Font Name
        - aSupersededFont   : Number of superseded font
        - aSupersededEntity : Text Definition Entity
        - aScale            : No. of grid units = 1 text height unit
        - allASCIICodes     : ASCII codes for characters
        - allNextCharX & Y  : Grid locations of the next
        character's origin (Integer vals)
        - allPenMotions     : No. of pen motions for the characters
        - allPenFlags       : Pen up/down flags,
        0 = Down (default), 1 = Up
        - allMovePenToX & Y : Grid locations the pen will move to
        This method initializes the fields of the class TextFontDef.
        An exception is raised if the lengths of allASCIICodes,
        allNextChars, allPenMotions, allPenFlags and allMovePenTo
        are not same.
        """

    def FontCode(self) -> int:
        """returns the font code."""

    def FontName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns the font name."""

    def IsSupersededFontEntity(self) -> bool:
        """
        True if this definition supersedes another
        TextFontDefinition Entity,
        False if it supersedes value.
        """

    def SupersededFontCode(self) -> int:
        """returns the font number which this entity modifies."""

    def SupersededFontEntity(self) -> IGESGraph_TextFontDef:
        """returns the font entity which this entity modifies."""

    def Scale(self) -> int:
        """returns the number of grid units which equal one text height unit."""

    def NbCharacters(self) -> int:
        """returns the number of characters in this definition."""

    def ASCIICode(self, Chnum: int) -> int:
        """
        returns the ASCII code of Chnum'th character.
        Exception OutOfRange is raised if Chnum <= 0 or Chnum > NbCharacters
        """

    def NextCharOrigin(self, Chnum: int) -> tuple[int, int]:
        """
        returns grid location of origin of character next to Chnum'th char.
        Exception OutOfRange is raised if Chnum <= 0 or Chnum > NbCharacters
        """

    def NbPenMotions(self, Chnum: int) -> int:
        """
        returns number of pen motions for Chnum'th character.
        Exception OutOfRange is raised if Chnum <= 0 or Chnum > NbCharacters
        """

    def IsPenUp(self, Chnum: int, Motionnum: int) -> bool:
        """
        returns pen status(True if 1, False if 0) of Motionnum'th motion
        of Chnum'th character.
        Exception raised if Chnum <= 0 or Chnum > NbCharacters or
        Motionnum <= 0 or Motionnum > NbPenMotions
        """

    def NextPenPosition(self, Chnum: int, Motionnum: int) -> tuple[int, int]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGraph_ToolColor:
    """
    Tool to work on a Color. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolColor, ready to work"""

    @overload
    def __init__(self, theOther: IGESGraph_ToolColor) -> None: ...

    def ReadOwnParams(self, ent: IGESGraph_Color | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGraph_Color | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGraph_Color | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Color <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGraph_Color | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGraph_Color | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGraph_Color | None, entto: IGESGraph_Color | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGraph_Color | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGraph_ToolDefinitionLevel:
    """
    Tool to work on a DefinitionLevel. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolDefinitionLevel, ready to work"""

    @overload
    def __init__(self, theOther: IGESGraph_ToolDefinitionLevel) -> None: ...

    def ReadOwnParams(self, ent: IGESGraph_DefinitionLevel | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGraph_DefinitionLevel | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGraph_DefinitionLevel | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a DefinitionLevel <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGraph_DefinitionLevel | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGraph_DefinitionLevel | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGraph_DefinitionLevel | None, entto: IGESGraph_DefinitionLevel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGraph_DefinitionLevel | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGraph_ToolDrawingSize:
    """
    Tool to work on a DrawingSize. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolDrawingSize, ready to work"""

    @overload
    def __init__(self, theOther: IGESGraph_ToolDrawingSize) -> None: ...

    def ReadOwnParams(self, ent: IGESGraph_DrawingSize | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGraph_DrawingSize | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGraph_DrawingSize | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a DrawingSize <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESGraph_DrawingSize | None) -> bool:
        """
        Sets automatic unambiguous Correction on a DrawingSize
        (NbPropertyValues forced to 2)
        """

    def DirChecker(self, ent: IGESGraph_DrawingSize | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGraph_DrawingSize | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGraph_DrawingSize | None, entto: IGESGraph_DrawingSize | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGraph_DrawingSize | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGraph_ToolDrawingUnits:
    """
    Tool to work on a DrawingUnits. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolDrawingUnits, ready to work"""

    @overload
    def __init__(self, theOther: IGESGraph_ToolDrawingUnits) -> None: ...

    def ReadOwnParams(self, ent: IGESGraph_DrawingUnits | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGraph_DrawingUnits | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGraph_DrawingUnits | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a DrawingUnits <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESGraph_DrawingUnits | None) -> bool:
        """
        Sets automatic unambiguous Correction on a DrawingUnits
        (NbPropertyValues forced to 2)
        """

    def DirChecker(self, ent: IGESGraph_DrawingUnits | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGraph_DrawingUnits | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGraph_DrawingUnits | None, entto: IGESGraph_DrawingUnits | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGraph_DrawingUnits | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGraph_ToolHighLight:
    """
    Tool to work on a HighLight. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolHighLight, ready to work"""

    @overload
    def __init__(self, theOther: IGESGraph_ToolHighLight) -> None: ...

    def ReadOwnParams(self, ent: IGESGraph_HighLight | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGraph_HighLight | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGraph_HighLight | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a HighLight <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESGraph_HighLight | None) -> bool:
        """
        Sets automatic unambiguous Correction on a HighLight
        (NbPropertyValues forced to 1)
        """

    def DirChecker(self, ent: IGESGraph_HighLight | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGraph_HighLight | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGraph_HighLight | None, entto: IGESGraph_HighLight | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGraph_HighLight | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGraph_ToolIntercharacterSpacing:
    """
    Tool to work on a IntercharacterSpacing. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolIntercharacterSpacing, ready to work"""

    @overload
    def __init__(self, theOther: IGESGraph_ToolIntercharacterSpacing) -> None: ...

    def ReadOwnParams(self, ent: IGESGraph_IntercharacterSpacing | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGraph_IntercharacterSpacing | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGraph_IntercharacterSpacing | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a IntercharacterSpacing <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESGraph_IntercharacterSpacing | None) -> bool:
        """
        Sets automatic unambiguous Correction on a IntercharacterSpacing
        (NbPropertyValues forced to 1)
        """

    def DirChecker(self, ent: IGESGraph_IntercharacterSpacing | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGraph_IntercharacterSpacing | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGraph_IntercharacterSpacing | None, entto: IGESGraph_IntercharacterSpacing | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGraph_IntercharacterSpacing | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGraph_ToolLineFontDefPattern:
    """
    Tool to work on a LineFontDefPattern. Called by various
    Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolLineFontDefPattern, ready to work"""

    @overload
    def __init__(self, theOther: IGESGraph_ToolLineFontDefPattern) -> None: ...

    def ReadOwnParams(self, ent: IGESGraph_LineFontDefPattern | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGraph_LineFontDefPattern | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGraph_LineFontDefPattern | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a LineFontDefPattern <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGraph_LineFontDefPattern | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGraph_LineFontDefPattern | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGraph_LineFontDefPattern | None, entto: IGESGraph_LineFontDefPattern | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGraph_LineFontDefPattern | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGraph_ToolLineFontDefTemplate:
    """
    Tool to work on a LineFontDefTemplate. Called by various
    Modules (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolLineFontDefTemplate, ready to work"""

    @overload
    def __init__(self, theOther: IGESGraph_ToolLineFontDefTemplate) -> None: ...

    def ReadOwnParams(self, ent: IGESGraph_LineFontDefTemplate | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGraph_LineFontDefTemplate | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGraph_LineFontDefTemplate | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a LineFontDefTemplate <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGraph_LineFontDefTemplate | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGraph_LineFontDefTemplate | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGraph_LineFontDefTemplate | None, entto: IGESGraph_LineFontDefTemplate | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGraph_LineFontDefTemplate | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGraph_ToolLineFontPredefined:
    """
    Tool to work on a LineFontPredefined. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolLineFontPredefined, ready to work"""

    @overload
    def __init__(self, theOther: IGESGraph_ToolLineFontPredefined) -> None: ...

    def ReadOwnParams(self, ent: IGESGraph_LineFontPredefined | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGraph_LineFontPredefined | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGraph_LineFontPredefined | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a LineFontPredefined <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESGraph_LineFontPredefined | None) -> bool:
        """
        Sets automatic unambiguous Correction on a LineFontPredefined
        (NbPropertyValues forced to 1)
        """

    def DirChecker(self, ent: IGESGraph_LineFontPredefined | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGraph_LineFontPredefined | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGraph_LineFontPredefined | None, entto: IGESGraph_LineFontPredefined | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGraph_LineFontPredefined | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGraph_ToolNominalSize:
    """
    Tool to work on a NominalSize. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolNominalSize, ready to work"""

    @overload
    def __init__(self, theOther: IGESGraph_ToolNominalSize) -> None: ...

    def ReadOwnParams(self, ent: IGESGraph_NominalSize | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGraph_NominalSize | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGraph_NominalSize | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a NominalSize <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESGraph_NominalSize | None) -> bool:
        """
        Sets automatic unambiguous Correction on a NominalSize
        (NbPropertyValues forced to 2 or 3 according HasStandardName)
        """

    def DirChecker(self, ent: IGESGraph_NominalSize | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGraph_NominalSize | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGraph_NominalSize | None, entto: IGESGraph_NominalSize | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGraph_NominalSize | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGraph_ToolPick:
    """
    Tool to work on a Pick. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolPick, ready to work"""

    @overload
    def __init__(self, theOther: IGESGraph_ToolPick) -> None: ...

    def ReadOwnParams(self, ent: IGESGraph_Pick | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGraph_Pick | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGraph_Pick | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Pick <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESGraph_Pick | None) -> bool:
        """
        Sets automatic unambiguous Correction on a Pick
        (NbPropertyValues forced to 1)
        """

    def DirChecker(self, ent: IGESGraph_Pick | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGraph_Pick | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGraph_Pick | None, entto: IGESGraph_Pick | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGraph_Pick | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGraph_ToolTextDisplayTemplate:
    """
    Tool to work on a TextDisplayTemplate. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolTextDisplayTemplate, ready to work"""

    @overload
    def __init__(self, theOther: IGESGraph_ToolTextDisplayTemplate) -> None: ...

    def ReadOwnParams(self, ent: IGESGraph_TextDisplayTemplate | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGraph_TextDisplayTemplate | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGraph_TextDisplayTemplate | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a TextDisplayTemplate <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGraph_TextDisplayTemplate | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGraph_TextDisplayTemplate | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGraph_TextDisplayTemplate | None, entto: IGESGraph_TextDisplayTemplate | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGraph_TextDisplayTemplate | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGraph_ToolTextFontDef:
    """
    Tool to work on a TextFontDef. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolTextFontDef, ready to work"""

    @overload
    def __init__(self, theOther: IGESGraph_ToolTextFontDef) -> None: ...

    def ReadOwnParams(self, ent: IGESGraph_TextFontDef | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGraph_TextFontDef | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGraph_TextFontDef | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a TextFontDef <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGraph_TextFontDef | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGraph_TextFontDef | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGraph_TextFontDef | None, entto: IGESGraph_TextFontDef | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGraph_TextFontDef | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGraph_ToolUniformRectGrid:
    """
    Tool to work on a UniformRectGrid. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolUniformRectGrid, ready to work"""

    @overload
    def __init__(self, theOther: IGESGraph_ToolUniformRectGrid) -> None: ...

    def ReadOwnParams(self, ent: IGESGraph_UniformRectGrid | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGraph_UniformRectGrid | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGraph_UniformRectGrid | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a UniformRectGrid <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESGraph_UniformRectGrid | None) -> bool:
        """
        Sets automatic unambiguous Correction on a UniformRectGrid
        (NbPropertyValues forced to 9)
        """

    def DirChecker(self, ent: IGESGraph_UniformRectGrid | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGraph_UniformRectGrid | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGraph_UniformRectGrid | None, entto: IGESGraph_UniformRectGrid | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGraph_UniformRectGrid | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGraph_UniformRectGrid(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESUniformRectGrid, Type <406> Form <22>
    in package IGESGraph

    Stores sufficient information for the creation of
    a uniform rectangular grid within a drawing
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGraph_UniformRectGrid) -> None: ...

    def Init(self, nbProps: int, finite: int, line: int, weighted: int, aGridPoint: nanoocp.gp.gp_XY, aGridSpacing: nanoocp.gp.gp_XY, pointsX: int, pointsY: int) -> None:
        """
        This method is used to set the fields of the class
        UniformRectGrid
        - nbProps      : Number of property values (NP = 9)
        - finite       : Finite/Infinite grid flag
        - line         : Line/Point grid flag
        - weighted     : Weighted/Unweighted grid flag
        - aGridPoint   : Point on the grid
        - aGridSpacing : Grid spacing
        - pointsX      : No. of points/lines in X Direction
        - pointsY      : No. of points/lines in Y Direction
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values in <me>."""

    def IsFinite(self) -> bool:
        """
        returns False if <me> is an infinite grid,
        True if <me> is a finite grid.
        """

    def IsLine(self) -> bool:
        """
        returns False if <me> is a Point grid,
        True if <me> is a Line grid.
        """

    def IsWeighted(self) -> bool:
        """
        returns False if <me> is a Weighted grid,
        True if <me> is not a Weighted grid.
        """

    def GridPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """
        returns coordinates of lower left corner,
        if <me> is a finite grid,
        coordinates of an arbitrary point,
        if <me> is an infinite grid.
        """

    def GridSpacing(self) -> nanoocp.gp.gp_Vec2d:
        """returns the grid-spacing in drawing coordinates."""

    def NbPointsX(self) -> int:
        """
        returns the no. of points/lines in X direction
        (only applicable if IsFinite() = 1, i.e: a finite grid).
        """

    def NbPointsY(self) -> int:
        """
        returns the no. of points/lines in Y direction
        (only applicable if IsFinite() = 1, i.e: a finite grid).
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.IGESGraph
IGESGraph_Array1OfColor = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESGraph.IGESGraph_Color]
IGESGraph_Array1OfTextDisplayTemplate = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate]
IGESGraph_Array1OfTextFontDef = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESGraph.IGESGraph_TextFontDef]
IGESGraph_HArray1OfColor = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGraph.IGESGraph_Color]
IGESGraph_HArray1OfTextDisplayTemplate = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate]
IGESGraph_HArray1OfTextFontDef = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGraph.IGESGraph_TextFontDef]
