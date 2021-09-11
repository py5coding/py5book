Py5Graphics.begin_contour()
===========================

Use the ``begin_contour()`` and :doc:`py5graphics_end_contour` methods to create negative shapes within shapes such as the center of the letter 'O'.

Description
-----------

Use the ``begin_contour()`` and :doc:`py5graphics_end_contour` methods to create negative shapes within shapes such as the center of the letter 'O'. The ``begin_contour()`` method begins recording vertices for the shape and :doc:`py5graphics_end_contour` stops recording. The vertices that define a negative shape must "wind" in the opposite direction from the exterior shape. First draw vertices for the exterior shape in clockwise order, then for internal shapes, draw vertices counterclockwise.

These methods can only be used within a :doc:`py5graphics_begin_shape` & :doc:`py5graphics_end_shape` pair and transformations such as :doc:`py5graphics_translate`, :doc:`py5graphics_rotate`, and :doc:`py5graphics_scale` do not work within a ``begin_contour()`` & :doc:`py5graphics_end_contour` pair. It is also not possible to use other shapes, such as :doc:`py5graphics_ellipse` or :doc:`py5graphics_rect` within.

This method is the same as :doc:`sketch_begin_contour` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_begin_contour`.

Underlying Java method: PGraphics.beginContour

Syntax
------

.. code:: python

    begin_contour() -> None

Updated on September 11, 2021 16:51:34pm UTC

