# Py5Graphics.get_pixels()

Reads the color of any pixel or grabs a section of an `Py5Graphics` object canvas.

## Description

Reads the color of any pixel or grabs a section of an `Py5Graphics` object canvas. If no parameters are specified, the entire canvas is returned. Use the `x` and `y` parameters to get the value of one pixel. Get a section of the Py5Graphics drawing surface by specifying additional `w` and `h` parameters. When getting an image, the `x` and `y` parameters define the coordinates for the upper-left corner of the returned image, regardless of the current [](py5graphics_image_mode).

If the pixel requested is outside of the `Py5Graphics` object canvas, black is returned. The numbers returned are scaled according to the current color ranges, but only `RGB` values are returned by this function. For example, even though you may have drawn a shape with `color_mode(HSB)`, the numbers returned will be in `RGB` format.

If a width and a height are specified, `get_pixels(x, y, w, h)` returns a Py5Image corresponding to the part of the original Py5Image where the top left pixel is at the `(x, y)` position with a width of `w` a height of `h`.

Getting the color of a single pixel with `get_pixels(x, y)` is easy, but not as fast as grabbing the data directly from [](py5graphics_pixels) or [](py5graphics_np_pixels). The equivalent statement to `get_pixels(x, y)` using [](py5graphics_pixels) is `pixels[y*width+x]`. Using [](py5graphics_np_pixels) it is `np_pixels[y, x]`. See the reference for [](py5graphics_pixels) and [](py5graphics_np_pixels) for more information.

This method is the same as [](sketch_get_pixels) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_get_pixels).

Underlying Processing method: PGraphics.get

## Signatures

```python
get_pixels() -> Py5Image

get_pixels(
    x: int,  # x-coordinate of the pixel
    y: int,  # y-coordinate of the pixel
    /,
) -> int

get_pixels(
    x: int,  # x-coordinate of the pixel
    y: int,  # y-coordinate of the pixel
    w: int,  # width of pixel rectangle to get
    h: int,  # height of pixel rectangle to get
    /,
) -> Py5Image
```

Updated on April 15, 2023 22:56:12pm UTC
