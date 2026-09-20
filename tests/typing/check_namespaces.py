"""Static typing check for nested classes and C++ namespaces (run by mypy and ty, see tests/test_typing.py).
Lines with a trailing `# error:` comment must be reported; everything else must pass."""
import nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc
from nanoocp import Geom2d, Geom2dEval, Geom2dGridEval, NCollection, gp
from nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc import Base, Full

circle = Geom2d.Geom2d_Circle(gp.gp_Ax2d(), 2.0)
r: Geom2d.Geom2d_Curve.ResD1 = circle.EvalD1(0.0)                  # nested struct
pt: gp.gp_Pnt2d = r.Point
bad: gp.gp_Pnt = r.Point                                            # error: gp_Pnt2d is not gp_Pnt

poles = NCollection.NCollection_Array1[gp.gp_Pnt2d](1, 3)
bezier = Geom2d.Geom2d_BezierCurve(poles)                           # NCollection_Array1[T] accepted where OCCT wants the array
desc: Base | None = bezier.EvalRepresentation()                     # class in a namespace, null handle -> None
kind: Base.Kind = Full().GetKind()
same: nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base = Full()
also: Geom2dEval.Geom2dEval_RepCurveDesc.Base = Full()
wrong: Full = Base()                                                # error: Base is not Full

grid = Geom2dGridEval.Geom2dGridEval_Circle(circle).EvaluateGridD1(NCollection.NCollection_Array1[float](1, 2))
first: Geom2dGridEval.CurveD1 = grid.Value(1)                       # namespace named like the package
arr: NCollection.NCollection_Array1[Geom2dGridEval.CurveD1] = grid
d1: gp.gp_Vec2d = first.D1
