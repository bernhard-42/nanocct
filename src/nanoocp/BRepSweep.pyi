"""OCCT package BRepSweep (toolkit TKPrim)"""

from typing import overload

import nanoocp.BRep
import nanoocp.Sweep
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.gp


class BRepSweep_Builder:
    """implements the abstract Builder with the BRep Builder"""

    @overload
    def __init__(self, aBuilder: nanoocp.BRep.BRep_Builder) -> None:
        """Creates a Builder."""

    @overload
    def __init__(self, theOther: BRepSweep_Builder) -> None: ...

    def Builder(self) -> nanoocp.BRep.BRep_Builder: ...

    def MakeCompound(self, aCompound: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Returns an empty Compound."""

    def MakeCompSolid(self, aCompSolid: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Returns an empty CompSolid."""

    def MakeSolid(self, aSolid: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Returns an empty Solid."""

    def MakeShell(self, aShell: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Returns an empty Shell."""

    def MakeWire(self, aWire: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Returns an empty Wire."""

    @overload
    def Add(self, aShape1: nanoocp.TopoDS.TopoDS_Shape, aShape2: nanoocp.TopoDS.TopoDS_Shape, Orient: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Adds the Shape 1 in the Shape 2, set to
        <Orient> orientation.
        """

    @overload
    def Add(self, aShape1: nanoocp.TopoDS.TopoDS_Shape, aShape2: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Adds the Shape 1 in the Shape 2."""

class BRepSweep_Iterator:
    """
    This class provides iteration services required by
    the Generating Line (TopoDS Shape) of a BRepSweep.
    This tool is used to iterate on the direct
    sub-shapes of a Shape.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepSweep_Iterator) -> None: ...

    def __iter__(self) -> BRepSweep_Iterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Python addition: see __iter__."""

    def Init(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Reset the Iterator on sub-shapes of <aShape>."""

    def More(self) -> bool:
        """Returns True if there is a current sub-shape."""

    def Next(self) -> None:
        """Moves to the next sub-shape."""

    def Value(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the current sub-shape."""

    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Returns the orientation of the current sub-shape."""

class BRepSweep_Tool:
    """
    Provides the indexation and type analysis services
    required by the TopoDS generating Shape of BRepSweep.
    """

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Initialize the tool with <aShape>. The IndexTool
        must prepare an indexation for all the subshapes
        of this shape.
        """

    @overload
    def __init__(self, theOther: BRepSweep_Tool) -> None: ...

    def NbShapes(self) -> int:
        """Returns the number of subshapes in the shape."""

    def Index(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> int:
        """Returns the index of <aShape>."""

    def Shape(self, anIndex: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the Shape at Index anIdex."""

    def Type(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_ShapeEnum:
        """Returns the type of <aShape>."""

    def Orientation(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Returns the Orientation of <aShape>."""

    def SetOrientation(self, aShape: nanoocp.TopoDS.TopoDS_Shape, Or: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """Set the Orientation of <aShape> with Or."""

class BRepSweep_NumLinearRegularSweep:
    """
    This a generic class is used to build Sweept
    primitives with a generating "shape" and a
    directing "line".

    The indexation and type analysis services required
    for the generatrix are given by <Tool from BRepSweep>.

    The indexation and type analysis services required
    for the directrix are given by <NumShapeTool from Sweep>.

    The iteration services required for the generatrix
    are given by <Iterator from BRepSweep>.

    The iteration services required for the directrix
    are given by <NumShapeIterator from Sweep>.

    The topology is like a grid of shapes. Each shape
    of the grid must be addressable without confusion
    by one or two objects from the generating or
    directing shapes. Here are examples of correct
    associations to address:

    - a vertex : GenVertex - DirVertex
    - an edge  : GenVertex - DirEdge
    -          : GenEdge   - DirVertex
    - a face   : GenEdge   - DirEdge
    GenFace   - DirVertex
    ...

    "GenObject" is used to identify an object from the
    Generating Shape, and "DirObject" from the
    Directing Shape. So may they be from different
    types.

    The method Has... is given because in some special
    cases, a vertex, an edge or a face may be
    geometricaly nonexistent or not useful.
    """

    def MakeEmptyVertex(self, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the vertex addressed by [aGenV,aDirV], with its
        geometric part, but without subcomponents.
        """

    def MakeEmptyDirectingEdge(self, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the edge addressed by [aGenV,aDirE], with its
        geometric part, but without subcomponents.
        """

    def MakeEmptyGeneratingEdge(self, aGenE: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the edge addressed by [aGenE,aDirV], with its
        geometric part, but without subcomponents.
        """

    def SetParameters(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewVertex: nanoocp.TopoDS.TopoDS_Shape, aGenF: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> None:
        """
        Sets the parameters of the new vertex on the new
        face. The new face and new vertex where generated
        from aGenF, aGenV and aDirV .
        """

    def SetDirectingParameter(self, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aNewVertex: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> None:
        """
        Sets the parameter of the new vertex on the new
        edge. The new edge and new vertex where generated
        from aGenV aDirE, and aDirV.
        """

    def SetGeneratingParameter(self, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aNewVertex: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> None:
        """
        Sets the parameter of the new vertex on the new
        edge. The new edge and new vertex where generated
        from aGenE, aGenV and aDirV .
        """

    def MakeEmptyFace(self, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the face addressed by [aGenS,aDirS], with
        its geometric part, but without subcomponents. The
        couple aGenS, aDirS can be a "generating face and
        a directing vertex" or "a generating edge and a
        directing edge".
        """

    def SetPCurve(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aGenF: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape, orien: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Sets the PCurve for a new edge on a new face. The
        new edge and the new face were generated using
        aGenF, aGenE and aDirV.
        """

    def SetGeneratingPCurve(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape, aDirV: nanoocp.Sweep.Sweep_NumShape, orien: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Sets the PCurve for a new edge on a new face. The
        new edge and the new face were generated using
        aGenE, aDirE and aDirV.
        """

    def SetDirectingPCurve(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape, orien: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Sets the PCurve for a new edge on a new face. The
        new edge and the new face were generated using
        aGenE, aDirE and aGenV.
        """

    def DirectSolid(self, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopAbs.TopAbs_Orientation:
        """
        Returns the Orientation of the shell in the solid
        generated by the face aGenS with the edge aDirS.
        It is REVERSED if the surface is swept in the
        direction of the normal.
        """

    def GGDShapeIsToAdd(self, aNewShape: nanoocp.TopoDS.TopoDS_Shape, aNewSubShape: nanoocp.TopoDS.TopoDS_Shape, aGenS: nanoocp.TopoDS.TopoDS_Shape, aSubGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        Returns true if aNewSubShape (addressed by
        aSubGenS and aDirS) must be added in aNewShape
        (addressed by aGenS and aDirS).
        """

    def GDDShapeIsToAdd(self, aNewShape: nanoocp.TopoDS.TopoDS_Shape, aNewSubShape: nanoocp.TopoDS.TopoDS_Shape, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape, aSubDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        Returns true if aNewSubShape (addressed by
        aGenS and aSubDirS) must be added in aNewShape
        (addressed by aGenS and aDirS).
        """

    def SeparatedWires(self, aNewShape: nanoocp.TopoDS.TopoDS_Shape, aNewSubShape: nanoocp.TopoDS.TopoDS_Shape, aGenS: nanoocp.TopoDS.TopoDS_Shape, aSubGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        In some particular cases the topology of a
        generated face must be composed of independent
        closed wires, in this case this function returns
        true.
        """

    def SplitShell(self, aNewShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        In some particular cases the topology of a
        generated Shell must be composed of independent
        closed Shells, in this case this function returns
        a Compound of independent Shells.
        """

    def SetContinuity(self, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> None:
        """
        Called to propagate the continuity of every vertex
        between two edges of the generating wire aGenS on
        the generated edge and faces.
        """

    def HasShape(self, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        Returns true if aDirS and aGenS addresses a
        resulting Shape. In some specific cases the shape
        can be geometrically inexsistant, then this
        function returns false.
        """

    def IsInvariant(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns true if aGenS cannot be transformed."""

    @overload
    def Shape(self, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the resulting Shape indexed by aDirS and
        aGenS.
        """

    @overload
    def Shape(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the resulting Shape indexed by myDirWire
        and aGenS.
        """

    @overload
    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the resulting Shape indexed by myDirWire
        and myGenShape.
        """

    def IsUsed(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Returns true if the initial shape aGenS
        is used in result shape
        """

    def GenIsUsed(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Returns true if the shape, generated from theS
        is used in result shape
        """

    @overload
    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the resulting Shape indexed by the first
        Vertex of myDirWire and myGenShape.
        """

    @overload
    def FirstShape(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the resulting Shape indexed by the first
        Vertex of myDirWire and aGenS.
        """

    @overload
    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the resulting Shape indexed by the last
        Vertex of myDirWire and myGenShape.
        """

    @overload
    def LastShape(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the resulting Shape indexed by the last
        Vertex of myDirWire and aGenS.
        """

    def Closed(self) -> bool: ...

class BRepSweep_Trsf(BRepSweep_NumLinearRegularSweep):
    """
    This class is inherited from NumLinearRegularSweep
    to implement the simple swept primitives built
    moving a Shape with a Trsf. It often is possible
    to build the constructed subshapes by a simple
    move of the generating subshapes (shared topology
    and geometry). So two ways of construction are
    proposed:

    - sharing basis elements (the generatrice can be
    modified, for example PCurves can be added on
    faces);

    - copying everything.
    """

    def Init(self) -> None:
        """
        ends the construction of the swept primitive
        calling the virtual geometric functions that can't
        be called in the initialize.
        """

    def Process(self, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        function called to analyze the way of construction
        of the shapes generated by aGenS and aDirV.
        """

    def MakeEmptyVertex(self, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the vertex addressed by [aGenV,aDirV], with its
        geometric part, but without subcomponents.
        """

    def MakeEmptyDirectingEdge(self, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the edge addressed by [aGenV,aDirE], with its
        geometric part, but without subcomponents.
        """

    def MakeEmptyGeneratingEdge(self, aGenE: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the edge addressed by [aGenE,aDirV], with its
        geometric part, but without subcomponents.
        """

    def SetParameters(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewVertex: nanoocp.TopoDS.TopoDS_Shape, aGenF: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> None:
        """
        Sets the parameters of the new vertex on the new
        face. The new face and new vertex where generated
        from aGenF, aGenV and aDirV.
        """

    def SetDirectingParameter(self, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aNewVertex: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> None:
        """
        Sets the parameter of the new vertex on the new
        edge. The new edge and new vertex where generated
        from aGenV aDirE, and aDirV.
        """

    def SetGeneratingParameter(self, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aNewVertex: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> None:
        """
        Sets the parameter of the new vertex on the new
        edge. The new edge and new vertex where generated
        from aGenE, aGenV and aDirV.
        """

    def MakeEmptyFace(self, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the face addressed by [aGenS,aDirS], with
        its geometric part, but without subcomponents. The
        couple aGenS, aDirS can be a "generating face and
        a directing vertex" or "a generating edge and a
        directing edge".
        """

    def SetPCurve(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aGenF: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape, orien: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Sets the PCurve for a new edge on a new face. The
        new edge and the new face were generated using
        aGenF, aGenE and aDirV.
        """

    def SetGeneratingPCurve(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape, aDirV: nanoocp.Sweep.Sweep_NumShape, orien: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Sets the PCurve for a new edge on a new face. The
        new edge and the new face were generated using
        aGenE, aDirE and aDirV.
        """

    def SetDirectingPCurve(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape, orien: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Sets the PCurve for a new edge on a new face. The
        new edge and the new face were generated using
        aGenE, aDirE and aGenV.
        """

    def GGDShapeIsToAdd(self, aNewShape: nanoocp.TopoDS.TopoDS_Shape, aNewSubShape: nanoocp.TopoDS.TopoDS_Shape, aGenS: nanoocp.TopoDS.TopoDS_Shape, aSubGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        Returns true if aNewSubShape (addressed by
        aSubGenS and aDirS) must be added in aNewShape
        (addressed by aGenS and aDirS).
        """

    def GDDShapeIsToAdd(self, aNewShape: nanoocp.TopoDS.TopoDS_Shape, aNewSubShape: nanoocp.TopoDS.TopoDS_Shape, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape, aSubDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        Returns true if aNewSubShape (addressed by
        aGenS and aSubDirS) must be added in aNewShape
        (addressed by aGenS and aDirS).
        """

    def SeparatedWires(self, aNewShape: nanoocp.TopoDS.TopoDS_Shape, aNewSubShape: nanoocp.TopoDS.TopoDS_Shape, aGenS: nanoocp.TopoDS.TopoDS_Shape, aSubGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        In some particular cases the topology of a
        generated face must be composed of independent
        closed wires, in this case this function returns
        true.
        """

    def HasShape(self, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        Returns true if aDirS and aGenS addresses a
        resulting Shape. In some specific cases the shape
        can be geometrically inexsistant, then this
        function returns false.
        """

    def IsInvariant(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Returns true if the geometry of aGenS is not
        modified by the trsf of the BRepSweep Trsf.
        """

    def SetContinuity(self, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> None:
        """
        Called to propagate the continuity of every vertex
        between two edges of the generating wire aGenS on
        the generated edge and faces.
        """

class BRepSweep_Translation(BRepSweep_Trsf):
    """
    Provides an algorithm to build object by
    translation sweep.
    """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, N: nanoocp.Sweep.Sweep_NumShape, L: nanoocp.TopLoc.TopLoc_Location, V: nanoocp.gp.gp_Vec, C: bool, Canonize: bool = True) -> None:
        """
        Creates a topology by translating <S> with the
        vector <V>. If C is true S Sucomponents are copied
        If Canonize is true then generated surfaces
        are attempted to be canonized in simple types
        """

    @overload
    def __init__(self, theOther: BRepSweep_Translation) -> None: ...

    def MakeEmptyVertex(self, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the vertex addressed by [aGenV,aDirV], with its
        geometric part, but without subcomponents.
        """

    def MakeEmptyDirectingEdge(self, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the edge addressed by [aGenV,aDirE], with its
        geometric part, but without subcomponents.
        """

    def MakeEmptyGeneratingEdge(self, aGenE: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the edge addressed by [aGenE,aDirV], with its
        geometric part, but without subcomponents.
        """

    def SetParameters(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewVertex: nanoocp.TopoDS.TopoDS_Shape, aGenF: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> None:
        """
        Sets the parameters of the new vertex on the new
        face. The new face and new vertex where generated
        from aGenF, aGenV and aDirV .
        """

    def SetDirectingParameter(self, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aNewVertex: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> None:
        """
        Sets the parameter of the new vertex on the new
        edge. The new edge and new vertex where generated
        from aGenV aDirE, and aDirV.
        """

    def SetGeneratingParameter(self, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aNewVertex: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> None:
        """
        Sets the parameter of the new vertex on the new
        edge. The new edge and new vertex where generated
        from aGenE, aGenV and aDirV .
        """

    def MakeEmptyFace(self, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the face addressed by [aGenS,aDirS], with
        its geometric part, but without subcomponents. The
        couple aGenS, aDirS can be a "generating face and
        a directing vertex" or "a generating edge and a
        directing edge".
        """

    def SetPCurve(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aGenF: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape, orien: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Sets the PCurve for a new edge on a new face. The
        new edge and the new face were generated using
        aGenF, aGenE and aDirV.
        """

    def SetGeneratingPCurve(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape, aDirV: nanoocp.Sweep.Sweep_NumShape, orien: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Sets the PCurve for a new edge on a new face. The
        new edge and the new face were generated using
        aGenE, aDirE and aDirV.
        """

    def SetDirectingPCurve(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape, orien: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Sets the PCurve for a new edge on a new face. The
        new edge and the new face were generated using
        aGenE, aDirE and aGenV.
        """

    def DirectSolid(self, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopAbs.TopAbs_Orientation:
        """
        Returns the Orientation of the shell in the solid
        generated by the face aGenS with the edge aDirS.
        It is REVERSED if the surface is swept in the
        direction of the normal.
        """

    def GGDShapeIsToAdd(self, aNewShape: nanoocp.TopoDS.TopoDS_Shape, aNewSubShape: nanoocp.TopoDS.TopoDS_Shape, aGenS: nanoocp.TopoDS.TopoDS_Shape, aSubGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        Returns true if aNewSubShape (addressed by
        aSubGenS and aDirS) must be added in aNewShape
        (addressed by aGenS and aDirS).
        """

    def GDDShapeIsToAdd(self, aNewShape: nanoocp.TopoDS.TopoDS_Shape, aNewSubShape: nanoocp.TopoDS.TopoDS_Shape, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape, aSubDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        Returns true if aNewSubShape (addressed by
        aGenS and aSubDirS) must be added in aNewShape
        (addressed by aGenS and aDirS).
        """

    def SeparatedWires(self, aNewShape: nanoocp.TopoDS.TopoDS_Shape, aNewSubShape: nanoocp.TopoDS.TopoDS_Shape, aGenS: nanoocp.TopoDS.TopoDS_Shape, aSubGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        In some particular cases the topology of a
        generated face must be composed of independent
        closed wires, in this case this function returns
        true.
        Here it always returns false.
        """

    def HasShape(self, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        Returns true if aDirS and aGenS addresses a
        resulting Shape. In some specific cases the shape
        can be geometrically inexsistant, then this
        function returns false.
        """

    def IsInvariant(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Returns always false because here the
        transformation is a translation.
        """

    def Vec(self) -> nanoocp.gp.gp_Vec:
        """
        Returns the Vector of the Prism, if it is an infinite
        prism the Vec is unitar.
        """

class BRepSweep_Prism:
    """
    Provides natural constructors to build BRepSweep
    translated swept Primitives.
    """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.gp.gp_Vec, Copy: bool = False, Canonize: bool = True) -> None:
        """
        Builds the prism of base S and vector V. If C is true,
        S is copied. If Canonize is true then generated surfaces
        are attempted to be canonized in simple types
        """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, D: nanoocp.gp.gp_Dir, Inf: bool = True, Copy: bool = False, Canonize: bool = True) -> None:
        """
        Builds a semi-infinite or an infinite prism of base S.
        If Copy is true S is copied. If Inf is true the prism
        is infinite, if Inf is false the prism is infinite in
        the direction D. If Canonize is true then generated surfaces
        are attempted to be canonized in simple types
        """

    @overload
    def __init__(self, theOther: BRepSweep_Prism) -> None: ...

    @overload
    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape attached to the prism."""

    @overload
    def Shape(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the TopoDS Shape generated with aGenS
        (subShape of the generating shape).
        """

    @overload
    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape of the bottom of the prism."""

    @overload
    def FirstShape(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the TopoDS Shape of the bottom of the prism.
        generated with aGenS (subShape of the generating
        shape).
        """

    @overload
    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape of the top of the prism."""

    @overload
    def LastShape(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the TopoDS Shape of the top of the prism.
        generated with aGenS (subShape of the generating
        shape).
        """

    def Vec(self) -> nanoocp.gp.gp_Vec:
        """
        Returns the Vector of the Prism, if it is an infinite
        prism the Vec is unitar.
        """

    def IsUsed(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Returns true if the
        aGenS is used in resulting shape
        """

    def GenIsUsed(self, theS: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Returns true if the shape, generated from theS
        is used in result shape
        """

class BRepSweep_Rotation(BRepSweep_Trsf):
    """
    Provides an algorithm to build object by
    Rotation sweep.
    """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, N: nanoocp.Sweep.Sweep_NumShape, L: nanoocp.TopLoc.TopLoc_Location, A: nanoocp.gp.gp_Ax1, D: float, C: bool) -> None:
        """
        Creates a topology by rotating <S> around A with the
        angle D.
        """

    @overload
    def __init__(self, theOther: BRepSweep_Rotation) -> None: ...

    def MakeEmptyVertex(self, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the vertex addressed by [aGenV,aDirV], with its
        geometric part, but without subcomponents.
        """

    def MakeEmptyDirectingEdge(self, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the edge addressed by [aGenV,aDirE], with its
        geometric part, but without subcomponents.
        """

    def MakeEmptyGeneratingEdge(self, aGenE: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the edge addressed by [aGenE,aDirV], with its
        geometric part, but without subcomponents.
        """

    def SetParameters(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewVertex: nanoocp.TopoDS.TopoDS_Shape, aGenF: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> None:
        """
        Sets the parameters of the new vertex on the new
        face. The new face and new vertex where generated
        from aGenF, aGenV and aDirV .
        """

    def SetDirectingParameter(self, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aNewVertex: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> None:
        """
        Sets the parameter of the new vertex on the new
        edge. The new edge and new vertex where generated
        from aGenV aDirE, and aDirV.
        """

    def SetGeneratingParameter(self, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aNewVertex: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape) -> None:
        """
        Sets the parameter of the new vertex on the new
        edge. The new edge and new vertex where generated
        from aGenE, aGenV and aDirV .
        """

    def MakeEmptyFace(self, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds the face addressed by [aGenS,aDirS], with
        its geometric part, but without subcomponents. The
        couple aGenS, aDirS can be a "generating face and
        a directing vertex" or "a generating edge and a
        directing edge".
        """

    def SetPCurve(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aGenF: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aDirV: nanoocp.Sweep.Sweep_NumShape, orien: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Sets the PCurve for a new edge on a new face. The
        new edge and the new face were generated using
        aGenF, aGenE and aDirV.
        """

    def SetGeneratingPCurve(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape, aDirV: nanoocp.Sweep.Sweep_NumShape, orien: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Sets the PCurve for a new edge on a new face. The
        new edge and the new face were generated using
        aGenE, aDirE and aDirV.
        """

    def SetDirectingPCurve(self, aNewFace: nanoocp.TopoDS.TopoDS_Shape, aNewEdge: nanoocp.TopoDS.TopoDS_Shape, aGenE: nanoocp.TopoDS.TopoDS_Shape, aGenV: nanoocp.TopoDS.TopoDS_Shape, aDirE: nanoocp.Sweep.Sweep_NumShape, orien: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Sets the PCurve for a new edge on a new face. The
        new edge and the new face were generated using
        aGenE, aDirE and aGenV.
        """

    def DirectSolid(self, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> nanoocp.TopAbs.TopAbs_Orientation:
        """
        Returns the Orientation of the shell in the solid
        generated by the face aGenS with the edge aDirS.
        It is REVERSED if the surface is swept in the
        direction of the normal.
        """

    def GGDShapeIsToAdd(self, aNewShape: nanoocp.TopoDS.TopoDS_Shape, aNewSubShape: nanoocp.TopoDS.TopoDS_Shape, aGenS: nanoocp.TopoDS.TopoDS_Shape, aSubGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        Returns true if aNewSubShape (addressed by
        aSubGenS and aDirS) must be added in aNewShape
        (addressed by aGenS and aDirS).
        """

    def GDDShapeIsToAdd(self, aNewShape: nanoocp.TopoDS.TopoDS_Shape, aNewSubShape: nanoocp.TopoDS.TopoDS_Shape, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape, aSubDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        Returns true if aNewSubShape (addressed by
        aGenS and aSubDirS) must be added in aNewShape
        (addressed by aGenS and aDirS).
        """

    def SeparatedWires(self, aNewShape: nanoocp.TopoDS.TopoDS_Shape, aNewSubShape: nanoocp.TopoDS.TopoDS_Shape, aGenS: nanoocp.TopoDS.TopoDS_Shape, aSubGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        In some particular cases the topology of a
        generated face must be composed of independent
        closed wires, in this case this function returns
        true. The only case in which the function may
        return true is a planar face in a closed revol.
        """

    def SplitShell(self, aNewShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        In some particular cases the topology of a
        generated Shell must be composed of independent
        closed Shells, in this case this function returns
        a Compound of independent Shells.
        """

    def HasShape(self, aGenS: nanoocp.TopoDS.TopoDS_Shape, aDirS: nanoocp.Sweep.Sweep_NumShape) -> bool:
        """
        Returns true if aDirS and aGenS addresses a
        resulting Shape. In some specific cases the shape
        can be geometrically inexsistant, then this
        function returns false.
        """

    def IsInvariant(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Returns true when the geometry of aGenS is not
        modified by the rotation.
        """

    def Axe(self) -> nanoocp.gp.gp_Ax1:
        """returns the axis"""

    def Angle(self) -> float:
        """returns the angle."""

class BRepSweep_Revol:
    """
    Provides natural constructors to build BRepSweep
    rotated swept Primitives.
    """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, A: nanoocp.gp.gp_Ax1, C: bool = False) -> None:
        """
        Builds the Revol of meridian S axis A and angle 2*Pi.
        If C is true S is copied.
        """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, A: nanoocp.gp.gp_Ax1, D: float, C: bool = False) -> None:
        """
        Builds the Revol of meridian S axis A and angle D. If
        C is true S is copied.
        """

    @overload
    def __init__(self, theOther: BRepSweep_Revol) -> None: ...

    @overload
    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape attached to the Revol."""

    @overload
    def Shape(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the TopoDS Shape generated with aGenS
        (subShape of the generating shape).
        """

    @overload
    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def FirstShape(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the first shape of the revol (coinciding with
        the generating shape).
        """

    @overload
    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape of the top of the prism."""

    @overload
    def LastShape(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the TopoDS Shape of the top of the prism.
        generated with aGenS (subShape of the generating
        shape).
        """

    def Axe(self) -> nanoocp.gp.gp_Ax1:
        """returns the axis"""

    def Angle(self) -> float:
        """returns the angle."""

    def IsUsed(self, aGenS: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns true if the aGenS is used in resulting Shape"""
