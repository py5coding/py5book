# image()

The `image()` function draws an image to the display window.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for image()](/images/reference/Sketch_image_0.png)

</div><div class="example-cell-code">

```python
def setup():
    global img
    # images must be in the "data" directory to load correctly
    img = py5.load_image("laDefense.jpg")


def draw():
    py5.image(img, 0, 0)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for image()](/images/reference/Sketch_image_1.png)

</div><div class="example-cell-code">

```python
def setup():
    global img
    # images must be in the "data" directory to load correctly
    img = py5.load_image("laDefense.jpg")


def draw():
    py5.image(img, 0, 0)
    py5.image(img, 0, 0, py5.width//2, py5.height//2)
```

</div></div>

</div>

## Description

The `image()` function draws an image to the display window. Images must be in the Sketch's "data" directory to load correctly. Py5 currently works with GIF, JPEG, and PNG images. 

The `img` parameter specifies the image to display and by default the `a` and `b` parameters define the location of its upper-left corner. The image is displayed at its original size unless the `c` and `d` parameters specify a different size. The [](sketch_image_mode) function can be used to change the way these parameters draw the image.

Use the `u1`, `u2`, `v1`, and `v2` parameters to use only a subset of the image. These values are always specified in image space location, regardless of the current [](sketch_texture_mode) setting.

The color of an image may be modified with the [](sketch_tint) function. This function will maintain transparency for GIF and PNG images.

Underlying Processing method: [image](https://processing.org/reference/image_.html)

## Signatures

```python
image(
    img: Py5Image,  # the image to display
    a: float,  # x-coordinate of the image by default
    b: float,  # y-coordinate of the image by default
    /,
) -> None

image(
    img: Py5Image,  # the image to display
    a: float,  # x-coordinate of the image by default
    b: float,  # y-coordinate of the image by default
    c: float,  # width to display the image by default
    d: float,  # height to display the image by default
    /,
) -> None

image(
    img: Py5Image,  # the image to display
    a: float,  # x-coordinate of the image by default
    b: float,  # y-coordinate of the image by default
    c: float,  # width to display the image by default
    d: float,  # height to display the image by default
    u1: int,  # x-coordinate of the upper left corner of image subset
    v1: int,  # y-coordinate of the upper left corner of image subset
    u2: int,  # x-coordinate of the lower right corner of image subset
    v2: int,  # y-coordinate of the lower right corner of image subset
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
