import sys, time
from clang import cindex
INC = "/opt/local/occt-8_0_1-novtk/include/opencascade"
ARGS = ["-resource-dir", "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/clang/21", "-x", "c++", "-std=c++17", f"-I{INC}", "-isysroot", "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk"]
cindex.Config.set_library_file("/Library/Developer/CommandLineTools/usr/lib/libclang.dylib")
idx = cindex.Index.create()
hdr = sys.argv[1]
t0 = time.time()
tu = idx.parse(f"{INC}/{hdr}", args=ARGS, options=cindex.TranslationUnit.PARSE_SKIP_FUNCTION_BODIES)
print(f"parsed {hdr} in {time.time()-t0:.2f}s; diagnostics:", [d.spelling for d in tu.diagnostics if d.severity >= 3][:5])
K = cindex.CursorKind
for c in tu.cursor.get_children():
    if c.location.file is None or not c.location.file.name.endswith(hdr): continue
    if c.kind in (K.CLASS_DECL, K.STRUCT_DECL) and c.is_definition():
        bases = [b.type.spelling for b in c.get_children() if b.kind == K.CXX_BASE_SPECIFIER]
        print(f"\nclass {c.spelling} : {bases}   doc={c.brief_comment!r}")
        for mth in c.get_children():
            if mth.kind in (K.CXX_METHOD, K.CONSTRUCTOR) and mth.access_specifier == cindex.AccessSpecifier.PUBLIC:
                params = ", ".join(f"{p.type.spelling} {p.spelling}" for p in mth.get_arguments())
                flags = ("static " if mth.is_static_method() else "") + ("const " if mth.is_const_method() else "") + ("virtual " if mth.is_virtual_method() else "") + ("=0 " if mth.is_pure_virtual_method() else "")
                print(f"  {flags}{mth.result_type.spelling} {mth.spelling}({params})  # {mth.brief_comment!r}"[:170])
    elif c.kind == K.TYPEDEF_DECL or c.kind == K.ENUM_DECL:
        print(f"\n{c.kind.name} {c.spelling} = {c.underlying_typedef_type.spelling if c.kind==K.TYPEDEF_DECL else ''}")
