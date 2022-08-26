Py5Graphics.curve_vertex()
==========================

Specifies vertex coordinates for curves.

Description
-----------

Specifies vertex coordinates for curves. This method may only be used between :doc:`py5graphics_begin_shape` and :doc:`py5graphics_end_shape` and only when there is no ``MODE`` parameter specified to :doc:`py5graphics_begin_shape`. The first and last points in a series of ``curve_vertex()`` lines will be used to guide the beginning and end of the curve. A minimum of four points is required to draw a tiny curve between the second and third points. Adding a fifth point with ``curve_vertex()`` will draw the curve between the second, third, and fourth points. The ``curve_vertex()`` method is an implementation of Catmull-Rom splines. Using the 3D version requires rendering with ``P3D``.

This method is the same as :doc:`sketch_curve_vertex` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_curve_vertex`.

Underlying Processing method: PGraphics.curveVertex

Signatures
------

.. code:: python

    curve_vertex(
        x: float,  # the x-coordinate of the vertex
        y: float,  # the y-coordinate of the vertex
        /,
    ) -> None

    curve_vertex(
        x: float,  # the x-coordinate of the vertex
        y: float,  # the y-coordinate of the vertex
        z: float,  # the z-coordinate of the vertex
        /,
    ) -> None
Updated on August 25, 2022 19:59:03pm UTC

