# Py5Shape.no_stroke()

Disables the `Py5Shape` object's stroke (outline).

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for no_stroke()](/images/reference/Py5Shape_no_stroke_0.png)

</div><div class="example-cell-code">

```python
def setup():
    s = py5.create_shape()
    s.begin_shape()
    s.no_stroke()
    s.vertex(20, 80)
    s.vertex(50, 20)
    s.vertex(80, 80)
    s.end_shape(py5.CLOSE)

    py5.shape(s)
```

</div></div>

</div>

## Description

Disables the `Py5Shape` object's stroke (outline). If both `no_stroke()` and [](py5shape_no_fill) are called, nothing will be drawn to the screen.

This method can only be used within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

Underlying Processing method: PShape.noStroke

## Signatures

```python
no_stroke() -> None
```

Updated on March 06, 2023 02:49:26am UTC
