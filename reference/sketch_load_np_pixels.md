# load_np_pixels()

Loads the pixel data of the current display window into the [](sketch_np_pixels) array.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for load_np_pixels()](/images/reference/Sketch_load_np_pixels_0.png)

</div><div class="example-cell-code">

```python
def setup():
    my_image = py5.load_image("apples.jpg")
    py5.image(my_image, 0, 0)
    
    py5.load_np_pixels()
    py5.np_pixels[50:100, :, :] = py5.np_pixels[:50, :, :]
    py5.update_np_pixels()
```

</div></div>

</div>

## Description

Loads the pixel data of the current display window into the [](sketch_np_pixels) array. This method must always be called before reading from or writing to [](sketch_np_pixels). Subsequent changes to the display window will not be reflected in [](sketch_np_pixels) until `load_np_pixels()` is called again.

The `load_np_pixels()` method is similar to [](sketch_load_pixels) in that `load_np_pixels()` must be called before reading from or writing to [](sketch_np_pixels) just as [](sketch_load_pixels) must be called before reading from or writing to [](sketch_pixels).

Note that `load_np_pixels()` will as a side effect call [](sketch_load_pixels), so if your code needs to read [](sketch_np_pixels) and [](sketch_pixels) simultaneously, there is no need for a separate call to [](sketch_load_pixels). However, be aware that modifying both [](sketch_np_pixels) and [](sketch_pixels) simultaneously will likely result in the updates to [](sketch_pixels) being discarded.

## Signatures

```python
load_np_pixels() -> None
```

Updated on March 06, 2023 02:49:26am UTC
