Py5Shape.end_shape()
====================

This method is used to complete a custom shape created with the :doc:`sketch_create_shape` function.

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

This method is used to complete a custom shape created with the :doc:`sketch_create_shape` function. It's always and only used with :doc:`sketch_create_shape`.

Underlying Processing method: `PShape.endShape <https://processing.org/reference/PShape_endShape_.html>`_

Syntax
------

.. code:: python

    end_shape() -> None
    end_shape(mode: int, /) -> None

Parameters
----------

* **mode**: `int` - Either OPEN or CLOSE


Updated on November 12, 2021 11:30:58am UTC

