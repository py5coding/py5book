# pmouse_y

The system variable `pmouse_y` always contains the vertical position of the mouse in the frame previous to the current frame.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
# move the mouse quickly to see the difference
# between the current and previous position
def draw():
    py5.background(204)
    py5.line(20, py5.mouse_y, 80, py5.pmouse_y)
    py5.println(py5.mouse_y, ":", py5.pmouse_y)
```

</div></div>

</div>

## Description

The system variable `pmouse_y` always contains the vertical position of the mouse in the frame previous to the current frame.

For more detail on how `pmouse_y` is updated inside of mouse events and `draw()`, see the reference for [](sketch_pmouse_x).

Underlying Processing field: [pmouseY](https://processing.org/reference/pmouseY.html)

Updated on March 06, 2023 02:49:26am UTC
