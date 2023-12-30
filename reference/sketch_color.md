# color()

Creates colors for storing in variables of the `color` datatype (a 32 bit integer).

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for color()](/images/reference/Sketch_color_0.png)

</div><div class="example-cell-code">

```python
def setup():
    c = py5.color(255, 204, 0)  # define color 'c'
    py5.fill(c)  # use color variable 'c' as fill color
    py5.no_stroke()  # don't draw a stroke around shapes
    py5.rect(30, 20, 55, 55)  # draw rectangle
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for color()](/images/reference/Sketch_color_1.png)

</div><div class="example-cell-code">

```python
def setup():
    c = py5.color(255, 204, 0)  # define color 'c'
    py5.fill(c)  # use color variable 'c' as fill color
    py5.no_stroke()  # don't draw a stroke around shapes
    py5.ellipse(25, 25, 80, 80)  # draw left circle
    
    # using only one value with color()
    # generates a grayscale value.
    c = py5.color(65)  # update 'c' with grayscale value
    py5.fill(c)  # use updated 'c' as fill color
    py5.ellipse(75, 75, 80, 80)  # draw right circle
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for color()](/images/reference/Sketch_color_2.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.no_stroke()  # don't draw a stroke around shapes
    
    # if no color_mode is specified, then the
    # default of RGB with scale of 0-255 is used.
    c = py5.color(50, 55, 100)  # create a color for 'c'
    py5.fill(c)  # use color variable 'c' as fill color
    py5.rect(0, 10, 45, 80)  # draw left rect
    
    py5.color_mode(py5.HSB, 100)  # use HSB with scale of 0-100
    c = py5.color(50, 55, 100)  # update 'c' with new color
    py5.fill(c)  # use updated 'c' as fill color
    py5.rect(55, 10, 45, 80)  # draw right rect
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for color()](/images/reference/Sketch_color_3.png)

</div><div class="example-cell-code">

```python
def setup():
    c = 0xFFFFCC00  # define color 'c' using hex notation
    py5.fill(c)  # use color variable 'c' as fill color
    py5.no_stroke()  # don't draw a stroke around shapes
    py5.ellipse(25, 25, 80, 80)  # draw left circle
    
    c = "#00CCFF"  # define color 'c' using web color notation
    py5.fill(c)  # use updated 'c' as fill color
    py5.ellipse(75, 75, 80, 80)  # draw right circle
```

</div></div>

</div>

## Description

Creates colors for storing in variables of the `color` datatype (a 32 bit integer). The parameters are interpreted as `RGB` or `HSB` values depending on the current [](sketch_color_mode). The default mode is `RGB` values from 0 to 255 and, therefore, `color(255, 204, 0)` will return a bright yellow color (see the first example).

Note that if only one value is provided to `color()`, it will be interpreted as a grayscale value. Add a second value, and it will be used for alpha transparency. When three values are specified, they are interpreted as either `RGB` or `HSB` values. Adding a fourth value applies alpha transparency.

Note that you can also use hexadecimal notation and web color notation to specify colors, as in `c = 0xFFDDCC33` or `c = "#DDCC33FF"` in place of `c = color(221, 204, 51, 255)`. Additionally, the `color()` method can accept both color notations as a parameter.

When using hexadecimal notation to specify a color, use "`0x`" before the values (e.g., `0xFFCCFFAA`). The hexadecimal value must be specified with eight characters; the first two characters define the alpha component, and the remainder define the red, green, and blue components.

When using web color notation to specify a color, create a string beginning with the "`#`" character followed by three, four, six, or eight characters. The example colors `"#D93"` and `"#DD9933"` specify red, green, and blue values (in that order) for the color and assume the color has no transparency. The example colors `"#D93F"` and `"#DD9933FF"` specify red, green, blue, and alpha values (in that order) for the color. Notice that in web color notation the alpha channel is last, which is consistent with CSS colors, and in hexadecimal notation the alpha channel is first, which is consistent with Processing color values.

Underlying Processing method: [color](https://processing.org/reference/color_.html)

## Signatures

```python
color(
    cmap_input: float,  # input value when using colormap color mode
    /,
) -> int

color(
    cmap_input: float,  # input value when using colormap color mode
    alpha: int,  # alpha value relative to current color range
    /,
) -> int

color(
    fgray: float,  # number specifying value between white and black
    /,
) -> int

color(
    fgray: float,  # number specifying value between white and black
    falpha: float,  # alpha value relative to current color range
    /,
) -> int

color(
    gray: int,  # number specifying value between white and black
    /,
) -> int

color(
    gray: int,  # number specifying value between white and black
    alpha: int,  # alpha value relative to current color range
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
    alpha: float,  # alpha value relative to current color range
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
    alpha: int,  # alpha value relative to current color range
    /,
) -> int
```

Updated on October 06, 2023 13:36:04pm UTC
