# set_np_pixels()

Set the entire contents of [](sketch_np_pixels) to the contents of another properly sized and typed numpy array.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for set_np_pixels()](/images/reference/Sketch_set_np_pixels_0.png)

</div><div class="example-cell-code">

```python
import numpy as np

def setup():
    array = np.zeros((py5.height, py5.width, 3), dtype=np.uint8)
    array[:60, :, 0] = 200
    array[:, :40, 1] = 100
    array[20:, :, 2] = 250
    py5.set_np_pixels(array, bands='RGB')
```

</div></div>

</div>

## Description

Set the entire contents of [](sketch_np_pixels) to the contents of another properly sized and typed numpy array. The size of `array`'s first and second dimensions must match the height and width of the Sketch window, respectively. The array's `dtype` must be `np.uint8`.

The `bands` parameter is used to interpret the `array`'s color channel dimension (the array's third dimension). It can be one of `'L'` (single-channel grayscale), `'ARGB'`, `'RGB'`, or `'RGBA'`. If there is no alpha channel, `array` is assumed to have no transparency, but recall that the display window's pixels can never be transparent so any transparency in `array` will have no effect. If the `bands` parameter is `'L'`, `array`'s third dimension is optional.

This method makes its own calls to [](sketch_load_np_pixels) and [](sketch_update_np_pixels) so there is no need to call either explicitly.

This method exists because setting the array contents with the code `py5.np_pixels = array` will cause an error, while the correct syntax, `py5.np_pixels[:] = array`, might also be unintuitive for beginners.

## Signatures

```python
set_np_pixels(
    array: npt.NDArray[np.uint8],  # properly sized numpy array to be copied to np_pixels[]
    bands: str = "ARGB",  # color channels in the array's third dimension
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
