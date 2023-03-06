# Py5Font.get_size()

Get the font's size.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_size()](/images/reference/Py5Font_get_size_0.png)

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

Get the font's size.

Underlying Processing method: PFont.getSize

## Signatures

```python
get_size() -> int
```

Updated on March 06, 2023 02:49:26am UTC
