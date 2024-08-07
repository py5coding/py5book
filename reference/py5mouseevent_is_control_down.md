# Py5MouseEvent.is_control_down()

Return boolean value reflecting if the Control key is down.

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


def mouse_clicked(e):
    if e.is_control_down():
        py5.println('the control key is down')
    else:
        py5.println('the control key is not down')
```

</div></div>

</div>

## Description

Return boolean value reflecting if the Control key is down. The Control key is a modifier key and can be pressed at the same time as other keys.

Underlying Processing method: MouseEvent.isControlDown

## Signatures

```python
is_control_down() -> bool
```

Updated on May 02, 2024 03:24:20am UTC
