Py5Graphics.line()
==================

Draws a line (a direct path between two points) to the Py5Graphics drawing surface.

Description
-----------

Draws a line (a direct path between two points) to the Py5Graphics drawing surface. The version of ``line()`` with four parameters draws the line in 2D.  To color a line, use the :doc:`py5graphics_stroke` function. A line cannot be filled, therefore the :doc:`py5graphics_fill` function will not affect the color of a line. 2D lines are drawn with a width of one pixel by default, but this can be changed with the :doc:`py5graphics_stroke_weight` function. The version with six parameters allows the line to be placed anywhere within XYZ space. Drawing this shape in 3D with the ``z`` parameter requires the ``P3D`` renderer.

This method is the same as :doc:`sketch_line` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_line`.

Underlying Processing method: PGraphics.line

Signatures
----------

.. code:: python

    line(
        x1: float,  # x-coordinate of the first point
        y1: float,  # y-coordinate of the first point
        x2: float,  # x-coordinate of the second point
        y2: float,  # y-coordinate of the second point
        /,
    ) -> None

    line(
        x1: float,  # x-coordinate of the first point
        y1: float,  # y-coordinate of the first point
        z1: float,  # z-coordinate of the first point
        x2: float,  # x-coordinate of the second point
        y2: float,  # y-coordinate of the second point
        z2: float,  # z-coordinate of the second point
        /,
    ) -> None

Updated on September 01, 2022 14:08:27pm UTC

