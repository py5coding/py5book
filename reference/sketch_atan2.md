# atan2()

Calculates the angle (in radians) from a specified point to the coordinate origin as measured from the positive x-axis.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def draw():
    py5.background(204)
    py5.translate(py5.width/2, py5.height/2)
    a = py5.atan2(py5.mouse_y - py5.height/2, py5.mouse_x - py5.width/2)
    py5.rotate(a)
    py5.rect(-30, -5, 60, 10)
```

</div></div>

</div>

## Description

Calculates the angle (in radians) from a specified point to the coordinate origin as measured from the positive x-axis. Values are returned as a float in the range from `PI` to `-PI`. The `atan2()` function is most often used for orienting geometry to the position of the cursor. Note: The y-coordinate of the point is the first parameter, and the x-coordinate is the second parameter, due the the structure of calculating the tangent.

This function makes a call to the numpy `atan2()` function.

## Signatures

```python
atan2(
    y: Union[float, npt.ArrayLike],  # y-coordinate of the point
    x: Union[float, npt.ArrayLike],  # x-coordinate of the point
) -> Union[float, npt.NDArray]
```

Updated on March 06, 2023 02:49:26am UTC
