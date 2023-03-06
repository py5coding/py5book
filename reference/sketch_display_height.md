# display_height

System variable that stores the height of the entire screen display.

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

System variable that stores the height of the entire screen display. This can be used to run a full-screen program on any display size, but calling [](sketch_full_screen) is usually a better choice.

Underlying Processing field: [displayHeight](https://processing.org/reference/displayHeight.html)

Updated on March 06, 2023 02:49:26am UTC
