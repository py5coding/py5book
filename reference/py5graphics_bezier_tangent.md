# Py5Graphics.bezier_tangent()

Calculates the tangent of a point on a Bezier curve.

## Description

Calculates the tangent of a point on a Bezier curve. There is a good definition of *tangent* on Wikipedia.

This method is the same as [](sketch_bezier_tangent) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_bezier_tangent).

Underlying Processing method: PGraphics.bezierTangent

## Signatures

```python
bezier_tangent(
    a: float,  # coordinate of first point on the curve
    b: float,  # coordinate of first control point
    c: float,  # coordinate of second control point
    d: float,  # coordinate of second point on the curve
    t: float,  # value between 0 and 1
    /,
) -> float
```

Updated on March 06, 2023 02:49:26am UTC
