Py5Graphics.bezier_point()
==========================

Evaluates the Bezier at point t for points a, b, c, d.

Description
-----------

Evaluates the Bezier at point t for points a, b, c, d. The parameter t varies between 0 and 1, a and d are points on the curve, and b and c are the control points. This can be done once with the x coordinates and a second time with the y coordinates to get the location of a bezier curve at t.

This method is the same as :doc:`sketch_bezier_point` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_bezier_point`.

Underlying Processing method: PGraphics.bezierPoint

Syntax
------

.. code:: python

    bezier_point(a: float, b: float, c: float, d: float, t: float, /) -> float

Parameters
----------

* **a**: `float` - coordinate of first point on the curve
* **b**: `float` - coordinate of first control point
* **c**: `float` - coordinate of second control point
* **d**: `float` - coordinate of second point on the curve
* **t**: `float` - value between 0 and 1


Updated on November 12, 2021 11:30:58am UTC

