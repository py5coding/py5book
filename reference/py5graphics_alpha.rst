Py5Graphics.alpha()
===================

Extracts the alpha value from a color, scaled to match current :doc:`py5graphics_color_mode`.

Description
-----------

Extracts the alpha value from a color, scaled to match current :doc:`py5graphics_color_mode`.

The ``alpha()`` function is easy to use and understand, but it is slower than a technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can achieve the same results as ``alpha()`` but with greater speed by using the right shift operator (``>>``) with a bit mask. For example, ``alpha(c)`` and ``c >> 24 & 0xFF`` both extract the alpha value from a color variable ``c`` but the later is faster.

This method is the same as :doc:`sketch_alpha` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_alpha`.

Underlying Processing method: PGraphics.alpha

Signatures
------

.. code:: python

    alpha(
        rgb: int,  # any value of the color datatype
        /,
    ) -> float
Updated on August 25, 2022 19:59:03pm UTC

