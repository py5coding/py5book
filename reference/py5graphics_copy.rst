Py5Graphics.copy()
==================

Copies a region of pixels from the ``Py5Graphics`` object to another area of the canvas and copies a region of pixels from an image used as the ``src_img`` parameter into the ``Py5Graphics`` object.

Description
-----------

Copies a region of pixels from the ``Py5Graphics`` object to another area of the canvas and copies a region of pixels from an image used as the ``src_img`` parameter into the ``Py5Graphics`` object. If the source and destination regions aren't the same size, it will automatically resize the source pixels to fit the specified target region. No alpha information is used in the process, however if the source image has an alpha channel set, it will be copied as well.

This function ignores :doc:`py5graphics_image_mode`.

This method is the same as :doc:`sketch_copy` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_copy`.

Underlying Processing method: PGraphics.copy

Signatures
----------

.. code:: python

    copy() -> Py5Image

    copy(
        src: Py5Image,  # a source image to copy pixels from
        sx: int,  # x-coordinate of the source's upper left corner
        sy: int,  # y-coordinate of the source's upper left corner
        sw: int,  # source image width
        sh: int,  # source image height
        dx: int,  # x-coordinate of the destination's upper left corner
        dy: int,  # y-coordinate of the destination's upper left corner
        dw: int,  # destination image width
        dh: int,  # destination image height
        /,
    ) -> None

    copy(
        sx: int,  # x-coordinate of the source's upper left corner
        sy: int,  # y-coordinate of the source's upper left corner
        sw: int,  # source image width
        sh: int,  # source image height
        dx: int,  # x-coordinate of the destination's upper left corner
        dy: int,  # y-coordinate of the destination's upper left corner
        dw: int,  # destination image width
        dh: int,  # destination image height
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

