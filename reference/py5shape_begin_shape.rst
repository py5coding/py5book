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
    :number-lines:

    def setup():
        global s  # the Py5Shape object
        s = py5.create_shape()
        s.begin_shape()
        s.fill(0, 0, 255)
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

    </div>

Description
-----------

This method is used to start a custom shape created with the :doc:`sketch_create_shape` function. It's always and only used with :doc:`sketch_create_shape`.

Underlying Java method: `PShape.beginShape <https://processing.org/reference/PShape_beginShape_.html>`_

Syntax
------

.. code:: python

    begin_shape() -> None
    begin_shape(kind: int, /) -> None

Parameters
----------

* **kind**: `int` - Either POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS, or QUAD_STRIP


Updated on September 11, 2021 16:51:34pm UTC

