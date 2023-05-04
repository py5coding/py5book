# Py5Image.get_pixels()

Reads the color of any pixel or grabs a section of an image.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_pixels()](/images/reference/Py5Image_get_pixels_0.png)

</div><div class="example-cell-code">

```python
def setup():
    mountains = py5.load_image("rockies.jpg")
    c = mountains.get_pixels(60, 90)
    for i in range(25, 75):
        for j in range(25, 75):
            mountains.set_pixels(i, j, c)
    py5.image(mountains, 0, 0)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for get_pixels()](/images/reference/Py5Image_get_pixels_1.png)

</div><div class="example-cell-code">

```python
def setup():
    mountains = py5.load_image("rockies.jpg")
    py5.background(mountains)
    new_mountains = mountains.get_pixels(50, 0, 50, 100)
    py5.image(new_mountains, 0, 0)
```

</div></div>

</div>

## Description

Reads the color of any pixel or grabs a section of an image. If no parameters are specified, the entire image is returned. Use the `x` and `y` parameters to get the value of one pixel. Get a section of the image by specifying additional `w` and `h` parameters. When getting an image, the `x` and `y` parameters define the coordinates for the upper-left corner of the returned image, regardless of the current [](sketch_image_mode).

If the pixel requested is outside of the image, black is returned. The numbers returned are scaled according to the current color ranges, but only `RGB` values are returned by this function. For example, even though you may have drawn a shape with `color_mode(HSB)`, the numbers returned will be in `RGB` format.

Getting the color of a single pixel with `get_pixels(x, y)` is easy, but not as fast as grabbing the data directly from [](py5image_pixels). The equivalent statement to `get_pixels(x, y)` using [](py5image_pixels) is `pixels[y*width+x]`. See the reference for [](py5image_pixels) for more information.

Underlying Processing method: [PImage.get](https://processing.org/reference/PImage_get_.html)

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
