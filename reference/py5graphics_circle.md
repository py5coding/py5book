# Py5Graphics.circle()

Draws a circle to the screen.

## Description

Draws a circle to the screen. By default, the first two parameters set the location of the center, and the third sets the shape's width and height. The origin may be changed with the [](py5graphics_ellipse_mode) function.

This method is the same as [](sketch_circle) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_circle).

Underlying Processing method: PGraphics.circle

## Signatures

```python
circle(
    x: float,  # x-coordinate of the ellipse
    y: float,  # y-coordinate of the ellipse
    extent: float,  # width and height of the ellipse by default
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
