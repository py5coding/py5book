# window_resizable()

Set the Sketch window as resizable by the user.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.window_resizable(True)


def draw():
    py5.square(py5.random(py5.width), py5.random(py5.height), 10)
```

</div></div>

</div>

## Description

Set the Sketch window as resizable by the user. The user will be able to resize the window in the same way as they do for many other windows on their computer. By default, the Sketch window is not resizable.

Changing the window size will clear the drawing canvas. If you do this, the [](sketch_width) and [](sketch_height) variables will change.

This method provides the same functionality as [](py5surface_set_resizable) but without the need to interact directly with the [](py5surface) object.

Underlying Processing method: [windowResizable](https://processing.org/reference/windowResizable_.html)

## Signatures

```python
window_resizable(
    resizable: bool,  # should the Sketch window be resizable
    /,
) -> None
```

Updated on May 02, 2024 02:48:11am UTC
