# AddOns: workarounds for OCCT bugs

`nanocct.AddOns.ShapeClean.ShapeUpgrade_UnifySameDomain` is a drop-in replacement for OCCT's `ShapeUpgrade_UnifySameDomain`: same class name, same signatures for the members it has (constructor, `AllowInternalEdges`, `Build`, `Shape`, `History`). Importing it from `nanocct.ShapeUpgrade` gives OCCT's behaviour, importing it from `nanocct.AddOns.ShapeClean` gives OCCT's behaviour with three defects worked around. OCCT's source is not patched and no OCCT code is copied; all three workarounds only call OCCT's public API. Each has a canary test in `tests/test_AddOns.py` that fails once OCCT fixes the defect: then the workaround is deleted (Binding-Rules.md R-ADDON).

The class runs OCCT's unification as two passes, a face pass and then an edge pass, so that the steps below can sit between and after them.

## When the workarounds act

ShapeClean 1 is preventive: when it finds a full circle of arcs at risk, it protects it before the edge pass, without waiting to see whether OCCT would break it. ShapeClean 2 and 3 repair afterwards, and only what OCCT broke:

| | ShapeClean 2: merged edge one period away | ShapeClean 3: face merged with its mirror image |
| --- | --- | --- |
| acts only if something is broken | yes: only faces the edge pass left invalid (periodic, an edge merged from >= 2 pieces, not a seam) | yes, it repairs only if an output face is invalid; but before every face pass it keeps the curves of all periodic input faces and checks the new faces afterwards (bookkeeping, nothing is changed) |
| repairs only the broken shapes | yes: only the merged curve on the broken face | its whole group: every output face on the same surface, so a valid face sharing that surface with a broken one goes back to its input faces too |
| keeps a repair only if it is valid | yes, checked per edge: a face that would need two curves shifted at once is not repaired | yes: the group's input faces must be valid with their own curves |
| otherwise | OCCT's curve is put back | OCCT's curves are put back, the group stays as OCCT made it |

"Valid" is OCCT's `BRepCheck_Analyzer` on the face, not a check of the whole shape.

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

## ShapeClean 3: a face merged with its mirror image (build123d #902)

The defect: when the face pass merges two same-domain faces on surfaces of opposite handedness -- a face and its mirror image, e.g. a revolved part mirrored -- it maps the mirrored face's parameter-space curves onto the other surface correctly only up to a whole period. Its check whether the shared edge's new curve is the one it already has then takes that period offset for a second curve, and the shared edge becomes a false seam: the pair is built as two faces, one of them not closed, or the merge is abandoned after the curves were already shifted, which is not undone. The input shape is changed too.

- before OCCT's face pass (ShapeClean 1 step 1): keep the parameter-space curves of every face on a periodic surface as they are
- run OCCT's face pass
- check the output faces on periodic surfaces that the pass made, or kept with replaced curves (`BRepCheck_Analyzer`); valid faces stay as OCCT made them
- for an invalid face, its group is every output face on the same surface, together with the input faces they came from:
    - give those input faces their own curves back
    - if they are valid then, replace the group's new faces by them (`BRepTools_ReShape`, its history added); a kept face is repaired in place
    - otherwise put OCCT's curves back and leave the group as OCCT made it

Merges OCCT gets right stay merged; only a group it broke goes back to its input faces.
