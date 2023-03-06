# Py5Image.load_pixels()

Loads the pixel data for the image into its [](py5image_pixels) array.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for load_pixels()](/images/reference/Py5Image_load_pixels_0.png)

</div><div class="example-cell-code">

```python
def setup():
    global my_image
    global half_image
    half_image = py5.width * py5.height//2
    my_image = py5.load_image("apples.jpg")
    my_image.load_pixels()
    for i in range(0, half_image):
        my_image.pixels[i+half_image] = my_image.pixels[i]

    my_image.update_pixels()


def draw():
    py5.image(my_image, 0, 0)
```

</div></div>

</div>

## Description

Loads the pixel data for the image into its [](py5image_pixels) array. This function must always be called before reading from or writing to [](py5image_pixels).

Underlying Processing method: [PImage.loadPixels](https://processing.org/reference/PImage_loadPixels_.html)

## Signatures

```python
load_pixels() -> None
```

Updated on March 06, 2023 02:49:26am UTC
