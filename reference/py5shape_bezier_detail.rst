Py5Shape.bezier_detail()
========================

Sets a ``Py5Shape`` object's resolution at which Beziers display.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_bezier_detail_0.png
    :alt: example picture for bezier_detail()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)
        s1 = make_curve(5)
        s2 = make_curve(20)
        py5.shape(s1)
        py5.shape(s2, 40, 0)


    def make_curve(detail):
        s = py5.create_shape()
        s.begin_shape()
        s.no_fill()
        s.vertex(10, 20)
        s.bezier_detail(detail)
        s.bezier_vertex(60, 0, 60, 75, 10, 75)
        s.end_shape()
        return s

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets a ``Py5Shape`` object's resolution at which Beziers display. The default value is 20.

Drawing 2D bezier curves requires using the ``P2D`` renderer and drawing 3D bezier curves requires using the ``P3D`` renderer. When drawing directly with ``Py5Shape`` objects, bezier curves do not work at all using the default renderer.

This method can only be used within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Processing method: PShape.bezierDetail

Signatures
----------

.. code:: python

    bezier_detail(
        detail: int,  # resolution of the curves
        /,
    ) -> None

Updated on September 01, 2022 14:08:27pm UTC

