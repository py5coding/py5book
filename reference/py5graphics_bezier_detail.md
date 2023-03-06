# Py5Graphics.bezier_detail()

Sets the resolution at which Beziers display.

## Description

Sets the resolution at which Beziers display. The default value is 20. This function is only useful when using the `P3D` renderer; the default `P2D` renderer does not use this information.

This method is the same as [](sketch_bezier_detail) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_bezier_detail).

Underlying Processing method: PGraphics.bezierDetail

## Signatures

```python
bezier_detail(
    detail: int,  # resolution of the curves
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
