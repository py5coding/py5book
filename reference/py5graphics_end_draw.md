# Py5Graphics.end_draw()

Finalizes the rendering of a `Py5Graphics` object so that it can be shown on screen.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global pg
    py5.size(200, 200, py5.P2D)
    pg = py5.create_graphics(80, 80, py5.P2D)
    pg.begin_draw()
    pg.background(102)
    pg.stroke(255)
    pg.line(20, 20, 80, 80)
    pg.end_draw()


def draw():
    py5.image(pg, 10, 10)
```

</div></div>

</div>

## Description

Finalizes the rendering of a `Py5Graphics` object so that it can be shown on screen.

Underlying Processing method: [PGraphics.endDraw](https://processing.org/reference/PGraphics_endDraw_.html)

## Signatures

```python
end_draw() -> None
```

Updated on March 06, 2023 02:49:26am UTC
