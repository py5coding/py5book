# Py5Shape.stroke_join()

Sets the style of the joints which connect line segments in a `Py5Shape` object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for stroke_join()](/images/reference/Py5Shape_stroke_join_0.png)

</div><div class="example-cell-code">

```python
def setup():
    s = py5.create_shape()
    s.begin_shape()
    s.no_fill()
    s.stroke_weight(10.0)
    s.stroke_join(py5.MITER)
    s.vertex(35, 20)
    s.vertex(65, 50)
    s.vertex(35, 80)
    s.end_shape()

    py5.shape(s)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for stroke_join()](/images/reference/Py5Shape_stroke_join_1.png)

</div><div class="example-cell-code">

```python
def setup():
    s = py5.create_shape()
    s.begin_shape()
    s.no_fill()
    s.stroke_weight(10.0)
    s.stroke_join(py5.BEVEL)
    s.vertex(35, 20)
    s.vertex(65, 50)
    s.vertex(35, 80)
    s.end_shape()

    py5.shape(s)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for stroke_join()](/images/reference/Py5Shape_stroke_join_2.png)

</div><div class="example-cell-code">

```python
def setup():
    s = py5.create_shape()
    s.begin_shape()
    s.no_fill()
    s.stroke_weight(10.0)
    s.stroke_join(py5.ROUND)
    s.vertex(35, 20)
    s.vertex(65, 50)
    s.vertex(35, 80)
    s.end_shape()

    py5.shape(s)
```

</div></div>

</div>

## Description

Sets the style of the joints which connect line segments in a `Py5Shape` object. These joints are either mitered, beveled, or rounded and specified with the corresponding parameters `MITER`, `BEVEL`, and `ROUND`. The default joint is `MITER`.

This method can only be used within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

Underlying Processing method: PShape.strokeJoin

## Signatures

```python
stroke_join(
    join: int,  # either MITER, BEVEL, ROUND
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
