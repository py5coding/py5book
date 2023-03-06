# Py5Image.pixels[]

The pixels[] array contains the values for all the pixels in the image.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for pixels[]](/images/reference/Py5Image_pixels_0.png)

</div><div class="example-cell-code">

```python
def setup():
    global tower
    tower = py5.load_image("tower.jpg")
    dimension = tower.width * tower.height
    tower.load_pixels()
    for i in range(0, dimension, 2):
        tower.pixels[i] = "#000"

    tower.update_pixels()


def draw():
    py5.image(tower, 0, 0)
```

</div></div>

</div>

## Description

The pixels[] array contains the values for all the pixels in the image. These values are of the color datatype. This array is the size of the image, meaning if the image is 100 x 100 pixels, there will be 10,000 values and if the window is 200 x 300 pixels, there will be 60,000 values. 

Before accessing this array, the data must loaded with the [](py5image_load_pixels) method. Failure to do so may result in a Java `NullPointerException`. After the array data has been modified, the [](py5image_update_pixels) method must be run to update the content of the display window.

Underlying Processing field: [PImage.pixels](https://processing.org/reference/PImage_pixels.html)

Updated on March 06, 2023 02:49:26am UTC
