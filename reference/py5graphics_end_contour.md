# Py5Graphics.end_contour()

Use the [](py5graphics_begin_contour) and `end_contour()` methods to create negative shapes within shapes such as the center of the letter 'O'.

## Description

Use the [](py5graphics_begin_contour) and `end_contour()` methods to create negative shapes within shapes such as the center of the letter 'O'. The [](py5graphics_begin_contour) method begins recording vertices for the shape and `end_contour()` stops recording. The vertices that define a negative shape must "wind" in the opposite direction from the exterior shape. First draw vertices for the exterior shape in clockwise order, then for internal shapes, draw vertices counterclockwise.

These methods can only be used within a [](py5graphics_begin_shape) & [](py5graphics_end_shape) pair and transformations such as [](py5graphics_translate), [](py5graphics_rotate), and [](py5graphics_scale) do not work within a [](py5graphics_begin_contour) & `end_contour()` pair. It is also not possible to use other shapes, such as [](py5graphics_ellipse) or [](py5graphics_rect) within.

This method is the same as [](sketch_end_contour) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_end_contour).

Underlying Processing method: PGraphics.endContour

## Signatures

```python
end_contour() -> None
```

Updated on March 06, 2023 02:49:26am UTC
