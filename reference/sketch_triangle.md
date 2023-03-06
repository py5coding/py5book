# triangle()

A triangle is a plane created by connecting three points.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for triangle()](/images/reference/Sketch_triangle_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.triangle(30, 75, 58, 20, 86, 75)
```

</div></div>

</div>

## Description

A triangle is a plane created by connecting three points. The first two arguments specify the first point, the middle two arguments specify the second point, and the last two arguments specify the third point.

Underlying Processing method: [triangle](https://processing.org/reference/triangle_.html)

## Signatures

```python
triangle(
    x1: float,  # x-coordinate of the first point
    y1: float,  # y-coordinate of the first point
    x2: float,  # x-coordinate of the second point
    y2: float,  # y-coordinate of the second point
    x3: float,  # x-coordinate of the third point
    y3: float,  # y-coordinate of the third point
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
