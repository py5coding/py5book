# Py5Graphics.rotate_z()

Rotates around the z-axis the amount specified by the `angle` parameter.

## Description

Rotates around the z-axis the amount specified by the `angle` parameter. Angles should be specified in radians (values from `0` to `TWO_PI`) or converted from degrees to radians with the [](sketch_radians) function. Coordinates are always rotated around their relative position to the origin. Positive numbers rotate in a clockwise direction and negative numbers rotate in a counterclockwise direction. Transformations apply to everything that happens after and subsequent calls to the function accumulates the effect. For example, calling `rotate_z(PI/2)` and then `rotate_z(PI/2)` is the same as `rotate_z(PI)`. If `rotate_z()` is run within the `draw()`, the transformation is reset when the loop begins again. This function requires using `P3D` as a third parameter to [](sketch_size) as shown in the example.

This method is the same as [](sketch_rotate_z) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_rotate_z).

Underlying Processing method: PGraphics.rotateZ

## Signatures

```python
rotate_z(
    angle: float,  # angle of rotation specified in radians
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
