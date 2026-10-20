# AddOns: workarounds for OCCT bugs

`nanocct.AddOns.ShapeClean.ShapeUpgrade_UnifySameDomain` is a drop-in replacement for OCCT's `ShapeUpgrade_UnifySameDomain`: same class name, same signatures for the members it has (constructor, `AllowInternalEdges`, `Build`, `Shape`, `History`). Importing it from `nanocct.ShapeUpgrade` gives OCCT's behaviour, importing it from `nanocct.AddOns.ShapeClean` gives OCCT's behaviour with two defects worked around. OCCT's source is not patched and no OCCT code is copied; both workarounds only call OCCT's public API. Each has a canary test in `tests/test_AddOns.py` that fails once OCCT fixes the defect: then the workaround is deleted (Binding-Rules.md R-ADDON).

The class runs OCCT's unification as two passes, a face pass and then an edge pass, so that the steps below can sit between and after them.

## ShapeClean 1: a full circle made of arcs (OCCT issue #1541)

The defect: when the edge pass merges a full circle that consists of two or more arcs, OCCT joins the arcs' curves in the face's parameter space starting at the wrong junction. The edge tolerance inflates and the face can lose the edge (a sphere cut from a box, with the sphere's seam splitting the cut circle).

Step 1
- run OCCT's face pass alone (the circles to protect can only be found after it)

Step 2
- detect full circles present as >= 2 arcs: same centre, axis and radius, arcs summing to a full turn
- keep only those that are a hazard: a non-line curve in the parameter space of a non-planar face
- protect them: add enough of their junction vertices to OCCT's keep list (`KeepShapes`) that the edge pass cannot close the circle

Step 3
- run OCCT's edge pass with that keep list

Step 4
- merge each protected circle ourselves into one closed edge, joining the arcs' parameter-space curves in chain order and appending, never prepending
- check each merged circle (closed in parameter space, tolerance not inflated); a circle that fails stays split, which is valid
- if the shape with the merged circles is not valid, keep the arcs split
- compose the histories of the face pass, the edge pass and the merge

## ShapeClean 2: a merged edge one period away (build123d #1123, #1363)

The defect: when the edge pass merges a chain of edges, the joined parameter-space curve gets another parameter range than the merged 3D curve, so OCCT discards it and projects the 3D curve onto the surface again. The projection does not know where the face lies in parameter space: on a periodic surface (cylinder, torus) a loop that starts on the period line can land one period away from the rest of the face, and the face is invalid (a hole through a cylindrical face across its period line).

- after OCCT's edge pass (ShapeClean 1 step 3, before its step 4), look at every edge merged from >= 2 pieces (from the pass's history)
- for each face of that edge:
    - only faces that are U- or V-periodic, invalid (`BRepCheck_Analyzer`) and where the edge is not a seam are handled; every other face stays as OCCT made it
        - compare the merged curve with one of its pieces at the piece's midpoint (the midpoint projected onto the merged edge), in the face's parameter space
        - if they differ by whole periods (up to 1/1000 of a period), translate the merged curve back by those periods -- exact, no approximation, the merge itself stays
        - keep the translation only if the face is valid then; otherwise put OCCT's curve back

Why the midpoint and why only invalid faces: at a vertex a curve that wraps a period (a hole's loop around the tool's own cylinder) has two positions, so comparing there sees a period that is not there; and on valid faces a merged curve can sit a period away from its pieces and still be right -- shifting those broke fillets in build123d's examples.
