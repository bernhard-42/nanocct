"""OCCT package StepShape (toolkit TKDESTEP)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepBasic
import nanoocp.StepData
import nanoocp.StepGeom
import nanoocp.StepRepr
import nanoocp.TCollection


class StepShape_AngleRelator(enum.IntEnum):
    StepShape_Equal = 0

    StepShape_Large = 1

    StepShape_Small = 2

StepShape_Equal: StepShape_AngleRelator = StepShape_AngleRelator.StepShape_Equal

StepShape_Large: StepShape_AngleRelator = StepShape_AngleRelator.StepShape_Large

StepShape_Small: StepShape_AngleRelator = StepShape_AngleRelator.StepShape_Small

class StepShape_BooleanOperator(enum.IntEnum):
    StepShape_boDifference = 0

    StepShape_boIntersection = 1

    StepShape_boUnion = 2

StepShape_boDifference: StepShape_BooleanOperator = StepShape_BooleanOperator.StepShape_boDifference

StepShape_boIntersection: StepShape_BooleanOperator = ...

StepShape_boUnion: StepShape_BooleanOperator = StepShape_BooleanOperator.StepShape_boUnion

class StepShape_ShapeRepresentation(nanoocp.StepRepr.StepRepr_Representation):
    @overload
    def __init__(self) -> None:
        """Returns a ShapeRepresentation"""

    @overload
    def __init__(self, theOther: StepShape_ShapeRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_AdvancedBrepShapeRepresentation(StepShape_ShapeRepresentation):
    @overload
    def __init__(self) -> None:
        """Returns a AdvancedBrepShapeRepresentation"""

    @overload
    def __init__(self, theOther: StepShape_AdvancedBrepShapeRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_TopologicalRepresentationItem(nanoocp.StepRepr.StepRepr_RepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a TopologicalRepresentationItem"""

    @overload
    def __init__(self, theOther: StepShape_TopologicalRepresentationItem) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_FaceBound(StepShape_TopologicalRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a FaceBound"""

    @overload
    def __init__(self, theOther: StepShape_FaceBound) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aBound: StepShape_Loop | None, aOrientation: bool) -> None: ...

    def SetBound(self, aBound: StepShape_Loop | None) -> None: ...

    def Bound(self) -> StepShape_Loop: ...

    def SetOrientation(self, aOrientation: bool) -> None: ...

    def Orientation(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_Face(StepShape_TopologicalRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a Face"""

    @overload
    def __init__(self, theOther: StepShape_Face) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aBounds: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_FaceBound] | None) -> None: ...

    def SetBounds(self, aBounds: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_FaceBound] | None) -> None: ...

    def Bounds(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_FaceBound]: ...

    def BoundsValue(self, num: int) -> StepShape_FaceBound: ...

    def NbBounds(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_FaceSurface(StepShape_Face):
    @overload
    def __init__(self) -> None:
        """Returns a FaceSurface"""

    @overload
    def __init__(self, theOther: StepShape_FaceSurface) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aBounds: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_FaceBound] | None, aFaceGeometry: nanoocp.StepGeom.StepGeom_Surface | None, aSameSense: bool) -> None: ...

    def SetFaceGeometry(self, aFaceGeometry: nanoocp.StepGeom.StepGeom_Surface | None) -> None: ...

    def FaceGeometry(self) -> nanoocp.StepGeom.StepGeom_Surface: ...

    def SetSameSense(self, aSameSense: bool) -> None: ...

    def SameSense(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_AdvancedFace(StepShape_FaceSurface):
    @overload
    def __init__(self) -> None:
        """Returns a AdvancedFace"""

    @overload
    def __init__(self, theOther: StepShape_AdvancedFace) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_DimensionalLocation(nanoocp.StepRepr.StepRepr_ShapeAspectRelationship):
    """Representation of STEP entity DimensionalLocation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_DimensionalLocation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_AngularLocation(StepShape_DimensionalLocation):
    """Representation of STEP entity AngularLocation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_AngularLocation) -> None: ...

    def Init(self, aShapeAspectRelationship_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasShapeAspectRelationship_Description: bool, aShapeAspectRelationship_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aShapeAspectRelationship_RelatingShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None, aShapeAspectRelationship_RelatedShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None, aAngleSelection: StepShape_AngleRelator) -> None:
        """Initialize all fields (own and inherited)"""

    def AngleSelection(self) -> StepShape_AngleRelator:
        """Returns field AngleSelection"""

    def SetAngleSelection(self, AngleSelection: StepShape_AngleRelator) -> None:
        """Set field AngleSelection"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_DimensionalSize(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity DimensionalSize"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_DimensionalSize) -> None: ...

    def Init(self, aAppliesTo: nanoocp.StepRepr.StepRepr_ShapeAspect | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def AppliesTo(self) -> nanoocp.StepRepr.StepRepr_ShapeAspect:
        """Returns field AppliesTo"""

    def SetAppliesTo(self, AppliesTo: nanoocp.StepRepr.StepRepr_ShapeAspect | None) -> None:
        """Set field AppliesTo"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_AngularSize(StepShape_DimensionalSize):
    """Representation of STEP entity AngularSize"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_AngularSize) -> None: ...

    def Init(self, aDimensionalSize_AppliesTo: nanoocp.StepRepr.StepRepr_ShapeAspect | None, aDimensionalSize_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aAngleSelection: StepShape_AngleRelator) -> None:
        """Initialize all fields (own and inherited)"""

    def AngleSelection(self) -> StepShape_AngleRelator:
        """Returns field AngleSelection"""

    def SetAngleSelection(self, AngleSelection: StepShape_AngleRelator) -> None:
        """Set field AngleSelection"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_Block(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a Block"""

    @overload
    def __init__(self, theOther: StepShape_Block) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aPosition: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None, aX: float, aY: float, aZ: float) -> None: ...

    def SetPosition(self, aPosition: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None) -> None: ...

    def Position(self) -> nanoocp.StepGeom.StepGeom_Axis2Placement3d: ...

    def SetX(self, aX: float) -> None: ...

    def X(self) -> float: ...

    def SetY(self, aY: float) -> None: ...

    def Y(self) -> float: ...

    def SetZ(self, aZ: float) -> None: ...

    def Z(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_CsgPrimitive(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a CsgPrimitive SelectType"""

    @overload
    def __init__(self, theOther: StepShape_CsgPrimitive) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a CsgPrimitive Kind Entity that is :
        1 -> Sphere
        2 -> Block
        3 -> RightAngularWedge
        4 -> Torus
        5 -> RightCircularCone
        6 -> RightCircularCylinder
        0 else
        """

    def Sphere(self) -> StepShape_Sphere:
        """returns Value as a Sphere (Null if another type)"""

    def Block(self) -> StepShape_Block:
        """returns Value as a Block (Null if another type)"""

    def RightAngularWedge(self) -> StepShape_RightAngularWedge:
        """returns Value as a RightAngularWedge (Null if another type)"""

    def Torus(self) -> StepShape_Torus:
        """returns Value as a Torus (Null if another type)"""

    def RightCircularCone(self) -> StepShape_RightCircularCone:
        """returns Value as a RightCircularCone (Null if another type)"""

    def RightCircularCylinder(self) -> StepShape_RightCircularCylinder:
        """returns Value as a RightCircularCylinder (Null if another type)"""

class StepShape_BooleanOperand:
    @overload
    def __init__(self) -> None:
        """Returns a BooleanOperand SelectType"""

    @overload
    def __init__(self, theOther: StepShape_BooleanOperand) -> None: ...

    def SetTypeOfContent(self, aTypeOfContent: int) -> None: ...

    def TypeOfContent(self) -> int: ...

    def SolidModel(self) -> StepShape_SolidModel:
        """
        returns Value as a SolidModel (Null if another
        type)
        """

    def SetSolidModel(self, aSolidModel: StepShape_SolidModel | None) -> None: ...

    def HalfSpaceSolid(self) -> StepShape_HalfSpaceSolid:
        """
        returns Value as a HalfSpaceSolid (Null if
        another type)
        """

    def SetHalfSpaceSolid(self, aHalfSpaceSolid: StepShape_HalfSpaceSolid | None) -> None: ...

    def CsgPrimitive(self) -> StepShape_CsgPrimitive:
        """
        returns Value as a CsgPrimitive (Null if another
        type)
        CsgPrimitive is another Select Type
        """

    def SetCsgPrimitive(self, aCsgPrimitive: StepShape_CsgPrimitive) -> None: ...

    def BooleanResult(self) -> StepShape_BooleanResult:
        """
        returns Value as a BooleanResult (Null if another
        type)
        """

    def SetBooleanResult(self, aBooleanResult: StepShape_BooleanResult | None) -> None: ...

class StepShape_BooleanResult(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a BooleanResult"""

    @overload
    def __init__(self, theOther: StepShape_BooleanResult) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aOperator: StepShape_BooleanOperator, aFirstOperand: StepShape_BooleanOperand, aSecondOperand: StepShape_BooleanOperand) -> None: ...

    def SetOperator(self, aOperator: StepShape_BooleanOperator) -> None: ...

    def Operator(self) -> StepShape_BooleanOperator: ...

    def SetFirstOperand(self, aFirstOperand: StepShape_BooleanOperand) -> None: ...

    def FirstOperand(self) -> StepShape_BooleanOperand: ...

    def SetSecondOperand(self, aSecondOperand: StepShape_BooleanOperand) -> None: ...

    def SecondOperand(self) -> StepShape_BooleanOperand: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_BoxDomain(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a BoxDomain"""

    @overload
    def __init__(self, theOther: StepShape_BoxDomain) -> None: ...

    def Init(self, aCorner: nanoocp.StepGeom.StepGeom_CartesianPoint | None, aXlength: float, aYlength: float, aZlength: float) -> None: ...

    def SetCorner(self, aCorner: nanoocp.StepGeom.StepGeom_CartesianPoint | None) -> None: ...

    def Corner(self) -> nanoocp.StepGeom.StepGeom_CartesianPoint: ...

    def SetXlength(self, aXlength: float) -> None: ...

    def Xlength(self) -> float: ...

    def SetYlength(self, aYlength: float) -> None: ...

    def Ylength(self) -> float: ...

    def SetZlength(self, aZlength: float) -> None: ...

    def Zlength(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_HalfSpaceSolid(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a HalfSpaceSolid"""

    @overload
    def __init__(self, theOther: StepShape_HalfSpaceSolid) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aBaseSurface: nanoocp.StepGeom.StepGeom_Surface | None, aAgreementFlag: bool) -> None: ...

    def SetBaseSurface(self, aBaseSurface: nanoocp.StepGeom.StepGeom_Surface | None) -> None: ...

    def BaseSurface(self) -> nanoocp.StepGeom.StepGeom_Surface: ...

    def SetAgreementFlag(self, aAgreementFlag: bool) -> None: ...

    def AgreementFlag(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_BoxedHalfSpace(StepShape_HalfSpaceSolid):
    @overload
    def __init__(self) -> None:
        """Returns a BoxedHalfSpace"""

    @overload
    def __init__(self, theOther: StepShape_BoxedHalfSpace) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aBaseSurface: nanoocp.StepGeom.StepGeom_Surface | None, aAgreementFlag: bool, aEnclosure: StepShape_BoxDomain | None) -> None: ...

    def SetEnclosure(self, aEnclosure: StepShape_BoxDomain | None) -> None: ...

    def Enclosure(self) -> StepShape_BoxDomain: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ConnectedFaceSet(StepShape_TopologicalRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a ConnectedFaceSet"""

    @overload
    def __init__(self, theOther: StepShape_ConnectedFaceSet) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aCfsFaces: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Face] | None) -> None: ...

    def SetCfsFaces(self, aCfsFaces: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Face] | None) -> None: ...

    def CfsFaces(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Face]: ...

    def CfsFacesValue(self, num: int) -> StepShape_Face: ...

    def NbCfsFaces(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ClosedShell(StepShape_ConnectedFaceSet):
    @overload
    def __init__(self) -> None:
        """Returns a ClosedShell"""

    @overload
    def __init__(self, theOther: StepShape_ClosedShell) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_OrientedClosedShell(StepShape_ClosedShell):
    @overload
    def __init__(self) -> None:
        """Returns a OrientedClosedShell"""

    @overload
    def __init__(self, theOther: StepShape_OrientedClosedShell) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aClosedShellElement: StepShape_ClosedShell | None, aOrientation: bool) -> None: ...

    def SetClosedShellElement(self, aClosedShellElement: StepShape_ClosedShell | None) -> None: ...

    def ClosedShellElement(self) -> StepShape_ClosedShell: ...

    def SetOrientation(self, aOrientation: bool) -> None: ...

    def Orientation(self) -> bool: ...

    def SetCfsFaces(self, aCfsFaces: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Face] | None) -> None: ...

    def CfsFaces(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Face]: ...

    def CfsFacesValue(self, num: int) -> StepShape_Face: ...

    def NbCfsFaces(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_SolidModel(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a SolidModel"""

    @overload
    def __init__(self, theOther: StepShape_SolidModel) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ManifoldSolidBrep(StepShape_SolidModel):
    @overload
    def __init__(self) -> None:
        """Returns a ManifoldSolidBrep"""

    @overload
    def __init__(self, theOther: StepShape_ManifoldSolidBrep) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aOuter: StepShape_ClosedShell | None) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aOuter: StepShape_ConnectedFaceSet | None) -> None: ...

    def SetOuter(self, aOuter: StepShape_ConnectedFaceSet | None) -> None: ...

    def Outer(self) -> StepShape_ConnectedFaceSet: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_BrepWithVoids(StepShape_ManifoldSolidBrep):
    @overload
    def __init__(self) -> None:
        """Returns a BrepWithVoids"""

    @overload
    def __init__(self, theOther: StepShape_BrepWithVoids) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aOuter: StepShape_ClosedShell | None, aVoids: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedClosedShell] | None) -> None: ...

    def SetVoids(self, aVoids: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedClosedShell] | None) -> None: ...

    def Voids(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedClosedShell]: ...

    def VoidsValue(self, num: int) -> StepShape_OrientedClosedShell: ...

    def NbVoids(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_CompoundShapeRepresentation(StepShape_ShapeRepresentation):
    """Representation of STEP entity CompoundShapeRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_CompoundShapeRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_Vertex(StepShape_TopologicalRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a Vertex"""

    @overload
    def __init__(self, theOther: StepShape_Vertex) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_Edge(StepShape_TopologicalRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a Edge"""

    @overload
    def __init__(self, theOther: StepShape_Edge) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aEdgeStart: StepShape_Vertex | None, aEdgeEnd: StepShape_Vertex | None) -> None: ...

    def SetEdgeStart(self, aEdgeStart: StepShape_Vertex | None) -> None: ...

    def EdgeStart(self) -> StepShape_Vertex: ...

    def SetEdgeEnd(self, aEdgeEnd: StepShape_Vertex | None) -> None: ...

    def EdgeEnd(self) -> StepShape_Vertex: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ConnectedEdgeSet(StepShape_TopologicalRepresentationItem):
    """Representation of STEP entity ConnectedEdgeSet"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_ConnectedEdgeSet) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aCesEdges: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Edge] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def CesEdges(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Edge]:
        """Returns field CesEdges"""

    def SetCesEdges(self, CesEdges: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Edge] | None) -> None:
        """Set field CesEdges"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ConnectedFaceShapeRepresentation(nanoocp.StepRepr.StepRepr_Representation):
    """Representation of STEP entity ConnectedFaceShapeRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_ConnectedFaceShapeRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ConnectedFaceSubSet(StepShape_ConnectedFaceSet):
    """Representation of STEP entity ConnectedFaceSubSet"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_ConnectedFaceSubSet) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aConnectedFaceSet_CfsFaces: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Face] | None, aParentFaceSet: StepShape_ConnectedFaceSet | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ParentFaceSet(self) -> StepShape_ConnectedFaceSet:
        """Returns field ParentFaceSet"""

    def SetParentFaceSet(self, ParentFaceSet: StepShape_ConnectedFaceSet | None) -> None:
        """Set field ParentFaceSet"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ContextDependentShapeRepresentation(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepShape_ContextDependentShapeRepresentation) -> None: ...

    def Init(self, aRepRel: nanoocp.StepRepr.StepRepr_ShapeRepresentationRelationship | None, aProRel: nanoocp.StepRepr.StepRepr_ProductDefinitionShape | None) -> None: ...

    def RepresentationRelation(self) -> nanoocp.StepRepr.StepRepr_ShapeRepresentationRelationship: ...

    def SetRepresentationRelation(self, aRepRel: nanoocp.StepRepr.StepRepr_ShapeRepresentationRelationship | None) -> None: ...

    def RepresentedProductRelation(self) -> nanoocp.StepRepr.StepRepr_ProductDefinitionShape: ...

    def SetRepresentedProductRelation(self, aProRel: nanoocp.StepRepr.StepRepr_ProductDefinitionShape | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_CsgSelect:
    @overload
    def __init__(self) -> None:
        """Returns a CsgSelect SelectType"""

    @overload
    def __init__(self, theOther: StepShape_CsgSelect) -> None: ...

    def SetTypeOfContent(self, aTypeOfContent: int) -> None: ...

    def TypeOfContent(self) -> int: ...

    def BooleanResult(self) -> StepShape_BooleanResult:
        """returns Value as a BooleanResult (Null if another type)"""

    def SetBooleanResult(self, aBooleanResult: StepShape_BooleanResult | None) -> None: ...

    def CsgPrimitive(self) -> StepShape_CsgPrimitive:
        """returns Value as a CsgPrimitive (Null if another type)"""

    def SetCsgPrimitive(self, aCsgPrimitive: StepShape_CsgPrimitive) -> None: ...

class StepShape_CsgShapeRepresentation(StepShape_ShapeRepresentation):
    @overload
    def __init__(self) -> None:
        """Returns a CsgShapeRepresentation"""

    @overload
    def __init__(self, theOther: StepShape_CsgShapeRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_CsgSolid(StepShape_SolidModel):
    @overload
    def __init__(self) -> None:
        """Returns a CsgSolid"""

    @overload
    def __init__(self, theOther: StepShape_CsgSolid) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aTreeRootExpression: StepShape_CsgSelect) -> None: ...

    def SetTreeRootExpression(self, aTreeRootExpression: StepShape_CsgSelect) -> None: ...

    def TreeRootExpression(self) -> StepShape_CsgSelect: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_DefinitionalRepresentationAndShapeRepresentation(nanoocp.StepRepr.StepRepr_DefinitionalRepresentation):
    """
    Implements complex type
    (DEFINITIONAL_REPRESENTATION,REPRESENTATION,SHAPE_REPRESENTATION)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepShape_DefinitionalRepresentationAndShapeRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_DimensionalCharacteristic(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type DimensionalCharacteristic"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_DimensionalCharacteristic) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of DimensionalCharacteristic select type
        1 -> DimensionalLocation from StepShape
        2 -> DimensionalSize from StepShape
        0 else
        """

    def DimensionalLocation(self) -> StepShape_DimensionalLocation:
        """Returns Value as DimensionalLocation (or Null if another type)"""

    def DimensionalSize(self) -> StepShape_DimensionalSize:
        """Returns Value as DimensionalSize (or Null if another type)"""

class StepShape_DimensionalCharacteristicRepresentation(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity DimensionalCharacteristicRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_DimensionalCharacteristicRepresentation) -> None: ...

    def Init(self, aDimension: StepShape_DimensionalCharacteristic, aRepresentation: StepShape_ShapeDimensionRepresentation | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Dimension(self) -> StepShape_DimensionalCharacteristic:
        """Returns field Dimension"""

    def SetDimension(self, Dimension: StepShape_DimensionalCharacteristic) -> None:
        """Set field Dimension"""

    def Representation(self) -> StepShape_ShapeDimensionRepresentation:
        """Returns field Representation"""

    def SetRepresentation(self, Representation: StepShape_ShapeDimensionRepresentation | None) -> None:
        """Set field Representation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_DimensionalLocationWithPath(StepShape_DimensionalLocation):
    """Representation of STEP entity DimensionalLocationWithPath"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_DimensionalLocationWithPath) -> None: ...

    def Init(self, aShapeAspectRelationship_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasShapeAspectRelationship_Description: bool, aShapeAspectRelationship_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aShapeAspectRelationship_RelatingShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None, aShapeAspectRelationship_RelatedShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None, aPath: nanoocp.StepRepr.StepRepr_ShapeAspect | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Path(self) -> nanoocp.StepRepr.StepRepr_ShapeAspect:
        """Returns field Path"""

    def SetPath(self, Path: nanoocp.StepRepr.StepRepr_ShapeAspect | None) -> None:
        """Set field Path"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_DimensionalSizeWithPath(StepShape_DimensionalSize):
    """Representation of STEP entity DimensionalSizeWithPath"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_DimensionalSizeWithPath) -> None: ...

    def Init(self, aDimensionalSize_AppliesTo: nanoocp.StepRepr.StepRepr_ShapeAspect | None, aDimensionalSize_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aPath: nanoocp.StepRepr.StepRepr_ShapeAspect | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Path(self) -> nanoocp.StepRepr.StepRepr_ShapeAspect:
        """Returns field Path"""

    def SetPath(self, Path: nanoocp.StepRepr.StepRepr_ShapeAspect | None) -> None:
        """Set field Path"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_DirectedDimensionalLocation(StepShape_DimensionalLocation):
    """Representation of STEP entity DirectedDimensionalLocation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_DirectedDimensionalLocation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_EdgeBasedWireframeModel(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    """Representation of STEP entity EdgeBasedWireframeModel"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_EdgeBasedWireframeModel) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aEbwmBoundary: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ConnectedEdgeSet] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def EbwmBoundary(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ConnectedEdgeSet]:
        """Returns field EbwmBoundary"""

    def SetEbwmBoundary(self, EbwmBoundary: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ConnectedEdgeSet] | None) -> None:
        """Set field EbwmBoundary"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_EdgeBasedWireframeShapeRepresentation(StepShape_ShapeRepresentation):
    """Representation of STEP entity EdgeBasedWireframeShapeRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_EdgeBasedWireframeShapeRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_EdgeCurve(StepShape_Edge):
    @overload
    def __init__(self) -> None:
        """Returns a EdgeCurve"""

    @overload
    def __init__(self, theOther: StepShape_EdgeCurve) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aEdgeStart: StepShape_Vertex | None, aEdgeEnd: StepShape_Vertex | None, aEdgeGeometry: nanoocp.StepGeom.StepGeom_Curve | None, aSameSense: bool) -> None: ...

    def SetEdgeGeometry(self, aEdgeGeometry: nanoocp.StepGeom.StepGeom_Curve | None) -> None: ...

    def EdgeGeometry(self) -> nanoocp.StepGeom.StepGeom_Curve: ...

    def SetSameSense(self, aSameSense: bool) -> None: ...

    def SameSense(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_OrientedEdge(StepShape_Edge):
    @overload
    def __init__(self) -> None:
        """Returns a OrientedEdge"""

    @overload
    def __init__(self, theOther: StepShape_OrientedEdge) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aEdgeElement: StepShape_Edge | None, aOrientation: bool) -> None: ...

    def SetEdgeElement(self, aEdgeElement: StepShape_Edge | None) -> None: ...

    def EdgeElement(self) -> StepShape_Edge: ...

    def SetOrientation(self, aOrientation: bool) -> None: ...

    def Orientation(self) -> bool: ...

    def SetEdgeStart(self, aEdgeStart: StepShape_Vertex | None) -> None: ...

    def EdgeStart(self) -> StepShape_Vertex: ...

    def SetEdgeEnd(self, aEdgeEnd: StepShape_Vertex | None) -> None: ...

    def EdgeEnd(self) -> StepShape_Vertex: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_Loop(StepShape_TopologicalRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a Loop"""

    @overload
    def __init__(self, theOther: StepShape_Loop) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_EdgeLoop(StepShape_Loop):
    @overload
    def __init__(self) -> None:
        """Returns a EdgeLoop"""

    @overload
    def __init__(self, theOther: StepShape_EdgeLoop) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aEdgeList: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedEdge] | None) -> None: ...

    def SetEdgeList(self, aEdgeList: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedEdge] | None) -> None: ...

    def EdgeList(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedEdge]: ...

    def EdgeListValue(self, num: int) -> StepShape_OrientedEdge: ...

    def NbEdgeList(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_SweptAreaSolid(StepShape_SolidModel):
    @overload
    def __init__(self) -> None:
        """Returns a SweptAreaSolid"""

    @overload
    def __init__(self, theOther: StepShape_SweptAreaSolid) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aSweptArea: nanoocp.StepGeom.StepGeom_CurveBoundedSurface | None) -> None: ...

    def SetSweptArea(self, aSweptArea: nanoocp.StepGeom.StepGeom_CurveBoundedSurface | None) -> None: ...

    def SweptArea(self) -> nanoocp.StepGeom.StepGeom_CurveBoundedSurface: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ExtrudedAreaSolid(StepShape_SweptAreaSolid):
    @overload
    def __init__(self) -> None:
        """Returns a ExtrudedAreaSolid"""

    @overload
    def __init__(self, theOther: StepShape_ExtrudedAreaSolid) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aSweptArea: nanoocp.StepGeom.StepGeom_CurveBoundedSurface | None, aExtrudedDirection: nanoocp.StepGeom.StepGeom_Direction | None, aDepth: float) -> None: ...

    def SetExtrudedDirection(self, aExtrudedDirection: nanoocp.StepGeom.StepGeom_Direction | None) -> None: ...

    def ExtrudedDirection(self) -> nanoocp.StepGeom.StepGeom_Direction: ...

    def SetDepth(self, aDepth: float) -> None: ...

    def Depth(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_SweptFaceSolid(StepShape_SolidModel):
    @overload
    def __init__(self) -> None:
        """Returns a SweptFaceSolid"""

    @overload
    def __init__(self, theOther: StepShape_SweptFaceSolid) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aSweptArea: StepShape_FaceSurface | None) -> None: ...

    def SetSweptFace(self, aSweptArea: StepShape_FaceSurface | None) -> None: ...

    def SweptFace(self) -> StepShape_FaceSurface: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ExtrudedFaceSolid(StepShape_SweptFaceSolid):
    @overload
    def __init__(self) -> None:
        """Returns a ExtrudedFaceSolid"""

    @overload
    def __init__(self, theOther: StepShape_ExtrudedFaceSolid) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aSweptArea: StepShape_FaceSurface | None, aExtrudedDirection: nanoocp.StepGeom.StepGeom_Direction | None, aDepth: float) -> None: ...

    def SetExtrudedDirection(self, aExtrudedDirection: nanoocp.StepGeom.StepGeom_Direction | None) -> None: ...

    def ExtrudedDirection(self) -> nanoocp.StepGeom.StepGeom_Direction: ...

    def SetDepth(self, aDepth: float) -> None: ...

    def Depth(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_FaceBasedSurfaceModel(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    """Representation of STEP entity FaceBasedSurfaceModel"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_FaceBasedSurfaceModel) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aFbsmFaces: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ConnectedFaceSet] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def FbsmFaces(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ConnectedFaceSet]:
        """Returns field FbsmFaces"""

    def SetFbsmFaces(self, FbsmFaces: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ConnectedFaceSet] | None) -> None:
        """Set field FbsmFaces"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_FaceOuterBound(StepShape_FaceBound):
    @overload
    def __init__(self) -> None:
        """Returns a FaceOuterBound"""

    @overload
    def __init__(self, theOther: StepShape_FaceOuterBound) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_FacetedBrep(StepShape_ManifoldSolidBrep):
    @overload
    def __init__(self) -> None:
        """Returns a FacetedBrep"""

    @overload
    def __init__(self, theOther: StepShape_FacetedBrep) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_FacetedBrepAndBrepWithVoids(StepShape_ManifoldSolidBrep):
    @overload
    def __init__(self) -> None:
        """Returns a FacetedBrepAndBrepWithVoids"""

    @overload
    def __init__(self, theOther: StepShape_FacetedBrepAndBrepWithVoids) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aOuter: StepShape_ClosedShell | None, aFacetedBrep: StepShape_FacetedBrep | None, aBrepWithVoids: StepShape_BrepWithVoids | None) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aOuter: StepShape_ClosedShell | None, aVoids: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedClosedShell] | None) -> None: ...

    def SetFacetedBrep(self, aFacetedBrep: StepShape_FacetedBrep | None) -> None: ...

    def FacetedBrep(self) -> StepShape_FacetedBrep: ...

    def SetBrepWithVoids(self, aBrepWithVoids: StepShape_BrepWithVoids | None) -> None: ...

    def BrepWithVoids(self) -> StepShape_BrepWithVoids: ...

    def SetVoids(self, aVoids: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedClosedShell] | None) -> None: ...

    def Voids(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedClosedShell]: ...

    def VoidsValue(self, num: int) -> StepShape_OrientedClosedShell: ...

    def NbVoids(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_FacetedBrepShapeRepresentation(StepShape_ShapeRepresentation):
    @overload
    def __init__(self) -> None:
        """Returns a FacetedBrepShapeRepresentation"""

    @overload
    def __init__(self, theOther: StepShape_FacetedBrepShapeRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_GeometricallyBoundedSurfaceShapeRepresentation(StepShape_ShapeRepresentation):
    @overload
    def __init__(self) -> None:
        """Returns a GeometricallyBoundedSurfaceShapeRepresentation"""

    @overload
    def __init__(self, theOther: StepShape_GeometricallyBoundedSurfaceShapeRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_GeometricallyBoundedWireframeShapeRepresentation(StepShape_ShapeRepresentation):
    @overload
    def __init__(self) -> None:
        """Returns a GeometricallyBoundedWireframeShapeRepresentation"""

    @overload
    def __init__(self, theOther: StepShape_GeometricallyBoundedWireframeShapeRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_GeometricSetSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a GeometricSetSelect SelectType"""

    @overload
    def __init__(self, theOther: StepShape_GeometricSetSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a GeometricSetSelect Kind Entity that is :
        1 -> Point
        2 -> Curve
        3 -> Surface
        0 else
        """

    def Point(self) -> nanoocp.StepGeom.StepGeom_Point:
        """returns Value as a Point (Null if another type)"""

    def Curve(self) -> nanoocp.StepGeom.StepGeom_Curve:
        """returns Value as a Curve (Null if another type)"""

    def Surface(self) -> nanoocp.StepGeom.StepGeom_Surface:
        """returns Value as a Surface (Null if another type)"""

class StepShape_GeometricSet(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a GeometricSet"""

    @overload
    def __init__(self, theOther: StepShape_GeometricSet) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aElements: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_GeometricSetSelect] | None) -> None: ...

    def SetElements(self, aElements: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_GeometricSetSelect] | None) -> None: ...

    def Elements(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_GeometricSetSelect]: ...

    def ElementsValue(self, num: int) -> StepShape_GeometricSetSelect: ...

    def NbElements(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_GeometricCurveSet(StepShape_GeometricSet):
    @overload
    def __init__(self) -> None:
        """Returns a GeometricCurveSet"""

    @overload
    def __init__(self, theOther: StepShape_GeometricCurveSet) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_LimitsAndFits(nanoocp.Standard.Standard_Transient):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepShape_LimitsAndFits) -> None: ...

    def Init(self, form_variance: nanoocp.TCollection.TCollection_HAsciiString | None, zone_variance: nanoocp.TCollection.TCollection_HAsciiString | None, grade: nanoocp.TCollection.TCollection_HAsciiString | None, source: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def FormVariance(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetFormVariance(self, form_variance: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def ZoneVariance(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetZoneVariance(self, zone_variance: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Grade(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetGrade(self, grade: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Source(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetSource(self, source: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_LoopAndPath(StepShape_TopologicalRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a LoopAndPath"""

    @overload
    def __init__(self, theOther: StepShape_LoopAndPath) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aLoop: StepShape_Loop | None, aPath: StepShape_Path | None) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aEdgeList: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedEdge] | None) -> None: ...

    def SetLoop(self, aLoop: StepShape_Loop | None) -> None: ...

    def Loop(self) -> StepShape_Loop: ...

    def SetPath(self, aPath: StepShape_Path | None) -> None: ...

    def Path(self) -> StepShape_Path: ...

    def SetEdgeList(self, aEdgeList: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedEdge] | None) -> None: ...

    def EdgeList(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedEdge]: ...

    def EdgeListValue(self, num: int) -> StepShape_OrientedEdge: ...

    def NbEdgeList(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ManifoldSurfaceShapeRepresentation(StepShape_ShapeRepresentation):
    @overload
    def __init__(self) -> None:
        """Returns a ManifoldSurfaceShapeRepresentation"""

    @overload
    def __init__(self, theOther: StepShape_ManifoldSurfaceShapeRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ValueQualifier(nanoocp.StepData.StepData_SelectType):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepShape_ValueQualifier) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of ValueQualifier Select Type :
        1 -> PrecisionQualifier from StepShape
        2 -> TypeQualifier from StepShape
        3 -> UnceraintyQualifier .. not yet implemented
        4 -> ValueFormatTypeQualifier
        """

    def PrecisionQualifier(self) -> StepShape_PrecisionQualifier:
        """Returns Value as PrecisionQualifier"""

    def TypeQualifier(self) -> StepShape_TypeQualifier:
        """Returns Value as TypeQualifier"""

    def ValueFormatTypeQualifier(self) -> StepShape_ValueFormatTypeQualifier:
        """Returns Value as ValueFormatTypeQualifier"""

class StepShape_MeasureQualification(nanoocp.Standard.Standard_Transient):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepShape_MeasureQualification) -> None: ...

    def Init(self, name: nanoocp.TCollection.TCollection_HAsciiString | None, description: nanoocp.TCollection.TCollection_HAsciiString | None, qualified_measure: nanoocp.Standard.Standard_Transient | None, qualifiers: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ValueQualifier] | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetName(self, name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetDescription(self, description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def QualifiedMeasure(self) -> nanoocp.Standard.Standard_Transient: ...

    def SetQualifiedMeasure(self, qualified_measure: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def Qualifiers(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ValueQualifier]: ...

    def NbQualifiers(self) -> int: ...

    def SetQualifiers(self, qualifiers: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ValueQualifier] | None) -> None: ...

    def QualifiersValue(self, num: int) -> StepShape_ValueQualifier: ...

    def SetQualifiersValue(self, num: int, aqualifier: StepShape_ValueQualifier) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_MeasureRepresentationItemAndQualifiedRepresentationItem(nanoocp.StepRepr.StepRepr_RepresentationItem):
    """
    Added for Dimensional Tolerances
    Complex Type between MeasureRepresentationItem and
    QualifiedRepresentationItem
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepShape_MeasureRepresentationItemAndQualifiedRepresentationItem) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aValueComponent: nanoocp.StepBasic.StepBasic_MeasureValueMember | None, aUnitComponent: nanoocp.StepBasic.StepBasic_Unit, qualifiers: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ValueQualifier] | None) -> None: ...

    def SetMeasure(self, Measure: nanoocp.StepBasic.StepBasic_MeasureWithUnit | None) -> None: ...

    def Measure(self) -> nanoocp.StepBasic.StepBasic_MeasureWithUnit: ...

    def Qualifiers(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ValueQualifier]: ...

    def NbQualifiers(self) -> int: ...

    def SetQualifiers(self, qualifiers: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ValueQualifier] | None) -> None: ...

    def QualifiersValue(self, num: int) -> StepShape_ValueQualifier: ...

    def SetQualifiersValue(self, num: int, aqualifier: StepShape_ValueQualifier) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_NonManifoldSurfaceShapeRepresentation(StepShape_ShapeRepresentation):
    """Representation of STEP entity NonManifoldSurfaceShapeRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_NonManifoldSurfaceShapeRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_OpenShell(StepShape_ConnectedFaceSet):
    @overload
    def __init__(self) -> None:
        """Returns a OpenShell"""

    @overload
    def __init__(self, theOther: StepShape_OpenShell) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_OrientedFace(StepShape_Face):
    @overload
    def __init__(self) -> None:
        """Returns a OrientedFace"""

    @overload
    def __init__(self, theOther: StepShape_OrientedFace) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aFaceElement: StepShape_Face | None, aOrientation: bool) -> None: ...

    def SetFaceElement(self, aFaceElement: StepShape_Face | None) -> None: ...

    def FaceElement(self) -> StepShape_Face: ...

    def SetOrientation(self, aOrientation: bool) -> None: ...

    def Orientation(self) -> bool: ...

    def SetBounds(self, aBounds: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_FaceBound] | None) -> None: ...

    def Bounds(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_FaceBound]: ...

    def BoundsValue(self, num: int) -> StepShape_FaceBound: ...

    def NbBounds(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_OrientedOpenShell(StepShape_OpenShell):
    @overload
    def __init__(self) -> None:
        """Returns a OrientedOpenShell"""

    @overload
    def __init__(self, theOther: StepShape_OrientedOpenShell) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aOpenShellElement: StepShape_OpenShell | None, aOrientation: bool) -> None: ...

    def SetOpenShellElement(self, aOpenShellElement: StepShape_OpenShell | None) -> None: ...

    def OpenShellElement(self) -> StepShape_OpenShell: ...

    def SetOrientation(self, aOrientation: bool) -> None: ...

    def Orientation(self) -> bool: ...

    def SetCfsFaces(self, aCfsFaces: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Face] | None) -> None: ...

    def CfsFaces(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Face]: ...

    def CfsFacesValue(self, num: int) -> StepShape_Face: ...

    def NbCfsFaces(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_Path(StepShape_TopologicalRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a Path"""

    @overload
    def __init__(self, theOther: StepShape_Path) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aEdgeList: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedEdge] | None) -> None: ...

    def SetEdgeList(self, aEdgeList: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedEdge] | None) -> None: ...

    def EdgeList(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedEdge]: ...

    def EdgeListValue(self, num: int) -> StepShape_OrientedEdge: ...

    def NbEdgeList(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_OrientedPath(StepShape_Path):
    @overload
    def __init__(self) -> None:
        """Returns a OrientedPath"""

    @overload
    def __init__(self, theOther: StepShape_OrientedPath) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aPathElement: StepShape_EdgeLoop | None, aOrientation: bool) -> None: ...

    def SetPathElement(self, aPathElement: StepShape_EdgeLoop | None) -> None: ...

    def PathElement(self) -> StepShape_EdgeLoop: ...

    def SetOrientation(self, aOrientation: bool) -> None: ...

    def Orientation(self) -> bool: ...

    def SetEdgeList(self, aEdgeList: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedEdge] | None) -> None: ...

    def EdgeList(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedEdge]: ...

    def EdgeListValue(self, num: int) -> StepShape_OrientedEdge: ...

    def NbEdgeList(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ToleranceMethodDefinition(nanoocp.StepData.StepData_SelectType):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepShape_ToleranceMethodDefinition) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of ValueQualifier Select Type :
        1 -> ToleranceValue from StepShape
        2 -> LimitsAndFits from StepShape
        """

    def ToleranceValue(self) -> StepShape_ToleranceValue:
        """Returns Value as ToleranceValue"""

    def LimitsAndFits(self) -> StepShape_LimitsAndFits:
        """Returns Value as LimitsAndFits"""

class StepShape_PlusMinusTolerance(nanoocp.Standard.Standard_Transient):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepShape_PlusMinusTolerance) -> None: ...

    def Init(self, range: StepShape_ToleranceMethodDefinition, toleranced_dimension: StepShape_DimensionalCharacteristic) -> None: ...

    def Range(self) -> StepShape_ToleranceMethodDefinition: ...

    def SetRange(self, range: StepShape_ToleranceMethodDefinition) -> None: ...

    def TolerancedDimension(self) -> StepShape_DimensionalCharacteristic: ...

    def SetTolerancedDimension(self, toleranced_dimension: StepShape_DimensionalCharacteristic) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_PointRepresentation(StepShape_ShapeRepresentation):
    """Representation of STEP entity PointRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_PointRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_PolyLoop(StepShape_Loop):
    @overload
    def __init__(self) -> None:
        """Returns a PolyLoop"""

    @overload
    def __init__(self, theOther: StepShape_PolyLoop) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aPolygon: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepGeom.StepGeom_CartesianPoint] | None) -> None: ...

    def SetPolygon(self, aPolygon: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepGeom.StepGeom_CartesianPoint] | None) -> None: ...

    def Polygon(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepGeom.StepGeom_CartesianPoint]: ...

    def PolygonValue(self, num: int) -> nanoocp.StepGeom.StepGeom_CartesianPoint: ...

    def NbPolygon(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_PrecisionQualifier(nanoocp.Standard.Standard_Transient):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepShape_PrecisionQualifier) -> None: ...

    def Init(self, precision_value: int) -> None: ...

    def PrecisionValue(self) -> int: ...

    def SetPrecisionValue(self, precision_value: int) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_QualifiedRepresentationItem(nanoocp.StepRepr.StepRepr_RepresentationItem):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepShape_QualifiedRepresentationItem) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, qualifiers: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ValueQualifier] | None) -> None: ...

    def Qualifiers(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ValueQualifier]: ...

    def NbQualifiers(self) -> int: ...

    def SetQualifiers(self, qualifiers: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ValueQualifier] | None) -> None: ...

    def QualifiersValue(self, num: int) -> StepShape_ValueQualifier: ...

    def SetQualifiersValue(self, num: int, aqualifier: StepShape_ValueQualifier) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ReversibleTopologyItem(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a ReversibleTopologyItem SelectType"""

    @overload
    def __init__(self, theOther: StepShape_ReversibleTopologyItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a ReversibleTopologyItem Kind Entity that is :
        1 -> Edge
        2 -> Path
        3 -> Face
        4 -> FaceBound
        5 -> ClosedShell
        6 -> OpenShell
        0 else
        """

    def Edge(self) -> StepShape_Edge:
        """returns Value as a Edge (Null if another type)"""

    def Path(self) -> StepShape_Path:
        """returns Value as a Path (Null if another type)"""

    def Face(self) -> StepShape_Face:
        """returns Value as a Face (Null if another type)"""

    def FaceBound(self) -> StepShape_FaceBound:
        """returns Value as a FaceBound (Null if another type)"""

    def ClosedShell(self) -> StepShape_ClosedShell:
        """returns Value as a ClosedShell (Null if another type)"""

    def OpenShell(self) -> StepShape_OpenShell:
        """returns Value as a OpenShell (Null if another type)"""

class StepShape_RevolvedAreaSolid(StepShape_SweptAreaSolid):
    @overload
    def __init__(self) -> None:
        """Returns a RevolvedAreaSolid"""

    @overload
    def __init__(self, theOther: StepShape_RevolvedAreaSolid) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aSweptArea: nanoocp.StepGeom.StepGeom_CurveBoundedSurface | None, aAxis: nanoocp.StepGeom.StepGeom_Axis1Placement | None, aAngle: float) -> None: ...

    def SetAxis(self, aAxis: nanoocp.StepGeom.StepGeom_Axis1Placement | None) -> None: ...

    def Axis(self) -> nanoocp.StepGeom.StepGeom_Axis1Placement: ...

    def SetAngle(self, aAngle: float) -> None: ...

    def Angle(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_RevolvedFaceSolid(StepShape_SweptFaceSolid):
    @overload
    def __init__(self) -> None:
        """Returns a RevolvedFaceSolid"""

    @overload
    def __init__(self, theOther: StepShape_RevolvedFaceSolid) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aSweptArea: StepShape_FaceSurface | None) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aSweptArea: StepShape_FaceSurface | None, aAxis: nanoocp.StepGeom.StepGeom_Axis1Placement | None, aAngle: float) -> None: ...

    def SetAxis(self, aAxis: nanoocp.StepGeom.StepGeom_Axis1Placement | None) -> None: ...

    def Axis(self) -> nanoocp.StepGeom.StepGeom_Axis1Placement: ...

    def SetAngle(self, aAngle: float) -> None: ...

    def Angle(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_RightAngularWedge(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a RightAngularWedge"""

    @overload
    def __init__(self, theOther: StepShape_RightAngularWedge) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aPosition: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None, aX: float, aY: float, aZ: float, aLtx: float) -> None: ...

    def SetPosition(self, aPosition: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None) -> None: ...

    def Position(self) -> nanoocp.StepGeom.StepGeom_Axis2Placement3d: ...

    def SetX(self, aX: float) -> None: ...

    def X(self) -> float: ...

    def SetY(self, aY: float) -> None: ...

    def Y(self) -> float: ...

    def SetZ(self, aZ: float) -> None: ...

    def Z(self) -> float: ...

    def SetLtx(self, aLtx: float) -> None: ...

    def Ltx(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_RightCircularCone(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a RightCircularCone"""

    @overload
    def __init__(self, theOther: StepShape_RightCircularCone) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aPosition: nanoocp.StepGeom.StepGeom_Axis1Placement | None, aHeight: float, aRadius: float, aSemiAngle: float) -> None: ...

    def SetPosition(self, aPosition: nanoocp.StepGeom.StepGeom_Axis1Placement | None) -> None: ...

    def Position(self) -> nanoocp.StepGeom.StepGeom_Axis1Placement: ...

    def SetHeight(self, aHeight: float) -> None: ...

    def Height(self) -> float: ...

    def SetRadius(self, aRadius: float) -> None: ...

    def Radius(self) -> float: ...

    def SetSemiAngle(self, aSemiAngle: float) -> None: ...

    def SemiAngle(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_RightCircularCylinder(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a RightCircularCylinder"""

    @overload
    def __init__(self, theOther: StepShape_RightCircularCylinder) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aPosition: nanoocp.StepGeom.StepGeom_Axis1Placement | None, aHeight: float, aRadius: float) -> None: ...

    def SetPosition(self, aPosition: nanoocp.StepGeom.StepGeom_Axis1Placement | None) -> None: ...

    def Position(self) -> nanoocp.StepGeom.StepGeom_Axis1Placement: ...

    def SetHeight(self, aHeight: float) -> None: ...

    def Height(self) -> float: ...

    def SetRadius(self, aRadius: float) -> None: ...

    def Radius(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_SeamEdge(StepShape_OrientedEdge):
    """Representation of STEP entity SeamEdge"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_SeamEdge) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aOrientedEdge_EdgeElement: StepShape_Edge | None, aOrientedEdge_Orientation: bool, aPcurveReference: nanoocp.StepGeom.StepGeom_Pcurve | None) -> None:
        """Initialize all fields (own and inherited)"""

    def PcurveReference(self) -> nanoocp.StepGeom.StepGeom_Pcurve:
        """Returns field PcurveReference"""

    def SetPcurveReference(self, PcurveReference: nanoocp.StepGeom.StepGeom_Pcurve | None) -> None:
        """Set field PcurveReference"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ShapeDefinitionRepresentation(nanoocp.StepRepr.StepRepr_PropertyDefinitionRepresentation):
    """Representation of STEP entity ShapeDefinitionRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_ShapeDefinitionRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ShapeDimensionRepresentationItem(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a ShapeDimensionRepresentationItem select type"""

    @overload
    def __init__(self, theOther: StepShape_ShapeDimensionRepresentationItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a ShapeDimensionRepresentationItem Kind Entity that is :
        1 -> CompoundRepresentationItem
        2 -> DescriptiveRepresentationItem
        3 -> MeasureRepresentationItem
        4 -> Placement
        0 else
        """

    def CompoundRepresentationItem(self) -> nanoocp.StepRepr.StepRepr_CompoundRepresentationItem:
        """returns Value as a CompoundRepresentationItem (Null if another type)"""

    def DescriptiveRepresentationItem(self) -> nanoocp.StepRepr.StepRepr_DescriptiveRepresentationItem:
        """
        returns Value as a DescriptiveRepresentationItem (Null if another type)
        """

    def MeasureRepresentationItem(self) -> nanoocp.StepRepr.StepRepr_MeasureRepresentationItem:
        """returns Value as a MeasureRepresentationItem (Null if another type)"""

    def Placement(self) -> nanoocp.StepGeom.StepGeom_Placement:
        """returns Value as a Placement (Null if another type)"""

class StepShape_ShapeDimensionRepresentation(StepShape_ShapeRepresentation):
    """Representation of STEP entity ShapeDimensionRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_ShapeDimensionRepresentation) -> None: ...

    @overload
    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None, theContextOfItems: nanoocp.StepRepr.StepRepr_RepresentationContext | None) -> None:
        """Initialize all fields AP214"""

    @overload
    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ShapeDimensionRepresentationItem] | None, theContextOfItems: nanoocp.StepRepr.StepRepr_RepresentationContext | None) -> None:
        """Initialize all fields AP242"""

    def SetItemsAP242(self, theItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ShapeDimensionRepresentationItem] | None) -> None: ...

    def ItemsAP242(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ShapeDimensionRepresentationItem]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ShapeRepresentationWithParameters(StepShape_ShapeRepresentation):
    """Representation of STEP entity ShapeRepresentationWithParameters"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_ShapeRepresentationWithParameters) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_Shell(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a Shell SelectType"""

    @overload
    def __init__(self, theOther: StepShape_Shell) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a Shell Kind Entity that is :
        1 -> OpenShell
        2 -> ClosedShell
        0 else
        """

    def OpenShell(self) -> StepShape_OpenShell:
        """returns Value as a OpenShell (Null if another type)"""

    def ClosedShell(self) -> StepShape_ClosedShell:
        """returns Value as a ClosedShell (Null if another type)"""

class StepShape_ShellBasedSurfaceModel(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a ShellBasedSurfaceModel"""

    @overload
    def __init__(self, theOther: StepShape_ShellBasedSurfaceModel) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aSbsmBoundary: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Shell] | None) -> None: ...

    def SetSbsmBoundary(self, aSbsmBoundary: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Shell] | None) -> None: ...

    def SbsmBoundary(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Shell]: ...

    def SbsmBoundaryValue(self, num: int) -> StepShape_Shell: ...

    def NbSbsmBoundary(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_SolidReplica(StepShape_SolidModel):
    @overload
    def __init__(self) -> None:
        """Returns a SolidReplica"""

    @overload
    def __init__(self, theOther: StepShape_SolidReplica) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aParentSolid: StepShape_SolidModel | None, aTransformation: nanoocp.StepGeom.StepGeom_CartesianTransformationOperator3d | None) -> None: ...

    def SetParentSolid(self, aParentSolid: StepShape_SolidModel | None) -> None: ...

    def ParentSolid(self) -> StepShape_SolidModel: ...

    def SetTransformation(self, aTransformation: nanoocp.StepGeom.StepGeom_CartesianTransformationOperator3d | None) -> None: ...

    def Transformation(self) -> nanoocp.StepGeom.StepGeom_CartesianTransformationOperator3d: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_Sphere(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a Sphere"""

    @overload
    def __init__(self, theOther: StepShape_Sphere) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aRadius: float, aCentre: nanoocp.StepGeom.StepGeom_Point | None) -> None: ...

    def SetRadius(self, aRadius: float) -> None: ...

    def Radius(self) -> float: ...

    def SetCentre(self, aCentre: nanoocp.StepGeom.StepGeom_Point | None) -> None: ...

    def Centre(self) -> nanoocp.StepGeom.StepGeom_Point: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_Subedge(StepShape_Edge):
    """Representation of STEP entity Subedge"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_Subedge) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aEdge_EdgeStart: StepShape_Vertex | None, aEdge_EdgeEnd: StepShape_Vertex | None, aParentEdge: StepShape_Edge | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ParentEdge(self) -> StepShape_Edge:
        """Returns field ParentEdge"""

    def SetParentEdge(self, ParentEdge: StepShape_Edge | None) -> None:
        """Set field ParentEdge"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_Subface(StepShape_Face):
    """Representation of STEP entity Subface"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepShape_Subface) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aFace_Bounds: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_FaceBound] | None, aParentFace: StepShape_Face | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ParentFace(self) -> StepShape_Face:
        """Returns field ParentFace"""

    def SetParentFace(self, ParentFace: StepShape_Face | None) -> None:
        """Set field ParentFace"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_SurfaceModel(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a SurfaceModel SelectType"""

    @overload
    def __init__(self, theOther: StepShape_SurfaceModel) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a SurfaceModel Kind Entity that is :
        1 -> ShellBasedSurfaceModel
        2 -> FaceBasedSurfaceModel
        0 else
        """

    def ShellBasedSurfaceModel(self) -> StepShape_ShellBasedSurfaceModel:
        """returns Value as a ShellBasedSurfaceModel (Null if another type)"""

class StepShape_ToleranceValue(nanoocp.Standard.Standard_Transient):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepShape_ToleranceValue) -> None: ...

    def Init(self, lower_bound: nanoocp.Standard.Standard_Transient | None, upper_bound: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def LowerBound(self) -> nanoocp.Standard.Standard_Transient: ...

    def SetLowerBound(self, lower_bound: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def UpperBound(self) -> nanoocp.Standard.Standard_Transient: ...

    def SetUpperBound(self, upper_bound: nanoocp.Standard.Standard_Transient | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_Torus(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a Torus"""

    @overload
    def __init__(self, theOther: StepShape_Torus) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aPosition: nanoocp.StepGeom.StepGeom_Axis1Placement | None, aMajorRadius: float, aMinorRadius: float) -> None: ...

    def SetPosition(self, aPosition: nanoocp.StepGeom.StepGeom_Axis1Placement | None) -> None: ...

    def Position(self) -> nanoocp.StepGeom.StepGeom_Axis1Placement: ...

    def SetMajorRadius(self, aMajorRadius: float) -> None: ...

    def MajorRadius(self) -> float: ...

    def SetMinorRadius(self, aMinorRadius: float) -> None: ...

    def MinorRadius(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_TransitionalShapeRepresentation(StepShape_ShapeRepresentation):
    @overload
    def __init__(self) -> None:
        """Returns a TransitionalShapeRepresentation"""

    @overload
    def __init__(self, theOther: StepShape_TransitionalShapeRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_TypeQualifier(nanoocp.Standard.Standard_Transient):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepShape_TypeQualifier) -> None: ...

    def Init(self, name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetName(self, name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_ValueFormatTypeQualifier(nanoocp.Standard.Standard_Transient):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepShape_ValueFormatTypeQualifier) -> None: ...

    def Init(self, theFormatType: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Init all field own and inherited"""

    def FormatType(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field FormatType"""

    def SetFormatType(self, theFormatType: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field FormatType"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_VertexLoop(StepShape_Loop):
    @overload
    def __init__(self) -> None:
        """Returns a VertexLoop"""

    @overload
    def __init__(self, theOther: StepShape_VertexLoop) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aLoopVertex: StepShape_Vertex | None) -> None: ...

    def SetLoopVertex(self, aLoopVertex: StepShape_Vertex | None) -> None: ...

    def LoopVertex(self) -> StepShape_Vertex: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepShape_VertexPoint(StepShape_Vertex):
    @overload
    def __init__(self) -> None:
        """Returns a VertexPoint"""

    @overload
    def __init__(self, theOther: StepShape_VertexPoint) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aVertexGeometry: nanoocp.StepGeom.StepGeom_Point | None) -> None: ...

    def SetVertexGeometry(self, aVertexGeometry: nanoocp.StepGeom.StepGeom_Point | None) -> None: ...

    def VertexGeometry(self) -> nanoocp.StepGeom.StepGeom_Point: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.StepShape
StepShape_Array1OfConnectedEdgeSet = nanoocp.NCollection.NCollection_Array1[nanoocp.StepShape.StepShape_ConnectedEdgeSet]
StepShape_Array1OfConnectedFaceSet = nanoocp.NCollection.NCollection_Array1[nanoocp.StepShape.StepShape_ConnectedFaceSet]
StepShape_Array1OfEdge = nanoocp.NCollection.NCollection_Array1[nanoocp.StepShape.StepShape_Edge]
StepShape_Array1OfFace = nanoocp.NCollection.NCollection_Array1[nanoocp.StepShape.StepShape_Face]
StepShape_Array1OfFaceBound = nanoocp.NCollection.NCollection_Array1[nanoocp.StepShape.StepShape_FaceBound]
StepShape_Array1OfGeometricSetSelect = nanoocp.NCollection.NCollection_Array1[nanoocp.StepShape.StepShape_GeometricSetSelect]
StepShape_Array1OfOrientedClosedShell = nanoocp.NCollection.NCollection_Array1[nanoocp.StepShape.StepShape_OrientedClosedShell]
StepShape_Array1OfOrientedEdge = nanoocp.NCollection.NCollection_Array1[nanoocp.StepShape.StepShape_OrientedEdge]
StepShape_Array1OfShapeDimensionRepresentationItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepShape.StepShape_ShapeDimensionRepresentationItem]
StepShape_Array1OfShell = nanoocp.NCollection.NCollection_Array1[nanoocp.StepShape.StepShape_Shell]
StepShape_Array1OfValueQualifier = nanoocp.NCollection.NCollection_Array1[nanoocp.StepShape.StepShape_ValueQualifier]
StepShape_HArray1OfConnectedEdgeSet = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ConnectedEdgeSet]
StepShape_HArray1OfConnectedFaceSet = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ConnectedFaceSet]
StepShape_HArray1OfEdge = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Edge]
StepShape_HArray1OfFace = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Face]
StepShape_HArray1OfFaceBound = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_FaceBound]
StepShape_HArray1OfGeometricSetSelect = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_GeometricSetSelect]
StepShape_HArray1OfOrientedClosedShell = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedClosedShell]
StepShape_HArray1OfOrientedEdge = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_OrientedEdge]
StepShape_HArray1OfShapeDimensionRepresentationItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ShapeDimensionRepresentationItem]
StepShape_HArray1OfShell = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_Shell]
StepShape_HArray1OfValueQualifier = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepShape.StepShape_ValueQualifier]
