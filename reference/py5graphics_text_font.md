# Py5Graphics.text_font()

Sets the current font that will be drawn with the [](py5graphics_text) function.

## Description

Sets the current font that will be drawn with the [](py5graphics_text) function. Fonts must be created for py5 with [](sketch_create_font) or loaded with [](sketch_load_font) before they can be used. The font set through `text_font()` will be used in all subsequent calls to the [](py5graphics_text) function. If no `size` parameter is specified, the font size defaults to the original size (the size in which it was created with [](py5functions_create_font_file)) overriding any previous calls to `text_font()` or [](py5graphics_text_size).

When fonts are rendered as an image texture (as is the case with the `P2D` and `P3D` renderers as well as with [](sketch_load_font) and vlw files), you should create fonts at the sizes that will be used most commonly. Using `text_font()` without the size parameter will result in the cleanest type.

This method is the same as [](sketch_text_font) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_text_font).

Underlying Processing method: PGraphics.textFont

## Signatures

```python
text_font(
    which: Py5Font,  # any variable of the type Py5Font
    /,
) -> None

text_font(
    which: Py5Font,  # any variable of the type Py5Font
    size: float,  # the size of the letters in units of pixels
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC