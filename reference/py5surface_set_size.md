# Py5Surface.set_size()

Set a new width and height for the Sketch window.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def draw():
    py5.square(py5.random(py5.width), py5.random(py5.height), 10)

py5.run_sketch(block=False)

# while the sketch is running, get the surface and change the size
surface = py5.get_surface()
surface.set_size(400, 400)
```

</div></div>

</div>

## Description

Set a new width and height for the Sketch window. You do not need to call [](py5surface_set_resizable) before calling this.

Changing the window size will clear the drawing canvas. If you do this, the [](sketch_width) and [](sketch_height) variables will change.

This method provides the same functionality as [](sketch_window_resize).

Underlying Processing method: PSurface.setSize

## Signatures

```python
set_size(
    width: int,  # new window width
    height: int,  # new window height
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
