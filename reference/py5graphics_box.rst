Py5Graphics.box()
=================

A box is an extruded rectangle.

Description
-----------

A box is an extruded rectangle. A box with equal dimensions on all sides is a cube.

This method is the same as :doc:`sketch_box` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_box`.

Underlying Processing method: PGraphics.box

Syntax
------

.. code:: python

    box(size: float, /) -> None
    box(w: float, h: float, d: float, /) -> None

Parameters
----------

* **d**: `float` - dimension of the box in the z-dimension
* **h**: `float` - dimension of the box in the y-dimension
* **size**: `float` - dimension of the box in all dimensions (creates a cube)
* **w**: `float` - dimension of the box in the x-dimension


Updated on November 12, 2021 11:30:58am UTC

