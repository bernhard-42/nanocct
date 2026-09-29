"""Static typing check for pointer parameters with a null default (run by mypy and ty, see tests/test_typing.py).
Lines with a trailing `# error:` comment must be reported; everything else must pass."""
from nanocct import BSplCLib, NCollection, gp

knots = NCollection.NCollection_Array1[float](1, 4)
poles = NCollection.NCollection_Array1[gp.gp_Pnt2d](1, 2)
weights = NCollection.NCollection_Array1[float](1, 2)
# R-PTR-NULL (State.md 8.22): const NCollection_Array1<double>* theWeights = nullptr is `NCollection_Array1[float] | None = None`
omitted = BSplCLib.BSplCLib_Cache(1, False, knots, poles)
explicit = BSplCLib.BSplCLib_Cache(1, False, knots, poles, None)
rational = BSplCLib.BSplCLib_Cache(1, False, knots, poles, weights)
wrong = BSplCLib.BSplCLib_Cache(1, False, knots, poles, 1.0)             # error: a float is not a weights array
