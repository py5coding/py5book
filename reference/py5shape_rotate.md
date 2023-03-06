# Py5Shape.rotate()

Rotates the shape the amount specified by the `angle` parameter.

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
    py5.scale(0.2)
    py5.shape(s, py5.width//2, py5.height//2)


def mouse_pressed():
    # rotate the shape each time the mouse is pressed
    s.rotate(0.1)
```

</div></div>

</div>

## Description

Rotates the shape the amount specified by the `angle` parameter. Angles should be specified in radians (values from 0 to `TWO_PI`) or converted from degrees to radians with the [](sketch_radians) method.

Shapes are always rotated around the upper-left corner of their bounding box. Positive numbers rotate objects in a clockwise direction. Transformations apply to everything that happens after and subsequent calls to the method accumulates the effect. For example, calling `rotate(HALF_PI)` and then `rotate(HALF_PI)` is the same as `rotate(PI)`. This transformation is applied directly to the shape, it's not refreshed each time `draw()` is run.

Underlying Processing method: [PShape.rotate](https://processing.org/reference/PShape_rotate_.html)

## Signatures

```python
rotate(
    angle: float,  # angle of rotation specified in radians
    /,
) -> None

rotate(
    angle: float,  # angle of rotation specified in radians
    v0: float,  # x-coordinate of vector to rotate around
    v1: float,  # y-coordinate of vector to rotate around
    v2: float,  # z-coordinate of vector to rotate around
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
