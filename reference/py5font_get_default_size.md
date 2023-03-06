# Py5Font.get_default_size()

Get the font's size that will be used when [](sketch_text_font) is called.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_default_size()](/images/reference/Py5Font_get_default_size_0.png)

</div><div class="example-cell-code">

```python
def setup():
    font = py5.create_font('DejaVu Sans', 15)
    py5.text_font(font)

    py5.text(font.get_name(), 5, 20)
    py5.text(font.get_post_script_name(), 5, 40)
    py5.text(font.get_size(), 5, 60)
    py5.text(font.get_default_size(), 5, 80)
```

</div></div>

</div>

## Description

Get the font's size that will be used when [](sketch_text_font) is called. When drawing with 2x pixel density, bitmap fonts in OpenGL need to be created at double the requested size. This ensures that they're shown at half on displays (so folks don't have to change their sketch code).

Underlying Processing method: PFont.getDefaultSize

## Signatures

```python
get_default_size() -> int
```

Updated on March 06, 2023 02:49:26am UTC
