# Py5Image.update_np_pixels()

Updates the image with the data in the [](py5image_np_pixels) array.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for update_np_pixels()](/images/reference/Py5Image_update_np_pixels_0.png)

</div><div class="example-cell-code">

```python
def setup():
    my_image = py5.load_image("apples.jpg")
    my_image.load_np_pixels()
    my_image.np_pixels[:50, :, :] = my_image.np_pixels[50:100, :, :]
    my_image.update_np_pixels()
    py5.image(my_image, 0, 0)
```

</div></div>

</div>

## Description

Updates the image with the data in the [](py5image_np_pixels) array. Use in conjunction with [](py5image_load_np_pixels). If you're only reading pixels from the array, there's no need to call `update_np_pixels()` — updating is only necessary to apply changes.

The `update_np_pixels()` method is similar to [](py5image_update_pixels) in that `update_np_pixels()` must be called after modifying [](py5image_np_pixels) just as [](py5image_update_pixels) must be called after modifying [](py5image_pixels).

## Signatures

```python
update_np_pixels() -> None
```

Updated on March 06, 2023 02:49:26am UTC
