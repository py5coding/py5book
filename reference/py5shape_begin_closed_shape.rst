Py5Shape.begin_closed_shape()
=============================

This method is used to start a custom closed shape created with the :doc:`sketch_create_shape` function.

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
        global s  # the Py5Shape object
        s = py5.create_shape()
        with s.begin_closed_shape():
            s.stroke_weight(5)
            s.no_fill()
            s.vertex(0, 0)
            s.vertex(0, 50)
            s.vertex(50, 0)


    def draw():
        py5.shape(s, 25, 25)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

This method is used to start a custom closed shape created with the :doc:`sketch_create_shape` function. It's always and only used with :doc:`sketch_create_shape`.

This method should only be used as a context manager, as shown in the example. When used as a context manager, this will ensure that :doc:`py5shape_end_shape` always gets called, just like when using :doc:`py5shape_begin_shape` as a context manager. The difference is that when exiting, the parameter ``CLOSE`` will be passed to :doc:`py5shape_end_shape`, connecting the last vertex to the first. This will close the shape. If this method were to be used not as a context manager, it won't be able to close the shape by making the call to :doc:`py5shape_end_shape`.

Underlying Processing method: `PShape.beginShape <https://processing.org/reference/PShape_beginShape_.html>`_

Signatures
------

.. code:: python

    begin_closed_shape() -> None

    begin_closed_shape(
        kind: int,  # Either POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS, or QUAD_STRIP
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

