# Py5Surface.set_icon()

Set the Sketch window icon.

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

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def settings():
    py5.size(200, 200, py5.P2D)
    PJOGL = py5.JClass("processing.opengl.PJOGL")
    PJOGL.setIcon("data/logo-64x64.png")


def setup():
    surface = py5.get_surface()
    surface.set_title("py5 window")
    surface.set_always_on_top(True)


py5.run_sketch(block=False)
```

</div></div>

</div>

## Description

Set the Sketch window icon. This will typically appear in the window's title bar. The default window icon is the same as Processing's.

This method will not work for the `P2D` or `P3D` renderers. Setting the icon for those renderers is a bit tricky; the icon must be a PNG file and it must be done in `settings()`. See the second example to learn how to do that.

Underlying Processing method: PSurface.setIcon

## Signatures

```python
set_icon(
    icon: Py5Image,  # image to use as the window icon
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
