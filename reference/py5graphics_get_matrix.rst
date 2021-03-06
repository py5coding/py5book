Py5Graphics.get_matrix()
========================

Get the current matrix as a numpy array.

Description
-----------

Get the current matrix as a numpy array. Use the ``target`` parameter to put the matrix data in a properly sized and typed numpy array.

This method is the same as :doc:`sketch_get_matrix` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_get_matrix`.

Underlying Processing method: PGraphics.getMatrix

Syntax
------

.. code:: python

    get_matrix() -> npt.NDArray[np.floating]
    get_matrix(target: npt.NDArray[np.floating], /) -> npt.NDArray[np.floating]

Parameters
----------

* **target**: `npt.NDArray[np.floating]` - transformation matrix with a shape of 2x3 for 2D transforms or 4x4 for 3D transforms


Updated on February 26, 2022 13:22:44pm UTC

