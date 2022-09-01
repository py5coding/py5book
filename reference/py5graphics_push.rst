Py5Graphics.push()
==================

The ``push()`` function saves the current drawing style settings and transformations, while :doc:`py5graphics_pop` restores these settings.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Graphics_push_0.png
    :alt: example picture for push()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)

        g = py5.create_graphics(60, 60, py5.P2D)
        with g.begin_draw():
            g.translate(30, 30)
            with g.push():
                g.stroke("#F00")
                g.scale(2)
                with g.begin_closed_shape():
                    g.vertex(-10, -10)
                    g.vertex(10, -10)
                    g.vertex(10, 10)
                    g.vertex(-10, 10)
            with g.begin_closed_shape():
                g.vertex(-10, -10)
                g.vertex(10, -10)
                g.vertex(10, 10)
                g.vertex(-10, 10)

        py5.image(g, 0, 0)
        py5.image(g, 25, 25)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The ``push()`` function saves the current drawing style settings and transformations, while :doc:`py5graphics_pop` restores these settings. Note that these functions are always used together. They allow you to change the style and transformation settings and later return to what you had. When a new state is started with ``push()``, it builds on the current style and transform information.

``push()`` stores information related to the current transformation state and style settings controlled by the following functions: :doc:`py5graphics_rotate`, :doc:`py5graphics_translate`, :doc:`py5graphics_scale`, :doc:`py5graphics_fill`, :doc:`py5graphics_stroke`, :doc:`py5graphics_tint`, :doc:`py5graphics_stroke_weight`, :doc:`py5graphics_stroke_cap`, :doc:`py5graphics_stroke_join`, :doc:`py5graphics_image_mode`, :doc:`py5graphics_rect_mode`, :doc:`py5graphics_ellipse_mode`, :doc:`py5graphics_color_mode`, :doc:`py5graphics_text_align`, :doc:`py5graphics_text_font`, :doc:`py5graphics_text_mode`, :doc:`py5graphics_text_size`, and :doc:`py5graphics_text_leading`.

The ``push()`` and :doc:`py5graphics_pop` functions can be used in place of :doc:`py5graphics_push_matrix`, :doc:`py5graphics_pop_matrix`, :doc:`py5graphics_push_style`, and :doc:`py5graphics_pop_style`. The difference is that ``push()`` and :doc:`py5graphics_pop` control both the transformations (rotate, scale, translate) and the drawing styles at the same time.

This method can be used as a context manager to ensure that :doc:`py5graphics_pop` always gets called, as shown in the example.

This method is the same as :doc:`sketch_push` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_push`.

Underlying Processing method: PGraphics.push

Signatures
----------

.. code:: python

    push() -> None

Updated on September 01, 2022 14:08:27pm UTC

