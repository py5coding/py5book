# Py5Graphics.to_pil()

Get the Py5Graphics drawing surface as a PIL Image object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for to_pil()](/images/reference/Py5Graphics_to_pil_0.png)

</div><div class="example-cell-code">

```python
def setup():
    g = py5.create_graphics(80, 80)
    with g.begin_draw():
        g.stroke_weight(5)
        for x in range(0, g.width, 10):
            g.line(x, 0, x, g.height)

    img = g.to_pil()
    img = img.rotate(45)
    py5.image(img, 10, 10)
```

</div></div>

</div>

## Description

Get the Py5Graphics drawing surface as a PIL Image object. The returned PIL Image object can include the entirety of the Py5Graphics drawing surface or a rectangular subsection. Use the `x`, `y`, `h`, and `w` parameters to specify the bounds of a rectangular subsection.

This method is the same as [](sketch_to_pil) but linked to a `Py5Graphics` object.

## Signatures

```python
to_pil() -> PIL_Image

to_pil(
    x: int,  # x-coordinate of the source's upper left corner
    y: int,  # y-coordinate of the source's upper left corner
    w: int,  # source width
    h: int,  # source height
) -> PIL_Image
```

Updated on August 07, 2023 14:29:21pm UTC
