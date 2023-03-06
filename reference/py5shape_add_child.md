# Py5Shape.add_child()

Adds a child `Py5Shape` object to a parent `Py5Shape` object that is defined as a `GROUP`.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(200, 200)
    # make a group Py5Shape
    house = py5.create_shape(py5.GROUP)

    # make three shapes
    path = py5.create_shape()
    path.begin_shape()
    path.vertex(-20, -20)
    path.vertex(0, -40)
    path.vertex(20, -20)
    path.end_shape()
    rectangle = py5.create_shape(py5.RECT, -20, -20, 40, 40)
    opening = py5.create_shape(py5.ELLIPSE, 0, 0, 20, 20)

    # add all three as children
    house.add_child(path)
    house.add_child(rectangle)
    house.add_child(opening)

    py5.background(52)
    py5.translate(py5.mouse_x, py5.mouse_y)
    py5.shape(house)
```

</div></div>

</div>

## Description

Adds a child `Py5Shape` object to a parent `Py5Shape` object that is defined as a `GROUP`. In the example, the three shapes `path`, `rectangle`, and `circle` are added to a parent `Py5Shape` variable named `house` that is a `GROUP`.

Underlying Processing method: [PShape.addChild](https://processing.org/reference/PShape_addChild_.html)

## Signatures

```python
add_child(
    who: Py5Shape,  # any variable of type Py5Shape
    /,
) -> None

add_child(
    who: Py5Shape,  # any variable of type Py5Shape
    idx: int,  # the layer position in which to insert the new child
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
