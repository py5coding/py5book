Py5Shape.curve_detail()
=======================

Sets the resolution at which a ``Py5Shape`` object's curves display.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_curve_detail_0.png
    :alt: example picture for curve_detail()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.size(100, 100, py5.P2D)
        py5.shape(draw_curves(30, 2, "#FF0000"))
        py5.shape(draw_curves(70, 20, "#0000FF"))


    def draw_curves(y, detail, color):
        s = py5.create_shape()
        s.begin_shape()
        s.no_fill()
        s.stroke(color)
        s.curve_detail(detail)
        s.curve_vertex(0, y)
        s.curve_vertex(10, y-10)
        s.curve_vertex(20, y)
        s.curve_vertex(50, y+20)
        s.curve_vertex(80, y)
        s.curve_vertex(90, y+10)
        s.curve_vertex(100, y)
        s.end_shape()
        return s

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the resolution at which a ``Py5Shape`` object's curves display. The default value is 20.

Drawing 2D curves requires using the ``P2D`` renderer and drawing 3D curves requires using the ``P3D`` renderer. When drawing directly with ``Py5Shape`` objects, curves do not work at all using the default renderer.

This method can only be used within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

Underlying Processing method: PShape.curveDetail

Signatures
----------

.. code:: python

    curve_detail(
        detail: int,  # resolution of the curves
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

