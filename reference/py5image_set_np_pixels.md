# Py5Image.set_np_pixels()

Set the entire contents of [](py5image_np_pixels) to the contents of another properly sized and typed numpy array.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import numpy as np

def make_array(value):
    return np.full((50, 50, 1), value, dtype=np.uint8)

def setup():
    global img
    py5.image_mode(py5.CENTER)
    img = py5.create_image(50, 50, py5.RGB)

def draw():
    py5.background(128)
    array = make_array(py5.frame_count % 256)
    img.set_np_pixels(array, bands='L')
    py5.image(img, py5.mouse_x, py5.mouse_y)
```

</div></div>

</div>

## Description

Set the entire contents of [](py5image_np_pixels) to the contents of another properly sized and typed numpy array. The size of `array`'s first and second dimensions must match the height and width of the image, respectively. The array's `dtype` must be `np.uint8`.

The `bands` parameter is used to interpret the `array`'s color channel dimension (the array's third dimension). It can be one of `'L'` (single-channel grayscale), `'ARGB'`, `'RGB'`, or `'RGBA'`. If there is no alpha channel, `array` is assumed to have no transparency. If the `bands` parameter is `'L'`, `array`'s third dimension is optional.

This method makes its own calls to [](py5image_load_np_pixels) and [](py5image_update_np_pixels) so there is no need to call either explicitly.

This method exists because setting the array contents with the code `img.np_pixels = array` will cause an error, while the correct syntax, `img.np_pixels[:] = array`, might also be unintuitive for beginners.

Note that the [](sketch_convert_image) method can also be used to convert a numpy array into a new Py5Image object.

## Signatures

```python
set_np_pixels(
    array: npt.NDArray[np.uint8],  # properly sized numpy array to be copied to np_pixels[]
    bands: str = "ARGB",  # color channels in the array's third dimension
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
