# update_np_pixels()

Updates the display window with the data in the [](sketch_np_pixels) array.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for update_np_pixels()](/images/reference/Sketch_update_np_pixels_0.png)

</div><div class="example-cell-code">

```python
def setup():
    img = py5.load_image("rockies.jpg")
    py5.image(img, 0, 0)
    py5.load_np_pixels()
    py5.np_pixels[50:100, :, :] = py5.np_pixels[:50, :, :]
    py5.update_np_pixels()
```

</div></div>

</div>

## Description

Updates the display window with the data in the [](sketch_np_pixels) array. Use in conjunction with [](sketch_load_np_pixels). If you're only reading pixels from the array, there's no need to call `update_np_pixels()` — updating is only necessary to apply changes.

The `update_np_pixels()` method is similar to [](sketch_update_pixels) in that `update_np_pixels()` must be called after modifying [](sketch_np_pixels) just as [](sketch_update_pixels) must be called after modifying [](sketch_pixels).

## Signatures

```python
update_np_pixels() -> None
```

Updated on March 06, 2023 02:49:26am UTC
