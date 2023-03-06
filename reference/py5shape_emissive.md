# Py5Shape.emissive()

Sets the emissive color of a `Py5Shape` object's material.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for emissive()](/images/reference/Py5Shape_emissive_0.png)

</div><div class="example-cell-code">

```python
def create_strip(use_emissive):
    s = py5.create_shape()
    s.begin_shape(py5.TRIANGLE_STRIP)
    if use_emissive:
        s.emissive(0, 50, 100)
    s.vertex(10, 40, -25)
    s.vertex(20, 0, -10)
    s.vertex(30, 40, 0)
    s.vertex(40, 0, 5)
    s.vertex(50, 40, 0)
    s.vertex(60, 0, -10)
    s.vertex(70, 40, -25)
    s.end_shape()
    return s


def setup():
    py5.size(100, 100, py5.P3D)
    py5.background(0)
    py5.directional_light(200, 200, 200, .5, 0, -1)
    py5.shape(create_strip(False), 0, 5)
    py5.shape(create_strip(True), 0, 50)
```

</div></div>

</div>

## Description

Sets the emissive color of a `Py5Shape` object's material. Use in combination with [](py5shape_ambient), [](py5shape_specular), and [](py5shape_shininess) to set the material properties of a `Py5Shape` object.

This method can only be used within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair. The emissive color setting will be applied to vertices added after the call to this method.

Underlying Processing method: PShape.emissive

## Signatures

```python
emissive(
    gray: float,  # value between black and white, by default 0 to 255
    /,
) -> None

emissive(
    rgb: int,  # color to set
    /,
) -> None

emissive(
    x: float,  # red or hue value (depending on current color mode)
    y: float,  # green or saturation value (depending on current color mode)
    z: float,  # blue or brightness value (depending on current color mode)
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
