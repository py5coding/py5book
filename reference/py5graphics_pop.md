# Py5Graphics.pop()

The `pop()` function restores the previous drawing style settings and transformations after [](py5graphics_push) has changed them.

## Description

The `pop()` function restores the previous drawing style settings and transformations after [](py5graphics_push) has changed them. Note that these functions are always used together. They allow you to change the style and transformation settings and later return to what you had. When a new state is started with [](py5graphics_push), it builds on the current style and transform information.

[](py5graphics_push) stores information related to the current transformation state and style settings controlled by the following functions: [](py5graphics_rotate), [](py5graphics_translate), [](py5graphics_scale), [](py5graphics_fill), [](py5graphics_stroke), [](py5graphics_tint), [](py5graphics_stroke_weight), [](py5graphics_stroke_cap), [](py5graphics_stroke_join), [](py5graphics_image_mode), [](py5graphics_rect_mode), [](py5graphics_ellipse_mode), [](py5graphics_color_mode), [](py5graphics_text_align), [](py5graphics_text_font), [](py5graphics_text_mode), [](py5graphics_text_size), and [](py5graphics_text_leading).

The [](py5graphics_push) and `pop()` functions can be used in place of [](py5graphics_push_matrix), [](py5graphics_pop_matrix), [](py5graphics_push_style), and [](py5graphics_pop_style). The difference is that [](py5graphics_push) and `pop()` control both the transformations (rotate, scale, translate) and the drawing styles at the same time.

This method is the same as [](sketch_pop) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_pop).

Underlying Processing method: PGraphics.pop

## Signatures

```python
pop() -> None
```

Updated on March 06, 2023 02:49:26am UTC
