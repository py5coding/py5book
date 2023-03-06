# Py5Shape.get_child()

Extracts a child `Py5Shape` object from a parent `Py5Shape` object that is defined as a `GROUP`.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_child()](/images/reference/Py5Shape_get_child_0.png)

</div><div class="example-cell-code">

```python
def setup():
    states = py5.load_shape("us_map.svg")
    ohio = states.get_child("OH")
    ohio.disable_style()

    py5.background(192)
    py5.scale(0.1)
    py5.translate(25, 225)
    py5.shape(states, 0, 0)
    py5.fill(255, 0, 0)
    py5.shape(ohio, 0, 0)
```

</div></div>

</div>

## Description

Extracts a child `Py5Shape` object from a parent `Py5Shape` object that is defined as a `GROUP`. Specify the name of the shape with the `target` parameter, or use the index with the `index` parameter. The shape is returned as a `Py5Shape` object, or `None` is returned if there is an error.

Underlying Processing method: [PShape.getChild](https://processing.org/reference/PShape_getChild_.html)

## Signatures

```python
get_child(
    index: int,  # the layer position of the shape to get
    /,
) -> Py5Shape

get_child(
    target: str,  # the name of the shape to get
    /,
) -> Py5Shape
```

Updated on March 06, 2023 02:49:26am UTC
