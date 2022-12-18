Py5Graphics.color()
===================

Creates colors for storing in variables of the ``color`` datatype (a 32 bit integer).

Description
-----------

Creates colors for storing in variables of the ``color`` datatype (a 32 bit integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending on the current :doc:`py5graphics_color_mode`. The default mode is ``RGB`` values from 0 to 255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow color (see the first example).

Note that if only one value is provided to ``color()``, it will be interpreted as a grayscale value. Add a second value, and it will be used for alpha transparency. When three values are specified, they are interpreted as either ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

Note that when using hexadecimal notation, it is not necessary to use ``color()``, as in: ``c = 0x006699``

This method is the same as :doc:`sketch_color` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_color`.

Underlying Processing method: PGraphics.color

Signatures
----------

.. code:: python

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

Updated on September 01, 2022 14:08:27pm UTC

