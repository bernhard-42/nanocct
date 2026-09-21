"""OCCT package BRepPrimAPI (toolkit TKPrim)"""

from typing import overload

import nanoocp.BRepBuilderAPI
import nanoocp.BRepPrim
import nanoocp.BRepSweep
import nanoocp.Geom
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.TopoDS
import nanoocp.gp


class BRepPrimAPI_MakeBox(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    Describes functions to build parallelepiped boxes.
    A MakeBox object provides a framework for:
    -   defining the construction of a box,
    -   implementing the construction algorithm, and
    -   consulting the result.
    Constructs a box such that its sides are parallel to the axes of
    -   the global coordinate system, or
    -   the local coordinate system Axis. and
    -   with a corner at (0, 0, 0) and of size (dx, dy, dz), or
    -   with a corner at point P and of size (dx, dy, dz), or
    -   with corners at points P1 and P2.
    Exceptions
    Standard_DomainError if: dx, dy, dz are less than or equal to
    Precision::Confusion(), or
    -   the vector joining the points P1 and P2 has a
    component projected onto the global coordinate
    system less than or equal to Precision::Confusion().
    In these cases, the box would be flat.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt) -> None:
        """Make a box with corners P1,P2."""

    @overload
    def __init__(self, dx: float, dy: float, dz: float) -> None:
        """Make a box with a corner at 0,0,0 and the other dx,dy,dz"""

    @overload
    def __init__(self, P: nanoocp.gp.gp_Pnt, dx: float, dy: float, dz: float) -> None:
        """Make a box with a corner at P and size dx, dy, dz."""

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, dx: float, dy: float, dz: float) -> None:
        """
        Make a box with Ax2 (the left corner and the axis) and size dx, dy, dz.
        """

    @overload
    def __init__(self, theOther: BRepPrimAPI_MakeBox) -> None: ...

    @overload
    def Init(self, theDX: float, theDY: float, theDZ: float) -> None:
        """Init a box with a corner at 0,0,0 and the other theDX, theDY, theDZ"""

    @overload
    def Init(self, thePnt: nanoocp.gp.gp_Pnt, theDX: float, theDY: float, theDZ: float) -> None:
        """Init a box with a corner at thePnt and size theDX, theDY, theDZ."""

    @overload
    def Init(self, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt) -> None:
        """Init a box with corners thePnt1, thePnt2."""

    @overload
    def Init(self, theAxes: nanoocp.gp.gp_Ax2, theDX: float, theDY: float, theDZ: float) -> None:
        """
        Init a box with Ax2 (the left corner and the theAxes) and size theDX, theDY, theDZ.
        """

    def Wedge(self) -> nanoocp.BRepPrim.BRepPrim_Wedge:
        """Returns the internal algorithm."""

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Stores the solid in myShape."""

    def Shell(self) -> nanoocp.TopoDS.TopoDS_Shell:
        """Returns the constructed box as a shell."""

    def Solid(self) -> nanoocp.TopoDS.TopoDS_Solid:
        """Returns the constructed box as a solid."""

    def BottomFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns ZMin face"""

    def BackFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns XMin face"""

    def FrontFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns XMax face"""

    def LeftFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns YMin face"""

    def RightFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns YMax face"""

    def TopFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns ZMax face"""

class BRepPrimAPI_MakeOneAxis(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    The abstract class MakeOneAxis is the root class of
    algorithms used to construct rotational primitives.
    """

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Stores the solid in myShape."""

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns the lateral face of the rotational primitive."""

    def Shell(self) -> nanoocp.TopoDS.TopoDS_Shell:
        """Returns the constructed rotational primitive as a shell."""

    def Solid(self) -> nanoocp.TopoDS.TopoDS_Solid:
        """Returns the constructed rotational primitive as a solid."""

class BRepPrimAPI_MakeCone(BRepPrimAPI_MakeOneAxis):
    """
    Describes functions to build cones or portions of cones.
    A MakeCone object provides a framework for:
    -   defining the construction of a cone,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, R1: float, R2: float, H: float) -> None:
        """
        Make a cone.
        @param[in] R1  cone bottom radius, may be null (z = 0)
        @param[in] R2  cone top radius, may be null (z = H)
        @param[in] H   cone height
        """

    @overload
    def __init__(self, R1: float, R2: float, H: float, angle: float) -> None:
        """
        Make a cone.
        @param[in] R1     cone bottom radius, may be null (z = 0)
        @param[in] R2     cone top radius, may be null (z = H)
        @param[in] H      cone height
        @param[in] angle  angle to create a part cone
        """

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, R1: float, R2: float, H: float) -> None:
        """
        Make a cone.
        @param[in] axes  coordinate system for the construction of the cone
        @param[in] R1    cone bottom radius, may be null (z = 0)
        @param[in] R2    cone top radius, may be null (z = H)
        @param[in] H     cone height
        """

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, R1: float, R2: float, H: float, angle: float) -> None:
        """
        Make a cone of height H radius R1 in the plane z =
        0, R2 in the plane Z = H. R1 and R2 may be null.
        Take a section of <angle>
        Constructs a cone, or a portion of a cone, of height H,
        and radius R1 in the plane z = 0 and R2 in the plane
        z = H. The result is a sharp cone if R1 or R2 is equal to 0.
        The cone is constructed about the "Z Axis" of either:
        -   the global coordinate system, or
        -   the local coordinate system Axes.
        It is limited in these coordinate systems as follows:
        -   in the v parametric direction (the Z coordinate), by
        the two parameter values 0 and H,
        -   and in the u parametric direction (defined by the
        angle of rotation around the Z axis), in the case of a
        portion of a cone, by the two parameter values 0 and
        angle. Angle is given in radians.
        The resulting shape is composed of:
        -   a lateral conical face
        -   two planar faces in the planes z = 0 and z = H,
        or only one planar face in one of these two planes if a
        radius value is null (in the case of a complete cone,
        these faces are circles), and
        -   and in the case of a portion of a cone, two planar
        faces to close the shape. (either two parallelograms or
        two triangles, in the planes u = 0 and u = angle).
        Exceptions
        Standard_DomainError if:
        -   H is less than or equal to Precision::Confusion(), or
        -   the half-angle at the apex of the cone, defined by
        R1, R2 and H, is less than Precision::Confusion()/H, or greater than
        (Pi/2)-Precision::Confusion()/H.f
        """

    @overload
    def __init__(self, theOther: BRepPrimAPI_MakeCone) -> None: ...

    def Cone(self) -> nanoocp.BRepPrim.BRepPrim_Cone:
        """Returns the algorithm."""

class BRepPrimAPI_MakeCylinder(BRepPrimAPI_MakeOneAxis):
    """
    Describes functions to build cylinders or portions of cylinders.
    A MakeCylinder object provides a framework for:
    -   defining the construction of a cylinder,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, R: float, H: float) -> None:
        """
        Make a cylinder.
        @param[in] R  cylinder radius
        @param[in] H  cylinder height
        """

    @overload
    def __init__(self, R: float, H: float, Angle: float) -> None:
        """
        Make a cylinder (part cylinder).
        @param[in] R      cylinder radius
        @param[in] H      cylinder height
        @param[in] Angle  defines the missing portion of the cylinder
        """

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, R: float, H: float) -> None:
        """
        Make a cylinder of radius R and length H.
        @param[in] Axes  coordinate system for the construction of the cylinder
        @param[in] R     cylinder radius
        @param[in] H     cylinder height
        """

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, R: float, H: float, Angle: float) -> None:
        """
        Make a cylinder of radius R and length H with
        angle H.
        Constructs
        -   a cylinder of radius R and height H, or
        -   a portion of cylinder of radius R and height H, and of
        the angle Angle defining the missing portion of the cylinder.
        The cylinder is constructed about the "Z Axis" of either:
        -   the global coordinate system, or
        -   the local coordinate system Axes.
        It is limited in this coordinate system as follows:
        -   in the v parametric direction (the Z axis), by the two
        parameter values 0 and H,
        -   and in the u parametric direction (the rotation angle
        around the Z Axis), in the case of a portion of a
        cylinder, by the two parameter values 0 and Angle.
        Angle is given in radians.
        The resulting shape is composed of:
        -   a lateral cylindrical face,
        -   two planar faces in the planes z = 0 and z = H
        (in the case of a complete cylinder, these faces are circles), and
        -   in case of a portion of a cylinder, two additional
        planar faces to close the shape.(two rectangles in the
        planes u = 0 and u = Angle).
        Exceptions Standard_DomainError if:
        -   R is less than or equal to Precision::Confusion(), or
        -   H is less than or equal to Precision::Confusion().
        """

    @overload
    def __init__(self, theOther: BRepPrimAPI_MakeCylinder) -> None: ...

    def Cylinder(self) -> nanoocp.BRepPrim.BRepPrim_Cylinder:
        """Returns the algorithm."""

class BRepPrimAPI_MakeHalfSpace(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    Describes functions to build half-spaces.
    A half-space is an infinite solid, limited by a surface. It
    is built from a face or a shell, which bounds it, and with
    a reference point, which specifies the side of the
    surface where the matter of the half-space is located.
    A half-space is a tool commonly used in topological
    operations to cut another shape.
    A MakeHalfSpace object provides a framework for:
    -   defining and implementing the construction of a half-space, and
    -   consulting the result.
    """

    @overload
    def __init__(self, Face: nanoocp.TopoDS.TopoDS_Face, RefPnt: nanoocp.gp.gp_Pnt) -> None:
        """Make a HalfSpace defined with a Face and a Point."""

    @overload
    def __init__(self, Shell: nanoocp.TopoDS.TopoDS_Shell, RefPnt: nanoocp.gp.gp_Pnt) -> None:
        """Make a HalfSpace defined with a Shell and a Point."""

    @overload
    def __init__(self, theOther: BRepPrimAPI_MakeHalfSpace) -> None: ...

    def Solid(self) -> nanoocp.TopoDS.TopoDS_Solid:
        """Returns the constructed half-space as a solid."""

class BRepPrimAPI_MakeSweep(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    The abstract class MakeSweep is
    the root class of swept primitives.
    Sweeps are objects you obtain by sweeping a profile along a path.
    The profile can be any topology and the path is usually a curve or
    a wire. The profile generates objects according to the following rules:
    -      Vertices generate Edges
    -      Edges generate Faces.
    -      Wires generate Shells.
    -      Faces generate Solids.
    -      Shells generate Composite Solids.
    You are not allowed to sweep Solids and Composite Solids.
    Two kinds of sweeps are implemented in the BRepPrimAPI package:
    -      The linear sweep called a Prism
    -      The rotational sweep called a Revol
    Swept constructions along complex profiles such as BSpline curves
    are also available in the BRepOffsetAPI package..
    """

    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape of the bottom of the sweep."""

    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape of the top of the sweep."""

class BRepPrimAPI_MakePrism(BRepPrimAPI_MakeSweep):
    """
    Describes functions to build linear swept topologies, called prisms.
    A prism is defined by:
    -   a basis shape, which is swept, and
    -   a sweeping direction, which is:
    -   a vector for finite prisms, or
    -   a direction for infinite or semi-infinite prisms.
    The basis shape must not contain any solids.
    The profile generates objects according to the following rules:
    -   Vertices generate Edges
    -   Edges generate Faces.
    -   Wires generate Shells.
    -   Faces generate Solids.
    -   Shells generate Composite Solids
    A MakePrism object provides a framework for:
    -   defining the construction of a prism,
    -   implementing the construction algorithm, and
    -   consulting the result.
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
        If Inf is true the prism is infinite, if Inf is false
        the prism is semi-infinite (in the direction D). If C
        is true S is copied (for semi-infinite prisms).
        If Canonize is true then generated surfaces
        are attempted to be canonized in simple types
        """

    @overload
    def __init__(self, theOther: BRepPrimAPI_MakePrism) -> None: ...

    def Prism(self) -> nanoocp.BRepSweep.BRepSweep_Prism:
        """Returns the internal sweeping algorithm."""

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Builds the resulting shape (redefined from MakeShape)."""

    @overload
    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape of the bottom of the prism."""

    @overload
    def FirstShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the TopoDS Shape of the bottom of the prism.
        generated with theShape (subShape of the generating shape).
        """

    @overload
    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the TopoDS Shape of the top of the prism.
        In the case of a finite prism, FirstShape returns the
        basis of the prism, in other words, S if Copy is false;
        otherwise, the copy of S belonging to the prism.
        LastShape returns the copy of S translated by V at the
        time of construction.
        """

    @overload
    def LastShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the TopoDS Shape of the top of the prism.
        generated with theShape (subShape of the generating shape).
        """

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns ListOfShape from TopTools."""

    def IsDeleted(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns true if the shape S has been deleted."""

class BRepPrimAPI_MakeRevol(BRepPrimAPI_MakeSweep):
    """
    Class to make revolved sweep topologies.

    a revolved sweep is defined by :

    * A basis topology which is swept.

    The basis topology must not contain solids
    (neither composite solids.).

    The basis topology may be copied or shared in
    the result.

    * A rotation axis and angle :

    - The axis is an Ax1 from gp.

    - The angle is in [0, 2*Pi].

    - The angle default value is 2*Pi.

    The result is a topology with a higher dimension :

    - Vertex -> Edge.
    - Edge   -> Face.
    - Wire   -> Shell.
    - Face   -> Solid.
    - Shell  -> CompSolid.

    Sweeping a Compound sweeps the elements of the
    compound and creates a compound with the
    results.
    """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, A: nanoocp.gp.gp_Ax1, Copy: bool = False) -> None:
        """
        Builds the Revol of base S, axis A and angle 2*Pi. If
        C is true, S is copied.
        """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, A: nanoocp.gp.gp_Ax1, D: float, Copy: bool = False) -> None:
        """
        Builds the Revol of base S, axis A and angle D. If C
        is true, S is copied.
        """

    @overload
    def __init__(self, theOther: BRepPrimAPI_MakeRevol) -> None: ...

    def Revol(self) -> nanoocp.BRepSweep.BRepSweep_Revol:
        """Returns the internal sweeping algorithm."""

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Builds the resulting shape (redefined from MakeShape)."""

    @overload
    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the first shape of the revol (coinciding with
        the generating shape).
        """

    @overload
    def FirstShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the TopoDS Shape of the beginning of the revolution,
        generated with theShape (subShape of the generating shape).
        """

    @overload
    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape of the end of the revol."""

    @overload
    def LastShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the TopoDS Shape of the end of the revolution,
        generated with theShape (subShape of the generating shape).
        """

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns list of shape generated from shape S
        Warning: shape S must be shape of type VERTEX, EDGE, FACE, SOLID.
        For shapes of other types method always returns empty list
        """

    def IsDeleted(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns true if the shape S has been deleted."""

    def HasDegenerated(self) -> bool:
        """Check if there are degenerated edges in the result."""

    def Degenerated(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the list of degenerated edges"""

class BRepPrimAPI_MakeRevolution(BRepPrimAPI_MakeOneAxis):
    """
    Describes functions to build revolved shapes.
    A MakeRevolution object provides a framework for:
    -   defining the construction of a revolved shape,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, Meridian: nanoocp.Geom.Geom_Curve | None) -> None: ...

    @overload
    def __init__(self, Meridian: nanoocp.Geom.Geom_Curve | None, angle: float) -> None: ...

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, Meridian: nanoocp.Geom.Geom_Curve | None) -> None: ...

    @overload
    def __init__(self, Meridian: nanoocp.Geom.Geom_Curve | None, VMin: float, VMax: float) -> None: ...

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, Meridian: nanoocp.Geom.Geom_Curve | None, angle: float) -> None: ...

    @overload
    def __init__(self, Meridian: nanoocp.Geom.Geom_Curve | None, VMin: float, VMax: float, angle: float) -> None: ...

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, Meridian: nanoocp.Geom.Geom_Curve | None, VMin: float, VMax: float) -> None:
        """Make a revolution body by rotating a curve around Z."""

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, Meridian: nanoocp.Geom.Geom_Curve | None, VMin: float, VMax: float, angle: float) -> None:
        """
        Make a revolution body by rotating a curve around Z.
        For all algorithms the resulting shape is composed of
        -   a lateral revolved face,
        -   two planar faces in planes parallel to the plane z =
        0, and passing by the extremities of the revolved
        portion of Meridian, if these points are not on the Z
        axis (in case of a complete revolved shape, these faces are circles),
        -   and in the case of a portion of a revolved shape, two
        planar faces to close the shape (in the planes u = 0 and u = angle).
        """

    @overload
    def __init__(self, theOther: BRepPrimAPI_MakeRevolution) -> None: ...

    def Revolution(self) -> nanoocp.BRepPrim.BRepPrim_Revolution:
        """Returns the algorithm."""

class BRepPrimAPI_MakeSphere(BRepPrimAPI_MakeOneAxis):
    """
    Describes functions to build spheres or portions of spheres.
    A MakeSphere object provides a framework for:
    -   defining the construction of a sphere,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, R: float) -> None:
        """
        Make a sphere.
        @param[in] R  sphere radius
        """

    @overload
    def __init__(self, R: float, angle: float) -> None:
        """
        Make a sphere (spherical wedge).
        @param[in] R      sphere radius
        @param[in] angle  angle between the radii lying within the bounding semidisks
        """

    @overload
    def __init__(self, Center: nanoocp.gp.gp_Pnt, R: float) -> None:
        """
        Make a sphere.
        @param[in] Center  sphere center coordinates
        @param[in] R       sphere radius
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax2, R: float) -> None:
        """
        Make a sphere.
        @param[in] Axis  coordinate system for the construction of the sphere
        @param[in] R     sphere radius
        """

    @overload
    def __init__(self, R: float, angle1: float, angle2: float) -> None:
        """
        Make a sphere (spherical segment).
        @param[in] R  sphere radius
        @param[in] angle1  first angle defining a spherical segment
        @param[in] angle2  second angle defining a spherical segment
        """

    @overload
    def __init__(self, Center: nanoocp.gp.gp_Pnt, R: float, angle: float) -> None:
        """
        Make a sphere (spherical wedge).
        @param[in] Center  sphere center coordinates
        @param[in] R       sphere radius
        @param[in] angle   angle between the radii lying within the bounding semidisks
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax2, R: float, angle: float) -> None:
        """
        Make a sphere (spherical wedge).
        @param[in] Axis   coordinate system for the construction of the sphere
        @param[in] R      sphere radius
        @param[in] angle  angle between the radii lying within the bounding semidisks
        """

    @overload
    def __init__(self, R: float, angle1: float, angle2: float, angle3: float) -> None:
        """
        Make a sphere (spherical segment).
        @param[in] R       sphere radius
        @param[in] angle1  first angle defining a spherical segment
        @param[in] angle2  second angle defining a spherical segment
        @param[in] angle3  angle between the radii lying within the bounding semidisks
        """

    @overload
    def __init__(self, Center: nanoocp.gp.gp_Pnt, R: float, angle1: float, angle2: float) -> None:
        """
        Make a sphere (spherical segment).
        @param[in] Center  sphere center coordinates
        @param[in] R       sphere radius
        @param[in] angle1  first angle defining a spherical segment
        @param[in] angle2  second angle defining a spherical segment
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax2, R: float, angle1: float, angle2: float) -> None:
        """
        Make a sphere (spherical segment).
        @param[in] Axis    coordinate system for the construction of the sphere
        @param[in] R       sphere radius
        @param[in] angle1  first angle defining a spherical segment
        @param[in] angle2  second angle defining a spherical segment
        """

    @overload
    def __init__(self, Center: nanoocp.gp.gp_Pnt, R: float, angle1: float, angle2: float, angle3: float) -> None:
        """
        Make a sphere (spherical segment).
        @param[in] Center  sphere center coordinates
        @param[in] R       sphere radius
        @param[in] angle1  first angle defining a spherical segment
        @param[in] angle2  second angle defining a spherical segment
        @param[in] angle3  angle between the radii lying within the bounding semidisks
        """

    @overload
    def __init__(self, Axis: nanoocp.gp.gp_Ax2, R: float, angle1: float, angle2: float, angle3: float) -> None:
        """
        Make a sphere of radius R.
        For all algorithms The resulting shape is composed of
        -   a lateral spherical face,
        -   two planar faces parallel to the plane z = 0 if the
        sphere is truncated in the v parametric direction, or
        only one planar face if angle1 is equal to -p/2 or if
        angle2 is equal to p/2 (these faces are circles in
        case of a complete truncated sphere),
        -   and in case of a portion of sphere, two planar faces
        to shut the shape.(in the planes u = 0 and u = angle).
        """

    @overload
    def __init__(self, theOther: BRepPrimAPI_MakeSphere) -> None: ...

    def Sphere(self) -> nanoocp.BRepPrim.BRepPrim_Sphere:
        """Returns the algorithm."""

class BRepPrimAPI_MakeTorus(BRepPrimAPI_MakeOneAxis):
    """
    Describes functions to build tori or portions of tori.
    A MakeTorus object provides a framework for:
    -   defining the construction of a torus,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, R1: float, R2: float) -> None:
        """
        Make a torus.
        @param[in] R1  distance from the center of the pipe to the center of the torus
        @param[in] R2  radius of the pipe
        """

    @overload
    def __init__(self, R1: float, R2: float, angle: float) -> None:
        """
        Make a section of a torus.
        @param[in] R1     distance from the center of the pipe to the center of the torus
        @param[in] R2     radius of the pipe
        @param[in] angle  angle to create a torus pipe segment
        """

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, R1: float, R2: float) -> None:
        """
        Make a torus.
        @param[in] Axes  coordinate system for the construction of the sphere
        @param[in] R1    distance from the center of the pipe to the center of the torus
        @param[in] R2    radius of the pipe
        """

    @overload
    def __init__(self, R1: float, R2: float, angle1: float, angle2: float) -> None:
        """
        Make  a torus with angles on the small circle.
        @param[in] R1      distance from the center of the pipe to the center of the torus
        @param[in] R2      radius of the pipe
        @param[in] angle1  first  angle to create a torus ring segment
        @param[in] angle2  second angle to create a torus ring segment
        """

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, R1: float, R2: float, angle: float) -> None:
        """
        Make a section of a torus.
        @param[in] Axes   coordinate system for the construction of the sphere
        @param[in] R1     distance from the center of the pipe to the center of the torus
        @param[in] R2     radius of the pipe
        @param[in] angle  angle to create a torus pipe segment
        """

    @overload
    def __init__(self, R1: float, R2: float, angle1: float, angle2: float, angle: float) -> None:
        """
        Make  a torus with angles on the small circle.
        @param[in] R1      distance from the center of the pipe to the center of the torus
        @param[in] R2      radius of the pipe
        @param[in] angle1  first  angle to create a torus ring segment
        @param[in] angle2  second angle to create a torus ring segment
        @param[in] angle   angle to create a torus pipe segment
        """

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, R1: float, R2: float, angle1: float, angle2: float) -> None:
        """
        Make a torus.
        @param[in] Axes    coordinate system for the construction of the sphere
        @param[in] R1      distance from the center of the pipe to the center of the torus
        @param[in] R2      radius of the pipe
        @param[in] angle1  first  angle to create a torus ring segment
        @param[in] angle2  second angle to create a torus ring segment
        """

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, R1: float, R2: float, angle1: float, angle2: float, angle: float) -> None:
        """
        Make a section of a torus of radii R1 R2.
        For all algorithms The resulting shape is composed of
        -      a lateral toroidal face,
        -      two conical faces (defined by the equation v = angle1 and
        v = angle2) if the sphere is truncated in the v parametric
        direction (they may be cylindrical faces in some
        particular conditions), and in case of a portion
        of torus, two planar faces to close the shape.(in the planes
        u = 0 and u = angle).
        Notes:
        -      The u parameter corresponds to a rotation angle around the Z axis.
        -      The circle whose radius is equal to the minor radius,
        located in the plane defined by the X axis and the Z axis,
        centered on the X axis, on its positive side, and positioned
        at a distance from the origin equal to the major radius, is
        the reference circle of the torus. The rotation around an
        axis parallel to the Y axis and passing through the center
        of the reference circle gives the v parameter on the
        reference circle. The X axis gives the origin of the v
        parameter. Near 0, as v increases, the Z coordinate increases
        (following the standard trigonometric convention: Z = r*sin(v)).
        """

    @overload
    def __init__(self, theOther: BRepPrimAPI_MakeTorus) -> None: ...

    def Torus(self) -> nanoocp.BRepPrim.BRepPrim_Torus:
        """Returns the algorithm."""

class BRepPrimAPI_MakeWedge(nanoocp.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    """
    Describes functions to build wedges, i.e. boxes with inclined faces.
    A MakeWedge object provides a framework for:
    -   defining the construction of a wedge,
    -   implementing the construction algorithm, and
    -   consulting the result.
    """

    @overload
    def __init__(self, dx: float, dy: float, dz: float, ltx: float) -> None: ...

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, dx: float, dy: float, dz: float, ltx: float) -> None:
        """Make a STEP right angular wedge. (ltx >= 0)"""

    @overload
    def __init__(self, dx: float, dy: float, dz: float, xmin: float, zmin: float, xmax: float, zmax: float) -> None: ...

    @overload
    def __init__(self, Axes: nanoocp.gp.gp_Ax2, dx: float, dy: float, dz: float, xmin: float, zmin: float, xmax: float, zmax: float) -> None:
        """Make a wedge. The face at dy is xmin,zmin xmax,zmax"""

    @overload
    def __init__(self, theOther: BRepPrimAPI_MakeWedge) -> None: ...

    def Wedge(self) -> nanoocp.BRepPrim.BRepPrim_Wedge:
        """Returns the internal algorithm."""

    def Build(self, theRange: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """Stores the solid in myShape."""

    def Shell(self) -> nanoocp.TopoDS.TopoDS_Shell:
        """Returns the constructed box in the form of a shell."""

    def Solid(self) -> nanoocp.TopoDS.TopoDS_Solid:
        """Returns the constructed box in the form of a solid."""
