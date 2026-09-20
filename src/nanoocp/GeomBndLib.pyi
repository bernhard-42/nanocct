"""OCCT package GeomBndLib (toolkit TKGeomBase)"""

from typing import overload

import nanoocp.Adaptor2d
import nanoocp.Adaptor3d
import nanoocp.Bnd
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.gp


class GeomBndLib_BezierCurve:
    """
    Computes bounding box for a 3D Bezier curve (Geom_BezierCurve).
    Uses poles convex hull + sampling for deflection estimation.
    """

    def __init__(self, theCurve: nanoocp.Geom.Geom_BezierCurve) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_BezierCurve: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full curve."""

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for arc [theU1, theU2]."""

    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box using numerical optimization."""

class GeomBndLib_BezierCurve2d:
    """
    Computes bounding box for a 2D Bezier curve (Geom2d_BezierCurve).
    Uses poles convex hull + sampling for deflection estimation.
    """

    def __init__(self, theCurve: nanoocp.Geom2d.Geom2d_BezierCurve) -> None: ...

    def Geometry(self) -> nanoocp.Geom2d.Geom2d_BezierCurve: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for full curve."""

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for arc [theU1, theU2]."""

    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute precise bounding box using numerical optimization."""

class GeomBndLib_BezierSurface:
    """
    Computes bounding box for a Bezier surface (Geom_BezierSurface).
    Uses poles convex hull for full surface, grid sampling for trimmed patches.
    """

    def __init__(self, theSurf: nanoocp.Geom.Geom_BezierSurface) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_BezierSurface: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full surface."""

    @overload
    def Box(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for surface patch [theUMin, theUMax] x [theVMin, theVMax].
        """

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box for full surface."""

    @overload
    def BoxOptimal(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box using numerical optimization."""

class GeomBndLib_BSplineCurve:
    """
    Computes bounding box for a 3D BSpline curve (Geom_BSplineCurve).
    Uses poles convex hull with knot-based index selection + sampling.
    """

    def __init__(self, theCurve: nanoocp.Geom.Geom_BSplineCurve) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_BSplineCurve: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full curve."""

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for arc [theU1, theU2]."""

    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box using numerical optimization."""

class GeomBndLib_BSplineCurve2d:
    """
    Computes bounding box for a 2D BSpline curve (Geom2d_BSplineCurve).
    Uses poles convex hull with knot-based index selection + sampling.
    """

    def __init__(self, theCurve: nanoocp.Geom2d.Geom2d_BSplineCurve) -> None: ...

    def Geometry(self) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for full curve."""

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for arc [theU1, theU2]."""

    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute precise bounding box using numerical optimization."""

class GeomBndLib_BSplineSurface:
    """
    Computes bounding box for a BSpline surface (Geom_BSplineSurface).
    Uses poles convex hull with knot-based index selection via ComputePolesIndexes.
    """

    def __init__(self, theSurf: nanoocp.Geom.Geom_BSplineSurface) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_BSplineSurface: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full surface."""

    @overload
    def Box(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for surface patch [theUMin, theUMax] x [theVMin, theVMax].
        """

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box for full surface."""

    @overload
    def BoxOptimal(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box using numerical optimization."""

class GeomBndLib_Circle:
    """
    Computes bounding box for a 3D circle (Geom_Circle).
    Uses analytical per-coordinate extrema computation.

    Static methods accepting gp_Circ can be used directly without
    constructing a Geom_Circle handle.
    """

    def __init__(self, theCircle: nanoocp.Geom.Geom_Circle) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_Circle: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full circle."""

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for arc [theU1, theU2]."""

    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """For analytical curves, BoxOptimal is same as Box."""

    @overload
    @staticmethod
    def Box_s(theCirc: nanoocp.gp.gp_Circ, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for a full circle defined by gp_Circ."""

    @overload
    @staticmethod
    def Box_s(theCirc: nanoocp.gp.gp_Circ, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for a circle arc [theU1, theU2] defined by gp_Circ.
        """

class GeomBndLib_Circle2d:
    """
    Computes bounding box for a 2D circle (Geom2d_Circle).
    Uses analytical per-coordinate extrema computation.

    Static methods accepting gp_Circ2d can be used directly without
    constructing a Geom2d_Circle handle.
    """

    def __init__(self, theCircle: nanoocp.Geom2d.Geom2d_Circle) -> None: ...

    def Geometry(self) -> nanoocp.Geom2d.Geom2d_Circle: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for full circle."""

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for arc [theU1, theU2]."""

    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """For analytical curves, BoxOptimal is same as Box."""

    @overload
    @staticmethod
    def Box_s(theCirc: nanoocp.gp.gp_Circ2d, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for a full circle defined by gp_Circ2d."""

    @overload
    @staticmethod
    def Box_s(theCirc: nanoocp.gp.gp_Circ2d, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """
        Compute bounding box for a circle arc [theU1, theU2] defined by gp_Circ2d.
        """

class GeomBndLib_Cone:
    """
    Computes bounding box for a conical surface (Geom_ConicalSurface).
    Uses ElSLib iso-curves and GeomBndLib_ConicHelpers for circle arc bounding.
    """

    def __init__(self, theSurf: nanoocp.Geom.Geom_ConicalSurface) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_ConicalSurface: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full cone."""

    @overload
    def Box(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for cone patch [theUMin, theUMax] x [theVMin, theVMax].
        """

    @overload
    def BoxOptimal(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """For analytical surfaces, BoxOptimal is same as Box."""

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute optimal bounding box for full surface."""

class GeomBndLib_Cylinder:
    """
    Computes bounding box for a cylindrical surface (Geom_CylindricalSurface).
    Uses ElSLib iso-curves and GeomBndLib_ConicHelpers for circle arc bounding.
    """

    def __init__(self, theSurf: nanoocp.Geom.Geom_CylindricalSurface) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_CylindricalSurface: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full cylinder."""

    @overload
    def Box(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for cylinder patch [theUMin, theUMax] x [theVMin, theVMax].
        """

    @overload
    def BoxOptimal(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """For analytical surfaces, BoxOptimal is same as Box."""

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute optimal bounding box for full surface."""

class GeomBndLib_Ellipse:
    """
    Computes bounding box for a 3D ellipse (Geom_Ellipse).
    Uses analytical per-coordinate extrema computation.

    Static methods accepting gp_Elips can be used directly without
    constructing a Geom_Ellipse handle.
    """

    def __init__(self, theEllipse: nanoocp.Geom.Geom_Ellipse) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_Ellipse: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full ellipse."""

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for arc [theU1, theU2]."""

    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """For analytical curves, BoxOptimal is same as Box."""

    @overload
    @staticmethod
    def Box_s(theElips: nanoocp.gp.gp_Elips, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for a full ellipse defined by gp_Elips."""

    @overload
    @staticmethod
    def Box_s(theElips: nanoocp.gp.gp_Elips, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for an ellipse arc [theU1, theU2] defined by gp_Elips.
        """

class GeomBndLib_Ellipse2d:
    """
    Computes bounding box for a 2D ellipse (Geom2d_Ellipse).
    Uses analytical per-coordinate extrema computation.

    Static methods accepting gp_Elips2d can be used directly without
    constructing a Geom2d_Ellipse handle.
    """

    def __init__(self, theEllipse: nanoocp.Geom2d.Geom2d_Ellipse) -> None: ...

    def Geometry(self) -> nanoocp.Geom2d.Geom2d_Ellipse: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for full ellipse."""

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for arc [theU1, theU2]."""

    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """For analytical curves, BoxOptimal is same as Box."""

    @overload
    @staticmethod
    def Box_s(theElips: nanoocp.gp.gp_Elips2d, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for a full ellipse defined by gp_Elips2d."""

    @overload
    @staticmethod
    def Box_s(theElips: nanoocp.gp.gp_Elips2d, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """
        Compute bounding box for an ellipse arc [theU1, theU2] defined by gp_Elips2d.
        """

class GeomBndLib_Hyperbola:
    """
    Computes bounding box for a 3D hyperbola (Geom_Hyperbola).
    Handles infinite parameters by opening the box in appropriate directions.

    Static method accepting gp_Hypr can be used directly without
    constructing a Geom_Hyperbola handle.
    """

    def __init__(self, theHyperbola: nanoocp.Geom.Geom_Hyperbola) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_Hyperbola: ...

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for arc [theU1, theU2]."""

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full curve."""

    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """For analytical curves, BoxOptimal is same as Box."""

    @staticmethod
    def Box_s(theHypr: nanoocp.gp.gp_Hypr, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for a hyperbola arc [theU1, theU2] defined by gp_Hypr.
        """

class GeomBndLib_Hyperbola2d:
    """
    Computes bounding box for a 2D hyperbola (Geom2d_Hyperbola).
    Handles infinite parameters by opening the box in appropriate directions.

    Static method accepting gp_Hypr2d can be used directly without
    constructing a Geom2d_Hyperbola handle.
    """

    def __init__(self, theHyperbola: nanoocp.Geom2d.Geom2d_Hyperbola) -> None: ...

    def Geometry(self) -> nanoocp.Geom2d.Geom2d_Hyperbola: ...

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for arc [theU1, theU2]."""

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for full curve."""

    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """For analytical curves, BoxOptimal is same as Box."""

    @staticmethod
    def Box_s(theHypr: nanoocp.gp.gp_Hypr2d, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """
        Compute bounding box for a 2D hyperbola arc [theU1, theU2] defined by gp_Hypr2d.
        """

class GeomBndLib_OffsetCurve:
    """
    Computes bounding box for a 3D offset curve (Geom_OffsetCurve).
    Computes the bounding box of the basis curve and enlarges it by |offset|.
    """

    def __init__(self, theCurve: nanoocp.Geom.Geom_OffsetCurve) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_OffsetCurve: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full curve."""

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for arc [theU1, theU2]."""

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box for full curve."""

    @overload
    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute precise bounding box for arc [theU1, theU2] by sampling the offset curve.
        """

class GeomBndLib_OffsetCurve2d:
    """
    Computes bounding box for a 2D offset curve (Geom2d_OffsetCurve).
    Computes the bounding box of the basis curve and enlarges it by |offset|.
    """

    def __init__(self, theCurve: nanoocp.Geom2d.Geom2d_OffsetCurve) -> None: ...

    def Geometry(self) -> nanoocp.Geom2d.Geom2d_OffsetCurve: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for full curve."""

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for arc [theU1, theU2]."""

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute precise bounding box for full curve."""

    @overload
    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """
        Compute precise bounding box for arc [theU1, theU2] by sampling the offset curve.
        """

class GeomBndLib_OffsetSurface:
    """
    Computes bounding box for an offset surface (Geom_OffsetSurface).
    Computes the bounding box of the basis surface and enlarges it by |offset|.
    """

    def __init__(self, theSurf: nanoocp.Geom.Geom_OffsetSurface) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_OffsetSurface: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full surface."""

    @overload
    def Box(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for surface patch [theUMin, theUMax] x [theVMin, theVMax].
        """

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box for full surface."""

    @overload
    def BoxOptimal(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute precise bounding box for surface patch using PSO numerical optimization.
        """

class GeomBndLib_OtherCurve:
    """
    Computes bounding box for a general 3D curve via adaptor.
    Uses sampling + PSO/Brent numerical optimization for BoxOptimal.
    """

    def __init__(self, theCurve: nanoocp.Adaptor3d.Adaptor3d_Curve) -> None: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full curve."""

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for arc [theU1, theU2]."""

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box for full curve."""

    @overload
    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box using PSO + Brent optimization."""

class GeomBndLib_OtherCurve2d:
    """
    Computes bounding box for a general 2D curve via adaptor.
    Uses sampling + PSO/Brent numerical optimization for BoxOptimal.
    """

    def __init__(self, theCurve: nanoocp.Adaptor2d.Adaptor2d_Curve2d) -> None: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for full curve."""

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for arc [theU1, theU2]."""

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute precise bounding box for full curve."""

    @overload
    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute precise bounding box using PSO + Brent optimization."""

class GeomBndLib_OtherSurface:
    """
    Computes bounding box for a general surface via adaptor.
    Uses grid sampling for Box and PSO/Powell numerical optimization for BoxOptimal.
    """

    def __init__(self, theSurf: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full surface."""

    @overload
    def Box(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for surface patch [theUMin, theUMax] x [theVMin, theVMax].
        """

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box for full surface."""

    @overload
    def BoxOptimal(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box using PSO + Powell optimization."""

class GeomBndLib_Parabola:
    """
    Computes bounding box for a 3D parabola (Geom_Parabola).
    Handles infinite parameters by opening the box in appropriate directions.

    Static method accepting gp_Parab can be used directly without
    constructing a Geom_Parabola handle.
    """

    def __init__(self, theParabola: nanoocp.Geom.Geom_Parabola) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_Parabola: ...

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for arc [theU1, theU2]."""

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full curve."""

    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """For analytical curves, BoxOptimal is same as Box."""

    @staticmethod
    def Box_s(theParab: nanoocp.gp.gp_Parab, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for a parabola arc [theU1, theU2] defined by gp_Parab.
        """

class GeomBndLib_Parabola2d:
    """
    Computes bounding box for a 2D parabola (Geom2d_Parabola).
    Handles infinite parameters by opening the box in appropriate directions.

    Static method accepting gp_Parab2d can be used directly without
    constructing a Geom2d_Parabola handle.
    """

    def __init__(self, theParabola: nanoocp.Geom2d.Geom2d_Parabola) -> None: ...

    def Geometry(self) -> nanoocp.Geom2d.Geom2d_Parabola: ...

    @overload
    def Box(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for arc [theU1, theU2]."""

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """Compute bounding box for full curve."""

    def BoxOptimal(self, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """For analytical curves, BoxOptimal is same as Box."""

    @staticmethod
    def Box_s(theParab: nanoocp.gp.gp_Parab2d, theU1: float, theU2: float, theTol: float) -> nanoocp.Bnd.Bnd_Box2d:
        """
        Compute bounding box for a 2D parabola arc [theU1, theU2] defined by gp_Parab2d.
        """

class GeomBndLib_Plane:
    """
    Computes bounding box for a 3D plane (Geom_Plane).
    Handles infinite parameters by opening box sides based on the plane normal direction.
    """

    def __init__(self, thePlane: nanoocp.Geom.Geom_Plane) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_Plane: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full plane (infinite)."""

    @overload
    def Box(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for plane patch [theUMin, theUMax] x [theVMin, theVMax].
        """

    @overload
    def BoxOptimal(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """For analytical surfaces, BoxOptimal is same as Box."""

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute optimal bounding box for full surface."""

class GeomBndLib_Sphere:
    """
    Computes bounding box for a spherical surface (Geom_SphericalSurface).
    Uses direct extremal-point computation and ElSLib iso-curves with
    GeomBndLib_ConicHelpers for circle arc bounding.
    """

    def __init__(self, theSurf: nanoocp.Geom.Geom_SphericalSurface) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_SphericalSurface: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full sphere."""

    @overload
    def Box(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for sphere patch [theUMin, theUMax] x [theVMin, theVMax].
        """

    @overload
    def BoxOptimal(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """For analytical surfaces, BoxOptimal is same as Box."""

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute optimal bounding box for full surface."""

class GeomBndLib_SurfaceOfExtrusion:
    """
    Computes bounding box for a surface of linear extrusion (Geom_SurfaceOfLinearExtrusion).
    Uses pure analytical approach: P(U, V) = BasisCurve(U) + V * Direction,
    so the box is computed from the basis curve box extended along the direction.
    """

    def __init__(self, theSurf: nanoocp.Geom.Geom_SurfaceOfLinearExtrusion) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_SurfaceOfLinearExtrusion: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full surface."""

    @overload
    def Box(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for surface patch [theUMin, theUMax] x [theVMin, theVMax].
        """

    @overload
    def BoxOptimal(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box using tight basis curve bounds."""

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box for full surface."""

class GeomBndLib_SurfaceOfRevolution:
    """
    Computes bounding box for a surface of revolution (Geom_SurfaceOfRevolution).
    Uses analytical approach: samples the basis curve at multiple V values,
    constructs the revolution circle for each sample point, and bounds each
    circle arc using GeomBndLib_Circle.
    """

    def __init__(self, theSurf: nanoocp.Geom.Geom_SurfaceOfRevolution) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_SurfaceOfRevolution: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full surface."""

    @overload
    def Box(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for surface patch [theUMin, theUMax] x [theVMin, theVMax].
        """

    @overload
    def BoxOptimal(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box using tight basis curve bounds."""

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box for full surface."""

class GeomBndLib_Torus:
    """
    Computes bounding box for a toroidal surface (Geom_ToroidalSurface).
    Uses 8-point polygon approximation via GeomBndLib_ConicHelpers and
    extremal-point computation for degenerate torus (Ra < Ri).
    """

    def __init__(self, theSurf: nanoocp.Geom.Geom_ToroidalSurface) -> None: ...

    def Geometry(self) -> nanoocp.Geom.Geom_ToroidalSurface: ...

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full torus."""

    @overload
    def Box(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for torus patch [theUMin, theUMax] x [theVMin, theVMax].
        """

    @overload
    def BoxOptimal(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute precise bounding box for torus patch using PSO + Powell optimization.
        """

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box for full torus."""

class GeomBndLib_Surface:
    """
    Variant-based dispatcher for 3D surface bounding box computation.
    Auto-detects the surface type and delegates to the appropriate specialized class.
    """

    @overload
    def __init__(self, theSurf: nanoocp.Adaptor3d.Adaptor3d_Surface) -> None:
        """Construct from an adaptor surface."""

    @overload
    def __init__(self, theSurf: nanoocp.Geom.Geom_Surface) -> None:
        """Construct from a Geom_Surface handle."""

    def GetType(self) -> nanoocp.GeomAbs.GeomAbs_SurfaceType:
        """Return detected surface type."""

    @overload
    def Box(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute bounding box for full surface."""

    @overload
    def Box(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute bounding box for surface patch [theUMin, theUMax] x [theVMin, theVMax].
        """

    @overload
    def BoxOptimal(self, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """Compute precise bounding box for full surface."""

    @overload
    def BoxOptimal(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float) -> nanoocp.Bnd.Bnd_Box:
        """
        Compute precise bounding box for surface patch [theUMin, theUMax] x [theVMin, theVMax].
        """

    @overload
    def Add(self, theTol: float, theBox: nanoocp.Bnd.Bnd_Box) -> None:
        """Add bounding box for full surface."""

    @overload
    def Add(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float, theBox: nanoocp.Bnd.Bnd_Box) -> None:
        """
        Add bounding box for surface patch [theUMin, theUMax] x [theVMin, theVMax].
        """

    @overload
    def AddOptimal(self, theTol: float, theBox: nanoocp.Bnd.Bnd_Box) -> None:
        """Add precise bounding box for full surface."""

    @overload
    def AddOptimal(self, theUMin: float, theUMax: float, theVMin: float, theVMax: float, theTol: float, theBox: nanoocp.Bnd.Bnd_Box) -> None:
        """
        Add precise bounding box for surface patch [theUMin, theUMax] x [theVMin, theVMax].
        """
