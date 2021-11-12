Py5Graphics.pixel_density
=========================

Get the pixel density of the Py5Graphics drawing surface.

Description
-----------

Get the pixel density of the Py5Graphics drawing surface. By default this is 1 but it can be changed by calling :doc:`sketch_pixel_density` in ``settings()``.

When the pixel density has been set to more than 1, it changes all of the pixel operations including the way :doc:`py5graphics_get`, :doc:`py5graphics_blend`, :doc:`py5graphics_copy`, :doc:`py5graphics_update_pixels`, and :doc:`py5graphics_update_np_pixels` all work. See the reference for :doc:`py5graphics_pixel_width` and :doc:`py5graphics_pixel_height` for more information.

Underlying Processing field: PGraphics.pixelDensity


Updated on November 12, 2021 11:30:58am UTC

