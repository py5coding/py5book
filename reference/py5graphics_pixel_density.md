# Py5Graphics.pixel_density

Get the pixel density of the Py5Graphics drawing surface.

## Description

Get the pixel density of the Py5Graphics drawing surface. By default this is 1 but it can be changed by calling [](sketch_pixel_density) in `settings()`.

When the pixel density has been set to more than 1, it changes all of the pixel operations including the way [](py5graphics_get_pixels), [](py5graphics_set_pixels), [](py5graphics_blend), [](py5graphics_copy), [](py5graphics_update_pixels), and [](py5graphics_update_np_pixels) all work. See the reference for [](py5graphics_pixel_width) and [](py5graphics_pixel_height) for more information.

Underlying Processing field: PGraphics.pixelDensity

Updated on April 16, 2023 17:26:49pm UTC
