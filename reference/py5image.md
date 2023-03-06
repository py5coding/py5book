# Py5Image

Datatype for storing images.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for Py5Image](/images/reference/Py5Image_0.png)

</div><div class="example-cell-code">

```python
def setup():
    global photo
    photo = py5.load_image("laDefense.jpg")


def draw():
    py5.image(photo, 0, 0)
```

</div></div>

</div>

## Description

Datatype for storing images. Py5 can load `.gif`, `.jpg`, `.tga`, and `.png` images using the [](sketch_load_image) function. Py5 can also convert common Python image objects using the [](sketch_convert_image) function. Images may be displayed in 2D and 3D space. The `Py5Image` class contains fields for the [](py5image_width) and [](py5image_height) of the image, as well as arrays called [](py5image_pixels) and [](py5image_np_pixels) that contain the values for every pixel in the image. The methods described below allow easy access to the image's pixels and alpha channel and simplify the process of compositing.

Before using the [](py5image_pixels) array, be sure to use the [](py5image_load_pixels) method on the image to make sure that the pixel data is properly loaded. Similarly, be sure to use the [](py5image_load_np_pixels) method on the image before using the [](py5image_np_pixels) array.

To create a new image, use the [](sketch_create_image) function. Do not use the syntax `Py5Image()`.

Underlying Processing class: [PImage](https://processing.org/reference/PImage.html)

The following methods and fields are provided:

```{include} include_py5image.md
```

Updated on March 06, 2023 02:49:26am UTC
