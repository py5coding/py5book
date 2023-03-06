# lerp()

Calculates a number between two numbers at a specific increment.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for lerp()](/images/reference/Sketch_lerp_0.png)

</div><div class="example-cell-code">

```python
def setup():
    a = 20
    b = 80
    c = py5.lerp(a, b, 0.2)
    d = py5.lerp(a, b, 0.5)
    e = py5.lerp(a, b, 0.8)
    py5.begin_shape(py5.POINTS)
    py5.vertex(a, 50)
    py5.vertex(b, 50)
    py5.vertex(c, 50)
    py5.vertex(d, 50)
    py5.vertex(e, 50)
    py5.end_shape()
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for lerp()](/images/reference/Sketch_lerp_1.png)

</div><div class="example-cell-code">

```python
def setup():
    x1 = 15
    y1 = 10
    x2 = 80
    y2 = 90
    py5.line(x1, y1, x2, y2)
    for i in range(10):
        x = py5.lerp(x1, x2, i/10) + 10
        y = py5.lerp(y1, y2, i/10)
        py5.point(x, y)
```

</div></div>

</div>

## Description

Calculates a number between two numbers at a specific increment. The `amt` parameter is the amount to interpolate between the two values where 0.0 equal to the first point, 0.1 is very near the first point, 0.5 is half-way in between, etc. The lerp function is convenient for creating motion along a straight path and for drawing dotted lines. If the `amt` parameter is greater than 1.0 or less than 0.0, the interpolated value will be outside of the range specified by the `start` and `stop` parameter values.

## Signatures

```python
lerp(
    start: Union[float, npt.NDArray],  # first value
    stop: Union[float, npt.NDArray],  # second value
    amt: Union[float, npt.NDArray],  # float between 0.0 and 1.0
) -> Union[float, npt.NDArray]
```

Updated on March 06, 2023 02:49:26am UTC
