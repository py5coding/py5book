# Py5Graphics.set_np_pixels()

Set the entire contents of [](py5graphics_np_pixels) to the contents of another properly sized and typed numpy array.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for set_np_pixels()](/images/reference/Py5Graphics_set_np_pixels_0.png)

</div><div class="example-cell-code">

```python
import numpy as np

def setup():
    py5.background(255, 0, 0)
    array = np.full((50, 50, 1), 240, dtype=np.uint8)
    g = py5.create_graphics(50, 50)
    with g.begin_draw():
        g.set_np_pixels(array, bands='L')
    py5.image(g, 20, 20)
```

</div></div>

</div>

## Description

Set the entire contents of [](py5graphics_np_pixels) to the contents of another properly sized and typed numpy array. The size of `array`'s first and second dimensions must match the height and width of the Py5Graphics drawing surface, respectively. The array's `dtype` must be `np.uint8`. This must be used after [](py5graphics_begin_draw) but can be used after [](py5graphics_end_draw).

The `bands` parameter is used to interpret the `array`'s color channel dimension (the array's third dimension). It can be one of `'L'` (single-channel grayscale), `'ARGB'`, `'RGB'`, or `'RGBA'`. If there is no alpha channel, `array` is assumed to have no transparency. Unlike the main drawing window, a Py5Graphics drawing surface's pixels can be transparent so using the alpha channel will work properly. If the `bands` parameter is `'L'`, `array`'s third dimension is optional.

This method makes its own calls to [](py5graphics_load_np_pixels) and [](py5graphics_update_np_pixels) so there is no need to call either explicitly.

This method exists because setting the array contents with the code `g.np_pixels = array` will cause an error, while the correct syntax, `g.np_pixels[:] = array`, might also be unintuitive for beginners.

This method is the same as [](sketch_set_np_pixels) but linked to a `Py5Graphics` object.

## Signatures

```python
set_np_pixels(
    array: npt.NDArray[np.uint8],  # properly sized numpy array to be copied to np_pixels[]
    bands: str = "ARGB",  # color channels in the array's third dimension
) -> None
```

Updated on August 07, 2023 14:29:21pm UTC
