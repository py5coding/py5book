# Py5Graphics.scale()

Increases or decreases the size of a shape by expanding and contracting vertices.

## Description

Increases or decreases the size of a shape by expanding and contracting vertices. Objects always scale from their relative origin to the coordinate system. Scale values are specified as decimal percentages. For example, the function call `scale(2.0)` increases the dimension of a shape by 200%.

Transformations apply to everything that happens after and subsequent calls to the function multiply the effect. For example, calling `scale(2.0)` and then `scale(1.5)` is the same as `scale(3.0)`. Using this function with the `z` parameter requires using `P3D` as the renderer. This function can be further controlled with [](py5graphics_push_matrix) and [](py5graphics_pop_matrix).

This method is the same as [](sketch_scale) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_scale).

Underlying Processing method: PGraphics.scale

## Signatures

```python
scale(
    s: float,  # percentage to scale the object
    /,
) -> None

scale(
    x: float,  # percentage to scale the object in the x-axis
    y: float,  # percentage to scale the object in the y-axis
    /,
) -> None

scale(
    x: float,  # percentage to scale the object in the x-axis
    y: float,  # percentage to scale the object in the y-axis
    z: float,  # percentage to scale the object in the z-axis
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
