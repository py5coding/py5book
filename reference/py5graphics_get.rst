Py5Graphics.get()
=================

Reads the color of any pixel or grabs a section of an ``Py5Graphics`` object canvas.

Description
-----------

Reads the color of any pixel or grabs a section of an ``Py5Graphics`` object canvas. If no parameters are specified, the entire canvas is returned. Use the ``x`` and ``y`` parameters to get the value of one pixel. Get a section of the Py5Graphics drawing surface by specifying additional ``w`` and ``h`` parameters. When getting an image, the ``x`` and ``y`` parameters define the coordinates for the upper-left corner of the returned image, regardless of the current :doc:`py5graphics_image_mode`.

If the pixel requested is outside of the ``Py5Graphics`` object canvas, black is returned. The numbers returned are scaled according to the current color ranges, but only ``RGB`` values are returned by this function. For example, even though you may have drawn a shape with ``color_mode(HSB)``, the numbers returned will be in ``RGB`` format.

If a width and a height are specified, ``get(x, y, w, h)`` returns a Py5Image corresponding to the part of the original Py5Image where the top left pixel is at the ``(x, y)`` position with a width of ``w`` a height of ``h``.

Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast as grabbing the data directly from :doc:`py5graphics_pixels` or :doc:`py5graphics_np_pixels`. The equivalent statement to ``get(x, y)`` using :doc:`py5graphics_pixels` is ``pixels[y*width+x]``. Using :doc:`py5graphics_np_pixels` it is ``np_pixels[y, x]``. See the reference for :doc:`py5graphics_pixels` and :doc:`py5graphics_np_pixels` for more information.

This method is the same as :doc:`sketch_get` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_get`.

Underlying Processing method: PGraphics.get

Signatures
----------

.. code:: python

    get() -> Py5Image

    get(
        x: int,  # x-coordinate of the pixel
        y: int,  # y-coordinate of the pixel
        /,
    ) -> int

    get(
        x: int,  # x-coordinate of the pixel
        y: int,  # y-coordinate of the pixel
        w: int,  # width of pixel rectangle to get
        h: int,  # height of pixel rectangle to get
        /,
    ) -> Py5Image

Updated on September 01, 2022 14:08:27pm UTC

