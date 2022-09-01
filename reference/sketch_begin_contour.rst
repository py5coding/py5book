begin_contour()
===============

Use the ``begin_contour()`` and :doc:`sketch_end_contour` methods to create negative shapes within shapes such as the center of the letter 'O'.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_contour_0.png
    :alt: example picture for begin_contour()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.translate(50, 50)
        py5.stroke(255, 0, 0)
        py5.begin_shape()
        # exterior part of shape, clockwise winding
        py5.vertex(-40, -40)
        py5.vertex(40, -40)
        py5.vertex(40, 40)
        py5.vertex(-40, 40)
        py5.begin_contour()
        # interior part of shape, counter-clockwise winding
        py5.vertex(-20, -20)
        py5.vertex(-20, 20)
        py5.vertex(20, 20)
        py5.vertex(20, -20)
        py5.end_contour()
        py5.end_shape(py5.CLOSE)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_begin_contour_1.png
    :alt: example picture for begin_contour()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.translate(50, 50)
        py5.stroke(255, 0, 0)
        with py5.begin_closed_shape():
            # exterior part of shape, clockwise winding
            py5.vertex(-40, -40)
            py5.vertex(40, -40)
            py5.vertex(40, 40)
            py5.vertex(-40, 40)
            with py5.begin_contour():
                # interior part of shape, counter-clockwise winding
                py5.vertex(-20, -20)
                py5.vertex(-20, 20)
                py5.vertex(20, 20)
                py5.vertex(20, -20)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Use the ``begin_contour()`` and :doc:`sketch_end_contour` methods to create negative shapes within shapes such as the center of the letter 'O'. The ``begin_contour()`` method begins recording vertices for the shape and :doc:`sketch_end_contour` stops recording. The vertices that define a negative shape must "wind" in the opposite direction from the exterior shape. First draw vertices for the exterior shape in clockwise order, then for internal shapes, draw vertices counterclockwise.

These methods can only be used within a :doc:`sketch_begin_shape` & :doc:`sketch_end_shape` pair and transformations such as :doc:`sketch_translate`, :doc:`sketch_rotate`, and :doc:`sketch_scale` do not work within a ``begin_contour()`` & :doc:`sketch_end_contour` pair. It is also not possible to use other shapes, such as :doc:`sketch_ellipse` or :doc:`sketch_rect` within.

This method can be used as a context manager to ensure that :doc:`sketch_end_contour` always gets called, as shown in the second example.

Underlying Processing method: `beginContour <https://processing.org/reference/beginContour_.html>`_

Signatures
----------

.. code:: python

    begin_contour() -> None

Updated on September 01, 2022 14:08:27pm UTC

