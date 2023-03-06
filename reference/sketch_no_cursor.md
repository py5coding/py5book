# no_cursor()

Hides the cursor from view.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
# press the mouse to hide the cursor
def draw():
    if py5.is_mouse_pressed:
        py5.no_cursor()
    else:
        py5.cursor(py5.HAND)
```

</div></div>

</div>

## Description

Hides the cursor from view. Will not work when running the program in full screen (Present) mode.

Underlying Processing method: [noCursor](https://processing.org/reference/noCursor_.html)

## Signatures

```python
no_cursor() -> None
```

Updated on March 06, 2023 02:49:26am UTC
