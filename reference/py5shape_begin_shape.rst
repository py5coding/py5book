Py5Shape.begin_shape()
======================

This method is used to start a custom shape created with the :doc:`sketch_create_shape` function.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        global s  # the Py5Shape object
        s = py5.create_shape()
        s.begin_shape()
        s.fill("#F00")
        s.no_stroke()
        s.vertex(0, 0)
        s.vertex(0, 50)
        s.vertex(50, 0)
        s.end_shape()


    def draw():
        py5.shape(s, 25, 25)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        global s  # the Py5Shape object
        s = py5.create_shape()
        with s.begin_shape():
            s.fill("#F00")
            s.no_stroke()
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

This method is used to start a custom shape created with the :doc:`sketch_create_shape` function. It's always and only used with :doc:`sketch_create_shape`.

Drawing commands to a custom shape must always conclude with a call to the :doc:`py5shape_end_shape` method. This method can be used as a context manager to ensure that :doc:`py5shape_end_shape` always gets called, as shown in the second example. Use :doc:`py5shape_begin_closed_shape` to create a context manager that will pass the ``CLOSE`` parameter to :doc:`sketch_end_shape`, closing the shape.

Underlying Processing method: `PShape.beginShape <https://processing.org/reference/PShape_beginShape_.html>`_

Signatures
----------

.. code:: python

    begin_shape() -> None

    begin_shape(
        kind: int,  # Either POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS, or QUAD_STRIP
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

