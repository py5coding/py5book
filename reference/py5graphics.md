# Py5Graphics

Main graphics and rendering context, as well as the base `API` implementation for processing "core".

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global pg
    pg = py5.create_graphics(40, 40)


def draw():
    pg.begin_draw()
    pg.background(100)
    pg.stroke(255)
    pg.line(20, 20, py5.mouse_x, py5.mouse_y)
    pg.end_draw()
    py5.image(pg, 9, 30)
    py5.image(pg, 51, 30)
```

</div></div>

</div>

## Description

Main graphics and rendering context, as well as the base `API` implementation for processing "core". Use this class if you need to draw into an off-screen graphics buffer. A Py5Graphics object can be constructed with the [](sketch_create_graphics) function. The [](py5graphics_begin_draw) and [](py5graphics_end_draw) methods (see example) are necessary to set up the buffer and to finalize it. The fields and methods for this class are extensive.

It is critically important that calls to this object's drawing methods are only used between [](py5graphics_begin_draw) and [](py5graphics_end_draw). Forgetting to call [](py5graphics_begin_draw) will likely result in an ugly and unhelpful Java exception.

To create a new graphics context, use the [](sketch_create_graphics) function. Do not use the syntax `Py5Graphics()`.

Underlying Processing class: [PGraphics](https://processing.org/reference/PGraphics.html)

The following methods and fields are provided:

```{include} include_py5graphics.md
```

Updated on March 06, 2023 02:49:26am UTC
