# window_x

The x-coordinate of the current window location.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def draw():
    py5.rect(py5.random(py5.width), py5.random(py5.height), 10, 10)
    py5.println(f'Sketch window location is ({py5.window_x}, {py5.window_y})')
```

</div></div>

</div>

## Description

The x-coordinate of the current window location. The location is measured from the Sketch window's upper left corner.

Underlying Processing field: windowX

Updated on March 06, 2023 02:49:26am UTC
