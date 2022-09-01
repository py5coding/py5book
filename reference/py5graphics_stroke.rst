Py5Graphics.stroke()
====================

Sets the color used to draw lines and borders around shapes.

Description
-----------

Sets the color used to draw lines and borders around shapes. This color is either specified in terms of the RGB or HSB color depending on the current :doc:`py5graphics_color_mode`. The default color space is RGB, with each value in the range from 0 to 255.

When using hexadecimal notation to specify a color, use "``0x``" before the values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with eight characters; the first two characters define the alpha component, and the remainder define the red, green, and blue components.

When using web color notation to specify a color, create a string beginning with the "``#``" character followed by three, four, six, or eight characters. The example colors ``"#D93"`` and ``"#DD9933"`` specify red, green, and blue values (in that order) for the color and assume the color has no transparency. The example colors ``"#D93F"`` and ``"#DD9933FF"`` specify red, green, blue, and alpha values (in that order) for the color. Notice that in web color notation the alpha channel is last, which is consistent with CSS colors, and in hexadecimal notation the alpha channel is first, which is consistent with Processing color values.

The value for the gray parameter must be less than or equal to the current maximum value as specified by :doc:`py5graphics_color_mode`. The default maximum value is 255.

When drawing in 2D with the default renderer, you may need ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of performance). See the :doc:`py5graphics_hint` documentation for more details.

This method is the same as :doc:`sketch_stroke` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_stroke`.

Underlying Processing method: PGraphics.stroke

Signatures
----------

.. code:: python

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
        v1: float,  # red or hue value (depending on current color mode)
        v2: float,  # green or saturation value (depending on current color mode)
        v3: float,  # blue or brightness value (depending on current color mode)
        /,
    ) -> None

    stroke(
        v1: float,  # red or hue value (depending on current color mode)
        v2: float,  # green or saturation value (depending on current color mode)
        v3: float,  # blue or brightness value (depending on current color mode)
        alpha: float,  # opacity of the stroke
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

