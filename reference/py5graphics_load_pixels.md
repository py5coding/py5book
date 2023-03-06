# Py5Graphics.load_pixels()

Loads the pixel data of the current Py5Graphics drawing surface into the [](py5graphics_pixels) array.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for load_pixels()](/images/reference/Py5Graphics_load_pixels_0.png)

</div><div class="example-cell-code">

```python
def setup():
    g = py5.create_graphics(60, 60)
    g.begin_draw()
    g.background(255, 0, 0)
    g.rect(10, 10, 40, 40)
    g.load_pixels()
    yellow = "#FF0"
    for i in range(len(g.pixels) // 2):
        g.pixels[i] = yellow
    g.update_pixels()
    g.end_draw()

    py5.background(240)
    py5.image(g, 20, 20)
```

</div></div>

</div>

## Description

Loads the pixel data of the current Py5Graphics drawing surface into the [](py5graphics_pixels) array. This function must always be called before reading from or writing to [](py5graphics_pixels). Subsequent changes to the Py5Graphics drawing surface will not be reflected in [](py5graphics_pixels) until `load_pixels()` is called again.

This method is the same as [](sketch_load_pixels) but linked to a `Py5Graphics` object.

Underlying Processing method: PGraphics.loadPixels

## Signatures

```python
load_pixels() -> None
```

Updated on March 06, 2023 02:49:26am UTC
