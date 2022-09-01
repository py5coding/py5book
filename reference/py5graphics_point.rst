Py5Graphics.point()
===================

Draws a point, a coordinate in space at the dimension of one pixel.

Description
-----------

Draws a point, a coordinate in space at the dimension of one pixel. The first parameter is the horizontal value for the point, the second value is the vertical value for the point, and the optional third value is the depth value. Drawing this shape in 3D with the ``z`` parameter requires the ``P3D`` renderer.

Use :doc:`py5graphics_stroke` to set the color of a ``point()``.

Point appears round with the default ``stroke_cap(ROUND)`` and square with ``stroke_cap(PROJECT)``. Points are invisible with ``stroke_cap(SQUARE)`` (no cap).

Using ``point()`` with ``strokeWeight(1)`` or smaller may draw nothing to the Py5Graphics drawing surface, depending on the graphics settings of the computer. Workarounds include setting the pixel using the :doc:`py5graphics_pixels` or :doc:`py5graphics_np_pixels` arrays or drawing the point using either :doc:`py5graphics_circle` or :doc:`py5graphics_square`.

This method is the same as :doc:`sketch_point` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_point`.

Underlying Processing method: PGraphics.point

Signatures
----------

.. code:: python

    point(
        x: float,  # x-coordinate of the point
        y: float,  # y-coordinate of the point
        /,
    ) -> None

    point(
        x: float,  # x-coordinate of the point
        y: float,  # y-coordinate of the point
        z: float,  # z-coordinate of the point
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

