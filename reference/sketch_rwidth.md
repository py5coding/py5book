# rwidth

The width of the scale invariant display window.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
  py5.window_resizable(True)
  py5.window_ratio(1280, 720)

  py5.cursor(py5.CROSS)
  py5.stroke_weight(10)


def draw():
  py5.background(255, 0, 0)
  py5.fill(255)
  py5.rect(0, 0, py5.rwidth, py5.rheight)

  py5.fill(0)
  py5.text_align(py5.CENTER, py5.CENTER)
  x, y = py5.rwidth / 2, py5.rheight / 2
  py5.text_size(200)
  py5.text(f'{py5.rmouse_x}, {py5.rmouse_y}', x, y - 100)
  py5.text_size(100)
  py5.text(f'top={int(py5.ratio_top)} left={int(py5.ratio_left)}', x, y + 100)
  py5.text(f'scale={round(py5.ratio_scale, 3)}', x, y + 200)
```

</div></div>

</div>

## Description

The width of the scale invariant display window. This will be the value of the `wide` parameter used in the call to [](sketch_window_ratio) that activates scale invariant drawing. This field should only be used in a scale invariant Sketch. See [](sketch_window_ratio) for more information about how to activate this and why it is useful.

Underlying Processing field: rwidth

Updated on March 06, 2023 02:49:26am UTC
