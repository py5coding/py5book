Py5Graphics.green()
===================

Extracts the green value from a color, scaled to match current :doc:`py5graphics_color_mode`.

Description
-----------

Extracts the green value from a color, scaled to match current :doc:`py5graphics_color_mode`.

The ``green()`` function is easy to use and understand, but it is slower than a technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can achieve the same results as ``green()`` but with greater speed by using the right shift operator (``>>``) with a bit mask. For example, ``green(c)`` and ``c >> 8 & 0xFF`` both extract the green value from a color variable ``c`` but the later is faster.

This method is the same as :doc:`sketch_green` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_green`.

Underlying Java method: PGraphics.green

Syntax
------

.. code:: python

    green(rgb: int, /) -> float

Parameters
----------

* **rgb**: `int` - any value of the color datatype


Updated on September 11, 2021 16:51:34pm UTC

