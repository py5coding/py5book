Py5Graphics.curve()
===================

Draws a curved line on the ``Py5Graphics`` object.

Description
-----------

Draws a curved line on the ``Py5Graphics`` object. The first and second parameters specify the beginning control point and the last two parameters specify the ending control point. The middle parameters specify the start and stop of the curve. Longer curves can be created by putting a series of ``curve()`` functions together or using :doc:`py5graphics_curve_vertex`. An additional function called :doc:`py5graphics_curve_tightness` provides control for the visual quality of the curve. The ``curve()`` function is an implementation of Catmull-Rom splines. Using the 3D version requires rendering with ``P3D``.

This method is the same as :doc:`sketch_curve` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_curve`.

Underlying Processing method: PGraphics.curve

Signatures
----------

.. code:: python

    curve(
        x1: float,  # coordinates for the beginning control point
        y1: float,  # coordinates for the beginning control point
        x2: float,  # coordinates for the first point
        y2: float,  # coordinates for the first point
        x3: float,  # coordinates for the second point
        y3: float,  # coordinates for the second point
        x4: float,  # coordinates for the ending control point
        y4: float,  # coordinates for the ending control point
        /,
    ) -> None

    curve(
        x1: float,  # coordinates for the beginning control point
        y1: float,  # coordinates for the beginning control point
        z1: float,  # coordinates for the beginning control point
        x2: float,  # coordinates for the first point
        y2: float,  # coordinates for the first point
        z2: float,  # coordinates for the first point
        x3: float,  # coordinates for the second point
        y3: float,  # coordinates for the second point
        z3: float,  # coordinates for the second point
        x4: float,  # coordinates for the ending control point
        y4: float,  # coordinates for the ending control point
        z4: float,  # coordinates for the ending control point
        /,
    ) -> None

Updated on September 01, 2022 14:08:27pm UTC

