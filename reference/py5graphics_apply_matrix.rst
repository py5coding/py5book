Py5Graphics.apply_matrix()
==========================

Multiplies the current matrix by the one specified through the parameters.

Description
-----------

Multiplies the current matrix by the one specified through the parameters. This is very slow because it will try to calculate the inverse of the transform, so avoid it whenever possible. The equivalent function in OpenGL is ``gl_mult_matrix()``.

This method is the same as :doc:`sketch_apply_matrix` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_apply_matrix`.

Underlying Processing method: PGraphics.applyMatrix

Signatures
------

.. code:: python

    apply_matrix(
        n00: float,  # numeric value in row 0 and column 0 of the matrix
        n01: float,  # numeric value in row 0 and column 1 of the matrix
        n02: float,  # numeric value in row 0 and column 2 of the matrix
        n03: float,  # numeric value in row 0 and column 3 of the matrix
        n10: float,  # numeric value in row 1 and column 0 of the matrix
        n11: float,  # numeric value in row 1 and column 1 of the matrix
        n12: float,  # numeric value in row 1 and column 2 of the matrix
        n13: float,  # numeric value in row 1 and column 3 of the matrix
        n20: float,  # numeric value in row 2 and column 0 of the matrix
        n21: float,  # numeric value in row 2 and column 1 of the matrix
        n22: float,  # numeric value in row 2 and column 2 of the matrix
        n23: float,  # numeric value in row 2 and column 3 of the matrix
        n30: float,  # numeric value in row 3 and column 0 of the matrix
        n31: float,  # numeric value in row 3 and column 1 of the matrix
        n32: float,  # numeric value in row 3 and column 2 of the matrix
        n33: float,  # numeric value in row 3 and column 3 of the matrix
        /,
    ) -> None

    apply_matrix(
        n00: float,  # numeric value in row 0 and column 0 of the matrix
        n01: float,  # numeric value in row 0 and column 1 of the matrix
        n02: float,  # numeric value in row 0 and column 2 of the matrix
        n10: float,  # numeric value in row 1 and column 0 of the matrix
        n11: float,  # numeric value in row 1 and column 1 of the matrix
        n12: float,  # numeric value in row 1 and column 2 of the matrix
        /,
    ) -> None

    apply_matrix(
        source: npt.NDArray[np.floating],  # transformation matrix with a shape of 2x3 for 2D transforms or 4x4 for 3D transforms
        /,
    ) -> None
Updated on August 26, 2022 19:48:56pm UTC

