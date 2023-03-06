# Py5Image.load_np_pixels()

Loads the pixel data of the image into the [](py5image_np_pixels) array.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for load_np_pixels()](/images/reference/Py5Image_load_np_pixels_0.png)

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

Loads the pixel data of the image into the [](py5image_np_pixels) array. This method must always be called before reading from or writing to [](py5image_np_pixels). Subsequent changes to the image will not be reflected in [](py5image_np_pixels) until `py5image_load_np_pixels()` is called again.

The `load_np_pixels()` method is similar to [](py5image_load_pixels) in that `load_np_pixels()` must be called before reading from or writing to [](py5image_np_pixels) just as [](py5image_load_pixels) must be called before reading from or writing to [](py5image_pixels).

Note that `load_np_pixels()` will as a side effect call [](py5image_load_pixels), so if your code needs to read [](py5image_np_pixels) and [](py5image_pixels) simultaneously, there is no need for a separate call to [](py5image_load_pixels). However, be aware that modifying both [](py5image_np_pixels) and [](py5image_pixels) simultaneously will likely result in the updates to [](py5image_pixels) being discarded.

## Signatures

```python
load_np_pixels() -> None
```

Updated on March 06, 2023 02:49:26am UTC
