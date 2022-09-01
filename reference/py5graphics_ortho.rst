Py5Graphics.ortho()
===================

Sets an orthographic projection and defines a parallel clipping volume.

Description
-----------

Sets an orthographic projection and defines a parallel clipping volume. All objects with the same dimension appear the same size, regardless of whether they are near or far from the camera. The parameters to this function specify the clipping volume where left and right are the minimum and maximum x values, top and bottom are the minimum and maximum y values, and near and far are the minimum and maximum z values. If no parameters are given, the default is used: ``ortho(-width/2, width/2, -height/2, height/2)``.

This method is the same as :doc:`sketch_ortho` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_ortho`.

Underlying Processing method: PGraphics.ortho

Signatures
----------

.. code:: python

    ortho() -> None

    ortho(
        left: float,  # left plane of the clipping volume
        right: float,  # right plane of the clipping volume
        bottom: float,  # bottom plane of the clipping volume
        top: float,  # top plane of the clipping volume
        /,
    ) -> None

    ortho(
        left: float,  # left plane of the clipping volume
        right: float,  # right plane of the clipping volume
        bottom: float,  # bottom plane of the clipping volume
        top: float,  # top plane of the clipping volume
        near: float,  # maximum distance from the origin to the viewer
        far: float,  # maximum distance from the origin away from the viewer
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

