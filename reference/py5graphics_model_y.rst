Py5Graphics.model_y()
=====================

Returns the three-dimensional X, Y, Z position in model space.

Description
-----------

Returns the three-dimensional X, Y, Z position in model space. This returns the Y value for a given coordinate based on the current set of transformations (scale, rotate, translate, etc.) The Y value can be used to place an object in space relative to the location of the original point once the transformations are no longer in use. 

To see an example for how this can be used, see :doc:`sketch_model_y`. In that example, the :doc:`sketch_model_x`, ``model_y()``, and :doc:`sketch_model_z` methods (which are analogous to the :doc:`py5graphics_model_x`, ``model_y()``, and :doc:`py5graphics_model_z` methods) record the location of a box in space after being placed using a series of translate and rotate commands. After :doc:`sketch_pop_matrix` is called, those transformations no longer apply, but the (x, y, z) coordinate returned by the model functions is used to place another box in the same location.

This method is the same as :doc:`sketch_model_y` but linked to a ``Py5Graphics`` object.

Underlying Processing method: PGraphics.modelY

Syntax
------

.. code:: python

    model_y(x: float, y: float, z: float, /) -> float

Parameters
----------

* **x**: `float` - 3D x-coordinate to be mapped
* **y**: `float` - 3D y-coordinate to be mapped
* **z**: `float` - 3D z-coordinate to be mapped


Updated on November 12, 2021 11:30:58am UTC

