# Py5Font

Py5Font is the font class for py5.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for Py5Font](/images/reference/Py5Font_0.png)

</div><div class="example-cell-code">

```python
def setup():
    font = py5.create_font("DejaVu Sans", 32)
    py5.text_font(font)
    py5.text("word", 10, 50)
```

</div></div>

</div>

## Description

Py5Font is the font class for py5. To create a font to use with py5, use [](py5functions_create_font_file). This will create a font in the format py5 requires. Py5 displays fonts using the .vlw font format, which uses images for each letter, rather than defining them through vector data. The [](sketch_load_font) function constructs a new font and [](sketch_text_font) makes a font active. The [](py5font_list) method creates a list of the fonts installed on the computer, which is useful information to use with the [](sketch_create_font) function for dynamically converting fonts into a format to use with py5.

To create a new font dynamically, use the [](sketch_create_font) function. Do not use the syntax `Py5Font()`.

Underlying Processing class: [PFont](https://processing.org/reference/PFont.html)

The following methods and fields are provided:

```{include} include_py5font.md
```

Updated on March 06, 2023 02:49:26am UTC
