# Py5Graphics.quad()

A quad is a quadrilateral, a four sided polygon.

## Description

A quad is a quadrilateral, a four sided polygon. It is similar to a rectangle, but the angles between its edges are not constrained to ninety degrees. The first pair of parameters (x1,y1) sets the first vertex and the subsequent pairs should proceed clockwise or counter-clockwise around the defined shape.

This method is the same as [](sketch_quad) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_quad).

Underlying Processing method: PGraphics.quad

## Signatures

```python
quad(
    x1: float,  # x-coordinate of the first corner
    y1: float,  # y-coordinate of the first corner
    x2: float,  # x-coordinate of the second corner
    y2: float,  # y-coordinate of the second corner
    x3: float,  # x-coordinate of the third corner
    y3: float,  # y-coordinate of the third corner
    x4: float,  # x-coordinate of the fourth corner
    y4: float,  # y-coordinate of the fourth corner
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
