# Py5Image.set_pixels()

Changes the color of any pixel or writes an image directly into the Py5Image object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for set_pixels()](/images/reference/Py5Image_set_pixels_0.png)

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

</div>

## Description

Changes the color of any pixel or writes an image directly into the Py5Image object.

The `x` and `y` parameters specify the pixel to change and the color parameter specifies the color value. The color parameter `c` is affected by the current color mode (the default is RGB values from 0 to 255). When setting an image, the `x` and `y` parameters define the coordinates for the upper-left corner of the image, regardless of the current [](sketch_image_mode).

Setting the color of a single pixel with `set_pixels(x, y)` is easy, but not as fast as putting the data directly into [](py5image_pixels). The equivalent statement to `set_pixels(x, y, 0)` using [](py5image_pixels) is `pixels[y*py5.width+x] = 0`. See the reference for [](py5image_pixels) for more information.

Underlying Processing method: [PImage.set](https://processing.org/reference/PImage_set_.html)

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
    img: Py5Image,  # image to copy into the Py5Image object
    /,
) -> None
```

Updated on April 15, 2023 22:56:12pm UTC
