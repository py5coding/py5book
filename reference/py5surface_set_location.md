# Py5Surface.set_location()

Set the Sketch's window location.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
py5.run_sketch(block=False)
surface = py5.get_surface()
# move the sketch window to the upper left corner of the display
surface.set_location(0, 0)
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
            surface.set_location(py5.random_int(py5.display_width),
                                 py5.random_int(py5.display_height))
        surface.set_visible(visible)
```

</div></div>

</div>

## Description

Set the Sketch's window location. Calling this repeatedly from the `draw()` function may result in a sluggish Sketch. Negative or invalid coordinates are ignored. To hide a Sketch window, use [](py5surface_set_visible).

This method provides the same functionality as [](sketch_window_move).

Underlying Processing method: PSurface.setLocation

## Signatures

```python
set_location(
    x: int,  # x-coordinate for window location
    y: int,  # y-coordinate for window location
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
