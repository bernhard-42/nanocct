"""OCCT package IGESControl (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.DE
import nanoocp.IFSelect
import nanoocp.IGESData
import nanoocp.IGESToBRep
import nanoocp.Interface
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopoDS
import nanoocp.Transfer
import nanoocp.XSControl
import nanoocp.TCollection


class IGESControl_ActorWrite(nanoocp.Transfer.Transfer_ActorOfFinderProcess):
    """Actor to write Shape to IGES"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESControl_ActorWrite) -> None: ...

    def Recognize(self, start: nanoocp.Transfer.Transfer_Finder | None) -> bool:
        """Recognizes a ShapeMapper"""

    def Transfer(self, start: nanoocp.Transfer.Transfer_Finder | None, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Transfer.Transfer_Binder:
        """
        Transfers Shape to IGES Entities

        ModeTrans may be : 0 -> groups of Faces
        or 1 -> BRep
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESControl_AlgoContainer(nanoocp.IGESToBRep.IGESToBRep_AlgoContainer):
    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: IGESControl_AlgoContainer) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESControl_Controller(nanoocp.XSControl.XSControl_Controller):
    """Controller for IGES-5.1"""

    @overload
    def __init__(self, modefnes: bool = False) -> None:
        """
        Initializes the use of IGES Norm (the first time) and returns
        a Controller for IGES-5.1
        If <modefnes> is True, sets it to internal FNES format
        """

    @overload
    def __init__(self, theOther: IGESControl_Controller) -> None: ...

    def NewModel(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        Creates a new empty Model ready to receive data of the Norm.
        It is taken from IGES Template Model
        """

    def ActorRead(self, model: nanoocp.Interface.Interface_InterfaceModel | None) -> nanoocp.Transfer.Transfer_ActorOfTransientProcess:
        """
        Returns the Actor for Read attached to the pair (norm,appli)
        It is an Actor from IGESToBRep, adapted from an IGESModel :
        Unit, tolerances
        """

    def TransferWriteShape(self, shape: nanoocp.TopoDS.TopoDS_Shape, FP: nanoocp.Transfer.Transfer_FinderProcess | None, model: nanoocp.Interface.Interface_InterfaceModel | None, modetrans: int = 0, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """
        Takes one Shape and transfers it to the InterfaceModel
        (already created by NewModel for instance)
        <modetrans> is to be interpreted by each kind of XstepAdaptor
        Returns a status : 0 OK  1 No result  2 Fail  -1 bad modeshape
        -2 bad model (requires an IGESModel)
        modeshape : 0 group of face (version < 5.1)
        1  BREP-version 5.1 of IGES
        """

    @staticmethod
    def Init() -> bool:
        """
        Standard Initialisation. It creates a Controller for IGES and
        records it to various names, available to select it later
        Returns True when done, False if could not be done
        Also, it creates and records an Adaptor for FNES
        """

    def Customise(self, WS: nanoocp.XSControl.XSControl_WorkSession | None) -> nanoocp.XSControl.XSControl_WorkSession: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESControl_IGESBoundary(nanoocp.IGESToBRep.IGESToBRep_IGESBoundary):
    """
    Translates IGES boundary entity (types 141, 142 and 508)
    in Advanced Data Exchange.
    Redefines translation and treatment methods from inherited
    open class IGESToBRep_IGESBoundary.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, CS: nanoocp.IGESToBRep.IGESToBRep_CurveAndSurface) -> None:
        """Creates an object and calls inherited constructor."""

    @overload
    def __init__(self, theOther: IGESControl_IGESBoundary) -> None: ...

    def Check(self, result: bool, checkclosure: bool, okCurve3d: bool, okCurve2d: bool) -> None:
        """
        Checks result of translation of IGES boundary entities
        (types 141, 142 or 508).
        Checks consistency of 2D and 3D representations and keeps
        only one if they are inconsistent.
        Checks the closure of resulting wire and if it is not closed,
        checks 2D and 3D representation and updates the resulting
        wire to contain only closed representation.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESControl_Reader(nanoocp.XSControl.XSControl_Reader):
    """
    Reads IGES files, checks them and translates their contents into Open CASCADE models.
    The IGES data can be that of a whole model or that of a specific list of entities in the model.
    As in XSControl_Reader, you specify the list using a selection.
    For translation of iges files it is possible to use the following sequence:
    To change parameters of translation
    class Interface_Static should be used before the beginning of translation
    (see IGES Parameters and General Parameters)
    Creation of reader
    IGESControl_Reader reader;
    To load a file in a model use method:
    reader.ReadFile("filename.igs")
    To check a loading file use method Check:
    reader.Check(failsonly); where failsonly is equal to true or
    false;
    To print the results of load:
    reader.PrintCheckLoad(failsonly,mode) where mode is equal to the value of
    enumeration IFSelect_PrintCount
    To transfer entities from a model the following methods can be used:
    for the whole model
    reader.TransferRoots(onlyvisible); where onlyvisible is equal to
    true or false;
    To transfer a list of entities:
    reader.TransferList(list);
    To transfer one entity
    reader.TransferEntity(ent) or reader.Transfer(num);
    To obtain a result the following method can be used:
    reader.IsDone()
    reader.NbShapes() and reader.Shape(num); or reader.OneShape();
    To print the results of transfer use method:
    reader.PrintTransferInfo(failwarn,mode); where printfail is equal to the
    value of enumeration IFSelect_PrintFail, mode see above.
    Gets correspondence between an IGES entity and a result shape obtained therefrom.
    reader.TransientProcess();
    TopoDS_Shape shape =
    TransferBRep::ShapeResult(reader.TransientProcess(),ent);
    """

    @overload
    def __init__(self) -> None:
        """Creates a Reader from scratch"""

    @overload
    def __init__(self, WS: nanoocp.XSControl.XSControl_WorkSession | None, scratch: bool = True) -> None:
        """Creates a Reader from an already existing Session"""

    @overload
    def __init__(self, theOther: IGESControl_Reader) -> None: ...

    def SetReadVisible(self, ReadRoot: bool) -> None:
        """
        Set the transion of ALL Roots (if theReadOnlyVisible is False)
        or of Visible Roots (if theReadOnlyVisible is True)
        """

    def GetReadVisible(self) -> bool: ...

    def IGESModel(self) -> nanoocp.IGESData.IGESData_IGESModel:
        """
        Returns the model as a IGESModel.
        It can then be consulted (header, product)
        """

    def NbRootsForTransfer(self) -> int:
        """
        Determines the list of root entities from Model which are candidate for
        a transfer to a Shape (type of entities is PRODUCT)
        <theReadOnlyVisible> is taken into account to define roots
        """

    def PrintTransferInfo(self, failwarn: nanoocp.IFSelect.IFSelect_PrintFail, mode: nanoocp.IFSelect.IFSelect_PrintCount) -> None:
        """Prints Statistics and check list for Transfer"""

class IGESControl_ToolContainer(nanoocp.IGESToBRep.IGESToBRep_ToolContainer):
    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: IGESControl_ToolContainer) -> None: ...

    def IGESBoundary(self) -> nanoocp.IGESToBRep.IGESToBRep_IGESBoundary:
        """Returns IGESControl_IGESBoundary"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESControl_Writer:
    """
    This class creates and writes
    IGES files from CAS.CADE models. An IGES file can be written to
    an existing IGES file or to a new one.
    The translation can be performed in one or several
    operations. Each translation operation
    outputs a distinct root entity in the IGES file.
    To write an IGES file it is possible to use the following sequence:
    To modify the IGES file header or to change translation
    parameters it is necessary to use class Interface_Static (see
    IGESParameters and GeneralParameters).
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a writer object with the
        default unit (millimeters) and write mode (Face).
        IGESControl_Writer (const char* const unit,
        const int modecr = 0);
        """

    @overload
    def __init__(self, theUnit: str, theModecr: int = 0) -> None:
        """
        Creates a writer with given
        values for units and for write mode.
        theUnit may be any unit that is accepted by the IGES standard.
        By default, it is the millimeter.
        theModecr defines the write mode and may be:
        - 0: Faces (default)
        - 1: BRep.
        """

    @overload
    def __init__(self, theModel: nanoocp.IGESData.IGESData_IGESModel | None, theModecr: int = 0) -> None:
        """
        Creates a writer object with the
        prepared IGES model theModel in write mode.
        theModecr defines the write mode and may be:
        - 0: Faces (default)
        - 1: BRep.
        """

    @overload
    def __init__(self, theOther: IGESControl_Writer) -> None: ...

    def Model(self) -> nanoocp.IGESData.IGESData_IGESModel:
        """Returns the IGES model to be written in output."""

    def TransferProcess(self) -> nanoocp.Transfer.Transfer_FinderProcess: ...

    def SetTransferProcess(self, TP: nanoocp.Transfer.Transfer_FinderProcess | None) -> None:
        """
        Returns/Sets the TransferProcess : it contains final results
        and if some, check messages
        """

    def AddShape(self, sh: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Translates a Shape to IGES Entities and adds them to the model
        Returns True if done, False if Shape not suitable for IGES or null
        """

    def AddGeom(self, geom: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Translates a Geometry (Surface or Curve) to IGES Entities and
        adds them to the model
        Returns True if done, False if geom is neither a Surface or
        a Curve suitable for IGES or is null
        """

    def AddEntity(self, ent: nanoocp.IGESData.IGESData_IGESEntity | None) -> bool:
        """Adds an IGES entity (and the ones it references) to the model"""

    def ComputeModel(self) -> None:
        """
        Computes the entities found in
        the model, which is ready to be written.
        This contrasts with the default computation of headers only.
        """

    @overload
    def Write(self, fnes: bool = False) -> tuple[bool, str]:
        """
        Computes then writes the model to an OStream
        Returns True when done, false in case of error
        """

    @overload
    def Write(self, file: str, fnes: bool = False) -> bool:
        """
        Prepares and writes an IGES model
        either to an OStream, S or to a file name,CString.
        Returns True if the operation was performed correctly and
        False if an error occurred (for instance,
        if the processor could not create the file).
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
