# pmouse_x

The variable `pmouse_x` always contains the horizontal position of the mouse in the frame previous to the current frame.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
# move the mouse quickly to see the difference
# between the current and previous position
def draw():
    py5.background(204)
    py5.line(py5.mouse_x, 20, py5.pmouse_x, 80)
    py5.println(py5.mouse_x, ":", py5.pmouse_x)
```

</div></div>

</div>

## Description

The variable `pmouse_x` always contains the horizontal position of the mouse in the frame previous to the current frame.

You may find that `pmouse_x` and [](sketch_pmouse_y) have different values when referenced inside of `draw()` and inside of mouse events like `mouse_pressed()` and `mouse_moved()`. Inside `draw()`, `pmouse_x` and [](sketch_pmouse_y) update only once per frame (once per trip through the `draw()` loop). But inside mouse events, they update each time the event is called. If these values weren't updated immediately during mouse events, then the mouse position would be read only once per frame, resulting in slight delays and choppy interaction. If the mouse variables were always updated multiple times per frame, then something like `line(pmouse_x, pmouse_y, mouse_x, mouse_y)` inside `draw()` would have lots of gaps, because `pmouse_x` may have changed several times in between the calls to [](sketch_line).

If you want values relative to the previous frame, use `pmouse_x` and [](sketch_pmouse_y) inside `draw()`. If you want continuous response, use `pmouse_x` and [](sketch_pmouse_y) inside the mouse event functions.

Underlying Processing field: [pmouseX](https://processing.org/reference/pmouseX.html)

Updated on December 07, 2024 22:07:08pm UTC
