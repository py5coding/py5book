Py5Shape.no_stroke()
====================

Disables the ``Py5Shape`` object's stroke (outline).

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_no_stroke_0.png
    :alt: example picture for no_stroke()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        s = py5.create_shape()
        s.begin_shape()
        s.no_stroke()
        s.vertex(20, 80)
        s.vertex(50, 20)
        s.vertex(80, 80)
        s.end_shape(py5.CLOSE)

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Disables the ``Py5Shape`` object's stroke (outline). If both ``no_stroke()`` and :doc:`py5shape_no_fill` are called, nothing will be drawn to the screen.

This method can only be used within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Processing method: PShape.noStroke

Signatures
------

.. code:: python

    no_stroke() -> None
Updated on August 25, 2022 20:01:47pm UTC

