Py5Graphics.pop_style()
=======================

The :doc:`py5graphics_push_style` function saves the current style settings and ``pop_style()`` restores the prior settings; these functions are always used together.

Description
-----------

The :doc:`py5graphics_push_style` function saves the current style settings and ``pop_style()`` restores the prior settings; these functions are always used together. They allow you to change the style settings and later return to what you had. When a new style is started with :doc:`py5graphics_push_style`, it builds on the current style information. The :doc:`py5graphics_push_style` and ``pop_style()`` method pairs can be nested to provide more control.

This method is the same as :doc:`sketch_pop_style` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_pop_style`.

Underlying Processing method: PGraphics.popStyle

Syntax
------

.. code:: python

    pop_style() -> None

Updated on November 12, 2021 11:30:58am UTC

