"""OCCT package BOPAlgo (toolkit TKBO)"""

from collections.abc import Sequence
import enum
from typing import overload

import nanoocp.BOPDS
import nanoocp.BOPTools
import nanoocp.BRepTools
import nanoocp.Bnd
import nanoocp.IntTools
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp


class BOPAlgo_Operation(enum.IntEnum):
    BOPAlgo_COMMON = 0

    BOPAlgo_FUSE = 1

    BOPAlgo_CUT = 2

    BOPAlgo_CUT21 = 3

    BOPAlgo_SECTION = 4

    BOPAlgo_UNKNOWN = 5

BOPAlgo_COMMON: BOPAlgo_Operation = BOPAlgo_Operation.BOPAlgo_COMMON

BOPAlgo_FUSE: BOPAlgo_Operation = BOPAlgo_Operation.BOPAlgo_FUSE

BOPAlgo_CUT: BOPAlgo_Operation = BOPAlgo_Operation.BOPAlgo_CUT

BOPAlgo_CUT21: BOPAlgo_Operation = BOPAlgo_Operation.BOPAlgo_CUT21

BOPAlgo_SECTION: BOPAlgo_Operation = BOPAlgo_Operation.BOPAlgo_SECTION

BOPAlgo_UNKNOWN: BOPAlgo_Operation = BOPAlgo_Operation.BOPAlgo_UNKNOWN

class BOPAlgo_CheckStatus(enum.IntEnum):
    BOPAlgo_CheckUnknown = 0

    BOPAlgo_BadType = 1

    BOPAlgo_SelfIntersect = 2

    BOPAlgo_TooSmallEdge = 3

    BOPAlgo_NonRecoverableFace = 4

    BOPAlgo_IncompatibilityOfVertex = 5

    BOPAlgo_IncompatibilityOfEdge = 6

    BOPAlgo_IncompatibilityOfFace = 7

    BOPAlgo_OperationAborted = 8

    BOPAlgo_GeomAbs_C0 = 9

    BOPAlgo_InvalidCurveOnSurface = 10

    BOPAlgo_NotValid = 11

BOPAlgo_CheckUnknown: BOPAlgo_CheckStatus = BOPAlgo_CheckStatus.BOPAlgo_CheckUnknown

BOPAlgo_BadType: BOPAlgo_CheckStatus = BOPAlgo_CheckStatus.BOPAlgo_BadType

BOPAlgo_SelfIntersect: BOPAlgo_CheckStatus = BOPAlgo_CheckStatus.BOPAlgo_SelfIntersect

BOPAlgo_TooSmallEdge: BOPAlgo_CheckStatus = BOPAlgo_CheckStatus.BOPAlgo_TooSmallEdge

BOPAlgo_NonRecoverableFace: BOPAlgo_CheckStatus = BOPAlgo_CheckStatus.BOPAlgo_NonRecoverableFace

BOPAlgo_IncompatibilityOfVertex: BOPAlgo_CheckStatus = ...

BOPAlgo_IncompatibilityOfEdge: BOPAlgo_CheckStatus = BOPAlgo_CheckStatus.BOPAlgo_IncompatibilityOfEdge

BOPAlgo_IncompatibilityOfFace: BOPAlgo_CheckStatus = BOPAlgo_CheckStatus.BOPAlgo_IncompatibilityOfFace

BOPAlgo_OperationAborted: BOPAlgo_CheckStatus = BOPAlgo_CheckStatus.BOPAlgo_OperationAborted

BOPAlgo_GeomAbs_C0: BOPAlgo_CheckStatus = BOPAlgo_CheckStatus.BOPAlgo_GeomAbs_C0

BOPAlgo_InvalidCurveOnSurface: BOPAlgo_CheckStatus = BOPAlgo_CheckStatus.BOPAlgo_InvalidCurveOnSurface

BOPAlgo_NotValid: BOPAlgo_CheckStatus = BOPAlgo_CheckStatus.BOPAlgo_NotValid

class BOPAlgo_GlueEnum(enum.IntEnum):
    """
    The Enumeration describes an additional option for the algorithms
    in the Boolean Component such as General Fuse, Boolean operations,
    Section, Maker Volume, Splitter and Cells Builder algorithms.

    The Gluing options have been designed to speed up the computation
    of the interference among arguments of the operations on special cases,
    in which the arguments may be overlapping but do not have real intersections
    between their sub-shapes.

    This option cannot be used on the shapes having real intersections,
    like intersection vertex between edges, or intersection vertex between
    edge and a face or intersection line between faces.

    There are two possibilities of overlapping shapes:
    1. The shapes can be partially coinciding - the faces do not have
    intersection curves, but overlapping. The faces of such arguments will
    be split during the operation;
    2. The shapes can be fully coinciding - there should be no partial
    overlapping of the faces, thus no intersection of type EDGE/FACE at all.
    In such cases the faces will not be split during the operation.

    Even though there are no real intersections on such cases without Gluing options the algorithm
    will still intersect the sub-shapes of the arguments with interfering bounding boxes.

    The performance improvement in gluing mode is achieved by excluding
    the most time consuming computations according to the given Gluing parameter:
    1. Computation of FACE/FACE intersections for partial coincidence;
    2. And computation of VERTEX/FACE, EDGE/FACE and FACE/FACE intersections for full
    coincidence.

    By setting the Gluing option for the operation user should guarantee
    that the arguments are really coinciding. The algorithms do not check this itself.
    Setting inappropriate option for the operation is likely to lead to incorrect result.

    There are following items in the enumeration:
    **BOPAlgo_GlueOff** - default value for the algorithms, Gluing is switched off;
    **BOPAlgo_GlueShift** - Glue option for shapes with partial coincidence;
    **BOPAlgo_GlueFull** - Glue option for shapes with full coincidence.
    """

    BOPAlgo_GlueOff = 0

    BOPAlgo_GlueShift = 1

    BOPAlgo_GlueFull = 2

BOPAlgo_GlueOff: BOPAlgo_GlueEnum = BOPAlgo_GlueEnum.BOPAlgo_GlueOff

BOPAlgo_GlueShift: BOPAlgo_GlueEnum = BOPAlgo_GlueEnum.BOPAlgo_GlueShift

BOPAlgo_GlueFull: BOPAlgo_GlueEnum = BOPAlgo_GlueEnum.BOPAlgo_GlueFull

class BOPAlgo_Options:
    """
    The class provides the following options for the algorithms in Boolean Component:
    - *Memory allocation tool* - tool for memory allocations;
    - *Error and warning reporting* - allows recording warnings and errors occurred
    during the operation.
    Error means that the algorithm has failed.
    - *Parallel processing mode* - provides the possibility to perform operation in parallel mode;
    - *Fuzzy tolerance* - additional tolerance for the operation to detect
    touching or coinciding cases;
    - *Using the Oriented Bounding Boxes* - Allows using the Oriented Bounding Boxes of the shapes
    for filtering the intersections.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """Constructor with allocator"""

    @overload
    def __init__(self, theOther: BOPAlgo_Options) -> None: ...

    def Allocator(self) -> nanoocp.NCollection.NCollection_BaseAllocator:
        """Returns allocator"""

    def Clear(self) -> None:
        """
        Clears all warnings and errors, and any data cached by the algorithm.
        User defined options are not cleared.
        """

    def AddError(self, theAlert: nanoocp.Message.Message_Alert | None) -> None:
        """Adds the alert as error (fail)"""

    def AddWarning(self, theAlert: nanoocp.Message.Message_Alert | None) -> None:
        """Adds the alert as warning"""

    def HasErrors(self) -> bool:
        """Returns true if algorithm has failed"""

    def HasError(self, theType: nanoocp.Standard.Standard_Type | None) -> bool:
        """Returns true if algorithm has generated error of specified type"""

    def HasWarnings(self) -> bool:
        """Returns true if algorithm has generated some warning alerts"""

    def HasWarning(self, theType: nanoocp.Standard.Standard_Type | None) -> bool:
        """Returns true if algorithm has generated warning of specified type"""

    def GetReport(self) -> nanoocp.Message.Message_Report:
        """Returns report collecting all errors and warnings"""

    def DumpErrors(self) -> str:
        """Dumps the error status into the given stream"""

    def DumpWarnings(self) -> str:
        """Dumps the warning statuses into the given stream"""

    def ClearWarnings(self) -> None:
        """Clears the warnings of the algorithm"""

    @staticmethod
    def GetParallelMode() -> bool:
        """Gets the global parallel mode"""

    @staticmethod
    def SetParallelMode(theNewMode: bool) -> None:
        """Sets the global parallel mode"""

    def SetRunParallel(self, theFlag: bool) -> None:
        """
        Set the flag of parallel processing
        if <theFlag> is true  the parallel processing is switched on
        if <theFlag> is false the parallel processing is switched off
        """

    def RunParallel(self) -> bool:
        """Returns the flag of parallel processing"""

    def SetFuzzyValue(self, theFuzz: float) -> None:
        """Sets the additional tolerance"""

    def FuzzyValue(self) -> float:
        """Returns the additional tolerance"""

    def SetUseOBB(self, theUseOBB: bool) -> None:
        """Enables/Disables the usage of OBB"""

    def UseOBB(self) -> bool:
        """Returns the flag defining usage of OBB"""

class BOPAlgo_Algo(BOPAlgo_Options):
    """
    The class provides the root interface for the algorithms in Boolean Component.
    """

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        The main method to implement the operation
        Providing the range allows to enable Progress indicator User break functionalities.
        """

class BOPAlgo_ParallelAlgo(BOPAlgo_Algo):
    """
    Additional root class to provide interface to be launched from parallel vector.
    It already has the range as a field, and has to be used with caution to create
    scope from the range only once.
    """

    def Perform(self) -> None:
        """The main method to implement the operation"""

    def SetProgressRange(self, theRange: nanoocp.Message.Message_ProgressRange) -> None:
        """Sets the range for a single run"""

class BOPAlgo_PISteps:
    """
    Class for representing the relative contribution of each step of
    the operation to the whole progress
    """

    @overload
    def __init__(self, theNbOp: int) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BOPAlgo_PISteps) -> None: ...

    def Steps(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns the steps"""

    def ChangeSteps(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """Returns modifiable steps"""

    def SetStep(self, theOperation: int, theStep: float) -> None:
        """Assign the value theStep to theOperation"""

    def GetStep(self, theOperation: int) -> float:
        """Returns the step assigned to the operation"""

class BOPAlgo_CheckResult:
    """
    contains information about faulty shapes and faulty types
    can't be processed by Boolean Operations
    """

    @overload
    def __init__(self) -> None:
        """empty constructor"""

    @overload
    def __init__(self, theOther: BOPAlgo_CheckResult) -> None: ...

    def SetShape1(self, TheShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """sets ancestor shape (object) for faulty sub-shapes"""

    def AddFaultyShape1(self, TheShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """adds faulty sub-shapes from object to a list"""

    def SetShape2(self, TheShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """sets ancestor shape (tool) for faulty sub-shapes"""

    def AddFaultyShape2(self, TheShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """adds faulty sub-shapes from tool to a list"""

    def GetShape1(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """returns ancestor shape (object) for faulties"""

    def GetShape2(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """returns ancestor shape (tool) for faulties"""

    def GetFaultyShapes1(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """returns list of faulty shapes for object"""

    def GetFaultyShapes2(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """returns list of faulty shapes for tool"""

    def SetCheckStatus(self, TheStatus: BOPAlgo_CheckStatus) -> None:
        """set status of faulty"""

    def GetCheckStatus(self) -> BOPAlgo_CheckStatus:
        """gets status of faulty"""

    def SetMaxDistance1(self, theDist: float) -> None:
        """Sets max distance for the first shape"""

    def SetMaxDistance2(self, theDist: float) -> None:
        """Sets max distance for the second shape"""

    def SetMaxParameter1(self, thePar: float) -> None:
        """Sets the parameter for the first shape"""

    def SetMaxParameter2(self, thePar: float) -> None:
        """Sets the parameter for the second shape"""

    def GetMaxDistance1(self) -> float:
        """Returns the distance for the first shape"""

    def GetMaxDistance2(self) -> float:
        """Returns the distance for the second shape"""

    def GetMaxParameter1(self) -> float:
        """Returns the parameter for the fircst shape"""

    def GetMaxParameter2(self) -> float:
        """Returns the parameter for the second shape"""

class BOPAlgo_ArgumentAnalyzer(BOPAlgo_Algo):
    """check the validity of argument(s) for Boolean Operations"""

    @overload
    def __init__(self) -> None:
        """empty constructor"""

    @overload
    def __init__(self, theOther: BOPAlgo_ArgumentAnalyzer) -> None: ...

    def SetShape1(self, TheShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """sets object shape"""

    def SetShape2(self, TheShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """sets tool shape"""

    def GetShape1(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """returns object shape;"""

    def GetShape2(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """returns tool shape"""

    def OperationType(self) -> BOPAlgo_Operation:
        """returns ref"""

    def SetOperationType(self, theValue: BOPAlgo_Operation) -> None:
        """
        Python addition: sets the value OperationType() returns by reference in C++.
        """

    def StopOnFirstFaulty(self) -> bool:
        """returns ref"""

    def SetStopOnFirstFaulty(self, theValue: bool) -> None:
        """
        Python addition: sets the value StopOnFirstFaulty() returns by reference in C++.
        """

    def ArgumentTypeMode(self) -> bool:
        """
        Returns (modifiable) mode
        that means checking types of shapes.
        """

    def SetArgumentTypeMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value ArgumentTypeMode() returns by reference in C++.
        """

    def SelfInterMode(self) -> bool:
        """
        Returns (modifiable) mode that means
        checking of self-intersection of shapes.
        """

    def SetSelfInterMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value SelfInterMode() returns by reference in C++.
        """

    def SmallEdgeMode(self) -> bool:
        """
        Returns (modifiable) mode that means
        checking of small edges.
        """

    def SetSmallEdgeMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value SmallEdgeMode() returns by reference in C++.
        """

    def RebuildFaceMode(self) -> bool:
        """
        Returns (modifiable) mode that means
        checking of possibility to split or rebuild faces.
        """

    def SetRebuildFaceMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value RebuildFaceMode() returns by reference in C++.
        """

    def TangentMode(self) -> bool:
        """
        Returns (modifiable) mode that means
        checking of tangency between subshapes.
        """

    def SetTangentMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value TangentMode() returns by reference in C++.
        """

    def MergeVertexMode(self) -> bool:
        """
        Returns (modifiable) mode that means
        checking of problem of merging vertices.
        """

    def SetMergeVertexMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value MergeVertexMode() returns by reference in C++.
        """

    def MergeEdgeMode(self) -> bool:
        """
        Returns (modifiable) mode that means
        checking of problem of merging edges.
        """

    def SetMergeEdgeMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value MergeEdgeMode() returns by reference in C++.
        """

    def ContinuityMode(self) -> bool:
        """
        Returns (modifiable) mode that means
        checking of problem of continuity of the shape.
        """

    def SetContinuityMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value ContinuityMode() returns by reference in C++.
        """

    def CurveOnSurfaceMode(self) -> bool:
        """
        Returns (modifiable) mode that means
        checking of problem of invalid curve on surface.
        """

    def SetCurveOnSurfaceMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value CurveOnSurfaceMode() returns by reference in C++.
        """

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """performs analysis"""

    def HasFaulty(self) -> bool:
        """result of test"""

    def GetCheckResult(self) -> nanoocp.NCollection.NCollection_List[nanoocp.BOPAlgo.BOPAlgo_CheckResult]:
        """returns a result of test"""

class BOPAlgo_BuilderShape(BOPAlgo_Algo):
    """
    Root class for algorithms that has shape as result.

    The class provides the History mechanism, which allows
    tracking the modification of the input shapes during
    the operation. It uses the *BRepTools_History* tool
    as a storer for history objects.
    """

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        @name Getting the result
        Returns the result of algorithm
        """

    def Modified(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        @name History methods
        Returns the list of shapes Modified from the shape theS.
        """

    def Generated(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of shapes Generated from the shape theS."""

    def IsDeleted(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Returns true if the shape theS has been deleted.
        In this case the shape will have no Modified elements,
        but can have Generated elements.
        """

    def HasModified(self) -> bool:
        """
        Returns true if any of the input shapes has been modified during operation.
        """

    def HasGenerated(self) -> bool:
        """
        Returns true if any of the input shapes has generated shapes during operation.
        """

    def HasDeleted(self) -> bool:
        """
        Returns true if any of the input shapes has been deleted during operation.
        """

    def History(self) -> nanoocp.BRepTools.BRepTools_History:
        """History Tool"""

    def SetToFillHistory(self, theHistFlag: bool) -> None:
        """
        @name Enabling/Disabling the history collection.
        Allows disabling the history collection
        """

    def HasHistory(self) -> bool:
        """Returns flag of history availability"""

class BOPAlgo_Builder(BOPAlgo_BuilderShape):
    """
    The class is a General Fuse algorithm - base algorithm for the
    algorithms in the Boolean Component. Its main purpose is to build
    the split parts of the argument shapes from which the result of
    the operations is combined.
    The result of the General Fuse algorithm itself is a compound
    containing all split parts of the arguments.

    Additionally to the options of the base classes, the algorithm has
    the following options:
    - *Safe processing mode* - allows to avoid modification of the input
    shapes during the operation (by default it is off);
    - *Gluing options* - allows to speed up the calculation of the intersections
    on the special cases, in which some sub-shapes are coinciding.
    - *Disabling the check for inverted solids* - Disables/Enables the check of the input solids
    for inverted status (holes in the space). The default value is TRUE,
    i.e. the check is performed. Setting this flag to FALSE for inverted
    solids, most likely will lead to incorrect results.

    The algorithm returns the following warnings:
    - *BOPAlgo_AlertUnableToOrientTheShape* - in case the check on the orientation of the split
    shape
    to match the orientation of the original shape has
    failed.

    The algorithm returns the following Error statuses:
    - *BOPAlgo_AlertTooFewArguments* - in case there are no enough arguments to perform the
    operation;
    - *BOPAlgo_AlertNoFiller* - in case the intersection tool has not been created;
    - *BOPAlgo_AlertIntersectionFailed* - in case the intersection of the arguments has failed;
    - *BOPAlgo_AlertBuilderFailed* - in case building splits of arguments has failed with some
    unexpected error.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_Builder) -> None: ...

    def Clear(self) -> None:
        """Clears the content of the algorithm."""

    def PPaveFiller(self) -> BOPAlgo_PaveFiller:
        """Returns the PaveFiller, algorithm for sub-shapes intersection."""

    def PDS(self) -> nanoocp.BOPDS.BOPDS_DS:
        """Returns the Data Structure, holder of intersection information."""

    def Context(self) -> nanoocp.IntTools.IntTools_Context:
        """Returns the Context, tool for cashing heavy algorithms."""

    def AddArgument(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        @name Arguments
        Adds the argument to the operation.
        """

    def SetArguments(self, theLS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Sets the list of arguments for the operation."""

    def Arguments(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of arguments."""

    def SetNonDestructive(self, theFlag: bool) -> None:
        """
        @name Options
        Sets the flag that defines the mode of treatment.
        In non-destructive mode the argument shapes are not modified. Instead
        a copy of a sub-shape is created in the result if it is needed to be updated.
        This flag is taken into account if internal PaveFiller is used only.
        In the case of calling PerformWithFiller the corresponding flag of that PaveFiller
        is in force.
        """

    def NonDestructive(self) -> bool:
        """
        Returns the flag that defines the mode of treatment.
        In non-destructive mode the argument shapes are not modified. Instead
        a copy of a sub-shape is created in the result if it is needed to be updated.
        """

    def SetGlue(self, theGlue: BOPAlgo_GlueEnum) -> None:
        """Sets the glue option for the algorithm"""

    def Glue(self) -> BOPAlgo_GlueEnum:
        """Returns the glue option of the algorithm"""

    def SetCheckInverted(self, theCheck: bool) -> None:
        """Enables/Disables the check of the input solids for inverted status"""

    def CheckInverted(self) -> bool:
        """
        Returns the flag defining whether the check for input solids on inverted status
        should be performed or not.
        """

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        @name Performing the operation
        Performs the operation.
        The intersection will be performed also.
        """

    def PerformWithFiller(self, theFiller: BOPAlgo_PaveFiller, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Performs the operation with the prepared filler.
        The intersection will not be performed in this case.
        """

    @overload
    def BuildBOP(self, theObjects: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theObjState: nanoocp.TopAbs.TopAbs_State, theTools: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theToolsState: nanoocp.TopAbs.TopAbs_State, theRange: nanoocp.Message.Message_ProgressRange, theReport: nanoocp.Message.Message_Report | None = None) -> None:
        """
        @name BOPs on open solids
        Builds the result shape according to the given states for the objects
        and tools. These states can be unambiguously converted into the Boolean operation type.
        Thus, it performs the Boolean operation on the given groups of shapes.

        The result is built basing on the result of Builder operation (GF or any other).
        The only condition for the Builder is that the splits of faces should be created
        and classified relatively solids.

        The method uses classification approach for choosing the faces which will
        participate in building the result shape:
        - All faces from each group having the given state for the opposite group
        will be taken into result.

        Such approach shows better results (in comparison with BOPAlgo_BuilderSolid approach)
        when working with open solids. However, the result may not be always
        correct on such data (at least, not as expected) as the correct classification
        of the faces relatively open solids is not always possible and may vary
        depending on the chosen classification point on the face.

        History is not created for the solids in this method.

        To avoid pollution of the report of Builder algorithm, there is a possibility to pass
        the different report to collect the alerts of the method only. But, if the new report
        is not given, the Builder report will be used.
        So, even if Builder passed without any errors, but some error has been stored into its report
        in this method, for the following calls the Builder report must be cleared.

        The method may set the following errors:
        - BOPAlgo_AlertBuilderFailed - Building operation has not been performed yet or failed;
        - BOPAlgo_AlertBOPNotSet - invalid BOP type is given (COMMON/FUSE/CUT/CUT21 are supported);
        - BOPAlgo_AlertTooFewArguments - arguments are not given;
        - BOPAlgo_AlertUnknownShape - the shape is unknown for the operation.

        Parameters:
        @param theObjects     - The group of Objects for BOP;
        @param theObjState    - State for objects faces to pass into result;
        @param theTools       - The group of Tools for BOP;
        @param theToolsState  - State for tools faces to pass into result;
        @param theReport      - The alternative report to avoid pollution of the main one.
        """

    @overload
    def BuildBOP(self, theObjects: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theTools: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theOperation: BOPAlgo_Operation, theRange: nanoocp.Message.Message_ProgressRange, theReport: nanoocp.Message.Message_Report | None = None) -> None:
        """
        Builds the result of Boolean operation of given type
        basing on the result of Builder operation (GF or any other).

        The method converts the given type of operation into the states
        for the objects and tools required for their face to pass into result
        and performs the call to the same method, but with states instead
        of operation type.

        The conversion looks as follows:
        - COMMON is built from the faces of objects located IN any of the tools
        and vice versa.
        - FUSE   is built from the faces OUT of all given shapes;
        - CUT    is built from the faces of the objects OUT of the tools and
        faces of the tools located IN solids of the objects.

        @param theObjects   - The group of Objects for BOP;
        @param theTools     - The group of Tools for BOP;
        @param theOperation - The BOP type;
        @param theRange     - The parameter to progressIndicator
        @param theReport    - The alternative report to avoid pollution of the global one.
        """

    def Images(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """
        @name Images/Origins
        Returns the map of images.
        """

    def Origins(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """Returns the map of origins."""

    def ShapesSD(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """
        Returns the map of Same Domain (SD) shapes - coinciding shapes
        from different arguments.
        """

class BOPAlgo_ToolsProvider(BOPAlgo_Builder):
    """Auxiliary class providing API to operate tool arguments."""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_ToolsProvider) -> None: ...

    def Clear(self) -> None:
        """Clears internal fields and arguments"""

    def AddTool(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Adds Tool argument of the operation"""

    def SetTools(self, theShapes: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Adds the Tool arguments of the operation"""

    def Tools(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the Tool arguments of the operation"""

class BOPAlgo_BOP(BOPAlgo_ToolsProvider):
    """
    The class represents the Building part of the Boolean Operations
    algorithm.
    The arguments of the algorithms are divided in two groups - *Objects*
    and *Tools*.
    The algorithm builds the splits of the given arguments using the intersection
    results and combines the result of Boolean Operation of given type:
    - *FUSE* - union of two groups of objects;
    - *COMMON* - intersection of two groups of objects;
    - *CUT* - subtraction of one group from the other.

    The rules for the arguments and type of the operation are the following:
    - For Boolean operation *FUSE* all arguments should have equal dimensions;
    - For Boolean operation *CUT* the minimal dimension of *Tools* should not be
    less than the maximal dimension of *Objects*;
    - For Boolean operation *COMMON* the arguments can have any dimension.

    The class is a General Fuse based algorithm. Thus, all options
    of the General Fuse algorithm such as Fuzzy mode, safe processing mode,
    parallel processing mode, gluing mode and history support are also
    available in this algorithm.

    Additionally to the Warnings of the parent class the algorithm returns
    the following warnings:
    - *BOPAlgo_AlertEmptyShape* - in case some of the input shapes are empty shapes.

    Additionally to Errors of the parent class the algorithm returns
    the following Error statuses:
    - *BOPAlgo_AlertBOPIsNotSet* - in case the type of Boolean operation is not set;
    - *BOPAlgo_AlertBOPNotAllowed* - in case the operation of given type is not allowed on
    given inputs;
    - *BOPAlgo_AlertSolidBuilderFailed* - in case the BuilderSolid algorithm failed to
    produce the Fused solid.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_BOP) -> None: ...

    def Clear(self) -> None:
        """Clears internal fields and arguments"""

    def SetOperation(self, theOperation: BOPAlgo_Operation) -> None: ...

    def Operation(self) -> BOPAlgo_Operation: ...

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

class BOPAlgo_BuilderArea(BOPAlgo_Algo):
    """
    The root class for algorithms to build
    faces/solids from set of edges/faces
    """

    def SetContext(self, theContext: nanoocp.IntTools.IntTools_Context | None) -> None:
        """Sets the context for the algorithms"""

    def Shapes(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the input shapes"""

    def SetShapes(self, theLS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Sets the shapes for building areas"""

    def Loops(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the found loops"""

    def Areas(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the found areas"""

    def SetAvoidInternalShapes(self, theAvoidInternal: bool) -> None:
        """
        Defines the preventing of addition of internal parts into result.
        The default value is FALSE, i.e. the internal parts are added into result.
        """

    def IsAvoidInternalShapes(self) -> bool:
        """Returns the AvoidInternalShapes flag"""

class BOPAlgo_BuilderFace(BOPAlgo_BuilderArea):
    """
    The algorithm to build new faces from the given faces and
    set of edges lying on this face.

    The algorithm returns the following Error statuses:
    - *BOPAlgo_AlertNullInputShapes* - in case the given face is a null shape.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_BuilderFace) -> None: ...

    def SetFace(self, theFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Sets the face generatix"""

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns the face generatix"""

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Performs the algorithm"""

    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

class BOPAlgo_BuilderSolid(BOPAlgo_BuilderArea):
    """
    Solid Builder is the algorithm for building solids from set of faces.
    The given faces should be non-intersecting, i.e. all coinciding parts
    of the faces should be shared among them.

    The algorithm performs the following steps to build the solids:
    1. Find:
    - faces orientated INTERNAL;
    - alone faces given twice with different orientation;
    2. Build all possible closed shells from the rest of the faces
    (*BOPAlgo_ShellSplitter* is used for that);
    3. Classify the obtained shells on the Holes and Growths;
    4. Build solids from the Growth shells, put Hole shells into closest Growth solids;
    5. Classify all unused faces relatively created solids and put them as internal
    shells into the closest solids;
    6. Find all unclassified faces, i.e. faces outside of all created solids,
    make internal shells from them and put these shells into a warning.

    It is possible to avoid all internal shells in the resulting solids.
    For that it is necessary to use the method SetAvoidInternalShapes(true)
    of the base class. In this case the steps 5 and 6 will not be performed at all.

    The algorithm may return the following warnings:
    - *BOPAlgo_AlertShellSplitterFailed* in case the ShellSplitter algorithm has failed;
    - *BOPAlgo_AlertSolidBuilderUnusedFaces* in case there are some faces outside of
    created solids left.

    Example of usage of the algorithm:
    ~~~~
    const NCollection_List<TopoDS_Shape>& aFaces = ...;     // Faces to build the solids
    bool isAvoidInternals = ...;      // Flag which defines whether to create the
    internal shells or not BOPAlgo_BuilderSolid aBS;                     // Solid Builder tool
    aBS.SetShapes(aFaces);                        // Set the faces
    aBS.SetAvoidInternalShapes(isAvoidInternals); // Set the AvoidInternalShapesFlag
    aBS.Perform();                                // Perform the operation
    if (!aBS.IsDone())                            // Check for the errors
    {
    // error treatment
    Standard_SStream aSStream;
    aBS.DumpErrors(aSStream);
    return;
    }
    if (aBS.HasWarnings())                        // Check for the warnings
    {
    // warnings treatment
    Standard_SStream aSStream;
    aBS.DumpWarnings(aSStream);
    }

    const NCollection_List<TopoDS_Shape>& aSolids = aBS.Areas(); // Obtaining the result solids
    ~~~~
    """

    @overload
    def __init__(self) -> None:
        """
        @name Constructors
        Empty constructor
        """

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """Constructor with allocator"""

    @overload
    def __init__(self, theOther: BOPAlgo_BuilderSolid) -> None: ...

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        @name Performing the operation
        Performs the construction of the solids from the given faces
        """

    def GetBoxesMap(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.Bnd.Bnd_Box, nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """
        @name Getting the bounding boxes of the created solids
        For classification purposes the algorithm builds the bounding boxes
        for all created solids. This method returns the data map of solid - box pairs.
        """

class BOPAlgo_SectionAttribute:
    """
    Class is a container of the flags used
    by intersection algorithm
    """

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theAproximation: bool, thePCurveOnS1: bool, thePCurveOnS2: bool) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BOPAlgo_SectionAttribute) -> None: ...

    @overload
    def Approximation(self, theApprox: bool) -> None:
        """Sets the Approximation flag"""

    @overload
    def Approximation(self) -> bool:
        """Returns the Approximation flag"""

    @overload
    def PCurveOnS1(self, thePCurveOnS1: bool) -> None:
        """Sets the PCurveOnS1 flag"""

    @overload
    def PCurveOnS1(self) -> bool:
        """Returns the PCurveOnS1 flag"""

    @overload
    def PCurveOnS2(self, thePCurveOnS2: bool) -> None:
        """Sets the PCurveOnS2 flag"""

    @overload
    def PCurveOnS2(self) -> bool:
        """Returns the PCurveOnS2 flag"""

class BOPAlgo_PaveFiller(BOPAlgo_Algo):
    """
    The class represents the Intersection phase of the
    Boolean Operations algorithm.
    It performs the pairwise intersection of the sub-shapes of
    the arguments in the following order:
    1. Vertex/Vertex;
    2. Vertex/Edge;
    3. Edge/Edge;
    4. Vertex/Face;
    5. Edge/Face;
    6. Face/Face.

    The results of intersection are stored into the Data Structure
    of the algorithm.

    Additionally to the options provided by the parent class,
    the algorithm has the following options:
    - *Section attributes* - allows to customize the intersection of the faces
    (avoid approximation or building 2d curves);
    - *Safe processing mode* - allows to avoid modification of the input
    shapes during the operation (by default it is off);
    - *Gluing options* - allows to speed up the calculation on the special
    cases, in which some sub-shapes are coincide.

    The algorithm returns the following Warning statuses:
    - *BOPAlgo_AlertSelfInterferingShape* - in case some of the argument shapes are self-interfering
    shapes;
    - *BOPAlgo_AlertTooSmallEdge* - in case some edges of the input shapes have no valid range;
    - *BOPAlgo_AlertNotSplittableEdge* - in case some edges of the input shapes has such a small
    valid range so it cannot be split;
    - *BOPAlgo_AlertBadPositioning* - in case the positioning of the input shapes leads to creation
    of small edges;
    - *BOPAlgo_AlertIntersectionOfPairOfShapesFailed* - in case intersection of some of the
    sub-shapes has failed;
    - *BOPAlgo_AlertAcquiredSelfIntersection* - in case some sub-shapes of the argument become
    connected
    through other shapes;
    - *BOPAlgo_AlertBuildingPCurveFailed* - in case building 2D curve for some of the edges
    on the faces has failed.

    The algorithm returns the following Error alerts:
    - *BOPAlgo_AlertTooFewArguments* - in case there are no enough arguments to
    perform the operation;
    - *BOPAlgo_AlertIntersectionFailed* - in case some unexpected error occurred;
    - *BOPAlgo_AlertNullInputShapes* - in case some of the arguments are null shapes.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_PaveFiller) -> None: ...

    def DS(self) -> nanoocp.BOPDS.BOPDS_DS: ...

    def PDS(self) -> nanoocp.BOPDS.BOPDS_DS: ...

    def SetArguments(self, theLS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Sets the arguments for operation"""

    def AddArgument(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Adds the argument for operation"""

    def Arguments(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of arguments"""

    def Context(self) -> nanoocp.IntTools.IntTools_Context: ...

    def SetSectionAttribute(self, theSecAttr: BOPAlgo_SectionAttribute) -> None: ...

    def SetNonDestructive(self, theFlag: bool) -> None:
        """
        Sets the flag that defines the mode of treatment.
        In non-destructive mode the argument shapes are not modified. Instead
        a copy of a sub-shape is created in the result if it is needed to be updated.
        """

    def NonDestructive(self) -> bool:
        """
        Returns the flag that defines the mode of treatment.
        In non-destructive mode the argument shapes are not modified. Instead
        a copy of a sub-shape is created in the result if it is needed to be updated.
        """

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    def SetGlue(self, theGlue: BOPAlgo_GlueEnum) -> None:
        """Sets the glue option for the algorithm"""

    def Glue(self) -> BOPAlgo_GlueEnum:
        """Returns the glue option of the algorithm"""

    def SetAvoidBuildPCurve(self, theValue: bool) -> None:
        """Sets the flag to avoid building of p-curves of edges on faces"""

    def IsAvoidBuildPCurve(self) -> bool:
        """Returns the flag to avoid building of p-curves of edges on faces"""

class BOPAlgo_CheckerSI(BOPAlgo_PaveFiller):
    """
    Checks the shape on self-interference.

    The algorithm can set the following errors:
    - *BOPAlgo_AlertMultipleArguments* - The number of the input arguments is not one;
    - *BOPALgo_ErrorIntersectionFailed* - The check has been aborted during intersection of
    sub-shapes. In case the error has occurred during intersection of sub-shapes, i.e. in
    BOPAlgo_PaveFiller::PerformInternal() method, the errors from this method directly will be
    returned.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_CheckerSI) -> None: ...

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    def SetLevelOfCheck(self, theLevel: int) -> None:
        """
        Sets the level of checking shape on self-interference.
        It defines which interferences will be checked:
        0 - only V/V;
        1 - V/V and V/E;
        2 - V/V, V/E and E/E;
        3 - V/V, V/E, E/E and V/F;
        4 - V/V, V/E, E/E, V/F and E/F;
        5 - V/V, V/E, E/E, V/F, E/F and F/F;
        6 - V/V, V/E, E/E, V/F, E/F, F/F and V/S;
        7 - V/V, V/E, E/E, V/F, E/F, F/F, V/S and E/S;
        8 - V/V, V/E, E/E, V/F, E/F, F/F, V/S, E/S and F/S;
        9 - V/V, V/E, E/E, V/F, E/F, F/F, V/S, E/S, F/S and S/S - all interferences (Default value)
        """

class BOPAlgo_MakePeriodic(BOPAlgo_Options):
    """
    BOPAlgo_MakePeriodic is the tool for making an arbitrary shape periodic
    in 3D space in specified directions.

    Periodicity of the shape means that the shape can be repeated in any
    periodic direction any number of times without creation of the new
    geometry or splits.

    The idea is to make the shape look identical on the opposite sides of the
    periodic directions, so when translating the copy of a shape on the period
    there will be no coinciding parts of different dimensions.

    If necessary the algorithm will trim the shape to fit it into the
    requested period by splitting it by the planes limiting the shape's
    requested period.

    For making the shape periodic in certain direction the algorithm performs
    the following steps:
    * Creates the copy of the shape and moves it on the period into negative
    side of the requested direction;
    * Splits the negative side of the shape by the moved copy, ensuring copying
    of the geometry from positive side to negative;
    * Creates the copy of the shape (with already split negative side) and moves
    it on the period into the positive side of the requested direction;
    * Splits the positive side of the shape by the moved copy, ensuring copying
    of the geometry from negative side to positive.

    The algorithm also associates the identical (or twin) shapes located
    on the opposite sides of the result shape.
    Using the *GetTwins()* method it is possible to get the twin shapes from
    the opposite sides.

    Algorithm also provides the methods to repeat the periodic shape in
    periodic directions. The subsequent repetitions are performed on the
    repeated shape, thus repeating the shape two times in X direction will
    create result in three shapes (original plus two copies).
    Single subsequent repetition will result already in 6 shapes.
    The repetitions can be cleared and started over.

    The algorithm supports History of shapes modifications, thus
    it is possible to track how the shape has been changed to make it periodic
    and what new shapes have been created during repetitions.

    The algorithm supports the parallel processing mode, which allows faster
    completion of the operations.

    The algorithm supports the Error/Warning system and returns the following alerts:
    - *BOPAlgo_AlertNoPeriodicityRequired* - Error alert is given if no periodicity
    has been requested in any direction;
    - *BOPAlgo_AlertUnableToTrim* - Error alert is given if the trimming of the shape
    for fitting it into requested period has failed;
    - *BOPAlgo_AlertUnableToMakeIdentical* - Error alert is given if splitting of the
    shape by its moved copies has failed;
    - *BOPAlgo_AlertUnableToRepeat* - Warning alert is given if the gluing of the repeated
    shapes has failed.

    Example of usage of the algorithm:
    ~~~~
    TopoDS_Shape aShape = ...;                 // The shape to make periodic
    bool bMakeXPeriodic = ...;     // Flag for making or not the shape periodic in X
    direction double aXPeriod = ...;              // X period for the shape bool
    isXTrimmed = ...;         // Flag defining whether it is necessary to trimming
    // the shape to fit to X period
    double aXFirst = ...;               // Start of the X period
    // (really necessary only if the trimming is
    requested)
    bool bRunParallel = ...;       // Parallel processing mode or single

    BOPAlgo_MakePeriodic aPeriodicityMaker;                   // Periodicity maker
    aPeriodicityMaker.SetShape(aShape);                       // Set the shape
    aPeriodicityMaker.MakeXPeriodic(bMakePeriodic, aXPeriod); // Making the shape periodic in X
    direction aPeriodicityMaker.SetTrimmed(isXTrimmed, aXFirst);        // Trim the shape to fit X
    period aPeriodicityMaker.SetRunParallel(bRunParallel);           // Set the parallel processing
    mode aPeriodicityMaker.Perform();                              // Performing the operation

    if (aPeriodicityMaker.HasErrors())                        // Check for the errors
    {
    // errors treatment
    Standard_SStream aSStream;
    aPeriodicityMaker.DumpErrors(aSStream);
    return;
    }
    if (aPeriodicityMaker.HasWarnings())                      // Check for the warnings
    {
    // warnings treatment
    Standard_SStream aSStream;
    aPeriodicityMaker.DumpWarnings(aSStream);
    }
    const TopoDS_Shape& aPeriodicShape = aPeriodicityMaker.Shape(); // Result periodic shape


    aPeriodicityMaker.XRepeat(2);                                    // Making repetitions
    const TopoDS_Shape& aRepeat = aPeriodicityMaker.RepeatedShape(); // Getting the repeated shape
    aPeriodicityMaker.ClearRepetitions();                            // Clearing the repetitions
    ~~~~
    """

    @overload
    def __init__(self) -> None:
        """
        @name Constructor
        Empty constructor
        """

    @overload
    def __init__(self, theOther: BOPAlgo_MakePeriodic) -> None: ...

    class PeriodicityParams:
        """
        @name Definition of the structure to keep all periodicity parameters
        Structure to keep all periodicity parameters:
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: BOPAlgo_MakePeriodic.PeriodicityParams) -> None: ...

        def Clear(self) -> None:
            """Returns all previously set parameters to default values"""

        @property
        def myPeriodic(self) -> list[bool]:
            """Array of flags defining whether the shape should be"""

        @myPeriodic.setter
        def myPeriodic(self, arg: Sequence[bool], /) -> None: ...

        @property
        def myPeriod(self) -> list[float]:
            """Array of XYZ period values. Defining the period for any"""

        @myPeriod.setter
        def myPeriod(self, arg: Sequence[float], /) -> None: ...

        @property
        def myIsTrimmed(self) -> list[bool]:
            """Array of flags defining whether the input shape has to be"""

        @myIsTrimmed.setter
        def myIsTrimmed(self, arg: Sequence[bool], /) -> None: ...

        @property
        def myPeriodFirst(self) -> list[float]:
            """Array of start parameters of the XYZ periods: required for trimming"""

        @myPeriodFirst.setter
        def myPeriodFirst(self, arg: Sequence[float], /) -> None: ...

    def SetShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        @name Setting the shape to make it periodic
        Sets the shape to make it periodic.
        @param[in] theShape  The shape to make periodic.
        """

    def SetPeriodicityParameters(self, theParams: BOPAlgo_MakePeriodic.PeriodicityParams) -> None:
        """
        @name Setters/Getters for periodicity parameters structure
        Sets the periodicity parameters.
        @param[in] theParams  Periodicity parameters
        """

    def PeriodicityParameters(self) -> BOPAlgo_MakePeriodic.PeriodicityParams: ...

    def MakePeriodic(self, theDirectionID: int, theIsPeriodic: bool, thePeriod: float = 0.0) -> None:
        """
        @name Methods for setting/getting periodicity info using ID as a direction
        Sets the flag to make the shape periodic in specified direction:
        - 0 - X direction;
        - 1 - Y direction;
        - 2 - Z direction.

        @param[in] theDirectionID  The direction's ID;
        @param[in] theIsPeriodic  Flag defining periodicity in given direction;
        @param[in] thePeriod  Required period in given direction.
        """

    def IsPeriodic(self, theDirectionID: int) -> bool:
        """
        Returns the info about Periodicity of the shape in specified direction.
        @param[in] theDirectionID  The direction's ID.
        """

    def Period(self, theDirectionID: int) -> float:
        """
        Returns the Period of the shape in specified direction.
        @param[in] theDirectionID  The direction's ID.
        """

    def MakeXPeriodic(self, theIsPeriodic: bool, thePeriod: float = 0.0) -> None:
        """
        @name Named methods for setting/getting info about shape's periodicity
        Sets the flag to make the shape periodic in X direction.
        @param[in] theIsPeriodic  Flag defining periodicity in X direction;
        @param[in] thePeriod  Required period in X direction.
        """

    def IsXPeriodic(self) -> bool:
        """Returns the info about periodicity of the shape in X direction."""

    def XPeriod(self) -> float:
        """Returns the XPeriod of the shape"""

    def MakeYPeriodic(self, theIsPeriodic: bool, thePeriod: float = 0.0) -> None:
        """
        Sets the flag to make the shape periodic in Y direction.
        @param[in] theIsPeriodic  Flag defining periodicity in Y direction;
        @param[in] thePeriod  Required period in Y direction.
        """

    def IsYPeriodic(self) -> bool:
        """Returns the info about periodicity of the shape in Y direction."""

    def YPeriod(self) -> float:
        """Returns the YPeriod of the shape."""

    def MakeZPeriodic(self, theIsPeriodic: bool, thePeriod: float = 0.0) -> None:
        """
        Sets the flag to make the shape periodic in Z direction.
        @param[in] theIsPeriodic  Flag defining periodicity in Z direction;
        @param[in] thePeriod  Required period in Z direction.
        """

    def IsZPeriodic(self) -> bool:
        """Returns the info about periodicity of the shape in Z direction."""

    def ZPeriod(self) -> float:
        """Returns the ZPeriod of the shape."""

    def SetTrimmed(self, theDirectionID: int, theIsTrimmed: bool, theFirst: float = 0.0) -> None:
        """
        @name Methods for setting/getting trimming info taking Direction ID as a parameter
        Defines whether the input shape is already trimmed in specified direction
        to fit the period in this direction.
        Direction is defined by an ID:
        - 0 - X direction;
        - 1 - Y direction;
        - 2 - Z direction.

        If the shape is not trimmed it is required to set the first parameter
        of the period in that direction.
        The algorithm will make the shape fit into the period.

        Before calling this method, the shape has to be set to be periodic in this direction.

        @param[in] theDirectionID  The direction's ID;
        @param[in] theIsTrimmed  The flag defining trimming of the shape in given direction;
        @param[in] theFirst  The first periodic parameter in the given direction.
        """

    def IsInputTrimmed(self, theDirectionID: int) -> bool:
        """
        Returns whether the input shape was trimmed in the specified direction.
        @param[in] theDirectionID  The direction's ID.
        """

    def PeriodFirst(self, theDirectionID: int) -> float:
        """
        Returns the first periodic parameter in the specified direction.
        @param[in] theDirectionID  The direction's ID.
        """

    def SetXTrimmed(self, theIsTrimmed: bool, theFirst: bool = False) -> None:
        """
        @name Named methods for setting/getting trimming info
        Defines whether the input shape is already trimmed in X direction
        to fit the X period. If the shape is not trimmed it is required
        to set the first parameter for the X period.
        The algorithm will make the shape fit into the period.

        Before calling this method, the shape has to be set to be periodic in this direction.

        @param[in] theIsTrimmed  Flag defining whether the shape is already trimmed
        in X direction to fit the X period;
        @param[in] theFirst  The first X periodic parameter.
        """

    def IsInputXTrimmed(self) -> bool:
        """Returns whether the input shape was already trimmed for X period."""

    def XPeriodFirst(self) -> float:
        """Returns the first parameter for the X period."""

    def SetYTrimmed(self, theIsTrimmed: bool, theFirst: bool = False) -> None:
        """
        Defines whether the input shape is already trimmed in Y direction
        to fit the Y period. If the shape is not trimmed it is required
        to set the first parameter for the Y period.
        The algorithm will make the shape fit into the period.

        Before calling this method, the shape has to be set to be periodic in this direction.

        @param[in] theIsTrimmed  Flag defining whether the shape is already trimmed
        in Y direction to fit the Y period;
        @param[in] theFirst  The first Y periodic parameter.
        """

    def IsInputYTrimmed(self) -> bool:
        """Returns whether the input shape was already trimmed for Y period."""

    def YPeriodFirst(self) -> float:
        """Returns the first parameter for the Y period."""

    def SetZTrimmed(self, theIsTrimmed: bool, theFirst: bool = False) -> None:
        """
        Defines whether the input shape is already trimmed in Z direction
        to fit the Z period. If the shape is not trimmed it is required
        to set the first parameter for the Z period.
        The algorithm will make the shape fit into the period.

        Before calling this method, the shape has to be set to be periodic in this direction.

        @param[in] theIsTrimmed  Flag defining whether the shape is already trimmed
        in Z direction to fit the Z period;
        @param[in] theFirst  The first Z periodic parameter.
        """

    def IsInputZTrimmed(self) -> bool:
        """Returns whether the input shape was already trimmed for Z period."""

    def ZPeriodFirst(self) -> float:
        """Returns the first parameter for the Z period."""

    def Perform(self) -> None:
        """
        @name Performing  the operation
        Makes the shape periodic in necessary directions
        """

    def RepeatShape(self, theDirectionID: int, theTimes: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        @name Using the algorithm to repeat the shape
        Performs repetition of the shape in specified direction
        required number of times.
        Negative value of times means that the repetition should
        be perform in negative direction.
        Makes the repeated shape a base for following repetitions.

        @param[in] theDirectionID  The direction's ID;
        @param[in] theTimes  Requested number of repetitions.
        """

    def XRepeat(self, theTimes: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Repeats the shape in X direction specified number of times.
        Negative value of times means that the repetition should be
        perform in negative X direction.
        Makes the repeated shape a base for following repetitions.

        @param[in] theTimes  Requested number of repetitions.
        """

    def YRepeat(self, theTimes: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Repeats the shape in Y direction specified number of times.
        Negative value of times means that the repetition should be
        perform in negative Y direction.
        Makes the repeated shape a base for following repetitions.

        @param[in] theTimes  Requested number of repetitions.
        """

    def ZRepeat(self, theTimes: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Repeats the shape in Z direction specified number of times.
        Negative value of times means that the repetition should be
        perform in negative Z direction.
        Makes the repeated shape a base for following repetitions.

        @param[in] theTimes  Requested number of repetitions.
        """

    def RepeatedShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        @name Starting the repetitions over
        Returns the repeated shape
        """

    def ClearRepetitions(self) -> None:
        """
        Clears all performed repetitions.
        The next repetition will be performed on the base shape.
        """

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        @name Obtaining the result shape
        Returns the resulting periodic shape
        """

    def GetTwins(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        @name Getting the identical shapes
        Returns the identical shapes for the given shape located
        on the opposite periodic side.
        Returns empty list in case the shape has no twin.

        @param[in] theS  Shape to get the twins for.
        """

    def History(self) -> nanoocp.BRepTools.BRepTools_History:
        """
        @name Getting the History of the algorithm
        Returns the History of the algorithm
        """

    def Clear(self) -> None:
        """
        @name Clearing the algorithm from previous runs
        Clears the algorithm from previous runs
        """

    @staticmethod
    def ToDirectionID(theDirectionID: int) -> int:
        """
        @name Conversion of the integer to ID of periodic direction
        Converts the integer to ID of periodic direction
        """

class BOPAlgo_MakeConnected(BOPAlgo_Options):
    """
    BOPAlgo_MakeConnected is the algorithm for making the touching
    shapes connected or glued, i.e. for making the coinciding geometries
    be topologically shared among the shapes.

    The input shapes should be of the same dimension, otherwise
    the gluing will not make any sense.

    After the shapes are made connected, the border elements of input shapes
    are associated with the shapes to which they belong. At that, the orientation of
    the border element in the shape is taken into account.
    The associations are made for the following types:
    - For input SOLIDS, the resulting FACES are associated with the input solids;
    - For input FACES, the resulting EDGES are associated with the input faces;
    - For input EDGES, the resulting VERTICES are associated with the input edges.

    In frames of this algorithm the input shapes are called materials,
    and the association process is called the material association.
    The material association allows finding the coinciding elements for the opposite
    input shapes. These elements will be associated to at least two materials.

    After making the shapes connected, it is possible to make the connected
    shape periodic using the *BOPAlgo_MakePeriodic* tool.
    After making the shape periodic, the material associations will be updated
    to correspond to the actual state of the result shape.
    Repetition of the periodic shape is also possible here. Material associations
    are not going to be lost.

    The algorithm supports history of shapes modification, thus it is possible
    to track the modification of the input shapes during the operations.
    Additionally to standard history methods, the algorithm provides the
    the method *GetOrigins()* which allows obtaining the input shapes from which
    the resulting shape has been created.

    The algorithm supports the parallel processing mode, which allows faster
    completion of the operations.

    The algorithm returns the following Error/Warning messages:
    - *BOPAlgo_AlertTooFewArguments* - error alert is given on the attempt to run
    the algorithm without the arguments;
    - *BOPAlgo_AlertMultiDimensionalArguments* - error alert is given on the attempt
    to run the algorithm on multi-dimensional arguments;
    - *BOPAlgo_AlertUnableToGlue* - error alert is given if the gluer algorithm
    is unable to glue the given arguments;
    - *BOPAlgo_AlertUnableToMakePeriodic* - warning alert is given if the periodicity
    maker is unable to make the connected shape periodic with given options;
    - *BOPAlgo_AlertShapeIsNotPeriodic* - warning alert is given on the attempt to
    repeat the shape before making it periodic.

    Here is the example of usage of the algorithm:
    ~~~~
    NCollection_List<TopoDS_Shape> anArguments = ...;  // Shapes to make connected
    bool bRunParallel = ...;     // Parallel processing mode

    BOPAlgo_MakeConnected aMC;               // Tool for making the shapes connected
    aMC.SetArguments(anArguments);           // Set the shapes
    aMC.SetRunParallel(bRunParallel);        // Set parallel processing mode
    aMC.Perform();                           // Perform the operation

    if (aMC.HasErrors())                     // Check for the errors
    {
    // errors treatment
    Standard_SStream aSStream;
    aMC.DumpErrors(aSStream);
    return;
    }
    if (aMC.HasWarnings())                   // Check for the warnings
    {
    // warnings treatment
    Standard_SStream aSStream;
    aMC.DumpWarnings(aSStream);
    }

    const TopoDS_Shape& aGluedShape = aMC.Shape(); // Connected shape

    // Checking material associations
    TopAbs_ShapeEnum anElemType = ...;       // Type of border element
    TopExp_Explorer anExp(anArguments.First(), anElemType);
    for (; anExp.More(); anExp.Next())
    {
    const TopoDS_Shape& anElement = anExp.Current();
    const NCollection_List<TopoDS_Shape>& aNegativeM = aMC.MaterialsOnNegativeSide(anElement);
    const NCollection_List<TopoDS_Shape>& aPositiveM = aMC.MaterialsOnPositiveSide(anElement);
    }

    // Making the connected shape periodic
    BOPAlgo_MakePeriodic::PeriodicityParams aParams = ...; // Options for periodicity of the
    connected shape aMC.MakePeriodic(aParams);

    // Shape repetition after making it periodic
    // Check if the shape has been made periodic successfully
    if (aMC.PeriodicityTool().HasErrors())
    {
    // Periodicity maker error treatment
    }

    // Shape repetition in periodic directions
    aMC.RepeatShape(0, 2);

    const TopoDS_Shape& aShape = aMC.PeriodicShape(); // Periodic and repeated shape
    ~~~~
    """

    @overload
    def __init__(self) -> None:
        """
        @name Constructor
        Empty constructor
        """

    @overload
    def __init__(self, theOther: BOPAlgo_MakeConnected) -> None: ...

    def SetArguments(self, theArgs: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        @name Setters for the shapes to make connected
        Sets the shape for making them connected.
        @param[in] theArgs  The arguments for the operation.
        """

    def AddArgument(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Adds the shape to the arguments.
        @param[in] theS  One of the argument shapes.
        """

    def Arguments(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of arguments of the operation."""

    def Perform(self) -> None:
        """
        @name Performing the operations
        Performs the operation, i.e. makes the input shapes connected.
        """

    def MakePeriodic(self, theParams: BOPAlgo_MakePeriodic.PeriodicityParams) -> None:
        """
        @name Shape periodicity & repetition
        Makes the connected shape periodic.
        Repeated calls of this method overwrite the previous calls
        working with the basis connected shape.
        @param[in] theParams  Periodic options.
        """

    def RepeatShape(self, theDirectionID: int, theTimes: int) -> None:
        """
        Performs repetition of the periodic shape in specified direction
        required number of times.
        @param[in] theDirectionID  The direction's ID (0 for X, 1 for Y, 2 for Z);
        @param[in] theTimes  Requested number of repetitions (sign of the value defines
        the side of the repetition direction (positive or negative)).
        """

    def ClearRepetitions(self) -> None:
        """
        Clears the repetitions performed on the periodic shape,
        keeping the shape periodic.
        """

    def PeriodicityTool(self) -> BOPAlgo_MakePeriodic:
        """Returns the periodicity tool."""

    def MaterialsOnPositiveSide(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        @name Material transitions
        Returns the original shapes which images contain the
        the given shape with FORWARD orientation.
        @param[in] theS  The shape for which the materials are necessary.
        """

    def MaterialsOnNegativeSide(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the original shapes which images contain the
        the given shape with REVERSED orientation.
        @param[in] theS  The shape for which the materials are necessary.
        """

    def History(self) -> nanoocp.BRepTools.BRepTools_History:
        """
        @name History methods
        Returns the history of operations
        """

    def GetModified(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes modified from the given shape.
        @param[in] theS  The shape for which the modified shapes are necessary.
        """

    def GetOrigins(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of original shapes from which the current shape has been created.
        @param[in] theS  The shape for which the origins are necessary.
        """

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        @name Getting the result shapes
        Returns the resulting connected shape
        """

    def PeriodicShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the resulting periodic & repeated shape"""

    def Clear(self) -> None:
        """
        @name Clearing the contents of the algorithm from previous runs
        Clears the contents of the algorithm.
        """

class BOPAlgo_MakerVolume(BOPAlgo_Builder):
    """
    The algorithm is to build solids from set of shapes.
    It uses the BOPAlgo_Builder algorithm to intersect the given shapes
    and build the images of faces (if needed) and BOPAlgo_BuilderSolid
    algorithm to build the solids.

    Steps of the algorithm:
    1. Collect all faces: intersect the shapes if necessary and collect
    the images of faces, otherwise just collect the faces to the
    <myFaces> list;
    All faces on this step added twice, with orientation FORWARD
    and REVERSED;

    2. Create bounding box covering all the faces from <myFaces> and
    create solid box from corner points of that bounding box
    (myBBox, mySBox). Add faces from that box to <myFaces>;

    3. Build solids from <myFaces> using BOPAlgo_BuilderSolid algorithm;

    4. Treat the result: Eliminate solid containing faces from <mySBox>;

    5. Fill internal shapes: add internal vertices and edges into
    created solids;

    6. Prepare the history.

    Fields:
    <myIntersect> - boolean flag. It defines whether intersect shapes
    from <myArguments> (if set to TRUE) or not (FALSE).
    The default value is TRUE. By setting it to FALSE
    the user should guarantee that shapes in <myArguments>
    do not interfere with each other, otherwise the result
    is unpredictable.

    <myBBox>      - bounding box, covering all faces from <myFaces>.

    <mySBox>      - Solid box created from the corner points of <myBBox>.

    <myFaces>     - the list is to keep the "final" faces, that will be
    given to the BOPAlgo_BuilderSolid algorithm.
    If the shapes have been interfered it should contain
    the images of the source shapes, otherwise its just
    the original faces.
    It also contains the faces from <mySBox>.

    Fields inherited from BOPAlgo_Builder:

    <myArguments> - list of the source shapes. The source shapes can have
    any type, but each shape must not be self-interfered.

    <myShape>     - Result shape:
    - empty compound - if no solids were created;
    - solid - if created only one solid;
    - compound of solids - if created more than one solid.

    Fields inherited from BOPAlgo_Algo:

    <myRunParallel> - Defines whether the parallel processing is
    switched on or not.
    <myReport> - Error status of the operation. Additionally to the
    errors of the parent algorithm it can have the following values:
    - *BOPAlgo_AlertSolidBuilderFailed* - BOPAlgo_BuilderSolid algorithm has failed.

    Example:

    BOPAlgo_MakerVolume aMV;
    //
    aMV.SetArguments(aLS); //source shapes
    aMV.SetRunParallel(bRunParallel); //parallel or single mode
    aMV.SetIntersect(bIntersect); //intersect or not the shapes from <aLS>
    //
    aMV.Perform(); //perform the operation
    if (aMV.HasErrors()) { //check error status
    return;
    }
    //
    const TopoDS_Shape& aResult = aMV.Shape();  //result of the operation
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: BOPAlgo_MakerVolume) -> None: ...

    def Clear(self) -> None:
        """Clears the data."""

    def SetIntersect(self, bIntersect: bool) -> None:
        """
        Sets the flag myIntersect:
        if <bIntersect> is TRUE the shapes from <myArguments> will be intersected.
        if <bIntersect> is FALSE no intersection will be done.
        """

    def IsIntersect(self) -> bool:
        """Returns the flag <myIntersect>."""

    def Box(self) -> nanoocp.TopoDS.TopoDS_Solid:
        """Returns the solid box <mySBox>."""

    def Faces(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the processed faces <myFaces>."""

    def SetAvoidInternalShapes(self, theAvoidInternal: bool) -> None:
        """
        Defines the preventing of addition of internal for solid parts into the result.
        By default the internal parts are added into result.
        """

    def IsAvoidInternalShapes(self) -> bool:
        """Returns the AvoidInternalShapes flag"""

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Performs the operation."""

class BOPAlgo_RemoveFeatures(BOPAlgo_BuilderShape):
    """
    The RemoveFeatures algorithm is intended for reconstruction of
    the shape by removal of the unwanted parts from it. These parts can
    be holes, protrusions, spikes, fillets etc.
    The shape itself is not modified, the new shape is built in
    the result.

    Currently, only the shapes of type SOLID, COMPSOLID, and
    COMPOUND of Solids are supported. And only the FACEs can be
    removed from the shape.

    On the input the algorithm accepts the shape itself and the
    faces which have to be removed. It does not matter how the faces
    are given. It could be the separate faces or the collections of faces.
    The faces should belong to the initial shape, and those that
    do not belong will be ignored.
    Before reconstructing the shape, the algorithm will sort all
    the given faces on the connected blocks (features).

    The features will be removed from the shape one by one.
    It will allow removing all possible features even if there
    were problems with the removal of some of them.

    The removed feature is filled by the extension of the faces adjacent
    to the feature. In general, the algorithm of removing of the single
    feature from the shape looks as follows:
    - Find the faces adjacent to the feature;
    - Extend the adjacent faces to cover the feature;
    - Trim the extended faces by the bounds of original face
    (except for bounds common with the feature), so it will cover
    the feature only;
    - Rebuild the solids with reconstructed adjacent faces
    avoiding the faces from the feature.

    If the removal is successful, the result is overwritten with the
    new shape and the next feature is treated. Otherwise, the warning
    will be given.

    The algorithm has the following options:
    - History support;

    and the options available from base class:
    - Error/Warning reporting system;
    - Parallel processing mode.

    Please note that the other options of the base class are not supported
    here and will have no effect.

    <b>History support</b> allows tracking modification of the input shape
    in terms of Modified, IsDeleted and Generated. The history is
    available through the methods of the history tool *BRepTools_History*,
    which can be accessed here through the method *History()*.
    By default, the history is collected, but it is possible to disable it
    using the method *SetToFillHistory(false)*;

    <b>Error/Warning reporting system</b> - allows obtaining the extended overview
    of the Errors/Warnings occurred during the operation. As soon as any error
    appears the algorithm stops working. The warnings allow continuing the job,
    informing the user that something went wrong.
    The algorithm returns the following errors/warnings:
    - *BOPAlgo_AlertTooFewArguments* - the error alert is given if the input
    shape does not contain any solids;
    - *BOPAlgo_AlertUnsupportedType* - the warning alert is given if the input
    shape contains not only solids, but also other shapes;
    - *BOPAlgo_AlertNoFacesToRemove* - the error alert is given in case
    there are no faces to remove from the shape (nothing to do);
    - *BOPAlgo_AlertUnableToRemoveTheFeature* - the warning alert is given to
    inform the user the removal of the feature is not possible. The algorithm
    will still try to remove the other features;
    - *BOPAlgo_AlertRemoveFeaturesFailed* - the error alert is given in case if
    the operation was aborted by the unknown reason.

    <b>Parallel processing mode</b> - allows running the algorithm in parallel mode
    obtaining the result faster.

    The algorithm has certain limitations:
    - Intersection of the connected faces adjacent to the feature should not be empty.
    It means, that such faces should not be tangent to each other.
    If the intersection of the adjacent faces will be empty, the algorithm will
    be unable to trim the faces correctly and, most likely, the feature will not be removed.
    - The algorithm does not process the INTERNAL parts of the solids, they are simply
    removed during reconstruction.

    Note that for successful removal of the feature, the extended faces adjacent
    to the feature should cover the feature completely, otherwise the solids will
    not be rebuild.

    Here is the example of usage of the algorithm:
    ~~~~
    TopoDS_Shape aSolid = ...;              // Input shape to remove the features from
    NCollection_List<TopoDS_Shape> aFaces = ...;      // Faces to remove from the shape
    bool bRunParallel = ...;    // Parallel processing mode
    bool isHistoryNeeded = ...; // History support

    BOPAlgo_RemoveFeatures aRF;             // Feature removal algorithm
    aRF.SetShape(aSolid);                   // Set the shape
    aRF.AddFacesToRemove(aFaces);           // Add faces to remove
    aRF.SetRunParallel(bRunParallel);       // Define the processing mode (parallel or single)
    aRF.SetToFillHistory(isHistoryNeeded);  // Define whether to track the shapes modifications
    aRF.Perform();                          // Perform the operation
    if (aRF.HasErrors())                    // Check for the errors
    {
    // error treatment
    return;
    }
    if (aRF.HasWarnings())                  // Check for the warnings
    {
    // warnings treatment
    }
    const TopoDS_Shape& aResult = aRF.Shape(); // Result shape
    ~~~~

    The algorithm preserves the type of the input shape in the result shape. Thus,
    if the input shape is a COMPSOLID, the resulting solids will also be put into a COMPSOLID.

    When all possible features are removed, the shape is simplified by
    removing extra edges and vertices, created during operation, from the result shape.
    """

    @overload
    def __init__(self) -> None:
        """
        @name Constructors
        Empty constructor
        """

    @overload
    def __init__(self, theOther: BOPAlgo_RemoveFeatures) -> None: ...

    def SetShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        @name Setting input data for the algorithm
        Sets the shape for processing.
        @param[in] theShape  The shape to remove the faces from.
        It should either be the SOLID, COMPSOLID or COMPOUND of Solids.
        """

    def InputShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the input shape"""

    def AddFaceToRemove(self, theFace: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Adds the face to remove from the input shape.
        @param[in] theFace  The shape to extract the faces for removal.
        """

    def AddFacesToRemove(self, theFaces: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Adds the faces to remove from the input shape.
        @param[in] theFaces  The list of shapes to extract the faces for removal.
        """

    def FacesToRemove(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of faces which have been requested for removal
        from the input shape.
        """

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        @name Performing the operation
        Performs the operation
        """

    def Clear(self) -> None:
        """
        @name Clearing the contents of the algorithm
        Clears the contents of the algorithm from previous run,
        allowing reusing it for following removals.
        """

class BOPAlgo_Section(BOPAlgo_Builder):
    """
    The algorithm to build a Section between the arguments.
    The Section consists of vertices and edges.
    The Section contains:
    1. new vertices that are subjects of V/V, E/E, E/F, F/F interferences
    2. vertices that are subjects of V/E, V/F interferences
    3. new edges that are subjects of F/F interferences
    4. edges that are Common Blocks
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """Constructor with allocator"""

    @overload
    def __init__(self, theOther: BOPAlgo_Section) -> None: ...

class BOPAlgo_ShellSplitter(BOPAlgo_Algo):
    """
    The class provides the splitting of the set of connected faces
    on separate loops
    """

    @overload
    def __init__(self) -> None:
        """empty constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """constructor"""

    @overload
    def __init__(self, theOther: BOPAlgo_ShellSplitter) -> None: ...

    def AddStartElement(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """adds a face <theS> to process"""

    def StartElements(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """return the faces to process"""

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """performs the algorithm"""

    def Shells(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """returns the loops"""

    @staticmethod
    def SplitBlock(theCB: nanoocp.BOPTools.BOPTools_ConnexityBlock) -> None: ...

class BOPAlgo_Tools:
    """Provides tools used in the intersection part of Boolean operations"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_Tools) -> None: ...

    @staticmethod
    def FillMap(thePB1: nanoocp.BOPDS.BOPDS_PaveBlock | None, theF: int, theMILI: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.BOPDS.BOPDS_PaveBlock, nanoocp.NCollection.NCollection_List[int]], theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @staticmethod
    def ComputeToleranceOfCB(theCB: nanoocp.BOPDS.BOPDS_CommonBlock | None, theDS: nanoocp.BOPDS.BOPDS_DS, theContext: nanoocp.IntTools.IntTools_Context | None) -> float: ...

    @staticmethod
    def EdgesToWires(theEdges: nanoocp.TopoDS.TopoDS_Shape, theWires: nanoocp.TopoDS.TopoDS_Shape, theShared: bool = False, theAngTol: float = 1e-08) -> int:
        """
        Creates planar wires from the given edges.
        The input edges are expected to be planar. And for the performance
        sake the method does not check if the edges are really planar.
        Thus, the result wires will also be not planar if the input edges are not planar.
        The edges may be not shared, but the resulting wires will be sharing the
        coinciding parts and intersecting parts.
        The output wires may be non-manifold and contain free and multi-connected vertices.
        Parameters:
        <theEdges> - input edges;
        <theWires> - output wires;
        <theShared> - boolean flag which defines whether the input edges are already
        shared or have to be intersected;
        <theAngTol> - the angular tolerance which will be used for distinguishing
        the planes in which the edges are located. Default value is
        1.e-8 which is used for intersection of planes in IntTools_FaceFace.
        Method returns the following error statuses:
        0 - in case of success (at least one wire has been built);
        1 - in case there are no edges in the given shape;
        2 - sharing of the edges has failed.
        """

    @staticmethod
    def WiresToFaces(theWires: nanoocp.TopoDS.TopoDS_Shape, theFaces: nanoocp.TopoDS.TopoDS_Shape, theAngTol: float = 1e-08) -> bool:
        """
        Creates planar faces from given planar wires.
        The method does not check if the wires are really planar.
        The input wires may be non-manifold but should be shared.
        The wires located in the same planes and included into other wires will create
        holes in the faces built from outer wires.
        The tolerance values of the input shapes may be modified during the operation
        due to projection of the edges on the planes for creation of 2D curves.
        Parameters:
        <theWires> - the given wires;
        <theFaces> - the output faces;
        <theAngTol> - the angular tolerance for distinguishing the planes in which
        the wires are located. Default value is 1.e-8 which is used
        for intersection of planes in IntTools_FaceFace.
        Method returns TRUE in case of success, i.e. at least one face has been built.
        """

    @staticmethod
    def IntersectVertices(theVertices: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, float, nanoocp.TopTools.TopTools_ShapeMapHasher], theFuzzyValue: float, theChains: nanoocp.NCollection.NCollection_List[nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]]) -> None:
        """Finds chains of intersecting vertices"""

    @staticmethod
    def ClassifyFaces(theFaces: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theSolids: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theRunParallel: bool, theInParts: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], theShapeBoxMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.Bnd.Bnd_Box, nanoocp.TopTools.TopTools_ShapeMapHasher] = ..., theSolidsIF: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher] = ..., theRange: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IntTools.IntTools_Context:
        """
        Classifies the faces <theFaces> relatively solids <theSolids>.
        The IN faces for solids are stored into output data map <theInParts>.

        The map <theSolidsIF> contains INTERNAL faces of the solids, to avoid
        their additional classification.

        Firstly, it checks the intersection of bounding boxes of the shapes.
        If the Box is not stored in the <theShapeBoxMap> map, it builds the box.
        If the bounding boxes of solid and face are interfering the classification is performed.

        It is assumed that all faces and solids are already intersected and
        do not have any geometrically coinciding parts without topological
        sharing of these parts
        """

    @staticmethod
    def FillInternals(theSolids: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theParts: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theImages: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], theContext: nanoocp.IntTools.IntTools_Context | None) -> None:
        """
        Classifies the given parts relatively the given solids and
        fills the solids with the parts classified as INTERNAL.

        @param theSolids  - The solids to put internals to
        @param theParts   - The parts to classify relatively solids
        @param theImages  - Possible images of the parts that has to be classified
        @param theContext - cached geometrical tools to speed-up classifications
        """

    @staticmethod
    def TrsfToPoint(theBox1: nanoocp.Bnd.Bnd_Box, theBox2: nanoocp.Bnd.Bnd_Box, theTrsf: nanoocp.gp.gp_Trsf, thePoint: nanoocp.gp.gp_Pnt = ..., theCriteria: float = 100000.0) -> bool:
        """
        Computes the transformation needed to move the objects
        to the given point to increase the quality of computations.
        Returns true if the objects are located far from the given point
        (relatively given criteria), false otherwise.
        @param theBox1 the AABB of the first object
        @param theBox2 the AABB of the second object
        @param theTrsf the computed transformation
        @param thePoint the Point to compute transformation to
        @param theCriteria the Criteria to check whether thranformation is required
        """

class BOPAlgo_WireEdgeSet:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_WireEdgeSet) -> None: ...

    def Clear(self) -> None: ...

    def SetFace(self, aF: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def AddStartElement(self, sS: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def StartElements(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

    def AddShape(self, sS: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Shapes(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]: ...

class BOPAlgo_WireSplitter(BOPAlgo_Algo):
    """
    The class is to build loops from the given set of edges.

    It returns the following Error statuses
    - *BOPAlgo_AlertNullInputShapes* - in case there no input edges to build the loops.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_WireSplitter) -> None: ...

    def SetWES(self, theWES: BOPAlgo_WireEdgeSet) -> None: ...

    def WES(self) -> BOPAlgo_WireEdgeSet: ...

    def SetContext(self, theContext: nanoocp.IntTools.IntTools_Context | None) -> None:
        """Sets the context for the algorithm"""

    def Context(self) -> nanoocp.IntTools.IntTools_Context:
        """Returns the context"""

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @staticmethod
    def MakeWire(theLE: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theW: nanoocp.TopoDS.TopoDS_Wire) -> None: ...

    @staticmethod
    def SplitBlock(theF: nanoocp.TopoDS.TopoDS_Face, theCB: nanoocp.BOPTools.BOPTools_ConnexityBlock, theContext: nanoocp.IntTools.IntTools_Context | None) -> None: ...

class BOPAlgo_EdgeInfo:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_EdgeInfo) -> None: ...

    def SetEdge(self, theE: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def SetPassed(self, theFlag: bool) -> None: ...

    def Passed(self) -> bool: ...

    def SetInFlag(self, theFlag: bool) -> None: ...

    def IsIn(self) -> bool: ...

    def SetAngle(self, theAngle: float) -> None: ...

    def Angle(self) -> float: ...

    def IsInside(self) -> bool: ...

    def SetIsInside(self, theIsInside: bool) -> None: ...

class BOPAlgo_CellsBuilder(BOPAlgo_Builder):
    """
    The algorithm is based on the General Fuse algorithm (GFA).
    The result of GFA is all split parts of the Arguments.

    The purpose of this algorithm is to provide the result with the content of:
    1. Cells (parts) defined by the user;
    2. Internal boundaries defined by the user.

    In other words the algorithm should provide the possibility for the user to add
    or remove any part to (from) result and remove any internal boundaries between parts.

    All the requirements of GFA for the DATA are inherited in this algorithm.
    The arguments could be of any type (dimension) and should be valid
    in terms of BRepCheck_Analyzer and BOPAlgo_ArgumentAnalyzer.

    Results:

    The result of the algorithm is compound containing selected parts of the basic types (VERTEX,
    EDGE, FACE or SOLID). The default result is empty compound. It is possible to add any split part
    to the result by using the methods AddToRessult() and AddAllToResult(). It is also possible to
    remove any part from the result by using methods RemoveFromResult() and RemoveAllFromResult().
    The method RemoveAllFromResult() is also suitable for clearing the result.

    To remove Internal boundaries it is necessary to set the same material to the
    parts between which the boundaries should be removed and call the method
    RemoveInternalBoundaries(). The material should not be equal to 0, as this is default material
    value. The boundaries between parts with this value will not be removed. One part cannot be
    added with the different materials. It is also possible to remove the boundaries during
    combining the result. To do this it is necessary to set the material for parts (not equal to 0)
    and set the flag bUpdate to TRUE. For the arguments of the types FACE or EDGE it is recommended
    to remove the boundaries in the end when the result is completely built.
    It will help to avoid self-intersections in the result.

    Note, that if the result contains the parts with same material but of different
    dimension the boundaries between such parts will not be removed.
    Currently, the removal of the internal boundaries between multi-dimensional shapes is not
    supported.

    It is possible to create typed Containers from the parts added to result by using method
    MakeContainers(). The type of the containers will depend on the type of the arguments: WIRES for
    EEDGE, SHELLS for FACES and COMPSOLIDS for SOLIDS. The result will be compound containing
    containers. Adding of the parts to such result will not update containers. The result compound
    will contain the containers and new added parts (of basic type). Removing of the parts from such
    result may affect some containers if the parts that should be removed is in container. In this
    case this container will be rebuilt without that part.

    History:

    The algorithm supports history information for basic types of the shapes - VERTEX, EDGE, FACE.
    This information available through the methods IsDeleted() and Modified().

    In DRAW Test Harness it is available through the same commands
    as for Boolean Operations (bmodified, bgenerated and bisdeleted).

    The algorithm can return the following Error Statuses:
    - Error status acquired in the General Fuse algorithm.
    The Error status can be checked with HasErrors() method.
    If the Error status is not equal to zero, the result cannot be trustworthy.

    The algorithm can set the following Warning Statuses:
    - Warning status acquired in the General Fuse algorithm;
    - BOPAlgo_AlertRemovalOfIBForMDimShapes
    - BOPAlgo_AlertRemovalOfIBForFacesFailed
    - BOPAlgo_AlertRemovalOfIBForEdgesFailed
    - BOPAlgo_AlertRemovalOfIBForSolidsFailed

    The Warning status can be checked with HasWarnings() method or printed with the DumpWarnings()
    method. If warnings are recorded, the result may be not as expected.

    Examples:

    1. API
    @code
    BOPAlgo_CellsBuilder aCBuilder;
    NCollection_List<TopoDS_Shape> aLS = ...; // arguments
    // parallel or single mode (the default value is FALSE)
    bool toRunParallel = false;
    // fuzzy option (default value is 0)
    double aTol = 0.0;
    //
    aCBuilder.SetArguments (aLS);
    aCBuilder.SetRunParallel (toRunParallel);
    aCBuilder.SetFuzzyValue (aTol);
    //
    aCBuilder.Perform();
    if (aCBuilder.HasErrors()) // check error status
    {
    return;
    }
    // empty compound, as nothing has been added yet
    const TopoDS_Shape& aRes = aCBuilder.Shape();
    // all split parts
    const TopoDS_Shape& aRes = aCBuilder.GetAllParts();
    //
    NCollection_List<TopoDS_Shape> aLSToTake  = ...; // parts of these arguments will be taken into
    result NCollection_List<TopoDS_Shape> aLSToAvoid = ...; // parts of these arguments will not be
    taken into result
    //
    // defines the material common for the cells,
    // i.e. the boundaries between cells with the same material will be removed.
    // By default it is set to 0.
    // Thus, to remove some boundary the value of this variable should not be equal to 0.
    int iMaterial = ...;
    // defines whether to update the result right now or not
    bool toUpdate = ...;
    // adding to result
    aCBuilder.AddToResult (aLSToTake, aLSToAvoid, iMaterial, toUpdate);
    aR = aCBuilder.Shape(); // the result
    // removing of the boundaries (should be called only if toUpdate is false)
    aCBuilder.RemoveInternalBoundaries();
    //
    // removing from result
    aCBuilder.AddAllToResult();
    aCBuilder.RemoveFromResult (aLSToTake, aLSToAvoid);
    aR = aCBuilder.Shape(); // the result
    @endcode

    2. DRAW Test Harness
    @code
    psphere s1 15
    psphere s2 15
    psphere s3 15
    ttranslate s1 0 0 10
    ttranslate s2 20 0 10
    ttranslate s3 10 0 0
    # adding arguments
    bclearobjects; bcleartools
    baddobjects s1 s2 s3
    # intersection
    bfillds
    # rx will contain all split parts
    bcbuild rx
    # add to result the part that is common for all three spheres
    bcadd res s1 1 s2 1 s3 1 -m 1
    # add to result the part that is common only for first and third spheres
    bcadd res s1 1 s2 0 s3 1 -m 1
    # remove internal boundaries
    bcremoveint res
    @endcode
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_CellsBuilder) -> None: ...

    def Clear(self) -> None:
        """Redefined method Clear - clears the contents."""

    def AddToResult(self, theLSToTake: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theLSToAvoid: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theMaterial: int = 0, theUpdate: bool = False) -> None:
        """
        Adding the parts to result.
        The parts are defined by two lists of shapes:
        <theLSToTake> defines the arguments which parts should be taken into result;
        <theLSToAvoid> defines the arguments which parts should not be taken into result;
        To be taken into result the part must be IN for all shapes from the list
        <theLSToTake> and must be OUT of all shapes from the list <theLSToAvoid>.

        To remove internal boundaries between any cells in the result
        <theMaterial> variable should be used. The boundaries between
        cells with the same material will be removed. Default value is 0.
        Thus, to remove any boundary the value of this variable should not be equal to 0.
        <theUpdate> parameter defines whether to remove boundaries now or not.
        """

    def AddAllToResult(self, theMaterial: int = 0, theUpdate: bool = False) -> None:
        """
        Add all split parts to result.
        <theMaterial> defines the removal of internal boundaries;
        <theUpdate> parameter defines whether to remove boundaries now or not.
        """

    def RemoveFromResult(self, theLSToTake: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], theLSToAvoid: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Removing the parts from result.
        The parts are defined by two lists of shapes:
        <theLSToTake> defines the arguments which parts should be removed from result;
        <theLSToAvoid> defines the arguments which parts should not be removed from result.
        To be removed from the result the part must be IN for all shapes from the list
        <theLSToTake> and must be OUT of all shapes from the list <theLSToAvoid>.
        """

    def RemoveAllFromResult(self) -> None:
        """Remove all parts from result."""

    def RemoveInternalBoundaries(self) -> None:
        """
        Removes internal boundaries between cells with the same material.
        If the result contains the cells with same material but of different dimension
        the removal of internal boundaries between these cells will not be performed.
        In case of some errors during the removal the method will set the appropriate warning
        status - use GetReport() to access them.
        """

    def GetAllParts(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Get all split parts."""

    def MakeContainers(self) -> None:
        """Makes the Containers of proper type from the parts added to result."""

class BOPAlgo_Splitter(BOPAlgo_ToolsProvider):
    """
    The **Splitter algorithm** is the algorithm for splitting a group of
    arbitrary shapes by the other group of arbitrary shapes.
    The arguments of the operation are divided on two groups:
    *Objects* - shapes that will be split;
    *Tools*   - shapes by which the *Objects* will be split.
    The result of the operation contains only the split parts
    of the shapes from the group of *Objects*.
    The split parts of the shapes from the group of *Tools* are excluded
    from the result.
    The shapes can be split by the other shapes from the same group
    (in case these shapes are interfering).

    The class is a General Fuse based algorithm. Thus, all options
    of the General Fuse algorithm such as Fuzzy mode, safe processing mode,
    parallel processing mode, gluing mode and history support are also
    available in this algorithm.
    There is no requirement on the existence of the *Tools* shapes.
    And if there are no *Tools* shapes, the result of the splitting
    operation will be equivalent to the General Fuse result.

    The implementation of the algorithm is minimal - only the methods
    CheckData() and Perform() have been overridden.
    The method BOPAlgo_Builder::BuildResult(), which adds the split parts of the arguments
    into result, does not have to be overridden, because its native implementation
    performs the necessary actions for the Splitter algorithm - it adds
    the split parts of only Objects into result, avoiding the split parts of Tools.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theAllocator: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_Splitter) -> None: ...

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Performs the operation"""

class BOPAlgo_AlertUserBreak(nanoocp.Message.Message_Alert):
    """Boolean operation was stopped by user"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_AlertUserBreak) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertBOPNotAllowed(nanoocp.Message.Message_Alert):
    """Boolean operation of given type is not allowed on the given inputs"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_AlertBOPNotAllowed) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertBOPNotSet(nanoocp.Message.Message_Alert):
    """The type of Boolean Operation is not set"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_AlertBOPNotSet) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertBuilderFailed(nanoocp.Message.Message_Alert):
    """Building of the result shape has failed"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_AlertBuilderFailed) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertIntersectionFailed(nanoocp.Message.Message_Alert):
    """The intersection of the arguments has failed"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_AlertIntersectionFailed) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertMultipleArguments(nanoocp.Message.Message_Alert):
    """More than one argument is provided"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_AlertMultipleArguments) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertNoFiller(nanoocp.Message.Message_Alert):
    """The Pave Filler (the intersection tool) has not been created"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_AlertNoFiller) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertNullInputShapes(nanoocp.Message.Message_Alert):
    """Null input shapes"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_AlertNullInputShapes) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertPostTreatFF(nanoocp.Message.Message_Alert):
    """Cannot connect face intersection curves"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_AlertPostTreatFF) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertSolidBuilderFailed(nanoocp.Message.Message_Alert):
    """The BuilderSolid algorithm has failed"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_AlertSolidBuilderFailed) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertTooFewArguments(nanoocp.Message.Message_Alert):
    """There are no enough arguments to perform the operation"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_AlertTooFewArguments) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertBadPositioning(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """
    The positioning of the shapes leads to creation of the small edges without valid range
    """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        The positioning of the shapes leads to creation of the small edges without valid range
        """

    @overload
    def __init__(self, theOther: BOPAlgo_AlertBadPositioning) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertEmptyShape(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Some of the arguments are empty shapes"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Some of the arguments are empty shapes"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertEmptyShape) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertNotSplittableEdge(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """
    Some edges are very small and have such a small valid range, that they cannot be split
    """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Some edges are very small and have such a small valid range, that they cannot be split
        """

    @overload
    def __init__(self, theOther: BOPAlgo_AlertNotSplittableEdge) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertRemovalOfIBForEdgesFailed(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Removal of internal boundaries among Edges has failed"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Removal of internal boundaries among Edges has failed"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertRemovalOfIBForEdgesFailed) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertRemovalOfIBForFacesFailed(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Removal of internal boundaries among Faces has failed"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Removal of internal boundaries among Faces has failed"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertRemovalOfIBForFacesFailed) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertRemovalOfIBForMDimShapes(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """
    Removal of internal boundaries among the multi-dimensional shapes is not supported yet
    """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Removal of internal boundaries among the multi-dimensional shapes is not supported yet
        """

    @overload
    def __init__(self, theOther: BOPAlgo_AlertRemovalOfIBForMDimShapes) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertRemovalOfIBForSolidsFailed(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Removal of internal boundaries among Solids has failed"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Removal of internal boundaries among Solids has failed"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertRemovalOfIBForSolidsFailed) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertSelfInterferingShape(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Some of the arguments are self-interfering shapes"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Some of the arguments are self-interfering shapes"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertSelfInterferingShape) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertShellSplitterFailed(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """
    The positioning of the shapes leads to creation of the small edges without valid range
    """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        The positioning of the shapes leads to creation of the small edges without valid range
        """

    @overload
    def __init__(self, theOther: BOPAlgo_AlertShellSplitterFailed) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertTooSmallEdge(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Some edges are too small and have no valid range"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Some edges are too small and have no valid range"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertTooSmallEdge) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertIntersectionOfPairOfShapesFailed(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Intersection of pair of shapes has failed"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Intersection of pair of shapes has failed"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertIntersectionOfPairOfShapesFailed) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertBuildingPCurveFailed(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Building 2D curve of edge on face has failed"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Building 2D curve of edge on face has failed"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertBuildingPCurveFailed) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertAcquiredSelfIntersection(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """
    Some sub-shapes of some of the argument become connected through
    other shapes and the argument became self-interfered
    """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Some sub-shapes of some of the argument become connected through
        other shapes and the argument became self-interfered
        """

    @overload
    def __init__(self, theOther: BOPAlgo_AlertAcquiredSelfIntersection) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertUnsupportedType(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Unsupported type of input shape"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Unsupported type of input shape"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertUnsupportedType) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertNoFacesToRemove(nanoocp.Message.Message_Alert):
    """No faces have been found for removal"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_AlertNoFacesToRemove) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertUnableToRemoveTheFeature(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Unable to remove the feature"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Unable to remove the feature"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertUnableToRemoveTheFeature) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertRemoveFeaturesFailed(nanoocp.Message.Message_Alert):
    """The Feature Removal algorithm has failed"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_AlertRemoveFeaturesFailed) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertSolidBuilderUnusedFaces(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """
    Some of the faces passed to the Solid Builder algorithm have not been classified
    and not used for solids creation
    """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Some of the faces passed to the Solid Builder algorithm have not been classified
        and not used for solids creation
        """

    @overload
    def __init__(self, theOther: BOPAlgo_AlertSolidBuilderUnusedFaces) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertFaceBuilderUnusedEdges(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """
    Some of the edges passed to the Face Builder algorithm have not been classified
    and not used for faces creation
    """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Some of the edges passed to the Face Builder algorithm have not been classified
        and not used for faces creation
        """

    @overload
    def __init__(self, theOther: BOPAlgo_AlertFaceBuilderUnusedEdges) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertUnableToOrientTheShape(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Unable to orient the shape correctly"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Unable to orient the shape correctly"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertUnableToOrientTheShape) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertUnknownShape(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Shape is unknown for operation"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Shape is unknown for operation"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertUnknownShape) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertNoPeriodicityRequired(nanoocp.Message.Message_Alert):
    """No periodicity has been requested for the shape"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_AlertNoPeriodicityRequired) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertUnableToTrim(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Unable to trim the shape for making it periodic (BOP Common fails)"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Unable to trim the shape for making it periodic (BOP Common fails)"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertUnableToTrim) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertUnableToMakeIdentical(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """
    Unable to make the shape to look identical on opposite sides (Splitter fails)
    """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Unable to make the shape to look identical on opposite sides (Splitter fails)
        """

    @overload
    def __init__(self, theOther: BOPAlgo_AlertUnableToMakeIdentical) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertUnableToRepeat(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Unable to repeat the shape (Gluer fails)"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Unable to repeat the shape (Gluer fails)"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertUnableToRepeat) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertMultiDimensionalArguments(nanoocp.Message.Message_Alert):
    """Multi-dimensional arguments"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BOPAlgo_AlertMultiDimensionalArguments) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertUnableToMakePeriodic(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Unable to make the shape periodic"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Unable to make the shape periodic"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertUnableToMakePeriodic) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertUnableToGlue(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Unable to glue the shapes"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Unable to glue the shapes"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertUnableToGlue) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertShapeIsNotPeriodic(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """The shape is not periodic"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """The shape is not periodic"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertShapeIsNotPeriodic) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BOPAlgo_AlertUnableToMakeClosedEdgeOnFace(nanoocp.TopoDS.TopoDS_AlertWithShape):
    """Unable to make closed edge on face (to make a seam)"""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Unable to make closed edge on face (to make a seam)"""

    @overload
    def __init__(self, theOther: BOPAlgo_AlertUnableToMakeClosedEdgeOnFace) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.BOPAlgo
import nanoocp.TopTools
BOPAlgo_ListOfCheckResult = nanoocp.NCollection.NCollection_List[nanoocp.BOPAlgo.BOPAlgo_CheckResult]
