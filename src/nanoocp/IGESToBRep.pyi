"""OCCT package IGESToBRep (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.DE
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.IGESBasic
import nanoocp.IGESData
import nanoocp.IGESGeom
import nanoocp.IGESSolid
import nanoocp.Interface
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.ShapeExtend
import nanoocp.Standard
import nanoocp.TopoDS
import nanoocp.Transfer
import nanoocp.gp
import nanoocp.TCollection


class IGESToBRep:
    """
    Provides tools in order to transfer IGES entities
    to CAS.CADE.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESToBRep) -> None: ...

    @staticmethod
    def Init() -> None:
        """Creates and initializes default AlgoContainer."""

    @staticmethod
    def SetAlgoContainer(aContainer: IGESToBRep_AlgoContainer | None) -> None:
        """Sets default AlgoContainer"""

    @staticmethod
    def AlgoContainer() -> IGESToBRep_AlgoContainer:
        """Returns default AlgoContainer"""

    @staticmethod
    def IsCurveAndSurface(start: nanoocp.IGESData.IGESData_IGESEntity | None) -> bool:
        """
        Return True if the IGESEntity can be transferred by
        TransferCurveAndSurface.
        ex: All IGESEntity from IGESGeom
        """

    @staticmethod
    def IsBasicCurve(start: nanoocp.IGESData.IGESData_IGESEntity | None) -> bool:
        """
        Return True if the IGESEntity can be transferred by
        TransferBasicCurve.
        ex: CircularArc, ConicArc, Line, CopiousData,
        BSplineCurve, SplineCurve... from IGESGeom :
        104,110,112,126
        """

    @staticmethod
    def IsBasicSurface(start: nanoocp.IGESData.IGESData_IGESEntity | None) -> bool:
        """
        Return True if the IGESEntity can be transferred by
        TransferBasicSurface.
        ex: BSplineSurface, SplineSurface... from IGESGeom :
        114,128
        """

    @staticmethod
    def IsTopoCurve(start: nanoocp.IGESData.IGESData_IGESEntity | None) -> bool:
        """
        Return True if the IGESEntity can be transferred by
        TransferTopoCurve.
        ex: all Curves from IGESGeom :
        all basic curves,102,130,142,144
        """

    @staticmethod
    def IsTopoSurface(start: nanoocp.IGESData.IGESData_IGESEntity | None) -> bool:
        """
        Return True if the IGESEntity can be transferred by
        TransferTopoSurface.
        ex: All Surfaces from IGESGeom :
        all basic surfaces,108,118,120,122,141,143
        """

    @staticmethod
    def IsBRepEntity(start: nanoocp.IGESData.IGESData_IGESEntity | None) -> bool:
        """
        Return True if the IGESEntity can be transferred by
        TransferBRepEntity.
        ex: VertexList, EdgeList, Loop, Face, Shell,
        Manifold Solid BRep Object from IGESSolid :
        502, 504, 508, 510, 514, 186.
        """

    @staticmethod
    def IGESCurveToSequenceOfIGESCurve(curve: nanoocp.IGESData.IGESData_IGESEntity | None) -> tuple[int, nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]]: ...

    @staticmethod
    def TransferPCurve(fromedge: nanoocp.TopoDS.TopoDS_Edge, toedge: nanoocp.TopoDS.TopoDS_Edge, face: nanoocp.TopoDS.TopoDS_Face) -> bool: ...

class IGESToBRep_Actor(nanoocp.Transfer.Transfer_ActorOfTransientProcess):
    """
    This class performs the transfer of an Entity from
    IGESToBRep

    I.E. for each type of Entity, it invokes the appropriate Tool
    then returns the Binder which contains the Result
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESToBRep_Actor) -> None: ...

    def SetModel(self, model: nanoocp.Interface.Interface_InterfaceModel | None) -> None: ...

    def SetContinuity(self, continuity: int = 0) -> None:
        """
        ---Purpose   By default continuity = 0
        if continuity = 1 : try C1
        if continuity = 2 : try C2
        """

    def GetContinuity(self) -> int:
        """Return "thecontinuity\""""

    def Recognize(self, start: nanoocp.Standard.Standard_Transient | None) -> bool: ...

    def Transfer(self, start: nanoocp.Standard.Standard_Transient | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Transfer.Transfer_Binder: ...

    def UsedTolerance(self) -> float:
        """
        Returns the tolerance which was actually used, either from
        the file or from statics
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESToBRep_AlgoContainer(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: IGESToBRep_AlgoContainer) -> None: ...

    def SetToolContainer(self, TC: IGESToBRep_ToolContainer | None) -> None:
        """Sets ToolContainer"""

    def ToolContainer(self) -> IGESToBRep_ToolContainer:
        """Returns ToolContainer"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESToBRep_CurveAndSurface:
    """Provides methods to transfer CurveAndSurface from IGES to CASCADE."""

    @overload
    def __init__(self) -> None:
        """
        Creates a tool CurveAndSurface ready to run, with
        epsilons set to 1.E-04, myModeTopo to True, the
        optimization of the continuity to False.
        """

    @overload
    def __init__(self, eps: float, epsGeom: float, epsCoeff: float, mode: bool, modeapprox: bool, optimized: bool) -> None:
        """Creates a tool CurveAndSurface ready to run."""

    @overload
    def __init__(self, theOther: IGESToBRep_CurveAndSurface) -> None: ...

    def Init(self) -> None:
        """
        Initializes the field of the tool CurveAndSurface with
        default creating values.
        """

    def SetEpsilon(self, eps: float) -> None:
        """Changes the value of "myEps\""""

    def GetEpsilon(self) -> float:
        """Returns the value of "myEps\""""

    def SetEpsCoeff(self, eps: float) -> None:
        """Changes the value of "myEpsCoeff\""""

    def GetEpsCoeff(self) -> float:
        """Returns the value of "myEpsCoeff\""""

    def SetEpsGeom(self, eps: float) -> None:
        """Changes the value of "myEpsGeom\""""

    def GetEpsGeom(self) -> float:
        """Returns the value of "myEpsGeom\""""

    def SetMinTol(self, mintol: float) -> None:
        """Changes the value of "myMinTol\""""

    def SetMaxTol(self, maxtol: float) -> None:
        """Changes the value of "myMaxTol\""""

    def UpdateMinMaxTol(self) -> None:
        """
        Sets values of "myMinTol" and "myMaxTol" as follows
        myMaxTol = Max ("read.maxprecision.val", myEpsGeom * myUnitFactor)
        myMinTol = Precision::Confusion()
        Remark: This method is automatically invoked each time the values
        of "myEpsGeom" or "myUnitFactor" are changed
        """

    def GetMinTol(self) -> float:
        """Returns the value of "myMinTol\""""

    def GetMaxTol(self) -> float:
        """Returns the value of "myMaxTol\""""

    def SetModeApprox(self, mode: bool) -> None:
        """Changes the value of "myModeApprox\""""

    def GetModeApprox(self) -> bool:
        """Returns the value of "myModeApprox\""""

    def SetModeTransfer(self, mode: bool) -> None:
        """Changes the value of "myModeIsTopo\""""

    def GetModeTransfer(self) -> bool:
        """Returns the value of "myModeIsTopo\""""

    def SetOptimized(self, optimized: bool) -> None:
        """Changes the value of "myContIsOpti\""""

    def GetOptimized(self) -> bool:
        """Returns the value of "myContIsOpti\""""

    def GetUnitFactor(self) -> float:
        """Returns the value of " myUnitFactor\""""

    def SetSurfaceCurve(self, ival: int) -> None:
        """Changes the value of "mySurfaceCurve\""""

    def GetSurfaceCurve(self) -> int:
        """
        Returns the value of "mySurfaceCurve" 0 = value in
        file, 2 = keep 2d and compute 3d, 3 = keep 3d and
        compute 2d
        """

    def SetModel(self, model: nanoocp.IGESData.IGESData_IGESModel | None) -> None:
        """Set the value of "myModel\""""

    def GetModel(self) -> nanoocp.IGESData.IGESData_IGESModel:
        """Returns the value of "myModel\""""

    def SetContinuity(self, continuity: int) -> None:
        """
        Changes the value of "myContinuity"
        if continuity = 0 do nothing else
        if continuity = 1 try C1
        if continuity = 2 try C2
        """

    def GetContinuity(self) -> int:
        """Returns the value of "myContinuity\""""

    def SetTransferProcess(self, TP: nanoocp.Transfer.Transfer_TransientProcess | None) -> None:
        """Set the value of "myMsgReg\""""

    def GetTransferProcess(self) -> nanoocp.Transfer.Transfer_TransientProcess:
        """Returns the value of "myMsgReg\""""

    def TransferCurveAndSurface(self, start: nanoocp.IGESData.IGESData_IGESEntity | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the result of the transfert of any IGES Curve
        or Surface Entity. If the transfer has failed, this
        member return a NullEntity.
        """

    def TransferGeometry(self, start: nanoocp.IGESData.IGESData_IGESEntity | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the result of the transfert the geometry of
        any IGESEntity. If the transfer has failed, this
        member return a NullEntity.
        """

    def SendFail(self, start: nanoocp.IGESData.IGESData_IGESEntity | None, amsg: nanoocp.Message.Message_Msg) -> None:
        """Records a new Fail message"""

    def SendWarning(self, start: nanoocp.IGESData.IGESData_IGESEntity | None, amsg: nanoocp.Message.Message_Msg) -> None:
        """Records a new Warning message"""

    def SendMsg(self, start: nanoocp.IGESData.IGESData_IGESEntity | None, amsg: nanoocp.Message.Message_Msg) -> None:
        """
        Records a new Information message from the definition
        of a Msg (Original+Value)
        """

    def HasShapeResult(self, start: nanoocp.IGESData.IGESData_IGESEntity | None) -> bool:
        """
        Returns True if start was already treated and has a result in "myMap"
        else returns False.
        """

    @overload
    def GetShapeResult(self, start: nanoocp.IGESData.IGESData_IGESEntity | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the result of the transfer of the IGESEntity "start" contained
        in "myMap" . (if HasShapeResult is True).
        """

    @overload
    def GetShapeResult(self, start: nanoocp.IGESData.IGESData_IGESEntity | None, num: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the numth result of the IGESEntity start (type VertexList or
        EdgeList) in "myMap". (if NbShapeResult is not null).
        """

    def SetShapeResult(self, start: nanoocp.IGESData.IGESData_IGESEntity | None, result: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """set in "myMap" the result of the transfer of the IGESEntity "start"."""

    def NbShapeResult(self, start: nanoocp.IGESData.IGESData_IGESEntity | None) -> int:
        """
        Returns the number of shapes results contained in "myMap" for the
        IGESEntity start (type VertexList or EdgeList).
        """

    def AddShapeResult(self, start: nanoocp.IGESData.IGESData_IGESEntity | None, result: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        set in "myMap" the result of the transfer of the entity of the
        IGESEntity start (type VertexList or EdgeList).
        """

    def SetSurface(self, theSurface: nanoocp.Geom.Geom_Surface | None) -> None: ...

    def Surface(self) -> nanoocp.Geom.Geom_Surface: ...

    def GetUVResolution(self) -> float: ...

class IGESToBRep_BasicCurve(IGESToBRep_CurveAndSurface):
    """
    Provides methods to transfer basic geometric curves entities
    from IGES to CASCADE.
    These can be:
    * Circular arc
    * Conic arc
    * Spline curve
    * BSpline curve
    * Line
    * Copious data
    * Point
    * Transformation matrix
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a tool BasicCurve ready to run, with
        epsilons set to 1.E-04, TheModeTopo to True, the
        optimization of the continuity to False.
        """

    @overload
    def __init__(self, CS: IGESToBRep_CurveAndSurface) -> None:
        """
        Creates a tool BasicCurve ready to run and sets its
        fields as CS's.
        """

    @overload
    def __init__(self, eps: float, epsGeom: float, epsCoeff: float, mode: bool, modeapprox: bool, optimized: bool) -> None:
        """Creates a tool BasicCurve ready to run."""

    @overload
    def __init__(self, theOther: IGESToBRep_BasicCurve) -> None: ...

    def TransferBasicCurve(self, start: nanoocp.IGESData.IGESData_IGESEntity | None) -> nanoocp.Geom.Geom_Curve:
        """
        Transfer a IGESEntity which answer True to the
        member : IGESToBRep::IsBasicCurve(IGESEntity). If this
        Entity could not be converted, this member returns a NullEntity.
        """

    def Transfer2dBasicCurve(self, start: nanoocp.IGESData.IGESData_IGESEntity | None) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        Transfert a IGESEntity which answer True to the
        member : IGESToBRep::IsBasicCurve(IGESEntity).
        The IGESEntity must be a curve UV and its associed TRSF must
        be planar. If this Entity could not be converted, this member
        returns a NullEntity.
        """

    def TransferBSplineCurve(self, start: nanoocp.IGESGeom.IGESGeom_BSplineCurve | None) -> nanoocp.Geom.Geom_Curve: ...

    def Transfer2dBSplineCurve(self, start: nanoocp.IGESGeom.IGESGeom_BSplineCurve | None) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def TransferCircularArc(self, start: nanoocp.IGESGeom.IGESGeom_CircularArc | None) -> nanoocp.Geom.Geom_Curve: ...

    def Transfer2dCircularArc(self, start: nanoocp.IGESGeom.IGESGeom_CircularArc | None) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def TransferConicArc(self, start: nanoocp.IGESGeom.IGESGeom_ConicArc | None) -> nanoocp.Geom.Geom_Curve: ...

    def Transfer2dConicArc(self, start: nanoocp.IGESGeom.IGESGeom_ConicArc | None) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def TransferCopiousData(self, start: nanoocp.IGESGeom.IGESGeom_CopiousData | None) -> nanoocp.Geom.Geom_BSplineCurve: ...

    def Transfer2dCopiousData(self, start: nanoocp.IGESGeom.IGESGeom_CopiousData | None) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    def TransferLine(self, start: nanoocp.IGESGeom.IGESGeom_Line | None) -> nanoocp.Geom.Geom_Curve: ...

    def Transfer2dLine(self, start: nanoocp.IGESGeom.IGESGeom_Line | None) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def TransferSplineCurve(self, start: nanoocp.IGESGeom.IGESGeom_SplineCurve | None) -> nanoocp.Geom.Geom_BSplineCurve: ...

    def Transfer2dSplineCurve(self, start: nanoocp.IGESGeom.IGESGeom_SplineCurve | None) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    def TransferTransformation(self, start: nanoocp.IGESGeom.IGESGeom_TransformationMatrix | None) -> nanoocp.Geom.Geom_Transformation: ...

class IGESToBRep_BasicSurface(IGESToBRep_CurveAndSurface):
    """
    Provides methods to transfer basic geometric surface entities
    from IGES to CASCADE.
    These can be:
    * Spline surface
    * BSpline surface
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a tool BasicSurface ready to run, with
        epsilons set to 1.E-04, TheModeTopo to True, the
        optimization of the continuity to False.
        """

    @overload
    def __init__(self, CS: IGESToBRep_CurveAndSurface) -> None:
        """
        Creates a tool BasicSurface ready to run and sets its
        fields as CS's.
        """

    @overload
    def __init__(self, eps: float, epsGeom: float, epsCoeff: float, mode: bool, modeapprox: bool, optimized: bool) -> None:
        """Creates a tool BasicSurface ready to run."""

    @overload
    def __init__(self, theOther: IGESToBRep_BasicSurface) -> None: ...

    def TransferBasicSurface(self, start: nanoocp.IGESData.IGESData_IGESEntity | None) -> nanoocp.Geom.Geom_Surface:
        """Returns Surface from Geom if the last transfer has succeeded."""

    def TransferPlaneSurface(self, start: nanoocp.IGESSolid.IGESSolid_PlaneSurface | None) -> nanoocp.Geom.Geom_Plane:
        """Returns Plane from Geom if the transfer has succeeded."""

    def TransferRigthCylindricalSurface(self, start: nanoocp.IGESSolid.IGESSolid_CylindricalSurface | None) -> nanoocp.Geom.Geom_CylindricalSurface:
        """Returns CylindricalSurface from Geom if the transfer has succeeded."""

    def TransferRigthConicalSurface(self, start: nanoocp.IGESSolid.IGESSolid_ConicalSurface | None) -> nanoocp.Geom.Geom_ConicalSurface:
        """Returns ConicalSurface from Geom if the transfer has succeeded."""

    def TransferSphericalSurface(self, start: nanoocp.IGESSolid.IGESSolid_SphericalSurface | None) -> nanoocp.Geom.Geom_SphericalSurface:
        """Returns SphericalSurface from Geom if the transfer has succeeded."""

    def TransferToroidalSurface(self, start: nanoocp.IGESSolid.IGESSolid_ToroidalSurface | None) -> nanoocp.Geom.Geom_ToroidalSurface:
        """Returns SphericalSurface from Geom if the transfer has succeeded."""

    def TransferSplineSurface(self, start: nanoocp.IGESGeom.IGESGeom_SplineSurface | None) -> nanoocp.Geom.Geom_BSplineSurface:
        """Returns BSplineSurface from Geom if the transfer has succeeded."""

    def TransferBSplineSurface(self, start: nanoocp.IGESGeom.IGESGeom_BSplineSurface | None) -> nanoocp.Geom.Geom_BSplineSurface:
        """Returns BSplineSurface from Geom if the transfer has succeeded."""

class IGESToBRep_BRepEntity(IGESToBRep_CurveAndSurface):
    """
    Provides methods to transfer BRep entities
    ( VertexList 502, EdgeList 504, Loop 508,
    Face 510, Shell 514, ManifoldSolid 186)
    from IGES to CASCADE.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a tool BRepEntity ready to run, with
        epsilons set to 1.E-04, TheModeTopo to True, the
        optimization of the continuity to False.
        """

    @overload
    def __init__(self, CS: IGESToBRep_CurveAndSurface) -> None:
        """
        Creates a tool BRepEntity ready to run and sets its
        fields as CS's.
        """

    @overload
    def __init__(self, eps: float, epsGeom: float, epsCoeff: float, mode: bool, modeapprox: bool, optimized: bool) -> None:
        """Creates a tool BRepEntity ready to run."""

    @overload
    def __init__(self, theOther: IGESToBRep_BRepEntity) -> None: ...

    def TransferBRepEntity(self, start: nanoocp.IGESData.IGESData_IGESEntity | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.TopoDS.TopoDS_Shape:
        """Transfer the BRepEntity" : Face, Shell or ManifoldSolid."""

    def TransferVertex(self, start: nanoocp.IGESSolid.IGESSolid_VertexList | None, index: int) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Transfer the entity number "index" of the VertexList "start\""""

    def TransferEdge(self, start: nanoocp.IGESSolid.IGESSolid_EdgeList | None, index: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """Transfer the entity number "index" of the EdgeList "start"."""

    def TransferLoop(self, start: nanoocp.IGESSolid.IGESSolid_Loop | None, Face: nanoocp.TopoDS.TopoDS_Face, trans: nanoocp.gp.gp_Trsf2d, uFact: float) -> nanoocp.TopoDS.TopoDS_Shape:
        """Transfer the Loop Entity"""

    def TransferFace(self, start: nanoocp.IGESSolid.IGESSolid_Face | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """Transfer the Face Entity"""

    def TransferShell(self, start: nanoocp.IGESSolid.IGESSolid_Shell | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.TopoDS.TopoDS_Shape:
        """Transfer the Shell Entity"""

    def TransferManifoldSolid(self, start: nanoocp.IGESSolid.IGESSolid_ManifoldSolid | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.TopoDS.TopoDS_Shape:
        """Transfer the ManifoldSolid Entity"""

class IGESToBRep_IGESBoundary(nanoocp.Standard.Standard_Transient):
    """
    This class is intended to translate IGES boundary entity
    (142-CurveOnSurface, 141-Boundary or 508-Loop) into the wire.
    Methods Transfer are virtual and are redefined in Advanced
    Data Exchange to optimize the translation and take into
    account advanced parameters.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, CS: IGESToBRep_CurveAndSurface) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: IGESToBRep_IGESBoundary) -> None: ...

    def Init(self, CS: IGESToBRep_CurveAndSurface, entity: nanoocp.IGESData.IGESData_IGESEntity | None, face: nanoocp.TopoDS.TopoDS_Face, trans: nanoocp.gp.gp_Trsf2d, uFact: float, filepreference: int) -> None:
        """
        Inits the object with parameters common for all
        types of IGES boundaries.
        <CS>: object to be used for retrieving translation parameters
        and sending messages,
        <entity>: boundary entity to be processed,
        <face>, <trans>, <uFact>: as for IGESToBRep_TopoCurve
        <filepreference>: preferred representation (2 or 3) given
        in the IGES file
        """

    def WireData(self) -> nanoocp.ShapeExtend.ShapeExtend_WireData:
        """Returns the resulting wire"""

    def WireData3d(self) -> nanoocp.ShapeExtend.ShapeExtend_WireData:
        """
        Returns the wire from 3D curves (edges contain 3D curves
        and may contain pcurves)
        """

    def WireData2d(self) -> nanoocp.ShapeExtend.ShapeExtend_WireData:
        """
        Returns the wire from 2D curves (edges contain pcurves
        only)
        """

    @overload
    def Transfer(self, curve3d: nanoocp.IGESData.IGESData_IGESEntity | None, toreverse3d: bool, curves2d: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None, number: int) -> tuple[bool, bool, bool, bool]:
        """
        Translates 141 and 142 entities.
        Returns True if the curve has been successfully translated,
        otherwise returns False.
        <okCurve..>: flags that indicate whether corresponding
        representation has been successfully translated
        (must be set to True before first call),
        <curve3d>: model space curve for 142 and current model space
        curve for 141,
        <toreverse3d>: False for 142 and current orientation flag
        for 141,
        <curves2d>: 1 parameter space curve for 142 or list of
        them for current model space curves for 141,
        <number>: 1 for 142 and rank number of model space curve for 141.
        """

    @overload
    def Transfer(self, curve3d: nanoocp.ShapeExtend.ShapeExtend_WireData | None, curves2d: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None, toreverse2d: bool, number: int) -> tuple[bool, bool, bool, bool, nanoocp.ShapeExtend.ShapeExtend_WireData]:
        """
        Translates 508 entity.
        Returns True if the curve has been successfully translated,
        otherwise returns False.
        Input object IGESBoundary must be created and initialized
        before.
        <okCurve..>: flags that indicate whether corresponding
        representation has been successfully translated
        (must be set to True before first call),
        <curve3d>: result of translation of current edge,
        <curves2d>: list of parameter space curves for edge,
        <toreverse2d>: orientation flag of current edge in respect
        to its model space curve,
        <number>: rank number of edge,
        <lsewd>: returns the result of translation of current edge.
        """

    def Check(self, result: bool, checkclosure: bool, okCurve3d: bool, okCurve2d: bool) -> None:
        """
        Checks result of translation of IGES boundary entities
        (types 141, 142 or 508).
        Checks consistency of 2D and 3D representations and keeps
        only one if they are inconsistent.
        <result>: result of translation (returned by Transfer),
        <checkclosure>: False for 142 without parent 144 entity,
        otherwise True,
        <okCurve3d>, <okCurve2d>: those returned by Transfer.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESToBRep_Reader:
    """
    A simple way to read geometric IGES data.
    Encapsulates reading file and calling transfer tools
    """

    @overload
    def __init__(self) -> None:
        """Creates a Reader"""

    @overload
    def __init__(self, theOther: IGESToBRep_Reader) -> None: ...

    def LoadFile(self, filename: str) -> int:
        """
        Loads a Model from a file.Returns 0 if success.
        returns 1 if the file could not be opened,
        returns -1 if an error occurred while the file was being loaded.
        """

    def SetModel(self, model: nanoocp.IGESData.IGESData_IGESModel | None) -> None:
        """
        Specifies a Model to work on
        Also clears the result and Done status, sets TransientProcess
        """

    def Model(self) -> nanoocp.IGESData.IGESData_IGESModel:
        """Returns the Model to be worked on."""

    def SetTransientProcess(self, TP: nanoocp.Transfer.Transfer_TransientProcess | None) -> None:
        """
        Allows to set an already defined TransientProcess
        (to be called after LoadFile or SetModel)
        """

    def TransientProcess(self) -> nanoocp.Transfer.Transfer_TransientProcess:
        """Returns the TransientProcess"""

    def Actor(self) -> IGESToBRep_Actor:
        """Returns "theActor\""""

    def Clear(self) -> None:
        """Clears the results between two translation operations."""

    def Check(self, withprint: bool) -> bool:
        """
        Checks the IGES file that was
        loaded into memory. Displays error messages in the default
        message file if withprint is true. Returns True if no fail
        message was found and False if there was at least one fail message.
        """

    def TransferRoots(self, onlyvisible: bool = True, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Translates root entities in an
        IGES file. true is the default value and means that only
        visible root entities are translated. false
        translates all of the roots (visible and invisible).
        """

    def Transfer(self, num: int, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Transfers an Entity given its rank in the Model (Root or not)
        Returns True if it is recognized as Geom-Topol.
        (But it can have failed : see IsDone)
        """

    def IsDone(self) -> bool:
        """Returns True if the LAST Transfer/TransferRoots was a success"""

    def UsedTolerance(self) -> float:
        """
        Returns the Tolerance which has been actually used, converted
        in millimeters
        (either that from File or that from Session, according the mode)
        """

    def NbShapes(self) -> int:
        """Returns the number of shapes produced by the translation."""

    def Shape(self, num: int = 1) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the num the resulting shape in a translation operation."""

    def OneShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns all of the results in a
        single shape which is:
        - a null shape if there are no results,
        - a shape if there is one result,
        - a compound containing the resulting shapes if there are several.
        """

    @overload
    def SetShapeFixParameters(self, theParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Sets parameters for shape processing.
        @param theParameters the parameters for shape processing.
        """

    @overload
    def SetShapeFixParameters(self, theParameters: nanoocp.DE.DE_ShapeFixParameters, theAdditionalParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString] = ...) -> None:
        """
        Sets parameters for shape processing.
        Parameters from @p theParameters are copied to the internal map.
        Parameters from @p theAdditionalParameters are copied to the internal map
        if they are not present in @p theParameters.
        @param theParameters the parameters for shape processing.
        @param theAdditionalParameters the additional parameters for shape processing.
        """

    def GetShapeFixParameters(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]:
        """
        Returns parameters for shape processing that was set by SetParameters() method.
        @return the parameters for shape processing. Empty map if no parameters were set.
        """

    def SetShapeProcessFlags(self, theFlags: set[int]) -> None:
        """
        Sets flags defining operations to be performed on shapes.
        @param theFlags The flags defining operations to be performed on shapes.
        """

    def GetShapeProcessFlags(self) -> set[int]:
        """
        Returns flags defining operations to be performed on shapes.
        @return The flags defining operations to be performed on shapes.
        """

class IGESToBRep_ToolContainer(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: IGESToBRep_ToolContainer) -> None: ...

    def IGESBoundary(self) -> IGESToBRep_IGESBoundary:
        """Returns IGESToBRep_IGESBoundary"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESToBRep_TopoCurve(IGESToBRep_CurveAndSurface):
    """
    Provides methods to transfer topologic curves entities
    from IGES to CASCADE.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a tool TopoCurve ready to run, with
        epsilons set to 1.E-04, TheModeTopo to True, the
        optimization of the continuity to False.
        """

    @overload
    def __init__(self, CS: IGESToBRep_CurveAndSurface) -> None: ...

    @overload
    def __init__(self, CS: IGESToBRep_TopoCurve) -> None:
        """
        Creates a tool TopoCurve ready to run and sets its
        fields as CS's.
        """

    @overload
    def __init__(self, eps: float, epsGeom: float, epsCoeff: float, mode: bool, modeapprox: bool, optimized: bool) -> None:
        """Creates a tool TopoCurve ready to run."""

    def TransferTopoCurve(self, start: nanoocp.IGESData.IGESData_IGESEntity | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Transfer2dTopoCurve(self, start: nanoocp.IGESData.IGESData_IGESEntity | None, face: nanoocp.TopoDS.TopoDS_Face, trans: nanoocp.gp.gp_Trsf2d, uFact: float) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def TransferTopoBasicCurve(self, start: nanoocp.IGESData.IGESData_IGESEntity | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Transfer2dTopoBasicCurve(self, start: nanoocp.IGESData.IGESData_IGESEntity | None, face: nanoocp.TopoDS.TopoDS_Face, trans: nanoocp.gp.gp_Trsf2d, uFact: float) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def TransferPoint(self, start: nanoocp.IGESGeom.IGESGeom_Point | None) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def Transfer2dPoint(self, start: nanoocp.IGESGeom.IGESGeom_Point | None) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def TransferCompositeCurve(self, start: nanoocp.IGESGeom.IGESGeom_CompositeCurve | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Transfer2dCompositeCurve(self, start: nanoocp.IGESGeom.IGESGeom_CompositeCurve | None, face: nanoocp.TopoDS.TopoDS_Face, trans: nanoocp.gp.gp_Trsf2d, uFact: float) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def TransferOffsetCurve(self, start: nanoocp.IGESGeom.IGESGeom_OffsetCurve | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Transfer2dOffsetCurve(self, start: nanoocp.IGESGeom.IGESGeom_OffsetCurve | None, face: nanoocp.TopoDS.TopoDS_Face, trans: nanoocp.gp.gp_Trsf2d, uFact: float) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def TransferCurveOnSurface(self, start: nanoocp.IGESGeom.IGESGeom_CurveOnSurface | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def TransferCurveOnFace(self, face: nanoocp.TopoDS.TopoDS_Face, start: nanoocp.IGESGeom.IGESGeom_CurveOnSurface | None, trans: nanoocp.gp.gp_Trsf2d, uFact: float, IsCurv: bool) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Transfers a CurveOnSurface directly on a face to trim it.
        The CurveOnSurface have to be defined Outer or Inner.
        """

    def TransferBoundary(self, start: nanoocp.IGESGeom.IGESGeom_Boundary | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def TransferBoundaryOnFace(self, face: nanoocp.TopoDS.TopoDS_Face, start: nanoocp.IGESGeom.IGESGeom_Boundary | None, trans: nanoocp.gp.gp_Trsf2d, uFact: float) -> nanoocp.TopoDS.TopoDS_Shape:
        """Transfers a Boundary directly on a face to trim it."""

    def ApproxBSplineCurve(self, start: nanoocp.Geom.Geom_BSplineCurve | None) -> None: ...

    def NbCurves(self) -> int:
        """Returns the count of Curves in "TheCurves\""""

    def Curve(self, num: int = 1) -> nanoocp.Geom.Geom_Curve:
        """
        Returns a Curve given its rank, by default the first one
        (null Curvee if out of range) in "TheCurves\"
        """

    def Approx2dBSplineCurve(self, start: nanoocp.Geom2d.Geom2d_BSplineCurve | None) -> None: ...

    def NbCurves2d(self) -> int:
        """Returns the count of Curves in "TheCurves2d\""""

    def Curve2d(self, num: int = 1) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        Returns a Curve given its rank, by default the first one
        (null Curvee if out of range) in "TheCurves2d\"
        """

    def SetBadCase(self, value: bool) -> None:
        """Sets TheBadCase flag"""

    def BadCase(self) -> bool:
        """Returns TheBadCase flag"""

class IGESToBRep_TopoSurface(IGESToBRep_CurveAndSurface):
    """
    Provides methods to transfer topologic surfaces entities
    from IGES to CASCADE.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a tool TopoSurface ready to run, with
        epsilons set to 1.E-04, TheModeTopo to True, the
        optimization of the continuity to False.
        """

    @overload
    def __init__(self, CS: IGESToBRep_CurveAndSurface) -> None:
        """
        Creates a tool TopoSurface ready to run and sets its
        fields as CS's.
        """

    @overload
    def __init__(self, eps: float, epsGeom: float, epsCoeff: float, mode: bool, modeapprox: bool, optimized: bool) -> None:
        """Creates a tool TopoSurface ready to run."""

    @overload
    def __init__(self, theOther: IGESToBRep_TopoSurface) -> None: ...

    def TransferTopoSurface(self, start: nanoocp.IGESData.IGESData_IGESEntity | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def TransferTopoBasicSurface(self, start: nanoocp.IGESData.IGESData_IGESEntity | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def TransferRuledSurface(self, start: nanoocp.IGESGeom.IGESGeom_RuledSurface | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def TransferSurfaceOfRevolution(self, start: nanoocp.IGESGeom.IGESGeom_SurfaceOfRevolution | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def TransferTabulatedCylinder(self, start: nanoocp.IGESGeom.IGESGeom_TabulatedCylinder | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def TransferOffsetSurface(self, start: nanoocp.IGESGeom.IGESGeom_OffsetSurface | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def TransferTrimmedSurface(self, start: nanoocp.IGESGeom.IGESGeom_TrimmedSurface | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def TransferBoundedSurface(self, start: nanoocp.IGESGeom.IGESGeom_BoundedSurface | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def TransferPlane(self, start: nanoocp.IGESGeom.IGESGeom_Plane | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def TransferPerforate(self, start: nanoocp.IGESBasic.IGESBasic_SingleParent | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def ParamSurface(self, start: nanoocp.IGESData.IGESData_IGESEntity | None, trans: nanoocp.gp.gp_Trsf2d) -> tuple[nanoocp.TopoDS.TopoDS_Shape, float]: ...
