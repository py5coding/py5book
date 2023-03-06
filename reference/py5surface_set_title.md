# Py5Surface.set_title()

Set the Sketch window's title.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    surface = py5.get_surface()
    surface.set_title("py5 window")
    surface.set_always_on_top(True)
    surface.set_icon(py5.load_image("logo-64x64.png"))
```

</div></div>

</div>

## Description

Set the Sketch window's title. This will typically appear at the window's title bar. The default window title is "Sketch".

This method provides the same functionality as [](sketch_window_title).

Underlying Processing method: PSurface.setTitle

## Signatures

```python
set_title(
    title: str,  # new window title
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
