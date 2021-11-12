Py5Graphics.curve_tangent()
===========================

Calculates the tangent of a point on a curve.

Description
-----------

Calculates the tangent of a point on a curve. There's a good definition of *tangent* on Wikipedia.

This method is the same as :doc:`sketch_curve_tangent` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_curve_tangent`.

Underlying Processing method: PGraphics.curveTangent

Syntax
------

.. code:: python

    curve_tangent(a: float, b: float, c: float, d: float, t: float, /) -> float

Parameters
----------

* **a**: `float` - coordinate of first point on the curve
* **b**: `float` - coordinate of first control point
* **c**: `float` - coordinate of second control point
* **d**: `float` - coordinate of second point on the curve
* **t**: `float` - value between 0 and 1


Updated on November 12, 2021 11:30:58am UTC

