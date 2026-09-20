"""Static typing check for the NCollection_Xxx[T] spelling (run by mypy and ty, see tests/test_typing.py).
Lines with a trailing `# error:` comment must be reported; everything else must pass."""
from nanoocp import NCollection, Standard, TCollection, TColStd

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
alias = TColStd.TColStd_Array1OfReal(1, 3)
alias_value: float = alias.Value(1)

h = NCollection.NCollection_HArray1[Standard.Standard_Persistent](1, 2)
t: Standard.Standard_Transient = h                                  # HArray1 is a Transient
p: Standard.Standard_Persistent = h.Value(1)
part: NCollection.NCollection_Array1[Standard.Standard_Persistent] = h.Array1()
rc: int = h.GetRefCount()


def total(arr: NCollection.NCollection_Array1[float]) -> float:    # accepts every double array
    return sum(arr)


total(a)
total(alias)

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
hs_t: Standard.Standard_Transient = hs
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
