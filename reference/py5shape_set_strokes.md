# Py5Shape.set_strokes()

Set the stroke color for each of the individual vertices of a `Py5Shape`.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for set_strokes()](/images/reference/Py5Shape_set_strokes_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.size(100, 100, py5.P2D)

    py5.stroke_weight(15)
    py5.no_fill()

    rect = py5.create_shape()
    with rect.begin_closed_shape():
        rect.vertex(20, 20)
        rect.vertex(20, 80)
        rect.vertex(80, 80)
        rect.vertex(80, 20)

    strokes = [py5.color(x * 85, 0, 0) for x in range(4)]
    rect.set_strokes(strokes)

    py5.shape(rect)
```

</div></div>

</div>

## Description

Set the stroke color for each of the individual vertices of a `Py5Shape`. The length of the passed `strokes` array must equal the number of vertices in the shape. This method exists to provide an alternative to repeatedly calling [](py5shape_set_fill) in a loop.

This method can only be used after the shape has been created. Do not use this method between the calls to [](py5shape_begin_shape) and [](py5shape_end_shape).

## Signatures

```python
set_strokes(
    strokes: npt.NDArray[np.int32],  # array of stroke colors
    /,
) -> None
```

Updated on October 09, 2023 23:33:46pm UTC
