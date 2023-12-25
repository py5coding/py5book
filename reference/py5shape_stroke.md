# Py5Shape.stroke()

Sets the color used to draw the `Py5Shape` object's lines.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for stroke()](/images/reference/Py5Shape_stroke_0.png)

</div><div class="example-cell-code">

```python
def setup():
    s = py5.create_shape()
    s.begin_shape()
    s.stroke(255, 0, 0)
    s.vertex(20, 80)
    s.vertex(50, 20)
    s.vertex(80, 80)
    s.end_shape(py5.CLOSE)

    py5.shape(s)
```

</div></div>

</div>

## Description

Sets the color used to draw the `Py5Shape` object's lines. This color is either specified in terms of the RGB or HSB color depending on the current [](sketch_color_mode). The default color space is RGB, with each value in the range from 0 to 255.

This method can only be used within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

When using hexadecimal notation to specify a color, use "`0x`" before the values (e.g., `0xFFCCFFAA`). The hexadecimal value must be specified with eight characters; the first two characters define the alpha component, and the remainder define the red, green, and blue components.

When using web color notation to specify a color, create a string beginning with the "`#`" character followed by three, four, six, or eight characters. The example colors `"#D93"` and `"#DD9933"` specify red, green, and blue values (in that order) for the color and assume the color has no transparency. The example colors `"#D93F"` and `"#DD9933FF"` specify red, green, blue, and alpha values (in that order) for the color. Notice that in web color notation the alpha channel is last, which is consistent with CSS colors, and in hexadecimal notation the alpha channel is first, which is consistent with Processing color values.

The value for the gray parameter must be less than or equal to the current maximum value as specified by [](sketch_color_mode). The default maximum value is 255.

When drawing in 2D with the default renderer, you may need `hint(ENABLE_STROKE_PURE)` to improve drawing quality (at the expense of performance). See the [](sketch_hint) documentation for more details.

This method has additional color functionality that is not reflected in the method's signatures. For example, you can pass the name of a color (e.g. "green", "mediumpurple", etc). Look at the online ["All About Colors"](/integrations/colors) Python Ecosystem Integration tutorial for more information.

Underlying Processing method: PShape.stroke

## Signatures

```python
stroke(
    gray: float,  # specifies a value between white and black
    /,
) -> None

stroke(
    gray: float,  # specifies a value between white and black
    alpha: float,  # opacity of the stroke
    /,
) -> None

stroke(
    rgb: int,  # color value in hexadecimal notation
    /,
) -> None

stroke(
    rgb: int,  # color value in hexadecimal notation
    alpha: float,  # opacity of the stroke
    /,
) -> None

stroke(
    x: float,  # red or hue value (depending on current color mode)
    y: float,  # green or saturation value (depending on current color mode)
    z: float,  # blue or brightness value (depending on current color mode)
    /,
) -> None

stroke(
    x: float,  # red or hue value (depending on current color mode)
    y: float,  # green or saturation value (depending on current color mode)
    z: float,  # blue or brightness value (depending on current color mode)
    alpha: float,  # opacity of the stroke
    /,
) -> None
```

Updated on December 25, 2023 16:36:33pm UTC
