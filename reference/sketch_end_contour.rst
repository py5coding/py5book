end_contour()
=============

Use the :doc:`sketch_begin_contour` and ``end_contour()`` methods to create negative shapes within shapes such as the center of the letter 'O'.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_end_contour_0.png
    :alt: example picture for end_contour()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.translate(50, 50)
        py5.stroke(255, 0, 0)
        py5.begin_shape()
        # exterior part of shape, clockwise winding
        py5.vertex(-40, -40)
        py5.vertex(40, -40)
        py5.vertex(40, 40)
        py5.vertex(-40, 40)
        # interior part of shape, counter-clockwise winding
        py5.begin_contour()
        py5.vertex(-20, -20)
        py5.vertex(-20, 20)
        py5.vertex(20, 20)
        py5.vertex(20, -20)
        py5.end_contour()
        py5.end_shape(py5.CLOSE)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Use the :doc:`sketch_begin_contour` and ``end_contour()`` methods to create negative shapes within shapes such as the center of the letter 'O'. The :doc:`sketch_begin_contour` method begins recording vertices for the shape and ``end_contour()`` stops recording. The vertices that define a negative shape must "wind" in the opposite direction from the exterior shape. First draw vertices for the exterior shape in clockwise order, then for internal shapes, draw vertices counterclockwise.

These methods can only be used within a :doc:`sketch_begin_shape` & :doc:`sketch_end_shape` pair and transformations such as :doc:`sketch_translate`, :doc:`sketch_rotate`, and :doc:`sketch_scale` do not work within a :doc:`sketch_begin_contour` & ``end_contour()`` pair. It is also not possible to use other shapes, such as :doc:`sketch_ellipse` or :doc:`sketch_rect` within.

Underlying Processing method: `endContour <https://processing.org/reference/endContour_.html>`_

Signatures
----------

.. code:: python

    end_contour() -> None

Updated on September 01, 2022 16:36:02pm UTC

