# shape()

Draws shapes to the display window.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for shape()](/images/reference/Sketch_shape_0.png)

</div><div class="example-cell-code">

```python
def setup():
    global s
    s = py5.load_shape("bot.svg")


def draw():
    py5.shape(s, 10, 10, 80, 80)
```

</div></div>

</div>

## Description

Draws shapes to the display window. Shapes must be in the Sketch's "data" directory to load correctly. Py5 currently works with SVG, OBJ, and custom-created shapes. The `shape` parameter specifies the shape to display and the coordinate parameters define the location of the shape from its upper-left corner. The shape is displayed at its original size unless the `c` and `d` parameters specify a different size. The [](sketch_shape_mode) function can be used to change the way these parameters are interpreted.

Underlying Processing method: [shape](https://processing.org/reference/shape_.html)

## Signatures

```python
shape(
    shape: Py5Shape,  # the shape to display
    /,
) -> None

shape(
    shape: Py5Shape,  # the shape to display
    a: float,  # x-coordinate of the shape
    b: float,  # y-coordinate of the shape
    c: float,  # width to display the shape
    d: float,  # height to display the shape
    /,
) -> None

shape(
    shape: Py5Shape,  # the shape to display
    x: float,  # x-coordinate of the shape
    y: float,  # y-coordinate of the shape
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
