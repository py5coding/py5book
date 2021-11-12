Py5Graphics.bezier()
====================

Draws a Bezier curve on the ``Py5Graphics`` object.

Description
-----------

Draws a Bezier curve on the ``Py5Graphics`` object. These curves are defined by a series of anchor and control points. The first two parameters specify the first anchor point and the last two parameters specify the other anchor point. The middle parameters specify the control points which define the shape of the curve. Bezier curves were developed by French engineer Pierre Bezier. Using the 3D version requires rendering with ``P3D``.

This method is the same as :doc:`sketch_bezier` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_bezier`.

Underlying Processing method: PGraphics.bezier

Syntax
------

.. code:: python

    bezier(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
    bezier(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

Parameters
----------

* **x1**: `float` - coordinates for the first anchor point
* **x2**: `float` - coordinates for the first control point
* **x3**: `float` - coordinates for the second control point
* **x4**: `float` - coordinates for the second anchor point
* **y1**: `float` - coordinates for the first anchor point
* **y2**: `float` - coordinates for the first control point
* **y3**: `float` - coordinates for the second control point
* **y4**: `float` - coordinates for the second anchor point
* **z1**: `float` - coordinates for the first anchor point
* **z2**: `float` - coordinates for the first control point
* **z3**: `float` - coordinates for the second control point
* **z4**: `float` - coordinates for the second anchor point


Updated on November 12, 2021 11:30:58am UTC

