Py5Graphics.begin_contour()
===========================

Use the ``begin_contour()`` and :doc:`py5graphics_end_contour` methods to create negative shapes within shapes such as the center of the letter 'O'.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(200, 200, py5.P2D)

        g = py5.create_graphics(100, 100, py5.P2D)
        with g.begin_draw():
            with g.begin_closed_shape():
                g.vertex(20, 20)
                g.vertex(80, 20)
                g.vertex(80, 80)
                g.vertex(20, 80)
                with g.begin_contour():
                    g.vertex(40, 40)
                    g.vertex(40, 60)
                    g.vertex(60, 60)
                    g.vertex(60, 40)

        py5.image(g, 50, 50)
        py5.image(g, 80, 80)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Use the ``begin_contour()`` and :doc:`py5graphics_end_contour` methods to create negative shapes within shapes such as the center of the letter 'O'. The ``begin_contour()`` method begins recording vertices for the shape and :doc:`py5graphics_end_contour` stops recording. The vertices that define a negative shape must "wind" in the opposite direction from the exterior shape. First draw vertices for the exterior shape in clockwise order, then for internal shapes, draw vertices counterclockwise.

These methods can only be used within a :doc:`py5graphics_begin_shape` & :doc:`py5graphics_end_shape` pair and transformations such as :doc:`py5graphics_translate`, :doc:`py5graphics_rotate`, and :doc:`py5graphics_scale` do not work within a ``begin_contour()`` & :doc:`py5graphics_end_contour` pair. It is also not possible to use other shapes, such as :doc:`py5graphics_ellipse` or :doc:`py5graphics_rect` within.

This method can be used as a context manager to ensure that :doc:`py5graphics_end_contour` always gets called, as shown in the example.

This method is the same as :doc:`sketch_begin_contour` but linked to a ``Py5Graphics`` object.

Underlying Java method: PGraphics.beginContour

Syntax
------

.. code:: python

    begin_contour() -> None

Updated on September 23, 2021 10:56:03am UTC

