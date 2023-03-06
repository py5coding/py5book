# Py5Shape.scale()

Increases or decreases the size of a shape by expanding and contracting vertices.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global s
    s = py5.load_shape("bot.svg")


def draw():
    py5.background(204)
    py5.shape(s)


def mouse_pressed():
    # shrink the shape 90% each time the mouse is pressed
    s.scale(0.9)
```

</div></div>

</div>

## Description

Increases or decreases the size of a shape by expanding and contracting vertices. Shapes always scale from the relative origin of their bounding box. Scale values are specified as decimal percentages. For example, the method call `scale(2.0)` increases the dimension of a shape by 200%. Subsequent calls to the method multiply the effect. For example, calling `scale(2.0)` and then `scale(1.5)` is the same as `scale(3.0)`. This transformation is applied directly to the shape; it's not refreshed each time `draw()` is run. 

Using this method with the `z` parameter requires using the `P3D` parameter in combination with size.

Underlying Processing method: [PShape.scale](https://processing.org/reference/PShape_scale_.html)

## Signatures

```python
scale(
    s: float,  # percentate to scale the object
    /,
) -> None

scale(
    x: float,  # percentage to scale the object in the x-axis
    y: float,  # percentage to scale the object in the y-axis
    /,
) -> None

scale(
    x: float,  # percentage to scale the object in the x-axis
    y: float,  # percentage to scale the object in the y-axis
    z: float,  # percentage to scale the object in the z-axis
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
