# Py5Graphics.set_pixels()

Changes the color of any pixel or writes an image directly into the Py5Graphics object.

## Description

Changes the color of any pixel or writes an image directly into the Py5Graphics object.

The `x` and `y` parameters specify the pixel to change and the color parameter specifies the color value. The color parameter `c` is affected by the current color mode (the default is RGB values from 0 to 255). When setting an image, the `x` and `y` parameters define the coordinates for the upper-left corner of the image, regardless of the current [](py5graphics_image_mode).

Setting the color of a single pixel with `set_pixels(x, y)` is easy, but not as fast as putting the data directly into [](py5graphics_pixels). The equivalent statement to `set_pixels(x, y, 0)` using [](py5graphics_pixels) is `pixels[y*py5.width+x] = 0`. See the reference for [](py5graphics_pixels) for more information.

This method is the same as [](sketch_set_pixels) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_set_pixels).

Underlying Processing method: PGraphics.set

## Signatures

```python
set_pixels(
    x: int,  # x-coordinate of the pixel
    y: int,  # y-coordinate of the pixel
    c: int,  # any color value
    /,
) -> None

set_pixels(
    x: int,  # x-coordinate of the pixel
    y: int,  # y-coordinate of the pixel
    img: Py5Image,  # image to copy into the Py5Graphics object
    /,
) -> None
```

Updated on April 15, 2023 22:56:12pm UTC
