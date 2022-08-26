Py5Graphics.set_matrix()
========================

Set the current matrix to the one specified through the parameter ``source``.

Description
-----------

Set the current matrix to the one specified through the parameter ``source``. Inside the Processing code it will call :doc:`py5graphics_reset_matrix` followed by :doc:`py5graphics_apply_matrix`. This will be very slow because :doc:`py5graphics_apply_matrix` will try to calculate the inverse of the transform, so avoid it whenever possible.

This method is the same as :doc:`sketch_set_matrix` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_set_matrix`.

Underlying Processing method: PGraphics.setMatrix

Signatures
------

.. code:: python

    set_matrix(
        source: npt.NDArray[np.floating],  # transformation matrix with a shape of 2x3 for 2D transforms or 4x4 for 3D transforms
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

