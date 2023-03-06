# Py5Surface.set_always_on_top()

Set the Sketch window to always be on top of other windows.

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

Set the Sketch window to always be on top of other windows. By default, the Sketch window can be covered by other windows. Setting this to `True` will keep that from happening.

Underlying Processing method: PSurface.setAlwaysOnTop

## Signatures

```python
set_always_on_top(
    always: bool,  # should the Sketch window always be on top of other windows
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
