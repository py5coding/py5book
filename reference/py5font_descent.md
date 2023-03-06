# Py5Font.descent()

Get the descent of this font from the baseline.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for descent()](/images/reference/Py5Font_descent_0.png)

</div><div class="example-cell-code">

```python
def setup():
    font_size = 45
    font = py5.create_font('DejaVu Sans', font_size)
    py5.text_font(font)

    baseline = py5.height / 2
    ascent = baseline - font.ascent() * font_size
    descent = baseline + font.descent() * font_size

    py5.text("py5", 10, baseline)
    py5.line(0, ascent, py5.width, ascent)
    py5.line(0, baseline, py5.width, baseline)
    py5.line(0, descent, py5.width, descent)
```

</div></div>

</div>

## Description

Get the descent of this font from the baseline. The value is based on a font of size 1. Multiply it by the font size to get the offset from the baseline.

Underlying Processing method: PFont.descent

## Signatures

```python
descent() -> float
```

Updated on March 06, 2023 02:49:26am UTC
