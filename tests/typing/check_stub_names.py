"""Static typing check for names the stubs spelled unresolvably until State.md 8.22 (b) (run by mypy and ty, see tests/test_typing.py).
Lines with a trailing `# error:` comment must be reported; everything else must pass. Before the fix mypy saw both results as
unresolved, i.e. Any, and reported neither error line (ty resolved them already)."""
from nanocct import BRepGraphInc, NCollection, OpenGl, TCollection


def shared(ctx: OpenGl.OpenGl_Context) -> None:
    # NCollection_Shared<T> as a result: the concrete class (it derives from T's class), not the lookup object's name
    res: NCollection.NCollection_DataMap[TCollection.TCollection_AsciiString, OpenGl.OpenGl_Resource] = ctx.SharedResources()
    wrong: int = ctx.SharedResources()                                     # error: a DataMap is not an int


def storage(s: BRepGraphInc.BRepGraphInc_Storage, i: BRepGraphInc.BRepGraph_EdgeCurve3DRepId) -> None:
    # the module's class EdgeCurve3DRep, whose name a method of BRepGraphInc_Storage shadows inside the class body
    rep: BRepGraphInc.EdgeCurve3DRep = s.ChangeEdgeCurve3DRep(i)
    wrong: int = s.ChangeEdgeCurve3DRep(i)                                 # error: EdgeCurve3DRep is not an int
