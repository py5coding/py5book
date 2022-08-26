Py5Graphics.begin_closed_shape()
================================

This method is used to start a custom closed shape.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Graphics_begin_closed_shape_0.png
    :alt: example picture for begin_closed_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)

        g = py5.create_graphics(60, 60, py5.P2D)
        with g.begin_draw():
            with g.begin_closed_shape():
                g.vertex(10, 10)
                g.vertex(50, 10)
                g.vertex(50, 50)
                g.vertex(10, 50)
                with g.begin_contour():
                    g.vertex(20, 20)
                    g.vertex(20, 40)
                    g.vertex(40, 40)
                    g.vertex(40, 20)

        py5.image(g, 0, 0)
        py5.image(g, 25, 25)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

This method is used to start a custom closed shape. This method should only be used as a context manager, as shown in the example. When used as a context manager, this will ensure that :doc:`py5graphics_end_shape` always gets called, just like when using :doc:`py5graphics_begin_shape` as a context manager. The difference is that when exiting, the parameter ``CLOSE`` will be passed to :doc:`py5graphics_end_shape`, connecting the last vertex to the first. This will close the shape. If this method were to be used not as a context manager, it won't be able to close the shape by making the call to :doc:`py5graphics_end_shape`.

This method is the same as :doc:`sketch_begin_closed_shape` but linked to a ``Py5Graphics`` object.

Underlying Processing method: PGraphics.beginShape

Signatures
------

.. code:: python

    begin_closed_shape() -> None

    begin_closed_shape(
        kind: int,  # Either POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS, or QUAD_STRIP
        /,
    ) -> None
Updated on August 25, 2022 19:59:03pm UTC

