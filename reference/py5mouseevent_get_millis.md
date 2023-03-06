# Py5MouseEvent.get_millis()

Return the event's timestamp.

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
    py5.println('mouse event time:', e.get_millis())
```

</div></div>

</div>

## Description

Return the event's timestamp. This will be measured in milliseconds.

Underlying Processing method: getMillis

## Signatures

```python
get_millis() -> int
```

Updated on March 06, 2023 02:49:26am UTC
