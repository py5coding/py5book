Py5Graphics.screen_x()
======================

Takes a three-dimensional X, Y, Z position and returns the X value for where it will appear on a (two-dimensional) screen.

Description
-----------

Takes a three-dimensional X, Y, Z position and returns the X value for where it will appear on a (two-dimensional) screen.

This method is the same as :doc:`sketch_screen_x` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_screen_x`.

Underlying Processing method: PGraphics.screenX

Syntax
------

.. code:: python

    screen_x(x: float, y: float, /) -> float
    screen_x(x: float, y: float, z: float, /) -> float

Parameters
----------

* **x**: `float` - 3D x-coordinate to be mapped
* **y**: `float` - 3D y-coordinate to be mapped
* **z**: `float` - 3D z-coordinate to be mapped


Updated on November 12, 2021 11:30:58am UTC

