# stroke_join()

Sets the style of the joints which connect line segments.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for stroke_join()](/images/reference/Sketch_stroke_join_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.no_fill()
    py5.stroke_weight(10.0)
    py5.stroke_join(py5.MITER)
    py5.begin_shape()
    py5.vertex(35, 20)
    py5.vertex(65, 50)
    py5.vertex(35, 80)
    py5.end_shape()
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for stroke_join()](/images/reference/Sketch_stroke_join_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.no_fill()
    py5.stroke_weight(10.0)
    py5.stroke_join(py5.BEVEL)
    py5.begin_shape()
    py5.vertex(35, 20)
    py5.vertex(65, 50)
    py5.vertex(35, 80)
    py5.end_shape()
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for stroke_join()](/images/reference/Sketch_stroke_join_2.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.no_fill()
    py5.stroke_weight(10.0)
    py5.stroke_join(py5.ROUND)
    py5.begin_shape()
    py5.vertex(35, 20)
    py5.vertex(65, 50)
    py5.vertex(35, 80)
    py5.end_shape()
```

</div></div>

</div>

## Description

Sets the style of the joints which connect line segments. These joints are either mitered, beveled, or rounded and specified with the corresponding parameters `MITER`, `BEVEL`, and `ROUND`. The default joint is `MITER`.

Underlying Processing method: [strokeJoin](https://processing.org/reference/strokeJoin_.html)

## Signatures

```python
stroke_join(
    join: int,  # either MITER, BEVEL, ROUND
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
