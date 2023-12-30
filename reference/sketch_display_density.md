# display_density()

This function returns the number "2" if the screen is a high-density screen (called a Retina display on macOS or high-dpi on Windows and Linux) and a "1" if not.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.pixel_density(py5.display_density())
    py5.no_stroke()


def draw():
    py5.background(0)
    py5.ellipse(30, 48, 36, 36)
    py5.ellipse(70, 48, 36, 36)
```

</div></div>

</div>

## Description

This function returns the number "2" if the screen is a high-density screen (called a Retina display on macOS or high-dpi on Windows and Linux) and a "1" if not. This information is useful for a program to adapt to run at double the pixel density on a screen that supports it.

Underlying Processing method: [displayDensity](https://processing.org/reference/displayDensity_.html)

## Signatures

```python
display_density() -> int

display_density(
    display: int,  # the display number to check (1-indexed to match the Preferences dialog box)
    /,
) -> int
```

Updated on December 27, 2023 13:47:02pm UTC
