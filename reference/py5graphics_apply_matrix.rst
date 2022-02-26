Py5Graphics.apply_matrix()
==========================

Multiplies the current matrix by the one specified through the parameters.

Description
-----------

Multiplies the current matrix by the one specified through the parameters. This is very slow because it will try to calculate the inverse of the transform, so avoid it whenever possible. The equivalent function in OpenGL is ``gl_mult_matrix()``.

This method is the same as :doc:`sketch_apply_matrix` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_apply_matrix`.

Underlying Processing method: PGraphics.applyMatrix

Syntax
------

.. code:: python

    apply_matrix(n00: float, n01: float, n02: float, n03: float, n10: float, n11: float, n12: float, n13: float, n20: float, n21: float, n22: float, n23: float, n30: float, n31: float, n32: float, n33: float, /) -> None
    apply_matrix(n00: float, n01: float, n02: float, n10: float, n11: float, n12: float, /) -> None
    apply_matrix(source: npt.NDArray[np.floating], /) -> None

Parameters
----------

* **n00**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n01**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n02**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n03**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n10**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n11**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n12**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n13**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n20**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n21**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n22**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n23**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n30**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n31**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n32**: `float` - numbers which define the 4x4 matrix to be multiplied
* **n33**: `float` - numbers which define the 4x4 matrix to be multiplied
* **source**: `npt.NDArray[np.floating]` - transformation matrix with a shape of 2x3 for 2D transforms or 4x4 for 3D transforms


Updated on February 26, 2022 13:22:44pm UTC

