# Py5Graphics.load_np_pixels()

Loads the pixel data of the current Py5Graphics drawing surface into the [](py5graphics_np_pixels) array.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for load_np_pixels()](/images/reference/Py5Graphics_load_np_pixels_0.png)

</div><div class="example-cell-code">

```python
def setup():
    g = py5.create_graphics(80, 80)
    g.begin_draw()
    g.background(255)
    g.rect(10, 10, 60, 60)
    g.load_np_pixels()
    g.np_pixels[:, 40:, 1:] = [255, 0, 0]
    g.update_np_pixels()
    g.end_draw()
    py5.image(g, 10, 10)
```

</div></div>

</div>

## Description

Loads the pixel data of the current Py5Graphics drawing surface into the [](py5graphics_np_pixels) array. This method must always be called before reading from or writing to [](py5graphics_np_pixels). It should only be used between calls to [](py5graphics_begin_draw) and [](py5graphics_end_draw). Subsequent changes to the Py5Graphics drawing surface will not be reflected in [](py5graphics_np_pixels) until `load_np_pixels()` is called again.

The `load_np_pixels()` method is similar to [](py5graphics_load_pixels) in that `load_np_pixels()` must be called before reading from or writing to [](py5graphics_np_pixels) just as [](py5graphics_load_pixels) must be called before reading from or writing to [](py5graphics_pixels).

Note that `load_np_pixels()` will as a side effect call [](py5graphics_load_pixels), so if your code needs to read [](py5graphics_np_pixels) and [](py5graphics_pixels) simultaneously, there is no need for a separate call to [](py5graphics_load_pixels). However, be aware that modifying both [](py5graphics_np_pixels) and [](py5graphics_pixels) simultaneously will likely result in the updates to [](py5graphics_pixels) being discarded.

This method is the same as [](sketch_load_np_pixels) but linked to a `Py5Graphics` object.

## Signatures

```python
load_np_pixels() -> None
```

Updated on March 06, 2023 02:49:26am UTC
