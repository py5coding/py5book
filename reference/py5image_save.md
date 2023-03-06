# Py5Image.save()

Save the Py5Image object to an image file.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    for _ in range(10):
        py5.rect(py5.random_int(py5.width), py5.random_int(py5.height), 10, 10)
    img = py5.get(10, 10, 80, 80)
    img.save('/tmp/cropped_random_squares.jpg')
```

</div></div>

</div>

## Description

Save the Py5Image object to an image file. This method uses the Python library Pillow to write the image, so it can save images in any format that that library supports.

Use the `drop_alpha` parameter to drop the alpha channel from the image. This defaults to `True`. Some image formats such as JPG do not support alpha channels, and Pillow will throw an error if you try to save an image with the alpha channel in that format.

The `use_thread` parameter will save the image in a separate Python thread. This improves performance by returning before the image has actually been written to the file.

## Signatures

```python
save(
    filename: Union[str, Path, BytesIO],  # output filename
    *,
    format: str = None,  # image format, if not determined from filename extension
    drop_alpha: bool = True,  # remove the alpha channel when saving the image
    use_thread: bool = False,  # write file in separate thread
    **params
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
