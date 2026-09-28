"""Static typing check for the NCollection_Xxx[T] spelling (run by mypy and ty, see tests/test_typing.py).
Lines with a trailing `# error:` comment must be reported; everything else must pass."""
from nanocct import NCollection, Standard, TCollection

a = NCollection.NCollection_Array1[float](1, 4)
a.SetValue(1, 0.5)
a[2] = 1.5
x: float = a.Value(1)
y: float = a[2]
n: int = len(a)
values: list[float] = list(a)
lower: int = a.Lower()

concrete = NCollection.NCollection_Array1__double(1, 2)             # the runtime class of every [float] array
generic: NCollection.NCollection_Array1[float] = concrete           # ... is a subclass of the generic spelling

h = NCollection.NCollection_HArray1[Standard.Standard_Persistent](1, 2)
arr_base: NCollection.NCollection_Array1[Standard.Standard_Persistent] = h   # HArray1 is (statically and at runtime) an Array1
p: Standard.Standard_Persistent = h.Value(1)
part: NCollection.NCollection_Array1[Standard.Standard_Persistent] = h.Array1()
rc: int = h.GetRefCount()


def total(arr: NCollection.NCollection_Array1[float]) -> float:    # accepts every double array
    return sum(arr)


total(a)

a.SetValue(1, "x")            # error: str is not float
bad: str = a.Value(1)         # error: float is not str
h.SetValue(1, 3.0)            # error: float is not Standard_Persistent
total(h)                      # error: HArray1[Standard_Persistent] is not Array1[float]
NCollection.NCollection_Array1[float](1, 2, 3, 4, 5)   # error: no such overload

# ---- List / Sequence / HSequence
l = NCollection.NCollection_List[int]()
l.Append(1)
first: int = l.First()
it = NCollection.NCollection_List__int.Iterator(l)      # ty rejects NCollection_List[int].Iterator (mypy accepts it)
while it.More():
    v: int = it.Value()
    it.Next()
s = NCollection.NCollection_Sequence[TCollection.TCollection_AsciiString]()
s.Append(TCollection.TCollection_AsciiString("a"))
sv: TCollection.TCollection_AsciiString = s.Value(1)
hs = NCollection.NCollection_HSequence[TCollection.TCollection_AsciiString]()
hs_base: NCollection.NCollection_Sequence[TCollection.TCollection_AsciiString] = hs
hs_len: int = len(hs)
l.Append("x")                 # error: str is not int
sbad: int = s[1]              # error: TCollection_AsciiString is not int

# ---- hashed kinds
d = NCollection.NCollection_DataMap[int, float]()
d.Bind(1, 1.5)
dv: float = d.Find(1)
dv2: float = d[1]
maybe: float | None = d.Seek(2)
im = NCollection.NCollection_IndexedMap[TCollection.TCollection_AsciiString]()
idx: int = im.Add(TCollection.TCollection_AsciiString("a"))
key: TCollection.TCollection_AsciiString = im.FindKey(1)
m = NCollection.NCollection_Map[int]()
ok: bool = m.Add(3)
d.Bind("x", 1.0)              # error: str is not int
bad_key: str = im.FindKey(1)  # error: TCollection_AsciiString is not str

# ---- Array2 / DynamicArray / DoubleMap / Shared, and HArray1 as an Array1
a2 = NCollection.NCollection_Array2[float](1, 2, 1, 3)
a2_v: float = a2.Value(1, 2)
a2_t: float = a2[(1, 2)]
h1: NCollection.NCollection_Array1[Standard.Standard_Persistent] = h      # HArray1 is an Array1
h2 = NCollection.NCollection_HArray2[float](1, 2, 1, 2, 0.0)
h2_rc: int = h2.GetRefCount()
dyn = NCollection.NCollection_DynamicArray[int]()
dyn_v: int = dyn.Append(1)
dmap = NCollection.NCollection_DoubleMap[int, TCollection.TCollection_AsciiString]()
dmap.Bind(1, TCollection.TCollection_AsciiString("one"))
k2: TCollection.TCollection_AsciiString = dmap.Find1(1)
k1: int = dmap.Find2(TCollection.TCollection_AsciiString("one"))
shared = NCollection.NCollection_Shared[NCollection.NCollection_Map[int]]()
shared_ok: bool = shared.Add(1)                                            # Map API through the concrete class
shared_rc: int = shared.GetRefCount()
a2.SetValue(1, 2, "x")        # error: str is not float
dmap.Bind("a", "b")           # error: str is not int
