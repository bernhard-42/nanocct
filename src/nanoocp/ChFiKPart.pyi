"""OCCT package ChFiKPart (toolkit TKFillet)"""

from typing import overload

import nanoocp.Adaptor3d
import nanoocp.ChFiDS
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAdaptor
import nanoocp.TopAbs
import nanoocp.TopOpeBRepDS
import nanoocp.gp


class ChFiKPart_ComputeData:
    """
    Methodes de classe permettant de remplir une
    SurfData dans les cas particuliers de conges
    suivants:
    - cylindre entre 2 surfaces planes,
    - tore/sphere entre un plan et un cylindre othogonal,
    - tore/sphere entre un plan et un cone othogonal,

    - tore entre un plan et une droite orthogonale (rotule).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ChFiKPart_ComputeData) -> None: ...

    @staticmethod
    def Compute(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, Sp: nanoocp.ChFiDS.ChFiDS_Spine | None, Iedge: int) -> tuple[bool, nanoocp.ChFiDS.ChFiDS_SurfData]:
        """
        Computes a simple fillet in several particular
        cases.
        """

    @overload
    @staticmethod
    def ComputeCorner(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, OrFace1: nanoocp.TopAbs.TopAbs_Orientation, OrFace2: nanoocp.TopAbs.TopAbs_Orientation, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, minRad: float, majRad: float, P1S1: nanoocp.gp.gp_Pnt2d, P2S1: nanoocp.gp.gp_Pnt2d, P1S2: nanoocp.gp.gp_Pnt2d, P2S2: nanoocp.gp.gp_Pnt2d) -> bool:
        """Computes a toric or spheric corner fillet."""

    @overload
    @staticmethod
    def ComputeCorner(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, OrFace1: nanoocp.TopAbs.TopAbs_Orientation, OrFace2: nanoocp.TopAbs.TopAbs_Orientation, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, Rad: float, PS1: nanoocp.gp.gp_Pnt2d, P1S2: nanoocp.gp.gp_Pnt2d, P2S2: nanoocp.gp.gp_Pnt2d) -> bool:
        """Computes spheric corner fillet with non iso pcurve on S2."""

    @overload
    @staticmethod
    def ComputeCorner(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, OfS: nanoocp.TopAbs.TopAbs_Orientation, OS: nanoocp.TopAbs.TopAbs_Orientation, OS1: nanoocp.TopAbs.TopAbs_Orientation, OS2: nanoocp.TopAbs.TopAbs_Orientation, Radius: float) -> bool:
        """Computes a toric corner rotule."""

@overload
def ChFiKPart_MakeChAsym(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, Pln: nanoocp.gp.gp_Pln, Con: nanoocp.gp.gp_Cone, fu: float, lu: float, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, Dis: float, Angle: float, Spine: nanoocp.gp.gp_Circ, First: float, Ofpl: nanoocp.TopAbs.TopAbs_Orientation, plandab: bool, DisOnP: bool) -> bool: ...

@overload
def ChFiKPart_MakeChAsym(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, Pln: nanoocp.gp.gp_Pln, Cyl: nanoocp.gp.gp_Cylinder, fu: float, lu: float, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, Dis: float, Angle: float, Spine: nanoocp.gp.gp_Circ, First: float, Ofpl: nanoocp.TopAbs.TopAbs_Orientation, plandab: bool, DisOnP: bool) -> bool: ...

@overload
def ChFiKPart_MakeChAsym(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, Pln: nanoocp.gp.gp_Pln, Cyl: nanoocp.gp.gp_Cylinder, fu: float, lu: float, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, Dis: float, Angle: float, Spine: nanoocp.gp.gp_Lin, First: float, Ofpl: nanoocp.TopAbs.TopAbs_Orientation, plandab: bool, DisOnP: bool) -> bool: ...

@overload
def ChFiKPart_MakeChAsym(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, Pl1: nanoocp.gp.gp_Pln, Pl2: nanoocp.gp.gp_Pln, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, Dis: float, Angle: float, Spine: nanoocp.gp.gp_Lin, First: float, Of1: nanoocp.TopAbs.TopAbs_Orientation, DisOnP1: bool) -> bool: ...

@overload
def ChFiKPart_MakeChamfer(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, theMode: nanoocp.ChFiDS.ChFiDS_ChamfMode, Pln: nanoocp.gp.gp_Pln, Con: nanoocp.gp.gp_Cone, fu: float, lu: float, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, Dis1: float, Dis2: float, Spine: nanoocp.gp.gp_Circ, First: float, Ofpl: nanoocp.TopAbs.TopAbs_Orientation, plandab: bool) -> bool: ...

@overload
def ChFiKPart_MakeChamfer(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, theMode: nanoocp.ChFiDS.ChFiDS_ChamfMode, Pln: nanoocp.gp.gp_Pln, Cyl: nanoocp.gp.gp_Cylinder, fu: float, lu: float, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, Dis1: float, Dis2: float, Spine: nanoocp.gp.gp_Circ, First: float, Ofpl: nanoocp.TopAbs.TopAbs_Orientation, plandab: bool) -> bool: ...

@overload
def ChFiKPart_MakeChamfer(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, theMode: nanoocp.ChFiDS.ChFiDS_ChamfMode, Pln: nanoocp.gp.gp_Pln, Cyl: nanoocp.gp.gp_Cylinder, fu: float, lu: float, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, Dis1: float, Dis2: float, Spine: nanoocp.gp.gp_Lin, First: float, Ofpl: nanoocp.TopAbs.TopAbs_Orientation, plandab: bool) -> bool: ...

@overload
def ChFiKPart_MakeChamfer(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, theMode: nanoocp.ChFiDS.ChFiDS_ChamfMode, Pl1: nanoocp.gp.gp_Pln, Pl2: nanoocp.gp.gp_Pln, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, Dis1: float, Dis2: float, Spine: nanoocp.gp.gp_Lin, First: float, Of1: nanoocp.TopAbs.TopAbs_Orientation) -> bool: ...

def ChFiKPart_CornerSpine(S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, P1S1: nanoocp.gp.gp_Pnt2d, P2S1: nanoocp.gp.gp_Pnt2d, P1S2: nanoocp.gp.gp_Pnt2d, P2S2: nanoocp.gp.gp_Pnt2d, R: float, cyl: nanoocp.gp.gp_Cylinder, circ: nanoocp.gp.gp_Circ) -> tuple[float, float]: ...

def ChFiKPart_InPeriod(U: float, UFirst: float, ULast: float, Eps: float) -> float: ...

def ChFiKPart_PCurve(UV1: nanoocp.gp.gp_Pnt2d, UV2: nanoocp.gp.gp_Pnt2d, Pardeb: float, Parfin: float) -> nanoocp.Geom2d.Geom2d_BSplineCurve: ...

def ChFiKPart_ProjPC(Cg: nanoocp.GeomAdaptor.GeomAdaptor_Curve, Sg: nanoocp.GeomAdaptor.GeomAdaptor_Surface) -> nanoocp.Geom2d.Geom2d_Curve: ...

def ChFiKPart_IndexCurveInDS(C: nanoocp.Geom.Geom_Curve | None, DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure) -> int: ...

def ChFiKPart_IndexSurfaceInDS(S: nanoocp.Geom.Geom_Surface | None, DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure) -> int: ...

@overload
def ChFiKPart_MakeFillet(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, Pln: nanoocp.gp.gp_Pln, Con: nanoocp.gp.gp_Cone, fu: float, lu: float, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, Radius: float, Spine: nanoocp.gp.gp_Circ, First: float, Ofpl: nanoocp.TopAbs.TopAbs_Orientation, plandab: bool) -> bool: ...

@overload
def ChFiKPart_MakeFillet(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, Pln: nanoocp.gp.gp_Pln, Cyl: nanoocp.gp.gp_Cylinder, fu: float, lu: float, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, Radius: float, Spine: nanoocp.gp.gp_Lin, First: float, Ofpl: nanoocp.TopAbs.TopAbs_Orientation, plandab: bool) -> bool: ...

@overload
def ChFiKPart_MakeFillet(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, Pln: nanoocp.gp.gp_Pln, Cyl: nanoocp.gp.gp_Cylinder, fu: float, lu: float, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, Radius: float, Spine: nanoocp.gp.gp_Circ, First: float, Ofpl: nanoocp.TopAbs.TopAbs_Orientation, plandab: bool) -> bool: ...

@overload
def ChFiKPart_MakeFillet(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, Pl1: nanoocp.gp.gp_Pln, Pl2: nanoocp.gp.gp_Pln, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, Radius: float, Spine: nanoocp.gp.gp_Lin, First: float, Of1: nanoocp.TopAbs.TopAbs_Orientation) -> bool: ...

def ChFiKPart_MakeRotule(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, pl: nanoocp.gp.gp_Pln, pl1: nanoocp.gp.gp_Pln, pl2: nanoocp.gp.gp_Pln, opl: nanoocp.TopAbs.TopAbs_Orientation, opl1: nanoocp.TopAbs.TopAbs_Orientation, opl2: nanoocp.TopAbs.TopAbs_Orientation, r: float, ofpl: nanoocp.TopAbs.TopAbs_Orientation) -> bool: ...

def ChFiKPart_Sphere(DStr: nanoocp.TopOpeBRepDS.TopOpeBRepDS_DataStructure, Data: nanoocp.ChFiDS.ChFiDS_SurfData | None, S1: nanoocp.Adaptor3d.Adaptor3d_Surface | None, S2: nanoocp.Adaptor3d.Adaptor3d_Surface | None, OrFace1: nanoocp.TopAbs.TopAbs_Orientation, OrFace2: nanoocp.TopAbs.TopAbs_Orientation, Or1: nanoocp.TopAbs.TopAbs_Orientation, Or2: nanoocp.TopAbs.TopAbs_Orientation, Rad: float, PS1: nanoocp.gp.gp_Pnt2d, P1S2: nanoocp.gp.gp_Pnt2d, P2S2: nanoocp.gp.gp_Pnt2d) -> bool: ...
