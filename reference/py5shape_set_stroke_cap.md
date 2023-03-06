# Py5Shape.set_stroke_cap()

Sets the style for rendering line endings in a `Py5Shape` object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for set_stroke_cap()](/images/reference/Py5Shape_set_stroke_cap_0.png)

</div><div class="example-cell-code">

```python
def setup():
    s = py5.create_shape()
    s.begin_shape()
    s.stroke_weight(12.0)
    s.vertex(20, 0)
    s.vertex(80, 0)
    s.end_shape()

    py5.shape(s, 0, 30)
    s.set_stroke_cap(py5.SQUARE)
    py5.shape(s, 0, 50)
    s.set_stroke_cap(py5.PROJECT)
    py5.shape(s, 0, 70)
```

</div></div>

</div>

## Description

Sets the style for rendering line endings in a `Py5Shape` object. These ends are either squared, extended, or rounded, each of which specified with the corresponding parameters: `SQUARE`, `PROJECT`, and `ROUND`. The default cap is `ROUND`.

This method differs from [](py5shape_stroke_cap) in that it is only to be used outside the [](py5shape_begin_shape) and [](py5shape_end_shape) methods.

Underlying Processing method: PShape.setStrokeCap

## Signatures

```python
set_stroke_cap(
    cap: int,  # either SQUARE, PROJECT, or ROUND
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
