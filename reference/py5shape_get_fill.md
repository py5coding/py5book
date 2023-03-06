# Py5Shape.get_fill()

Gets the fill color used for a `Py5Shape` object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_fill()](/images/reference/Py5Shape_get_fill_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.no_stroke()
    py5.fill(200, 50, 50)
    s = py5.create_shape(py5.RECT, 20, 20, 60, 60)
    py5.shape(s)

    fill = s.get_fill(0)
    py5.println(py5.red(fill), py5.green(fill), py5.blue(fill)) # 200, 50, 50
```

</div></div>

</div>

## Description

Gets the fill color used for a `Py5Shape` object. This method can get the fill assigned to each vertex, but most likely the value will be the same for all vertices.

This method can only be used for a complete `Py5Shape` object, and never within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair.

Underlying Processing method: PShape.getFill

## Signatures

```python
get_fill(
    index: int,  # vertex index
    /,
) -> int
```

Updated on March 06, 2023 02:49:26am UTC
