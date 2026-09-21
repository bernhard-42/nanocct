"""OCCT package BRepAlgoAPI (toolkit TKBO)"""

from typing import overload

import nanoocp.BOPAlgo
import nanoocp.BRepBuilderAPI
import nanoocp.BRepTools
import nanoocp.Geom
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopoDS
import nanoocp.gp


class BRepAlgoAPI_Algo(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """Provides the root interface for the API algorithms"""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns a shape built by the shape construction algorithm.
        Does not check if the shape is built.
        """

    def Clear(self) -> None:
        """
        Clears all warnings and errors, and any data cached by the algorithm.
        User defined options are not cleared.
        """

    def ClearWarnings(self) -> None:
        """Clears the warnings of the algorithm"""

    def DumpErrors(self) -> object:
        """Dumps the error status into the given stream"""

    def DumpWarnings(self) -> object:
        """Dumps the warning statuses into the given stream"""

    def FuzzyValue(self) -> float:
        """Returns the additional tolerance"""

    def GetReport(self) -> nanoocp.Message.Message_Report:
        """Returns report collecting all errors and warnings"""

    def HasError(self, theType: nanoocp.Standard.Standard_Type | None) -> bool:
        """Returns true if algorithm has generated error of specified type"""

    def HasErrors(self) -> bool:
        """Returns true if algorithm has failed"""

    def HasWarning(self, theType: nanoocp.Standard.Standard_Type | None) -> bool:
        """Returns true if algorithm has generated warning of specified type"""

    def HasWarnings(self) -> bool:
        """Returns true if algorithm has generated some warning alerts"""

    def RunParallel(self) -> bool:
        """Returns the flag of parallel processing"""

    def SetFuzzyValue(self, theFuzz: float) -> None:
        """Sets the additional tolerance"""

    def SetRunParallel(self, theFlag: bool) -> None:
        """
        Set the flag of parallel processing
        if <theFlag> is true  the parallel processing is switched on
        if <theFlag> is false the parallel processing is switched off
        """

    def SetUseOBB(self, theUseOBB: bool) -> None:
        """Enables/Disables the usage of OBB"""

class BRepAlgoAPI_BuilderAlgo(BRepAlgoAPI_Algo):
    """
    The class contains API level of the General Fuse algorithm.

    Additionally to the options defined in the base class, the algorithm has
    the following options:
    - *Safe processing mode* - allows to avoid modification of the input
    shapes during the operation (by default it is off);
    - *Gluing options* - allows to speed up the calculation of the intersections
    on the special cases, in which some sub-shapes are coinciding.
    - *Disabling the check for inverted solids* - Disables/Enables the check of the input solids
    for inverted status (holes in the space). The default value is TRUE,
    i.e. the check is performed. Setting this flag to FALSE for inverted
    solids, most likely will lead to incorrect results.
    - *Disabling history collection* - allows disabling the collection of the history
    of shapes modifications during the operation.

    It returns the following Error statuses:
    - 0 - in case of success;
    - *BOPAlgo_AlertTooFewArguments* - in case there are no enough arguments to perform the
    operation;
    - *BOPAlgo_AlertIntersectionFailed* - in case the intersection of the arguments has failed;
    - *BOPAlgo_AlertBuilderFailed* - in case building of the result shape has failed.

    Warnings statuses from underlying DS Filler and Builder algorithms
    are collected in the report.

    The class provides possibility to simplify the resulting shape by unification
    of the tangential edges and faces. It is performed by the method *SimplifyResult*.
    See description of this method for more details.
    """

    @overload
    def __init__(self) -> None:
        """
        @name Constructors
        Empty constructor
        """

    @overload
    def __init__(self, thePF: nanoocp.BOPAlgo.BOPAlgo_PaveFiller) -> None:
        """Constructor with prepared Filler object"""

    def SetArguments(self, theLS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        @name Setting/Getting data for the algorithm
        Sets the arguments
        """

    def Arguments(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Gets the arguments"""

    def SetNonDestructive(self, theFlag: bool) -> None:
        """
        @name Setting options
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

    def SetGlue(self, theGlue: nanoocp.BOPAlgo.BOPAlgo_GlueEnum) -> None:
        """
        Sets the glue option for the algorithm,
        which allows increasing performance of the intersection
        of the input shapes.
        """

    def Glue(self) -> nanoocp.BOPAlgo.BOPAlgo_GlueEnum:
        """Returns the glue option of the algorithm"""

    def SetCheckInverted(self, theCheck: bool) -> None:
        """Enables/Disables the check of the input solids for inverted status"""

    def CheckInverted(self) -> bool:
        """
        Returns the flag defining whether the check for input solids on inverted status
        should be performed or not.
        """

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        @name Performing the operation
        Performs the algorithm
        """

    def SimplifyResult(self, theUnifyEdges: bool = True, theUnifyFaces: bool = True, theAngularTol: float = 1e-12) -> None:
        """
        @name Result simplification
        Simplification of the result shape is performed by the means of
        *ShapeUpgrade_UnifySameDomain* algorithm. The result of the operation will
        be overwritten with the simplified result.

        The simplification is performed without creation of the Internal shapes,
        i.e. shapes connections will never be broken.

        Simplification is performed on the whole result shape. Thus, if the input
        shapes contained connected tangent edges or faces unmodified during the operation
        they will also be unified.

        After simplification, the History of result simplification is merged into the main
        history of operation. So, it is taken into account when asking for Modified,
        Generated and Deleted shapes.

        Some options of the main operation are passed into the Unifier:
        - Fuzzy tolerance of the operation is given to the Unifier as the linear tolerance.
        - Non destructive mode here controls the safe input mode in Unifier.

        @param theUnifyEdges Controls the edges unification. TRUE by default.
        @param theUnifyFaces Controls the faces unification. TRUE by default.
        @param theAngularTol Angular criteria for tangency of edges and faces.
        Precision::Angular() by default.
        """

    def Modified(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        @name History support
        Returns the shapes modified from the shape <theS>.
        If any, the list will contain only those splits of the
        given shape, contained in the result.
        """

    def Generated(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes generated from the shape <theS>.
        In frames of Boolean Operations algorithms only Edges and Faces
        could have Generated elements, as only they produce new elements
        during intersection:
        - Edges can generate new vertices;
        - Faces can generate new edges and vertices.
        """

    def IsDeleted(self, aS: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Checks if the shape <theS> has been completely removed from the result,
        i.e. the result does not contain the shape itself and any of its splits.
        Returns TRUE if the shape has been deleted.
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
        Normally, General Fuse operation should not have Deleted elements,
        but all derived operation can have.
        """

    def SetToFillHistory(self, theHistFlag: bool) -> None:
        """
        @name Enabling/Disabling the history collection.
        Allows disabling the history collection
        """

    def HasHistory(self) -> bool:
        """Returns flag of history availability"""

    def SectionEdges(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        @name Getting the section edges
        Returns a list of section edges.
        The edges represent the result of intersection between arguments of operation.
        """

    def History(self) -> nanoocp.BRepTools.BRepTools_History:
        """History tool"""

class BRepAlgoAPI_BooleanOperation(BRepAlgoAPI_BuilderAlgo):
    """
    The root API class for performing Boolean Operations on arbitrary shapes.

    The arguments of the operation are divided in two groups - *Objects* and *Tools*.
    Each group can contain any number of shapes, but each shape should be valid
    in terms of *BRepCheck_Analyzer* and *BOPAlgo_ArgumentAnalyzer*.
    The algorithm builds the splits of the given arguments using the intersection
    results and combines the result of Boolean Operation of given type:
    - *FUSE* - union of two groups of objects;
    - *COMMON* - intersection of two groups of objects;
    - *CUT* - subtraction of one group from the other;
    - *SECTION* - section edges and vertices of all arguments;

    The rules for the arguments and type of the operation are the following:
    - For Boolean operation *FUSE* all arguments should have equal dimensions;
    - For Boolean operation *CUT* the minimal dimension of *Tools* should not be
    less than the maximal dimension of *Objects*;
    - For Boolean operation *COMMON* the arguments can have any dimension.
    - For Boolean operation *SECTION* the arguments can be of any type.

    Additionally to the errors of the base class the algorithm returns
    the following Errors:
    - *BOPAlgo_AlertBOPNotSet* - in case the type of Boolean Operation is not set.
    """

    @overload
    def __init__(self) -> None:
        """
        @name Constructors
        Empty constructor
        """

    @overload
    def __init__(self, thePF: nanoocp.BOPAlgo.BOPAlgo_PaveFiller) -> None:
        """Constructor with precomputed intersections of arguments."""

    def Shape1(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        @name Setting/getting arguments
        Returns the first argument involved in this Boolean operation.
        Obsolete
        """

    def Shape2(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the second argument involved in this Boolean operation.
        Obsolete
        """

    def SetTools(self, theLS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Sets the Tool arguments"""

    def Tools(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the Tools arguments"""

    def SetOperation(self, theBOP: nanoocp.BOPAlgo.BOPAlgo_Operation) -> None:
        """
        @name Setting/Getting the type of Boolean operation
        Sets the type of Boolean operation
        """

    def Operation(self) -> nanoocp.BOPAlgo.BOPAlgo_Operation:
        """Returns the type of Boolean Operation"""

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        @name Performing the operation
        Performs the Boolean operation.
        """

class BRepAlgoAPI_Check(nanoocp.BOPAlgo.BOPAlgo_Options):
    """
    The class Check provides a diagnostic tool for checking the validity
    of the single shape or couple of shapes.
    The shapes are checked on:
    - Topological validity;
    - Small edges;
    - Self-interference;
    - Validity for Boolean operation of certain type (for couple of shapes only).

    The class provides two ways of checking shape(-s)
    1. Constructors
    BRepAlgoAPI_Check aCh(theS);
    bool isValid = aCh.IsValid();
    2. Methods SetData and Perform
    BRepAlgoAPI_Check aCh;
    aCh.SetData(theS1, theS2, BOPAlgo_FUSE, false);
    aCh.Perform();
    bool isValid = aCh.IsValid();
    """

    @overload
    def __init__(self) -> None:
        """
        @name Constructors
        Empty constructor.
        """

    @overload
    def __init__(self, theS: nanoocp.TopoDS.TopoDS_Shape, bTestSE: bool = True, bTestSI: bool = True, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Constructor for checking single shape.

        @param[in] theS  - the shape to check;
        @param[in] bTestSE  - flag which specifies whether to check the shape
        on small edges or not; by default it is set to TRUE;
        @param[in] bTestSI  - flag which specifies whether to check the shape
        on self-interference or not; by default it is set to TRUE;
        @param[in] theRange  - parameter to use progress indicator
        """

    @overload
    def __init__(self, theS1: nanoocp.TopoDS.TopoDS_Shape, theS2: nanoocp.TopoDS.TopoDS_Shape, theOp: nanoocp.BOPAlgo.BOPAlgo_Operation = BOPAlgo_Operation.BOPAlgo_UNKNOWN, bTestSE: bool = True, bTestSI: bool = True, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Constructor for checking the couple of shapes.
        Additionally to the validity checks of each given shape,
        the types of the given shapes will be checked on validity
        for Boolean operation of given type.

        @param[in] theS1  - the first shape to check;
        @param[in] theS2  - the second shape to check;
        @param[in] theOp  - the type of Boolean Operation for which the validity
        of given shapes should be checked.
        @param[in] bTestSE  - flag which specifies whether to check the shape
        on small edges or not; by default it is set to TRUE;
        @param[in] bTestSI  - flag which specifies whether to check the shape
        on self-interference or not; by default it is set to TRUE;
        @param[in] theRange  - parameter to use progress indicator
        """

    @overload
    def __init__(self, theOther: BRepAlgoAPI_Check) -> None: ...

    @overload
    def SetData(self, theS: nanoocp.TopoDS.TopoDS_Shape, bTestSE: bool = True, bTestSI: bool = True) -> None:
        """
        @name Initializing the algorithm
        Initializes the algorithm with single shape.

        @param[in] theS  - the shape to check;
        @param[in] bTestSE  - flag which specifies whether to check the shape
        on small edges or not; by default it is set to TRUE;
        @param[in] bTestSI  - flag which specifies whether to check the shape
        on self-interference or not; by default it is set to TRUE;
        """

    @overload
    def SetData(self, theS1: nanoocp.TopoDS.TopoDS_Shape, theS2: nanoocp.TopoDS.TopoDS_Shape, theOp: nanoocp.BOPAlgo.BOPAlgo_Operation = BOPAlgo_Operation.BOPAlgo_UNKNOWN, bTestSE: bool = True, bTestSI: bool = True) -> None:
        """
        Initializes the algorithm with couple of shapes.
        Additionally to the validity checks of each given shape,
        the types of the given shapes will be checked on validity
        for Boolean operation of given type.

        @param[in] theS1  - the first shape to check;
        @param[in] theS2  - the second shape to check;
        @param[in] theOp  - the type of Boolean Operation for which the validity
        of given shapes should be checked.
        @param[in] bTestSE  - flag which specifies whether to check the shape
        on small edges or not; by default it is set to TRUE;
        @param[in] bTestSI  - flag which specifies whether to check the shape
        on self-interference or not; by default it is set to TRUE;
        """

    def Perform(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        @name Performing the operation
        Performs the check.
        """

    def IsValid(self) -> bool:
        """
        @name Getting the results.
        Shows whether shape(s) valid or not.
        """

    def Result(self) -> nanoocp.NCollection.NCollection_List[nanoocp.BOPAlgo.BOPAlgo_CheckResult]:
        """Returns faulty shapes."""

class BRepAlgoAPI_Common(BRepAlgoAPI_BooleanOperation):
    """
    The class provides Boolean common operation
    between arguments and tools (Boolean Intersection).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, PF: nanoocp.BOPAlgo.BOPAlgo_PaveFiller) -> None:
        """
        Empty constructor
        <PF> - PaveFiller object that is carried out
        """

    @overload
    def __init__(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Constructor with two shapes
        <S1>  -argument
        <S2>  -tool
        <anOperation> - the type of the operation
        Obsolete
        """

    @overload
    def __init__(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, PF: nanoocp.BOPAlgo.BOPAlgo_PaveFiller, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Constructor with two shapes
        <S1>  -argument
        <S2>  -tool
        <anOperation> - the type of the operation
        <PF> - PaveFiller object that is carried out
        Obsolete
        """

class BRepAlgoAPI_Cut(BRepAlgoAPI_BooleanOperation):
    """
    The class Cut provides Boolean cut operation
    between arguments and tools (Boolean Subtraction).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, PF: nanoocp.BOPAlgo.BOPAlgo_PaveFiller) -> None:
        """
        Empty constructor
        <PF> - PaveFiller object that is carried out
        """

    @overload
    def __init__(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Constructor with two shapes
        <S1>  -argument
        <S2>  -tool
        <anOperation> - the type of the operation
        Obsolete
        """

    @overload
    def __init__(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, aDSF: nanoocp.BOPAlgo.BOPAlgo_PaveFiller, bFWD: bool = True, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Constructor with two shapes
        <S1>  -argument
        <S2>  -tool
        <anOperation> - the type of the operation
        <PF> - PaveFiller object that is carried out
        Obsolete
        """

class BRepAlgoAPI_Defeaturing(BRepAlgoAPI_Algo):
    """
    The BRepAlgoAPI_Defeaturing algorithm is the API algorithm intended for
    removal of the unwanted parts from the shape. The unwanted parts
    (or features) can be holes, protrusions, gaps, chamfers, fillets etc.
    The shape itself is not modified, the new shape is built as the result.

    The actual removal of the features from the shape is performed by
    the low-level *BOPAlgo_RemoveFeatures* tool. So the defeaturing algorithm
    has the same options, input data requirements, limitations as the
    low-level algorithm.

    <b>Input data</b>

    Currently, only the shapes of type SOLID, COMPSOLID, and COMPOUND of Solids
    are supported. And only the FACEs can be removed from the shape.

    On the input the algorithm accepts the shape itself and the
    features which have to be removed. It does not matter how the features
    are given. It could be the separate faces or the collections
    of faces. The faces should belong to the initial shape, and those that
    do not belong will be ignored.

    <b>Options</b>

    The algorithm has the following options:
    - History support;

    and the options available from base class:
    - Error/Warning reporting system;
    - Parallel processing mode.

    Please note that the other options of the base class are not supported
    here and will have no effect.

    For the details on the available options please refer to the description
    of *BOPAlgo_RemoveFeatures* algorithm.

    <b>Limitations</b>

    The defeaturing algorithm has the same limitations as *BOPAlgo_RemoveFeatures*
    algorithm.

    <b>Example</b>

    Here is the example of usage of the algorithm:
    ~~~~
    TopoDS_Shape aSolid = ...;               // Input shape to remove the features from
    NCollection_List<TopoDS_Shape> aFeatures = ...;    // Features to remove from the shape
    bool bRunParallel = ...;     // Parallel processing mode
    bool isHistoryNeeded = ...;  // History support

    BRepAlgoAPI_Defeaturing aDF;             // De-Featuring algorithm
    aDF.SetShape(aSolid);                    // Set the shape
    aDF.AddFacesToRemove(aFaces);            // Add faces to remove
    aDF.SetRunParallel(bRunParallel);        // Define the processing mode (parallel or single)
    aDF.SetToFillHistory(isHistoryNeeded);   // Define whether to track the shapes modifications
    aDF.Build();                             // Perform the operation
    if (!aDF.IsDone())                       // Check for the errors
    {
    // error treatment
    Standard_SStream aSStream;
    aDF.DumpErrors(aSStream);
    return;
    }
    if (aDF.HasWarnings())                   // Check for the warnings
    {
    // warnings treatment
    Standard_SStream aSStream;
    aDF.DumpWarnings(aSStream);
    }
    const TopoDS_Shape& aResult = aDF.Shape(); // Result shape
    ~~~~

    The algorithm preserves the type of the input shape in the result shape. Thus,
    if the input shape is a COMPSOLID, the resulting solids will also be put into a COMPSOLID.
    """

    @overload
    def __init__(self) -> None:
        """
        @name Constructors
        Empty constructor
        """

    @overload
    def __init__(self, theOther: BRepAlgoAPI_Defeaturing) -> None: ...

    def SetShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        @name Setting input data for the algorithm
        Sets the shape for processing.
        @param[in] theShape  The shape to remove the features from.
        It should either be the SOLID, COMPSOLID or COMPOUND of Solids.
        """

    def InputShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the input shape"""

    def AddFaceToRemove(self, theFace: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Adds the features to remove from the input shape.
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

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        @name Performing the operation
        Performs the operation
        """

    def SetToFillHistory(self, theFlag: bool) -> None:
        """
        @name History Methods
        Defines whether to track the modification of the shapes or not.
        """

    def HasHistory(self) -> bool:
        """Returns whether the history was requested or not."""

    def Modified(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes modified from the shape <theS> during the operation.
        """

    def Generated(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes generated from the shape <theS> during the operation.
        """

    def IsDeleted(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Returns true if the shape <theS> has been deleted during the operation.
        It means that the shape has no any trace in the result.
        Otherwise it returns false.
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
        """Returns the History of shapes modifications"""

class BRepAlgoAPI_Fuse(BRepAlgoAPI_BooleanOperation):
    """
    The class provides Boolean fusion operation
    between arguments and tools (Boolean Union).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, PF: nanoocp.BOPAlgo.BOPAlgo_PaveFiller) -> None:
        """
        Empty constructor
        <PF> - PaveFiller object that is carried out
        """

    @overload
    def __init__(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Constructor with two shapes
        <S1>  -argument
        <S2>  -tool
        <anOperation> - the type of the operation
        Obsolete
        """

    @overload
    def __init__(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, aDSF: nanoocp.BOPAlgo.BOPAlgo_PaveFiller, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Constructor with two shapes
        <S1>  -argument
        <S2>  -tool
        <anOperation> - the type of the operation
        <PF> - PaveFiller object that is carried out
        Obsolete
        """

class BRepAlgoAPI_Section(BRepAlgoAPI_BooleanOperation):
    """
    The algorithm is to build a Section operation between arguments and tools.
    The result of Section operation consists of vertices and edges.
    The result of Section operation contains:
    1. new vertices that are subjects of V/V, E/E, E/F, F/F interferences
    2. vertices that are subjects of V/E, V/F interferences
    3. new edges that are subjects of F/F interferences
    4. edges that are Common Blocks
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, PF: nanoocp.BOPAlgo.BOPAlgo_PaveFiller) -> None:
        """
        Empty constructor
        <PF> - PaveFiller object that is carried out
        """

    @overload
    def __init__(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, PerformNow: bool = True) -> None:
        """
        Constructor with two shapes
        <S1>  -argument
        <S2>  -tool
        <PerformNow> - the flag:
        if <PerformNow>=True - the algorithm is performed immediately
        Obsolete
        """

    @overload
    def __init__(self, S1: nanoocp.TopoDS.TopoDS_Shape, Pl: nanoocp.gp.gp_Pln, PerformNow: bool = True) -> None:
        """
        Constructor with two shapes
        <S1>  - argument
        <Pl>  - tool
        <PerformNow> - the flag:
        if <PerformNow>=True - the algorithm is performed immediately
        Obsolete
        """

    @overload
    def __init__(self, S1: nanoocp.TopoDS.TopoDS_Shape, Sf: nanoocp.Geom.Geom_Surface | None, PerformNow: bool = True) -> None:
        """
        Constructor with two shapes
        <S1>  - argument
        <Sf>  - tool
        <PerformNow> - the flag:
        if <PerformNow>=True - the algorithm is performed immediately
        Obsolete
        """

    @overload
    def __init__(self, Sf: nanoocp.Geom.Geom_Surface | None, S2: nanoocp.TopoDS.TopoDS_Shape, PerformNow: bool = True) -> None:
        """
        Constructor with two shapes
        <Sf>  - argument
        <S2>  - tool
        <PerformNow> - the flag:
        if <PerformNow>=True - the algorithm is performed immediately
        Obsolete
        """

    @overload
    def __init__(self, Sf1: nanoocp.Geom.Geom_Surface | None, Sf2: nanoocp.Geom.Geom_Surface | None, PerformNow: bool = True) -> None:
        """
        Constructor with two shapes
        <Sf1>  - argument
        <Sf2>  - tool
        <PerformNow> - the flag:
        if <PerformNow>=True - the algorithm is performed immediately
        Obsolete
        """

    @overload
    def __init__(self, S1: nanoocp.TopoDS.TopoDS_Shape, S2: nanoocp.TopoDS.TopoDS_Shape, aDSF: nanoocp.BOPAlgo.BOPAlgo_PaveFiller, PerformNow: bool = True) -> None:
        """
        Constructor with two shapes
        <S1>  -argument
        <S2>  -tool
        <PF> - PaveFiller object that is carried out
        <PerformNow> - the flag:
        if <PerformNow>=True - the algorithm is performed immediately
        Obsolete
        """

    @overload
    def Init1(self, S1: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        initialize the argument
        <S1>  - argument
        Obsolete
        """

    @overload
    def Init1(self, Pl: nanoocp.gp.gp_Pln) -> None:
        """
        initialize the argument
        <Pl>  - argument
        Obsolete
        """

    @overload
    def Init1(self, Sf: nanoocp.Geom.Geom_Surface | None) -> None:
        """
        initialize the argument
        <Sf>  - argument
        Obsolete
        """

    @overload
    def Init2(self, S2: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        initialize the tool
        <S2>  - tool
        Obsolete
        """

    @overload
    def Init2(self, Pl: nanoocp.gp.gp_Pln) -> None:
        """
        initialize the tool
        <Pl>  - tool
        Obsolete
        """

    @overload
    def Init2(self, Sf: nanoocp.Geom.Geom_Surface | None) -> None:
        """
        initialize the tool
        <Sf>  - tool
        Obsolete
        """

    def Approximation(self, B: bool) -> None: ...

    def ComputePCurveOn1(self, B: bool) -> None:
        """
        Indicates whether the P-Curve should be (or not)
        performed on the argument.
        By default, no parametric 2D curve (pcurve) is defined for the
        edges of the result.
        If ComputePCurve1 equals true, further computations performed
        to attach an P-Curve in the parametric space of the argument
        to the constructed edges.
        Obsolete
        """

    def ComputePCurveOn2(self, B: bool) -> None:
        """
        Indicates whether the P-Curve should be (or not)
        performed on the tool.
        By default, no parametric 2D curve (pcurve) is defined for the
        edges of the result.
        If ComputePCurve1 equals true, further computations performed
        to attach an P-Curve in the parametric space of the tool
        to the constructed edges.
        Obsolete
        """

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Performs the algorithm
        Filling interference Data Structure (if it is necessary)
        Building the result of the operation.
        """

    def HasAncestorFaceOn1(self, E: nanoocp.TopoDS.TopoDS_Shape, F: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        get the face of the first part giving section edge <E>.
        Returns True on the 3 following conditions :
        1/ <E> is an edge returned by the Shape() metwod.
        2/ First part of section performed is a shape.
        3/ <E> is built on a intersection curve (i.e <E>
        is not the result of common edges)
        When False, F remains untouched.
        Obsolete
        """

    def HasAncestorFaceOn2(self, E: nanoocp.TopoDS.TopoDS_Shape, F: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Identifies the ancestor faces of
        the intersection edge E resulting from the last
        computation performed in this framework, that is, the faces of
        the two original shapes on which the edge E lies:
        -      HasAncestorFaceOn1 gives the ancestor face in the first shape, and
        -      HasAncestorFaceOn2 gives the ancestor face in the second shape.
        These functions return true if an ancestor face F is found, or false if not.
        An ancestor face is identifiable for the edge E if the following
        conditions are satisfied:
        -  the first part on which this algorithm performed its
        last computation is a shape, that is, it was not given as
        a surface or a plane at the time of construction of this
        algorithm or at a later time by the Init1 function,
        - E is one of the elementary edges built by the
        last computation of this section algorithm.
        To use these functions properly, you have to test the returned
        Boolean value before using the ancestor face: F is significant
        only if the returned Boolean value equals true.
        Obsolete
        """

class BRepAlgoAPI_Splitter(BRepAlgoAPI_BuilderAlgo):
    """
    The class contains API level of the **Splitter** algorithm,
    which allows splitting a group of arbitrary shapes by the
    other group of arbitrary shapes.
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

    The algorithm returns the following Error statuses:
    - 0 - in case of success;
    - *BOPAlgo_AlertTooFewArguments*    - in case there is no enough arguments for the
    operation;
    - *BOPAlgo_AlertIntersectionFailed* - in case the Intersection of the arguments has failed;
    - *BOPAlgo_AlertBuilderFailed*      - in case the Building of the result has failed.
    """

    @overload
    def __init__(self) -> None:
        """
        @name Constructors
        Empty constructor
        """

    @overload
    def __init__(self, thePF: nanoocp.BOPAlgo.BOPAlgo_PaveFiller) -> None:
        """Constructor with already prepared intersection tool - PaveFiller"""

    def SetTools(self, theLS: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        @name Setters/Getters for the Tools
        Sets the Tool arguments
        """

    def Tools(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the Tool arguments"""

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        @name Performing the operation
        Performs the Split operation.
        Performs the intersection of the argument shapes (both objects and tools)
        and splits objects by the tools.
        """
