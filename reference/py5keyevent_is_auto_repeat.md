# Py5KeyEvent.is_auto_repeat()

Identifies if the pressed key is auto repeating, as faciliated by the computer's operating system.

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


def key_pressed(e):
    if e.is_auto_repeat():
        py5.println('key press is auto repeating')
    else:
        py5.println('key press is not auto repeating')
```

</div></div>

</div>

## Description

Identifies if the pressed key is auto repeating, as faciliated by the computer's operating system. This method might work differently (or not at all) depending on the renderer used by the Sketch and the operating system the Sketch is run on.

Underlying Processing method: KeyEvent.isAutoRepeat

## Signatures

```python
is_auto_repeat() -> bool
```

Updated on May 02, 2024 03:24:20am UTC
