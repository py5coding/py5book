# save_frame()

Save the current frame as an image.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def draw():
    for _ in range(10):
        py5.rect(py5.random_int(py5.width), py5.random_int(py5.height), 10, 10)
    py5.save_frame('/tmp/random_squares_####.jpg')
```

</div></div>

</div>

## Description

Save the current frame as an image. This method uses the Python library Pillow to write the image, so it can save images in any format that that library supports.

Use the `drop_alpha` parameter to drop the alpha channel from the image. This defaults to `True`. Some image formats such as JPG do not support alpha channels, and Pillow will throw an error if you try to save an image with the alpha channel in that format.

The `use_thread` parameter will save the image in a separate Python thread. This improves performance by returning before the image has actually been written to the file.

This method is the same as [](sketch_save) except it will replace a sequence of `#` symbols in the `filename` parameter with the frame number. This is useful when saving an image sequence for a running animation. The first frame number will be 1.

## Signatures

```python
save_frame(
    filename: Union[str, Path, BytesIO],  # output filename
    *,
    format: str = None,  # image format, if not determined from filename extension
    drop_alpha: bool = True,  # remove the alpha channel when saving the image
    use_thread: bool = False,  # write file in separate thread
    **params
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
