"""OCCT package IMeshTools (toolkit TKMesh)"""

import enum
from typing import overload

import nanoocp.GeomAbs
import nanoocp.IMeshData
import nanoocp.Message
import nanoocp.Standard
import nanoocp.TopoDS
import nanoocp.gp


class IMeshTools_MeshAlgoType(enum.IntEnum):
    """
    Enumerates built-in meshing algorithms factories implementing IMeshTools_MeshAlgoFactory
    interface.
    """

    IMeshTools_MeshAlgoType_DEFAULT = -1

    IMeshTools_MeshAlgoType_Watson = 0

    IMeshTools_MeshAlgoType_Delabella = 1

IMeshTools_MeshAlgoType_DEFAULT: IMeshTools_MeshAlgoType = ...

IMeshTools_MeshAlgoType_Watson: IMeshTools_MeshAlgoType = ...

IMeshTools_MeshAlgoType_Delabella: IMeshTools_MeshAlgoType = ...

class IMeshTools_ModelBuilder(nanoocp.Message.Message_Algorithm):
    """
    Interface class represents API for tool building discrete model.

    The following statuses should be used by default:
    Message_Done1 - model has been successfully built.
    Message_Fail1 - empty shape.
    Message_Fail2 - model has not been build due to unexpected reason.
    """

    def Perform(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theParameters: IMeshTools_Parameters) -> nanoocp.IMeshData.IMeshData_Model:
        """
        Exceptions protected method to create discrete model for the given shape.
        Returns nullptr in case of failure.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshTools_Parameters:
    """Structure storing meshing parameters"""

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theOther: IMeshTools_Parameters) -> None: ...

    @staticmethod
    def RelMinSize() -> float:
        """
        Returns factor used to compute default value of MinSize
        (minimum mesh edge length) from deflection
        """

    @property
    def MeshAlgo(self) -> IMeshTools_MeshAlgoType:
        """2D Delaunay triangulation algorithm factory to use"""

    @MeshAlgo.setter
    def MeshAlgo(self, arg: IMeshTools_MeshAlgoType, /) -> None: ...

    @property
    def Angle(self) -> float:
        """Angular deflection used to tessellate the boundary edges"""

    @Angle.setter
    def Angle(self, arg: float, /) -> None: ...

    @property
    def Deflection(self) -> float:
        """Linear deflection used to tessellate the boundary edges"""

    @Deflection.setter
    def Deflection(self, arg: float, /) -> None: ...

    @property
    def AngleInterior(self) -> float:
        """Angular deflection used to tessellate the face interior"""

    @AngleInterior.setter
    def AngleInterior(self, arg: float, /) -> None: ...

    @property
    def DeflectionInterior(self) -> float:
        """Linear deflection used to tessellate the face interior"""

    @DeflectionInterior.setter
    def DeflectionInterior(self, arg: float, /) -> None: ...

    @property
    def MinSize(self) -> float:
        """
        Minimum size parameter limiting size of triangle's edges to prevent
        sinking into amplification in case of distorted curves and surfaces.
        """

    @MinSize.setter
    def MinSize(self, arg: float, /) -> None: ...

    @property
    def InParallel(self) -> bool:
        """Switches on/off multi-thread computation"""

    @InParallel.setter
    def InParallel(self, arg: bool, /) -> None: ...

    @property
    def Relative(self) -> bool:
        """
        Switches on/off relative computation of edge tolerance
        If true, deflection used for the polygonalisation of each edge will be
        <defle> * Size of Edge. The deflection used for the faces will be the
        maximum deflection of their edges.
        """

    @Relative.setter
    def Relative(self, arg: bool, /) -> None: ...

    @property
    def InternalVerticesMode(self) -> bool:
        """
        Mode to take or not to take internal face vertices into account
        in triangulation process
        """

    @InternalVerticesMode.setter
    def InternalVerticesMode(self, arg: bool, /) -> None: ...

    @property
    def ControlSurfaceDeflection(self) -> bool:
        """
        Parameter to check the deviation of triangulation and interior of
        the face
        """

    @ControlSurfaceDeflection.setter
    def ControlSurfaceDeflection(self, arg: bool, /) -> None: ...

    @property
    def EnableControlSurfaceDeflectionAllSurfaces(self) -> bool: ...

    @EnableControlSurfaceDeflectionAllSurfaces.setter
    def EnableControlSurfaceDeflectionAllSurfaces(self, arg: bool, /) -> None: ...

    @property
    def CleanModel(self) -> bool:
        """Cleans temporary data model when algorithm is finished."""

    @CleanModel.setter
    def CleanModel(self, arg: bool, /) -> None: ...

    @property
    def AdjustMinSize(self) -> bool:
        """
        Enables/disables local adjustment of min size depending on edge size.
        Disabled by default.
        """

    @AdjustMinSize.setter
    def AdjustMinSize(self, arg: bool, /) -> None: ...

    @property
    def ForceFaceDeflection(self) -> bool:
        """
        Enables/disables usage of shape tolerances for computing face deflection.
        Disabled by default.
        """

    @ForceFaceDeflection.setter
    def ForceFaceDeflection(self, arg: bool, /) -> None: ...

    @property
    def AllowQualityDecrease(self) -> bool:
        """
        Allows/forbids the decrease of the quality of the generated mesh
        over the existing one.
        """

    @AllowQualityDecrease.setter
    def AllowQualityDecrease(self, arg: bool, /) -> None: ...

class IMeshTools_ModelAlgo(nanoocp.Standard.Standard_Transient):
    """
    Interface class providing API for algorithms intended to update or modify discrete model.
    """

    def Perform(self, theModel: nanoocp.IMeshData.IMeshData_Model | None, theParameters: IMeshTools_Parameters, theRange: nanoocp.Message.Message_ProgressRange) -> bool:
        """Exceptions protected processing of the given model."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshTools_Context(nanoocp.IMeshData.IMeshData_Shape):
    """
    Interface class representing context of BRepMesh algorithm.
    Intended to cache discrete model and instances of tools for
    its processing.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: IMeshTools_Context) -> None: ...

    def BuildModel(self) -> bool:
        """
        Builds model using assigned model builder.
        @return True on success, False elsewhere.
        """

    def DiscretizeEdges(self) -> bool:
        """
        Performs discretization of model edges using assigned edge discret algorithm.
        @return True on success, False elsewhere.
        """

    def HealModel(self) -> bool:
        """
        Performs healing of discrete model built by DiscretizeEdges() method
        using assigned healing algorithm.
        @return True on success, False elsewhere.
        """

    def PreProcessModel(self) -> bool:
        """
        Performs pre-processing of discrete model using assigned algorithm.
        Performs auxiliary actions such as cleaning shape from old triangulation.
        @return True on success, False elsewhere.
        """

    def DiscretizeFaces(self, theRange: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Performs meshing of faces of discrete model using assigned meshing algorithm.
        @return True on success, False elsewhere.
        """

    def PostProcessModel(self) -> bool:
        """
        Performs post-processing of discrete model using assigned algorithm.
        @return True on success, False elsewhere.
        """

    def Clean(self) -> None:
        """Cleans temporary context data."""

    def GetModelBuilder(self) -> IMeshTools_ModelBuilder:
        """Gets instance of a tool to be used to build discrete model."""

    def SetModelBuilder(self, theBuilder: IMeshTools_ModelBuilder | None) -> None:
        """Sets instance of a tool to be used to build discrete model."""

    def GetEdgeDiscret(self) -> IMeshTools_ModelAlgo:
        """Gets instance of a tool to be used to discretize edges of a model."""

    def SetEdgeDiscret(self, theEdgeDiscret: IMeshTools_ModelAlgo | None) -> None:
        """Sets instance of a tool to be used to discretize edges of a model."""

    def GetModelHealer(self) -> IMeshTools_ModelAlgo:
        """Gets instance of a tool to be used to heal discrete model."""

    def SetModelHealer(self, theModelHealer: IMeshTools_ModelAlgo | None) -> None:
        """Sets instance of a tool to be used to heal discrete model."""

    def GetPreProcessor(self) -> IMeshTools_ModelAlgo:
        """Gets instance of pre-processing algorithm."""

    def SetPreProcessor(self, thePreProcessor: IMeshTools_ModelAlgo | None) -> None:
        """Sets instance of pre-processing algorithm."""

    def GetFaceDiscret(self) -> IMeshTools_ModelAlgo:
        """Gets instance of meshing algorithm."""

    def SetFaceDiscret(self, theFaceDiscret: IMeshTools_ModelAlgo | None) -> None:
        """Sets instance of meshing algorithm."""

    def GetPostProcessor(self) -> IMeshTools_ModelAlgo:
        """Gets instance of post-processing algorithm."""

    def SetPostProcessor(self, thePostProcessor: IMeshTools_ModelAlgo | None) -> None:
        """Sets instance of post-processing algorithm."""

    def GetParameters(self) -> IMeshTools_Parameters:
        """Gets parameters to be used for meshing."""

    def ChangeParameters(self) -> IMeshTools_Parameters:
        """Gets reference to parameters to be used for meshing."""

    def GetModel(self) -> nanoocp.IMeshData.IMeshData_Model:
        """Returns discrete model of a shape."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshTools_CurveTessellator(nanoocp.Standard.Standard_Transient):
    """Interface class providing API for edge tessellation tools."""

    def PointsNb(self) -> int:
        """Returns number of tessellation points."""

    def Value(self, theIndex: int, thePoint: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """
        Returns parameters of solution with the given index.
        @param theIndex index of tessellation point.
        @param thePoint tessellation point.
        @param theParameter parameters on PCurve corresponded to the solution.
        @return True in case of valid result, false elewhere.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshTools_MeshAlgo(nanoocp.Standard.Standard_Transient):
    """
    Interface class providing API for algorithms intended to create mesh for discrete face.
    """

    def Perform(self, theDFace: nanoocp.IMeshData.IMeshData_Face | None, theParameters: IMeshTools_Parameters, theRange: nanoocp.Message.Message_ProgressRange) -> None:
        """Performs processing of the given face."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshTools_MeshAlgoFactory(nanoocp.Standard.Standard_Transient):
    """
    Base interface for factories producing instances of triangulation
    algorithms taking into account type of surface of target face.
    """

    def GetAlgo(self, theSurfaceType: nanoocp.GeomAbs.GeomAbs_SurfaceType, theParameters: IMeshTools_Parameters) -> IMeshTools_MeshAlgo:
        """Creates instance of meshing algorithm for the given type of surface."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshTools_MeshBuilder(nanoocp.Message.Message_Algorithm):
    """
    Builds mesh for each face of shape without triangulation.
    In case if some faces of shape have already been triangulated
    checks deflection of existing polygonal model and re-uses it
    if deflection satisfies the specified parameter. Otherwise
    nullifies existing triangulation and build triangulation anew.

    The following statuses are used:
    Message_Done1 - algorithm has finished without errors.
    Message_Fail1 - invalid context.
    Message_Fail2 - algorithm has faced unexpected error.
    Message_Fail3 - fail to discretize edges.
    Message_Fail4 - can't heal discrete model.
    Message_Fail5 - fail to pre-process model.
    Message_Fail6 - fail to discretize faces.
    Message_Fail7 - fail to post-process model.
    Message_Warn1 - shape contains no objects to mesh.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theContext: IMeshTools_Context | None) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: IMeshTools_MeshBuilder) -> None: ...

    def SetContext(self, theContext: IMeshTools_Context | None) -> None:
        """Sets context for algorithm."""

    def GetContext(self) -> IMeshTools_Context:
        """Gets context of algorithm."""

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange) -> None:
        """Performs meshing to the shape using current context."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshTools_ShapeVisitor(nanoocp.Standard.Standard_Transient):
    """Interface class for shape visitor."""

    @overload
    def Visit(self, theFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Handles TopoDS_Face object."""

    @overload
    def Visit(self, theEdge: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Handles TopoDS_Edge object."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IMeshTools_ShapeExplorer(nanoocp.IMeshData.IMeshData_Shape):
    """Explores TopoDS_Shape for parts to be meshed - faces and free edges."""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: IMeshTools_ShapeExplorer) -> None: ...

    def Accept(self, theVisitor: IMeshTools_ShapeVisitor | None) -> None:
        """Starts exploring of a shape."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
