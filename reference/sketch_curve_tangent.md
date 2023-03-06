# curve_tangent()

Calculates the tangent of a point on a curve.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for curve_tangent()](/images/reference/Sketch_curve_tangent_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.no_fill()
    py5.curve(5, 26, 73, 24, 73, 61, 15, 65)
    steps = 6
    for i in range(0, steps+1):
        t = i / steps
        x = py5.curve_point(5, 73, 73, 15, t)
        y = py5.curve_point(26, 24, 61, 65, t)
        #ellipse(x, y, 5, 5)
        tx = py5.curve_tangent(5, 73, 73, 15, t)
        ty = py5.curve_tangent(26, 24, 61, 65, t)
        a = py5.atan2(ty, tx)
        a -= py5.PI/2.0
        py5.line(x, y, py5.cos(a)*8 + x, py5.sin(a)*8 + y)
```

</div></div>

</div>

## Description

Calculates the tangent of a point on a curve. There's a good definition of *tangent* on Wikipedia.

Underlying Processing method: [curveTangent](https://processing.org/reference/curveTangent_.html)

## Signatures

```python
curve_tangent(
    a: float,  # coordinate of first point on the curve
    b: float,  # coordinate of first control point
    c: float,  # coordinate of second control point
    d: float,  # coordinate of second point on the curve
    t: float,  # value between 0 and 1
    /,
) -> float
```

Updated on March 06, 2023 02:49:26am UTC
