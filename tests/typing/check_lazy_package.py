"""`import nanoocp` + attribute access type-checks: the package is lazy at runtime (PEP 562), so
nanoocp/__init__.pyi has to declare the submodules or a checker rejects nanoocp.gp (Design.md 5.1, 6b)."""
import nanoocp

p: nanoocp.gp.gp_Pnt = nanoocp.gp.gp_Pnt(1.0, 2.0, 3.0)
x: float = p.X()
d = nanoocp.gp.gp_Dir(1.0, 0.0, 0.0)

bad: str = p.X()              # error: float is not str
nanoocp.NoSuchPackage         # error: no such attribute
