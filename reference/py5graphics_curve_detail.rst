Py5Graphics.curve_detail()
==========================

Sets the resolution at which curves display.

Description
-----------

Sets the resolution at which curves display. The default value is 20. This function is only useful when using the ``P3D`` renderer as the default ``P2D`` renderer does not use this information.

This method is the same as :doc:`sketch_curve_detail` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_curve_detail`.

Underlying Processing method: PGraphics.curveDetail

Syntax
------

.. code:: python

    curve_detail(detail: int, /) -> None

Parameters
----------

* **detail**: `int` - resolution of the curves


Updated on November 12, 2021 11:30:58am UTC

