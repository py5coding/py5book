# Py5Image.copy()

Copies a region of pixels from one image into another.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for copy()](/images/reference/Py5Image_copy_0.png)

</div><div class="example-cell-code">

```python
def setup():
    global apples
    apples = py5.load_image("apples.jpg")
    x = py5.width//2
    apples.copy(x, 0, x, py5.height, 0, 0, x, py5.height)


def draw():
    py5.image(apples, 0, 0)
```

</div></div>

</div>

## Description

Copies a region of pixels from one image into another. If the source and destination regions aren't the same size, it will automatically resize source pixels to fit the specified target region. No alpha information is used in the process, however if the source image has an alpha channel set, it will be copied as well.

This function ignores [](sketch_image_mode).

If you want to create a new image with the contents of a rectangular region of a `Py5Image` object, check out the [`.get_pixels(x, y, w, h)`](py5image_get_pixels) method, where x, y, w, h, are the position and dimensions of the area to be copied. It will return a `Py5Image object`.

Underlying Processing method: [PImage.copy](https://processing.org/reference/PImage_copy_.html)

## Signatures

```python
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
```

Updated on March 06, 2023 02:49:26am UTC
