# Py5Shape.stroke_cap()

Sets the style for rendering line endings in a `Py5Shape` object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for stroke_cap()](/images/reference/Py5Shape_stroke_cap_0.png)

</div><div class="example-cell-code">

```python
def make_line(cap):
    s = py5.create_shape()
    s.begin_shape()
    s.stroke_weight(12.0)
    s.stroke_cap(cap)
    s.vertex(20, 0)
    s.vertex(80, 0)
    s.end_shape()
    return s


def setup():
    py5.shape(make_line(py5.ROUND), 0, 30)
    py5.shape(make_line(py5.SQUARE), 0, 50)
    py5.shape(make_line(py5.PROJECT), 0, 70)
```

</div></div>

</div>

## Description

Sets the style for rendering line endings in a `Py5Shape` object. These ends are either squared, extended, or rounded, each of which specified with the corresponding parameters: `SQUARE`, `PROJECT`, and `ROUND`. The default cap is `ROUND`.

This method can only be used within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

Underlying Processing method: PShape.strokeCap

## Signatures

```python
stroke_cap(
    cap: int,  # either SQUARE, PROJECT, or ROUND
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
