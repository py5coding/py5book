# Py5Shape.get_stroke_weight()

Gets the width of the stroke used for lines and points in a `Py5Shape` object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_stroke_weight()](/images/reference/Py5Shape_get_stroke_weight_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.stroke_weight(4)
    s = py5.create_shape(py5.RECT, 20, 20, 60, 60)
    py5.shape(s)

    py5.println(s.get_stroke_weight(0)) # 4.0
```

</div></div>

</div>

## Description

Gets the width of the stroke used for lines and points in a `Py5Shape` object. All widths are set in units of pixels. This method can get the stroke weight assigned to each vertex, but most likely the value will be the same for all vertices.

This method can only be used for a complete `Py5Shape` object, and never within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

Underlying Processing method: PShape.getStrokeWeight

## Signatures

```python
get_stroke_weight(
    index: int,  # vertex index
    /,
) -> float
```

Updated on March 06, 2023 02:49:26am UTC
