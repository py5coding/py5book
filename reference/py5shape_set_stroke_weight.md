# Py5Shape.set_stroke_weight()

Sets the width of the stroke used for lines and points in a `Py5Shape` object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for set_stroke_weight()](/images/reference/Py5Shape_set_stroke_weight_0.png)

</div><div class="example-cell-code">

```python
def setup():
    s = py5.create_shape()
    s.begin_shape()
    s.stroke_weight(1)
    s.vertex(20, 0)
    s.vertex(80, 0)
    s.end_shape()

    py5.shape(s, 0, 20)
    s.set_stroke_weight(4)
    py5.shape(s, 0, 40)
    s.set_stroke_weight(10)
    py5.shape(s, 0, 70)
```

</div></div>

</div>

## Description

Sets the width of the stroke used for lines and points in a `Py5Shape` object. All widths are set in units of pixels. Attempting to set this for individual vertices may not work, depending on the renderer used and other factors.

This method differs from [](py5shape_stroke_weight) in that it is only to be used outside the [](py5shape_begin_shape) and [](py5shape_end_shape) methods.

Underlying Processing method: PShape.setStrokeWeight

## Signatures

```python
set_stroke_weight(
    index: int,  # vertex index
    weight: float,  # the weight (in pixels) of the stroke
    /,
) -> None

set_stroke_weight(
    weight: float,  # the weight (in pixels) of the stroke
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
