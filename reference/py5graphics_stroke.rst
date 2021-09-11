Py5Graphics.stroke()
====================

Sets the color used to draw lines and borders around shapes.

Description
-----------

Sets the color used to draw lines and borders around shapes. This color is either specified in terms of the RGB or HSB color depending on the current :doc:`py5graphics_color_mode`. The default color space is RGB, with each value in the range from 0 to 255.

When using hexadecimal notation to specify a color, use "``0x``" before the values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with eight characters; the first two characters define the alpha component, and the remainder define the red, green, and blue components.

When using web color notation to specify a color, create a four or seven character string beginning with the "``#``" character (e.g., ``"#FC3"`` or ``"#FFCC33"``). After the "``#``" character, the remainder of the string is similar to hexadecimal notation, but without an alpha component.

The value for the gray parameter must be less than or equal to the current maximum value as specified by :doc:`py5graphics_color_mode`. The default maximum value is 255.

When drawing in 2D with the default renderer, you may need ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of performance). See the :doc:`py5graphics_hint` documentation for more details.

This method is the same as :doc:`sketch_stroke` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_stroke`.

Underlying Java method: PGraphics.stroke

Syntax
------

.. code:: python

    stroke(gray: float, /) -> None
    stroke(gray: float, alpha: float, /) -> None
    stroke(rgb: int, /) -> None
    stroke(rgb: int, alpha: float, /) -> None
    stroke(v1: float, v2: float, v3: float, /) -> None
    stroke(v1: float, v2: float, v3: float, alpha: float, /) -> None

Parameters
----------

* **alpha**: `float` - opacity of the stroke
* **gray**: `float` - specifies a value between white and black
* **rgb**: `int` - color value in hexadecimal notation
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on September 11, 2021 16:51:34pm UTC

