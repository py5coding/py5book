# Py5Shape.is3d()

Boolean value reflecting if the shape is or is not a 3D shape.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for is3d()](/images/reference/Py5Shape_is3d_0.png)

</div><div class="example-cell-code">

```python
def setup():
    s = py5.create_shape()
    s.begin_shape()
    s.vertex(30, 20)
    s.vertex(85, 20)
    s.vertex(85, 75)
    s.vertex(30, 75)
    s.end_shape(py5.CLOSE)

    py5.println(s.is2d(), s.is3d())
    py5.shape(s)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for is3d()](/images/reference/Py5Shape_is3d_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P3D)
    s = py5.create_shape()
    s.begin_shape()
    s.vertex(30, 20)
    s.vertex(85, 20)
    s.vertex(85, 75)
    s.vertex(30, 75)
    s.end_shape(py5.CLOSE)

    py5.println(s.is2d(), s.is3d())
    py5.shape(s)
```

</div></div>

</div>

## Description

Boolean value reflecting if the shape is or is not a 3D shape.

This will be `True` if the shape is created in a Sketch using a 3D renderer such as `P3D`, even if it only uses 2D coordinates.

Underlying Processing method: PShape.is3D

## Signatures

```python
is3d() -> bool
```

Updated on November 05, 2024 03:08:47am UTC
