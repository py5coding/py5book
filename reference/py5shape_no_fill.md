# Py5Shape.no_fill()

Disables the `Py5Shape` object's filling geometry.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for no_fill()](/images/reference/Py5Shape_no_fill_0.png)

</div><div class="example-cell-code">

```python
def setup():
    s = py5.create_shape()
    s.begin_shape()
    s.no_fill()
    s.vertex(20, 80)
    s.vertex(50, 20)
    s.vertex(80, 80)
    s.end_shape(py5.CLOSE)

    py5.shape(s)
```

</div></div>

</div>

## Description

Disables the `Py5Shape` object's filling geometry. If both [](py5shape_no_stroke) and `no_fill()` are called, nothing will be drawn to the screen.

This method can only be used within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

Underlying Processing method: PShape.noFill

## Signatures

```python
no_fill() -> None
```

Updated on March 06, 2023 02:49:26am UTC
