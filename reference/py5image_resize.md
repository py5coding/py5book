# Py5Image.resize()

Resize the Py5Image object to a new height and width.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for resize()](/images/reference/Py5Image_resize_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.rect(10, 10, 80, 80)
    py5.fill(255, 0, 0)
    py5.rect(15, 15, 10, 60)
    img = py5.get_pixels()
    for x in [80, 60, 40]:
        img_copy = img.copy()
        img_copy.resize(x, 0, py5.BICUBIC)
        py5.image(img_copy, 100 - x, 100 - x)
```

</div></div>

</div>

## Description

Resize the Py5Image object to a new height and width. This will modify the Py5Image object in place, meaning that rather than returning a resized copy, it will modify your existing Py5Image object. If this isn't what you want, pair this method with [](py5image_copy), as shown in the example.

To make the image scale proportionally, use 0 as the value for either the `w` or `h` parameter.

The default resize interpolation mode is `BILINEAR`. Alternatively you can interpolate using the `NEAREST_NEIGHBOR` method, which is faster but yields the lowest quality results. You can also use `BICUBIC` interpolation, which is the most computationally intensive but looks the best, particularly for up-scaling operations.

Underlying Processing method: [PImage.resize](https://processing.org/reference/PImage_resize_.html)

## Signatures

```python
resize(
    w: int,  # width to size image to
    h: int,  # height to size image to
    /,
) -> None

resize(
    w: int,  # width to size image to
    h: int,  # height to size image to
    interpolation_mode: int,  # interpolation method for resize operation
    /,
) -> None
```

Updated on August 23, 2025 20:21:04pm UTC
