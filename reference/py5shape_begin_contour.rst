Py5Shape.begin_contour()
========================

Use the ``begin_contour()`` and :doc:`py5shape_end_contour` methods to create negative shapes within a ``Py5Shape`` object such as the center of the letter 'O'.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_begin_contour_0.png
    :alt: example picture for begin_contour()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)
        s = py5.create_shape()
        s.begin_shape()
        # exterior part of shape, clockwise winding
        s.vertex(20, 20)
        s.vertex(80, 20)
        s.vertex(80, 80)
        s.vertex(20, 80)
        # interior part of shape, counter-clockwise winding
        s.begin_contour()
        s.vertex(40, 40)
        s.vertex(40, 60)
        s.vertex(60, 60)
        s.vertex(60, 40)
        s.end_contour()
        s.end_shape(py5.CLOSE)
        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_begin_contour_1.png
    :alt: example picture for begin_contour()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)
        s = py5.create_shape()
        with s.begin_closed_shape():
            # exterior part of shape, clockwise winding
            s.vertex(20, 20)
            s.vertex(80, 20)
            s.vertex(80, 80)
            s.vertex(20, 80)
            # interior part of shape, counter-clockwise winding
            with s.begin_contour():
                s.vertex(40, 40)
                s.vertex(40, 60)
                s.vertex(60, 60)
                s.vertex(60, 40)

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Use the ``begin_contour()`` and :doc:`py5shape_end_contour` methods to create negative shapes within a ``Py5Shape`` object such as the center of the letter 'O'. The ``begin_contour()`` method begins recording vertices for the shape and :doc:`py5shape_end_contour` stops recording. The vertices that define a negative shape must "wind" in the opposite direction from the exterior shape. First draw vertices for the exterior shape in clockwise order, then for internal shapes, draw vertices counterclockwise.

These methods can only be used within a :doc:`py5shape_begin_shape` & :doc:`py5shape_end_shape` pair and transformations such as :doc:`py5shape_translate`, :doc:`py5shape_rotate`, and :doc:`py5shape_scale` do not work within a ``begin_contour()`` & :doc:`py5shape_end_contour` pair. It is also not possible to use other shapes, such as :doc:`sketch_ellipse` or :doc:`sketch_rect` within.

This method can be used as a context manager to ensure that :doc:`py5shape_end_contour` always gets called, as shown in the second example.

Underlying Processing method: `PShape.beginContour <https://processing.org/reference/PShape_beginContour_.html>`_

Signatures
------

.. code:: python

    begin_contour() -> None
Updated on August 25, 2022 20:01:47pm UTC

