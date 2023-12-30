# Py5Shape.set_fills()

Set the fill color for each of the individual vertices of a `Py5Shape`.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for set_fills()](/images/reference/Py5Shape_set_fills_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P2D)

    py5.no_stroke()

    rect = py5.create_shape()
    with rect.begin_closed_shape():
        rect.vertex(10, 10)
        rect.vertex(10, 90)
        rect.vertex(90, 90)
        rect.vertex(90, 10)

    fills = [py5.color(x * 85, 0, 0) for x in range(4)]
    rect.set_fills(fills)

    py5.shape(rect)
```

</div></div>

</div>

## Description

Set the fill color for each of the individual vertices of a `Py5Shape`. The length of the passed `fills` array must equal the number of vertices in the shape. This method exists to provide an alternative to repeatedly calling [](py5shape_set_fill) in a loop.

This method can only be used after the shape has been created. Do not use this method between the calls to [](py5shape_begin_shape) and [](py5shape_end_shape).

## Signatures

```python
set_fills(
    fills: npt.NDArray[np.int32],  # array of fill colors
    /,
) -> None
```

Updated on October 09, 2023 23:33:46pm UTC
