"""OCCT package TDataXtd (toolkit TKCAF)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.Quantity
import nanoocp.Standard
import nanoocp.TDF
import nanoocp.TDataStd
import nanoocp.TNaming
import nanoocp.TopoDS
import nanoocp.gp


class TDataXtd_GeometryEnum(enum.IntEnum):
    """
    The terms of this enumeration define the types of geometric shapes available.
    """

    TDataXtd_ANY_GEOM = 0

    TDataXtd_POINT = 1

    TDataXtd_LINE = 2

    TDataXtd_CIRCLE = 3

    TDataXtd_ELLIPSE = 4

    TDataXtd_SPLINE = 5

    TDataXtd_PLANE = 6

    TDataXtd_CYLINDER = 7

TDataXtd_ANY_GEOM: TDataXtd_GeometryEnum = TDataXtd_GeometryEnum.TDataXtd_ANY_GEOM

TDataXtd_POINT: TDataXtd_GeometryEnum = TDataXtd_GeometryEnum.TDataXtd_POINT

TDataXtd_LINE: TDataXtd_GeometryEnum = TDataXtd_GeometryEnum.TDataXtd_LINE

TDataXtd_CIRCLE: TDataXtd_GeometryEnum = TDataXtd_GeometryEnum.TDataXtd_CIRCLE

TDataXtd_ELLIPSE: TDataXtd_GeometryEnum = TDataXtd_GeometryEnum.TDataXtd_ELLIPSE

TDataXtd_SPLINE: TDataXtd_GeometryEnum = TDataXtd_GeometryEnum.TDataXtd_SPLINE

TDataXtd_PLANE: TDataXtd_GeometryEnum = TDataXtd_GeometryEnum.TDataXtd_PLANE

TDataXtd_CYLINDER: TDataXtd_GeometryEnum = TDataXtd_GeometryEnum.TDataXtd_CYLINDER

class TDataXtd_ConstraintEnum(enum.IntEnum):
    """
    The terms of this enumeration define the types
    of available constraint.
    ==================
    """

    TDataXtd_RADIUS = 0

    TDataXtd_DIAMETER = 1

    TDataXtd_MINOR_RADIUS = 2

    TDataXtd_MAJOR_RADIUS = 3

    TDataXtd_TANGENT = 4

    TDataXtd_PARALLEL = 5

    TDataXtd_PERPENDICULAR = 6

    TDataXtd_CONCENTRIC = 7

    TDataXtd_COINCIDENT = 8

    TDataXtd_DISTANCE = 9

    TDataXtd_ANGLE = 10

    TDataXtd_EQUAL_RADIUS = 11

    TDataXtd_SYMMETRY = 12

    TDataXtd_MIDPOINT = 13

    TDataXtd_EQUAL_DISTANCE = 14

    TDataXtd_FIX = 15

    TDataXtd_RIGID = 16

    TDataXtd_FROM = 17

    TDataXtd_AXIS = 18

    TDataXtd_MATE = 19

    TDataXtd_ALIGN_FACES = 20

    TDataXtd_ALIGN_AXES = 21

    TDataXtd_AXES_ANGLE = 22

    TDataXtd_FACES_ANGLE = 23

    TDataXtd_ROUND = 24

    TDataXtd_OFFSET = 25

TDataXtd_RADIUS: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_RADIUS

TDataXtd_DIAMETER: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_DIAMETER

TDataXtd_MINOR_RADIUS: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_MINOR_RADIUS

TDataXtd_MAJOR_RADIUS: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_MAJOR_RADIUS

TDataXtd_TANGENT: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_TANGENT

TDataXtd_PARALLEL: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_PARALLEL

TDataXtd_PERPENDICULAR: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_PERPENDICULAR

TDataXtd_CONCENTRIC: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_CONCENTRIC

TDataXtd_COINCIDENT: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_COINCIDENT

TDataXtd_DISTANCE: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_DISTANCE

TDataXtd_ANGLE: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_ANGLE

TDataXtd_EQUAL_RADIUS: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_EQUAL_RADIUS

TDataXtd_SYMMETRY: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_SYMMETRY

TDataXtd_MIDPOINT: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_MIDPOINT

TDataXtd_EQUAL_DISTANCE: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_EQUAL_DISTANCE

TDataXtd_FIX: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_FIX

TDataXtd_RIGID: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_RIGID

TDataXtd_FROM: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_FROM

TDataXtd_AXIS: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_AXIS

TDataXtd_MATE: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_MATE

TDataXtd_ALIGN_FACES: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_ALIGN_FACES

TDataXtd_ALIGN_AXES: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_ALIGN_AXES

TDataXtd_AXES_ANGLE: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_AXES_ANGLE

TDataXtd_FACES_ANGLE: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_FACES_ANGLE

TDataXtd_ROUND: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_ROUND

TDataXtd_OFFSET: TDataXtd_ConstraintEnum = TDataXtd_ConstraintEnum.TDataXtd_OFFSET

class TDataXtd:
    """
    This package defines extension of standard attributes for
    modelling (mainly for work with geometry).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataXtd) -> None: ...

    @staticmethod
    def IDList(anIDList: nanoocp.NCollection.NCollection_List[nanoocp.Standard.Standard_GUID]) -> None:
        """
        Appends to <anIDList> the list of the attributes
        IDs of this package. CAUTION: <anIDList> is NOT
        cleared before use.
        Print of TDataExt enumeration
        =============================
        """

    @overload
    @staticmethod
    def Print(GEO: TDataXtd_GeometryEnum) -> str:
        """
        Prints the name of the geometry dimension <GEO> as a String on
        the Stream <S> and returns <S>.
        """

    @overload
    @staticmethod
    def Print(CTR: TDataXtd_ConstraintEnum) -> str:
        """
        Prints the name of the constraint <CTR> as a String on
        the Stream <S> and returns <S>.
        """

class TDataXtd_Axis(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """
    The basis to define an axis attribute.

    Warning: Use TDataXtd_Geometry attribute to retrieve the
    gp_Lin of the Axis attribute
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataXtd_Axis) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        Returns the GUID for an axis.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label) -> TDataXtd_Axis:
        """
        Finds or creates an axis attribute defined by the label.
        In the case of a creation of an axis, a compatible
        named shape should already be associated with label.
        Exceptions
        Standard_NullObject if no compatible named shape is
        associated with the label.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, L: nanoocp.gp.gp_Lin) -> TDataXtd_Axis:
        """
        Axis methods
        ============
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class TDataXtd_Constraint(nanoocp.TDF.TDF_Attribute):
    """
    The groundwork to define constraint attributes.
    The constraint attribute contains the following sorts of data:
    -   Type whether the constraint attribute is a
    geometric constraint or a dimension
    -   Value the real number value of a numeric
    constraint such as an angle or a radius
    -   Geometries to identify the geometries
    underlying the topological attributes which
    define the constraint (up to 4)
    -   Plane for 2D constraints.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataXtd_Constraint) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns the GUID for constraints."""

    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label) -> TDataXtd_Constraint:
        """
        Finds or creates the 2D constraint attribute
        defined by the planar topological attribute plane
        and the label label.
        Constraint methods
        ==================
        """

    @overload
    def Set(self, type: TDataXtd_ConstraintEnum, G1: nanoocp.TNaming.TNaming_NamedShape | None) -> None:
        """
        Finds or creates the constraint attribute defined
        by the topological attribute G1 and the constraint type type.
        """

    @overload
    def Set(self, type: TDataXtd_ConstraintEnum, G1: nanoocp.TNaming.TNaming_NamedShape | None, G2: nanoocp.TNaming.TNaming_NamedShape | None) -> None:
        """
        Finds or creates the constraint attribute defined
        by the topological attributes G1 and G2, and by
        the constraint type type.
        """

    @overload
    def Set(self, type: TDataXtd_ConstraintEnum, G1: nanoocp.TNaming.TNaming_NamedShape | None, G2: nanoocp.TNaming.TNaming_NamedShape | None, G3: nanoocp.TNaming.TNaming_NamedShape | None) -> None:
        """
        Finds or creates the constraint attribute defined
        by the topological attributes G1, G2 and G3, and
        by the constraint type type.
        """

    @overload
    def Set(self, type: TDataXtd_ConstraintEnum, G1: nanoocp.TNaming.TNaming_NamedShape | None, G2: nanoocp.TNaming.TNaming_NamedShape | None, G3: nanoocp.TNaming.TNaming_NamedShape | None, G4: nanoocp.TNaming.TNaming_NamedShape | None) -> None:
        """
        Finds or creates the constraint attribute defined
        by the topological attributes G1, G2, G3 and G4,
        and by the constraint type type.
        methods to read constraint fields
        =================================
        """

    @overload
    def Verified(self) -> bool:
        """
        Returns true if this constraint attribute is valid.
        By default, true is returned.
        When the value of a dimension is changed or
        when a geometry is moved, false is returned
        until the solver sets it back to true.
        """

    @overload
    def Verified(self, status: bool) -> None:
        """
        Returns true if this constraint attribute defined by status is valid.
        By default, true is returned.
        When the value of a dimension is changed or
        when a geometry is moved, false is returned until
        the solver sets it back to true.
        If status is false, Verified is set to false.
        """

    def GetType(self) -> TDataXtd_ConstraintEnum:
        """
        Returns the type of constraint.
        This will be an element of the
        TDataXtd_ConstraintEnum enumeration.
        """

    def IsPlanar(self) -> bool:
        """
        Returns true if this constraint attribute is
        two-dimensional.
        """

    def GetPlane(self) -> nanoocp.TNaming.TNaming_NamedShape:
        """
        Returns the topological attribute of the plane
        used for planar - i.e., 2D - constraints.
        This plane is attached to another label.
        If the constraint is not planar, in other words, 3D,
        this function will return a null handle.
        """

    def IsDimension(self) -> bool:
        """
        Returns true if this constraint attribute is a
        dimension, and therefore has a value.
        """

    def GetValue(self) -> nanoocp.TDataStd.TDataStd_Real:
        """
        Returns the value of a dimension.
        This value is a reference to a TDataStd_Real attribute.
        If the attribute is not a dimension, this value will
        be 0. Use IsDimension to test this condition.
        """

    def NbGeometries(self) -> int:
        """
        Returns the number of geometry attributes in this constraint attribute.
        This number will be between 1 and 4.
        """

    def GetGeometry(self, Index: int) -> nanoocp.TNaming.TNaming_NamedShape:
        """
        Returns the integer index Index used to access
        the array of the constraint or stored geometries of a dimension
        Index has a value between 1 and 4.
        methods to write constraint fields (use builder)
        ==================================
        """

    def ClearGeometries(self) -> None:
        """
        Removes the geometries involved in the
        constraint or dimension from the array of
        topological attributes where they are stored.
        """

    def SetType(self, CTR: TDataXtd_ConstraintEnum) -> None:
        """Finds or creates the type of constraint CTR."""

    def SetPlane(self, plane: nanoocp.TNaming.TNaming_NamedShape | None) -> None:
        """
        Finds or creates the plane of the 2D constraint
        attribute, defined by the planar topological attribute plane.
        """

    def SetValue(self, V: nanoocp.TDataStd.TDataStd_Real | None) -> None:
        """
        Finds or creates the real number value V of the dimension constraint attribute.
        """

    def SetGeometry(self, Index: int, G: nanoocp.TNaming.TNaming_NamedShape | None) -> None:
        """
        Finds or creates the underlying geometry of the
        constraint defined by the topological attribute G
        and the integer index Index.
        """

    @overload
    def Inverted(self, status: bool) -> None: ...

    @overload
    def Inverted(self) -> bool: ...

    @overload
    def Reversed(self, status: bool) -> None: ...

    @overload
    def Reversed(self) -> bool: ...

    @staticmethod
    def CollectChildConstraints(aLabel: nanoocp.TDF.TDF_Label, TheList: nanoocp.NCollection.NCollection_List[nanoocp.TDF.TDF_Label]) -> None:
        """collects constraints on Childs for label <aLabel>"""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def References(self, DS: nanoocp.TDF.TDF_DataSet | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataXtd_Geometry(nanoocp.TDF.TDF_Attribute):
    """
    This class is used to model construction geometry.
    The specific geometric construction of the
    attribute is defined by an element of the
    enumeration TDataXtd_GeometryEnum.
    This attribute may also be used to qualify underlying
    geometry of the associated NamedShape. for
    Constructuion element by example.
    """

    @overload
    def __init__(self) -> None:
        """
        This and the next methods are used to retrieve underlying geometry of the NamedShape,
        even if no Geometry Attribute is associated.
        if not found or not compliant geometry return False.
        """

    @overload
    def __init__(self, theOther: TDataXtd_Geometry) -> None: ...

    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label) -> TDataXtd_Geometry:
        """
        API class methods
        =================
        Finds, or creates, a Geometry attribute defined by the label label.
        The default type of geometry is the value
        ANY_GEOM of the enumeration TDataXtd_GeometryEnum.
        To specify another value of this enumeration, use
        the function SetType.
        """

    @overload
    @staticmethod
    def Type(L: nanoocp.TDF.TDF_Label) -> TDataXtd_GeometryEnum:
        """
        Returns the label L used to define the type of
        geometric construction for the geometry attribute.
        """

    @overload
    @staticmethod
    def Type(S: nanoocp.TNaming.TNaming_NamedShape | None) -> TDataXtd_GeometryEnum:
        """
        Returns the topological attribute S used to define
        the type of geometric construction for the geometry attribute.
        """

    @overload
    @staticmethod
    def Point(L: nanoocp.TDF.TDF_Label, G: nanoocp.gp.gp_Pnt) -> bool:
        """Returns the point attribute defined by the label L and the point G."""

    @overload
    @staticmethod
    def Point(S: nanoocp.TNaming.TNaming_NamedShape | None, G: nanoocp.gp.gp_Pnt) -> bool:
        """
        Returns the point attribute defined by the topological attribute S and the point G.
        """

    @overload
    @staticmethod
    def Axis(L: nanoocp.TDF.TDF_Label, G: nanoocp.gp.gp_Ax1) -> bool:
        """Returns the axis attribute defined by the label L and the axis G."""

    @overload
    @staticmethod
    def Axis(S: nanoocp.TNaming.TNaming_NamedShape | None, G: nanoocp.gp.gp_Ax1) -> bool:
        """
        Returns the axis attribute defined by the topological attribute S and the axis G.
        """

    @overload
    @staticmethod
    def Line(L: nanoocp.TDF.TDF_Label, G: nanoocp.gp.gp_Lin) -> bool:
        """Returns the line attribute defined by the label L and the line G."""

    @overload
    @staticmethod
    def Line(S: nanoocp.TNaming.TNaming_NamedShape | None, G: nanoocp.gp.gp_Lin) -> bool:
        """
        Returns the line attribute defined by the topological attribute S and the line G.
        """

    @overload
    @staticmethod
    def Circle(L: nanoocp.TDF.TDF_Label, G: nanoocp.gp.gp_Circ) -> bool:
        """Returns the circle attribute defined by the label L and the circle G."""

    @overload
    @staticmethod
    def Circle(S: nanoocp.TNaming.TNaming_NamedShape | None, G: nanoocp.gp.gp_Circ) -> bool:
        """
        Returns the circle attribute defined by the topological attribute S and the circle G.
        """

    @overload
    @staticmethod
    def Ellipse(L: nanoocp.TDF.TDF_Label, G: nanoocp.gp.gp_Elips) -> bool:
        """
        Returns the ellipse attribute defined by the label L and the ellipse G.
        """

    @overload
    @staticmethod
    def Ellipse(S: nanoocp.TNaming.TNaming_NamedShape | None, G: nanoocp.gp.gp_Elips) -> bool:
        """
        Returns the ellipse attribute defined by the
        topological attribute S and the ellipse G.
        """

    @overload
    @staticmethod
    def Plane(L: nanoocp.TDF.TDF_Label, G: nanoocp.gp.gp_Pln) -> bool:
        """Returns the plane attribute defined by the label L and the plane G."""

    @overload
    @staticmethod
    def Plane(S: nanoocp.TNaming.TNaming_NamedShape | None, G: nanoocp.gp.gp_Pln) -> bool:
        """
        Returns the plane attribute defined by the
        topological attribute S and the plane G.
        """

    @overload
    @staticmethod
    def Cylinder(L: nanoocp.TDF.TDF_Label, G: nanoocp.gp.gp_Cylinder) -> bool:
        """
        Returns the cylinder attribute defined by the label L and the cylinder G.
        """

    @overload
    @staticmethod
    def Cylinder(S: nanoocp.TNaming.TNaming_NamedShape | None, G: nanoocp.gp.gp_Cylinder) -> bool:
        """
        Returns the cylinder attribute defined by the
        topological attribute S and the cylinder G.
        """

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns the GUID for geometry attributes."""

    def SetType(self, T: TDataXtd_GeometryEnum) -> None:
        """
        Returns the type of geometric construction T of this attribute.
        T will be a value of the enumeration TDataXtd_GeometryEnum.
        """

    def GetType(self) -> TDataXtd_GeometryEnum:
        """Returns the type of geometric construction."""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataXtd_Pattern(nanoocp.TDF.TDF_Attribute):
    """a general pattern model"""

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the attribute."""

    def PatternID(self) -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the attribute."""

    def NbTrsfs(self) -> int:
        """Give the number of transformation"""

    def ComputeTrsfs(self, Trsfs: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Trsf]) -> None:
        """Give the transformations"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataXtd_PatternStd(TDataXtd_Pattern):
    """
    to create a PatternStd
    (LinearPattern, CircularPattern, RectangularPattern,
    RadialCircularPattern, MirrorPattern)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataXtd_PatternStd) -> None: ...

    @staticmethod
    def GetPatternID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label) -> TDataXtd_PatternStd:
        """Find, or create, a PatternStd attribute"""

    @overload
    def Signature(self, signature: int) -> None: ...

    @overload
    def Signature(self) -> int: ...

    @overload
    def Axis1(self, Axis1: nanoocp.TNaming.TNaming_NamedShape | None) -> None: ...

    @overload
    def Axis1(self) -> nanoocp.TNaming.TNaming_NamedShape: ...

    @overload
    def Axis2(self, Axis2: nanoocp.TNaming.TNaming_NamedShape | None) -> None: ...

    @overload
    def Axis2(self) -> nanoocp.TNaming.TNaming_NamedShape: ...

    @overload
    def Axis1Reversed(self, Axis1Reversed: bool) -> None: ...

    @overload
    def Axis1Reversed(self) -> bool: ...

    @overload
    def Axis2Reversed(self, Axis2Reversed: bool) -> None: ...

    @overload
    def Axis2Reversed(self) -> bool: ...

    @overload
    def Value1(self, value: nanoocp.TDataStd.TDataStd_Real | None) -> None: ...

    @overload
    def Value1(self) -> nanoocp.TDataStd.TDataStd_Real: ...

    @overload
    def Value2(self, value: nanoocp.TDataStd.TDataStd_Real | None) -> None: ...

    @overload
    def Value2(self) -> nanoocp.TDataStd.TDataStd_Real: ...

    @overload
    def NbInstances1(self, NbInstances1: nanoocp.TDataStd.TDataStd_Integer | None) -> None: ...

    @overload
    def NbInstances1(self) -> nanoocp.TDataStd.TDataStd_Integer: ...

    @overload
    def NbInstances2(self, NbInstances2: nanoocp.TDataStd.TDataStd_Integer | None) -> None: ...

    @overload
    def NbInstances2(self) -> nanoocp.TDataStd.TDataStd_Integer: ...

    @overload
    def Mirror(self, plane: nanoocp.TNaming.TNaming_NamedShape | None) -> None: ...

    @overload
    def Mirror(self) -> nanoocp.TNaming.TNaming_NamedShape: ...

    def NbTrsfs(self) -> int: ...

    def ComputeTrsfs(self, Trsfs: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Trsf]) -> None: ...

    def PatternID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def References(self, aDataSet: nanoocp.TDF.TDF_DataSet | None) -> None: ...

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataXtd_Placement(nanoocp.TDataStd.TDataStd_GenericEmpty):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataXtd_Placement) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============
        """

    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label) -> TDataXtd_Placement:
        """
        Find, or create, a Placement attribute.
        Placement attribute is returned.
        Placement methods
        =================
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class TDataXtd_Plane(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """
    The basis to define a plane attribute.
    Warning: Use TDataXtd_Geometry attribute to retrieve the
    gp_Pln of the Plane attribute
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataXtd_Plane) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============

        Returns the GUID for plane attributes.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label) -> TDataXtd_Plane:
        """
        Finds or creates the plane attribute defined by
        the label label.
        Warning
        If you are creating the attribute with this syntax, a
        planar face should already be associated with label.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, P: nanoocp.gp.gp_Pln) -> TDataXtd_Plane:
        """
        Finds, or creates, a Plane attribute and sets <P> as
        generated the associated NamedShape.
        Plane methods
        =============
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class TDataXtd_Point(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """
    The basis to define a point attribute.
    The topological attribute must contain a vertex.
    You use this class to create reference points in a design.

    Warning: Use TDataXtd_Geometry attribute to retrieve the
    gp_Pnt of the Point attribute
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataXtd_Point) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        class methods
        =============

        Returns the GUID for point attributes.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label) -> TDataXtd_Point:
        """
        Sets the label Label as a point attribute.
        If no object is found, a point attribute is created.
        """

    @overload
    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, P: nanoocp.gp.gp_Pnt) -> TDataXtd_Point:
        """
        Sets the label Label as a point attribute containing the point P.
        If no object is found, a point attribute is created.
        Point methods
        =============
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class TDataXtd_Position(nanoocp.TDF.TDF_Attribute):
    """Position of a Label"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataXtd_Position) -> None: ...

    @overload
    @staticmethod
    def Set(aLabel: nanoocp.TDF.TDF_Label, aPos: nanoocp.gp.gp_Pnt) -> None:
        """
        Create if not found the TDataXtd_Position attribute set its position to <aPos>
        """

    @overload
    @staticmethod
    def Set(aLabel: nanoocp.TDF.TDF_Label) -> TDataXtd_Position:
        """
        Find an existing, or create an empty, Position.
        the Position attribute is returned.
        """

    @staticmethod
    def Get(aLabel: nanoocp.TDF.TDF_Label, aPos: nanoocp.gp.gp_Pnt) -> bool:
        """
        Search label <aLabel) for the TDataXtd_Position attribute and get its position
        if found returns True
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the attribute."""

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the attribute."""

    def Restore(self, anAttribute: nanoocp.TDF.TDF_Attribute | None) -> None:
        """
        Restores the contents from <anAttribute> into this
        one. It is used when aborting a transaction.
        """

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """
        Returns an new empty attribute from the good end
        type. It is used by the copy algorithm.
        """

    def Paste(self, intoAttribute: nanoocp.TDF.TDF_Attribute | None, aRelocTationable: nanoocp.TDF.TDF_RelocationTable | None) -> None:
        """
        This method is different from the "Copy" one,
        because it is used when copying an attribute from
        a source structure into a target structure. This
        method pastes the current attribute to the label
        corresponding to the insertor. The pasted
        attribute may be a brand new one or a new version
        of the previous one.
        """

    def GetPosition(self) -> nanoocp.gp.gp_Pnt: ...

    def SetPosition(self, aPos: nanoocp.gp.gp_Pnt) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TDataXtd_Presentation(nanoocp.TDF.TDF_Attribute):
    """
    Attribute containing parameters of presentation of the shape,
    e.g. the shape attached to the same label and displayed using
    TPrsStd tools (see TPrsStd_AISPresentation).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: TDataXtd_Presentation) -> None: ...

    @staticmethod
    def Set(theLabel: nanoocp.TDF.TDF_Label, theDriverId: nanoocp.Standard.Standard_GUID) -> TDataXtd_Presentation:
        """
        Create if not found the TDataXtd_Presentation attribute and set its driver GUID
        """

    @staticmethod
    def Unset(theLabel: nanoocp.TDF.TDF_Label) -> None:
        """Remove attribute of this type from the label"""

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the attribute."""

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the attribute."""

    def Restore(self, anAttribute: nanoocp.TDF.TDF_Attribute | None) -> None:
        """
        Restores the contents from <anAttribute> into this
        one. It is used when aborting a transaction.
        """

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """
        Returns an new empty attribute from the good end
        type. It is used by the copy algorithm.
        """

    def Paste(self, intoAttribute: nanoocp.TDF.TDF_Attribute | None, aRelocTationable: nanoocp.TDF.TDF_RelocationTable | None) -> None:
        """
        This method is different from the "Copy" one,
        because it is used when copying an attribute from
        a source structure into a target structure. This
        method pastes the current attribute to the label
        corresponding to the insertor. The pasted
        attribute may be a brand new one or a new version
        of the previous one.
        """

    def BackupCopy(self) -> nanoocp.TDF.TDF_Attribute: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def GetDriverGUID(self) -> nanoocp.Standard.Standard_GUID:
        """
        Returns the GUID of the driver managing display of associated AIS object
        """

    def SetDriverGUID(self, theGUID: nanoocp.Standard.Standard_GUID) -> None:
        """Sets the GUID of the driver managing display of associated AIS object"""

    def IsDisplayed(self) -> bool: ...

    def HasOwnMaterial(self) -> bool: ...

    def HasOwnTransparency(self) -> bool: ...

    def HasOwnColor(self) -> bool: ...

    def HasOwnWidth(self) -> bool: ...

    def HasOwnMode(self) -> bool: ...

    def HasOwnSelectionMode(self) -> bool: ...

    def SetDisplayed(self, theIsDisplayed: bool) -> None: ...

    def SetMaterialIndex(self, theMaterialIndex: int) -> None: ...

    def SetTransparency(self, theValue: float) -> None: ...

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_NameOfColor) -> None: ...

    def SetWidth(self, theWidth: float) -> None: ...

    def SetMode(self, theMode: int) -> None: ...

    def GetNbSelectionModes(self) -> int:
        """
        Returns the number of selection modes of the attribute.
        It starts with 1 .. GetNbSelectionModes().
        """

    def SetSelectionMode(self, theSelectionMode: int, theTransaction: bool = True) -> None:
        """
        Sets selection mode.
        If "theTransaction" flag is OFF, modification of the attribute doesn't influence the
        transaction mechanism (the attribute doesn't participate in undo/redo because of this
        modification). Certainly, if any other data of the attribute is modified (display mode, color,
        ...), the attribute will be included into undo/redo.
        """

    def AddSelectionMode(self, theSelectionMode: int, theTransaction: bool = True) -> None: ...

    def MaterialIndex(self) -> int: ...

    def Transparency(self) -> float: ...

    def Color(self) -> nanoocp.Quantity.Quantity_NameOfColor: ...

    def Width(self) -> float: ...

    def Mode(self) -> int: ...

    def SelectionMode(self, index: int = 1) -> int: ...

    def UnsetMaterial(self) -> None: ...

    def UnsetTransparency(self) -> None: ...

    def UnsetColor(self) -> None: ...

    def UnsetWidth(self) -> None: ...

    def UnsetMode(self) -> None: ...

    def UnsetSelectionMode(self) -> None: ...

    @staticmethod
    def getColorNameFromOldEnum(theOld: int) -> nanoocp.Quantity.Quantity_NameOfColor:
        """
        Convert values of old Quantity_NameOfColor to new enumeration for reading old documents
        after #0030969 (Coding Rules - refactor Quantity_Color.cxx color table definition).
        """

    @staticmethod
    def getOldColorNameFromNewEnum(theNew: nanoocp.Quantity.Quantity_NameOfColor) -> int:
        """
        Convert Quantity_NameOfColor to old enumeration value for writing documents in compatible
        format.
        """

class TDataXtd_Shape(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """
    A Shape is associated in the framework with :
    a NamedShape attribute
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TDataXtd_Shape) -> None: ...

    @staticmethod
    def Find(current: nanoocp.TDF.TDF_Label) -> tuple[bool, TDataXtd_Shape]:
        """
        class methods
        =============
        try to retrieve a Shape attribute at <current> label
        or in fathers label of <current>. Returns True if
        found and set <S>.
        """

    @staticmethod
    def New(label: nanoocp.TDF.TDF_Label) -> TDataXtd_Shape:
        """
        Find, or create, a Shape attribute. the Shape attribute
        is returned. Raises if <label> has attribute.
        """

    @staticmethod
    def Set(label: nanoocp.TDF.TDF_Label, shape: nanoocp.TopoDS.TopoDS_Shape) -> TDataXtd_Shape:
        """
        Create or update associated NamedShape attribute. the
        Shape attribute is returned.
        """

    @staticmethod
    def Get(label: nanoocp.TDF.TDF_Label) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        the Shape from associated NamedShape attribute
        is returned.
        """

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """
        Shape methods
        =============
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def References(self, DS: nanoocp.TDF.TDF_DataSet | None) -> None: ...

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class TDataXtd_Triangulation(nanoocp.TDF.TDF_Attribute):
    """
    An Ocaf attribute containing a mesh (Poly_Triangulation).
    It duplicates all methods from Poly_Triangulation.
    It is highly recommended to modify the mesh through the methods of this attribute,
    but not directly via the underlying Poly_Triangulation object.
    In this case Undo/Redo will work fine and robust.
    """

    @overload
    def __init__(self) -> None:
        """
        A constructor.
        Don't use it directly,
        use please the static method Set(),
        which returns the attribute attached to a label.
        """

    @overload
    def __init__(self, theOther: TDataXtd_Triangulation) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns the ID of the triangulation attribute."""

    @overload
    @staticmethod
    def Set_s(theLabel: nanoocp.TDF.TDF_Label) -> TDataXtd_Triangulation:
        """Finds or creates a triangulation attribute."""

    @overload
    @staticmethod
    def Set_s(theLabel: nanoocp.TDF.TDF_Label, theTriangulation: nanoocp.Poly.Poly_Triangulation | None) -> TDataXtd_Triangulation:
        """
        Finds or creates a triangulation attribute.
        Initializes the attribute by a Poly_Triangulation object.
        """

    def Set(self, theTriangulation: nanoocp.Poly.Poly_Triangulation | None) -> None:
        """Sets the triangulation."""

    def Get(self) -> nanoocp.Poly.Poly_Triangulation:
        """Returns the underlying triangulation."""

    @overload
    def Deflection(self) -> float:
        """Returns the deflection of this triangulation."""

    @overload
    def Deflection(self, theDeflection: float) -> None:
        """
        Sets the deflection of this triangulation to theDeflection.
        See more on deflection in Polygon2D
        """

    def RemoveUVNodes(self) -> None:
        """Deallocates the UV nodes."""

    def NbNodes(self) -> int:
        """@return the number of nodes for this triangulation."""

    def NbTriangles(self) -> int:
        """@return the number of triangles for this triangulation."""

    def HasUVNodes(self) -> bool:
        """
        @return true if 2D nodes are associated with 3D nodes for this triangulation.
        """

    def Node(self, theIndex: int) -> nanoocp.gp.gp_Pnt:
        """
        @return node at the given index.
        Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """

    def SetNode(self, theIndex: int, theNode: nanoocp.gp.gp_Pnt) -> None:
        """
        The method differs from Poly_Triangulation!
        Sets a node at the given index.
        Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """

    def UVNode(self, theIndex: int) -> nanoocp.gp.gp_Pnt2d:
        """
        @return UVNode at the given index.
        Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """

    def SetUVNode(self, theIndex: int, theUVNode: nanoocp.gp.gp_Pnt2d) -> None:
        """
        The method differs from Poly_Triangulation!
        Sets a UVNode at the given index.
        Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """

    def Triangle(self, theIndex: int) -> nanoocp.Poly.Poly_Triangle:
        """
        @return triangle at the given index.
        Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbTriangles.
        """

    def SetTriangle(self, theIndex: int, theTriangle: nanoocp.Poly.Poly_Triangle) -> None:
        """
        The method differs from Poly_Triangulation!
        Sets a triangle at the given index.
        Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbTriangles.
        """

    def SetNormal(self, theIndex: int, theNormal: nanoocp.gp.gp_Dir) -> None:
        """
        Changes normal at the given index.
        Raises Standard_OutOfRange exception.
        """

    def HasNormals(self) -> bool:
        """Returns true if nodal normals are defined."""

    def Normal(self, theIndex: int) -> nanoocp.gp.gp_Dir:
        """
        @return normal at the given index.
        Raises Standard_OutOfRange exception.
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Inherited attribute methods"""

    def Restore(self, theAttribute: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
TDataXtd_Array1OfTrsf = nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Trsf]
