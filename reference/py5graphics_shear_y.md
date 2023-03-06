# Py5Graphics.shear_y()

Shears a shape around the y-axis the amount specified by the `angle` parameter.

## Description

Shears a shape around the y-axis the amount specified by the `angle` parameter. Angles should be specified in radians (values from `0` to `TWO_PI`) or converted to radians with the [](sketch_radians) function. Objects are always sheared around their relative position to the origin and positive numbers shear objects in a clockwise direction. Transformations apply to everything that happens after and subsequent calls to the function accumulates the effect. For example, calling `shear_y(PI/2)` and then `shear_y(PI/2)` is the same as `shear_y(PI)`.
 
Technically, `shear_y()` multiplies the current transformation matrix by a rotation matrix. This function can be further controlled by the [](py5graphics_push_matrix) and [](py5graphics_pop_matrix) functions.

This method is the same as [](sketch_shear_y) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_shear_y).

Underlying Processing method: PGraphics.shearY

## Signatures

```python
shear_y(
    angle: float,  # angle of shear specified in radians
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
