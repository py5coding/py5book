# Py5Graphics.shape()

Draws shapes to the Py5Graphics drawing surface.

## Description

Draws shapes to the Py5Graphics drawing surface. Shapes must be in the Sketch's "data" directory to load correctly. Py5 currently works with SVG, OBJ, and custom-created shapes. The `shape` parameter specifies the shape to display and the coordinate parameters define the location of the shape from its upper-left corner. The shape is displayed at its original size unless the `c` and `d` parameters specify a different size. The [](py5graphics_shape_mode) function can be used to change the way these parameters are interpreted.

This method is the same as [](sketch_shape) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_shape).

Underlying Processing method: PGraphics.shape

## Signatures

```python
shape(
    shape: Py5Shape,  # the shape to display
    /,
) -> None

shape(
    shape: Py5Shape,  # the shape to display
    a: float,  # x-coordinate of the shape
    b: float,  # y-coordinate of the shape
    c: float,  # width to display the shape
    d: float,  # height to display the shape
    /,
) -> None

shape(
    shape: Py5Shape,  # the shape to display
    x: float,  # x-coordinate of the shape
    y: float,  # y-coordinate of the shape
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
