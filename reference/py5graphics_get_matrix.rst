Py5Graphics.get_matrix()
========================

Get the current matrix as a numpy array.

Description
-----------

Get the current matrix as a numpy array. Use the ``target`` parameter to put the matrix data in a properly sized and typed numpy array.

This method is the same as :doc:`sketch_get_matrix` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_get_matrix`.

Underlying Java method: PGraphics.getMatrix

Syntax
------

.. code:: python

    get_matrix() -> NDArray[(Any, Any), Float]
    get_matrix(target: NDArray[(2, 3), Float], /) -> NDArray[(2, 3), Float]
    get_matrix(target: NDArray[(4, 4), Float], /) -> NDArray[(4, 4), Float]

Parameters
----------

* **target**: `NDArray[(2, 3), Float]` - transformation matrix data
* **target**: `NDArray[(4, 4), Float]` - transformation matrix data


Updated on September 11, 2021 16:51:34pm UTC

