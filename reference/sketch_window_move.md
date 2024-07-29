# window_move()

Set the Sketch's window location.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
py5.run_sketch(block=False)
# move the sketch window to the upper left corner of the display
py5.window_move(0, 0)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
# this sketch will hide itself and reappear elsewhere on your display.
def setup():
    global surface
    global visible
    surface = py5.get_surface()
    visible = True


def draw():
    global visible
    if py5.frame_count % 250 == 0:
        # this negates the visible variable
        visible = not visible
        if visible:
            py5.window_move(py5.random_int(py5.display_width),
                            py5.random_int(py5.display_height))
        surface.set_visible(visible)
```

</div></div>

</div>

## Description

Set the Sketch's window location. Calling this repeatedly from the `draw()` function may result in a sluggish Sketch. Negative or invalid coordinates are ignored. To hide a Sketch window, use [](py5surface_set_visible).

This method provides the same functionality as [](py5surface_set_location) but without the need to interact directly with the [](py5surface) object.

Underlying Processing method: [windowMove](https://processing.org/reference/windowMove_.html)

## Signatures

```python
window_move(
    x: int,  # x-coordinate for window location
    y: int,  # y-coordinate for window location
    /,
) -> None
```

Updated on May 02, 2024 02:48:11am UTC
