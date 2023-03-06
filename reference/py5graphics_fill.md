# Py5Graphics.fill()

Sets the color used to fill shapes.

## Description

Sets the color used to fill shapes. For example, if you run `fill(204, 102, 0)`, all subsequent shapes will be filled with orange. This color is either specified in terms of the `RGB` or `HSB` color depending on the current [](py5graphics_color_mode). The default color space is `RGB`, with each value in the range from 0 to 255.

When using hexadecimal notation to specify a color, use "`0x`" before the values (e.g., `0xFFCCFFAA`). The hexadecimal value must be specified with eight characters; the first two characters define the alpha component, and the remainder define the red, green, and blue components.

When using web color notation to specify a color, create a string beginning with the "`#`" character followed by three, four, six, or eight characters. The example colors `"#D93"` and `"#DD9933"` specify red, green, and blue values (in that order) for the color and assume the color has no transparency. The example colors `"#D93F"` and `"#DD9933FF"` specify red, green, blue, and alpha values (in that order) for the color. Notice that in web color notation the alpha channel is last, which is consistent with CSS colors, and in hexadecimal notation the alpha channel is first, which is consistent with Processing color values.

The value for the "gray" parameter must be less than or equal to the current maximum value as specified by [](py5graphics_color_mode). The default maximum value is 255.

To change the color of an image or a texture, use [](py5graphics_tint).

This method is the same as [](sketch_fill) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_fill).

Underlying Processing method: PGraphics.fill

## Signatures

```python
fill(
    gray: float,  # number specifying value between white and black
    /,
) -> None

fill(
    gray: float,  # number specifying value between white and black
    alpha: float,  # opacity of the fill
    /,
) -> None

fill(
    rgb: int,  # color variable or hex value
    /,
) -> None

fill(
    rgb: int,  # color variable or hex value
    alpha: float,  # opacity of the fill
    /,
) -> None

fill(
    v1: float,  # red or hue value (depending on current color mode)
    v2: float,  # green or saturation value (depending on current color mode)
    v3: float,  # blue or brightness value (depending on current color mode)
    /,
) -> None

fill(
    v1: float,  # red or hue value (depending on current color mode)
    v2: float,  # green or saturation value (depending on current color mode)
    v3: float,  # blue or brightness value (depending on current color mode)
    alpha: float,  # opacity of the fill
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
