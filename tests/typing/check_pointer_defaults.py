"""Static typing check for class pointer parameters, with and without a null default (run by mypy and ty, see tests/test_typing.py).
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
# ... and without a default (State.md 8.23): the 2D BuildCache's weights are `NCollection_Array1[float] | None`, still required
omitted.BuildCache(0.25, knots, poles, None)
omitted.BuildCache(0.25, knots, poles, weights)
omitted.BuildCache(0.25, knots, poles)                                  # error: the 2D overload has no default
