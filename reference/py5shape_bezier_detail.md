# Py5Shape.bezier_detail()

Sets a `Py5Shape` object's resolution at which Beziers display.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for bezier_detail()](/images/reference/Py5Shape_bezier_detail_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P2D)
    s1 = make_curve(5)
    s2 = make_curve(20)
    py5.shape(s1)
    py5.shape(s2, 40, 0)


def make_curve(detail):
    s = py5.create_shape()
    s.begin_shape()
    s.no_fill()
    s.vertex(10, 20)
    s.bezier_detail(detail)
    s.bezier_vertex(60, 0, 60, 75, 10, 75)
    s.end_shape()
    return s
```

</div></div>

</div>

## Description

Sets a `Py5Shape` object's resolution at which Beziers display. The default value is 20.

Drawing 2D bezier curves requires using the `P2D` renderer and drawing 3D bezier curves requires using the `P3D` renderer. When drawing directly with `Py5Shape` objects, bezier curves do not work at all using the default renderer.

This method can only be used within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

Underlying Processing method: PShape.bezierDetail

## Signatures

```python
bezier_detail(
    detail: int,  # resolution of the curves
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
