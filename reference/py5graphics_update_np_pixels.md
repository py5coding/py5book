# Py5Graphics.update_np_pixels()

Updates the Py5Graphics drawing surface with the data in the [](py5graphics_np_pixels) array.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for update_np_pixels()](/images/reference/Py5Graphics_update_np_pixels_0.png)

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

Updates the Py5Graphics drawing surface with the data in the [](py5graphics_np_pixels) array. Use in conjunction with [](py5graphics_load_np_pixels). If you're only reading pixels from the array, there's no need to call `update_np_pixels()` — updating is only necessary to apply changes. Working with [](py5graphics_np_pixels) can only be done between calls to [](py5graphics_begin_draw) and [](py5graphics_end_draw).

The `update_np_pixels()` method is similar to [](py5graphics_update_pixels) in that `update_np_pixels()` must be called after modifying [](py5graphics_np_pixels) just as [](py5graphics_update_pixels) must be called after modifying [](py5graphics_pixels).

This method is the same as [](sketch_update_np_pixels) but linked to a `Py5Graphics` object.

## Signatures

```python
update_np_pixels() -> None
```

Updated on March 06, 2023 02:49:26am UTC
