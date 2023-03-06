# Py5Shape.stroke_weight()

Sets the width of the stroke used for lines and points in a `Py5Shape` object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for stroke_weight()](/images/reference/Py5Shape_stroke_weight_0.png)

</div><div class="example-cell-code">

```python
def make_line(weight):
    s = py5.create_shape()
    s.begin_shape()
    s.stroke_weight(weight)
    s.vertex(20, 0)
    s.vertex(80, 0)
    s.end_shape()
    return s


def setup():
    py5.shape(make_line(1), 0, 20) # default
    py5.shape(make_line(4), 0, 40)
    py5.shape(make_line(10), 0, 70)
```

</div></div>

</div>

## Description

Sets the width of the stroke used for lines and points in a `Py5Shape` object. All widths are set in units of pixels.

This method can only be used within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

Underlying Processing method: PShape.strokeWeight

## Signatures

```python
stroke_weight(
    weight: float,  # the weight (in pixels) of the stroke
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
