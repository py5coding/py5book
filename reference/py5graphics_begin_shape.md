# Py5Graphics.begin_shape()

Using the `begin_shape()` and [](py5graphics_end_shape) functions allow creating more complex forms.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for begin_shape()](/images/reference/Py5Graphics_begin_shape_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P2D)

    g = py5.create_graphics(60, 60, py5.P2D)
    with g.begin_draw():
        with g.begin_shape():
            g.no_fill()
            g.stroke_weight(5)
            g.vertex(10, 10)
            g.vertex(50, 10)
            g.vertex(50, 50)
            g.vertex(10, 50)

    py5.image(g, 0, 0)
    py5.image(g, 25, 25)
```

</div></div>

</div>

## Description

Using the `begin_shape()` and [](py5graphics_end_shape) functions allow creating more complex forms. `begin_shape()` begins recording vertices for a shape and [](py5graphics_end_shape) stops recording. The value of the `kind` parameter tells it which types of shapes to create from the provided vertices. With no mode specified, the shape can be any irregular polygon. The parameters available for `begin_shape()` are `POINTS`, `LINES`, `TRIANGLES`, `TRIANGLE_FAN`, `TRIANGLE_STRIP`, `QUADS`, and `QUAD_STRIP`. After calling the `begin_shape()` function, a series of [](py5graphics_vertex) commands must follow. To stop drawing the shape, call [](py5graphics_end_shape). The [](py5graphics_vertex) function with two parameters specifies a position in 2D and the [](py5graphics_vertex) function with three parameters specifies a position in 3D. Each shape will be outlined with the current stroke color and filled with the fill color. 

Transformations such as [](py5graphics_translate), [](py5graphics_rotate), and [](py5graphics_scale) do not work within `begin_shape()`. It is also not possible to use other shapes, such as [](py5graphics_ellipse) or [](py5graphics_rect) within `begin_shape()`. 

The `P2D` and `P3D` renderers allow [](py5graphics_stroke) and [](py5graphics_fill) to be altered on a per-vertex basis, but the default renderer does not. Settings such as [](py5graphics_stroke_weight), [](py5graphics_stroke_cap), and [](py5graphics_stroke_join) cannot be changed while inside a `begin_shape()` & [](py5graphics_end_shape) block with any renderer.

This method can be used as a context manager to ensure that [](py5graphics_end_shape) always gets called, as shown in the example. Use [](py5graphics_begin_closed_shape) to create a context manager that will pass the `CLOSE` parameter to [](sketch_end_shape), closing the shape.

This method is the same as [](sketch_begin_shape) but linked to a `Py5Graphics` object. To see more example code for how it can be used, see [](sketch_begin_shape).

Underlying Processing method: PGraphics.beginShape

## Signatures

```python
begin_shape() -> None

begin_shape(
    kind: int,  # Either POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS, or QUAD_STRIP
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
