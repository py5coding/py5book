# display_width

Variable that stores the width of the entire screen display.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(py5.display_width, py5.display_height)
    py5.line(0, 0, py5.width, py5.height)
```

</div></div>

</div>

## Description

Variable that stores the width of the entire screen display. This can be used to run a full-screen program on any display size, but calling [](sketch_full_screen) is usually a better choice.

Underlying Processing field: [displayWidth](https://processing.org/reference/displayWidth.html)

Updated on December 07, 2024 22:07:08pm UTC
