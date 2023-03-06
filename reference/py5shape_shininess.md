# Py5Shape.shininess()

Sets the amount of gloss in the surface of a `Py5Shape` object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for shininess()](/images/reference/Py5Shape_shininess_0.png)

</div><div class="example-cell-code">

```python
def create_strip(use_shininess):
    s = py5.create_shape()
    s.begin_shape(py5.TRIANGLE_STRIP)
    if use_shininess:
        s.shininess(5)
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
    py5.ambient_light(102, 102, 102)
    py5.light_specular(204, 204, 204)
    py5.directional_light(150, 150, 150, .5, 0, -1)
    py5.shape(create_strip(False), 0, 5)
    py5.shape(create_strip(True), 0, 50)
```

</div></div>

</div>

## Description

Sets the amount of gloss in the surface of a `Py5Shape` object. Use in combination with [](py5shape_ambient), [](py5shape_specular), and [](py5shape_emissive) to set the material properties of a `Py5Shape` object.

This method can only be used within a [](py5shape_begin_shape) and [](py5shape_end_shape) pair. The shininess color setting will be applied to vertices added after the call to this method.

Underlying Processing method: PShape.shininess

## Signatures

```python
shininess(
    shine: float,  # degree of shininess
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
