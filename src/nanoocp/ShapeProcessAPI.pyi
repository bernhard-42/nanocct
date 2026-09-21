"""OCCT package ShapeProcessAPI (toolkit TKShHealing)"""

from typing import overload

import nanoocp.Message
import nanoocp.NCollection
import nanoocp.ShapeProcess
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.TopTools


class ShapeProcessAPI_ApplySequence:
    """Applies one of the sequence read from resource file."""

    @overload
    def __init__(self, rscName: str, seqName: str = '') -> None:
        """
        Creates an object and loads resource file and sequence of
        operators given by their names.
        """

    @overload
    def __init__(self, theOther: ShapeProcessAPI_ApplySequence) -> None: ...

    def Context(self) -> nanoocp.ShapeProcess.ShapeProcess_ShapeContext:
        """
        Returns object for managing resource file and sequence of
        operators.
        """

    def PrepareShape(self, shape: nanoocp.TopoDS.TopoDS_Shape, fillmap: bool = False, until: nanoocp.TopAbs.TopAbs_ShapeEnum = TopAbs_ShapeEnum.TopAbs_SHAPE, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Performs sequence of operators stored in myRsc.
        If <fillmap> is True adds history "shape-shape" into myMap
        for shape and its subshapes until level <until> (included).
        If <until> is TopAbs_SHAPE, all the subshapes are considered.
        """

    def ClearMap(self) -> None:
        """Clears myMap with accumulated history."""

    def Map(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """Returns myMap with accumulated history."""

    def PrintPreparationResult(self) -> None:
        """
        Prints result of preparation onto the messenger of the context.
        Note that results can be accumulated from previous preparations
        it method ClearMap was not called before PrepareShape.
        """
