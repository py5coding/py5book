# Py5Shape.color_mode()

Changes the way a `Py5Shape` object interprets color data.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for color_mode()](/images/reference/Py5Shape_color_mode_0.png)

</div><div class="example-cell-code">

```python
def setup():
    s = py5.create_shape()
    s.color_mode(s.RGB, 1.0)
    with s.begin_closed_shape():
        s.fill(0.8, 0.6, 0.4)
        s.vertex(20, 80)
        s.vertex(50, 20)
        s.vertex(80, 80)

    py5.shape(s)
```

</div></div>

</div>

## Description

Changes the way a `Py5Shape` object interprets color data. By default, the parameters for [](py5shape_fill) and [](py5shape_stroke) are defined by values between 0 and 255 using the `RGB` color model. The `color_mode()` function is used to change the numerical range used for specifying colors and to switch color systems. For example, calling `color_mode(RGB, 1.0)` will specify that values are specified between 0 and 1. The limits for defining colors are altered by setting the parameters `max`, `max_x`, `max_y`, `max_z`, and `max_a`.

After changing the range of values for colors with code like `color_mode(HSB, 360, 100, 100)`, those ranges remain in use until they are explicitly changed again. For example, after running `color_mode(HSB, 360, 100, 100)` and then changing back to `color_mode(RGB)`, the range for R will be 0 to 360 and the range for G and B will be 0 to 100. To avoid this, be explicit about the ranges when changing the color mode. For instance, instead of `color_mode(RGB)`, write `color_mode(RGB, 255, 255, 255)`.

Underlying Processing method: PShape.colorMode

## Signatures

```python
color_mode(
    mode: int,  # Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness
    /,
) -> None

color_mode(
    mode: int,  # Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness
    max: float,  # range for all color elements
    /,
) -> None

color_mode(
    mode: int,  # Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness
    max_x: float,  # range for the red or hue depending on the current color mode
    max_y: float,  # range for the green or saturation depending on the current color mode
    max_z: float,  # range for the blue or brightness depending on the current color mode
    /,
) -> None

color_mode(
    mode: int,  # Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness
    max_x: float,  # range for the red or hue depending on the current color mode
    max_y: float,  # range for the green or saturation depending on the current color mode
    max_z: float,  # range for the blue or brightness depending on the current color mode
    max_a: float,  # range for the alpha
    /,
) -> None
```

Updated on June 26, 2023 01:46:19am UTC
