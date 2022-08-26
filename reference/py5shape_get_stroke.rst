Py5Shape.get_stroke()
=====================

Gets the stroke color used for lines and points in a ``Py5Shape`` object.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_stroke_0.png
    :alt: example picture for get_stroke()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.stroke_weight(4)
        py5.stroke(200, 50, 50)
        s = py5.create_shape(py5.RECT, 20, 20, 60, 60)
        py5.shape(s)

        stroke = s.get_stroke(0)
        py5.println(py5.red(stroke), py5.green(stroke), py5.blue(stroke)) # 200, 50, 50

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Gets the stroke color used for lines and points in a ``Py5Shape`` object. This method can get the stroke assigned to each vertex, but most likely the value will be the same for all vertices.

This method can only be used for a complete ``Py5Shape`` object, and never within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Processing method: PShape.getStroke

Signatures
------

.. code:: python

    get_stroke(
        index: int,  # vertex index
        /,
    ) -> int
Updated on August 25, 2022 20:01:47pm UTC

