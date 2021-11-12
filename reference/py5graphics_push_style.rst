Py5Graphics.push_style()
========================

The ``push_style()`` function saves the current style settings and :doc:`py5graphics_pop_style` restores the prior settings.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Graphics_push_style_0.png
    :alt: example picture for push_style()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)

        g = py5.create_graphics(60, 60, py5.P2D)
        with g.begin_draw():
            with g.push_style():
                g.stroke("#F00")
                with g.begin_closed_shape():
                    g.vertex(10, 10)
                    g.vertex(50, 10)
                    g.vertex(50, 50)
                    g.vertex(10, 50)
            with g.begin_closed_shape():
                g.vertex(12, 12)
                g.vertex(48, 12)
                g.vertex(48, 48)
                g.vertex(12, 48)

        py5.image(g, 0, 0)
        py5.image(g, 25, 25)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The ``push_style()`` function saves the current style settings and :doc:`py5graphics_pop_style` restores the prior settings. Note that these functions are always used together. They allow you to change the style settings and later return to what you had. When a new style is started with ``push_style()``, it builds on the current style information. The ``push_style()`` and :doc:`py5graphics_pop_style` method pairs can be nested to provide more control. (See the second example for a demonstration.)

The style information controlled by the following functions are included in the style: :doc:`py5graphics_fill`, :doc:`py5graphics_stroke`, :doc:`py5graphics_tint`, :doc:`py5graphics_stroke_weight`, :doc:`py5graphics_stroke_cap`, :doc:`py5graphics_stroke_join`, :doc:`py5graphics_image_mode`, :doc:`py5graphics_rect_mode`, :doc:`py5graphics_ellipse_mode`, :doc:`py5graphics_shape_mode`, :doc:`py5graphics_color_mode`, :doc:`py5graphics_text_align`, :doc:`py5graphics_text_font`, :doc:`py5graphics_text_mode`, :doc:`py5graphics_text_size`, :doc:`py5graphics_text_leading`, :doc:`py5graphics_emissive`, :doc:`py5graphics_specular`, :doc:`py5graphics_shininess`, and :doc:`py5graphics_ambient`.

This method can be used as a context manager to ensure that :doc:`py5graphics_pop_style` always gets called, as shown in the example.

This method is the same as :doc:`sketch_push_style` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_push_style`.

Underlying Processing method: PGraphics.pushStyle

Syntax
------

.. code:: python

    push_style() -> None

Updated on November 12, 2021 11:30:58am UTC

