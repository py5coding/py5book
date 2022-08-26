Py5Shape.stroke_weight()
========================

Sets the width of the stroke used for lines and points in a ``Py5Shape`` object.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_stroke_weight_0.png
    :alt: example picture for stroke_weight()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def make_line(weight):
        s = py5.create_shape()
        s.begin_shape()
        s.stroke_weight(weight)
        s.vertex(20, 0)
        s.vertex(80, 0)
        s.end_shape()
        return s


    def setup():
        py5.shape(make_line(1), 0, 20) # default
        py5.shape(make_line(4), 0, 40)
        py5.shape(make_line(10), 0, 70)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the width of the stroke used for lines and points in a ``Py5Shape`` object. All widths are set in units of pixels.

This method can only be used within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Processing method: PShape.strokeWeight

Signatures
------

.. code:: python

    stroke_weight(
        weight: float,  # the weight (in pixels) of the stroke
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

