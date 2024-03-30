# pixel_density()

This function makes it possible for py5 to render using all of the pixels on high resolutions screens like Apple Retina displays and Windows High-DPI displays.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.pixel_density(2)
    py5.no_stroke()


def draw():
    py5.background(0)
    py5.ellipse(30, 48, 36, 36)
    py5.ellipse(70, 48, 36, 36)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.pixel_density(py5.display_density())
    # pulling the display's density dynamically
    py5.no_stroke()


def draw():
    py5.background(0)
    py5.ellipse(30, 48, 36, 36)
    py5.ellipse(70, 48, 36, 36)
```

</div></div>

</div>

## Description

This function makes it possible for py5 to render using all of the pixels on high resolutions screens like Apple Retina displays and Windows High-DPI displays. This function can only be run once within a program. It is intended to be called from the `settings()` function.

When programming in [module mode](content-py5-modes-module-mode) and [imported mode](content-py5-modes-imported-mode), py5 will allow calls to `pixel_density()` from the `setup()` function if it is called at the beginning of `setup()`. This allows the user to omit the `settings()` function, much like what can be done while programming in the Processing IDE. Py5 does this by inspecting the `setup()` function and attempting to split it into synthetic `settings()` and `setup()` functions if both were not created by the user and the real `setup()` function contains a call to `pixel_density()`, or calls to [](sketch_size), [](sketch_full_screen), [](sketch_smooth), or [](sketch_no_smooth). Calls to those functions must be at the very beginning of `setup()`, before any other Python code (but comments are ok). This feature is not available when programming in [class mode](content-py5-modes-class-mode).

The `pixel_density()` should only be used with hardcoded numbers (in almost all cases this number will be 2) or in combination with [](sketch_display_density) as in the second example.

When the pixel density is set to more than 1, it changes all of the pixel operations including the way [](sketch_get_pixels), [](sketch_set_pixels), [](sketch_blend), [](sketch_copy), [](sketch_update_pixels), and [](sketch_update_np_pixels) all work. See the reference for [](sketch_pixel_width) and [](sketch_pixel_height) for more information.

Underlying Processing method: [pixelDensity](https://processing.org/reference/pixelDensity_.html)

## Signatures

```python
pixel_density(
    density: int,  # 1 or 2
    /,
) -> None
```

Updated on March 18, 2024 05:08:14am UTC
