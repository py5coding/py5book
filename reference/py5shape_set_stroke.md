# Py5Shape.set_stroke()

The `set_stroke()` method defines the outline color of a `Py5Shape`.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global c
    py5.size(640, 360, py5.P2D)
    c = py5.create_shape(py5.RECT, -20, -20, 40, 40)
    c.set_stroke("#FFFFFF")


def draw():
    py5.background(51)
    c.set_fill(py5.color(py5.random_int(255)))
    py5.translate(py5.mouse_x, py5.mouse_y)
    py5.shape(c)
```

</div></div>

</div>

## Description

The `set_stroke()` method defines the outline color of a `Py5Shape`. This method is used after shapes are created or when a shape is defined explicitly (e.g. `create_shape(RECT, 20, 20, 60, 60)`) as shown in the example. When a shape is created with [](py5shape_begin_shape) and [](py5shape_end_shape), its attributes may be changed with [](py5shape_fill) and [](py5shape_stroke) within [](py5shape_begin_shape) and [](py5shape_end_shape). However, after the shape is created, only the `set_stroke()` method can define a new stroke value for the `Py5Shape`.

Underlying Processing method: [PShape.setStroke](https://processing.org/reference/PShape_setStroke_.html)

## Signatures

```python
set_stroke(
    index: int,  # vertex index
    stroke: int,  # any color value
    /,
) -> None

set_stroke(
    stroke: bool,  # allow stroke
    /,
) -> None

set_stroke(
    stroke: int,  # any color value
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
