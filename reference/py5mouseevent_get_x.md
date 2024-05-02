# Py5MouseEvent.get_x()

Return the x position of the mouse at the time of this mouse event.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(200, 200, py5.P2D)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.square(py5.random(py5.width), py5.random(py5.height), 10)


def mouse_clicked(e):
    py5.println(e.get_x(), e.get_y())
```

</div></div>

</div>

## Description

Return the x position of the mouse at the time of this mouse event. This information can also be obtained with [](sketch_mouse_x).

Underlying Processing method: MouseEvent.getX

## Signatures

```python
get_x() -> int
```

Updated on May 02, 2024 03:24:20am UTC
