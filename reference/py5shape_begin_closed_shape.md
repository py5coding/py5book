# Py5Shape.begin_closed_shape()

This method is used to start a custom closed shape created with the [](sketch_create_shape) function.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global s  # the Py5Shape object
    s = py5.create_shape()
    with s.begin_closed_shape():
        s.stroke_weight(5)
        s.no_fill()
        s.vertex(0, 0)
        s.vertex(0, 50)
        s.vertex(50, 0)


def draw():
    py5.shape(s, 25, 25)
```

</div></div>

</div>

## Description

This method is used to start a custom closed shape created with the [](sketch_create_shape) function. It's always and only used with [](sketch_create_shape).

This method should only be used as a context manager, as shown in the example. When used as a context manager, this will ensure that [](py5shape_end_shape) always gets called, just like when using [](py5shape_begin_shape) as a context manager. The difference is that when exiting, the parameter `CLOSE` will be passed to [](py5shape_end_shape), connecting the last vertex to the first. This will close the shape. If this method were to be used not as a context manager, it won't be able to close the shape by making the call to [](py5shape_end_shape).

Underlying Processing method: [PShape.beginShape](https://processing.org/reference/PShape_beginShape_.html)

## Signatures

```python
begin_closed_shape() -> None

begin_closed_shape(
    kind: int,  # Either POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS, or QUAD_STRIP
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
