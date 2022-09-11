Py5Graphics.quadratic_vertex()
==============================

Specifies vertex coordinates for quadratic Bezier curves.

Description
-----------

Specifies vertex coordinates for quadratic Bezier curves. Each call to ``quadratic_vertex()`` defines the position of one control point and one anchor point of a Bezier curve, adding a new segment to a line or shape. The first time ``quadratic_vertex()`` is used within a :doc:`py5graphics_begin_shape` call, it must be prefaced with a call to :doc:`py5graphics_vertex` to set the first anchor point. This method must be used between :doc:`py5graphics_begin_shape` and :doc:`py5graphics_end_shape` and only when there is no ``MODE`` parameter specified to :doc:`py5graphics_begin_shape`. Using the 3D version requires rendering with ``P3D``.

This method is the same as :doc:`sketch_quadratic_vertex` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_quadratic_vertex`.

Underlying Processing method: PGraphics.quadraticVertex

Signatures
----------

.. code:: python

    quadratic_vertex(
        cx: float,  # the x-coordinate of the control point
        cy: float,  # the y-coordinate of the control point
        cz: float,  # the z-coordinate of the control point
        x3: float,  # the x-coordinate of the anchor point
        y3: float,  # the y-coordinate of the anchor point
        z3: float,  # the z-coordinate of the anchor point
        /,
    ) -> None

    quadratic_vertex(
        cx: float,  # the x-coordinate of the control point
        cy: float,  # the y-coordinate of the control point
        x3: float,  # the x-coordinate of the anchor point
        y3: float,  # the y-coordinate of the anchor point
        /,
    ) -> None

Updated on September 01, 2022 14:08:27pm UTC

