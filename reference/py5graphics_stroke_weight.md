# Py5Graphics.stroke_weight()

Sets the width of the stroke used for lines, points, and the border around shapes.

## Description

Sets the width of the stroke used for lines, points, and the border around shapes. All widths are set in units of pixels.

Using [](py5graphics_point) with `strokeWeight(1)` or smaller may draw nothing to the Py5Graphics drawing surface, depending on the graphics settings of the computer. Workarounds include setting the pixel using the [](py5graphics_pixels) or [](py5graphics_np_pixels) arrays or drawing the point using either [](py5graphics_circle) or [](py5graphics_square).

This method is the same as [](sketch_stroke_weight) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_stroke_weight).

Underlying Processing method: PGraphics.strokeWeight

## Signatures

```python
stroke_weight(
    weight: float,  # the weight (in pixels) of the stroke
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
