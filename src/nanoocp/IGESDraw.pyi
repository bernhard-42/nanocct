"""OCCT package IGESDraw (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.IGESData
import nanoocp.IGESDimen
import nanoocp.IGESGeom
import nanoocp.IGESGraph
import nanoocp.Interface
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.gp


class IGESDraw:
    """
    This package contains the group of classes necessary for
    Structure Entities implied in Drawings and Structured
    Graphics (Sets for drawing, Drawings and Views).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw) -> None: ...

    @staticmethod
    def Init() -> None:
        """Prepares dynamic data (Protocol, Modules) for this package"""

    @staticmethod
    def Protocol() -> IGESDraw_Protocol:
        """Returns the Protocol for this Package"""

class IGESDraw_CircArraySubfigure(nanoocp.IGESData.IGESData_IGESEntity):
    """
    Defines IGES Circular Array Subfigure Instance Entity,
    Type <414> Form Number <0> in package IGESDraw

    Used to produce copies of object called the base entity,
    arranging them around the edge of an imaginary circle
    whose center and radius are specified
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw_CircArraySubfigure) -> None: ...

    def Init(self, aBase: nanoocp.IGESData.IGESData_IGESEntity | None, aNumLocs: int, aCenter: nanoocp.gp.gp_XYZ, aRadius: float, aStAngle: float, aDelAngle: float, aFlag: int, allNumPos: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """
        This method is used to set the fields of the class
        CircArraySubfigure
        - aBase     : Base entity
        - aNumLocs  : Total number of possible instance locations
        - aCenter   : Coordinates of Center of imaginary circle
        - aRadius   : Radius of imaginary circle
        - aStAngle  : Start angle in radians
        - aDelAngle : Delta angle in radians
        - aFlag     : DO-DON'T flag to control which portion to
        display
        - allNumPos : All position to be or not to be processed
        """

    def BaseEntity(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the base entity, copies of which are produced"""

    def NbLocations(self) -> int:
        """returns total number of possible instance locations"""

    def CenterPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the center of the imaginary circle"""

    def TransformedCenterPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the Transformed center of the imaginary circle"""

    def CircleRadius(self) -> float:
        """returns the radius of the imaginary circle"""

    def StartAngle(self) -> float:
        """returns the start angle in radians"""

    def DeltaAngle(self) -> float:
        """returns the delta angle in radians"""

    def ListCount(self) -> int:
        """returns 0 if all elements to be displayed"""

    def DisplayFlag(self) -> bool:
        """returns True if (ListCount = 0) all elements are to be displayed"""

    def DoDontFlag(self) -> bool:
        """
        returns 0 if half or fewer of the elements of the array are defined
        returns 1 if half or more of the elements are defined
        """

    def PositionNum(self, Index: int) -> bool:
        """
        returns whether Index is to be processed (DO)
        or not to be processed(DON'T)
        if (ListCount = 0) return theDoDontFlag
        raises exception if Index <= 0 or Index > ListCount().
        """

    def ListPosition(self, Index: int) -> int:
        """
        returns the Index'th value position
        raises exception if Index <= 0 or Index > ListCount().
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_ConnectPoint(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESConnectPoint, Type <132> Form Number <0>
    in package IGESDraw

    Connect Point Entity describes a point of connection for
    zero, one or more entities. Its referenced from Composite
    curve, or Network Subfigure Definition/Instance, or Flow
    Associative Instance, or it may stand alone.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw_ConnectPoint) -> None: ...

    def Init(self, aPoint: nanoocp.gp.gp_XYZ, aDisplaySymbol: nanoocp.IGESData.IGESData_IGESEntity | None, aTypeFlag: int, aFunctionFlag: int, aFunctionIdentifier: nanoocp.TCollection.TCollection_HAsciiString | None, anIdentifierTemplate: nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate | None, aFunctionName: nanoocp.TCollection.TCollection_HAsciiString | None, aFunctionTemplate: nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate | None, aPointIdentifier: int, aFunctionCode: int, aSwapFlag: int, anOwnerSubfigure: nanoocp.IGESData.IGESData_IGESEntity | None) -> None:
        """
        This method is used to set the fields of the class
        ConnectPoint
        - aPoint               : A Coordinate point
        - aDisplaySymbol       : Display symbol Geometry
        - aTypeFlag            : Type of the connection
        - aFunctionFlag        : Function flag for the connection
        - aFunctionIdentifier  : Connection Point Function Identifier
        - anIdentifierTemplate : Connection Point Function Template
        - aFunctionName        : Connection Point Function Name
        - aFunctionTemplate    : Connection Point Function Template
        - aPointIdentifier     : Unique Connect Point Identifier
        - aFunctionCode        : Connect Point Function Code
        - aSwapFlag            : Connect Point Swap Flag
        - anOwnerSubfigure     : Pointer to the "Owner" Entity
        """

    def Point(self) -> nanoocp.gp.gp_Pnt:
        """returns the coordinate of the connection point"""

    def TransformedPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the Transformed coordinate of the connection point"""

    def HasDisplaySymbol(self) -> bool:
        """
        returns True if Display symbol is specified
        else returns False
        """

    def DisplaySymbol(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        if display symbol specified returns display symbol geometric entity
        else returns NULL Handle
        """

    def TypeFlag(self) -> int:
        """
        return value specifies a particular type of connection :
        Type Flag = 0   : Not Specified(default)
        1   : Nonspecific logical  point of connection
        2   : Nonspecific physical point of connection
        101 : Logical component pin
        102 : Logical part connector
        103 : Logical offpage connector
        104 : Logical global signal connector
        201 : Physical PWA surface mount pin
        202 : Physical PWA blind pin
        203 : Physical PWA thru-pin
        5001-9999 : Implementor defined.
        """

    def FunctionFlag(self) -> int:
        """
        returns Function Code that specifies a particular function for the
        ECO576 connection :
        e.g.,        Function Flag = 0 : Unspecified(default)
        = 1 : Electrical Signal
        = 2 : Fluid flow Signal
        """

    def FunctionIdentifier(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """return HAsciiString identifying Pin Number or Nozzle Label etc."""

    def HasIdentifierTemplate(self) -> bool:
        """
        returns True if Text Display Template is specified for Identifier
        else returns False
        """

    def IdentifierTemplate(self) -> nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate:
        """
        if Text Display Template for the Function Identifier is defined,
        returns TestDisplayTemplate
        else returns NULL Handle
        """

    def FunctionName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns Connection Point Function Name"""

    def HasFunctionTemplate(self) -> bool:
        """
        returns True if Text Display Template is specified for Function Name
        else returns False
        """

    def FunctionTemplate(self) -> nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate:
        """
        if Text Display Template for the Function Name is defined,
        returns TestDisplayTemplate
        else returns NULL Handle
        """

    def PointIdentifier(self) -> int:
        """returns the Unique Connect Point Identifier"""

    def FunctionCode(self) -> int:
        """returns the Connect Point Function Code"""

    def SwapFlag(self) -> bool:
        """
        return value = 0 : Connect point may be swapped(default)
        = 1 : Connect point may not be swapped
        """

    def HasOwnerSubfigure(self) -> bool:
        """
        returns True if Network Subfigure Instance/Definition Entity
        is specified
        else returns False
        """

    def OwnerSubfigure(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns "owner" Network Subfigure Instance Entity,
        or Network Subfigure Definition Entity, or NULL Handle.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_Drawing(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESDrawing, Type <404> Form <0>
    in package IGESDraw

    Specifies a drawing as a collection of annotation entities
    defined in drawing space, and views which together
    constitute a single representation of a part
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw_Drawing) -> None: ...

    def Init(self, allViews: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_ViewKindEntity] | None, allViewOrigins: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XY] | None, allAnnotations: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """
        This method is used to set the fields of the class
        Drawing
        - allViews       : Pointers to DEs of View entities
        - allViewOrigins : Origin coordinates of transformed Views
        - allAnnotations : Pointers to DEs of Annotation entities
        raises exception if Lengths of allViews and allViewOrigins are
        not same.
        """

    def NbViews(self) -> int:
        """returns the number of view pointers in <me>"""

    def ViewItem(self, ViewIndex: int) -> nanoocp.IGESData.IGESData_ViewKindEntity:
        """
        returns the ViewKindEntity indicated by ViewIndex
        raises an exception if ViewIndex <= 0 or ViewIndex > NbViews().
        """

    def ViewOrigin(self, TViewIndex: int) -> nanoocp.gp.gp_Pnt2d:
        """
        returns the Drawing space coordinates of the origin of the
        Transformed view indicated by TViewIndex
        raises an exception if TViewIndex <= 0 or TViewIndex > NbViews().
        """

    def NbAnnotations(self) -> int:
        """returns the number of Annotation entities in <me>"""

    def Annotation(self, AnnotationIndex: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the Annotation entity in this Drawing, indicated by the
        AnnotationIndex
        raises an exception if AnnotationIndex <= 0 or
        AnnotationIndex > NbAnnotations().
        """

    def ViewToDrawing(self, NumView: int, ViewCoords: nanoocp.gp.gp_XYZ) -> nanoocp.gp.gp_XY: ...

    def DrawingUnit(self) -> tuple[bool, float]:
        """
        Returns the Drawing Unit Value if it is specified (by a
        specific property entity)
        If not specified, returns False, and val as zero :
        unit to consider is then the model unit in GlobalSection
        """

    def DrawingSize(self) -> tuple[bool, float, float]:
        """
        Returns the Drawing Size if it is specified (by a
        specific property entity)
        If not specified, returns False, and X,Y as zero :
        unit to consider is then the model unit in GlobalSection
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_DrawingWithRotation(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESDrawingWithRotation, Type <404> Form <1>
    in package IGESDraw

    Permits rotation, in addition to transformation and
    scaling, between the view and drawing coordinate systems
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw_DrawingWithRotation) -> None: ...

    def Init(self, allViews: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_ViewKindEntity] | None, allViewOrigins: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XY] | None, allOrientationAngles: nanoocp.NCollection.NCollection_HArray1[float] | None, allAnnotations: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """
        This method is used to set the fields of the class
        DrawingWithRotation
        - allViews             : Pointers to View entities
        - allViewOrigins       : Origin coords of transformed views
        - allOrientationAngles : Orientation angles of transformed views
        - allAnnotations       : Pointers to Annotation entities
        raises exception if Lengths of allViews, allViewOrigins and
        allOrientationAngles are not same.
        """

    def NbViews(self) -> int:
        """returns the number of view pointers in <me>"""

    def ViewItem(self, Index: int) -> nanoocp.IGESData.IGESData_ViewKindEntity:
        """
        returns the View entity indicated by Index
        raises an exception if Index <= 0 or Index > NbViews().
        """

    def ViewOrigin(self, Index: int) -> nanoocp.gp.gp_Pnt2d:
        """
        returns the Drawing space coordinates of the origin of the
        Transformed view indicated by Index
        raises an exception if Index <= 0 or Index > NbViews().
        """

    def OrientationAngle(self, Index: int) -> float:
        """
        returns the Orientation angle for the Transformed view
        indicated by Index
        raises an exception if Index <= 0 or Index > NbViews().
        """

    def NbAnnotations(self) -> int:
        """returns the number of Annotation entities in <me>"""

    def Annotation(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the Annotation entity in this Drawing, indicated by Index
        raises an exception if Index <= 0 or Index > NbAnnotations().
        """

    def ViewToDrawing(self, NumView: int, ViewCoords: nanoocp.gp.gp_XYZ) -> nanoocp.gp.gp_XY: ...

    def DrawingUnit(self) -> tuple[bool, float]:
        """
        Returns the Drawing Unit Value if it is specified (by a
        specific property entity)
        If not specified, returns False, and val as zero :
        unit to consider is then the model unit in GlobalSection
        """

    def DrawingSize(self) -> tuple[bool, float, float]:
        """
        Returns the Drawing Size if it is specified (by a
        specific property entity)
        If not specified, returns False, and X,Y as zero :
        unit to consider is then the model unit in GlobalSection
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_GeneralModule(nanoocp.IGESData.IGESData_GeneralModule):
    """
    Definition of General Services for IGESDraw (specific part)
    This Services comprise : Shared & Implied Lists, Copy, Check
    """

    @overload
    def __init__(self) -> None:
        """Creates a GeneralModule from IGESDraw and puts it into GeneralLib"""

    @overload
    def __init__(self, theOther: IGESDraw_GeneralModule) -> None: ...

    def OwnSharedCase(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a given IGESEntity <ent>, from
        its specific parameters : specific for each type
        """

    def OwnImpliedCase(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Specific list of Entities implied by an IGESEntity <ent> (in
        addition to Associativities). Redefined for ViewsVisible ...
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

    def OwnRenewCase(self, CN: int, entfrom: nanoocp.IGESData.IGESData_IGESEntity | None, entto: nanoocp.IGESData.IGESData_IGESEntity | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Renews parameters which are specific of each Type of Entity :
        redefined for ViewsVisible ... (takes only the implied ref.s
        which have also been copied)
        """

    def OwnDeleteCase(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None) -> None:
        """
        Clears parameters with can cause looping structures :
        redefined for ViewsVisible ... (clears the implied ref.s)
        """

    def CategoryNumber(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, shares: nanoocp.Interface.Interface_ShareTool) -> int:
        """
        Returns a category number which characterizes an entity
        Planar : Auxiliary
        Subfigures and ConnectPoint : Structure
        others : Drawing
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_LabelDisplay(nanoocp.IGESData.IGESData_LabelDisplayEntity):
    """
    defines IGESLabelDisplay, Type <402> Form <5>
    in package IGESDraw

    Permits one or more displays for the
    entity labels of an entity
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw_LabelDisplay) -> None: ...

    def Init(self, allViews: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_ViewKindEntity] | None, allTextLocations: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ] | None, allLeaderEntities: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESDimen.IGESDimen_LeaderArrow] | None, allLabelLevels: nanoocp.NCollection.NCollection_HArray1[int] | None, allDisplayedEntities: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """
        This method is used to set the fields of the class
        LabelDisplay
        - allViews             : Pointers to View Entities
        - allTextLocations     : Coordinates of text locations in the views
        - allLeaderEntities    : Pointers to Leader Entities in the views
        - allLabelLevels       : Entity label level numbers in the views
        - allDisplayedEntities : Pointers to the entities being displayed
        raises exception if Lengths of allViews, allTextLocations,
        allLeaderEntities, allLabelLevels and allDisplayedEntities are
        not same.
        """

    def NbLabels(self) -> int:
        """returns the number of label placements in <me>"""

    def ViewItem(self, ViewIndex: int) -> nanoocp.IGESData.IGESData_ViewKindEntity:
        """
        returns the View entity indicated by ViewIndex
        raises an exception if ViewIndex <= 0 or ViewIndex > NbLabels().
        """

    def TextLocation(self, ViewIndex: int) -> nanoocp.gp.gp_Pnt:
        """
        returns the 3d-Point coordinates of the text location, in the
        view indicated by ViewIndex
        raises an exception if ViewIndex <= 0 or ViewIndex > NbLabels().
        """

    def LeaderEntity(self, ViewIndex: int) -> nanoocp.IGESDimen.IGESDimen_LeaderArrow:
        """
        returns the Leader entity in the view indicated by ViewIndex
        raises an exception if ViewIndex <= 0 or ViewIndex > NbLabels().
        """

    def LabelLevel(self, ViewIndex: int) -> int:
        """
        returns the Entity label level number in the view indicated
        by ViewIndex
        raises an exception if ViewIndex <= 0 or ViewIndex > NbLabels().
        """

    def DisplayedEntity(self, EntityIndex: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the entity indicated by EntityIndex
        raises an exception if EntityIndex <= 0 or EntityIndex > NbLabels().
        """

    def TransformedTextLocation(self, ViewIndex: int) -> nanoocp.gp.gp_Pnt:
        """
        returns the transformed 3d-Point coordinates of the text
        location, in the view indicated by ViewIndex
        raises an exception if ViewIndex <= 0 or ViewIndex > NbLabels().
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_NetworkSubfigure(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGES Network Subfigure Instance Entity,
    Type <420> Form Number <0> in package IGESDraw

    Used to specify each instance of Network Subfigure
    Definition Entity (Type 320, Form 0).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw_NetworkSubfigure) -> None: ...

    def Init(self, aDefinition: IGESDraw_NetworkSubfigureDef | None, aTranslation: nanoocp.gp.gp_XYZ, aScaleFactor: nanoocp.gp.gp_XYZ, aTypeFlag: int, aDesignator: nanoocp.TCollection.TCollection_HAsciiString | None, aTemplate: nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate | None, allConnectPoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESDraw.IGESDraw_ConnectPoint] | None) -> None:
        """
        This method is used to set the fields of the class
        NetworkSubfigure
        - aDefinition      : Network Subfigure Definition Entity
        - aTranslation     : Translation data relative to the model
        space or the definition space
        - aScaleFactor     : Scale factors in the definition space
        - aTypeFlag        : Type flag
        - aDesignator      : Primary reference designator
        - aTemplate        : Primary reference designator Text
        display Template Entity
        - allConnectPoints : Associated Connect Point Entities
        """

    def SubfigureDefinition(self) -> IGESDraw_NetworkSubfigureDef:
        """returns Network Subfigure Definition Entity specified by this entity"""

    def Translation(self) -> nanoocp.gp.gp_XYZ:
        """
        returns Translation Data relative to either model space or to
        the definition space of a referring entity
        """

    def TransformedTranslation(self) -> nanoocp.gp.gp_XYZ:
        """
        returns the Transformed Translation Data relative to either model
        space or to the definition space of a referring entity
        """

    def ScaleFactors(self) -> nanoocp.gp.gp_XYZ:
        """returns Scale factor in definition space(x, y, z axes)"""

    def TypeFlag(self) -> int:
        """
        returns Type Flag which implements the distinction between Logical
        design and Physical design data,and is required if both are present.
        Type Flag = 0 : Not specified (default)
        = 1 : Logical
        = 2 : Physical
        """

    def ReferenceDesignator(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns the primary reference designator"""

    def HasDesignatorTemplate(self) -> bool:
        """
        returns True if Text Display Template Entity is specified,
        else False
        """

    def DesignatorTemplate(self) -> nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate:
        """
        returns primary reference designator Text Display Template Entity,
        or null. If null, no Text Display Template Entity specified
        """

    def NbConnectPoints(self) -> int:
        """returns the number of associated Connect Point Entities"""

    def ConnectPoint(self, Index: int) -> IGESDraw_ConnectPoint:
        """
        returns the Index'th  associated Connect point Entity
        raises exception if Index <= 0 or Index > NbConnectPoints()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_NetworkSubfigureDef(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESNetworkSubfigureDef,
    Type <320> Form Number <0> in package IGESDraw

    This class differs from the ordinary subfigure definition
    in that it defines a specialized subfigure, one whose
    instances may participate in networks.

    The Number of associated(child) Connect Point Entities
    in the Network Subfigure Instance must match the number
    in the Network Subfigure Definition, their order must
    be identical, and any unused points of connection in
    the instance must be indicated by a null(zero) pointer.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw_NetworkSubfigureDef) -> None: ...

    def Init(self, aDepth: int, aName: nanoocp.TCollection.TCollection_HAsciiString | None, allEntities: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None, aTypeFlag: int, aDesignator: nanoocp.TCollection.TCollection_HAsciiString | None, aTemplate: nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate | None, allPointEntities: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESDraw.IGESDraw_ConnectPoint] | None) -> None:
        """
        This method is used to set fields of the class
        NetworkSubfigureDef
        - aDepth           : Depth of Subfigure
        (indicating the amount of nesting)
        - aName            : Subfigure Name
        - allEntities      : Associated subfigures Entities exclusive
        of primary reference designator and
        Control Points.
        - aTypeFlag        : Type flag determines which Entity
        belongs in which design
        (Logical design or Physical design)
        - aDesignator      : Designator HAsciiString and its Template
        - allPointEntities : Associated Connect Point Entities
        """

    def Depth(self) -> int:
        """
        returns Depth of Subfigure(indication the amount of nesting)
        Note : The Depth is inclusive of both Network Subfigure Definition
        Entity and the Ordinary Subfigure Definition Entity.
        Thus, the two may be nested.
        """

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns the Subfigure Name"""

    def NbEntities(self) -> int:
        """
        returns Number of Associated(child) entries in subfigure exclusive
        of primary reference designator and Control Points
        """

    def Entity(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the Index'th IGESEntity in subfigure exclusive of primary
        reference designator and Control Points
        raises exception if Index <=0 or Index > NbEntities()
        """

    def TypeFlag(self) -> int:
        """
        return value = 0 : Not Specified
        = 1 : Logical  design
        = 2 : Physical design
        """

    def Designator(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """returns Primary Reference Designator"""

    def HasDesignatorTemplate(self) -> bool:
        """
        returns True if Text Display Template is specified for
        primary designator else returns False
        """

    def DesignatorTemplate(self) -> nanoocp.IGESGraph.IGESGraph_TextDisplayTemplate:
        """
        if Text Display Template specified then return TextDisplayTemplate
        else return NULL Handle
        """

    def NbPointEntities(self) -> int:
        """returns the Number Of Associated(child) Connect Point Entities"""

    def HasPointEntity(self, Index: int) -> bool:
        """
        returns True is Index'th Associated Connect Point Entity is present
        else returns False
        raises exception if Index is out of bound
        """

    def PointEntity(self, Index: int) -> IGESDraw_ConnectPoint:
        """
        returns the Index'th Associated Connect Point Entity
        raises exception if Index <= 0 or Index > NbPointEntities()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_PerspectiveView(nanoocp.IGESData.IGESData_ViewKindEntity):
    """
    defines IGESPerspectiveView, Type <410> Form <1>
    in package IGESDraw

    Supports a perspective view.
    Any geometric projection is defined by a view plane
    and the projectors that pass through the view plane.
    Projectors can be visualized as rays of light that
    form an image by passing through the viewed object
    and striking the view plane.
    The projectors are defined via a point called the
    Centre-of-Projection or the eye-point.
    A perspective view is formed by all projectors that
    emanate from the Centre-of-Projection and pass
    through the view plane.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw_PerspectiveView) -> None: ...

    def Init(self, aViewNumber: int, aScaleFactor: float, aViewNormalVector: nanoocp.gp.gp_XYZ, aViewReferencePoint: nanoocp.gp.gp_XYZ, aCenterOfProjection: nanoocp.gp.gp_XYZ, aViewUpVector: nanoocp.gp.gp_XYZ, aViewPlaneDistance: float, aTopLeft: nanoocp.gp.gp_XY, aBottomRight: nanoocp.gp.gp_XY, aDepthClip: int, aBackPlaneDistance: float, aFrontPlaneDistance: float) -> None:
        """
        This method is used to set the fields of the class
        PerspectiveView
        - aViewNumber         : The desired view
        - aScaleFactor        : Scale factor
        - aViewNormalVector   : View plane normal vector (model space)
        - aViewReferencePoint : View reference point     (model space)
        - aCenterOfProjection : Center Of Projection     (model space)
        - aViewUpVector       : View up vector           (model space)
        - aViewPlaneDistance  : View plane distance      (model space)
        - aTopLeft            : Top-left point of clipping window
        - aBottomRight        : Bottom-right point of clipping window
        - aDepthClip          : Depth clipping indicator
        - aBackPlaneDistance  : Distance of back clipping plane
        - aFrontPlaneDistance : Distance of front clipping plane
        """

    def IsSingle(self) -> bool:
        """Returns True (for a single view)"""

    def NbViews(self) -> int:
        """Returns 1 (single view)"""

    def ViewItem(self, num: int) -> nanoocp.IGESData.IGESData_ViewKindEntity:
        """For a single view, returns <me> whatever <num>"""

    def ViewNumber(self) -> int:
        """returns the view number associated with <me>"""

    def ScaleFactor(self) -> float:
        """returns the scale factor associated with <me>"""

    def ViewNormalVector(self) -> nanoocp.gp.gp_Vec:
        """returns the View plane normal vector (model space)"""

    def ViewReferencePoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the View reference point (model space)"""

    def CenterOfProjection(self) -> nanoocp.gp.gp_Pnt:
        """returns the Center Of Projection (model space)"""

    def ViewUpVector(self) -> nanoocp.gp.gp_Vec:
        """returns the View up vector (model space)"""

    def ViewPlaneDistance(self) -> float:
        """returns the View plane distance (model space)"""

    def TopLeft(self) -> nanoocp.gp.gp_Pnt2d:
        """returns the top left point of the clipping window"""

    def BottomRight(self) -> nanoocp.gp.gp_Pnt2d:
        """returns the bottom right point of the clipping window"""

    def DepthClip(self) -> int:
        """
        returns the Depth clipping indicator
        0 = No depth clipping
        1 = Back clipping plane ON
        2 = Front clipping plane ON
        3 = Back and front clipping planes ON
        """

    def BackPlaneDistance(self) -> float:
        """
        returns the View coordinate denoting the location of
        the back clipping plane
        """

    def FrontPlaneDistance(self) -> float:
        """
        returns the View coordinate denoting the location of
        the front clipping plane
        """

    def ViewMatrix(self) -> nanoocp.IGESData.IGESData_TransfEntity:
        """returns the Transformation Matrix"""

    def ModelToView(self, coords: nanoocp.gp.gp_XYZ) -> nanoocp.gp.gp_XYZ:
        """
        returns XYX from the Model space to the View space by
        applying the View Matrix
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_Planar(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESPlanar, Type <402> Form <16>
    in package IGESDraw

    Indicates that a collection of entities is coplanar.The
    entities may be geometric, annotative, and/or structural.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw_Planar) -> None: ...

    def Init(self, nbMats: int, aTransformationMatrix: nanoocp.IGESGeom.IGESGeom_TransformationMatrix | None, allEntities: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """
        This method is used to set the fields of the class Planar
        - nbMats                : Number of Transformation matrices
        - aTransformationMatrix : Pointer to the Transformation matrix
        - allEntities           : Pointers to the entities specified
        """

    def NbMatrices(self) -> int:
        """returns the number of Transformation matrices in <me>"""

    def NbEntities(self) -> int:
        """
        returns the number of Entities in the plane pointed to by this
        associativity
        """

    def IsIdentityMatrix(self) -> bool:
        """
        returns True if TransformationMatrix is Identity Matrix,
        i.e:- No Matrix defined.
        """

    def TransformMatrix(self) -> nanoocp.IGESGeom.IGESGeom_TransformationMatrix:
        """
        returns the Transformation matrix moving data from the XY plane
        into space or zero
        """

    def Entity(self, EntityIndex: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the Entity on the specified plane, indicated by EntityIndex
        raises an exception if EntityIndex <= 0 or
        EntityIndex > NbEntities()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_Protocol(nanoocp.IGESData.IGESData_Protocol):
    """Description of Protocol for IGESDraw"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw_Protocol) -> None: ...

    def NbResources(self) -> int:
        """
        Gives the count of Resource Protocol. Here, one
        (Protocol from IGESDimen)
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

class IGESDraw_ReadWriteModule(nanoocp.IGESData.IGESData_ReadWriteModule):
    """
    Defines Draw File Access Module for IGESDraw (specific parts)
    Specific actions concern : Read and Write Own Parameters of
    an IGESEntity.
    """

    @overload
    def __init__(self) -> None:
        """Creates a ReadWriteModule & puts it into ReaderLib & WriterLib"""

    @overload
    def __init__(self, theOther: IGESDraw_ReadWriteModule) -> None: ...

    def CaseIGES(self, typenum: int, formnum: int) -> int:
        """Defines Case Numbers for Entities of IGESDraw"""

    def ReadOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """Reads own parameters from file for an Entity of IGESDraw"""

    def WriteOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_RectArraySubfigure(nanoocp.IGESData.IGESData_IGESEntity):
    """
    Defines IGES Rectangular Array Subfigure Instance Entity,
    Type <412> Form Number <0> in package IGESDraw
    Used to produce copies of object called the base entity,
    arranging them in equally spaced rows and columns
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw_RectArraySubfigure) -> None: ...

    def Init(self, aBase: nanoocp.IGESData.IGESData_IGESEntity | None, aScale: float, aCorner: nanoocp.gp.gp_XYZ, nbCols: int, nbRows: int, hDisp: float, vtDisp: float, rotationAngle: float, doDont: int, allNumPos: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """
        This method is used to set the fields of the class
        RectArraySubfigure
        - aBase         : a base entity which is replicated
        - aScale        : Scale Factor
        - aCorner       : lower left hand corner for the entire array
        - nbCols        : Number of columns of the array
        - nbRows        : Number of rows of the array
        - hDisp         : Column separations
        - vtDisp        : Row separation
        - rotationAngle : Rotation angle specified in radians
        - allDont       : DO-DON'T flag to control which portion
        to display
        - allNumPos     : List of positions to be or not to be
        displayed
        """

    def BaseEntity(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the base entity, copies of which are produced"""

    def ScaleFactor(self) -> float:
        """returns the scale factor"""

    def LowerLeftCorner(self) -> nanoocp.gp.gp_Pnt:
        """returns coordinates of lower left hand corner for the entire array"""

    def TransformedLowerLeftCorner(self) -> nanoocp.gp.gp_Pnt:
        """returns Transformed coordinates of lower left corner for the array"""

    def NbColumns(self) -> int:
        """returns number of columns in the array"""

    def NbRows(self) -> int:
        """returns number of rows in the array"""

    def ColumnSeparation(self) -> float:
        """returns horizontal distance between columns"""

    def RowSeparation(self) -> float:
        """returns vertical distance between rows"""

    def RotationAngle(self) -> float:
        """returns rotation angle in radians"""

    def DisplayFlag(self) -> bool:
        """returns True if (ListCount = 0) i.e., all elements to be displayed"""

    def ListCount(self) -> int:
        """returns 0 if all replicated entities to be displayed"""

    def DoDontFlag(self) -> bool:
        """
        returns 0 if half or fewer of the elements of the array are defined
        1 if half or more of the elements are defined
        """

    def PositionNum(self, Index: int) -> bool:
        """
        returns whether Index is to be processed (DO)
        or not to be processed(DON'T)
        if (ListCount = 0) return theDoDontFlag
        """

    def ListPosition(self, Index: int) -> int:
        """
        returns the Index'th value position
        raises exception if Index <= 0 or Index > ListCount()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_SegmentedViewsVisible(nanoocp.IGESData.IGESData_ViewKindEntity):
    """
    defines IGESSegmentedViewsVisible, Type <402> Form <19>
    in package IGESDraw

    Permits the association of display parameters with the
    segments of curves in a given view
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw_SegmentedViewsVisible) -> None: ...

    def Init(self, allViews: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_ViewKindEntity] | None, allBreakpointParameters: nanoocp.NCollection.NCollection_HArray1[float] | None, allDisplayFlags: nanoocp.NCollection.NCollection_HArray1[int] | None, allColorValues: nanoocp.NCollection.NCollection_HArray1[int] | None, allColorDefinitions: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGraph.IGESGraph_Color] | None, allLineFontValues: nanoocp.NCollection.NCollection_HArray1[int] | None, allLineFontDefinitions: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_LineFontEntity] | None, allLineWeights: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """
        This method is used to set the fields of the class
        SegmentedViewsVisible
        - allViews                : Pointers to View Entities
        - allBreakpointParameters : Parameters of breakpoints
        - allDisplayFlags         : Display flags
        - allColorValues          : Color Values
        - allColorDefinitions     : Color Definitions
        - allLineFontValues       : LineFont values
        - allLineFontDefinitions  : LineFont Definitions
        - allLineWeights          : Line weights
        raises exception if Lengths of allViews, allBreakpointParameters,
        allDisplayFlags, allColorValues, allColorDefinitions,
        allLineFontValues, allLineFontDefinitions and allLineWeights
        are not same.
        """

    def IsSingle(self) -> bool:
        """Returns False (for a complex view)"""

    def NbViews(self) -> int:
        """Returns the count of Views referenced by <me> (inherited)"""

    def NbSegmentBlocks(self) -> int:
        """
        returns the number of view/segment blocks in <me>
        Similar to NbViews but has a more general significance
        """

    def ViewItem(self, ViewIndex: int) -> nanoocp.IGESData.IGESData_ViewKindEntity:
        """
        returns the View entity indicated by ViewIndex
        raises an exception if ViewIndex <= 0 or
        ViewIndex > NbSegmentBlocks()
        """

    def BreakpointParameter(self, BreakpointIndex: int) -> float:
        """
        returns the parameter of the breakpoint indicated by
        BreakpointIndex
        raises an exception if BreakpointIndex <= 0 or
        BreakpointIndex > NbSegmentBlocks().
        """

    def DisplayFlag(self, FlagIndex: int) -> int:
        """
        returns the Display flag indicated by FlagIndex
        raises an exception if FlagIndex <= 0 or
        FlagIndex > NbSegmentBlocks().
        """

    def IsColorDefinition(self, ColorIndex: int) -> bool:
        """
        returns True if the ColorIndex'th value of the
        "theColorDefinitions" field of <me> is a pointer
        raises an exception if ColorIndex <= 0 or
        ColorIndex > NbSegmentBlocks().
        """

    def ColorValue(self, ColorIndex: int) -> int:
        """
        returns the Color value indicated by ColorIndex
        raises an exception if ColorIndex <= 0 or
        ColorIndex > NbSegmentBlocks().
        """

    def ColorDefinition(self, ColorIndex: int) -> nanoocp.IGESGraph.IGESGraph_Color:
        """
        returns the Color definition entity indicated by ColorIndex
        raises an exception if ColorIndex <= 0 or
        ColorIndex > NbSegmentBlocks().
        """

    def IsFontDefinition(self, FontIndex: int) -> bool:
        """
        returns True if the FontIndex'th value of the
        "theLineFontDefinitions" field of <me> is a pointer
        raises an exception if FontIndex <= 0 or
        FontIndex > NbSegmentBlocks().
        """

    def LineFontValue(self, FontIndex: int) -> int:
        """
        returns the LineFont value indicated by FontIndex
        raises an exception if FontIndex <= 0 or
        FontIndex > NbSegmentBlocks().
        """

    def LineFontDefinition(self, FontIndex: int) -> nanoocp.IGESData.IGESData_LineFontEntity:
        """
        returns the LineFont definition entity indicated by FontIndex
        raises an exception if FontIndex <= 0 or
        FontIndex > NbSegmentBlocks().
        """

    def LineWeightItem(self, WeightIndex: int) -> int:
        """
        returns the LineWeight value indicated by WeightIndex
        raises an exception if WeightIndex <= 0 or
        WeightIndex > NbSegmentBlocks().
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_SpecificModule(nanoocp.IGESData.IGESData_SpecificModule):
    """
    Defines Services attached to IGES Entities :
    Dump & OwnCorrect, for IGESDraw
    """

    @overload
    def __init__(self) -> None:
        """Creates a SpecificModule from IGESDraw & puts it into SpecificLib"""

    @overload
    def __init__(self, theOther: IGESDraw_SpecificModule) -> None: ...

    def OwnDump(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Specific Dump (own parameters) for IGESDraw"""

    def OwnCorrect(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None) -> bool:
        """
        Performs non-ambiguous Corrections on Entities which support
        them (Planar)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_ToolCircArraySubfigure:
    """
    Tool to work on a CircArraySubfigure. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolCircArraySubfigure, ready to work"""

    @overload
    def __init__(self, theOther: IGESDraw_ToolCircArraySubfigure) -> None: ...

    def ReadOwnParams(self, ent: IGESDraw_CircArraySubfigure | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDraw_CircArraySubfigure | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDraw_CircArraySubfigure | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a CircArraySubfigure <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDraw_CircArraySubfigure | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDraw_CircArraySubfigure | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDraw_CircArraySubfigure | None, entto: IGESDraw_CircArraySubfigure | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDraw_CircArraySubfigure | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDraw_ToolConnectPoint:
    """
    Tool to work on a ConnectPoint. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolConnectPoint, ready to work"""

    @overload
    def __init__(self, theOther: IGESDraw_ToolConnectPoint) -> None: ...

    def ReadOwnParams(self, ent: IGESDraw_ConnectPoint | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDraw_ConnectPoint | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDraw_ConnectPoint | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ConnectPoint <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDraw_ConnectPoint | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDraw_ConnectPoint | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDraw_ConnectPoint | None, entto: IGESDraw_ConnectPoint | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDraw_ConnectPoint | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDraw_ToolDrawing:
    """
    Tool to work on a Drawing. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolDrawing, ready to work"""

    @overload
    def __init__(self, theOther: IGESDraw_ToolDrawing) -> None: ...

    def ReadOwnParams(self, ent: IGESDraw_Drawing | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDraw_Drawing | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDraw_Drawing | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Drawing <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESDraw_Drawing | None) -> bool:
        """
        Sets automatic unambiguous Correction on a Drawing
        (Null Views are removed from list)
        """

    def DirChecker(self, ent: IGESDraw_Drawing | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDraw_Drawing | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDraw_Drawing | None, entto: IGESDraw_Drawing | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDraw_Drawing | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDraw_ToolDrawingWithRotation:
    """
    Tool to work on a DrawingWithRotation. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolDrawingWithRotation, ready to work"""

    @overload
    def __init__(self, theOther: IGESDraw_ToolDrawingWithRotation) -> None: ...

    def ReadOwnParams(self, ent: IGESDraw_DrawingWithRotation | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDraw_DrawingWithRotation | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDraw_DrawingWithRotation | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a DrawingWithRotation <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESDraw_DrawingWithRotation | None) -> bool:
        """
        Sets automatic unambiguous Correction on a DrawingWithRotation
        (Null Views are removed from list)
        """

    def DirChecker(self, ent: IGESDraw_DrawingWithRotation | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDraw_DrawingWithRotation | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDraw_DrawingWithRotation | None, entto: IGESDraw_DrawingWithRotation | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDraw_DrawingWithRotation | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDraw_ToolLabelDisplay:
    """
    Tool to work on a LabelDisplay. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolLabelDisplay, ready to work"""

    @overload
    def __init__(self, theOther: IGESDraw_ToolLabelDisplay) -> None: ...

    def ReadOwnParams(self, ent: IGESDraw_LabelDisplay | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDraw_LabelDisplay | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDraw_LabelDisplay | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a LabelDisplay <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDraw_LabelDisplay | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDraw_LabelDisplay | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDraw_LabelDisplay | None, entto: IGESDraw_LabelDisplay | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDraw_LabelDisplay | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDraw_ToolNetworkSubfigure:
    """
    Tool to work on a NetworkSubfigure. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolNetworkSubfigure, ready to work"""

    @overload
    def __init__(self, theOther: IGESDraw_ToolNetworkSubfigure) -> None: ...

    def ReadOwnParams(self, ent: IGESDraw_NetworkSubfigure | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDraw_NetworkSubfigure | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDraw_NetworkSubfigure | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a NetworkSubfigure <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDraw_NetworkSubfigure | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDraw_NetworkSubfigure | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDraw_NetworkSubfigure | None, entto: IGESDraw_NetworkSubfigure | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDraw_NetworkSubfigure | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDraw_ToolNetworkSubfigureDef:
    """
    Tool to work on a NetworkSubfigureDef. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolNetworkSubfigureDef, ready to work"""

    @overload
    def __init__(self, theOther: IGESDraw_ToolNetworkSubfigureDef) -> None: ...

    def ReadOwnParams(self, ent: IGESDraw_NetworkSubfigureDef | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDraw_NetworkSubfigureDef | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDraw_NetworkSubfigureDef | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a NetworkSubfigureDef <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDraw_NetworkSubfigureDef | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDraw_NetworkSubfigureDef | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDraw_NetworkSubfigureDef | None, entto: IGESDraw_NetworkSubfigureDef | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDraw_NetworkSubfigureDef | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDraw_ToolPerspectiveView:
    """
    Tool to work on a PerspectiveView. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolPerspectiveView, ready to work"""

    @overload
    def __init__(self, theOther: IGESDraw_ToolPerspectiveView) -> None: ...

    def ReadOwnParams(self, ent: IGESDraw_PerspectiveView | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDraw_PerspectiveView | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDraw_PerspectiveView | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a PerspectiveView <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDraw_PerspectiveView | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDraw_PerspectiveView | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDraw_PerspectiveView | None, entto: IGESDraw_PerspectiveView | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDraw_PerspectiveView | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDraw_ToolPlanar:
    """
    Tool to work on a Planar. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolPlanar, ready to work"""

    @overload
    def __init__(self, theOther: IGESDraw_ToolPlanar) -> None: ...

    def ReadOwnParams(self, ent: IGESDraw_Planar | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDraw_Planar | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDraw_Planar | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Planar <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESDraw_Planar | None) -> bool:
        """
        Sets automatic unambiguous Correction on a Planar
        (NbMatrices forced to 1)
        """

    def DirChecker(self, ent: IGESDraw_Planar | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDraw_Planar | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDraw_Planar | None, entto: IGESDraw_Planar | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDraw_Planar | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDraw_ToolRectArraySubfigure:
    """
    Tool to work on a RectArraySubfigure. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolRectArraySubfigure, ready to work"""

    @overload
    def __init__(self, theOther: IGESDraw_ToolRectArraySubfigure) -> None: ...

    def ReadOwnParams(self, ent: IGESDraw_RectArraySubfigure | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDraw_RectArraySubfigure | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDraw_RectArraySubfigure | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a RectArraySubfigure <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDraw_RectArraySubfigure | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDraw_RectArraySubfigure | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDraw_RectArraySubfigure | None, entto: IGESDraw_RectArraySubfigure | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDraw_RectArraySubfigure | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDraw_ToolSegmentedViewsVisible:
    """
    Tool to work on a SegmentedViewsVisible. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSegmentedViewsVisible, ready to work"""

    @overload
    def __init__(self, theOther: IGESDraw_ToolSegmentedViewsVisible) -> None: ...

    def ReadOwnParams(self, ent: IGESDraw_SegmentedViewsVisible | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDraw_SegmentedViewsVisible | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDraw_SegmentedViewsVisible | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a SegmentedViewsVisible <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDraw_SegmentedViewsVisible | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDraw_SegmentedViewsVisible | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDraw_SegmentedViewsVisible | None, entto: IGESDraw_SegmentedViewsVisible | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDraw_SegmentedViewsVisible | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDraw_ToolView:
    """
    Tool to work on a View. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolView, ready to work"""

    @overload
    def __init__(self, theOther: IGESDraw_ToolView) -> None: ...

    def ReadOwnParams(self, ent: IGESDraw_View | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDraw_View | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDraw_View | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a View <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESDraw_View | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDraw_View | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDraw_View | None, entto: IGESDraw_View | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESDraw_View | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESDraw_ToolViewsVisible:
    """
    Tool to work on a ViewsVisible. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolViewsVisible, ready to work"""

    @overload
    def __init__(self, theOther: IGESDraw_ToolViewsVisible) -> None: ...

    def ReadOwnParams(self, ent: IGESDraw_ViewsVisible | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDraw_ViewsVisible | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDraw_ViewsVisible | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ViewsVisible <ent>, from
        its specific (own) parameters shared not implied (the Views)
        """

    def OwnImplied(self, ent: IGESDraw_ViewsVisible | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ViewsVisible <ent>, from
        its specific (own) implied parameters : the Displayed Entities
        """

    def DirChecker(self, ent: IGESDraw_ViewsVisible | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDraw_ViewsVisible | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDraw_ViewsVisible | None, entto: IGESDraw_ViewsVisible | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Copies Specific Parameters shared not implied, i.e. all but
        the Displayed Entities
        """

    def OwnRenew(self, entfrom: IGESDraw_ViewsVisible | None, entto: IGESDraw_ViewsVisible | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Copies Specific implied Parameters : the Displayed Entities
        which have already been copied
        """

    def OwnWhenDelete(self, ent: IGESDraw_ViewsVisible | None) -> None:
        """
        Clears specific implied parameters, which cause looping
        structures; required for deletion
        """

    def OwnDump(self, ent: IGESDraw_ViewsVisible | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

    def OwnCorrect(self, ent: IGESDraw_ViewsVisible | None) -> bool:
        """
        Sets automatic unambiguous Correction on a ViewsVisible
        (all displayed entities must refer to <ent> in directory part,
        else the list is cleared)
        """

class IGESDraw_ToolViewsVisibleWithAttr:
    """
    Tool to work on a ViewsVisibleWithAttr. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolViewsVisibleWithAttr, ready to work"""

    @overload
    def __init__(self, theOther: IGESDraw_ToolViewsVisibleWithAttr) -> None: ...

    def ReadOwnParams(self, ent: IGESDraw_ViewsVisibleWithAttr | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESDraw_ViewsVisibleWithAttr | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESDraw_ViewsVisibleWithAttr | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ViewsVisibleWithAttr <ent>, from
        its specific (own) parameters shared not implied, i.e. all but
        the Displayed Entities
        """

    def OwnImplied(self, ent: IGESDraw_ViewsVisibleWithAttr | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ViewsVisible <ent>, from
        its specific (own) implied parameters : the Displayed Entities
        """

    def DirChecker(self, ent: IGESDraw_ViewsVisibleWithAttr | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESDraw_ViewsVisibleWithAttr | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESDraw_ViewsVisibleWithAttr | None, entto: IGESDraw_ViewsVisibleWithAttr | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Copies Specific Parameters shared not implied, i.e. all but
        the Displayed Entities
        """

    def OwnRenew(self, entfrom: IGESDraw_ViewsVisibleWithAttr | None, entto: IGESDraw_ViewsVisibleWithAttr | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """
        Copies Specific implied Parameters : the Displayed Entities
        which have already been copied
        """

    def OwnWhenDelete(self, ent: IGESDraw_ViewsVisibleWithAttr | None) -> None:
        """
        Clears specific implied parameters, which cause looping
        structures; required for deletion
        """

    def OwnDump(self, ent: IGESDraw_ViewsVisibleWithAttr | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

    def OwnCorrect(self, ent: IGESDraw_ViewsVisibleWithAttr | None) -> bool:
        """
        Sets automatic unambiguous Correction on a ViewsVisibleWithAttr
        (all displayed entities must refer to <ent> in directory part,
        else the list is cleared)
        """

class IGESDraw_View(nanoocp.IGESData.IGESData_ViewKindEntity):
    """
    defines IGES View Entity, Type <410> Form <0>
    in package IGESDraw

    Used to define a framework for specifying a viewing
    orientation of an object in three dimensional model
    space (X,Y,Z). The framework is also used to support
    the projection of all or part of model space onto a
    view volume.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw_View) -> None: ...

    def Init(self, aViewNum: int, aScale: float, aLeftPlane: nanoocp.IGESGeom.IGESGeom_Plane | None, aTopPlane: nanoocp.IGESGeom.IGESGeom_Plane | None, aRightPlane: nanoocp.IGESGeom.IGESGeom_Plane | None, aBottomPlane: nanoocp.IGESGeom.IGESGeom_Plane | None, aBackPlane: nanoocp.IGESGeom.IGESGeom_Plane | None, aFrontPlane: nanoocp.IGESGeom.IGESGeom_Plane | None) -> None:
        """
        This method is used to set fields of the class View
        - aViewNum     : View number
        - aScale       : Scale factor
        - aLeftPlane   : Left   plane of view volume
        - aTopPlane    : Top    plane of view volume
        - aRightPlane  : Right  plane of view volume
        - aBottomPlane : Bottom plane of view volume
        - aBackPlane   : Back   plane of view volume
        - aFrontPlane  : Front  plane of view volume
        """

    def IsSingle(self) -> bool:
        """Returns True (for a single view)"""

    def NbViews(self) -> int:
        """Returns 1 (single view)"""

    def ViewItem(self, num: int) -> nanoocp.IGESData.IGESData_ViewKindEntity:
        """For a single view, returns <me> whatever <num>"""

    def ViewNumber(self) -> int:
        """returns integer number identifying view orientation"""

    def ScaleFactor(self) -> float:
        """returns the scale factor(Default = 1.0)"""

    def HasLeftPlane(self) -> bool:
        """returns False if left side of view volume is not present"""

    def LeftPlane(self) -> nanoocp.IGESGeom.IGESGeom_Plane:
        """returns the left side of view volume, or null handle"""

    def HasTopPlane(self) -> bool:
        """returns False if top of view volume is not present"""

    def TopPlane(self) -> nanoocp.IGESGeom.IGESGeom_Plane:
        """returns the top of view volume, or null handle"""

    def HasRightPlane(self) -> bool:
        """returns False if right side of view volume is not present"""

    def RightPlane(self) -> nanoocp.IGESGeom.IGESGeom_Plane:
        """returns the right side of view volume, or null handle"""

    def HasBottomPlane(self) -> bool:
        """returns False if bottom of view volume is not present"""

    def BottomPlane(self) -> nanoocp.IGESGeom.IGESGeom_Plane:
        """returns the bottom of view volume, or null handle"""

    def HasBackPlane(self) -> bool:
        """returns False if back of view volume is not present"""

    def BackPlane(self) -> nanoocp.IGESGeom.IGESGeom_Plane:
        """returns the back of view volume, or null handle"""

    def HasFrontPlane(self) -> bool:
        """returns False if front of view volume is not present"""

    def FrontPlane(self) -> nanoocp.IGESGeom.IGESGeom_Plane:
        """returns the front of view volume, or null handle"""

    def ViewMatrix(self) -> nanoocp.IGESData.IGESData_TransfEntity:
        """returns the Transformation Matrix"""

    def ModelToView(self, coords: nanoocp.gp.gp_XYZ) -> nanoocp.gp.gp_XYZ:
        """
        returns XYZ from the Model space to the View space by
        applying the View Matrix
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_ViewsVisible(nanoocp.IGESData.IGESData_ViewKindEntity):
    """
    Defines IGESViewsVisible, Type <402>, Form <3>
    in package IGESDraw

    If an entity is to be displayed in more than one views,
    this class instance is used, which contains the Visible
    views and the associated entity Displays.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw_ViewsVisible) -> None: ...

    def Init(self, allViewEntities: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_ViewKindEntity] | None, allDisplayEntity: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """
        This method is used to set the fields of the class
        ViewsVisible
        - allViewEntities  : All View kind entities
        - allDisplayEntity : All entities whose display is specified
        """

    def InitImplied(self, allDisplayEntity: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """Changes only the list of Displayed Entities (Null allowed)"""

    def IsSingle(self) -> bool:
        """Returns False (for a complex view)"""

    def NbViews(self) -> int:
        """returns the Number of views visible"""

    def NbDisplayedEntities(self) -> int:
        """
        returns the number of entities displayed in the Views or zero if
        no Entities specified in these Views
        """

    def ViewItem(self, Index: int) -> nanoocp.IGESData.IGESData_ViewKindEntity:
        """
        returns the Index'th ViewKindEntity Entity
        raises exception if Index <= 0 or Index > NbViewsVisible()
        """

    def DisplayedEntity(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the Index'th entity whose display is being specified by
        this associativity instance
        raises exception if Index <= 0 or Index > NbEntityDisplayed()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESDraw_ViewsVisibleWithAttr(nanoocp.IGESData.IGESData_ViewKindEntity):
    """
    defines IGESViewsVisibleWithAttr, Type <402>, Form <4>
    in package IGESDraw

    This class is extension of Class ViewsVisible. It is used
    for those entities that are visible in multiple views, but
    must have a different line font, color number, or
    line weight in each view.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESDraw_ViewsVisibleWithAttr) -> None: ...

    def Init(self, allViewEntities: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_ViewKindEntity] | None, allLineFonts: nanoocp.NCollection.NCollection_HArray1[int] | None, allLineDefinitions: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_LineFontEntity] | None, allColorValues: nanoocp.NCollection.NCollection_HArray1[int] | None, allColorDefinitions: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGraph.IGESGraph_Color] | None, allLineWeights: nanoocp.NCollection.NCollection_HArray1[int] | None, allDisplayEntities: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """
        This method is used to set fields of the class
        ViewsVisibleWithAttr
        - allViewEntities     : All View kind entities
        - allLineFonts        : All Line Font values or zero(0)
        - allLineDefinitions  : Line Font Definition
        (if Line Font value = 0)
        - allColorValues      : All Color values
        - allColorDefinitions : All Color Definition Entities
        - allLineWeights      : All Line Weight values
        - allDisplayEntities  : Entities which are member of
        this associativity
        raises exception if Lengths of allViewEntities, allLineFonts,
        allColorValues,allColorDefinitions, allLineWeights are not same
        """

    def InitImplied(self, allDisplayEntity: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """Changes only the list of Displayed Entities (Null allowed)"""

    def IsSingle(self) -> bool:
        """Returns False (for a complex view)"""

    def NbViews(self) -> int:
        """
        returns the number of Views containing the view visible, line font,
        color number, and line weight information
        """

    def NbDisplayedEntities(self) -> int:
        """
        returns the number of entities which have this particular set of
        display characteristic, or zero if no Entities specified
        """

    def ViewItem(self, Index: int) -> nanoocp.IGESData.IGESData_ViewKindEntity:
        """
        returns the Index'th ViewKindEntity entity
        raises exception if Index <= 0 or Index > NbViews()
        """

    def LineFontValue(self, Index: int) -> int:
        """
        returns the Index'th Line font value or zero
        raises exception if Index <= 0 or Index > NbViews()
        """

    def IsFontDefinition(self, Index: int) -> bool:
        """
        returns True if the Index'th Line Font Definition is specified
        else returns False
        raises exception if Index <= 0 or Index > NbViews()
        """

    def FontDefinition(self, Index: int) -> nanoocp.IGESData.IGESData_LineFontEntity:
        """
        returns the Index'th Line Font Definition Entity or NULL(0)
        raises exception if Index <= 0 or Index > NbViews()
        """

    def ColorValue(self, Index: int) -> int:
        """
        returns the Index'th Color number value
        raises exception if Index <= 0 or Index > NbViews()
        """

    def IsColorDefinition(self, Index: int) -> bool:
        """
        returns True if Index'th Color Definition is specified
        else returns False
        raises exception if Index <= 0 or Index > NbViews()
        """

    def ColorDefinition(self, Index: int) -> nanoocp.IGESGraph.IGESGraph_Color:
        """
        returns the Index'th Color Definition Entity
        raises exception if Index <= 0 or Index > NbViews()
        """

    def LineWeightItem(self, Index: int) -> int:
        """
        returns the Index'th Color Line Weight
        raises exception if Index <= 0 or Index > NbViews()
        """

    def DisplayedEntity(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns Index'th Display entity with this particular characteristics
        raises exception if Index <= 0 or Index > NbEntities()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.IGESDraw
IGESDraw_Array1OfConnectPoint = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESDraw.IGESDraw_ConnectPoint]
IGESDraw_Array1OfViewKindEntity = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESData.IGESData_ViewKindEntity]
IGESDraw_HArray1OfConnectPoint = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESDraw.IGESDraw_ConnectPoint]
IGESDraw_HArray1OfViewKindEntity = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_ViewKindEntity]
