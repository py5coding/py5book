# Py5Shape.curve_vertex()

Specifies a `Py5Shape` object's vertex coordinates for curves.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for curve_vertex()](/images/reference/Sketch_curve_vertex_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P2D)
    s = py5.create_shape()
    s.begin_shape()
    s.no_fill()
    s.curve_vertex(84, 91)
    s.curve_vertex(84, 91)
    s.curve_vertex(68, 19)
    s.curve_vertex(21, 17)
    s.curve_vertex(32, 100)
    s.curve_vertex(32, 100)
    s.end_shape()
    py5.shape(s)
```

</div></div>

</div>

## Description

Specifies a `Py5Shape` object's vertex coordinates for curves. This method may only be used between [](py5shape_begin_shape) and [](py5shape_end_shape) and only when there is no `MODE` parameter specified to [](py5shape_begin_shape). The first and last points in a series of `curve_vertex()` lines will be used to guide the beginning and end of the curve. A minimum of four points is required to draw a tiny curve between the second and third points. Adding a fifth point with `curve_vertex()` will draw the curve between the second, third, and fourth points. The `curve_vertex()` method is an implementation of Catmull-Rom splines.

Drawing 2D curves requires using the `P2D` renderer and drawing 3D curves requires using the `P3D` renderer. When drawing directly with `Py5Shape` objects, curves do not work at all using the default renderer.

This method can only be used within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

Underlying Processing method: PShape.curveVertex

## Signatures

```python
curve_vertex(
    x: float,  # the x-coordinate of the vertex
    y: float,  # the y-coordinate of the vertex
    /,
) -> None

curve_vertex(
    x: float,  # the x-coordinate of the vertex
    y: float,  # the y-coordinate of the vertex
    z: float,  # the z-coordinate of the vertex
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
