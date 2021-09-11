Py5Graphics.model_x()
=====================

Returns the three-dimensional X, Y, Z position in model space.

Description
-----------

Returns the three-dimensional X, Y, Z position in model space. This returns the X value for a given coordinate based on the current set of transformations (scale, rotate, translate, etc.) The X value can be used to place an object in space relative to the location of the original point once the transformations are no longer in use. 

To see an example for how this can be used, see :doc:`sketch_model_x`. In that example, the ``model_x()``, :doc:`sketch_model_y`, and :doc:`sketch_model_z` methods (which are analogous to the ``model_x()``, :doc:`py5graphics_model_y`, and :doc:`py5graphics_model_z` methods) record the location of a box in space after being placed using a series of translate and rotate commands. After :doc:`sketch_pop_matrix` is called, those transformations no longer apply, but the (x, y, z) coordinate returned by the model functions is used to place another box in the same location.

This method is the same as :doc:`sketch_model_x` but linked to a ``Py5Graphics`` object.

Underlying Java method: PGraphics.modelX

Syntax
------

.. code:: python

    model_x(x: float, y: float, z: float, /) -> float

Parameters
----------

* **x**: `float` - 3D x-coordinate to be mapped
* **y**: `float` - 3D y-coordinate to be mapped
* **z**: `float` - 3D z-coordinate to be mapped


Updated on September 11, 2021 16:51:34pm UTC

