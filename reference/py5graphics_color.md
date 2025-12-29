# Py5Graphics.color()

Creates colors for storing in variables of the `color` datatype (a 32 bit integer).

## Description

Creates colors for storing in variables of the `color` datatype (a 32 bit integer). The parameters are interpreted as `RGB` or `HSB` values depending on the current [](py5graphics_color_mode). The default mode is `RGB` values from 0 to 255 and, therefore, `color(255, 204, 0)` will return a bright yellow color (see the first example).

Note that if only one value is provided to `color()`, it will be interpreted as a grayscale value. Add a second value, and it will be used for alpha transparency. When three values are specified, they are interpreted as either `RGB` or `HSB` values. Adding a fourth value applies alpha transparency.

Note that when using hexadecimal notation, it is not necessary to use `color()`, as in: `c = 0x006699`

If you have matplotlib installed, you can  create colors using matplotlib's named colors by passing a color name as a string to this method. See the list of named colors in the [Matplotlib Named Colors reference](https://matplotlib.org/stable/gallery/color/named_colors.html). For more information, see the Matplotlib Named Colors section in the <a href="/integrations/colors.html#matplotlib-named-colors">All About Colors</a> integration documentation page. There's also other color related information on that page; go read it to learn more about various ways py5 makes it easy for you to work with color.

This method is the same as [](sketch_color) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_color).

Underlying Processing method: PGraphics.color

## Signatures

```python
color(
    c: int,  # color value
    /,
) -> int

color(
    c: int,  # color value
    alpha: float,  # alpha value relative to current color range
    /,
) -> int

color(
    c: int,  # color value
    alpha: int,  # alpha value relative to current color range
    /,
) -> int

color(
    gray: float,  # gray value relative to current color range
    /,
) -> int

color(
    gray: float,  # gray value relative to current color range
    alpha: float,  # alpha value relative to current color range
    /,
) -> int

color(
    hex_code: str,  # hex color code
    /,
) -> int

color(
    hex_code: str,  # hex color code
    alpha: int,  # alpha value relative to current color range
    /,
) -> int

color(
    v1: float,  # red or hue values relative to the current color range
    v2: float,  # green or saturation values relative to the current color range
    v3: float,  # blue or brightness values relative to the current color range
    /,
) -> int

color(
    v1: float,  # red or hue values relative to the current color range
    v2: float,  # green or saturation values relative to the current color range
    v3: float,  # blue or brightness values relative to the current color range
    a: float,  # alpha value relative to current color range
    /,
) -> int

color(
    v1: int,  # red or hue values relative to the current color range
    v2: int,  # green or saturation values relative to the current color range
    v3: int,  # blue or brightness values relative to the current color range
    /,
) -> int

color(
    v1: int,  # red or hue values relative to the current color range
    v2: int,  # green or saturation values relative to the current color range
    v3: int,  # blue or brightness values relative to the current color range
    a: int,  # alpha value relative to current color range
    /,
) -> int
```

Updated on December 28, 2025 07:16:49am UTC
