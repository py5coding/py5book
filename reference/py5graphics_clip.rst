Py5Graphics.clip()
==================

Limits the rendering to the boundaries of a rectangle defined by the parameters.

Description
-----------

Limits the rendering to the boundaries of a rectangle defined by the parameters. The boundaries are drawn based on the state of the :doc:`py5graphics_image_mode` fuction, either ``CORNER``, ``CORNERS``, or ``CENTER``.

This method is the same as :doc:`sketch_clip` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_clip`.

Underlying Processing method: PGraphics.clip

Signatures
----------

.. code:: python

    clip(
        a: float,  # x-coordinate of the rectangle, by default
        b: float,  # y-coordinate of the rectangle, by default
        c: float,  # width of the rectangle, by default
        d: float,  # height of the rectangle, by default
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

