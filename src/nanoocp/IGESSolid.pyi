"""OCCT package IGESSolid (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.IGESBasic
import nanoocp.IGESData
import nanoocp.IGESGeom
import nanoocp.Interface
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp


class IGESSolid:
    """This package consists of B-Rep and CSG Solid entities"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid) -> None: ...

    @staticmethod
    def Init() -> None:
        """Prepares dynamic data (Protocol, Modules) for this package"""

    @staticmethod
    def Protocol() -> IGESSolid_Protocol:
        """Returns the Protocol for this Package"""

class IGESSolid_Block(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines Block, Type <150> Form Number <0>
    in package IGESSolid
    The Block is a rectangular parallelopiped, defined with
    one vertex at (X1, Y1, Z1) and three edges lying along
    the local +X, +Y, +Z axes.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_Block) -> None: ...

    def Init(self, aSize: nanoocp.gp.gp_XYZ, aCorner: nanoocp.gp.gp_XYZ, aXAxis: nanoocp.gp.gp_XYZ, aZAxis: nanoocp.gp.gp_XYZ) -> None:
        """
        This method is used to set the fields of the class Block
        - aSize   : Length in each local directions
        - aCorner : Corner point coordinates. Default (0,0,0)
        - aXAxis  : Unit vector defining local X-axis
        default (1,0,0)
        - aZAxis  : Unit vector defining local Z-axis
        default (0,0,1)
        """

    def Size(self) -> nanoocp.gp.gp_XYZ:
        """returns the size of the block"""

    def XLength(self) -> float:
        """returns the length of the Block along the local X-direction"""

    def YLength(self) -> float:
        """returns the length of the Block along the local Y-direction"""

    def ZLength(self) -> float:
        """returns the length of the Block along the local Z-direction"""

    def Corner(self) -> nanoocp.gp.gp_Pnt:
        """returns the corner point coordinates of the Block"""

    def TransformedCorner(self) -> nanoocp.gp.gp_Pnt:
        """
        returns the corner point coordinates of the Block after applying
        the TransformationMatrix
        """

    def XAxis(self) -> nanoocp.gp.gp_Dir:
        """returns the direction defining the local X-axis"""

    def TransformedXAxis(self) -> nanoocp.gp.gp_Dir:
        """
        returns the direction defining the local X-axis after applying
        TransformationMatrix
        """

    def YAxis(self) -> nanoocp.gp.gp_Dir:
        """
        returns the direction defining the local Y-axis
        it is the cross product of ZAxis and XAxis
        """

    def TransformedYAxis(self) -> nanoocp.gp.gp_Dir:
        """
        returns the direction defining the local Y-axis after applying
        TransformationMatrix
        """

    def ZAxis(self) -> nanoocp.gp.gp_Dir:
        """returns the direction defining the local X-axis"""

    def TransformedZAxis(self) -> nanoocp.gp.gp_Dir:
        """
        returns the direction defining the local Z-axis after applying
        TransformationMatrix
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_BooleanTree(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines BooleanTree, Type <180> Form Number <0>
    in package IGESSolid
    The Boolean tree describes a binary tree structure
    composed of regularized Boolean operations and operands,
    in post-order notation.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_BooleanTree) -> None: ...

    def Init(self, operands: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None, operations: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """
        This method is used to set the fields of the class
        BooleanTree
        - operands   : Array containing pointer to DE of operands
        - operations : Array containing integer type for operations
        """

    def Length(self) -> int:
        """returns the length of the post-order list"""

    def IsOperand(self, Index: int) -> bool:
        """
        returns True if Index'th value in the post-order list is an Operand;
        else returns False if it is an Integer Operations
        raises exception if Index < 1 or Index > Length()
        """

    def Operand(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the Index'th value in the post-order list only if it is
        an operand else returns NULL
        raises exception if Index < 1 or Index > Length()
        """

    def Operation(self, Index: int) -> int:
        """
        returns the Index'th value in the post-order list only if it is
        an operation else returns 0
        raises exception if Index < 1 or Index > Length()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_ConeFrustum(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines ConeFrustum, Type <156> Form Number <0>
    in package IGESSolid
    The Cone Frustum is defined by the center of the
    larger circular face of the frustum, its radius, a unit
    vector in the axis direction, a height in this direction
    and a second circular face with radius which is lesser
    than the first face.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_ConeFrustum) -> None: ...

    def Init(self, Ht: float, R1: float, R2: float, Center: nanoocp.gp.gp_XYZ, anAxis: nanoocp.gp.gp_XYZ) -> None:
        """
        This method is used to set the fields of the class
        ConeFrustum
        - Ht     : the Height of cone
        - R1     : Radius of the larger face
        - R2     : Radius of the smaller face (default 0)
        - Center : Center of the larger face (default (0,0,0))
        - anAxis : Unit vector in axis direction (default (0,0,1))
        """

    def Height(self) -> float:
        """returns the height of the cone frustum"""

    def LargerRadius(self) -> float:
        """returns the radius of the larger face of the cone frustum"""

    def SmallerRadius(self) -> float:
        """returns the radius of the second face of the cone frustum"""

    def FaceCenter(self) -> nanoocp.gp.gp_Pnt:
        """returns the center of the larger face of the cone frustum"""

    def TransformedFaceCenter(self) -> nanoocp.gp.gp_Pnt:
        """
        returns the center of the larger face of the cone frustum
        after applying TransformationMatrix
        """

    def Axis(self) -> nanoocp.gp.gp_Dir:
        """returns the direction of the axis of the cone frustum"""

    def TransformedAxis(self) -> nanoocp.gp.gp_Dir:
        """
        returns the direction of the axis of the cone frustum
        after applying TransformationMatrix
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_ConicalSurface(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines ConicalSurface, Type <194> Form Number <0,1>
    in package IGESSolid
    The right circular conical surface is defined by a
    point on the axis on the cone, the direction of the axis
    of the cone, the radius of the cone at the axis point and
    the cone semi-angle.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_ConicalSurface) -> None: ...

    def Init(self, aLocation: nanoocp.IGESGeom.IGESGeom_Point | None, anAxis: nanoocp.IGESGeom.IGESGeom_Direction | None, aRadius: float, anAngle: float, aRefdir: nanoocp.IGESGeom.IGESGeom_Direction | None) -> None:
        """
        This method is used to set the fields of the class
        ConicalSurface
        - aLocation : Location of the point on axis
        - anAxis    : Direction of the axis
        - aRadius   : Radius at axis point
        - anAngle   : Value of semi-angle in degrees (0<angle<90)
        - aRefdir   : Reference direction (parametrised surface)
        Null if unparametrised surface.
        """

    def LocationPoint(self) -> nanoocp.IGESGeom.IGESGeom_Point:
        """returns the location of the point on the axis"""

    def Axis(self) -> nanoocp.IGESGeom.IGESGeom_Direction:
        """returns the direction of the axis"""

    def Radius(self) -> float:
        """returns the radius at the axis point"""

    def SemiAngle(self) -> float:
        """returns the semi-angle value"""

    def ReferenceDir(self) -> nanoocp.IGESGeom.IGESGeom_Direction:
        """
        returns the reference direction of the conical surface in case
        of parametrised surface. For unparametrised surface it returns
        NULL.
        """

    def IsParametrised(self) -> bool:
        """returns True if Form no is 1 else false"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_Cylinder(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines Cylinder, Type <154> Form Number <0>
    in package IGESSolid
    This defines a solid cylinder
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_Cylinder) -> None: ...

    def Init(self, aHeight: float, aRadius: float, aCenter: nanoocp.gp.gp_XYZ, anAxis: nanoocp.gp.gp_XYZ) -> None:
        """
        This method is used to set the fields of the class
        Cylinder
        - aHeight : Cylinder height
        - aRadius : Cylinder radius
        - aCenter : First face center coordinates (default (0,0,0))
        - anAxis  : Unit vector in axis direction (default (0,0,1))
        """

    def Height(self) -> float:
        """returns the cylinder height"""

    def Radius(self) -> float:
        """returns the cylinder radius"""

    def FaceCenter(self) -> nanoocp.gp.gp_Pnt:
        """returns the first face center coordinates."""

    def TransformedFaceCenter(self) -> nanoocp.gp.gp_Pnt:
        """returns the first face center after applying TransformationMatrix"""

    def Axis(self) -> nanoocp.gp.gp_Dir:
        """returns the vector in axis direction"""

    def TransformedAxis(self) -> nanoocp.gp.gp_Dir:
        """
        returns the vector in axis direction after applying
        TransformationMatrix
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_CylindricalSurface(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines CylindricalSurface, Type <192> Form Number <0,1>
    in package IGESSolid
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_CylindricalSurface) -> None: ...

    def Init(self, aLocation: nanoocp.IGESGeom.IGESGeom_Point | None, anAxis: nanoocp.IGESGeom.IGESGeom_Direction | None, aRadius: float, aRefdir: nanoocp.IGESGeom.IGESGeom_Direction | None) -> None:
        """
        This method is used to set the fields of the class
        CylindricalSurface
        - aLocation : the location of the point on axis
        - anAxis    : the direction of the axis
        - aRadius   : the radius at the axis point
        - aRefdir   : the reference direction (parametrised surface)
        default NULL (unparametrised surface)
        """

    def LocationPoint(self) -> nanoocp.IGESGeom.IGESGeom_Point:
        """returns the point on the axis"""

    def Axis(self) -> nanoocp.IGESGeom.IGESGeom_Direction:
        """returns the direction on the axis"""

    def Radius(self) -> float:
        """returns the radius at the axis point"""

    def IsParametrised(self) -> bool:
        """returns whether the surface is parametrised or not"""

    def ReferenceDir(self) -> nanoocp.IGESGeom.IGESGeom_Direction:
        """
        returns the reference direction only for parametrised surface
        else returns NULL
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_VertexList(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines VertexList, Type <502> Form Number <1>
    in package IGESSolid
    A vertex is a point in R3. A vertex is the bound of an
    edge and can participate in the bounds of a face.
    It contains one or more vertices.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_VertexList) -> None: ...

    def Init(self, vertices: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ] | None) -> None:
        """
        This method is used to set the fields of the class
        VertexList
        - vertices : the vertices in the list
        """

    def NbVertices(self) -> int:
        """return the number of vertices in the list"""

    def Vertex(self, num: int) -> nanoocp.gp.gp_Pnt:
        """
        returns the num'th vertex in the list
        raises exception if num <= 0 or num > NbVertices()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_EdgeList(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines EdgeList, Type <504> Form <1>
    in package IGESSolid
    EdgeList is defined as a segment joining two vertices
    It contains one or more edge tuples.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_EdgeList) -> None: ...

    def Init(self, curves: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None, startVertexList: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESSolid.IGESSolid_VertexList] | None, startVertexIndex: nanoocp.NCollection.NCollection_HArray1[int] | None, endVertexList: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESSolid.IGESSolid_VertexList] | None, endVertexIndex: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """
        This method is used to set the fields of the class
        EdgeList
        - curves           : the model space curves
        - startVertexList  : the vertex list that contains the
        start vertices
        - startVertexIndex : the index of the vertex in the
        corresponding vertex list
        - endVertexList    : the vertex list that contains the
        end vertices
        - endVertexIndex   : the index of the vertex in the
        corresponding vertex list
        raises exception if size of curves,startVertexList,startVertexIndex,
        endVertexList and endVertexIndex do no match
        """

    def NbEdges(self) -> int:
        """returns the number of edges in the edge list"""

    def Curve(self, num: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the num'th model space curve
        raises Exception if num <= 0 or num > NbEdges()
        """

    def StartVertexList(self, num: int) -> IGESSolid_VertexList:
        """
        returns the num'th start vertex list
        raises Exception if num <= 0 or num > NbEdges()
        """

    def StartVertexIndex(self, num: int) -> int:
        """
        returns the index of num'th start vertex in
        the corresponding start vertex list
        raises Exception if num <= 0 or num > NbEdges()
        """

    def EndVertexList(self, num: int) -> IGESSolid_VertexList:
        """
        returns the num'th end vertex list
        raises Exception if num <= 0 or num > NbEdges()
        """

    def EndVertexIndex(self, num: int) -> int:
        """
        returns the index of num'th end vertex in
        the corresponding end vertex list
        raises Exception if num <= 0 or num > NbEdges()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_Ellipsoid(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines Ellipsoid, Type <168> Form Number <0>
    in package IGESSolid
    The ellipsoid is a solid bounded by the surface defined
    by:
    X^2       Y^2       Z^2
    -----  +  -----  +  -----  =  1
    LX^2      LY^2      LZ^2
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_Ellipsoid) -> None: ...

    def Init(self, aSize: nanoocp.gp.gp_XYZ, aCenter: nanoocp.gp.gp_XYZ, anXAxis: nanoocp.gp.gp_XYZ, anZAxis: nanoocp.gp.gp_XYZ) -> None:
        """
        This method is used to set the fields of the class
        Ellipsoid
        - aSize      : Lengths in the local X,Y,Z directions
        - aCenter    : Center point of ellipsoid (default (0,0,0))
        - anXAxis    : Unit vector defining local X-axis
        default (1,0,0)
        - anZAxis    : Unit vector defining local Z-axis
        default (0,0,1)
        """

    def Size(self) -> nanoocp.gp.gp_XYZ:
        """returns the size"""

    def XLength(self) -> float:
        """returns the length in the local X-direction"""

    def YLength(self) -> float:
        """returns the length in the local Y-direction"""

    def ZLength(self) -> float:
        """returns the length in the local Z-direction"""

    def Center(self) -> nanoocp.gp.gp_Pnt:
        """returns the center of the ellipsoid"""

    def TransformedCenter(self) -> nanoocp.gp.gp_Pnt:
        """
        returns the center of the ellipsoid after applying
        TransformationMatrix
        """

    def XAxis(self) -> nanoocp.gp.gp_Dir:
        """returns the vector corresponding to the local X-direction"""

    def TransformedXAxis(self) -> nanoocp.gp.gp_Dir:
        """
        returns the vector corresponding to the local X-direction
        after applying TransformationMatrix
        """

    def YAxis(self) -> nanoocp.gp.gp_Dir:
        """
        returns the vector corresponding to the local Y-direction
        which is got by taking cross product of ZAxis and XAxis
        """

    def TransformedYAxis(self) -> nanoocp.gp.gp_Dir:
        """
        returns the vector corresponding to the local Y-direction
        (which is got by taking cross product of ZAxis and XAxis)
        after applying TransformationMatrix
        """

    def ZAxis(self) -> nanoocp.gp.gp_Dir:
        """returns the vector corresponding to the local Z-direction"""

    def TransformedZAxis(self) -> nanoocp.gp.gp_Dir:
        """
        returns the vector corresponding to the local Z-direction
        after applying TransformationMatrix
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_Loop(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines Loop, Type <508> Form Number <1>
    in package IGESSolid
    A Loop entity specifies a bound of a face. It represents
    a connected collection of face boundaries, seams, and
    poles of a single face.

    From IGES-5.3, a Loop can be free with Form Number 0,
    else it is a bound of a face (it is the default)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_Loop) -> None: ...

    def Init(self, types: nanoocp.NCollection.NCollection_HArray1[int] | None, edges: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None, index: nanoocp.NCollection.NCollection_HArray1[int] | None, orient: nanoocp.NCollection.NCollection_HArray1[int] | None, nbParameterCurves: nanoocp.NCollection.NCollection_HArray1[int] | None, isoparametricFlags: nanoocp.IGESBasic.IGESBasic_HArray1OfHArray1OfInteger | None, curves: nanoocp.IGESBasic.IGESBasic_HArray1OfHArray1OfIGESEntity | None) -> None:
        """
        This method is used to set the fields of the class Loop
        - types              : 0 = Edge; 1 = Vertex
        - edges              : Pointer to the EdgeList or VertexList
        - index              : Index of the edge into the EdgeList
        VertexList entity
        - orient             : Orientation flag of the edge
        - nbParameterCurves  : the number of parameter space curves
        for each edge
        - isoparametricFlags : the isoparametric flag of the
        parameter space curve
        - curves             : the parameter space curves
        raises exception if length of types, edges, index, orient and
        nbParameterCurves do not match or the length of
        isoparametricFlags and curves do not match
        """

    def IsBound(self) -> bool:
        """Tells if a Loop is a Bound (FN 1) else it is free (FN 0)"""

    def SetBound(self, bound: bool) -> None:
        """
        Sets or Unset the Bound Status (from Form Number)
        Default is True
        """

    def NbEdges(self) -> int:
        """returns the number of edge tuples"""

    def EdgeType(self, Index: int) -> int:
        """
        returns the type of Index'th edge (0 = Edge, 1 = Vertex)
        raises exception if Index <= 0 or Index > NbEdges()
        """

    def Edge(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        return the EdgeList or VertexList corresponding to the Index
        raises exception if Index <= 0 or Index > NbEdges()
        """

    def Orientation(self, Index: int) -> bool:
        """
        returns the orientation flag corresponding to Index'th edge
        raises exception if Index <= 0 or Index > NbEdges()
        """

    def NbParameterCurves(self, Index: int) -> int:
        """
        return the number of parameter space curves associated with
        Index'th Edge
        raises exception if Index <= 0 or Index > NbEdges()
        """

    def IsIsoparametric(self, EdgeIndex: int, CurveIndex: int) -> bool: ...

    def ParametricCurve(self, EdgeIndex: int, CurveIndex: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the CurveIndex'th parameter space curve associated with
        EdgeIndex'th edge
        raises exception if EdgeIndex <= 0 or EdgeIndex > NbEdges() or
        if CurveIndex <= 0 or CurveIndex > NbParameterCurves(EdgeIndex)
        """

    def ListIndex(self, num: int) -> int:
        """raises exception If num <= 0 or num > NbEdges()"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_Face(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines Face, Type <510> Form Number <1>
    in package IGESSolid
    Face entity is a bound (partial) which has finite area
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_Face) -> None: ...

    def Init(self, aSurface: nanoocp.IGESData.IGESData_IGESEntity | None, outerLoopFlag: bool, loops: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESSolid.IGESSolid_Loop] | None) -> None:
        """
        This method is used to set the fields of the class Face
        - aSurface      : Pointer to the underlying surface
        - outerLoopFlag : True means the first loop is the outer loop
        - loops         : Array of loops bounding the face
        """

    def Surface(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the underlying surface of the face"""

    def NbLoops(self) -> int:
        """returns the number of the loops bounding the face"""

    def HasOuterLoop(self) -> bool:
        """checks whether there is an outer loop or not"""

    def Loop(self, Index: int) -> IGESSolid_Loop:
        """
        returns the Index'th loop that bounds the face
        raises exception if Index < 0 or Index >= NbLoops
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_GeneralModule(nanoocp.IGESData.IGESData_GeneralModule):
    """
    Definition of General Services for IGESSolid (specific part)
    This Services comprise : Shared & Implied Lists, Copy, Check
    """

    @overload
    def __init__(self) -> None:
        """Creates a GeneralModule from IGESSolid and puts it into GeneralLib"""

    @overload
    def __init__(self, theOther: IGESSolid_GeneralModule) -> None: ...

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
        Shape for all
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_Shell(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines Shell, Type <514> Form Number <1>
    in package IGESSolid
    Shell entity is a connected entity of dimensionality 2
    which divides R3 into two arcwise connected open subsets,
    one of which is finite. Inside of the shell is defined to
    be the finite region.
    From IGES-5.3, Form can be <1> for Closed or <2> for Open
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_Shell) -> None: ...

    def Init(self, allFaces: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESSolid.IGESSolid_Face] | None, allOrient: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """
        This method is used to set the fields of the class Shell
        - allFaces  : the faces comprising the shell
        - allOrient : the orientation flags of the shell
        raises exception if length of allFaces & allOrient do not match
        """

    def IsClosed(self) -> bool:
        """
        Tells if a Shell is Closed, i.e. if its FormNumber is 1
        (this is the default)
        """

    def SetClosed(self, closed: bool) -> None:
        """Sets or Unsets the Closed status (FormNumber = 1 else 2)"""

    def NbFaces(self) -> int:
        """returns the number of the face entities in the shell"""

    def Face(self, Index: int) -> IGESSolid_Face:
        """
        returns the Index'th face entity of the shell
        raises exception if Index <= 0 or Index > NbFaces()
        """

    def Orientation(self, Index: int) -> bool:
        """
        returns the orientation of Index'th face w.r.t the direction of
        the underlying surface
        raises exception if Index <= 0 or Index > NbFaces()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_ManifoldSolid(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines ManifoldSolid, Type <186> Form Number <0>
    in package IGESSolid
    A manifold solid is a bounded, closed, and finite volume
    in three dimensional Euclidean space
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_ManifoldSolid) -> None: ...

    def Init(self, aShell: IGESSolid_Shell | None, shellflag: bool, voidShells: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESSolid.IGESSolid_Shell] | None, voidShellFlags: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """
        This method is used to set the fields of the class
        ManifoldSolid
        - aShell         : pointer to the shell
        - shellflag      : orientation flag of shell
        - voidShells     : the void shells
        - voidShellFlags : orientation of the void shells
        raises exception if length of voidShells and voidShellFlags
        do not match
        """

    def Shell(self) -> IGESSolid_Shell:
        """returns the Shell entity which is being referred"""

    def OrientationFlag(self) -> bool:
        """returns the orientation flag of the shell"""

    def NbVoidShells(self) -> int:
        """returns the number of void shells"""

    def VoidShell(self, Index: int) -> IGESSolid_Shell:
        """
        returns Index'th void shell.
        raises exception if Index <= 0 or Index > NbVoidShells()
        """

    def VoidOrientationFlag(self, Index: int) -> bool:
        """
        returns Index'th orientation flag.
        raises exception if Index <= 0 or Index > NbVoidShells()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_PlaneSurface(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines PlaneSurface, Type <190> Form Number <0,1>
    in package IGESSolid
    A plane surface entity is defined by a point on the
    surface and a normal to it.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_PlaneSurface) -> None: ...

    def Init(self, aLocation: nanoocp.IGESGeom.IGESGeom_Point | None, aNormal: nanoocp.IGESGeom.IGESGeom_Direction | None, refdir: nanoocp.IGESGeom.IGESGeom_Direction | None) -> None:
        """
        This method is used to set the fields of the class
        PlaneSurface
        - aLocation : the point on the surface
        - aNormal   : the surface normal direction
        - refdir    : the reference direction (default NULL) for
        unparameterised curves
        """

    def LocationPoint(self) -> nanoocp.IGESGeom.IGESGeom_Point:
        """returns the point on the surface"""

    def Normal(self) -> nanoocp.IGESGeom.IGESGeom_Direction:
        """returns the normal to the surface"""

    def ReferenceDir(self) -> nanoocp.IGESGeom.IGESGeom_Direction:
        """
        returns the reference direction (for parameterised curve)
        returns NULL for unparameterised curve
        """

    def IsParametrised(self) -> bool:
        """returns True if parameterised, else False"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_Protocol(nanoocp.IGESData.IGESData_Protocol):
    """Description of Protocol for IGESSolid"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_Protocol) -> None: ...

    def NbResources(self) -> int:
        """
        Gives the count of Resource Protocol. Here, one
        (Protocol from IGESGeom)
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

class IGESSolid_ReadWriteModule(nanoocp.IGESData.IGESData_ReadWriteModule):
    """
    Defines Solid File Access Module for IGESSolid (specific parts)
    Specific actions concern : Read and Write Own Parameters of
    an IGESEntity.
    """

    @overload
    def __init__(self) -> None:
        """Creates a ReadWriteModule & puts it into ReaderLib & WriterLib"""

    @overload
    def __init__(self, theOther: IGESSolid_ReadWriteModule) -> None: ...

    def CaseIGES(self, typenum: int, formnum: int) -> int:
        """Defines Case Numbers for Entities of IGESSolid"""

    def ReadOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """Reads own parameters from file for an Entity of IGESSolid"""

    def WriteOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_RightAngularWedge(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines RightAngularWedge, Type <152> Form Number <0>
    in package IGESSolid
    A right angular wedge is a triangular/trapezoidal prism
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_RightAngularWedge) -> None: ...

    def Init(self, aSize: nanoocp.gp.gp_XYZ, lowX: float, aCorner: nanoocp.gp.gp_XYZ, anXAxis: nanoocp.gp.gp_XYZ, anZAxis: nanoocp.gp.gp_XYZ) -> None:
        """
        This method is used to set the fields of the class
        RightAngularWedge
        - aSize    : the lengths along the local axes
        - lowX     : the length at the smaller X-side
        - aCorner  : the corner point coordinates
        default (0,0,0)
        - anXAxis  : the unit vector defining local X-axis
        default (1,0,0)
        - anZAxis  : the unit vector defining local Z-axis
        default (0,0,1)
        """

    def Size(self) -> nanoocp.gp.gp_XYZ:
        """returns the size"""

    def XBigLength(self) -> float:
        """returns the length along the local X-axis"""

    def XSmallLength(self) -> float:
        """returns the smaller length along the local X-direction at Y=LY"""

    def YLength(self) -> float:
        """returns the length along the local Y-axis"""

    def ZLength(self) -> float:
        """returns the length along the local Z-axis"""

    def Corner(self) -> nanoocp.gp.gp_Pnt:
        """returns the corner point coordinates"""

    def TransformedCorner(self) -> nanoocp.gp.gp_Pnt:
        """
        returns the corner point coordinates after applying
        TransformationMatrix
        """

    def XAxis(self) -> nanoocp.gp.gp_Dir:
        """returns the direction defining the local X-axis"""

    def TransformedXAxis(self) -> nanoocp.gp.gp_Dir:
        """
        returns the direction defining the local X-axis
        after applying the TransformationMatrix
        """

    def YAxis(self) -> nanoocp.gp.gp_Dir:
        """
        returns the direction defining the local Y-axis
        it is got by taking the cross product of ZAxis and XAxis
        """

    def TransformedYAxis(self) -> nanoocp.gp.gp_Dir:
        """
        returns the direction defining the local Y-axis
        after applying the TransformationMatrix
        """

    def ZAxis(self) -> nanoocp.gp.gp_Dir:
        """returns the direction defining the local Z-axis"""

    def TransformedZAxis(self) -> nanoocp.gp.gp_Dir:
        """
        returns the direction defining the local Z-axis
        after applying the TransformationMatrix
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_SelectedComponent(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines SelectedComponent, Type <182> Form Number <0>
    in package IGESSolid
    The Selected Component entity provides a means of
    selecting one component of a disjoint CSG solid
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_SelectedComponent) -> None: ...

    def Init(self, anEntity: IGESSolid_BooleanTree | None, selectPnt: nanoocp.gp.gp_XYZ) -> None:
        """
        This method is used to set the fields of the class
        SelectedComponent
        - anEntity  : the Boolean tree entity
        - selectPnt : Point in or on the desired component
        """

    def Component(self) -> IGESSolid_BooleanTree:
        """returns the Boolean tree entity"""

    def SelectPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the point on/in the selected component"""

    def TransformedSelectPoint(self) -> nanoocp.gp.gp_Pnt:
        """
        returns the point on/in the selected component
        after applying TransformationMatrix
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_SolidAssembly(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines SolidAssembly, Type <184> Form <0>
    in package IGESSolid
    Solid assembly is a collection of items which possess a
    shared fixed geometric relationship.

    From IGES-5.3, From 1 says that at least one item is a Brep
    else all are Primitives, Boolean Trees, Solid Instances or
    other Assemblies
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_SolidAssembly) -> None: ...

    def Init(self, allItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None, allMatrices: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGeom.IGESGeom_TransformationMatrix] | None) -> None:
        """
        This method is used to set the fields of the class
        SolidAssembly
        - allItems    : the collection of items
        - allMatrices : transformation matrices corresponding to each
        item
        raises exception if the length of allItems & allMatrices
        do not match
        """

    def HasBrep(self) -> bool:
        """Tells if at least one item is a Brep, from FormNumber"""

    def SetBrep(self, hasbrep: bool) -> None:
        """
        Sets or Unsets the status "HasBrep" from FormNumber
        Default is False
        """

    def NbItems(self) -> int:
        """returns the number of items in the collection"""

    def Item(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the Index'th item
        raises exception if Index <= 0 or Index > NbItems()
        """

    def TransfMatrix(self, Index: int) -> nanoocp.IGESGeom.IGESGeom_TransformationMatrix:
        """
        returns the transformation matrix of the Index'th item
        raises exception if Index <= 0 or Index > NbItems()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_SolidInstance(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines SolidInstance, Type <430> Form Number <0>
    in package IGESSolid
    This provides a mechanism for replicating a solid
    representation.

    From IGES-5.3, Form may be <1> for a BREP
    Else it is for a Boolean Tree, Primitive, other Solid Inst.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_SolidInstance) -> None: ...

    def Init(self, anEntity: nanoocp.IGESData.IGESData_IGESEntity | None) -> None:
        """
        This method is used to set the fields of the class
        SolidInstance
        - anEntity : the entity corresponding to the solid
        """

    def IsBrep(self) -> bool:
        """
        Tells if a SolidInstance is for a BREP
        Default is False
        """

    def SetBrep(self, brep: bool) -> None:
        """Sets or unsets the Brep status (FormNumber = 1 else 0)"""

    def Entity(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the solid entity"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_SolidOfLinearExtrusion(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines SolidOfLinearExtrusion, Type <164> Form Number <0>
    in package IGESSolid
    Solid of linear extrusion is defined by translating an
    area determined by a planar curve
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_SolidOfLinearExtrusion) -> None: ...

    def Init(self, aCurve: nanoocp.IGESData.IGESData_IGESEntity | None, aLength: float, aDirection: nanoocp.gp.gp_XYZ) -> None:
        """
        This method is used to set the fields of the class
        SolidOfLinearExtrusion
        - aCurve     : the planar curve that is to be translated
        - aLength    : the length of extrusion
        - aDirection : the vector specifying the direction of extrusion
        default (0,0,1)
        """

    def Curve(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the planar curve that is to be translated"""

    def ExtrusionLength(self) -> float:
        """returns the Extrusion Length"""

    def ExtrusionDirection(self) -> nanoocp.gp.gp_Dir:
        """returns the Extrusion direction"""

    def TransformedExtrusionDirection(self) -> nanoocp.gp.gp_Dir:
        """returns ExtrusionDirection after applying TransformationMatrix"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_SolidOfRevolution(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines SolidOfRevolution, Type <162> Form Number <0,1>
    in package IGESSolid
    This entity is defined by revolving the area determined
    by a planar curve about a specified axis through a given
    fraction of full rotation.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_SolidOfRevolution) -> None: ...

    def Init(self, aCurve: nanoocp.IGESData.IGESData_IGESEntity | None, aFract: float, aAxisPnt: nanoocp.gp.gp_XYZ, aDirection: nanoocp.gp.gp_XYZ) -> None:
        """
        This method is used to set the fields of the class
        SolidOfRevolution
        - aCurve     : the curve entity that is to be revolved
        - aFract     : the fraction of full rotation (default 1.0)
        - aAxisPnt   : the point on the axis
        - aDirection : the direction of the axis
        """

    def SetClosedToAxis(self, mode: bool) -> None:
        """
        Sets the Curve to be by default, Closed to Axis (Form 0)
        if <mode> is True, Closed to Itself (Form 1) else
        """

    def IsClosedToAxis(self) -> bool:
        """
        Returns True if Form Number = 0
        if Form no is 0, then the curve is closed to axis
        if 1, the curve is closed to itself.
        """

    def Curve(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the curve entity that is to be revolved"""

    def Fraction(self) -> float:
        """
        returns the fraction of full rotation that the curve is to
        be rotated
        """

    def AxisPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the point on the axis"""

    def TransformedAxisPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the point on the axis after applying Trans.Matrix"""

    def Axis(self) -> nanoocp.gp.gp_Dir:
        """returns the direction of the axis"""

    def TransformedAxis(self) -> nanoocp.gp.gp_Dir:
        """
        returns the direction of the axis after applying
        TransformationMatrix
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_SpecificModule(nanoocp.IGESData.IGESData_SpecificModule):
    """Defines Services attached to IGES Entities : Dump, for IGESSolid"""

    @overload
    def __init__(self) -> None:
        """Creates a SpecificModule from IGESSolid & puts it into SpecificLib"""

    @overload
    def __init__(self, theOther: IGESSolid_SpecificModule) -> None: ...

    def OwnDump(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Specific Dump (own parameters) for IGESSolid"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_Sphere(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines Sphere, Type <158> Form Number <0>
    in package IGESSolid
    This defines a sphere with a center and radius
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_Sphere) -> None: ...

    def Init(self, aRadius: float, aCenter: nanoocp.gp.gp_XYZ) -> None:
        """
        This method is used to set the fields of the class Sphere
        - aRadius : the radius of the sphere
        - aCenter : the center point coordinates (default (0,0,0))
        """

    def Radius(self) -> float:
        """returns the radius of the sphere"""

    def Center(self) -> nanoocp.gp.gp_Pnt:
        """returns the center of the sphere"""

    def TransformedCenter(self) -> nanoocp.gp.gp_Pnt:
        """
        returns the center of the sphere after applying
        TransformationMatrix
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_SphericalSurface(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines SphericalSurface, Type <196> Form Number <0,1>
    in package IGESSolid
    Spherical surface is defined by a center and radius.
    In case of parametrised surface an axis and a
    reference direction is provided.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_SphericalSurface) -> None: ...

    def Init(self, aCenter: nanoocp.IGESGeom.IGESGeom_Point | None, aRadius: float, anAxis: nanoocp.IGESGeom.IGESGeom_Direction | None, aRefdir: nanoocp.IGESGeom.IGESGeom_Direction | None) -> None:
        """
        This method is used to set the fields of the class
        SphericalSurface
        - aCenter : the coordinates of the center point
        - aRadius : value of radius
        - anAxis  : the direction of the axis
        Null in case of Unparametrised surface
        - aRefdir : the reference direction
        Null in case of Unparametrised surface
        """

    def Center(self) -> nanoocp.IGESGeom.IGESGeom_Point:
        """returns the center of the spherical surface"""

    def TransformedCenter(self) -> nanoocp.gp.gp_Pnt:
        """
        returns the center of the spherical surface after applying
        TransformationMatrix
        """

    def Radius(self) -> float:
        """returns the radius of the spherical surface"""

    def Axis(self) -> nanoocp.IGESGeom.IGESGeom_Direction:
        """
        returns the direction of the axis (Parametrised surface)
        Null is returned if the surface is not parametrised
        """

    def ReferenceDir(self) -> nanoocp.IGESGeom.IGESGeom_Direction:
        """
        returns the reference direction (Parametrised surface)
        Null is returned if the surface is not parametrised
        """

    def IsParametrised(self) -> bool:
        """Returns True if the surface is parametrised, else False"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_ToolBlock:
    """
    Tool to work on a Block. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolBlock, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolBlock) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_Block | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_Block | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_Block | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Block <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_Block | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_Block | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_Block | None, entto: IGESSolid_Block | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_Block | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolBooleanTree:
    """
    Tool to work on a BooleanTree. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolBooleanTree, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolBooleanTree) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_BooleanTree | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_BooleanTree | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_BooleanTree | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a BooleanTree <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_BooleanTree | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_BooleanTree | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_BooleanTree | None, entto: IGESSolid_BooleanTree | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_BooleanTree | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolConeFrustum:
    """
    Tool to work on a ConeFrustum. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolConeFrustum, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolConeFrustum) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_ConeFrustum | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_ConeFrustum | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_ConeFrustum | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ConeFrustum <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_ConeFrustum | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_ConeFrustum | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_ConeFrustum | None, entto: IGESSolid_ConeFrustum | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_ConeFrustum | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolConicalSurface:
    """
    Tool to work on a ConicalSurface. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolConicalSurface, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolConicalSurface) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_ConicalSurface | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_ConicalSurface | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_ConicalSurface | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ConicalSurface <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_ConicalSurface | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_ConicalSurface | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_ConicalSurface | None, entto: IGESSolid_ConicalSurface | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_ConicalSurface | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolCylinder:
    """
    Tool to work on a Cylinder. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolCylinder, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolCylinder) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_Cylinder | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_Cylinder | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_Cylinder | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Cylinder <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_Cylinder | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_Cylinder | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_Cylinder | None, entto: IGESSolid_Cylinder | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_Cylinder | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolCylindricalSurface:
    """
    Tool to work on a CylindricalSurface. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolCylindricalSurface, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolCylindricalSurface) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_CylindricalSurface | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_CylindricalSurface | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_CylindricalSurface | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a CylindricalSurface <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_CylindricalSurface | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_CylindricalSurface | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_CylindricalSurface | None, entto: IGESSolid_CylindricalSurface | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_CylindricalSurface | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolEdgeList:
    """
    Tool to work on a EdgeList. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolEdgeList, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolEdgeList) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_EdgeList | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_EdgeList | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_EdgeList | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a EdgeList <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_EdgeList | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_EdgeList | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_EdgeList | None, entto: IGESSolid_EdgeList | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_EdgeList | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolEllipsoid:
    """
    Tool to work on a Ellipsoid. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolEllipsoid, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolEllipsoid) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_Ellipsoid | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_Ellipsoid | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_Ellipsoid | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Ellipsoid <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_Ellipsoid | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_Ellipsoid | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_Ellipsoid | None, entto: IGESSolid_Ellipsoid | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_Ellipsoid | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolFace:
    """
    Tool to work on a Face. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolFace, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolFace) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_Face | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_Face | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_Face | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Face <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_Face | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_Face | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_Face | None, entto: IGESSolid_Face | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_Face | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolLoop:
    """
    Tool to work on a Loop. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolLoop, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolLoop) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_Loop | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_Loop | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_Loop | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Loop <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_Loop | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_Loop | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_Loop | None, entto: IGESSolid_Loop | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_Loop | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolManifoldSolid:
    """
    Tool to work on a ManifoldSolid. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolManifoldSolid, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolManifoldSolid) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_ManifoldSolid | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_ManifoldSolid | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_ManifoldSolid | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ManifoldSolid <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_ManifoldSolid | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_ManifoldSolid | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_ManifoldSolid | None, entto: IGESSolid_ManifoldSolid | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_ManifoldSolid | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolPlaneSurface:
    """
    Tool to work on a PlaneSurface. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolPlaneSurface, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolPlaneSurface) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_PlaneSurface | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_PlaneSurface | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_PlaneSurface | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a PlaneSurface <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_PlaneSurface | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_PlaneSurface | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_PlaneSurface | None, entto: IGESSolid_PlaneSurface | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_PlaneSurface | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolRightAngularWedge:
    """
    Tool to work on a RightAngularWedge. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolRightAngularWedge, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolRightAngularWedge) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_RightAngularWedge | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_RightAngularWedge | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_RightAngularWedge | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a RightAngularWedge <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_RightAngularWedge | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_RightAngularWedge | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_RightAngularWedge | None, entto: IGESSolid_RightAngularWedge | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_RightAngularWedge | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolSelectedComponent:
    """
    Tool to work on a SelectedComponent. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSelectedComponent, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolSelectedComponent) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_SelectedComponent | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_SelectedComponent | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_SelectedComponent | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a SelectedComponent <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_SelectedComponent | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_SelectedComponent | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_SelectedComponent | None, entto: IGESSolid_SelectedComponent | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_SelectedComponent | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolShell:
    """
    Tool to work on a Shell. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolShell, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolShell) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_Shell | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_Shell | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_Shell | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Shell <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_Shell | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_Shell | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_Shell | None, entto: IGESSolid_Shell | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_Shell | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolSolidAssembly:
    """
    Tool to work on a SolidAssembly. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSolidAssembly, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolSolidAssembly) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_SolidAssembly | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_SolidAssembly | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_SolidAssembly | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a SolidAssembly <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_SolidAssembly | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_SolidAssembly | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_SolidAssembly | None, entto: IGESSolid_SolidAssembly | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_SolidAssembly | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolSolidInstance:
    """
    Tool to work on a SolidInstance. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSolidInstance, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolSolidInstance) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_SolidInstance | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_SolidInstance | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_SolidInstance | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a SolidInstance <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_SolidInstance | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_SolidInstance | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_SolidInstance | None, entto: IGESSolid_SolidInstance | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_SolidInstance | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolSolidOfLinearExtrusion:
    """
    Tool to work on a SolidOfLinearExtrusion. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSolidOfLinearExtrusion, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolSolidOfLinearExtrusion) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_SolidOfLinearExtrusion | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_SolidOfLinearExtrusion | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_SolidOfLinearExtrusion | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a SolidOfLinearExtrusion <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_SolidOfLinearExtrusion | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_SolidOfLinearExtrusion | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_SolidOfLinearExtrusion | None, entto: IGESSolid_SolidOfLinearExtrusion | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_SolidOfLinearExtrusion | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolSolidOfRevolution:
    """
    Tool to work on a SolidOfRevolution. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSolidOfRevolution, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolSolidOfRevolution) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_SolidOfRevolution | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_SolidOfRevolution | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_SolidOfRevolution | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a SolidOfRevolution <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_SolidOfRevolution | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_SolidOfRevolution | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_SolidOfRevolution | None, entto: IGESSolid_SolidOfRevolution | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_SolidOfRevolution | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolSphere:
    """
    Tool to work on a Sphere. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSphere, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolSphere) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_Sphere | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_Sphere | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_Sphere | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Sphere <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_Sphere | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_Sphere | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_Sphere | None, entto: IGESSolid_Sphere | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_Sphere | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolSphericalSurface:
    """
    Tool to work on a SphericalSurface. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSphericalSurface, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolSphericalSurface) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_SphericalSurface | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_SphericalSurface | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_SphericalSurface | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a SphericalSurface <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_SphericalSurface | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_SphericalSurface | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_SphericalSurface | None, entto: IGESSolid_SphericalSurface | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_SphericalSurface | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolToroidalSurface:
    """
    Tool to work on a ToroidalSurface. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolToroidalSurface, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolToroidalSurface) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_ToroidalSurface | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_ToroidalSurface | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_ToroidalSurface | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ToroidalSurface <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_ToroidalSurface | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_ToroidalSurface | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_ToroidalSurface | None, entto: IGESSolid_ToroidalSurface | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_ToroidalSurface | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolTorus:
    """
    Tool to work on a Torus. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolTorus, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolTorus) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_Torus | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_Torus | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_Torus | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Torus <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_Torus | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_Torus | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_Torus | None, entto: IGESSolid_Torus | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_Torus | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_ToolVertexList:
    """
    Tool to work on a VertexList. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolVertexList, ready to work"""

    @overload
    def __init__(self, theOther: IGESSolid_ToolVertexList) -> None: ...

    def ReadOwnParams(self, ent: IGESSolid_VertexList | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESSolid_VertexList | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESSolid_VertexList | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a VertexList <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESSolid_VertexList | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESSolid_VertexList | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESSolid_VertexList | None, entto: IGESSolid_VertexList | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESSolid_VertexList | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESSolid_TopoBuilder:
    """
    This class manages the creation of an IGES Topologic entity
    (BREP : ManifoldSolid, Shell, Face)
    This includes definiting of Vertex and Edge Lists,
    building of Edges and Loops
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an empty TopoBuilder
        This creates also a unique VertexList and a unique EdgeList,
        empty, but which can be referenced from starting
        """

    @overload
    def __init__(self, theOther: IGESSolid_TopoBuilder) -> None: ...

    def Clear(self) -> None:
        """
        Resets the TopoBuilder for an entirely new operation
        (with a new EdgeList, a new VertexList, new Shells, ...)
        """

    def AddVertex(self, val: nanoocp.gp.gp_XYZ) -> None:
        """Adds a Vertex to the VertexList"""

    def NbVertices(self) -> int:
        """Returns the count of already recorded Vertices"""

    def Vertex(self, num: int) -> nanoocp.gp.gp_XYZ:
        """Returns a Vertex, given its rank"""

    def VertexList(self) -> IGESSolid_VertexList:
        """
        Returns the VertexList. It can be referenced, but it remains
        empty until call to EndShell or EndSolid
        """

    def AddEdge(self, curve: nanoocp.IGESData.IGESData_IGESEntity | None, vstart: int, vend: int) -> None:
        """
        Adds an Edge (3D) to the EdgeList, defined by a Curve and
        two number of Vertex, for start and end
        """

    def NbEdges(self) -> int:
        """Returns the count of recorded Edges (3D)"""

    def Edge(self, num: int) -> tuple[nanoocp.IGESData.IGESData_IGESEntity, int, int]:
        """Returns the definition of an Edge (3D) given its rank"""

    def EdgeList(self) -> IGESSolid_EdgeList:
        """
        Returns the EdgeList. It can be referenced, but it remains
        empty until call to EndShell or EndSolid
        """

    def MakeLoop(self) -> None:
        """
        Begins the definition of a new Loop : it is the Current Loop
        All Edges (UV) defined by MakeEdge/EndEdge will be added in it
        The Loop can then be referenced but is empty. It will be
        filled with its Edges(UV) by EndLoop (from SetOuter/AddInner)
        """

    def MakeEdge(self, edgetype: int, edge3d: int, orientation: int) -> None:
        """
        Defines an Edge(UV), to be added in the current Loop by EndEdge
        <edgetype> gives the type of the edge
        <edge3d> identifies the Edge(3D) used as support
        The EdgeList is always the current one
        <orientation gives the orientation flag
        It is then necessary to :
        - give the parametric curves
        - close the definition of this edge(UV) by EndEdge, else
        the next call to MakeEdge will erase this one
        """

    def AddCurveUV(self, curve: nanoocp.IGESData.IGESData_IGESEntity | None, iso: int) -> None:
        """Adds a Parametric Curve (UV) to the current Edge(UV)"""

    def EndEdge(self) -> None:
        """
        Closes the definition of an Edge(UV) and adds it to the
        current Loop
        """

    def MakeFace(self, surface: nanoocp.IGESData.IGESData_IGESEntity | None) -> None:
        """
        Begins the definition of a new Face, on a surface
        All Loops defined by MakeLoop will be added in it, according
        the closing call : SetOuter for the Outer Loop (by default,
        if SetOuter is not called, no OuterLoop is defined);
        AddInner for the list of Inner Loops (there can be none)
        """

    def SetOuter(self) -> None:
        """
        Closes the current Loop and sets it Loop as Outer Loop. If no
        current Loop has yet been defined, does nothing.
        """

    def AddInner(self) -> None:
        """
        Closes the current Loop and adds it to the list of Inner Loops
        for the current Face
        """

    def EndFace(self, orientation: int) -> None:
        """
        Closes the definition of the current Face, fills it and adds
        it to the current Shell with an orientation flag (0/1)
        """

    def MakeShell(self) -> None:
        """
        Begins the definition of a new Shell (either Simple or in a
        Solid)
        """

    def EndSimpleShell(self) -> None:
        """Closes the whole definition as that of a simple Shell"""

    def SetMainShell(self, orientation: int) -> None:
        """
        Closes the definition of the current Shell as for the Main
        Shell of a Solid, with an orientation flag (0/1)
        """

    def AddVoidShell(self, orientation: int) -> None:
        """
        Closes the definition of the current Shell and adds it to the
        list of Void Shells of a Solid, with an orientation flag (0/1)
        """

    def EndSolid(self) -> None:
        """
        Closes the whole definition as that of a ManifoldSolid
        Its call is exclusive from that of EndSimpleShell
        """

    def Shell(self) -> IGESSolid_Shell:
        """
        Returns the current Shell. The current Shell is created empty
        by MakeShell and filled by EndShell
        """

    def Solid(self) -> IGESSolid_ManifoldSolid:
        """
        Returns the current ManifoldSolid. It is created empty by
        Create and filled by EndSolid
        """

class IGESSolid_ToroidalSurface(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines ToroidalSurface, Type <198> Form Number <0,1>
    in package IGESSolid
    This entity is defined by the center point, the axis
    direction and the major and minor radii. In case of
    parametrised surface a reference direction is provided.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_ToroidalSurface) -> None: ...

    def Init(self, aCenter: nanoocp.IGESGeom.IGESGeom_Point | None, anAxis: nanoocp.IGESGeom.IGESGeom_Direction | None, majRadius: float, minRadius: float, Refdir: nanoocp.IGESGeom.IGESGeom_Direction | None) -> None:
        """
        This method is used to set the fields of the class
        ToroidalSurface
        - aCenter   : the center point coordinates
        - anAxis    : the direction of the axis
        - majRadius : the major radius
        - minRadius : the minor radius
        - Refdir    : the reference direction (parametrised)
        default Null for unparametrised surface
        """

    def Center(self) -> nanoocp.IGESGeom.IGESGeom_Point:
        """returns the center point coordinates of the surface"""

    def TransformedCenter(self) -> nanoocp.gp.gp_Pnt:
        """
        returns the center point coordinates of the surface
        after applying TransformationMatrix
        """

    def Axis(self) -> nanoocp.IGESGeom.IGESGeom_Direction:
        """returns the direction of the axis"""

    def MajorRadius(self) -> float:
        """returns the major radius of the surface"""

    def MinorRadius(self) -> float:
        """returns the minor radius of the surface"""

    def ReferenceDir(self) -> nanoocp.IGESGeom.IGESGeom_Direction:
        """
        returns the reference direction (parametrised surface)
        Null is returned if the surface is not parametrised
        """

    def IsParametrised(self) -> bool:
        """Returns True if the surface is parametrised, else False"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESSolid_Torus(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines Torus, Type <160> Form Number <0>
    in package IGESSolid
    A Torus is a solid formed by revolving a circular disc
    about a specified coplanar axis.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESSolid_Torus) -> None: ...

    def Init(self, R1: float, R2: float, aPoint: nanoocp.gp.gp_XYZ, anAxisdir: nanoocp.gp.gp_XYZ) -> None:
        """
        This method is used to set the fields of the class Torus
        - R1     : distance from center of torus to center
        of circular disc to be revolved
        - R2     : radius of circular disc
        - aPoint : center point coordinates (default (0,0,0))
        - anAxis : unit vector in axis direction (default (0,0,1))
        """

    def MajorRadius(self) -> float:
        """
        returns the distance from the center of torus to the center of
        the disc to be revolved
        """

    def DiscRadius(self) -> float:
        """returns the radius of the disc to be revolved"""

    def AxisPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the center of torus"""

    def TransformedAxisPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the center of torus after applying TransformationMatrix"""

    def Axis(self) -> nanoocp.gp.gp_Dir:
        """returns direction of the axis"""

    def TransformedAxis(self) -> nanoocp.gp.gp_Dir:
        """returns direction of the axis after applying TransformationMatrix"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.IGESSolid
IGESSolid_Array1OfFace = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESSolid.IGESSolid_Face]
IGESSolid_Array1OfLoop = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESSolid.IGESSolid_Loop]
IGESSolid_Array1OfShell = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESSolid.IGESSolid_Shell]
IGESSolid_Array1OfVertexList = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESSolid.IGESSolid_VertexList]
IGESSolid_HArray1OfFace = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESSolid.IGESSolid_Face]
IGESSolid_HArray1OfLoop = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESSolid.IGESSolid_Loop]
IGESSolid_HArray1OfShell = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESSolid.IGESSolid_Shell]
IGESSolid_HArray1OfVertexList = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESSolid.IGESSolid_VertexList]
