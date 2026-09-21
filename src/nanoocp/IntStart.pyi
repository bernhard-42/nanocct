"""OCCT package IntStart (toolkit TKGeomAlgo)"""

import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.gp


class IntStart_SITopolTool(nanoocp.Standard.Standard_Transient):
    """
    template class for a topological tool.
    This tool is linked with the surface on which
    the classification has to be made.
    """

    def Classify(self, P: nanoocp.gp.gp_Pnt2d, Tol: float) -> nanoocp.TopAbs.TopAbs_State: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
