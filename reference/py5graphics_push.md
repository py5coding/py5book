# Py5Graphics.push()

The `push()` function saves the current drawing style settings and transformations, while [](py5graphics_pop) restores these settings.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for push()](/images/reference/Py5Graphics_push_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P2D)

    g = py5.create_graphics(60, 60, py5.P2D)
    with g.begin_draw():
        g.translate(30, 30)
        with g.push():
            g.stroke("#F00")
            g.scale(2)
            with g.begin_closed_shape():
                g.vertex(-10, -10)
                g.vertex(10, -10)
                g.vertex(10, 10)
                g.vertex(-10, 10)
        with g.begin_closed_shape():
            g.vertex(-10, -10)
            g.vertex(10, -10)
            g.vertex(10, 10)
            g.vertex(-10, 10)

    py5.image(g, 0, 0)
    py5.image(g, 25, 25)
```

</div></div>

</div>

## Description

The `push()` function saves the current drawing style settings and transformations, while [](py5graphics_pop) restores these settings. Note that these functions are always used together. They allow you to change the style and transformation settings and later return to what you had. When a new state is started with `push()`, it builds on the current style and transform information.

`push()` stores information related to the current transformation state and style settings controlled by the following functions: [](py5graphics_rotate), [](py5graphics_translate), [](py5graphics_scale), [](py5graphics_fill), [](py5graphics_stroke), [](py5graphics_tint), [](py5graphics_stroke_weight), [](py5graphics_stroke_cap), [](py5graphics_stroke_join), [](py5graphics_image_mode), [](py5graphics_rect_mode), [](py5graphics_ellipse_mode), [](py5graphics_color_mode), [](py5graphics_text_align), [](py5graphics_text_font), [](py5graphics_text_mode), [](py5graphics_text_size), and [](py5graphics_text_leading).

The `push()` and [](py5graphics_pop) functions can be used in place of [](py5graphics_push_matrix), [](py5graphics_pop_matrix), [](py5graphics_push_style), and [](py5graphics_pop_style). The difference is that `push()` and [](py5graphics_pop) control both the transformations (rotate, scale, translate) and the drawing styles at the same time.

This method can be used as a context manager to ensure that [](py5graphics_pop) always gets called, as shown in the example.

This method is the same as [](sketch_push) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_push).

Underlying Processing method: PGraphics.push

## Signatures

```python
push() -> None
```

Updated on March 06, 2023 02:49:26am UTC
