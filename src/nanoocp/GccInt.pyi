"""OCCT package GccInt (toolkit TKGeomAlgo)"""

import enum
from typing import overload

import nanoocp.Standard
import nanoocp.gp


class GccInt_IType(enum.IntEnum):
    GccInt_Lin = 0

    GccInt_Cir = 1

    GccInt_Ell = 2

    GccInt_Par = 3

    GccInt_Hpr = 4

    GccInt_Pnt = 5

GccInt_Lin: GccInt_IType = GccInt_IType.GccInt_Lin

GccInt_Cir: GccInt_IType = GccInt_IType.GccInt_Cir

GccInt_Ell: GccInt_IType = GccInt_IType.GccInt_Ell

GccInt_Par: GccInt_IType = GccInt_IType.GccInt_Par

GccInt_Hpr: GccInt_IType = GccInt_IType.GccInt_Hpr

GccInt_Pnt: GccInt_IType = GccInt_IType.GccInt_Pnt

class GccInt_Bisec(nanoocp.Standard.Standard_Transient):
    """
    The deferred class GccInt_Bisec is the root class for
    elementary bisecting loci between two simple geometric
    objects (i.e. circles, lines or points).
    Bisecting loci between two geometric objects are such
    that each of their points is at the same distance from the
    two geometric objects. It is typically a curve, such as a
    line, circle or conic.
    Generally there is more than one elementary object
    which is the solution to a bisecting loci problem: each
    solution is described with one elementary bisecting
    locus. For example, the bisectors of two secant straight
    lines are two perpendicular straight lines.
    The GccInt package provides concrete implementations
    of the following elementary derived bisecting loci:
    -   lines, circles, ellipses, hyperbolas and parabolas, and
    -   points (not used in this context).
    The GccAna package provides numerous algorithms for
    computing the bisecting loci between circles, lines or
    points, whose solutions are these types of elementary bisecting locus.
    """

    def ArcType(self) -> GccInt_IType:
        """
        Returns the type of bisecting object (line, circle,
        parabola, hyperbola, ellipse, point).
        """

    def Point(self) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the bisecting line when ArcType returns Pnt.
        An exception DomainError is raised if ArcType is not a Pnt.
        """

    def Line(self) -> nanoocp.gp.gp_Lin2d:
        """
        Returns the bisecting line when ArcType returns Lin.
        An exception DomainError is raised if ArcType is not a Lin.
        """

    def Circle(self) -> nanoocp.gp.gp_Circ2d:
        """
        Returns the bisecting line when ArcType returns Cir.
        An exception DomainError is raised if ArcType is not a Cir.
        """

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr2d:
        """
        Returns the bisecting line when ArcType returns Hpr.
        An exception DomainError is raised if ArcType is not a Hpr.
        """

    def Parabola(self) -> nanoocp.gp.gp_Parab2d:
        """
        Returns the bisecting line when ArcType returns Par.
        An exception DomainError is raised if ArcType is not a Par.
        """

    def Ellipse(self) -> nanoocp.gp.gp_Elips2d:
        """
        Returns the bisecting line when ArcType returns Ell.
        An exception DomainError is raised if ArcType is not an Ell.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GccInt_BCirc(GccInt_Bisec):
    """
    Describes a circle as a bisecting curve between two 2D
    geometric objects (such as circles or points).
    """

    @overload
    def __init__(self, Circ: nanoocp.gp.gp_Circ2d) -> None:
        """Constructs a bisecting curve whose geometry is the 2D circle Circ."""

    @overload
    def __init__(self, theOther: GccInt_BCirc) -> None: ...

    def Circle(self) -> nanoocp.gp.gp_Circ2d:
        """Returns a 2D circle which is the geometry of this bisecting curve."""

    def ArcType(self) -> GccInt_IType:
        """
        Returns GccInt_Cir, which is the type of any GccInt_BCirc bisecting curve.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GccInt_BElips(GccInt_Bisec):
    """
    Describes an ellipse as a bisecting curve between two
    2D geometric objects (such as circles or points).
    """

    @overload
    def __init__(self, Ellipse: nanoocp.gp.gp_Elips2d) -> None:
        """Constructs a bisecting curve whose geometry is the 2D ellipse Ellipse."""

    @overload
    def __init__(self, theOther: GccInt_BElips) -> None: ...

    def Ellipse(self) -> nanoocp.gp.gp_Elips2d:
        """Returns a 2D ellipse which is the geometry of this bisecting curve."""

    def ArcType(self) -> GccInt_IType:
        """
        Returns GccInt_Ell, which is the type of any GccInt_BElips bisecting curve.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GccInt_BHyper(GccInt_Bisec):
    """
    Describes a hyperbola as a bisecting curve between two
    2D geometric objects (such as circles or points).
    """

    @overload
    def __init__(self, Hyper: nanoocp.gp.gp_Hypr2d) -> None:
        """Constructs a bisecting curve whose geometry is the 2D hyperbola Hyper."""

    @overload
    def __init__(self, theOther: GccInt_BHyper) -> None: ...

    def Hyperbola(self) -> nanoocp.gp.gp_Hypr2d:
        """Returns a 2D hyperbola which is the geometry of this bisecting curve."""

    def ArcType(self) -> GccInt_IType:
        """
        Returns GccInt_Hpr, which is the type of any GccInt_BHyper bisecting curve.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GccInt_BLine(GccInt_Bisec):
    """
    Describes a line as a bisecting curve between two 2D
    geometric objects (such as lines, circles or points).
    """

    @overload
    def __init__(self, Line: nanoocp.gp.gp_Lin2d) -> None:
        """Constructs a bisecting line whose geometry is the 2D line Line."""

    @overload
    def __init__(self, theOther: GccInt_BLine) -> None: ...

    def Line(self) -> nanoocp.gp.gp_Lin2d:
        """Returns a 2D line which is the geometry of this bisecting line."""

    def ArcType(self) -> GccInt_IType:
        """
        Returns GccInt_Lin, which is the type of any GccInt_BLine bisecting line.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GccInt_BParab(GccInt_Bisec):
    """
    Describes a parabola as a bisecting curve between two
    2D geometric objects (such as lines, circles or points).
    """

    @overload
    def __init__(self, Parab: nanoocp.gp.gp_Parab2d) -> None:
        """Constructs a bisecting curve whose geometry is the 2D parabola Parab."""

    @overload
    def __init__(self, theOther: GccInt_BParab) -> None: ...

    def Parabola(self) -> nanoocp.gp.gp_Parab2d:
        """Returns a 2D parabola which is the geometry of this bisecting curve."""

    def ArcType(self) -> GccInt_IType:
        """
        Returns GccInt_Par, which is the type of any GccInt_BParab bisecting curve.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GccInt_BPoint(GccInt_Bisec):
    """
    Describes a point as a bisecting object between two 2D geometric objects.
    """

    @overload
    def __init__(self, Point: nanoocp.gp.gp_Pnt2d) -> None:
        """Constructs a bisecting object whose geometry is the 2D point Point."""

    @overload
    def __init__(self, theOther: GccInt_BPoint) -> None: ...

    def Point(self) -> nanoocp.gp.gp_Pnt2d:
        """Returns a 2D point which is the geometry of this bisecting object."""

    def ArcType(self) -> GccInt_IType:
        """
        Returns GccInt_Pnt, which is the type of any GccInt_BPoint bisecting object.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
