# Py5Graphics.smooth()

Draws all geometry with smooth (anti-aliased) edges.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
x = 0


def setup():
    global pg
    py5.full_screen(py5.P2D)
    pg = py5.create_graphics(py5.width, py5.height, py5.P2D)
    pg.smooth(4)


def draw():
    global x
    pg.begin_draw()
    pg.background(0)
    pg.ellipse(x, py5.height//2, py5.height/4, py5.height/4)
    pg.end_draw()
    py5.image(pg, 0, 0)
    x += 1
```

</div></div>

</div>

## Description

Draws all geometry with smooth (anti-aliased) edges. This behavior is the default, so `smooth()` only needs to be used when a program needs to set the smoothing in a different way. The `level` parameter increases the amount of smoothness. This is the level of over sampling applied to the graphics buffer.

With the `P2D` and `P3D` renderers, `smooth(2)` is the default, this is called "2x anti-aliasing." The code `smooth(4)` is used for 4x anti-aliasing and `smooth(8)` is specified for "8x anti-aliasing." The maximum anti-aliasing level is determined by the hardware of the machine that is running the software, so `smooth(4)` and `smooth(8)` will not work with every computer.

The default renderer uses `smooth(3)` by default. This is bicubic smoothing. The other option for the default renderer is `smooth(2)`, which is bilinear smoothing.

The `smooth()` method can only be run once for a `Py5Graphics` object and it must be called right after the object is created with [](sketch_create_graphics) and before [](py5graphics_begin_draw).

This method is the same as [](sketch_smooth) but linked to a `Py5Graphics` object.

Underlying Processing method: PGraphics.smooth

## Signatures

```python
smooth() -> None

smooth(
    quality: int,  # either 2, 3, 4, or 8 depending on the renderer
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
