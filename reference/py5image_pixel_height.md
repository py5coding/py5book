# Py5Image.pixel_height

Height of the Py5Image object in pixels.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.pixel_density(2)
    img = py5.create_image(100, 100, py5.RGB)
    py5.println(img.pixel_density, img.pixel_width, img.pixel_height)  # prints 1, 100, 100
```

</div></div>

</div>

## Description

Height of the Py5Image object in pixels. This will be the same as [](py5image_height), even if the Sketch used [](sketch_pixel_density) to set the pixel density to a value greater than 1.

Underlying Processing field: PImage.pixelHeight

Updated on March 06, 2023 02:49:26am UTC
