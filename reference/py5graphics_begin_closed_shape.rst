Py5Graphics.begin_closed_shape()
================================

This method is used to start a custom closed shape.

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

This method is used to start a custom closed shape. This method should only be used as a context manager, as shown in the example. When used as a context manager, this will ensure that :doc:`py5graphics_end_shape` always gets called, just like when using :doc:`py5graphics_begin_shape` as a context manager. The difference is that when exiting, the parameter ``CLOSE`` will be passed to :doc:`py5graphics_end_shape`, connecting the last vertex to the first. This will close the shape. If this method were to be used not as a context manager, it won't be able to close the shape by making the call to :doc:`py5graphics_end_shape`.

This method is the same as :doc:`sketch_begin_closed_shape` but linked to a ``Py5Graphics`` object.

Underlying Java method: PGraphics.beginShape

Syntax
------

.. code:: python

    begin_closed_shape() -> None
    begin_closed_shape(kind: int, /) -> None

Parameters
----------

* **kind**: `int` - Either POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS, or QUAD_STRIP


Updated on September 23, 2021 10:56:03am UTC

