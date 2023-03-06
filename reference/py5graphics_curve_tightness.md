# Py5Graphics.curve_tightness()

Modifies the quality of forms created with [](py5graphics_curve) and [](py5graphics_curve_vertex).

## Description

Modifies the quality of forms created with [](py5graphics_curve) and [](py5graphics_curve_vertex). The parameter `tightness` determines how the curve fits to the vertex points. The value 0.0 is the default value for `tightness` (this value defines the curves to be Catmull-Rom splines) and the value 1.0 connects all the points with straight lines. Values within the range -5.0 and 5.0 will deform the curves but will leave them recognizable and as values increase in magnitude, they will continue to deform.

This method is the same as [](sketch_curve_tightness) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_curve_tightness).

Underlying Processing method: PGraphics.curveTightness

## Signatures

```python
curve_tightness(
    tightness: float,  # amount of deformation from the original vertices
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
