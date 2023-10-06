# g

The [](py5graphics) object used by the Sketch.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.g.rect(10, 10, 50, 50)
    py5.println(type(py5.g))
```

</div></div>

</div>

## Description

The [](py5graphics) object used by the Sketch. Internally, all of Processing's drawing functionality comes from interaction with PGraphics objects, and this will provide direct access to the PGraphics object used by the Sketch.

Use of `g` was deprecated in version 0.9.1 and was removed in version 0.9.2. Please use [](sketch_get_graphics) instead.

Underlying Processing field: g

Updated on October 06, 2023 20:06:55pm UTC
