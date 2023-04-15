# set_pixels()

Changes the color of any pixel or writes an image directly into the drawing surface.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for set_pixels()](/images/reference/Sketch_set_pixels_0.png)

</div><div class="example-cell-code">

```python
def setup():
    for i in range(100):
        for j in range(100):
            c = py5.color(2 * j, 2 * i, 0)
            py5.set_pixels(i, j, c)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for set_pixels()](/images/reference/Sketch_set_pixels_1.png)

</div><div class="example-cell-code">

```python
def setup():
    img = py5.load_image("laDefense.jpg")
    py5.set_pixels(0, 0, img)
```

</div></div>

</div>

## Description

Changes the color of any pixel or writes an image directly into the drawing surface.

The `x` and `y` parameters specify the pixel to change and the color parameter specifies the color value. The color parameter `c` is affected by the current color mode (the default is RGB values from 0 to 255). When setting an image, the `x` and `y` parameters define the coordinates for the upper-left corner of the image, regardless of the current [](sketch_image_mode).

Setting the color of a single pixel with `py5.set_pixels(x, y)` is easy, but not as fast as putting the data directly into [](sketch_pixels). The equivalent statement to `py5.set_pixels(x, y, 0)` using [](sketch_pixels) is `py5.pixels[y*py5.width+x] = 0`. See the reference for [](sketch_pixels) for more information.

Underlying Processing method: [set](https://processing.org/reference/set_.html)

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
    img: Py5Image,  # image to copy into the Sketch window
    /,
) -> None
```

Updated on April 15, 2023 22:56:12pm UTC
