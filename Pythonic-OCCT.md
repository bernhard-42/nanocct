# Pythonic addition to the OCCT bindings

## NCollections

**Design: [2a Naming conventions](Design.md#2a-naming-conventions), [6a NCollection containers](Design.md#6a-ncollection-containers-hand-written-binders)**

### Generics support

Let's look at the C++ example `NCollection_Array1<gp_Dir>`:

The nanocct generator binds this as a class `NCollection_Array1__gp_Dir`

```python
from nanocct.NCollection import NCollection_Array1__gp_Dir

a = NCollection_Array1__gp_Dir(1, 3)
```

and adds a Python generics type definition to it

```python
from nanocct.gp import gp_Dir
from nanocct.NCollection import NCollection_Array1

b = NCollection_Array1[gp_Dir](1, 3)
```

1. The two constructs are the same type

   ```python
   In[1]: NCollection_Array1__gp_Dir is NCollection_Array1[gp_Dir]
   Out[1]: True
   ```

2. Different element types are different classes

   ```python
   In[2]: NCollection_Array1[gp_Dir] is NCollection_Array1[int]
   Out[2]: False
   ```

3. `isinstance` can be used with both types

   ```python
   In[3]: isinstance(a, NCollection_Array1)
   Out[3]: True

   In[4]: isinstance(b, NCollection_Array1)
   Out[4]: True

   In[5]: isinstance(a, NCollection_Array1__gp_Dir)
   Out[5]: True

   In[6]: isinstance(b, NCollection_Array1__gp_Dir)
   Out[6]: True

   In[7]: type(a) is type(b)
   Out[7]: True
   ```

4. There is a minimal overhead using generic types:

   ```python
   In [8]: %timeit NCollection_Array1__gp_Dir(1, 3)
   42.9 ns ± 0.575 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

   In [9]: %timeit NCollection_Array1[gp_Dir](1, 3)
   79.2 ns ± 1.84 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
   ```

   | Statement                          | Timing             |
   | ---------------------------------- | ------------------ |
   | `NCollection_Array1__gp_Dir(1, 3)` | 42.9 ns ± 0.575 ns |
   | `NCollection_Array1[gp_Dir](1, 3)` | 79.2 ns ± 1.84 ns  |

   Typically, the NCollections don't appear in large loops where the nanoseconds could pile up, but are created once and then filled in a loop. Since both statements create the same type at runtime, accessing the NCollections takes the same time.

### C++ scalar types

A Python type stands for a C++ template argument: `float` for C++ `double`, `int`, `bool`, and `str` for `std::string`. Python has no own type for five more C++ scalars used in OCCT 8, so `nanocct.NCollection` exports a marker for each:

| Marker      | C++ type             |
| ----------- | -------------------- |
| `float32`   | `float` (32-bit)     |
| `uchar`     | `unsigned char`      |
| `uint`      | `unsigned int`       |
| `ulong`     | `unsigned long`      |
| `ulonglong` | `unsigned long long` |

With them, every NCollection class of nanocct can be spelled generically:

```python
In [1]: from nanocct.NCollection import NCollection_Array1, NCollection_HArray1, float32, uchar
   ...: from nanocct.Poly import Poly_Triangulation

In [2]: NCollection_HArray1[float32].__name__, NCollection_HArray1[uchar].__name__
Out[2]: ('NCollection_HArray1__float', 'NCollection_HArray1__unsigned_char')

In [3]: NCollection_Array1[float].__name__
Out[3]: 'NCollection_Array1__double'
```

The markers are only keys. The values are plain Python floats and ints, and the C++ class does the conversion, e.g. the rounding to 32 bits:

```python
In [4]: normals = NCollection_HArray1[float32](1, 9, 0.0)   # 3 nodes, x y z each
   ...: normals.SetValue(1, 0.1)
   ...: normals.Value(1)
Out[4]: 0.10000000149011612

In [5]: tri = Poly_Triangulation(3, 1, False, False)
   ...: tri.SetNormals(normals)
   ...: tri.HasNormals()
Out[5]: True
```

For type checkers the markers are aliases of `float` and `int`: precision is not a Python type, the same as for every other C++ `float` or `unsigned int` parameter of the bindings. So a type checker does not tell `NCollection_HArray1[float32]` from `NCollection_HArray1[float]`; handing the wrong one to OCCT fails at runtime with a `TypeError`.

### numpy zero-copy support

The nanocct generator gives e.g. `NCollection_Array1` and `NCollection_Array2` numpy's array protocol, `__array__`, see [details](#numpy-zero-copy-support-in-detail).

```python
In [1]: from nanocct.NCollection import NCollection_Array1
   ...: from nanocct.gp import gp_Vec
   ...: import numpy as np
   ...:
   ...: a = NCollection_Array1[gp_Vec](1, 3)
   ...:
   ...: a.SetValue(1, gp_Vec(1, 0, 0))
   ...: a.SetValue(2, gp_Vec(0, 1, 0))
   ...: a.SetValue(3, gp_Vec(0, 0, 1))

In [2]: np.asarray(a)
Out[2]:
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
```

This accesses the C++ values from Python without copying them (zero-copy access)

### Index access

`a[i]` makes OCCT's item access available with OCCT's index, and nothing more: `NCollection_Array1` counts from `Lower()`, `NCollection_Sequence` and the indexed maps from 1, `NCollection_DynamicArray` and `NCollection_LinearVector` from 0. There are no negative indices and no slices, because a negative index is a real OCCT index for an array like `NCollection_Array1[float](-2, 2)`. For Python-style indexing, use a numpy view or a list:

```python
In [1]: import numpy as np
   ...: from nanocct.NCollection import NCollection_Array1
   ...:
   ...: a = NCollection_Array1[float](1, 8)
   ...: for i in range(1, 9):
   ...:     a.SetValue(i, i * 10.0)

In [2]: a[1], a[3]
Out[2]: (10.0, 30.0)

In [3]: a.Last(), np.asarray(a)[-1], list(a)[-1]
Out[3]: (80.0, np.float64(80.0), 80.0)
```

OCCT's own `At(i)` is 0-based like `np.asarray(a)[i]`, and range-checked: `NCollection_Array1`, `NCollection_Array2` (`At(row, col)`) and `NCollection_Sequence` have it, together with their `HArray`/`HSequence` variants. Unlike a numpy view, it works for every element type, e.g. an array of `TopoDS_Shape`. It takes no negative index.

```python
In [4]: a.At(0), a.At(2)
Out[4]: (10.0, 30.0)

In [5]: list(a)[0], np.asarray(a)[2]
Out[5]: (10.0, np.float64(30.0))
```

Timing

```python
In [6]: %timeit a.Value(3)
17 ns ± 0.0779 ns per loop (mean ± std. dev. of 7 runs, 100,000,000 loops each)

In [7]: %timeit a[3]
19.7 ns ± 0.257 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
```

| Statement    | Timing             |
| ------------ | ------------------ |
| `a.Value(3)` | 17 ns ± 0.0779 ns  |
| `a[3]`       | 19.7 ns ± 0.257 ns |

**Note:** nanocct keeps OCCT's C++ contract for index access and adds no checks of its own. Where OCCT checks the range, an out-of-range index raises `Standard_OutOfRange` (`a[0]` above). Where OCCT does not, it behaves as in C++: `NCollection_DynamicArray`'s `Value`, `ChangeValue` and `d[i]`, or `NCollection_Mat4.GetValue`, read whatever memory lies past the end, and can crash the Python interpreter.

### Iterating over NCollections

- 100 `float` element `NCollection`

  ```python
  In [1]: import numpy as np
     ...: from nanocct.NCollection import NCollection_Array1
     ...:
     ...: N = 100
     ...: a = NCollection_Array1[float](1, N)
     ...: for i in range(1, N+1):
     ...:     a.SetValue(i, i * 10.0)
     ...:

  In [2]: %timeit [a.Value(i) for i in range(1, N + 1)]
  2.06 μs ± 14.9 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

  In [3]: %timeit list(a)
  1.17 μs ± 11.2 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
  ```

- 10 `float` element `NCollection`

  ```python
  In [4]: N = 10
     ...: a = NCollection_Array1[float](1, N)
     ...: for i in range(1, N+1):
     ...:     a.SetValue(i, i * 10.0)
     ...:

  In [5]: %timeit [a.Value(i) for i in range(1, N + 1)]
  248 ns ± 2.55 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

  In [6]: %timeit list(a)
  221 ns ± 2.69 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
  ```

| Statement                               | 100 elements      | 10 elements      |
| --------------------------------------- | ----------------- | ---------------- |
| `[a.Value(i) for i in range(1, N + 1)]` | 2.06 μs ± 14.9 ns | 248 ns ± 2.55 ns |
| `list(a)`                               | 1.17 μs ± 11.2 ns | 221 ns ± 2.69 ns |

Below 7 or 8 elements, `list(a)` gets slightly slower due to the creating the iterator.

### Uninitialised values

Like in C++, a new array of a scalar type (`float`, `int`, `bool`, `float32`, …) is not initialised: OCCT allocates the memory and leaves it as it is. It often reads as `0.0`, but that is chance, and a larger array can show values left over from earlier allocations. Class elements such as `gp_Vec` are default-constructed. Use OCCT's `Init(value)`, or the fill value of the `NCollection_HArray1` constructor:

```python
In [1]: from nanocct.NCollection import NCollection_Array1, NCollection_HArray1
   ...: from nanocct.gp import gp_Vec
   ...:
   ...: a = NCollection_Array1[float](1, 3)
   ...: a.Init(0.0)
   ...: list(a)
Out[1]: [0.0, 0.0, 0.0]

In [2]: list(NCollection_HArray1[float](1, 3, 0.5))
Out[2]: [0.5, 0.5, 0.5]

In [3]: [v.Coord() for v in NCollection_Array1[gp_Vec](1, 2)]
Out[3]: [(0.0, 0.0, 0.0), (0.0, 0.0, 0.0)]
```

## Iterating over OCCT iterators

**Binding rule: R-ITER ([Design 2c](Design.md#2c-python-additions))**

Every OCCT class with `More()`, `Next()` and a `Current()` or `Value()` is a Python iterable: `TopExp_Explorer`, `TopoDS_Iterator`, `BRepTools_WireExplorer` and the other OCCT iterators, and the `Iterator` classes of the NCollections. A `for` loop runs OCCT's own `More()`/`Next()` loop and yields `Current()` (or `Value()`).

```python
In [1]: from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
   ...: from nanocct.TopExp import TopExp, TopExp_Explorer
   ...: from nanocct.TopAbs import TopAbs_ShapeEnum
   ...: from nanocct.TopoDS import TopoDS_Iterator, TopoDS_Shape
   ...: from nanocct.TopTools import TopTools_ShapeMapHasher
   ...: from nanocct.NCollection import NCollection_IndexedMap
   ...:
   ...: FACE, EDGE = TopAbs_ShapeEnum.TopAbs_FACE, TopAbs_ShapeEnum.TopAbs_EDGE
   ...: box = BRepPrimAPI_MakeBox(1, 2, 3).Shape()

In [2]: [f.ShapeType().name for f in TopExp_Explorer(box, FACE)]
Out[2]: ['TopAbs_FACE', 'TopAbs_FACE', 'TopAbs_FACE', 'TopAbs_FACE', 'TopAbs_FACE', 'TopAbs_FACE']

In [3]: [c.ShapeType().name for c in TopoDS_Iterator(box)]
Out[3]: ['TopAbs_SHELL']
```

The loop advances the iterator object itself, so it is used up afterwards, like a file. OCCT's `ReInit()` starts it again:

```python
In [4]: ex = TopExp_Explorer(box, FACE)
   ...: len(list(ex)), len(list(ex))
Out[4]: (6, 0)

In [5]: ex.ReInit()
   ...: len(list(ex))
Out[5]: 6
```

An explorer visits a shared sub-shape once for every shape it belongs to: each edge of a box is part of two faces. `TopExp.MapShapes` collects each sub-shape once (OCCT's shape maps compare with `IsSame`):

```python
In [6]: edges = NCollection_IndexedMap[TopoDS_Shape, TopTools_ShapeMapHasher]()
   ...: TopExp.MapShapes_s(box, EDGE, edges)
   ...: len(list(TopExp_Explorer(box, EDGE))), edges.Size()
Out[6]: (24, 12)
```

### Timings

A compound of 100 boxes (600 faces, 2400 edge visits, 1200 distinct edges):

```python
In [7]: from nanocct.BRep import BRep_Builder
   ...: from nanocct.TopoDS import TopoDS_Compound
   ...:
   ...: builder, comp = BRep_Builder(), TopoDS_Compound()
   ...: builder.MakeCompound(comp)
   ...: for i in range(100):
   ...:     builder.Add(comp, BRepPrimAPI_MakeBox(1, 1, 1).Shape())

In [8]: %%timeit
   ...: ex, out = TopExp_Explorer(comp, EDGE), []
   ...: while ex.More():
   ...:     out.append(ex.Current())
   ...:     ex.Next()
155 μs ± 929 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [9]: %timeit [e for e in TopExp_Explorer(comp, EDGE)]
122 μs ± 781 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [10]: %timeit list(TopExp_Explorer(comp, EDGE))
114 μs ± 616 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [11]: %%timeit
    ...: m = NCollection_IndexedMap[TopoDS_Shape, TopTools_ShapeMapHasher]()
    ...: TopExp.MapShapes_s(comp, EDGE, m)
    ...: list(m)
106 μs ± 735 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
```

| Statement                                                                                                         | Timing                              |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `ex, out = TopExp_Explorer(comp, EDGE), []; while ex.More(): out.append(ex.Current()); ex.Next()`                 | 155&nbsp;μs&nbsp;±&nbsp;929&nbsp;ns |
| `[e for e in TopExp_Explorer(comp, EDGE)]`                                                                        | 122&nbsp;μs&nbsp;±&nbsp;781&nbsp;ns |
| `list(TopExp_Explorer(comp, EDGE))`                                                                               | 114&nbsp;μs&nbsp;±&nbsp;616&nbsp;ns |
| `m = NCollection_IndexedMap[TopoDS_Shape, TopTools_ShapeMapHasher](); TopExp.MapShapes_s(comp, EDGE, m); list(m)` | 106&nbsp;μs&nbsp;±&nbsp;735&nbsp;ns |

A `for` loop or `list()` is about 20–25 % faster than a hand-written `More()`/`Next()` loop. `TopExp.MapShapes` is the fastest here, although it also removes the duplicates: the traversal runs in one C++ call, and it returns 1 200 instead of 2 400 shapes.

## numpy zero-copy support in detail

**Binding rule: R-VIEW ([Design 2c](Design.md#2c-python-additions))**

### Support for the numpy array protocol

The nanocct generator gives `NCollection_Array1` and `NCollection_Array2` (and their `HArray1`/`HArray2` variants) numpy's array protocol, `__array__`, for every element type that is a packed run of numpy scalars: the C++ scalars `double`, `float`, `int`, `bool`, `unsigned char`, `gp_Pnt`, `gp_Vec`, `gp_Dir`, `gp_XYZ`, their 2d counterparts, `Poly_Triangle` and the `NCollection_Vec2/3/4` types. `Poly_ArrayOfNodes`, `Poly_ArrayOfUVNodes`, `Image_PixMap` and `NCollection_Buffer` have it too. This allows to access large C++ arrays from Python with zero-copy:

- `np.asarray(a)` is a view of OCCT's own memory: no copy, and writes go straight into the OCCT array.
- `np.array(a)` is an independent copy.

Collections without a packed element type (an `NCollection_Array1` of `TopoDS_Shape`, maps, lists, sequences) have no `__array__`.

```python
In [1]: from nanocct.NCollection import NCollection_Array1
   ...: from nanocct.gp import gp_Vec
   ...: import numpy as np
   ...:
   ...: a = NCollection_Array1[gp_Vec](1, 3)
   ...:
   ...: a.SetValue(1, gp_Vec(1, 0, 0))
   ...: a.SetValue(2, gp_Vec(0, 1, 0))
   ...: a.SetValue(3, gp_Vec(0, 0, 1))

In [2]: v = np.asarray(a)
   ...: v
Out[2]:
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])

In [3]: v[0, 0] = 42.0
   ...: a.Value(1).X()
Out[3]: 42.0

In [4]: c = np.array(a)
   ...: c[0, 0] = 7.0
   ...: a.Value(1).X()
Out[4]: 42.0
```

Let's make a little benchmark

```python
In [1]: from nanocct.NCollection import NCollection_Array1
   ...: from nanocct.gp import gp_Vec
   ...: import numpy as np
   ...:
   ...: N = 1000000
   ...: a = NCollection_Array1[gp_Vec](1, N)
   ...:
   ...: for i in range(1, N + 1):
   ...:     a.SetValue(i, gp_Vec(i, i/10, i/100))
   ...:
```

To access the vectors as python tuples, one uses:

```python
In [2]: %timeit [a.Value(i).Coord() for i in range(1, N + 1)]
99.9 ms ± 2.47 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [3]: %timeit np.asarray(a)  # zero copy
233 ns ± 1.91 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

In [4]: %timeit np.array(a)
328 μs ± 6.35 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

| Statement                                       | Timing            |
| ----------------------------------------------- | ----------------- |
| `[a.Value(i).Coord() for i in range(1, N + 1)]` | 99.9 ms ± 2.47 ms |
| `np.array(a)`                                   | 328 μs ± 6.35 μs  |
| `np.asarray(a)` (zero copy)                     | 233 ns ± 1.91 ns  |

`np.asarray(a)` only creates the view, so its time does not depend on the size of the array; `np.array(a)` copies all 24 MB.

Finally, compare some values:

```python
In [5]: p = [a.Value(i).Coord() for i in range(1, N + 1)]
   ...: p[0:3]
Out[5]: [(1.0, 0.1, 0.01), (2.0, 0.2, 0.02), (3.0, 0.3, 0.03)]

In [6]: q = np.asarray(a)
   ...: q[0:3]
Out[6]:
array([[1.  , 0.1 , 0.01],
       [2.  , 0.2 , 0.02],
       [3.  , 0.3 , 0.03]])
```

### Special case: Triangulations

A `Poly_Triangulation` holds four arrays: nodes, triangles, UV nodes and normals. OCCT's own accessors `InternalNodes()`, `InternalTriangles()`, `InternalUVNodes()` and `InternalNormals()` return references to the triangulation's storage, and `np.asarray` turns each into a zero-copy view.

```python
In [1]: import numpy as np
   ...: from nanocct.BRep import BRep_Tool
   ...: from nanocct.BRepMesh import BRepMesh_IncrementalMesh
   ...: from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
   ...: from nanocct.TopAbs import TopAbs_ShapeEnum
   ...: from nanocct.TopExp import TopExp_Explorer
   ...: from nanocct.TopLoc import TopLoc_Location
   ...: import nanocct.TopoDS as TopoDS
   ...:
   ...: box = BRepPrimAPI_MakeBox(10.0, 20.0, 30.0).Shape()
   ...: BRepMesh_IncrementalMesh(box, 0.1)
   ...: face = TopoDS.Face(TopExp_Explorer(box, TopAbs_ShapeEnum.TopAbs_FACE).Current())
   ...: tri = BRep_Tool.Triangulation_s(face, TopLoc_Location())

In [2]: tri.NbNodes(), tri.NbTriangles()
Out[2]: (4, 2)

In [3]: nodes = np.asarray(tri.InternalNodes())
   ...: nodes
Out[3]:
array([[ 0.,  0.,  0.],
       [ 0.,  0., 30.],
       [ 0., 20.,  0.],
       [ 0., 20., 30.]])

In [4]: tris = np.asarray(tri.InternalTriangles())
   ...: tris
Out[4]:
array([[2, 1, 3],
       [2, 3, 4]], dtype=int32)
```

The triangle indices are OCCT's and therefore **1-based**. To correlate them correctly, subtract 1 to index the nodes, e.g. to get the corner coordinates of every triangle:

```python
In [5]: nodes[tris - 1][0]  # align to the 1-based C++ indices
Out[5]:
array([[ 0.,  0., 30.],
       [ 0.,  0.,  0.],
       [ 0., 20.,  0.]])
```

UV nodes and normals are optional. When a triangulation has none, the array is empty, and OCCT's `HasUVNodes()`/`HasNormals()` tell whether they are there:

```python
In [6]: tri.HasUVNodes(), tri.HasNormals()
Out[6]: (True, False)

In [7]: np.asarray(tri.InternalUVNodes())
Out[7]:
array([[  0.,   0.],
       [ 30.,   0.],
       [  0., -20.],
       [ 30., -20.]])

In [8]: np.asarray(tri.InternalNormals())
Out[8]: array([], shape=(0, 3), dtype=float32)
```

Only a non-const reference is zero-copy. An OCCT accessor that returns a `const` reference, such as `Triangles()`, is bound as a copy, so `np.asarray` on it views that copy and writes never reach the triangulation:

```python
In [9]: copy = np.asarray(tri.Triangles())
   ...: copy[0] = [1, 1, 1]
   ...: tri.Triangle(1).Get()
Out[9]: (2, 1, 3)

In [10]: view = np.asarray(tri.InternalTriangles())
    ...: view[0] = [1, 1, 1]
    ...: tri.Triangle(1).Get()
Out[10]: (1, 1, 1)
```

## Mutable primitive references

**Binding rule: R-REF-PRIMITIVE ([Design 2c](Design.md#2c-python-additions))**

Many OCCT settings are a method that returns a writable reference to a number, e.g. `int& ShapeFix_Face::FixWireMode()`. In C++ the value is set by assigning to the result, `face.FixWireMode() = 0;`. Python has no references to numbers, so nanocct keeps the getter under its OCCT name and adds a setter: `Set<Name>`, with a `Change` prefix dropped (`ChangeValue` → `SetValue`), unless OCCT already has a method of that name. Its docstring starts with "Python addition".

```python
In [1]: from nanocct.ShapeFix import ShapeFix_Face
   ...: from nanocct.math import math_Matrix
   ...:
   ...: face = ShapeFix_Face()
   ...: face.FixWireMode()
Out[1]: -1

In [2]: face.SetFixWireMode(0)
   ...: face.FixWireMode()
Out[2]: 0
```

Assigning the getter's result to a variable only changes the variable: `x = face.FixWireMode(); x = 1` leaves the face untouched.

The same rule covers references with arguments, like `double& math_Matrix::Value(int, int)`, and the C++ operators `()` and `[]`: their setter is `__setitem__`, with a tuple for several indices.

```python
In [3]: m = math_Matrix(1, 2, 1, 2, 0.0)
   ...: m.SetValue(1, 2, 5.0)
   ...: m.Value(1, 2)
Out[3]: 5.0

In [4]: m[(2, 1)] = 7.0
   ...: m(2, 1), m.Value(2, 1)
Out[4]: (7.0, 7.0)
```

## Operators

**Binding rules: R-OPERATOR, R-IOP, R-FREE-OP, R-STR ([Design 2c](Design.md#2c-python-additions))**

C++ operators become the matching Python special methods, and they keep OCCT's meaning:

| Types                                           | C++                                                   | Python                     | OCCT's meaning                                                                                                           |
| ----------------------------------------------- | ----------------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `gp_Vec v, v1, v2`                              | `v1 + v2`, `v * 2.0`, `-v`                            | `v1 + v2`, `v * 2.0`, `-v` | `Added`, `Multiplied`, `Reversed` (a `gp_Vec`)                                                                           |
| `gp_Vec v`                                      | `2.0 * v` (a free `operator*(double, const gp_Vec&)`) | `2.0 * v`                  | `Multiplied` (a `gp_Vec`)                                                                                                |
| `gp_Vec v1, v2`                                 | `v1 * v2`                                             | `v1 * v2`                  | `Dot`: a `double` / `float`, not an element-wise product                                                                 |
| `gp_Vec v1, v2`                                 | `v1 ^ v2`                                             | `v1 ^ v2`                  | `Crossed` (a `gp_Vec`)                                                                                                   |
| `gp_Vec v1, v2`                                 | `v1 += v2` (returns `void`)                           | `v1 += v2`                 | `Add`: changes `v1`, which stays the same object                                                                         |
| `TopoDS_Shape s1, s2`                           | `s1 == s2`                                            | `s1 == s2`                 | `IsEqual`: the same shape, location and orientation, not the same geometry, see [Equality](#equality-in-occt-and-python) |
| `math_Matrix m`, `NCollection_Array1<double> a` | `m(1, 1)`, `a[i]`                                     | `m(1, 1)`, `a[i]`          | OCCT's `operator()`, `operator[]`                                                                                        |
| `math_Matrix m`                                 | `std::cout << m`                                      | `str(m)`, `print(m)`       | OCCT's own text; `repr(m)` stays Python's default                                                                        |

```python
In [1]: from nanocct.gp import gp_Pnt, gp_Vec
   ...: from nanocct.math import math_Matrix
   ...: from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
   ...:
   ...: v1, v2 = gp_Vec(1, 2, 3), gp_Vec(4, 5, 6)
   ...: (v1 + v2).Coord(), (2.0 * v1).Coord()
Out[1]: ((5.0, 7.0, 9.0), (2.0, 4.0, 6.0))

In [2]: v1 * v2, (v1 ^ v2).Coord()
Out[2]: (32.0, (-3.0, 6.0, -3.0))

In [3]: v = gp_Vec(1, 1, 1)
   ...: before = id(v)
   ...: v += v2
   ...: v.Coord(), id(v) == before
Out[3]: ((5.0, 6.0, 7.0), True)

In [4]: box = BRepPrimAPI_MakeBox(1, 1, 1).Shape()
   ...: box == box, box == BRepPrimAPI_MakeBox(1, 1, 1).Shape()
Out[4]: (True, False)

In [5]: str(math_Matrix(1, 2, 1, 2, 1.5)).splitlines()[0]
Out[5]: 'math_Matrix of RowNumber = 2 and ColNumber = 2'
```

A class without an OCCT `operator==` compares by identity, as any Python object does. `gp_Pnt` is one of them; OCCT compares points with a tolerance:

```python
In [6]: p1, p2 = gp_Pnt(1, 2, 3), gp_Pnt(1, 2, 3)
   ...: p1 == p2, p1.IsEqual(p2, 1e-7)
Out[6]: (False, True)
```

## Equality in OCCT and Python

### Python level

| Term     | Test      | Meaning                                                                                                                                                |
| -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| identity | `a is b`  | the same _Python object_. nanocct creates a new Python object for every value it returns, so a face fetched twice is two objects: `f2 is f` → `False`. |
| equality | `a == b`  | whatever the class's `__eq__` says. A class without `__eq__` falls back to identity.                                                                   |
| hash     | `hash(a)` | a dict or set first compares hashes, then `==`. Python requires that `a == b` implies `hash(a) == hash(b)`.                                            |

### OCCT, for shapes

A `TopoDS_Shape` is a triple: a pointer to the underlying topology (the `TShape`), a `Location` (a placement) and an `Orientation`.

| Term                                          | Compares                                                                                   |
| --------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `IsPartner`                                   | the same `TShape`                                                                          |
| `IsSame`                                      | the same `TShape` and `Location`; orientation may differ                                   |
| `IsEqual` = `operator==`                      | the same `TShape`, `Location` **and** `Orientation`                                        |
| `std::hash<TopoDS_Shape>`                     | `TShape` pointer and `Location`, _not_ orientation, so it fits both `IsSame` and `IsEqual` |
| `TopTools_ShapeMapHasher` (OCCT's shape maps) | that hash, with **`IsSame`** as equality                                                   |

### C++ and Python side by side

Everything except `is` is OCCT's own API, under the same name in both languages; the operators call OCCT's methods.

| Name           | C++ (OCCT)                                                                                    | Python (nanocct)                                                                                                                                                                                                      |
| -------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `is`           | — (closest: comparing addresses, `&a == &b`)                                                  | Python's own operator: the same Python object                                                                                                                                                                         |
| `IsPartner`    | `TopoDS_Shape::IsPartner`                                                                     | `f.IsPartner(g)`                                                                                                                                                                                                      |
| `IsSame`       | `TopoDS_Shape::IsSame`                                                                        | `f.IsSame(g)`                                                                                                                                                                                                         |
| `IsEqual`      | `TopoDS_Shape::IsEqual`                                                                       | `f.IsEqual(g)`                                                                                                                                                                                                        |
| `IsNotEqual`   | `TopoDS_Shape::IsNotEqual`                                                                    | `f.IsNotEqual(g)`                                                                                                                                                                                                     |
| `==`           | `operator==`, defined as `IsEqual`                                                            | `f == g`, which calls `IsEqual`                                                                                                                                                                                       |
| `!=`           | `operator!=`, defined as `IsNotEqual`                                                         | `f != g`, which calls `IsNotEqual`                                                                                                                                                                                    |
| hash           | `std::hash<TopoDS_Shape>`, used by `std::unordered_*` containers, an unsigned 64-bit `size_t` | `hash(f)`: the same 64-bit value, read as a signed integer (a value ≥ 2⁶³ shows as negative; CPython reports the one value −1 as −2). It hashes the `TShape` pointer, so it changes from run to run in both languages |
| map membership | `Contains` of an OCCT map with `TopTools_ShapeMapHasher`                                      | `m.Contains(g)`                                                                                                                                                                                                       |

Compared with face `f` of a box:

| `g`, compared with `f`              | `g is f` | `IsPartner` | `IsSame` | `IsEqual`/`==` | same hash |
| ----------------------------------- | -------- | ----------- | -------- | -------------- | --------- |
| the same face, fetched again        | False    | True        | True     | True           | True      |
| `f.Reversed()`                      | False    | True        | True     | False          | True      |
| `f.Moved(loc)`                      | False    | True        | False    | False          | False     |
| the face of a second, identical box | False    | False       | False    | False          | False     |

### Shapes as dict keys and in OCCT maps

A Python dict and OCCT's shape maps (`NCollection_IndexedMap[TopoDS_Shape, TopTools_ShapeMapHasher]` and the other `TopTools_ShapeMapHasher` maps) both look up in two steps, first the hash, then an equality test, but not the same one:

| Step        | Python dict (`g in d`)                                                  | OCCT map (`m.Contains(g)`)                                 |
| ----------- | ----------------------------------------------------------------------- | ---------------------------------------------------------- |
| 1. hash     | `std::hash<TopoDS_Shape>`: `TShape` and `Location`, not the orientation | the same hash (`TopTools_ShapeMapHasher` uses `std::hash`) |
| 2. equality | `==`, i.e. `IsEqual`: the orientation counts                            | `IsSame`: the orientation does not count                   |

So a dict finds `g` if `g == f`, and an OCCT map finds it if `g.IsSame(f)`: a reversed face is a different dict key but the same map entry. A moved face changes the `Location`, which is part of the hash, so neither finds it.

### OCCT, for points

| Term                     | Compares                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------ |
| `gp_Pnt.IsEqual(p, tol)` | distance ≤ `tol`                                                                     |
| `std::equal_to<gp_Pnt>`  | each coordinate within `Epsilon(x)`, about one unit in the last place (`gp_Pnt.hxx`) |
| `std::hash<gp_Pnt>`      | the exact bits of the three doubles                                                  |

## Enums

**Binding rules: R-ENUM, R-ANON-ENUM ([Design 2c](Design.md#2c-python-additions))**

OCCT's enums are Python `enum.IntEnum` classes. As in C++, the enumerators of an unscoped enum are also names in the module (`TopAbs.TopAbs_FACE`), they are integers, and an `int` is accepted where OCCT expects the enum. An `enum class` stays nested in its class (`gp_Dir.D.NZ`).

```python
In [1]: from nanocct.TopAbs import TopAbs_ShapeEnum, TopAbs_FACE
   ...: from nanocct.Font import Font_FontAspect, Font_FA_Bold

In [2]: TopAbs_FACE is TopAbs_ShapeEnum.TopAbs_FACE, int(TopAbs_FACE), TopAbs_FACE == 4
Out[2]: (True, 4, True)

In [3]: TopAbs_FACE.name, TopAbs_ShapeEnum(4), TopAbs_ShapeEnum["TopAbs_EDGE"]
Out[3]: ('TopAbs_FACE', TopAbs_ShapeEnum.TopAbs_FACE, TopAbs_ShapeEnum.TopAbs_EDGE)

In [4]: [m.name for m in TopAbs_ShapeEnum][:3]
Out[4]: ['TopAbs_COMPOUND', 'TopAbs_COMPSOLID', 'TopAbs_SOLID']
```

OCCT's alias enumerators, like `Font_FA_Bold = Font_FontAspect_Bold`, are equal to the enumerator they stand for but a separate object, so compare enums with `==`, not `is`:

```python
In [5]: Font_FA_Bold == Font_FontAspect.Font_FontAspect_Bold, Font_FA_Bold is Font_FontAspect.Font_FontAspect_Bold
Out[5]: (True, False)
```

## Exceptions

**Design: [4.2](Design.md#42-three-kinds-of-c-types)**

OCCT's C++ exceptions arrive in Python as exception classes with the same names and the same hierarchy as in C++, with OCCT's own message. `Standard_Failure` is the root of all of them and derives from Python's `RuntimeError`. They are not mapped to Python's built-in categories: `Standard_OutOfRange` is not an `IndexError`, so catch OCCT's classes (or `Standard_Failure`).

```python
In [1]: from nanocct.gp import gp_Dir, gp_Pnt
   ...: from nanocct.gce import gce_MakeLin
   ...: from nanocct.Standard import Standard_Failure
   ...: from nanocct.StdFail import StdFail_NotDone

In [2]: try:
   ...:     gp_Dir(0, 0, 0)
   ...: except Standard_Failure as e:
   ...:     err = e
   ...: type(err).__name__, str(err)
Out[2]: ('Standard_ConstructionError', 'gp_Dir() - input vector has zero norm')

In [3]: [c.__name__ for c in type(err).__mro__][:4]
Out[3]: ['Standard_ConstructionError', 'Standard_DomainError', 'Standard_Failure', 'RuntimeError']
```

Many OCCT algorithms report a failure through a status first, and raise only when the missing result is asked for:

```python
In [4]: mk = gce_MakeLin(gp_Pnt(1, 1, 1), gp_Pnt(1, 1, 1))
   ...: mk.IsDone(), mk.Status()
Out[4]: (False, gce_ErrorType.gce_ConfusedPoints)

In [5]: try:
   ...:     mk.Value()
   ...: except StdFail_NotDone as e:
   ...:     msg = str(e)
   ...: msg
Out[5]: 'gce_MakeLin::Value() - no result'
```

## Doc strings

The nanocct generator copies the C++ `//!` documentation strings as Python docstrings

```python
In [14]: TopExp.MapShapes_s?

Signature:   TopExp.MapShapes_s(*args, **kwargs)
Type:        nb_func
String form: <nanobind.nb_func object at 0x115e4fa40>
Docstring:
MapShapes_s(S: nanocct.TopoDS.TopoDS_Shape, T: nanocct.TopAbs.TopAbs_ShapeEnum, M: nanocct.NCollection.NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher) -> None
MapShapes_s(S: nanocct.TopoDS.TopoDS_Shape, M: nanocct.NCollection.NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher, cumOri: bool = True, cumLoc: bool = True) -> None
MapShapes_s(S: nanocct.TopoDS.TopoDS_Shape, M: nanocct.NCollection.NCollection_Map__TopoDS_Shape__TopTools_ShapeMapHasher, cumOri: bool = True, cumLoc: bool = True) -> None

Overloaded function.

1. ``MapShapes_s(S: nanocct.TopoDS.TopoDS_Shape, T: nanocct.TopAbs.TopAbs_ShapeEnum, M: nanocct.NCollection.NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher) -> None``

Tool to explore a topological data structure.
Stores in the map <M> all the sub-shapes of <S>
of type <T>.

Warning: The map is not cleared at first.

2. ``MapShapes_s(S: nanocct.TopoDS.TopoDS_Shape, M: nanocct.NCollection.NCollection_IndexedMap__TopoDS_Shape__TopTools_ShapeMapHasher, cumOri: bool = True, cumLoc: bool = True) -> None``

Stores in the map <M> all the sub-shapes of <S>.
- If cumOri is true, the function composes all
sub-shapes with the orientation of S.
- If cumLoc is true, the function multiplies all
sub-shapes by the location of S, i.e. it applies to
each sub-shape the transformation that is associated with S.

3. ``MapShapes_s(S: nanocct.TopoDS.TopoDS_Shape, M: nanocct.NCollection.NCollection_Map__TopoDS_Shape__TopTools_ShapeMapHasher, cumOri: bool = True, cumLoc: bool = True) -> None``

Stores in the map <M> all the sub-shapes of <S>.
- If cumOri is true, the function composes all
sub-shapes with the orientation of S.
- If cumLoc is true, the function multiplies all
sub-shapes by the location of S, i.e. it applies to
each sub-shape the transformation that is associated with S.
```
