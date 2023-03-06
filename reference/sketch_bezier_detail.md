# bezier_detail()

Sets the resolution at which Beziers display.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
# move the mouse left and right to see the detail change

def setup():
    py5.size(100, 100, py5.P3D)
    py5.no_fill()


def draw():
    py5.background(204)
    d = int(py5.remap(py5.mouse_x, 0, 100, 1, 20))
    py5.bezier_detail(d)
    py5.bezier(85, 20, 10, 10, 90, 90, 15, 80)
```

</div></div>

</div>

## Description

Sets the resolution at which Beziers display. The default value is 20. This function is only useful when using the `P3D` renderer; the default `P2D` renderer does not use this information.

Underlying Processing method: [bezierDetail](https://processing.org/reference/bezierDetail_.html)

## Signatures

```python
bezier_detail(
    detail: int,  # resolution of the curves
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
