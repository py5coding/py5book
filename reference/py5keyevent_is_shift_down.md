# Py5KeyEvent.is_shift_down()

Return boolean value reflecting if the Shift key is down.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(200, 200)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.square(py5.random(py5.width), py5.random(py5.height), 10)


def key_pressed(e):
    if e.is_shift_down():
        py5.println('the shift key is down')
    else:
        py5.println('the shift key is not down')
```

</div></div>

</div>

## Description

Return boolean value reflecting if the Shift key is down. The Shift key is a modifier key and can be pressed at the same time as other keys.

Underlying Processing method: KeyEvent.isShiftDown

## Signatures

```python
is_shift_down() -> bool
```

Updated on May 02, 2024 03:24:20am UTC
