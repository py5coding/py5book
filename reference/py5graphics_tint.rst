Py5Graphics.tint()
==================

Sets the fill value for displaying images.

Description
-----------

Sets the fill value for displaying images. Images can be tinted to specified colors or made transparent by including an alpha value.

To apply transparency to an image without affecting its color, use white as the tint color and specify an alpha value. For instance, ``tint(255, 128)`` will make an image 50% transparent (assuming the default alpha range of 0-255, which can be changed with :doc:`py5graphics_color_mode`).

When using hexadecimal notation to specify a color, use "``0x``" before the values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with eight characters; the first two characters define the alpha component, and the remainder define the red, green, and blue components.

When using web color notation to specify a color, create a four or seven character string beginning with the "``#``" character (e.g., ``"#FC3"`` or ``"#FFCC33"``). After the "``#``" character, the remainder of the string is similar to hexadecimal notation, but without an alpha component.

The value for the gray parameter must be less than or equal to the current maximum value as specified by :doc:`py5graphics_color_mode`. The default maximum value is 255.

The ``tint()`` function is also used to control the coloring of textures in 3D.

This method is the same as :doc:`sketch_tint` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_tint`.

Underlying Java method: PGraphics.tint

Syntax
------

.. code:: python

    tint(gray: float, /) -> None
    tint(gray: float, alpha: float, /) -> None
    tint(rgb: int, /) -> None
    tint(rgb: int, alpha: float, /) -> None
    tint(v1: float, v2: float, v3: float, /) -> None
    tint(v1: float, v2: float, v3: float, alpha: float, /) -> None

Parameters
----------

* **alpha**: `float` - opacity of the image
* **gray**: `float` - specifies a value between white and black
* **rgb**: `int` - color value in hexadecimal notation
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on September 11, 2021 16:51:34pm UTC

