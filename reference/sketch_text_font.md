# text_font()

Sets the current font that will be drawn with the [](sketch_text) function.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for text_font()](/images/reference/Sketch_text_font_0.png)

</div><div class="example-cell-code">

```python
def setup():
    # the font "andalemo.ttf" must be located in the
    # current sketch's "data" directory to load successfully
    mono = py5.create_font("andalemo.ttf", 32)
    py5.background(0)
    py5.text_font(mono)
    py5.text("word", 12, 60)
```

</div></div>

</div>

## Description

Sets the current font that will be drawn with the [](sketch_text) function. Fonts must be created for py5 with [](sketch_create_font) or loaded with [](sketch_load_font) before they can be used. The font set through `text_font()` will be used in all subsequent calls to the [](sketch_text) function. If no `size` parameter is specified, the font size defaults to the original size (the size in which it was created with [](py5functions_create_font_file)) overriding any previous calls to `text_font()` or [](sketch_text_size).

When fonts are rendered as an image texture (as is the case with the `P2D` and `P3D` renderers as well as with [](sketch_load_font) and vlw files), you should create fonts at the sizes that will be used most commonly. Using `text_font()` without the size parameter will result in the cleanest type.

Underlying Processing method: [textFont](https://processing.org/reference/textFont_.html)

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
