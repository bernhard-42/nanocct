"""OCCT package BRepProj (toolkit TKBool)"""

from typing import overload

import nanoocp.TopoDS
import nanoocp.gp


class BRepProj_Projection:
    """
    The Projection class provides conical and
    cylindrical projections of Edge or Wire on
    a Shape from TopoDS. The result will be a Edge
    or Wire from TopoDS.
    """

    @overload
    def __init__(self, Wire: nanoocp.TopoDS.TopoDS_Shape, Shape: nanoocp.TopoDS.TopoDS_Shape, D: nanoocp.gp.gp_Dir) -> None:
        """Makes a Cylindrical projection of Wire om Shape"""

    @overload
    def __init__(self, Wire: nanoocp.TopoDS.TopoDS_Shape, Shape: nanoocp.TopoDS.TopoDS_Shape, P: nanoocp.gp.gp_Pnt) -> None:
        """Makes a Conical projection of Wire om Shape"""

    @overload
    def __init__(self, theOther: BRepProj_Projection) -> None: ...

    def __iter__(self) -> BRepProj_Projection:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Python addition: see __iter__."""

    def IsDone(self) -> bool:
        """returns False if the section failed"""

    def Init(self) -> None:
        """Resets the iterator by resulting wires."""

    def More(self) -> bool:
        """Returns True if there is a current result wire"""

    def Next(self) -> None:
        """Move to the next result wire."""

    def Current(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns the current result wire."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Compound:
        """Returns the complete result as compound of wires."""
