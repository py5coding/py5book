# hot_reload_draw()

Perform a hot reload of the Sketch's draw function.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import time


def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)


def draw2():
    py5.circle(py5.mouse_x, py5.mouse_y, 10)


py5.run_sketch()

time.sleep(10)
py5.hot_reload_draw(draw2)
```

</div></div>

</div>

## Description

Perform a hot reload of the Sketch's draw function. This method allows you to replace a running Sketch's draw function with a different one.

## Signatures

```python
hot_reload_draw(
    draw: Callable,  # function to replace existing draw function
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
