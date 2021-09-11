Py5Graphics.pixel_width
=======================

Width of the Py5Graphics drawing surface in pixels.

Description
-----------

Width of the Py5Graphics drawing surface in pixels. When ``pixel_density(2)`` was used in ``settings()`` to make use of a high resolution display (called a Retina display on OSX or high-dpi on Windows and Linux), the width and height of the Py5Graphics drawing surface does not change, but the number of pixels is doubled. As a result, all operations that use pixels (like :doc:`py5graphics_load_pixels`, :doc:`py5graphics_get`, etc.) happen in this doubled space. As a convenience, the variables ``pixel_width`` and :doc:`py5graphics_pixel_height` hold the actual width and height of the drawing surface in pixels. This is useful for any Py5Graphics objects that use the :doc:`py5graphics_pixels` or :doc:`py5graphics_np_pixels` arrays, for instance, because the number of elements in each array will be ``pixel_width*pixel_height``, not ``width*height``.

This field is the same as :doc:`sketch_pixel_width` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_pixel_width`.

Underlying Java field: PGraphics.pixelWidth


Updated on September 11, 2021 16:51:34pm UTC

