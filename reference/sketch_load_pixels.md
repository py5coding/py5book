# load_pixels()

Loads the pixel data of the current display window into the [](sketch_pixels) array.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for load_pixels()](/images/reference/Sketch_load_pixels_0.png)

</div><div class="example-cell-code">

```python
def setup():
    half_image = py5.width*py5.height//2
    my_image = py5.load_image("apples.jpg")
    py5.image(my_image, 0, 0)
    
    py5.load_pixels()
    for i in range(0, half_image):
        py5.pixels[i+half_image] = py5.pixels[i]
    
    py5.update_pixels()
```

</div></div>

</div>

## Description

Loads the pixel data of the current display window into the [](sketch_pixels) array. This function must always be called before reading from or writing to [](sketch_pixels). Subsequent changes to the display window will not be reflected in [](sketch_pixels) until `load_pixels()` is called again.

Underlying Processing method: [loadPixels](https://processing.org/reference/loadPixels_.html)

## Signatures

```python
load_pixels() -> None
```

Updated on March 06, 2023 02:49:26am UTC
