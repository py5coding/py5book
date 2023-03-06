# Py5Image.width

The width of the image in units of pixels.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for width](/images/reference/Py5Image_width_0.png)

</div><div class="example-cell-code">

```python
def setup():
    tiles = py5.load_image("tiles.jpg")
    py5.image(tiles, 20, 10)
    py5.rect(55, 10, tiles.width, tiles.height)
```

</div></div>

</div>

## Description

The width of the image in units of pixels.

Underlying Processing field: [PImage.width](https://processing.org/reference/PImage_width.html)

Updated on March 06, 2023 02:49:26am UTC
