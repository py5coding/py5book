# Py5MouseEvent.get_count()

Get the number of mouse clicks.

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
    py5.println('mouse click count:', e.get_count())


def mouse_wheel(e):
    direction = "down" if e.get_count() == 1 else "up"
    py5.println(f"mouse wheel rotating {direction}")
```

</div></div>

</div>

## Description

Get the number of mouse clicks. This will be 1 for a single mouse click and 2 for a double click. The value can be much higher if the user clicks fast enough.

This method also responds to the mouse wheel. It will be 1 when the mouse wheel is rotating down and -1 when the mouse wheel is rotating up.

Underlying Processing method: MouseEvent.getCount

## Signatures

```python
get_count() -> int
```

Updated on May 02, 2024 03:24:20am UTC
