# to_pil()

Get the Sketch drawing surface as a PIL Image object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for to_pil()](/images/reference/Sketch_to_pil_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.stroke_weight(5)
    for x in range(0, 100, 10):
        py5.line(x, 0, x, 100)
    img = py5.to_pil()
    img = img.rotate(45)
    py5.image(img, 0, 0)
```

</div></div>

</div>

## Description

Get the Sketch drawing surface as a PIL Image object. The returned PIL Image object can include the entirety of the Sketch drawing surface or a rectangular subsection. Use the `x`, `y`, `h`, and `w` parameters to specify the bounds of a rectangular subsection.

## Signatures

```python
to_pil() -> PIL_Image

to_pil(
    x: int,  # x-coordinate of the source's upper left corner
    y: int,  # y-coordinate of the source's upper left corner
    w: int,  # source width
    h: int,  # source height
    /,
) -> PIL_Image
```

Updated on August 07, 2023 14:29:21pm UTC
