Py5Graphics.color_mode()
========================

Changes the way py5 interprets color data.

Description
-----------

Changes the way py5 interprets color data. By default, the parameters for :doc:`py5graphics_fill`, :doc:`py5graphics_stroke`, :doc:`py5graphics_background`, and :doc:`py5graphics_color` are defined by values between 0 and 255 using the ``RGB`` color model. The ``color_mode()`` function is used to change the numerical range used for specifying colors and to switch color systems. For example, calling ``color_mode(RGB, 1.0)`` will specify that values are specified between 0 and 1. The limits for defining colors are altered by setting the parameters ``max``, ``max1``, ``max2``, ``max3``, and ``max_a``.

After changing the range of values for colors with code like ``color_mode(HSB, 360, 100, 100)``, those ranges remain in use until they are explicitly changed again. For example, after running ``color_mode(HSB, 360, 100, 100)`` and then changing back to ``color_mode(RGB)``, the range for R will be 0 to 360 and the range for G and B will be 0 to 100. To avoid this, be explicit about the ranges when changing the color mode. For instance, instead of ``color_mode(RGB)``, write ``color_mode(RGB, 255, 255, 255)``.

This method is the same as :doc:`sketch_color_mode` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_color_mode`.

Underlying Processing method: PGraphics.colorMode

Signatures
----------

.. code:: python

    color_mode(
        mode: int,  # Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness
        /,
    ) -> None

    color_mode(
        mode: int,  # Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness
        max1: float,  # range for the red or hue depending on the current color mode
        max2: float,  # range for the green or saturation depending on the current color mode
        max3: float,  # range for the blue or brightness depending on the current color mode
        /,
    ) -> None

    color_mode(
        mode: int,  # Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness
        max1: float,  # range for the red or hue depending on the current color mode
        max2: float,  # range for the green or saturation depending on the current color mode
        max3: float,  # range for the blue or brightness depending on the current color mode
        max_a: float,  # range for the alpha
        /,
    ) -> None

    color_mode(
        mode: int,  # Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness
        max: float,  # range for all color elements
        /,
    ) -> None

Updated on September 01, 2022 14:08:27pm UTC

