"""OCCT package VrmlConverter (toolkit TKDEVRML)"""

import enum
from typing import overload

import nanoocp.Adaptor3d
import nanoocp.Aspect
import nanoocp.BRepAdaptor
import nanoocp.HLRAlgo
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.Standard
import nanoocp.TopoDS
import nanoocp.Vrml
import nanoocp.gp


class VrmlConverter_TypeOfCamera(enum.IntEnum):
    VrmlConverter_NoCamera = 0

    VrmlConverter_PerspectiveCamera = 1

    VrmlConverter_OrthographicCamera = 2

VrmlConverter_NoCamera: VrmlConverter_TypeOfCamera = VrmlConverter_TypeOfCamera.VrmlConverter_NoCamera

VrmlConverter_PerspectiveCamera: VrmlConverter_TypeOfCamera = ...

VrmlConverter_OrthographicCamera: VrmlConverter_TypeOfCamera = ...

class VrmlConverter_TypeOfLight(enum.IntEnum):
    VrmlConverter_NoLight = 0

    VrmlConverter_DirectionLight = 1

    VrmlConverter_PointLight = 2

    VrmlConverter_SpotLight = 3

VrmlConverter_NoLight: VrmlConverter_TypeOfLight = VrmlConverter_TypeOfLight.VrmlConverter_NoLight

VrmlConverter_DirectionLight: VrmlConverter_TypeOfLight = ...

VrmlConverter_PointLight: VrmlConverter_TypeOfLight = ...

VrmlConverter_SpotLight: VrmlConverter_TypeOfLight = VrmlConverter_TypeOfLight.VrmlConverter_SpotLight

class VrmlConverter_Curve:
    """
    Curve - computes the presentation of objects to be
    seen as curves (the computation will be made
    with a constant number of points), converts this one
    into VRML objects and writes (adds) them into
    anOStream. All requested properties of the
    representation are specify in aDrawer of Drawer
    class (VrmlConverter).
    This kind of the presentation is converted into
    IndexedLineSet (VRML).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: VrmlConverter_Curve) -> None: ...

    @overload
    @staticmethod
    def Add(aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aDrawer: VrmlConverter_Drawer | None) -> str:
        """
        adds to the OStream the drawing of the curve aCurve.
        The aspect is defined by LineAspect in aDrawer.
        """

    @overload
    @staticmethod
    def Add(aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, aDrawer: VrmlConverter_Drawer | None) -> str:
        """
        adds to the OStream the drawing of the curve aCurve.
        The aspect is defined by LineAspect in aDrawer.
        The drawing will be limited between the points of parameter
        U1 and U2.
        """

    @overload
    @staticmethod
    def Add(aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, aNbPoints: int) -> str:
        """
        adds to the OStream the drawing of the curve aCurve.
        The aspect is the current aspect.
        The drawing will be limited between the points of parameter
        U1 and U2. aNbPoints defines number of points on one interval.
        """

class VrmlConverter_DeflectionCurve:
    """
    DeflectionCurve - computes the presentation of
    objects to be seen as curves, converts this one into
    VRML objects and writes (adds) into
    anOStream. All requested properties of the
    representation are specify in aDrawer.
    This kind of the presentation
    is converted into IndexedLineSet (VRML).
    The computation will be made according to a maximal
    chordial deviation.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: VrmlConverter_DeflectionCurve) -> None: ...

    @overload
    @staticmethod
    def Add(aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aDrawer: VrmlConverter_Drawer | None) -> str:
        """
        adds to the OStream the drawing of the curve aCurve with
        respect to the maximal chordial deviation defined
        by the drawer aDrawer.
        The aspect is defined by LineAspect in aDrawer.
        """

    @overload
    @staticmethod
    def Add(aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, aDrawer: VrmlConverter_Drawer | None) -> str:
        """
        adds to the OStream the drawing of the curve aCurve with
        respect to the maximal chordial deviation defined
        by the drawer aDrawer.
        The aspect is defined by LineAspect in aDrawer.
        The drawing will be limited between the points of parameter
        U1 and U2.
        """

    @overload
    @staticmethod
    def Add(aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aDeflection: float, aLimit: float) -> str: ...

    @overload
    @staticmethod
    def Add(aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aDeflection: float, aDrawer: VrmlConverter_Drawer | None) -> str:
        """
        adds to the OStream the drawing of the curve aCurve with
        respect to the maximal chordial deviation aDeflection.
        The aspect is the current aspect
        """

    @overload
    @staticmethod
    def Add(aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, U1: float, U2: float, aDeflection: float) -> str:
        """
        adds to the OStream the drawing of the curve aCurve with
        respect to the maximal chordial deviation aDeflection.
        The aspect is the current aspect
        The drawing will be limited between the points of parameter
        U1 and U2.
        """

    @overload
    @staticmethod
    def Add(aCurve: nanoocp.Adaptor3d.Adaptor3d_Curve, aParams: nanoocp.NCollection.NCollection_HArray1[float] | None, aNbNodes: int, aDrawer: VrmlConverter_Drawer | None) -> str:
        """
        adds to the OStream the drawing of the curve aCurve with
        the array of parameters to retrieve points on curve.
        """

class VrmlConverter_Drawer(nanoocp.Standard.Standard_Transient):
    """
    qualifies the aspect properties for
    the VRML conversation of a specific kind of object.
    This includes for example color, maximal chordial deviation, etc...
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: VrmlConverter_Drawer) -> None: ...

    def SetTypeOfDeflection(self, aTypeOfDeflection: nanoocp.Aspect.Aspect_TypeOfDeflection) -> None:
        """
        by default: TOD_Relative; however, except for the shapes,
        the drawing will be made using the absolute deviation.
        """

    def TypeOfDeflection(self) -> nanoocp.Aspect.Aspect_TypeOfDeflection: ...

    def SetMaximalChordialDeviation(self, aChordialDeviation: float) -> None:
        """
        Defines the maximal chordial deviation when drawing any curve;
        If this value is one of the obvious parameters of methods,
        current value from Drawer won't be used.
        This value is used by:

        VrmlConverter_DeflectionCurve
        VrmlConverter_WFDeflectionRestrictedFace
        VrmlConverter_WFDeflectionShape
        """

    def MaximalChordialDeviation(self) -> float:
        """
        returns the maximal chordial deviation.
        Default value: 0.1
        """

    def SetDeviationCoefficient(self, aCoefficient: float) -> None:
        """default 0.001"""

    def DeviationCoefficient(self) -> float: ...

    def SetDiscretisation(self, d: int) -> None:
        """
        default: 17 points.
        Defines the Discretisation (myNbPoints) when drawing any curve;
        If this value is one of the obvious parameters of methods,
        current value from Drawer won't be used.
        This value is used by:

        VrmlConverter_Curve
        VrmlConverter_WFRestrictedFace
        VrmlConverter_WFShape
        """

    def Discretisation(self) -> int: ...

    def SetMaximalParameterValue(self, Value: float) -> None:
        """
        defines the maximum value allowed for the first and last
        parameters of an infinite curve.
        Default value: 500.
        VrmlConverter_Curve
        VrmlConverter_WFRestrictedFace
        VrmlConverter_WFShape
        """

    def MaximalParameterValue(self) -> float: ...

    def SetIsoOnPlane(self, OnOff: bool) -> None:
        """
        enables the drawing of isos on planes.
        By default there are no isos on planes.
        """

    def IsoOnPlane(self) -> bool:
        """returns True if the drawing of isos on planes is enabled."""

    def UIsoAspect(self) -> VrmlConverter_IsoAspect:
        """
        Defines the attributes which are used when drawing an
        U isoparametric curve of a face. Defines the number
        of U isoparametric curves to be drawn for a single face.
        The default values are the same default values from Vrml package.

        These attributes are used by the following algorithms:
        VrmlConverter_WFRestrictedFace
        VrmlConverter_WFDeflectionRestrictedFace
        """

    def SetUIsoAspect(self, anAspect: VrmlConverter_IsoAspect | None) -> None: ...

    def VIsoAspect(self) -> VrmlConverter_IsoAspect:
        """
        Defines the attributes which are used when drawing an
        V isoparametric curve of a face. Defines the number
        of V isoparametric curves to be drawn for a single face.
        The default values are the same default values from Vrml package.

        These attributes are used by the following algorithms:
        VrmlConverter_WFRestrictedFace
        VrmlConverter_WFDeflectionRestrictedFace
        """

    def SetVIsoAspect(self, anAspect: VrmlConverter_IsoAspect | None) -> None: ...

    def FreeBoundaryAspect(self) -> VrmlConverter_LineAspect:
        """
        The default values are the same default values from Vrml package.
        These attributes are used by the following algorithms:
        VrmlConverter_WFShape
        VrmlConverter_WFDeflectionShape
        """

    def SetFreeBoundaryAspect(self, anAspect: VrmlConverter_LineAspect | None) -> None: ...

    def SetFreeBoundaryDraw(self, OnOff: bool) -> None:
        """
        enables the drawing the free boundaries
        By default the free boundaries are drawn.
        """

    def FreeBoundaryDraw(self) -> bool:
        """returns True if the drawing of the free boundaries is enabled."""

    def WireAspect(self) -> VrmlConverter_LineAspect:
        """
        The default values are the same default values from Vrml package.
        These attributes are used by the following algorithms:
        VrmlConverter_WFShape
        VrmlConverter_WFDeflectionShape
        """

    def SetWireAspect(self, anAspect: VrmlConverter_LineAspect | None) -> None: ...

    def SetWireDraw(self, OnOff: bool) -> None:
        """
        enables the drawing the wire
        By default the wire are drawn.
        """

    def WireDraw(self) -> bool:
        """returns True if the drawing of the wire is enabled."""

    def UnFreeBoundaryAspect(self) -> VrmlConverter_LineAspect:
        """
        The default values are the same default values from Vrml package.
        These attributes are used by the following algorithms:
        VrmlConverter_WFShape
        VrmlConverter_WFDeflectionShape
        """

    def SetUnFreeBoundaryAspect(self, anAspect: VrmlConverter_LineAspect | None) -> None: ...

    def SetUnFreeBoundaryDraw(self, OnOff: bool) -> None:
        """
        enables the drawing the unfree boundaries
        By default the unfree boundaries are drawn.
        """

    def UnFreeBoundaryDraw(self) -> bool:
        """returns True if the drawing of the unfree boundaries is enabled."""

    def LineAspect(self) -> VrmlConverter_LineAspect:
        """The default values are the same default values from Vrml package."""

    def SetLineAspect(self, anAspect: VrmlConverter_LineAspect | None) -> None: ...

    def PointAspect(self) -> VrmlConverter_PointAspect: ...

    def SetPointAspect(self, anAspect: VrmlConverter_PointAspect | None) -> None: ...

    def ShadingAspect(self) -> VrmlConverter_ShadingAspect:
        """The default values are the same default values from Vrml package."""

    def SetShadingAspect(self, anAspect: VrmlConverter_ShadingAspect | None) -> None: ...

    def DrawHiddenLine(self) -> bool:
        """
        returns true if the hidden lines are to be drawn.
        By default the hidden lines are not drawn.
        """

    def EnableDrawHiddenLine(self) -> None:
        """sets DrawHiddenLine = true  - the hidden lines are drawn."""

    def DisableDrawHiddenLine(self) -> None:
        """sets DrawHiddenLine = false - the hidden lines are not drawn."""

    def HiddenLineAspect(self) -> VrmlConverter_LineAspect:
        """
        returns LineAspect for the hidden lines.
        The default values are the same default values from Vrml package.
        """

    def SetHiddenLineAspect(self, anAspect: VrmlConverter_LineAspect | None) -> None:
        """sets LineAspect for the hidden lines."""

    def SeenLineAspect(self) -> VrmlConverter_LineAspect:
        """
        returns LineAspect for the seen lines.
        The default values are the same default values from Vrml package.
        """

    def SetSeenLineAspect(self, anAspect: VrmlConverter_LineAspect | None) -> None:
        """sets LineAspect for the seen lines."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlConverter_HLRShape:
    """
    HLRShape - computes the presentation of objects
    with removal of their hidden lines for a specific
    projector, converts them into VRML objects and
    writes (adds) them into anOStream. All requested
    properties of the representation are specify in
    aDrawer of Drawer class. This kind of the presentation
    is converted into IndexedLineSet and if they are defined
    in Projector info:
    PerspectiveCamera,
    OrthographicCamera,
    DirectionLight,
    PointLight,
    SpotLight
    from Vrml package.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: VrmlConverter_HLRShape) -> None: ...

    @staticmethod
    def Add(aShape: nanoocp.TopoDS.TopoDS_Shape, aDrawer: VrmlConverter_Drawer | None, aProjector: VrmlConverter_Projector | None) -> str: ...

class VrmlConverter_LineAspect(nanoocp.Standard.Standard_Transient):
    """
    qualifies the aspect properties for
    the VRML conversation of a Curve and a DeflectionCurve.
    """

    @overload
    def __init__(self) -> None:
        """
        create a default LineAspect.
        Default value: HasMaterial = False - a line hasn't own material (color)
        """

    @overload
    def __init__(self, aMaterial: nanoocp.Vrml.Vrml_Material | None, OnOff: bool) -> None: ...

    @overload
    def __init__(self, theOther: VrmlConverter_LineAspect) -> None: ...

    def SetMaterial(self, aMaterial: nanoocp.Vrml.Vrml_Material | None) -> None: ...

    def Material(self) -> nanoocp.Vrml.Vrml_Material: ...

    def SetHasMaterial(self, OnOff: bool) -> None:
        """
        defines the necessary of writing own Material from Vrml into output OStream.
        By default False - the material is not writing into OStream,
        True - the material is writing.
        """

    def HasMaterial(self) -> bool:
        """returns True if the materials is writing into OStream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlConverter_IsoAspect(VrmlConverter_LineAspect):
    """
    qualifies the aspect properties for
    the VRML conversation of iso curves.
    """

    @overload
    def __init__(self) -> None:
        """
        create a default IsoAspect.
        Default value: myNumber - 10.
        """

    @overload
    def __init__(self, aMaterial: nanoocp.Vrml.Vrml_Material | None, OnOff: bool, aNumber: int) -> None: ...

    @overload
    def __init__(self, theOther: VrmlConverter_IsoAspect) -> None: ...

    def SetNumber(self, aNumber: int) -> None: ...

    def Number(self) -> int:
        """
        returns the number of U or V isoparametric curves drawn for a
        single face.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlConverter_PointAspect(nanoocp.Standard.Standard_Transient):
    """
    qualifies the aspect properties for
    the VRML conversation of a Point Set.
    """

    @overload
    def __init__(self) -> None:
        """
        create a default PointAspect.
        Default value: HasMaterial = False - a line hasn't own material (color)
        """

    @overload
    def __init__(self, aMaterial: nanoocp.Vrml.Vrml_Material | None, OnOff: bool) -> None: ...

    @overload
    def __init__(self, theOther: VrmlConverter_PointAspect) -> None: ...

    def SetMaterial(self, aMaterial: nanoocp.Vrml.Vrml_Material | None) -> None: ...

    def Material(self) -> nanoocp.Vrml.Vrml_Material: ...

    def SetHasMaterial(self, OnOff: bool) -> None:
        """
        defines the necessary of writing own Material from Vrml into output OStream.
        By default False - the material is not writing into OStream,
        True - the material is writing.
        """

    def HasMaterial(self) -> bool:
        """returns True if the materials is writing into OStream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlConverter_Projector(nanoocp.Standard.Standard_Transient):
    """
    defines projector and calculates properties of cameras and lights from Vrml
    (OrthograpicCamera, PerspectiveCamera, DirectionalLight, PointLight, SpotLight
    and MatrixTransform) to display all scene shapes with arbitrary locations
    for requested the Projection Vector, High Point Direction and the Focus
    and adds them (method Add) to anOSream.
    """

    @overload
    def __init__(self, Shapes: nanoocp.NCollection.NCollection_Array1[nanoocp.TopoDS.TopoDS_Shape], Focus: float, DX: float, DY: float, DZ: float, XUp: float, YUp: float, ZUp: float, Camera: VrmlConverter_TypeOfCamera = VrmlConverter_TypeOfCamera.VrmlConverter_NoCamera, Light: VrmlConverter_TypeOfLight = VrmlConverter_TypeOfLight.VrmlConverter_NoLight) -> None: ...

    @overload
    def __init__(self, theOther: VrmlConverter_Projector) -> None: ...

    def SetCamera(self, aCamera: VrmlConverter_TypeOfCamera) -> None: ...

    def Camera(self) -> VrmlConverter_TypeOfCamera: ...

    def SetLight(self, aLight: VrmlConverter_TypeOfLight) -> None: ...

    def Light(self) -> VrmlConverter_TypeOfLight: ...

    def Add(self) -> str:
        """
        Adds into anOStream if they are defined in Create.
        PerspectiveCamera,
        OrthographicCamera,
        DirectionLight,
        PointLight,
        SpotLight
        with MatrixTransform from VrmlConverter;
        """

    def Projector(self) -> nanoocp.HLRAlgo.HLRAlgo_Projector: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlConverter_ShadedShape:
    """
    ShadedShape - computes the shading presentation of shapes
    by triangulation algorithms, converts this one into VRML objects
    and writes (adds) into anOStream.
    All requested properties of the representation including
    the maximal chordial deviation are specify in aDrawer.
    This kind of the presentation is converted into
    IndexedFaceSet (VRML).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: VrmlConverter_ShadedShape) -> None: ...

    @staticmethod
    def Add(aShape: nanoocp.TopoDS.TopoDS_Shape, aDrawer: VrmlConverter_Drawer | None) -> str: ...

    @staticmethod
    def ComputeNormal(aFace: nanoocp.TopoDS.TopoDS_Face, pc: nanoocp.Poly.Poly_Connect, Nor: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Dir]) -> None: ...

class VrmlConverter_ShadingAspect(nanoocp.Standard.Standard_Transient):
    """
    qualifies the aspect properties for
    the VRML conversation of ShadedShape.
    """

    @overload
    def __init__(self) -> None:
        """create a default ShadingAspect."""

    @overload
    def __init__(self, theOther: VrmlConverter_ShadingAspect) -> None: ...

    def SetFrontMaterial(self, aMaterial: nanoocp.Vrml.Vrml_Material | None) -> None: ...

    def FrontMaterial(self) -> nanoocp.Vrml.Vrml_Material: ...

    def SetShapeHints(self, aShapeHints: nanoocp.Vrml.Vrml_ShapeHints) -> None: ...

    def ShapeHints(self) -> nanoocp.Vrml.Vrml_ShapeHints: ...

    def SetHasNormals(self, OnOff: bool) -> None:
        """
        defines necessary of a calculation of normals for ShadedShape to more
        accurately display curved surfaces, pacticularly when smoooth or phong
        shading is used in VRML viewer.
        By default False - the normals are not calculated,
        True - the normals are calculated.
        Warning: If normals are calculated the resulting VRML file will
        be substantially lager.
        """

    def HasNormals(self) -> bool:
        """returns True if the normals are calculating"""

    def SetHasMaterial(self, OnOff: bool) -> None:
        """
        defines necessary of writing Material from Vrml into output OStream.
        By default False - the material is not writing into OStream,
        True - the material is writing.
        """

    def HasMaterial(self) -> bool:
        """returns True if the materials is writing into OStream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlConverter_WFDeflectionRestrictedFace:
    """
    WFDeflectionRestrictedFace - computes the
    wireframe presentation of faces with
    restrictions by displaying a given number of U
    and/or V isoparametric curves, converts his
    into VRML objects and writes (adds) them into
    anOStream. All requested properties of the
    representation are specify in aDrawer of Drawer
    class (Prs3d). This kind of the presentation
    is converted into IndexedFaceSet and
    IndexedLineSet (VRML).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: VrmlConverter_WFDeflectionRestrictedFace) -> None: ...

    @overload
    @staticmethod
    def Add(aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, aDrawer: VrmlConverter_Drawer | None) -> str: ...

    @overload
    @staticmethod
    def Add(aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, DrawUIso: bool, DrawVIso: bool, Deflection: float, NBUiso: int, NBViso: int, aDrawer: VrmlConverter_Drawer | None) -> str: ...

    @staticmethod
    def AddUIso(aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, aDrawer: VrmlConverter_Drawer | None) -> str: ...

    @staticmethod
    def AddVIso(aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, aDrawer: VrmlConverter_Drawer | None) -> str: ...

class VrmlConverter_WFDeflectionShape:
    """
    WFDeflectionShape - computes the wireframe
    presentation of compound set of faces, edges and
    vertices by displaying a given number of U and/or
    V isoparametric curves, converts this one into VRML
    objects and writes (adds) them into anOStream.
    All requested properties of the representation are
    specify in aDrawer.
    This kind of the presentation is converted into
    IndexedLineSet and PointSet (VRML).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: VrmlConverter_WFDeflectionShape) -> None: ...

    @staticmethod
    def Add(aShape: nanoocp.TopoDS.TopoDS_Shape, aDrawer: VrmlConverter_Drawer | None) -> str: ...

class VrmlConverter_WFRestrictedFace:
    """
    WFRestrictedFace - computes the wireframe
    presentation of faces with restrictions by
    displaying a given number of U and/or V
    isoparametric curves, converts this one into VRML
    objects and writes (adds) into anOStream.
    All requested properties of the representation
    are specify in aDrawer.
    This kind of the presentation is converted into
    IndexedLineSet (VRML).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: VrmlConverter_WFRestrictedFace) -> None: ...

    @overload
    @staticmethod
    def Add(aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, aDrawer: VrmlConverter_Drawer | None) -> str: ...

    @overload
    @staticmethod
    def Add(aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, DrawUIso: bool, DrawVIso: bool, NBUiso: int, NBViso: int, aDrawer: VrmlConverter_Drawer | None) -> str: ...

    @staticmethod
    def AddUIso(aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, aDrawer: VrmlConverter_Drawer | None) -> str: ...

    @staticmethod
    def AddVIso(aFace: nanoocp.BRepAdaptor.BRepAdaptor_Surface | None, aDrawer: VrmlConverter_Drawer | None) -> str: ...

class VrmlConverter_WFShape:
    """
    WFShape - computes the wireframe presentation of
    compound set of faces, edges and vertices by
    displaying a given number of U and/or V isoparametric
    curves converts this one into VRML objects and writes (adds)
    them into anOStream.
    All requested properties of the representation are
    specify in aDrawer.
    This kind of the presentation is converted into
    IndexedLineSet and PointSet (VRML).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: VrmlConverter_WFShape) -> None: ...

    @staticmethod
    def Add(aShape: nanoocp.TopoDS.TopoDS_Shape, aDrawer: VrmlConverter_Drawer | None) -> str: ...
