# window_resize()

Set a new width and height for the Sketch window.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def draw():
    py5.square(py5.random(py5.width), py5.random(py5.height), 10)

py5.run_sketch(block=False)

# while the sketch is running, change the window size
py5.window_resize(400, 400)
```

</div></div>

</div>

## Description

Set a new width and height for the Sketch window. You do not need to call [](sketch_window_resizable) before calling this.

Changing the window size will clear the drawing canvas. If you do this, the [](sketch_width) and [](sketch_height) variables will change.

This method provides the same functionality as [](py5surface_set_size) but without the need to interact directly with the [](py5surface) object.

Underlying Processing method: [windowResize](https://processing.org/reference/windowResize_.html)

## Signatures

```python
window_resize(
    new_width: int,  # new window width
    new_height: int,  # new window height
    /,
) -> None
```

Updated on May 02, 2024 02:48:11am UTC
