"""OCCT package XSAlgo (toolkit TKXSBase)"""

from typing import overload

import nanoocp.DE
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.ShapeExtend
import nanoocp.ShapeProcess
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.Transfer
import nanoocp.TopTools


class XSAlgo:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XSAlgo) -> None: ...

    @staticmethod
    def Init() -> None:
        """
        Provides initerface to the algorithms from Shape Healing
        and others for XSTEP processors.
        Creates and initializes default AlgoContainer.
        """

    @staticmethod
    def SetAlgoContainer(aContainer: XSAlgo_AlgoContainer | None) -> None:
        """Sets default AlgoContainer"""

    @staticmethod
    def AlgoContainer() -> XSAlgo_AlgoContainer:
        """Returns default AlgoContainer"""

class XSAlgo_AlgoContainer(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: XSAlgo_AlgoContainer) -> None: ...

    def PrepareForTransfer(self) -> None:
        """
        Performs actions necessary for preparing environment
        for transfer. Empty in Open version.
        """

    def ProcessShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape, thePrec: float, theMaxTol: float, thePrscfile: str, thePseq: str, theProgress: nanoocp.Message.Message_ProgressRange = ..., theNonManifold: bool = False, theDetailingLevel: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_VERTEX) -> tuple[nanoocp.TopoDS.TopoDS_Shape, nanoocp.Standard.Standard_Transient]:
        """
        Does shape processing with specified tolerances
        @param[in] theShape shape to process
        @param[in] thePrec basic precision and tolerance
        @param[in] theMaxTol maximum allowed tolerance
        @param[in] thePrscfile name of the resource file
        @param[in] thePseq name of the sequence of operators defined in the resource file for Shape
        Processing
        @param[out] theInfo information to be recorded in the translation map
        @param[in] theProgress progress indicator
        @param[in] theNonManifold flag to proceed with non-manifold topology
        @param[in] theDetailingLevel the lowest shape type to be processed, lower shapes are ignored
        @return the processed shape
        """

    def CheckPCurve(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face, thePrecision: float, theIsSeam: bool) -> bool:
        """
        Checks quality of pcurve of the edge on the given face,
        and corrects it if necessary.
        """

    @overload
    def MergeTransferInfo(self, TP: nanoocp.Transfer.Transfer_TransientProcess | None, info: nanoocp.Standard.Standard_Transient | None, startTPitem: int = 1) -> None: ...

    @overload
    def MergeTransferInfo(self, FP: nanoocp.Transfer.Transfer_FinderProcess | None, info: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Updates translation map (TP or FP) with information
        resulting from ShapeProcessing
        Parameter startTPitem can be used for optimisation, to
        restrict modifications to entities stored in TP starting
        from item startTPitem
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XSAlgo_ShapeProcessor:
    """
    Shape Processing module.
    Allows to define and apply general Shape Processing as a customizable sequence of operators.
    """

    @overload
    def __init__(self, theParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString], theShapeFixParameters: nanoocp.DE.DE_ShapeFixParameters = ...) -> None:
        """
        Constructor.
        @param theParameters Pre-filled parameter map to be used in the processing.
        @param theShapeFixParameters Shape healing parameters to be used in the processing.
        If @p theParameters has some shape healing values, they will override the
        corresponding values from @p theShapeFixParameters.
        """

    @overload
    def __init__(self, theParameters: nanoocp.DE.DE_ShapeFixParameters) -> None:
        """
        Constructor.
        @param theParameters Parameters to be used in the processing.
        """

    @overload
    def __init__(self, theOther: XSAlgo_ShapeProcessor) -> None: ...

    def GetContext(self) -> nanoocp.ShapeProcess.ShapeProcess_ShapeContext:
        """
        Get the context of the last processing.
        Only valid after the ProcessShape() method was called.
        @return Shape context.
        """

    @overload
    def MergeTransferInfo(self, theTransientProcess: nanoocp.Transfer.Transfer_TransientProcess | None, theFirstTPItemIndex: int) -> None:
        """
        Merge the results of the shape processing with the transfer process.
        @param theTransientProcess Transfer process to merge with.
        @param theFirstTPItemIndex Index of the first item in the transfer process to merge with.
        """

    @overload
    def MergeTransferInfo(self, theFinderProcess: nanoocp.Transfer.Transfer_FinderProcess | None) -> None:
        """
        Merge the results of the shape processing with the finder process.
        @param theFinderProcess Finder process to merge with.
        """

    @staticmethod
    def CheckPCurve(theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face, thePrecision: float, theIsSeam: bool) -> bool:
        """
        Check quality of pcurve of the edge on the given face, and correct it if necessary.
        @param theEdge Edge to check.
        @param theFace Face on which the edge is located.
        @param thePrecision Precision to use for checking.
        @param theIsSeam Flag indicating whether the edge is a seam edge.
        @return True if the pcurve was corrected, false if it was dropped.
        """

    @staticmethod
    def FillParameterMap(theParameters: nanoocp.DE.DE_ShapeFixParameters, theIsReplace: bool, theMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Fill the parameter map with the values from the specified parameters.
        @param theParameters Parameters to be used in the processing.
        @param theIsForce Flag indicating whether parameter should be replaced if it already exists in
        the map.
        @param theMap Map to fill.
        """

    @staticmethod
    def SetShapeFixParameters(theParameters: nanoocp.DE.DE_ShapeFixParameters, theAdditionalParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString], theTargetParameterMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Sets parameters for shape processing.
        Parameters from @p theParameters are copied to the output map.
        Parameters from @p theAdditionalParameters are copied to the output map
        if they are not present in @p theParameters.
        @param theParameters the parameters for shape processing.
        @param theAdditionalParameters the additional parameters for shape processing.
        @param theTargetParameterMap Map to set the parameters in.
        """

    @overload
    @staticmethod
    def SetParameter(theKey: str, theValue: nanoocp.DE.DE_ShapeFixParameters.FixMode, theIsReplace: bool, theMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None: ...

    @overload
    @staticmethod
    def SetParameter(theKey: str, theValue: float, theIsReplace: bool, theMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None: ...

    @overload
    @staticmethod
    def SetParameter(theKey: str, theValue: nanoocp.TCollection.TCollection_AsciiString, theIsReplace: bool, theMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Set the parameter in the map.
        @param theKey Key of the parameter.
        @param theValue Value of the parameter.
        @param theIsReplace Flag indicating whether parameter should be replaced if it already exists
        in the map.
        @param theMap Map to set the parameter in.
        """

    @staticmethod
    def PrepareForTransfer() -> None:
        """
        The function is designed to set the length unit for the application before performing a
        transfer operation. It ensures that the length unit is correctly configured based on the
        value associated with the key "xstep.cascade.unit".
        """

    @overload
    @staticmethod
    def MergeShapeTransferInfo(theFinderProcess: nanoocp.Transfer.Transfer_TransientProcess | None, theModifiedShapesMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theFirstTPItemIndex: int, theMessages: nanoocp.ShapeExtend.ShapeExtend_MsgRegistrator | None) -> None:
        """
        Merge the results of the shape processing with the finder process.
        @param theTransientProcess Transfer process to merge with.
        @param theModifiedShapesMap Map of modified shapes.
        @param theFirstTPItemIndex Index of the first item in the transfer process to merge with.
        @param theMessages Messages to add.
        """

    @overload
    @staticmethod
    def MergeShapeTransferInfo(theTransientProcess: nanoocp.Transfer.Transfer_FinderProcess | None, theModifiedShapesMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theMessages: nanoocp.ShapeExtend.ShapeExtend_MsgRegistrator | None) -> None:
        """
        Merge the results of the shape processing with the transfer process.
        @param theTransientProcess Transfer process to merge with.
        @param theModifiedShapesMap Map of modified shapes.
        @param theFirstTPItemIndex Index of the first item in the transfer process to merge with.
        @param theMessages Messages to add.
        """
