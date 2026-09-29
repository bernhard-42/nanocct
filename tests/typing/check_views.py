"""The zero-copy views (R-VIEW) are numpy's array protocol. `np.asarray(obj)` must type-check with the real
dtype where it is static, and `__array__` must be absent where it is absent at runtime.
"""
import numpy as np
from numpy.typing import NDArray

from nanocct import Image, NCollection, Poly, gp

# The container's __array__ is on the concrete class, not on the generic one: its dtype is the element's,
# and numpy's stubs carry it through np.asarray. Inferred first, assigned second: mypy accepts a wrong dtype in
# `x: NDArray[np.int32] = np.asarray(pnts)` although it infers float64 for np.asarray(pnts) (measured, numpy 2.5.3).
pnts = NCollection.NCollection_Array1__gp_Pnt(1, 3)
xyz = np.asarray(pnts)
exact: NDArray[np.float64] = xyz
wrong: NDArray[np.int32] = xyz                                  # error: float64 is not int32

tris = NCollection.NCollection_Array1__Poly_Triangle(1, 3)
idx: NDArray[np.int32] = np.asarray(tris)

grid = NCollection.NCollection_Array2__double(1, 2, 1, 3)
cells: NDArray[np.float64] = np.asarray(grid)

held = NCollection.NCollection_HArray1__double(1, 3, 0.0)      # inherited from the Array1 sibling
vals: NDArray[np.float64] = np.asarray(held)

normals: NDArray[np.float32] = np.asarray(Poly.Poly_Triangulation(3, 1, True, True).InternalNormals())

# The generic spelling has no __array__, so np.asarray gives an array of unknown dtype -- not an error.
generic = NCollection.NCollection_Array1[gp.gp_Pnt](1, 3)
anything = np.asarray(generic)

# An element type with nothing packed to view has no __array__, and the stub must say so rather than
# promising one for every NCollection_Array1[_T].
shapes = NCollection.NCollection_Array1__TopoDS_Shape(1, 2)
shapes.__array__()                                              # error: no such attribute

# A dtype decided at runtime (IsDoublePrecision(), the pixel format) is an array of unknown dtype.
nodes = np.asarray(Poly.Poly_Triangulation(3, 1, True, False).InternalNodes())
pix = np.asarray(Image.Image_PixMap())
buf: NDArray[np.uint8] = np.asarray(NCollection.NCollection_Buffer(
    NCollection.NCollection_BaseAllocator.CommonBaseAllocator_s()))
