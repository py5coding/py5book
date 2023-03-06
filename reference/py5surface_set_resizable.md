# Py5Surface.set_resizable()

Set the Sketch window as resizable by the user.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    surface = py5.get_surface()
    surface.set_resizable(True)


def draw():
    py5.square(py5.random(py5.width), py5.random(py5.height), 10)
```

</div></div>

</div>

## Description

Set the Sketch window as resizable by the user. The user will be able to resize the window in the same way as they do for many other windows on their computer. By default, the Sketch window is not resizable.

Changing the window size will clear the drawing canvas. If you do this, the [](sketch_width) and [](sketch_height) variables will change.

This method provides the same functionality as [](sketch_window_resizable).

Underlying Processing method: PSurface.setResizable

## Signatures

```python
set_resizable(
    resizable: bool,  # should the Sketch window be resizable
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
