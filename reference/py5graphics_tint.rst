Py5Graphics.tint()
==================

Sets the fill value for displaying images.

Description
-----------

Sets the fill value for displaying images. Images can be tinted to specified colors or made transparent by including an alpha value.

To apply transparency to an image without affecting its color, use white as the tint color and specify an alpha value. For instance, ``tint(255, 128)`` will make an image 50% transparent (assuming the default alpha range of 0-255, which can be changed with :doc:`py5graphics_color_mode`).

When using hexadecimal notation to specify a color, use "``0x``" before the values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with eight characters; the first two characters define the alpha component, and the remainder define the red, green, and blue components.

When using web color notation to specify a color, create a string beginning with the "``#``" character followed by three, four, six, or eight characters. The example colors ``"#D93"`` and ``"#DD9933"`` specify red, green, and blue values (in that order) for the color and assume the color has no transparency. The example colors ``"#D93F"`` and ``"#DD9933FF"`` specify red, green, blue, and alpha values (in that order) for the color. Notice that in web color notation the alpha channel is last, which is consistent with CSS colors, and in hexadecimal notation the alpha channel is first, which is consistent with Processing color values.

The value for the gray parameter must be less than or equal to the current maximum value as specified by :doc:`py5graphics_color_mode`. The default maximum value is 255.

The ``tint()`` function is also used to control the coloring of textures in 3D.

This method is the same as :doc:`sketch_tint` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_tint`.

Underlying Processing method: PGraphics.tint

Signatures
----------

.. code:: python

    tint(
        gray: float,  # specifies a value between white and black
        /,
    ) -> None

    tint(
        gray: float,  # specifies a value between white and black
        alpha: float,  # opacity of the image
        /,
    ) -> None

    tint(
        rgb: int,  # color value in hexadecimal notation
        /,
    ) -> None

    tint(
        rgb: int,  # color value in hexadecimal notation
        alpha: float,  # opacity of the image
        /,
    ) -> None

    tint(
        v1: float,  # red or hue value (depending on current color mode)
        v2: float,  # green or saturation value (depending on current color mode)
        v3: float,  # blue or brightness value (depending on current color mode)
        /,
    ) -> None

    tint(
        v1: float,  # red or hue value (depending on current color mode)
        v2: float,  # green or saturation value (depending on current color mode)
        v3: float,  # blue or brightness value (depending on current color mode)
        alpha: float,  # opacity of the image
        /,
    ) -> None

Updated on September 01, 2022 14:08:27pm UTC

