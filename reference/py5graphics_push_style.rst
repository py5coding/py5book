Py5Graphics.push_style()
========================

The ``push_style()`` function saves the current style settings and :doc:`py5graphics_pop_style` restores the prior settings.

Description
-----------

The ``push_style()`` function saves the current style settings and :doc:`py5graphics_pop_style` restores the prior settings. Note that these functions are always used together. They allow you to change the style settings and later return to what you had. When a new style is started with ``push_style()``, it builds on the current style information. The ``push_style()`` and :doc:`py5graphics_pop_style` method pairs can be nested to provide more control. (See the second example for a demonstration.)

The style information controlled by the following functions are included in the style: :doc:`py5graphics_fill`, :doc:`py5graphics_stroke`, :doc:`py5graphics_tint`, :doc:`py5graphics_stroke_weight`, :doc:`py5graphics_stroke_cap`, :doc:`py5graphics_stroke_join`, :doc:`py5graphics_image_mode`, :doc:`py5graphics_rect_mode`, :doc:`py5graphics_ellipse_mode`, :doc:`py5graphics_shape_mode`, :doc:`py5graphics_color_mode`, :doc:`py5graphics_text_align`, :doc:`py5graphics_text_font`, :doc:`py5graphics_text_mode`, :doc:`py5graphics_text_size`, :doc:`py5graphics_text_leading`, :doc:`py5graphics_emissive`, :doc:`py5graphics_specular`, :doc:`py5graphics_shininess`, and :doc:`py5graphics_ambient`.

This method is the same as :doc:`sketch_push_style` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_push_style`.

Underlying Java method: PGraphics.pushStyle

Syntax
------

.. code:: python

    push_style() -> None

Updated on September 11, 2021 16:51:34pm UTC

