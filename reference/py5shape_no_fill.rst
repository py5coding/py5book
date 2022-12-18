Py5Shape.no_fill()
==================

Disables the ``Py5Shape`` object's filling geometry.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_no_fill_0.png
    :alt: example picture for no_fill()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        s = py5.create_shape()
        s.begin_shape()
        s.no_fill()
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

Disables the ``Py5Shape`` object's filling geometry. If both :doc:`py5shape_no_stroke` and ``no_fill()`` are called, nothing will be drawn to the screen.

This method can only be used within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Processing method: PShape.noFill

Signatures
----------

.. code:: python

    no_fill() -> None

Updated on September 01, 2022 16:36:02pm UTC

