# Py5Font.get_glyph_count()

Get the number of glyphs contained in the font.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_glyph_count()](/images/reference/Py5Font_get_glyph_count_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P2D)
    font_size = 32
    font1 = py5.create_font('DejaVu Sans', font_size)
    font2 = py5.load_font('DejaVu_Sans-32.vlw')
    font3 = py5.create_font('DejaVu Sans', font_size, True, 'py5')

    py5.println(font1.get_glyph_count())
    py5.println(font2.get_glyph_count())
    py5.println(font3.get_glyph_count())

    py5.text_font(font1)
    py5.text('py5', 10, 30)

    py5.text_font(font2)
    py5.text('py5', 10, 60)

    py5.text_font(font3)
    py5.text('py5', 10, 90)
```

</div></div>

</div>

## Description

Get the number of glyphs contained in the font. This will be 0 if the font is a "lazy font" that creates glyphs as they are needed by the Sketch. This will be the case if the font was created with [](sketch_create_font) without using the `charset` parameter.

Underlying Processing method: PFont.getGlyphCount

## Signatures

```python
get_glyph_count() -> int
```

Updated on March 06, 2023 02:49:26am UTC
