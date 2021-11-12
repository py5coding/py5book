Py5Graphics.bezier_vertex()
===========================

Specifies vertex coordinates for Bezier curves.

Description
-----------

Specifies vertex coordinates for Bezier curves. Each call to ``bezier_vertex()`` defines the position of two control points and one anchor point of a Bezier curve, adding a new segment to a line or shape. The first time ``bezier_vertex()`` is used within a :doc:`py5graphics_begin_shape` call, it must be prefaced with a call to :doc:`py5graphics_vertex` to set the first anchor point. This function must be used between :doc:`py5graphics_begin_shape` and :doc:`py5graphics_end_shape` and only when there is no ``MODE`` parameter specified to :doc:`py5graphics_begin_shape`. Using the 3D version requires rendering with ``P3D``.

This method is the same as :doc:`sketch_bezier_vertex` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_bezier_vertex`.

Underlying Processing method: PGraphics.bezierVertex

Syntax
------

.. code:: python

    bezier_vertex(x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
    bezier_vertex(x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

Parameters
----------

* **x2**: `float` - the x-coordinate of the 1st control point
* **x3**: `float` - the x-coordinate of the 2nd control point
* **x4**: `float` - the x-coordinate of the anchor point
* **y2**: `float` - the y-coordinate of the 1st control point
* **y3**: `float` - the y-coordinate of the 2nd control point
* **y4**: `float` - the y-coordinate of the anchor point
* **z2**: `float` - the z-coordinate of the 1st control point
* **z3**: `float` - the z-coordinate of the 2nd control point
* **z4**: `float` - the z-coordinate of the anchor point


Updated on November 12, 2021 11:30:58am UTC

