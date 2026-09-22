"""OCCT package IGESDimen (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.IGESData
import nanoocp.IGESGeom
import nanoocp.IGESGraph
import nanoocp.Interface
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.gp


class IGESDimen:
    """
    This package represents Entities applied to Dimensions
    ie. Annotation Entities and attached Properties and
    Associativities.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen) -> None: ...

    @staticmethod
    def Init() -> None:
        """Prepares dynamic data (Protocol, Modules) for this package"""

    @staticmethod
    def Protocol() -> IGESDimen_Protocol:
        """Returns the Protocol for this Package"""

class IGESDimen_AngularDimension(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines AngularDimension, Type <202> Form <0>
    in package IGESDimen
    Used to dimension angles
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_AngularDimension) -> None: ...

    def Init(self, aNote: IGESDimen_GeneralNote | None, aLine: IGESDimen_WitnessLine | None, anotherLine: IGESDimen_WitnessLine | None, aVertex: nanoocp.gp.gp_XY, aRadius: float, aLeader: IGESDimen_LeaderArrow | None, anotherLeader: IGESDimen_LeaderArrow | None) -> None:
        """
        This method is used to set the fields of the class
        AngularDimension
        - aNote         : General Note Entity
        - aLine         : First Witness Line Entity or Null
        Handle
        - anotherLine   : Second Witness Line Entity or Null
        Handle
        - aVertex       : Coordinates of vertex point
        - aRadius       : Radius of leader arcs
        - aLeader       : First Leader Entity
        - anotherLeader : Second Leader Entity
        """

    def Note(self) -> IGESDimen_GeneralNote:
        """returns the General Note Entity of the Dimension."""

    def HasFirstWitnessLine(self) -> bool:
        """returns False if theFirstWitnessLine is Null Handle."""

    def FirstWitnessLine(self) -> IGESDimen_WitnessLine:
        """returns the First Witness Line Entity or Null Handle."""

    def HasSecondWitnessLine(self) -> bool:
        """returns False if theSecondWitnessLine is Null Handle."""

    def SecondWitnessLine(self) -> IGESDimen_WitnessLine:
        """returns the Second Witness Line Entity or Null Handle."""

    def Vertex(self) -> nanoocp.gp.gp_Pnt2d:
        """returns the coordinates of the Vertex point as Pnt2d from gp."""

    def TransformedVertex(self) -> nanoocp.gp.gp_Pnt2d:
        """
        returns the coordinates of the Vertex point as Pnt2d from gp
        after Transformation. (Z = 0.0 for Transformation)
        """

    def Radius(self) -> float:
        """returns the Radius of the Leader arcs."""

    def FirstLeader(self) -> IGESDimen_LeaderArrow:
        """returns the First Leader Entity."""

    def SecondLeader(self) -> IGESDimen_LeaderArrow:
        """returns the Second Leader Entity."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_BasicDimension(nanoocp.IGESData.IGESData_IGESEntity):
    """
    Defines IGES Basic Dimension, Type 406, Form 31,
    in package IGESDimen
    The basic Dimension Property indicates that the referencing
    dimension entity is to be displayed with a box around text.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_BasicDimension) -> None: ...

    def Init(self, nbPropVal: int, lowerLeft: nanoocp.gp.gp_XY, lowerRight: nanoocp.gp.gp_XY, upperRight: nanoocp.gp.gp_XY, upperLeft: nanoocp.gp.gp_XY) -> None: ...

    def NbPropertyValues(self) -> int:
        """returns the number of properties = 8"""

    def LowerLeft(self) -> nanoocp.gp.gp_Pnt2d:
        """returns coordinates of lower left corner"""

    def LowerRight(self) -> nanoocp.gp.gp_Pnt2d:
        """returns coordinates of lower right corner"""

    def UpperRight(self) -> nanoocp.gp.gp_Pnt2d:
        """returns coordinates of upper right corner"""

    def UpperLeft(self) -> nanoocp.gp.gp_Pnt2d:
        """returns coordinates of upper left corner"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_CenterLine(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines CenterLine, Type <106> Form <20-21>
    in package IGESDimen
    Is an entity appearing as crosshairs or as a
    construction between 2 positions
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_CenterLine) -> None: ...

    def Init(self, aDataType: int, aZdisp: float, dataPnts: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XY] | None) -> None:
        """
        This method is used to set the fields of the class
        CenterLine
        - aDataType      : Interpretation Flag, always = 1
        - aZDisplacement : Common z displacement
        - dataPnts       : Data points (x and y)
        """

    def SetCrossHair(self, mode: bool) -> None:
        """Sets FormNumber to 20 if <mode> is True, 21 else"""

    def Datatype(self) -> int:
        """returns Interpretation Flag : IP = 1."""

    def NbPoints(self) -> int:
        """returns Number of Data Points."""

    def ZDisplacement(self) -> float:
        """returns Common Z displacement."""

    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        returns the data point as Pnt from gp.
        raises exception if Index <= 0 or Index > NbPoints()
        """

    def TransformedPoint(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        returns the data point as Pnt from gp after Transformation.
        raises exception if Index <= 0 or Index > NbPoints()
        """

    def IsCrossHair(self) -> bool:
        """returns True if Form is 20."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_CurveDimension(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines CurveDimension, Type <204> Form <0>
    in package IGESDimen
    Used to dimension curves
    Consists of one tail segment of nonzero length
    beginning with an arrowhead and which serves to define
    the orientation
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_CurveDimension) -> None: ...

    def Init(self, aNote: IGESDimen_GeneralNote | None, aCurve: nanoocp.IGESData.IGESData_IGESEntity | None, anotherCurve: nanoocp.IGESData.IGESData_IGESEntity | None, aLeader: IGESDimen_LeaderArrow | None, anotherLeader: IGESDimen_LeaderArrow | None, aLine: IGESDimen_WitnessLine | None, anotherLine: IGESDimen_WitnessLine | None) -> None:
        """
        This method is used to set the fields of the class
        CurveDimension
        - aNote         : General Note Entity
        - aCurve        : First Curve Entity
        - anotherCurve  : Second Curve Entity or a Null Handle
        - aLeader       : First Leader Entity
        - anotherLeader : Second Leader Entity
        - aLine         : First Witness Line Entity or a Null
        Handle
        - anotherLine   : Second Witness Line Entity or a Null
        Handle
        """

    def Note(self) -> IGESDimen_GeneralNote:
        """returns the General Note Entity"""

    def FirstCurve(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the First curve Entity"""

    def HasSecondCurve(self) -> bool:
        """returns False if theSecondCurve is a Null Handle."""

    def SecondCurve(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the Second curve Entity or a Null Handle."""

    def FirstLeader(self) -> IGESDimen_LeaderArrow:
        """returns the First Leader Entity"""

    def SecondLeader(self) -> IGESDimen_LeaderArrow:
        """returns the Second Leader Entity"""

    def HasFirstWitnessLine(self) -> bool:
        """returns False if theFirstWitnessLine is a Null Handle."""

    def FirstWitnessLine(self) -> IGESDimen_WitnessLine:
        """returns the First Witness Line Entity or a Null Handle."""

    def HasSecondWitnessLine(self) -> bool:
        """returns False if theSecondWitnessLine is a Null Handle."""

    def SecondWitnessLine(self) -> IGESDimen_WitnessLine:
        """returns the Second Witness Line Entity or a Null Handle."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_DiameterDimension(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines DiameterDimension, Type <206> Form <0>
    in package IGESDimen
    Used for dimensioning diameters
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_DiameterDimension) -> None: ...

    def Init(self, aNote: IGESDimen_GeneralNote | None, aLeader: IGESDimen_LeaderArrow | None, anotherLeader: IGESDimen_LeaderArrow | None, aCenter: nanoocp.gp.gp_XY) -> None:
        """
        This method is used to set the fields of the class
        DiameterDimension
        - aNote         : General Note Entity
        - aLeader       : First Leader Entity
        - anotherLeader : Second Leader Entity or a Null Handle.
        - aCenter       : Arc center coordinates
        """

    def Note(self) -> IGESDimen_GeneralNote:
        """returns the General Note Entity"""

    def FirstLeader(self) -> IGESDimen_LeaderArrow:
        """returns the First Leader Entity"""

    def HasSecondLeader(self) -> bool:
        """returns False if theSecondleader is a Null Handle."""

    def SecondLeader(self) -> IGESDimen_LeaderArrow:
        """returns the Second Leader Entity"""

    def Center(self) -> nanoocp.gp.gp_Pnt2d:
        """returns the Arc Center coordinates as Pnt2d from package gp"""

    def TransformedCenter(self) -> nanoocp.gp.gp_Pnt2d:
        """
        returns the Arc Center coordinates as Pnt2d from package gp
        after Transformation. (Z = 0.0 for Transformation)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_DimensionDisplayData(nanoocp.IGESData.IGESData_IGESEntity):
    """
    Defines IGES Dimension Display Data, Type <406> Form <30>,
    in package IGESDimen
    The Dimensional Display Data Property is optional but when
    present must be referenced by a dimension entity.
    The information it contains could be extracted from the text,
    leader and witness line data with difficulty.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_DimensionDisplayData) -> None: ...

    def Init(self, numProps: int, aDimType: int, aLabelPos: int, aCharSet: int, aString: nanoocp.TCollection.TCollection_HAsciiString | None, aSymbol: int, anAng: float, anAlign: int, aLevel: int, aPlace: int, anOrient: int, initVal: float, notes: nanoocp.NCollection.NCollection_HArray1[int] | None, startInd: nanoocp.NCollection.NCollection_HArray1[int] | None, endInd: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None: ...

    def NbPropertyValues(self) -> int:
        """returns the number of property values (14)"""

    def DimensionType(self) -> int:
        """returns the dimension type"""

    def LabelPosition(self) -> int:
        """returns the preferred label position"""

    def CharacterSet(self) -> int:
        """returns the character set interpretation"""

    def LString(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns e.g., 8HDIAMETER"""

    def DecimalSymbol(self) -> int: ...

    def WitnessLineAngle(self) -> float:
        """returns the witness line angle in radians"""

    def TextAlignment(self) -> int:
        """returns the text alignment"""

    def TextLevel(self) -> int:
        """returns the text level"""

    def TextPlacement(self) -> int:
        """returns the preferred text placement"""

    def ArrowHeadOrientation(self) -> int:
        """returns the arrowhead orientation"""

    def InitialValue(self) -> float:
        """returns the primary dimension initial value"""

    def NbSupplementaryNotes(self) -> int:
        """returns the number of supplementary notes or zero"""

    def SupplementaryNote(self, Index: int) -> int:
        """
        returns the Index'th supplementary note
        raises exception if Index <= 0 or Index > NbSupplementaryNotes()
        """

    def StartIndex(self, Index: int) -> int:
        """
        returns the Index'th note start index
        raises exception if Index <= 0 or Index > NbSupplementaryNotes()
        """

    def EndIndex(self, Index: int) -> int:
        """
        returns the Index'th note end index
        raises exception if Index <= 0 or Index > NbSupplemetaryNotes()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_DimensionedGeometry(nanoocp.IGESData.IGESData_IGESEntity):
    """
    Defines IGES Dimensioned Geometry, Type <402> Form <13>,
    in package IGESDimen
    This entity has been replaced by the new form of Dimensioned
    Geometry Associativity Entity (Type 402, Form 21) and should no
    longer be used by preprocessors.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_DimensionedGeometry) -> None: ...

    def Init(self, nbDims: int, aDimension: nanoocp.IGESData.IGESData_IGESEntity | None, entities: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None: ...

    def NbDimensions(self) -> int:
        """returns the number of dimensions"""

    def NbGeometryEntities(self) -> int:
        """returns the number of associated geometry entities"""

    def DimensionEntity(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the Dimension entity"""

    def GeometryEntity(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the num'th Geometry entity
        raises exception if Index <= 0 or Index > NbGeometryEntities()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_DimensionTolerance(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines Dimension Tolerance, Type <406>, Form <29>
    in package IGESDimen
    Provides tolerance information for a dimension which
    can be used by the receiving system to regenerate the
    dimension.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_DimensionTolerance) -> None: ...

    def Init(self, nbPropVal: int, aSecTolFlag: int, aTolType: int, aTolPlaceFlag: int, anUpperTol: float, aLowerTol: float, aSignFlag: bool, aFracFlag: int, aPrecision: int) -> None:
        """
        This method is used to set the fields of the class
        DimensionTolerance
        - nbPropVal     : Number of property values, default = 8
        - aSecTolFlag   : Secondary Tolerance Flag
        0 = Applies to primary dimension
        1 = Applies to secondary dimension
        2 = Display values as fractions
        - aTolType      : Tolerance Type
        1  = Bilateral
        2  = Upper/Lower
        3  = Unilateral Upper
        4  = Unilateral Lower
        5  = Range - min before max
        6  = Range - min after max
        7  = Range - min above max
        8  = Range - min below max
        9  = Nominal + Range - min above max
        10 = Nominal + Range - min below max
        - aTolPlaceFlag : Tolerance Placement Flag
        1 = Before nominal value
        2 = After nominal value
        3 = Above nominal value
        4 = Below nominal value
        - anUpperTol    : Upper Tolerance
        - aLowerTol     : Lower Tolerance
        - aSignFlag     : Sign Suppression Flag
        - aFracFlag     : Fraction Flag
        0 = Display values as decimal numbers
        1 = Display values as mixed fractions
        2 = Display values as fractions
        - aPrecision    : Precision Value
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values, always = 8"""

    def SecondaryToleranceFlag(self) -> int:
        """returns the Secondary Tolerance Flag"""

    def ToleranceType(self) -> int:
        """returns the Tolerance Type"""

    def TolerancePlacementFlag(self) -> int:
        """returns the Tolerance Placement Flag, default = 2"""

    def UpperTolerance(self) -> float:
        """returns the Upper or Bilateral Tolerance Value"""

    def LowerTolerance(self) -> float:
        """returns the Lower Tolerance Value"""

    def SignSuppressionFlag(self) -> bool:
        """returns the Sign Suppression Flag"""

    def FractionFlag(self) -> int:
        """returns the Fraction Flag"""

    def Precision(self) -> int:
        """returns the Precision for Value Display"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_DimensionUnits(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines Dimension Units, Type <406>, Form <28>
    in package IGESDimen
    Describes the units and formatting details of the
    nominal value of a dimension.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_DimensionUnits) -> None: ...

    def Init(self, nbPropVal: int, aSecondPos: int, aUnitsInd: int, aCharSet: int, aFormat: nanoocp.TCollection.TCollection_HAsciiString | None, aFracFlag: int, aPrecision: int) -> None:
        """
        This method is used to set the fields of the class
        DimensionUnits
        - nbPropVal  : Number of property values, always = 6
        - aSecondPos : Secondary Dimension Position
        0 = This is the main text
        1 = Before primary dimension
        2 = After primary dimension
        3 = Above primary dimension
        4 = Below primary dimension
        - aUnitsInd  : Units Indicator
        - aCharSet   : Character Set used
        - aFormat    : Format HAsciiString
        1 = Standard ASCII
        1001 = Symbol Font 1
        1002 = Symbol Font 2
        1003 = Drafting Font
        - aFracFlag  : Fraction Flag
        0 = Display values as decimal numbers
        1 = Display values as fractions
        - aPrecision : Precision Value
        """

    def NbPropertyValues(self) -> int:
        """returns the number of property values"""

    def SecondaryDimenPosition(self) -> int:
        """returns position of secondary dimension w.r.t. primary dimension"""

    def UnitsIndicator(self) -> int:
        """returns the units indicator"""

    def CharacterSet(self) -> int:
        """returns the character set interpretation"""

    def FormatString(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns the string used in formatting value"""

    def FractionFlag(self) -> int:
        """returns the fraction flag"""

    def PrecisionOrDenominator(self) -> int:
        """
        returns the precision/denominator
        number of decimal places when FractionFlag() = 0
        denominator of fraction when FractionFlag() = 1
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_LeaderArrow(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines LeaderArrow, Type <214> Form <1-12>
    in package IGESDimen
    Consists of one or more line segments except when
    leader is part of an angular dimension, with links to
    presumed text item
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_LeaderArrow) -> None: ...

    def Init(self, height: float, width: float, depth: float, position: nanoocp.gp.gp_XY, segments: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XY] | None) -> None:
        """
        This method is used to set the fields of the class
        LeaderArrow
        - height      : ArrowHead height
        - width       : ArrowHead width
        - depth       : Z Depth
        - position    : ArrowHead coordinates
        - segments    : Segment tail coordinate pairs
        """

    def SetFormNumber(self, form: int) -> None:
        """
        Changes FormNumber (indicates the Shape of the Arrow)
        Error if not in range [0-12]
        """

    def NbSegments(self) -> int:
        """returns number of segments"""

    def ArrowHeadHeight(self) -> float:
        """returns ArrowHead height"""

    def ArrowHeadWidth(self) -> float:
        """returns ArrowHead width"""

    def ZDepth(self) -> float:
        """returns Z depth"""

    def ArrowHead(self) -> nanoocp.gp.gp_Pnt2d:
        """returns ArrowHead coordinates"""

    def TransformedArrowHead(self) -> nanoocp.gp.gp_Pnt:
        """returns ArrowHead coordinates after Transformation"""

    def SegmentTail(self, Index: int) -> nanoocp.gp.gp_Pnt2d:
        """
        returns segment tail coordinates.
        raises exception if Index <= 0 or Index > NbSegments
        """

    def TransformedSegmentTail(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        returns segment tail coordinates after Transformation.
        raises exception if Index <= 0 or Index > NbSegments
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_FlagNote(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines FlagNote, Type <208> Form <0>
    in package IGESDimen
    Is label information formatted in different ways
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_FlagNote) -> None: ...

    def Init(self, leftCorner: nanoocp.gp.gp_XYZ, anAngle: float, aNote: IGESDimen_GeneralNote | None, someLeaders: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESDimen.IGESDimen_LeaderArrow] | None) -> None:
        """
        This method is used to set the fields of the class
        FlagNote
        - leftCorner  : Lower left corner of the Flag
        - anAngle     : Rotation angle in radians
        - aNote       : General Note Entity
        - someLeaders : Leader Entities
        """

    def LowerLeftCorner(self) -> nanoocp.gp.gp_Pnt:
        """returns Lower Left coordinate of Flag as Pnt from package gp"""

    def TransformedLowerLeftCorner(self) -> nanoocp.gp.gp_Pnt:
        """
        returns Lower Left coordinate of Flag as Pnt from package gp
        after Transformation.
        """

    def Angle(self) -> float:
        """returns Rotation angle in radians"""

    def Note(self) -> IGESDimen_GeneralNote:
        """returns General Note Entity"""

    def NbLeaders(self) -> int:
        """returns number of Arrows (Leaders) or zero"""

    def Leader(self, Index: int) -> IGESDimen_LeaderArrow:
        """
        returns Leader Entity
        raises exception if Index <= 0 or Index > NbLeaders()
        """

    def Height(self) -> float:
        """
        returns Height computed by the formula :
        Height = 2 * CH   where CH is from theNote
        """

    def CharacterHeight(self) -> float:
        """returns the Character Height (from General Note)"""

    def Length(self) -> float:
        """
        returns Length computed by the formula :
        Length = TW + 0.4*CH  where CH is from theNote
        and TW is from theNote
        """

    def TextWidth(self) -> float:
        """returns the Text Width (from General Note)"""

    def TipLength(self) -> float:
        """
        returns TipLength computed by the formula :
        TipLength = 0.5 * H / tan 35(deg)  where H is Height()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_GeneralLabel(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines GeneralLabel, Type <210> Form <0>
    in package IGESDimen
    Used for general labeling with leaders
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_GeneralLabel) -> None: ...

    def Init(self, aNote: IGESDimen_GeneralNote | None, someLeaders: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESDimen.IGESDimen_LeaderArrow] | None) -> None:
        """
        This method is used to set the fields of the class
        GeneralLabel
        - aNote       : General Note Entity
        - someLeaders : Associated Leader Entities
        """

    def Note(self) -> IGESDimen_GeneralNote:
        """returns General Note Entity"""

    def NbLeaders(self) -> int:
        """returns Number of Leaders"""

    def Leader(self, Index: int) -> IGESDimen_LeaderArrow:
        """
        returns Leader Entity
        raises exception if Index <= 0 or Index > NbLeaders()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_GeneralModule(nanoocp.IGESData.IGESData_GeneralModule):
    """
    Definition of General Services for IGESDimen (specific part)
    This Services comprise : Shared & Implied Lists, Copy, Check
    """

    @overload
    def __init__(self) -> None:
        """Creates a GeneralModule from IGESDimen and puts it into GeneralLib"""

    @overload
    def __init__(self, theOther: IGESDimen_GeneralModule) -> None: ...

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

class IGESDimen_GeneralNote(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines GeneralNote, Type <212> Form <0-8, 100-200, 105>
    in package IGESDimen
    Used for formatting boxed text in different ways
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_GeneralNote) -> None: ...

    def Init(self, nbChars: nanoocp.NCollection.NCollection_HArray1[int] | None, widths: nanoocp.NCollection.NCollection_HArray1[float] | None, heights: nanoocp.NCollection.NCollection_HArray1[float] | None, fontCodes: nanoocp.NCollection.NCollection_HArray1[int] | None, fonts: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGraph.IGESGraph_TextFontDef] | None, slants: nanoocp.NCollection.NCollection_HArray1[float] | None, rotations: nanoocp.NCollection.NCollection_HArray1[float] | None, mirrorFlags: nanoocp.NCollection.NCollection_HArray1[int] | None, rotFlags: nanoocp.NCollection.NCollection_HArray1[int] | None, start: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ] | None, texts: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None:
        """
        This method is used to set the fields of the class
        GeneralNote
        - nNbChars      : number of chars strings
        - widths        : Box widths
        - heights       : Box heights
        - fontCodes     : Font codes, default = 1
        - fonts         : Text Font Definition Entities
        - slants        : Slant angles in radians
        - rotations     : Rotation angles in radians
        - mirrorFlags   : Mirror flags
        - rotFlags      : Rotation internal text flags
        - start         : Text start points
        - texts         : Text strings
        raises exception if there is mismatch between the various
        Array Lengths.
        """

    def SetFormNumber(self, form: int) -> None:
        """
        Changes FormNumber (indicates Graphical Representation)
        Error if not in ranges [0-8] or [100-102] or 105
        """

    def NbStrings(self) -> int:
        """returns number of text strings in General Note"""

    def NbCharacters(self, Index: int) -> int:
        """
        returns number of characters of string or zero
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def BoxWidth(self, Index: int) -> float:
        """
        returns Box width of string
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def BoxHeight(self, Index: int) -> float:
        """
        returns Box height of string
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def IsFontEntity(self, Index: int) -> bool:
        """
        returns False if Value, True if Entity
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def FontCode(self, Index: int) -> int:
        """
        returns Font code (default = 1) of string
        returns 0 if IsFontEntity () is True
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def FontEntity(self, Index: int) -> nanoocp.IGESGraph.IGESGraph_TextFontDef:
        """
        returns Text Font Definition Entity of string
        returns a Null Handle if IsFontEntity () returns False
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def SlantAngle(self, Index: int) -> float:
        """
        returns Slant angle of string in radians
        default value = PI/2
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def RotationAngle(self, Index: int) -> float:
        """
        returns Rotation angle of string in radians
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def MirrorFlag(self, Index: int) -> int:
        """
        returns Mirror Flag of string
        0 = no mirroring
        1 = mirror axis is perpendicular to the text base line
        2 = mirror axis is text base line
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def RotateFlag(self, Index: int) -> int:
        """
        returns Rotate internal text Flag of string
        0 = text horizontal
        1 = text vertical
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def StartPoint(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        returns text start point of Index'th string
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def TransformedStartPoint(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        returns text start point of Index'th string after Transformation
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def ZDepthStartPoint(self, Index: int) -> float:
        """
        returns distance from Start Point plane of string
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def Text(self, Index: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns text string
        raises exception if Index <= 0 or Index > NbStrings()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_GeneralSymbol(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines General Symbol, Type <228>, Form <0-3,5001-9999>
    in package IGESDimen
    Consists of zero or one (Form 0) or one (all other
    forms), one or more geometry entities which define
    a symbol, and zero, one or more associated leaders.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_GeneralSymbol) -> None: ...

    def Init(self, aNote: IGESDimen_GeneralNote | None, allGeoms: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None, allLeaders: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESDimen.IGESDimen_LeaderArrow] | None) -> None:
        """
        This method is used to set the fields of the class
        GeneralSymbol
        - aNote      : General Note, null for form 0
        - allGeoms   : Geometric Entities
        - allLeaders : Leader Arrows
        """

    def SetFormNumber(self, form: int) -> None:
        """
        Changes FormNumber (indicates the Nature of the Symbol)
        Error if not in ranges [0-3] or [> 5000]
        """

    def HasNote(self) -> bool:
        """returns True if there is associated General Note Entity"""

    def Note(self) -> IGESDimen_GeneralNote:
        """returns Null handle for form 0 only"""

    def NbGeomEntities(self) -> int:
        """returns number of Geometry Entities"""

    def GeomEntity(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the Index'th Geometry Entity
        raises exception if Index <= 0 or Index > NbGeomEntities()
        """

    def NbLeaders(self) -> int:
        """returns number of Leaders or zero if not specified"""

    def LeaderArrow(self, Index: int) -> IGESDimen_LeaderArrow:
        """
        returns the Index'th Leader Arrow
        raises exception if Index <= 0 or Index > NbLeaders()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_LinearDimension(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines LinearDimension, Type <216> Form <0>
    in package IGESDimen
    Used for linear dimensioning
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_LinearDimension) -> None: ...

    def Init(self, aNote: IGESDimen_GeneralNote | None, aLeader: IGESDimen_LeaderArrow | None, anotherLeader: IGESDimen_LeaderArrow | None, aWitness: IGESDimen_WitnessLine | None, anotherWitness: IGESDimen_WitnessLine | None) -> None:
        """
        This method is used to set the fields of the class
        LinearDimension
        - aNote          : General Note Entity
        - aLeader        : First Leader Entity
        - anotherLeader  : Second Leader Entity
        - aWitness       : First Witness Line Entity or a Null
        Handle
        - anotherWitness : Second Witness Line Entity or a Null
        Handle
        """

    def SetFormNumber(self, form: int) -> None:
        """
        Changes FormNumber (indicates the Nature of the Dimension
        Unspecified, Diameter or Radius)
        Error if not in range [0-2]
        """

    def Note(self) -> IGESDimen_GeneralNote:
        """returns General Note Entity"""

    def FirstLeader(self) -> IGESDimen_LeaderArrow:
        """returns first Leader Entity"""

    def SecondLeader(self) -> IGESDimen_LeaderArrow:
        """returns second Leader Entity"""

    def HasFirstWitness(self) -> bool:
        """returns False if no first witness line"""

    def FirstWitness(self) -> IGESDimen_WitnessLine:
        """returns first Witness Line Entity or a Null Handle"""

    def HasSecondWitness(self) -> bool:
        """returns False if no second witness line"""

    def SecondWitness(self) -> IGESDimen_WitnessLine:
        """returns second Witness Line Entity or a Null Handle"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_NewDimensionedGeometry(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines New Dimensioned Geometry, Type <402>, Form <21>
    in package IGESDimen
    Links a dimension entity with the geometry entities it
    is dimensioning, so that later, in the receiving
    database, the dimension can be automatically recalculated
    and redrawn should the geometry be changed.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_NewDimensionedGeometry) -> None: ...

    def Init(self, nbDimens: int, aDimen: nanoocp.IGESData.IGESData_IGESEntity | None, anOrientation: int, anAngle: float, allEntities: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None, allLocations: nanoocp.NCollection.NCollection_HArray1[int] | None, allPoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ] | None) -> None:
        """
        This method is used to set the fields of the class
        NewDimensionedGeometry
        - nbDimen       : Number of Dimensions, default = 1
        - aDimen        : Dimension Entity
        - anOrientation : Dimension Orientation Flag
        - anAngle       : Angle Value
        - allEntities   : Geometric Entities
        - allLocations  : Dimension Location Flags
        - allPoints     : Points on the Geometry Entities
        exception raised if lengths of entities, locations, points
        are not the same
        """

    def NbDimensions(self) -> int:
        """returns the number of dimensions"""

    def NbGeometries(self) -> int:
        """returns the number of associated geometry entities"""

    def DimensionEntity(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the dimension entity"""

    def DimensionOrientationFlag(self) -> int:
        """returns the dimension orientation flag"""

    def AngleValue(self) -> float:
        """returns the angle value"""

    def GeometryEntity(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the Index'th geometry entity
        raises exception if Index <= 0 or Index > NbGeometries()
        """

    def DimensionLocationFlag(self, Index: int) -> int:
        """
        returns the Index'th geometry entity's dimension location flag
        raises exception if Index <= 0 or Index > NbGeometries()
        """

    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        coordinate of point on Index'th geometry entity
        raises exception if Index <= 0 or Index > NbGeometries()
        """

    def TransformedPoint(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        coordinate of point on Index'th geometry entity after Transformation
        raises exception if Index <= 0 or Index > NbGeometries()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_NewGeneralNote(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines NewGeneralNote, Type <213> Form <0>
    in package IGESDimen
    Further attributes for formatting text strings
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_NewGeneralNote) -> None: ...

    def Init(self, width: float, height: float, justifyCode: int, areaLoc: nanoocp.gp.gp_XYZ, areaRotationAngle: float, baseLinePos: nanoocp.gp.gp_XYZ, normalInterlineSpace: float, charDisplays: nanoocp.NCollection.NCollection_HArray1[int] | None, charWidths: nanoocp.NCollection.NCollection_HArray1[float] | None, charHeights: nanoocp.NCollection.NCollection_HArray1[float] | None, interCharSpc: nanoocp.NCollection.NCollection_HArray1[float] | None, interLineSpc: nanoocp.NCollection.NCollection_HArray1[float] | None, fontStyles: nanoocp.NCollection.NCollection_HArray1[int] | None, charAngles: nanoocp.NCollection.NCollection_HArray1[float] | None, controlCodeStrings: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None, nbChars: nanoocp.NCollection.NCollection_HArray1[int] | None, boxWidths: nanoocp.NCollection.NCollection_HArray1[float] | None, boxHeights: nanoocp.NCollection.NCollection_HArray1[float] | None, charSetCodes: nanoocp.NCollection.NCollection_HArray1[int] | None, charSetEntities: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None, slAngles: nanoocp.NCollection.NCollection_HArray1[float] | None, rotAngles: nanoocp.NCollection.NCollection_HArray1[float] | None, mirrorFlags: nanoocp.NCollection.NCollection_HArray1[int] | None, rotateFlags: nanoocp.NCollection.NCollection_HArray1[int] | None, startPoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ] | None, texts: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None:
        """
        This method is used to set the fields of the class
        NewGeneralNote
        - width                : Width of text containment area
        - height               : Height of text containment area
        - justifyCode          : Justification code
        - areaLoc              : Text containment area location
        - areaRotationAngle    : Text containment area rotation
        - baseLinePos          : Base line position
        - normalInterlineSpace : Normal interline spacing
        - charDisplays         : Character display type
        - charWidths           : Character width
        - charHeights          : Character height
        - interCharSpc         : Intercharacter spacing
        - interLineSpc         : Interline spacing
        - fontStyles           : Font style
        - charAngles           : Character angle
        - controlCodeStrings   : Control Code string
        - nbChars              : Number of characters in string
        - boxWidths            : Box width
        - boxHeights           : Box height
        - charSetCodes         : Character Set Interpretation
        - charSetEntities      : Character Set Font
        - slAngles             : Slant angle of text in radians
        - rotAngles            : Rotation angle of text in radians
        - mirrorFlags          : Type of mirroring
        - rotateFlags          : Rotate internal text flag
        - startPoints          : Text start point
        - texts                : Text strings
        raises exception if there is mismatch between the various
        Array Lengths.
        """

    def TextWidth(self) -> float:
        """returns width of text containment area of all strings in the note"""

    def TextHeight(self) -> float:
        """returns height of text containment area of all strings in the note"""

    def JustifyCode(self) -> int:
        """
        returns Justification code of all strings within the note
        0 = no justification
        1 = right justified
        2 = center justified
        3 = left justified
        """

    def AreaLocation(self) -> nanoocp.gp.gp_Pnt:
        """returns Text containment area Location point"""

    def TransformedAreaLocation(self) -> nanoocp.gp.gp_Pnt:
        """returns Text containment area Location point after Transformation"""

    def ZDepthAreaLocation(self) -> float:
        """returns distance from the containment area plane"""

    def AreaRotationAngle(self) -> float:
        """returns rotation angle of text containment area in radians"""

    def BaseLinePosition(self) -> nanoocp.gp.gp_Pnt:
        """returns position of first base line"""

    def TransformedBaseLinePosition(self) -> nanoocp.gp.gp_Pnt:
        """returns position of first base line after Transformation"""

    def ZDepthBaseLinePosition(self) -> float:
        """returns distance from the Base line position plane"""

    def NormalInterlineSpace(self) -> float:
        """returns Normal Interline Spacing"""

    def NbStrings(self) -> int:
        """returns number of text HAsciiStrings"""

    def CharacterDisplay(self, Index: int) -> int:
        """
        returns Fixed/Variable width character display of string
        0 = Fixed
        1 = Variable
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def IsVariable(self, Index: int) -> bool:
        """
        returns False if Character display width is Fixed
        optional method, if required
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def CharacterWidth(self, Index: int) -> float:
        """
        returns Character Width of string
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def CharacterHeight(self, Index: int) -> float:
        """
        returns Character Height of string
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def InterCharacterSpace(self, Index: int) -> float:
        """
        returns Inter-character spacing of string
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def InterlineSpace(self, Index: int) -> float:
        """
        returns Interline spacing of string
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def FontStyle(self, Index: int) -> int:
        """
        returns FontStyle of string
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def CharacterAngle(self, Index: int) -> float:
        """
        returns CharacterAngle of string
        Angle returned will be between 0 and 2PI
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def ControlCodeString(self, Index: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns ControlCodeString of string
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def NbCharacters(self, Index: int) -> int:
        """
        returns number of characters in string or zero
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def BoxWidth(self, Index: int) -> float:
        """
        returns Box width of string
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def BoxHeight(self, Index: int) -> float:
        """
        returns Box height of string
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def IsCharSetEntity(self, Index: int) -> bool:
        """
        returns False if Value, True if Pointer (Entity)
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def CharSetCode(self, Index: int) -> int:
        """
        returns Character Set Interpretation (default = 1) of string
        returns 0 if IsCharSetEntity () is True
        1 = Standard ASCII
        1001 = Symbol Font1
        1002 = Symbol Font2
        1003 = Symbol Font3
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def CharSetEntity(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns Character Set Interpretation of string
        returns a Null Handle if IsCharSetEntity () is False
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def SlantAngle(self, Index: int) -> float:
        """
        returns Slant angle of string in radians
        default value = PI/2
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def RotationAngle(self, Index: int) -> float:
        """
        returns Rotation angle of string in radians
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def MirrorFlag(self, Index: int) -> int:
        """
        returns Mirror Flag of string
        0 = no mirroring
        1 = mirror axis is perpendicular to the text base line
        2 = mirror axis is text base line
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def IsMirrored(self, Index: int) -> bool:
        """
        returns False if MirrorFlag = 0. ie. no mirroring
        else returns True
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def RotateFlag(self, Index: int) -> int:
        """
        returns Rotate internal text Flag of string
        0 = text horizontal
        1 = text vertical
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def StartPoint(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        returns text start point of string
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def TransformedStartPoint(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        returns text start point of string after Transformation
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def ZDepthStartPoint(self, Index: int) -> float:
        """
        returns distance from the start point plane
        raises exception if Index <= 0 or Index > NbStrings()
        """

    def Text(self, Index: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        returns text string
        raises exception if Index <= 0 or Index > NbStrings()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_OrdinateDimension(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGES Ordinate Dimension, Type <218> Form <0, 1>,
    in package IGESDimen
    Note: The ordinate dimension entity is used to
    indicate dimensions from a common base line.
    Dimensioning is only permitted along the XT
    or YT axis.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_OrdinateDimension) -> None: ...

    def Init(self, aNote: IGESDimen_GeneralNote | None, aType: bool, aLine: IGESDimen_WitnessLine | None, anArrow: IGESDimen_LeaderArrow | None) -> None: ...

    def IsLine(self) -> bool:
        """returns True if Witness Line and False if Leader (only for Form 0)"""

    def IsLeader(self) -> bool:
        """returns True if Leader and False if Witness Line (only for Form 0)"""

    def Note(self) -> IGESDimen_GeneralNote:
        """returns the General Note entity associated."""

    def WitnessLine(self) -> IGESDimen_WitnessLine:
        """returns the Witness Line associated or Null handle"""

    def Leader(self) -> IGESDimen_LeaderArrow:
        """returns the Leader associated or Null handle"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_PointDimension(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGES Point Dimension, Type <220> Form <0>,
    in package IGESDimen
    A Point Dimension Entity consists of a leader, text, and
    an optional circle or hexagon enclosing the text
    IGES specs for this entity mention SimpleClosedPlanarCurve
    Entity(106/63)which is not listed in LIST.Text In the sequel
    we have ignored this & considered only the other two entity
    for representing the hexagon or circle enclosing the text.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_PointDimension) -> None: ...

    def Init(self, aNote: IGESDimen_GeneralNote | None, anArrow: IGESDimen_LeaderArrow | None, aGeom: nanoocp.IGESData.IGESData_IGESEntity | None) -> None: ...

    def Note(self) -> IGESDimen_GeneralNote: ...

    def LeaderArrow(self) -> IGESDimen_LeaderArrow: ...

    def GeomCase(self) -> int:
        """
        returns the type of geometric entity.
        0 if no hexagon or circle encloses the text
        1 if CircularArc
        2 if CompositeCurve
        3 otherwise
        """

    def Geom(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the Geometry Entity, Null handle if GeomCase(me) .eq. 0"""

    def CircularArc(self) -> nanoocp.IGESGeom.IGESGeom_CircularArc:
        """returns Null handle if GeomCase(me) .ne. 1"""

    def CompositeCurve(self) -> nanoocp.IGESGeom.IGESGeom_CompositeCurve:
        """returns Null handle if GeomCase(me) .ne. 2"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_Protocol(nanoocp.IGESData.IGESData_Protocol):
    """Description of Protocol for IGESDimen"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_Protocol) -> None: ...

    def NbResources(self) -> int:
        """
        Gives the count of Resource Protocol. Here, two
        (Protocols from IGESGraph and IGESGeom)
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

class IGESDimen_RadiusDimension(nanoocp.IGESData.IGESData_IGESEntity):
    """
    Defines IGES Radius Dimension, type <222> Form <0, 1>,
    in package IGESDimen.
    A Radius Dimension Entity consists of a General Note, a
    leader, and an arc center point. A second form of this
    entity accounts for the occasional need to have two
    leader entities referenced.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_RadiusDimension) -> None: ...

    def Init(self, aNote: IGESDimen_GeneralNote | None, anArrow: IGESDimen_LeaderArrow | None, arcCenter: nanoocp.gp.gp_XY, anotherArrow: IGESDimen_LeaderArrow | None) -> None: ...

    def InitForm(self, form: int) -> None:
        """
        Allows to change Form Number
        (1 admits null arrow)
        """

    def Note(self) -> IGESDimen_GeneralNote:
        """returns the General Note entity"""

    def Leader(self) -> IGESDimen_LeaderArrow:
        """returns the Leader Arrow entity"""

    def Center(self) -> nanoocp.gp.gp_Pnt2d:
        """returns the coordinates of the Arc Center"""

    def TransformedCenter(self) -> nanoocp.gp.gp_Pnt:
        """
        returns the coordinates of the Arc Center after Transformation
        (Z coord taken from ZDepth of Leader Entity)
        """

    def HasLeader2(self) -> bool:
        """returns True if form is 1, False if 0"""

    def Leader2(self) -> IGESDimen_LeaderArrow:
        """returns Null handle if Form is 0"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_ReadWriteModule(nanoocp.IGESData.IGESData_ReadWriteModule):
    """
    Defines Dimen File Access Module for IGESDimen (specific parts)
    Specific actions concern : Read and Write Own Parameters of
    an IGESEntity
    """

    @overload
    def __init__(self) -> None:
        """Creates a ReadWriteModule & puts it into ReaderLib & WriterLib"""

    @overload
    def __init__(self, theOther: IGESDimen_ReadWriteModule) -> None: ...

    def CaseIGES(self, typenum: int, formnum: int) -> int:
        """Defines Case Numbers for Entities of IGESDimen"""

    def ReadOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """Reads own parameters from file for an Entity of IGESDimen"""

    def WriteOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_Section(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines Section, Type <106> Form <31-38>
    in package IGESDimen
    Contains information to display sectioned sides
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_Section) -> None: ...

    def Init(self, dataType: int, aDisp: float, dataPoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XY] | None) -> None:
        """
        This method is used to set the fields of the class
        Section
        - dataType   : Interpretation Flag, always = 1
        - aDisp      : Common z displacement
        - dataPoints : Data points
        """

    def SetFormNumber(self, form: int) -> None:
        """
        Changes FormNumber (indicates the Type of the Hatches)
        Error if not in range [31-38]
        """

    def Datatype(self) -> int:
        """returns Interpretation Flag, always = 1"""

    def NbPoints(self) -> int:
        """returns number of Data Points"""

    def ZDisplacement(self) -> float:
        """returns common Z displacement"""

    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        returns Index'th data point
        raises exception if Index <= 0 or Index > NbPoints()
        """

    def TransformedPoint(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        returns Index'th data point after Transformation
        raises exception if Index <= 0 or Index > NbPoints()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_SectionedArea(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGES Sectioned Area, Type <230> Form <0>,
    in package IGESDimen
    A sectioned area is a portion of a design which is to be
    filled with a pattern of lines. Ordinarily, this entity
    is used to reveal or expose shape or material characteri-
    stics defined by other entities. It consists of a pointer
    to an exterior definition curve, a specification of the
    pattern of lines, the coordinates of a point on a pattern
    line, the distance between the pattern lines, the angle
    between the pattern lines and the X-axis of definition
    space, and the specification of any enclosed definition
    curves (commonly known as islands).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_SectionedArea) -> None: ...

    def Init(self, aCurve: nanoocp.IGESData.IGESData_IGESEntity | None, aPattern: int, aPoint: nanoocp.gp.gp_XYZ, aDistance: float, anAngle: float, someIslands: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None: ...

    def SetInverted(self, mode: bool) -> None:
        """
        Sets the cross hatches to be inverted or not,
        according value of <mode> (corresponds to FormNumber)
        """

    def IsInverted(self) -> bool:
        """
        Returns True if cross hatches as Inverted, else they are
        Standard (Inverted : Form=1, Standard : Form=0)
        """

    def ExteriorCurve(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the exterior definition curve"""

    def Pattern(self) -> int:
        """returns fill pattern code"""

    def PassingPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns point thru which line should pass"""

    def TransformedPassingPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns point thru which line should pass after Transformation"""

    def ZDepth(self) -> float:
        """returns the Z depth"""

    def Distance(self) -> float:
        """returns the normal distance between lines"""

    def Angle(self) -> float:
        """returns the angle of lines with XT axis"""

    def NbIslands(self) -> int:
        """returns the number of island curves"""

    def IslandCurve(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the interior definition curves, returns Null Handle
        exception raised if Index <= 0 or Index > NbIslands()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_SpecificModule(nanoocp.IGESData.IGESData_SpecificModule):
    """
    Defines Services attached to IGES Entities :
    Dump & OwnCorrect, for IGESDimen
    """

    @overload
    def __init__(self) -> None:
        """Creates a SpecificModule from IGESDimen & puts it into SpecificLib"""

    @overload
    def __init__(self, theOther: IGESDimen_SpecificModule) -> None: ...

    def OwnDump(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Specific Dump (own parameters) for IGESDimen"""

    def OwnCorrect(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None) -> bool:
        """
        Performs non-ambiguous Corrections on Entities which support
        them (BasicDimension,CenterLine,DimensionDisplayData,
        DimensionTolerance,DimensionUnits,DimensionedGeometry,
        NewDimensionedGeometry,Section,WitnessLine)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDimen_ToolAngularDimension:
    """
    Tool to work on a AngularDimension. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolAngularDimension, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolAngularDimension) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_AngularDimension | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_AngularDimension | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_AngularDimension | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a AngularDimension <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDimen_AngularDimension | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_AngularDimension | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_AngularDimension | None, entto: IGESDimen_AngularDimension | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_AngularDimension | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolBasicDimension:
    """
    Tool to work on a BasicDimension. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolBasicDimension, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolBasicDimension) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_BasicDimension | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_BasicDimension | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_BasicDimension | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a BasicDimension <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESDimen_BasicDimension | None) -> bool:
        """
        Sets automatic unambiguous Correction on a BasicDimension
        (NbPropertyValues forced to 8)
        """

    def DirChecker(self, ent: IGESDimen_BasicDimension | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_BasicDimension | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_BasicDimension | None, entto: IGESDimen_BasicDimension | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_BasicDimension | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolCenterLine:
    """
    Tool to work on a CenterLine. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolCenterLine, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolCenterLine) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_CenterLine | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_CenterLine | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_CenterLine | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a CenterLine <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESDimen_CenterLine | None) -> bool:
        """
        Sets automatic unambiguous Correction on a CenterLine
        (LineFont forced to Rank = 1, DataType forced to 1)
        """

    def DirChecker(self, ent: IGESDimen_CenterLine | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_CenterLine | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_CenterLine | None, entto: IGESDimen_CenterLine | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_CenterLine | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolCurveDimension:
    """
    Tool to work on a CurveDimension. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolCurveDimension, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolCurveDimension) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_CurveDimension | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_CurveDimension | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_CurveDimension | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a CurveDimension <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDimen_CurveDimension | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_CurveDimension | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_CurveDimension | None, entto: IGESDimen_CurveDimension | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_CurveDimension | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolDiameterDimension:
    """
    Tool to work on a DiameterDimension. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolDiameterDimension, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolDiameterDimension) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_DiameterDimension | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_DiameterDimension | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_DiameterDimension | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a DiameterDimension <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDimen_DiameterDimension | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_DiameterDimension | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_DiameterDimension | None, entto: IGESDimen_DiameterDimension | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_DiameterDimension | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolDimensionDisplayData:
    """
    Tool to work on a DimensionDisplayData. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolDimensionDisplayData, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolDimensionDisplayData) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_DimensionDisplayData | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_DimensionDisplayData | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_DimensionDisplayData | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a DimensionDisplayData <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESDimen_DimensionDisplayData | None) -> bool:
        """
        Sets automatic unambiguous Correction on a DimensionDisplayData
        (NbPropertyValues forced to 14)
        """

    def DirChecker(self, ent: IGESDimen_DimensionDisplayData | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_DimensionDisplayData | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_DimensionDisplayData | None, entto: IGESDimen_DimensionDisplayData | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_DimensionDisplayData | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolDimensionedGeometry:
    """
    Tool to work on a DimensionedGeometry. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolDimensionedGeometry, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolDimensionedGeometry) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_DimensionedGeometry | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_DimensionedGeometry | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_DimensionedGeometry | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a DimensionedGeometry <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESDimen_DimensionedGeometry | None) -> bool:
        """
        Sets automatic unambiguous Correction on a DimensionedGeometry
        (NbDimensions forced to 1)
        """

    def DirChecker(self, ent: IGESDimen_DimensionedGeometry | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_DimensionedGeometry | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_DimensionedGeometry | None, entto: IGESDimen_DimensionedGeometry | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_DimensionedGeometry | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolDimensionTolerance:
    """
    Tool to work on a DimensionTolerance. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolDimensionTolerance, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolDimensionTolerance) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_DimensionTolerance | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_DimensionTolerance | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_DimensionTolerance | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a DimensionTolerance <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESDimen_DimensionTolerance | None) -> bool:
        """
        Sets automatic unambiguous Correction on a DimensionTolerance
        (NbPropertyValues forced to 8)
        """

    def DirChecker(self, ent: IGESDimen_DimensionTolerance | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_DimensionTolerance | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_DimensionTolerance | None, entto: IGESDimen_DimensionTolerance | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_DimensionTolerance | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolDimensionUnits:
    """
    Tool to work on a DimensionUnits. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolDimensionUnits, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolDimensionUnits) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_DimensionUnits | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_DimensionUnits | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_DimensionUnits | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a DimensionUnits <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESDimen_DimensionUnits | None) -> bool:
        """
        Sets automatic unambiguous Correction on a DimensionUnits
        (NbPropertyValues forced to 6)
        """

    def DirChecker(self, ent: IGESDimen_DimensionUnits | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_DimensionUnits | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_DimensionUnits | None, entto: IGESDimen_DimensionUnits | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_DimensionUnits | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolFlagNote:
    """
    Tool to work on a FlagNote. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolFlagNote, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolFlagNote) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_FlagNote | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_FlagNote | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_FlagNote | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a FlagNote <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDimen_FlagNote | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_FlagNote | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_FlagNote | None, entto: IGESDimen_FlagNote | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_FlagNote | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolGeneralLabel:
    """
    Tool to work on a GeneralLabel. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolGeneralLabel, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolGeneralLabel) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_GeneralLabel | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_GeneralLabel | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_GeneralLabel | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a GeneralLabel <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDimen_GeneralLabel | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_GeneralLabel | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_GeneralLabel | None, entto: IGESDimen_GeneralLabel | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_GeneralLabel | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolGeneralNote:
    """
    Tool to work on a GeneralNote. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolGeneralNote, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolGeneralNote) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_GeneralNote | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_GeneralNote | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_GeneralNote | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a GeneralNote <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDimen_GeneralNote | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_GeneralNote | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_GeneralNote | None, entto: IGESDimen_GeneralNote | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_GeneralNote | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolGeneralSymbol:
    """
    Tool to work on a GeneralSymbol. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolGeneralSymbol, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolGeneralSymbol) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_GeneralSymbol | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_GeneralSymbol | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_GeneralSymbol | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a GeneralSymbol <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDimen_GeneralSymbol | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_GeneralSymbol | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_GeneralSymbol | None, entto: IGESDimen_GeneralSymbol | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_GeneralSymbol | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolLeaderArrow:
    """
    Tool to work on a LeaderArrow. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolLeaderArrow, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolLeaderArrow) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_LeaderArrow | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_LeaderArrow | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_LeaderArrow | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a LeaderArrow <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDimen_LeaderArrow | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_LeaderArrow | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_LeaderArrow | None, entto: IGESDimen_LeaderArrow | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_LeaderArrow | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolLinearDimension:
    """
    Tool to work on a LinearDimension. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolLinearDimension, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolLinearDimension) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_LinearDimension | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_LinearDimension | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_LinearDimension | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a LinearDimension <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDimen_LinearDimension | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_LinearDimension | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_LinearDimension | None, entto: IGESDimen_LinearDimension | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_LinearDimension | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolNewDimensionedGeometry:
    """
    Tool to work on a NewDimensionedGeometry. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolNewDimensionedGeometry, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolNewDimensionedGeometry) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_NewDimensionedGeometry | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_NewDimensionedGeometry | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_NewDimensionedGeometry | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a NewDimensionedGeometry <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESDimen_NewDimensionedGeometry | None) -> bool:
        """
        Sets automatic unambiguous Correction on a NewDimensionedGeometry
        (NbDimensions forced to 1, Transf Nullified in D.E.)
        """

    def DirChecker(self, ent: IGESDimen_NewDimensionedGeometry | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_NewDimensionedGeometry | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_NewDimensionedGeometry | None, entto: IGESDimen_NewDimensionedGeometry | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_NewDimensionedGeometry | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolNewGeneralNote:
    """
    Tool to work on a NewGeneralNote. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolNewGeneralNote, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolNewGeneralNote) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_NewGeneralNote | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_NewGeneralNote | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_NewGeneralNote | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a NewGeneralNote <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDimen_NewGeneralNote | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_NewGeneralNote | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_NewGeneralNote | None, entto: IGESDimen_NewGeneralNote | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_NewGeneralNote | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolOrdinateDimension:
    """
    Tool to work on a OrdinateDimension. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolOrdinateDimension, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolOrdinateDimension) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_OrdinateDimension | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_OrdinateDimension | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_OrdinateDimension | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a OrdinateDimension <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDimen_OrdinateDimension | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_OrdinateDimension | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_OrdinateDimension | None, entto: IGESDimen_OrdinateDimension | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_OrdinateDimension | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolPointDimension:
    """
    Tool to work on a PointDimension. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolPointDimension, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolPointDimension) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_PointDimension | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_PointDimension | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_PointDimension | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a PointDimension <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDimen_PointDimension | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_PointDimension | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_PointDimension | None, entto: IGESDimen_PointDimension | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_PointDimension | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolRadiusDimension:
    """
    Tool to work on a RadiusDimension. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolRadiusDimension, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolRadiusDimension) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_RadiusDimension | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_RadiusDimension | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_RadiusDimension | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a RadiusDimension <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDimen_RadiusDimension | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_RadiusDimension | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_RadiusDimension | None, entto: IGESDimen_RadiusDimension | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_RadiusDimension | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolSection:
    """
    Tool to work on a Section. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSection, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolSection) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_Section | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_Section | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_Section | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Section <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESDimen_Section | None) -> bool:
        """
        Sets automatic unambiguous Correction on a Section
        (LineFont forced to Rank = 1, DataType forced to 1)
        """

    def DirChecker(self, ent: IGESDimen_Section | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_Section | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_Section | None, entto: IGESDimen_Section | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_Section | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolSectionedArea:
    """
    Tool to work on a SectionedArea. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSectionedArea, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolSectionedArea) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_SectionedArea | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_SectionedArea | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_SectionedArea | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a SectionedArea <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDimen_SectionedArea | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_SectionedArea | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_SectionedArea | None, entto: IGESDimen_SectionedArea | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_SectionedArea | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_ToolWitnessLine:
    """
    Tool to work on a WitnessLine. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolWitnessLine, ready to work"""

    @overload
    def __init__(self, theOther: IGESDimen_ToolWitnessLine) -> None: ...

    def ReadOwnParams(self, ent: IGESDimen_WitnessLine | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDimen_WitnessLine | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDimen_WitnessLine | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a WitnessLine <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESDimen_WitnessLine | None) -> bool:
        """
        Sets automatic unambiguous Correction on a WitnessLine
        (LineFont forced to Rank = 1, DataType forced to 1)
        """

    def DirChecker(self, ent: IGESDimen_WitnessLine | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDimen_WitnessLine | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDimen_WitnessLine | None, entto: IGESDimen_WitnessLine | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDimen_WitnessLine | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDimen_WitnessLine(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines WitnessLine, Type <106> Form <40>
    in package IGESDimen
    Contains one or more straight line segments associated
    with drafting entities of various types
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDimen_WitnessLine) -> None: ...

    def Init(self, dataType: int, aDisp: float, dataPoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XY] | None) -> None:
        """
        This method is used to set the fields of the class
        WitnessLine
        - dataType   : Interpretation Flag, always = 1
        - aDispl     : Common z displacement
        - dataPoints : Data points
        """

    def Datatype(self) -> int:
        """returns Interpretation Flag, always = 1"""

    def NbPoints(self) -> int:
        """returns number of Data Points"""

    def ZDisplacement(self) -> float:
        """returns common Z displacement"""

    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        returns Index'th. data point
        raises exception if Index <= 0 or Index > NbPoints
        """

    def TransformedPoint(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        returns data point after Transformation.
        raises exception if Index <= 0 or Index > NbPoints
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.IGESDimen
IGESDimen_Array1OfGeneralNote = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESDimen.IGESDimen_GeneralNote]
IGESDimen_Array1OfLeaderArrow = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESDimen.IGESDimen_LeaderArrow]
IGESDimen_HArray1OfGeneralNote = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESDimen.IGESDimen_GeneralNote]
IGESDimen_HArray1OfLeaderArrow = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESDimen.IGESDimen_LeaderArrow]
