# Py5Graphics.rotate()

Rotates the amount specified by the `angle` parameter.

## Description

Rotates the amount specified by the `angle` parameter. Angles must be specified in radians (values from `0` to `TWO_PI`), or they can be converted from degrees to radians with the [](sketch_radians) function. 
 
The coordinates are always rotated around their relative position to the origin. Positive numbers rotate objects in a clockwise direction and negative numbers rotate in the couterclockwise direction. Transformations apply to everything that happens afterward, and subsequent calls to the function compound the effect. For example, calling `rotate(PI/2.0)` once and then calling `rotate(PI/2.0)` a second time is the same as a single `rotate(PI)`. All tranformations are reset when `draw()` begins again. 
 
Technically, `rotate()` multiplies the current transformation matrix by a rotation matrix. This function can be further controlled by [](py5graphics_push_matrix) and [](py5graphics_pop_matrix).

This method is the same as [](sketch_rotate) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_rotate).

Underlying Processing method: PGraphics.rotate

## Signatures

```python
rotate(
    angle: float,  # angle of rotation specified in radians
    /,
) -> None

rotate(
    angle: float,  # angle of rotation specified in radians
    x: float,  # x-coordinate of vector to rotate around
    y: float,  # y-coordinate of vector to rotate around
    z: float,  # z-coordinate of vector to rotate around
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
