# Py5Graphics.push_style()

The `push_style()` function saves the current style settings and [](py5graphics_pop_style) restores the prior settings.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for push_style()](/images/reference/Py5Graphics_push_style_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P2D)

    g = py5.create_graphics(60, 60, py5.P2D)
    with g.begin_draw():
        with g.push_style():
            g.stroke("#F00")
            with g.begin_closed_shape():
                g.vertex(10, 10)
                g.vertex(50, 10)
                g.vertex(50, 50)
                g.vertex(10, 50)
        with g.begin_closed_shape():
            g.vertex(12, 12)
            g.vertex(48, 12)
            g.vertex(48, 48)
            g.vertex(12, 48)

    py5.image(g, 0, 0)
    py5.image(g, 25, 25)
```

</div></div>

</div>

## Description

The `push_style()` function saves the current style settings and [](py5graphics_pop_style) restores the prior settings. Note that these functions are always used together. They allow you to change the style settings and later return to what you had. When a new style is started with `push_style()`, it builds on the current style information. The `push_style()` and [](py5graphics_pop_style) method pairs can be nested to provide more control. (See the second example for a demonstration.)

The style information controlled by the following functions are included in the style: [](py5graphics_fill), [](py5graphics_stroke), [](py5graphics_tint), [](py5graphics_stroke_weight), [](py5graphics_stroke_cap), [](py5graphics_stroke_join), [](py5graphics_image_mode), [](py5graphics_rect_mode), [](py5graphics_ellipse_mode), [](py5graphics_shape_mode), [](py5graphics_color_mode), [](py5graphics_text_align), [](py5graphics_text_font), [](py5graphics_text_mode), [](py5graphics_text_size), [](py5graphics_text_leading), [](py5graphics_emissive), [](py5graphics_specular), [](py5graphics_shininess), and [](py5graphics_ambient).

This method can be used as a context manager to ensure that [](py5graphics_pop_style) always gets called, as shown in the example.

This method is the same as [](sketch_push_style) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_push_style).

Underlying Processing method: PGraphics.pushStyle

## Signatures

```python
push_style() -> None
```

Updated on March 06, 2023 02:49:26am UTC
