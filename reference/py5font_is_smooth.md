# Py5Font.is_smooth()

Boolean value reflecting if smoothing (anti-aliasing) was used when the font was created.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for is_smooth()](/images/reference/Py5Font_is_smooth_0.png)

</div><div class="example-cell-code">

```python
def setup():
    font1 = py5.create_font('DejaVu Sans', 45)
    font2 = py5.create_font('DejaVu Sans', 45, False)

    py5.text_font(font1)
    py5.println(font1.is_smooth())
    py5.text('py5', 10, 40)

    py5.println(font2.is_smooth())
    py5.text_font(font2)
    py5.text('py5', 10, 90)
```

</div></div>

</div>

## Description

Boolean value reflecting if smoothing (anti-aliasing) was used when the font was created. By default, [](sketch_create_font) will use smoothing.

Underlying Processing method: PFont.isSmooth

## Signatures

```python
is_smooth() -> bool
```

Updated on March 06, 2023 02:49:26am UTC
