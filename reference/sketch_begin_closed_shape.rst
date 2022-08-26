begin_closed_shape()
====================

This method is used to start a custom closed shape.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_closed_shape_0.png
    :alt: example picture for begin_closed_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.translate(50, 50)
        with py5.begin_closed_shape():
            py5.vertex(-40, -40)
            py5.vertex(40, -40)
            py5.vertex(40, 40)
            py5.vertex(-40, 40)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_closed_shape_1.png
    :alt: example picture for begin_closed_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.translate(25, 50)
        py5.stroke_weight(4)
        py5.stroke("#F00")
        with py5.begin_closed_shape():
            py5.vertex(-20, -40)
            py5.vertex(20, -40)
            py5.vertex(20, 40)
            py5.vertex(-20, 40)

        py5.translate(50, 0)
        py5.stroke("#00F")
        with py5.begin_shape():
            py5.vertex(-20, -40)
            py5.vertex(20, -40)
            py5.vertex(20, 40)
            py5.vertex(-20, 40)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

This method is used to start a custom closed shape. This method should only be used as a context manager, as shown in the examples. When used as a context manager, this will ensure that :doc:`sketch_end_shape` always gets called, just like when using :doc:`sketch_begin_shape` as a context manager. The difference is that when exiting, the parameter ``CLOSE`` will be passed to :doc:`sketch_end_shape`, connecting the last vertex to the first. This will close the shape. If this method were to be used not as a context manager, it won't be able to close the shape by making the call to :doc:`sketch_end_shape`.

Underlying Processing method: `beginShape <https://processing.org/reference/beginShape_.html>`_

Signatures
------

.. code:: python

    begin_closed_shape() -> None

    begin_closed_shape(
        kind: int,  # Either POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS, or QUAD_STRIP
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

