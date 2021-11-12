Py5Graphics.bezier_detail()
===========================

Sets the resolution at which Beziers display.

Description
-----------

Sets the resolution at which Beziers display. The default value is 20. This function is only useful when using the ``P3D`` renderer; the default ``P2D`` renderer does not use this information.

This method is the same as :doc:`sketch_bezier_detail` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_bezier_detail`.

Underlying Processing method: PGraphics.bezierDetail

Syntax
------

.. code:: python

    bezier_detail(detail: int, /) -> None

Parameters
----------

* **detail**: `int` - resolution of the curves


Updated on November 12, 2021 11:30:58am UTC

