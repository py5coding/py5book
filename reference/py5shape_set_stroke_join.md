# Py5Shape.set_stroke_join()

Sets the style of the joints which connect line segments in a `Py5Shape` object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for set_stroke_join()](/images/reference/Py5Shape_set_stroke_join_0.png)

</div><div class="example-cell-code">

```python
def setup():
    s = py5.create_shape()
    s.begin_shape()
    s.no_fill()
    s.stroke_weight(10.0)
    s.stroke_join(py5.MITER)
    s.vertex(10, 20)
    s.vertex(40, 50)
    s.vertex(10, 80)
    s.end_shape()

    py5.shape(s)
    s.set_stroke_join(py5.BEVEL)
    py5.shape(s, 25, 0)
    s.set_stroke_join(py5.ROUND)
    py5.shape(s, 50, 0)
```

</div></div>

</div>

## Description

Sets the style of the joints which connect line segments in a `Py5Shape` object. These joints are either mitered, beveled, or rounded and specified with the corresponding parameters `MITER`, `BEVEL`, and `ROUND`. The default joint is `MITER`.

This method differs from [](py5shape_stroke_join) in that it is only to be used outside the [](py5shape_begin_shape) and [](py5shape_end_shape) methods.

Underlying Processing method: PShape.setStrokeJoin

## Signatures

```python
set_stroke_join(
    join: int,  # either MITER, BEVEL, ROUND
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
