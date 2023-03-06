# Py5Font.get_name()

Get the font's name.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_name()](/images/reference/Py5Font_get_name_0.png)

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

Get the font's name.

Underlying Processing method: PFont.getName

## Signatures

```python
get_name() -> str
```

Updated on March 06, 2023 02:49:26am UTC
