"""Static typing check for names the stubs spelled unresolvably until State.md 8.22 (b) (run by mypy and ty, see tests/test_typing.py).
Lines with a trailing `# error:` comment must be reported; everything else must pass. Before the fix mypy saw both results as
unresolved, i.e. Any, and reported neither error line (ty resolved them already)."""
from nanocct import AIS, BRepGraphInc, GProp, Graphic3d, Image, NCollection, OpenGl, StepVisual, TCollection


def shared(ctx: OpenGl.OpenGl_Context) -> None:
    # NCollection_Shared<T> as a result: the concrete class (it derives from T's class), not the lookup object's name
    res: NCollection.NCollection_DataMap[TCollection.TCollection_AsciiString, OpenGl.OpenGl_Resource] = ctx.SharedResources()
    wrong: int = ctx.SharedResources()                                     # error: a DataMap is not an int


def storage(s: BRepGraphInc.BRepGraphInc_Storage, i: BRepGraphInc.BRepGraph_EdgeCurve3DRepId) -> None:
    # the module's class EdgeCurve3DRep, whose name a method of BRepGraphInc_Storage shadows inside the class body
    rep: BRepGraphInc.EdgeCurve3DRep = s.ChangeEdgeCurve3DRep(i)
    wrong: int = s.ChangeEdgeCurve3DRep(i)                                 # error: EdgeCurve3DRep is not an int


def vec(rgba: Graphic3d.NCollection_Vec4__unsigned_char) -> None:
    # a result that is another instantiation of the template (6c follows the members of an instantiation): it used to be
    # the quoted C++ spelling "NCollection_Vec3<unsigned char>", i.e. Any
    rgb: Graphic3d.NCollection_Vec3__unsigned_char = rgba.xyz()
    wrong: int = rgba.xyz()                                                # error: a Vec3 is not an int


def tessellated(geo: StepVisual.StepVisual_TessellatedGeometricSet) -> None:
    # NCollection_Handle<X> is X (R-NCHANDLE): it used to be the quoted C++ spelling, i.e. Any
    items: NCollection.NCollection_Array1[StepVisual.StepVisual_TessellatedItem] = geo.Items()
    geo.Init(TCollection.TCollection_HAsciiString("set"), None)            # a null handle
    wrong: int = geo.Items()                                               # error: an array is not an int


def underscore_names(buffer: AIS.AIS_ViewInputBuffer, rgba: Image.Image_ColorRGB32) -> None:
    # names that start or end with one underscore are C++ names, not private ones (stubgen include_private, State.md 8.22 (vi)):
    # the R-KEYWORD enum value None_, OCCT's own a_(), the nested struct AIS_ViewInputBuffer::_orientation
    kind: GProp.GProp_PEquation.Type = GProp.GProp_PEquation.Type.None_
    alpha: int = rgba.a_()
    orient: AIS.AIS_ViewInputBuffer._orientation = buffer.Orientation
    fit: bool = orient.ToFitAll
    wrong: int = buffer.Orientation                                        # error: a struct is not an int

