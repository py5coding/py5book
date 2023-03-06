# rotate_x()

Rotates around the x-axis the amount specified by the `angle` parameter.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for rotate_x()](/images/reference/Sketch_rotate_x_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.translate(py5.width//2, py5.height//2)
    py5.rotate_x(py5.PI/3.0)
    py5.rect(-26, -26, 52, 52)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for rotate_x()](/images/reference/Sketch_rotate_x_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    py5.translate(py5.width//2, py5.height//2)
    py5.rotate_x(py5.radians(60))
    py5.rect(-26, -26, 52, 52)
```

</div></div>

</div>

## Description

Rotates around the x-axis the amount specified by the `angle` parameter. Angles should be specified in radians (values from `0` to `TWO_PI`) or converted from degrees to radians with the [](sketch_radians) function. Coordinates are always rotated around their relative position to the origin. Positive numbers rotate in a clockwise direction and negative numbers rotate in a counterclockwise direction. Transformations apply to everything that happens after and subsequent calls to the function accumulates the effect. For example, calling `rotate_x(PI/2)` and then `rotate_x(PI/2)` is the same as `rotate_x(PI)`. If `rotate_x()` is run within the `draw()`, the transformation is reset when the loop begins again. This function requires using `P3D` as a third parameter to [](sketch_size) as shown in the example.

Underlying Processing method: [rotateX](https://processing.org/reference/rotateX_.html)

## Signatures

```python
rotate_x(
    angle: float,  # angle of rotation specified in radians
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
