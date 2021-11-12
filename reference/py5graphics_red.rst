Py5Graphics.red()
=================

Extracts the red value from a color, scaled to match current :doc:`py5graphics_color_mode`.

Description
-----------

Extracts the red value from a color, scaled to match current :doc:`py5graphics_color_mode`.

The ``red()`` function is easy to use and understand, but it is slower than a technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can achieve the same results as ``red()`` but with greater speed by using the right shift operator (``>>``) with a bit mask. For example, ``red(c)`` and ``c >> 16 & 0xFF`` both extract the red value from a color variable ``c`` but the later is faster.

This method is the same as :doc:`sketch_red` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_red`.

Underlying Processing method: PGraphics.red

Syntax
------

.. code:: python

    red(rgb: int, /) -> float

Parameters
----------

* **rgb**: `int` - any value of the color datatype


Updated on November 12, 2021 11:30:58am UTC

