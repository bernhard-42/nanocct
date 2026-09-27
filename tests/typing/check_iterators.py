"""Binder Iterator classes are Python iterators (R-ITER); a class deriving from one (Graphic3d_SequenceOfHClipPlane::Iterator) too."""
from OCP3x.Graphic3d import Graphic3d_ClipPlane, Graphic3d_SequenceOfHClipPlane
from OCP3x.NCollection import NCollection_DataMap, NCollection_DataMap__int__double, NCollection_List, NCollection_List__int

lst = NCollection_List[int]()
it = NCollection_List__int.Iterator(lst)
v: int = it.Value()
for x in it:
    n: int = x
m = NCollection_DataMap[int, float]()
for f in NCollection_DataMap__int__double.Iterator(m):
    ff: float = f
seq = Graphic3d_SequenceOfHClipPlane()
for p in Graphic3d_SequenceOfHClipPlane.Iterator(seq):
    plane: Graphic3d_ClipPlane = p
