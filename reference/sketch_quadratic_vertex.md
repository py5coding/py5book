# quadratic_vertex()

Specifies vertex coordinates for quadratic Bezier curves.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for quadratic_vertex()](/images/reference/Sketch_quadratic_vertex_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.no_fill()
    py5.stroke_weight(4)
    py5.begin_shape()
    py5.vertex(20, 20)
    py5.quadratic_vertex(80, 20, 50, 50)
    py5.end_shape()
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for quadratic_vertex()](/images/reference/Sketch_quadratic_vertex_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.no_fill()
    py5.stroke_weight(4)
    py5.begin_shape()
    py5.vertex(20, 20)
    py5.quadratic_vertex(80, 20, 50, 50)
    py5.quadratic_vertex(20, 80, 80, 80)
    py5.vertex(80, 60)
    py5.end_shape()
```

</div></div>

</div>

## Description

Specifies vertex coordinates for quadratic Bezier curves. Each call to `quadratic_vertex()` defines the position of one control point and one anchor point of a Bezier curve, adding a new segment to a line or shape. The first time `quadratic_vertex()` is used within a [](sketch_begin_shape) call, it must be prefaced with a call to [](sketch_vertex) to set the first anchor point. This method must be used between [](sketch_begin_shape) and [](sketch_end_shape) and only when there is no `MODE` parameter specified to [](sketch_begin_shape). Using the 3D version requires rendering with `P3D`.

Underlying Processing method: [quadraticVertex](https://processing.org/reference/quadraticVertex_.html)

## Signatures

```python
quadratic_vertex(
    cx: float,  # the x-coordinate of the control point
    cy: float,  # the y-coordinate of the control point
    cz: float,  # the z-coordinate of the control point
    x3: float,  # the x-coordinate of the anchor point
    y3: float,  # the y-coordinate of the anchor point
    z3: float,  # the z-coordinate of the anchor point
    /,
) -> None

quadratic_vertex(
    cx: float,  # the x-coordinate of the control point
    cy: float,  # the y-coordinate of the control point
    x3: float,  # the x-coordinate of the anchor point
    y3: float,  # the y-coordinate of the anchor point
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
