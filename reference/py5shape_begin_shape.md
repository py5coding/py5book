# Py5Shape.begin_shape()

This method is used to start a custom shape created with the [](sketch_create_shape) function.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global s  # the Py5Shape object
    s = py5.create_shape()
    s.begin_shape()
    s.fill("#F00")
    s.no_stroke()
    s.vertex(0, 0)
    s.vertex(0, 50)
    s.vertex(50, 0)
    s.end_shape()


def draw():
    py5.shape(s, 25, 25)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global s  # the Py5Shape object
    s = py5.create_shape()
    with s.begin_shape():
        s.fill("#F00")
        s.no_stroke()
        s.vertex(0, 0)
        s.vertex(0, 50)
        s.vertex(50, 0)


def draw():
    py5.shape(s, 25, 25)
```

</div></div>

</div>

## Description

This method is used to start a custom shape created with the [](sketch_create_shape) function. It's always and only used with [](sketch_create_shape).

Drawing commands to a custom shape must always conclude with a call to the [](py5shape_end_shape) method. This method can be used as a context manager to ensure that [](py5shape_end_shape) always gets called, as shown in the second example. Use [](py5shape_begin_closed_shape) to create a context manager that will pass the `CLOSE` parameter to [](sketch_end_shape), closing the shape.

Underlying Processing method: [PShape.beginShape](https://processing.org/reference/PShape_beginShape_.html)

## Signatures

```python
begin_shape() -> None

begin_shape(
    kind: int,  # Either POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS, or QUAD_STRIP
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
